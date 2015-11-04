# OJ_data

This directory should contain data used by the OJ, like list of problems, list of users, etc.

This is a sample directory following the required structure:

To prevent users from making scripts which copy other user's solutions and run them, unset read permissions for others on all files in `OJ_data` and `OJ_sandbox`.

<pre>
	OJ_data/
	+-- files/				(If you want some files to be available for programs to read, put them here. You can also have subfolders.)
	+-- problems/			(Contains all problems of the online judge)
	|   +-- TEST/				(problem code)
	|   |   +-- in/				(test cases inputs)
	|   |   |   +-- sample/		(sample input)
	|   |   |   |   `-- 1.txt
	|   |   |   +-- 1.txt
	|   |   |   +-- 2.txt
	|   |   |   `-- 3.txt
	|   |   +-- out/			(test cases outputs. This is optional if you are using a checker or solution program)
	|   |   |   +-- sample/		(sample output)
	|   |   |   |   `-- 1.txt
	|   |   |   +-- 1.txt
	|   |   |   +-- 2.txt
	|   |   |   `-- 3.txt
	|   |   `-- problem.md		(problem statement)
	|   `-- FCTRL/				(problem code)
	|		+-- editorial.md	(Problem's editorial)
	|		+-- in/				(test cases inputs)
	|       |   +-- sample.txt	(sample input)
	|		|   +-- small.txt
	|		|   `-- big.txt
	|		+-- out/			(test cases outputs. This is optional if you are using a checker or solution program)
	|       |   +-- sample.txt	(sample output)
	|		|   +-- small.txt
	|		|   `-- big.txt
	|		+-- problem.md		(problem statement)
	|		+-- sample_in/		(sample input)
	|		|   `-- 1.txt
	|		`-- sample_out/		(sample output)
	|			`-- 1.txt
	`-- users/					(this directory contains data of all users)
		+-- user1/				(username of the user)
		|	`-- TEST/			(problem code for which user1 has made a submission(s))
		|		+-- 1.py		(source code of 1st submission)
		|		+-- 2.c			(source code of 2nd submission)
		`-- user2/
			+-- TEST/
			|	+-- 1.py
			|	+-- 2.cpp
			|	+-- 3.cpp
			|	`-- 4.java
			`-- FCTRL/
				`-- 1.py
</pre>
