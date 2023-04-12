## Asset allocation tool

This is a projects with the goal of developing an asset allocation tool which will simulate potential outcomes for different allocation strategies and risk tolerance.
This will be extended to use optimization algorithms to determine optimal asset allocation based on risk tolerance.

### Asset Allocation Strategies

Optimal asset allocation strategies used for given risk tolerances to try will be linear programming or quadratic programming

### Technologies and Frameworks:
#### Data Analysis, Processing and Visualisation:

- NumPy
- Pandas
- SciKit-learn

#### Data Visualisation
- MatplotLib
- Seaborn

#### Deployment
- Django/Flask
- Azure


### Financial Data:

Financial data pulled from [EOD Historical Data](https://eodhistoricaldata.com) api. This is using End-Of-Day Historical Stock Market Data for a range of tickers, including US stocks, ETFs and Mutual Funds. Data should already be adjusted to splits and dividends.

Demo access is limited to AAPL and VTI so these will be used for initial development.


### File Structuring

- Data: Contains raw and processed data files used in the project
- Notebooks: Jupyter notebooks for each step of the project
- Src: Contains the project source code
- Tests: unit tests for python files in src folder