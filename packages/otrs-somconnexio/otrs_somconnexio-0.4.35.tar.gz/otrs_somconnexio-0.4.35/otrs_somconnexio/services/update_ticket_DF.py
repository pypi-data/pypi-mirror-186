# coding: utf-8
from otrs_somconnexio.client import OTRSClient


class UpdateTicketDF:
    """
    Abstract service class to update a given OTRS ticket DF's.

    Class method '_prepare_dynamic_fields' needs to be implemented in child classes
    """

    def __init__(self, ticket_number):
        self.ticket_number = ticket_number

    def run(self):
        otrs_client = OTRSClient()
        ticket = otrs_client.get_ticket_by_number(
            self.ticket_number, dynamic_fields=True
        )
        otrs_client.update_ticket(
            ticket.tid,
            article=None,
            dynamic_fields=self._prepare_dynamic_fields(ticket),
        )
