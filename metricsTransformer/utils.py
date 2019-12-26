class Metrics:
    pass


def maxMin(num, rmin, rmax):
    tmin = 0
    tmax = 1
    return ((num - rmin) / (rmax - rmin)) * (tmax - tmin) + tmin


def getMetrics(mappingsHeader, mappingsBody, metricNames):
    results={}
    for key in mappingsBody:
        m = Metrics()
        review=mappingsBody[key]
        for metric in metricNames:
            weigthsum = 0
            for v in mappingsHeader[metric]:

                if (v["name"] == "" or v["name"] is None):
                    setattr(m, metric,None)
                    continue
                if not hasattr(m, metric):
                    setattr(m, metric, v["weight"]*maxMin(review[v["name"]], v["min"], v["max"]))
                else:
                    setattr(m, metric,
                            (getattr(m, metric) + v["weight"]*maxMin(review[v["name"]], v["min"], v["max"])))

                weigthsum+=v["weight"]
            if getattr(m, metric) is None:
                continue
            setattr(m, metric,
                    (getattr(m, metric)/weigthsum))
        results[key]=m.__dict__

    return results

