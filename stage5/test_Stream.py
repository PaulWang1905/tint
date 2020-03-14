from music21 import *

aStream = stream.Stream()
src = list(range(12))
src = src[2:4] + src[0:2] + src[8:9]+src[4:8]+src[9:12]
print(src)
for i in range(0,12,3):
    print(src[i:i +3])
    aStream.append(chord.Chord(src[i:i + 3]))

print(aStream)
for c in aStream:
    print(c)
    print(c.orderedPitchClassesString)
a = [0,1,2]
a = chord.Chord(a)

print(a)
