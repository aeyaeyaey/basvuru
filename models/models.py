# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class basvuru(models.Model):
#     _name = 'basvuru.basvuru'
#     _description = 'basvuru.basvuru'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import api, SUPERUSER_ID

def pre_init_hook(cr):
    env = api.Environment(cr, SUPERUSER_ID, {})
    stages_to_delete = [
        'hr_recruitment.stage_job1',
        'hr_recruitment.stage_job2',
        'hr_recruitment.stage_job3',
        'hr_recruitment.stage_job4',
        'hr_recruitment.stage_job5'
    ]
    for stage_xml_id in stages_to_delete:
        try:
            stage_id = env['ir.model.data'].xmlid_to_res_id(stage_xml_id, raise_if_not_found=False)
            if stage_id:
                env['hr.recruitment.stage'].browse(stage_id).unlink()
        except ValueError:
            # XML ID not found, skip
            continue
