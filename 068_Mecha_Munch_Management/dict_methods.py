# !/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@File               : dict_methods.py
@Project            : 068_Mecha_Munch_Management
@CreateTime         : 2026/8/16 23:39
@Author             : biaobro
@Software           : PyCharm
@Last Modify Time   : 2026/8/16 23:39 
@Version            : 1.0
@Description        : None
"""

"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    Parameters:
        current_cart (dict): The current shopping cart.
        items_to_add (iterable): The items to add to the cart.

    Returns:
        dict: The updated user cart dictionary.
    """
    for item_key in items_to_add:
        if item_key in current_cart.keys():
            current_cart[item_key] = current_cart[item_key] + 1
        else:
            current_cart[item_key] = 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    Parameters:
        notes (iterable): Group of items to add to cart.

    Returns:
        dict: A user shopping cart dictionary.
    """
    user_cart = {}
    for item in list(notes):
        user_cart[item] = 1
    return user_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    Parameters:
        ideas (dict): The "recipe ideas" dict. 第1个参数是 dict 字典
        recipe_updates (iterable): Updates for the ideas section. 第2个参数是 列表 或 元组

    Returns:
        dict: The updated "recipe ideas" dict.
    """
    dict_recipe_updates = dict(recipe_updates)
    for key in dict_recipe_updates.keys():
        ideas[key] = dict_recipe_updates[key]
    return ideas


def sort_entries(cart):
    """Sort a user's shopping cart in alphabetical order.

    Parameters:
        cart (dict): A user's shopping cart dictionary.

    Returns:
        dict: A user's shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Combine user's order to aisle and refrigeration information.

    Parameters:
        cart (dict): The user's shopping cart dictionary.
        aisle_mapping (dict): The aisle and refrigeration information dictionary.

    Returns:
        dict: The fulfillment dictionary ready to send to store.
    """
    result = {}
    for key in reversed(sorted(cart.keys())):
        aisle_mapping[key].insert(0, cart[key])
        result[key] = aisle_mapping[key]
    return result


def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    Parameters:
        fulfillment cart (dict): The fulfillment cart to send to store.
        store_inventory (dict): The stores available inventory.

    Returns:
        dict: The store_inventory updated.
    """
    for key in fulfillment_cart.keys():
        store_inventory[key][0] = store_inventory[key][0] - fulfillment_cart[key][0]
        if store_inventory[key][0] <= 0:
            store_inventory[key][0] = "Out of Stock"
    return store_inventory

print(update_recipes(
    {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
    'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
    'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}},
    [('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
    ('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
    ('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})]
    ))
