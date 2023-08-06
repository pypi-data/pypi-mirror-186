#### This is a module contains functions to find speed, distance or time if other two are given ####

###############  Enter distance in km as int and time in (hours,minutes) as a tupple  ###############

def getSpeed(distance,time):
    h,m = time
    ntime = ((h*60) + m)/60
    speed = distance/ntime
    return str(speed) + ' km/h'

##############################  Enter speed in km/h and distance in km  ##############################

def getTime(speed,distance):
    val = distance/speed
    return convertToHMSFormat(val)

################  Enter speed in km/h as int and time in (hours,minutes) as a tupple  #################

def getDistance(speed,time):
    h,m = time
    ntime = ((h*60) + m)/60
    distance = speed * ntime
    return str(distance) + ' km'

##################### A function to convert value into hours:minutes:seconds format  ###################

def convertToHMSFormat(val):
    sec = val * 3600
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    min = sec // 60
    sec %= 60
    return "%02d:%02d:%02d" % (hour, min, sec) 

######################################################################################################





