import threading
import time

from soyuz.api.dx import DxApi
from soyuz.dx.variables import Type, Property


class Heartbeat(object):
    REMOTE_FOLDER_PATH = '/soyuz_agents'

    def __init__(self, api, soyuz_id, update_interval):
        # type: (DxApi, str, float) -> None

        self.__api = api
        self.__soyuz_id = soyuz_id
        self.__update_interval = update_interval

        self.__heartbeat_thread = threading.Thread(target=self.__heartbeat, args=(), daemon=True)

    def start(self):
        self.__heartbeat_thread.start()

    def __heartbeat(self):
        while True:
            record = self.__find_or_create_heartbeat_record()
            record.set_properties({Property.HEART_BEAT: str(int(time.time()))})
            time.sleep(self.__update_interval)

    def __find_or_create_heartbeat_record(self):
        records = self.__api.find_data_objects(classname="record",
                                               folder=self.REMOTE_FOLDER_PATH,
                                               typename=Type.HEART_BEAT,
                                               name=self.__soyuz_id,
                                               properties={Property.SOYUZ_ID: self.__soyuz_id},
                                               return_handler=True)
        if len(records) != 0:
            return records[0]

        return self.__api.create_record(types=[Type.HEART_BEAT],
                                        folder=self.REMOTE_FOLDER_PATH,
                                        name=self.__soyuz_id,
                                        properties={Property.SOYUZ_ID: self.__soyuz_id},
                                        close=True,
                                        parents=True)
