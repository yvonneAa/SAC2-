#Ask the user to enter the total number of students in the class 
s = int(input("Total number of students in the class?: "))

#Ask user the total number of periods of the class is held in a week. (between 1 and 5) 
period = int(input("How many periods of this class is held in a week?(1-5): "))

#Create a dictionary to hold key (name) and value (attendance)
student = {}

#For how many students ask the user for student name, and the attenence of each class (P= present, A= absent)
for i in range(s):
    name = input("\n"+"Enter name for student: ")
    #Make variable for attendance input (P/A)
    attend = []
    for i in range(period):
        #While asking for attendance per period, ensure P or A was input
        while True:
            a = input(f"Enter attendance for {name} (P/A) for period {(i+1)}: ")
            #If user input correct value in 'a' (P/A) continue with program
            if a.upper() in ['P','A']:
                attend.append(a.upper())
                break
            #If user input incorrect value in 'a' give an error message
            else:
                print("Invalid submission. Please input P or A.")
        #Enter key (name) and value (attend) into dictionary 'student'
        student[name] = attend
                
#Print 'Attendance Report' on new line
print("\n"+"Attendance Report:")
#Calculate the attendance percentage per person 
for key, value in student.items():
    #Create variable for 'percent' as an integer
    percent = 0
    #For every item in value (attend)
    for i in value:
        #If value is equal to 'P', add 1 to variable 'percent'
        if i == 'P':
            percent = percent+1
    #Calculate percentage
    percentage = 0
    percentageRounded = 0
    if percent >= 1:
        percentage = percent/period*100
        percentageRounded = round(percentage, 2)
    else:
        percentage = percent
        percentageRounded = percent
    #Print student attendance report
    #If percentage below 75, print a warning along with their attendance percentage
    if percentage < 75:
        print(f"{key}: {percent} period/s present ({percentageRounded}%) - Warning: Low Attendance")
    else:
        print(f"{key}: {percent} period/s present ({percentageRounded}%)")
    
#Write data to a file
myFile = open("studentAttendance.txt","wt")
for item in student:
    myFile.write(str(student))
myFile.close()
#Print Data written to file on a new line
print("\n"+"Data written to file")
    
    
            
    