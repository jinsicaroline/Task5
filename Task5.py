#program 1 

#string of vowels
vowels = 'aeiou'

#string of inputs
ip_str = 'GuviGeeks Network Private Limited?'

#for caseless comparisions converts input string to lowercase.
ip_str = ip_str.casefold()

#dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0) #{a:0, e:0, i:0, o:0, u:0}

#iterates  the vowels
for char in ip_str:
    #checks for each character in count
    if char in count:
        #count value changes 0 to 1 and increase if repeated with same characters
        count[char] += 1

print(count)
#output : {'a': 1, 'e': 5, 'i': 4, 'o': 1, 'u': 1}

#-----------------------------------------------------------------------------------------------------------#

#program 2
def contnum(n):
     # initializing starting number 
    num = 1
    # outer loop to handle number of rows
    for i in range(0, n):
     # not re assigning num
        # num = 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing number
            print(num, end=" ")
         
            # incrementing number at each column
            num = num + 1
     
        # ending line after each row
        print("\r")
 
n = 6
 
# sending 5 as argument
# calling Function
contnum(n)
#output :
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 

#...........................................................................................................#

#Program3

string = "GuviGeeks Network Private Limited "

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""

for i in range(len(string)):
    if string[i] not in vowels:
        result = result + string[i]

print("\nAfter removing Vowels: ", result)

#output : After removing Vowels:  GvGks Ntwrk Prvt Lmtd

#...........................................................................................................#

#program 4

string='madam'
count=0
temp=[]
for i in string:
    if(i not in temp):
        count+=1
        temp.append(i)
print('Total Unique Characters count:',count)  

#output : Total Unique Characters count: 3

#..........................................................................................................#

#Program 5

x = "malayalam"
w = ""
for i in x:
    w = i + w
if (x == w):
    print("True")
else:
    print("False")

#output : True

#...........................................................................................................#

#Program 6

from difflib import SequenceMatcher

string1 = 'one two three four'
string2 = 'one two nine ten'

match = SequenceMatcher(None, string1, string2).find_longest_match(
    0, len(string1), 0, len(string2))

print(match)  # Match(a=0, b=0, size=8)

# one two
print(string1[match.a:match.a + match.size])

# one two
print(string2[match.b:match.b + match.size])

#output : Match(a=0, b=0, size=8)
one two 
one two 

#..........................................................................................................#

#Program 7

# initializing string
test_str = "GuviGeeks Network Private Limited"

# printing original string
print ("The original string is : " + test_str)

# creating an empty dictionary
freq = {}

# counting frequency of each character
for char in test_str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# finding the character with maximum frequency
max_char = max(freq, key=freq.get)

# printing result
print("The maximum of all characters in GuviGeeks Network Private Limited is : " + str(max_char))

#output : The original string is : GuviGeeks Network Private Limited
The maximum of all characters in GuviGeeks Network Private Limited is : e

#..........................................................................................................#

#Program 8

str1 = str(input ("Enter string 1: "))
str2 = str(input ("Enter string 2: "))

#Convert into lowercase and sort
str1 = sorted(str1.lower())
str2 = sorted(str2.lower())

print("String 1 after sorting: ", str1)
print("String 2 after sorting: ", str2)

#Define a function to match strings
def isAnagram():
    if (str1 == str2) :
        return "The strings are anagrams."
    else:
        return "The strings are not anagrams."

print(isAnagram())

#output : 
Enter string 1: listen
Enter string 2: silent
String 1 after sorting:  ['e', 'i', 'l', 'n', 's', 't']
String 2 after sorting:  ['e', 'i', 'l', 'n', 's', 't']
The strings are anagrams.

#...........................................................................................................#

#Program 9

entence = "Welcome to python programming"
words = 0
for i in sentence:
    if i == " " or i == "\t" or i == "\n":
        words += 1
if len(sentence) > 0:
    print("Number of words:", words + 1)
else:
    print("Number of words: 0")

#output : Number of words: 4

#...........................................................................................................#