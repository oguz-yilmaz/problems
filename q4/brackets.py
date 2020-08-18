def is_properly_closed(bracket_string):
    if not bracket_string:
        return false

    bracket_stack = []
    opened = ['(', '{', '[']
    closed = [')', '}', ']']

    for item in bracket_string:
        if item in opened:
            bracket_stack.append(item)
        elif item in closed:
            if not len(bracket_stack):
                return False
            else:
                if opened.index(bracket_stack.pop()) != closed.index(item):
                    return False
        else:
            return False

    return True


print(is_properly_closed("{[]}"))
print(is_properly_closed("{(])}"))
print(is_properly_closed("{([)]}"))
