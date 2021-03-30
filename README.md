----
# 🔮 PensionPal - the UK's first AI retirement savings prediction model

## Introduction

`pensionpal` is a tool that predicts an individual's future retirement income based on publicly available employment and salary data from LinkedIn and Glassdoor. On the backend it is a python 🐍 package and on the frontend it has a simple chatbot 🤖 interface.

## Usage Example

### How PensionPal works

Running `python setup.py install` installs packages, which include:
- ✂️ **`linkedin_scraper.py`** - scrapes users LinkedIn profile and exports to a .csv file
- 🧼 **`data_clean.py`** - cleans .csv file and formats for data analysis purposes
- 🤑 **`glassdoor_scraper.py`** - cross-references employment data from LinkedIn in .csv file and accounts for salary growth and inflation etc
- 🧮 **`pension_predictor_past.py`** - calculates size of current pension pots (401ks) based on % of income set out in UK government's auto enrolment legislation
- 🔮 **`pension_predictor_future.py`** - uses Markov Chains to predict future pension (401k) contributions based on comparable career trajectories on LinkedIn  # work in progress

### A worked example

`linkedin_scraper.py` scrapes profile via the scrape() function

```js
// main.js
import Vue from "vue";
import App from "./App.vue";
import router from "./router";
// import the plugin
import Calendar from "vue2-baremetrics-calendar";

Vue.config.productionTip = false;
```

> 32

`data_clean.py'

`glassdoor_scraper.py` scrapes profile via the scrape() function

`data_clean.py` formats profile data into editable file

`glassdoor_scraper.py`

`pension_predictor_past.py`

`pension_predictor_future.py`



### Chatbot

`pensionpal` is integrated with a chatbot interface .


### Contribution

Feel free to contribute. Just open an issue to discuss something before creating a PR.
