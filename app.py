import os
import atexit
from flask import Flask, render_template, Response, request
from data_predication import DataPredication
from data_generator import DataGenerator
from apscheduler.schedulers.background import BackgroundScheduler


app = Flask(__name__, template_folder="templetes")


@app.route('/', methods=['GET'])
def index():
    return render_template('homeclass.html')


@app.route('/predication', methods=['POST', 'GET'])
def predict():
    d = DataPredication()
    data = d.predict()
    return data[0]



def update_data():
    scheduler = BackgroundScheduler()
    generator = DataGenerator()
    scheduler.add_job(func=generator.generate, trigger="interval", days=1)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())


if __name__ == '__main__':
    # update_data()
    app.run(debug=True)
