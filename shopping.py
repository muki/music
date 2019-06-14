print(Scale.default)

Scale.default = Scale.chromatic

scale = Scale.major

notes = ['p', 7, 6, 5, 4, 3, 2, 5, 4, 3, 2, 1, 0, -1, 0, 1, 2, 0, 1, 2, 3, 0, -1, 3,
         2, 4, 7, 6, 7, 4, 5, 7, 6, 5, 4, 3, 2, 3, 4, 2, 1, 4, 0, 2, 5, 6, 7, 4,
         3.5, 4, 5, 3.5, 2, 4, 1, 3.5, 6, 7, 8, 5, 4, 5, 6, 4, 3, 6, 2, 4, 7, 8, 9, 7,
         5, 6, 7, 8, 9, 4, 3.5, 5, 7, 8, 9, 3.5, 4, 5, 6, 7, 8, 3, 2, 4, 6, 7, 8, 2,
         3.5, 4, 5, 6, 7, 2, 1, 3.5, 5, 6, 7, 5, 6, 11, 10.5, 9, 8, 7, 6, 9, 8, 7, 6, 5,
         4, 3.5, 4, 5, 6, 4, 5, 6, 7, 4, 3.5, 7, 6, 4, 5, 6, 7, 8, 9, 7, 8, 9, 9.5, 11,
         12, 11, 10.5, 9, 8, 7, 6, '1', 7, '1', 5, '1', -10, 4, 3.5, 4, 5, 4, 6, 4, 3.5, 4, 7, 4,
         8, 4, 3.5, 4, 9, 4, 9.5, 8, 7, 6, 5, 4, 9, 10.5, 10.5, '2', 4, 4, '5']
bass_notes = [0, '3', 'p', '1', 7, '3', 6, '1', 5, '3', 4, '1', 3, '1', 1, '1', 4, '1',
        7, '1', 8, '1', 9, '1', 10, '1', 11, '1', 4, '1', 7, '3', 6, '1', 5, '1', 7, '1', 5, '1',
        8, '3', 7, '1', 6, '1', 8, '1', 6, '1', 2, '3', 1, '1', 0, '3', 'p', '1',
        7, '1', 7, '1', 7, '1', 5, '1', 5, '1', 5, '1', 6, '1', 6, '1', 6, '1', 4, '1', 4, '1', 4, '1',
        5, '1', 5, '1', 5, '1', 3.5, '1', 3.5, '1', 3.5, '1', 4, '1', 6, '1', 8, '1', 11, '3', 10.5, '1',
        9, '3', 8, '1', 7, '1', 5, '1', 8, '1', 4, '3', 'p', '1', 7, '3', 'p', '1',
        3.5, '3', 'p', '1', 4, '1', 0, '1', 1, '1', 4, '3', 'p', '3', 4, '1', 5, '1',
        6, '3', 'p', '3', 4, '1', 6, '1', 7, '1', 5, '1', 8, '1', 4, '5']


from generators import Generators
gens = Generators()

mel = gens.generateMelody(notes, scale=Scale.major)
oct = gens.generateOctaves(notes)
dur = gens.generateDurations(notes)
amp = gens.generateAmps(notes, 0.4)

mel2 = gens.generateMelody(bass_notes, scale=Scale.major)
oct2 = gens.generateOctaves(bass_notes)
dur2 = gens.generateDurations(bass_notes)
amp2 = gens.generateAmps(bass_notes, 0.4)

print(sum(dur2))

print(SynthDefs)

Clock.clear()

Clock.bpm = 140

d5 >> play('XXT[XT][XT]X[TT] ', amp=0.2, pan=[-0.8, -0.8, 0.8])
d6 >> play('xxO[xO][xO]xO[xx] ', amp=0.2, pan=[0.8, -0.8, 0.8, 0.8])
d7 >> play('[OO]', amp=0.07).after(4, 'stop')

m3 >> play('[YY]', amp=0.6).after(4, 'stop')
m7 >> play('[ii]', amp=0.07).after(4, 'stop')
c2 >> play('h', dur=1/4, sample=P[:8].rotate([0, 1, 3]), rate=4, pan=linvar([0.5, -0.5], 20), amp=0.2)

m3 >> play('[YY]', amp=0.8).after(4, 'stop')

m7 >> play('[ii]', amp=0.07).after(4, 'stop')
d3 >> play("n", dur=1/4, amp=PWhite(0.1,0.2), rate=PWhite(.98,1.02), pan=linvar([-0.5, 0.5], 20), sample=6)

d4 >> play(' ([ #]  )  ( i )  (  [ii]   )  ', amp=0.3, pan=[0.7, 0.3, -0.7, 0.3, -0.3])

m1 >> play('[   ( b)]       i    ( # [   ib]   [  Nb])  ', amp=0.1, bpm=140)

m1 >> play('[   ( b)]   (  [bb])    i    (  [   ib]   [  Nb])  ', amp=0.15, bpm=140)

