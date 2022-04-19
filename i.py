# i.py
# CS175
# spring


'''
IIIII
  I
  I
  I
IIIII
'''

def i(symbol, line):
    s = symbol
    line1 = s*5
    line2 = f'  {s}'
    line3 = line2
    line4 = line2
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
        return 'invalid line'
    
# tast code
def main():

    print(i('I', 1))
    print(i('I', 2))
    print(i('I', 3))
    print(i('I', 4))
    print(i('I', 5))
    print()
    

if __name__ == '__main__':
    main()
