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

""" Articles forms """

import formencode
from formencode import validators

from .validators import List


# articles.create, articles.modify
# api.articles.create, api.articles.modify
class CreateForm(formencode.Schema):
    """
    :param title: Title
    :param text: Text
    :param status: Status
    """
    allow_extra_fields = True
    filter_extra_fields = True

    title = validators.String(not_empty=True)
    text = validators.String(not_empty=True)
    status = validators.OneOf(['draft', 'published', 'refused'], not_empty=True)


# api.articles.status
class StatusForm(formencode.Schema):
    """
    :param status: Status
    """
    allow_extra_fields = True
    filter_extra_fields = True

    status = validators.OneOf(['draft', 'published', 'refused'], not_empty=True)


# api.articles.search
class SearchForm(formencode.Schema):
    """
    :param exact: Text search strings must exact match the title of article
    :param excluded_ids: List of article Ids to exclude from result
    :param selected_ids: List of article Ids to include in result
    :param status: Status of article
    :param term: Text search string used to filter articles. Only articles containing the term in their title will be returned
    :param text: Text
    :param title: Title
    """
    allow_extra_fields = True
    filter_extra_fields = True

    exact = validators.StringBool(if_missing=False, if_empty=False)
    excluded_ids = List(validators.Int())
    selected_ids = List(validators.Int())
    status = validators.OneOf(['draft', 'published', 'refused'], if_empty=None, if_missing=None)
    term = validators.String(if_missing=None, if_empty=None)
    text = validators.String(if_empty=None, if_missing=None)
    title = validators.String(if_empty=None, if_missing=None)
