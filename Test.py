

'''
Point = 1
Made 3pt Shot (3PM)= 1
Field Goals Attempted (FGA) = -1
Field Goals Made (FGM) = 2
Free Throws Attempted (FTA) = -1
Free Throws Made (FTM) = 1
Rebound (REB)= 1
Assist (AST)= 2
Steal (STL) = 4
Block (BLK) = 4
Turnover (TOV) = -2


#Not accounting for FieldGoal Attempt because I will calculate that in later function


Num3Points():

        Made 3 point --> 1
        Points --> 3
        Field Goals Made --> 2


Num2Pointers():

    Points --> 2
    FieldGoals Made --> 2


FieldGoalDeductions():

    return (FieldGoalsAttempted + FieldGoalsMissed) * -1


FreeThrowReductions():

    reutrn (NumFieldGoalsMissed + numFieldGoalsMade) * -1


FreeThrows():

    FreeThros Made --> 1
    Points --> 1



Num3PointShots --> int
Num2Pointers --> int
numFieldGoals Missed --> int
Field Goals attempted --> int
Field goals Missed --> int
NumFreeThrowsMade --> int
NumFreeThrosMissed --> int



HELPER FUNCTIONS FOR THE PARAMETERS BELOW:

    just be added to the overall score

    Ex: score += Rebounds * 1

NON SHOTS

Rebounds --> int
Assist --> int
Steal --> int
Block --> int
Turnover --> int


3-pointer made = 5 (3 for three points scored, 1 for a 3-pointer, 2 for a field goal made, and -1 for a field goal attempt; 3+1+2-1=5).

2-pointer made = 3 (2 for two points scored, 2 for a field goal made, -1 for a field goal attempt; 2+2-1=3)

Free throw made = 1 (1 for one point scored, 1 for a free throw made, -1 for a free throw attempt; 1+1-1=1)
'''



def Calculate(data):

    score = 0

    score += data["num3Points"] * 6
    score += data["num2Points"] * 4
    score += data["numFreeThrowsMade"] * 2

    score += data["rebounds"]
    score += data["assists"] * 2
    score += data["steal"] * 4
    score += data["blocks"] * 4

    score -= data["turnovers"] * 2

    score -= data["numFieldGoals"]
    score -= data["numFreeThrows"]

    return score


def GetRequiredData(li):

    ret = {}

    if li[16] == "":

        PA3 = 0
    else:

        PA3 = int(float(li[16].strip()))


    if not li[17]:

        P3Percent = 0.0

    else:

        P3Percent = float(li[17].strip())


    PA2 = int(li[14].strip())
    P2Percent = float(li[15].strip())
    FTA = int(li[12].strip())
    FTPercent = float(li[13].strip())
    GP = int(li[5].strip())
    RPG = float(li[24].strip())
    APG = float(li[26].strip())

    tempSPG = li[28].strip()

    if tempSPG:

        SPG = float(tempSPG)

    else:

        SPG = 0



    if len(li) <= 29 or not li[29]:

        BPG = 0

    else:


        BPG = float(li[29].strip())

    if len(li) <= 30 or not li[30]:

        TOPG = 0

    else:

        TOPG = float(li[30].strip())


    ret["num3Points"] = int(PA3 * P3Percent)
    ret["num2Points"] = int(PA2 * P2Percent)
    ret["numFieldGoals"] = PA2 + PA3
    ret["numFreeThrowsMade"] = int(FTA * FTPercent)
    ret["numFreeThrows"] = FTA

    ret["rebounds"] = int(RPG * GP)
    ret["assists"] = int(APG * GP)
    ret["steal"] = int(SPG * GP)
    ret["blocks"] = int(BPG * GP)
    ret["turnovers"] = int(TOPG * GP)

    return ret


best = {"C": ("", 0),"C-F": ("", 0), "F": ("", 0), "F-C": ("", 0), "F-G": ("", 0), "G": ("", 0), "G-F": ("", 0)}



with open("NBAStats.csv") as f:

    f.readline()
    f.readline()


    for line in f:


        li = line.strip().split(",")



        data = GetRequiredData(li)

        score = Calculate(data)

        position = li[3]

        if score > best[position][1]:

            best[position] = (li[1], score)

    print(best)





