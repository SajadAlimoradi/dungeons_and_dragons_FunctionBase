import time
import os
from pyfiglet import Figlet
from termcolor import colored


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


def loading_game() -> None:
    """
    showing loading for player; it means game is so heavy and cool :)
    this function return nothing
    """
    second_counter: int = 0
    while second_counter < 3:
        second_counter += 1
        print("LOADING.  ")
        time.sleep(0.25)
        clear_screen()
        print("LOADING.. ")
        time.sleep(0.25)
        clear_screen()
        print("LOADING...")
        time.sleep(0.25)
        clear_screen()
    start_message = Figlet(font='standard')
    print(colored(start_message.renderText('Are  you  ready  ?!'), 'red'))
    time.sleep(1)
    clear_screen()
    print(colored(start_message.renderText('GO'), 'red'))
    time.sleep(0.5)
    clear_screen()
