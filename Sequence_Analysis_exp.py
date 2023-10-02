# Stat module for stat.median()
import statistics
text_file = input()
seq_list = []



 # Read file
try:
    opened = open(text_file, "r")
except FileNotFoundError:
    None
except IOError:
    None



# Validate elements in file.
def validate(opened):
    for line in opened:
        try:
            seq_list.append(float(line))
        except ValueError:
            continue    
    return seq_list

# Print element sequence.
def number_sequence(seq_list):
        count = 0
        vount = 0
        for element in seq_list:
            count += 1

        for element in range(count - 1):
            print((round(seq_list[vount], 4)),end=" ")
            vount += 1 
        
        try:
            print(round(seq_list[-1], 4))
        except IndexError:
            return

# Print element sum sequence.         
def sequence_sum(seq_list):
        temp_list = []
        count = 0
        vount = 0

        for element in seq_list:
            count += 1
        
        for element in range(count - 1):
            temp_list.append(seq_list[vount])
            print(round(sum(temp_list), 4), end=" ")
            vount += 1 
        
        try:
            temp_list.append(seq_list[-1])    
        except IndexError:
            return
        print(round(sum(temp_list), 4))

# Print sorted element sequence.
def sorted_sequence(seq_list):
    count = 0
    vount = 0
    seq_list = sorted(seq_list)
 
    for element in seq_list:
        vount += 1

    for element in range(vount - 1):
        print(round(seq_list[count], 4), end=" ")
        count += 1
    
    try:
        print(round(seq_list[-1], 4))
    except IndexError:
        return

# Print median value of sequence.
def median_in_sequence(seq_list):
    try:
        median_var = statistics.median(seq_list)
        median_var = round(float(median_var), 4)
        print(median_var)
    except statistics.StatisticsError:
        return seq_list
    
def main():
    validate(opened)
    number_sequence(seq_list)
    sequence_sum(seq_list)
    sorted_sequence(seq_list)
    median_in_sequence(seq_list)

main()

opened.close()