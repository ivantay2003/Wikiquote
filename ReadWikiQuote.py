from api_manager import api_manager
from json_manager import JSONData
from html_manager import HTMLManager
import html_manager
import sys

if len(sys.argv) > 1 :

    name = sys.argv[1]
    name = name.title()
    print ("Checking name :" + name)
    apimanager = api_manager()
    r = apimanager.request_via_api(apimanager.url, page = name , section = 1 , action ="parse" , format="json" , disabletoc = 1 , disablelimitreport = 1, origin = "*"  )

    jsonData = JSONData()
    jData = jsonData.parse_data(r)

    xmlData = jData['parse']['text']['*']
    #print ("Data " + jData['parse']['text']['*'])


    web_page_manager = HTMLManager(xmlData, None)
    html_lists = web_page_manager.find_all_lists()

    quotes = []


    for html_list in html_lists:
        web_page_manager.remove_sublists(html_list)
        quotes.extend(html_manager.extract_text_from_list(html_list))

    print (quotes[0])
    print ("Author :" + name)
#answer = list(map(language_manager.transform_to_unicode, quotes))




