#Q1

from email.mime import text


ask_name = input("Tell me your name: ")
ask_year = int(input("Tell me your birth year: "))
current_year = 2026
print(f"Hello {ask_name}, your are {current_year - ask_year} years old")

#Q2
txt = 'LMaasleitbtui'
print(txt[0:15:2])

#Q3
string1 = input("Enter message: ")
print(len(string1))
print(string1.upper())
print(string1.lower())

#Q4
palindrome = input("Enter a word:")
if palindrome == palindrome[::-1]:
    print(palindrome, "is a palindrome")
else:
    print(palindrome, "isn't a palindrome")

#Q5
string2 = input("Enter a string: ")
vowels = 0
consonants = 0
for str in string2.lower():
    if str in "aeiuo":
        vowels +=1
    else:
        consonants +=1
print(f"Number of vowels: {vowels}")
print(f"Number of consonants : {consonants}")

#Q6
stringfirst = input("Enter your first string: ")
stringsecond = input("Enter your second string: ")
if stringsecond in stringfirst:
    print(f"{stringsecond} is a part of {stringfirst}")
else:
    print(f"{stringsecond} has nothing much to do with {stringfirst}")

#Q7
sentence = input("Enter a sentence: ")
replace_word = input("Enter a word from that sentence to replace: ")
new_word = input("Enter a a new word for it: ")
new_sentence = sentence.replace(replace_word, new_word)
print(new_sentence)

#Q8
string3 = input("Enter a string: ")
print("First character of the string is ", string3[0])
print("Last character of the string is ", string3[-1])

#Q9
string4= input("Enter a string: ")
print("Reversed string is ", string4[::-1])

#Q10
sentence1= input("Enter a sentence: ")
words = sentence.split()
print(f"Number of words in {sentence1} is {len(words)}")

#Q11
string_digit = input("Enter a stirng: ")
has_digit = False
for char in string_digit:
    if char.isdigit():
        has_digit = True
if has_digit:
    print(f"The string {string_digit} has a digit")
else:
    print(f"The string {string_digit} has no digit")

#Q12
words = ['book', 'pen', 'pencil']
separator =input("Enter a separator: ")
joined_sep = separator.join(words)
print(joined_sep)