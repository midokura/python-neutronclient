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

from neutronclient.neutron.v2_0.midonet import tunnelzone

COMMANDS_MIDONET = {
    'tunnelzone-list': tunnelzone.ListTunnelZone,
    'tunnelzone-show': tunnelzone.ShowTunnelZone,
    'tunnelzone-create': tunnelzone.CreateTunnelZone,
    'tunnelzone-update': tunnelzone.UpdateTunnelZone,
    'tunnelzone-delete': tunnelzone.DeleteTunnelZone,
    'tunnelzone-host-list': tunnelzone.ListTunnelZoneHost,
    'tunnelzone-host-show': tunnelzone.ShowTunnelZoneHost,
    'tunnelzone-host-create': tunnelzone.CreateTunnelZoneHost,
    'tunnelzone-host-update': tunnelzone.UpdateTunnelZoneHost,
    'tunnelzone-host-delete': tunnelzone.DeleteTunnelZoneHost
}
