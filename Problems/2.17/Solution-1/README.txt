Implementation of Algorithm 2.3 for job scheduling
Author: Ryan McIntyre

Input is comma-separated list of jobs tuples (deadline,profit).
Line splits are removed. The sample input is the one shown in
problem 2.20.

Output is a schedule for maximum profit. Jobs are referenced by
index, starting at 0, inferred from their order in the input,
so, unlike the text, when nothing is scheduled at time t,
Schedule[t] = -1.
