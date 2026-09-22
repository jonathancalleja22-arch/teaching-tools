student_name = "Jonathan"
date = "01.01.2020"
duration_hrs = 2.5
fee = 50
online_inperson = "online"
paid = True

rate_per_hour = fee / duration_hrs
print(rate_per_hour)

student_name_2 = "Jonathan"
date_2 = "01.01.2020"
duration_hrs_2 = 2.5
fee_2 = 50
online_inperson_2 = "online"
paid_2 = True

total_income = fee + fee_2
total_hours = duration_hrs + duration_hrs_2

print("Total Income: ", total_income)
print("Total Income Type: ",type(total_income))
print("Total Income is an integer because multiplying 2 integers together outputs and integer")
print("Total Hours: ", total_hours)
