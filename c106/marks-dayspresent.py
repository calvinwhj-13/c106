import csv
import plotly.express as px
with open("data/marks-dayspresent.csv") as csv_file :
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = 'Days Present ', y = 'Marks In Percentage')
    fig.show() 