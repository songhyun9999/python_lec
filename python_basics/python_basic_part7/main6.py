print(python_basics.python_basic_part7.calcpkg.operation.add(10, 20))
print(python_basics.python_basic_part7.calcpkg.geometry.rectangle_are(30, 30))

from calcpkg import *
print(operation.add(10, 20))
print(geometry.triangle_area(20, 40))

from calcpkg.operation import  *
from calcpkg.geometry import *

print(mul(10,20))
print(rectangle_are(20,20))
