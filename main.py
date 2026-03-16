"""
Simple Calculator Application
Provides basic arithmetic operations and pay calculation.
"""

from operations import add, subtract, multiply, divide, power, calculate_pay


def get_float_input(prompt: str) -> float:
    """
    Get validated float input from user.
    
    Args:
        prompt: Message to display to user
        
    Returns:
        Valid float value
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input. Please enter a number.")


def display_menu():
    """Display calculator menu options."""
    print("\n" + "="*40)
    print("       SIMPLE CALCULATOR")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Pay Calculator (Overtime)")
    print("0. Exit")
    print("="*40)


def basic_operation():
    """Handle basic arithmetic operations."""
    num1 = get_float_input("Enter first number: ")
    num2 = get_float_input("Enter second number: ")
    return num1, num2


def run_calculator():
    """Main calculator loop."""
    while True:
        display_menu()
        choice = input("\nSelect operation (0-6): ").strip()
        
        try:
            if choice == '0':
                print("\n✅ Thank you for using Simple Calculator!")
                break
                
            elif choice == '1':
                num1, num2 = basic_operation()
                result = add(num1, num2)
                print(f"\n📊 Result: {num1} + {num2} = {result}")
                
            elif choice == '2':
                num1, num2 = basic_operation()
                result = subtract(num1, num2)
                print(f"\n📊 Result: {num1} - {num2} = {result}")
                
            elif choice == '3':
                num1, num2 = basic_operation()
                result = multiply(num1, num2)
                print(f"\n📊 Result: {num1} × {num2} = {result}")
                
            elif choice == '4':
                num1, num2 = basic_operation()
                result = divide(num1, num2)
                print(f"\n📊 Result: {num1} ÷ {num2} = {result}")
                
            elif choice == '5':
                base = get_float_input("Enter base: ")
                exponent = get_float_input("Enter exponent: ")
                result = power(base, exponent)
                print(f"\n📊 Result: {base}^{exponent} = {result}")
                
            elif choice == '6':
                hours = get_float_input("Enter hours worked: ")
                rate = get_float_input("Enter hourly rate: $")
                pay = calculate_pay(hours, rate)
                print(f"\n💰 Total Pay: ${pay:.2f}")
                
                # Show breakdown for overtime
                if hours > 40:
                    regular = 40 * rate
                    overtime = (hours - 40) * rate * 1.5
                    print(f"   Regular (40 hrs): ${regular:.2f}")
                    print(f"   Overtime ({hours-40} hrs @ 1.5x): ${overtime:.2f}")
                
            else:
                print("\n❌ Invalid choice. Please select 0-6.")
                
        except ValueError as e:
            print(f"\n❌ Error: {e}")
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    run_calculator()
