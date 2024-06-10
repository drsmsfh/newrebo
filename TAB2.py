my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
target_value = 30

if target_value in my_dict.values():  # Check if value exists
  for key, value in my_dict.items():
    if value == target_value:
      print(key)
      break
else:
     print("Key not found")
