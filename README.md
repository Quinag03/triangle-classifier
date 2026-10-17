# Triangle Classifier

A Python program that determines whether three side lengths form a valid triangle and classifies the triangle.

## Files

- `triangle.py` — triangle validation and classification functions
- `test_triangle.py` — Copilot-reviewed pytest unit tests
- `test_acceptance.py` — end-to-end acceptance test
- `requirements.txt` — project dependency list

## How to Run the Tests

Install pytest:

```bash
python -m pip install -r requirements.txt
```

Run all tests:

```bash
python -m pytest -v
```

## Classification Rules

- A triangle is invalid if any side is less than or equal to zero.
- A triangle is invalid if the sum of two sides is less than or equal to the remaining side.
- Three equal sides are `Equilateral`.
- Exactly two equal sides are `Isosceles`.
- Three different sides are `Scalene`.
- A right triangle receives the prefix `Right`, such as `Right Scalene`.

An equilateral triangle cannot be right because all of its angles are 60 degrees. A right triangle must have one 90-degree angle.

## Equivalence Classes and Boundaries

| Category | Example | Expected result |
|---|---|---|
| Non-positive side length | `(0, 1, 1)` | `Invalid` |
| Triangle-inequality failure | `(1, 1, 3)` | `Invalid` |
| Degenerate boundary | `(1, 2, 3)` | `Invalid` |
| Equilateral | `(1, 1, 1)` | `Equilateral` |
| Isosceles | `(2, 2, 3)` | `Isosceles` |
| Scalene | `(2, 3, 4)` | `Scalene` |
| Right triangle with non-integer side | `(1, 1, sqrt(2))` | `Right Isosceles` |

## Copilot Review Log

| Test | Copilot-suggested? | Decision | Why |
|---|---|---|---|
| `test_equilateral` | Yes | Kept | It correctly checks that three equal valid sides return `Equilateral`. |
| `test_isosceles` | Yes | Kept | It checks an isosceles triangle in all three side orders. |
| `test_scalene` | Yes | Edited | Copilot used `(3, 4, 5)`, which is a right triangle and returns `Right Scalene`; I changed it to `(2, 3, 4)`. |
| `test_invalid` | Yes | Kept | It correctly checks zero in each side position. |
| `test_degenerate` | Yes | Kept | It checks the boundary where two sides add up exactly to the third. |
| `test_right_isosceles` | Yes | Kept | It uses `sqrt(2)`, so the implementation must use a tolerance rather than exact Pythagorean equality. |

## Acceptance Criteria

1. Given three side lengths that cannot form a triangle, including a degenerate triangle, the system returns `Invalid` without crashing.
2. Given valid side lengths, the system returns the correct shape classification.
3. Given valid right-triangle side lengths, the system returns a result beginning with `Right` so the studio can reinforce the corners.

## AI-Use Disclosure

GitHub Copilot autocomplete was used to draft the Part 2 unit tests. I reviewed every suggestion against the assignment specification and corrected Copilot's incorrect scalene test. ChatGPT was used for programming guidance and troubleshooting. I manually typed the Part 3 acceptance test without using GitHub Copilot and verified all work by running `python -m pytest -v`.