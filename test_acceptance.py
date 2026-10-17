from triangle import classify_triangle


def test_stained_glass_customer_requirements():
    # A buildable right-angle piece is identified for reinforced corners.
    assert classify_triangle(3, 4, 5) == "Right Scalene"

    # A non-buildable piece gives a clear result instead of crashing.
    assert classify_triangle(1, 2, 3) == "Invalid"

    # A normal buildable piece reports its shape.
    assert classify_triangle(2, 2, 3) == "Isosceles"