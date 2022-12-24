import re


def to_camel_case(text):
    regex = r'_|-'
    text_list = re.split(regex, text)
    for i in range(len(text_list) - 1):
        text_list[i + 1] = text_list[i + 1].capitalize()
    return "".join(text_list)


string = to_camel_case("the-stealth_warrior")
print(string)
