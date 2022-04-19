# j.py
# CS175
# spring


'''
    J
    J
    J
J   J
 JJJ
'''

def j(symbol, line):
    s = symbol
    line1 = f'    {s}'
    line2 = line1
    line3 = line1
    line4 = f'{s}   {s}'
    line5 = f' {s}{s}{s}'

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
        return 'invalid line'
    
# tast code
def main():

    print(j('J', 1))
    print(j('J', 2))
    print(j('J', 3))
    print(j('J', 4))
    print(j('J', 5))
    print()
    

if __name__ == '__main__':
    main()
