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

""" Custom predicates for Pyramid """


class EnumPredicate:
    """
    The route defined by:

    config.add_route('route-name', '/foo/{kind}/bar', enum_predicate=dict(kind=('one', 'two')))

    Will only match the following urls:
     * /foo/one/bar
     * /foo/two/bar
    """

    # pylint: disable=unused-argument
    def __init__(self, params, config):
        self.names = list(params)
        self.params = params

    def __call__(self, context, request):
        matchdict = context['match']
        for name, values in self.params.items():
            if matchdict.get(name) not in values:
                return False
        return True

    def text(self):
        """ Predicate identifier """
        return str(self.params)

    phash = text


class NumericPredicate:
    """
    The route defined by:

    config.add_route('route-name', '/foo/{id}/bar', numeric_predicate='id')

    Will only match the following urls:
     * /foo/[0-9]+/bar
    """

    # pylint: disable=unused-argument
    def __init__(self, names, config):
        if isinstance(names, str):
            self.names = (names, )
        else:
            self.names = names

    def __call__(self, context, request):
        matchdict = context['match']
        for name in self.names:
            if not matchdict.get(name).isnumeric():
                return False
        return True

    def text(self):
        """ Predicate identifier """
        return str(self.names)

    phash = text


def includeme(config):
    """
    Set up standard configurator registrations. Use via:

    .. code-block:: python

    config = Configurator()
    config.include('pyramid_helpers.predicates')
    """

    config.add_route_predicate('enum_predicate', EnumPredicate)
    config.add_route_predicate('numeric_predicate', NumericPredicate)
