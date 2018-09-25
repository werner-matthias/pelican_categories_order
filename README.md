# Categories Order

While Pelican allows for sorting articles or pages, the categories can
only be sorted in alphabetic order (or reverse). This plugin allows
for an abritary order.

## Why would I need it?

If cateogries appear in menu or sidebar, one might want a different
order than alphabetic order. E.g., I want alway the categorys "misc" to
be the last.

## Installation

Copy the `pelican_categories_order` folder to  a place your
`PLUGIN_PATHS`.
Next, add `pelican_categories_order` to the `PLUGIN` list, e.g.:

	PLUGINS = [' pelican_categories_order']

## Configuration

Add a dictionary `CATEGORIES_ORDER` to your `pelicanconf.py` in the
following way:

	CATEGORIES_ORDER = {
		'category b': 10,
		'category a': 20,
		'misc':       999,
		}

A category that does not exist in `CATEGORIES_ORDER` will be ordered
with the order value 100.
