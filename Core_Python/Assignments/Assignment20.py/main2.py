from SY import SYMARKS
from TY import TYMarks

sy_student = SYMARKS(80, 85, 90)
sy_student.display()
print("SY Total:", sy_student.total_marks())
print("SY Average:", sy_student.average())
print()

ty_student = TYMarks(88, 92)
ty_student.display()
print("TY Total:", ty_student.total())
print("TY Average:", ty_student.average())
