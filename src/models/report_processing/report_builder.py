import os
from pathlib import Path
from src.models.report_processing.task_calculator import TaskCalculator

class ReportBuilder:
    __task_calculator: TaskCalculator

    def __init__(self, events) -> None:
        self.__events: dict

    @classmethod
    def from_path(cls, origin_path: str) -> str:
        list_files = os.listdir(origin_path)
        content_merge = ''
        for file in list_files:
            with open(origin_path + '/' + file, "r") as content_file:
                for line in content_file:
                    if line != '':
                        content_merge += line.strip() + "\n"
        return content_merge

    def move_files(self, target_path: Path) -> None:
        pass

    def show_report():
        pass