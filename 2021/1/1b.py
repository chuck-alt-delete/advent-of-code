'''
--- Part Two ---

Considering every single measurement isn't as useful as you expected: there's just too much noise in the data.

Instead, consider sums of a three-measurement sliding window.
'''

import sys

def countIncreasesWindowed(file):

    depths = []
    count = 0

    with open(file) as f:
        for line in f:
            depths.append(int(line))
    
    for i in range(len(depths) - 3):
        current_window = depths[i+1:i+4]
        previous_window = depths[i:i+3]
        if sum(current_window) > sum(previous_window):
            count += 1

    return count

if __name__ == "__main__":
    print(countIncreasesWindowed(sys.argv[1]))