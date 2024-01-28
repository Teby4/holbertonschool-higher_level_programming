#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0")
    else:
        total_sum = 0
        for i in range(1, argc + 1):
            total_sum += int(sys.argv[i])

        print(total_sum)
