import requests
import json

def getMenu(resId):

	url = "https://www.swiggy.com/dapi/menu/pl?page-type=REGULAR_MENU&complete-menu=true&lat=12.9715987&lng=77.5945627&restaurantId="+str(resId)+"&catalog_qa=undefined&submitAction=ENTER"

	payload = {}
	headers = {
	  'authority': 'www.swiggy.com',
	  '__fetch_req__': 'true',
	  'accept': '*/*',
	  'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
	  'content-type': 'application/json',
	  'cookie': '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; fontsLoaded=1; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; _gid=GA1.2.20002083.1699354044; _is_logged_in=1; _session_tid=f2cb44ebb47f9a108dba31127f46f0e38d9fe7360e4ba24fcd7cdbebcf7982b2f03304ad2bb76f3985c64fffd04df5a923f4a370a02b48c575b30ecde687ac05418777976b4ba253b376b7b84b4fb705c72163d4e824cd61e226bba51365deff8bff0c306a32d5aa62f762efcbfd1307; userLocation={%22address%22:%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22%22%2C%22lat%22:12.9715987%2C%22lng%22:77.5945627}; dadl=true; _ga=GA1.2.632603772.1699354044; _ga_34JYJ0BCRN=GS1.1.1699367212.3.0.1699367212.0.0.0; _sid=abv15058-c8eb-4242-87f6-fdf7ef8351b6; _gat_UA-53591212-4=1; _ga_4BQKMMC7Y9=GS1.2.1699367211.2.1.1699368029.60.0.0; _device_id=93f05170-dd94-7668-a8b1-ece02e47604b; _is_logged_in=1; _session_tid=4b0c57186017feea45695988e22f3a5af039b3e32f0d2983e536d1d864a1da83c96e5c0b3794f10be750a507c2499db8964e6528bc41f9d6e96e8931e371acb7ffd06db995c728b521fa577ad8dfc2222b5f70f088cf99d52834e8cd399fadf65a39ba25118400d510aa0dc9b03523ae; _sid=abwf6506-bb2e-4e9b-874f-1ce9eb167cb0',
	  'dnt': '1',
	  'referer': 'https://www.swiggy.com/restaurants/the-baklava-company-race-course-road-central-bangalore-bangalore-729421',
	  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	  'sec-ch-ua-mobile': '?0',
	  'sec-ch-ua-platform': '"macOS"',
	  'sec-fetch-dest': 'empty',
	  'sec-fetch-mode': 'cors',
	  'sec-fetch-site': 'same-origin',
	  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
	}

	response = requests.request("GET", url, headers=headers, data=payload)

	return response.json()
