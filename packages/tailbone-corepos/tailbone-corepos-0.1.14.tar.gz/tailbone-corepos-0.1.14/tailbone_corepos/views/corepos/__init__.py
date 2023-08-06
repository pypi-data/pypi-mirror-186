# -*- coding: utf-8; -*-
################################################################################
#
#  Rattail -- Retail Software Framework
#  Copyright © 2010-2022 Lance Edgar
#
#  This file is part of Rattail.
#
#  Rattail is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Rattail is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  Rattail.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
CORE POS views
"""

from .master import CoreOfficeMasterView


def includeme(config):
    config.include('tailbone_corepos.views.corepos.parameters')
    config.include('tailbone_corepos.views.corepos.tablesyncrules')
    config.include('tailbone_corepos.views.corepos.users')
    config.include('tailbone_corepos.views.corepos.groups')
    config.include('tailbone_corepos.views.corepos.stores')
    config.include('tailbone_corepos.views.corepos.departments')
    config.include('tailbone_corepos.views.corepos.subdepartments')
    config.include('tailbone_corepos.views.corepos.superdepartments')
    config.include('tailbone_corepos.views.corepos.vendors')
    config.include('tailbone_corepos.views.corepos.origins')
    config.include('tailbone_corepos.views.corepos.products')
    config.include('tailbone_corepos.views.corepos.likecodes')
    config.include('tailbone_corepos.views.corepos.scaleitems')
    config.include('tailbone_corepos.views.corepos.members')
    config.include('tailbone_corepos.views.corepos.customers')
    config.include('tailbone_corepos.views.corepos.employees')
    config.include('tailbone_corepos.views.corepos.coupons')
    config.include('tailbone_corepos.views.corepos.taxrates')
    config.include('tailbone_corepos.views.corepos.transactions')
    config.include('tailbone_corepos.views.corepos.batches')
    config.include('tailbone_corepos.views.corepos.purchaseorders')
