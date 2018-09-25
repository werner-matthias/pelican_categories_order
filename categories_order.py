"""
Category Order
"""

from pelican import signals

order_setting = dict()

def order_function(category):
    global order_setting
    key = category[0]._name
    if key in order_setting:
        return order_setting[key]
    else:
        return 100

def reorder_categories(generator):
    global order_setting    
    if 'CATEGORIES_ORDER' in generator.settings:
        order_setting = generator.settings['CATEGORIES_ORDER']
        generator.categories.sort(key=order_function)
    return

def register():
    signals.article_generator_finalized.connect(reorder_categories)
