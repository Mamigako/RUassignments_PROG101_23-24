from submodule import extract_first_number_from_string

def main():
    
    run_like_hell_ehem_I_mean_run_like_samples()

    run_interactive()

def run_like_hell_ehem_I_mean_run_like_samples():
    search_string = input()
    first_number = extract_first_number_from_string(search_string)
    print(first_number)


def run_interactive():
    demand = "Numbers! Give me numbers! But hide them inside a string for me to find: "
    search_string = input(demand)

    first_number = extract_first_number_from_string(search_string)

    if first_number == -1:
        print("Hey! There is no number in this string >:(")
    else:
        print(f"Delicious! {first_number}, I see you!")


main()
