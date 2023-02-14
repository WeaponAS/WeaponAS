import datetime
def monthname(Date):
    if Date==1:
        MN='January'
    elif Date==2:
        MN='February'
    elif Date==3:
        MN='March'
    elif Date==4:
        MN='April'
    elif Date==5:
        MN='May'
    elif Date==6:
        MN='June'
    elif Date==7:
        MN='July'
    elif Date==8:
        MN='August'
    elif Date==9:
        MN='September'
    elif Date==10:
        MN='October'
    elif Date==11:
        MN='November'
    elif Date==12:
        MN='December'
    else:
        print("Month Can't go above 12 and below 1")
    return MN

def dateconv():
    Y=int(input('Year (YYYY): '))
    M=int(input('Month (MM): '))
    D=int(input('Date (DD): '))
    Date=datetime.datetime(Y,M,D)
    return Date
    

def Dayname(Dayname):
    if Dayname == 1:
        DN = "Sunday"
    elif Dayname ==2:
        DN="Monday"
    elif Dayname==3:
        DN="Tuesday"
    elif Dayname==4:
        DN="Wednesday"
    elif Dayname==5:
        DN="Thursday"
    elif Dayname==6:
        DN="Friday"
    elif Dayname==7:
        DN="Saturday"
    else:
        print("Week have a only 7 Days, Maybe you are from another planet ?")
    return DN