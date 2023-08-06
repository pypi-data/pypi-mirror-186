# fingoti-sdk


## Requirements.

Python >=3.6

## Installation & Usage

### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install fingoti-sdk
```

(you may need to run `pip` with root permission: `sudo pip install fingoti-sdk`)

Then import the package:

```python
import fingoti
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import fingoti
from pprint import pprint
from fingoti.api import device_api
from fingoti.model.claim_request import ClaimRequest
from fingoti.model.claim_result import ClaimResult
from fingoti.model.claimed_device_response import ClaimedDeviceResponse
from fingoti.model.claimed_devices_dto import ClaimedDevicesDto
from fingoti.model.default import Default
from fingoti.model.device_nodes_response import DeviceNodesResponse
from fingoti.model.device_request import DeviceRequest
from fingoti.model.mqtt_device_response import MqttDeviceResponse
from fingoti.model.patch_gateway import PatchGateway
from fingoti.model.update_request import UpdateRequest
from fingoti.model.update_response import UpdateResponse
# Defining the host is optional and defaults to https://api.fingoti.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fingoti.Configuration(
    host = "https://api.fingoti.com"
)

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = '<YOUR_API_KEY>'
configuration.api_key_prefix['Bearer'] = 'Bearer'


# Enter a context with an instance of the API client
with fingoti.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = device_api.DeviceApi(api_client)
    id = "id_example" # str |

    try:
        # Unclaim a Fingoti device.
        api_response = api_instance.delete_device_id(id)
        pprint(api_response)
    except fingoti.ApiException as e:
        print("Exception when calling DeviceApi->delete_device_id: %s\n" % e)
```

## Getting Started - Not generated

Here we will briefly cover the steps needed to get up and running with the SDK

### Create a configuration

The first step to communicating with the Fingoti infrastructure is authentication and configureation, to do this you will need an API key which can be obtained from http://account.fingoti.com, once you have an API key you can create a configuration as shown below

```python
import fingoti

config = fingoti.Configuration()
config.api_key["Bearer"] = "<your-api-key>"
config.api_key_prefix["Bearer"] = "Bearer"
```

Now you have a configuration we can use that to authenticate requests to the Fingoti infrastructure, lets start with a basic Organisation information request.

### Using the APIs

In the SDK the diffrent sections of the infrastructure are split into seperate API's in the example below, we are going to use the Organisation API to retrieve basic information about your Organisation.

```python
from fingoti.api import organisation_api

with fingoti.ApiClient(config) as api_client:

    organisationApi = organisation_api.OrganisationApi(apiClient)

    try:
        response = organisationApi.get_organisation()
        pprint(response)
    except fingoti.ApiException as e:
        print("Exception when calling get_organisation: %s\n" % e)
```

You should see a response containing your organisation information printed in the terminal, if it does, great! You can now explore the rest of the docuemntation to find API's that fit your requirements.

### Device Control/Communication

Alongside the API's this package also comes with what we call a command builder which allows you to assemble requests to send to your Fingoti devices. It works in a similar way to the other API's and takes the same configuration shown in [Create a configuration](#create-a-configuration), see below

```python
from fingoti.command import builder

with fingoti.ApiClient(config) as api_client:
    commands = builder.Builder(api_client, "A0B1C3D4E5")

    """
    Device commands can have read or write operation, in general read commands do not require a payload

    All write operations require a payload
    """

    "Adds a deviceColour read command, deviceColour has a read & write operation, in this case we do not need to send a payload for the read command"
    commands.addDeviceColour()

    "Adds a deviceColour write command, as this is a deviceColour write command we are adding a payload"
    commands.addDeviceColour(100, 25, 75)

    "Adds a devicePower read command, devicePower only has a read command, therefore no payload is required"
    commands.addDevicePower()

    "Adds a uartData write command, uartData only has a write command so it requires a payload"
    commands.addUARTData([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100])

    """
    As mentioned in some cases a read command will require a payload

    We will demonstrate this with a scheduleCron command
    """

    "Adds a scheduleCron read command, this will read the cron string for schedule slot 2"
    commands.addScheduleCron(2)

    "Adds a scheduleCron write command, this will set the cron string for schedule slot 2"
    commands.addScheduleCron(2, "20 * * * *")

    "The .log() method will print what the builder has assembled in the background, this is useful for debugging"
    commands.log()

    "Once you've finished assembling commands, send them"
    result = commands.send()
    print(result.to_dict())
