from FoxDot import Scale, FloorDiv

class Generators():
  def generateMelody(self, melody, scale=Scale.major):
    # ignores strings but respects pauses
    output = []
    for n in melody:
        if type(n) == int:
            output.append(scale[n])
        elif type(n) == float:
            output.append(scale[int(FloorDiv(n, 1))] + 1)
        elif n == 'p':
            output.append(0)
        elif type(n) == tuple:
            midput = []
            for m in n:
                if type(m) == int:
                    midput.append(scale[m])
                else:
                    midput.append(scale[int(FloorDiv(m, 1))] + 1)
            output.append(tuple(midput))
    return output

  def generateOctaves(self, melody, octave=6):
      output = []
      for n in melody:
          if type(n) == tuple:
              output.append(octave + FloorDiv(n[0], 7))
          elif type(n) != str:
              output.append(octave + FloorDiv(n, 7))
          elif n == 'p':
              output.append(octave)
      return output

  def generateDurations(self, melody):
      output = []
      pauses = 0
      for i, n in enumerate(melody):
          if (type(n) == str) and n != 'p':
              pauses += 1
              if i > 0:
                  output[i - pauses] = output[i - pauses] + int(n)
          else:
              output.append(1)
      return output

  def generateAmps(self, melody, amp=0.4):
      output = []
      for n in melody:
          if n == 'p':
              output.append(0)
          elif type(n) != str:
              output.append(amp)
      return output

  def silentExcept(self, audible, ran=16, amp=0.4):
      output = []
      for n in range(0, ran):
          if n % audible == 0:
              output.append(amp)
          else:
              output.append(0)
      return output