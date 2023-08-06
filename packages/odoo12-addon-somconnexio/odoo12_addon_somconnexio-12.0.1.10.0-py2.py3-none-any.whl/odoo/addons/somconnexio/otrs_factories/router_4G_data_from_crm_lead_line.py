from otrs_somconnexio.otrs_models.router_4G_data import Router4GData


class Router4GDataFromCRMLeadLine:

    def __init__(self, crm_lead_line):
        self.crm_lead_line = crm_lead_line

    def build(self):
        isp_info = self.crm_lead_line.broadband_isp_info

        previous_internal_provider_ref = ""
        if isp_info.service_supplier_id:
            previous_internal_provider_ref = isp_info.service_supplier_id.ref

        return Router4GData(
            order_id=self.crm_lead_line.id,
            phone_number=isp_info.previous_phone_number or isp_info.phone_number,
            service_address=isp_info.service_full_street,
            service_city=isp_info.service_city,
            service_zip=isp_info.service_zip_code,
            service_subdivision=isp_info.service_state_id.name,
            service_subdivision_code="{}-{}".format(
                isp_info.service_country_id.code,
                isp_info.service_state_id.code
            ),
            shipment_address=isp_info.delivery_full_street,
            shipment_city=isp_info.delivery_city,
            shipment_zip=isp_info.delivery_zip_code,
            shipment_subdivision=isp_info.delivery_state_id.name,
            previous_provider=isp_info.previous_provider.code or 'None',
            previous_owner_vat=isp_info.previous_owner_vat_number or '',
            previous_owner_name=isp_info.previous_owner_first_name or '',
            previous_owner_surname=isp_info.previous_owner_name or '',
            previous_service=self._previous_service(),
            previous_internal_provider=previous_internal_provider_ref,
            previous_contract_phone=isp_info.previous_contract_phone,
            previous_contract_address=isp_info.previous_contract_address,
            notes=self.crm_lead_line.lead_id.description,
            iban=self.crm_lead_line.lead_id.iban,
            email=self.crm_lead_line.lead_id.email_from,
            product=self.crm_lead_line.product_id.default_code,
            adsl_coverage=isp_info.adsl_coverage,
            mm_fiber_coverage=isp_info.mm_fiber_coverage,
            vdf_fiber_coverage=isp_info.vdf_fiber_coverage,
            orange_fiber_coverage=isp_info.orange_fiber_coverage,
            type=isp_info.type,
        )

    def _previous_service(self):
        previous_service = self.crm_lead_line.broadband_isp_info.previous_service
        if not previous_service:
            return "None"

        OTRS_PREVIOUS_SERVICE_MAPPING = {
            "adsl": "ADSL",
            "fiber": "Fibra",
            "4G": "4G",
        }
        return OTRS_PREVIOUS_SERVICE_MAPPING.get(previous_service, "Other")
