from flask import Flask, jsonify  
import pandas as pd

app = Flask(__name__)

csv_file = 'day-13/Submission/programming_languages.csv'

def read_csv():
    df = pd.read_csv(csv_file)
    return df.to_dict(orient='records')

@app.route('/', methods=['GET'])
def get_langs():
    data = read_csv()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)