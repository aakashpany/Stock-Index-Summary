import json
import requests


def proddata(inputResult):
    table = {}
    # id = inputResult['id']
    name = inputResult['name']
    title = inputResult['title']
    url = requests.get("https://indexapi.aws.merqurian.com/index/" + inputResult['id'] + "/metrics/price_return/data")
    data3 = json.loads(url.text)
    result2 = data3['results']
    newLength = len(result2) - 1
    lastObject = result2[newLength]
    last_date = lastObject['id']
    metrics = lastObject['metrics']
    priceObject = metrics[0]
    last_level = priceObject['value']
    for variable in ["name", "title", "last_date", "last_level"]:
        table[variable] = eval(variable)
    return table
