import requests
import json
import res_menu
import csv
from enum import Enum


resIdsMaster = []
# name of csv file  
filename = "restuarant_list_location.txt"
file = open(filename, 'w')

url = "https://www.swiggy.com/dapi/restaurants/list/update"

class Location(Enum):
    # Location = latitude, longitude, cookie
    #Bengaluru = 12.9715987, 77.5945627, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; _sid=absec261-55bf-4858-a7d9-72ad11c11525; fontsLoaded=1; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; _gid=GA1.2.20002083.1699354044; _is_logged_in=1; _session_tid=f2cb44ebb47f9a108dba31127f46f0e38d9fe7360e4ba24fcd7cdbebcf7982b2f03304ad2bb76f3985c64fffd04df5a923f4a370a02b48c575b30ecde687ac05418777976b4ba253b376b7b84b4fb705c72163d4e824cd61e226bba51365deff8bff0c306a32d5aa62f762efcbfd1307; userLocation={%22address%22:%22Bengaluru%2C%20Karnataka%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22%22%2C%22lat%22:12.9715987%2C%22lng%22:77.5945627}; dadl=true; _ga_4BQKMMC7Y9=GS1.2.1699354156.1.1.1699354775.28.0.0; WZRK_S_W86-ZZK-WR6Z=%7B%22p%22%3A1%2C%22s%22%3A1699357473%2C%22t%22%3A1699357473%7D; _gat_0=1; _ga_34JYJ0BCRN=GS1.1.1699357472.2.1.1699357473.0.0.0; _ga=GA1.1.632603772.1699354044; _device_id=93f05170-dd94-7668-a8b1-ece02e47604b; _is_logged_in=1; _session_tid=55bf98cefbc8f1f938c52f9a8b91488f3d1475a4071e4d34870c16baa9b9bb8f6d9d9f3d0125b7f6f7844be672a9888fa1a70545597cb3d6e52d163a84e69092a84e34cfada581a377cf674609c8c15b30aec922ea5166561f20108fd5df00e7e7370307c547ef7bb5d54359de8c4519; _sid=absd938d-7659-4f14-b6a5-16f72462b576'
    Kannuru = 13.0927094, 77.6547023, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; deviceId=s%3Ad88234b2-820e-bd2c-7ce9-e14b343c8e28.RCXo5of%2FRWQu2nIQzy35xEqBbb7r%2B%2BxFmM60LgIgY8c; versionCode=1200; platform=web; subplatform=mweb; statusBarHeight=0; bottomOffset=0; genieWebTrackEnabled=false; accessibility-enabled=false; lat=s%3A12.9715987.H8kN2HbLClMk82S%2FOPQk%2FWfg8UZxpPZxCVuehLrjzz0; lng=s%3A77.5945627.6hoVNIeUVmIOLLWjqb2ZrBnIbpDixu8o9%2B6qRTMmxu8; address=s%3ABengaluru%2C%20Karnataka%2C%20India.yWk8cXWQtla5Dulo0B%2BBVAVIJr%2FTDzDFsKhCLQN6mjA; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; tid=s%3A9568d26d-61e3-4a88-94f9-0158a19782dc.4%2FVjIseDz64vZWpLUOP5tPzrnkAJo6vmx0zmTG09mVA; _ga_0N81HC0898=GS1.1.1702752544.1.0.1702752545.0.0.0; fontsLoaded=1; _gid=GA1.2.209256776.1703159384; dadl=true; _ga_YD063E4XCC=GS1.2.1703174570.1.0.1703174570.0.0.0; _ga_76P34S6XQ2=GS1.1.1703174569.1.0.1703174574.0.0.0; _ga_LK8E6WBG6G=GS1.1.1703174570.1.0.1703174574.0.0.0; _ga_7JY7T788PK=GS1.1.1703174626.1.1.1703174708.0.0.0; _ga=GA1.2.632603772.1699354044; _guest_tid=56e130cc-a411-49f1-a0f7-c6aa9e529495; _sid=b5dd372f-b888-4390-97ee-93e5ce74ff74; _gat_UA-53591212-4=1; _ga_4BQKMMC7Y9=GS1.2.1703188818.11.1.1703190082.60.0.0; _ga_34JYJ0BCRN=GS1.1.1703188820.16.1.1703190083.0.0.0; userLocation={%22address%22:%22Kannuru%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Kannuru%22%2C%22lat%22:13.0927094%2C%22lng%22:77.6547023}'
    Kothanur = 13.0551932, 77.6422206, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; deviceId=s%3Ad88234b2-820e-bd2c-7ce9-e14b343c8e28.RCXo5of%2FRWQu2nIQzy35xEqBbb7r%2B%2BxFmM60LgIgY8c; versionCode=1200; platform=web; subplatform=mweb; statusBarHeight=0; bottomOffset=0; genieWebTrackEnabled=false; accessibility-enabled=false; lat=s%3A12.9715987.H8kN2HbLClMk82S%2FOPQk%2FWfg8UZxpPZxCVuehLrjzz0; lng=s%3A77.5945627.6hoVNIeUVmIOLLWjqb2ZrBnIbpDixu8o9%2B6qRTMmxu8; address=s%3ABengaluru%2C%20Karnataka%2C%20India.yWk8cXWQtla5Dulo0B%2BBVAVIJr%2FTDzDFsKhCLQN6mjA; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; tid=s%3A9568d26d-61e3-4a88-94f9-0158a19782dc.4%2FVjIseDz64vZWpLUOP5tPzrnkAJo6vmx0zmTG09mVA; _ga_0N81HC0898=GS1.1.1702752544.1.0.1702752545.0.0.0; fontsLoaded=1; _gid=GA1.2.209256776.1703159384; dadl=true; _ga_YD063E4XCC=GS1.2.1703174570.1.0.1703174570.0.0.0; _ga_76P34S6XQ2=GS1.1.1703174569.1.0.1703174574.0.0.0; _ga_LK8E6WBG6G=GS1.1.1703174570.1.0.1703174574.0.0.0; _ga_7JY7T788PK=GS1.1.1703174626.1.1.1703174708.0.0.0; _ga=GA1.2.632603772.1699354044; _guest_tid=56e130cc-a411-49f1-a0f7-c6aa9e529495; _sid=b5dd372f-b888-4390-97ee-93e5ce74ff74; _ga_4BQKMMC7Y9=GS1.2.1703188818.11.1.1703190082.60.0.0; _ga_34JYJ0BCRN=GS1.1.1703188820.16.1.1703190083.0.0.0; userLocation={%22address%22:%22Kothanur%2C%20Bengaluru%2C%20Karnataka%20560077%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Kothanur%22%2C%22lat%22:13.0551932%2C%22lng%22:77.6422206}'
    Hennur = 13.0359337, 77.64314759999999, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; deviceId=s%3Ad88234b2-820e-bd2c-7ce9-e14b343c8e28.RCXo5of%2FRWQu2nIQzy35xEqBbb7r%2B%2BxFmM60LgIgY8c; versionCode=1200; platform=web; subplatform=mweb; statusBarHeight=0; bottomOffset=0; genieWebTrackEnabled=false; accessibility-enabled=false; lat=s%3A12.9715987.H8kN2HbLClMk82S%2FOPQk%2FWfg8UZxpPZxCVuehLrjzz0; lng=s%3A77.5945627.6hoVNIeUVmIOLLWjqb2ZrBnIbpDixu8o9%2B6qRTMmxu8; address=s%3ABengaluru%2C%20Karnataka%2C%20India.yWk8cXWQtla5Dulo0B%2BBVAVIJr%2FTDzDFsKhCLQN6mjA; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; tid=s%3A9568d26d-61e3-4a88-94f9-0158a19782dc.4%2FVjIseDz64vZWpLUOP5tPzrnkAJo6vmx0zmTG09mVA; _ga_0N81HC0898=GS1.1.1702752544.1.0.1702752545.0.0.0; fontsLoaded=1; _gid=GA1.2.209256776.1703159384; dadl=true; _ga_YD063E4XCC=GS1.2.1703174570.1.0.1703174570.0.0.0; _ga_76P34S6XQ2=GS1.1.1703174569.1.0.1703174574.0.0.0; _ga_LK8E6WBG6G=GS1.1.1703174570.1.0.1703174574.0.0.0; _ga_7JY7T788PK=GS1.1.1703174626.1.1.1703174708.0.0.0; _ga=GA1.2.632603772.1699354044; _guest_tid=56e130cc-a411-49f1-a0f7-c6aa9e529495; _sid=b5dd372f-b888-4390-97ee-93e5ce74ff74; _ga_4BQKMMC7Y9=GS1.2.1703188818.11.1.1703190082.60.0.0; _ga_34JYJ0BCRN=GS1.1.1703188820.16.1.1703190083.0.0.0; userLocation={%22address%22:%22Hennur%20Gardens%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Hennur%20Gardens%22%2C%22lat%22:13.0359337%2C%22lng%22:77.64314759999999}'
    Bagalur = 13.151285, 77.668837, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; deviceId=s%3Ad88234b2-820e-bd2c-7ce9-e14b343c8e28.RCXo5of%2FRWQu2nIQzy35xEqBbb7r%2B%2BxFmM60LgIgY8c; versionCode=1200; platform=web; subplatform=mweb; statusBarHeight=0; bottomOffset=0; genieWebTrackEnabled=false; accessibility-enabled=false; lat=s%3A12.9715987.H8kN2HbLClMk82S%2FOPQk%2FWfg8UZxpPZxCVuehLrjzz0; lng=s%3A77.5945627.6hoVNIeUVmIOLLWjqb2ZrBnIbpDixu8o9%2B6qRTMmxu8; address=s%3ABengaluru%2C%20Karnataka%2C%20India.yWk8cXWQtla5Dulo0B%2BBVAVIJr%2FTDzDFsKhCLQN6mjA; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; tid=s%3A9568d26d-61e3-4a88-94f9-0158a19782dc.4%2FVjIseDz64vZWpLUOP5tPzrnkAJo6vmx0zmTG09mVA; _ga_0N81HC0898=GS1.1.1702752544.1.0.1702752545.0.0.0; fontsLoaded=1; _gid=GA1.2.209256776.1703159384; dadl=true; _ga_YD063E4XCC=GS1.2.1703174570.1.0.1703174570.0.0.0; _ga_76P34S6XQ2=GS1.1.1703174569.1.0.1703174574.0.0.0; _ga_LK8E6WBG6G=GS1.1.1703174570.1.0.1703174574.0.0.0; _ga_7JY7T788PK=GS1.1.1703174626.1.1.1703174708.0.0.0; _ga=GA1.2.632603772.1699354044; _guest_tid=56e130cc-a411-49f1-a0f7-c6aa9e529495; _sid=b5dd372f-b888-4390-97ee-93e5ce74ff74; _ga_4BQKMMC7Y9=GS1.2.1703188818.11.1.1703190082.60.0.0; _ga_34JYJ0BCRN=GS1.1.1703188820.16.1.1703190083.0.0.0; userLocation={%22address%22:%22Bagalur%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Bagalur%22%2C%22lat%22:13.151285%2C%22lng%22:77.668837}'
    ChikkagubbiVillage = 13.0807009, 77.6622027, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; deviceId=s%3Ad88234b2-820e-bd2c-7ce9-e14b343c8e28.RCXo5of%2FRWQu2nIQzy35xEqBbb7r%2B%2BxFmM60LgIgY8c; versionCode=1200; platform=web; subplatform=mweb; statusBarHeight=0; bottomOffset=0; genieWebTrackEnabled=false; accessibility-enabled=false; lat=s%3A12.9715987.H8kN2HbLClMk82S%2FOPQk%2FWfg8UZxpPZxCVuehLrjzz0; lng=s%3A77.5945627.6hoVNIeUVmIOLLWjqb2ZrBnIbpDixu8o9%2B6qRTMmxu8; address=s%3ABengaluru%2C%20Karnataka%2C%20India.yWk8cXWQtla5Dulo0B%2BBVAVIJr%2FTDzDFsKhCLQN6mjA; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; tid=s%3A9568d26d-61e3-4a88-94f9-0158a19782dc.4%2FVjIseDz64vZWpLUOP5tPzrnkAJo6vmx0zmTG09mVA; _ga_0N81HC0898=GS1.1.1702752544.1.0.1702752545.0.0.0; fontsLoaded=1; _gid=GA1.2.209256776.1703159384; dadl=true; _ga_YD063E4XCC=GS1.2.1703174570.1.0.1703174570.0.0.0; _ga_76P34S6XQ2=GS1.1.1703174569.1.0.1703174574.0.0.0; _ga_LK8E6WBG6G=GS1.1.1703174570.1.0.1703174574.0.0.0; _ga_7JY7T788PK=GS1.1.1703174626.1.1.1703174708.0.0.0; _ga=GA1.2.632603772.1699354044; _guest_tid=56e130cc-a411-49f1-a0f7-c6aa9e529495; _sid=b5dd372f-b888-4390-97ee-93e5ce74ff74; _ga_4BQKMMC7Y9=GS1.2.1703188818.11.1.1703190082.60.0.0; _ga_34JYJ0BCRN=GS1.1.1703188820.16.1.1703190083.0.0.0; userLocation={%22address%22:%22Chikkagubbi%20Village%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Chikkagubbi%20Village%22%2C%22lat%22:13.0807009%2C%22lng%22:77.6622027}'
    Belahalli = 13.1004985, 77.6426919, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; deviceId=s%3Ad88234b2-820e-bd2c-7ce9-e14b343c8e28.RCXo5of%2FRWQu2nIQzy35xEqBbb7r%2B%2BxFmM60LgIgY8c; versionCode=1200; platform=web; subplatform=mweb; statusBarHeight=0; bottomOffset=0; genieWebTrackEnabled=false; accessibility-enabled=false; lat=s%3A12.9715987.H8kN2HbLClMk82S%2FOPQk%2FWfg8UZxpPZxCVuehLrjzz0; lng=s%3A77.5945627.6hoVNIeUVmIOLLWjqb2ZrBnIbpDixu8o9%2B6qRTMmxu8; address=s%3ABengaluru%2C%20Karnataka%2C%20India.yWk8cXWQtla5Dulo0B%2BBVAVIJr%2FTDzDFsKhCLQN6mjA; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; tid=s%3A9568d26d-61e3-4a88-94f9-0158a19782dc.4%2FVjIseDz64vZWpLUOP5tPzrnkAJo6vmx0zmTG09mVA; _ga_0N81HC0898=GS1.1.1702752544.1.0.1702752545.0.0.0; fontsLoaded=1; _gid=GA1.2.209256776.1703159384; dadl=true; _ga_YD063E4XCC=GS1.2.1703174570.1.0.1703174570.0.0.0; _ga_76P34S6XQ2=GS1.1.1703174569.1.0.1703174574.0.0.0; _ga_LK8E6WBG6G=GS1.1.1703174570.1.0.1703174574.0.0.0; _ga_7JY7T788PK=GS1.1.1703174626.1.1.1703174708.0.0.0; _ga=GA1.2.632603772.1699354044; _guest_tid=56e130cc-a411-49f1-a0f7-c6aa9e529495; _sid=b5dd372f-b888-4390-97ee-93e5ce74ff74; _ga_4BQKMMC7Y9=GS1.2.1703188818.11.1.1703190082.60.0.0; _ga_34JYJ0BCRN=GS1.1.1703188820.16.1.1703190083.0.0.0; userLocation={%22address%22:%22Bellahalli%2C%20Bengaluru%2C%20Karnataka%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Bellahalli%22%2C%22lat%22:13.1004985%2C%22lng%22:77.6426919}'
    Visthar = 13.0701427, 77.6590526, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; deviceId=s%3Ad88234b2-820e-bd2c-7ce9-e14b343c8e28.RCXo5of%2FRWQu2nIQzy35xEqBbb7r%2B%2BxFmM60LgIgY8c; versionCode=1200; platform=web; subplatform=mweb; statusBarHeight=0; bottomOffset=0; genieWebTrackEnabled=false; accessibility-enabled=false; lat=s%3A12.9715987.H8kN2HbLClMk82S%2FOPQk%2FWfg8UZxpPZxCVuehLrjzz0; lng=s%3A77.5945627.6hoVNIeUVmIOLLWjqb2ZrBnIbpDixu8o9%2B6qRTMmxu8; address=s%3ABengaluru%2C%20Karnataka%2C%20India.yWk8cXWQtla5Dulo0B%2BBVAVIJr%2FTDzDFsKhCLQN6mjA; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; tid=s%3A9568d26d-61e3-4a88-94f9-0158a19782dc.4%2FVjIseDz64vZWpLUOP5tPzrnkAJo6vmx0zmTG09mVA; _ga_0N81HC0898=GS1.1.1702752544.1.0.1702752545.0.0.0; fontsLoaded=1; _gid=GA1.2.209256776.1703159384; dadl=true; _ga_YD063E4XCC=GS1.2.1703174570.1.0.1703174570.0.0.0; _ga_76P34S6XQ2=GS1.1.1703174569.1.0.1703174574.0.0.0; _ga_LK8E6WBG6G=GS1.1.1703174570.1.0.1703174574.0.0.0; _ga_7JY7T788PK=GS1.1.1703174626.1.1.1703174708.0.0.0; _ga=GA1.2.632603772.1699354044; _guest_tid=56e130cc-a411-49f1-a0f7-c6aa9e529495; _sid=b5dd372f-b888-4390-97ee-93e5ce74ff74; _ga_4BQKMMC7Y9=GS1.2.1703188818.11.1.1703190082.60.0.0; _ga_34JYJ0BCRN=GS1.1.1703188820.16.1.1703190083.0.0.0; userLocation={%22address%22:%22Visthar%2C%20Bengaluru%2C%20Karnataka%20560077%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Visthar%22%2C%22lat%22:13.0701427%2C%22lng%22:77.6590526}'
    RammanaLayout = 13.0521424, 77.656476, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; deviceId=s%3Ad88234b2-820e-bd2c-7ce9-e14b343c8e28.RCXo5of%2FRWQu2nIQzy35xEqBbb7r%2B%2BxFmM60LgIgY8c; versionCode=1200; platform=web; subplatform=mweb; statusBarHeight=0; bottomOffset=0; genieWebTrackEnabled=false; accessibility-enabled=false; lat=s%3A12.9715987.H8kN2HbLClMk82S%2FOPQk%2FWfg8UZxpPZxCVuehLrjzz0; lng=s%3A77.5945627.6hoVNIeUVmIOLLWjqb2ZrBnIbpDixu8o9%2B6qRTMmxu8; address=s%3ABengaluru%2C%20Karnataka%2C%20India.yWk8cXWQtla5Dulo0B%2BBVAVIJr%2FTDzDFsKhCLQN6mjA; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; tid=s%3A9568d26d-61e3-4a88-94f9-0158a19782dc.4%2FVjIseDz64vZWpLUOP5tPzrnkAJo6vmx0zmTG09mVA; _ga_0N81HC0898=GS1.1.1702752544.1.0.1702752545.0.0.0; fontsLoaded=1; _gid=GA1.2.209256776.1703159384; dadl=true; _ga_YD063E4XCC=GS1.2.1703174570.1.0.1703174570.0.0.0; _ga_76P34S6XQ2=GS1.1.1703174569.1.0.1703174574.0.0.0; _ga_LK8E6WBG6G=GS1.1.1703174570.1.0.1703174574.0.0.0; _ga_7JY7T788PK=GS1.1.1703174626.1.1.1703174708.0.0.0; _ga=GA1.2.632603772.1699354044; _guest_tid=56e130cc-a411-49f1-a0f7-c6aa9e529495; _sid=b5dd372f-b888-4390-97ee-93e5ce74ff74; _ga_4BQKMMC7Y9=GS1.2.1703188818.11.1.1703190082.60.0.0; _ga_34JYJ0BCRN=GS1.1.1703188820.16.1.1703190083.0.0.0; userLocation={%22address%22:%22Rammana%20Layout%2C%20Bengaluru%2C%20Karnataka%20560077%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22%22%2C%22lat%22:13.0521424%2C%22lng%22:77.656476}'
    KalyanNagar = 13.0239923, 77.643294, '__SW=H8agoKjjkvD3FHRlrtjYRcxbh9FWDZMv; _device_id=d88234b2-820e-bd2c-7ce9-e14b343c8e28; WZRK_G=ca303006ebc843ec8af16a6e44395d83; _gcl_au=1.1.791078301.1699354043; deviceId=s%3Ad88234b2-820e-bd2c-7ce9-e14b343c8e28.RCXo5of%2FRWQu2nIQzy35xEqBbb7r%2B%2BxFmM60LgIgY8c; versionCode=1200; platform=web; subplatform=mweb; statusBarHeight=0; bottomOffset=0; genieWebTrackEnabled=false; accessibility-enabled=false; lat=s%3A12.9715987.H8kN2HbLClMk82S%2FOPQk%2FWfg8UZxpPZxCVuehLrjzz0; lng=s%3A77.5945627.6hoVNIeUVmIOLLWjqb2ZrBnIbpDixu8o9%2B6qRTMmxu8; address=s%3ABengaluru%2C%20Karnataka%2C%20India.yWk8cXWQtla5Dulo0B%2BBVAVIJr%2FTDzDFsKhCLQN6mjA; addressId=s%3A.4Wx2Am9WLolnmzVcU32g6YaFDw0QbIBFRj2nkO7P25s; tid=s%3A9568d26d-61e3-4a88-94f9-0158a19782dc.4%2FVjIseDz64vZWpLUOP5tPzrnkAJo6vmx0zmTG09mVA; _ga_0N81HC0898=GS1.1.1702752544.1.0.1702752545.0.0.0; fontsLoaded=1; _gid=GA1.2.209256776.1703159384; dadl=true; _ga_YD063E4XCC=GS1.2.1703174570.1.0.1703174570.0.0.0; _ga_76P34S6XQ2=GS1.1.1703174569.1.0.1703174574.0.0.0; _ga_LK8E6WBG6G=GS1.1.1703174570.1.0.1703174574.0.0.0; _ga_7JY7T788PK=GS1.1.1703174626.1.1.1703174708.0.0.0; _ga=GA1.2.632603772.1699354044; _guest_tid=56e130cc-a411-49f1-a0f7-c6aa9e529495; _sid=b5dd372f-b888-4390-97ee-93e5ce74ff74; _ga_4BQKMMC7Y9=GS1.2.1703188818.11.1.1703190082.60.0.0; _ga_34JYJ0BCRN=GS1.1.1703188820.16.1.1703190083.0.0.0; userLocation={%22address%22:%22Kalyan%20Nagar%2C%20Bengaluru%2C%20Karnataka%20560043%2C%20India%22%2C%22area%22:%22%22%2C%22deliveryLocation%22:%22Kalyan%20Nagar%22%2C%22lat%22:13.0239923%2C%22lng%22:77.643294}'


    def __init__(self, latitude, longitude, cookie):
        self.lat = latitude
        self.lng = longitude
        self.cookie = cookie

