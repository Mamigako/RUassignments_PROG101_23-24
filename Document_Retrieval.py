import string
Quit_Prompt = "quit"

def main():

    text_file = input()
    

    try:
        long_strings = open_and_read(text_file)
   
    except FileNotFoundError:
        return
    

    doc_dict = create_dict(text_file)

    search_or_print_prompt = input()


    while search_or_print_prompt != Quit_Prompt:

        if search_or_print_prompt == "search": 
            
            word = input()
            
            try:
                search_for_words(word, doc_dict)
            
            except ValueError:
                print("No match")


        elif search_or_print_prompt == "print":
            
            doc_num = input()

            try:
                print_doc(doc_num, long_strings)
            
            except ValueError:
                print("No match")
        
        search_or_print_prompt = input()




def open_and_read(text_file):

    doc_list = []
    
    with open(text_file) as file:
        doc_line = ""
    
        for line in file:
            line = line.strip()
            if "<END OF DOCUMENT>" not in line:

                doc_line += line + "\n"
            
            else:
                doc_list.append(doc_line)
                doc_line = ""
                continue
    
    return doc_list


def create_dict(text_file):

    doc_dict = {}
    doc_index = 1
    
    with open(text_file) as file:
    
        for line in file:
            line = line.strip()
            line = line.strip("\n")

            if line == "<END OF DOCUMENT>":
                doc_index += 1
                continue
    
            for word in line.split():
                
                word = word.strip(string.punctuation).lower()
                
                if word in doc_dict:
                    doc_dict[word].add(str(doc_index))
                else:
                    doc_dict[word] = set(str(doc_index))

    return doc_dict


def search_for_words(word, doc_dict):
    
    doc_intersect = set()
    
    for el in word.split():
        
        if el.lower() not in doc_dict:
            print("No match")
            return
        
        doc_intersect = doc_dict[el].intersection(doc_dict[el])
    
    if doc_intersect == False:
        print("No match")
    else:
        print(f"Documents matching search: {' '.join(map(lambda x: str(x), sorted(doc_intersect)))}")


def print_doc(doc_num, long_strings):
    
    if not doc_num.isdigit():
        print("No match")
        return
    elif int(doc_num) <= 0:
        print("No match")
        return    
    
    else:

        if len(long_strings) < int(doc_num): 
            print("No match")
            return
        else:
            print(f"Document #{doc_num}:")
        

        print(long_strings[int(doc_num)-1])
    


main()
