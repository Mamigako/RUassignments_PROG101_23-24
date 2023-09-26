def main():
    num1_str = input()
    num2_str = input()

    result = divide_safe(num1_str, num2_str)
    print(result)


def divide_safe(num1_str, num2_str):
    """Returns num1/num2 if the input is valid, else None."""
    try: 
        num1_str, num2_str = float(num1_str), float(num2_str)
    except ValueError:
        return None
    try:
        result = num1_str/num2_str
        return round(result, 5)
    except ZeroDivisionError:
        return None


if __name__ == "__main__":
    main()
