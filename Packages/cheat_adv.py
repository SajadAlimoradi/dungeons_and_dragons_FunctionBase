import time
import os
import logging
from Packages import (
    find_player,
    ground
)
from playsound import playsound
from termcolor import colored
from pyfiglet import Figlet
from enum import Enum
from PIL import Image


class sign_of_game (Enum):
    """
    sign of different roles which play in the game are saved here.
    """
    FIRE_SIGN: str = '\U0001F525'
    BOMB_SIGN: str = '\U0001F4A3'
    DRAGON_SIGN: str = '\U0001F432'
    LOSING_SIGN: str = '\U0001F4A8'


class sound_and_imgs_of_game(Enum):
    """
    path of voice are played, saved here.
    """
    comeonman: str = "D:\\Django\\Project_01\\D_and_D_V3.2\\Sounds\\comeonman.mp3" # noqa E501
    cheat_code_1: str = "D:\\Django\\Project_01\\D_and_D_V3.2\\Sounds\\cheat_code_1.mp3" # noqa E501
    sound_adv_1: str = "D:\\Django\\Project_01\\D_and_D_V3.2\\Sounds\\adv1.mp3"
    img_adv_1: str = "D:\\Django\\Project_01\\D_and_D_V3.2\\imgs\\adv1.jpg"


# logger is defined here
logger = logging.getLogger(__name__)
file_h = logging.FileHandler('helper/cheat_adv.log')
file_f = logging.Formatter('%(asctime)s - %(filename)s - %(message)s')
file_h.setFormatter(file_f)
file_h.setLevel(logging.INFO)
logger.addHandler(file_h)
logger.setLevel(logging.INFO)


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


def cheat_code(play_ground: list, cross_player: str, user_avatar: str, life_counter: int, level_number: int) -> None: # noqa E501

    """ some cheat code defined in the game, this function handle them

    Parameters
    ----------
    play_ground: list : the ground of play

    cross_player: str : the button which user press (left, right,...)

    user_avatar: str : the avatra of user

    life_counter: int : the situation of player life

    level_number: int : the level of the game which player choose


    Returns
    -------
    this function doesn't have any return

    """
    if cross_player == "comeonman":
        logger.info(f'player press [{cross_player}] cheatcode') # noqa E501
        logger.info('player win')
        clear_screen()
        x_player, y_player = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
        play_ground[x_player + 1][y_player] = sign_of_game.FIRE_SIGN.value
        play_ground[x_player - 1][y_player] = sign_of_game.FIRE_SIGN.value
        play_ground[x_player][y_player + 1] = sign_of_game.FIRE_SIGN.value
        play_ground[x_player][y_player - 1] = sign_of_game.FIRE_SIGN.value
        ground.print_ground(play_ground, life_counter, user_avatar)
        playsound(sound_and_imgs_of_game.comeonman.value) # noqa E501
        playsound(sound_and_imgs_of_game.cheat_code_1.value) # noqa E501
        win_message = Figlet(font='standard')
        print(colored(win_message.renderText('YOU WIN'), 'blue'))
        quit()
    elif cross_player == "bomb":
        logger.info(f'player press [{cross_player}] cheatcode') # noqa E501
        x_player, y_player = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
        if x_player < level_number - 2:
            play_ground[x_player + 1][y_player] = sign_of_game.BOMB_SIGN.value
            ground.print_ground(play_ground, life_counter, user_avatar)
            x_bomb, y_bomb = find_player.find_player(user_avatar, play_ground, level_number) # noqa E501
            time.sleep(0.5)
            clear_screen()
            play_ground[x_player + 1][y_player] = '()'
            play_ground[x_player + 2][y_player] = sign_of_game.BOMB_SIGN.value
            ground.print_ground(play_ground, life_counter, user_avatar)
        else:
            print("you can't bombing")
            ground.print_ground(play_ground, life_counter, user_avatar)
    elif cross_player == "fire":
        logger.info(f'player press [{cross_player}] cheatcode') # noqa E501
        x_bomb, y_bomb = find_player.find_player(sign_of_game.BOMB_SIGN.value, play_ground, level_number) # noqa E501
        if (x_bomb is not None) and (y_bomb is not None):
            play_ground[x_bomb][y_bomb] = sign_of_game.FIRE_SIGN.value
            clear_screen()
            ground.print_ground(play_ground, life_counter, user_avatar)
            x_fire, y_fire = find_player.find_player(sign_of_game.FIRE_SIGN.value, play_ground, level_number) # noqa E501
            x_dragon, y_dragon = find_player.find_player(sign_of_game.DRAGON_SIGN.value, play_ground, level_number) # noqa E501
            time.sleep(1)
            play_ground[x_fire][y_fire] = '()'
            if (x_dragon - x_fire == 0 and abs(y_dragon - y_fire) == 1) or (abs(x_dragon - x_fire) == 1 and y_dragon - y_fire == 0): # noqa E501
                logger.info('player win')
                play_ground[x_dragon][y_dragon] = sign_of_game.LOSING_SIGN.value # noqa E501
                clear_screen()
                ground.print_ground(play_ground, life_counter, user_avatar)
                playsound(sound_and_imgs_of_game.cheat_code_1.value) # noqa E501
                win_message = Figlet(font='standard')
                print(colored(win_message.renderText('Horray Dragon killed! YOU WIN'), 'blue')) # noqa E501
                quit()
        else:
            ground.print_ground(play_ground, life_counter, user_avatar)
            pass


def advertising(play_ground: list, cross_player: str, life_counter: int, user_avatar: str, level_number: int) -> int: # noqa E501
    """
    this function run the advertisment and change situation of player's life
    Parameters
    ----------
    play_ground: list : the ground of play

    cross_player: str : the button which user press (left, right,...)

    user_avatar: str : the avatar of user

    life_counter: int : the situation of player life

    level_number: int : the level of the game which player choose

    Returns
    -------
    this function return the situation of user's life.

    """
    life_counter = life_counter
    if cross_player == "adv":
        logger.info(f'player press watching ads') # noqa E501
        adv = Image.open(sound_and_imgs_of_game.img_adv_1.value) # noqa E501
        adv.show()
        playsound(sound_and_imgs_of_game.sound_adv_1.value)
        new_life_counter = life_counter + 1
        ground.print_ground(play_ground, new_life_counter, user_avatar)
        return new_life_counter
    else:
        return life_counter
