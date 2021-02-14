# 1. Reverse the words in a list
##   problem_1("I am hungry")
##
# "hungry am I"

def reverseWords(string):
    string_list = string.split(' ')

    new_sentence = ''

    for index in range(len(string_list)-1, -1, -1):
        new_sentence = new_sentence + string_list[index] + ' '

# new_sentence.strip()

    return new_sentence.strip()


# 2. Given a list of words, return a list of [word, count] paris, ordered by count.
##  problem_2(["hello", "world", "world"])
##
# [["hello", 1], ["world", 2]]

def wordsCount(list_of_word):
    wordsCountDict = {}
    wordsCountList = []

    for word in list_of_word:
        wordsCountDict[word] = wordsCountDict.get(word, 0) + 1

    for word, count in wordsCountDict.items():
        wordsCountList.append([word, count])

    return wordsCountList

# 3. Given a set of rows, return a string that renders it in an HTML table.
##
##  problem_3([["one", "uno"], ["two", "dos"]])
##
# This should be one long string
# <table>
# <tbody>
# <tr><td>one</td><td>uno</td></tr>
# <tr><td>two</td><td>dos</td></tr>
# </tbody>
# </table>


def htmlTable(list_of_word):

    start = "<table>\n" + "  <tbody>\n"
    end = "  </tbody>\n" + "</table>"

    table = ''
    for word in list_of_word:
        table = table + f"    <tr><td>{word[0]}</td><td>{word[1]}</td></tr>\n"

    return start + table + end


# 4. Sort a list of file sizes. "K", "M", and "G" are abbreviations for kilobytes, megabytes, and gigabytes. A number without a suffix is in bytes.
##  problem_4(["1M", "20G", "5012"])
##
# ["5012", "1M", "20G"]

def sort_file_sizes(list_of_fsizes):

    list_of_fsizes.sort(key=file_size)

    return list_of_fsizes


def file_size(file_in_string):
    """ Calculate file sizes in bytes for sorting."""

    if file_in_string.endswith("K"):
        file_size = int(file_in_string[:-1])*1000
    elif file_in_string.endswith("M"):
        file_size = int(file_in_string[:-1])*1000000
    elif file_in_string.endswith("G"):
        file_size = int(file_in_string[:-1])*1000000000
    else:
        file_size = int(file_in_string)

    return file_size


# 5. Print all the prime numbers up to and including the value passed in.
# problem_5(17)
##
# [2, 3, 5, 7, 11, 13, 17]

def primeNum(num: int):
    """ Print all the prime numbers up to and including the value passed in."""

    numList = []

    for n in range(num + 1):
        if isPrime(n) == True:
            numList.append(n)

    return numList

# Helper Function


def isPrime(number):
    """ Take in an integer. Return True if it is."""

    if number <= 1:
        return False

    for num in range(2, number):
        if number % num == 0:
            return False

    return True


# 6. Given a target word and list of words, return words from the list that are anagrams of the target word.
#   problem_6("cat", ["act", "cat", "hat"])
#    ["act", "cat"]

def anagramList(target_word, word_list):

    anagramList = [word for word in word_list if sorted(
        word) == sorted(target_word)]

    return anagramList


# 7. Render a template with the given values.

##  template = "{name} uses {product}? I use {product}, too!"
##  values = [["name", "John"], ["product", "Vim"]]

##  problem_7(template, values)
##  "John uses Vim? I use Vim, too!"

def templateVal(template, values):

    result = ''

    for innerlist in values:
        word = innerlist[0]
        wordR = innerlist[1]
        result = template.replace(("{" + word + "}"), wordR)
        template = result

    return template


# 8. Test if two deeply nested arrays hold the same values
##
array1 = [1, [2, [3]], [4, 5]]
array2 = [1, [2, [3]], [4, 5]]
##  problem_8(array1, array2)
##
# true


def sameArrays(array1, array2):

    if len(array1) != len(array2):
        return False

    for i in range(len(array1)):
        if isinstance(array1[i], list) and isinstance(array2[i], list):
            if not sameArrays(array1[i], array2[i]):
                return False
        elif not isinstance(array1[i], list) and not isinstance(array2[i], list):
            if array1[i] != array2[i]:
                return False
        else:
            return False

    return True


# 9. Given a string of parentheses, test if it is balanced.
##
# problem_9("(()())")
# true

def isPair(string):
    """ Given a string of parentheses, return true if balanced."""

    counter = 0

    for item in string:
        if item == "(":
            counter += 1
        elif item == ")":
            counter -= 1
            if counter < 0:
                return False

    return not counter


# 10. Given a year and month, render the calendar month as a string--Sunday through Saturday
##
##  problem_10(2012, 12)
##
# 1
# 2  3  4  5  6  7  8
# 9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31

def printCal(year, month):

    import calendar
    calendar.setfirstweekday(calendar.SUNDAY)
    calList = calendar.month(year, month).split("\n")

    calStr = ''
    for line in range(2, len(calList)-1):
        calStr = calStr + calList[line] + "\n"

    return calStr[:-1]

    ######### Code Signal ##########


def isLucky(n):

    string = str(n)

    first_half = string[:int(len(string)/2)]
    second_half = string[int(len(string)/2):]

    first_half_total = sum([int(num) for num in first_half])
    second_half_total = sum([int(num) for num in second_half])

    return first_half_total == second_half_total


def isLuckyBen(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n//10
    return sum(digits[:int(len(digits)/2)]) == sum(digits[int(len(digits)/2):])


def sortByHeight(a):

    tree_index = []

    # Keep track of the position of -1?
    for index, num in enumerate(a):
        if num == -1:
            tree_index.append(index)

    a.sort()

    a_wo_tree = a[len(tree_index):]

    for index in tree_index:
        a_wo_tree.insert(index, -1)

    return a_wo_tree
