class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
    max = 0

    for i in range(len(self.__elements)):
        for j in range(len(self.__elements)):
            abs_max = abs(self.__elements[i] - self.__elements[j])
            if abs_max > max:
                max = abs_max
    self.maximumDifference = max


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
