""" ## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list

file_path = "SalesData.csv"  
data = csv_to_list(file_path)
print(data)

for dat in data[1:]:
    average_store = {}
    store_name = dat[0]
    sales = dat[1:]
    print(sales) """
"""     sales = map(int, dat[1:])
    total_sales = sum(sales)
    average_store['store_name'] = store_name
    average_store['total_sales'] = total_sales
    print(average_store) """






""" def alltemp():
    for temp in temperatures[1:]: #doesn't work
        temperatures = ["labels", 32, 50, 77, 104]
        celcius = map(lambda x: ((x - 32) * 5 / 9), temperatures)
        print(list(celcius))
alltemp() """


    
#[[1,2,3],
 #[Bay, 7, 7, 6],
 #[8th,7,7,5],]
#x[2]y [2]y

#Lambda function is an anonymous function, it has no name. We use it inside map to condense the map function. You can just say lambda, create this instead of giving something a name and then doing the same thing. We don't have to write return too so it simplifies.




""" fee = 0
print("hi")
while True:
    Python_Programming = courses["Python Programming"]
    Machine_Learning = courses["Machine Learning"]
    Business_Strategy = courses["Business Strategy"]
    Marketing_101 = courses["Marketing 101"]
    Cybersecurity = courses["Cybersecurity"]
    student_enrollment = print(str(input(f"What course would you like to enroll in?")))
    classes = []

    if student_enrollment == "Python Programming":
        if Python_Programming["seats"] == 0:
            print("Python Programming is full. Suggesting Machine Learning or Cybersecurity instead")
        else:
            fee += Python_Programming["fee"]
        
    elif student_enrollment == "Machine Learning":
        if Machine_Learning["seats"] == 0:
            print("Machine Learning is full. Suggesting Python Programming or Cybersecurity instead")
        else:
            fee += Machine_Learning["fee"]

    elif student_enrollment == "Business Strategy":
        if Business_Strategy["seats"] == 0:
            print("Business Strategy is full. Suggesting Marketing 101 instead")
        else:
            fee += Business_Strategy["fee"]

    elif student_enrollment == "Marketing_101":
        if Marketing_101["seats"] == 0:
            print("Marketing 101 is full. Suggesting Business Strategy instead")
        else:
            fee += Marketing_101["fee"]

    elif student_enrollment == "Cybersecurity":
        if Cybersecurity["seats"] == 0:
            print("Cybersecurity is full. Suggesting Python Programming or Machine Learning instead")
        else:
            fee += Cybersecurity["fee"]

    checkout = print(input(f"You are in {student_enrollment}, would you like to exit?(yes or no)"))
    if checkout == "yes":
        print("Your total payment without discount is ${fee}")
        if student_enrollment >= 3:
            fee * 0.95
        if student_enrollment == "Python Programming" or "Machine Learning" or "Cybersecurity":
            fee -= 20
        print("Your total payment with discount is ${fee}")
        break
    elif checkout == "no":
        continue """
#for i in course in courses.item():
    #if course[seats] > 0
        #print i
        #break

courses = {
    "Python Programming": {"fee": 150, "seats": 0, "category": "Technology"},
    "Machine Learning": {"fee": 200, "seats": 3, "category": "Technology"},
    "Business Strategy": {"fee": 100, "seats": 5, "category": "Business"},
    "Marketing 101": {"fee": 120, "seats": 2, "category": "Business"},
    "Cybersecurity": {"fee": 180, "seats": 4, "category": "Technology"}
}
fee = 0
student_enrollment = ["Python programming", "Business Strategy", "Marketing 101"]
print(student_enrollment["Python Programming"])
for i in student_enrollment in courses.item():
    if student_enrollment["Python Programming"]
        print i
        

