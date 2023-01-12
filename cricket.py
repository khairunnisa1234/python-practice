'''
t20 = 20ovwers
odi = 50 overs
test = unlimited overs
use input
based on the tat balls print 
over ki six balls

'''

match_type = str(input("enter the value : "))
if match_type == "ttwenty":
    print(20*6)
elif match_type == "odi":
    print(50*6)
elif match_type == "test":
    print("infinity balls")
else :
    print("cricket")