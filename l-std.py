lbucket = {
	# 20 August 2023
    "python":          [3154,   4355249],
    "r":               [958,    941914],
    "pinescript":      [880,    905050],
    "mql":             [474,    959713],
    "c/c++":           [196,    263704],
    "java":            [194,    430490],
    "javascript":      [193,    305350],
    "c#":              [152,    328351]
}

tags   = [k for k in lbucket.keys()]
cviews = [v[0] for v in lbucket.values()]
sviews = sum(cviews)
print("SumViews: ", sviews)
for v in cviews: print((v / sviews) * 100)
means  = [round(v[1] / v[0], 2) for v in lbucket.values()]