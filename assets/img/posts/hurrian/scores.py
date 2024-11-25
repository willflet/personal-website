import abjad

hymn = [
    [[5,2],3], [[2,7],1], [[5,2],3], [[7,5],1], [[3,5],10],
    [[3,5],2], [[4,6],1], [[7,5],2], [[1,6],2], [[2,7],2],
    [[3,7],1], [[1,6],2], [[2,7],1], [[4,1],1], [[2,4],1], [[3,5],4],
    [[4,6],1], [[7,5],2], [[1,6],4], [[2,7],1], [[4,1],1], [[7,5],1],
    [[1,6],4], [[7,5],1], [[1,6],2], [[7,5],1], [[1,6],2], [[2,7],2],
    [[6,3],2], [[5,2],3], [[6,3],1], [[5,2],4], [[6,3],1], [[5,2],2]
]

pitches = {1:"e''",2:"d''",3:"c''",4:"b'",5:"a'",6:"g'",7:"f'",8:"e'",9:"d'",10:"c'"}

QUAVER = abjad.Duration(1,8)
CROTCHET = 2*QUAVER

staff = abjad.Staff()
for (interval, length) in hymn:
    for i in range(length):
        staff.append(abjad.Note(pitches[interval[1]], CROTCHET))
        if interval[1] in (1,2):
            low_note = abjad.NoteHead(pitches[interval[1]+7])
            abjad.tweak(low_note).font_size = -3
            chord = abjad.Chord([], CROTCHET)
            chord.note_heads.extend([staff[-1].note_head, low_note])
            staff[-1] = chord

abjad.attach(abjad.TimeSignature((18, 4)), staff[0])
abjad.attach(abjad.TimeSignature((9, 4)), staff[18])
abjad.attach(abjad.TimeSignature((10, 4)), staff[27])
abjad.attach(abjad.TimeSignature((10, 4)), staff[37])
abjad.attach(abjad.TimeSignature((12, 4)), staff[47])
abjad.attach(abjad.TimeSignature((13, 4)), staff[59])

score = abjad.Score([staff])
score.add_final_bar_line()
abjad.show(score)
