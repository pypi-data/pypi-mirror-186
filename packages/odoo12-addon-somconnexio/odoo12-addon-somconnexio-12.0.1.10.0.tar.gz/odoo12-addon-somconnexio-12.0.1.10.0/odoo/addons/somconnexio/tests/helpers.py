from faker import Faker
from datetime import datetime, timedelta
import random

faker = Faker("es_CA")


def random_ref():
    return str(random.randint(0, 99999))


def random_mobile_phone():
    return str(random.randint(6, 7)) + str(faker.random_number(digits=8))


def random_landline_number():
    return str(random.randint(8, 9)) + str(faker.random_number(digits=8))


def subscription_request_create_data(odoo_env):
    return {
        'partner_id': 0,
        'already_cooperator': False,
        'is_company': False,
        'firstname': faker.first_name(),
        'lastname': faker.last_name(),
        'email': faker.email(),
        'ordered_parts': 1,
        "share_product_id": odoo_env.browse_ref(
            "easy_my_coop.product_template_share_type_2_demo"
        ).product_variant_id.id,
        'address': faker.street_address(),
        'city': faker.city(),
        'zip_code': faker.postcode(),
        'country_id': odoo_env.ref('base.es'),
        'date': datetime.now() - timedelta(days=12),
        'company_id': 1,
        'source': 'manual',
        'lang': random.choice(["es_ES", "ca_ES"]),
        'sponsor_id': False,
        'vat': faker.vat_id(),
        'discovery_channel_id': odoo_env.browse_ref(
            'somconnexio.other_cooperatives'
        ).id,
        'iban': faker.iban(),
        'state': 'draft',
    }


def partner_create_data(odoo_env):
    return {
        'parent_id': False,
        'name': faker.name(),
        'email': faker.email(),
        'street': faker.street_address(),
        'street2': faker.street_address(),
        'city': faker.city(),
        'zip_code': faker.postcode(),
        'country_id': odoo_env.ref('base.es'),
        'state_id': odoo_env.ref('base.state_es_b'),
        'customer': True,
        'ref': random_ref(),
        'lang': random.choice(["es_ES", "ca_ES"]),
    }


def crm_lead_create(odoo_env, partner_id, service_category, portability=False):
    product_tmpl_switcher = {
        'mobile': _mobil_service_product_create_data(odoo_env),
        'fiber': _fiber_service_product_create_data(odoo_env),
        'adsl': _adsl_service_product_create_data(odoo_env),
        '4G': _4G_service_product_create_data(odoo_env),
    }
    product_tmpl_args = product_tmpl_switcher.get(service_category)

    product_tmpl = odoo_env['product.template'].create(product_tmpl_args)
    crm_lead_line_args = {
        'name': 'CRM Lead',
        'product_id': product_tmpl.product_variant_id.id,
    }
    isp_info_args = {
        'type': 'portability',
        'previous_contract_type': 'contract',
        'previous_provider': odoo_env.ref('somconnexio.previousprovider39').id,
        'phone_number': None,
    } if portability else {'type': 'new'}

    if service_category == 'mobile':
        isp_info_args.update({'phone_number': random_mobile_phone()})
        isp_info = odoo_env['mobile.isp.info'].create(isp_info_args)
        crm_lead_line_args.update({'mobile_isp_info': isp_info.id})
    else:
        isp_info_args.update({
            'phone_number': '-' if service_category == '4G'
            else random_landline_number()
        })
        isp_info = odoo_env['broadband.isp.info'].create(isp_info_args)
        crm_lead_line_args.update({'broadband_isp_info': isp_info.id})
    crm_lead_line = odoo_env['crm.lead.line'].create(crm_lead_line_args)

    return odoo_env['crm.lead'].create(
        {
            'name': 'Test Lead',
            'partner_id': partner_id.id,
            'iban': partner_id.bank_ids[0].sanitized_acc_number,
            'lead_line_ids': [(6, 0, [crm_lead_line.id])],
            'stage_id': odoo_env.ref("crm.stage_lead1").id,
        }
    )


def _mobil_service_product_create_data(odoo_env):
    return {
        'name': 'Sense minutes',
        'type': 'service',
        'categ_id': odoo_env.ref('somconnexio.mobile_service').id
    }


def _fiber_service_product_create_data(odoo_env):
    return {
        'name': 'Fiber 200 Mb',
        'type': 'service',
        'categ_id': odoo_env.ref('somconnexio.broadband_fiber_service').id
    }


def _adsl_service_product_create_data(odoo_env):
    return {
        'name': 'ADSL 20Mb',
        'type': 'service',
        'categ_id': odoo_env.ref('somconnexio.broadband_adsl_service').id
    }


def _4G_service_product_create_data(odoo_env):
    return {
        'name': 'Router 4G',
        'type': 'service',
        'categ_id': odoo_env.ref('somconnexio.broadband_4G_service').id
    }
