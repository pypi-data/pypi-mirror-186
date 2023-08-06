# pyramid-helpers -- Helpers to develop Pyramid applications
# By: Cyril Lacoux <clacoux@easter-eggs.com>
#     Valéry Febvre <vfebvre@easter-eggs.com>
#
# Copyright (C) 2011-2022 Cyril Lacoux, Easter-eggs
# https://gitlab.com/yack/pyramid-helpers
#
# This file is part of pyramid-helpers.
#
# pyramid-helpers is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# pyramid-helpers is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" Authentication forms """

import formencode
from formencode import validators


# auth.sign-in
class SignInForm(formencode.Schema):
    """
    :param username: The username to authenticate
    :param password: The password to validate
    :param redirect: URL to redirect to if authentication is successful
    """

    allow_extra_fields = True
    filter_extra_fields = True

    username = validators.String(not_empty=True)
    password = validators.String(not_empty=True)
    redirect = validators.String(if_missing=None, if_empty=None)
