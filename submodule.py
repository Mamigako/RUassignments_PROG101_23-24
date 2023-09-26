def decimal_to_binary(decimal: int) -> str:
    """Converts an integer from decimal to its binary representation."""
    bin_string = ""

    while decimal // 2 != 0:

        remainder = decimal % 2
        bin_string += str(remainder)
        decimal = decimal // 2
    if decimal // 2 == 0:
        bin_string += (str(decimal % 2))
    return bin_string[::-1]