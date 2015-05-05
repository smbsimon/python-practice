def hey(what):
    what = what.strip()

    if not what:
        return 'Fine. Be that way!'
    elif what.isupper():
        return 'Woah, chill out!'
    elif what.endswith('?'):
        return 'Sure.'
    else:
        return "Whatever."
