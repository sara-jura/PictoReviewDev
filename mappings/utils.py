class Metrics:
    def __init__(self):
        self.relevance = None
        self.novelty = None
        self.techQuality = None
        self.stateOfArt = None
        self.evaluation = None
        self.significance = None
        self.presentation = None


def maxMin(num, rmin, rmax):
    tmin = 0
    tmax = 1
    return ((num - rmin) / (rmax - rmin)) * (tmax - tmin) + tmin


def getMetrics(mappingsHeader, mappingsBody, metricNames):
    m = Metrics()
    for metric in metricNames:
        for v in mappingsHeader[metric]:
            v["name"]
            mappingsBody[v["name"]]
            if (v["name"] == "" or v["name"] is None):
                setattr(m, metric,None)
            if getattr(m, metric) is None:
                setattr(m, metric, maxMin(mappingsBody[v["name"]], v["min"], v["max"]))
            else:
                setattr(m, metric,
                            (getattr(m, metric) + maxMin(mappingsBody[v["name"]], v["min"], v["max"])) / 2)

    return m.__dict__

data = {"mappingsheader": {
    "orderMapping": False,
    "mappings": {
        "relevance": [
            {"max": 5, "name": "rel1", "min": 0},
            {"max": 5, "name": "rel2", "min": -5}
        ],
        "novelty": [
            {"max": 1, "name": "nov", "min": -1}
        ],
        "techQuality": [
            {"max": 5, "name": "tech", "min": 0}
        ],
        "stateOfArt": [
            {"max": 5, "name": "state", "min": 0}
        ],
        "evaluation": [
            {"max": 5, "name": "eval", "min": 0}
        ],
        "significance": [
            {"max": 5, "name": "sig", "min": 0}
        ],
        "presentation": [
            {"max": None, "name": "", "min": None}
        ]
    }
},
    "mappingsbody": {"rel1": 1, "rel2": 2, "nov": 0, "tech": 3, "state": 3, "eval": 2, "sig": 1}}

data2 = {"mappingsheader": {
    "orderMapping": True,
    "mappings": {
        "relevance": [
            {"max": 5, "name": 0, "min": 0},
            {"max": 5, "name": 1, "min": -5}
        ],
        "novelty": [
            {"max": 1, "name": 2, "min": -1}
        ],
        "techQuality": [
            {"max": 5, "name": 3, "min": 0}
        ],
        "stateOfArt": [
            {"max": 5, "name": 4, "min": 0}
        ],
        "evaluation": [
            {"max": 5, "name": 5, "min": 0}
        ],
        "significance": [
            {"max": 5, "name": 6, "min": 0}
        ],
        "presentation": [
            {"max": None, "name": "", "min": None}
        ]
    }
},
    "mappingsbody": [1, 2, 0, 3, 3, 2, 1]}
data2["mappingsheader"]["mappings"].keys()
metrics = getMetrics(data2["mappingsheader"]["mappings"], data2["mappingsbody"],
                     list(data2["mappingsheader"]["mappings"].keys()))
if (data["mappingsheader"]["orderMapping"]):
    print("ordermapping")

print(metrics)
