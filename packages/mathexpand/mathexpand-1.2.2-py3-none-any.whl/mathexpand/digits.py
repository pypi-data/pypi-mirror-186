def take_digits(number, return_type="l"):
    digits_list = list()
    digits_dict = {}
    temp = number

    for _ in range(len(str(number)) - 1):
        divisor = int("1" + (len(str(temp))-1) * "0")
        digits_list.append(int((temp - temp % divisor) / divisor))
        digits_dict[divisor] = int((temp - temp % divisor) / divisor)

        temp = temp % divisor

    digits_list.append(temp)
    digits_dict[1] = temp

    if return_type=="l":
        return digits_list
    elif return_type=="d":
        return digits_dict
    else:
        print("math-expand error(digits→take_digits):请传递正确的return_type实参(Please pass the correct return_type argument)")
        return digits_list

# print(take_digits(23532))
# print(take_digits(36483, "l"))
# print(take_digits(32543, "d"))
# print(take_digits(24325, "abc"))