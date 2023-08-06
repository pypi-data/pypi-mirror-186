import os
import importlib
import threading
import subprocess
from datetime import datetime
from urllib.parse import urlparse
import logging
from colorlog import ColoredFormatter
import requests
import json

LOG_LEVEL = logging.DEBUG
datefmt = '%Y-%m-%d %H:%M:%S'
LOGFORMAT = "%(log_color)s[%(asctime)s][%(levelname)-8s]%(reset)s %(log_color)s%(message)s%(reset)s"
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT, datefmt)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger('Magic Endpoint')
log.setLevel(LOG_LEVEL)
log.addHandler(stream)

RUN_PATH = os.getenv('RUN_PATH', '/tmp/innocuous/endpoint/app')
IMAGE_TMPE_PATH = os.getenv('IMAGE_TMPE_PATH', os.path.join(RUN_PATH, 'images'))
SERVER_URL = os.getenv('SERVER_URL', 'http://3.142.10.136:8000')

if not os.path.exists(IMAGE_TMPE_PATH):
    subprocess.run(f'mkdir -p {IMAGE_TMPE_PATH}', shell=True)

def __download(url, path):
    cmd = f'wget -nv {url} -P {path} 2>&1 |cut -d\\" -f2'
    process = subprocess.check_output(cmd, shell=True)
    return process.decode('utf-8').replace('\n', '').replace('\r', '')

def __clean():
    subprocess.run(f'rm -rf {IMAGE_TMPE_PATH}/*', shell=True)

def download(urls, clean=True):
    if clean:
        __clean()
    file_list = []
    for url in urls:
        file_fullname = __download(url, IMAGE_TMPE_PATH)
        file_list.append(file_fullname)
    return file_list

def save(files, clean=True):
    if clean:
        __clean()
    file_list = []
    for file in files:
        file_location = os.path.join(IMAGE_TMPE_PATH, file.filename)
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())	
            file_list.append(file_location)
    return file_list

class EventHandler:
    def __init__(self):
        self.listeners = []
    
    def __iadd__(self, listener):
        self.listeners.append(listener)
        return self
    
    def trigger(self, *args, **kwargs):
        for listener in self.listeners:
            listener(*args, **kwargs)

class ModelLoader():
    __instance_lock = threading.Lock()

    def __init__(self):
        self._path = ''
        self._new_checkpoint_path_s3 = ''
        self._checkpoint_name = ''
        self._checkpoint_id = None
        self._model = {}
        self._config = {}
        self.UpdateCheckpointHandler = EventHandler()
        
    def __new__(cls, *args, **kwargs):
        if not hasattr(ModelLoader, "_instance"):
            with ModelLoader.__instance_lock:
                if not hasattr(ModelLoader, "_instance"):
                    ModelLoader._instance = object.__new__(cls)
        return ModelLoader._instance

    def _setDownloader(self, downloader):
        self.downloader = downloader

    @property
    def checkpoint_path(self):
        log.info('Getting checkpoint path . . . ')
        return self._path

    @checkpoint_path.setter
    def checkpoint_path(self, value):
        if os.path.isfile(value):
            self._path = value
            log.info('New modelLoaders checkpoint_path set')
        else:
            print('Error, file not exist.')

    @property
    def checkpoint_name(self):
        log.info('Getting checkpoint name . . . ')
        return self._checkpoint_name

    @checkpoint_name.setter
    def checkpoint_name(self, value):
        self._checkpoint_name = value
        log.info('New modelLoaders checkpoint_name set')

    @property
    def checkpoint_id(self):
        log.info('Getting checkpoint id . . . ')
        return self._checkpoint_id

    @checkpoint_id.setter
    def checkpoint_id(self, value):
        self._checkpoint_id = value
        log.info('New modelLoaders checkpoint_id set')

    def save_new_checkpoint_path(self, delete_last=True):
        if self._new_checkpoint_path_s3 != '':
            log.info('Downloading from {}'.format(self._new_checkpoint_path_s3))
            path = self.downloader(self._new_checkpoint_path_s3)
            self._new_checkpoint_path_s3 = ''
            if delete_last:
                if self.checkpoint_path != '':
                    os.remove(self.checkpoint_path)
            self.checkpoint_path = path
            log.info('New checkpoint path set to {}'.format(self.checkpoint_path))
            self.checkpoint_name = os.path.basename(self.checkpoint_path)
            log.info('getting checkpoint info . . .')
            log.info('server url: {}'.format(f'{SERVER_URL}/api/experiment/checkpoint/{self.checkpoint_name}'))
            r = requests.get(f'{SERVER_URL}/api/experiment/checkpoint/{self.checkpoint_name}')
            data = json.loads(r.text)
            log.info('checkpoint data: {}'.format(data))
            self.checkpoint_id = data['id']
            return path
        else:
            raise Exception("Class attribute _new_checkpoint_path_s3 not set")

    def update_model(self, model):
        log.info('about to update model with checkpoint handler and new model')
        self.UpdateCheckpointHandler.trigger(self.checkpoint_id)
        self._model = model

    def get_model(self):
        return self._model

    def update_config(self, config):
        self._config = config

    def get_config(self):
        return self._config

class PipelineHepler():
    __instance_lock = threading.Lock()

    def __init__(self):
        self._metric = []
        self._index = -1

    def __new__(cls, *args, **kwargs):
        if not hasattr(PipelineHepler, "_instance"):
            with PipelineHepler.__instance_lock:
                if not hasattr(PipelineHepler, "_instance"):
                    PipelineHepler._instance = object.__new__(cls)
        return PipelineHepler._instance

   
    def get_last_metric(self):
        return self._metric[self._index]

    
    def get_metric(self, index=None):
        if index == None:
            return self._metric
        elif index >= 0:
            return self._metric[index]
    
    def update_last_metric(self, metric):
        self._metric.append(metric)
        self._index += 1

class FileHelper():
    __instance_lock = threading.Lock()

    def __init__(self):
        pass
        
    def __new__(cls, *args, **kwargs):
        if not hasattr(FileHelper, "_instance"):
            with FileHelper.__instance_lock:
                if not hasattr(FileHelper, "_instance"):
                    FileHelper._instance = object.__new__(cls)
        return FileHelper._instance

    def _setDownloader(self, downloader):
        self.downloader = downloader

    def _setUploader(self, uploader):
        self.uploader = uploader

    def get(self, source, local_path=None):
        """ Get file from s3
        source: path of s3
        """
        return self.downloader(source)

    def save(self, source, destination):
        """ Save file to s3
        source: source file path
        destination: s3 save path
        """
        self.uploader(source, destination)

    def import_package(self, path):
        """ Import package by path
        path: package path
        """
        path = self.downloader(path)
        spec = importlib.util.spec_from_file_location('user_import_model', path)
        md = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(md)
        return md
