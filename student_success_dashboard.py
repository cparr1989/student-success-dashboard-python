courses = {}

def add_course():
    course_name = input("Enter course name: ")

    if course_name in courses:
        print("Course already exists.")
    else:
        courses[course_name] = {
            "hours_studied": 0,
            "assignments_completed": 0,
            "assignments_missing": 0,
            "quiz_scores": [],
            "notes": []
        }
        print("Course added successfully.")

def add_study_session():
    course_name = input("Enter course name: ")

    if course_name not in courses:
        print("Course not found. Add the course first.")
        return

    hours = float(input("Hours studied: "))
    completed = int(input("Assignments completed: "))
    missing = int(input("Assignments missing: "))
    quiz_score = float(input("Quiz or test score: "))
    note = input("Study note or reminder: ")

    courses[course_name]["hours_studied"] += hours
    courses[course_name]["assignments_completed"] += completed
    courses[course_name]["assignments_missing"] += missing
    courses[course_name]["quiz_scores"].append(quiz_score)
    courses[course_name]["notes"].append(note)

    print("Study session saved.")

def view_dashboard():
    print("\nStudent Success Dashboard")
    print("-------------------------")

    if not courses:
        print("No courses added yet.")
        return

    for course, data in courses.items():
        scores = data["quiz_scores"]

        if scores:
            average_score = sum(scores) / len(scores)
        else:
            average_score = 0

        total_assignments = data["assignments_completed"] + data["assignments_missing"]

        if total_assignments > 0:
            completion_rate = (data["assignments_completed"] / total_assignments) * 100
        else:
            completion_rate = 0

        print(f"\nCourse: {course}")
        print(f"Hours Studied: {data['hours_studied']}")
        print(f"Assignments Completed: {data['assignments_completed']}")
        print(f"Assignments Missing: {data['assignments_missing']}")
        print(f"Assignment Completion Rate: {completion_rate:.2f}%")
        print(f"Average Quiz/Test Score: {average_score:.2f}%")

        if average_score >= 90 and completion_rate >= 90:
            print("Performance Status: Excellent")
        elif average_score >= 75 and completion_rate >= 75:
            print("Performance Status: Good")
        elif average_score >= 60:
            print("Performance Status: Needs Improvement")
        else:
            print("Performance Status: At Risk")

        print("Notes:")
        for note in data["notes"]:
            print("-", note)

def view_summary():
    total_hours = 0
    total_completed = 0
    total_missing = 0

    for data in courses.values():
        total_hours += data["hours_studied"]
        total_completed += data["assignments_completed"]
        total_missing += data["assignments_missing"]

    print("\nOverall Academic Summary")
    print("------------------------")
    print(f"Total Courses: {len(courses)}")
    print(f"Total Hours Studied: {total_hours}")
    print(f"Total Assignments Completed: {total_completed}")
    print(f"Total Assignments Missing: {total_missing}")

    if total_missing == 0:
        print("Overall Status: On Track")
    elif total_missing <= 2:
        print("Overall Status: Needs Attention")
    else:
        print("Overall Status: High Priority")

def main():
    while True:
        print("\nStudent Success Dashboard")
        print("1. Add Course")
        print("2. Add Study Session")
        print("3. View Course Dashboard")
        print("4. View Overall Summary")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            add_study_session()
        elif choice == "3":
            view_dashboard()
        elif choice == "4":
            view_summary()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

main()
