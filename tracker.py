def calculate_rate(fee, duration):
    rate_per_hour = fee / duration
    return rate_per_hour

def is_below_standard(rate, treshold=300):
    if rate < treshold:
        return True
    else:
        return False

def process_lesson(student, fee, duration, paid):
    print("Student Name: ", student)
    print("Fee: ", fee)
    print("Lesson Duration :", duration, "hr")

    if  is_below_standard(calculate_rate(fee, duration)):
        print("WARNING: Rate below standard!")

    if paid:
        return fee
    else:
        return 0

students = []
fees = []
durations  = []
paid_status = []

no_of_lessons = int(input("How many lessons do you want to enter? "))

while no_of_lessons > 0:
    student_name = input("Please enter the student name: ")
    students.append(student_name)
    fee_collected = int(input("Please enter the fee collected: "))
    fees.append(fee_collected)
    lesson_duration = float(input("Please enter the lesson duration in hours: "))
    durations.append(lesson_duration)
    current_paid_status = input("Has the lesson been paid already? (yes/no): ")
    if current_paid_status.lower() == "yes":
        paid_status.append(True)
    elif current_paid_status.lower() == "no":
        paid_status.append(False)

    no_of_lessons -= 1

unpaid = 0
paid_total = 0

for i in range(len(fees)):
    income = process_lesson(students[i], fees[i], durations[i], paid_status[i])
    paid_total += income
    if income == 0:
        unpaid += 1


print("Total Income Received: ", paid_total)
print("Number of unpaid lesson: ", unpaid)
