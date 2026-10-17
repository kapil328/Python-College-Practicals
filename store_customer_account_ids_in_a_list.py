
# Store customer account IDs in a list
ids = [101, 205, 310, 415, 520]

# Take customer ID from the user
key = int(input("Enter Customer ID: "))

# ---------- Linear Search ----------
if key in ids:
    print("Linear Search: ID Found")
else:
    print("Linear Search: ID Not Found")

# ---------- Binary Search ----------
low = 0
high = len(ids) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if ids[mid] == key:
        found = True
        break
    elif ids[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

# Display Binary Search result
if found:
    print("Binary Search: ID Found")
else:
    print("Binary Search: ID Not Found")
