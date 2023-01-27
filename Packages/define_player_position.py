import random
from enum import Enum


class sign_of_game(Enum):
    """
    sign of different roles which play in the game are saved here.
    """
    LOSING_SIGN: str = '\U0001F4A8'
    DUNGEON_SIGN: str = '\U0001F49A'
    DRAGON_SIGN: str = '\U0001F432'
    LIFE_SIGN: str = '\U0001F9E1'
    BOMB: str = '\U0001F4A3'


def define_player_position(play_ground: list, level_number: int, user_avatar) -> list: # noqa E501
    """
    this function define position of different roles in the ground of the game

    Parameters
    ----------
    play_ground: list : the ground of play

    level_number: int : the level of the game which player choose

    user_avatar : the avatra of user


    Returns
    -------
    this function return the ground of the game
    """
    x_dragon: int = random.randint(level_number-3, level_number-1)
    y_dragon: int = random.randint(level_number-3, level_number-1)
    play_ground[x_dragon][y_dragon] = sign_of_game.DRAGON_SIGN.value

    x_player: int = random.randint(3, level_number-2)
    y_player: int = random.randint(3, level_number-2)
    play_ground[x_player][y_player] = user_avatar

    x_dungeon: int = random.randint(1, 3)
    y_dungeon: int = random.randint(1, 3)
    play_ground[x_dungeon][y_dungeon] = sign_of_game.DUNGEON_SIGN.value

    return play_ground
