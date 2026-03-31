import csv

def read_grades(file_name):
    try:
        with open(file_name, 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
            return data
    except FileNotFoundError:
        print("Error: grades.csv file not found.")
        return []
def validate_grades(data):
    for row in data:
        score = float(row['Score'])
        if score < 0 or score > 100:
            print(f"Invalid score found: {score}")
            return False
    return True
def validate_weights(data):
    total = 0
    formative = 0
    summative = 0

    for row in data:
        weight = float(row['Weight'])
        total += weight

        if row['Category'] == 'Formative':
            formative += weight
        elif row['Category'] == 'Summative':
            summative += weight

    if total != 100:
        print("Error: Total weight is not 100")
        return False

    if formative != 60:
        print("Error: Formative weight must be 60")
        return False

    if summative != 40:
        print("Error: Summative weight must be 40")
        return False

    return True

def calculate_gpa(data):
    total_score = 0

    for row in data:
        score = float(row['Score'])
        weight = float(row['Weight'])
        total_score += (score * weight) / 100

    gpa = (total_score / 100) * 5.0
    return total_score, gpa

def check_pass_fail(data):
    formative_total = 0
    formative_weight = 0

    summative_total = 0
    summative_weight = 0

    for row in data:
        score = float(row['Score'])
        weight = float(row['Weight'])

        if row['Category'] == 'Formative':
            formative_total += score * weight
            formative_weight += weight
        else:
            summative_total += score * weight
            summative_weight += weight

    formative_avg = formative_total / formative_weight
    summative_avg = summative_total / summative_weight

    if formative_avg >= 50 and summative_avg >= 50:
        return "PASSED"
    else:
        return "FAILED"

def resubmission(data):
    failed = []

    for row in data:
        if row['Category'] == 'Formative' and float(row['Score']) < 50:
            failed.append(row)

    if not failed:
        return []

    max_weight = max(float(row['Weight']) for row in failed)

    result = [
        row['Assignment']
        for row in failed
        if float(row['Weight']) == max_weight
    ]

    return result

def main():
    data = read_grades("grades.csv")

    if not data:
        return

    if not validate_grades(data):
        return

    if not validate_weights(data):
        return

    total, gpa = calculate_gpa(data)
    status = check_pass_fail(data)
    resubmit = resubmission(data)

    print("===== GRADE REPORT =====")
    print(f"Total Grade: {total}")
    print(f"GPA: {gpa}")
    print(f"Status: {status}")

    if resubmit:
        print("Resubmission Required For:")
        for item in resubmit:
            print("-", item)

main()
