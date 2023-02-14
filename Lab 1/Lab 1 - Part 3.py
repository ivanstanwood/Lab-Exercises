#Today, were gonna be reviewing dictionaries. Put simply, dictionaries allow you to
#pair up a VALUE with a KEY, and the values and keys within a dictionary can be accessed
#and changed.

sample_dictionary = {'1': 'one', '2': 'two', '3': 'three', '4': 'four'}   #Here, we assigned a dictionary to the variable "sample_dictionary"
print(sample_dictionary)

#We can do alot of things with dictionaries, here I will show some built-in functions.

def pop_function(dictionary):  #This function "pops" the element of the specified key
    dictionary.pop('1')
    return dictionary

def get_function(dictionary):        #This function gives the value of the specified key
    dic_value = dictionary.get('2')
    return dic_value

def keys_function(dictionary):     #This function gives a complete list of the keys within the dictionary
    dic_value = dictionary.keys()
    return dic_value

def update_function(dictionary):
    new_key = {'5': 'five'}            #This function updates the dictionary with whatever key-value pair you input
    updated_dic = dictionary.update(new_key)
    return updated_dic

print("")
print(update_function(sample_dictionary))