student_motiviert = True
student_ausgeschlafen = False
unterricht_spannend = True

lernerfolg = student_ausgeschlafen or (student_motiviert and unterricht_spannend) 

print lernerfolg

lernerfolg = (student_ausgeschlafen or student_motiviert) and unterricht_spannend

print lernerfolg

unterricht_spannend = False


print student_ausgeschlafen or (student_motiviert and unterricht_spannend) 

print (student_ausgeschlafen or student_motiviert) and unterricht_spannend
