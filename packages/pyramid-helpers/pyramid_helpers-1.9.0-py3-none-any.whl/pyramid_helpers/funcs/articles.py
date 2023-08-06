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

""" Pyramid-Helpers functions for articles management """

import sqlalchemy as sa

from pyramid_helpers.models import DBSession
from pyramid_helpers.models.articles import Article


def build_search_query(sort='id', order='asc', **criteria):
    """ Build a search query from criteria """

    query = DBSession.query(Article)

    # Filters
    if criteria.get('excluded_ids'):
        query = query.filter(~Article.id.in_(criteria['excluded_ids']))

    if criteria.get('selected_ids'):
        query = query.filter(Article.id.in_(criteria['selected_ids']))

    if criteria.get('term'):
        if criteria.get('exact') is True:
            query = query.filter(Article.title == criteria['term'])
        else:
            query = query.filter(
                Article.title.ilike('%{0}%'.format(criteria['term'].replace(' ', '%'))),
            )

    if criteria.get('title'):
        query = query.filter(
            Article.title.ilike('%{0}%'.format(criteria['title'].replace(' ', '%'))),
        )

    if criteria.get('text'):
        query = query.filter(
            Article.text.ilike('%{0}%'.format(criteria['text'].replace(' ', '%'))),
        )

    if criteria.get('status'):
        query = query.filter(Article.status == criteria['status'])

    # Order
    if sort == 'id':
        order_by = [Article.id]
    elif sort == 'creation_date':
        order_by = [Article.creation_date]
    elif sort == 'modification_date':
        order_by = [Article.modification_date]
    elif sort == 'title':
        order_by = [Article.title]
    elif sort == 'status':
        order_by = [Article.status]

    sa_func = sa.asc if order == 'asc' else sa.desc
    query = query.order_by(*[sa_func(column) for column in order_by])

    return query


def create_or_modify(request, form, article=None):
    """ Create or modify function """

    translate = request.translate

    if form.errors:
        return None

    # Check title unicity
    same_title = DBSession.query(Article).filter_by(title=form.result['title']).first()
    if same_title and same_title != article:
        form.errors['title'] = translate('Title already used in another article')
        return None

    # Do the job
    if article is None:
        article = Article()
        DBSession.add(article)

    # Set author
    form.result['author'] = request.authenticated_user

    # Update object
    article.from_dict(form.result)

    # Flushing the session to get new id
    DBSession.flush()

    return article


def get_article(request):
    """ Extract article id from query and return corresponding database object """

    article_id = request.matchdict.get('article')
    if article_id is None:
        return None

    return DBSession.get(Article, article_id)
