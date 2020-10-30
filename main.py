from airtable import Airtable
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.campaign import Campaign

from datetime import datetime

import traceback
import configparser
import requests

config = configparser.ConfigParser()
config.read('config.cfg')

# Airtable Variables
at_table_name = config.get('AIRTABLE', 'TABLE_NAME')
at_base_id = config.get('AIRTABLE', 'BASE_ID')
at_api_key = config.get('AIRTABLE', 'API_KEY')

# Facebook Variables
fb_app_id = config.get('FACEBOOK', 'APP_ID')
fb_secret = config.get('FACEBOOK', 'APP_SECRET')
fb_token = config.get('FACEBOOK', 'ACCESS_TOKEN')

print(fb_app_id,
fb_secret,
fb_token)

class airtableSync:
	def __init__(self, record_id, table_name = at_table_name):
		self.record_id   = record_id
		self.table_name  = table_name

	def at_instance(self):
		return Airtable(at_base_id, self.table_name, api_key=at_api_key)

	def fb_instance(self):
		return FacebookAdsApi.init(fb_app_id, fb_secret, fb_token)

	def get_adset_id(self):
		return self.at_instance().get(self.record_id)['fields']['FB Adset ID']

	def get_campaign_insights(self):
		fb_instance = self.fb_instance()

		print(fb_instance.__dict__)

		adset_id = self.get_adset_id()

		fields = [
			'cost_per_conversion'
		]

		params = {
		  'fields': fields,
		  'access_token': fb_token
		}

		response = requests.get(f'https://graph.facebook.com/v8.0/23845695225790479/insights', params=params)
		print(response.__dict__)

		return response


# set test variables
record_id  = "recDE4SwTI2fI9Lqh"

p1 = airtableSync(record_id, at_table_name)

campaign_id = p1.get_adset_id()
campaign_insights = p1.get_campaign_insights()

print(f"Adset ID: {campaign_id}")
print(f"Campaign Insights: {campaign_insights}")

