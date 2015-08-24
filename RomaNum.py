from utilities import keysign1,keysign
def getRoma(note,key):
    
    interval=keysign1(note) - keysign1(key)+1
    if interval <0:
        interval=12+interval+1
    if interval==1: return'I'
    elif interval==2: return 'bII'
    elif interval==3: return'II'
    elif interval==4: return'bIII'
    elif interval==5: return'III'
    elif interval==6: return'IV'
    elif interval==7: return'bV'
    elif interval==8: return'V'
    elif interval==9: return'bVI'
    elif interval==10: return'VI'
    elif interval==11: return'bVII'
    elif interval==12: return'VII'
    elif interval==0: return'VII'

def getRoma1(note,key):
    print note
    interval=keysign1(note) - keysign1(key)+1
    if interval <0:
        interval=12+interval+1
    if interval==1: return'1'
    elif interval==2: return 'b2'
    elif interval==3: return'2'
    elif interval==4: return'b3'
    elif interval==5: return'3'
    elif interval==6: return'4'
    elif interval==7: return'b5'
    elif interval==8: return'5'
    elif interval==9: return'b6'
    elif interval==10: return'6'
    elif interval==11: return'b7'
    elif interval==12: return'7'
    elif interval==0: return'7'


def convertToRomaNum (stepArray, key):
    toReturn =[] #of strings
    for i in range (0,len(stepArray)):
            if " " in stepArray[i]:
                pre=' '.join(stepArray[i].replace("'",'').split()[:-1])
                after=getRoma(stepArray[i].replace("'",'').split()[-1],key)
                toReturn.append(pre+" "+after)
               
            elif "^" in stepArray[i]:
                temp=''
                for c in stepArray[i].split("^"):
                    if c==stepArray[i].split("^")[len(stepArray[i].split("^"))-1]:
                        temp+=getRoma1(c.replace("'",''),key)
                    else:
                        temp+=getRoma1(c.replace("'",''),key)+'^'
                toReturn.append(temp)
            else:
                temp=getRoma1(stepArray[i].replace("'",""),key)
                toReturn.append(temp)
    return toReturn
            
