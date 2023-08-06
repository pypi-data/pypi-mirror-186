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

""" Pyramid-Helpers application """

from pyramid.config import Configurator
from pyramid.settings import asbool

from pyramid_helpers.resources import Root


# pylint: disable=unused-argument
def main(global_config, **settings):
    """
    This function returns a Pyramid WSGI application.
    """

    # Global config
    config = Configurator(
        root_factory=Root,
        settings=settings,
    )

    # Session setup
    config.include('pyramid_beaker')

    # Mako setup
    config.include('pyramid_mako')

    # Transaction manager
    config.include('pyramid_tm')

    # Model setup
    config.include('pyramid_helpers.models')

    # Pyramid Helpers
    includeme(config)

    #
    # Applicative routes
    #

    # Routes defined in views/__init__.py
    config.add_route('api-doc', '/api-doc')
    config.add_route('auth.sign-in', '/auth/sign-in')
    config.add_route('auth.sign-out', '/auth/sign-out')
    config.add_route('index', '/')
    config.add_route('i18n', '/i18n')
    config.add_route('predicates', '/predicates')
    config.add_route('predicates.enum', '/predicates/{predicate}', enum_predicate=dict(predicate=('value1', 'value2')))
    config.add_route('predicates.numeric-1', '/predicates/{predicate1}', numeric_predicate='predicate1')
    config.add_route('predicates.numeric-2', '/predicates/{predicate1}/{predicate2}', numeric_predicate=('predicate1', 'predicate2'))
    config.add_route('validators', '/validators')

    # Routes defined in views/articles.py
    config.add_route('articles.create', '/articles/create')
    config.add_route('articles.delete', '/articles/{article}/delete', numeric_predicate='article')
    config.add_route('articles.modify', '/articles/{article}/modify', numeric_predicate='article')
    config.add_route('articles.search', '/articles')
    config.add_route('articles.visual', '/articles/{article}', numeric_predicate='article')

    # Routes defined in views/api/articles.py
    config.add_route('api.articles.create', '/api/1.0/articles', request_method='POST')
    config.add_route('api.articles.delete', '/api/1.0/articles/{article}', numeric_predicate='article', request_method='DELETE')
    config.add_route('api.articles.modify', '/api/1.0/articles/{article}', numeric_predicate='article', request_method='PUT')
    config.add_route('api.articles.search', '/api/1.0/articles', request_method='GET')
    config.add_route('api.articles.status', '/api/1.0/articles/{article}/status', numeric_predicate='article', request_method='PUT')
    config.add_route('api.articles.visual', '/api/1.0/articles/{article}', numeric_predicate='article', request_method='GET')

    # Scan Pyramid-Helpers views modules
    config.scan('pyramid_helpers.views')

    # Create Pyramid WSGI app
    app = config.make_wsgi_app()

    return app


def includeme(config):
    """
    Set up standard configurator registrations. Use via:

    .. code-block:: python

    config = Configurator()
    config.include('pyramid_helpers')
    """

    registry = config.registry
    settings = registry.settings

    # Static route
    config.add_static_view('/_pyramid-helpers/static', 'pyramid_helpers:static')

    # Utils setup
    config.include('pyramid_helpers.utils')

    # LDAP configuration
    if asbool(settings.get('ldap.enabled')):
        config.include('pyramid_helpers.ldap')

    # RADIUS configuration
    if asbool(settings.get('radius.enabled')):
        config.include('pyramid_helpers.radius')

    # Authentication setup
    if asbool(settings.get('auth.enabled')):
        config.include('pyramid_helpers.auth')

    # Forms setup
    if asbool(settings.get('forms.enabled')):
        config.include('pyramid_helpers.forms')

    # I18n setup
    if asbool(settings.get('i18n.enabled')):
        config.include('pyramid_helpers.i18n')

    # Pagers setup
    if asbool(settings.get('pagers.enabled')):
        config.include('pyramid_helpers.paginate')

    # Custom predicates
    if asbool(settings.get('predicates.enabled')):
        config.include('pyramid_helpers.predicates')

    # CSV/JSON renderers
    config.include('pyramid_helpers.renderers')
