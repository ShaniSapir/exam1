import random

_id = [3, 2, 3, 0, 6, 0, 5, 9, 0]
question_arr = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
print("The chosen question is: ", question_arr[(random.choice(_id) + random.randint(0, 12))])
