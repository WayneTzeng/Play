import sys
import time
import urllib.request as request
import json
Placename = {
                  0 : 'F-D0047-049',  #'基隆市'
                  1 : 'F-D0047-061',  #'臺北市'
                  2 : 'F-D0047-069',  #'新北市'             
                  3 : 'F-D0047-005',  #'桃園市'
                  4 : 'F-D0047-009',  #'新竹縣'
                  5 : 'F-D0047-013',  #'苗栗縣'
                  6 : 'F-D0047-053',  #'新竹市'
                  7 : 'F-D0047-073',  #'臺中市'
                  8 : 'F-D0047-021',  #'南投縣'
                  9 : 'F-D0047-017',  #'彰化縣'
                 10 : 'F-D0047-025',  #'雲林縣'
                 11 : 'F-D0047-057',  #'嘉義市'
                 12 : 'F-D0047-029',  #'嘉義縣'
                 13 : 'F-D0047-077',  #'臺南市'
                 14 : 'F-D0047-065',  #'高雄市'
                 15 : 'F-D0047-033',  #'屏東縣'
                 16 : 'F-D0047-001',  #'宜蘭縣'
                 17 : 'F-D0047-041',  #'花蓮縣'
                 18 : 'F-D0047-037',  #'臺東縣'
                 19 : 'F-D0047-045',  #'澎湖縣'
                 20 : 'F-D0047-081',  #'連江縣'
                 21 : 'F-D0047-085',  #'金門縣'
}
for q in Placename:
    PlaceNo = Placename[q]
    #print(PlaceNo)
    #print(PlaceNo)

localtime = time.strftime("%Y-%m-%dT24:00:00",time.localtime())
        
#氣象資料表
#DATA = ['F-D0047-089','F-C0032-001',]

HTTPLINE =  {
                'scheme':'https://',
                'netloc':'opendata.cwb.gov.tw',
                'path':'/api/v1/rest/datastore/',
                #'DATA': PlaceNo ,
                'Authorization': '?Authorization=CWB-C4D5FA06-0CE0-4F90-B004-B08ECDDF5EF8', 
                'elementName': 'elementName=PoP6h,AT,CI,WX',
                'limit': 'limit=36', 
                'timeTo': "timeTo="+localtime,
                'format': 'format=JSON',

    }
#print(HTTPLINE['DATA'])
for q in Placename:
    PlaceNo = Placename[q]
    #for url in range(0,22):
    HTTP_1 = HTTPLINE['scheme']+HTTPLINE['netloc']+HTTPLINE['path']+PlaceNo
    #HTTP_1 = HTTPLINE['scheme']+HTTPLINE['netloc']+HTTPLINE['path']+HTTPLINE['DATA']
    HTTP_2 = HTTPLINE['Authorization']+"&"+HTTPLINE['elementName']+"&"+HTTPLINE['format']+"&"+HTTPLINE['timeTo']#+"&"+HTTPLINE['limit']
    url = HTTP_1+HTTP_2
    #print(url)
        

    with request.urlopen(url) as respones :
        data = json.load(respones)
        PlaceName= data['records']['locations'][0]['location']
        try:    
            open('DD.json', 'w', encoding='utf-8') as file:
                json.dump(PlaceName1, file, ensure_ascii=False)  
            with open('DD.json', 'a', encoding='utf-8') as file:        
                for z in range(0,30):
                    PlaceName1 = PlaceName[z]#['locationName']     
                    #vv = {}
                    #vv[z] = PlaceName1
                    json.dump(PlaceName1, file, ensure_ascii=False)  
                    print(PlaceName1)    
                     
                            
        except:
            pass

                              
    
    #data1 = json.load(data.text)
    #with open('data.json', 'w', encoding='utf-8') as file:
    #    file.write(data1['records']) 

#print(data['records']['location'][0]['weatherElement'][0])
       
#with open('data.json', 'w', encoding='utf-8') as file:
#   file.write(PlaceName1) 
    
    
    #for ii in range(0,2):
    #    wa  = twlo['weatherElement'][ii]
    #wa1 = list(wa)
    #datas = str(twlo+wa1)
    
    #print(twlo)
    
        





   
   

#data['records']['location'][i]['locationName']







#一般天氣預報-今明36小時天氣預報  預設全台
#   F-C0032-001


