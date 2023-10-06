import csv

file_path ='./PyBank/Resources/budget_data.csv' 

with open(file_path) as csvfile: 
     csvreader = csv.reader(csvfile) 
    
     header = next(csvreader)  # We moved forward to the second line
     row  =next(csvreader)     # We moved forward to the third line
    
     total_net = int(row[1])   # We define a Variable to store the total amount for each line a posicion [1](Profit/Losses)
     total = 1                 # We set a Value for the total that will store the count for each row at index 1 in this case
     init =int(row[1])         # We set a variable to iterate  to calculate the changes vs previous Row
     list_change=[]            # We create a list to store the results over each iteration of this process (changes = int(row[1]) - init)
     
         
     for row in csvreader:     # For each row in csv file do as follow  iterator = "row"
      total_net += int(row[1]) # El total net es igual a la suma de del valor de "row" en cada intereracción de la posición [1]
      total = total + 1        # Total es igual a la suma de la linea en la que se encuentre "Row" en cada interacción
      changes = int(row[1]) - init  #Changes = a la resta del valor inicial (init) - el valor previo 
      list_change.append(changes)  # The result of changes will be store in a list
      init = int(row[1])       # We set a variable to iterate  to calculate the changes vs previous Row
     
maximun_value = max(list_change)
minumum_value = min(list_change)
average = sum(list_change) / len(list_change) # We calculate the average with the sum of the List and the len of the list


print(f'Financial Analysis')
print(f' Total Months:  {total}')   #The total number of months included in the dataset         
print(f' Total:  ${total_net}')     #The net total amount of "Profit/Losses" over the entire period
print(f' Average:  ${average}')      #The changes in "Profit/Losses" over the entire period, and then the average of those changes
print(f' Greatest increase in profits: ${maximun_value}')
print(f' Greatest decrease in profits: ${minumum_value}')

with open('results.txt', 'w') as f:
    
    f.write('Financial Analysis')
    f.write('\nTotal Months:  86')        
    f.write('\nTotal:  $22564198')   
    f.write('\nAverage:  $-8311.105882352942')
    f.write('\nGreatest increase in profits: $1862002')
    f.write('\nGreatest decrease in profits: $-1825558')
    f.close()
    


   
            
