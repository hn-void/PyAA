def extract_aa(num, aa_list, from_left=True):
    extracted_aa = []
    for aa in aa_list:
        if from_left:
            extracted_aa.append(aa[:num])
        else:
            if num == 0:
                extracted_aa.append('')
            else:
                extracted_aa.append(aa[-num:])
    return extracted_aa


def set_font_color_red():
    print('\033[31m', end='')


def set_font_color_green():
    print('\033[32m', end='')


def set_font_color_blue():
    print('\033[34m', end='')


def reset_font_change():
    print('\033[39m', end='')


def animation_with_2(counter: int, frequency: int, aa_1: list, aa_2: list):
    if counter % frequency < frequency / 2:
        return aa_1
    else:
        return aa_2
