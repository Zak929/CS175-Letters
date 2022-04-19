# y.py

# 
# Y   Y
#  Y Y
#   Y 
#   Y
#   Y 
#    
#
def y(symbol, line):
    s = symbol
    line1 = f'{s}   {s}'
    line2 = f' {s} {s}'
    line3 = f'  {s}'
    line4 = line3
    line5 = line3

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
    for i in range(1, 6):
        print(y('Y', i))
        
main()
