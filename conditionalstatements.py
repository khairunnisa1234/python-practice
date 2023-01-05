''' 
t20 = 20 overs
odi = 50 overs
test= unlimited overs

input from user wt is match tyoe
depend son matchtype should print overs


'''
match_type = str(input("enter the match type "))
if match_type == "ttwenty":
    print("twenty overs")
elif match_type == "odi":
    print("fifty overs")
elif match_type == "test": 
    print("unlimited overs")
else:
    print("ivalid format")

#should keep equal double symbol ==
#shpuld keep quations to decalration of name