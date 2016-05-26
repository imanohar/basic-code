print "Greetings! This your friendly Celsius to Fahrenheit temperature converter."
cel=raw_input("What's the current temperature in Celsius?\n")

try:
    fahr=float(cel)* float(9/5) + 32
    print "It's "+str(float(fahr))+" degrees Fahrenheit..."
    if float(cel)>=40:
        print "Woah, many heat it is."
    elif float(cel)>=35 and float(cel)<=39:
        print "Damn hot..."
    elif float(cel)<=34 and float(cel)>=28:
        print 'Swalpa sweating aagtha idhe... '
    elif float(cel)<=27 and float(cel)>=15:
        print 'Damn cool...'
    elif float(cel)<=15 and float(cel)>=5:
        print 'Many cold it is.'
    elif float(cel)<=5:
        print 'Macchaaa, freezing ra!'
except:
    print 'Dude, type a valid degree in Celsius, ra.'

que=raw_input("Do you need to convert another temperature? y/n\n")
try:
    if str(que)==str('y'):
        cel=raw_input("What's the current temperature in Celsius?\n")
        try:
            fahr=float(cel)* float(9/5) + 32
            print "It's "+str(float(fahr))+" degrees Fahrenheit..."
            if float(cel)>=40:
                print "Woah, many heat it is."
            elif float(cel)>=35 and float(cel)<=39:
                print "Damn hot..."
            elif float(cel)<=34 and float(cel)>=28:
                print 'Swalpa sweating aagtha idhe... '
            elif float(cel)<=27 and float(cel)>=15:
                print 'Damn cool...'
            elif float(cel)<=15 and float(cel)>=5:
                print 'Many cold it is.'
            elif float(cel)<=5:
                print 'Macchaaa, freezing ra!'
        except:
            print 'Dude, type a valid degree in Celsius, ra.'
    elif str(que)==str('n'):
        print "Ok, goodbye!"
except:
    print "Eh? OK bai."
