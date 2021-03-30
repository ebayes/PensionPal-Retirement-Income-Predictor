----
# 🔮 PensionPal - the UK's first AI retirement savings prediction model

## Introduction

`pensionpal` is a tool that predicts an individual's future retirement income based on publicly available employment and salary data from LinkedIn and Glassdoor. On the backend it is a python 🐍 package and on the frontend it has a simple chatbot 🤖 interface.

## Usage Example

### How PensionPal works

Running `python setup.py install` installs packages, which include:
- ✂️ **`linkedin_scraper.py`** - scrapes users LinkedIn profile and exports to a .csv file
- 🧼 **`data_clean.py`** - cleans .csv file and formats for data analysis
- 🤑 **`glassdoor_scraper.py`** - cross-references employment data from LinkedIn in .csv file and accounts for salary growth and inflation etc
- 🧮 **`pension_predictor.py`** - calculates size of current pension pots (401ks) based on % of income set out in UK government's auto enrolment legislation and projects values into the future
- 🔮 **`glassdoor_compare.py`** - uses Markov Chains to predict future pension (401k) contributions based on comparable career trajectories on LinkedIn  # work in progress

### A worked example

*The following example contains real data from an anonymised source.*

`linkedin_scraper.py` scrapes profile via the Person() function

```py
from linkedin_scraper import Person
person = Person("https://www.linkedin.com/in/edbayes/")
print(person)
```

> StartDate | EndDate | Employer | Role
> --- | --- | --- | ---
> Feb 2016 | Present | Technical Support Manager (Executive Officer) | Department for Work and Pensions (DWP)
> Nov 2014 | Feb 2016 | Specialist | Apple

`data_clean.py' uses `numpy' to format the data into a format for analysis via the Clean() function

```py
import numpy as np
cleanPerson = Clean(person)
print(cleanPerson)
```

> StartMonth | StartYear | EndMonth | EndYear | TotalMonths | Employer | Role
> --- | --- | --- | --- | --- | --- | ---
> 2 | 2016 | nan | nan | 62 | Technical Support Manager (Executive Officer) | Department for Work and Pensions (DWP)
> 11 | 2014 | 2 | 2016 | 15 | Specialist | Apple

`glassdoor_scraper.py` scrapes profile via the scrape() function

```py
from glassdoor_scraper import Salary
salary = Salary(cleanPerson)
print(salary)
```

> No | ... | Salary
> --- | --- | --- 
> 0 | ... | 
> 1 | ... |  

`pension_predictor.py` predicts size of pension pot via the PredictPast() function and retirement income via the PredictFuture() function

```py
from pension_predictor import past and future
pensionpots = PredictPast(salary)
futurepension = PredictFuture(pensionpots)
print(futurepensions)
```

> No | ... | PotPrediction | PotPredictionEnd | RetirementIncome
> --- | --- | --- | --- | ---
> 0 | ... | 1035.26 | 4235 | 177.70
> 1 | ... | nan | nan | 3677


### Chatbot

`pensionpal` is integrated with a chatbot interface .


### Contribution

Feel free to contribute. Just open an issue to discuss something before creating a PR.
