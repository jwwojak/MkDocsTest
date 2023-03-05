wells=[["A1", "A2","A3"],["B1","B2","B3"]]
print(wells)
[['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(wells[1])
['B1', 'B2', 'B3']
print(wells[0])
['A1', 'A2', 'A3']
print(wells[1][1])
B2
wells=[]
print(wells)
[]
wells.append("A1")
print(wells)
['A1']
wells.append("A2)
             
SyntaxError: incomplete input
wells.append("A2")
             
print(wells)
             
['A1', 'A2']
print(wells[1])
             
A2

# What I want to do is pass label value to a well.

# This uses via load_label.
