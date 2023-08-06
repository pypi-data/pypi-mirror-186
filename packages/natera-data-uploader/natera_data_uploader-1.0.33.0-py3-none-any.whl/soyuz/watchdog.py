import logging
import os
import signal
import subprocess
import threading
import time
from subprocess import Popen


class SequenceFolderWatchDog(object):
    def __init__(self, seq_folder_path, check_interval, timeout, target_pid=None):
        # type: (str, float, float, int) -> None

        self.__seq_folder_path = os.path.abspath(os.path.expanduser(seq_folder_path))
        self.__target_pid = target_pid if target_pid else os.getpid()
        self.__check_interval = check_interval
        self.__timeout = timeout

        self.__watch_dog_thread = threading.Thread(target=self.__watch_dog, args=(), daemon=True)

    def start(self):
        self.__watch_dog_thread.start()

    def __watch_dog(self):
        while True:
            if self.__call_with_timeout(["ls", self.__seq_folder_path], self.__timeout):
                time.sleep(self.__check_interval)
            else:
                logging.warning("The {} sequence folder is not available, will kill a main process...".format(
                    self.__seq_folder_path))
                os.kill(self.__target_pid, signal.SIGKILL)

    @staticmethod
    def __call_with_timeout(cmd, timeout):
        # type: (list, float) -> bool

        start = time.time()
        p = Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        while time.time() - start < timeout:
            if p.poll() is not None:
                return True

            time.sleep(0.5)

        p.kill()

        return False
