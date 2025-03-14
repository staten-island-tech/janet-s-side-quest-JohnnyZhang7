## This function opens the CSV for You!
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
""" print(data) """

for dat in data[1:]:
    average_store = {}
    store_name = dat[0]
    sales = dat[1:]
    print(sales)
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
        
