from ChordBook import chordCheck,getChord
from utilities import keysign1, keysign,removeDups, keyCheck
from RomaNum import getRoma,getRoma1,convertToRomaNum

def xmlparseRomaNum(xml):
    import xml.etree.ElementTree as ET;
    piece = ET.parse(xml)
    root=piece.getroot()
    
    final=[]
    counter=0;

    def make (part,measure,s,o,d,t):
            return {
            "part":part,
            "measure":measure,
            "steps" :s,
            "octave" :o,
            "duration":d,
            "type":t
            }

    class xmlparser ():
            octaveArray=[]
            stepArray=[]
            alterArray=[]
            octaveChordArray=[]
            stepChordArray=[]
            alterChordArray=[]
            durationArray=[]
            duration=0
            Type=''
            TypeArray=[]
            key='C'
            mode='major'
            division=0
            for se in root:
                if se.tag=='part':
                    parts=se.attrib["id"]
                    for measure in se.iter('measure'):
                        measures=measure.attrib["number"]
                        if measure.findall('attributes')!=[]: 
                            for y in measure.findall('attributes'):
                                if y.find('divisions')!=None and duration==0:
                                    division= int(y.find('divisions').text)
                                for s in y.findall('key'):
                                    if s.find('mode') !=None:
                                        mode=s.find('mode').text
                                    key=keyCheck (int(s.find('fifths').text),mode) 
                                #for s in y.findall('time'):
                                 #   print ((s.find('beats').text)+(s.find('beat-type').text))
                                    print key    
                        for x in measure.findall('note'):
                            if(x.findall('chord')!=[]):
                                for q in x.findall('pitch'):
                                    stepChordArray.append(q.find('step').text)
                                    octaveChordArray.append(int(q.find('octave').text))
                                    if (q.find('alter')!=None):
                                        alterChordArray.append(int(q.find('alter').text))
                                    else:
                                        alterChordArray.append(0)
                                duration=int(x.find('duration').text)
                                Type=(x.find('type').text)
                            else:
                                
                                if(len(alterChordArray)>=2):
                                    stepArray.append(getChord(stepChordArray,octaveChordArray,alterChordArray))
                                    octaveArray.append(min(octaveChordArray))
                                    durationArray.append(duration)
                                    TypeArray.append(Type)
                                    octaveChordArray=[]
                                    stepChordArray=[]
                                    alterChordArray=[]
                                elif(len(alterChordArray)==1):
                                    if alterChordArray[0]==0:
                                        stepArray.extend((stepChordArray[0]))
                                    elif alterChordArray[0]==1:
                                        stepArray.append((stepChordArray[0])+'#')
                                    elif alterChordArray[0]==-1:
                                        stepArray.append((stepChordArray[0])+'b')
                                    octaveArray.append(octaveChordArray[0])
                                    durationArray.append(duration)
                                    TypeArray.append(Type)
                                    octaveChordArray=[]
                                    stepChordArray=[]
                                    alterChordArray=[]
                                for q in x.findall('pitch'):
                                    stepChordArray.append(q.find('step').text)
                                    octaveChordArray.append(int(q.find('octave').text))
                                    if (q.find('alter')!=None):
                                        alterChordArray.append(int(q.find('alter').text))
                                    else:
                                        alterChordArray.append(0)
                                if x.find('duration')!=None:
                                    duration=int(x.find('duration').text)
                                    Type=(x.find('type').text)
                        if(len(alterChordArray)>=2):
                            stepArray.append(getChord(stepChordArray,octaveChordArray,alterChordArray))
                            octaveArray.append(min(octaveChordArray))
                            durationArray.append(duration)
                            TypeArray.append(Type)
                            octaveChordArray=[]
                            stepChordArray=[]
                            alterChordArray=[]
                        elif len(alterChordArray)==1:
                            if alterChordArray[0]==0:
                                stepArray.extend((stepChordArray[0]))
                            elif alterChordArray[0]==1:
                                stepArray.append((stepChordArray[0])+'#')
                            elif alterChordArray[0]==-1:
                                stepArray.append((stepChordArray[0])+'b')
                            octaveArray.extend((octaveChordArray))
                            alterArray.extend((alterChordArray))
                            durationArray.append(duration)
                            TypeArray.append(Type)
                            octaveChordArray=[]
                            stepChordArray=[]
                            alterChordArray=[]


                        stepArray=convertToRomaNum (stepArray, key)
                        print stepArray
                        final.append(make(parts,measures,str(stepArray).strip('[]'),str(octaveArray).strip('[]'),str(durationArray).strip('[]'),str(TypeArray).strip('[]')))
                        stepArray=[]
                        octaveArray=[]
                        alterArray=[]
                        durationArray=[]
                        TypeArray=[]
                
    print final
    return final;

def test(xml):
    import xml.etree.ElementTree as ET;
    import ChordBook.py as CB;
    piece = ET.parse(xml)
    root=piece.getroot()
    
    for se in root:
        if se.tag=='part':
            print se.attrib["id"]

temp = xmlparseRomaNum('./SampleXML/beatle.xml')

print temp[0]['measure']
a= "carl"
b="liu"

a=a+b
print a



