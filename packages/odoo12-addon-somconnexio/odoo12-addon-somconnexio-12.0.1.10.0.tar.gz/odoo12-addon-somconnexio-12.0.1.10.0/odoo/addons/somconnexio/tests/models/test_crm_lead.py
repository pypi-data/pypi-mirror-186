from ..sc_test_case import SCTestCase
from odoo.exceptions import ValidationError
from ..helpers import crm_lead_create

from datetime import timedelta


class CRMLeadTest(SCTestCase):
    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)

        self.partner_id = self.browse_ref('somconnexio.res_partner_2_demo')
        self.crm_lead_iban = 'ES6000491500051234567891'
        self.crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
            }]
        )

    def test_crm_lead_action_set_won(self):
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'stage_id': self.browse_ref('crm.stage_lead3').id,
            }]
        )
        crm_lead.action_set_won()
        self.assertEquals(crm_lead.stage_id, self.browse_ref('crm.stage_lead4'))

    def test_crm_lead_activation_notes_fiber(self):
        '''
        Test that only non-cancelled mobile portability lines from same
        partner, created 2 days before or after the target lead creation date,
        are taken into account for the activation notes
        '''

        other_partner_id = self.browse_ref('somconnexio.res_partner_1_demo')
        self.env['res.partner.bank'].create({
            'acc_type': 'iban',
            'acc_number': 'ES6000491500051234567893',
            'partner_id': other_partner_id.id
        })

        target_crm_lead = crm_lead_create(self.env, self.partner_id, "fiber",
                                          portability=True)
        mbl_1_crm_lead = crm_lead_create(self.env, self.partner_id, "mobile",
                                         portability=True)
        mbl_2_crm_lead = crm_lead_create(self.env, self.partner_id, "mobile",
                                         portability=True)
        mbl_3_crm_lead = crm_lead_create(self.env, self.partner_id, "mobile",
                                         portability=True)
        mbl_4_crm_lead = crm_lead_create(self.env, self.partner_id, "mobile",
                                         portability=True)
        mbl_5_crm_lead = crm_lead_create(self.env, self.partner_id, "mobile",
                                         portability=True)
        mbl_6_crm_lead = crm_lead_create(self.env, self.partner_id, "mobile")
        mbl_7_crm_lead = crm_lead_create(self.env, other_partner_id, "mobile",
                                         portability=True)
        adsl_crm_lead = crm_lead_create(self.env, self.partner_id, "adsl",
                                        portability=True)
        router_4G_crm_lead = crm_lead_create(self.env, self.partner_id, "4G",
                                             portability=True)

        target_crm_lead.action_set_remesa()

        mbl_3_crm_lead.action_set_cancelled()

        # Only leads within +- 2 days from target_crm_lead date open
        mbl_1_crm_lead.date_open = target_crm_lead.date_open \
            + timedelta(days=1, hours=20)  # Within time
        mbl_2_crm_lead.date_open = target_crm_lead.date_open \
            - timedelta(days=0, hours=8)  # Within time
        mbl_4_crm_lead.date_open = target_crm_lead.date_open \
            + timedelta(days=3, hours=8)  # Off time
        mbl_5_crm_lead.date_open = target_crm_lead.date_open \
            - timedelta(days=323)  # Off time

        self.assertFalse(target_crm_lead.lead_line_ids.activation_notes)

        target_crm_lead.action_set_won()

        self.assertIn(
            mbl_1_crm_lead.lead_line_ids.mobile_isp_info_phone_number,
            target_crm_lead.lead_line_ids.activation_notes
        )
        self.assertIn(
            mbl_2_crm_lead.lead_line_ids.mobile_isp_info_phone_number,
            target_crm_lead.lead_line_ids.activation_notes
        )
        # Cancelled
        self.assertNotIn(
            mbl_3_crm_lead.lead_line_ids.mobile_isp_info_phone_number,
            target_crm_lead.lead_line_ids.activation_notes
        )
        # Created after 2 days
        self.assertNotIn(
            mbl_4_crm_lead.lead_line_ids.mobile_isp_info_phone_number,
            target_crm_lead.lead_line_ids.activation_notes
        )
        # Created before 2 days
        self.assertNotIn(
            mbl_5_crm_lead.lead_line_ids.mobile_isp_info_phone_number,
            target_crm_lead.lead_line_ids.activation_notes
        )
        # Non portability
        self.assertNotIn(
            mbl_6_crm_lead.lead_line_ids.mobile_isp_info_phone_number,
            target_crm_lead.lead_line_ids.activation_notes
        )
        # From other partner
        self.assertNotIn(
            mbl_7_crm_lead.lead_line_ids.mobile_isp_info_phone_number,
            target_crm_lead.lead_line_ids.activation_notes
        )
        # ADSL
        self.assertNotIn(
            adsl_crm_lead.lead_line_ids.broadband_isp_info_phone_number,
            target_crm_lead.lead_line_ids.activation_notes
        )
        # 4G
        self.assertNotIn(
            router_4G_crm_lead.lead_line_ids.broadband_isp_info_phone_number,
            target_crm_lead.lead_line_ids.activation_notes
        )

    def test_crm_lead_activation_notes_mbl(self):
        target_crm_lead = crm_lead_create(self.env, self.partner_id, "mobile",
                                          portability=True)
        crm_lead_create(self.env, self.partner_id, "fiber")
        fiber_crm_lead = crm_lead_create(self.env, self.partner_id, "fiber",
                                         portability=True)

        target_crm_lead.action_set_remesa()

        self.assertFalse(target_crm_lead.lead_line_ids.activation_notes)

        expected_notes = "Altres línies en provisió: {}".format(
            fiber_crm_lead.lead_line_ids.broadband_isp_info_phone_number)

        target_crm_lead.action_set_won()
        self.assertEquals(
            target_crm_lead.lead_line_ids.activation_notes, expected_notes)

    def test_crm_lead_action_set_won_raise_error_if_not_in_remesa_stage(self):
        self.assertNotEqual(self.crm_lead.stage_id, self.browse_ref('crm.stage_lead3'))
        self.assertRaisesRegex(
            ValidationError,
            "The crm lead must be in remesa stage.",
            self.crm_lead.action_set_won
        )

    def test_crm_lead_action_set_remesa_raise_error_if_not_in_new_stage(self):
        self.crm_lead.write(
            {
                'iban': 'ES91 2100 0418 4502 0005 1332',
                'stage_id': self.browse_ref('crm.stage_lead4').id,
            })
        self.assertNotEqual(self.crm_lead.stage_id, self.browse_ref('crm.stage_lead1'))
        self.assertRaisesRegex(
            ValidationError,
            "The crm lead must be in new stage.",
            self.crm_lead.action_set_remesa
        )

    def test_crm_lead_action_validation_error_crm_lead_with_multiple_lines(self):
        mobile_isp_info = self.env['mobile.isp.info'].create({
            'type': 'new',
        })
        mobile_crm_lead_line_1 = self.env['crm.lead.line'].create({
            'name': 'lead line 1',
            'partner': self.partner_id.id,
            'product_id': self.ref('somconnexio.SenseMinuts500MB'),
            'mobile_isp_info': mobile_isp_info.id,
        })
        mobile_crm_lead_line_2 = self.env['crm.lead.line'].create({
            'name': 'lead line 2',
            'partner': self.browse_ref('somconnexio.res_partner_1_demo').id,
            'product_id': self.ref('somconnexio.SenseMinuts500MB'),
            'mobile_isp_info': mobile_isp_info.id,
        })

        self.crm_lead.write({
            'lead_line_ids': [(6, False, [mobile_crm_lead_line_1.id,
                                          mobile_crm_lead_line_2.id])]
        })
        self.assertNotEqual(self.crm_lead.stage_id, self.browse_ref('crm.stage_lead4'))

        self.assertRaises(
            ValidationError,
            self.crm_lead.action_set_won
        )

    def test_crm_lead_action_set_cancelled(self):
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'stage_id': self.browse_ref('somconnexio.stage_lead5').id,
            }]
        )
        crm_lead.action_set_cancelled()
        self.assertEquals(crm_lead.stage_id, self.browse_ref('somconnexio.stage_lead5'))

    def test_ensure_crm_lead_iban_in_partner(self):
        self.crm_lead.write(
            {
                'iban': self.crm_lead_iban,
                'stage_id': self.browse_ref('crm.stage_lead3').id,
            })

        self.assertEquals(len(self.partner_id.bank_ids), 1)
        self.assertNotEqual(self.crm_lead_iban,
                            self.partner_id.bank_ids[0].sanitized_acc_number)

        self.crm_lead.action_set_won()

        self.assertEquals(len(self.partner_id.bank_ids), 2)
        self.assertEquals(self.crm_lead_iban,
                          self.partner_id.bank_ids[1].sanitized_acc_number)

    def test_crm_lead_partner_email(self):
        self.assertEquals(self.crm_lead.email_from, self.partner_id.email)

    def test_crm_lead_subscription_request_email(self):
        subscription_request_id = self.browse_ref(
            'somconnexio.sc_subscription_request_2_demo')

        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'New Test Lead',
                'subscription_request_id': subscription_request_id.id,
            }]
        )
        self.assertEquals(crm_lead.email_from, subscription_request_id.email)

    def test_crm_lead_new_email(self):
        new_email = "new.email@demo.net"
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'New Test Lead',
                'partner_id': self.partner_id.id,
                'email_from': new_email,
            }]
        )
        self.assertEquals(crm_lead.email_from, new_email)

    def test_crm_lead_action_set_remesa(self):
        mobile_isp_info = self.env['mobile.isp.info'].create({
            'type': 'new',
        })
        product_mobile = self.env.ref(
            "somconnexio.100MinSenseDades_product_template"
        ).product_variant_id
        lead_line_vals = {
            'name': '666666666',
            'product_id': product_mobile.id,
            'mobile_isp_info': mobile_isp_info.id,
        }
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )
        crm_lead.action_set_remesa()
        self.assertEquals(crm_lead.stage_id, self.browse_ref('crm.stage_lead3'))

    def test_crm_lead_action_set_remesa_raise_error_without_partner(self):
        mobile_isp_info = self.env['mobile.isp.info'].create({
            'type': 'new',
        })
        product_mobile = self.env.ref(
            "somconnexio.100MinSenseDades_product_template"
        ).product_variant_id
        lead_line_vals = {
            'name': '666666666',
            'product_id': product_mobile.id,
            'mobile_isp_info': mobile_isp_info.id,
        }
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': None,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )
        self.assertRaisesRegex(
            ValidationError,
            "Error in {}: The subscription request related must be validated.".format(crm_lead.lead_line_id),  # noqa
            crm_lead.action_set_remesa
        )

    def test_crm_lead_action_set_remesa_raise_error_with_invalid_bank(self):
        mobile_isp_info = self.env['mobile.isp.info'].create({
            'type': 'new',
        })
        product_mobile = self.env.ref(
            "somconnexio.100MinSenseDades_product_template"
        ).product_variant_id
        lead_line_vals = {
            'name': '666666666',
            'product_id': product_mobile.id,
            'mobile_isp_info': mobile_isp_info.id,
        }
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': 'ES6099991500051234567891',
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )
        self.assertRaisesRegex(
            ValidationError,
            "Error in {}: Invalid bank.".format(crm_lead.lead_line_id),
            crm_lead.action_set_remesa
        )

    def test_crm_lead_action_set_remesa_raise_error_with_existent_phone_number(self):
        product_mobile = self.env.ref(
            "somconnexio.100MinSenseDades_product_template"
        ).product_variant_id
        previous_provider = self.ref("somconnexio.previousprovider1")
        mobile_isp_info = self.env['mobile.isp.info'].create({
            'type': 'portability',
            'phone_number': '663322234',
            'previous_contract_type': 'contract',
            'previous_provider': previous_provider,
        })
        lead_line_vals = {
            'name': '663322234',
            'product_id': product_mobile.id,
            'mobile_isp_info': mobile_isp_info.id,
        }
        self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
                'stage_id': self.env.ref("crm.stage_lead4").id,
            }]
        )
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )
        self.assertRaisesRegex(
            ValidationError,
            "Error in {}: Contract or validated CRMLead with the same phone already exists.".format(crm_lead.lead_line_id),  # noqa
            crm_lead.action_set_remesa
        )

    def test_crm_lead_action_set_remesa_location_change_existent_phone_number(self):
        crm_lead = crm_lead_create(self.env, self.partner_id, "mobile")

        copied_mobile_isp_info = crm_lead.lead_line_ids.mobile_isp_info.copy()
        copied_mobile_isp_info.type = "location_change"

        lead_line_vals = {
            'name': 'copied crm lead line',
            'product_id': crm_lead.lead_line_ids.product_id.id,
            'mobile_isp_info': copied_mobile_isp_info.id
        }

        copied_crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )
        copied_crm_lead.action_set_remesa()

        self.assertTrue(copied_crm_lead.skip_duplicated_phone_validation)

    def test_crm_lead_action_set_remesa_raise_error_with_duplicate_phone_number_in_new_line(self):  # noqa
        product_mobile = self.env.ref(
            "somconnexio.100MinSenseDades_product_template"
        ).product_variant_id
        previous_provider = self.ref("somconnexio.previousprovider1")
        mobile_isp_info = self.env['mobile.isp.info'].create({
            'type': 'portability',
            'phone_number': '663322234',
            'previous_contract_type': 'contract',
            'previous_provider': previous_provider,
        })
        lead_line_vals = {
            'name': '663322234',
            'product_id': product_mobile.id,
            'mobile_isp_info': mobile_isp_info.id,
        }
        crm_leads = self.env['crm.lead'].create(
            [
                {
                    'name': 'Test Lead',
                    'partner_id': self.partner_id.id,
                    'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                    'lead_line_ids': [(0, 0, lead_line_vals)],
                    'stage_id': self.env.ref("crm.stage_lead1").id,
                },
                {
                    'name': 'Test Lead',
                    'partner_id': self.partner_id.id,
                    'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                    'lead_line_ids': [(0, 0, lead_line_vals)],
                    'stage_id': self.env.ref("crm.stage_lead1").id,
                }
            ]
        )
        self.assertRaisesRegex(
            ValidationError,
            "Error in {}: Duplicated phone number in CRMLead petitions.".format(crm_leads[0].lead_line_id),  # noqa
            crm_leads.action_set_remesa,
        )

    def test_crm_lead_action_set_remesa_dont_raise_error_with_existent_phone_number_if_skip_true(self):  # noqa
        product_mobile = self.env.ref(
            "somconnexio.100MinSenseDades_product_template"
        ).product_variant_id
        previous_provider = self.ref("somconnexio.previousprovider1")
        mobile_isp_info = self.env['mobile.isp.info'].create({
            'type': 'portability',
            'phone_number': '663322234',
            'previous_contract_type': 'contract',
            'previous_provider': previous_provider,
        })
        lead_line_vals = {
            'name': '663322234',
            'product_id': product_mobile.id,
            'mobile_isp_info': mobile_isp_info.id,
        }
        self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
                'stage_id': self.env.ref("crm.stage_lead4").id,
            }]
        )
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
                'skip_duplicated_phone_validation': True
            }]
        )

        self.assertNotEquals(crm_lead.stage_id, self.browse_ref('crm.stage_lead3'))
        crm_lead.action_set_remesa()
        self.assertEquals(crm_lead.stage_id, self.browse_ref('crm.stage_lead3'))

    def test_crm_lead_action_set_remesa_dont_raise_error_with_existent_phone_number_if_dash(self):  # noqa
        product_broadband = self.env.ref(
            "somconnexio.ADSL20MB100MinFixMobile_product_template"
        ).product_variant_id
        previous_provider = self.ref("somconnexio.previousprovider3")
        broadband_isp_info = self.env['broadband.isp.info'].create({
            'type': 'portability',
            'phone_number': '-',
            'previous_service': 'adsl',
            'previous_provider': previous_provider,
        })
        lead_line_vals = {
            'name': '-',
            'product_id': product_broadband.id,
            'broadband_isp_info': broadband_isp_info.id,
        }
        self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
                'stage_id': self.env.ref("crm.stage_lead4").id,
            }]
        )
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )

        self.assertNotEquals(crm_lead.stage_id, self.browse_ref('crm.stage_lead3'))
        crm_lead.action_set_remesa()
        self.assertEquals(crm_lead.stage_id, self.browse_ref('crm.stage_lead3'))

    def test_mobile_phone_number_portability_format_validation(self):
        product_mobile = self.env.ref(
            "somconnexio.100MinSenseDades_product_template"
        ).product_variant_id
        previous_provider = self.ref("somconnexio.previousprovider1")
        mobile_isp_info = self.env['mobile.isp.info'].create({
            'type': 'portability',
            'phone_number': '497453838',
            'previous_contract_type': 'contract',
            'previous_provider': previous_provider,
        })
        lead_line_vals = {
            'name': '497453838',
            'product_id': product_mobile.id,
            'mobile_isp_info': mobile_isp_info.id,
        }
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )

        self.assertRaisesRegex(
            ValidationError,
            'Mobile phone number has to be a 9 digit number starting with 6 or 7',
            crm_lead.action_set_remesa
        )

    def test_broadband_phone_number_portability_format_validation(self):
        product_broadband = self.env.ref(
            "somconnexio.ADSL20MB100MinFixMobile_product_template"
        ).product_variant_id
        previous_provider = self.ref("somconnexio.previousprovider3")
        broadband_isp_info = self.env['broadband.isp.info'].create({
            'type': 'portability',
            'phone_number': '497453838',
            'previous_service': 'adsl',
            'previous_contract_type': 'contract',
            'previous_provider': previous_provider,
        })
        lead_line_vals = {
            'name': '497453838',
            'product_id': product_broadband.id,
            'broadband_isp_info': broadband_isp_info.id,
        }
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )

        self.assertRaisesRegex(
            ValidationError,
            'Landline phone number has to be a dash "-" '
            'or a 9 digit number starting with 8 or 9',
            crm_lead.action_set_remesa
        )

    def test_broadband_phone_number_portability_skip_format_validation(self):
        product_broadband = self.env.ref(
            "somconnexio.ADSL20MB100MinFixMobile_product_template"
        ).product_variant_id
        previous_provider = self.ref("somconnexio.previousprovider3")
        broadband_isp_info = self.env['broadband.isp.info'].create({
            'type': 'portability',
            'phone_number': '497453838',
            'previous_service': 'adsl',
            'previous_provider': previous_provider,
        })
        lead_line_vals = {
            'name': '497453838',
            'product_id': product_broadband.id,
            'broadband_isp_info': broadband_isp_info.id,
            'check_phone_number': True,
        }
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )
        crm_lead.action_set_remesa()
        self.assertEquals(crm_lead.stage_id, self.browse_ref('crm.stage_lead3'))

    def test_broadband_phone_number_portability_format_validation_dash(self):
        product_broadband = self.env.ref(
            "somconnexio.ADSL20MBSenseFix"
        ).product_variant_id
        previous_provider = self.ref("somconnexio.previousprovider3")
        broadband_isp_info = self.env['broadband.isp.info'].create({
            'type': 'portability',
            'phone_number': '-',
            'previous_service': 'adsl',
            'previous_contract_type': 'contract',
            'previous_provider': previous_provider,
        })
        lead_line_vals = {
            'name': '497453838',
            'product_id': product_broadband.id,
            'broadband_isp_info': broadband_isp_info.id,
        }
        crm_lead = self.env['crm.lead'].create(
            [{
                'name': 'Test Lead',
                'partner_id': self.partner_id.id,
                'iban': self.partner_id.bank_ids[0].sanitized_acc_number,
                'lead_line_ids': [(0, 0, lead_line_vals)],
            }]
        )

        crm_lead.action_set_remesa()
        self.assertEquals(crm_lead.stage_id, self.browse_ref('crm.stage_lead3'))
