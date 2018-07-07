import json

class JSONData :

    def parse_data (self, r):
        j = None

        try:
            j = json.loads(r)


        except ValueError:

            print ("JSON error ")

        return j