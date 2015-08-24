def keysign(step, octave, alter):
    if step=='C':
        return 1+12*octave+alter
    elif step=='D':
        return 3+12*octave+alter
    elif step=='E':
        return 5+12*octave+alter
    elif step=='F':
        return 6+12*octave+alter
    elif step=='G':
        return 8+12*octave+alter
    elif step=='A':
        return 10+12*octave+alter
    elif step=='B':
        return 12+12*octave+alter

def keysign1(key):
    
    if key=='C': return 1
    elif key=='C#/Db': return 2
    elif key=='C#': return 2
    elif key=='Db': return 2
    elif key=='D': return 3
    elif key=='D#/Eb': return 4
    elif key=='D#': return 4
    elif key=='Eb': return 4
    elif key=='E': return 5
    elif key=='E#': return 5
    elif key=='Fb': return 5
    elif key=='F': return 6
    elif key=='F#/Gb': return 7
    elif key=='F#': return 7
    elif key=='Gb': return 7
    elif key=='G': return 8
    elif key=='G#/Ab': return 9
    elif key=='G#': return 9
    elif key=='Ab': return 9
    elif key=='A': return 10
    elif key=='A#/Bb': return 11
    elif key=='A#': return 11
    elif key=='Bb': return 11
    elif key=='B': return 12
    elif key=='B#': return 12
    elif key=='Cb': return 12

def removeDups(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def keyCheck (fifths,mode): 
    if mode == 'major':
        if fifths == 0: return 'C'
        elif fifths == 1: return 'G'
        elif fifths == 2: return 'D'
        elif fifths == 3: return 'A'
        elif fifths == 4: return 'E'
        elif fifths == 5: return 'B'
        elif fifths == -1: return 'F'
        elif fifths == -2: return 'A#/Bb'
        elif fifths == -3: return 'D#/Eb'
        elif fifths == -4: return 'G#/Ab'
        elif fifths == -5: return 'C#/Db'
        elif fifths == -6: return 'F#/Gb'
    elif mode == 'minor':
        if fifths == 0: return 'A'
        elif fifths == 1: return 'E'
        elif fifths == 2: return 'B'
        elif fifths == 3: return 'F#/Gb'
        elif fifths == 4: return 'C#/Db'
        elif fifths == 5: return 'G#/Ab'
        elif fifths == -1: return 'D'
        elif fifths == -2: return 'G'
        elif fifths == -3: return 'C'
        elif fifths == -4: return 'F'
        elif fifths == -5: return 'A#/Bb'
        elif fifths == -6: return 'D#/Eb'
