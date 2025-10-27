score = input()
score_1, score_2 = map(int, score.split(':'))
if (score_1 > score_2):
    print(1)
elif score_2 > score_1:
    print(2)
else:
    print(0)