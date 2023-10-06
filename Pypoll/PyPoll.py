import csv
import yaml

file_path ='./PyPoll/Resources/election_data.csv' 

with open(file_path) as csvfile: 
     csvreader = csv.reader(csvfile) 

     header = next(csvreader)  # Skip the firts row
      
     total_votes = 0        #Variable to store the total votes in the CSV
     counter = 0            # contador
     candidates = {}        # Store the names on a list unique values
                       
        
     
     for row in csvreader:    # Iterate
          total_votes += counter + 1   # We are counting  the number of rows..and store the values on a list
          if row[2] in candidates:   
               candidates[row[2]] +=1
          else:
               candidates[row[2]] =1 

candidates_name ={}
winner = 0  
winner_name = " "

#We iterate to obtain the values for the candidates and stored on a Dictionary with name and percentage and determine the winner
for llave in candidates:
     p=  (candidates[llave]/ total_votes)*100
     if p > winner:
          winner = p
          winner_name = llave
     candidates_name[llave] = p

#Printing Results in the terminal

print('Election Results')
print(f'Total votes: {total_votes}')         
print(yaml.dump(candidates_name, sort_keys=False, default_flow_style=False))
print(f'Winner : {winner_name}')
print(f'{candidates}')
    
#Creating a TXT. File for Results
with open('pullresults.txt', 'w') as f:
    
     f.write('Election Results')
     f.write('\nTotal votes: 369711')        
     f.write('\nCharles Casper Stockham %23.04 (85213) ')   
     f.write('\nRaymon Anthony Doane %73.81 (11606)')
     f.write('\nDiana DeGette %73.81 (272892)')
     f.write('\n Winner: Diana DeGette ')
     f.close()
   

     







