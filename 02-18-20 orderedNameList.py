# Given an input of names as a list of strings, create another list that shortens each name using the following criteria:
# Use their first name only if no other person in the list shares a first name
# Use their first name + last initial if any other person in the list shares a first name, but does not share a last initial
# Use their full name if any other person in the list shares their first name + last initial
# input:
# [
#   "Jason Alexander",
#   "Megan Smith",
#   "Megan Fox",
#   "Jason Sudekis",
#   "Jason Avocado",
#   "Iris Kuhn"
# ]
# output (order is not important):
# [
#   "Jason Alexander",
#   "Megan S.",
#   "Megan F.",
#   "Jason S.",
#   "Jason Avocado",
#   "Iris"
# ]

# Check: first name unique -> first name only
# Check: if 1st name not unique, look for last name initial -> 
# Check: if 1st name not unique, last name's first initial not unique -> add entire name

#Empty list -> []
# "Jason Alexander".split(' ') -> [["Jason", "Alexander"], ["Megan", "Smith"], ["Megan", "Fox"]]

def OrderedNameList(nameList: list):

    splitNameList = [name.split(" ") for name in nameList]
   
    firstNameDict = {}      # This creates a dictionary to keep track of the number of first names
    for name in splitNameList:
        firstNameDict[name[0]] = firstNameDict.get(name[0], 0) + 1

    fnamelnameiniDict = {}      # This creates a dictionary with first name with last initial and count them, like {"Jason A.": 2, "Megan F.":1, }
    for name in splitNameList:
        fnamelnameiniDict[f"{name[0]} {name[1][0]}."] = fnamelnameiniDict.get(f"{name[0]} {name[1][0]}.", 0) + 1

    newList = []
    for name in splitNameList:
        if firstNameDict[name[0]] == 1:
            newList.append(name[0])
        elif fnamelnameiniDict[f"{name[0]} {name[1][0]}."] == 1:
            newList.append(f"{name[0]} {name[1][0]}.")
        else:
            newList.append(" ".join(name))

    return newList



def OrderedNameList1(nameList: list):

    splitNameList = [name.split(" ") for name in nameList]
   
    firstNameDict = {}      
    for name in splitNameList:      # find all first names as keys then add last initial as values -> {'Jason': ['A', 'S', 'A'], 'Megan': ['S', 'F'], 'Iris': ['K']}
        firstNameDict[name[0]] = firstNameDict.get(name[0], [])  # This will create an empty list for value if the name (key) doesn't exist
        firstNameDict[name[0]].append(name[1][0])

    newList = []
    for name in splitNameList:
        if len(firstNameDict[name[0]]) == 1:  # counting how many values associated with the key. If only 1 values found, eg. 'Iris': ['K']
            newList.append(name[0])
        elif  len(firstNameDict[name[0]]) >= 1 and firstNameDict[name[0]].count(name[1][0]) == 1: # if more than 1 values, then see if only one last initial
            newList.append(f"{name[0]} {name[1][0]}.")
        else:   # if it doesn't meet the above criteria
            newList.append(" ".join(name))

    return newList

print(OrderedNameList(["Jason Alexander", "Megan Smith", "Megan Fox", "Jason Sudekis", "Jason Avocado", "Siena Aguayo"]))
print(OrderedNameList1(["Jason Alexander", "Megan Smith", "Megan Fox", "Jason Sudekis", "Jason Avocado", "Siena Aguayo"]))
