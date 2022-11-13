# -----------------------------------------------------------------------------
# Двоичная система
# -----------------------------------------------------------------------------


# 0011 1111 (2) - 1 + 2 + 4 + 8 + 16 + 32 = 63 (10)

# 81 (10) - 101 0001 (2)
# 81 / 2 = 40.5 = 1
# 40 / 2 = 20 = 0
# 20 / 2 = 10 = 0
# 10 / 2 = 5 = 0
# 5 / 2 = 2.5 = 1
# 2 / 2 = 1 = 0
# 1

# 37 (10) - 00100101 (2)
# 37 / 2 = 18.5 = 1
# 18 / 2 = 9 = 0
# 9 / 2 = 4.5 = 1
# 4 / 2 = 2 = 0
# 2 / 2 = 1 = 0
# 1 <--

# 1010011010 (2) - 010 011 010 001 (2) = 2321 (8) = 1232 (8)
# 1010011010 (2)
# 1 010
def binary_to_octal(binary_number: str, limit: int = 3):
    octal_number = ''
    binary_number = binary_number[::-1]
    code_table = {
        '000': '0', '001': '1', '010': '2', '011': '3',
        '100': '4', '101': '5', '110': '6', '111': '7'
    }
    while binary_number != '':
        new_binary = binary_number[:limit][::-1]

        try:
            octal_number += code_table[new_binary]
        except KeyError:
            octal_number += code_table[
                '0' * (limit - len(binary_number)) + new_binary
            ]

        binary_number = binary_number[limit:]

    print(f"Octal number: {octal_number[::-1]}")


# 100 (8) - 001 000 000 (2)
def octal_to_binary(octal_number: str):
    binary_number = []
    is_error = False
    code_table = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'
    }
    for octal_char in octal_number:
        try:
            binary_number.append(code_table[octal_char])
        except KeyError:
            is_error = True
            print(f"Error octal number: {octal_char}")

    if not is_error:
        print(f"Binary number: {''.join(binary_number)}")


#def decimal_to_binary(decimal_number: int):
    binary_number = []
    while decimal_number != 1:
        binary_number.append(str(decimal_number % 2))
        decimal_number //= 2

    binary_number.append(str(decimal_number))
    binary_number.reverse()

    print(f"Binary number: {''.join(binary_number)}")
 def binary_to_decimal(binary_number: str):
    # 01101011 (2) - 1 + 2 + 8 + 32 + 64 - 107 (10)
    # 11010110 -> 1 -> 1 -> 0 ->
    step = 0
    decimal_number = 0
    binary_number = binary_number[::-1]
    for bin_char in binary_number:
        decimal_number += int(bin_char) * 2 ** step
        step += 1

    print(f"Decimal number: {decimal_number}")


if __name__ == "__main__":
    print("0 - Decimal to binary\n"
          "1 - Binary to decimal\n"
          "2 - Octal to binary\n"
          "3 - Binary to octal\n"
          "4 - Exit")
    while True:
        print('-' * 50)
        choice = input("Your choice: ")
        match choice:
            case '0':
                decimal_num = int(input("Decimal number: "))
                decimal_to_binary(decimal_num)
            case '1':
                binary_num = input("Binary number: ")
                binary_to_decimal(binary_num)
            case '2':
                octal_num = input("Octal number: ")
                octal_to_binary(octal_num)
            case '3':
                binary_num = input("Binary number: ")
                binary_to_octal(binary_num)
            case '4':
                break
            case _:
                print("Wrong choice")

# -----------------------------------------------------------------------------
# Восьмеричная система
# -----------------------------------------------------------------------------

# 000 (2) - 0 (8)
# 001 (2) - 1 (8)
# 011 (2) - 3 (8)
# 111 (2) - 7 (8)


# 611 (8) - 110 001 001 (2)

# 001000000 (2) - 000 000 001 (2) - 0 0 1 (8) - 100 (8)
# 1010011010 (2) - 010 011 010 001 (2) = 2321 (8) = 1232 (8)

# -----------------------------------------------------------------------------
# Шестнадцатиричная система система
# -----------------------------------------------------------------------------

# 19F (16) - 0001 1001 1111 (2) - 000 110 011 111 (2) - 0637 (8)
# - 1 + 2 + 4 + 8 + 16 + 128 + 256 - 415 (10)

# 666 (10) - 10 1001 1010 (2) - 010 011 010 001 (2) - 2321 - 1232(8)
# - 0010 1001 1010 (2) - 2910 (16) - 29A (16)
# 666 / 2 = 333 - 0
# 333 / 2 = 166.5 - 1
# 166 / 2 = 83 - 0
# 83 / 2 = 41.5 - 1
# 41 / 2 = 20.5 - 1
# 20 / 2 = 10 - 0
# 10 / 2 = 5 - 0
# 5 / 2 = 2.5 - 1
# 2 / 2 = 1 - 0
# 1

# 1010011010 (2) - 1010 1001 0010 - 1092 - A92 - 29A (16)
