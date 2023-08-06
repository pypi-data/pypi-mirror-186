from reactivecli.utils.formats import formats


def __check_and_change(field, string, item):

    for _item in formats[field].keys():
        if item == _item:
            return f"{formats[field][item]}{string}{formats['reset']}"

    return string


def color(string: str, color: str):
    return __check_and_change('colors', string, color)


def background(string: str, color: str):
    return __check_and_change('backgrounds', string, color)


def decoration(string: str, decoration: str):
    return __check_and_change('decorations', string, decoration)


def error(string: str):
    if len(string) > 0:
        error_label = "╔ERROR---╗\n║ @@@    ║\n╚═════---╝".replace(
            "---", "═" * len(string)).replace("@@@", string)
        return color(error_label, "red")
    return string
