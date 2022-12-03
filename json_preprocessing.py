#Обработка json файла
import pandas as pd
import re


def json_parse(json):
    with open(json, 'r') as f:
        data = json.loads(f.read())
        data = data.apply(lambda x: int(re.sub('[^0-9]', '', str(x).split(',')[0])))
        data = pd.DataFrame(data)
        user_data = data.T
        print(user_data)
    return user_data
