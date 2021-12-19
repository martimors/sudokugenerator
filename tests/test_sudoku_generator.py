from logging import getLogger, basicConfig, DEBUG
import numpy as np
import pytest
from numpy.typing import ArrayLike
from services.sudoku_generator_service import SudokuGenerator



basicConfig(format="%(levelname)s:%(message)s", level=DEBUG)

logger = getLogger()


@pytest.fixture
def sut():
    return SudokuGenerator


@pytest.mark.parametrize(
    "seed,expected",
    [
        (
            "foo",
            np.array(
                [
                    [8, 5, 6, 4, 3, 9, 1, 2, 7],
                    [4, 3, 2, 6, 1, 5, 8, 7, 9],
                    [7, 1, 9, 5, 8, 2, 3, 6, 4],
                    [9, 6, 5, 3, 4, 1, 7, 8, 2],
                    [1, 8, 4, 2, 7, 6, 9, 5, 3],
                    [5, 7, 3, 8, 2, 4, 6, 9, 1],
                    [2, 4, 7, 1, 9, 8, 5, 3, 6],
                    [3, 2, 8, 9, 6, 7, 4, 1, 5],
                    [6, 9, 1, 7, 5, 3, 2, 4, 8],
                ]
            ),
        ),
        (
            "bar",
            np.array(
                [
                    [7, 2, 3, 8, 5, 1, 4, 9, 6],
                    [8, 5, 4, 1, 3, 6, 2, 7, 9],
                    [1, 6, 9, 5, 8, 7, 3, 4, 2],
                    [6, 8, 7, 4, 1, 5, 9, 2, 3],
                    [5, 3, 6, 9, 2, 4, 7, 8, 1],
                    [4, 9, 2, 3, 6, 8, 1, 5, 7],
                    [3, 1, 5, 7, 9, 2, 8, 6, 4],
                    [2, 7, 1, 6, 4, 9, 5, 3, 8],
                    [9, 4, 8, 2, 7, 3, 6, 1, 5],
                ]
            ),
        ),
        (
            "baz",
            np.array(
                [
                    [8, 4, 1, 5, 3, 7, 9, 6, 2],
                    [9, 5, 6, 1, 2, 3, 8, 4, 7],
                    [3, 2, 7, 4, 5, 6, 1, 9, 8],
                    [5, 6, 9, 3, 1, 2, 7, 8, 4],
                    [2, 9, 4, 6, 7, 8, 5, 1, 3],
                    [4, 7, 2, 8, 6, 1, 3, 5, 9],
                    [6, 1, 8, 7, 9, 4, 2, 3, 5],
                    [1, 3, 5, 2, 8, 9, 4, 7, 6],
                    [7, 8, 3, 9, 4, 5, 6, 2, 1],
                ]
            ),
        ),
    ],
)
def test_generate_sudoku(sut: SudokuGenerator, seed, expected: ArrayLike):
    sudoku: ArrayLike = sut.generate(random_seed=seed)
    assert (sudoku == expected).all()