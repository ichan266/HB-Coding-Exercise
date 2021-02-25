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

# Empty list -> []
# "Jason Alexander".split(' ') -> [["Jason", "Alexander"], ["Megan", "Smith"], ["Megan", "Fox"]]

def OrderedNameList(nameList: list):

    splitNameList = [name.split(" ") for name in nameList]

    # This creates a dictionary to keep track of the number of first names
    firstNameDict = {}
    for name in splitNameList:
        fname = name[0]
        firstNameDict[fname] = firstNameDict.get(fname, 0) + 1

    # This creates a dictionary with first name with last initial and count them, like {"Jason A.": 2, "Megan F.":1, }
    fnamelnameiniDict = {}
    for name in splitNameList:
        fname, lini = name[0], name[1][0]
        fnamelnameiniDict[f"{fname} {lini}."] = fnamelnameiniDict.get(
            f"{fname} {lini}.", 0) + 1

    newList = []
    for name in splitNameList:
        fname, lini = name[0], name[1][0]
        if firstNameDict[fname] == 1:
            newList.append(fname)
        elif fnamelnameiniDict[f"{fname} {lini}."] == 1:
            newList.append(f"{fname} {lini}.")
        else:
            newList.append(" ".join(name))

    return newList


def OrderedNameList1(nameList: list):

    splitNameList = [name.split(" ")
                     for name in nameList]  # -> ["Jason", "Avocado"]

    firstNameDict = {}
    # find all first names as keys then add last initial as values -> {'Jason': ['A', 'S', 'A'], 'Megan': ['S', 'F'], 'Iris': ['K']}
    for name in splitNameList:
        # This will create an empty list for value if the name (key) doesn't exist
        fname, lini = name[0], name[1][0]
        firstNameDict[fname] = firstNameDict.get(fname, [])
        firstNameDict[fname].append(lini)

    newList = []
    for name in splitNameList:
        # counting how many values (last initial) associated with the key (first name). If only 1 values found, eg. 'Iris': ['K']
        fname, lini = name[0], name[1][0]
        if len(firstNameDict[fname]) == 1:
            newList.append(fname)
        # if more than 1 values, then see if only one last initial
        elif len(firstNameDict[fname]) >= 1 and firstNameDict[fname].count(lini) == 1:
            newList.append(f"{fname} {lini}.")
        else:   # if it doesn't meet the above criteria
            newList.append(" ".join(name))

    return newList


print(OrderedNameList(["Jason Alexander", "Megan Smith",
                       "Megan Fox", "Jason Sudekis", "Jason Avocado", "Siena Aguayo"]))
print(OrderedNameList1(["Jason Alexander", "Megan Smith",
                        "Megan Fox", "Jason Sudekis", "Jason Avocado", "Siena Aguayo"]))
