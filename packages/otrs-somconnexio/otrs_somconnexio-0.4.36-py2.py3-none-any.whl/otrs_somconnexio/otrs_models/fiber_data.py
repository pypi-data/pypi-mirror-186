from otrs_somconnexio.otrs_models.internet_data import InternetData


class FiberData(InternetData):
    service_type = 'fiber'

    def __init__(self, **args):
        self.previous_contract_pon = args.get("previous_contract_pon", "")
        self.previous_contract_fiber_speed = args.get("previous_contract_fiber_speed", "")
        self.activation_notes = args.get("activation_notes", "")
        self.all_grouped_SIMS_recieved = args.get("all_grouped_SIMS_recieved")
        self.has_grouped_mobile_with_previous_owner = args.get("has_grouped_mobile_with_previous_owner")
        for key in ["previous_contract_pon", "previous_contract_fiber_speed",
                    "activation_notes", "all_grouped_SIMS_recieved",
                    "has_grouped_mobile_with_previous_owner"]:
            args.pop(key, None)
        super().__init__(**args)
