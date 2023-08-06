# coding: utf-8
from pyotrs.lib import DynamicField

from .update_ticket_DF import UpdateTicketDF


class UnblockMobilePackTicket(UpdateTicketDF):
    """
    Unblock the mobile pack tickets.

    Once the fiber provisioning is closed, we can start with the mobile provisioning to complete
    the pack products.
    Unblock is to change the DynamicField_recuperarProvisio to 1
    """

    def __init__(self, ticket_number, introduced_date):
        self.introduced_date = introduced_date
        super().__init__(ticket_number)

    def _prepare_dynamic_fields(self, ticket):
        dynamic_fields = [
            DynamicField(name='recuperarProvisio', value=1),
        ]
        if bool(ticket.dynamic_field_get("SIMrebuda").value):
            dynamic_fields.append(
                DynamicField(name="dataIntroPlataforma", value=self.introduced_date),
            )
        return dynamic_fields
