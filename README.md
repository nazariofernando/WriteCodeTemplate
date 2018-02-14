# WriteCodeTemplate
Write a Code Template practice problem for compsci competitions taken from ITMOx: I2CPx (edx.org)

**Prompt:**

In a programming competition, most solutions have to perform similar actions, such as opening and closing input and output files. Everyone who participated in competitions encountered this situation and, as a result, invented a code template for personal use.

A code template is a program, which serves as the starting point for writing the actual solution to a programming problem. Being a template, it is typically written once for all solutions at the beginning of the competition.

However, there is a problem. Everyone has her/his own favourite language for programming competitions, and of course the code template is prepared for this language as well.

Alice, Beatrice and Cynthia are forming a team, and now they have to agree on which programming language to choose. After long discussions, they decided to choose a language, for which they have a code template which takes the minimum time to type.

Assume that the keyboard, which is used in the competition, is rectangular, and every symbol presents at most once on this keyboard. Let's introduce a Cartesian coordinate system, such that the coordinates of all keys are integers. What's more, all x values belong to the [1;W] range, all y values belong to the [1;H] range, and the lower left key has the coordinate of (1;1).

The distance between the two symbols on this keyboard is the maximum of the differences of key coordinates where these two symbols are located. For instance, if symbol A has a key with coordinates (Xa,Ya), and symbol B has a key at (Xb,Yb), then the distance between A and B is max(|Xa-Xb|,|Ya-Yb|).

The time to type a code template is the sum of distances between the first and the second symbol, the second and the third symbol, …, the next-to-last and the last symbol of the template. Whitespaces of all sorts and newline characters are not counted as symbols of the template.

Alice, Beatrice and Cynthia each proposed her own template for her favourite programming language. Please help them to choose the optimal ones!

Input:
The first line of the input ﬁle contains two integer numbers W and H (1<=W,H<=94) – the width and the height of the keyboard. The next H lines contain W ASCII symbols each with possible codes from 33 to 126 inclusively. These lines determine the keyboard. Each symbol occurs at most once.

After this, three blocks follow, each containing a code template description. The first line of each block is the name of the programming language. The name of the programming language does not exceed 100 characters and may contain ASCII symbols from 33 to 126. The next line contains a string %TEMPLATE-START%. The following lines contain the code template itself. In every line, the allowed symbols are ASCII symbols from 32 to 126, however, whitespaces (ASCII code 32) should be ignored. The code template never contains a string %TEMPLATE-END%. In the line following the last line of the code template there is a string %TEMPLATE-END%.

The number of symbols in every code template does not exceed 10000 (not including newline characters). Every symbol in a template will exist on the keyboard (which was described in the beginning of the input file).

Output:
In the first line of the output file print the name of the language of the code template, which the team should choose. The second line should contain the time needed to type the chosen code template. If there are several possible code templates with the same time, output the one which comes first in the input file.
