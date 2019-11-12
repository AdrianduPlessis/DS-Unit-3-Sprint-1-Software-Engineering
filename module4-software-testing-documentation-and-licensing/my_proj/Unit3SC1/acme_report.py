#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # Generate and add random products.
    for _ in range(num_products):
        rand_adjective = sample(ADJECTIVES, 1)[0]
        rand_noun = sample(NOUNS, 1)[0]
        rand_name = f'{rand_adjective} {rand_noun}'

        rand_price = randint(5, 100)
        rand_weight = randint(5, 100)

        rand_flammability = uniform(0.0, 2.5)

        rand_product = Product(rand_name, rand_price, rand_weight, rand_flammability)
        products.append(rand_product)

    return products


def count_unique(items):
    unique_items = set(items)
    num_unique = len(unique_items)
    return num_unique


def average(val):
    total = sum(val)
    count = len(val)
    avr = total / count

    return avr


def inventory_report(products):
    # Loop over the products to calculate the report.
    # TODO Make DRY
    names = []

    prices = []
    weights = []
    flammabilities = []
    features_to_average = [prices, weights, flammabilities]

    for product in products:
        names.append(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)

    print(f'Unique product names: {count_unique(names)}')
    for feature in features_to_average:
        print(f'Average price: {average(feature)}')


if __name__ == '__main__':
    inventory_report(generate_products())
