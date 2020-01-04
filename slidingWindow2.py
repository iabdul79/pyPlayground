def sampling(arr, d):
    l = len(arr)
    parts = l//d
    ai = [i * d for i in range(parts)]
    # a0, a1, a2, a3 = 0, l//4, l//2, 3*l//4
    max_arr = [max(arr[i:i+d]) for i in ai]
    return min(max_arr)

def cal2(arr,d):
    l = len(arr)
    current_max = max(arr[:d])
    final_min_max = sampling(arr, d)
    for i in range(1, l-d+1):
        remove = arr[i-1]
        addin = arr[i+d-1]
        if addin >= final_min_max:
            i = i + d
            current_max = addin
            continue
        
        if remove < current_max: 
            continue

        if remove == current_max:
            current_max = max(arr[i:i+d])

        final_min_max = min(final_min_max, current_max)
    return final_min_max
    
# Complete the solve function below.
def solve(arr, queries):
    return [cal2(arr,d) for d in queries]