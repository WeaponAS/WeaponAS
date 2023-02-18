import mysql.connector as sql
import MonthName
import time
import datetime as date
conn=sql.connect(host='localhost',user='root',passwd='0')
conn.autocommit=True
if conn.is_connected():
    print('\n Connected Succesfully')
else:
    print('\n Not Connected')
c1=conn.cursor()
#######################################################
while True:
    print("\t\t\t\tMain Menu")
    print('Balance : ')
    print('\n\n1> Record Entry')
    print('2> analyse previous records')
    print('3> ')
    print('9> Setup (need to perform every month)')
    print('0) Quit Program')
########################################################
    act=int(input('Enter Action to be performed (0-3) : '))
    if act==1:
        Paticular=input('Enter Particular : ')
        NOTE=input('Enter Note to the Account : ')
        Outflow=float(input('Enter Outflow Amount : '))
        Inflow=float(input('Enter Inflow Amount : '))
        Date,Y,M,D = MonthName.dateconv()
        MN=MonthName.monthname(M)
        c1.execute('insert into table {}_{} values({},{},{},{},{})'.format(MN,Y,Date,Paticular,NOTE,Outflow,Inflow))
    
    
    elif act==2:
        print('1) Date wise\n2) Particular wise\n3) Month wise \n4) Year wise')
        try:
            SubOption=int(input('How Your want to See records : '))
        except:
            print('Type given Interger only')
        
        
        if SubOption==1:
            Year=int(input("Which Year's Record : "))
            Month=int(input('Enter Month No.(1-12) : '))
            MN=MonthName.monthname(Month)
            print('For Search : ')
            Date=MonthName.dateconv()
            print('1) Default\n2) Between\n3) Two Conditions\n0) Exit')
            DateWiseOption=int(input('Enter One Option (0-3): '))

            if DateWiseOption==1:
                a=c1.execute('select * from {}_{} where Date="{}"'.format(MN,Year,Date))
                for i in a:
                    print(a)


            elif DateWiseOption==2:
                Date2=MonthName.dateconv()
                a=c1.execute('select * from {}_{} where Date between {} and {}'.format(MN,Year,Date,Date2))
                for i in a:
                    print(a)


            elif DateWiseOption==3:
                print('Column Name:\n\tDate , Particular, Outflow, Inflow')
                Condition2nd=input('Enter Column Name (mentioned above) to Take another condition : ')

                if Condition2nd.upper()=='DATE':
                    And_Or=input('How Do You You Want to apply conditions (AND / OR ) : ')
                    print('For Another Condition')
                    Date2=MonthName.dateconv()

                    if And_Or.upper()=='AND':
                        a=c1.execute('select * from {}_{} where Date = "{}" and Date = "{}"'.format(MN,Year,Date,Date2))
                        for i in a:
                            print(a)

                    elif And_Or.upper()=='OR':
                        a=c1.execute('select * from {}_{} where Date = "{}" or Date="{}"'.format(MN,Year,Date,Date2))
                        for i in a:
                            print(a)
                    else:
                        print('Not a valid input')

                elif Condition2nd.upper()=='PARTICULAR':
                    print('Enter Particular Name to search for phase in the name')
                    PaticularLike=input('Enter Particular Name : ')
                    a=c1.execute('select * from {}_{} where Particular like "%{}%"'.format(MN,Year,PaticularLike))
                    for i in a:
                        print(a)

                elif Condition2nd.upper()=='OUTFLOW':
                    while True:
                        print('1) BETWEEN\t2) More than\t3) less than\t4) NULL values\t5) Equal To\n0) Exit')
                        OutflowRange=int(input('Enter Your Choice (0-5): '))
                        
                        if OutflowRange==1:
                            AMT1=int(input('Show Records Between This Amount : '))
                            AMT2=int(input('And This Amount : '))
                            a=c1.execute('select * from {}_{} where Outflow between {} and {}'.format(MN,Year,AMT1,AMT2))
                            for i in a:
                                print(a)
                            break
                        elif OutflowRange==2:

                            AMT1=int(input('Show Records Greater Than This Amount : '))
                            a=c1.execute('select * from {}_{} where Outflow > {}'.format(MN,Year,AMT1))
                            for i in a:
                                print(a)
                            break
                        
                        elif OutflowRange==3:
                            AMT1=int(input('Show Records Less than this Amount : '))
                            a=c1.execute('select * from {}_{} where Outflow between {} and {}'.format(MN,Year,AMT1,AMT2))
                            for i in a:
                                print(a)
                            break
                        
                        elif OutflowRange==4:
                            a=c1.execute('select * from {}_{} where Outflow is NULL'.format(MN,Year))
                            for i in a:
                                print(a)
                            break
                        
                        elif OutflowRange==5:
                            AMT1=int(input('Show Records Equal to this amount : '))
                            a=c1.execute('select * from {}_{} where Outflow ={}'.format(MN,Year,AMT1))
                        
                        elif Outflow==0:
                            break
                        
                        else:
                            print('Not a Valid Input')
    elif act==3:
        print("Nothing to show")
        pass
    elif act==9:
        try:
            c1.execute('create database if not exists Journal')
            c1.execute('use journal')
            while True:
                try:
                    Month=int(input('Enter Month No.(1-12) : '))
                except:
                    print('Type integer only')
                if Month>12 or Month<0:
                    print('Not Valid Month')
                else:
                    break
            Year=int(input('Enter Year (yyyy): '))
            MN=MonthName.monthname(Month)
            c1.execute('create table if not exists {}_{}(Date date,Particulat varchar(1000),Note varchar(2000),Outflow int,Inflow int)'.format(MN,Year))
        except:
            print('Somthing is not Right')