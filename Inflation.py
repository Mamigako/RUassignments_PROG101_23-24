text_file = input()


def open_file(text_file):
    try:
        return open(text_file)
    except FileNotFoundError:
        return None
    except IOError:
        return None

# Return tuple list.
def extract_lines(opened):
    output_list = []
    
    for line in opened:
        temp_list = line.split()
        floatment = None
        stringment = None
        tuplement = None
        for element in temp_list:
            try:
                floatment = float(element)
            except ValueError:
                stringment = element
            except TypeError:
                stringment = element
            if floatment == None:
                continue
            elif stringment == None:
                continue
            else:
                tuplement = stringment, floatment
                output_list.append(tuplement)
    
    opened.close()

    for line in output_list:
        print(line)

    return output_list

# Return tuple with year, low, top index.
def secondary_lines(output_list):

    tt_list = []    
    year_var = output_list[0][0][:-3]
    index_list = []
    
    for elements in output_list:

        if year_var in elements[0]:
            index_list.append(elements[-1])
            
        elif year_var not in elements:
            second_tuple = int(year_var), index_list[0], index_list[-1]
            tt_list.append(second_tuple)
            year_var = elements[0][:-3]
            index_list = []
            index_list.append(elements[-1])

    index_list.append(output_list[-1][-1])
    second_tuple = int(year_var), index_list[0], index_list[-1]
    tt_list.append(second_tuple)
    
    for line in tt_list:
        print(line)

    return tt_list

# Return inflation tuple.
def inflation(tt_list):

    inflation_list = []
    
    for element in tt_list:
        year = element[0]
        inflation_var = ((float(element[-1]) - float(element[-2])) / float(element[-2])) * 100
        inflation_var = round(inflation_var, 2)
        inflation_tuple = year, inflation_var
        inflation_list.append(inflation_tuple)

    for line in inflation_list:
        print(line)
        

def main(text_file):

    opened = open_file(text_file)
    
    if opened != None:
        output_list  = extract_lines(opened)
        tt_list = secondary_lines(output_list)
        inflation(tt_list)


main(text_file)
