def tuple_to_list(tuple_input):
    return list(tuple_input)


tuple_data = (1,2,3,4,5)
list_data = tuple_to_list(tuple_data)
print("Tuple:", tuple_data)
print("List:", list_data)