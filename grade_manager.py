"""
grade_manager.py
Main entry point for the terminal-based student grade management system.
"""
from modules.validators import get_valid_name, get_valid_mark
from modules.grading import calculate_grade
from modules.reports import display_results

def main():
    # Storage structure: List of dictionaries to support duplicate names safely
    students = []

    print("Welcome to the Modular Student Grade Manager!")

    while True:
        print("\n--- Menu ---")
        print("1. Add Student")
        print("2. Show Results & Summary")
        print("3. Quit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            print("\n--- Add New Student ---")
            name = get_valid_name()
            mark = get_valid_mark()
            grade = calculate_grade(mark)
            
            students.append({'name': name, 'mark': mark, 'grade': grade})
            print(f"Success: Added {name} with mark {mark} (Grade: {grade}).")
            
        elif choice == '2':
            display_results(students)
            
        elif choice == '3':
            print("\nExiting Grade Manager. Goodbye!")
            break
        else:
            print("\nError: Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()