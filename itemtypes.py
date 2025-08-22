a = [1,1000,1]
r = 3
warehouse_list = a 
shelves_to_remove = r
shelf_list = a
warehouse_size = len(a)
item_type_dictionary={}

total_item_types = 0
best_item_types = 0
for item in warehouse_list:
    if str(item) in item_type_dictionary:
        item_type_dictionary[str(item)] += 1
    else:
        item_type_dictionary[str(item)] = 1
        total_item_types+=1

first_shelves_seen = shelf_list[:r]

for item in first_shelves_seen:
    item_type_dictionary[str(item)] -= 1
    if item_type_dictionary[str(item)] == 0:
        total_item_types -= 1
best_item_types = total_item_types

for i in range(warehouse_size-shelves_to_remove):
    item_type_dictionary[str(warehouse_list[i])] += 1
    if item_type_dictionary[str(warehouse_list[i])] == 1:
        total_item_types += 1
    
    item_type_dictionary[str(warehouse_list[i+shelves_to_remove])] -= 1

    if item_type_dictionary[str(warehouse_list[i+shelves_to_remove])] == 0:
        total_item_types -= 1

    if best_item_types < total_item_types:
        best_item_types = total_item_types

print(best_item_types)

