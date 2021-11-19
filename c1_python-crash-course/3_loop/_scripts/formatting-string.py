def student_grade(name, grade):
        return "{name} received {grade}% on the exam".format (name= name , grade=grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

def to_celcius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>8.3f} C".format(x, to_celcius(x)))
