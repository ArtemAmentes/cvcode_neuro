from flask import Flask, request, jsonify
import traceback
from  model import mlp
from json_preprocessing import json_parse
pip
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if mlp:
        try:
            json_ = request.json
            query = json_parse(json_)
            prediction = mlp.predict(query)
            print(prediction)
            prediction_list = prediction.tolist()
            print(prediction_list)
            print('Using MLP')
            return jsonify({'prediction': str(prediction_list)})

        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print ('Load the model first')
        return ('No model here to use')


if __name__ == '__main__':
    try:
        port = int(sys.argv[1])  # This is for a command-line input
    except:
        port = 5000  # If you don't provide any

    app.run(port=port, debug=True, host='0.0.0.0')