import json,requests,time
import xlrd
import xlwt
from xlwt import Workbook

read_loc = "/Users/alex/Downloads/TransactionData.xlsx"
write_loc = "/Users/alex/Downloads/TransactionData_Res.xlsx"

def modifyResWithCrsComment(htConfCode):
	url = "https://booking.hoteltrader.com/admin3135/modify"
	#print(url)
	data = {
			    "htConfCode": htConfCode,
			    "sendUpstream": "true",
			    "modifiedBy": "alan@hoteltrader.com",
			    "status": "MODIFY",
			    "rooms": [
			        {
			            "htRoomConfCode": htConfCode + "-1",
			            "status": "MODIFY",
			            "roomOtaSpecialRequestList": ["Room and Tax only paid via VCC.  If issues arise while processing VCC, please contact customerservice@hoteltrader.com or call 1.646-847-9944.  Do not charge the room and tax directly to guest or provide Hotel Trader contact info and our rates to the guest."]
			        }
			    ]
			}
	headers = {'Content-type': 'application/json',
				'Accept': 'application/vnd.paywithextend.v2021-03-12+json'}
	x = requests.post(url, data=json.dumps(data), headers=headers)
	print(x.content)
	time.sleep(10)

res = get_future_synxis_res()

for i in res:
	ht_confirmation_code = str(i[0])
	ht_confirmation_code = ht_confirmation_code.replace("-1","")
	print(ht_confirmation_code)
	modifyResWithCrsComment(ht_confirmation_code)
	break

def writeToSheet() :
	wb2 = Workbook()
	sheet1 = wb2.add_sheet("Sheet 2")

	for index in range(1,708):
		vcc_id = str(read_sheet(index))
		print(vcc_id)
		res=get_res_details(vcc_id)
		print(res)

		style = xlwt.XFStyle()
		style.num_format_str = 'YY-MMM-D h:mm:ss' # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss, [h]:mm:ss, mm:ss.0
		  
		sheet1.write(index, 0, str(res[0][0]))
		sheet1.write(index, 1, str(res[0][1]))
		sheet1.write(index, 2, res[0][2],style)
		sheet1.write(index, 3, str(res[0][3]))
		sheet1.write(index, 4, res[0][4],style)
		sheet1.write(index, 5, str(res[0][5]))
		sheet1.write(index, 6, res[0][6],style)
  
		wb2.save(write_loc)
