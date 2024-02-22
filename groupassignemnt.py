print("Welcome to Uniten Business Development Unit Rental System\n")
print("List of facilities\n")
print("1.\tPBL Classroom(30pax)\n2.\tMeeting Room(60pax)\n3.\tWorkstation Computer Lab ITMS(30pax)\n4.\tSwimming Pool\n")

select_facility = input("Please select the facility you would like to book by inserting the relevant number: ")

while(select_facility != "1" and select_facility != "2" and select_facility != "3" and select_facility != "4"):
    select_facility = input("Please enter the correct number (1-4): ")

if(select_facility == "1"):
    facility_name = "PBL Classroom"
elif(select_facility == "2"):
    facility_name = "Meeting Room"
elif(select_facility == "3"):
    facility_name = "Workstation Computer Lab ITMS"
else:
    facility_name = "Swimming Pool"

print("\nYou inserted number", select_facility, ",", facility_name)

student_staff = input("\nAre you Uniten Student/Staff? (Type Yes or No): ")
student_staff = student_staff.lower()

while(student_staff != "yes" and student_staff != "no"):
    student_staff = input("Please type only Yes or No: ")
    student_staff = student_staff.lower()
    
if(student_staff == "yes"):
    student_staff_type = "Uniten Student/Staff"
else:
    student_staff_type = "Public"
    
print("You choose", student_staff_type, "as option.")

day = input("\nWhen would you like to book, mention the day only: ")
day = day.lower()

day_check = True

while(day_check):
    if(day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday"):
        weekday_index = 0
        day_check = False
    elif(day == "saturday" or day == "sunday"):
        weekday_index = 1
        day_check = False
    else:
        day = input("Please enter correct day: ")
        day = day.lower()

print("You choose", day.capitalize(), "as option.")

hour = input("\nHow many hours would you like to book/rent (Kindly type numbers only): ")
while(not hour.isdecimal()):
    hour = input("Please input type numbers only: ")
hour = int(hour)
        
### Determine rate based on the data given by user

# facility : PBL Classroom & meeting room
if(select_facility == "1" or select_facility == "2"):
    if(student_staff == "yes"):
        if(weekday_index == 0):
            rate = 100
        else:
            rate = 150
    else:
        if(weekday_index == 0):
            rate = 150
        else:
            rate = 200

#facility : Workstation Computer Lab, ITMS
elif(select_facility == "3"):
    if(student_staff == "yes"):
        if(weekday_index == 0):
            rate = 200
        else:
            rate = 250
    else:
        if(weekday_index == 0):
            rate = 250
        else:
            rate = 300

# facility : Swimming Pool
else:
    if(student_staff == "yes"):
        if(weekday_index == 0):
            rate = 30
        else:
            rate = 35
    else:
        if(weekday_index == 0):
            rate = 60
        else:
            rate = 65
            
total_payment = hour*rate

print("\n========================================================")
print("\n\t Facilities:", facility_name,"\n\t Uniten Student/Staff:", student_staff_type, 
      "\n\t Day:", day.capitalize(), "\n\t Hours:", hour)
print("\n========================================================")

while(total_payment > 0):
    print("\nTotal amount you need to pay: RM", round(total_payment, 2))
    payment = input("Please insert amount of payment: ")
    while(not payment.isdecimal()):
        payment = input("Please use only number: ")
    total_payment -= int(payment)
       
if(total_payment < 0):
    print("Giving back change...\nRM",total_payment*-1, "is returned")
        
input("\nThank you for booking the court using Uniten Business Development Unit Rental System")