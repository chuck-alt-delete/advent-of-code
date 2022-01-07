'''
Given a list of depth measurements, return the count of the number of times
a depth measurement increases from the previous measurement

To run:
python3 1.py 1.input 
'''
import sys

def countIncreases(file):
    count = 0
    with open(file) as f:
        linenum = 1
        previous = int(f.readline()) # moves cursor to next line
        for line in f:
            depth = int(line)
            linenum += 1
            if depth > previous:
                print(f"increase at line {linenum}")
                count += 1
            previous = depth
    return count

if __name__ == "__main__":
    print(countIncreases(sys.argv[1]))