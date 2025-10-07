from collections import Counter

def validate_password(password):
    if not password:
        return "INVALID", None

    freq = Counter(password)

    # Check for any number appearing an odd number of times
    has_odd_count = any(count % 2 != 0 for count in freq.values())

    most_common = freq.most_common()
    max_freq = most_common[0][1]

    # Get all numbers tied with max frequency
    tied = [num for num, count in most_common if count == max_freq]
    smallest_most_frequent = min(tied)

    if has_odd_count:
        return "INVALID", smallest_most_frequent

    if len(tied) == 1:
        return "VALID", tied[0]
    else:
        return "INVALID", smallest_most_frequent

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    password = list(map(int, data[1:N+1]))  # Next N numbers
    
    # Call user logic function
    validation_result, most_frequent_element = validate_password(password)
    
    # Print the output
    print(validation_result)
    if most_frequent_element is not None:
        print(most_frequent_element)

if __name__ == "__main__":
    main()