```
After running the script you should see 2 outputs, the first one is the what was sent to the device and the second is what the device responded with, This is just a small introduction into the command builder and you can find a full list of avaliable commands, HERE

## Documentation for API Endpoints


| Class             | Method                                                                                           | HTTP request                               | Description                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------ | ---------------------------------------------------------------------------------------- |
| _DeviceApi_       | [**delete_device_id**](docs/DeviceApi.md#delete_device_id)                                       | **DELETE** /v1/device/{id}                 | Unclaim a Fingoti device.                                                                |
| _DeviceApi_       | [**get_device**](docs/DeviceApi.md#get_device)                                                   | **GET** /v1/device                         | Get all devices.                                                                         |
| _DeviceApi_       | [**get_device_id**](docs/DeviceApi.md#get_device_id)                                             | **GET** /v1/device/{id}                    | Get specified device.                                                                    |
| _DeviceApi_       | [**get_device_id_nodes**](docs/DeviceApi.md#get_device_id_nodes)                                 | **GET** /v1/device/{id}/nodes              | Get all nodes latched to a gateway.                                                      |
| _DeviceApi_       | [**patch_device_id**](docs/DeviceApi.md#patch_device_id)                                         | **PATCH** /v1/device/{id}                  | Update your Fingoti device.                                                              |
| _DeviceApi_       | [**post_device**](docs/DeviceApi.md#post_device)                                                 | **POST** /v1/device                        | Claim a new Fingoti device.                                                              |
| _DeviceApi_       | [**post_device_sendrequest**](docs/DeviceApi.md#post_device_sendrequest)                         | **POST** /v1/device/sendrequest            | Send a request to a Fingoti device.                                                      |
| _DeviceApi_       | [**post_device_update**](docs/DeviceApi.md#post_device_update)                                   | **POST** /v1/device/update                 | Initiate a device update.                                                                |
| _FollowingsApi_   | [**delete_followings_id**](docs/FollowingsApi.md#delete_followings_id)                           | **DELETE** /v1/followings/{id}             | Delete a Pin Following. This is not recoverable.                                         |
| _FollowingsApi_   | [**get_followings**](docs/FollowingsApi.md#get_followings)                                       | **GET** /v1/followings                     | Get all pin followings.                                                                  |
| _FollowingsApi_   | [**get_followings_id**](docs/FollowingsApi.md#get_followings_id)                                 | **GET** /v1/followings/{id}                | Get specified pin following.                                                             |
| _FollowingsApi_   | [**patch_followings_id**](docs/FollowingsApi.md#patch_followings_id)                             | **PATCH** /v1/followings/{id}              | Update pin following.                                                                    |
| _FollowingsApi_   | [**post_followings**](docs/FollowingsApi.md#post_followings)                                     | **POST** /v1/followings                    | Create a new pin following.                                                              |
| _OrganisationApi_ | [**delete_organisation_addresses_id**](docs/OrganisationApi.md#delete_organisation_addresses_id) | **DELETE** /v1/organisation/addresses/{id} | Delete an address. This is not recoverable.                                              |
| _OrganisationApi_ | [**delete_organisation_presets_id**](docs/OrganisationApi.md#delete_organisation_presets_id)     | **DELETE** /v1/organisation/presets/{id}   | Delete specified preset.                                                                 |
| _OrganisationApi_ | [**delete_organisation_roles_id**](docs/OrganisationApi.md#delete_organisation_roles_id)         | **DELETE** /v1/organisation/roles/{id}     | Delete a role. Role must not be assigned to any users. This is not recoverable.          |
| _OrganisationApi_ | [**delete_organisation_tokens_id**](docs/OrganisationApi.md#delete_organisation_tokens_id)       | **DELETE** /v1/organisation/tokens/{id}    | Delete a Token. Token will no longer authenticate API requests. This is not recoverable. |
| _OrganisationApi_ | [**delete_organisation_users_id**](docs/OrganisationApi.md#delete_organisation_users_id)         | **DELETE** /v1/organisation/users/{id}     | Remove a user from the organisation.                                                     |
| _OrganisationApi_ | [**get_organisation**](docs/OrganisationApi.md#get_organisation)                                 | **GET** /v1/organisation                   | Get your Fingoti organisaiton information.                                               |
| _OrganisationApi_ | [**get_organisation_addresses**](docs/OrganisationApi.md#get_organisation_addresses)             | **GET** /v1/organisation/addresses         | Get all addresses.                                                                       |
| _OrganisationApi_ | [**get_organisation_addresses_id**](docs/OrganisationApi.md#get_organisation_addresses_id)       | **GET** /v1/organisation/addresses/{id}    | Get specified address.                                                                   |
| _OrganisationApi_ | [**get_organisation_partner**](docs/OrganisationApi.md#get_organisation_partner)                 | **GET** /v1/organisation/partner           | Get partner information.                                                                 |
| _OrganisationApi_ | [**get_organisation_presets**](docs/OrganisationApi.md#get_organisation_presets)                 | **GET** /v1/organisation/presets           | Get all presets.                                                                         |
| _OrganisationApi_ | [**get_organisation_presets_id**](docs/OrganisationApi.md#get_organisation_presets_id)           | **GET** /v1/organisation/presets/{id}      | Get specified preset.                                                                    |
| _OrganisationApi_ | [**get_organisation_roles**](docs/OrganisationApi.md#get_organisation_roles)                     | **GET** /v1/organisation/roles             | Get all roles.                                                                           |
| _OrganisationApi_ | [**get_organisation_roles_id**](docs/OrganisationApi.md#get_organisation_roles_id)               | **GET** /v1/organisation/roles/{id}        | Get specified role.                                                                      |
| _OrganisationApi_ | [**get_organisation_tenants**](docs/OrganisationApi.md#get_organisation_tenants)                 | **GET** /v1/organisation/tenants           | Get all tenants.                                                                         |
| _OrganisationApi_ | [**get_organisation_tokens**](docs/OrganisationApi.md#get_organisation_tokens)                   | **GET** /v1/organisation/tokens            | Get all API tokens.                                                                      |
| _OrganisationApi_ | [**get_organisation_tokens_id**](docs/OrganisationApi.md#get_organisation_tokens_id)             | **GET** /v1/organisation/tokens/{id}       | Get specified token.                                                                     |
| _OrganisationApi_ | [**get_organisation_users**](docs/OrganisationApi.md#get_organisation_users)                     | **GET** /v1/organisation/users             | Get all users.                                                                           |
| _OrganisationApi_ | [**get_organisation_users_id**](docs/OrganisationApi.md#get_organisation_users_id)               | **GET** /v1/organisation/users/{id}        | Get specidfied user.                                                                     |
| _OrganisationApi_ | [**patch_organisation**](docs/OrganisationApi.md#patch_organisation)                             | **PATCH** /v1/organisation                 | Update your Fingoti organisation.                                                        |
| _OrganisationApi_ | [**patch_organisation_addresses_id**](docs/OrganisationApi.md#patch_organisation_addresses_id)   | **PATCH** /v1/organisation/addresses/{id}  | Update organisation address.                                                             |
| _OrganisationApi_ | [**patch_organisation_presets_id**](docs/OrganisationApi.md#patch_organisation_presets_id)       | **PATCH** /v1/organisation/presets/{id}    | Update organisation preset.                                                              |
| _OrganisationApi_ | [**patch_organisation_roles_id**](docs/OrganisationApi.md#patch_organisation_roles_id)           | **PATCH** /v1/organisation/roles/{id}      | Update organisation role.                                                                |
| _OrganisationApi_ | [**patch_organisation_tokens_id**](docs/OrganisationApi.md#patch_organisation_tokens_id)         | **PATCH** /v1/organisation/tokens/{id}     | Update API token.                                                                        |
| _OrganisationApi_ | [**patch_organisation_users_id**](docs/OrganisationApi.md#patch_organisation_users_id)           | **PATCH** /v1/organisation/users/{id}      | Update organisation user.                                                                |
| _OrganisationApi_ | [**post_organisation**](docs/OrganisationApi.md#post_organisation)                               | **POST** /v1/organisation                  | Register a new Fingoti organisation.                                                     |
| _OrganisationApi_ | [**post_organisation_addresses**](docs/OrganisationApi.md#post_organisation_addresses)           | **POST** /v1/organisation/addresses        | Create a new address.                                                                    |
| _OrganisationApi_ | [**post_organisation_presets**](docs/OrganisationApi.md#post_organisation_presets)               | **POST** /v1/organisation/presets          | Create a new preset.                                                                     |
| _OrganisationApi_ | [**post_organisation_roles**](docs/OrganisationApi.md#post_organisation_roles)                   | **POST** /v1/organisation/roles            | Create a new role.                                                                       |
| _OrganisationApi_ | [**post_organisation_tenants**](docs/OrganisationApi.md#post_organisation_tenants)               | **POST** /v1/organisation/tenants          | Create new tenant. This is only available to partner organisations.                      |
| _OrganisationApi_ | [**post_organisation_tokens**](docs/OrganisationApi.md#post_organisation_tokens)                 | **POST** /v1/organisation/tokens           | Generate new API token.                                                                  |
| _OrganisationApi_ | [**post_organisation_users**](docs/OrganisationApi.md#post_organisation_users)                   | **POST** /v1/organisation/users            | Invite a new user to the organisation.                                                   |
| _ReportApi_       | [**get_report_id_commands**](docs/ReportApi.md#get_report_id_commands)                           | **GET** /v1/report/{id}/commands           | Retrieve command log                                                                     |
| _ReportApi_       | [**get_report_usage**](docs/ReportApi.md#get_report_usage)                                       | **GET** /v1/report/usage                   | Retrieve property usage statistics per day per device                                    |
| _UserApi_         | [**delete_user_tokens_id**](docs/UserApi.md#delete_user_tokens_id)                               | **DELETE** /v1/user/tokens/{id}            | Delete a Token. Token will no longer authenticate API requests. This is not recoverable. |
| _UserApi_         | [**get_user**](docs/UserApi.md#get_user)                                                         | **GET** /v1/user                           | Get your Fingoti user.                                                                   |
| _UserApi_         | [**get_user_organisations**](docs/UserApi.md#get_user_organisations)                             | **GET** /v1/user/organisations             | Get all organisations you are a member of.                                               |
| _UserApi_         | [**get_user_sessions**](docs/UserApi.md#get_user_sessions)                                       | **GET** /v1/user/sessions                  | Get all user sessions.                                                                   |
| _UserApi_         | [**get_user_tokens**](docs/UserApi.md#get_user_tokens)                                           | **GET** /v1/user/tokens                    | Get all API tokens.                                                                      |
| _UserApi_         | [**get_user_tokens_id**](docs/UserApi.md#get_user_tokens_id)                                     | **GET** /v1/user/tokens/{id}               | Get specified token.                                                                     |
| _UserApi_         | [**patch_user**](docs/UserApi.md#patch_user)                                                     | **PATCH** /v1/user                         | Update Fingoti user.                                                                     |
| _UserApi_         | [**patch_user_tokens_id**](docs/UserApi.md#patch_user_tokens_id)                                 | **PATCH** /v1/user/tokens/{id}             | Update API token.                                                                        |
| _UserApi_         | [**post_user**](docs/UserApi.md#post_user)                                                       | **POST** /v1/user                          | Register a new Fingoti user.                                                             |
| _UserApi_         | [**post_user_tokens**](docs/UserApi.md#post_user_tokens)                                         | **POST** /v1/user/tokens                   | Generate new API token.                                                                  |
| _WebhookApi_      | [**delete_webhook_id**](docs/WebhookApi.md#delete_webhook_id)                                    | **DELETE** /v1/webhook/{id}                | Delete a Webhook. This is not recoverable.                                               |
| _WebhookApi_      | [**get_webhook**](docs/WebhookApi.md#get_webhook)                                                | **GET** /v1/webhook                        | Get all registered webhooks.                                                             |
| _WebhookApi_      | [**get_webhook_id**](docs/WebhookApi.md#get_webhook_id)                                          | **GET** /v1/webhook/{id}                   | Get specified webhook.                                                                   |
| _WebhookApi_      | [**get_webhook_logs**](docs/WebhookApi.md#get_webhook_logs)                                      | **GET** /v1/webhook/logs                   | Get all registered webhooks with call logs.                                              |
| _WebhookApi_      | [**patch_webhook_id**](docs/WebhookApi.md#patch_webhook_id)                                      | **PATCH** /v1/webhook/{id}                 | Update Fingoti webhook.                                                                  |
| _WebhookApi_      | [**post_webhook**](docs/WebhookApi.md#post_webhook)                                              | **POST** /v1/webhook                       | Register a new webhook.                                                                  |
| _WebhookApi_      | [**post_webhook_retry**](docs/WebhookApi.md#post_webhook_retry)                                  | **POST** /v1/webhook/retry                 | Retry a webhook.                                                                         |

## Documentation For Models

- [AddAddressRequest](docs/AddAddressRequest.md)
- [AddFollowDto](docs/AddFollowDto.md)
- [AddPresetRequest](docs/AddPresetRequest.md)
- [AddPresetResult](docs/AddPresetResult.md)
- [AddRoleRequest](docs/AddRoleRequest.md)
- [AddWebhookDto](docs/AddWebhookDto.md)
- [AddWebhookResult](docs/AddWebhookResult.md)
- [AllWebhooksDto](docs/AllWebhooksDto.md)
- [AzureMessage](docs/AzureMessage.md)
- [AzureMessageContent](docs/AzureMessageContent.md)
- [CallLogDto](docs/CallLogDto.md)
- [ClaimRequest](docs/ClaimRequest.md)
- [ClaimResult](docs/ClaimResult.md)
- [ClaimedDeviceResponse](docs/ClaimedDeviceResponse.md)
- [ClaimedDevicesDto](docs/ClaimedDevicesDto.md)
- [CloudReason](docs/CloudReason.md)
- [CommandDirection](docs/CommandDirection.md)
- [CommandLogResponse](docs/CommandLogResponse.md)
- [DataLogResponse](docs/DataLogResponse.md)
- [Default](docs/Default.md)
- [DefaultWithId](docs/DefaultWithId.md)
- [DefaultWithToken](docs/DefaultWithToken.md)
- [DeviceBlink](docs/DeviceBlink.md)
- [DeviceBus](docs/DeviceBus.md)
- [DeviceCloud](docs/DeviceCloud.md)
- [DeviceLocation](docs/DeviceLocation.md)
- [DeviceNodesResponse](docs/DeviceNodesResponse.md)
- [DevicePeblDto](docs/DevicePeblDto.md)
- [DevicePower](docs/DevicePower.md)
- [DeviceRequest](docs/DeviceRequest.md)
- [DeviceSession](docs/DeviceSession.md)
- [DeviceSupport](docs/DeviceSupport.md)
- [DeviceUptime](docs/DeviceUptime.md)
- [DeviceVersion](docs/DeviceVersion.md)
- [DeviceVyneDto](docs/DeviceVyneDto.md)
- [EngineWebhookDto](docs/EngineWebhookDto.md)
- [EngineWebhookResponse](docs/EngineWebhookResponse.md)
- [EngineWebhooksResponse](docs/EngineWebhooksResponse.md)
- [GatewayClaim](docs/GatewayClaim.md)
- [GatewayGpio](docs/GatewayGpio.md)
- [GatewayI2c](docs/GatewayI2c.md)
- [GatewayMqtt](docs/GatewayMqtt.md)
- [GatewayNetwork](docs/GatewayNetwork.md)
- [GatewayNode](docs/GatewayNode.md)
- [GatewaySchedule](docs/GatewaySchedule.md)
- [GatewayTimer](docs/GatewayTimer.md)
- [GatewayUart](docs/GatewayUart.md)
- [GatewayWifi](docs/GatewayWifi.md)
- [GetProfileResponse](docs/GetProfileResponse.md)
- [I2cSetup](docs/I2cSetup.md)
- [InviteUserDto](docs/InviteUserDto.md)
- [LocationPort](docs/LocationPort.md)
- [MessageType](docs/MessageType.md)
- [MqttDeviceResponse](docs/MqttDeviceResponse.md)
- [MqttSetup](docs/MqttSetup.md)
- [MqttStatus](docs/MqttStatus.md)
- [NetworkIp](docs/NetworkIp.md)
- [NetworkMac](docs/NetworkMac.md)
- [NewOrganisationTokenDto](docs/NewOrganisationTokenDto.md)
- [NewUserTokenDto](docs/NewUserTokenDto.md)
- [NodeAddress](docs/NodeAddress.md)
- [NodeData](docs/NodeData.md)
- [NodeDetect](docs/NodeDetect.md)
- [NodeLocation](docs/NodeLocation.md)
- [OrganisationAddressResponse](docs/OrganisationAddressResponse.md)
- [OrganisationAddressesDto](docs/OrganisationAddressesDto.md)
- [OrganisationFollowing](docs/OrganisationFollowing.md)
- [OrganisationFollowingResponse](docs/OrganisationFollowingResponse.md)
- [OrganisationPartnerResponse](docs/OrganisationPartnerResponse.md)
- [OrganisationPresetResponse](docs/OrganisationPresetResponse.md)
- [OrganisationPresetsDto](docs/OrganisationPresetsDto.md)
- [OrganisationResponse](docs/OrganisationResponse.md)
- [OrganisationRoleResponse](docs/OrganisationRoleResponse.md)
- [OrganisationRolesDto](docs/OrganisationRolesDto.md)
- [OrganisationTenantDto](docs/OrganisationTenantDto.md)
- [OrganisationTenantsResponse](docs/OrganisationTenantsResponse.md)
- [OrganisationUserResponse](docs/OrganisationUserResponse.md)
- [OrganisationUsersDto](docs/OrganisationUsersDto.md)
- [PartnerAddress](docs/PartnerAddress.md)
- [PartnerContact](docs/PartnerContact.md)
- [PatchAddressRequest](docs/PatchAddressRequest.md)
- [PatchDevice](docs/PatchDevice.md)
- [PatchFollowRequest](docs/PatchFollowRequest.md)
- [PatchGateway](docs/PatchGateway.md)
- [PatchOrganisationRequest](docs/PatchOrganisationRequest.md)
- [PatchOrganisationTokenRequest](docs/PatchOrganisationTokenRequest.md)
- [PatchPresetRequest](docs/PatchPresetRequest.md)
- [PatchRoleRequest](docs/PatchRoleRequest.md)
- [PatchUserRequest](docs/PatchUserRequest.md)
- [PatchUserTokenRequest](docs/PatchUserTokenRequest.md)
- [PatchWebhookRequest](docs/PatchWebhookRequest.md)
- [PeblDevice](docs/PeblDevice.md)
- [PeblGateway](docs/PeblGateway.md)
- [PortalUserOrganisationsDto](docs/PortalUserOrganisationsDto.md)
- [RegiserOrganisationDto](docs/RegiserOrganisationDto.md)
- [RegiserTenantDto](docs/RegiserTenantDto.md)
- [RegisterOrganisationResult](docs/RegisterOrganisationResult.md)
- [RegisterUserDto](docs/RegisterUserDto.md)
- [RequestOperation](docs/RequestOperation.md)
- [ScheduleSetup](docs/ScheduleSetup.md)
- [ScheduleStatus](docs/ScheduleStatus.md)
- [TimerRequest](docs/TimerRequest.md)
- [TimerStatus](docs/TimerStatus.md)
- [TokenSuccessResponse](docs/TokenSuccessResponse.md)
- [UartSetup](docs/UartSetup.md)
- [UartTrigger](docs/UartTrigger.md)
- [UpdateRequest](docs/UpdateRequest.md)
- [UpdateResponse](docs/UpdateResponse.md)
- [UpdateUserRole](docs/UpdateUserRole.md)
- [UsageTracking](docs/UsageTracking.md)
- [UsageTrackingResponse](docs/UsageTrackingResponse.md)
- [UserOrganisationsDto](docs/UserOrganisationsDto.md)
- [UserSessionsDto](docs/UserSessionsDto.md)
- [UserSessionsResponse](docs/UserSessionsResponse.md)
- [UserTokenDto](docs/UserTokenDto.md)
- [UserTokenResponse](docs/UserTokenResponse.md)
- [VyneDevice](docs/VyneDevice.md)
- [VyneGateway](docs/VyneGateway.md)
- [VyneNode](docs/VyneNode.md)
- [WebhookAttempts](docs/WebhookAttempts.md)
- [WebhookCallDto](docs/WebhookCallDto.md)
- [WebhookHeaders](docs/WebhookHeaders.md)
- [WebhookLogsResponse](docs/WebhookLogsResponse.md)
- [WebhookRetry](docs/WebhookRetry.md)
- [WebhookRetryRequest](docs/WebhookRetryRequest.md)
- [WebhookStatus](docs/WebhookStatus.md)
- [WifiDetect](docs/WifiDetect.md)
- [WifiSlot](docs/WifiSlot.md)
- [WifiStatus](docs/WifiStatus.md)

## Documentation For Authorization

## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header

## Author

## Notes for Large OpenAPI documents

If the OpenAPI document is large, imports in fingoti.apis and fingoti.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:

- `from fingoti.api.default_api import DefaultApi`
- `from fingoti.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:

```
import sys
sys.setrecursionlimit(1500)
import fingoti
from fingoti.apis import *
from fingoti.models import *
```
