"""
Implements two similar weak random number generators.
"""
first_global_counter = None
second_global_counter = None


def weak_generator_first():
    global first_global_counter
    first_global_counter = 57 if first_global_counter is None else first_global_counter
    res = ((first_global_counter+1) * 8**3) % 10**3
    first_global_counter = first_global_counter * 13**3 % 10**2
    return res


def weak_generator_second():
    global second_global_counter
    second_global_counter = 63 if second_global_counter is None else second_global_counter
    res = (5**7 * second_global_counter + 1) % (2**10)
    second_global_counter = second_global_counter * 15**3 % 10**2
    return res
