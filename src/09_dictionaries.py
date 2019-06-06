"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with 
lists!). 

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    }, 
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    }, 
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
new_waypoint = {
    "lat": 40,
    "lon": -120,
    "name": "a fourth place"
}

waypoints.append(new_waypoint)

# print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# YOUR CODE HERE
waypoint_change = {
    "lon": -130, 
    "name": "not a real place"
}

for waypoint in waypoints:
    if waypoint["name"] == "a place":
        waypoint.update(waypoint_change)

# print(waypoints)

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
for waypoint in waypoints:
    for key, value in waypoint.items():
        print(key + ":", value)


# Better way from Yanrong:
# for i in waypoints:
#     print("lat:", i["lat"], "lon", i["lon"], "name", i["name"])

        