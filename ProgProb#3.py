#!/usr/bin/env python
# coding: utf-8

# In[2]:


# octal_decimal_converter.py
# Convert between Octal and Decimal with input validation and repeat menu.

def octal_to_decimal(octal_str):
    """Convert an octal string to its decimal equivalent."""
    decimal_value = 0
    power = 0
    for digit in reversed(octal_str):
        decimal_value += int(digit) * (8 ** power)
        power += 1
    return decimal_value

def decimal_to_octal(decimal_num):
    """Convert a decimal integer to its octal equivalent as a string."""
    if decimal_num == 0:
        return "0"
    octal_digits = []
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_digits.insert(0, str(remainder))
        decimal_num //= 8
    return "".join(octal_digits)

def is_valid_octal(octal_str):
    """Check if a string is a valid octal number (digits 0–7 only)."""
    return all(ch in "01234567" for ch in octal_str)

def main():
    while True:
        print("\n--- Octal & Decimal Converter ---")
        print("1. Octal to Decimal")
        print("2. Decimal to Octal")
        print("3. Quit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            octal_str = input("Enter an octal number: ").strip()
            if not octal_str or not is_valid_octal(octal_str):
                print(" Error: Invalid octal number (digits must be 0–7 only).")
                continue
            decimal_value = octal_to_decimal(octal_str)
            print(f"✅ The decimal equivalent of {octal_str} is {decimal_value}")

        elif choice == "2":
            decimal_str = input("Enter a decimal number: ").strip()
            if not decimal_str.isdigit():
                print("Error: Please enter a valid non-negative integer.")
                continue
            decimal_num = int(decimal_str)
            octal_value = decimal_to_octal(decimal_num)
            print(f"The octal equivalent of {decimal_num} is {octal_value}")

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
