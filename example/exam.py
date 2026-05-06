# Python3 샘플 코드 #

import requests

url = 'http://apis.data.go.kr/1360000/RoadWthrInfoService/getCctvStnRoadWthr'
params ={'serviceKey' : '93e8e5a04758638ec6a8cc1f0edd690dd860ea0c08864b3401a482270558da39', 'pageNo' : '1', 'numOfRows' : '10', 'dataType' : 'XML', 'eqmtId' : '0500C00001', 'hhCode' : '00' }

response = requests.get(url, params=params)
print(response.content)



