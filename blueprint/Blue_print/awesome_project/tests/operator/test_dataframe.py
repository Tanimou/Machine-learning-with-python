import awesome_project as pack
import numpy as np
import pandas as pd


def test_tolower():
    df = pd.DataFrame(np.array([
            ['a', 'b', 'c'],
            ['A', 'B', 'C'],
            ['a', 'b', 'c']
        ]), columns=['x', 'y', 'z'])
    df = pack.tolower(df, 'y')
    assert(df['y'][1] == 'b')


def test_toupper():
    df = pd.DataFrame(np.array([
            ['a', 'b', 'c'],
            ['A', 'B', 'C'],
            ['a', 'b', 'c']
        ]), columns=['x', 'y', 'z'])
    df = pack.toupper(df, 'y')
    assert(df['y'][0] == 'B')