for location in Location:
    print(location)
    offset = 1
    statusCode = 0

    while statusCode == 0:

        payload = json.dumps({
            "lat": location.lat,
            "lng": location.lng,
            "filters": {
                "isFiltered": False,
                "facets": {
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
            'cookie': location.cookie,
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
            try:
                restaurants = jsonResponse['data']['cards'][0]['card']['card']['gridElements']['infoWithStyle']['restaurants']
                for restaurant in restaurants:
                    resId = restaurant['info']['id']
                    resIds.append(resId)
                    if resId not in resIdsMaster:
                        resIdsMaster.append(resId)
                        #print(restaurant['info']['id'] + "  " + restaurant['info']['name'])
                    offset = offset + 1
            except:
                statusCode = 1

        if len(resIds) == 0:
            statusCode = 1



print("Total number of restaurants in location : " + str(len(resIdsMaster)))

for resId in resIdsMaster:

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
                            fields = fields
                            #fields = fields + ", No Offer" 
                        if "rating" in item['card']['info']['ratings']['aggregatedRating']:
                            fields = fields + "," + item['card']['info']['ratings']['aggregatedRating']['rating']
                            fields = fields + "," + item['card']['info']['ratings']['aggregatedRating']['ratingCountV2']
                        else:
                            fields = fields + "," 
                            fields = fields + "," 
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
                        fields = fields
                        #fields = fields + ", No Offer" 
                    if "rating" in item['card']['info']['ratings']['aggregatedRating']:
                        fields = fields + "," + item['card']['info']['ratings']['aggregatedRating']['rating']
                        fields = fields + "," + item['card']['info']['ratings']['aggregatedRating']['ratingCountV2']
                    else:
                        fields = fields + "," 
                        fields = fields + "," 
                    file.write(fields)
                    file.write('\n') 
        except KeyError:
            print("KeyError")



