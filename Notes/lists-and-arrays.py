wells= ["A1", "A2", "A3", "B1", "B2", "B3"]


print(wells[2])

# calling a function, that's ( )
# index is [ ]

wells=[]
print(wells)
wells.append("A1")
print(wells)
wells.append("A2")
print(wells)
# get a specific well, A2
print(wells[1])

wells.extend(["A3", "B1", "B2", "B3"])
print(wells)
# remove by index value, use pop
wells.pop(0)
print(wells)
