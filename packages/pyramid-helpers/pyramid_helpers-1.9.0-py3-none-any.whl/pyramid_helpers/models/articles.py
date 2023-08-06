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

""" Pyramid-Helpers articles models """

import datetime

from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.types import DateTime
from sqlalchemy.types import Enum
from sqlalchemy.types import Integer
from sqlalchemy.types import Text
from sqlalchemy.types import Unicode

from pyramid_helpers.models import Base
from pyramid_helpers.models import DBSession


class Article(Base):
    """ ORM class mapped to articles table """

    __tablename__ = 'articles'

    # Primary key
    id = Column(Integer, primary_key=True)

    # Foreign key
    author_id = Column(Integer, ForeignKey('users.id'))

    # Attributes
    creation_date = Column(DateTime, nullable=False)
    modification_date = Column(DateTime, nullable=False)
    title = Column(Unicode(255), unique=True, nullable=False)
    text = Column(Text)
    status = Column(Enum('draft', 'published', 'refused'))

    # Relations
    author = relationship('User', backref='articles')

    def from_dict(self, data):
        """ Load data from dict """

        utcnow = datetime.datetime.utcnow()

        if 'author' in data:
            self.author = data['author']

        if 'status' in data:
            self.status = data['status']

        if 'text' in data:
            self.text = data['text']

        if 'title' in data:
            self.title = data['title']

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
            title=self.title,
            status=self.status,
        )

        if context == 'brief':
            return data

        if context:
            data['author'] = self.author.to_dict(context='brief')
        else:
            data['author'] = self.author

        data.update(dict(
            creation_date=self.creation_date,
            modification_date=self.modification_date,
            text=self.text,
        ))

        return data
