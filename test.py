import requests
import json
#response = requests.get("https://api.open.fec.gov/v1/committee/C00580100/totals/?api_key=qu9IQSkYHgSWbh0mPcIm445eWeQjTKeufNK79r9B&cycle=2018&cycle=2020")
#response = requests.get("https://api.open.fec.gov/v1/schedules/schedule_b/?api_key=qu9IQSkYHgSWbh0mPcIm445eWeQjTKeufNK79r9B&committee_id=C00580100&disbursement_description=legal%20consulting&sort=disbursement_date&recipient_name=jones%20day")
response = requests.get("https://api.open.fec.gov/v1/schedules/schedule_b/?recipient_name=JONES%20DAY&min_date=2017-01-01&committee_id=C00580100&api_key=qu9IQSkYHgSWbh0mPcIm445eWeQjTKeufNK79r9B&disbursement_description=legal%20consulting&sort=-disbursement_date&two_year_transaction_period=2020&two_year_transaction_period=2018&per_page=59")
json_response = response.json()
#dictionary = json.dumps(response.json(), sort_keys = True, indent = 4)
results = json_response['results']
disbursement_total = 0.0
for result in results:
    disbursement_total += result['disbursement_amount']
print(disbursement_total)
