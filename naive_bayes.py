def naive_bayes_algo(mood_1,age_1,qualification_1,gender_1,hobby_1,budget_1,climate_1,df):

 # Based on Bayes Theorem : P(A/B) = P(B/A)*P(A)/P(B)
 # Step1 : Calculate the prior Probability [i.e P(A)]
 # Step2 : Find Likelihood probability with each attribute for each class.
 # Step3 : Put values in Bayes Formula and get the Posterior Probability
 # Step4 : Select the class with the highest probability.  

# parameters = [Normal,19< and <29, Graduated, Male, H4(Adventure), Medium, Rainy]
# P(Historical/parameters) = P(Normal/Historical)*P(19< and <29/Historical)*
#                            P(Graduated/Historical)*P(Male/Historical)*P(H4/Historical)
#                            P(Medium/Historical)*P(Rainy/Historical)*P(Historical)/P(parameters)


    M = mood_1
    A = age_1
    Q = qualification_1
    G = gender_1
    H = hobby_1
    B = budget_1
    C = climate_1
    print(M,A,Q,G,H,B,C)

    # Step1 : Calculating the prior Probabilities
    countHistorical = (df.Area_of_Interest == "Historical").sum()
    countReligious  = (df.Area_of_Interest == "Religious").sum()
    countWildlife  = (df.Area_of_Interest == "Wildlife").sum()
    countAdventure  = (df.Area_of_Interest == "Adventure").sum()
    countShopping  = (df.Area_of_Interest == "Shopping").sum()

    #print("total Count of Historical Places:",countHistorical)
    #print("total Count of Religious Places :",countReligious)
    #print("total Count of Wildlife Places:",countWildlife)
    #print("total Count of Adventure Places:",countAdventure)
    #print("total Count of Shopping Places:",countShopping)

    # Step2 : Find Likelihood probability with each attribute for each class.

    countMoodHistorical = 0
    countMoodReligious = 0
    countMoodWildlife = 0
    countMoodAdventure = 0
    countMoodShopping = 0

    for i in range(len(df)):
        if df["Mood"][i]== M and df["Area_of_Interest"][i]=="Historical":
            countMoodHistorical+=1
        elif df["Mood"][i]== M and df["Area_of_Interest"][i]=="Religious":
            countMoodReligious+=1
        elif df["Mood"][i]== M and df["Area_of_Interest"][i]=="Wildlife":
            countMoodWildlife+=1
        elif df["Mood"][i]== M and df["Area_of_Interest"][i]=="Adventure":
            countMoodAdventure+=1
        elif df["Mood"][i]==M and df["Area_of_Interest"][i]=="Shopping":
            countMoodShopping+=1
        
    pCMH = countMoodHistorical/countHistorical
    pCMR = countMoodReligious/countReligious
    pCMW = countMoodWildlife/countWildlife
    pCMA = countMoodAdventure/countAdventure
    pCMS = countMoodShopping/countShopping
    #print(M," and Historical:",pCMH)
    #print(M," and Religious :",pCMR)
    #print(M," and Wildlife :",pCMW)
    #print(M," and Adventure :",pCMA)
    #print(M," and Shopping :",pCMS)

    countAgeHistorical = 0
    countAgeReligious = 0
    countAgeWildlife = 0
    countAgeAdventure = 0
    countAgeShopping = 0

    for i in range(len(df)):
        if df["Age"][i]== A and df["Area_of_Interest"][i]=="Historical":
            countAgeHistorical+=1
        elif df["Age"][i]== A and df["Area_of_Interest"][i]=="Religious":
            countAgeReligious+=1
        elif df["Age"][i]== A and df["Area_of_Interest"][i]=="Wildlife":
            countAgeWildlife+=1
        elif df["Age"][i]== A and df["Area_of_Interest"][i]=="Adventure":
            countAgeAdventure+=1
        elif df["Age"][i]== A and df["Area_of_Interest"][i]=="Shopping":
            countAgeShopping+=1
        
    pCAH = countAgeHistorical/countHistorical
    pCAR = countAgeReligious/countReligious
    pCAW = countAgeWildlife/countWildlife
    pCAA = countAgeAdventure/countAdventure
    pCAS = countAgeShopping/countShopping
    #print(A," and Historical:",pCAH)
    #print(A," and Religious :",pCAR)
    #print(A," and Wildlife :",pCAW)
    #print(A," and Adventure :",pCAA)
    #print(A," and Shopping :",pCAS)

    countQualificationHistorical = 0
    countQualificationReligious = 0
    countQualificationWildlife = 0
    countQualificationAdventure = 0
    countQualificationShopping = 0

    for i in range(len(df)):
        if df["Qualification"][i]== Q and df["Area_of_Interest"][i]=="Historical":
            countQualificationHistorical+=1
        elif df["Qualification"][i]== Q and df["Area_of_Interest"][i]=="Religious":
            countQualificationReligious+=1
        elif df["Qualification"][i]== Q and df["Area_of_Interest"][i]=="Wildlife":
            countQualificationWildlife+=1
        elif df["Qualification"][i]== Q and df["Area_of_Interest"][i]=="Adventure":
            countQualificationAdventure+=1
        elif df["Qualification"][i]== Q and df["Area_of_Interest"][i]=="Shopping":
            countQualificationShopping+=1
        
    pCQH = countQualificationHistorical/countHistorical
    pCQR = countQualificationReligious/countReligious
    pCQW = countQualificationWildlife/countWildlife
    pCQA = countQualificationAdventure/countAdventure
    pCQS = countQualificationShopping/countShopping
    #print(Q," and Historical:",pCQH)
    #print(Q," and Religious :",pCQR)
    #print(Q," and Wildlife :",pCQW)
    #print(Q," and Adventure :",pCQA)
    #print(Q," and Shopping :",pCQS)

    countGenderHistorical = 0
    countGenderReligious = 0
    countGenderWildlife = 0
    countGenderAdventure = 0
    countGenderShopping = 0

    for i in range(len(df)):
        if df["Gender"][i]== G and df["Area_of_Interest"][i]=="Historical":
            countGenderHistorical+=1
        elif df["Gender"][i]== G and df["Area_of_Interest"][i]=="Religious":
            countGenderReligious+=1
        elif df["Gender"][i]== G and df["Area_of_Interest"][i]=="Wildlife":
            countGenderWildlife+=1
        elif df["Gender"][i]== G and df["Area_of_Interest"][i]=="Adventure":
            countGenderAdventure+=1
        elif df["Gender"][i]== G and df["Area_of_Interest"][i]=="Shopping":
            countGenderShopping+=1
        
    pCGH = countGenderHistorical/countHistorical
    pCGR = countGenderReligious/countReligious
    pCGW = countGenderWildlife/countWildlife
    pCGA = countGenderAdventure/countAdventure
    pCGS = countGenderShopping/countShopping
    #print(G," and Historical:",pCGH)
    #print(G," and Religious :",pCGR)
    #print(G," and Wildlife :",pCGW)
    #print(G," and Adventure :",pCGA)
    #print(G," and Shopping :",pCGS)

    countHobbyHistorical = 0
    countHobbyReligious = 0
    countHobbyWildlife = 0
    countHobbyAdventure = 0
    countHobbyShopping = 0

    for i in range(len(df)):
        if df["Hobby"][i]== H and df["Area_of_Interest"][i]=="Historical":
            countHobbyHistorical+=1
        elif df["Hobby"][i]== H and df["Area_of_Interest"][i]=="Religious":
            countHobbyReligious+=1
        elif df["Hobby"][i]== H and df["Area_of_Interest"][i]=="Wildlife":
            countHobbyWildlife+=1
        elif df["Hobby"][i]== H and df["Area_of_Interest"][i]=="Adventure":
            countHobbyAdventure+=1
        elif df["Hobby"][i]== H and df["Area_of_Interest"][i]=="Shopping":
            countHobbyShopping+=1
        
    pCHH = countHobbyHistorical/countHistorical
    pCHR = countHobbyReligious/countReligious
    pCHW = countHobbyWildlife/countWildlife
    pCHA = countHobbyAdventure/countAdventure
    pCHS = countHobbyShopping/countShopping
    #print(H," and Historical:",pCHH)
    #print(H," and Religious :",pCHR)
    #print(H," and Wildlife :",pCHW)
    #print(H," and Adventure :",pCHA)
    #print(H," and Shopping :",pCHS)

    countBudgetHistorical = 0
    countBudgetReligious = 0
    countBudgetWildlife = 0
    countBudgetAdventure = 0
    countBudgetShopping = 0

    for i in range(len(df)):
        if df["Budget"][i]== B and df["Area_of_Interest"][i]=="Historical":
            countBudgetHistorical+=1
        elif df["Budget"][i]== B and df["Area_of_Interest"][i]=="Religious":
            countBudgetReligious+=1
        elif df["Budget"][i]== B and df["Area_of_Interest"][i]=="Wildlife":
            countBudgetWildlife+=1
        elif df["Budget"][i]== B and df["Area_of_Interest"][i]=="Adventure":
            countBudgetAdventure+=1
        elif df["Budget"][i]== B and df["Area_of_Interest"][i]=="Shopping":
            countBudgetShopping+=1
        
    pCBH = countBudgetHistorical/countHistorical
    pCBR = countBudgetReligious/countReligious
    pCBW = countBudgetWildlife/countWildlife
    pCBA = countBudgetAdventure/countAdventure
    pCBS = countBudgetShopping/countShopping
    #print(B," and Historical:",pCBH)
    #print(B," and Religious :",pCBR)
    #print(B," and Wildlife :",pCBW)
    #print(B," and Adventure :",pCBA)
    #print(B," and Shopping :",pCBS)

    countClimateHistorical = 0
    countClimateReligious = 0
    countClimateWildlife = 0
    countClimateAdventure = 0
    countClimateShopping = 0

    for i in range(len(df)):
        if df["Climate"][i]== C and df["Area_of_Interest"][i]=="Historical":
            countClimateHistorical+=1
        elif df["Climate"][i]== C and df["Area_of_Interest"][i]=="Religious":
            countClimateReligious+=1
        elif df["Climate"][i]== C and df["Area_of_Interest"][i]=="Wildlife":
            countClimateWildlife+=1
        elif df["Climate"][i]== C and df["Area_of_Interest"][i]=="Adventure":
            countClimateAdventure+=1
        elif df["Climate"][i]== C and df["Area_of_Interest"][i]=="Shopping":
            countClimateShopping+=1
        
    pCCH = countClimateHistorical/countHistorical
    pCCR = countClimateReligious/countReligious
    pCCW = countClimateWildlife/countWildlife
    pCCA = countClimateAdventure/countAdventure
    pCCS = countClimateShopping/countShopping
    #print(C," and Historical:",pCCH)
    #print(C," and Religious :",pCCR)
    #print(C," and Wildlife :",pCCW)
    #print(C," and Adventure :",pCCA)
    #print(C," and Shopping :",pCCS)

    # Step3 : Put values in Bayes Formula and get the Posterior Probability

    l = len(df)
    valueHistorical = (pCMH*pCAH*pCQH*pCGH*pCHH*pCBH*pCCH*countHistorical)/l
    valueReligious = (pCMR*pCAR*pCQR*pCGR*pCHR*pCBR*pCCR*countReligious)/l
    valueWildlife = (pCMW*pCAW*pCQW*pCGW*pCHW*pCBW*pCCW*countWildlife)/l
    valueAdventure = (pCMA*pCAA*pCQA*pCGA*pCHA*pCBA*pCCA*countAdventure)/l
    valueShopping = (pCMS*pCAS*pCQS*pCGS*pCHS*pCBS*pCCS*countShopping)/l

    total = valueHistorical + valueReligious + valueWildlife + valueAdventure  + valueShopping
    
    vh = valueHistorical/total
    vr = valueReligious/total
    vw = valueWildlife/total
    va = valueAdventure/total
    vs = valueShopping/total

    result = []
    #result_1 = [vh,vr,vw,va,vs]

    # Step4 : Select the class with the highest probability.

    m = max(vh,vr,vw,va,vs)
    result.append(m)
    if m==vh:
        result.append('Historical')
    elif m==vr:
        result.append('Religious')
    elif m==vw:
        result.append('Wildlife')
    elif m==va:
        result.append('Adventure')
    else:
        result.append('Shopping')
    print()
    print('Naive Bayes prediction:',result[1])
    print()
    return result


    #print(valueHistorical/total)
    #print(valueReligious/total)
    #print(valueWildlife/total)
    #print(valueAdventure/total)
    #print(valueShopping/total)
