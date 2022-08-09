#%%
""" -----------------------------------
    Copy using = operator
    creates a new variable
     that shares the reference of the original object
    both have same ID
"""
old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 'a']]
new_list = old_list

new_list[2][2] = 9

print('Old List:', old_list)
print('ID of Old List:', id(old_list))

print('New List:', new_list)
print('ID of New List:', id(new_list))


#%%
""" -----------------------------------
    DEEP Copy using copy.deepcopy() 
    A deep copy creates a new object
    independent copy of original object
     and all its nested objects
    both have different id
"""
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)
old_list[0]=[0,0,0]
print("Old list:", old_list,"\n ID :",id(old_list))
print("New list:", new_list,"\n ID :",id(new_list))


# %%
""" -----------------------------------
    SHALLOW COPY using copy.copy()
    both have different id
"""
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)
print("ID :",id(old_list[0]))
old_list[0][1]=[0,0,0]
print("ID :",id(old_list[0]))
old_list.append([4,4,4])
print("Old list:", old_list,"\n ID :",id(old_list))
print("New list:", new_list,"\n ID :",id(new_list))



# %%
