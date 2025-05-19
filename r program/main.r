library(ggplot2)
library(plotly)
library(dplyr)
library(readr)
library(tidyr)


set.seed(123)
covid_data <- data.frame(
    Country = rep(c ("USA", "India", "Brazil", "Australia"), each = 30),
    Daily_cases = c(rnorm(30, 5000, 10000),
                    rnorm(30, 40000, 15000),
                    rnorm(30, 30000, 12000 ),
                    rnorm( 30, 500, 200 ))
)


ggplot(covid_data,aes( x = country, y = Daily_cases, fill = country )) +
    geom_boxplot() +
    labs(
        title:"Daily COVID-19 case Distrubution by Country",
        x = "country",
        y = "Daily Cases",

    )+ 
    theme_minimal()


covid_vaccine_data <- covid_data %>%
group_by(Country) %>%
summarise(
    Avg_Cases = mean (Daily_Cases),
    Vaccination_Rate = c(65,55, 60, 90)
)


plot_ly(
    data = covid_vaccine_data,
    x = ~Vaccination_Rate,
    y = ~Avg_Cases,
    type = "scatter",
    mode = "markers+text",
    text = ~Country,
    marker = list(size = 15, color = rgba(93, 164, 214, 0.8), line = list(width = 2))
)%>%

layout (
    title = "COVID-19 Cases vs Vaccination Rate",
    xaxis = list(title = "Vaccination Rate (%)"),
    yaxis = list(title = "Average Daily Cases")
)