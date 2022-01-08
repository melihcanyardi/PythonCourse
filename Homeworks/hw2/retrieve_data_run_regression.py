import wbdata
import pandas as pd

# Retrieve Data from World Bank API
indicators = {
    "NY.GDP.PCAP.CD": "gdp_pc",
    "SP.POP.TOTL": "population",
    "SP.DYN.LE00.IN":"life_expectancy"
}

df = wbdata.get_dataframe(indicators=indicators, country="TUR", convert_date=True)

df.to_csv("data.csv")

# Linear Regression
from linear_regression import linear_regression
data = pd.read_csv("data.csv")

X = df[["gdp_pc", "population"]]
y = df["life_expectancy"]

coefficients, standard_errors, confidence_intervals = linear_regression(X, y)

pd.set_option('display.float_format', lambda x: '%.12f' % x)
regression_table = pd.DataFrame(linear_regression(X, y),
                                index=["Coefficients", "Standard Errors", "Confidence Intervals"],
                                columns=["Constant", "GDP per capita (current US$)", "Population, total"]).T

print(regression_table)