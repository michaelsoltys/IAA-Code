Solution to Problem 2.16 - Checks whether a schedule is feasible.
Author: Ryan McIntyre

Input starts with job list, as comma-separated tuples
(deadline,profit). Separated by a colon from the job list is the 
schedule, a comma-separated list of tuples (time,index), where the
index of a job is implied by the order of the job list. index starts
at 0, for convenience. Line splits are removed.

Sample input has been provided.

Output is True or False; also prints either confirmation that the
schedule is feasible or the first encountered reason that it is
not feasible.
