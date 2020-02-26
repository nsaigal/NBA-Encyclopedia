import requests
import json
import csv
from datetime import datetime

scheme = 'http://'
hostname = '127.0.0.1'
port = 8000
api = 'api/players/'

REQUEST_URL = scheme + hostname + ':' + str(port) + '/' + api

class IngestFromCSV():

    def parse_csv(self):
        with open('player_data.csv', 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            for index, value in enumerate(csv_reader):
                if index > 0 and index < 100:
                    first_name = value[0].split(' ')[0]
                    last_name = value[0].split(' ')[1]
                    start_year = value[1]
                    end_year = value[2]
                    position = value[3]
                    height = self.transform_height(value[4])
                    weight = int(value[5])
                    birthday = self.transform_date(value[6])
                    college = ''
                    if len(value) > 7:
                        college = value[7]
                    
                    self.post_player(first_name, last_name, start_year, end_year, height, weight, birthday, college, position)
            

    def post_player(self, first, last, start_year, end_year, height, weight, birthday, college='', position='G'):


        payload = {
            'first_name': first,
            'last_name': last,
            'start_year': start_year,
            'end_year': end_year,
            'birthday': birthday,
            'college': college,
            'position': position,
            'weight': weight,
            'height': height,
        }

        response = requests.post(REQUEST_URL, data=payload)
        print(json.dumps(response.json()))

    def transform_date(self, date_string):
        if date_string != '':
            d = datetime.strptime(date_string, '%B %d, %Y')
            return(d.strftime('%Y-%m-%d'))
        return ''
    
    def transform_height(self, height_string):
        if height_string != '':
            split = height_string.split('-')
            foot = int(split[0])
            inches = int(split[1])
            return (foot*12) + inches

ingestObject = IngestFromCSV()
ingestObject.parse_csv()