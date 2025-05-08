import matplotlib.pyplot as plt
import os
import pandas as pd


def plot_population(df, original_years):
    fig, ax = plt.subplots(figsize=(10, 5))

    for region in df['Region'].unique():
        region_data = df[df['Region'] == region].sort_values('Year')

        actual = region_data[region_data['Year'].isin(original_years)]
        forecast = region_data[~region_data['Year'].isin(original_years)]

        # Рисуем сначала фактические
        ax.plot(
            actual['Year'], actual['Population'],
            label=f"{region} (факт)",
            linewidth=2
        )

        # А потом прогноз — начиная с последнего фактического
        if not forecast.empty:
            joined = pd.concat([actual.tail(1), forecast])
            ax.plot(
                joined['Year'], joined['Population'],
                label=f"{region} (прогноз)",
                linestyle='--',
                linewidth=2,
                alpha=0.8
            )

    ax.set_xlabel('Год')
    ax.set_ylabel('Численность населения')
    ax.legend()
    static_dir = os.path.join(os.path.dirname(__file__), '..', 'static')
    os.makedirs(static_dir, exist_ok=True)
    chart_path = os.path.join(static_dir, 'chart.png')
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return 'chart.png'
