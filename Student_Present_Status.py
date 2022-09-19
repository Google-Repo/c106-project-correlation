import plotly.express as px
import csv

with open("Student Marks vs Days Present.csv") as s:
    df=csv.DictReader(s)
    fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
    fig.show()
