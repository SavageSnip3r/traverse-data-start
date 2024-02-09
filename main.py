
ageData = open("age-data.txt", "r")
numberData = open("number-data.txt", "r")
surveyResults = open("survey-results.txt", "r")

# ageA=0 
# ageB=0
# ageC=0
# ageD=0
# for x in ageData:
#     if int(x) < 18: # <18, ageA
#         ageA = ageA + 1
#     elif int(x) <= 35: # 18-35, ageB
#         ageB = ageB + 1
#     elif int(x) <= 65: # 36-65, ageC
#         ageC = ageC + 1
#     else: # >65, ageD
#         ageD = ageD + 1
# print(ageA, ageB, ageC, ageD)

# totalEven = 0
# totalOdd = 0
# for x in numberData:
#     if int(x)%2 == 0:
#         totalEven = totalEven + 1
#     else:
#         totalOdd = totalOdd + 1
# print(totalEven, totalOdd)

# totalYes = 0
# totalNo = 0
# totalMaybe = 0
# for x in surveyResults:
#     if x == "Yes\n" or x == "Yes":
#         totalYes = totalYes + 1
#     elif x == "No\n" or x == "No":
#         totalNo = totalNo + 1
#     elif x == "Maybe\n" or x == "Maybe":
#         totalMaybe = totalMaybe + 1
# print(totalYes, totalNo, totalMaybe)

# might be a better way to do this that i can't think of rn