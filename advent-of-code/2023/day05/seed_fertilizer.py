from typing import Callable
from bisect import bisect_right

def create_map(lines: list[str]) -> Callable[[int], int]:
    ranges: list[tuple[int, int, int]] = []
    while lines:
        line = lines.pop()
        if line.strip() == '':
            continue
        if line.strip().endswith("map:"):
            break
        destination_start, source_start, range_length = line.split(" ")
        ranges.append((int(source_start), int(destination_start), int(range_length)))
    ranges.sort(key=lambda x: x[0])

    def mapper(source_value: int):
        index = bisect_right(ranges, (source_value, 0, 0))
        if index == 0:
            return source_value

        source_start, destination_start, range_length = ranges[index - 1]
        if source_value <= source_start + range_length -  1:
            return destination_start + (source_value - source_start)
        return source_value
    return mapper
        

with open("day05/input.txt") as f:
    lines = f.readlines()
    seeds = [int(seed) for seed in lines[0].strip().split(":")[1].strip().split(" ")]
    print(seeds)
    humidToLocation = create_map(lines)
    tempToHumid = create_map(lines)
    lightToTemp = create_map(lines)
    waterToLight = create_map(lines)
    fertToWater = create_map(lines)
    soilToFert = create_map(lines)
    seedToSoil = create_map(lines)

    seed_pairs = []

    while seeds:
        seed_range = seeds.pop()
        seed_pairs.append((seeds.pop(), seed_range))
    locations = []
    for seed_start, seed_range in seed_pairs:
        for seed in range(seed_start, seed_start + seed_range):
            locations.append(humidToLocation(tempToHumid(lightToTemp(waterToLight(fertToWater(soilToFert(seedToSoil(seed))))))))
    print(min(locations))
        

