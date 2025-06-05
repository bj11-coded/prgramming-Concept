#  re module is used for regular expression operations in python
# it provides a powerful way to search, match, and manipulate strings using patterns
import re

txt = "this is a text"
x = re.search("Is", txt)
if x:
    print("it is a valid text")  # prints a match object if found, otherwise None
else:
    print("it is not a valid text")

# both search and match are case sensitive by default
x = re.match("Is", txt)
if x:
    print("it is a valid text")
else:
    print("it is not a valid text")

# to make it case insensitive we can use re.IGNORECASE

x = re.search("IS",txt, re.IGNORECASE)

if x:
    print("it is a valid text")
else:
    print("it is not a valid text")


textNew = "this text has 1 or some text which are duplicated text"
# to find all occurrences of a pattern in a string, we can use re.findall
x = re.findall("Text", textNew, re.IGNORECASE)

# ^ is used to search for a pattern at the beginning of a string
# y = re.search("^this",textNew)
# $ is used to search for a pattern at the end of a string
# y = re.search("text$",textNew)
# * or + is used to match the occrance of the given word more then one time

# set helps to find all occurrences of a pattern in a string
y = re.findall("[1-10]", textNew)
print(y)

if x:
    print(f"found {len(x)} occurrences of 'text'")
else:
    print("no occurrences found")


# special sequences in regex
# \d matches any digit
# \D matches any non-digit character
# \w matches any alphanumeric character (letters, digits, and underscores)
# \W matches any non-alphanumeric character
# \s matches any whitespace character (spaces, tabs, newlines)
# \S matches any non-whitespace character
# \b matches a word boundary
# \B matches a non-word boundary
# \n matches a newline character
# \t matches a tab character means a horizontal tab like space
# \z matches the end of the string
# \A matches the start of the string
# 

stri = "the quick    brown fox jumps over the lazy dog 123 \n characters owns"

seq = re.findall(r"\w",stri)
print(seq)

if seq:
    print("Match found")
else:
    print("Match not found")


# password regex
password = "passssD1@"

# A valid password must be between 8 and 20 characters long, contain at least one digit, one uppercase letter, one lowercase letter, and one special character
# The regex pattern for a valid password is:
# ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,20}$

validate_password = re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W]).{8,20}$", password)


if validate_password:
    print("Password is valid")
else:
    print("Password is not valid")
