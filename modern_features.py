"""
Demonstration of Python 3.12+ Features
This file showcases modern Python features available in 3.12+
"""

from typing import override
from collections.abc import Sequence


# ============================================================================
# PEP 695: Type Parameter Syntax (Python 3.12+)
# ============================================================================

# New generic class syntax
class Stack[T]:
    """Generic stack using Python 3.12+ syntax."""

    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


# New generic function syntax
def first[T](items: Sequence[T]) -> T:
    """Return first item from sequence."""
    return items[0]


def last[T](items: Sequence[T]) -> T:
    """Return last item from sequence."""
    return items[-1]


# ============================================================================
# @override Decorator (Python 3.12+)
# ============================================================================

class Animal:
    """Base animal class."""

    def sound(self) -> str:
        """Make a sound."""
        return "Some sound"


class Dog(Animal):
    """Dog that overrides sound."""

    @override  # Type checker verifies this actually overrides parent method
    def sound(self) -> str:
        """Dogs bark."""
        return "Woof!"


class Cat(Animal):
    """Cat that overrides sound."""

    @override
    def sound(self) -> str:
        """Cats meow."""
        return "Meow!"


# ============================================================================
# F-string Enhancements (Python 3.12+)
# ============================================================================

def format_user_data(user_data: dict[str, str]) -> str:
    """
    Python 3.12+ allows more flexible f-string syntax.
    Can use same quotes inside f-strings.
    """
    # Quotes inside f-strings work better in 3.12+
    name = f"User: {user_data["name"]}"
    status = f"Status: {user_data["status"]}"

    # Multi-line f-strings with better formatting
    result = f"""
        Name: {user_data["name"]}
        Email: {user_data.get("email", "N/A")}
        Status: {user_data["status"]}
    """

    return result.strip()


# ============================================================================
# Type Alias Statement (Python 3.12+)
# ============================================================================

# Old way (pre-3.12)
# Point: TypeAlias = tuple[float, float]

# New way (3.12+) - using 'type' statement
type Point = tuple[float, float]
type Matrix = list[list[float]]
type StringDict = dict[str, str]


def distance(p1: Point, p2: Point) -> float:
    """Calculate distance between two points."""
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# ============================================================================
# Example Usage
# ============================================================================

def main() -> None:
    """Demonstrate Python 3.12+ features."""

    # Generic stack with type inference
    stack: Stack[int] = Stack()
    stack.push(1)
    stack.push(2)
    print(f"Popped: {stack.pop()}")

    # Generic functions
    numbers = [1, 2, 3, 4, 5]
    print(f"First: {first(numbers)}")
    print(f"Last: {last(numbers)}")

    # Override decorator
    dog = Dog()
    cat = Cat()
    print(f"Dog says: {dog.sound()}")
    print(f"Cat says: {cat.sound()}")

    # F-string enhancements
    user = {"name": "Alice", "status": "active", "email": "alice@example.com"}
    print(format_user_data(user))

    # Type aliases
    point1: Point = (0.0, 0.0)
    point2: Point = (3.0, 4.0)
    print(f"Distance: {distance(point1, point2)}")


if __name__ == "__main__":
    main()