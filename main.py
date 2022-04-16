from pyairtable import Table

from datetime import datetime

import Geohash
import traceback
import configparser
import requests, json

config = configparser.ConfigParser()
config.read('config.cfg')

# Airtable
at_table_name = config.get('AIRTABLE', 'TABLE_NAME')
at_base_id = config.get('AIRTABLE', 'BASE_ID')
at_api_key = config.get('AIRTABLE', 'API_KEY')

# Quicket
quicket_base_url = config.get('QUICKET', 'BASE_URL')
quicket_api_key = config.get('QUICKET', 'API_KEY')

# today = datetime.today().strftime('%Y-%m-%dT%H:%M:%S')
# Last Modified Date
today = "2022-01-01T00:00:00"

class airtableSync:
	def __init__(self, record_id, table_name = at_table_name):
		self.record_id   = record_id
		self.table_name  = table_name

	def at_instance(self):
		return Airtable(at_base_id, self.table_name, api_key=at_api_key)


class Quicket:
	def __init__(self, base_url = quicket_base_url, api_key = quicket_api_key):
		self.base_url = base_url
		self.api_key  = api_key

	def get_events(self, pageSize, lastModified = today):
		url = f"{self.base_url}?api_key={self.api_key}&pageSize=5&page=1&lastModified={lastModified}&categories=1"

		payload = {}
		headers = {}

		response = requests.request("GET", url, headers=headers, data=payload)

		return response.json()

	def upcoming_event_check():
		# Date to check in date format:
		check_date = datetime.datetime.strptime("2021-09-08", "%Y-%d-%m").date()

		# Current week number:
		curr_week = datetime.date.today().strftime("%V")
		# number of next week
		next_week = (datetime.date.today()+datetime.timedelta(weeks=1)).strftime("%V")
		# number of the week after that
		week_after_next_week = (datetime.date.today()+datetime.timedelta(weeks=2)).strftime("%V")


		# Compare week numbers of next weeks to the week number of the date to check:
		if next_week == check_date.strftime("%V"):
		    # Date is within next week, put code here
		    pass
		elif week_after_next_week == check_date.strftime("%V"):
		    # Date is the week after next week, put code here
		    pass


# Quicket
p1 = Quicket(quicket_base_url, quicket_api_key)

results = p1.get_events(10)

# Create Airtable Object
at_object = []
for result in results["results"]:
	name         = result['name']
	description  = result['description']
	url          = result['url']
	imageUrl     = result['imageUrl']
	startDate    = result['startDate']
	endDate      = result['endDate']
	title 		 = result['venue']['name']
	addressLine1 = result['venue']['addressLine1']
	addressLine2 = result['venue']['addressLine2']
	latitude	 = result['venue']['latitude']
	longitude	 = result['venue']['longitude']
	levelOne	 = result['locality']['levelOne']
	levelTwo	 = result['locality']['levelTwo']
	levelThree	 = result['locality']['levelThree']

	geohash  = Geohash.encode(latitude, longitude)
	location = f"{addressLine1}, {addressLine2}, {levelThree}, {levelTwo}, {levelTwo}"

	files = []
	tags  = []
	at_data = {
		"Title": name,
		"Description": description,
		"files": files.append({f"https:{imageUrl}"}),
		"startDate": startDate,
		"endDate": endDate,
		"GeoHash": geohash,
		"Status": "Pending",
		"Type": "event",
		"Tags": tags.append("live"),
		"startDate": startDate,
		"endDate": endDate,
		"Bio": "bio",
		"Latitude": latitude,
		"Longitude": longitude,
		"HatchTips": "",
		"Location": location,
		"OperatingHours": "OperatingHours",
		"WidgetURL": url,
		"cell": "cell",
		"email": "",
		"hidden": True,
		"deleted": False,
		"geopoint": ""
	}

	# print(f"at_data: {json.dumps(at_data)}")

	at_object.append(at_data)

	# AT test

	# results = table.all()

	# print(results)

table = Table(at_api_key, at_base_id, at_table_name)
# table.create({"First Name': 'John'})
table.batch_create(at_object)

# print(count)

# Filter by date: check for events in the next week


# Filter by location


# Customize


# Build custom object


