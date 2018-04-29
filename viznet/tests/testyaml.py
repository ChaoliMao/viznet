import yaml, pdb, os
import numpy as np
from numpy.testing import dec, assert_, assert_raises, assert_almost_equal, assert_allclose
import matplotlib.pyplot as plt

from ..parsecircuit import _parse_lines, parsecircuit, vizcode
from .. import NodeBrush, DynamicShow, QuantumCircuit, Pin

def test_codes():
    assert_(_parse_lines('2:5') == slice(2,5))
    assert_(_parse_lines('2& 3&5') == [2,3,5])
    assert_(_parse_lines('2 ') == [2])

    # now use handler to show codes.
    handler = QuantumCircuit(num_bit=6)
    handler.x += 0.6
    with DynamicShow() as ds:
        vizcode(handler, '/C(2)--/NOT(3);')
        vizcode(handler, '/End(0:6)')

def test_parse():
    with open(os.path.dirname(__file__)+'/test.yaml') as f:
        datamap = yaml.safe_load(f)
    print(datamap)
    parsecircuit(datamap)

if __name__ == '__main__':
    test_codes()
    #test_parse()
