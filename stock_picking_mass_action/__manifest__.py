# Copyright 2014 Camptocamp SA - Guewen Baconnier
# Copyright 2018 Tecnativa - Vicent Cubells
# Copyright 2019 Tecnativa - Carlos Dauden
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Stock Picking Mass Action",
    "version": "13.0.1.0.0",
    "author": "Camptocamp, " "GRAP," "Tecnativa," "Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/stock-logistics-workflow/",
    "license": "AGPL-3",
    "category": "Warehouse Management",
    "depends": ["stock_account"],
    "data": ["wizard/mass_action_view.xml", "data/ir_cron.xml", "security/ir.model.access.csv"],
}
