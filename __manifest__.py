# -*- coding: utf-8 -*-
{
    'name': "basvuru",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',"hr_recruitment" , 'mail', 'website_hr_recruitment','survey','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/custom_basvuru_views.xml',
        'views/hr_applicant.xml',
        'views/user_form.xml',
        # 'views/update_recruitment_stages.xml',
        'data/stages_update.xml',
        'views/hr_department_views.xml',
        'data/ilce_mahalle_data.xml',
    ],


    'assets': {
            'web.assets_backend': [
                'basvuru/static/src/css/custom_style.css',
                # 'basvuru/static/src/js/department_capacity_check.js', # kapasite aşımı denemesi için kullanıldı
            ],
    },

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
