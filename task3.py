#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
 
number = str(float(""))

x = number % 2

x > 0
while True:
    print("That is not an even integer")
    if x ==0:
        break 

print("That is an even integer")
        
    

