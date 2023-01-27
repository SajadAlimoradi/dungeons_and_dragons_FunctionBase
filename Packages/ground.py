LIFE_SIGN: str = '\U0001F9E1'


# print play ground
def print_ground(play_ground: list, life_counter: int, user_avatar: str) -> None: # noqa E501
    """
    this function print play ground

    Parameters
    ----------
    life_counter : int : this parameter enter the situation of player life

    Returns
    -------

    """
    print(f"{user_avatar} -> {LIFE_SIGN} * {life_counter}")
    print("-------------\n")
    for line in play_ground:
        print(*line)
