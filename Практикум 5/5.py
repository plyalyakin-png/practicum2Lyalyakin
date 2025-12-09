h = int(input())
w = int(input())
BMI = round(w/(h/100)**2)
if BMI < 16:
    print('выраженный дефицит массы тела')
elif BMI >= 16 and BMI < 18.49:
    print('недостаточная масса тела')
elif BMI >= 18.5 and BMI <= 24.99:
    print('норма')
elif BMI >= 25 and BMI <= 29.99:
    print('избыточная масса тела')
elif BMI >= 30 and BMI <= 34.99:
    print('ожирение первой степени')
elif BMI >= 35 and BMI <= 39.99:
    print('ожирение второй степени')
else:
    print('ожирение третьей степени')
