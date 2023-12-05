from functools import partial
from typing import Callable, Iterable, TypeVar

T = TypeVar("T")
type SeedInterval = tuple[int, int]


def chain(*funcs: Callable[[T], T]) -> Callable[[T], T]:
    def chainCalling(
        arg: T,
        funcs: Iterable[Callable[[T], T]],
    ):
        result = arg
        for f in funcs:
            result = f(result)
        return result

    return partial(chainCalling, funcs=funcs)


def seeds_to_seed_intervals(seeds: list[int]) -> list[SeedInterval]:
    seed_intervals = []
    for i in range(0, len(seeds), 2):
        seed_intervals.append((seeds[i], seeds[i + 1]))
    return seed_intervals


def create_mapper(
    ranges: list[tuple[int, int, int]]
) -> Callable[[list[SeedInterval]], list[SeedInterval]]:
    def mapper(source_ranges: list[SeedInterval]) -> list[SeedInterval]:
        destination_ranges: set[SeedInterval] = set()
        for source_start, source_length in source_ranges:
            any_match = False
            source_end = source_start + source_length - 1
            for range_source_start, range_destination_start, range_length in ranges:
                range_source_end = range_source_start + range_length - 1
                if range_source_end < source_start:  # outside of range, range is before source
                    continue
                elif range_source_start > source_end:  # outside of range, range is after source
                    continue

                if (
                    range_source_start >= source_start and range_source_end <= source_end
                ):  # range is within source
                    any_match = True
                    destination_start = range_destination_start
                    destination_length = range_length

                    destination_ranges.add(
                        (destination_start, destination_length)
                    )  # Add mapped interval within source

                    if source_interval_length := range_source_start - source_start:
                        source_ranges.append(
                            (source_start, source_interval_length)
                        )  # Add mapped interval before range

                    if source_interval_length := source_end - range_source_end:
                        source_ranges.append(
                            (range_source_end + 1, source_interval_length)
                        )  # Add mapped interval after range
                elif (
                    range_source_start < source_start and range_source_end <= source_end
                ):  # range starts before source and ends within source
                    any_match = True
                    destination_start = range_destination_start + (
                        source_start - range_source_start
                    )
                    destination_length = range_length - (source_start - range_source_start)
                    destination_ranges.add((destination_start, destination_length))

                    if source_interval_length := source_end - range_source_end:
                        source_ranges.append((range_source_end + 1, source_end - range_source_end))
                elif (
                    range_source_start >= source_start and range_source_end > source_end
                ):  # range starts within source and ends after source
                    any_match = True
                    destination_start = range_destination_start
                    destination_length = range_length - (range_source_end - source_end)
                    destination_ranges.add((destination_start, destination_length))

                    if source_interval_length := range_source_start - source_start:
                        source_ranges.append((source_start, source_interval_length))
                elif (
                    range_source_start < source_start and range_source_end > source_end
                ):  # range starts before source and ends after source
                    any_match = True

                    destination_start = range_destination_start + (
                        source_start - range_source_start
                    )
                    destination_length = source_length
                    destination_ranges.add((destination_start, destination_length))
                else:
                    raise ValueError(
                        f"Unhandled case: {range_source_start=} {range_source_end=} {source_start=} {source_end=}"
                    )
            if not any_match:
                destination_ranges.add((source_start, source_length))
        result = list(destination_ranges)
        return result

    return mapper


def create_map(
    lines: list[str],
) -> Callable[[list[SeedInterval]], list[SeedInterval]]:
    ranges: list[tuple[int, int, int]] = []
    while lines:
        line = lines.pop()
        if line.strip() == "":
            continue
        if line.strip().endswith("map:"):
            break
        destination_start, source_start, range_length = line.split(" ")
        ranges.append((int(source_start), int(destination_start), int(range_length)))
    ranges.sort(key=lambda x: x[0])
    return create_mapper(ranges)


with open("day05/input.txt") as f:
    lines = f.readlines()
    seeds = [int(seed) for seed in lines[0].strip().split(":")[1].strip().split(" ")]

    humid_to_location = create_map(lines)
    temp_to_humid = create_map(lines)
    light_to_temp = create_map(lines)
    water_to_light = create_map(lines)
    fert_to_water = create_map(lines)
    soil_to_fert = create_map(lines)
    seed_to_soil = create_map(lines)

    seed_to_location = chain(
        seed_to_soil,
        soil_to_fert,
        fert_to_water,
        water_to_light,
        light_to_temp,
        temp_to_humid,
        humid_to_location,
    )
    print("Part 1:", min(seed_to_location([(seed, 1)])[0] for seed in seeds)[0])
    print("Part 2:", min(seed_to_location(seeds_to_seed_intervals(seeds)))[0])
