import pickle

from flask import Flask, request, jsonify

with open('capstone1.bin','rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('hotel-cancel-pred')

@app.route('/predict', methods=['POST'])
def predict():
    booking = request.get_json()
    print(f' BOOKING DETAILS : {booking}')
    X = dv.transform(booking)
    y_pred = model.predict(X)
    
    result = 'No'
    if (y_pred[0] == 1):
        result = 'Yes'

    result = {
        "Will this booking be cancelled ": f'{result},  Model Predicted value : {y_pred[0]}'
    }

    return jsonify(result)


## To serve this application using waitress use below command. in predict:app, predict is the name of this python file
## pipenv run waitress-serve --listen=0.0.0.0:9696 predict:app

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)