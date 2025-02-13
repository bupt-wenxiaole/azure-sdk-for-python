# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from ._models_py3 import CloudErrorBody
from ._models_py3 import DnsForwardingRuleset
from ._models_py3 import DnsForwardingRulesetListResult
from ._models_py3 import DnsForwardingRulesetPatch
from ._models_py3 import DnsResolver
from ._models_py3 import DnsResolverListResult
from ._models_py3 import DnsResolverPatch
from ._models_py3 import ForwardingRule
from ._models_py3 import ForwardingRuleListResult
from ._models_py3 import ForwardingRulePatch
from ._models_py3 import InboundEndpoint
from ._models_py3 import InboundEndpointListResult
from ._models_py3 import InboundEndpointPatch
from ._models_py3 import IpConfiguration
from ._models_py3 import OutboundEndpoint
from ._models_py3 import OutboundEndpointListResult
from ._models_py3 import OutboundEndpointPatch
from ._models_py3 import ProxyResource
from ._models_py3 import Resource
from ._models_py3 import SubResource
from ._models_py3 import SubResourceListResult
from ._models_py3 import SystemData
from ._models_py3 import TargetDnsServer
from ._models_py3 import TrackedResource
from ._models_py3 import VirtualNetworkDnsForwardingRuleset
from ._models_py3 import VirtualNetworkDnsForwardingRulesetListResult
from ._models_py3 import VirtualNetworkLink
from ._models_py3 import VirtualNetworkLinkListResult
from ._models_py3 import VirtualNetworkLinkPatch

from ._dns_resolver_management_client_enums import CreatedByType
from ._dns_resolver_management_client_enums import DnsResolverState
from ._dns_resolver_management_client_enums import ForwardingRuleState
from ._dns_resolver_management_client_enums import IpAllocationMethod
from ._dns_resolver_management_client_enums import ProvisioningState
from ._patch import __all__ as _patch_all
from ._patch import *  # type: ignore # pylint: disable=unused-wildcard-import
from ._patch import patch_sdk as _patch_sdk

__all__ = [
    "CloudErrorBody",
    "DnsForwardingRuleset",
    "DnsForwardingRulesetListResult",
    "DnsForwardingRulesetPatch",
    "DnsResolver",
    "DnsResolverListResult",
    "DnsResolverPatch",
    "ForwardingRule",
    "ForwardingRuleListResult",
    "ForwardingRulePatch",
    "InboundEndpoint",
    "InboundEndpointListResult",
    "InboundEndpointPatch",
    "IpConfiguration",
    "OutboundEndpoint",
    "OutboundEndpointListResult",
    "OutboundEndpointPatch",
    "ProxyResource",
    "Resource",
    "SubResource",
    "SubResourceListResult",
    "SystemData",
    "TargetDnsServer",
    "TrackedResource",
    "VirtualNetworkDnsForwardingRuleset",
    "VirtualNetworkDnsForwardingRulesetListResult",
    "VirtualNetworkLink",
    "VirtualNetworkLinkListResult",
    "VirtualNetworkLinkPatch",
    "CreatedByType",
    "DnsResolverState",
    "ForwardingRuleState",
    "IpAllocationMethod",
    "ProvisioningState",
]
__all__.extend([p for p in _patch_all if p not in __all__])
_patch_sdk()
