# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from vrt_lss_studio.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    EXPLORER = "Explorer"
    EXPERIMENTS = "Experiments"
    LOCATIONS = "Locations"
    PERFORMERS = "Performers"
    TRANSPORTS = "Transports"
    ORDERS = "Orders"
    HARDLINKS = "Hardlinks"
    TRIPS = "Trips"
    FACTS = "Facts"
    SYSTEM = "System"
