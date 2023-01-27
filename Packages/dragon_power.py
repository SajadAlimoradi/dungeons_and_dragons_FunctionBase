from Packages import (
    find_player,
    dragon_move,
    win_loss
)

DRAGON_SIGN: str = '\U0001F432'

def smelling_power(play_ground: list, attack_probability: float, life_counter: int, user_avatar: str, level_number: int) -> list: # noqa E501
    """detect the power of dragon smell and define how to act

    Parameters
    ----------
    play_ground: list : the ground of play

    attack_probability: float : probability of attack for dragon

    life_counter: int : the situation of player life

    user_avatar: str : the avatar of user

    level_number: int : the level of the game which player choose

    Returns
    -------
    this function return the ground of the game
    """
    row, col = find_player.find_player(user_avatar, play_ground, level_number)
    x_dragon, y_dragon = find_player.find_player(DRAGON_SIGN, play_ground, level_number) # noqa E501
    if attack_probability < 0.3:
        if (abs(row - x_dragon) == 0) and (abs(col - y_dragon) > 2 and (abs(col - y_dragon) <= 5)): # noqa E501
            print("YOU ARE IN DANGER!")
            play_ground = dragon_move.y_move_dragon(play_ground, life_counter, user_avatar, level_number) # noqa E501

        elif (abs(col - y_dragon) == 0) and (abs(row - x_dragon) > 2) and (abs(row - x_dragon) <= 5): # noqa E501
            print("YOU ARE IN DANGER!")
            play_ground = dragon_move.x_move_dragon(play_ground, life_counter, user_avatar, level_number) # noqa E501
    return play_ground

def hearing_power(play_ground: list, attack_probability: float, life_counter: int, user_avatar: str, level_number: int) -> int: # noqa E501
    """detect the power of dragon hearing and define how to act

        Parameters
    ----------
    play_ground: list : the ground of play

    attack_probability: float : probability of attack for dragon

    life_counter: int : the situation of player life

    user_avatar: str : the avatar of user

    level_number: int : the level of the game which player choose

    Returns
    -------
    this function return the ground of the game

    """
    row, col = find_player.find_player(user_avatar, play_ground, level_number)
    x_dragon, y_dragon = find_player.find_player(DRAGON_SIGN, play_ground, level_number) # noqa E501
    if attack_probability < 0.9:
        if (abs(row - x_dragon) == 0) and (abs(col - y_dragon) <= 2):
            print("hear", attack_probability)
            play_ground: list = dragon_move.y_move_dragon(play_ground, life_counter, user_avatar, level_number) # noqa E501
            life_situation: int = win_loss.lose(play_ground, life_counter, user_avatar, level_number) # noqa E501
            return life_situation
        elif (abs(col - y_dragon) == 0) and (abs(row - x_dragon) <= 2):
            print("hear", attack_probability)
            play_ground: list = dragon_move.x_move_dragon(play_ground, life_counter, user_avatar, level_number) # noqa E501
            life_situation: int = win_loss.lose(play_ground, life_counter, user_avatar, level_number) # noqa E501
            return life_situation
        else:
            return life_counter
    else:
        return life_counter
