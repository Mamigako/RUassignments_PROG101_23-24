def main():
    file_name = input()
    text = read_file(file_name)
    for line in text:
        print("{:s}".format(line.strip()[::-1]))

def read_file(file_name):
     text = open(file_name, "r")
     return text


if __name__ == "__main__":
    main()
