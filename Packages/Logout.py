from Packages import Login


def Logout(cross_player):
    if cross_player == 'logout':
        user_name, user_password, user_avatar = Login.Login()
        return user_name, user_password, user_avatar
    else:
        pass
