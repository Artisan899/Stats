
import matplotlib.pyplot as plt
import os
import pandas as pd

#Класс строит график численности населения по регионам, различая фактические и прогнозные значения.

class PopulationPlotter:
    def __init__(self, static_folder='static'):
        # Путь до папки для сохранения графика
        self.static_path = os.path.abspath(static_folder)
        os.makedirs(self.static_path, exist_ok=True)
        self.chart_filename = 'chart.png'

    #Метод строит и возвращает график

    def plot(self, df: pd.DataFrame, original_years: list[str | int]) -> str:
        fig, ax = plt.subplots(figsize=(10, 5))

        for region in df['Region'].unique():
            region_data = df[df['Region'] == region].sort_values('Year')

            actual = region_data[region_data['Year'].isin(original_years)]
            forecast = region_data[~region_data['Year'].isin(original_years)]

            ax.plot(
                actual['Year'], actual['Population'],
                label=f"{region} (факт)", linewidth=2
            )

            if not forecast.empty:
                joined = pd.concat([actual.tail(1), forecast])
                ax.plot(
                    joined['Year'], joined['Population'],
                    label=f"{region} (прогноз)", linestyle='--',
                    linewidth=2, alpha=0.8
                )

        ax.set_xlabel('Год')
        ax.set_ylabel('Численность населения')
        ax.legend()
        plt.tight_layout()

        full_path = os.path.join(self.static_path, self.chart_filename)
        plt.savefig(full_path)
        plt.close()

        return self.chart_filename
