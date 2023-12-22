from shapely import Polygon


def get_coordinates_from_instructions(lines: list[str]) -> list[tuple[int, int]]:
    coords: list[tuple[int, int]] = [(0, 0)]
    for line in lines:
        direction, length, _ = line.strip().split(" ")
        current_coord = coords[-1]
        if direction == "U":
            coords.append((current_coord[0], current_coord[1] + int(length)))
        elif direction == "D":
            coords.append((current_coord[0], current_coord[1] - int(length)))
        elif direction == "L":
            coords.append((current_coord[0] - int(length), current_coord[1]))
        elif direction == "R":
            coords.append((current_coord[0] + int(length), current_coord[1]))
        else:
            raise ValueError("Invalid direction")
    return coords


def get_coordinates_from_colors(lines: list[str]) -> list[tuple[int, int]]:
    coords: list[tuple[int, int]] = [(0, 0)]
    for line in lines:
        _, _, color = line.strip().split(" ")
        direction = color[-2]
        length = int(color[2:-2], base=16)
        current_coord = coords[-1]
        if direction == "3":
            coords.append((current_coord[0], current_coord[1] + length))
        elif direction == "1":
            coords.append((current_coord[0], current_coord[1] - length))
        elif direction == "2":
            coords.append((current_coord[0] - length, current_coord[1]))
        elif direction == "0":
            coords.append((current_coord[0] + length, current_coord[1]))
        else:
            raise ValueError("Invalid direction")
    return coords


def area_including_boundary(polygon: Polygon) -> int:
    return int(abs(polygon.area) + polygon.exterior.length / 2 + 1)


def main():
    with open("day18/input.txt") as f:
        lines = f.readlines()

    print("Part 1:", area_including_boundary(Polygon(get_coordinates_from_instructions(lines))))
    print("Part 2:", area_including_boundary(Polygon(get_coordinates_from_colors(lines))))


if __name__ == "__main__":
    main()
