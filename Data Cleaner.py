def clean_data(data):
    #step 1: Remove invalid values(None, empty string)
    filtered = [x for x in data if x not in (None, "")]
    #step 2: Remove duplicates while preserving order
    seen = set()
    unique = []
    for x in filtered:
        if x not in seen:
            seen.add(x)
            unique.append(x)
    #step 3: Sort final list
    sorted_list = sorted(unique)
    #step 4:Count removed values
    removed_count = len(data) - len(unique)
    return sorted_list, removed_count 
#Input 
data = [10,None,20, 10, "", 30, None, 40]
#Function call 
clean_list, removed = clean_data(data)
#Output
print("Clean List:", clean_list)
print("Removed Values Count:", removed)
