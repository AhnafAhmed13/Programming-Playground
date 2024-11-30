import cmath
import sys

def main():
    # Command line inputs
    _3b1b = False
    if len(sys.argv) > 1:
        if sys.argv[1] == "-3b1b":
            _3b1b = True
        else:
            print("Usage: python3 quadratic.py [-3b1b]")
            exit(1)

    # Coefficient inputs
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        c = int(input("c: "))
    except:
        print("Please enter a valid number!")
        exit(2)
    finally:
        print(f"You've entered: {a}x^2 + {b}x + {c}")

    # Function selection
    res = []
    if (_3b1b):
        print("3Blue1Brown Quadratic Formula:")
        res = quadratic_3b1b(a,b,c)
    else:
        print("Regular Quadratic Formula:")
        res = quadratic(a,b,c)

    # Print results
    print("roots:", res[0], res[1])

# Regular quadratic formula
def quadratic(a: int, b: int, c: int) -> list[int]:
    x1 = (-1*b + cmath.sqrt(b**2 - 4*a*c))/ (2*a)
    x2 = (-1*b - cmath.sqrt(b**2 - 4*a*c))/ (2*a)
    return [x1,x2]

# 3Blue1Brown quadratic formula
def quadratic_3b1b(a: int, b: int, c: int) -> list[int]:
    if a > 1:
        b /= a
        c /= a

    m = -1*b/2
    d_2 = m**2 - c
    d = cmath.sqrt(d_2)
    r = m + d
    s = m - d
    return [r,s]

if __name__ == "__main__":
    main()