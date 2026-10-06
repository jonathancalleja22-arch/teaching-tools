students = ["Ae", "Boon", "Cee"]
durations = [1.0, 1.5, 2.0]
fees = [400, 300, 600]
paid_status = [True, True, False]

data = [students,durations,paid_status]
total_income = 0 
unpaid_count = 0

for i in range(len(students)):

        for attr in data:
              print(attr[i])
        
        rate_per_hour = fees[i] / durations[i]
        print("Rate per hour:", rate_per_hour)

        if rate_per_hour < 300:
               print("Below standard rate!")

        if paid_status[i]:
              total_income += fees[i]
        else:
               unpaid_count += 1
               

print("Total Income: ", total_income)
print("Total Unpaid lessons: ", unpaid_count)    
