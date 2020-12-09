import sys
sys.setrecursionlimit(10000)


def single_character(regex, string):
    if regex == '.':
        return True
    elif regex == '':
        return True
    elif regex == string:
        return True
    else:
        return False


# matches string enclosed in ^ and $ exactly
# do i have to retype conditions for ?, *, + here with different recursive call?
def enclosed_match(regex, string):
    if regex == '' and string == '':
        return True
    elif regex == '' and string != '':
        return False
    elif string == '':
        return False
    if len(regex) > 1:
        if regex[1] == '.' and regex[0] == '\\':
            if string[0] == '.':
                return True
            else:
                return False
        if regex[1] in ('?', '*', '+', '\\') and regex[0] == '\\':
            return enclosed_match(regex[1:], string)
        elif regex[1] == '.' and regex[0] == '\\':
            return enclosed_match(regex, ('\\' + string))
        elif regex[1] == '?':
            return enclosed_match(regex[2:], string[1:]) or enclosed_match(regex[2:], string)
        elif regex[1] == '*':
            return enclosed_match(regex, string[1:]) or enclosed_match(regex[2:], string)
        elif regex[1] == '+':
            return enclosed_match(regex[2:], string[1:]) or enclosed_match(regex, string[1:]) \
                   and single_character(regex[0], string[0])
    if regex[0] in ('.', string[0]):
        return enclosed_match(regex[1:], string[1:])
    else:
        return False


# only looks at beginning of string for match
# this may be called several times with string[1:] from matching_strings to search in middle of string
def equal_string_match(regex, string):
    if regex == '':
        return True
    elif string == '':
        return regex == '$' or False
    if len(regex) > 1:
        if regex[1] == '.' and regex[0] == '\\':
            if string[0] == '.':
                return True
            else:
                return False
        if regex[1] in ('?', '*', '+', '\\') and regex[0] == '\\':
            return equal_string_match(regex[1:], string)
        elif regex[1] == '.' and regex[0] == '\\':
            return equal_string_match(regex, ('\\' + string))
        elif regex[1] == '?':
            return equal_string_match(regex[2:], string[1:]) or equal_string_match(regex[2:], string)
        elif regex[1] == '*':
            return equal_string_match(regex, string[1:]) or equal_string_match(regex[2:], string)
        elif regex[1] == '+':
            return equal_string_match(regex[2:], string[1:]) or equal_string_match(regex, string[1:]) \
                   and single_character(regex[0], string[0])
    if regex[0] in ('.', string[0]):
        return equal_string_match(regex[1:], string[1:])
    else:
        return False


# looks for a matching regex anywhere in a string
def matching_strings(regex, string):
    if regex == '':
        return True
    elif string == '':
        return False
    if equal_string_match(regex, string):
        return True
    else:
        return matching_strings(regex, string[1:])


# different conditions if string starts with ^, end with $, both, or neither
def start_match(regex, string):
    if regex.startswith('^') and regex.endswith('$') and regex[-2] != '\\':
        regex = regex[1:-1]
        if len(string) != len(regex) and not any(x in regex for x in ['?', '*', '+', '\\']):
            return False
        else:
            return enclosed_match(regex, string)
    elif regex.startswith('^'):
        regex = regex[1:]
        if equal_string_match(regex, string):
            return True
        else:
            return False
    elif regex.endswith('$') and regex[-2] != '\\':
        return matching_strings(regex, string)
    else:
        return matching_strings(regex, string)


def main():
    re, st = input().split('|')
    print(start_match(re, st))


if __name__ == "__main__":
    main()


# there are definitely some edge cases not encountered for in here
# hey this is super messy but i was going to give up and now i got it to work :D
