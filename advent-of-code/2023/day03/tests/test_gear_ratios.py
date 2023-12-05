import numpy as np

from ..gear_ratios import EnginePart, get_engine_parts_on_line


def test_get_engine_parts_on_line_single():
    lines = np.array(
        [
            [".", ".", ".", ".", ".", "."],
            [".", "1", "2", "%", ".", "."],
            [".", ".", ".", ".", ".", "."],
        ],
        dtype=str,
    )
    engine_parts = get_engine_parts_on_line(lines, 1)
    assert engine_parts == [EnginePart(start=1, end=2, number=12)]


def test_get_engine_parts_on_line_multiple():
    lines = np.array(
        [
            [".", ".", ".", ".", "#", ".", "."],
            [".", "1", "2", ".", "3", "4", "."],
            [".", ".", "$", ".", ".", ".", "."],
            [".", "3", "4", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
        ],
        dtype=str,
    )
    engine_parts = get_engine_parts_on_line(lines, 1)
    assert engine_parts == [
        EnginePart(start=1, end=2, number=12),
        EnginePart(start=4, end=5, number=34),
    ]
