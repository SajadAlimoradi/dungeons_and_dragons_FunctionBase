def type_check(cross_player: str):
    """
    this function check user 's input
    Parameters
    ----------
    cross_player: str :  the button which user press (left, right,...)


    Returns
    -------
    this functon return nothing
    """
    if len(cross_player) != 4 and cross_player in 'left':
        print("\nDo you mean 'left'?\n")
    elif len(cross_player) != 5 and cross_player in 'right':
        print("\nDo you mean 'right'?\n")
    elif len(cross_player) != 2 and cross_player in 'up':
        print("\nDo you mean 'up'?\n")
    elif len(cross_player) != 4 and cross_player in 'down':
        print("\nDo you mean 'down'?\n")
    elif len(cross_player) != 4 and cross_player in 'bomb':
        print("\nDo you mean 'bomb'?\n")
    elif len(cross_player) != 4 and cross_player in 'fire':
        print("\nDo you mean 'fire'?\n")
    elif cross_player == " ":
        print("\nHow can i guess what do you want!!\n")
