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
Authentication module for Pyramid-Helpers

Useful documentation can be found at:
 * https://docs.pylonsproject.org/projects/pyramid/en/latest/api/security.html
 * https://docs.pylonsproject.org/projects/pyramid-cookbook/en/latest/auth/index.html
"""

import hashlib
import logging

from beaker.util import NoneType

from pyramid.authentication import AuthTktCookieHelper
from pyramid.authentication import extract_http_basic_credentials
from pyramid.authorization import ACLHelper
from pyramid.authorization import Authenticated
from pyramid.authorization import Everyone

from pyramid_helpers.utils import ConfigurationError
from pyramid_helpers.utils import get_settings
from pyramid_helpers.utils import parse_settings
from pyramid_helpers.utils import request_cache
from pyramid_helpers.utils import resolve_dotted


BACKENDS = {}

SETTINGS_DEFAULTS = {
    'auth': {
        'backend': None,
        'policies': ['cookie', ],
        'get_principals': None,
        'get_user_by_username': None,
    },
    'policy:basic': {
        'realm': 'Pyramid-Helpers Application',
    },
    'policy:cookie': {
        'secret': 'the-big-secret-for-secured-authentication',
        'hashalg': 'sha512',
    },
    'policy:remote': {
        'fake_user': None,
        'header': None,
        'login_url': None,
        'logout_url': None,
    },
    'policy:token': {
        'header': 'X-PH-Authentication-Token',
        'query_param': None,
        'get_username_by_token': None,
    },
}

SETTINGS_RULES = {
    'auth': [
        ('enabled', (bool, NoneType), 'enabled must be a boolean or an integer'),
        ('backend', (str, NoneType), 'backend must be a string designating a valid backend'),
        ('policies', (list, NoneType), 'policies must be a comma separated list of policies'),
        ('get_principals', (str,), 'get_principals must be a string designating a valid callback'),
        ('get_user_by_username', (str,), 'get_user_by_username must be a string designating a valid callback'),
    ],
    'policy:basic': [
        ('realm', (str, NoneType), 'realm must be a string designating a realm authentication'),
    ],
    'policy:cookie': [
        ('secret', (str, NoneType), 'secret must be a string designating a secret'),
        ('hashalg', (str, NoneType), 'hashalg must be a string designating a valid hashalg'),
    ],
    'policy:remote': [
        ('fake_user', (str, NoneType), 'fake_user must be a string designating a username'),
        ('header', (str, NoneType), 'header must be a string designating a HTTP header'),
        ('login_url', (str, NoneType), 'login_url must be a string designating a valid url'),
        ('logout_url', (str, NoneType), 'logout_url must be a string designating a valid url'),
    ],
    'policy:token': [
        ('header', (str, NoneType), 'header must be a string designating a HTTP header'),
        ('query_param', (str, NoneType), 'query_param must be a string designating a query parameter'),
        ('get_username_by_token', (str, NoneType), 'get_username_by_token must be a string designating a valid callback'),
    ],
}


log = logging.getLogger(__name__)


class AuthenticationBackend:
    """ Authentication backend base class """

    __name__ = None

    def __enter__(self):
        """
        This method is called by the `with:` statement and should be overriden
        to execute some tasks **before** validating the password.
        """

        return self

    def __exit__(self, type_, value, traceback):
        """
        This method is called by the `with:` statement and should be overriden
        to execute some tasks **after** validating the password.
        """

    # pylint: disable=unused-argument
    def setup(self, *args, **kwargs):
        """ Register authentication backend """

        if self.__name__ is None:
            log.error('[AUTH] Attribute `.__name__` of AuthenticationBackend instance must be set')
            return False

        if self.__name__ in BACKENDS:
            log.error('[AUTH] An authentication backend is already registered for %s', self.__name__)
            return False

        # Registering object
        BACKENDS[self.__name__] = self

        log.info('[AUTH] Registered authentication backend, name=%s, class=%s', self.__name__, self.__class__.__name__)

        return True

    def validate_password(self, username, password, request):
        """ Please, override this method to implement the password validation """

        raise NotImplementedError()


class MultiSecurityPolicy:
    """
    A Pyramid security policy that implements the following protocols:
     * basic
     * cookie
     * remote
     * token
    """

    POLICIES = ['cookie', 'basic', 'remote', 'token']

    # pylint: disable=too-many-arguments, no-self-use
    def __init__(self, policies, hashalg='sha512', realm='Pyramid Helpers', secret=None):

        for policy in policies:
            if policy not in self.POLICIES:
                raise ConfigurationError(f'[AUTH] Invalid policy: {policy}')

        self.cookie = AuthTktCookieHelper(secret, hashalg=hashalg) if 'cookie' in policies else None
        self.policies = policies
        self.realm = realm

    def authenticated_userid(self, request):
        """ Get user id identifying the trusted and verified user, or None if unauthenticated """

        identity = request.identity
        if identity is None:
            return None

        return identity['userid']

    def forget(self, request):
        """ Get set of headers suitable for «forgetting» the current user on subsequent requests """

        if request.authentication_policy == 'basic':
            # Ask client to re-authenticate
            return [('WWW-Authenticate', f'Basic realm="{self.realm}"')]

        if self.cookie:
            # Delete cookie
            return self.cookie.forget(request)

        return []

    @request_cache()
    def identity(self, request):
        """ Get the identity of the current user """

        # Extract data
        credentials = extract_http_basic_credentials(request)
        policy = request.headers.get('X-PH-Authentication-Policy')
        remote_user = request.environ.get('REMOTE_USER')
        token = extract_token(request)

        # Guess and check policy
        if policy is None:
            if remote_user:
                policy = 'remote'

            elif credentials:
                policy = 'basic'

            elif token:
                policy = 'token'

            elif self.cookie:
                policy = 'cookie'

        if policy not in self.policies:
            policy = self.policies[0]

        # Store policy to request
        # Policy may be set by the fake user tween
        if getattr(request, 'authentication_policy', None) is None:
            request.authentication_policy = policy

        if policy == 'basic':
            if credentials and check_credentials(credentials.username, credentials.password, request):
                identity = dict(userid=credentials.username)
            else:
                identity = None

        elif policy == 'remote':
            if remote_user:
                identity = dict(userid=remote_user)
            else:
                identity = None

        elif policy == 'token':
            userid = get_username_by_token(token, request)
            if userid:
                identity = dict(userid=userid)
            else:
                identity = None

        else:
            # Cookie
            identity = self.cookie.identify(request)

        if identity is None:
            return None

        # Add principals
        principals = get_principals(identity['userid'], request)
        if principals is None:
            return None

        identity['principals'] = principals

        return identity

    def permits(self, request, context, permission):
        """
        Get an instance of `pyramid.security.Allowed` if a user of the given identity is allowed the permission in the current context,
        else return an instance of `pyramid.security.Denied`
        """

        identity = request.identity

        principals = set([Everyone])
        if identity is not None:
            principals.add(Authenticated)
            principals.add(identity['userid'])
            principals.update(identity['principals'])

        return ACLHelper().permits(context, principals, permission)

    def remember(self, request, username, **kw):
        """ Get set of headers suitable for «remembering« the user id """

        if request.authentication_policy != 'cookie':
            # Do nothing
            return []

        # Set cookie
        return self.cookie.remember(request, username, **kw)


def auth_fake_user_tween_factory(handler, registry):
    """
    Tween that adds a fake user to environ to simulate remote user based
    authentication.
    """

    settings = registry.settings
    username = settings['auth']['policy:remote']['fake_user']

    def auth_fake_user_tween(request):
        # Add fake user as REMOTE_USER if requested
        environ = request.environ
        environ['REMOTE_USER'] = username

        # Set the authentication policy
        request.authentication_policy = 'fake_user'

        return handler(request)

    return auth_fake_user_tween


def auth_header_user_tween_factory(handler, registry):
    """
    Tween that adds remote user from header
    This is useful when application is behind a proxy that handles authentication
    """

    settings = registry.settings
    header = settings['auth']['policy:remote']['header']

    def auth_header_user_tween(request):
        if header in request.headers:
            request.environ['REMOTE_USER'] = request.headers[header]

        return handler(request)

    return auth_header_user_tween


def check_credentials(username, password, request):
    """ Check extracted credential using configured backend """

    params = get_settings(request, 'auth', 'auth')

    backend_ = BACKENDS.get(params['backend'])
    if backend_ is None:
        # Invalid backend
        return False

    with backend_ as backend:
        return backend.validate_password(username, password, request)


def extract_token(request):
    """ Extract authentication token from request """

    params = get_settings(request, 'auth', 'policy:token')

    if params.get('query_param'):
        return request.GET.get(params['query_param'])

    if params.get('header'):
        return request.headers.get(params['header'])

    return None


def get_principals(username, request):
    """ Wrapper to get_principals function defined in settings """

    params = get_settings(request, 'auth', 'auth')
    func = params['get_principals']

    return func(username, request)


def get_user_by_username(username, request):
    """ Wrapper to get_user_by_username function defined in settings """

    params = get_settings(request, 'auth', 'auth')
    func = params['get_user_by_username']

    return func(username, request)


def get_username_by_token(token, request):
    """ Wrapper to get_username_by_token function defined in settings """

    params = get_settings(request, 'auth', 'policy:token')
    func = params['get_username_by_token']

    return func(token, request)


def on_before_renderer(event):
    """ Add authenticated_user and has_permission() to renderer context """

    request = event['request']

    event['authentication_policy'] = request.authentication_policy
    event['authenticated_user'] = request.authenticated_user
    event['has_permission'] = request.has_permission


def on_new_request(event):
    """ Add authenticated_user to request """

    request = event.request
    request.authenticated_user = get_user_by_username(request.authenticated_userid, request)

    if not hasattr(request, 'authentication_policy'):
        request.authentication_policy = None


def includeme(config):
    """
    Set up standard configurator registrations. Use via:

    .. code-block:: python

    config = Configurator()
    config.include('pyramid_helpers.auth')
    """

    config.add_subscriber(on_before_renderer, 'pyramid.events.BeforeRender')
    config.add_subscriber(on_new_request, 'pyramid.events.NewRequest')

    # Load an parse settings
    settings = get_settings(config, 'auth')
    if settings is None:
        raise ConfigurationError('[AUTH] Invalid or missing configuration for AUTH, please check auth.filepath directive')

    settings = parse_settings(settings, SETTINGS_RULES, defaults=SETTINGS_DEFAULTS)

    # Check policies
    if 'all' in settings['auth']['policies']:
        settings['auth']['policies'] = MultiSecurityPolicy.POLICIES[:]
    else:
        for policy in settings['auth']['policies']:
            if policy not in MultiSecurityPolicy.POLICIES:
                raise ConfigurationError(f'[AUTH] Invalid policy for parameters policies in section [auth]: {policy}')

    # Check backend
    if settings['auth']['backend'] is None:
        raise ConfigurationError('[AUTH] Missing value for parameter backend in section [auth]')

    if settings['auth']['backend'] not in BACKENDS:
        raise ConfigurationError(f'[AUTH] Invalid value for parameter backend in section [auth]: {settings["auth"]["backend"]}')

    # Check hashalg
    if settings['policy:cookie']['hashalg'] not in hashlib.algorithms_available:
        raise ConfigurationError(f'[AUTH] Invalid value for parameter hashalg in section [policy:cookie]: {settings["auth"]["policy:cookie"]["hashalg"]}')

    # Resolve get_principals
    func = resolve_dotted(settings['auth']['get_principals'])
    if func is None:
        raise ConfigurationError(f'[AUTH] Invalid value for parameter get_principals in section [auth]: {settings["auth"]["get_principals"]}')
    settings['auth']['get_principals'] = func

    # Resolve get_user_by_username
    func = resolve_dotted(settings['auth']['get_user_by_username'])
    if func is None:
        raise ConfigurationError(f'[AUTH] Invalid value for parameter get_user_by_username in section [auth]: {settings["auth"]["get_user_by_username"]}')
    settings['auth']['get_user_by_username'] = func

    # Resolve get_username_by_token if needed
    if 'token' in settings['auth']['policies']:
        func = resolve_dotted(settings['policy:token']['get_username_by_token'])
        if func is None:
            raise ConfigurationError(f'[AUTH] Invalid value for parameter get_username_by_token in section [policy:token]: {settings["policy:token"]["get_username_by_token"]}')
        settings['policy:token']['get_username_by_token'] = func

    # Add fake user tween if needed
    if 'remote' in settings['auth']['policies']:
        if settings['policy:remote']['fake_user'] is not None:
            log.warning(
                '[AUTH] POLICY `remote` IS ENABLED WITH `fake_user` SET TO `%s`, USER `%s` WILL BE AUTOMATICALLY CONNECTED WITHOUT ANY AUTHENTICATION, THIS IS VERY DANGEROUS !!!',
                settings['policy:remote']['fake_user'],
                settings['policy:remote']['fake_user']
            )
            config.add_tween('pyramid_helpers.auth.auth_fake_user_tween_factory')

        if settings['policy:remote']['header'] is not None:
            log.warning(
                '[AUTH] POLICY `remote` IS ENABLED WITH `header` SET TO `%s`, UNLESS THE APPLICATION IS BEHIND A PROXY THAT MANAGES THIS HEADER, THIS IS VERY DANGEROUS !!!',
                settings['policy:remote']['header']
            )
            config.add_tween('pyramid_helpers.auth.auth_header_user_tween_factory')

    # Set security policy
    config.set_security_policy(MultiSecurityPolicy(
        settings['auth']['policies'],
        hashalg=settings['policy:cookie']['hashalg'],
        realm=settings['policy:basic']['realm'],
        secret=settings['policy:cookie']['secret'],
    ))

    log.info('[AUTH] Initialization complete: policies=%s, backend=%s', settings['auth']['policies'], settings['auth']['backend'])
