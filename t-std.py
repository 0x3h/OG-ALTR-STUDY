import numpy as np

tagbucket = {
	# 17 August 2023
    "technical-indicator":   [64,     198693],
    "binance":               [471,    1247847],
    "yahoo-finance":         [518,    1194687],
    "google-finance":        [56,     222481],
    "yfinance":              [481,    622890],
    "mplfinance":            [119,    243489],
    "forex":                 [56,     99614],
    "algorithmic-trading":   [350,    588097],
    "quantitative-finance":  [298,    492248],
    "finance":               [1008,   1545297],
    "interactive-brokers":   [225,    276078],
    "trading":               [324,    389401],
    "back-testing":          [104,    101032],
    "stock":                 [476,    450966],
    #"hft":                   [4,      586],
    "coinbase-api":          [95,     93637],
    #"kucoin":                [41,     37694],
    #"huobi":                 [3,      1627],
    "ccxt":                  [136,    269358], # python-specific
    #"orderbook":             [4,      2939],
    "quantlib":              [160,    206510],
    "cryptocurrency":        [219,    336435],
    "stockquotes":           [74,     129610],
    #"computational-finance": [15,     14020],
    "ta-lib":                [200,    491729],
    "candlestick-chart":     [169,    472049],
    #"candlesticks":          [12,     10418]
}

tags   = [k for k in tagbucket.keys()]
cviews = [v[1] for v in tagbucket.values()]
means  = [round(v[1] / v[0], 2) for v in tagbucket.values()]
#for m in means: print(m)
stdd   = np.std(cviews)
print("STD: ", stdd)
covs   = [(tags[i], round(stdd / means[i], 2)) for i in range(len(means))]
for cov in covs: print(cov)
rsd    = [100 * (stdd - cviews[i]) / cviews[i] for i in range(len(cviews))]
for i in range(len(rsd)): print(tags[i], round(abs(rsd[i]), 2))