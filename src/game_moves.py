import numpy as np


def winner_confirmation(game_state):
    """Confirm if the state of the game is winning.

    Arguments:
        game_state {2darray} -- game state

    Returns:
        [Boolean] -- True or False

    """
    game_state_win = np.array(
        [[-1, 0, 1, 2, 3, 4, -1], [-1, 5, 6, 7, 8, 9, -1]])
    if np.array_equal(game_state, game_state_win):
        return True
    else:
        return False


def mov_izq_up(game_state):
    """Move top row to the left.

    Arguments:
        game_state {2darray} -- game state

    Returns:
        [2darray, mov] -- [game state array, function mov]

    """
    mov = mov_izq_up
    i = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1]])
    j = np.array([[1, 2, 3, 4, 5, 6, 0],
                  [0, 1, 2, 3, 4, 5, 6]])
    # advance indexing copy()
    return game_state[(i, j)], mov


def mov_der_up(game_state):
    """Move top row to the right.

    Arguments:
        game_state {2darray} -- game state

    Returns:
        [2darray, mov] -- [game state array, function mov]

    """
    mov = mov_der_up
    i = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1]])
    j = np.array([[6, 0, 1, 2, 3, 4, 5],
                  [0, 1, 2, 3, 4, 5, 6]])
    # advance indexing copy()
    return game_state[(i, j)], mov


def mov_izq_down(game_state):
    """Move bottom row to the left.

    Arguments:
        game_state {2darray} -- game state

    Returns:
        [2darray, mov] -- [game state array, function mov]

    """
    mov = mov_izq_down
    i = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1]])
    j = np.array([[0, 1, 2, 3, 4, 5, 6],
                  [1, 2, 3, 4, 5, 6, 0]])
    # advance indexing copy()
    return game_state[(i, j)], mov


def mov_der_down(game_state):
    """Move bottom row to the right.

    Arguments:
        game_state {2darray} -- game state

    Returns:
        [2darray, mov] -- [game state array, function mov]

    """
    mov = mov_der_down
    i = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [1, 1, 1, 1, 1, 1, 1]])
    j = np.array([[0, 1, 2, 3, 4, 5, 6],
                  [6, 0, 1, 2, 3, 4, 5]])
    # advance indexing copy()
    return game_state[(i, j)], mov


def mov_flip(game_state):
    """Flip six center blocks (3 tops row and 3 bottom row).

    Arguments:
        game_state {2darray} -- game state

    Returns:
        [2darray, mov] -- [game state array, function mov]

    """
    mov = mov_flip
    i = np.array([[0, 0, 1, 1, 1, 0, 0],
                  [1, 1, 0, 0, 0, 1, 1]])
    j = np.array([[0, 1, 2, 3, 4, 5, 6],
                  [0, 1, 2, 3, 4, 5, 6]])
    # advance indexing copy()
    return game_state[(i, j)], mov


def mov_posible(game_state, before_mov=None):
    """Return all posibles movements in current state.

    Arguments:
        game_state {2darray} -- game state

    Keyword Arguments:
        before_mov {function} -- Before call functions mov (default: {None})

    Returns:
        [list] -- list of functions with all posible movements
        
    """
    movements = [mov_izq_up, mov_der_up, mov_izq_down, mov_der_down, mov_flip]
    if before_mov == None:
        len(movements)
    else:
        if before_mov == mov_izq_up:
            movements.remove(mov_der_up)
        elif before_mov == mov_der_up:
            movements.remove(mov_izq_up)
        elif before_mov == mov_izq_down:
            movements.remove(mov_der_down)
        elif before_mov == mov_der_down:
            movements.remove(mov_izq_down)
        elif before_mov == mov_flip:
            movements.remove(mov_flip)

    if (game_state[0][0] != -1) and mov_izq_up in movements:
        movements.remove(mov_izq_up)
    if (game_state[1][0] != -1) and mov_izq_down in movements:
        movements.remove(mov_izq_down)
    if (game_state[0][6] != -1) and mov_der_up in movements:
        movements.remove(mov_der_up)
    if (game_state[1][6] != -1) and mov_der_down in movements:
        movements.remove(mov_der_down)
    return movements