m2 >> play('              d( [ d] )f( [ff])  ', amp=0.6)

m3 >> play('[YY]').after(4, 'stop')
d7 >> play('[OO]', amp=0.07).after(4, 'stop')

Group(m1, d4, d5, d4, d3).solo()

m4 >> play(' (    )   ( [  N])   ', amp=0.2)

m5 >> play('     ', amp=0.4)

m7 >> play('([ii i ii][ii]  [iii] [ii])', amp=0.09).after(16, 'stop')
m3 >> play('([YY Y][Y] Y  [YY] )', amp=0.7).after(16, 'stop')
d7 >> play('[OO] [OOO]  ([(OO  )][OOO] )', amp=0.07).after(16, 'stop')

m7 >> play('                [ii][ii][ii][ii]([ii i ii][ii]  [iii] [ii])', amp=0.09).after(32, 'stop')
m3 >> play('[YY][YY] [YY] [Y ][YY][ Y][YY] [YY]  ', amp=0.7).after(32, 'stop')
d7 >> play('[OO][OO][OO][OO]         [OO] [OOOO] ', amp=0.07).after(32, 'stop')

base_m = P[0, 0, 0, 0, 2, 3, 3.5, 4] | P[0, 4, 0, 0, 2, 3, 3.5, 4]
accent_m = P[0, 2, 3, 0, 5, 3, 3.5, 4] | P[0, 0, 0, 0, 5, 3, 3.5, 4] 

base_d = P[1, 0.75, 3.75, 0.25, 0.75, 0.5, 0.5, 0.5]

bridge_m = P[0, 7, 0, 4, 3, 2, 3, 4, 2, 3, 0]
bridge_d = P[1, 0.75, 3.75, 0.25, 0.25, 0.25, 0.25, 0.5, 0.25, 0.25, 0.5]

maj = 0, 2, 4, 5
dim = 0, 1.5, 3.5, 5
dom7 = 0, 3, 5, 7
dim7 = 0,2,4,7

k3.stop()
p1.stop()
k2.stop()
m3 >> play('[YY]', amp=0.8).after(4, 'stop')
d7 >> play('[OO]', amp=0.07).after(4, 'stop')
b1 >> sawbass(P[base_m | base_m | accent_m].stretch(40) | bridge_m,
           dur=base_d.stretch(40) | bridge_d,
           sus=P[base_d.stretch(40) | bridge_d] * 0.2,
           amp=0.4,
#           amp=0.2,
           vib=8,
           vibdepth=0.045,
           delay=4,
           bend=0.05
           )# + P[dim7, dim7, dim7]
k2 >> ambi(amp=0.3, dur=PDur([3, 5], 8) | PDur([1, 7], 8) | PDur([7, 1], 8), bend=linvar([1.2, 1], 40), amplify=0.4, tremolo=3).follow(b1) + var([7, 4, 2, 7, 9, 9, 11, 12, 14, 14, 14, 14], 8) # up to 6
#d7 >> play('[OO]', amp=0.07).after(4, 'stop')
k3 >> ambi(amp=0.4, dur=PDur([3, 5], 8) | PDur([1, 7], 8) | PDur([7, 1], 8), bend=0, sus=0.3, amplify=1).follow(b1) # up to 0.6

k3.stop()
p1.stop()
k2.stop()
m3 >> play('[ii]', amp=0.08).after(4, 'stop')
d7 >> play('[OO]', amp=0.07).after(4, 'stop')
b1 >> sawbass(P[base_m | base_m | accent_m].stretch(40) | bridge_m,
           dur=base_d.stretch(40) | bridge_d,
           sus=P[base_d.stretch(40) | bridge_d] * 0.2,
#           amp=0.4,
           amp=0.2,
           vib=8,
           vibdepth=0.045,
           delay=4,
#           bend=0.3
           ) + P[dim7, dom7, dim7]

m3 >> play('[YY]', amp=0.8).after(4, 'stop')
d7 >> play('[OO]', amp=0.07).after(4, 'stop')

k3.stop()
p1 >> saw(P[base_m | base_m | accent_m].stretch(40),
          dur=base_d.stretch(48) | bridge_d,
          sus=P[base_d.stretch(48) | bridge_d] * 0.8,
          tremolo=0,
          amp=0.2) + P[dim7, dom7, dim7, dim7, dom7]
#          amp=0.5).follow(b2)
#          amp=0.3) + P[dim7, dim7, dim7, dim7, dim7, dim7]

p1.stop()

d7 >> play('[OO]', amp=0.07).after(4, 'stop')
k3 >> ambi(amp=0.4, dur=PDur([3, 5], 8) | PDur([1, 7], 8) | PDur([7, 1], 8), bend=0, sus=0.3, amplify=1).follow(b1) # up to 0.6

k3.amplify = 1

k3.stop()

### vijuge ###
print(linvar([0, 1], 20))

