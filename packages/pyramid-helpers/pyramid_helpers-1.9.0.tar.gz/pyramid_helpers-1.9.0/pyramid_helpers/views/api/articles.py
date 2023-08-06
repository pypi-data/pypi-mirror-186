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

"""
Articles API
"""

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config

from pyramid_helpers.forms import validate
from pyramid_helpers.forms.articles import CreateForm
from pyramid_helpers.forms.articles import SearchForm
from pyramid_helpers.forms.articles import StatusForm
from pyramid_helpers.funcs.articles import build_search_query
from pyramid_helpers.funcs.articles import create_or_modify
from pyramid_helpers.funcs.articles import get_article
from pyramid_helpers.models import DBSession
from pyramid_helpers.paginate import paginate


@view_config(route_name='api.articles.create', renderer='json', permission='articles.create')
@validate('article', CreateForm)
def create(request):
    """
    Creates an article
    """
    form = request.forms['article']

    article = create_or_modify(request, form)
    if article is None:
        raise HTTPBadRequest(json=form.errors)

    result = dict(
        url=request.path_qs,
        method=request.method,
        params=form.params,
        apiVersion='1.0',
        result=True,
        article=article.to_dict(context='create'),
    )

    request.response.status_int = 201
    return result


@view_config(route_name='api.articles.delete', renderer='json', permission='articles.delete')
def delete(request):
    """
    Deletes an article
    """
    translate = request.translate

    article = get_article(request)
    if article is None:
        raise HTTPNotFound(detail=translate('Invalid article'))

    DBSession.delete(article)

    result = dict(
        url=request.path_qs,
        method=request.method,
        apiVersion='1.0',
        result=True,
    )

    return result


@view_config(route_name='api.articles.modify', renderer='json', permission='articles.modify')
@validate('article', CreateForm)
def modify(request):
    """
    Modifies an article
    """
    translate = request.translate
    form = request.forms['article']

    article = get_article(request)
    if article is None:
        raise HTTPNotFound(detail=translate('Invalid article'))

    if not create_or_modify(request, form, article=article):
        raise HTTPBadRequest(json=form.errors)

    result = dict(
        url=request.path_qs,
        method=request.method,
        params=form.params,
        apiVersion='1.0',
        result=True,
        article=article.to_dict(context='modify'),
    )

    return result


@view_config(route_name='api.articles.status', renderer='json', permission='articles.modify')
@validate('status', StatusForm)
def status(request):
    """
    Changes an article status
    """
    translate = request.translate
    form = request.forms['status']

    article = get_article(request)
    if article is None:
        raise HTTPNotFound(detail=translate('Invalid article'))

    if form.errors:
        raise HTTPBadRequest(json=form.errors)

    # Update object
    article.from_dict(form.result)

    result = dict(
        url=request.path_qs,
        method=request.method,
        params=form.params,
        apiVersion='1.0',
        result=True,
        article=article.to_dict(context='modify'),
    )

    return result


@view_config(route_name='api.articles.search', renderer='json', permission='articles.search')
@paginate('articles', limit=10, sort='id', order='desc')
@validate('search', SearchForm, method='get')
def search(request):
    """
    Searches in articles
    """
    form = request.forms['search']
    pager = request.pagers['articles']

    if form.errors:
        raise HTTPBadRequest(json=form.errors)

    query = build_search_query(order=pager.order, sort=pager.sort, **form.result)
    pager.set_collection(query)

    result = dict(
        url=request.path_qs,
        method=request.method,
        params=form.params,
        apiVersion='1.0',
        result=True,
        articles=dict(
            items=[article.to_dict(context='search') for article in pager],
            pager=pager.to_dict(),
        )
    )

    return result


@view_config(route_name='api.articles.visual', renderer='json', permission='articles.visual')
def visual(request):
    """
    Gets an article
    """
    translate = request.translate

    article = get_article(request)
    if article is None:
        raise HTTPNotFound(detail=translate('Invalid article'))

    result = dict(
        url=request.path_qs,
        method=request.method,
        apiVersion='1.0',
        result=True,
        article=article.to_dict(context='visual'),
    )

    return result
