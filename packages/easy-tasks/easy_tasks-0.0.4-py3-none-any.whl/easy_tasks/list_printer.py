from copy import deepcopy
from varname import nameof
from colorful_terminal import *


def pretty_print_list(
    List: list,
    print_list_name: bool = True,
    colored: bool = True,
    name_rgb=(255, 175, 0),
    value_rgb=(0, 255, 255),
    syntax_rgb=(200, 200, 200),
):
    if colored:
        n_color = Fore.rgb(*name_rgb)
        v_color = Fore.rgb(*value_rgb)
        s_color = Fore.rgb(*syntax_rgb)
        reset = Fore.RESET
    else:
        n_color = ""
        v_color = ""
        reset = ""
        s_color = ""
    if print_list_name:
        try:
            list_name = nameof(List, frame=2)
        except:
            list_name = "<name of list not found>"
        name = n_color + list_name + reset + s_color + " = [\n" + reset
        spacer = "\t"
    else:
        name = ""
        spacer = ""
    len_list = len(List)
    for i, v in enumerate(List):
        v = repr(v)
        ink = f"{spacer}{v_color}{v}{reset}"
        if i != len_list - 1 and print_list_name:
            ink += s_color + "," + reset
        name += ink + "\n"
    if print_list_name:
        name += s_color + "]" + reset
    colored_print(name)


def pretty_print_nested_list(
    List: list[list],
    print_list_name: bool = True,
    colored: bool = True,
    name_rgb=(255, 175, 0),
    value1_rgb=(0, 255, 255),
    value2_rgb=(255, 255, 0),
    syntax_rgb=(200, 200, 200),
):
    try:
        name = nameof(List, frame=2)
    except:
        name = "<name of list not found>"
    if colored:
        n_color = Fore.rgb(*name_rgb)
        v1_color = Fore.rgb(*value1_rgb)
        v2_color = Fore.rgb(*value2_rgb)
        s_color = Fore.rgb(*syntax_rgb)
        reset = Fore.RESET
    else:
        n_color = ""
        v1_color = ""
        v2_color = ""
        reset = ""
        s_color = ""
    vcols = (v1_color, v2_color)
    spacer = "\t"

    data = List
    padding = 1

    if len(data) == 0:
        raise ValueError("List is empty!")
    dataset = deepcopy(data)
    row_lenghts = []
    for row in dataset:
        row_lenghts.append(len(row))
    cols = max(row_lenghts)
    for row in dataset:
        while len(row) < cols:
            row.append("")
    col_widths = []
    for i in range(cols):
        col = [row[i] for row in dataset]
        col_width = max(len(str(word)) for word in col) + padding  # padding
        col_widths.append(col_width)
    s = ""
    if print_list_name:
        s += n_color + name + reset + " = [\n"
    len_data = len(dataset)
    for row_index, row in enumerate(dataset):
        len_row = len(row)
        if print_list_name:
            s += spacer
        s += s_color + "[" + reset

        for index, word in enumerate(row):
            str_word = str(word)
            if type(word) == str:
                str_word = "'" + str_word + "'"
            if str_word != "''":
                if index != len_row - 1 and not all(
                    [w == "" for w in row[index + 1 :]]
                ):
                    str_word += s_color + "," + reset
                s += (
                    vcols[index % 2]
                    + str_word
                    + "".ljust(-len(str(word)) + col_widths[index])
                    + reset
                )

        s += s_color + TermAct.Cursor_Back + "]" + reset
        if row_index != len_data - 1:
            if print_list_name:
                s += s_color + "," + reset
            s += "\n"
    if print_list_name:
        s += s_color + "\n]" + reset
    colored_print(s)
