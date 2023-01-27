import os
import random
import logging
from enum import Enum
from Packages import (
    Banner,
    level_game,
    Register,
    Login,
    user_player_sign,
    loading,
    ground,
    cheat_adv,
    player_move,
    dragon_power,
    win_loss,
    define_player_position
)

# number of player's life
life_counter: int = 3


# define player emoji
class sign_of_game(Enum):
    """ """
    LOSING_SIGN: str = '\U0001F4A8'
    DUNGEON_SIGN: str = '\U0001F49A'
    DRAGON_SIGN: str = '\U0001F432'
    LIFE_SIGN: str = '\U0001F9E1'
    BOMB: str = '\U0001F4A3'


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


# define ground of the game
def make_ground(level_number: int) -> list:
    """

    Parameters
    ----------
    level_number: int : stage of level which user choose is detected here.


    Returns
    -------
    The ground of game that user choose will be returned
    (base on the game's level)
    """
    play_ground: list = list()
    for column in range(level_number):
        empty_row: list = []
        for row in range(level_number):
            empty_row.append("()")
        play_ground.append(empty_row)
    return play_ground


'''
==============================================================================
GAME IS STARTING HERE!

prerequisite of starting game is going to be prepare.

like, login/register/level/establishing roles of game, etc
==============================================================================
'''

# Banner is running then user register or login the game
Banner.banner()
while True:
    clear_screen()
    enter_situation: str = input("\nPlease choose : Login / Register\n").casefold() # noqa E501
    if enter_situation == 'register':
        user_name, user_password, user_avatar = Register.Register()
        logging.basicConfig(filename='helper/login_register_total.log', format='%(asctime)s - %(filename)s - %(message)s', level=logging.INFO) # noqa E501
        logging.info(f'{user_name} Registered')
    elif enter_situation == 'login':
        user_name, user_password, user_avatar = Login.Login()
        logging.basicConfig(filename='helper/login_register_total.log', format='%(asctime)s - %(filename)s - %(message)s', level=logging.INFO) # noqa E501
        logging.info(f'{user_name} Logged in')
        break
    else:
        print("Please choose between these options")

# user choose the level of the game
user_level = input('Which level do you want to play? Easy - Medium - Hard\n\n').lower() # noqa E501
# user's ground print base on the level which user choose
level_number: int = level_game.detect_level(user_level)
play_ground: list = make_ground(level_number)
# avatar of user will be established
user_avatar: str = user_player_sign.user_player(user_avatar)
# after making ground, now roles are going to be established in the ground of the game # noqa E501
play_ground = define_player_position.define_player_position(play_ground, level_number, user_avatar) # noqa E501
# game is loading here (game need loading because it is so KHAFAN! :) )
loading.loading_game()
# all the roles are ready! ground of game is going to be printed here.
ground.print_ground(play_ground, life_counter, user_avatar)

'''
==============================================================================
prerequisite(like, login/register/level of game/establishing roles) of
starting game is ready.

Now game is going to start.
==============================================================================
'''

while True:
    attack_probability: float = random.random()
    cross_player: str = input("\nWhere Should I Go ?\n")
    clear_screen()
    if cross_player == "adv":
        life_counter: int = cheat_adv.advertising(play_ground, cross_player, life_counter, user_avatar, level_number) # noqa E501
    play_ground: list = player_move.move_left(play_ground, cross_player, life_counter, user_avatar, level_number, user_name) # noqa E501
    play_ground: list = player_move.move_right(play_ground, cross_player, life_counter, user_avatar, level_number, user_name) # noqa E501
    play_ground: list = player_move.move_up(play_ground, cross_player, life_counter, user_avatar, level_number, user_name) # noqa E501
    play_ground: list = player_move.move_down(play_ground, cross_player, life_counter, user_avatar, level_number, user_name) # noqa E501
    player_move.move_check(play_ground, cross_player, life_counter, user_avatar, level_number) # noqa E501
    player_move.move_help(play_ground, cross_player, life_counter, user_avatar, level_number) # noqa E501
    dragon_power.smelling_power(play_ground, attack_probability, life_counter, user_avatar, level_number) # noqa E501
    life_counter: int = dragon_power.hearing_power(play_ground, attack_probability, life_counter, user_avatar, level_number) # noqa E501
    win_loss.win(play_ground, life_counter, user_avatar, level_number)
    cheat_adv.cheat_code(play_ground, cross_player, user_avatar, life_counter, level_number) # noqa E501
    # print(attack_probability)
