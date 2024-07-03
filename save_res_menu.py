import requests
import json
import res_menu
import csv

# name of csv file  
filename = "restuarant_analysis_shawarma.txt"
file = open(filename, 'w')

def saveResMenu(resIds):

	for resId in resIds:
		print(resId)

				# writing to csv file
		resMenu = res_menu.getMenu(resId)
		restuarantInfo = {}
		itemCategories = []
		try:
			restuarantInfo = resMenu['data']['cards'][0]['card']['card']['info']
			print(restuarantInfo)
			itemCategories = resMenu['data']['cards'][2]['groupedCard']['cardGroupMap']['REGULAR']['cards']
		except:
			print(resId + " No data")
			continue
		for itemCategory in itemCategories:
			try:
				if(itemCategory['card']['card']['@type'] == "type.googleapis.com/swiggy.presentation.food.v2.NestedItemCategory"):
					categories = itemCategory['card']['card']['categories']
					for category in categories:
						items = category['itemCards']
						for item in items:
							if "name" in restuarantInfo:
								fields = "" + restuarantInfo['name'].replace(","," ")
							if "areaName" in restuarantInfo:
								fields = fields + "," + restuarantInfo['areaName'].replace(","," ")
							else:
								fields = fields + ","
							if "cuisines" in restuarantInfo:
								fields = fields + "," + ' '.join(map(str, restuarantInfo['cuisines'])).replace(","," ")
							else:
								fields = fields + ","
							if "avgRating" in restuarantInfo:
								fields = fields + "," + str(restuarantInfo['avgRating'])
							else:
								fields = fields + ","
							if "totalRatings" in restuarantInfo:
								fields = fields + "," + str(restuarantInfo['totalRatings'])
							else:
								fields = fields + ","
							if "isOpen" in restuarantInfo:
								fields = fields + "," + str(restuarantInfo['isOpen'])
							else:
								fields = fields + ","
							if "costForTwo" in restuarantInfo:
								fields = fields + "," + str(restuarantInfo['costForTwo'])
							else:
								fields = fields + ","
							if "title" in itemCategory['card']['card']:
								fields = fields + "," + itemCategory['card']['card']['title'].replace(","," ")
							else:
								fields = fields + ","
							if "title" in category:
								fields = fields + "," + category['title'].replace(","," ")
							else:
								fields = fields + ","
							if "name" in item['card']['info']:
								fields = fields + "," + item['card']['info']['name'].replace(","," ")
								itemName = item['card']['info']['name'].replace(","," ")
							else:
								fields = fields + ","
							if "description" in item['card']['info']:
								fields = fields + "," + item['card']['info']['description'].replace(","," ").replace("\n"," ")
							else:
								fields = fields + ","
							if "price" in item['card']['info']:
								fields = fields + "," + str(item['card']['info']['price'])
							else:
								fields = fields + ","
							if "imageId" in item['card']['info']:
								fields = fields + ",Y"
							else:
								fields = fields + ",N"
							if "offerTags" in item['card']['info']:
								fields = fields
								#fields = fields + "," + item['card']['info']['offerTags'][0]['title'].replace(","," ")
							else:
								fields = fields + ", No Offer" 
							if "rating" in item['card']['info']['ratings']['aggregatedRating']:
								fields = fields + "," + item['card']['info']['ratings']['aggregatedRating']['rating']
								fields = fields + "," + item['card']['info']['ratings']['aggregatedRating']['ratingCountV2']
							else:
								fields = fields + "," 
								fields = fields + "," 
							if itemName.find("Shawarma") > 0:
								file.write(fields)
								file.write('\n') 

				if(itemCategory['card']['card']['@type'] == "type.googleapis.com/swiggy.presentation.food.v2.ItemCategory"):
					items = itemCategory['card']['card']['itemCards']
					for item in items:
						if "name" in restuarantInfo:
							fields = "" + restuarantInfo['name'].replace(","," ")
						if "areaName" in restuarantInfo:
							fields = fields + "," + restuarantInfo['areaName'].replace(","," ")
						else:
							fields = fields + ","
						if "cuisines" in restuarantInfo:
							fields = fields + "," + ' '.join(map(str, restuarantInfo['cuisines'])).replace(","," ")
						else:
							fields = fields + ","
						if "avgRating" in restuarantInfo:
							fields = fields + "," + str(restuarantInfo['avgRating'])
						else:
							fields = fields + ","
						if "totalRatings" in restuarantInfo:
							fields = fields + "," + str(restuarantInfo['totalRatings'])
						else:
							fields = fields + ","
						if "isOpen" in restuarantInfo:
							fields = fields + "," + str(restuarantInfo['isOpen'])
						else:
							fields = fields + ","
						if "costForTwo" in restuarantInfo:
							fields = fields + "," + str(restuarantInfo['costForTwo'])
						else:
							fields = fields + ","
							fields = fields + ","
						if "title" in itemCategory['card']['card']:
							fields = fields + "," + itemCategory['card']['card']['title'].replace(","," ")
						else:
							fields = fields + ","
						if "name" in item['card']['info']:
							fields = fields + "," + item['card']['info']['name'].replace(","," ")
							itemName = item['card']['info']['name'].replace(","," ")
						else:
							fields = fields + ","
						if "description" in item['card']['info']:
							fields = fields + "," + item['card']['info']['description'].replace(","," ").replace("\n"," ")
						else:
							fields = fields + ","
						if "price" in item['card']['info']:
							fields = fields + "," + str(item['card']['info']['price'])
						else:
							fields = fields + ","
						if "imageId" in item['card']['info']:
							fields = fields + ",Y"
						else:
							fields = fields + ",N"
						if "offerTags" in item['card']['info']:
							fields = fields
							#fields = fields + "," + item['card']['info']['offerTags'][0]['title'].replace(","," ")
						else:
							fields = fields + ", No Offer" 
						if "rating" in item['card']['info']['ratings']['aggregatedRating']:
							fields = fields + "," + item['card']['info']['ratings']['aggregatedRating']['rating']
							fields = fields + "," + item['card']['info']['ratings']['aggregatedRating']['ratingCountV2']
						else:
							fields = fields + "," 
							fields = fields + "," 
						if itemName.find("Shawarma") > 0:
							file.write(fields)
							file.write('\n') 
			except KeyError:
				print("KeyError")