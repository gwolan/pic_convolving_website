import threading
import time
from .Config import file_life_time_secs
from django.core.files.storage import FileSystemStorage


class FileToRemove:
    def remove_image(self):
        time.sleep(file_life_time_secs)
        self.file_storage.delete(self.path)
        self.is_removed = True

    def __init__(self, path):
        self.path = path
        self.file_storage = FileSystemStorage()
        self.is_removed = False
        self.thread = threading.Thread(target=self.remove_image)
        self.thread.setDaemon(True)
        self.thread.start()
