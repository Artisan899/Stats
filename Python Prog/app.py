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


@app.route('/alice',methods=['GET', 'POST'])
def alice():
    table_data = None
    error_message = None

    if request.method == 'POST':
        if 'datafile' not in request.files:
            error_message = "Not found"
        else:
            file = request.files['datafile']
            if file.filename == '':
                error_message = "Not chosen"
            elif not file.filename.endswith('.csv'):
                error_message = "Need CSV!"
            else:
                try:
                    daf = pd.read_csv(file)

                    expected_columns = ['Year', 'VVP', 'VNP']
                    if not all(col in daf.columns for col in expected_columns):
                        error_message = f"CSV trebuet {', '.join(expected_columns)}"
                    else:
                        table_data = daf[expected_columns].to_dict(orient='records')
                except Exception as e:
                    error_message = f"ASHIBKA {e}"

    return render_template('alice.html', table_data=table_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
