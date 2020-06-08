from __future__ import print_function
import time
from pprint import pprint
import json

from collections import OrderedDict
from dotted.collection import DottedDict

# Rename swagger_client to something that makes sense:  fec_client
# Ideally the fec_python swagger client code would call itself this,
# but I couldn't get the codegen API to do the right thing.
import swagger_client as fec_client
from swagger_client.rest import ApiException

import config

api_key = config.api_key # str |  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  (default to DEMO_KEY)

# Configure API key authorization: apiKey
configuration = fec_client.Configuration()
configuration.api_key['api_key'] = api_key
# Set host to use the FEC HTTP API
configuration.host = 'https://api.open.fec.gov/v1'

# create an instance of the DisbursementsApi API class
disbursements_api = fec_client.DisbursementsApi(fec_client.ApiClient(configuration))



# This is an ordered mapping of 'dotted' AKA nested key
# names in a schedule_b result object record.
# It explicitly maps the nested API results key to
# the name of the column header we'll use for the google sheets api.
# The column name values are only used when constructing the first
# row to send to google sheets, as it will be used as the column header.
dotted_result_keys_to_column_names = OrderedDict({
    'committee_id': 'committee_id',
    'file_number': 'file_number',
    'line_number_label': 'line_number_label',
    'committee.city': 'committee_city',
    'committee.committee_type_full': 'committee_type_full',
    'committee.name': 'committee_name'
})


def get_schedule_b_results(
    committee_id=['C00618389', 'C00637512'],
    sort='-disbursement_date',
    two_year_transaction_period=[2018, 2020]
):
    """
    Gets the first page of schedule b results for the given parameters.
    The returned value will be the list of result object records.
    """
    try:
        api_response = disbursements_api.schedules_schedule_b_get(
            api_key,
            committee_id=committee_id,
            sort=sort,
            two_year_transaction_period=two_year_transaction_period
        )
        return api_response.to_dict()['results']
    except ApiException as e:
        print("Exception when calling DisbursementsApi->schedules_schedule_b_get: %s\n" % e)




def schedule_b_results_to_rows(results):
    """
    Converts schedule_b result object records into a list of google sheet rows.
    """

    # Create an empty list of rows.  Each element in this list is a row.
    rows = []

    # Iterate over each result object in the list of results.
    for result in results:
        # Convert the result to a DottedDict so we can use nested dotted keys
        # instead of having to look deeper into the nested structure.
        # This lets us do e.g.
        # result['committee.name'] instead of result['committee']['name']
        result = DottedDict(result)

        # Create an empty row.  Each element in this will be a cell value in google sheets.
        row = []
        # Iterate over each of our result keys in order.
        for result_key in dotted_result_keys_to_column_names.keys():
            # Use the dotted key to lookup the value we want and append it to the row.
            row.append(result[result_key])

        # Store the row we just created in our larger list of rows.
        rows.append(row)

    # Return all of the rows with the column name headers prepended as the first row.
    column_header_row = list(dotted_result_keys_to_column_names.values())
    return column_header_row + rows


results = get_schedule_b_results()
google_sheets_values = schedule_b_results_to_rows(results)

pprint(google_sheets_values)