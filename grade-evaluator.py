import csv

def load_grades(filename):
    """Load grades from CSV file"""
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        print("Error: File not found")
        return None

def validate_grades(data):
    """Validate category weights"""
    if not data:
        return False

    formative_weight = 0
    summative_weight = 0

    for row in data:
        try:
            score = float(row['Score'])
            weight = float(row['Weight'])
            category = row['Category']

            if category == "Formative":
                formative_weight += weight
            elif category == "Summative":
                summative_weight += weight
            else:
                print(f"Error: Unknown category {category}")
                return False

        except KeyError:
            print("Error: Missing required column in CSV")
            return False
        except ValueError:
            print("Error: Invalid numeric value")
            return False

    # ✅ CHANGED RULE (Option 2 fix)
    if formative_weight != 40:
        print("Error: Formative weight must be 40")
        return False

    if summative_weight != 60:
        print("Error: Summative weight must be 60")
        return False

    return True


def calculate_grade(data):
    """Calculate final grade"""
    total = 0

    for row in data:
        score = float(row['Score'])
        weight = float(row['Weight'])
        total += score * (weight / 100)

    return total


def calculate_gpa(grade):
    """Convert grade to GPA"""
    if grade >= 70:
        return 4.0
    elif grade >= 60:
        return 3.0
    elif grade >= 50:
        return 2.0
    elif grade >= 40:
        return 1.0
    else:
        return 0.0


def main():
    filename = "grades.csv"
    data = load_grades(filename)

    if data is None:
        return

    if not validate_grades(data):
        return

    final_grade = calculate_grade(data)
    gpa = calculate_gpa(final_grade)

    print("\n===== GRADE REPORT =====")
    print(f"Total Grade: {final_grade:.2f}")
    print(f"GPA: {gpa:.1f}")

    if final_grade >= 50:
        print("Status: PASSED")
    else:
        print("Status: FAILED")


if __name__ == "__main__":
    main()
