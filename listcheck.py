# Travel Packing List and Selection
packing_list = ['clothes', 'toothbrush', 'passport', 'camera']
item_to_check = str(input())

# TODO: Write a line of code to check if the item_to_check is in the packing_list
if item_to_check in packing_list:
    print("item present: " + str(item_to_check))
    index = packing_list.index(item_to_check)
    print(index)
else:
    print(f" str(item_to_check) not present")
    packing_list.append(item_to_check)
    print("new list: " + str(packing_list))