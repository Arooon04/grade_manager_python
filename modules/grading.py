"""
grading.py
Grade calculation logic based on specified ranges.
"""

def calculate_grade(mark):
    """Determines the letter grade based on inclusive boundaries."""
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'E'