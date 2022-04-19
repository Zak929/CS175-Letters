#Julianna rubinetti
#P.py
#CS-501A
def g(symbol, line):
    s = symbol
    line1 = s*5
    line2 = (f'{s}')
    line3 = line1
    line4 = (f'{s}   {s}')
    line5 = line1

    if line == 1:
        return line1
    elif line == 2:
        return line2
    elif line == 3:
        return line3
    elif line == 4:
        return line4
    elif line == 5:
        return line5

    else:
        return 'Invalid Line'


def main():
    print(g('G', 1))
    print(g('G', 2))
    print(g('G', 3))
    print(g('G', 4))
    print(g('G', 5))


if __name__ == '__main__':
    main()
