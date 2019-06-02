import src.game_moves as jugada
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import to_agraph
import argparse


max_deep = 0
G = nx.MultiDiGraph()
G.graph['edge'] = {'arrowsize': '0.6', 'splines': 'curved'}
G.graph['graph'] = {'scale': '3'}

def recursive_function(game_state, mov_before, deep):
    global max_deep
    if jugada.winner_confirmation(game_state):
        print("Winner")
    if deep == max_deep:
        return
    else:
        posibles = jugada.mov_posible(game_state, mov_before)
        for mov in posibles:
            state_new, mov_before_new = mov(game_state)
            G.add_node(str(game_state))
            G.add_edge(str(game_state), str(state_new))
            recursive_function(state_new, mov_before_new, deep + 1)


def main(deep):
    global max_deep
    max_deep = deep
    game_state = np.array([[-1, 1, 4, 0, 7, 2, -1], [-1, 5, 8, 9, 3, 6, -1]])
    recursive_function(game_state, None, 1)
    A = to_agraph(G)
    A.layout('dot')
    A.draw('brute_force.png')


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Brute Force')

    parser.add_argument('-D', '--deep',
                        help='recursive deep',
                        type=float,
                        required=True)

    args = parser.parse_args()
    main(deep=args.deep)
