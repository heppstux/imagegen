#
# (C) 2015 by Stephan S. Hepper
#
# WIP is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# WIP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with WIP. If not, see <http://www.gnu.org/licenses/>.
#

from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^(((?P<width>\d+)(x(?P<height>\d+))?(/(?P<color>[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3}))?)(/(?P<background>[0-9A-Fa-f]{6}|[0-9A-Fa-f]{3}))?)(?P<fileFormat>(\.png|\.jpg|\.jpeg)?)$', 'imagegen.views.pngImage'),
)
