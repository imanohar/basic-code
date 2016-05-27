h=raw_input('Input work hours:\n')
r=raw_input('Input hourly rate:\n')

def computepay(h,r):
    try:
        if float(h) > 40:
            p = (40*float(r))+((float(h)-40) * float(r)*1.5) 
        elif float(h)<=40:
            p=float(h)*float(r)
        print "Here's how much you made:"
        print p
    except:
        print "Error, please input valid numerals."


    again = raw_input("Would you like to try again? y/n\n")
    if str.lower(again) == "y":
        h=raw_input('Input work hours:\n')
        r=raw_input('Input hourly rate:\n')
        computepay(h,r)
    elif str.lower(again) == "n":
        print "Ok, goodbye."
    else:
        print "Huh? Ok bai."

computepay(h,r)
