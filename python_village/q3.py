string = "OLHyrgeTzIm3GBjNEPz1T4vsNCV40o5IQSCw00EmY5TVWZpit3wUPScxQyFlY86ImCpskiEh05KFNavJlW7OiPo7kp3frqNHUkOnychodactylusFzitlTN7fallaxJWF1jzltZKRXRi31Sp26xm76mRTKsDgx5RlL3vX4CfNKjsTDZJB4P67FcKgclrHkwoPL0z84K."
word1 = string[98:111 + 1] # +1 so the last character of the given string also gets included
word2 = string[120:125 + 1]
result = word1 + " " + word2
print(result)


"""
  For simple concatenation:

  str1 = "Hello"
  str2 = " World!"
  result = str1 + str2
  print(result)  # Output: Hello World!

  This provides a concise and readable way to embed variables directly within a string:

  name = "Alice"
  age = 30
  result = f"Hello, my name is {name} and I am {age} years old."
  print(result)  # Output: Hello, my name is Alice and I am 30 years old.

  This is efficient for concatenating a large number of strings, especially if they are stored in a list or iterable:

  words = ["Hello", "World", "from", "Python"]
  result = " ".join(words)
  print(result)  # Output: Hello World from Python
"""
