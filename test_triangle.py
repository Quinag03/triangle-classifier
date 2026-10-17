import math
from triangle import classify_triangle, is_valid_triangle


# Test that an equilateral triangle is classified correctly.
def test_equilateral():
    assert classify_triangle(1, 1, 1) == "Equilateral"

# Test that a triangle with exactly two equal sides is classified as Isosceles.
def test_isosceles():
    assert classify_triangle(2, 2, 3) == "Isosceles"
    assert classify_triangle(2, 3, 2) == "Isosceles"
    assert classify_triangle(3, 2, 2) == "Isosceles"

# Test that three different valid side lengths are classified as Scalene.
def test_scalene():
    assert classify_triangle(2, 3, 4) == "Scalene"

# Test that a triangle with a side length of zero is Invalid.
def test_invalid():
    assert classify_triangle(0, 1, 1) == "Invalid"
    assert classify_triangle(1, 0, 1) == "Invalid"
    assert classify_triangle(1, 1, 0) == "Invalid"

# Test that a degenerate triangle, where two sides add up exactly to the third, is Invalid.
def test_degenerate():
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(2, 3, 1) == "Invalid"
    assert classify_triangle(3, 1, 2) == "Invalid"

# Test that a right triangle with non-integer side lengths is classified as Right Isosceles.
def test_right_isosceles():
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Isosceles"