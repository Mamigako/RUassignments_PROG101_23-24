def main():
    
    """A function that reads in names of Javelin throwers and outputs their recorded throws 
    along with the athlete with the highest average in the end."""

    try:
        filename = input()

        file_stream = open_file(filename)

        throw_dict = make_dictionary(file_stream)

    except TypeError:
        return

    print_throws(throw_dict)

    print(find_highest_average(throw_dict))


def open_file(filename):

    try:
        file_stream = open(filename)
    
        return file_stream
    
    except FileNotFoundError:
        return None
    except TypeError:
        return None
    
def make_dictionary(file_stream):

    throw_dict = {}

    for line in file_stream:
    
        if line.strip().split(" ")[0] + " " + line.strip().split(" ")[1] not in throw_dict:
            throw_dict[line.strip().split(" ")[0] + " " + line.strip().split(" ")[1]] = [line.strip().split(" ")[2]]
        else:
            throw_dict[line.strip().split(" ")[0] + " " + line.strip().split(" ")[1]].append(line.strip().split(" ")[2])
    
    return throw_dict
        
def print_throws(throw_dict):

    for key in throw_dict:
        
        val_string = ""

        for value in throw_dict[key]:
            val_string += value + " "
        
        print("{:<20}".format(key)+f"Throws: {val_string}")


def find_highest_average(throw_dict):

    high_dict = {}
    for key in throw_dict:
        if len(throw_dict[key]) > 1:
            average = 0
            count = 0
            for value in throw_dict[key]:
                average += float(value)
                count += 1
            high_dict[key] = average/count

  
    # Outputting the highest average.
    maxval = 0
    maxkeyvalpair = ""
    for key in high_dict:
        if high_dict[key] > maxval:
            maxval = high_dict[key]
            maxkeyvalpair = key + ": " + str(round(high_dict[key], 2))
        
            
    return maxkeyvalpair



if __name__ == "__main__":
    main()
    