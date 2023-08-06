import typing_extensions

from vrt_lss_studio.apis.tags import TagValues
from vrt_lss_studio.apis.tags.explorer_api import ExplorerApi
from vrt_lss_studio.apis.tags.experiments_api import ExperimentsApi
from vrt_lss_studio.apis.tags.locations_api import LocationsApi
from vrt_lss_studio.apis.tags.performers_api import PerformersApi
from vrt_lss_studio.apis.tags.transports_api import TransportsApi
from vrt_lss_studio.apis.tags.orders_api import OrdersApi
from vrt_lss_studio.apis.tags.hardlinks_api import HardlinksApi
from vrt_lss_studio.apis.tags.trips_api import TripsApi
from vrt_lss_studio.apis.tags.facts_api import FactsApi
from vrt_lss_studio.apis.tags.system_api import SystemApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.EXPLORER: ExplorerApi,
        TagValues.EXPERIMENTS: ExperimentsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.PERFORMERS: PerformersApi,
        TagValues.TRANSPORTS: TransportsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.HARDLINKS: HardlinksApi,
        TagValues.TRIPS: TripsApi,
        TagValues.FACTS: FactsApi,
        TagValues.SYSTEM: SystemApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.EXPLORER: ExplorerApi,
        TagValues.EXPERIMENTS: ExperimentsApi,
        TagValues.LOCATIONS: LocationsApi,
        TagValues.PERFORMERS: PerformersApi,
        TagValues.TRANSPORTS: TransportsApi,
        TagValues.ORDERS: OrdersApi,
        TagValues.HARDLINKS: HardlinksApi,
        TagValues.TRIPS: TripsApi,
        TagValues.FACTS: FactsApi,
        TagValues.SYSTEM: SystemApi,
    }
)
