from flask import Flask, render_template, request
import pandas as pd


#Population
from services.Population.analyzer import PopulationAnalyzer
from services.Population.forecast import ForecastService
from services.Population.plotter import PopulationPlotter

#VVP
from services.VVP.analyzer import  VVPAnalyzer
from services.VVP.forecast import  VVP_ForecastService
from services.VVP.plotter import  plot_gdp_gnp


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_url = None
    result = None
    table_data = None

    if request.method == 'POST':
        file = request.files['datafile']
        period = int(request.form['period'])
        df = pd.read_csv(file, encoding='cp1251')

        analyzer = PopulationAnalyzer(df)
        worst, least = analyzer.min_max_decline()

        worst = (worst[0], int(worst[1]))
        least = (least[0], int(least[1]))


        forecast = ForecastService()
        df_forecast = forecast.forecast(df, period)
        original_years = df['Year'].unique().tolist()
        plotter = PopulationPlotter()
        chart_url = plotter.plot(df_forecast, original_years)


        result = {'worst': worst, 'least': least}

        table_data = df.to_dict(orient='records')

    return render_template('index.html', chart_url=chart_url, result=result, table_data=table_data)


@app.route('/java')
#Testtesttest
def java():
    return render_template('java.html')


@app.route('/alice', methods=['GET', 'POST'])
def alice():
    table_data = None
    error_message = None
    chart_url = None
    stats = None

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
                        stats = VVPAnalyzer.calculate_growth_decline(daf)
                        period = 15
                        df_forecast = VVP_ForecastService.forecast(daf, period)
                        original_years = daf['Year'].unique().tolist()
                        chart_url = plot_gdp_gnp(df_forecast, original_years)

                except Exception as e:
                    error_message = f"ASHIBKA {e}"

    return render_template('alice.html', table_data=table_data, error_message=error_message, chart_url=chart_url, stats=stats)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
