# Examples used to test the main symbolic fuzzer function
import math

# function 1 greatest common factor
def gcd(a: int, b: int) -> int:
    if a < b:
        c: int = a
        a = b
        b = c

    while b != 0:
        c: int = a
        a = b
        b = c % b
    return a

# function 2 checks what kind of triangle it is based on the length of sides
def check_triangle(a: int, b: int, c: int) -> int:
    if a == b:
        if a == c:
            if b == c:
                return "Equilateral"
            else:
                return "Isosceles"
        else:
            return "Isosceles"
    else:
        if b != c:
            if a == c:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            return "Isosceles"


# function 3 finds the absolute value of a number
def abs_value(x: float) -> float:
    if x < 0:
        v: float = -x
    else:
        v: float = x
    return v

# function 4 calculates the sum of a list of numbers
def calculate_sum(a, *args):
    sum = a
    for i in args:
        sum += i
    return sum

# function 5 calculates for roots using quadratic equation
def quad_solver(a, b, c):
    discriminant = b ^ 2 - 4 * a * c
    r1, r2 = 0, 0
    i1, i2 = 0, 0
    if discriminant >= 0:
        droot = math.sqrt(discriminant)
        r1 = (-b + droot) / (2 * a)
        r2 = (-b - droot) / (2 * a)
    else:
        droot = math.sqrt(-1 * discriminant)
        droot_ = droot / (2 * a)
        r1, i1 = -b / (2 * a), droot_
        r2, i2 = -b / (2 * a), -droot_
    if i1 == 0 and i2 == 0:
        return (r1, r2)
    return ((r1, i1), (r2, i2))
