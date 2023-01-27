import csv
import os
import time
from enum import Enum


class player (Enum):
    """avatar which user can choose them are saved here."""
    one = '\U0001F47D'
    two = '\U0001F916'
    three = '\U0001F921'


# cleaning
def clear_screen() -> int:
    """this function clean screen from previous code which ran"""
    return os.system('cls')


def Register() -> str:
    """handling registration of user and save it in csv file"""
    clear_screen()
    with open('helper/user_data.csv', 'a', newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter=',')
        print(f'one : {player.one.value}  two : {player.two.value}  three: {player.three.value}') # noqa E501
        while True:
            user_avatar: str = input("Please choose your avatar : one / two / three\n") # noqa E501
            if user_avatar not in ['one', 'two', 'three']:
                print("Please enter correct number")
            else:
                break
        user_name: str = input("UserName : ")
        user_password: str = input("Password : ")
        # confirm_user_password = input("confirm_user_password : ")
        # clear_screen()
        while True:
            confirm_user_password = input("Confirm Password : ")
            clear_screen()
            if user_password == confirm_user_password:
                csv_writer.writerow([user_name, user_password, user_avatar])
                print("You Registered Succsesfully")
                time.sleep(1)
                clear_screen()
                return user_name, user_password, user_avatar
                break
            else:
                print("Please enter correct")
                time.sleep(1)
                clear_screen()
