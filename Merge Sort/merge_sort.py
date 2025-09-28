
# Input
a = [4,3,5,2,6,1,7,0]

def main():
    print(f"\n\nBefore sorting:\n{a}\n")

    # Sort
    merge_sort(0,len(a)-1)

    print(f"After sorting:\n{a}")

def merge_sort(l,r):
    global a
    
    # Base case
    if l == r:
        return
    
    # Divide
    mid = (l + r) // 2
    merge_sort(l,mid)
    merge_sort(mid+1,r)
    
    # Build temporary list
    size = r - l + 1
    sorted_list = [0] * size
    p = 0

    # Use 2 pointers to sort 2 halves
    i = l
    j = mid + 1
    while i <= mid and j <= r:
        if a[i] < a[j]:
            sorted_list[p] = a[i]
            i += 1
        else:
            sorted_list[p] = a[j]
            j += 1
        p += 1
        
    while i <= mid:
        sorted_list[p] = a[i]
        i += 1
        p += 1
        
    while j <= r:
        sorted_list[p] = a[j]
        j += 1
        p += 1
        
    print(f"{a}\n[{l}, {r}] -> {sorted_list}\n")
    for i in range(size):
        a[l + i] = sorted_list[i]
    print(f"{a}\n")

if __name__ == "__main__":
    main()