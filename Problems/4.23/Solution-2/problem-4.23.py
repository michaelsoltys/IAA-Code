# Introduction to the Analysis of Algorithms (3rd ed)
# Michael Soltys
## Solution to problem 4.23
## Luke LaFountaine, Carlos A. Gomez
## 11/10/2016
## python 3

import sys
from collections import namedtuple
from bisect import bisect_left


def get_predecessor(activities, u):

    h = []

    for i in range(len(activities)):
        start = activities[i].start

        idx = bisect_left(u, start)
        if u[idx] > start:
            idx -= 1

        h.append(idx)

    return h


def activity_selection(activities):

    # sort activities by finish
    activities = sorted(activities, key=lambda activity: activity.finish)
    n = len(activities)

    # u = distinct finish times and the earliest start time (length k)
    u = set([x.finish for x in activities])

    # add earliest start time
    u.add(min(set([x.start for x in activities])))
    u = sorted(list(u))
    k = len(u)

    # a = maximum possible profit array (length k)
    a = [0] * k

    # h(i) = largest number s.t. u[i] <= s[i]
    h = get_predecessor(activities, u)

    optimal_ending_here = [[] for x in range(n)]
    optimal = optimal_ending_here[0]
    global_max = 0

    # calculate the optimal profit for each finish time
    for j in range(1, k):

        local_max = 0
        for i in range(n):

            finish, profit = activities[i].finish, activities[i].profit

            if finish == u[j]:

                if profit + a[h[i]] > local_max:
                    local_max = profit + a[h[i]]
                    optimal_ending_here[j] = optimal_ending_here[h[i]][:] + [activities[i]]

        if local_max > a[j-1]:
            a[j] = local_max

            if local_max > global_max:
                global_max = local_max
                optimal = optimal_ending_here[j]

        else:
            a[j] = a[j-1]
            optimal_ending_here[j] = optimal_ending_here[j-1]

    return global_max, optimal


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print('Usage: python3 activity_selection.py <activities file>')
        sys.exit(0)

    # named type for handling activities
    Activity = namedtuple('Activity', ['start', 'finish', 'profit'])

    # read activities
    with open(sys.argv[1]) as f:
        raw_data = f.read().strip('()').split('),(')
        activities = [Activity(*(map(int, x.split(',')))) for x in raw_data]  # sorry

    print(activity_selection(activities))
