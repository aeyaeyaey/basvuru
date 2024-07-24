from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


class HrApplicant(models.Model):
    _inherit = 'hr.applicant'

    partner_id = fields.Many2one('res.partner', "Contact", copy=False)

    partner_gender = fields.Selection([
        ('male', 'Erkek'),
        ('female', 'Kadın'),
    ], compute='_compute_partner_fields', string='Cinsiyet', store=True)

    partner_school_email = fields.Char(string="Okul Email", related='partner_id.school_email_yeni', store=True)
    partner_nationality_id = fields.Many2one('res.country', string='Uyruk', related='partner_id.nationality_id_yeni',
                                             store=True)
    partner_tc_kimlik_no = fields.Char(string="Tc Kimlik No", related='partner_id.tc_kimlik_no_yeni', store=True)
    partner_birth_date = fields.Date(string="Doğum Günü", related='partner_id.birth_date_yeni', store=True)
    partner_birth_place = fields.Char(string="Doğum Yeri", related='partner_id.birth_place_yeni', store=True)

    @api.depends('partner_id')
    def _compute_partner_fields(self):
        for applicant in self:
            if applicant.partner_id:
                applicant.partner_gender = applicant.partner_id.gender_yeni
            else:
                applicant.partner_gender = False

    @api.model
    def create(self, vals):
        res = super(HrApplicant, self).create(vals)
        if res.partner_id:
            res.partner_gender = res.partner_id.gender_yeni
        return res

    def write(self, vals):
        res = super(HrApplicant, self).write(vals)
        for applicant in self:
            if applicant.partner_id:
                applicant.partner_gender = applicant.partner_id.gender_yeni
        return res
