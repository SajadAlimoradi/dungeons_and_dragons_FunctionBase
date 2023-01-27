level_game: dict = {
    'easy': 8,
    'medium': 10,
    'hard': 12
}


# define player emoji
def detect_level(user_level: str) -> int:
    """
    this function translate the input of user from string to int
    Parameters
    ----------
    level_game : enter the dictionary of defined level

    user_level : the level which user enter will be enter here as string

    Returns
    -------
    the level which user enter will be return as int
    """
    for level, level_number in level_game.items():
        if level == user_level:
            return level_number
            break
        else:
            return level_game['medium']
