#Обработка json файла
import pandas as pd


def json_parse(json):
    json=pd.DataFrame.from_dict(data = json, orient='index')
    user_data = json.T
    print(user_data)
    return user_data
