s = input("Enter time in 12 hr format: ")  #hh:mm:ssAP/PM format
hh,mm,ss = map(int,s[:-2].split(":"))
p = s[-2:]
if hh <= 12 and (mm <= 60 and ss <= 60):
    hh = hh%12
    if p=="PM":
        hh = hh + 12
        print(str("%02d")%hh +":"+str('%02d')%mm +":"+str('%02d')%ss)
    else:
        print(str("%02d")%hh+":"+str("%02d")%mm+":"+str("%02d")%ss)
else:
    print("Invalid time")
