<h4>Introduction</h4>
In this exercise you will be filtering genetic data to return only the bases at specified positions in a fictional genome. The test includes 4 parts of increasing complexity.  We'd like you to proceed sequentially.  To help you, we created a template to fill out. This is a timed test (2 hours from when you start), but we don't expect everyone to finish.  It's important to proceed sequentially so we can assess your progress. Not finishing is fine! We will evaluate your code based and if needed will follow up with questions on-site.

<h4>Here's the basic task</h4>
The process has two inputs -- genome data and a filter definition -- and outputs filtered genome data in the same format as the input. 
The genome data looks like this:
 
```
[[5, "G"],
 [6, "A"],
 [7, "TCGTC"],
 [15, "G"],
 [19, "TA"],
 [20, "C"],
 [22, "T"]]
```

 
The number for each entry is a position in the genome, and the letter is the base at that position.
 
The filter definition looks like this:
 
```
[[6, 7],
 [15, 20]]
```

Each entry defines an interval; the first number is a start position, and the second number is an end position. The start position is included in the range but the end position is excluded. 

<h4>Task #1</h4>
Produce a program to perform the process described above. 
You can assume that the entries in both input lists are sorted by position.

Input data: 
```
[[5, "G"],
 [6, "A"],
 [7, "T"],
 [15, "G"],
 [19, "T"],
 [20, "C"],
 [22, "T"]]
```

Filter:
```
[[6, 7],
 [15, 20]]
```

Output data:
```
[[6, "A"],
 [15, "G"],
 [19, "T"]]
```
 
<h4>Task #2</h4>
Extend your program to support a genome input file with multiple bases listed on a single line; 
the new representation of the example input above would be:

Input data:
```
[[5, "GAT"],
 [15, "G"],
 [19, "TC"],
 [22, "T"]]
```

Filter:
```
[[6, 7],
 [15, 20]]
```
 
Rows should pass the filter if they contain any base at a position that passes the filter; 
so the new output using the original filter would be:

Output data:
```
[[5, "GAT"],
 [15, "G"],
 [19, "TC"]]
```
 
<h4>Task #3</h4>
Extend your program to edit rows down to only the part of each row that matches the filter, 
so that the input from step (2) goes back to matching the output from step (1).

Input data: 
```
[[5, "GAT"],
 [15, "G"],
 [19, "TC"],
 [22, "T"]]
```

Filter:
```
[[6, 7],
 [15, 20]]
```

Output data:
```
[[6, "A"],
 [15, "G"],
 [19, "T"]]
```
 
<h4>Task #4</h4>
Extend your program to support genome input files that have up to two different bases for any given position. Assume
the output order does not matter for the same start position `[11, "T"]` vs `[11, "A"]`. For instance this file would 
now be valid:

Input data:
```
[[5, "G"],
 [5, "T"],
 [10, "GTC"],
 [11, "AT"],
 [13, "ACA"]]
```

Filter:
```
[[6, 7],
 [11, 13],
 [15, 20]]
```

Output data: 
```
[[11, "T"],
 [11, "A"],
 [12, "C"],
 [12, "T"],
 [15, "A"]]
```