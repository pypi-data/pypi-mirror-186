"""
Type annotations for groundstation service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_groundstation/type_defs/)

Usage::

    ```python
    from mypy_boto3_groundstation.type_defs import AntennaDemodDecodeDetailsTypeDef

    data: AntennaDemodDecodeDetailsTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    AngleUnitsType,
    BandwidthUnitsType,
    ConfigCapabilityTypeType,
    ContactStatusType,
    CriticalityType,
    EndpointStatusType,
    EphemerisInvalidReasonType,
    EphemerisSourceType,
    EphemerisStatusType,
    FrequencyUnitsType,
    PolarizationType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AntennaDemodDecodeDetailsTypeDef",
    "DecodeConfigTypeDef",
    "DemodulationConfigTypeDef",
    "EirpTypeDef",
    "CancelContactRequestRequestTypeDef",
    "S3RecordingDetailsTypeDef",
    "ResponseMetadataTypeDef",
    "ConfigListItemTypeDef",
    "DataflowEndpointConfigTypeDef",
    "S3RecordingConfigTypeDef",
    "TrackingConfigTypeDef",
    "UplinkEchoConfigTypeDef",
    "ElevationTypeDef",
    "CreateMissionProfileRequestRequestTypeDef",
    "DataflowEndpointListItemTypeDef",
    "SocketAddressTypeDef",
    "DeleteConfigRequestRequestTypeDef",
    "DeleteDataflowEndpointGroupRequestRequestTypeDef",
    "DeleteEphemerisRequestRequestTypeDef",
    "DeleteMissionProfileRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeContactRequestRequestTypeDef",
    "DescribeEphemerisRequestRequestTypeDef",
    "SecurityDetailsTypeDef",
    "S3ObjectTypeDef",
    "EphemerisMetaDataTypeDef",
    "FrequencyBandwidthTypeDef",
    "FrequencyTypeDef",
    "GetConfigRequestRequestTypeDef",
    "GetDataflowEndpointGroupRequestRequestTypeDef",
    "GetMinuteUsageRequestRequestTypeDef",
    "GetMissionProfileRequestRequestTypeDef",
    "GetSatelliteRequestRequestTypeDef",
    "GroundStationDataTypeDef",
    "PaginatorConfigTypeDef",
    "ListConfigsRequestRequestTypeDef",
    "ListContactsRequestRequestTypeDef",
    "ListDataflowEndpointGroupsRequestRequestTypeDef",
    "ListEphemeridesRequestRequestTypeDef",
    "ListGroundStationsRequestRequestTypeDef",
    "ListMissionProfilesRequestRequestTypeDef",
    "MissionProfileListItemTypeDef",
    "ListSatellitesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "ReserveContactRequestRequestTypeDef",
    "TimeRangeTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateEphemerisRequestRequestTypeDef",
    "UpdateMissionProfileRequestRequestTypeDef",
    "ConfigIdResponseTypeDef",
    "ContactIdResponseTypeDef",
    "DataflowEndpointGroupIdResponseTypeDef",
    "EphemerisIdResponseTypeDef",
    "GetMinuteUsageResponseTypeDef",
    "GetMissionProfileResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MissionProfileIdResponseTypeDef",
    "ListConfigsResponseTypeDef",
    "ContactDataTypeDef",
    "ListDataflowEndpointGroupsResponseTypeDef",
    "DataflowEndpointTypeDef",
    "DescribeContactRequestContactScheduledWaitTypeDef",
    "EphemerisDescriptionTypeDef",
    "EphemerisItemTypeDef",
    "OEMEphemerisTypeDef",
    "GetSatelliteResponseTypeDef",
    "SatelliteListItemTypeDef",
    "SpectrumConfigTypeDef",
    "UplinkSpectrumConfigTypeDef",
    "ListGroundStationsResponseTypeDef",
    "ListConfigsRequestListConfigsPaginateTypeDef",
    "ListContactsRequestListContactsPaginateTypeDef",
    "ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef",
    "ListEphemeridesRequestListEphemeridesPaginateTypeDef",
    "ListGroundStationsRequestListGroundStationsPaginateTypeDef",
    "ListMissionProfilesRequestListMissionProfilesPaginateTypeDef",
    "ListSatellitesRequestListSatellitesPaginateTypeDef",
    "ListMissionProfilesResponseTypeDef",
    "TLEDataTypeDef",
    "ListContactsResponseTypeDef",
    "EndpointDetailsTypeDef",
    "EphemerisTypeDescriptionTypeDef",
    "ListEphemeridesResponseTypeDef",
    "ListSatellitesResponseTypeDef",
    "AntennaDownlinkConfigTypeDef",
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    "AntennaUplinkConfigTypeDef",
    "TLEEphemerisTypeDef",
    "ConfigDetailsTypeDef",
    "CreateDataflowEndpointGroupRequestRequestTypeDef",
    "GetDataflowEndpointGroupResponseTypeDef",
    "DescribeEphemerisResponseTypeDef",
    "ConfigTypeDataTypeDef",
    "EphemerisDataTypeDef",
    "DestinationTypeDef",
    "SourceTypeDef",
    "CreateConfigRequestRequestTypeDef",
    "GetConfigResponseTypeDef",
    "UpdateConfigRequestRequestTypeDef",
    "CreateEphemerisRequestRequestTypeDef",
    "DataflowDetailTypeDef",
    "DescribeContactResponseTypeDef",
)

AntennaDemodDecodeDetailsTypeDef = TypedDict(
    "AntennaDemodDecodeDetailsTypeDef",
    {
        "outputNode": str,
    },
    total=False,
)

DecodeConfigTypeDef = TypedDict(
    "DecodeConfigTypeDef",
    {
        "unvalidatedJSON": str,
    },
)

DemodulationConfigTypeDef = TypedDict(
    "DemodulationConfigTypeDef",
    {
        "unvalidatedJSON": str,
    },
)

EirpTypeDef = TypedDict(
    "EirpTypeDef",
    {
        "units": Literal["dBW"],
        "value": float,
    },
)

CancelContactRequestRequestTypeDef = TypedDict(
    "CancelContactRequestRequestTypeDef",
    {
        "contactId": str,
    },
)

S3RecordingDetailsTypeDef = TypedDict(
    "S3RecordingDetailsTypeDef",
    {
        "bucketArn": str,
        "keyTemplate": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

ConfigListItemTypeDef = TypedDict(
    "ConfigListItemTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
    },
    total=False,
)

_RequiredDataflowEndpointConfigTypeDef = TypedDict(
    "_RequiredDataflowEndpointConfigTypeDef",
    {
        "dataflowEndpointName": str,
    },
)
_OptionalDataflowEndpointConfigTypeDef = TypedDict(
    "_OptionalDataflowEndpointConfigTypeDef",
    {
        "dataflowEndpointRegion": str,
    },
    total=False,
)


class DataflowEndpointConfigTypeDef(
    _RequiredDataflowEndpointConfigTypeDef, _OptionalDataflowEndpointConfigTypeDef
):
    pass


_RequiredS3RecordingConfigTypeDef = TypedDict(
    "_RequiredS3RecordingConfigTypeDef",
    {
        "bucketArn": str,
        "roleArn": str,
    },
)
_OptionalS3RecordingConfigTypeDef = TypedDict(
    "_OptionalS3RecordingConfigTypeDef",
    {
        "prefix": str,
    },
    total=False,
)


class S3RecordingConfigTypeDef(
    _RequiredS3RecordingConfigTypeDef, _OptionalS3RecordingConfigTypeDef
):
    pass


TrackingConfigTypeDef = TypedDict(
    "TrackingConfigTypeDef",
    {
        "autotrack": CriticalityType,
    },
)

UplinkEchoConfigTypeDef = TypedDict(
    "UplinkEchoConfigTypeDef",
    {
        "antennaUplinkConfigArn": str,
        "enabled": bool,
    },
)

ElevationTypeDef = TypedDict(
    "ElevationTypeDef",
    {
        "unit": AngleUnitsType,
        "value": float,
    },
)

_RequiredCreateMissionProfileRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMissionProfileRequestRequestTypeDef",
    {
        "dataflowEdges": Sequence[Sequence[str]],
        "minimumViableContactDurationSeconds": int,
        "name": str,
        "trackingConfigArn": str,
    },
)
_OptionalCreateMissionProfileRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMissionProfileRequestRequestTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateMissionProfileRequestRequestTypeDef(
    _RequiredCreateMissionProfileRequestRequestTypeDef,
    _OptionalCreateMissionProfileRequestRequestTypeDef,
):
    pass


DataflowEndpointListItemTypeDef = TypedDict(
    "DataflowEndpointListItemTypeDef",
    {
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
    },
    total=False,
)

SocketAddressTypeDef = TypedDict(
    "SocketAddressTypeDef",
    {
        "name": str,
        "port": int,
    },
)

DeleteConfigRequestRequestTypeDef = TypedDict(
    "DeleteConfigRequestRequestTypeDef",
    {
        "configId": str,
        "configType": ConfigCapabilityTypeType,
    },
)

DeleteDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "DeleteDataflowEndpointGroupRequestRequestTypeDef",
    {
        "dataflowEndpointGroupId": str,
    },
)

DeleteEphemerisRequestRequestTypeDef = TypedDict(
    "DeleteEphemerisRequestRequestTypeDef",
    {
        "ephemerisId": str,
    },
)

DeleteMissionProfileRequestRequestTypeDef = TypedDict(
    "DeleteMissionProfileRequestRequestTypeDef",
    {
        "missionProfileId": str,
    },
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

DescribeContactRequestRequestTypeDef = TypedDict(
    "DescribeContactRequestRequestTypeDef",
    {
        "contactId": str,
    },
)

DescribeEphemerisRequestRequestTypeDef = TypedDict(
    "DescribeEphemerisRequestRequestTypeDef",
    {
        "ephemerisId": str,
    },
)

SecurityDetailsTypeDef = TypedDict(
    "SecurityDetailsTypeDef",
    {
        "roleArn": str,
        "securityGroupIds": Sequence[str],
        "subnetIds": Sequence[str],
    },
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "bucket": str,
        "key": str,
        "version": str,
    },
    total=False,
)

_RequiredEphemerisMetaDataTypeDef = TypedDict(
    "_RequiredEphemerisMetaDataTypeDef",
    {
        "source": EphemerisSourceType,
    },
)
_OptionalEphemerisMetaDataTypeDef = TypedDict(
    "_OptionalEphemerisMetaDataTypeDef",
    {
        "ephemerisId": str,
        "epoch": datetime,
        "name": str,
    },
    total=False,
)


class EphemerisMetaDataTypeDef(
    _RequiredEphemerisMetaDataTypeDef, _OptionalEphemerisMetaDataTypeDef
):
    pass


FrequencyBandwidthTypeDef = TypedDict(
    "FrequencyBandwidthTypeDef",
    {
        "units": BandwidthUnitsType,
        "value": float,
    },
)

FrequencyTypeDef = TypedDict(
    "FrequencyTypeDef",
    {
        "units": FrequencyUnitsType,
        "value": float,
    },
)

GetConfigRequestRequestTypeDef = TypedDict(
    "GetConfigRequestRequestTypeDef",
    {
        "configId": str,
        "configType": ConfigCapabilityTypeType,
    },
)

GetDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "GetDataflowEndpointGroupRequestRequestTypeDef",
    {
        "dataflowEndpointGroupId": str,
    },
)

GetMinuteUsageRequestRequestTypeDef = TypedDict(
    "GetMinuteUsageRequestRequestTypeDef",
    {
        "month": int,
        "year": int,
    },
)

GetMissionProfileRequestRequestTypeDef = TypedDict(
    "GetMissionProfileRequestRequestTypeDef",
    {
        "missionProfileId": str,
    },
)

GetSatelliteRequestRequestTypeDef = TypedDict(
    "GetSatelliteRequestRequestTypeDef",
    {
        "satelliteId": str,
    },
)

GroundStationDataTypeDef = TypedDict(
    "GroundStationDataTypeDef",
    {
        "groundStationId": str,
        "groundStationName": str,
        "region": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

ListConfigsRequestRequestTypeDef = TypedDict(
    "ListConfigsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListContactsRequestRequestTypeDef = TypedDict(
    "_RequiredListContactsRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "startTime": Union[datetime, str],
        "statusList": Sequence[ContactStatusType],
    },
)
_OptionalListContactsRequestRequestTypeDef = TypedDict(
    "_OptionalListContactsRequestRequestTypeDef",
    {
        "groundStation": str,
        "maxResults": int,
        "missionProfileArn": str,
        "nextToken": str,
        "satelliteArn": str,
    },
    total=False,
)


class ListContactsRequestRequestTypeDef(
    _RequiredListContactsRequestRequestTypeDef, _OptionalListContactsRequestRequestTypeDef
):
    pass


ListDataflowEndpointGroupsRequestRequestTypeDef = TypedDict(
    "ListDataflowEndpointGroupsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

_RequiredListEphemeridesRequestRequestTypeDef = TypedDict(
    "_RequiredListEphemeridesRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "satelliteId": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalListEphemeridesRequestRequestTypeDef = TypedDict(
    "_OptionalListEphemeridesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "statusList": Sequence[EphemerisStatusType],
    },
    total=False,
)


class ListEphemeridesRequestRequestTypeDef(
    _RequiredListEphemeridesRequestRequestTypeDef, _OptionalListEphemeridesRequestRequestTypeDef
):
    pass


ListGroundStationsRequestRequestTypeDef = TypedDict(
    "ListGroundStationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
        "satelliteId": str,
    },
    total=False,
)

ListMissionProfilesRequestRequestTypeDef = TypedDict(
    "ListMissionProfilesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

MissionProfileListItemTypeDef = TypedDict(
    "MissionProfileListItemTypeDef",
    {
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
    },
    total=False,
)

ListSatellitesRequestRequestTypeDef = TypedDict(
    "ListSatellitesRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)

_RequiredReserveContactRequestRequestTypeDef = TypedDict(
    "_RequiredReserveContactRequestRequestTypeDef",
    {
        "endTime": Union[datetime, str],
        "groundStation": str,
        "missionProfileArn": str,
        "satelliteArn": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalReserveContactRequestRequestTypeDef = TypedDict(
    "_OptionalReserveContactRequestRequestTypeDef",
    {
        "tags": Mapping[str, str],
    },
    total=False,
)


class ReserveContactRequestRequestTypeDef(
    _RequiredReserveContactRequestRequestTypeDef, _OptionalReserveContactRequestRequestTypeDef
):
    pass


TimeRangeTypeDef = TypedDict(
    "TimeRangeTypeDef",
    {
        "endTime": Union[datetime, str],
        "startTime": Union[datetime, str],
    },
)

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)

_RequiredUpdateEphemerisRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateEphemerisRequestRequestTypeDef",
    {
        "enabled": bool,
        "ephemerisId": str,
    },
)
_OptionalUpdateEphemerisRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateEphemerisRequestRequestTypeDef",
    {
        "name": str,
        "priority": int,
    },
    total=False,
)


class UpdateEphemerisRequestRequestTypeDef(
    _RequiredUpdateEphemerisRequestRequestTypeDef, _OptionalUpdateEphemerisRequestRequestTypeDef
):
    pass


_RequiredUpdateMissionProfileRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateMissionProfileRequestRequestTypeDef",
    {
        "missionProfileId": str,
    },
)
_OptionalUpdateMissionProfileRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateMissionProfileRequestRequestTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": Sequence[Sequence[str]],
        "minimumViableContactDurationSeconds": int,
        "name": str,
        "trackingConfigArn": str,
    },
    total=False,
)


class UpdateMissionProfileRequestRequestTypeDef(
    _RequiredUpdateMissionProfileRequestRequestTypeDef,
    _OptionalUpdateMissionProfileRequestRequestTypeDef,
):
    pass


ConfigIdResponseTypeDef = TypedDict(
    "ConfigIdResponseTypeDef",
    {
        "configArn": str,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ContactIdResponseTypeDef = TypedDict(
    "ContactIdResponseTypeDef",
    {
        "contactId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DataflowEndpointGroupIdResponseTypeDef = TypedDict(
    "DataflowEndpointGroupIdResponseTypeDef",
    {
        "dataflowEndpointGroupId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EphemerisIdResponseTypeDef = TypedDict(
    "EphemerisIdResponseTypeDef",
    {
        "ephemerisId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMinuteUsageResponseTypeDef = TypedDict(
    "GetMinuteUsageResponseTypeDef",
    {
        "estimatedMinutesRemaining": int,
        "isReservedMinutesCustomer": bool,
        "totalReservedMinuteAllocation": int,
        "totalScheduledMinutes": int,
        "upcomingMinutesScheduled": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMissionProfileResponseTypeDef = TypedDict(
    "GetMissionProfileResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEdges": List[List[str]],
        "minimumViableContactDurationSeconds": int,
        "missionProfileArn": str,
        "missionProfileId": str,
        "name": str,
        "region": str,
        "tags": Dict[str, str],
        "trackingConfigArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

MissionProfileIdResponseTypeDef = TypedDict(
    "MissionProfileIdResponseTypeDef",
    {
        "missionProfileId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListConfigsResponseTypeDef = TypedDict(
    "ListConfigsResponseTypeDef",
    {
        "configList": List[ConfigListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ContactDataTypeDef = TypedDict(
    "ContactDataTypeDef",
    {
        "contactId": str,
        "contactStatus": ContactStatusType,
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
    },
    total=False,
)

ListDataflowEndpointGroupsResponseTypeDef = TypedDict(
    "ListDataflowEndpointGroupsResponseTypeDef",
    {
        "dataflowEndpointGroupList": List[DataflowEndpointListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DataflowEndpointTypeDef = TypedDict(
    "DataflowEndpointTypeDef",
    {
        "address": SocketAddressTypeDef,
        "mtu": int,
        "name": str,
        "status": EndpointStatusType,
    },
    total=False,
)

_RequiredDescribeContactRequestContactScheduledWaitTypeDef = TypedDict(
    "_RequiredDescribeContactRequestContactScheduledWaitTypeDef",
    {
        "contactId": str,
    },
)
_OptionalDescribeContactRequestContactScheduledWaitTypeDef = TypedDict(
    "_OptionalDescribeContactRequestContactScheduledWaitTypeDef",
    {
        "WaiterConfig": WaiterConfigTypeDef,
    },
    total=False,
)


class DescribeContactRequestContactScheduledWaitTypeDef(
    _RequiredDescribeContactRequestContactScheduledWaitTypeDef,
    _OptionalDescribeContactRequestContactScheduledWaitTypeDef,
):
    pass


EphemerisDescriptionTypeDef = TypedDict(
    "EphemerisDescriptionTypeDef",
    {
        "ephemerisData": str,
        "sourceS3Object": S3ObjectTypeDef,
    },
    total=False,
)

EphemerisItemTypeDef = TypedDict(
    "EphemerisItemTypeDef",
    {
        "creationTime": datetime,
        "enabled": bool,
        "ephemerisId": str,
        "name": str,
        "priority": int,
        "sourceS3Object": S3ObjectTypeDef,
        "status": EphemerisStatusType,
    },
    total=False,
)

OEMEphemerisTypeDef = TypedDict(
    "OEMEphemerisTypeDef",
    {
        "oemData": str,
        "s3Object": S3ObjectTypeDef,
    },
    total=False,
)

GetSatelliteResponseTypeDef = TypedDict(
    "GetSatelliteResponseTypeDef",
    {
        "currentEphemeris": EphemerisMetaDataTypeDef,
        "groundStations": List[str],
        "noradSatelliteID": int,
        "satelliteArn": str,
        "satelliteId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

SatelliteListItemTypeDef = TypedDict(
    "SatelliteListItemTypeDef",
    {
        "currentEphemeris": EphemerisMetaDataTypeDef,
        "groundStations": List[str],
        "noradSatelliteID": int,
        "satelliteArn": str,
        "satelliteId": str,
    },
    total=False,
)

_RequiredSpectrumConfigTypeDef = TypedDict(
    "_RequiredSpectrumConfigTypeDef",
    {
        "bandwidth": FrequencyBandwidthTypeDef,
        "centerFrequency": FrequencyTypeDef,
    },
)
_OptionalSpectrumConfigTypeDef = TypedDict(
    "_OptionalSpectrumConfigTypeDef",
    {
        "polarization": PolarizationType,
    },
    total=False,
)


class SpectrumConfigTypeDef(_RequiredSpectrumConfigTypeDef, _OptionalSpectrumConfigTypeDef):
    pass


_RequiredUplinkSpectrumConfigTypeDef = TypedDict(
    "_RequiredUplinkSpectrumConfigTypeDef",
    {
        "centerFrequency": FrequencyTypeDef,
    },
)
_OptionalUplinkSpectrumConfigTypeDef = TypedDict(
    "_OptionalUplinkSpectrumConfigTypeDef",
    {
        "polarization": PolarizationType,
    },
    total=False,
)


class UplinkSpectrumConfigTypeDef(
    _RequiredUplinkSpectrumConfigTypeDef, _OptionalUplinkSpectrumConfigTypeDef
):
    pass


ListGroundStationsResponseTypeDef = TypedDict(
    "ListGroundStationsResponseTypeDef",
    {
        "groundStationList": List[GroundStationDataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListConfigsRequestListConfigsPaginateTypeDef = TypedDict(
    "ListConfigsRequestListConfigsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListContactsRequestListContactsPaginateTypeDef = TypedDict(
    "_RequiredListContactsRequestListContactsPaginateTypeDef",
    {
        "endTime": Union[datetime, str],
        "startTime": Union[datetime, str],
        "statusList": Sequence[ContactStatusType],
    },
)
_OptionalListContactsRequestListContactsPaginateTypeDef = TypedDict(
    "_OptionalListContactsRequestListContactsPaginateTypeDef",
    {
        "groundStation": str,
        "missionProfileArn": str,
        "satelliteArn": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListContactsRequestListContactsPaginateTypeDef(
    _RequiredListContactsRequestListContactsPaginateTypeDef,
    _OptionalListContactsRequestListContactsPaginateTypeDef,
):
    pass


ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef = TypedDict(
    "ListDataflowEndpointGroupsRequestListDataflowEndpointGroupsPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

_RequiredListEphemeridesRequestListEphemeridesPaginateTypeDef = TypedDict(
    "_RequiredListEphemeridesRequestListEphemeridesPaginateTypeDef",
    {
        "endTime": Union[datetime, str],
        "satelliteId": str,
        "startTime": Union[datetime, str],
    },
)
_OptionalListEphemeridesRequestListEphemeridesPaginateTypeDef = TypedDict(
    "_OptionalListEphemeridesRequestListEphemeridesPaginateTypeDef",
    {
        "statusList": Sequence[EphemerisStatusType],
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)


class ListEphemeridesRequestListEphemeridesPaginateTypeDef(
    _RequiredListEphemeridesRequestListEphemeridesPaginateTypeDef,
    _OptionalListEphemeridesRequestListEphemeridesPaginateTypeDef,
):
    pass


ListGroundStationsRequestListGroundStationsPaginateTypeDef = TypedDict(
    "ListGroundStationsRequestListGroundStationsPaginateTypeDef",
    {
        "satelliteId": str,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListMissionProfilesRequestListMissionProfilesPaginateTypeDef = TypedDict(
    "ListMissionProfilesRequestListMissionProfilesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListSatellitesRequestListSatellitesPaginateTypeDef = TypedDict(
    "ListSatellitesRequestListSatellitesPaginateTypeDef",
    {
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListMissionProfilesResponseTypeDef = TypedDict(
    "ListMissionProfilesResponseTypeDef",
    {
        "missionProfileList": List[MissionProfileListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TLEDataTypeDef = TypedDict(
    "TLEDataTypeDef",
    {
        "tleLine1": str,
        "tleLine2": str,
        "validTimeRange": TimeRangeTypeDef,
    },
)

ListContactsResponseTypeDef = TypedDict(
    "ListContactsResponseTypeDef",
    {
        "contactList": List[ContactDataTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EndpointDetailsTypeDef = TypedDict(
    "EndpointDetailsTypeDef",
    {
        "endpoint": DataflowEndpointTypeDef,
        "securityDetails": SecurityDetailsTypeDef,
    },
    total=False,
)

EphemerisTypeDescriptionTypeDef = TypedDict(
    "EphemerisTypeDescriptionTypeDef",
    {
        "oem": EphemerisDescriptionTypeDef,
        "tle": EphemerisDescriptionTypeDef,
    },
    total=False,
)

ListEphemeridesResponseTypeDef = TypedDict(
    "ListEphemeridesResponseTypeDef",
    {
        "ephemerides": List[EphemerisItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSatellitesResponseTypeDef = TypedDict(
    "ListSatellitesResponseTypeDef",
    {
        "nextToken": str,
        "satellites": List[SatelliteListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

AntennaDownlinkConfigTypeDef = TypedDict(
    "AntennaDownlinkConfigTypeDef",
    {
        "spectrumConfig": SpectrumConfigTypeDef,
    },
)

AntennaDownlinkDemodDecodeConfigTypeDef = TypedDict(
    "AntennaDownlinkDemodDecodeConfigTypeDef",
    {
        "decodeConfig": DecodeConfigTypeDef,
        "demodulationConfig": DemodulationConfigTypeDef,
        "spectrumConfig": SpectrumConfigTypeDef,
    },
)

_RequiredAntennaUplinkConfigTypeDef = TypedDict(
    "_RequiredAntennaUplinkConfigTypeDef",
    {
        "spectrumConfig": UplinkSpectrumConfigTypeDef,
        "targetEirp": EirpTypeDef,
    },
)
_OptionalAntennaUplinkConfigTypeDef = TypedDict(
    "_OptionalAntennaUplinkConfigTypeDef",
    {
        "transmitDisabled": bool,
    },
    total=False,
)


class AntennaUplinkConfigTypeDef(
    _RequiredAntennaUplinkConfigTypeDef, _OptionalAntennaUplinkConfigTypeDef
):
    pass


TLEEphemerisTypeDef = TypedDict(
    "TLEEphemerisTypeDef",
    {
        "s3Object": S3ObjectTypeDef,
        "tleData": Sequence[TLEDataTypeDef],
    },
    total=False,
)

ConfigDetailsTypeDef = TypedDict(
    "ConfigDetailsTypeDef",
    {
        "antennaDemodDecodeDetails": AntennaDemodDecodeDetailsTypeDef,
        "endpointDetails": EndpointDetailsTypeDef,
        "s3RecordingDetails": S3RecordingDetailsTypeDef,
    },
    total=False,
)

_RequiredCreateDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDataflowEndpointGroupRequestRequestTypeDef",
    {
        "endpointDetails": Sequence[EndpointDetailsTypeDef],
    },
)
_OptionalCreateDataflowEndpointGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDataflowEndpointGroupRequestRequestTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateDataflowEndpointGroupRequestRequestTypeDef(
    _RequiredCreateDataflowEndpointGroupRequestRequestTypeDef,
    _OptionalCreateDataflowEndpointGroupRequestRequestTypeDef,
):
    pass


GetDataflowEndpointGroupResponseTypeDef = TypedDict(
    "GetDataflowEndpointGroupResponseTypeDef",
    {
        "contactPostPassDurationSeconds": int,
        "contactPrePassDurationSeconds": int,
        "dataflowEndpointGroupArn": str,
        "dataflowEndpointGroupId": str,
        "endpointsDetails": List[EndpointDetailsTypeDef],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeEphemerisResponseTypeDef = TypedDict(
    "DescribeEphemerisResponseTypeDef",
    {
        "creationTime": datetime,
        "enabled": bool,
        "ephemerisId": str,
        "invalidReason": EphemerisInvalidReasonType,
        "name": str,
        "priority": int,
        "satelliteId": str,
        "status": EphemerisStatusType,
        "suppliedData": EphemerisTypeDescriptionTypeDef,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ConfigTypeDataTypeDef = TypedDict(
    "ConfigTypeDataTypeDef",
    {
        "antennaDownlinkConfig": AntennaDownlinkConfigTypeDef,
        "antennaDownlinkDemodDecodeConfig": AntennaDownlinkDemodDecodeConfigTypeDef,
        "antennaUplinkConfig": AntennaUplinkConfigTypeDef,
        "dataflowEndpointConfig": DataflowEndpointConfigTypeDef,
        "s3RecordingConfig": S3RecordingConfigTypeDef,
        "trackingConfig": TrackingConfigTypeDef,
        "uplinkEchoConfig": UplinkEchoConfigTypeDef,
    },
    total=False,
)

EphemerisDataTypeDef = TypedDict(
    "EphemerisDataTypeDef",
    {
        "oem": OEMEphemerisTypeDef,
        "tle": TLEEphemerisTypeDef,
    },
    total=False,
)

DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "configDetails": ConfigDetailsTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "dataflowDestinationRegion": str,
    },
    total=False,
)

SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "configDetails": ConfigDetailsTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "dataflowSourceRegion": str,
    },
    total=False,
)

_RequiredCreateConfigRequestRequestTypeDef = TypedDict(
    "_RequiredCreateConfigRequestRequestTypeDef",
    {
        "configData": ConfigTypeDataTypeDef,
        "name": str,
    },
)
_OptionalCreateConfigRequestRequestTypeDef = TypedDict(
    "_OptionalCreateConfigRequestRequestTypeDef",
    {
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateConfigRequestRequestTypeDef(
    _RequiredCreateConfigRequestRequestTypeDef, _OptionalCreateConfigRequestRequestTypeDef
):
    pass


GetConfigResponseTypeDef = TypedDict(
    "GetConfigResponseTypeDef",
    {
        "configArn": str,
        "configData": ConfigTypeDataTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

UpdateConfigRequestRequestTypeDef = TypedDict(
    "UpdateConfigRequestRequestTypeDef",
    {
        "configData": ConfigTypeDataTypeDef,
        "configId": str,
        "configType": ConfigCapabilityTypeType,
        "name": str,
    },
)

_RequiredCreateEphemerisRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEphemerisRequestRequestTypeDef",
    {
        "name": str,
        "satelliteId": str,
    },
)
_OptionalCreateEphemerisRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEphemerisRequestRequestTypeDef",
    {
        "enabled": bool,
        "ephemeris": EphemerisDataTypeDef,
        "expirationTime": Union[datetime, str],
        "kmsKeyArn": str,
        "priority": int,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateEphemerisRequestRequestTypeDef(
    _RequiredCreateEphemerisRequestRequestTypeDef, _OptionalCreateEphemerisRequestRequestTypeDef
):
    pass


DataflowDetailTypeDef = TypedDict(
    "DataflowDetailTypeDef",
    {
        "destination": DestinationTypeDef,
        "errorMessage": str,
        "source": SourceTypeDef,
    },
    total=False,
)

DescribeContactResponseTypeDef = TypedDict(
    "DescribeContactResponseTypeDef",
    {
        "contactId": str,
        "contactStatus": ContactStatusType,
        "dataflowList": List[DataflowDetailTypeDef],
        "endTime": datetime,
        "errorMessage": str,
        "groundStation": str,
        "maximumElevation": ElevationTypeDef,
        "missionProfileArn": str,
        "postPassEndTime": datetime,
        "prePassStartTime": datetime,
        "region": str,
        "satelliteArn": str,
        "startTime": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
