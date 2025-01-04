import sqlite3
import pandas as pd
import plotly.express as px

connection = sqlite3.connect("data/gapminder.db")
plotting_df = pd.read_sql("""SELECT * FROM plotting;""", con=connection)
connection.close()

# px.scatter param:
# animation_frame: time variable for animation
# hover_name: show the name when mouse move to the data
# log_x: if x label need to use log scale

fig = px.scatter(plotting_df, x="gdp_per_capita", y="life_expectancy",
                 animation_frame="dt_year", animation_group="country_name",
                 size="population", color="continent", hover_name="country_name", 
                 size_max=100, range_x=[500, 100000], range_y=[20, 90], log_x=True,
                 title="Gapminder Clone 1800-2023")
fig.write_html("gapminder_clone.html", auto_open=True)