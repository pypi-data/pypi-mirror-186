# coding: utf-8
from pyotrs.lib import DynamicField

from otrs_somconnexio.client import OTRSClient


class SearchTicketsService:
    """
    Search by queue, partner, states and DF OTRS tickets.
    """

    def __init__(self, configuration_class):
        """
        configuration_class: Any ticket configuration class from 'otrs-models/configurations'
        folder in this package
        """
        self.configuration = configuration_class

    def search(self, customer_code, state_list=["new"], df_dct={}):
        """
        df_dct (dict): key, value as list of DF with which we must search
        If value is a list of values, the method will return any match
        """

        state_list = [state for state in state_list]

        otrs_client = OTRSClient()

        process_id_df = DynamicField("ProcessManagementProcessID",
                                     self.configuration.process_id)
        activity_id_df = DynamicField("ProcessManagementActivityID",
                                      self.configuration.activity_id)
        df_list = [process_id_df, activity_id_df]

        for key, value in df_dct.items():
            df_list.append(DynamicField(key, search_patterns=list(value)))

        search_args = {
            "dynamic_fields": df_list,
            "Queues": [self.configuration.queue],
            "CustomerID": customer_code,
            "States": state_list,
        }

        return otrs_client.search_tickets(**search_args)
