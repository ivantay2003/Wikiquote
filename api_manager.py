import requests
import urllib.request
import urllib.parse
import requests

class api_manager () :

    #url = "https://random-quote-generator.herokuapp.com/api/quotes/random";

    url = "http://en.wikiquote.org/w/api.php"



    def readURL (self):
        r= urllib.request.urlopen(self.url).read().decode('utf-8')

        return r


    def request_via_api (self, base_url=url, disablelimitreport = None, disabletoc = None , action = None, page = None, format = None, section = None, origin = None, redirects = None):
        def set_value(dictionary, key, value):
            if value:
                dictionary[key] = value

        parameters = {}


        set_value(parameters , 'format' , format)
        set_value(parameters, 'page', page)
        set_value(parameters, 'section', section)
        set_value(parameters, 'action', action)
        set_value(parameters, 'disabletoc', disabletoc)
        set_value(parameters, 'disablelimitreport', disablelimitreport)
        set_value(parameters, 'origin', origin)

        #print (parameters)
        query_string = urllib.parse.urlencode(parameters)
        url = self.url + "?" + query_string
        with urllib.request.urlopen(url) as response:
            request = response.read()
            #print(request)

        return request



