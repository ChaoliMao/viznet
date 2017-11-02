import pdb
import numpy as np
from matplotlib import pyplot as plt

from ..netbasic import *
from ..zoo import *


def test_draw_rbm():
    plt.ion()
    fig = plt.figure(figsize=(6, 4))
    ax = plt.gca()
    draw_rbm(ax, 5, 4)
    ax.axis('equal')
    ax.axis('off')

    pdb.set_trace()
    plt.savefig('_rbm.png')


def test_draw_rbm_equivalent():
    with DynamicShow((6, 4), '_rbm.png') as d:
        draw_rbm(d.ax, 5, 4)


def test_draw_feed_forward():
    with DynamicShow((6, 6), '_feed_forward.png') as d:
        draw_feed_forward(d.ax, num_node_list=[5, 4, 1])


def test_theme_table():
    '''plot a table of node themes'''
    with DynamicShow((8, 4), filename='_theme_list.png') as d:
        handler = NNPlot(d.ax)
        for i, kind in enumerate(NODE_THEME_DICT.keys()):
            handler.add_node(name=kind[:2].upper(),
                             xy=(i // 2, i % 2), kind=kind)


if __name__ == '__main__':
    test_theme_table()
    test_draw_rbm()
    test_draw_rbm_equivalent()
    test_draw_feed_forward()
