import queue
import threading
import time
from .Config import file_queue_supervisor_wait_time_secs


class FileQueueSupervisor:
    def clear_object(self):
        while True:
            file_object = self.files_queue.get(block=True)

            while not file_object.is_removed:
                time.sleep(file_queue_supervisor_wait_time_secs)
            self.files_queue.task_done()

    def __init__(self):
        self.files_queue = queue.Queue()
        self.thread = threading.Thread(target=self.clear_object)
        self.thread.setDaemon(True)
        self.thread.start()
