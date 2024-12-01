import math
import sys

def main():
    print("Welcome to Trigonometry!")
    functions = ["sin", "cos", "tan"]
    function = input("Enter one of the following functions -> sin/cos/tan: ")
    if function not in functions:
        print("Please enter a valid function!")
        sys.exit(1)
    x = float(input("Enter the angle as degree: "))
    print(f"You've entered: {function}({x})")
    x = math.radians(x)
    res = None
    if function == "sin":
        res = sin(x)
    elif function == "cos":
        res = cos(x)
    elif function == "tan":
        res = tan(x)
    
    print(f"Result: {res}")

def sin(x: float) -> float:
    return round(math.sin(x), 2)

def cos(x: float) -> float:
    return round(math.cos(x), 2)

def tan(x: float) -> float:
    return round(math.tan(x), 2)

if __name__ == "__main__":
    main()