# Post to Airtable


# print(f"Events: {results}")

# print(f"{today}")
# 2021-06-11T11:05:00
# 2022-04-13T13:34:08
# 2022-01-01T00:00:00

# Categories
# Travel & Outdoor = 6
# Sports & Fitness = 5
# Music = 1

# {
#   "results": [
#     {
#       "id": 170781,
#       "name": "Hymns of the Passion",
#       "description": "<p><strong>A musical retelling of Hallgrímur Pétursson's Passíusálmar&nbsp;</strong></p><p><br></p><p>Throughout the centuries some of the richest expressions of religious sentiment has been contained within great art. Hallgrímur Pétursson’s Passíusálmar (Passion Hymns), a collection of some 50 poems and meditations tracing the journey of Christ from the garden to the cross, stands in this great tradition. Although, often unknown outside of his native country, Pétursson’s literary contributions have played an important role in the formation of Icelandic identity.</p><p><br></p><p>Join us for an evening of poetry in song as we enter into the narrative of Christ's journey from the garden to the cross. Hope City presents this unique retelling of a selection of these poems in a style that could be best described as \"contemplative folk\". Elements of subtle harmony, light percussion, and spoken word wrap around the raw guitars and emotive melodies, allowing the listener greater reflection upon the depth and beauty of the original poetry.</p>",
#       "url": "https://www.quicket.co.za/events/170781-hymns-of-the-passion/",
#       "imageUrl": "//images.quicket.co.za/0366543_360_360.Png",
#       "dateCreated": "2022-03-19T14:41:59.683",
#       "lastModified": "2022-04-13T12:37:06.7409627",
#       "startDate": "2022-04-13T19:50:00",
#       "endDate": "2022-04-13T21:00:00",
#       "venue": {
#         "id": 0,
#         "name": "Cape Town Union Church",
#         "addressLine1": "Kloof Street",
#         "addressLine2": "Tamboerskloof",
#         "latitude": -33.931095,
#         "longitude": 18.4092339
#       },
#       "locality": {
#         "levelOne": "South Africa",
#         "levelTwo": "Western Cape",
#         "levelThree": "Cape Town"
#       },
#       "organiser": {
#         "id": 0,
#         "name": " Hope City ",
#         "phone": "",
#         "mobile": "",
#         "facebookUrl": "https://www.facebook.com/events/762674287275262/",
#         "twitterHandle": "",
#         "hashTag": "",
#         "organiserPageUrl": "https://www.quicket.co.za/organisers/8276-hope-city"
#       },
#       "categories": [
#         {
#           "id": 1,
#           "name": "Music"
#         },
#         {
#           "id": 1,
#           "name": "Music"
#         }
#       ],
#       "tickets": [
#         {
#           "id": 334664,
#           "name": "General Seating",
#           "soldOut": false,
#           "provisionallySoldOut": false,
#           "price": 0,
#           "salesStart": "2022-03-19T14:42:00",
#           "salesEnd": "2022-04-13T21:00:00",
#           "description": "",
#           "donation": false,
#           "vendorTicket": false
#         }
#       ],
#       "schedules": [],
#       "refundFeePayableBy": 0
#     }
#   ],
#   "pageSize": 1,
#   "pages": 5,
#   "records": 5,
#   "extras": null,
#   "message": null,
#   "statusCode": 0
# }


#	{'Title': 'Rocking the Daisies Johannesburg', 'Description': '', 'files': ['//images.quicket.co.za/0311822_360_360.jpeg'], 'startDate': '2022-10-08T12:00:00', 'endDate': '2022-10-09T22:00:00', 'GeoHash': 'ke7fywck1zkg', 'Status': 'Pending', 'Type': 'event', 'Tags': 'live', 'Bio': 'bio', 'Latitude': -26.1975466, 'Longitude': 28.0608802, 'HatchTips': '', 'Location': 'South Park Lane , , Johannesburg, Gauteng, Gauteng', 'OperatingHours': 'OperatingHours', 'WidgetURL': 'https://www.quicket.co.za/events/98739-rocking-the-daisies-johannesburg/', 'cell': 'cell', 'email': '', 'hidden': True, 'deleted': False, 'geopoint': ''}
