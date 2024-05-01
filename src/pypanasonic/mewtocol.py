# Required libs: Regex
import re

#Variation Checker here
def formatCheck(inputs):
    result = False
    if (len(inputs) != 5):
        print("Wrong parameter input, the correct length should be 4, example R0000")
    else:
        matches = re.match('^[RXYT]\d{4}$', inputs)
        if (matches):
            result = True
        else:
            print("Wrong input, the correct should start wit either X,Y,R,T follow by 4 digit")
    return result


# There switches only accepts X,R,Y,T
# There are 4 char of the switch no
# Example, X0010, Y1200
def switchSingleOn(RelayToOperate):
    if(not formatCheck(RelayToOperate)):
        exit()
    return "%EE#WCS" + RelayToOperate + "1**" + "\r"


#Switch off
def switchSingleOff(RelayToOperate):
    if(not formatCheck(RelayToOperate)):
        exit()
    return "%EE#WCS" + RelayToOperate + "0**" + "\r"

def ReadSingleSwitch(RelayToOperate):
    if(not formatCheck(RelayToOperate)):
        exit()
    return "%EE#RCS" + RelayToOperate + "**" + "\r"


#Here is operate multiple switches
def readMultiSwitch(StartSW, EndSW):
    if(not formatCheck(StartSW)):
        exit()
    if(not formatCheck(EndSW)):
        exit()
    return "%EE#RCP" + StartSW + EndSW + "**" + "\r"


# Switch on multiple relays, define a range
# Example switchMultiOn("R0001","R0100")
def switchMultiOn(StartSW, EndSW):
    if(not formatCheck(StartSW)):
        exit()
    if(not formatCheck(EndSW)):
        exit()
    return "%EE#WCP" + "1**" + "\r"


#Read Register
#Example readDT(100,105), read DT100~DT105
def readDT(Start,End):
    start1 = re.match('^[0-9]+$',Start)
    end1 = re.match('^[0-9]+$',End)
    if(not start1 or  not end1):
        exit()
    return "%EE#RDD"+str(Start)+str(End)+"**"+"\r"

# Send message to PLC, you could use that for plc connectection test.
def plcVer():
    return "%EE#RT00\r"

