{
    'name': 'AI assistant to keep Odoo in sync with the latest vendor updates',
    'version': '1.0',
    'category': 'Extra Tools',
    'sequence': '-100',
    'description': """Bryo reads and understands vendor emails, extracts relevant information about the order, assists users on how to update Odoo and notifies the relevant stakeholders.""",
    'author': 'Bryo UG',
    'maintainer': 'Bryo UG',
    'license': 'LGPL-3',
    'website': 'https://www.bryo.io',
    'summary': 'Bryo reads and understands vendor emails, extracts relevant information about the order, assists users on how to update Odoo and notifies the relevant stakeholders.',
    "keywords": ["fulfillment", "bard", "chatgpt", "openai", "AI", "copilot", "llm"],
    'data': [
        'data/leadtime_copilot_channel_data.xml',
        'data/copilot_user_partner_data.xml',
    ],
    "depends": [
        "sale",
        "sale_stock",
        "mrp",
        "purchase"
    ],
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'installable': True,
}