import queue
import threading
import time
from django.core.files.storage import FileSystemStorage


def remove_images(paths):
    file_storage = FileSystemStorage()

    while True:
        path = paths.get(block=True)
        time.sleep(60)

        if path:
            file_storage.delete(path)
            paths.task_done()


class FileRemover:
    paths = queue.Queue()

    def __init__(self):
        self.thread.setDaemon(True)
        self.thread.start()

    thread = threading.Thread(target=remove_images, args=(paths,))
