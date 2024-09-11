# -*- coding: utf-8 -*-
###############################################################################
#
#    IPEMMA, S.A.
#
#    Copyright (C) 2023-TODAY Ipemma S.A.(<https://www.ipemma.com>)
#    Author: Marlon Macario (Contact : mmacario@ipemma.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################
{
    'name': "RMC Whatsapp",
    'version': '1.0.0',
    'category': 'Extra Tools',
    'summary': """Send whatsapp messages to the partner""",
    'description': """ This module helps you to send a whatsapp message to your 
     partners that are in sale order, purchase order, invoice and bills, and
     deliver orders.""",
    'author': 'IPEMMA',
    'company': 'IPEMMA, S.A.',
    'maintainer': 'IPEMMA, S.A.',
    'website': "https://www.ipemma.com",
    'depends': ['base', 'web', 'sale', 'stock', 'purchase', 'account',
                'contacts', 'website_livechat'],
    'data': [
        'security/ir.model.access.csv',
        'data/account_move_data.xml',
        'data/purchase_order_data.xml',
        'data/sale_order_data.xml',
        'data/stock_picking_data.xml',
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/stock_picking_views.xml',
        'views/account_move_views.xml',
        'views/mail_template_views.xml',
        'views/res_config_settings_views.xml',
        'views/mail_channel_views.xml',
        'wizard/send_whatsapp_message_views.xml',
    ],
    'external_dependencies': {
        'python': ['twilio'],
    },
    'images': ['static/description/banner.png'],
    'license': "AGPL-3",
    'installable': True,
    'auto_install': False,
    'application': False,
}
