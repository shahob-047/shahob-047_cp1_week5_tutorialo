 # values = [4, 5, 8]  index = 1  new_value = 11
def replace_value(values, index, new_value): 
    values[index] = new_value

 # values = [4, 5, 8, 11]  target = 11
def find_first(values, target):
    for i in range(len(values)): # index bo'yicha olish
        if values[i] == target:
            return i
    return -1  # targetga teng qiymat bo'lmasa listda

def summarize(values): 
    return (min(values), max(values), sum(values))


days = int(input("Enter the number of days: "))

original = []
for i in range(days): 
    practice_time = int(input("Enter typing practice time in minutes: "))
    original.append(practice_time)

updated = original[:]

index = int(input("Enter the index to correct: "))
new_practice_time = int(input("Enter the new practice time: "))

replace_value(updated, index, new_practice_time)

target = int(input("Enter the practice time to search for: "))

target_index = find_first(updated, target)

target_count = updated.count(target)

minimum, maximum, total = summarize(updated)  # tuple unpacking 

sorted_updated = sorted(updated)



print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_updated}")
print(f"Minimum practice time: {minimum} minutes")
print(f"Maximum practice time: {maximum} minutes")
print(f"Total practice time: {total} minutes")

if target_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {target_index}")

print(f"Matching values: {target_count}")
