import logging
from Packages import (
    find_player,
    ground,
    type_check
)

DRAGON_SIGN: str = '\U0001F432'
DUNGEON_SIGN: str = '\U0001F49A'

logger = logging.getLogger(__name__)
file_h = logging.FileHandler('helper/Player_move.log')
file_f = logging.Formatter('%(asctime)s - %(filename)s - %(message)s')
file_h.setFormatter(file_f)
file_h.setLevel(logging.INFO)
logger.addHandler(file_h)
logger.setLevel(logging.INFO)
'''
name of the function which start with [move], controls the user

'''

def move_left(play_ground: list, cross_player: str, life_counter: int, user_avatar: str, level_number: int, user_name: str) -> list: # noqa E501
    """
    Parameters
    ----------
    play_ground: list : the ground of play

    cross_player: str : the button which user press (left, right,...)

    user_avatar: str : the avatar of user

    life_counter: int : the situation of player life

    level_number: int : the level of the game which player choose

    user_name: str : the usename of the user

    Returns
    -------
    this function return the ground of the game.

    """
    if cross_player == 'left':
        row, col = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
        x_dragon, y_dragon = find_player.find_player(DRAGON_SIGN, play_ground, level_number) # noqa E501
        x_position: int = row
        y_position: int = col - 1
        logger.info(f'{user_name} press {cross_player} and now its location is {x_position},{y_position}') # noqa E501
        if y_position < 0 or (x_position == x_dragon and y_position == y_dragon): # noqa E501
            ground.print_ground(play_ground, life_counter, user_avatar)
        else:
            play_ground[row][col] = () # noqa E501
            play_ground[x_position][y_position] = user_avatar # noqa E501
            ground.print_ground(play_ground, life_counter, user_avatar)
    return play_ground


def move_right(play_ground: list, cross_player: str, life_counter: int, user_avatar: str, level_number: int, user_name: str) -> list: # noqa E501
    """
    Parameters
    ----------
    play_ground: list : the ground of play

    cross_player: str : the button which user press (left, right,...)

    user_avatar: str : the avatar of user

    life_counter: int : the situation of player life

    level_number: int : the level of the game which player choose

    user_name: str : the usename of the user

    Returns
    -------
    this function return the ground of the game.

    """
    if cross_player == 'right':
        row, col = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
        x_dragon, y_dragon = find_player.find_player(DRAGON_SIGN, play_ground, level_number) # noqa E501
        x_position: int = row
        y_position: int = col + 1
        logger.info(f'{user_name} press {cross_player} and now its location is {x_position},{y_position}') # noqa E501
        if y_position > level_number-1 or (x_position == x_dragon and y_position == y_dragon ): # noqa E501
            ground.print_ground(play_ground, life_counter, user_avatar)
        else:
            play_ground[row][col] = () # noqa E501
            play_ground[x_position][y_position] = user_avatar # noqa E501
            ground.print_ground(play_ground, life_counter, user_avatar)
    return play_ground


def move_down(play_ground: list, cross_player: str, life_counter: int, user_avatar: str, level_number: int, user_name: str) -> list: # noqa E501
    """
    Parameters
    ----------
    play_ground: list : the ground of play

    cross_player: str : the button which user press (left, right,...)

    user_avatar: str : the avatar of user

    life_counter: int : the situation of player life

    level_number: int : the level of the game which player choose

    user_name: str : the usename of the user

    Returns
    -------
    this function return the ground of the game.

    """
    if cross_player == 'down':
        row, col = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
        x_dragon, y_dragon = find_player.find_player(DRAGON_SIGN, play_ground, level_number) # noqa E501
        x_position: int = row + 1
        y_position: int = col
        logger.info(f'{user_name} press {cross_player} and now its location is {x_position},{y_position}') # noqa E501
        if x_position > level_number-1 or (x_position == x_dragon and y_position == y_dragon ): # noqa E501
            ground.print_ground(play_ground, life_counter, user_avatar)
        else:
            play_ground[row][col] = () # noqa E501
            play_ground[x_position][y_position] = user_avatar # noqa E501
            ground.print_ground(play_ground, life_counter, user_avatar)
    return play_ground


def move_up(play_ground: list, cross_player: str, life_counter: int, user_avatar: str, level_number: int, user_name: str) -> list: # noqa E501
    """
    Parameters
    ----------
    play_ground: list : the ground of play

    cross_player: str : the button which user press (left, right,...)

    user_avatar: str : the avatar of user

    life_counter: int : the situation of player life

    level_number: int : the level of the game which player choose

    user_name: str : the usename of the user

    Returns
    -------
    this function return the ground of the game.

    """
    if cross_player == 'up':
        row, col = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
        x_dragon, y_dragon = find_player.find_player(DRAGON_SIGN, play_ground, level_number) # noqa E501
        x_position: int = row - 1
        y_position: int = col
        logger.info(f'{user_name} press {cross_player} and now its location is {x_position},{y_position}') # noqa E501
        if x_position < 0 or ( y_position == y_dragon and x_position == x_dragon): # noqa E501
            ground.print_ground(play_ground, life_counter, user_avatar)
        else:
            play_ground[row][col] = () # noqa E501
            play_ground[x_position][y_position] = user_avatar # noqa E501
            ground.print_ground(play_ground, life_counter, user_avatar) # noqa E501
    return play_ground


def move_check(play_ground: list, cross_player: str, life_counter: int, user_avatar: str, level_number: int) -> None: # noqa E501
    """
t   his function check the input
    Parameters
    ----------
    play_ground: list : the ground of play

    cross_player: str : the button which user press (left, right,...)

    user_avatar: str : the avatar of user

    life_counter: int : the situation of player life

    level_number: int : the level of the game which player choose

    user_name: str : the usename of the user

    Returns
    -------
    this function return nothing

    """
    if cross_player not in ['left', 'right', 'up', 'down', 'help', 'adv', 'bomb', 'fire']: # noqa E501
        print('please enter correct sign')
        type_check.type_check(cross_player)
        ground.print_ground(play_ground, life_counter, user_avatar)


def move_help(play_ground: list, cross_player: str, life_counter: int, user_avatar: str, level_number: int) -> None: # noqa E501
    """
    this function help player to find dungeon

    Parameters
    ----------
    play_ground: list : the ground of play

    cross_player: str : the button which user press (left, right,...)

    user_avatar: str : the avatar of user

    life_counter: int : the situation of player life

    level_number: int : the level of the game which player choose

    user_name: str : the usename of the user

    Returns
    -------
    this function return nothing.

    """
    if cross_player == 'help':
        print("========================================================================================") # noqa E501
        print(''' for playing use this method
                North : up
                South : down
                East : left
                West : right
                ''')
        x_dungeon, y_dungeon = find_player.find_player(DUNGEON_SIGN, play_ground, level_number) # noqa E501
        x_player, y_player = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
        print(f'You can find dungeon {  abs(x_dungeon - x_player)} home upper or downer from player') # noqa E501
        print(f'You can find dungeon { abs(y_dungeon - y_player)} home lefter or righter from player') # noqa E501
        print("========================================================================================") # noqa E501
        ground.print_ground(play_ground, life_counter, user_avatar)
