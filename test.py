import json
from random import randint


with open('./api/fortune-cookie.json', 'r') as f:
    data_from_file = f.read()

data = json.loads(data_from_file)
data_len = len(data)
random_position = randint(0, data_len - 1)
print(data[random_position])