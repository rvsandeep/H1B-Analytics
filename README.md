# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years.

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.


# Approach

The directory structure for the repo is of following format :
```
      ├── README.md
      ├── run.sh
      ├── requirements.txt
      ├── .travis.yml
      ├── src
      │   └──H1BDataFrame.py
      │   └──DataTransformer.py
      │   └──AnalyticsEngine.py
      │   └──runner.py
      │   └──resources
      │       └── 2008fileformat.json
      │       └── 2009fileformat.json
      ├── tests
      │   └──test_dataframe.py
      │   └──test_analyticsengine.py
      │   └──test_datatransformer.py
      │   └──context.py
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── your-own-test_1
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
```

#### Code Pipeline

1.  **Data Handling** : `H1BDataFrame` hosts methods for reading csv files, accessing data and performing generic operations on the dataframe, similar to `pandas`.
2. **Data Pre-Processing** : `DataTransformer` currently hosts methods for renaming the raw input column names to a generic convention. Currently, the latest file structure is used as a standard. The files dated `2009` and before have different naming convention, hence the required mapping to transform from old convention to the latest is included as json files under `src/resources`.
3. **Analytics** : `AnalyticsEngine` hosts methods for performing basic analysis on the dataset, such as calculating the `top 10 statistics`. 

# Run Instructions

#### Running code  
Place the input file as `./input/h1b_input.csv` and run the `run.sh` script.

#### Running unit-tests
* Install the dependencies by running `pip install -r requirements.txt`
* run `pytest` command for the root of the project. `./H1B-Analytics/`
