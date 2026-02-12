#!/usr/bin/env python3

def main():
    nums = [2, 8, 9, 48, 8, 22, -12, 2]
    print(f"Original array: {nums}")
    new_nums = []
    for i in range(len(nums)):
        if (nums[i] > 5):
            new_nums.append(nums[i] + 2)
    print(f"New array: {new_nums}")

main()