# Python3 implementation of the approach 

# Function to return the count of 
# all distinct valid elements 
def countOccurrence(n, arr, k) :

    ans = 0; 

    # To avoid duplicates 
    hash = dict.fromkeys(arr,0); 

    # To store the count of arr[i] 
    # in range [i + 1, n - 1] 
    occurrence = dict.fromkeys(arr, 0); 

    for i in range(n - 1, -1, -1) :

        # To avoid duplicates 
        if (hash[arr[i]] == True) :
            continue; 

        # If occurrence in range i+1 to n 
        # becomes equal to K then increment
        # ans by 1 
        if (occurrence[arr[i]] >= k) :
            ans += 1; 
            hash[arr[i]] = True; 
        
        # Otherwise increase occurrence 
        # of arr[i] by 1 
        else :
            occurrence[arr[i]] += 1; 
    
    return ans; 

# Driver code 
if __name__ == "__main__" :

    arr = [1, 7, 4, 3, 4, 8, 7]
    n = len(arr) 
    k = 2
    print(countOccurrence(n, arr, k)); 

# This code is contributed by Ryuga