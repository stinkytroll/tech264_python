#  bad_string = 'I said 'Wow!''
#  print(bad_string)

# Explain: Why does this fail?
# Strings can be enclosed in both double and single quotes, so when 'Wow!' uses it again, python reads that as the
# string ending which gives a syntax error.

# Find 3 ways to make this string assignment work
bad_string = 'I said "Wow!"'

print(bad_string)

bad_string = '''I said 'Wow!'''

print(bad_string)

bad_string = """I said "Wow!"""

print(bad_string)

# Explain: What is best practice when deciding what quotes to use around strings in Python?
# Be consistent and use both double and single quotes, deciding based of readability.

