Code on Belady's anomaly added by Hang Zhang in COMP 554, fall 2019.

A Special case shows Belady's anomaly in FIFO

When we have a stream as  1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5

    Cache Info for each iteration when cache size is 4:
        cache: [1],misses: 1
        cache: [1, 2],misses: 2
        cache: [1, 2, 3],misses: 3
        cache: [1, 2, 3, 4],misses: 4
        cache: [1, 2, 3, 4],misses: 4
        cache: [1, 2, 3, 4],misses: 4
        cache: [2, 3, 4, 5],misses: 5
        cache: [3, 4, 5, 1],misses: 6
        cache: [4, 5, 1, 2],misses: 7
        cache: [5, 1, 2, 3],misses: 8
        cache: [1, 2, 3, 4],misses: 9
        cache: [2, 3, 4, 5],misses: 10

    Cache Info for each iteration when cache size is 3:
        cache: [1],misses: 1
        cache: [1, 2],misses: 2
        cache: [1, 2, 3],misses: 3
        cache: [2, 3, 4],misses: 4
        cache: [3, 4, 1],misses: 5
        cache: [4, 1, 2],misses: 6
        cache: [1, 2, 5],misses: 7
        cache: [1, 2, 5],misses: 7
        cache: [1, 2, 5],misses: 7
        cache: [2, 5, 3],misses: 8
        cache: [5, 3, 4],misses: 9
        cache: [5, 3, 4],misses: 9

This shows Belady's anomaly in FIFO, bigger cache can have more misses than a smaller one