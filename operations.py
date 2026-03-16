"""
Calculator operations module.
Contains basic arithmetic and pay calculation functions.
"""

def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide a by b.
    
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Calculate base raised to exponent."""
    return base ** exponent


def calculate_pay(hours: float, rate: float) -> float:
    """
    Calculate pay with overtime (1.5x after 40 hours).
    
    Args:
        hours: Total hours worked
        rate: Hourly rate
        
    Returns:
        Total pay amount
        
    Raises:
        ValueError: If hours or rate is negative
    """
    if hours < 0 or rate < 0:
        raise ValueError("Hours and rate must be non-negative")
    
    if hours <= 40:
        return hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        return regular_pay + overtime_pay
