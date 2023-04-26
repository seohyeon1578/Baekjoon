import requests
import json
import pandas as pd
from datetime import datetime, timedelta
from urllib import parse
from geopy.geocoders import Nominatim
import math
NX = 149            ## X축 격자점 수
NY = 253            ## Y축 격자점 수

Re = 6371.00877     ##  지도반경
grid = 5.0          ##  격자간격 (km)
slat1 = 30.0        ##  표준위도 1
slat2 = 60.0        ##  표준위도 2
olon = 126.0        ##  기준점 경도
olat = 38.0         ##  기준점 위도
xo = 210 / grid     ##  기준점 X좌표
yo = 675 / grid     ##  기준점 Y좌표
first = 0

if first == 0 :
    PI = math.asin(1.0) * 2.0
    DEGRAD = PI/ 180.0
    RADDEG = 180.0 / PI


    re = Re / grid
    slat1 = slat1 * DEGRAD
    slat2 = slat2 * DEGRAD
    olon = olon * DEGRAD
    olat = olat * DEGRAD

    sn = math.tan(PI * 0.25 + slat2 * 0.5) / math.tan(PI * 0.25 + slat1 * 0.5)
    sn = math.log(math.cos(slat1) / math.cos(slat2)) / math.log(sn)
    sf = math.tan(PI * 0.25 + slat1 * 0.5)
    sf = math.pow(sf, sn) * math.cos(slat1) / sn
    ro = math.tan(PI * 0.25 + olat * 0.5)
    ro = re * sf / math.pow(ro, sn)
    first = 1

def mapToGrid(lat, lon, code = 0 ):
    ra = math.tan(PI * 0.25 + lat * DEGRAD * 0.5)
    ra = re * sf / pow(ra, sn)
    theta = lon * DEGRAD - olon
    if theta > PI :
        theta -= 2.0 * PI
    if theta < -PI :
        theta += 2.0 * PI
    theta *= sn
    x = (ra * math.sin(theta)) + xo
    y = (ro - ra * math.cos(theta)) + yo
    x = int(x + 1.5)
    y = int(y + 1.5)
    return x, y

def gridToMap(x, y, code = 1):
    x = x - 1
    y = y - 1
    xn = x - xo
    yn = ro - y + yo
    ra = math.sqrt(xn * xn + yn * yn)
    if sn < 0.0 :
        ra = -ra
    alat = math.pow((re * sf / ra), (1.0 / sn))
    alat = 2.0 * math.atan(alat) - PI * 0.5
    if math.fabs(xn) <= 0.0 :
        theta = 0.0
    else :
        if math.fabs(yn) <= 0.0 :
            theta = PI * 0.5
            if xn < 0.0 :
                theta = -theta
        else :
            theta = math.atan2(xn, yn)
    alon = theta / sn + olon
    lat = alat * RADDEG
    lon = alon * RADDEG

    return lat, lon
def getBaseTime(base_time):
    base_time_units = {
        "0200": 210,
        "0500": 510,
        "0800": 810,
        "1100": 1110,
        "1400": 1410,
        "1700": 1710,
        "2000": 2010,
        "2300": 2310,
    }
    temp = []

    for time in base_time_units.values():
        temp.append(abs(base_time - time))

    return list(base_time_units.keys())[temp.index(min(temp))]

def geocoding(city):
    # geolocoder = Nominatim(user_agent = "South Korea", timeout=None)
    # geo = geolocoder.geocode(city)
    # crd = {
    #     "lat": geo.latitude,
    #     "lng": geo.longitude,
    # }
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + city
    headers= { "Authorization": "KakaoAK c55160d492298961f53ccb9234fb13ec"}
    api_json = json.loads(str(requests.get(url, headers=headers).text))
    address = api_json['documents'][0]['address']
    crd = {
        "lat": float(address['y']),
        "lng": float(address['x']),
    }

    return crd 
url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst'
date = datetime.today() - timedelta(hours=1)
base_date = date.strftime('%Y%m%d')
time = int(date.strftime('%H%M'))
base_time = getBaseTime(time)
xylist = pd.read_csv("C:/Users/DGSW/Documents/GitHub/Baekjoon/GOLD/기상청41_단기예보_격자_위경도_20221027_.csv", encoding="UTF-8")
uniq_xylist = xylist[['격자 X', '격자 Y']].drop_duplicates()
crd = geocoding("서울특별시")
x, y = mapToGrid(crd['lat'], crd['lng'])

print(crd)
print(base_time)
key = 'ZgGKqYwRYT%2FCl0H5xEowPF8NzgWoBStTDqduub1m12t3GeAY9dmVitguWV5pRBUFpKExZJx8c4ZXBOTe5wt8OQ%3D%3D'
params = f'?{parse.quote_plus("ServiceKey")}={key}&' + parse.urlencode({
    parse.quote_plus('numOfRows') : '14',
    parse.quote_plus('pageNo') : '1',
    parse.quote_plus('dataType') : 'JSON',
    parse.quote_plus('base_date') : 20230421,
    parse.quote_plus('base_time') : base_time,
    parse.quote_plus('nx') : ｘ,
    parse.quote_plus('ny') : ｙ,
})

response = requests.get(url + params)
text = response.text

data = json.loads(text)
if data["response"]["header"]["resultCode"] == '00':
    for item in data["response"]["body"]["items"]["item"]:
        if item["category"] == "POP":
            pop = item["fcstValue"]
        elif item["category"] == "SKY":
            sky = int(item["fcstValue"])
        elif item["category"] == "REH":
            reh = item["fcstValue"]
        elif item["category"] == "TMP":
            tmp = item["fcstValue"]
        elif item["category"] == "TMX":
            tmx = item["fcstValue"]
        elif item["category"] == "TMN":
            tmn = item["fcstValue"]
    if 0 <= sky <= 5:
        sky = "맑음"
    elif 6 <= sky <= 8:
        sky = "구름많음"
    elif 9 <= sky <= 10:
        sky = "흐림"
    result= '현재 온도 : {} \n강수확률: {} \n습도: {}\n구름: {}'.format(tmp, pop, reh, sky)
    print(result)
else:
    print('최근 3일내의 데이터만 가능')

# url = 'http://apis.data.go.kr/1360000/MidFcstInfoService/getMidFcst'
# key = 'ZgGKqYwRYT%2FCl0H5xEowPF8NzgWoBStTDqduub1m12t3GeAY9dmVitguWV5pRBUFpKExZJx8c4ZXBOTe5wt8OQ%3D%3D'
# params = f'?{parse.quote_plus("serviceKey")}={key}&' + parse.urlencode({
#     parse.quote_plus('pageNo') : '1',
#     parse.quote_plus('numOfRows') : '10',
#     parse.quote_plus('dataType') : 'JSON',
#     parse.quote_plus('stnId') : '108',
#     parse.quote_plus('tmFc') : '202304170600',
# })
# response = requests.get(url + params)
# text = response.text
# print(text)