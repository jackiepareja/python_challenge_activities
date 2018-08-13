# Write a loop to print all elements in hourly_temperature.
# Separate elements with a -> surrounded by spaces. Sample output for the given program:

hourly_temperature = [90, 92, 94, 95]
# Creates a new list to append the items with the arrows.
new_list = []
arrow = '->'
# Add an arrow for every odd index place.
# First print their index place
# Use an if statement to add the arrow after every even index place.

# prints the index place and the hour object
for hour in hourly_temperature:
    # for each hour iterates
    new_list.append(hour)
    # for each arrow iterates
    new_list.append(arrow)

# removes the last index item of the list.
new_list.pop(-1)
# print(new_list)

# iterates over the new list to print out without the quotations
for item in new_list:
    print(item, end=" ")



hourly_temperature = [90, 92, 94, 95]

new_list = []
arrow = '->'

for hour in hourly_temperature:
    new_list.append(hour)
    new_list.append(arrow)

new_list.pop(-1)

for i in new_list:

    print(i, end=' ')
