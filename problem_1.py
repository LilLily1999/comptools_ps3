# Problem 1
# Write a script (or Jupyter Notebook code block) that opens the file, 
# uses a for loop to read through the file line by line and, after finishing reading through the file, 
# reports the highest water level and the date and time that was observed.


# Open the file
fhand = open('/blue/bsc4452/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv')


# Skip the header line
next(fhand)


# Set the variables
max_float_preliminary = float('-inf')
max_date = ''
max_time = ''


# Loop reading the lines
for line in fhand:
    line = line.strip();
    
# Split by ,
    pieces = line.split(',')


# Name the columns
    date = pieces[0]
    time = pieces[1]
    preliminary = pieces[3].strip('"')
    
# Change it to float
    float_preliminary = float(preliminary)


# Search the highest water level
    if float_preliminary > max_float_preliminary:
        max_float_preliminary = float_preliminary
        max_date = date
        max_time = time
        
# Report the hightest water level 
print(f"The highest water level is {max_float_preliminary} ft observed on {max_date} at {max_time}.")
