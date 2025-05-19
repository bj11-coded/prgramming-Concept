library(ggplot2)
library(plotly)
library(dplyr)
library(readr)
library(tidyr)

retail_data <- data.frame(
    Month = rep(month.abb[1:6], 3),
    Category = rep(c("Electronics", "Clothing", "Groceries"), each = 6),
    Sales = c(12000, 13500, 14000, 15000, 16000, 17000, 
              9000, 9500, 10000, 11000, 10500, 11500,
              8000, 8500, 8300, 8700, 8600, 8900)
)

ggplot(retail_data, aes(x = Month, y = Sales, group = Category, color = Category)) +
    geom_line(size = 1.2) + 
    geom_point(size = 2) + 
    labs(
        title = "Monthly Sales by Category",
        x = "Month",
        y = "Sales ($)",
        color = "Category"
    ) + theme_minimal()

set.seed(123)
covid_data <- data.frame(
    Country = rep(c("USA", "India", "Brazil", "Australia"), each = 30),
    Daily_cases = c(rnorm(30, 5000, 10000),
                    rnorm(30, 40000, 15000),
                    rnorm(30, 30000, 12000),
                    rnorm(30, 500, 200))
)

ggplot(covid_data, aes(x = Country, y = Daily_cases, fill = Country)) +
    geom_boxplot() +
    labs(
        title = "Daily COVID-19 Case Distribution by Country",
        x = "Country",
        y = "Daily Cases"
    ) + 
    theme_minimal()

covid_vaccine_data <- covid_data %>%
    group_by(Country) %>%
    summarise(
        Avg_Cases = mean(Daily_cases),
        Vaccination_Rate = c(65, 55, 60, 90)
    )

plot_ly(
    data = covid_vaccine_data,
    x = ~Vaccination_Rate,
    y = ~Avg_Cases,
    type = "scatter",
    mode = "markers+text",
    text = ~Country,
    marker = list(size = 15, color = 'rgba(93,164,214,0.8)', line = list(width = 2))
) %>%
    layout(
        title = "COVID-19 Cases vs Vaccination Rate",
        xaxis = list(title = "Vaccination Rate (%)"),
        yaxis = list(title = "Average Daily Cases")
    )