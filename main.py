# List Filtering #
def filter_list(l):
    l = [i for i in l if type(i) != int]
    return print(l)
filter_list([1, 2, 'aasf', '1', '123', 123])


# Replace With Alphabet Position #
import string
def alphabet_position(text):
    alphabet = string.ascii_lowercase
    letter_to_position = {letter: str(position) for letter, position in zip(alphabet, range(1, 27))}
    result = [''.join(letter_to_position[char]) for char in text.lower() if char in letter_to_position]
    result = ' '.join(map(str, result))
    return result
print(alphabet_position("The sunset sets at twelve o' clock."))


# Stop gninnipS My sdroW! #
def spin_words(sentence):
    reversedSentence = [''.join(reversed(word)) if len(word) >= 5 else ''.join(word) for word in sentence.split()]
    result = ' '.join(map(str, reversedSentence))
    return print(result)
spin_words("Hey fellow warriors")


# Sum of Digits / Digital Root #
def digital_root(n):
    sumOfDigits = 0
    for i in iter(str(n)):
        sumOfDigits += int(i)
    if sumOfDigits > 9:
        n = sumOfDigits
        return digital_root(n)
    return sumOfDigits
print(digital_root(15))


# Array Diff #
def array_diff(a, b):
    return [i for i in a if i not in b]
print(array_diff([1, 2, 2, 2, 3], [2]))


# Remove vowels from string
def disemvowel(string_):
    return string_.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '').replace('A', '').replace('E', '').replace('I', '').replace('O', '').replace('U', '')
print(disemvowel("This website is for losers LOL!"))

#
def lovefunc(flower1, flower2):
    return False if (flower1 + flower2) % 2 == 0 else True
print(lovefunc(1, 8))


# Delete occurrences of an element if it occurs more than n times #
def delete_nth(order, max_e):
    count_dict = {}
    result = []
    for num in order:
        if count_dict.get(num, 0) < max_e:
            result.append(num)
            count_dict[num] = count_dict.get(num, 0) + 1
    return result
print(delete_nth([20,37,20,21], 1))

#Codewars' best solution
#The purpose of using order[:i] in the condition order[:i].count(o)<max_e is to check the frequency of the current element (o) within the processed portion of the list. This ensures that the delete_nth function only removes elements that appear more than max_e times in the entire order list, not just in the portion that has been processed so far.
#def teste(order,max_e):
#    return [o for i, o in enumerate(order) if order[:i].count(o)<max_e ] # yes!
#print(teste([20,37,20,21], 1))