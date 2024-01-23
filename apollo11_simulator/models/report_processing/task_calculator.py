import pandas as pd


class TaskCalculator:
    def __init__(self, events) -> None:
        self.__events = events

    def event_analysis(self) -> pd.DataFrame:
        return self.__events.groupby(['mission', 'device_status'])['device_type'].count().to_frame()

    def disconnection_management(self) -> pd.DataFrame:
        unkn_devices = self.__events[self.__events.device_status == 'UNKNOWN']
        return unkn_devices.groupby(['mission', 'device_type'])['device_status'].count()

    def mission_consolidation(self) -> pd.DataFrame:
        return sum(self.__events.device_status == 'KILLED')

    def percentage_calculation(self) -> pd.DataFrame:
        group_mission_device = self.__events.groupby(['mission', 'device_type'])['device_type'].count().rename('count')
        # Porcentaje de cada dispositivo en una mision
        result_1 = (group_mission_device / group_mission_device.groupby(level=0).sum()) * 100
        result_1.map(lambda x: f'{x:.2f} %')
        # Porcentaje de estado de dispositivos por mision
        group_mission_device_status = self.__events.groupby(['mission', 'device_status'])['device_status'].count().rename(
            'count')
        (group_mission_device_status / group_mission_device_status.groupby(level=0).sum()) * 100
        group_mission_device_all = self.__events.groupby(['mission', 'device_type', 'device_status'])[
            'device_status'].count().rename('count')
        result_3 = (group_mission_device_all / group_mission_device_all.groupby(level=0).sum()) * 100
        return result_3.map(lambda x: f'{x:.2f} %')
