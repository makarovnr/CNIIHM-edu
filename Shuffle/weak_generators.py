def weak_generator_first(s_i=0):
    return ( (s_i+1) * 8**3) % 10**3


def weak_generator_second(s_i=1):
    s_i = (5**7 * s_i + 1) % (2**10)
    return s_i
