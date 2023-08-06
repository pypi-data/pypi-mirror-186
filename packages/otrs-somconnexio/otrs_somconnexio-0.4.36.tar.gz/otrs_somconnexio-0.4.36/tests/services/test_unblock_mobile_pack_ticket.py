import unittest

from mock import ANY, Mock, call, patch

from otrs_somconnexio.services.unblock_mobile_pack_ticket import \
    UnblockMobilePackTicket


class UnblockMobilePackTicketTestCase(unittest.TestCase):

    @patch(
        "otrs_somconnexio.services.update_ticket_DF.OTRSClient",
        return_value=Mock(
            spec=[
                "update_ticket",
                "get_ticket_by_number",
            ]
        ),
    )
    @patch("otrs_somconnexio.services.unblock_mobile_pack_ticket.DynamicField")
    def test_run(self, MockDF, MockOTRSClient):
        ticket_number = "123"
        expected_df = object()
        MockDF.return_value = expected_df
        MockOTRSClient.return_value.get_ticket_by_number.return_value = Mock(
            spec=["tid", "dynamic_field_get"]
        )
        MockOTRSClient.return_value.get_ticket_by_number.return_value.tid = 321
        MockOTRSClient.return_value.get_ticket_by_number.return_value.dynamic_field_get.return_value = Mock(
            spec="value"
        )
        MockOTRSClient.return_value.get_ticket_by_number.return_value.dynamic_field_get.return_value.value = (
            0
        )

        UnblockMobilePackTicket(ticket_number, "2022-11-11").run()

        MockOTRSClient.return_value.get_ticket_by_number.assert_called_once_with(
            ticket_number,
            dynamic_fields=True,
        )
        MockOTRSClient.return_value.update_ticket.assert_called_once_with(
            MockOTRSClient.return_value.get_ticket_by_number.return_value.tid,
            article=None,
            dynamic_fields=[expected_df]
        )
        MockDF.assert_called_once_with(
            name="recuperarProvisio",
            value=1,
        )

    @patch(
        "otrs_somconnexio.services.update_ticket_DF.OTRSClient",
        return_value=Mock(
            spec=[
                "update_ticket",
                "get_ticket_by_number",
            ]
        ),
    )
    @patch("otrs_somconnexio.services.unblock_mobile_pack_ticket.DynamicField")
    def test_SIMrebuda(self, MockDF, MockOTRSClient):
        ticket_number = "123"
        expected_df = object()
        MockDF.return_value = expected_df
        MockOTRSClient.return_value.get_ticket_by_number.return_value = Mock(
            spec=["tid", "dynamic_field_get"]
        )
        MockOTRSClient.return_value.get_ticket_by_number.return_value.tid = 321
        MockOTRSClient.return_value.get_ticket_by_number.return_value.dynamic_field_get.return_value = Mock(
            spec="value"
        )
        MockOTRSClient.return_value.get_ticket_by_number.return_value.dynamic_field_get.return_value.value = (
            1
        )

        UnblockMobilePackTicket(ticket_number, "2022-11-11").run()

        MockOTRSClient.return_value.get_ticket_by_number.assert_called_once_with(
            ticket_number,
            dynamic_fields=True,
        )

        MockOTRSClient.return_value.update_ticket.assert_called_once_with(
            MockOTRSClient.return_value.get_ticket_by_number.return_value.tid,
            article=None,
            dynamic_fields=[ANY, ANY],
        )
        MockDF.assert_has_calls(
            [
                call(
                    name="recuperarProvisio",
                    value=1,
                ),
                call(
                    name="dataIntroPlataforma",
                    value="2022-11-11",
                ),
            ],
            any_order=True,
        )
