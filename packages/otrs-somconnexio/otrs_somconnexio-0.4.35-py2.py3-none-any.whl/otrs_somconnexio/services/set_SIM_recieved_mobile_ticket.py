# coding: utf-8
from pyotrs.lib import DynamicField

from .update_ticket_DF import UpdateTicketDF


class SetSIMRecievedMobileTicket(UpdateTicketDF):
    """
    Set DF SImRebuda to True to OTRS mobile tickets.
    """

    def _prepare_dynamic_fields(self, ticket):
        return [DynamicField(name='SIMrebuda', value=1)]
