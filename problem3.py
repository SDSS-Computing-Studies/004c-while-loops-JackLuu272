#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""

number = int(input("Enter a number: "))
n1 = 0
n2 = 1
count = 1

while count < 101:
    nth = n1 + n2
    n1 = n2 
    n2 = nth
    print(n1, end=" ")
    if n1 > 100:
        break