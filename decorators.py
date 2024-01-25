def make_bold(func):
    def wrapper(*args):
        return "<b>" + func(*args) + "</b>"

    return wrapper

def make_emphasis(func):
    def wrapper(*args):
        return "<em>" + func(*args) + "</em>"

    return wrapper


def make_underlined(func):
    def wrapper(*args):
        return "<u>" + func(*args) + "</u>"

    return wrapper


def make_heading(func):
    def wrapper(*args):
        if args:
            return f"<h{args[0]}>" + func(*args) + f"</h{args[0]}>"
        else:
            return "<h1>" + func(*args) + "</h1>"

    return wrapper