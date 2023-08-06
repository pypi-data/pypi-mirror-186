# this program Remove all consonants from string
 
test_str = "I am studying the course Tools and Techniques for Data Science"

print("The original string is : " + test_str)
res = []
for ch in test_str:
    if ch in "aeiouAEIOU":
        res.extend(ch)
res = " ".join(res)

print("String after consonants removal : " + str(res))