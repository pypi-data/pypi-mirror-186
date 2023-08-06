import numpy as np
import pylab

from skipi.norm import lp
from skipi import *
from uxdconverter.parser.general import GeneralParser

file = "Absorber.raw"
parser = GeneralParser(None)
ms = parser.parse(file)

fs = [m.as_function() for m in ms.get_measurements()]
_is = [fs[i].get_dom().intersect(fs[i+1].get_dom()) for i in range(len(fs)-1)]

#f1 = fs[0].remesh(_is[0])
#f2 = fs[1].remesh(_is[0])

it = 1

f1 = fs[it]
f2 = fs[it+1]

f1 = f1.vremesh((1.1, None))
f2 = f2.vremesh((1.1, None))

#f1 = f1.vremesh((None, 0.7))
#f2 = f2.vremesh((None, 0.7))

f1.plot()
f2.plot()
pylab.yscale("log")
pylab.show()

def scale_average(f1, f2):
    intersection = f1.get_dom().intersect(f2.get_dom())
    return np.average([f1(x) / f2(x) for x in intersection])

def scale_sum(f1, f2):
    intersection = f1.get_dom().intersect(f2.get_dom())
    return sum(f1(intersection)) / sum(f2(intersection))

def scale_l2min(f1, f2):
    intersection = f1.get_dom().intersect(f2.get_dom())

    return sum((f1*f2)(intersection)) / sum((f2**2)(intersection))

print(f"average {scale_average(f2, f1)}")
print(f"sum {scale_sum(f2, f1)}")
print(f"l2min {scale_l2min(f2, f1)}")

pylab.axhline(scale_average(f2, f1), color="blue")
pylab.axhline(scale_sum(f2, f1), color="red")
pylab.axhline(scale_l2min(f2, f1), color="green")

(f2/f1).plot(show=True)

f2.plot()
(f1*scale_average(f2, f1)).plot(color="blue")
(f1*scale_sum(f2, f1)).plot(color="red")
(f1*scale_l2min(f2, f1)).plot(color="green")
#(f2*scale_l2min(f2, f1)).plot()
pylab.yscale("log")
pylab.show()

f1 = f1.remesh(_is[it])
f2 = f2.remesh(_is[it])


print(lp(f1*scale_average(f2, f1) - f2))
print(lp(f1*scale_sum(f2, f1) - f2))
print(lp(f1*scale_l2min(f2, f1) - f2))