import math


def is_valid_triangle(a, b, c) -> bool:
    # A triangle needs three positive side lengths.
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # The sum of any two sides must be greater than the remaining side.
    if a + b <= c or a + c <= b or b + c <= a:
        return False

    return True


def classify_triangle(a, b, c) -> str:
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    # Decide the basic triangle type.
    if a == b == c:
        triangle_type = "Equilateral"
    elif a == b or a == c or b == c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"

    # Put the sides in order so the longest side is the possible hypotenuse.
    x, y, hypotenuse = sorted([a, b, c])

    # math.isclose uses a tolerance instead of exact decimal equality.
    is_right = math.isclose(
        x**2 + y**2,
        hypotenuse**2,
        rel_tol=1e-9,
        abs_tol=1e-9,
    )

    if is_right:
        return f"Right {triangle_type}"

    return triangle_type