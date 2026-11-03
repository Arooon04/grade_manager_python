"""
reports.py
Handles table rendering and class statistical summaries.
"""

def display_results(students):
    """Displays a neatly formatted table of students along with class statistics."""
    if not students:
        print("\nNo student records found yet.")
        return

    print("\n" + "=" * 50)
    print(f"{'STUDENT NAME':<25} | {'MARK':<6} | {'GRADE':<5}")
    print("-" * 50)
    
    total_marks = 0
    highest_mark = students[0]['mark']
    lowest_mark = students[0]['mark']

    for student in students:
        name = student['name']
        mark = student['mark']
        grade = student['grade']
        
        # Clean up display of marks (show as integer if whole number)
        mark_str = f"{int(mark)}" if mark.is_integer() else f"{mark:.1f}"
        print(f"{name:<25} | {mark_str:<6} | {grade:<5}")
        
        total_marks += mark
        if mark > highest_mark:
            highest_mark = mark
        if mark < lowest_mark:
            lowest_mark = mark

    count = len(students)
    average = total_marks / count
    
    avg_str = f"{int(average)}" if average.is_integer() else f"{average:.1f}"
    high_str = f"{int(highest_mark)}" if highest_mark.is_integer() else f"{highest_mark:.1f}"
    low_str = f"{int(lowest_mark)}" if lowest_mark.is_integer() else f"{lowest_mark:.1f}"

    print("-" * 50)
    print(f"Total Students : {count}")
    print(f"Class Average  : {avg_str}")
    print(f"Highest Mark   : {high_str}")
    print(f"Lowest Mark    : {low_str}")
    print("=" * 50 + "\n")