#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""


count = 2

while True:
    print(str(count))
    count = count + 2
    if count > 20:
        break