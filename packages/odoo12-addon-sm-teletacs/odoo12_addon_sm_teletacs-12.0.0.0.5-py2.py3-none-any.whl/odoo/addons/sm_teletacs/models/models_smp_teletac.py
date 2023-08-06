# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _
from odoo.addons.sm_maintenance.models.models_sm_resources import sm_resources
from odoo.addons.sm_maintenance.models.models_sm_utils import sm_utils


class smp_teletac(models.Model):
  _name = 'smp.sm_teletac'

  name = fields.Char(string=_("Name"), compute="_teletac_name")
  date = fields.Date(string=_("Date"))
  hour = fields.Char(string=_("Hour"))
  description = fields.Char(string=_("Description"))
  amount = fields.Float(string=_("Amount"))
  discount = fields.Float(string=_("Discount"))
  ttype = fields.Char(string=_("Type"))
  license_plate = fields.Char(string=_("License Plate (car)"))
  reservation_compute_id = fields.Many2one('smp.sm_reservation_compute', string=_("Related reservation"))
  related_invoice_id = fields.Many2one('account.invoice', string=_("Related invoice"))
  related_member_id = fields.Many2one('res.partner', string=_("Related member"),
    compute="_get_related_member_id", store=True)
  cs_user_type = fields.Char(string=_("cs user type"),
    compute="_get_cs_user_type", store=True)
  reservation_compute_invoiced = fields.Boolean(string=_("Compute invoiced"),
    compute="_check_compute_invoiced", store=True)
  reservation_compute_forgiven = fields.Boolean(string=_("Compute forgiven"),
    compute="_check_compute_forgiven", store=True)

  _order = "date desc"

  @api.depends('date', 'hour', 'ttype', 'license_plate')
  def _teletac_name(self):
    for record in self:
      record.name = str(record.date) + ' - ' + str(record.hour) + ' - ' + str(record.ttype) + ' - ' \
        + str(record.license_plate)

  @api.depends('reservation_compute_id', 'related_invoice_id')
  def _check_compute_invoiced(self):
    for record in self:
      if record.reservation_compute_id.id:
        record.reservation_compute_invoiced = record.reservation_compute_id.compute_invoiced
      else:
        record.reservation_compute_invoiced = False

  @api.depends('reservation_compute_id', 'related_invoice_id')
  def _check_compute_forgiven(self):
    for record in self:
      if record.reservation_compute_id.id:
        record.reservation_compute_forgiven = record.reservation_compute_id.compute_forgiven
      else:
        record.reservation_compute_forgiven = False

  @api.depends('reservation_compute_id')
  def _get_related_member_id(self):
    for record in self:
      if record.reservation_compute_id.id:
        record.related_member_id = record.reservation_compute_id.member_id
      else:
        record.related_member_id = False

  @api.depends('related_member_id')
  def _get_cs_user_type(self):
    for record in self:
      if record.reservation_compute_id.id:
        record.cs_user_type = record.related_member_id.cs_user_type

  @api.multi
  def compute(self):
    if self.env.context:
      if 'active_ids' in self.env.context:
        teletacs = self.env['smp.sm_teletac'].browse(self.env.context['active_ids'])
        if teletacs.exists():
          company = self.env.user.company_id
          q_car_owner_group_index = company.sm_carsharing_api_credentials_admin_group
          for teletac in teletacs:
            car = self.env['smp.sm_car'].search([
              ('license_plate', '=like', teletac.license_plate+"%"),
              ('owner_group_index','=',q_car_owner_group_index)
            ])
            if car.exists():
              query = [
                ('current_car', 'like', car[0].name),
                ('effectiveStartTime', '<=', str(sm_utils.local_to_utc_datetime(str(teletac.date) + ' ' + teletac.hour))),
                ('effectiveEndTime', '>=', str(sm_utils.local_to_utc_datetime(str(teletac.date) + ' ' + teletac.hour)))
              ]
              computes = self.env['smp.sm_reservation_compute'].search(query)
              if computes.exists():
                teletac.write({
                  'reservation_compute_id': computes[0].id
                })
    return sm_resources.getInstance().get_successful_action_message(self, _('Compute done successfully'), self._name)

  @api.multi
  def reset_state(self):
    if self.env.context:
      if 'active_ids' in self.env.context:
        teletacs = self.env['smp.sm_teletac'].browse(self.env.context['active_ids'])
        if teletacs.exists():
          for teletac in teletacs:
            teletac.related_invoice_id = None
            teletac.invoice_report_id = None
            teletac.reservation_compute_invoiced = False
