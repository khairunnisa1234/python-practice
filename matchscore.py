'''naga vijay kumar prathi5:33 PM
score = x

T20 -> x is less than 100 = bad
	   x is between 101-150 = Avg
	   x is Greater than 150 = Good


ODI -> x is less than 180 = bad
	   x is between 181-250 = Avg
	   x is Greater than 250 = Good


Test -> x is less than 220 = bad
	    x is between 221-290 = Avg
	    x is Greater than 290 = Good

ip = t20
score =90
op =bad

ip =odi
score = 200
op = avg

ip= test
score = =300
op = good
'''
match_type = str(input("enter the type : "))
match_score = int(input("enter the value :"))
if match_type=="t20":
    if match_score<100:
        print("bad")
    elif match_score>=101 and match_score<=150:
        print("average")
    elif match_score>150:
        print("good")
    else:
        print("cricket")
elif match_type=="odi":
    if match_score<180:
        print("bad")
    elif match_score>=181 and match_score<=250:
        print("average")
    elif match_score>250:
        print("good")
    else:
        print("cricket")
elif match_type =="test":

    if match_score<220:
        print("bad")
    elif match_score>=221 and match_score<=290:
        print("average")
    elif match_score>290:
        print("good")
    else:
        print("cricket")
else:
    print("criceket")