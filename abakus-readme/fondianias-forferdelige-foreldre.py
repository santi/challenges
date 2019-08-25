
def get_substrings(number):
    substrings = []
    for start_index in range(len(number)):
        for end_index in range(start_index + 1, len(number) + 1):
            substrings.append(number[start_index:end_index])
    return substrings


def is_dividable(dividend, divisor, lookup_table):
    if dividend in lookup_table[divisor]:
        return lookup_table[divisor][dividend]
    dividable = int(dividend) % divisor == 0
    lookup_table[divisor][dividend] = dividable
    return dividable


def is_single_child_parent(number, lookup_table):
    divisor = len(number)

    is_dividable_count = 0
    for substring in get_substrings(number):
        if is_dividable(substring, divisor, lookup_table):
            is_dividable_count += 1
            if is_dividable_count == 2:
                return False

    if is_dividable_count == 1:
        return True

def get_lookup_table(lower_limit, upper_limit):
    lookup_table = {}
    for length in range(len(str(lower_limit)), len(str(upper_limit)) + 1):
        lookup_table[length] = {}
    return lookup_table


def main():

    single_child_parents = []
    lower_limit = 1
    upper_limit = 1000000

    lookup_table = get_lookup_table(lower_limit, upper_limit)

    for i in range(lower_limit, upper_limit + 1):
        number = str(i)
        if is_single_child_parent(number, lookup_table):
            single_child_parents.append(i)
        
    print(sum(single_child_parents))

if __name__ == '__main__':
    main()
