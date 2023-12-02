import numpy as np

def arithmetic_arrangement(problems):
    
    if len(problems) > 5:
        print("Error: Too many problems.")
    
    arranged = ["","","",""]
    
    for i in problems:
        split = i.split()
        num1, op, num2 = split[0], split[1], split[2]
        
        if (num1.isdigit() and num2.isdigit()) == False:
            print("Error: Numbers must only contain digits.")
        if (op=="+" or op=="-") == False:
            print("Error: Operator must be '+' or '-'.")
        if ((len(num1)+len(num2))/2 > 4):
            print("Error: Numbers cannot be more than four digits.")
        width =  max(len(num1), len(num2)) + 2
        line3 = "-"*width
        arranged[0] += num1.rjust(width) + "    "
        arranged[1] += op + num2.rjust(width-1) + "    "
        arranged[2] += line3.rjust(width) + "    "
        arranged[3] += ""*width + "    "
    return "\n".join(arranged).rstrip()
        
    

problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arrangement(problems))
