from typing import Dict, Any

DEFAULT_CONFIG: Dict[str, Any] = {
    "highscore_filename": "highscores.json",
    "seed": 42,
    "lives": 3,
    "player_speed": 1,
    "points_per_pacgum": 10,
    "points_per_super_pacgum": 50,
    "points_per_ghost": 200,
    "pacgum_count": 42,
    "level_max_time": 90,
    "super_pacgum_duration": 8,
    "ghost_respawn_delay": 5,
    "levels": [
        {"width": 21, "height": 21},
        {"width": 21, "height": 21},
        {"width": 21, "height": 21},
        {"width": 21, "height": 21},
        {"width": 21, "height": 21},
        {"width": 21, "height": 21},
        {"width": 21, "height": 21},
        {"width": 21, "height": 21},
        {"width": 21, "height": 21},
        {"width": 21, "height": 21},
    ],
    "cheat_mode_enabled": False,
}
