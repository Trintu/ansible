#!/usr/bin/env python3
"""
Calculate mean and standard deviation based on the provided pseudocode
"""
import sys
import math

def mean(number_list):
    """
    mean(number_list) returns float  
    sum=0 
    for each number in number_list:  
        sum += number 
    return sum / length_of(number_list)
    """
    sum_val = 0
    for number in number_list:
        sum_val += number
    return sum_val / len(number_list)

def stddev(number_list, mean_val):
    """
    stddev(number_list, mean) returns float 
    sumofsquares = 0  
    for each number in number_list: 
        sumofsquares += (number - mean)^2  
    return square_root(sumofsquares/length_of(number_list))
    """
    sumofsquares = 0
    for number in number_list:
        sumofsquares += (number - mean_val) ** 2
    return math.sqrt(sumofsquares / len(number_list))

def main():
    # Read numbers from stdin
    number_list = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                number_list.append(float(line))
            except ValueError:
                continue
    
    if not number_list:
        print("Error: No valid numbers found")
        sys.exit(1)
    
    # Calculate mean
    mean_val = mean(number_list)
    
    # Calculate standard deviation
    stddev_val = stddev(number_list, mean_val)
    
    # Output results
    print(f"Count: {len(number_list)}")
    print(f"Mean: {mean_val:.2f} ms")
    print(f"Standard Deviation: {stddev_val:.2f} ms")
    print(f"Min: {min(number_list):.2f} ms")
    print(f"Max: {max(number_list):.2f} ms")

if __name__ == "__main__":
    main()
