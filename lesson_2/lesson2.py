#Number Data type

#Q1
num = float(input("Enter a float number: "))
rounded_num = round(num, 2)
print(rounded_num)

#Q2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

max_num = max(a,b,c)
min_num = min(a,b,c)
print("Max number is:", max_num)
print("Min number is:", min_num)

#Q3
x = int(input("Enter a number in kilometers: "))
meters = x * 1000
centimeters = x * 100000
print(f"{x} kilometers is equal to {meters} meters and {centimeters} centimeters.")

#Q4
a1 = int(input("Enter first number: "))
a2 = int(input("Enter second number: "))

quotient = a1//a2
remainder = a1%a2
print(f"Quotient : {quotient}")
print(f"Remainder : {remainder}")

#Q5
celcius = float(input("Enter temperature in Celcius: "))
fahrenheit = (celcius * 9/5) +32
print(f"{celcius} Celcius is equal to {fahrenheit} Fahrenheit")

#Q6
num1 = int(input("Enter number: "))
last_digit = num1 % 10
print(f"last digit of {num1} is {last_digit}")

#Q7
num2 = int(input("Enter number: "))
if num2 %2 == 0:
    print(f"{num2} is even")
else:
    print(f"{num2} is odd")

#String Questions

#Q1

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
for char in string2.lower():
    if char in "aeiuo":
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
words = sentence1.split()
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

#Q13
string = input("Enter a string: ")
result = string.replace(" ","")
print(result)

#Q14
stringno1 = input("Enter a string: ")
stringno2 = input("Enter a string: ")
if stringno1 == stringno2:
    print("Both strings are equal")
else: 
    print("Strings are not equal")

#Q15
sentence2 = input("Enter a sentence: ")
words2 = sentence2.split()
acronym = ""
for word in words2:
    acronym +=word[0].upper()
print(f"Acronym of {sentence2} is {acronym}")

#Q16
string5 = input("Enter a string: ")
char = input("Enter a character to remove: ")
result = string5.replace(char, "")
print(result)

#Q17
vowel_no = input("Enter a string: ")
replacement = vowel_no.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
print(replacement)

#Q18
string6 = input("Enter a string: ")
start = input("Enter a starting word: ")
end = input("Enter an ending word: ")
if string6.startswith(start) and string6.endswith(end):
    print(f"The string starts and ends with those words")
else:
    print("It does not match")

#Boolean Data type questions

#Q1
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()
if username == "" and password == "":
    print("Both username and password are empty")
else:
    print("Username and password aren't empty")

#Q2
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number : "))
if num1 == num2:
    print(f"{num1} is equal to {num2}")
else:
    print(f"{num1} is not equal to {num2}")

#Q3
num3 = int(input("Enter a number: "))
if num3>=0 and num3 %2 == 0:
    print(f"{num3} is positive and even")
else:
    print(f"{num3} is not both positive and even")

#Q4
num4 = int(input("Enter first number: "))
num5 = int(input("Enter second number: "))
num6 = int(input("Enter third number: "))
if num4 != num5 and num4 !=num6 and num5 != num6:
    print("All numbers are different")
else:
    print("Not all of the numbers are different")

#Q5
num7 = (input("Enter first string: "))
num8 = (input("Enter second string: "))
if len(num7) == len(num8):
    print("Both strings have the same length")
else:
    print("Strings have different lengths")

#Q6
num9 = int(input("Enter number: "))
if num9 % 3 == 0 and num9 % 5 == 0:
    print(f"{num9} is divisible by both 5 and 3")
else:
    print(f"{num9} is not divisible by both 3 and 5")

#Q7
num10 = int(input("Enter first number: "))
num11 = int(input("Enter second number: "))
if num10 + num11 > 50.8:
    print(f"The sum of {num10} and {num11} is greater than 50.8")
else:
    print(f"The sum of {num10} and {num11} is not greater than 50.8")

num12 = int(input("Enter a number: "))
if num12 > 10 and num12<20 :
    print(f"{num12} is between 10 and 20")