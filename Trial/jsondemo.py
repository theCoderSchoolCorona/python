import json
#json example

tester = {"happy": 200} #example dictionary



"""
with open("testerfile.json", "w") as f:  #creates a json or overwrites if one does not exist
    json_tester = json.dump(tester,f)


with open("testerfile.json", "r") as f:
    json_input = json.load(f)


print(json_input)
print(type(json_input))
"""

try:
    with open("doesnotexist.json", "r") as f:
        print("This can't happen cause I don't exist")

except:
    print('This file does not exist so make a new one with a write ->')