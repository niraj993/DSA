import re

# names = """
# Jaince is 22 Miraj is 26 and Manish is 34
# """
# pattern = r"\d{1,3}"
# ages = re.findall(pattern=pattern,string=names)
# name_pattern = r"[A-Z][a-z]*"
# name = re.findall(pattern=name_pattern,string=names)
# print("=========>",name)


# ip = "IP: 192.168.1.10"

# pattern = r"\d"

# result = re.findall(pattern=pattern,string=ip)
# print("=======>",result)






import re
# Q1 Extract number
input = "I have 25 apples and 10 oranges."
number = re.findall(pattern=r"\d{2}",string=input)
print("=========>",number)

# Q2 Python is a programming language
words = re.split(pattern=r"/s",string="Python is a programming language")
print("===========>",words)

# Q3 Python is easy. I use Python every day. Python is powerful.
# Find all occurrences of Python
occr = re.findall(pattern=r"Python",string="Python is easy. I use Python every day. Python is powerful.")
print("=============>",occr)

# Q4 Extract uppercase letters
upper_letter = re.findall(pattern=r"[A-Z]",string="Hello PYTHON Developer")
print("==========>",upper_letter)


# Q5 Extract lowercase letters

lower_case = re.findall(pattern=r"[a-z]",string="Hello PYTHON")
print("======>",lower_case)

# Q6. Extract vowels
vowels = re.findall(pattern=r"[aeiou]",string="Python Developer")
print("==========>",vowels)

# Q7. Extract words starting with P
# \w* → zero or more word characters after P
p_words = re.findall(pattern=r"P\w*",string="Python Java Perl PHP Ruby")
print("===========>",p_words)

# Q8. Find words ending with ing
end_word = re.findall(pattern=r"\b\w+ing\b",string="I am learning Python and building APIs")
print("==========>",end_word)


# Q9. Extract phone numbers
phone_number = re.findall(pattern=r"\d+",string="Contact Rahul at 9876543210 or Amit at 9123456789.")
print("===========>",phone_number)

# Q10. Extract email addresses
# Contact us at admin@gmail.com or support@company.com
email_id = re.findall(pattern=r"[a-zA-Z.]+@[a-zA-Z]+\.[a-zA-Z]{2,}",string="Contact us at admin@gmail.com or support@company.com")
print("==========>",email_id)


# Q11. Extract IP addresses
input = """
Server1: 192.168.1.10
Server2: 10.0.0.1
Server3: 172.16.0.5
"""
ips = re.findall(pattern=r"\d{1,3}(?:\.\d{1,3}){3}",string=input)
print("=============>",ips)




# Q12. Extract dates
# Today is 26-08-2026 and tomorrow is 27-08-2026.
dates = re.findall(pattern=r"\d{1,2}-\d{1,2}-\d{1,4}",string="Today is 26-08-2026 and tomorrow is 27-08-2026.")
print("===================>",dates)


# Q14. Find words containing only digits
# abc 123 xyz 4567 test 89
digits = re.findall(pattern=r"\d+",string="abc 123 xyz 4567 test 89")
print("==============>",digits)

# Q15. Find words containing only alphabets
# Python123 Python Developer123 Java
alphabets = re.findall(pattern=r"\b[A-Za-z]+\b",string="Python123 Python Developer123 Java")
print("==============>",alphabets)

# Q16. Extract ERROR messages
input = """
INFO Server started
ERROR Database connection failed
INFO User logged in
ERROR Connection timeout
"""
error_messages = re.findall(pattern=r"^ERROR.*",string=input,flags=re.MULTILINE)
print("===============>",error_messages)



interfaces = """
Interface Gi0/1 is UP
Interface Gi0/2 is DOWN
Interface Gi0/3 is UP
Interface Gi0/4 is DOWN
"""

result = []
for i in interfaces.splitlines():
    if "DOWN" in i:
        result.append(i.split(maxsplit=2)[1])
print("===========>",result)