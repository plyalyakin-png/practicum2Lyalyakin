score = input()
score_1, score_2, score_3 = map(int, score.split(' '))
record = score_1
if score_2 > record:
    record = score_2
if score_3 > record:
    record = score_3
print(record)