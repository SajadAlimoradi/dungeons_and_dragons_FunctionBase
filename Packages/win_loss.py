import os
import logging
from termcolor import colored
from playsound import playsound
from pyfiglet import Figlet
from Packages import (
    find_player,
    ground
)


LOSING_SIGN: str = '\U0001F4A8'
DUNGEON_SIGN: str = '\U0001F49A'


logger = logging.getLogger(__name__)
file_h = logging.FileHandler('helper/win_lose.log')
file_f = logging.Formatter('%(asctime)s - %(filename)s - %(message)s')
file_h.setFormatter(file_f)
file_h.setLevel(logging.INFO)
logger.addHandler(file_h)
logger.setLevel(logging.INFO)


def clear_screen() -> int:
    """
    this function clean screen from previous code which ran
    """
    return os.system('cls')

# define losing


def lose(play_ground: list, life_counter: int, user_avatar: str, level_number: int) -> int: # noqa E501
    """
    this function define the position which player lose
    if position of player reach to dragon;
    player going to die or lost one of it's life

    Parameters
    ----------
    life_counter : Optional[int] : this parameter enter the situation
    of player life (Default value = 3)

    Returns
    -------
    finally return new situation of life player

    """
    clear_screen()
    if life_counter > 0:
        logger.info('player lost one life')
        new_life_counter = life_counter - 1
        ground.print_ground(play_ground, new_life_counter, user_avatar)
        playsound("D:\\Django\\Project_01\\D_and_D_V3.2\\Sounds\\losinglife.mp3") # noqa E501
        lose_message = Figlet(font='standard')
        print(colored(lose_message.renderText('BE CAREFULL !'), 'blue'))
        print("By watching advertisment you can return your lost life ==== adv") # noqa E501
        return new_life_counter
    else:
        logger.info('player lose')
        x_player, y_player = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
        play_ground[x_player][y_player] = LOSING_SIGN # noqa E501
        ground.print_ground(play_ground, life_counter, user_avatar)# noqa E501
        playsound("D:\\Django\\Project_01\\D_and_D_V3.2\\Sounds\\losing.mp3")
        lose_message = Figlet(font='standard')
        print(colored(lose_message.renderText('YOU LOSE :('), 'blue'))
        quit()


# define winning
def win(play_ground: list, life_counter: int, user_avatar: str, level_number: int) -> None: # noqa E501
    """this function define the position which player win
    if player reach to the dungeon; player going to win

    Parameters
    ----------
    life_counter : Optional[int] this parameter enter the situation of player life # noqa E501
        (Default value = 3)

    Returns
    -------
    this function return nothing
    """
    x_dungeon, y_dungeon = find_player.find_player(DUNGEON_SIGN, play_ground, level_number) # noqa E501
    x_player, y_player = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
    if (abs(x_player - x_dungeon) == 1 and abs(y_player - y_dungeon) == 0) or (abs(x_player - x_dungeon) == 0 and abs(y_player - y_dungeon) == 1): # noqa E501
        logger.info('player win')
        clear_screen()
        ground.print_ground(play_ground, life_counter, user_avatar)
        playsound("D:\\Django\\Project_01\\D_and_D_V3.2\\Sounds\\winning.mp3")
        win_message = Figlet(font='standard')
        print(colored(win_message.renderText('YOU WIN :)'), 'blue'))
        quit()
