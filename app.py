## This function opens the CSV for You!
""" def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)
print(data)  # Output the list """

def alltemp():
    celcius = {}
    for temp in temperatures[1:]:
        temperatures = ["Label", 32, 50, 77, 104]
        "Label" == temp[0]
        celcius = map(int, temp[1:])
        celcius["Label"] = ((temperatures + 32) * 4 ) % 9
    print(celcius)
    

        


""" ( C = (F - 32) * frac{5}{9} ) """


    

