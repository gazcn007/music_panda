from utilities import keysign, removeDups
def invKeysign(num):
    if num%12==1: return'C'
    elif num%12==2: return 'C#/Db'
    elif num%12==3: return'D'
    elif num%12==4: return'D#/Eb'
    elif num%12==5: return'E'
    elif num%12==6: return'F'
    elif num%12==7: return'F#/Gb'
    elif num%12==8: return'G'
    elif num%12==9: return'G#/Ab'
    elif num%12==10: return'A'
    elif num%12==11: return'A#/Bb'
    elif num%12==0: return'B'

def make(quality,bass):
    return str (quality+' '+bass)

def chordCheck(interval,bass):
    if interval == [7]:
        return make ("Major5", invKeysign(bass))
    elif interval == [5]:
        return make ("Major5 1st inversion", invKeysign(bass+5))
    elif interval == [4,7]:
        return make("Major",invKeysign(bass))
    elif interval == [3,8]:
        return make("Major 1st inversion",invKeysign(bass+8))
    elif interval == [5,9]:
        return make("Major 2nd inversion",invKeysign(bass+5))
    elif interval == [3,7]:
        return make("Minor",invKeysign(bass))
    elif interval == [4,9]:
        return make("Minor 1st inversion",invKeysign(bass+9))   
    elif interval == [5,8]:
        return make("Minor 2nd inversion",invKeysign(bass+5)) 
    elif interval == [4,7,11]:
        return make("Major7",invKeysign(bass))   
    elif interval == [3,7,8]:
        return make("Major7 1st inversion",invKeysign(bass+8)) 
    elif interval == [4,5,9]:
        return make("Major7 2nd inversion",invKeysign(bass+5))   
    elif interval == [1,5,8]:
        return make("Major7 3rd inversion",invKeysign(bass+1))
    elif interval == [4,7,10]:
        return make("Dom7",invKeysign(bass))   
    elif interval == [3,6,8]:
        return make("Dom7 1st inversion",invKeysign(bass+8)) 
    elif interval == [3,5,9]:
        return make("Dom7 2nd inversion",invKeysign(bass+5))   
    elif interval == [2,6,9]:
        return make("Dom7 3rd inversion",invKeysign(bass+2)) 
    elif interval == [3,7,10]:
        return make("Minor7",invKeysign(bass))   
    elif interval == [4,7,9]:
        return make("Minor7 1st inversion",invKeysign(bass+9)) 
    elif interval == [3,6,9]:
        return make("Minor7 2nd inversion",invKeysign(bass+6))   
    elif interval == [3,6,10]:
        return make("Minor7 3rd inversion",invKeysign(bass+3))
    elif interval == [3,7,9]:
        return make("Dimished7",invKeysign(bass))   
    elif interval == [4,6,9]:
        return make("Dimished7 1st inversion",invKeysign(bass+9)) 
    elif interval == [2,6,9]:
        return make("Dimished7 2nd inversion",invKeysign(bass+6))   
        #<check>
    elif interval == [2,5,10]:
        return make("Dimished7 3rd inversion",invKeysign(bass+4))
        #</check>
    elif interval == [4,6,10]:
        return make("Dominant7 b5",invKeysign(bass))
    elif interval == [4,8,10]:
        return make("Dominant7 #5",invKeysign(bass))
    elif interval == [4,7,10,13]:
        return make("Dominant7 b9",invKeysign(bass))
    elif interval == [4,7,10,15]:
        return make("Dominant7 #9",invKeysign(bass))
    elif interval == [4,6,10,13]:
        return make("Dominant7 b5 b9",invKeysign(bass))
    elif interval == [4,8,10,15]:
        return make("Dominant7 #5 #9",invKeysign(bass))
    elif interval == [4,6,10,15]:
        return make("Dominant7 b5 #9",invKeysign(bass))
    elif interval == [4,8,10,13]:
        return make("Dominant7 #5 b9",invKeysign(bass))
    elif interval == [4,7,10,18]:
        return make("Dominant7 #11",invKeysign(bass))
    elif interval == [4,6,10,13]:
        return make("Dominant9 b5",invKeysign(bass))
    elif interval == [4,8,10,14]:
        return make("Dominant9 #5",invKeysign(bass))
    elif interval == [4,7,10,14,18]:
        return make("Dominant9 #11",invKeysign(bass))
    elif interval == [4,7,10,13,17,21]:
        return make("Dominant13 b9",invKeysign(bass))
    elif interval == [4,7,10,15,17,21]:
        return make("Dominant13 #9",invKeysign(bass))
    elif interval == [4,7,10,14,18,21]:
        return make("Dominant13 #11",invKeysign(bass))
    elif interval == [3,6,10]:
        return make("Minor7 b5",invKeysign(bass))
    elif interval == [3,8,10]:
        return make("Minor7 #5",invKeysign(bass))
    elif interval == [4,6,11]:
        return make("Major7 b5",invKeysign(bass))
    elif interval == [4,8,11]:
        return make("Major7 #5",invKeysign(bass))
    elif interval == [4,7,11,18]:
        return make("Major7 #11",invKeysign(bass))
    elif interval == [4,7,11,14,18]:
        return make("Major9 #11",invKeysign(bass))
    elif interval == [4,7,9]:
        return make("Major6",invKeysign(bass))
    elif interval == [3,7,9]:
        return make("Minor6",invKeysign(bass))
    elif interval == [2,4,7,9]:
        return make("Major6/9",invKeysign(bass))
    elif interval == [2,7]:
        return make("Sus2",invKeysign(bass))
    elif interval == [5,7]:
        return make("Sus4",invKeysign(bass))
    elif interval == [5,7,10]:
        return make("Dom7Sus4",invKeysign(bass))
    elif interval == [2,4,7]:
        return make("Major9",invKeysign(bass))
    elif interval == [3,4,7]:
        return make("Minor9",invKeysign(bass))
    else:
        return "wrong"

def getChord(step,octave,alter):
    temp=[]
    for i in range(0,len(step)):
            temp.append(keysign(step[i],octave[i],alter[i]))
    temp.sort()
    bassNote=(temp[0])
    interval=[]
    for i in range(0,len(temp)-1):
            if ((temp[i+1]-temp[0])<12):
                interval.append(temp[i+1]-temp[0])
            else:
                if((temp[i+1]-temp[0])%12!=0):
                    interval.append((temp[i+1]-temp[0])%12)
    
    interval.sort()
    removeDups(interval)
    if chordCheck(removeDups(interval),bassNote)=="wrong":
        temp=""
        for i in range(0,len(step)):
            temp+=step[i]
            if alter[i]==1:
                temp+="#"
            elif alter[i]==-1:
                temp+="b"
            if i!=len(step)-1:
                temp+="^"
        return temp
    else:
        return chordCheck(removeDups(interval),bassNote);



