# t.py

# TTTTT
#   T 
#   T
#   T 
#   T
#   
#
def t(symbol, line):
    s = symbol
    line1 = s*5
    line2 = f'  {s}'
    line3 = line2
    line4 = line2
    line5 = line2

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
        return "invalid line"


def main():
    for i in range(1,6):
        print( t('T', i) )
        

    
   

if __name__ == '__main__':
    main()

