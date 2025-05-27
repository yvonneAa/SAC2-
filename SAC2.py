#Ask the user to enter the total number of students in the class 
s = int(input("Total number of students in the class?: "))
#Create array for student names
sn = []
#Loop for students names
for i in range(s):
    na = input("What is this students name?: ")
    sn.append(na) #Append student names to array sn
#Ask user the total number of periods of the class is held in a week. (between 1 and 5) 
periods = int(input("How many periods of this class is held in a week?(1-5): "))
#Enter attendence of each user
for item in sn:
    for i in range(periods):
        attendance = input(f"Enter attendance for {sn}, period: ")
        
    

