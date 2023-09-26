def main():
    file_name = input()
    text = read_file(file_name)

    for line in text:
        new_linez = ""
        line = line.strip().split()
        reversed_words = [word[::-1] for word in line]
        new_linez = " ".join(reversed_words)
        print(new_linez)

def read_file(file_name):
     text = open(file_name, "r")
     return text


if __name__ == "__main__":
    main()
