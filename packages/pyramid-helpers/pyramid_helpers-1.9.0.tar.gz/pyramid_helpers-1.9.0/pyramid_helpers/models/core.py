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

""" Pyramid-Helpers core models """

import datetime
import logging

from passlib.context import CryptContext
from passlib.handlers.ldap_digests import ldap_crypt_schemes

from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.schema import Table
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import DateTime
from sqlalchemy.types import Enum
from sqlalchemy.types import Integer
from sqlalchemy.types import Text
from sqlalchemy.types import Unicode

from pyramid_helpers.auth import AuthenticationBackend
from pyramid_helpers.models import Base
from pyramid_helpers.models import DBSession


log = logging.getLogger(__name__)


# Users <-> Groups
user_groups_associations = Table(
    'user_groups_associations',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('group_id', Integer, ForeignKey('groups.id')),
)


class DatabaseAuthenticationBackend(AuthenticationBackend):
    """ Authentication backend for database """

    # pylint: disable=too-few-public-methods

    __name__ = 'database'

    # pylint: disable=no-self-use,unused-argument
    def validate_password(self, username, password, request):
        """ Validate password """

        user = get_user_by_username(username, request)
        if user is None:
            return False

        return user.validate_password(password)


class Group(Base):
    """ ORM class mapped to groups table """

    __tablename__ = 'groups'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Attributes
    creation_date = Column(DateTime, nullable=False)
    description = Column(Text)
    modification_date = Column(DateTime, nullable=False)
    name = Column(Unicode(255), unique=True)

    def from_dict(self, data):
        """ Load data from dict """

        utcnow = datetime.datetime.utcnow()

        if 'description' in data:
            self.description = data['description']

        if 'name' in data:
            self.name = data['name']

        if self.creation_date is None:
            self.creation_date = data.get('creation_date') or utcnow

        if data.get('modification_date'):
            self.modification_date = data['modification_date']

        elif DBSession.is_modified(self):
            self.modification_date = utcnow

        return DBSession.is_modified(self)

    def to_dict(self, context=None):
        """ Dump data to dict """

        data = dict(
            description=self.description,
            name=self.name,
        )

        if context in ('brief', 'search'):
            return data

        data.update(dict(
            creation_date=self.creation_date,
            modification_date=self.modification_date,
        ))

        return data


class User(Base):
    """ ORM class mapped to users table """

    # pylint: disable=too-many-instance-attributes

    __tablename__ = 'users'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Attributes
    creation_date = Column(DateTime, nullable=False)
    firstname = Column(Unicode(255))
    lastname = Column(Unicode(255))
    modification_date = Column(DateTime, nullable=False)
    password = Column(Unicode(32))
    status = Column(Enum('active', 'disabled'))
    timezone = Column(Unicode(255))
    token = Column(Unicode(255))
    username = Column(Unicode(255), unique=True, nullable=False)

    # Relations
    groups = relationship('Group', secondary=user_groups_associations)

    @property
    def fullname(self):
        """ Compute fullname from firstname, lastname or username """

        fullname = []
        if self.firstname:
            fullname.append(self.firstname)
        if self.lastname:
            fullname.append(self.lastname)
        if not fullname:
            fullname.append(self.username)
        return ' '.join(fullname)

    def from_dict(self, data):
        """ Load data from dict """

        utcnow = datetime.datetime.utcnow()

        if 'firstname' in data:
            self.firstname = data['firstname']

        if 'lastname' in data:
            self.lastname = data['lastname']

        if 'password' in data and not self.validate_password(data['password']):
            self.set_password(data['password'])

        if 'groups' in data:
            self.groups = data['groups']

        if 'status' in data:
            self.status = data['status']

        if 'timezone' in data:
            self.timezone = data['timezone']

        if 'token' in data:
            self.token = data['token']

        if 'username' in data:
            self.username = data['username']

        if self.creation_date is None:
            self.creation_date = data.get('creation_date') or utcnow

        if data.get('modification_date'):
            self.modification_date = data['modification_date']

        elif DBSession.is_modified(self):
            self.modification_date = utcnow

        return DBSession.is_modified(self)

    def to_dict(self, context=None):
        """ Dump data to dict """

        data = dict(
            id=self.id,
            fullname=self.fullname,
            status=self.status,
        )

        if context in ('brief', 'search'):
            return data

        if context:
            data['groups'] = [group.to_dict(context='brief') for group in self.groups]
        else:
            data['groups'] = self.groups

        data.update(dict(
            firstname=self.firstname,
            lastname=self.lastname,
            timezone=self.timezone,
            token=self.token,
            username=self.username,
        ))

        return data

    def set_password(self, password, scheme='ldap_sha512_crypt'):
        """ Hash and set password """

        if password is None:
            self.password = None
            return

        if self.validate_password(password):
            # Same password
            return

        ctx = CryptContext(default=scheme, schemes=ldap_crypt_schemes)
        self.password = ctx.hash(password)

    def validate_password(self, password):
        """ Validate password """

        if self.status != 'active':
            return False

        if self.password is None:
            return False

        # Verify password
        ctx = CryptContext(schemes=ldap_crypt_schemes)
        try:
            validated = ctx.verify(password, self.password)
        except ValueError:
            log.exception('Failed to verify password using CryptContext.verify() for user #%s', self.id)
            validated = False

        return validated


# pylint: disable=unused-argument
def get_principals(username, request):
    """ Get principals for user """

    user = get_user_by_username(username, request)
    if user is None:
        # Invalid user
        return None

    return [
        f'group:{group.name}'
        for group in user.groups
    ]


# pylint: disable=unused-argument
def get_user_by_username(username, request):
    """ Get user from database by username """

    if username is None:
        return None

    user = DBSession.query(User).filter_by(username=username).first()
    if user is None:
        log.warning('Failed to get user with username=%s', username)

    return user


# pylint: disable=unused-argument
def get_username_by_token(token, request):
    """ Get user from database by token """

    if token is None:
        return None

    user = DBSession.query(User).filter_by(token=token).first()
    if user is None:
        log.warning('Failed to get user with token=%s', token)
        return None

    return user.username
