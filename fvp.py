#francoske vrste poljub

Clock.clear()

print(SynthDefs)

print(Scale.major)

print(Scale.major)

help(Scale)

print(Scale.default)

# default scale should be major
Scale.default = Scale.major


print(maj)

major = [Scale.major[n] for n in [0, 2, 4, 5]]
minor = [Scale.minor[n] for n in [0, 2, 4, 5]]

maj = 0, 2, 4, 5
dim = 0, 1.5, 3.5, 5
dom7 = 0, 3, 5, 7
dim7 = 0,2,4,7

print(major)

t1 >> bell(P[major] | P[major] + [11, 7, 5, 7, 4, 7, 11] | P[major].reverse() + [7, 11] | P[major].reverse(),
           amp=P[(0, 0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0), (0, 1), (0, 0, 1)] * linvar([0.005, 0.01], 100),
           sus=3,
           bpm=1120) + var([minor])

t2 >> glass(amp=P[(0, 0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 0), (0, 1), (0, 0, 1)] * 0.7,
            sus=4,
            bpm=35).follow(t1)

d1 >> play('=',
           bpm=420,
           amp=linvar([0, 0.2], 50),
           pan=linvar([-0.5, 0.5], 10))

print(linvar([0, 0.2], 50))

b1 >> bass([0],
           bpm=35,
           amp=linvar([0, 0.2], 50),
           sus=16,
           dur=PDur([3], 22))

b1.amp = 0.2

print(SynthDefs)

v1 >> viola([0], oct=8, dur=8, amp=[0.4, 0], vib=0.1, tremolo=4, bend=1) + 4

v2 >> viola([0], oct=8, dur=8, amp=[0.4, 0, 0, 0.4, 0, 0.4], vib=0.1, tremolo=4, bend=1, delay=0.7) + 5

print(linvar([0, 1], 50))

d2 >> play('x-o-', amp=P[0.3, 0.4, 0.2, 0.4], dur=[1.5, 0.5, 1.5, 0.5], bpm=120, amplify=linvar([0, 1], 50))

d2.amplify = 1

d2 >> play('x-o-[x x ]xo-', amp=[0.3, 0.4, 0.2, 0.4], dur=[1.5, 0.5, 1.5, 0.5])

r1 >> razz(P[0, 2, 1, 4, 5] + (dom7),
           bpm=15,
           amp=0.1,
           sus=16,
           dur=PDur([3], 22),
           amplify=linvar([0, 1], 50))

r1.amplify = 1

d3 >> play("n", dur=1/4, amp=PWhite(0.1,0.2), rate=PWhite(.98,1.02), pan=0.5, sample=6)

p1 >> glass([4, 2, 4, 8, 7, 5, 5, 7, 8, 4, 2, 1], amp=0.7, bpm=60, sus=4, dur=1)

p2 >> sinepad([4, 2, 4, 8, 7, 5, 5, 7, 8, 4, 2, 1], amp=0.25, bpm=120, sus=2, dur=1).stop()

p3 >> sinepad([4, 2, 4, 8, 7, 5, 5, 7, 8, 4, 2, 1], amp=0.25, bpm=120, sus=2, dur=PDur([3, 1, 4], 8)) + (7)

p3.dur = P[PDur([3, 1, 4], 8) | PDur([2, 5, 1], 8)] # | PDur([1, 1, 7], 8)]

help(Player.rotate)

p1.stop()
p2.stop()

p3.stop()

print(linvar([0, 1], 50))

Group(p1, p3).amplify = 0 # linvar([0.8, 0], 50)

Group(v1, v2, r1).amplify = 0 # linvar([0.8, 0], 50)

p1.stop()
p3.stop()
v1.stop()
v2.stop()
r1.stop()

Group(d1, d2).amplify = linvar([0.8, 0], 50)

d1.stop()
d2.stop()

Clock.clear()

print(P[0, 2, 1, 4, 5])
