# Copyright 2011 OpenStack Foundation
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
# @author Jaume Devesa, devvesa@gmail.com, Midokura SARL
from __future__ import print_function

import argparse
import logging

from neutronclient.common import utils
from neutronclient.neutron import v2_0 as neutronV20
from neutronclient.neutron.v2_0 import network
from neutronclient.openstack.common.gettextutils import _


class AddNetworkToRoutingInstance(neutronV20.NeutronCommand):
    """Associate a network to a routing instance."""
    log = logging.getLogger(__name__ + '.AddNetworkToRoutingInstance')

    def get_parser(self, prog_name):
        parser = super(AddNetworkToRoutingInstance, self).get_parser(prog_name)
        parser.add_argument(
            'routinginstance',
            help=_('ID of the Routing Instance.'))
        parser.add_argument(
            'network',
            help=_('Network to add.'))
        return parser

    def run(self, parsed_args):
        self.log.debug('run(%s)' % parsed_args)
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        _net_id = neutronV20.find_resourceid_by_name_or_id(
            neutron_client, 'network', parsed_args.network)
        neutron_client.add_network_to_routinginstance(
            parsed_args.routinginstance, {'network_id': _net_id})
        print(_('Added network %s to routing instance') % parsed_args.network,
              file=self.app.stdout)


class RemoveNetworkFromRoutingInstance(neutronV20.NeutronCommand):
    """Disassociate a network from a routing instance."""
    log = logging.getLogger(__name__ + '.RemoveNetworkFromRoutingInstance')

    def get_parser(self, prog_name):
        parser = super(RemoveNetworkFromRoutingInstance,
                       self).get_parser(prog_name)
        parser.add_argument(
            'routinginstance',
            help=_('ID of the routing instance.'))
        parser.add_argument(
            'network',
            help=_('Network to remove.'))
        return parser

    def run(self, parsed_args):
        self.log.debug('run(%s)' % parsed_args)
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        _net_id = neutronV20.find_resourceid_by_name_or_id(
            neutron_client, 'network', parsed_args.network)
        neutron_client.remove_network_from_routinginstance(
            parsed_args.routinginstance, _net_id)
        print(_('Removed network %s from '
                'routing instance') % parsed_args.network,
              file=self.app.stdout)


class ListNetworksInRoutingInstance(network.ListNetwork):
    """List the network associated to a network instance."""
    log = logging.getLogger(__name__ + '.ListNetworksInRoutingInstance')
    list_columns = ['id', 'name', 'subnets']

    def get_parser(self, prog_name):
        parser = super(ListNetworksInRoutingInstance,
                       self).get_parser(prog_name)
        parser.add_argument(
            'routinginstance',
            help=_('ID of the Routing Instance to query.'))
        return parser

    def call_server(self, neutron_client, search_opts, parsed_args):
        data = neutron_client.list_networks_on_routinginstance(
            parsed_args.routinginstance, **search_opts)
        return data


class AddAgentToRoutingInstance(neutronV20.NeutronCommand):
    """Associate an agent to a routing instance."""
    log = logging.getLogger(__name__ + '.AddAgentToRoutingInstance')

    def get_parser(self, prog_name):
        parser = super(AddAgentToRoutingInstance, self).get_parser(prog_name)
        parser.add_argument(
            'routinginstance',
            help=_('ID of the Routing Instance.'))
        parser.add_argument(
            'agent',
            help=_('Agent to add.'))
        return parser

    def run(self, parsed_args):
        self.log.debug('run(%s)' % parsed_args)
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        neutron_client.add_agent_to_routinginstance(
            parsed_args.routinginstance, {'agent_id': parsed_args.agent})
        print(_('Added agent %s to routing instance') % parsed_args.agent,
              file=self.app.stdout)


class RemoveAgentFromRoutingInstance(neutronV20.NeutronCommand):
    """Disassociate an agent from a routing agent."""
    log = logging.getLogger(__name__ + '.RemoveAgentFromRoutingInstance')

    def get_parser(self, prog_name):
        parser = super(RemoveAgentFromRoutingInstance,
                       self).get_parser(prog_name)
        parser.add_argument(
            'routinginstance',
            help=_('ID of the routing instance.'))
        parser.add_argument(
            'agent',
            help=_('Agent to remove.'))
        return parser

    def run(self, parsed_args):
        self.log.debug('run(%s)' % parsed_args)
        neutron_client = self.get_client()
        neutron_client.format = parsed_args.request_format
        neutron_client.remove_agent_from_routinginstance(
            parsed_args.routinginstance, parsed_args.agent)
        print(_('Removed agent %s from '
                'routing instance') % parsed_args.agent,
              file=self.app.stdout)


