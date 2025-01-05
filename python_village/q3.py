"""
ID: INI3
Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. 
In other words, we should include elements s[b] and s[d] in our slice.
"""

string = "OLHyrgeTzIm3GBjNEPz1T4vsNCV40o5IQSCw00EmY5TVWZpit3wUPScxQyFlY86ImCpskiEh05KFNavJlW7OiPo7kp3frqNHUkOnychodactylusFzitlTN7fallaxJWF1jzltZKRXRi31Sp26xm76mRTKsDgx5RlL3vX4CfNKjsTDZJB4P67FcKgclrHkwoPL0z84K."
word1 = string[98 : 111 + 1]
word2 = string[120 : 125 + 1]
result = word1 + " " + word2
print(result)
