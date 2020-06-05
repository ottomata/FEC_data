from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'qu9IQSkYHgSWbh0mPcIm445eWeQjTKeufNK79r9B'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DisbursementsApi(swagger_client.ApiClient(configuration))
api_key = 'qu9IQSkYHgSWbh0mPcIm445eWeQjTKeufNK79r9B' # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)
min_date = '2017-01-01' # date | Minimum date (optional)
committee_id = ['C00580100'] # list[str] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits.  (optional)
sort = '-disbursement_date' # str | Provide a field to sort by. Use - for descending order. (optional) (default to -disbursement_date)
two_year_transaction_period = [2018, 2020] # list[int] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  (optional)

try:
    api_response = api_instance.schedules_schedule_b_get(api_key, min_date=min_date, committee_id=committee_id, sort=sort, two_year_transaction_period=two_year_transaction_period)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DisbursementsApi->schedules_schedule_b_get: %s\n" % e)
