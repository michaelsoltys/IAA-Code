# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
# Problem 5.13 - FIFO_cache
# Hang Zhang
# 11/14/2019
# python 3.7

def FIFO_cache(stream, cache_size):
    """
    :param stream:
    :param cache_size:
    For simplicity, we use an array as our input, index shows the order of an input stream,
    Each iteration prints out cache information
    """
    cache = []
    misses = 0
    for item in stream:
        if item not in cache:
            cache.append(item)
            misses += 1
        if len(cache) > cache_size:
            cache.pop(0)
        print(str.format("cache: {},misses: {}", cache, misses))








