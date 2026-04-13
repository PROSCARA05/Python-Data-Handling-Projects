# student_grade_manager.py
"""
Student Grade Management System
Demonstrates: lists, dictionaries, loops, conditionals, file handling
"""

class StudentGradeManager:
    def __init__(self):
        self.students = {}
    
    def add_student(self, name, grades=None):
        """Add a new student with optional grades"""
        if grades is None:
            grades = []
        self.students[name] = grades
        print(f"Student '{name}' added successfully!")
    
    def add_grade(self, name, grade):
        """Add a grade for a student"""
        if name in self.students:
            if 0 <= grade <= 100:
                self.students[name].append(grade)
                print(f"Added grade {grade} for {name}")
            else:
                print("Grade must be between 0 and 100")
        else:
            print(f"Student '{name}' not found!")
    
    def calculate_average(self, name):
        """Calculate average grade for a student"""
        if name in self.students and self.students[name]:
            avg = sum(self.students[name]) / len(self.students[name])
            return round(avg, 2)
        return 0
    
    def get_letter_grade(self, average):
        """Convert numerical grade to letter grade"""
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'
    
    def display_student_report(self, name):
        """Display complete report for a student"""
        if name in self.students:
            grades = self.students[name]
            if grades:
                avg = self.calculate_average(name)
                letter = self.get_letter_grade(avg)
                print(f"\n{'='*40}")
                print(f"Report for: {name}")
                print(f"{'='*40}")
                print(f"Grades: {grades}")
                print(f"Average: {avg}")
                print(f"Letter Grade: {letter}")
                print(f"Highest Grade: {max(grades)}")
                print(f"Lowest Grade: {min(grades)}")
                print(f"Number of Grades: {len(grades)}")
            else:
                print(f"No grades recorded for {name}")
        else:
            print(f"Student '{name}' not found!")
    
    def class_summary(self):
        """Display summary of all students"""
        if not self.students:
            print("No students enrolled!")
            return
        
        print(f"\n{'='*50}")
        print("CLASS SUMMARY")
        print(f"{'='*50}")
        for name in self.students:
            avg = self.calculate_average(name)
            letter = self.get_letter_grade(avg) if avg > 0 else 'N/A'
            print(f"{name:<15} | Avg: {avg:<6} | Grade: {letter}")
        
        # Calculate class average
        all_grades = [g for grades in self.students.values() for g in grades]
        if all_grades:
            class_avg = sum(all_grades) / len(all_grades)
            print(f"\nClass Average: {round(class_avg, 2)}")
    
    def top_performer(self):
        """Find student with highest average"""
        if not self.students:
            print("No students to evaluate!")
            return
        
        top_student = None
        top_avg = 0
        
        for name in self.students:
            avg = self.calculate_average(name)
            if avg > top_avg:
                top_avg = avg
                top_student = name
        
        if top_student:
            print(f"Top Performer: {top_student} (Average: {top_avg})")

# Interactive menu
def run_grade_manager():
    manager = StudentGradeManager()
    
    while True:
        print("\n" + "="*40)
        print("STUDENT GRADE MANAGER")
        print("="*40)
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Report")
        print("4. View Class Summary")
        print("5. Show Top Performer")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            name = input("Enter student name: ")
            manager.add_student(name)
        
        elif choice == '2':
            name = input("Enter student name: ")
            try:
                grade = float(input("Enter grade (0-100): "))
                manager.add_grade(name, grade)
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == '3':
            name = input("Enter student name: ")
            manager.display_student_report(name)
        
        elif choice == '4':
            manager.class_summary()
        
        elif choice == '5':
            manager.top_performer()
        
        elif choice == '6':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    run_grade_manager()