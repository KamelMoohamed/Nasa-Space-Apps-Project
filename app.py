import os
import atexit
from flask import Flask, render_template, Response
from data_predication import DataPredication
from data_generator import DataGenerator
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__, template_folder="templetes")


@app.route('/', methods=['GET'])
def index():
    return render_template('homeclass.html')


@app.route('/prediction', methods=['GET', 'POST'])
def predict():
    try:
        d = DataPredication()
        data = d.predict()
        return Response({
            "Label": data[0],
            "Data": data[1]
        },
        status=404)
    except:
        return Response(status=404)


def update_data():
    scheduler = BackgroundScheduler()
    generator = DataGenerator()
    scheduler.add_job(func=generator.generate, trigger="interval", days=1)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    update_data()
    app.run(debug=True)
