a=int(input("enter the marks:"))
match a:
    case  _ if a>=0 and a<=34:
        print("failed!") 
    case _ if a>=35 and a<=49:
        print("You have got a C")
    case _ if a>=50 and a<=59:
        print("You have got a C+")
    case _ if a>=60 and a<=69:
        print("You have got a B")
    case _ if a>=70 and a<=79:
        print("You have got a B+")
    case _ if a>=80 and a<=89:
        print("You have got an A")
    case _ if a>=90 and a<=99:
        print("You have got an A+")
    case _ if a==100:
        print("You have got an AA")