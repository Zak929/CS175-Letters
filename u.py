# u.py

# U   U
# U   U
# U   U
# U   U
#  UUU
#   
#
def u(symbol, line):
    s = symbol
    line1 = (f'{s}   {s}')
    line2 = line1
    line3 = line1
    line4 = line1
    line5 = (f' {s}{s}{s} ')

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
        print( u('U', i) )
        

    
   

if __name__ == '__main__':
    main()


