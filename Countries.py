import sys

COUNTRIES_OF_THE_WORLD = "countries.txt"
INPUT_PROMPT = "Enter a suffix for a country: "
Country_list = []

def read_file(text_file):
    return open(text_file, "r")

def get_suffix():
    # You can use stderr to display output in command line but not on Gradescope.
    sys.stderr.write(INPUT_PROMPT)
    return input()


def main():
    count = 0
    country_suffix = get_suffix()
    text = read_file(COUNTRIES_OF_THE_WORLD)

    for line in text:
        if line.strip().endswith(country_suffix):
            Country_list.append(line.strip())
            count += 1

    for country in Country_list:
        print(country)
        
    print(f"{count} countries with suffix {country_suffix} in total.")
    text.close()



# You might want to add some functions here, to break the program into smaller steps.




# -----------------------------------------------------------------------------------
# You'll often see the following two lines at the bottom of python files.
# This is a good way of setting up the program.
# It checks if this file is being run as the main program.
#
# Python modules have a special attribute called __name__,
# which indicates whether the file is being run as the main program,
# or being imported into another module.
#
# If it is being run, then its __name__ attribute will be "__main__".
# But if it is being imported, it's __name__ will be the name of the .py file.
#
# In case it is being imported, we don't want to run any functions, just import their names.
# But if it is being run, then we call the main() function to start the program.
if __name__ == "__main__":
    main()
