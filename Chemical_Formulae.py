from typing import Tuple

UI = False


def main():
    formula_1, formula_2 = get_formulae()

    chemical_set_1 = get_chemicals_in_formula(formula_1)
    chemical_set_2 = get_chemicals_in_formula(formula_2)

    state_common_chemicals(chemical_set_1, chemical_set_2)


def get_formulae(user_interface: bool = UI) -> Tuple[str]:
    """Asks the user for two chemical formulae, and returns them."""

    formula_1 = input("Enter a chemical formula:\n" if user_interface else "")
    formula_2 = input("Enter another chemical formula:\n" if user_interface else "")

    return formula_1, formula_2


def get_chemicals_in_formula(chemical_formula: str) -> set:
    """Returns the set of element found in the formula."""

    formula_list = []
    for char in range(len(chemical_formula)):
        
        if not chemical_formula[char].islower():
            if not chemical_formula[char].isdigit():
                try:
                    if chemical_formula[char+1].islower():
                        formula_list.append(chemical_formula[char]+ chemical_formula[char+1])
                    else:
                        formula_list.append(chemical_formula[char])
                except IndexError:
                    if not chemical_formula[char].isdigit():
                        if not chemical_formula[char].islower():
                            formula_list.append(chemical_formula[char])




    formula_set = set(formula_list)
    return formula_set


def state_common_chemicals(chemical_set_1: set, chemical_set_2: set) -> None:
    """Prints the chemicals common to both sets, in alphabetical order."""

    common_chemicals = chemical_set_1.intersection(chemical_set_2)
    for element in sorted(common_chemicals):
        if len(sorted(common_chemicals)) == 1:
            print(element)
            break
        elif element == sorted(common_chemicals)[-1]:
            print(element)
        else:
            print(element + ",", end=" ")


if __name__ == "__main__":
    main()
