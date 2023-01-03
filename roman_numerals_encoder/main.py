def solution(n):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D",
                "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L",
            "LX", "LXX", "LXXX", "XC"]
    units = ["", "I", "II", "III", "IV", "V",
             "VI", "VII", "VIII", "IX"]
    result = ""
    split_number = list(str(n))
    if len(split_number) == 4:
        result += f"{thousands[int(split_number[0])]}{hundreds[int(split_number[1])]}" \
                  f"{tens[int(split_number[2])]}{units[int(split_number[3])]}"
    if len(split_number) == 3:
        result += f"{hundreds[int(split_number[0])]}{tens[int(split_number[1])]}" \
                  f"{units[int(split_number[2])]}"
    if len(split_number) == 2:
        result += f"{tens[int(split_number[0])]}{units[int(split_number[1])]}"
    if len(split_number) == 1:
        result += f"{units[int(split_number[0])]}"
    return result


print(solution(2911))

# https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python
