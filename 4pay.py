h=raw_input('Input work hours:\n')
r=raw_input('Input hourly rate:\n')

def computepay(h,r):
    if float(h) > 40:
        p=(40*float(r))+((float(h)-40)*float(r)*1.5)
    elif float(h)<=40:
        p=float(h)*float(r)
    print "Here's how much you made:"
    print p
    again=raw_input("Would you like to make another calculation? y/n\n")
    if again=="y":
        h=raw_input('Input work hours:\n')
        r=raw_input('Input hourly rate:\n')
        computepay(h,r)
    else:
        print "Ok, goodbye."

try:
    computepay(h,r)
except:
    print "Error, please input valid numerals."
    again=raw_input("Would you like to try again?y/n\n")
    if again=="y":
        h=raw_input('Input work hours:\n')
        r=raw_input('Input hourly rate:\n')
        computepay(h,r)
    else:
        print "Ok, goodbye."
