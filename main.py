# List Filtering #
def filter_list(l):
   l = [i for i in l if type(i) != int]
   return print(l)
filter_list([1,2,'aasf','1','123',123])


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
spin_words( "Hey fellow warriors" )


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
print(array_diff([1,2,2,2,3],[2]))
