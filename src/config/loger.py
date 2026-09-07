from enum import Enum


class LogsType(Enum):
    GAME_LOGS = "GAME LOGS"
    LEVEL_LOGS = "LEVEL LOGS"
    CONFIG_LOGS = "CONFIG LOGS"


class Loger:
    def __init__(self , log_type:LogsType):
        self.log_type:LogsType = log_type

    def log(self ,message):
        print(f"{self.log_type.value}: {message}")
