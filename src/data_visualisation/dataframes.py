import pandas as pd
import plotly.express as px
from plotly.offline import plot

# data = pd.ExcelFile('../data/Problem C data.xlsx')
# df = data.parse('Edited Data')

# total_remaining_capital = df["Remaining capital"].sum()
# october_rating = df.groupby('October Rating')["Remaining capital"].sum().divide(total_remaining_capital) * 100
# october_rating = october_rating.reindex(['A+', 'A', 'B+', 'B', 'C', 'C-'])
# # october_rating = pd.Categorical(october_rating, ['A+', 'A', 'B+', 'B', 'C', 'C-'])
# # chart = october_rating.plot.bar(title='October Rating x Remaining Capital', ylabel="Remaining Capital (%)")
# chart = px.line(october_rating)
# div_plot = plot(chart, output_type="div")