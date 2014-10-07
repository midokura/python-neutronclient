# Copyright 2014 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.openstack.common.gettextutils import _


class ListTunnelZone(neutronV20.ListCommand):

    resource = 'tunnelzone'


class ShowTunnelZone(neutronV20.ShowCommand):

    resource = 'tunnelzone'


class CreateTunnelZone(neutronV20.CreateCommand):

    resource = 'tunnelzone'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'name', metavar='NAME',
            help=_('Name of the tunnelzone.'))
        parser.add_argument(
            '--type', dest='type',
            help=_('Tunnel type'))

    def args2body(self, parsed_args):
        body = {'tunnelzone': {
            'name': parsed_args.name}}
        if parsed_args.type:
            body[self.resource].update({'type': parsed_args.type})
        if parsed_args.tenant_id:
            body[self.resource].update({'tenant_id': parsed_args.tenant_id})
        return body


class UpdateTunnelZone(neutronV20.UpdateCommand):

    resource = 'tunnelzone'


class DeleteTunnelZone(neutronV20.DeleteCommand):

    resource = 'tunnelzone'


class ListTunnelZoneHost(neutronV20.ListCommand):

    resource = 'tunnelzonehost'


class ShowTunnelZoneHost(neutronV20.ShowCommand):

    resource = 'tunnelzonehost'


class CreateTunnelZoneHost(neutronV20.CreateCommand):

    resource = 'tunnelzonehost'

    def add_known_arguments(self, parser):
        parser.add_argument(
            'host_id', metavar='HOST_ID',
            help=_('Identifier of the host.'))
        parser.add_argument(
            'ip_address', metavar='IP_ADDRESS',
            help=_('IP address of the tunnel zone'))

    def args2body(self, parsed_args):
        body = {'tunnelzonehost': {
            'host_id': parsed_args.host_id,
            'ip_address': parsed_args.ip_address}}
        if parsed_args.tenant_id:
            body[self.resource].update({'tenant_id': parsed_args.tenant_id})
        return body


class UpdateTunnelZoneHost(neutronV20.UpdateCommand):

    resource = 'tunnelzonehost'


class DeleteTunnelZoneHost(neutronV20.DeleteCommand):

    resource = 'tunnelzonehost'
