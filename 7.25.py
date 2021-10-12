#JAKE BILLARD UHID 1582534

def exact_change_cash(cash_total):
    #Dollars
    dollar_num = cash_total // 100
    cash_total %= 100
    #Quarters
    quarter_num = cash_total // 25
    cash_total %= 25
    #Dimes
    dime_num = cash_total // 10
    cash_total %= 10
    #Nickels
    nickel_num = cash_total // 5
    cash_total %= 5
    #Pennies
    penny_num = cash_total

    return (dollar_num, quarter_num, dime_num, nickel_num, penny_num)

#Required
if __name__ == '__main__':
    inputvalue = int(input())
    dollar_num, quarter_num, dime_num, nickel_num, penny_num = exact_change_cash(inputvalue)

    if inputvalue <=0:
        print("no change")  #If Input is Less than 0
    else:
        #Dollars
        if dollar_num > 1:
            print("%d dollars" % dollar_num)
        elif dollar_num == 1:
            print("%d dollar" % dollar_num)
        #Quarters
        if quarter_num > 1:
            print("%d quarters" % quarter_num)
        elif quarter_num == 1:
            print("%d quarter" % quarter_num)
        #Dimes
        if dime_num > 1:
            print("%d dimes" % dime_num)
        elif dime_num == 1:
            print("%d dime" % dime_num)
        #Nickels
        if nickel_num > 1:
            print("%d nickels" % nickel_num)
        elif nickel_num == 1:
            print("%d nickel" % nickel_num)
        #Pennies
        if penny_num > 1:
            print("%d pennies" % penny_num)
        elif penny_num == 1:
            print("%d penny" % penny_num)
