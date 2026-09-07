from dataclasses import dataclass
from typing import List


@dataclass
class LevelConfig:
    width: int
    height: int


@dataclass
class GameConfig:
    highscore_filename: str
    seed: int
    lives: int
    player_speed: float
    points_per_pacgum: int
    points_per_super_pacgum: int
    points_per_ghost: int
    pacgum_count: int
    level_max_time: int
    super_pacgum_duration: int
    ghost_respawn_delay: int
    levels: List[LevelConfig]
    cheat_mode_enabled: bool
