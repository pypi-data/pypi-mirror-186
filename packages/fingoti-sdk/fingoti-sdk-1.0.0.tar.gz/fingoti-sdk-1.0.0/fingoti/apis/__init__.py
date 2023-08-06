
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from fingoti.api.device_api import DeviceApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from fingoti.api.device_api import DeviceApi
from fingoti.api.followings_api import FollowingsApi
from fingoti.api.organisation_api import OrganisationApi
from fingoti.api.report_api import ReportApi
from fingoti.api.user_api import UserApi
from fingoti.api.webhook_api import WebhookApi
