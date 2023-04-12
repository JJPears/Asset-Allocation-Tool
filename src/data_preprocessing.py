import pandas as pd
import requests

class DataPreprocessing:

    def __init__(self):
        self.data = None


    def getJsonDataFromApiAsDataframe(self, ticker, api_token=None):
        if api_token is None:
            api_token = "demo"

        urlForApi = "https://eodhistoricaldata.com/api/eod/{}?api_token={}&period=d&fmt=json".format(ticker, api_token)
        response = requests.get(urlForApi)

        if response.status_code == 200:
            return pd.json_normalize(response.json())
        else:
            raise Exception()

    
    def saveDataAsCsv(self, dataFrame, newFileName):
        dataFrame.to_csv('data/{}.csv'.format(newFileName))


if __name__ == '__main__':
    object = DataPreprocessing()
    data = object.getJsonDataFromApiAsDataframe('AAPL.US', 'demo')
    print(data.head(5))
    object.saveDataAsCsv(data, 'data')
        