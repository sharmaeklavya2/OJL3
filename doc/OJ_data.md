# OJ_data

This directory should contain data used by the OJ, like list of problems, list of users, etc.

This is a sample directory following the required structure:

To prevent users from making scripts which copy other user's solutions and run them, unset read permissions for others on all files in `OJ_data` and `OJ_sandbox`.

<pre>
	OJ_data/
	+-- files/				(If you want some files to be available for programs to read, put them here. You can also have subfolders.)
	+-- contests/
	|	`-- MAIN/			(Contains all problems of the online judge)
	|		+-- TEST/				(problem code)
	|		|   +-- in/				(test cases inputs)
	|		|   |   +-- sample/		(sample input)
	|		|   |   |   `-- 1.txt
	|		|   |   +-- 1.txt
	|		|   |   +-- 2.txt
	|		|   |   `-- 3.txt
	|		|   +-- out/			(test cases outputs. This is optional if you are using a checker or solution program)
	|		|   |   +-- sample/		(sample output)
	|		|   |   |   `-- 1.txt
	|		|   |   +-- 1.txt
	|		|   |   +-- 2.txt
	|		|   |   `-- 3.txt
	|		|   +-- problem.md		(problem statement)
	|		|	`-- data.json		(data about problem)
	|		`-- FCTRL/				(problem code)
	|			+-- editorial.md	(Problem's editorial)
	|			+-- in/				(test cases inputs)
	|			|   +-- sample.txt	(sample input)
	|			|   +-- small.txt
	|			|   `-- big.txt
	|			+-- out/			(test cases outputs. This is optional if you are using a checker or solution program)
	|			|   +-- sample.txt	(sample output)
	|			|   +-- small.txt
	|			|   `-- big.txt
	|			+-- problem.md		(problem statement)
	|			`-- data.json		(data about problem)
	`-- submissions/			(this directory contains submissions)
		+-- user1/				(username of user)
		|	+-- 1.py			(source code of 1st submission)
		|	+-- 2.c				(source code of 2nd submission)
		`-- user2/
			+-- 1.py
			+-- 2.cpp
			+-- 3.cpp
			+-- 4.java
			`-- 5.py
</pre>
