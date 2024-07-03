import requests
import json
import res_menu
import csv


# Change FileName Here
filename = "res_with_dish_listed.txt"
file = open(filename, 'w')
 
def saveResIdsWithDish(resIds, resIdsWithDish):

  for resId in resIds:

    # writing to csv file  

    resMenu = res_menu.getMenu(resId)
    restuarantInfo = {}
    itemCategories = []
    try:
      restuarantInfo = resMenu['data']['cards'][0]['card']['card']['info']
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
              itemName = ""
              if "name" in item['card']['info']:
                itemName = item['card']['info']['name'].replace(","," ")
              #Change ItemName Here
            if (
              itemName.find("Shawarma") >= 0
              or itemName.find("Al-Faham") >= 0
              or itemName.find("Al Faham") >= 0
              or itemName.find("Alfaham") >= 0
              or itemName.find("Kerala Porotta") >= 0
              or itemName.find("Kerala Parotta") >= 0
              or itemName.find("Porotta") >= 0
              or itemName.find("Parotta") >= 0
              ):
                if resId not in resIdsWithDish:
                  resIdsWithDish.append(resId)
                  fields = resId + "," + restuarantInfo['name'].replace(","," ")
                  file.write(fields)
                  file.write('\n') 

        if(itemCategory['card']['card']['@type'] == "type.googleapis.com/swiggy.presentation.food.v2.ItemCategory"):
          items = itemCategory['card']['card']['itemCards']
          for item in items:
            itemName = ""
            if "name" in item['card']['info']:
              itemName = item['card']['info']['name'].replace(","," ")
            if (
              itemName.find("Shawarma") >= 0
              or itemName.find("Al-Faham") >= 0
              or itemName.find("Al Faham") >= 0
              or itemName.find("Alfaham") >= 0
              or itemName.find("Kerala Porotta") >= 0
              or itemName.find("Kerala Parotta") >= 0
              or itemName.find("Porotta") >= 0
              or itemName.find("Parotta") >= 0
              ):
                if resId not in resIdsWithDish:
                  resIdsWithDish.append(resId)
                  fields = resId + "," + restuarantInfo['name'].replace(","," ")
                  file.write(fields)
                  file.write('\n') 
      except Exception as e: 
        print(e)
        continue
  return resIdsWithDish



