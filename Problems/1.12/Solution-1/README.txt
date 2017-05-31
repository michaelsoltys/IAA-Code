Implementation of Algorithm 1.3 - checks if input is a palindrome.
Author: Ryan McIntyre

Input: any interable, x.

Output: "True" if x is a palindrome. "False" otherwise.

The __main__ call first trys to call the algorithm on eval(x);
so if x is, for example, the string '[1,2,1]' it will return 
"True" as if x was the corresponding list, even though the 
string 'x' is not a palindrome. If eval(x) returns an error, 
it then tries to call the algorithm on x, as a string.
