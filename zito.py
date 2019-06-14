Clock.clear()

maj = 0, 2, 4, 5
dim = 0, 1.5, 3.5, 5
dom7 = 0, 3, 5, 7
dim7 = 0,2,4,7

zito = [[[7, 2, 5, 2, 4, 5, 1], [7, 2, 2, 1, 2, 2, 1]]]

p1 >> sawbass(zito, oct=[5], dur=8, amp=0.3, room=0.8, sus=7.8, fmod=linvar([-1, 1], 16), vib=7)

p2 >> saw(dur=PDur([3, 5], 7), amp=0.2, reverb=2).follow(p1) + 0

p3 >> saw(dur=PDur([2, 3], 4), amp=0.15, reverb=2).follow(p1) + 2

p4 >> saw(dur=PDur([1, 5], 7), amp=0.15, reverb=3).follow(p1) + 4

p5 >> saw(dur=PDur([2, 3], 3), amp=0.15, reverb=2).follow(p1) + 14

p6 >> prophet(dur=PDur([1, 5], 3), amp=0.1, reverb=2, sus=2, fmod=linvar([0.1, 2], 5)).follow(p1) + 0

k1 >> karp(dur=(PDur([3,5],8)), oct=6, reverb=2, sus=6, vib=0.2, amp=0.5).follow(p4)

# player one leads the way

p1 >> pluck(zito, scale=Scale.default.pentatonic, amp=0.5) + PRange(7)

d1 >> play('X   x   (  [hh] #)  (#x)   x', amp=0.4).stop()

d2 >> play(' 0 [(i ) ][ ( f)]', amp=0.4).sometimes('stutter').stop()

d3 >> play('  - ', amp=0.4).stop()


Clock.bpm = 120

# zrelo je žito
mel1 = [P[7, 6, 5, 7, 6, 5], P[2, 1, 1, 2, 1, 1]]
mel21 = [P[12, 11.5, 12, 9], P[2, 1, 1, 4]]
mel22 = [P[12, 12, 11.5, 12, 9], P[1, 1, 1, 1, 4]]
mel3 = [P[9, 12, 13, 14, 13, 12], P[2, 1, 1, 2, 1, 1]]
mel4 = [P[11, 8, 10, 9], P[2, 1, 1, 4]]
mel5 = [P[12, 8, 10, 9, 5, 7], P[2, 1, 1, 2, 1, 1]]
mel6 = [P[8, 8, 7, 6, 5], P[1, 1, 1, 1, 4]]
melfinal = (mel1[0] | mel21[0] | list(P(mel1[0]) + 3) | mel22[0] | mel3[0] | mel4[0] | mel5[0] | mel6[0])
durfinal = (mel1[1] | mel21[1] | mel1[1] | mel22[1] | mel3[1] | mel4[1] | mel5[1] | mel6[1])

m2 >> bell([16, 17, 14, 19, 20], amp=0.1, bpm=15, tremolo=12).stop()

m0 >> bell(mel1[0], dur=mel1[1], amp=[0.2, 0.2, 0.2], bpm=30, amplify=1.3, tremolo=3).stop()

m1 >> bell(mel3[0], dur=mel3[1], amp=[0, 0.2, 0.2], sus=mel21[1], bpm=30, amplify=1.3, delay=1).stop()

# r1 >> rave(amp=0.3, dur=4, bpm=30, sus=8).follow(m1)

m3 >> bell(melfinal.arp(list(dim7)), dur=durfinal, amp=[0.3, 0.2, 0.2], bpm=15, tremolo=6).stop()

m4 >> bell(melfinal, dur=durfinal, amp=0.4, bpm=60, sus=5, amplify=1.1).stop()

print(SynthDefs)

m5 >> bell(dur=durfinal, amp=0.1, bpm=60, sus=0.5).follow(m4).stop() + dim7
d6 >> play(" [--][--]([----]-)", amp=0.3).stop()

d7 >> play('  ( [ b]) 00c([ c]c)', amp=0.1).stop()
d5 >> play(' s  n  (--=) x', amp=0.5).stop()



Clock.clear()
