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
        

while True:
    course_choice = print(input(f"What course would you like to enroll in?"))
    checkout = print(input(f"Would you like to check out?"))
    if checkout == "no":
        course_choice = print(input(f"What course would you like to enroll in?"))
    fee = 0
    if course_choice == "Python Programming":
        print("No more seats, would you like to enroll in Machine Learning or Cybersecurity?")
    elif course_choice == "Machine Learning":
        fee + 200
        print(f"Your total is now ${fee}")
    elif course_choice == "Business Strategy":
        fee + 100
        print(f"Your total is now ${fee}")
    elif course_choice  == "Marketing 101": 
        fee + 120
        print(f"Your total is now ${fee}")
    elif course_choice == "Cybersecurity":
        fee + 180
        print(f"Your total is now ${fee}")

    if checkout == "yes":
        print(f"Your total payment without discount is ${"fee"}")
        if course_choice == "Machine Learning" or "Cybersecurity":
            fee -= 20
        elif course_choice >= 3:
            fee * 0.95
    break