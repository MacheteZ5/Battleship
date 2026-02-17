from enum import Enum


class PlayerType(Enum):
    player = 1
    cpu = 2


class Orientation(Enum):
    horizontal = 1
    vertical = 2


class GameMode(Enum):
    singlePlayer = 1
    multiPlayer = 2


class ShowDashboard(Enum):
    yes = 1
    no = 2


class ContinueGame(Enum):
    yes = 1
    no = 2
