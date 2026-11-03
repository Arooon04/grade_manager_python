"""
validators.py
Input validation utilities for safe terminal interactions.
"""

def get_valid_name():
    """Prompts until a non-empty name is provided."""
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Error: Name cannot be empty. Please try again.")

def get_valid_mark():
    """Prompts until a valid numeric mark between 0 and 100 is provided."""
    while True:
        user_input = input("Enter student mark (0-100): ").strip()
        try:
            mark = float(user_input)
            if 0 <= mark <= 100:
                return mark
            else:
                print("Error: Mark must be between 0 and 100 inclusive.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number (e.g., 85 or 74.5).")