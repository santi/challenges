from collections import defaultdict

def dfs(node: int, graph: dict[int, set[int]], visited: set[int], stack: list[int]):
    if node in visited:
        return stack
    visited.add(node)
    for child in graph[node]:
        if child not in visited:
            dfs(child, graph, visited, stack)
    stack.append(node)
    return stack

def fix_pages(pages: list[int], descendants: dict[int, set[int]]) -> int:
    sub_graph: dict[int, set[int]] = dict()
    for page in pages:
        sub_graph[page] = descendants[page].intersection(pages)

    ordering: list[int] = []
    visited: set[int] = set()
    for page in pages:
        dfs(page, sub_graph, visited, ordering)

    return ordering[len(ordering) // 2]

    
def get_middle_page(pages: list[int], descendants: dict[int, set[int]]) -> tuple[int, str]:
    bans: set[int] = set()
    for page in pages:
        if page in bans:
            return fix_pages(pages, descendants), "incorrect"
        bans = bans.union(descendants[page])
    return pages[len(pages) // 2], "correct"

def main():
    with open("day05/input.txt") as f:
        lines = map(lambda line: line.strip(), f.readlines())

    graph: dict[int, set[int]] = defaultdict(set)
    for line in lines:
        if line == "":
            break
        child, parent = list(map(int,line.split("|")))
        graph[parent].add(child)

    correct_sum = 0
    incorrect_sum = 0
    for line in lines:
        pages = list(map(int,line.split(",")))
        sum, correctness = get_middle_page(pages, graph)
        if correctness == "correct":
            correct_sum += sum
        else:
            incorrect_sum += sum

    print("Part 1:", correct_sum)
    print("Part 2:", incorrect_sum)
                

if __name__ == "__main__":
    main()