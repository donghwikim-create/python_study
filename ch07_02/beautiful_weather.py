from urllib import request
import json

# 도시별 격자 좌표
cities = {
    "서울": (60, 127),
    "부산": (98, 76),
    "대구": (89, 90),
    "인천": (55, 124),
    "광주": (58, 74),
    "대전": (67, 100),
    "울산": (102, 84)
}

service_key = "0308ba406254c2ecc5aa5bbe63e7c44d9ab506a9914688d8e062935f1d629644"

base_date = "20260620"
base_time = "1100"

for city, (nx, ny) in cities.items():

    url = (
        f"https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst"
        f"?serviceKey={service_key}"
        f"&pageNo=1"
        f"&numOfRows=1000"
        f"&dataType=JSON"
        f"&base_date={base_date}"
        f"&base_time={base_time}"
        f"&nx={nx}"
        f"&ny={ny}"
    )

    response = request.urlopen(url)
    data = json.loads(response.read().decode("utf-8"))

    items = data["response"]["body"]["items"]["item"]

    weather = ""
    min_temp = ""
    max_temp = ""

    for item in items:
        category = item["category"]

        if category == "SKY" and not weather:
            sky = item["fcstValue"]

            if sky == "1":
                weather = "맑음"
            elif sky == "3":
                weather = "구름많음"
            elif sky == "4":
                weather = "흐림"

        elif category == "TMN":
            min_temp = item["fcstValue"]

        elif category == "TMX":
            max_temp = item["fcstValue"]

    print(f"도시: {city}")
    print(f"날씨: {weather}")
    print(f"최저기온: {min_temp}℃")
    print(f"최고기온: {max_temp}℃")
    print("-" * 30)