#k2 >> ambi(amp=0.4, dur=PDur([3, 5], 8) | PDur([1, 7], 8) | PDur([7, 1], 8), bend=linvar([1, 0], 48), amplify=linvar([0, 1], 40)).follow(b1)# + var([0, 7, 4, 2, 7, 9, 9, 11, 12, 14, 14, 14, 7], 40)

#k2.amplify = 0

print(var([7, 4, 2, 7, 9, 9, 11, 12, 14, 14, 14, 14], 8))

k3.stop()

k2 >> ambi(amp=0.3, dur=PDur([3, 5], 8) | PDur([1, 7], 8) | PDur([7, 1], 8), bend=linvar([1.2, 1], 40), amplify=0.4, tremolo=3).follow(b1) + var([7, 4, 2, 7, 9, 9, 11, 12, 14, 14, 14, 14], 8) # up to 6

print(linvar([0, 1], 20))

k3.amplify = linvar([0, 1], 20)

k3.amplify = 0

#m3 >> play('[YY]', amp=0.8).after(4, 'stop')
#k1 >> varsaw(amp=0.2, dur=PDur([3, 5], 8) | PDur([1, 7], 8) | PDur([7, 1], 8), bend=1).follow(p1) + 0

#k1.stop()

k2.stop()

k1.stop()

m3 >> play('[YY]', amp=0.8).after(4, 'stop')
d7 >> play('[OO]', amp=0.07).after(4, 'stop')

k2.amplify = 0

k2.stop()



linvar([0.05, 0.15], 48)

k1.stop()

help(var)

print(SynthDefs)

Group(b1, p1).amplify = 1

k1.stop()


Clock.clear()








m1 >> sitar(mel, oct=oct, dur=dur, amp=0.4, sus=0.3, dist=0.4, vib=0, bpm=280, tremolo=4, amplify=1).stop()

m2 >> sitar(mel2, oct=P[oct2] - 1, dur=dur2, amp=0.3, sus=2, dist=0.4, vib=3, bpm=560, tremolo=1, amplify=1)

Group(m1, m2).solo()

m1.amp = 0.4
m2.amp = 0.35

print(sum(dur))

print(linvar([0, 1], 192))

m1 >> space(mel)

m1.stop()

print(m1.amp)

m1.amp = 1

b1 >> space(mel_b, oct=oct_b, dur=dur_b, amp=amp_b, vib=8, sus=4)

b2 >> sawbass(amp=[0, 0, 0.2], bend=0.5).follow(m1)

b2.stop()

b1 >> space(mel_b)

Clock.bpm = 120

Clock.clear()

m1.solo()

d1 >> play('-', dur=4/4, amp=0.4)

d2 >> play('-', dur=16/3, amp=0.4)

d3 >> play('[--]', dur=16/3, amp=0.4, offset=4)

d3.stop()

d4 >> play('x--o--', amp=0.3, bpm=140, delay=1)

c2 >> play('h', dur=1/4, sample=P[:8].rotate([0, 1, 3]), rate=4, pan=0.5, amp=0.2).stop()


Clock.bpm = 120

d1 >> play('([x ][[x ][x ]])[ X][x ][X ]', amp=0.5).stop()

d2 >> play('[--]').stop()

d3 >> play('000(0[----])')

d4 >> play('            =(=([==][===[==]]))')

d5 >> play('n      n').sometimes('stutter')

d6 >> play('[c ] (c [ c]) [ c]')

d7 >> play('(       A) ', amp=0.6).sometimes('stutter').stop()



d4 >> play("<  * ><[--]>").stop()


d4 >> play("x[--]o(=[-o])    ", dur=4/3, amp=0.4).every(16, 'reverse')

d4 >> play('-[xo](-x)-[(-x)]', amp=0.4).stop()

d4 >> play("x-x(=[--])", amp=1).stop()

d5 >> play("hh hh hh hh ").stop()

d4.stop()

bassUp = [0,2,4,5]
bassDown = [5.5,5,4,2]

bu_mel = gens.generateMelody(bassUp)
bd_mel = gens.generateMelody(bassDown)

print(SynthDefs)

m1.stop()

d1.stop()

print(dur)

mel = gens.generateMelody(notes, scale=Scale.major)
oct = gens.generateOctaves(notes)
dur = gens.generateDurations(notes)
amp = gens.generateAmps(notes, 0.4)
mel_b = gens.generateMelody(bass, scale=Scale.major)
oct_b = gens.generateOctaves(bass, octave=4)
dur_b = gens.generateDurations(bass)
amp_b = gens.generateAmps(bass, 0.4)
print(sum(dur))
print(sum(dur_b))

maj = 0, 2, 4, 5
dim = 0, 1.5, 3.5, 5
dom7 = 0, 3, 5, 7
dim7 = 0, 2, 4, 7


print(P(mel).reverse())

print(len(dur_b))

print(mel)

print(dur)

m1 >> saw([Scale.major | P[12]])

print(scale[6])

print(Scale.chromatic)

print(Scale.default)

Scale.default = Scale.chromatic

print(type(4.5) == float)

Clock.clear()
