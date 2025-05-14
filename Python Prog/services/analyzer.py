import pandas as pd

class PopulationAnalyzer:
    def __init__(self, df):
        self.df = df

    def min_max_decline(self):
        decline = {}
        for region in self.df['Region'].unique():
            values = self.df[self.df['Region'] == region].sort_values('Year')
            decline[region] = values['Population'].iloc[-1] - values['Population'].iloc[0]
        sorted_regions = sorted(decline.items(), key=lambda x: x[1])
        return sorted_regions[0], sorted_regions[-1]


#analyzer alisi
class VVPAnalyzer:
    @staticmethod
    def calculate_growth_decline(df):
        df_sorted = df.sort_values('Year')

        df_sorted['VVP_pct_change'] = (df_sorted['VVP'].pct_change() * 100).round(2)
        df_sorted['VNP_pct_change'] = (df_sorted['VNP'].pct_change() * 100).round(2)

        max_vvp_growth = df_sorted['VVP_pct_change'].max()
        max_vvp_decline = df_sorted['VVP_pct_change'].min()
        max_vnp_growth = df_sorted['VNP_pct_change'].max()
        max_vnp_decline = df_sorted['VNP_pct_change'].min()

        max_vvp_growth_year = df_sorted.loc[df_sorted['VVP_pct_change'] == max_vvp_growth, 'Year'].values[0]
        max_vvp_decline_year = df_sorted.loc[df_sorted['VVP_pct_change'] == max_vvp_decline, 'Year'].values[0]
        max_vnp_growth_year = df_sorted.loc[df_sorted['VNP_pct_change'] == max_vnp_growth, 'Year'].values[0]
        max_vnp_decline_year = df_sorted.loc[df_sorted['VNP_pct_change'] == max_vnp_decline, 'Year'].values[0]

        result = {
            'max_vvp_growth': max_vvp_growth,
            'max_vvp_decline': max_vvp_decline,
            'max_vnp_growth': max_vnp_growth,
            'max_vnp_decline': max_vnp_decline,
            'max_vvp_growth_year': max_vvp_growth_year,
            'max_vvp_decline_year': max_vvp_decline_year,
            'max_vnp_growth_year': max_vnp_growth_year,
            'max_vnp_decline_year': max_vnp_decline_year,
        }

        return result
