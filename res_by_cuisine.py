import requests
import json

url = "https://www.swiggy.com/dapi/restaurants/list/update"

def getResByCuisine():
	payload = json.dumps({
    "lat": 12.9715987,
    "lng": 77.5945627,
    "filters": {
      "isFiltered": True,
      "facets": {
        "catalog_cuisines": [
          {
            "value": "query_arabian"
          },
          {
            "value": "query_kerala"
          }
        ]
      }
    },
    "seoParams": {
      "seoUrl": "https://www.swiggy.com/",
      "pageType": "FOOD_HOMEPAGE",
      "apiName": "FoodHomePage"
    },
    "widgetOffset": {
      "Restaurant_Group_WebView_PB_Theme": "",
      "collectionV5RestaurantListWidget_SimRestoRelevance_food_seo": ""+str(offset)+"",
      "inlineFacetFilter": "",
      "restaurantCountWidget": ""
    },
    "page_type": "DESKTOP_WEB_LISTING",
    "_csrf": "Z7VOyfTJnRWb-dAIqLCKNkO9uIhv8QdUtU4L4Xko"
  })
  headers = {
    'authority': 'www.swiggy.com',
    '__fetch_req__': 'true',
    'accept': '*/*',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'cookie': '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; _sid=absec261-55bf-4858-a7d9-72ad11c11525; fontsLoaded=1; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; _gid=GA1.2.20002083.1699354044; _is_logged_in=1; _session_tid=f2cb44ebb47f9a108dba31127f46f0e38d9fe7360e4ba24fcd7cdbebcf7982b2f03304ad2bb76f3985c64fffd04df5a923f4a370a02b48c575b30ecde687ac05418777976b4ba253b376b7b84b4fb705c72163d4e824cd61e226bba51365deff8bff0c306a32d5aa62f762efcbfd1307; userLocation={%22address%22:%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22%22%2C%22lat%22:12.9715987%2C%22lng%22:77.5945627}; dadl=true; _ga_4BQKMMC7Y9=GS1.2.1699354156.1.1.1699354775.28.0.0; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A1%2C%22s%22%3A1699357473%2C%22t%22%3A1699357473%7D; _gat_0=1; _ga_34JYJ0BCRN=GS1.1.1699357472.2.1.1699357473.0.0.0; _ga=GA1.1.632603772.1699354044; _device_id=93f05170-dd94-7668-a8b1-ece02e47604b; _is_logged_in=1; _session_tid=55bf98cefbc8f1f938c52f9a8b91488f3d1475a4071e4d34870c16baa9b9bb8f6d9d9f3d0125b7f6f7844be672a9888fa1a70545597cb3d6e52d163a84e69092a84e34cfada581a377cf674609c8c15b30aec922ea5166561f20108fd5df00e7e7370307c547ef7bb5d54359de8c4519; _sid=absd938d-7659-4f14-b6a5-16f72462b576',
    'dnt': '1',
    'origin': 'https://www.swiggy.com',
    'referer': 'https://www.swiggy.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  jsonResponse = response.json()

  statusCode = jsonResponse['statusCode']

  resIds = []

  if(jsonResponse['statusCode'] == 0):
    restaurants = jsonResponse['data']['cards'][0]['card']['card']['gridElements']['infoWithStyle']['restaurants']
    for restaurant in restaurants:
      isArabian = 0 
      isKerala = 0
      for cuisine in restaurant['info']['cuisines']:
        if(cuisine == "Arabian"):
          isArabian = 1
        if(cuisine == "Kerala"):
          isKerala = 1
      if(isArabian == 1 or isKerala == 1):
        resIds.append(restaurant['info']['id'])
        print(restaurant['info']['id'] + "  " + restaurant['info']['name'])
      offset = offset + 1
