from typing import Dict, List, Set, Any
from collections import defaultdict
import json
from .comment_handler import CommentsHandler
from .defaults import DEFAULT_CONFIG
from .loger import Loger, LogsType
from .schema import GameConfig


class Loader:

    ALL_KEY = {
        "highscore_filename",
        "seed",
        "lives",
        "player_speed",
        "points_per_pacgum",
        "points_per_super_pacgum",
        "points_per_ghost",
        "pacgum_count",
        "level_max_time",
        "super_pacgum_duration",
        "ghost_respawn_delay",
        "levels",
        "cheat_mode_enabled",
    }

    def __init__(self, config_file: str) -> None:
        self.comment_handler: CommentsHandler = CommentsHandler()
        self.config_file = config_file
        self.cleaned_content = ""
        self.loger = Loger(LogsType.CONFIG_LOGS)

    def load(self) -> GameConfig:
        self._load_file()
        self._clean_file()
        self.data = self._retrive_config()
        self._validate_fields()
        return self._get_game_config()

    def _load_file(self) -> None:
        with open(self.config_file, "r", encoding='utf-8') as file:
            self.file_content = file.read()

    def _clean_file(self) -> None:
        self.comment_handler.brut_text = self.file_content
        self.cleaned_content = self.comment_handler.handle_comments()

    def _retrive_config(self) -> Dict[str, Any]:
        data = json.loads(self.cleaned_content)
        data = defaultdict(list, data)
        return data

    def _validate_fields(self) -> None:
        self._replace_missing()
        self._validate_values()

    def _replace_missing(self) -> None:
        for key in Loader.ALL_KEY:
            if key not in self.data.keys():
                default_value = DEFAULT_CONFIG.get(key, "")
                self.loger.log(f"missing key {key} replaced by {default_value}")
                self.data[key] = default_value

    def _validate_values(self) -> None:
        for key, value in self.data.items():
            if key not in ("highscore_filename", "cheat_mode_enabled", "levels"):
                try:
                    value = int(value)
                except (ValueError, TypeError):
                    value = DEFAULT_CONFIG.get(key)
                    self.loger.log(f"invalid value for {key} replaced by {DEFAULT_CONFIG.get(key, None)}")

            if key == "cheat_mode_enabled":
                if isinstance(value, bool):
                    pass
                elif isinstance(value, str) and value.lower() in ("true", "false"):
                    value = value.lower() == "true"
                else:
                    value = DEFAULT_CONFIG.get(key, None)
                    self.loger.log(f"invalid boolean value for {key} replaced by {DEFAULT_CONFIG.get(key, None)}")

            if key == "levels":
                validated_levels = []
                for level in value:
                    width = level.get("width", None)
                    height = level.get("height", None)
                    try:
                        width = int(width)
                        height = int(height)
                        validated_levels.append(level)
                    except (ValueError, TypeError):
                        self.loger.log(
                            f"invalid width/height ({width}, {height}) for {key} replaced by default"
                        )
                        validated_levels.append(DEFAULT_CONFIG.get("levels", [])[0])
                value = validated_levels

            self.data[key] = value

    def _get_game_config(self) -> GameConfig:
        return GameConfig(
            highscore_filename=self.data["highscore_filename"],
            seed=self.data["seed"],
            lives=self.data["lives"],
            player_speed=self.data["player_speed"],
            points_per_pacgum=self.data["points_per_pacgum"],
            points_per_super_pacgum=self.data["points_per_super_pacgum"],
            points_per_ghost=self.data["points_per_ghost"],
            pacgum_count=self.data["pacgum_count"],
            level_max_time=self.data["level_max_time"],
            super_pacgum_duration=self.data["super_pacgum_duration"],
            ghost_respawn_delay=self.data["ghost_respawn_delay"],
            levels=self.data["levels"],
            cheat_mode_enabled=self.data["cheat_mode_enabled"],
        )
