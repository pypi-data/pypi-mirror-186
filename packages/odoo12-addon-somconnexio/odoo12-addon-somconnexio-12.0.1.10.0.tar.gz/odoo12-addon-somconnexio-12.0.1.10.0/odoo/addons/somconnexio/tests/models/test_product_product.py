from ..sc_test_case import SCTestCase
from mock import patch


class TestProductionProduct(SCTestCase):
    def test_product_wo_catalog_name(self):
        product = self.browse_ref('somconnexio.Fibra100Mb')
        self.assertFalse(product.get_catalog_name('Min BA'))

    def test_product_catalog_name_in_template(self):
        product = self.browse_ref('somconnexio.100MinSenseDades')
        # noupdate=1 in product_attribute_value.xml
        product.product_tmpl_id.catalog_attribute_id.catalog_name = '100'
        self.assertEquals(product.get_catalog_name('Min'), '100')

    def test_product_catalog_name_in_product(self):
        product = self.browse_ref('somconnexio.100MinSenseDades')
        # noupdate=1 in product_attribute_value.xml
        product.attribute_value_ids.catalog_name = '0'
        self.assertEquals(product.get_catalog_name('Data'), '0')

    @patch('odoo.addons.mail.models.mail_thread.MailThread.message_post')
    def test_write(self, message_post_mock):
        product = self.browse_ref('somconnexio.Fibra100Mb')
        old_value = product.default_code
        product.write({'default_code': 'new-default-code-value'})
        expected_msg = "Field '{}' edited from '{}' to '{}'".format(
            'default_code', old_value, 'new-default-code-value'
        )
        message_post_mock.assert_called_once_with(body=expected_msg)
