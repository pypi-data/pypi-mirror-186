import logging

from odoo import _
from odoo.addons.component.core import Component

from . import schemas

_logger = logging.getLogger(__name__)


class ProductCatalog(Component):
    _inherit = "base.rest.service"
    _name = "product_catalog.service"
    _usage = "product-catalog"
    _collection = "emc.services"
    _description = """
        Product catalog service to expose all the SomConnexió service products
        and their prices and other attributes.
        Filtering by code is enabled to get a specific tax-related priceList.
        Filtering by service category is enabled to get products only
        Filtering by product code is enabled to get products available for a
        tariff change from selected product.
    """

    def search(self, code=None, categ=None, product_code=None):
        _logger.info("Searching product catalog...")

        product = self._get_filter_product(product_code)
        service_products = self._get_service_products(categ)

        domain = [('code', '=', code)] if code else []
        pricelists = self.env["product.pricelist"].search(domain)

        return {
            "pricelists": [
                self._build_response_from_pricelist(
                    pricelist,
                    service_products,
                    product
                ) for pricelist in pricelists
            ]
        }

    def _get_filter_product(self, product_code):
        if not product_code:
            return None
        domain = [('default_code', '=', product_code)]
        return self.env["product.product"].search(domain)

    def _build_response_from_pricelist(self, pricelist, products, product):
        if product and product.has_custom_products_to_change_tariff:
            pricelist_data = {
                "code": pricelist.code,
                "products": [
                    self._extract_product_info(p, pricelist.id)
                    for p in product.products_available_change_tariff
                ]
            }
        else:
            pricelist_data = {
                "code": pricelist.code,
                "products": [
                    self._extract_product_info(p, pricelist.id)
                    for p in products
                ]
            }
        return pricelist_data

    def _get_service_products(self, service_category):
        mobile_categ_id = self.env.ref('somconnexio.mobile_service').id,
        adsl_categ_id = self.env.ref('somconnexio.broadband_adsl_service').id,
        fiber_categ_id = self.env.ref('somconnexio.broadband_fiber_service').id
        router_4G_categ_id = self.env.ref('somconnexio.broadband_4G_service').id

        category_id_list = []
        if not service_category:
            category_id_list.extend([mobile_categ_id, adsl_categ_id,
                                     fiber_categ_id, router_4G_categ_id])
        elif service_category == "mobile":
            category_id_list.append(mobile_categ_id)
        elif service_category == "adsl":
            category_id_list.append(adsl_categ_id)
        elif service_category == "fiber":
            category_id_list.append(fiber_categ_id)
        elif service_category == "4G":
            category_id_list.append(router_4G_categ_id)

        service_product_templates = self.env["product.template"].search([
            ("categ_id", 'in', category_id_list),
        ])
        service_products = self.env["product.product"].search([
            ("product_tmpl_id", 'in', [tmpl.id for tmpl in service_product_templates]),
            ("public", '=', True),
        ])
        return service_products

    def _extract_product_info(self, product, pricelist_id):
        product.ensure_one()

        product_info = {
            "code": product.default_code,
            "name": _(product.showed_name),
            "price": product.with_context(pricelist=pricelist_id).price,
            "category": self._get_product_category(product),
            "minutes": None,
            "data": None,
            "bandwidth": None,
            "available_for": self._get_product_available_for(product),
        }
        if product_info.get("category") == "mobile":
            product_info.update({
                "minutes": self._get_minutes_from_mobile_product(product),
                "data": self._get_data_from_product(product),
            })
        elif product_info.get("category") == "adsl":
            product_info.update({
                "bandwidth": 20,
            })
        elif product_info.get("category") == "4G":
            product_info.update({
                "data": self._get_data_from_product(product),
            })
        else:
            product_info.update({
                "bandwidth": self._get_bandwith_from_BA_product(product),
            })

        return product_info

    def _get_product_available_for(self, product):
        sponsee_coop_agreement = self.env["coop.agreement"].search([
            ("code", "=", "SC")
        ])
        coop_agreements = self.env["coop.agreement"].search([
            ("code", "!=", "SC")
        ])
        sponsee_products = sponsee_coop_agreement.products
        coop_agreement_products = []
        for coop_agreement in coop_agreements:
            coop_agreement_products += coop_agreement.products

        coop_agreement_products = list(set(coop_agreement_products))

        available_for = ["member"]
        if product.product_tmpl_id in coop_agreement_products:
            available_for += ["coop_agreement"]
        if product.product_tmpl_id in sponsee_products:
            available_for += ["sponsored"]
        return available_for

    def _get_product_category(self, product):
        category = product.product_tmpl_id.categ_id
        if category == self.env.ref('somconnexio.mobile_service'):
            return "mobile"
        elif category == self.env.ref('somconnexio.broadband_fiber_service'):
            return "fiber"
        elif category == self.env.ref('somconnexio.broadband_adsl_service'):
            return "adsl"
        elif category == self.env.ref('somconnexio.broadband_4G_service'):
            return "4G"

    def _get_minutes_from_mobile_product(self, product):
        # Product code format: SE_SC_REC_MOBILE_T_*min*_*data*
        min = product.without_lang().get_catalog_name('Min')
        return 99999 if min == "UNL" else int(min)

    def _get_data_from_product(self, product):
        # Product code format: SE_SC_REC_MOBILE_T_*min*_*data*
        data = product.without_lang().get_catalog_name('Data')
        return int(data)

    def _get_bandwith_from_BA_product(self, product):
        # Product code format: SE_SC_REC_BA_F_**bandwith**
        bw = product.without_lang().get_catalog_name("Bandwidth")
        return int(bw)

    def _validator_search(self):
        return schemas.S_PRODUCT_CATALOG_REQUEST_SEARCH

    def _validator_return_search(self):
        return schemas.S_PRODUCT_CATALOG_RETURN_SEARCH
