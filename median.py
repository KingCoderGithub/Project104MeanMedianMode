import csv
with open("heightWeight.csv", newline = "") as f:
    reader = csv.reader(f)
    file_data = list(reader)
    
file_data.pop(0)
    
new_data = []
    
for i in range(len(file_data)) :
    number = file_data[i][1]
    new_data.append(number)
    
# median formula
n = len(new_data)
new_data.sort()

# floor division //
if n % 2 == 0 :
    # getting the first number
    median1 = float(new_data[n//2])
    # getting second number
    median2 = float(new_data[n//2-1])
    # getting mean for the above number
    median = (median1 + median2) / 2
    
else :
    median = new_data[n//2]
    
print("This is the median: " + str(median))