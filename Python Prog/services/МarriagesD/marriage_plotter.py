import matplotlib.pyplot as plt
import os

class MarriageDivorcePlotter:
    def __init__(self, static_folder='static'):
        self.static_path = os.path.abspath(static_folder)
        os.makedirs(self.static_path, exist_ok=True)

    def plot_by_year(self, df, original_years, forecast_years=[]):
        chart_path = os.path.join(self.static_path, 'marriages_divorces.png')
        plt.figure(figsize=(10, 5))

        grouped = df.groupby('Year').sum()

        plt.plot(grouped.index, grouped['Marriages'], label='Браки', linewidth=2)
        plt.plot(grouped.index, grouped['Divorces'], label='Разводы', linewidth=2)

        if forecast_years:
            forecasted = grouped.loc[forecast_years]
            plt.plot(forecasted.index, forecasted['Marriages'], '--', label='Браки (прогноз)', alpha=0.7)
            plt.plot(forecasted.index, forecasted['Divorces'], '--', label='Разводы (прогноз)', alpha=0.7)

        plt.xlabel('Год')
        plt.ylabel('Число')
        plt.legend()
        plt.grid()
        plt.tight_layout()
        plt.savefig(chart_path)
        plt.close()

        return 'marriages_divorces.png'
