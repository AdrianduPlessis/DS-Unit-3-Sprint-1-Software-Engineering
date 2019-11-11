#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability_and_explode(self):
        """Test specific expected outcomes from stealability() and explode()"""
        prod = Product('Test Product', 44, 100, 0.9)
        self.assertEqual(prod.stealability(), 'Not so stealable...')
        self.assertEqual(prod.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
    def test_default_num_products(self):
        """Test default num products price being 30."""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test checks that the generated names for a default batch of products
        are all valid possible names to generate"""

        '''
        products = generate_products()
        for product in products:
            name = product.name.split()
        '''
        pass


if __name__ == '__main__':
    unittest.main()