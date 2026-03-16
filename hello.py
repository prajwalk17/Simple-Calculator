"""
Pay Calculator with Overtime
Standalone script for calculating employee pay.
"""

def get_float_input(prompt: str) -> float:
    """Get validated float input from user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("❌ Value must be non-negative. Try again.")
                continue
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def calculate_pay(hours: float, rate: float) -> float:
    """
    Calculate pay with overtime (1.5x rate after 40 hours).
    
    Args:
        hours: Total hours worked
        rate: Hourly pay rate
        
    Returns:
        Total pay amount
    """
    if hours <= 40:
        return hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        return regular_pay + overtime_pay


def main():
    """Main function to run pay calculator."""
    print("="*40)
    print("     PAY CALCULATOR (with Overtime)")
    print("="*40)
    
    hours = get_float_input("Enter hours worked: ")
    rate = get_float_input("Enter hourly rate: $")
    
    total_pay = calculate_pay(hours, rate)
    
    print("\n" + "="*40)
    print(f"💰 Total Pay: ${total_pay:.2f}")
    
    if hours > 40:
        regular = 40 * rate
        overtime = (hours - 40) * rate * 1.5
        print(f"\nBreakdown:")
        print(f"  Regular (40 hrs @ ${rate:.2f}): ${regular:.2f}")
        print(f"  Overtime ({hours-40:.1f} hrs @ ${rate*1.5:.2f}): ${overtime:.2f}")
    
    print("="*40)


if __name__ == "__main__":
    main()
