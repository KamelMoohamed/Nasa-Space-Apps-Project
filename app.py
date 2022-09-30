from flask import Flask, render_template, Response
from data_predication import DataPredication

# Flask APP
app = Flask(__name__, template_folder="templetes")


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('homeclass.html')


@app.route('/prediction', methods=['GET', 'POST'])
def predict():
    try:
        d = DataPredication()
        data = d.predict()
        return Response({
            "label":data[0],
            "values":data[1]
        },
        status=404)

    except:
        return Response(status=404)


if __name__ == '__main__':
    app.run(debug=True)