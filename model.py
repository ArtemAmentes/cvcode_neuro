#Здесь будет модель для работы с данными
#модель загружает сохраненную модель и использует ее для предикта - не тренируется
from sklearn.neural_network import MLPClassifier
import pickle

mlp = MLPClassifier()
try:
    with open('model.pkl', 'rb') as fid:
        mlp = pickle.load(fid)
    print('Model loaded')
except:
    print('Model not loaded. Please, check!')

