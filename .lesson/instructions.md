# Instructions

Create a **private** GitHub repository named **A05**.

Your grade on this assignment is based on the correctness of your solutions and also your commit history.  Every time you begin working on a problem, push it to the ProblemP branch (where P is the problem number) of your A05 repo and every time you stop working on a problem, push again to your ProblemP branch.    

## Problem #1 - Recursion

(a) Write a recursive function that returns the sum of the elements stored at the even indexes of a given list.

(b) Write a recursive function that takes an immutable list and returns a list that removes all the negative elements from the immutable list.

(c) Write a recursive function that returns 1 if a list is strictly increasing, -1 if strictly decreasing, otherwise returns 0.

(d) Write a recursive function that mutates a list with a cumulative sum but only sum the positive values.  For example, [11, 3, -5, 6, -10, 7] should change to [11, 14, -5, 20, -10, 27].


## Problem #2 - Linked Lists

Your repl has LinkedList.java and LinkedList.py.  This is linked lists code that you cannot edit.

(a) Implement insertion sort using a linked list.

(b) Create a Stack class using a LinkedList as the only instance variable.  Your Stack class must have push, pop, top, isempty, and output methods.  The stack output from the statement
    push(10, push(20, push(30, None)))
should output exactly as

```
10 top 
20
30 bottom
```
(c) Create a Queue class using a LinkedList as the only instance variable.  Your Queue class must have enqueue, dequeue, isempty, and output methods.  The queue output from the statement
    enqueue(10, enqueue(20, enqueue(30, None)))
should output exactly as

```
front 10 <- 20 <- 30 back
```

## Problem #3 - An XUCS Scripting Language

Implement the following grammar for a simple scripting language:

```
<program> ::= <statement> | <program> <statement>
<statement> ::= <assignment> | <output>
<assignment> ::= <id> = <expression>
<output> ::= print <expression>
<expression> ::= <term> | <expression> <addition> <term>
<term> ::= <factor> | <term> <multiplication> <factor>
<factor> ::= <id> | <number> | -<factor> | (<expression>)
<id> ::= <letter> | <id><letter>
<letter> ::= a | b | c | ... | x | y | z
<number> ::= 0 | 1 | 2 | ... | 7 | 8 | 9
<addition> ::= + | -
<multiplication> ::= * | / | %
```
Here is a program using this grammar:

```
program
ab = 5
cde = ab + 3 / ab
ab = ab * -ab
cde = (ab + -2 % 10) - ab
print cde
```

Given a program in this language, run your program.

If a program's syntax is invalid, throw or raise *SyntaxError*.  If a program's execution is an arithmetic error, throw or raise *ArithmeticError*.  If any other error in the program, throw or raise *Exception*.