class ListAgentsInRoutingInstance(neutronV20.ListCommand):
    """List agents associated to a routing instance."""

    resource = 'agent'
    _formatters = {}
    log = logging.getLogger(__name__ + '.ListAgentsInRoutingInstance')
    list_columns = ['id', 'host', 'admin_state_up', 'alive']
    unknown_parts_flag = False

    def get_parser(self, prog_name):
        parser = super(ListAgentsInRoutingInstance,
                       self).get_parser(prog_name)
        parser.add_argument('routinginstance',
                            help=_('RoutingInstance to query.'))
        return parser

    def extend_list(self, data, parsed_args):
        for agent in data:
            agent['alive'] = ":-)" if agent['alive'] else 'xxx'

    def call_server(self, neutron_client, search_opts, parsed_args):
        data = neutron_client.list_agents_on_routinginstance(
            parsed_args.routinginstance, **search_opts)
        return data


class CreateRoutingInstance(neutronV20.CreateCommand):
    """Create a Routing Instance."""

    resource = 'routinginstance'
    log = logging.getLogger(__name__ + '.CreateRoutingInstance')

    def add_known_arguments(self, parser):
        parser.add_argument(
            '--nexthop',
            default='',
            help=argparse.SUPPRESS)
        parser.add_argument(
            '--advertise', dest='advertise',
            action='store_true',
            help=_('Advertise routes.'))
        parser.add_argument(
            '--discover', dest='discover',
            action='store_true',
            help=_('Discovery routes.'))

    def args2body(self, parsed_args):
        body_dict = {'advertise': parsed_args.advertise,
                     'discover': parsed_args.discover}
        if parsed_args.nexthop:
            body_dict['nexthop'] = parsed_args.nexthop
        body = {self.resource: body_dict}
        if parsed_args.tenant_id:
            body[self.resource].update({'tenant_id': parsed_args.tenant_id})
        return body


class DeleteRoutingInstance(neutronV20.DeleteCommand):
    """Delete a routing peer."""
    log = logging.getLogger(__name__ + '.DeleteRoutingInstance')
    resource = 'routinginstance'
    allow_names = False


class ListRoutingInstances(neutronV20.ListCommand):
    """List Routing Instances."""
    resource = 'routinginstance'
    log = logging.getLogger(__name__ + '.ListRoutingInstances')
    list_columns = ['id', 'tenant-id', 'nexthop', 'advertise',
                    'discover', 'networks', 'agents']
    sorting_support = True


class UpdateRoutingInstance(neutronV20.UpdateCommand):
    """Update network's information."""
    log = logging.getLogger(__name__ + '.UpdateRoutingInstance')
    resource = 'routinginstance'
    allow_names = False


class ShowRoutingInstance(neutronV20.ShowCommand):
    """Show information about a given Routing Instance."""
    resource = 'routinginstance'
    log = logging.getLogger(__name__ + '.ShowRoutingInstance')
    allow_names = False


class CreateRoutingPeer(neutronV20.CreateCommand):
    """Create a Routing Peer."""

    resource = 'routingpeer'
    log = logging.getLogger(__name__ + '.CreateRoutingPeer')

    def add_known_arguments(self, parser):
        parser.add_argument(
            'peer',
            help=_('Peer address.'))
        parser.add_argument(
            '--remote-as', type=int,
            required=True,
            help=_('BGP remote-as value')),
        parser.add_argument(
            '--password',
            help=_('Connection password to remote peer'))
        parser.add_argument(
            '--extra-config', type=utils.str2dict,
            help=_('Configuration of the peer.'))

    def args2body(self, parsed_args):
        body = {self.resource: {
                'peer': parsed_args.peer,
                'remote_as': parsed_args.remote_as,
                'password': parsed_args.password,
                'extra_config': parsed_args.extra_config or {}}}
        if parsed_args.tenant_id:
            body[self.resource].update({'tenant_id': parsed_args.tenant_id})
        return body
        return body


class UpdateRoutingPeer(neutronV20.UpdateCommand):
    """Update network's information."""
    log = logging.getLogger(__name__ + '.UpdateRoutingPeer')
    resource = 'routingpeer'


class DeleteRoutingPeer(neutronV20.DeleteCommand):
    """Delete a routing peer."""
    log = logging.getLogger(__name__ + '.DeleteRoutingPeer')
    resource = 'routingpeer'
    allow_names = False


class ListRoutingPeers(neutronV20.ListCommand):
    """List Routing Peers."""
    resource = 'routingpeer'
    log = logging.getLogger(__name__ + '.ListRoutingPeers')
    list_columns = ['id', 'peer', 'protocol', 'configuration']
    sorting_support = True


class ShowRoutingPeer(neutronV20.ShowCommand):
    """Show information about a given Routing Peer."""
    resource = 'routingpeer'
    log = logging.getLogger(__name__ + '.ShowRoutingPeer')
