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
