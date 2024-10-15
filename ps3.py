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


# Problem 2
# Either in a new script or modifying the above script, calculate the lowest, 
# highest and average water level observed during the time period. 
# As above, print the date and time for the lowest and highest readings. 

# Open the file
fhand = open('/blue/bsc4452/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv')

# Skip the header line
next(fhand)

# Set the variables
low_float_preliminary = float('inf')
low_date = ''
low_time = ''

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

# Search the lowest water level
    if float_preliminary < low_float_preliminary:
        low_float_preliminary = float_preliminary
        low_date = date
        low_time = time

# Caluculate the total sum and count
    total += float_preliminary
    count += 1
    
# Caluculate the average
average = total / count

# Report the average water level 
print(f"The average preliminary water level is {average} ft.")

# Report the lowest and average water level 
print(f"The lowest water level is {low_float_preliminary} ft observed on {low_date} at {low_time}.")


# Problem 3
# Write a script (or Jupyter Notebook) that calculates the fastest rise in water level 
# per 6-minute period between measurements (for this assignment, 
# assume that each line of the dataset is a 6-minute interval) and 
# reports the date and time that was observed and the change in water level from the previous recording.

# Open the file
fhand = open('/blue/bsc4452/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv')

# Skip the header line
next(fhand)

# Set the variables
previous_preliminary = "None"
largest_difference_float_preliminary = 0

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
    
# Caluculate the total sum and count
    if not previous_preliminary == "None":
        difference_float_preliminary = float_preliminary - previous_preliminary
        
    
        if difference_float_preliminary > largest_difference_float_preliminary:
            largest_difference_float_preliminary = difference_float_preliminary
            date_rise = date
            time_rise = time
        previous_preliminary = float_preliminary

    else:
        previous_preliminary = float_preliminary 
        

# Report the fastest rise in water level 
print(f"The fastest rise in water level is {largest_difference_float_preliminary} ft on {date_rise} at {time_rise}.")

# Problem 4
# Imagine that the file is providing live readings of the water level. 
# Write a script (or Jupyter Notebook) to print a line of text with a warning if any of these events occur:
# * The water level increases more than 0.25 since the previous recording.
# * The water level is over 5.0.
# * No reading is received at a time point.

# Open the file
fhand = open('/blue/bsc4452/bsc4452/share/Class_Files/data/CO-OPS_8727520_wl.csv')

# Skip the header line
next(fhand)

# Set the variables
previous_level = None

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

# Report if there's no value
    if preliminary == '':
        print(f"No reading received at {date} {time}.")
        continue

# Report if the water level is over 5.0
    if float_preliminary > 5.0 :
        print(f"The water level is over 5.0 at {date}, {time}.")

# Report if the water level increases more than 0.25 since the previous recording
    if previous_level is not None and float_preliminary - previous_level > 0.25 :
        print(f"The water level increases more than 0.25 since the previous recording at {date}, {time}.")

# Set the previous water level
    previous_level = float_preliminary



