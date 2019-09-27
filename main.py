from flask import Flask, render_template, request
import os
import preprocessing
import plotting
# konfigurasi awal
app = Flask(__name__)

# kumpulan route


@app.route('/')
def index():
    lima_data = preprocessing.lima_data()
    return render_template('data.html', data=lima_data)


@app.route('/plot')
def plot():
    data_1 = plotting.plot_hist_mpg()
    data_2 = plotting.plot_hist_hp()
    return render_template('plot.html', data=[data_1, data_2])

@app.route('/pre_data')
def pre_data():
    top_hp = preprocessing.top_3_hp()
    top_irit = preprocessing.top_3_irit()

    judul = ['Biggest HorsePower',  'Biggest Irit']
    
    return render_template('stat.html', data=[top_hp, top_irit], judul=judul)


# buat ngerender semuanya
if __name__ == '__main__':
    app.run(port=9876, debug=True)
