from flask import Flask, render_template, request
import pandas as pd
from services.analyzer import PopulationAnalyzer
from services.forecast import ForecastService
from services.plotter import plot_population

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_url = None
    result = None
    if request.method == 'POST':
        file = request.files['datafile']
        period = int(request.form['period'])
        df = pd.read_csv(file, encoding='cp1251')
        analyzer = PopulationAnalyzer(df)
        worst, least = analyzer.min_max_decline()
        forecast = ForecastService()
        df_forecast = forecast.forecast(df, period)
        original_years = df['Year'].unique().tolist()
        chart_url = plot_population(df_forecast, original_years)

        result = {'worst': worst, 'least': least}
    return render_template('index.html', chart_url=chart_url, result=result)

@app.route('/java')
def java():
    return render_template('java.html')


@app.route('/alice') #TEST
def alice():
    return render_template('alice.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
