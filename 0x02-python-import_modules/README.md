# Project: 0x02. Python - import & modules

## AUTHOR: *BASIL BASSEY*

*In partial fulfillment to the course requirement, ALX Software Engineering.*

## Resources

- [Modules](https://intranet.alxswe.com/rltoken/SY-cMfnwbHoPFaJ-D_LWig)
- [Command line arguments](https://intranet.alxswe.com/rltoken/5e3TphtJ6WSVkWsdd2eX_A)
- [Pycodestyle – Style Guide for Python Code](https://intranet.alxswe.com/rltoken/FlkAJ_kPXHC4Y65WrRvA4A)

**man or help:**

- `python3`

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/TYWTMEj3W1HhTHqMKu8kWA), **without the help of Google:**

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- How to use the built-in function `dir()`
- How to prevent code in your script from being executed when imported
- How to use command line arguments with your Python programs

### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
-The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`

## Task Files

0. `0-add.py` - **0. Import a simple function from a simple file** : imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
1. `1-calculation.py` - **1. My first toolbox!** : imports functions from the file calculator_1.py, does some Maths, and prints the result.
2. `2-args.py` - **2. How to make a script dynamic!** : a program that prints the number of and the list of its arguments.
3. `3-infinite_add.py` - **3. Infinite addition** : Write a program that prints the result of the addition of all arguments.
![cat meme](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/621c6dd72e1acff708141f3fab6dfa6ff37c5ee6.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230609%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230609T015158Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8b1071dee747fec04efe77b38729d5a048d7db5ba9c43c3810f4fe224c5e7006)
4. `4-hidden_discovery.py` - **4. Who are you?** : Write a program that prints all the names defined by the compiled module [hidden_4.pyc](https://github.com/alx-tools/0x02.py/raw/master/hidden_4.pyc)
5. `5-variable_load.py` - **5. Everything can be imported** : Write a program that imports the variable a from the file variable_load_5.py and prints its value.
6. `100-my_calculator.py` - **6. Build my own calculator!** : Write a program that imports all functions from the file calculator_1.py and handles basic operations.
7. `101-easy_print.py` - **7. Easy print** : Write a program that prints `#pythoniscool`, followed by a new line, in the standard output.
8. `102-magic_calculation.py` - **8. ByteCode -> Python #3** : Write the Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:

        3           0 LOAD_CONST               1 (0)
                    3 LOAD_CONST               2 (('add', 'sub'))
                    6 IMPORT_NAME              0 (magic_calculation_102)
                    9 IMPORT_FROM              1 (add)
                    12 STORE_FAST               2 (add)
                    15 IMPORT_FROM              2 (sub)
                    18 STORE_FAST               3 (sub)
                    21 POP_TOP

        4          22 LOAD_FAST                0 (a)
                    25 LOAD_FAST                1 (b)
                    28 COMPARE_OP               0 (<)
                    31 POP_JUMP_IF_FALSE       94

        5          34 LOAD_FAST                2 (add)
                    37 LOAD_FAST                0 (a)
                    40 LOAD_FAST                1 (b)
                    43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
                    46 STORE_FAST               4 (c)

        6          49 SETUP_LOOP              38 (to 90)
                    52 LOAD_GLOBAL              3 (range)
                    55 LOAD_CONST               3 (4)
                    58 LOAD_CONST               4 (6)
                    61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
                    64 GET_ITER
                >>   65 FOR_ITER                21 (to 89)
                    68 STORE_FAST               5 (i)

        7          71 LOAD_FAST                2 (add)
                    74 LOAD_FAST                4 (c)
                    77 LOAD_FAST                5 (i)
                    80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
                    83 STORE_FAST               4 (c)
                    86 JUMP_ABSOLUTE           65
                >>   89 POP_BLOCK

        8     >>   90 LOAD_FAST                4 (c)
                    93 RETURN_VALUE

        10     >>   94 LOAD_FAST                3 (sub)
                    97 LOAD_FAST                0 (a)
                    100 LOAD_FAST                1 (b)
                    103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
                    106 RETURN_VALUE
                    107 LOAD_CONST               0 (None)
                    110 RETURN_VALUE

9. `103-fast_alphabet.py` - **9. Fast alphabet** : Write a program that prints the alphabet in uppercase, followed by a new line.
