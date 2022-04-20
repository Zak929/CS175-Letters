# Zak Ahmed
# r.py

# RRRR
# R   R
# RRRR
# R  R
# R   R

def r(symbol, line):
    s = symbol
    # five lines that form Z
    line1 = s * 4
    line2 = f'{s}   {s}'
    line3 = line1
    line4 = f'{s}  {s}'
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
    print(r('R',1))
    print(r('R',2))
    print(r('R',3))
    print(r('R',4))
    print(r('R',5))

if __name__ == '__main__':
    main()
