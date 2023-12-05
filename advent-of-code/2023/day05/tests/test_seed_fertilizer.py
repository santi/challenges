from ..seed_fertilizer import create_mapper


def test_mapper_interval_before_source():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [(0, 5, 2)]  # 0,1 -> 5,6

    mapper = create_mapper(map_intervals)
    mapped = mapper(seed_intervals)
    assert mapped == [(4, 5)]


def test_mapper_interval_after_source():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [(10, 5, 2)]  # 10,11 -> 5,6

    mapper = create_mapper(map_intervals)
    mapped = mapper(seed_intervals)
    assert mapped == [(4, 5)]


def test_mapper_interval_within_source():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [(5, 8, 2)]  # 5,6 -> 8,9

    mapper = create_mapper(map_intervals)
    mapped = sorted(mapper(seed_intervals))
    assert mapped == sorted([(4, 1), (8, 2), (7, 2)])


def test_mapper_interval_total_source():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [(4, 8, 5)]  # 4,5,6,7,8 -> 8,9,10,11,12

    mapper = create_mapper(map_intervals)
    mapped = sorted(mapper(seed_intervals))
    assert mapped == sorted([(8, 5)])


def test_mapper_interval_overlap_start_source():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [(2, 8, 5)]  # 2,3,4,5,6 -> 8,9,10,11,12

    mapper = create_mapper(map_intervals)
    mapped = sorted(mapper(seed_intervals))
    assert mapped == sorted([(10, 3), (7, 2)])


def test_mapper_interval_overlap_outside_start_source():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [(2, 8, 7)]  # 2,3,4,5,6,7,8 -> 8,9,10,11,12,13,14

    mapper = create_mapper(map_intervals)
    mapped = sorted(mapper(seed_intervals))
    assert mapped == sorted([(10, 5)])


def test_mapper_interval_overlap_end_source():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [(7, 8, 5)]  # 7,8,9,10,11 -> 8,9,10,11,12

    mapper = create_mapper(map_intervals)
    mapped = sorted(mapper(seed_intervals))
    assert mapped == sorted([(4, 3), (8, 2)])


def test_mapper_interval_overlap_outside_end_source():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [
        (4, 8, 8)
    ]  # 4,5,6,7,8,9,10,11 -> 8,9,10,11,12,13,14,15

    mapper = create_mapper(map_intervals)
    mapped = sorted(mapper(seed_intervals))
    assert mapped == sorted([(8, 5)])


def test_mapper_interval_overlap_whole_source():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [
        (3, 8, 8)
    ]  # 3,4,5,6,7,8,9,10,11 -> 8,9,10,11,12,13,14,15,16

    mapper = create_mapper(map_intervals)
    mapped = sorted(mapper(seed_intervals))
    assert mapped == sorted([(9, 5)])


def test_mapper_interval_two_outside():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [(0, 8, 3), (9, 9, 14)]

    mapper = create_mapper(map_intervals)
    mapped = sorted(mapper(seed_intervals))
    assert mapped == sorted([(4, 5)])


def test_mapper_interval_two_below():
    seed_intervals: list[tuple[int, int]] = [(4, 5)]  # 4,5,6,7,8
    map_intervals: list[tuple[int, int, int]] = [(0, 8, 3), (0, 9, 2)]

    mapper = create_mapper(map_intervals)
    mapped = sorted(mapper(seed_intervals))
    assert mapped == sorted([(4, 5)])
