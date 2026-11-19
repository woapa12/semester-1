# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["York"] = "Ouse"
rivers["Manchester"] = "Irk"

print(rivers)

# Display all the keys
for i in rivers:
    print(i)
# Display all the values
for i in rivers.values():
    print(i)

# Display all the key:value pairs, as tuples
for i, j in rivers.items():
    print((i,j))

# Delete an entry from the rivers database
rivers.pop("Manchester")
print(rivers)