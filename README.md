----
# ð® PensionPal - the UK's first AI retirement savings prediction model

## Introduction

`pensionpal` is a tool that predicts an individual's future retirement income based on publicly available employment and salary data from LinkedIn and Glassdoor. The backend is built in python ð and the UI is mocked up using Figma and built in CSML ð¤ (open source chatbot language).

## How PensionPal works

Running `python setup.py install` installs packages, which include:
- âï¸ **`linkedin_scraper.py`** - scrapes users LinkedIn profile and exports to a .csv file
- ð§¼ **`data_clean.py`** - cleans .csv file and formats for data analysis
- ð¤ **`glassdoor_scraper.py`** - cross-references employment data from LinkedIn in .csv file and makes adjustments to account for salary growth etc
- ð§® **`pot_predictor.py`** - calculates size of current retirement pots and projects values into the future
- ð® **`glassdoor_compare.py`** - uses Markov Chains to predict future retirement pot contributions based on comparable career trajectories on LinkedIn  #Â work in progress

## A worked example

*The following example contains real data from an anonymised source.*

`linkedin_scraper.py` scrapes profile via the Person() function

```py
from linkedin_scraper import person
person = Person("https://www.linkedin.com/in/anonymous_user/")
print(person)
```

> StartDate | EndDate | Employer | Role
> --- | --- | --- | ---
> Feb 2016 | Present | Technical Support Manager (Executive Officer) | Department for Work and Pensions (DWP)
> Nov 2014 | Feb 2016 | Specialist | Apple

`data_clean.py` uses `numpy` to format the data into a format for analysis via the Clean() function

```py
import numpy as np
cleanPerson = Clean(person)
print(cleanPerson)
```

> StartMonth | StartYear | EndMonth | EndYear | TotalMonths | Employer | Role
> --- | --- | --- | --- | --- | --- | ---
> 2 | 2016 | nan | nan | 62 | Technical Support Manager | Department for Work and Pensions
> 11 | 2014 | 2 | 2016 | 15 | Specialist | Apple

`glassdoor_scraper.py` scrapes profile via the Salary() function and makes adjustments for salary growth and inflation.

```py
from glassdoor_scraper import salary
salary = Salary(cleanPerson)
print(salary)
```

> No | ... | Salary | SalaryAdjusted
> --- | --- | --- | ---
> 0 | ... | 26,350 | 26,350
> 1 | ... | 21,148 | 18,359

`pot_predictor.py` predicts the present value of the user's retirement pots via the PredictPast() function, and the future value (at the point of retirement) and retirement income using via the PredictFuture() function

```py
from pot_predictor import past, future
retirementpots = PredictPast(salary)
futurepots = PredictFuture(retirementpots)
print(futurepots)
```

> No | ... | PotPrediction | PotPredictionEnd | RetirementIncome
> --- | --- | --- | --- | ---
> 0 | ... | 1035.26 | 4235 | 177.70
> 1 | ... | nan | nan | 3677

## ð¥ Comparing predicted vs real projections

Working with real users (**n=14**), we have been able to validate the model by tracking down peoples retirement pots and comparing real figures to predicted ones produced by our model. Early results show a high level of accuracy.

Using the worked example above, real  ð  predicted outcomes can be compared.

ExamplePredicted | ExampleReal | MedianPredicted | AverageReal
--- | --- | --- | ---
3,855 | 3,222 | 4,604 | 2579

## ð£ Chatbot

`pensionpal` is integrated with a chatbot interface, built using open source platform CSML.

<img src="./pictures/csml.png" width="100%">


## ð» Web hosting

A mock up of frontend and backend integrated together is shown below, with social integration to access user data more efficiently.

<img src="./pictures/figma.png" width="100%">
