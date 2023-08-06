"""
Type annotations for ivschat service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ivschat/type_defs/)

Usage::

    ```python
    from mypy_boto3_ivschat.type_defs import CloudWatchLogsDestinationConfigurationTypeDef

    data: CloudWatchLogsDestinationConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import ChatTokenCapabilityType, FallbackResultType, LoggingConfigurationStateType

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CloudWatchLogsDestinationConfigurationTypeDef",
    "CreateChatTokenRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "MessageReviewHandlerTypeDef",
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    "DeleteMessageRequestRequestTypeDef",
    "DeleteRoomRequestRequestTypeDef",
    "FirehoseDestinationConfigurationTypeDef",
    "S3DestinationConfigurationTypeDef",
    "DisconnectUserRequestRequestTypeDef",
    "GetLoggingConfigurationRequestRequestTypeDef",
    "GetRoomRequestRequestTypeDef",
    "ListLoggingConfigurationsRequestRequestTypeDef",
    "ListRoomsRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "SendEventRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateChatTokenResponseTypeDef",
    "DeleteMessageResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "SendEventResponseTypeDef",
    "CreateRoomRequestRequestTypeDef",
    "CreateRoomResponseTypeDef",
    "GetRoomResponseTypeDef",
    "RoomSummaryTypeDef",
    "UpdateRoomRequestRequestTypeDef",
    "UpdateRoomResponseTypeDef",
    "DestinationConfigurationTypeDef",
    "ListRoomsResponseTypeDef",
    "CreateLoggingConfigurationRequestRequestTypeDef",
    "CreateLoggingConfigurationResponseTypeDef",
    "GetLoggingConfigurationResponseTypeDef",
    "LoggingConfigurationSummaryTypeDef",
    "UpdateLoggingConfigurationRequestRequestTypeDef",
    "UpdateLoggingConfigurationResponseTypeDef",
    "ListLoggingConfigurationsResponseTypeDef",
)

CloudWatchLogsDestinationConfigurationTypeDef = TypedDict(
    "CloudWatchLogsDestinationConfigurationTypeDef",
    {
        "logGroupName": str,
    },
)

_RequiredCreateChatTokenRequestRequestTypeDef = TypedDict(
    "_RequiredCreateChatTokenRequestRequestTypeDef",
    {
        "roomIdentifier": str,
        "userId": str,
    },
)
_OptionalCreateChatTokenRequestRequestTypeDef = TypedDict(
    "_OptionalCreateChatTokenRequestRequestTypeDef",
    {
        "attributes": Mapping[str, str],
        "capabilities": Sequence[ChatTokenCapabilityType],
        "sessionDurationInMinutes": int,
    },
    total=False,
)


class CreateChatTokenRequestRequestTypeDef(
    _RequiredCreateChatTokenRequestRequestTypeDef, _OptionalCreateChatTokenRequestRequestTypeDef
):
    pass


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

MessageReviewHandlerTypeDef = TypedDict(
    "MessageReviewHandlerTypeDef",
    {
        "fallbackResult": FallbackResultType,
        "uri": str,
    },
    total=False,
)

DeleteLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "DeleteLoggingConfigurationRequestRequestTypeDef",
    {
        "identifier": str,
    },
)

_RequiredDeleteMessageRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteMessageRequestRequestTypeDef",
    {
        "id": str,
        "roomIdentifier": str,
    },
)
_OptionalDeleteMessageRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteMessageRequestRequestTypeDef",
    {
        "reason": str,
    },
    total=False,
)


class DeleteMessageRequestRequestTypeDef(
    _RequiredDeleteMessageRequestRequestTypeDef, _OptionalDeleteMessageRequestRequestTypeDef
):
    pass


DeleteRoomRequestRequestTypeDef = TypedDict(
    "DeleteRoomRequestRequestTypeDef",
    {
        "identifier": str,
    },
)

FirehoseDestinationConfigurationTypeDef = TypedDict(
    "FirehoseDestinationConfigurationTypeDef",
    {
        "deliveryStreamName": str,
    },
)

S3DestinationConfigurationTypeDef = TypedDict(
    "S3DestinationConfigurationTypeDef",
    {
        "bucketName": str,
    },
)

_RequiredDisconnectUserRequestRequestTypeDef = TypedDict(
    "_RequiredDisconnectUserRequestRequestTypeDef",
    {
        "roomIdentifier": str,
        "userId": str,
    },
)
_OptionalDisconnectUserRequestRequestTypeDef = TypedDict(
    "_OptionalDisconnectUserRequestRequestTypeDef",
    {
        "reason": str,
    },
    total=False,
)


class DisconnectUserRequestRequestTypeDef(
    _RequiredDisconnectUserRequestRequestTypeDef, _OptionalDisconnectUserRequestRequestTypeDef
):
    pass


GetLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "GetLoggingConfigurationRequestRequestTypeDef",
    {
        "identifier": str,
    },
)

GetRoomRequestRequestTypeDef = TypedDict(
    "GetRoomRequestRequestTypeDef",
    {
        "identifier": str,
    },
)

ListLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "ListLoggingConfigurationsRequestRequestTypeDef",
    {
        "maxResults": int,
        "nextToken": str,
    },
    total=False,
)

ListRoomsRequestRequestTypeDef = TypedDict(
    "ListRoomsRequestRequestTypeDef",
    {
        "loggingConfigurationIdentifier": str,
        "maxResults": int,
        "messageReviewHandlerUri": str,
        "name": str,
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

_RequiredSendEventRequestRequestTypeDef = TypedDict(
    "_RequiredSendEventRequestRequestTypeDef",
    {
        "eventName": str,
        "roomIdentifier": str,
    },
)
_OptionalSendEventRequestRequestTypeDef = TypedDict(
    "_OptionalSendEventRequestRequestTypeDef",
    {
        "attributes": Mapping[str, str],
    },
    total=False,
)


class SendEventRequestRequestTypeDef(
    _RequiredSendEventRequestRequestTypeDef, _OptionalSendEventRequestRequestTypeDef
):
    pass


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

CreateChatTokenResponseTypeDef = TypedDict(
    "CreateChatTokenResponseTypeDef",
    {
        "sessionExpirationTime": datetime,
        "token": str,
        "tokenExpirationTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DeleteMessageResponseTypeDef = TypedDict(
    "DeleteMessageResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
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

SendEventResponseTypeDef = TypedDict(
    "SendEventResponseTypeDef",
    {
        "id": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateRoomRequestRequestTypeDef = TypedDict(
    "CreateRoomRequestRequestTypeDef",
    {
        "loggingConfigurationIdentifiers": Sequence[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "name": str,
        "tags": Mapping[str, str],
    },
    total=False,
)

CreateRoomResponseTypeDef = TypedDict(
    "CreateRoomResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "loggingConfigurationIdentifiers": List[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetRoomResponseTypeDef = TypedDict(
    "GetRoomResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "loggingConfigurationIdentifiers": List[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

RoomSummaryTypeDef = TypedDict(
    "RoomSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "loggingConfigurationIdentifiers": List[str],
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
    },
    total=False,
)

_RequiredUpdateRoomRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateRoomRequestRequestTypeDef",
    {
        "identifier": str,
    },
)
_OptionalUpdateRoomRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateRoomRequestRequestTypeDef",
    {
        "loggingConfigurationIdentifiers": Sequence[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "name": str,
    },
    total=False,
)


class UpdateRoomRequestRequestTypeDef(
    _RequiredUpdateRoomRequestRequestTypeDef, _OptionalUpdateRoomRequestRequestTypeDef
):
    pass


UpdateRoomResponseTypeDef = TypedDict(
    "UpdateRoomResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "id": str,
        "loggingConfigurationIdentifiers": List[str],
        "maximumMessageLength": int,
        "maximumMessageRatePerSecond": int,
        "messageReviewHandler": MessageReviewHandlerTypeDef,
        "name": str,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DestinationConfigurationTypeDef = TypedDict(
    "DestinationConfigurationTypeDef",
    {
        "cloudWatchLogs": CloudWatchLogsDestinationConfigurationTypeDef,
        "firehose": FirehoseDestinationConfigurationTypeDef,
        "s3": S3DestinationConfigurationTypeDef,
    },
    total=False,
)

ListRoomsResponseTypeDef = TypedDict(
    "ListRoomsResponseTypeDef",
    {
        "nextToken": str,
        "rooms": List[RoomSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLoggingConfigurationRequestRequestTypeDef",
    {
        "destinationConfiguration": DestinationConfigurationTypeDef,
    },
)
_OptionalCreateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLoggingConfigurationRequestRequestTypeDef",
    {
        "name": str,
        "tags": Mapping[str, str],
    },
    total=False,
)


class CreateLoggingConfigurationRequestRequestTypeDef(
    _RequiredCreateLoggingConfigurationRequestRequestTypeDef,
    _OptionalCreateLoggingConfigurationRequestRequestTypeDef,
):
    pass


CreateLoggingConfigurationResponseTypeDef = TypedDict(
    "CreateLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "id": str,
        "name": str,
        "state": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetLoggingConfigurationResponseTypeDef = TypedDict(
    "GetLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "id": str,
        "name": str,
        "state": LoggingConfigurationStateType,
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

LoggingConfigurationSummaryTypeDef = TypedDict(
    "LoggingConfigurationSummaryTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "id": str,
        "name": str,
        "state": LoggingConfigurationStateType,
        "tags": Dict[str, str],
        "updateTime": datetime,
    },
    total=False,
)

_RequiredUpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "identifier": str,
    },
)
_OptionalUpdateLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateLoggingConfigurationRequestRequestTypeDef",
    {
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "name": str,
    },
    total=False,
)


class UpdateLoggingConfigurationRequestRequestTypeDef(
    _RequiredUpdateLoggingConfigurationRequestRequestTypeDef,
    _OptionalUpdateLoggingConfigurationRequestRequestTypeDef,
):
    pass


UpdateLoggingConfigurationResponseTypeDef = TypedDict(
    "UpdateLoggingConfigurationResponseTypeDef",
    {
        "arn": str,
        "createTime": datetime,
        "destinationConfiguration": DestinationConfigurationTypeDef,
        "id": str,
        "name": str,
        "state": Literal["ACTIVE"],
        "tags": Dict[str, str],
        "updateTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListLoggingConfigurationsResponseTypeDef = TypedDict(
    "ListLoggingConfigurationsResponseTypeDef",
    {
        "loggingConfigurations": List[LoggingConfigurationSummaryTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
