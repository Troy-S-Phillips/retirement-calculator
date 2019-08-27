import pandas as pd
import numpy as np
import re
from markupsafe import Markup, escape
import locale
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')

def StockCalculation(SBalance,SYear,AYears):
    DisplayResult = ""

    StocksBalance = SBalance
    BondsBalance = StocksBalance

    StartingYear = SYear
    YearStart = StartingYear

    AmountOfYears = AYears
    CountOfYears = 0

    #Stocks = pd.read_excel(r'C:\Users\Troy\Desktop\histretSP.xlsx')
    #Stocks = pd.read_excel(r'/home/ubuntu/RetirementWebsite/histretSP.xlsx') #(used in EC2 instance)
    Stocks = pd.read_excel(r'/RetirementWebsite/histretSP.xlsx') #(used in Docker Container)
    
    while(CountOfYears < AmountOfYears):
        PreviousYearsStockGrowth = float(Stocks.loc[Stocks['Year'] == YearStart-1,['S&P 500 (includes dividends)']].values[0])
        PreviousYearsBondGrowth = float(Stocks.loc[Stocks['Year'] == YearStart-1,['Return on 10-year T. Bond']].values[0])
        ThisYearsStockGrowth = float(Stocks.loc[Stocks['Year'] == YearStart,['S&P 500 (includes dividends)']].values[0])
        ThisYearsBondGrowth = float(Stocks.loc[Stocks['Year'] == YearStart,['Return on 10-year T. Bond']].values[0])

        if PreviousYearsStockGrowth > 0:
            StocksBalance -= 100000
        else:
            BondsBalance -= 100000

        StocksBalance *= (1+ThisYearsStockGrowth)
        BondsBalance *= (1+ThisYearsBondGrowth)
        StocksBalance = ((StocksBalance+BondsBalance)/2)
        BondsBalance = StocksBalance
        CountOfYears += 1
        YearStart += 1

        if StocksBalance < 100000 or BondsBalance < 100000:
            DisplayResult = "There will be less than $100,000 in your bonds account and stock account at the beginning of "+ str(YearStart)
            return DisplayResult
        #print(YearStart,StocksBalance,BondsBalance) #Will be removed when turned into function

    Result = "If you start withdrawing $100k per year at "+ str(StartingYear) + " for "+ str(AmountOfYears) + " years you will have " + str(locale.currency(float(np.round(StocksBalance,2)), grouping = True)) + " in your stock account and " + str(locale.currency(float(np.round(BondsBalance,2)), grouping = True)) + " in your bonds account."
    DisplayResult = re.sub("\[ |]","",Result)
    return DisplayResult