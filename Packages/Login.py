import csv
import os
import time


# cleaning
def clear_screen() -> int:
    """
    this function clean screen from previous code which ran
    """
    return os.system('cls')


def Login() -> str:
    """
    handling login of user and check the input with database
    """
    clear_screen()
    while True:
        with open('helper/user_data.csv', 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            user_name = input("UserName : ")
            user_password = input("Password : ")
            clear_screen()
            for line in csv_reader:
                if user_name == line[0] and user_password == line[1]:
                    user_avater = line[2]
                    print("You Logged in Succsesfully")
                    time.sleep(1)
                    clear_screen()
                    return user_name, user_password, user_avater
                    break
            else:
                print("Please enter correct data")
