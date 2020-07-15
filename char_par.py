def digit_prop(symbol):
    symbol = ord(symbol)

    if not ((symbol >= ord('0')) and (symbol <= ord('9'))):
        return 'not a digit'

    symbol = symbol - '0'

    return 'odd' if symbol & 1 else 'even'
