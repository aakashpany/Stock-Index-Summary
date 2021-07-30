import requests
import json
import pandas as pd
import streamlit as st
import datamethods




response = requests.get("https://indexapi.aws.merqurian.com/index?type=test%2Cprod")
data = json.loads(response.text)
url = ''
dataList = []
dataList2 = []
for result in data['results']:
    print(json.dumps(result))
    prodData = datamethods.proddata(result)
    if result['stage'] == "prod":
        dataList.append(prodData)
    else:
        dataList2.append(prodData)

dataset = st.beta_container()

with dataset:
    st.header("Production Table")
    st.write(pd.DataFrame(dataList))
    st.subheader("Non-Production Table")
    st.write(pd.DataFrame(dataList2))
