Grid-specific implementation of kruskal's algorithm
Author: Ryan McIntyre

Input is n-grid, encoded as shown in the text, with two
differences: first, vertex indices are assumed to start
at 0, so in a 4-grid, for example, the first row would 
consist of integers 0 through 3. Second, the semi-colon
in each edge has been replaced with a comma, for ease of
parsing.

An input reflecting the grid shown in figure 2.5 has been 
provided in "input.txt".

Output is a minimum cost spanning forest. This particular
version prints a simple visual representation of the forest,
but it could be easily modified to instead return a list of
edges in the form (vertex1,vertex2,weight).
