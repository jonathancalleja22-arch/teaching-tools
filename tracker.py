student_name = "Mr. Example"
lesson_date = "18/09/2569"
duration_hrs = 3.0
fee_baht = 1800
online_or_inperson = "online"
paid = True

rate_per_hour = fee_baht / duration_hrs

print("Student Name: ", student_name)
print("Lesson Date: ", lesson_date)
print("Duration in Hours: ", duration_hrs)
print("Lesson Fee (baht): ", fee_baht)
print("Online/in-person: ", online_or_inperson)
print("Paid?: ", paid )
print("Rate per Hour: ", rate_per_hour)

if paid == False:
    print("Payment reminder needed")
else:
    print("Payment received")

if rate_per_hour >= 400:
    print("Premium rate")
elif rate_per_hour>= 250:
    print("Standard Rate")
else:
    print("Below standard rate - review")

if duration_hrs > 2 and paid == True:
    print("Long Session")


