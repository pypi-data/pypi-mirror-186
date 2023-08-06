import typing_extensions

from vrt_lss_studio.paths import PathValues
from vrt_lss_studio.apis.paths.studio_explorer import StudioExplorer
from vrt_lss_studio.apis.paths.studio_explorer_folder_key import StudioExplorerFolderKey
from vrt_lss_studio.apis.paths.studio_explorer_folder_key_duplication import StudioExplorerFolderKeyDuplication
from vrt_lss_studio.apis.paths.studio_experiments import StudioExperiments
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key import StudioExperimentsExperimentKey
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_duplication import StudioExperimentsExperimentKeyDuplication
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_settings import StudioExperimentsExperimentKeySettings
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_indicators import StudioExperimentsExperimentKeyIndicators
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_calculation_process_name import StudioExperimentsExperimentKeyCalculationProcessName
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_calculation import StudioExperimentsExperimentKeyCalculation
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_validation_process_name import StudioExperimentsExperimentKeyValidationProcessName
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_share import StudioExperimentsExperimentKeyShare
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_import_xlsx import StudioExperimentsExperimentKeyImportXlsx
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_import_json import StudioExperimentsExperimentKeyImportJson
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_import_json_url import StudioExperimentsExperimentKeyImportJsonUrl
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_export_xlsx import StudioExperimentsExperimentKeyExportXlsx
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_export_json import StudioExperimentsExperimentKeyExportJson
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_locations_list import StudioExperimentsExperimentKeyLocationsList
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_locations import StudioExperimentsExperimentKeyLocations
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_locations_essence_key import StudioExperimentsExperimentKeyLocationsEssenceKey
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_locations_geopoints import StudioExperimentsExperimentKeyLocationsGeopoints
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_performers_list import StudioExperimentsExperimentKeyPerformersList
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_performers import StudioExperimentsExperimentKeyPerformers
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_performers_essence_key import StudioExperimentsExperimentKeyPerformersEssenceKey
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_performers_geopoints import StudioExperimentsExperimentKeyPerformersGeopoints
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_transports_list import StudioExperimentsExperimentKeyTransportsList
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_transports import StudioExperimentsExperimentKeyTransports
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_transports_essence_key import StudioExperimentsExperimentKeyTransportsEssenceKey
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_transports_geopoints import StudioExperimentsExperimentKeyTransportsGeopoints
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_orders_list import StudioExperimentsExperimentKeyOrdersList
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_orders import StudioExperimentsExperimentKeyOrders
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_orders_essence_key import StudioExperimentsExperimentKeyOrdersEssenceKey
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_orders_geopoints import StudioExperimentsExperimentKeyOrdersGeopoints
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_hardlinks_list import StudioExperimentsExperimentKeyHardlinksList
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_hardlinks import StudioExperimentsExperimentKeyHardlinks
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_hardlinks_essence_key import StudioExperimentsExperimentKeyHardlinksEssenceKey
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_trips_list import StudioExperimentsExperimentKeyTripsList
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_trips import StudioExperimentsExperimentKeyTrips
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_trips_essence_key import StudioExperimentsExperimentKeyTripsEssenceKey
from vrt_lss_studio.apis.paths.studio_experiments_experiment_key_trips_tracks import StudioExperimentsExperimentKeyTripsTracks
from vrt_lss_studio.apis.paths.studio_system_check import StudioSystemCheck
from vrt_lss_studio.apis.paths.studio_system_version import StudioSystemVersion
from vrt_lss_studio.apis.paths.studio_file_filename import StudioFileFilename

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.STUDIO_EXPLORER: StudioExplorer,
        PathValues.STUDIO_EXPLORER_FOLDER_KEY: StudioExplorerFolderKey,
        PathValues.STUDIO_EXPLORER_FOLDER_KEY_DUPLICATION: StudioExplorerFolderKeyDuplication,
        PathValues.STUDIO_EXPERIMENTS: StudioExperiments,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY: StudioExperimentsExperimentKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_DUPLICATION: StudioExperimentsExperimentKeyDuplication,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_SETTINGS: StudioExperimentsExperimentKeySettings,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_INDICATORS: StudioExperimentsExperimentKeyIndicators,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_CALCULATION_PROCESS_NAME: StudioExperimentsExperimentKeyCalculationProcessName,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_CALCULATION: StudioExperimentsExperimentKeyCalculation,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_VALIDATION_PROCESS_NAME: StudioExperimentsExperimentKeyValidationProcessName,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_SHARE: StudioExperimentsExperimentKeyShare,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_IMPORT_XLSX: StudioExperimentsExperimentKeyImportXlsx,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_IMPORT_JSON: StudioExperimentsExperimentKeyImportJson,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_IMPORT_JSON_URL: StudioExperimentsExperimentKeyImportJsonUrl,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_EXPORT_XLSX: StudioExperimentsExperimentKeyExportXlsx,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_EXPORT_JSON: StudioExperimentsExperimentKeyExportJson,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_LOCATIONS_LIST: StudioExperimentsExperimentKeyLocationsList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_LOCATIONS: StudioExperimentsExperimentKeyLocations,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_LOCATIONS_ESSENCE_KEY: StudioExperimentsExperimentKeyLocationsEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_LOCATIONS_GEOPOINTS: StudioExperimentsExperimentKeyLocationsGeopoints,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_PERFORMERS_LIST: StudioExperimentsExperimentKeyPerformersList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_PERFORMERS: StudioExperimentsExperimentKeyPerformers,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_PERFORMERS_ESSENCE_KEY: StudioExperimentsExperimentKeyPerformersEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_PERFORMERS_GEOPOINTS: StudioExperimentsExperimentKeyPerformersGeopoints,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRANSPORTS_LIST: StudioExperimentsExperimentKeyTransportsList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRANSPORTS: StudioExperimentsExperimentKeyTransports,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRANSPORTS_ESSENCE_KEY: StudioExperimentsExperimentKeyTransportsEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRANSPORTS_GEOPOINTS: StudioExperimentsExperimentKeyTransportsGeopoints,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_ORDERS_LIST: StudioExperimentsExperimentKeyOrdersList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_ORDERS: StudioExperimentsExperimentKeyOrders,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_ORDERS_ESSENCE_KEY: StudioExperimentsExperimentKeyOrdersEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_ORDERS_GEOPOINTS: StudioExperimentsExperimentKeyOrdersGeopoints,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_HARDLINKS_LIST: StudioExperimentsExperimentKeyHardlinksList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_HARDLINKS: StudioExperimentsExperimentKeyHardlinks,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_HARDLINKS_ESSENCE_KEY: StudioExperimentsExperimentKeyHardlinksEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRIPS_LIST: StudioExperimentsExperimentKeyTripsList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRIPS: StudioExperimentsExperimentKeyTrips,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRIPS_ESSENCE_KEY: StudioExperimentsExperimentKeyTripsEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRIPS_TRACKS: StudioExperimentsExperimentKeyTripsTracks,
        PathValues.STUDIO_SYSTEM_CHECK: StudioSystemCheck,
        PathValues.STUDIO_SYSTEM_VERSION: StudioSystemVersion,
        PathValues.STUDIO_FILE_FILENAME: StudioFileFilename,
    }
)

path_to_api = PathToApi(
    {
        PathValues.STUDIO_EXPLORER: StudioExplorer,
        PathValues.STUDIO_EXPLORER_FOLDER_KEY: StudioExplorerFolderKey,
        PathValues.STUDIO_EXPLORER_FOLDER_KEY_DUPLICATION: StudioExplorerFolderKeyDuplication,
        PathValues.STUDIO_EXPERIMENTS: StudioExperiments,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY: StudioExperimentsExperimentKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_DUPLICATION: StudioExperimentsExperimentKeyDuplication,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_SETTINGS: StudioExperimentsExperimentKeySettings,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_INDICATORS: StudioExperimentsExperimentKeyIndicators,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_CALCULATION_PROCESS_NAME: StudioExperimentsExperimentKeyCalculationProcessName,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_CALCULATION: StudioExperimentsExperimentKeyCalculation,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_VALIDATION_PROCESS_NAME: StudioExperimentsExperimentKeyValidationProcessName,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_SHARE: StudioExperimentsExperimentKeyShare,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_IMPORT_XLSX: StudioExperimentsExperimentKeyImportXlsx,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_IMPORT_JSON: StudioExperimentsExperimentKeyImportJson,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_IMPORT_JSON_URL: StudioExperimentsExperimentKeyImportJsonUrl,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_EXPORT_XLSX: StudioExperimentsExperimentKeyExportXlsx,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_EXPORT_JSON: StudioExperimentsExperimentKeyExportJson,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_LOCATIONS_LIST: StudioExperimentsExperimentKeyLocationsList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_LOCATIONS: StudioExperimentsExperimentKeyLocations,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_LOCATIONS_ESSENCE_KEY: StudioExperimentsExperimentKeyLocationsEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_LOCATIONS_GEOPOINTS: StudioExperimentsExperimentKeyLocationsGeopoints,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_PERFORMERS_LIST: StudioExperimentsExperimentKeyPerformersList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_PERFORMERS: StudioExperimentsExperimentKeyPerformers,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_PERFORMERS_ESSENCE_KEY: StudioExperimentsExperimentKeyPerformersEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_PERFORMERS_GEOPOINTS: StudioExperimentsExperimentKeyPerformersGeopoints,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRANSPORTS_LIST: StudioExperimentsExperimentKeyTransportsList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRANSPORTS: StudioExperimentsExperimentKeyTransports,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRANSPORTS_ESSENCE_KEY: StudioExperimentsExperimentKeyTransportsEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRANSPORTS_GEOPOINTS: StudioExperimentsExperimentKeyTransportsGeopoints,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_ORDERS_LIST: StudioExperimentsExperimentKeyOrdersList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_ORDERS: StudioExperimentsExperimentKeyOrders,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_ORDERS_ESSENCE_KEY: StudioExperimentsExperimentKeyOrdersEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_ORDERS_GEOPOINTS: StudioExperimentsExperimentKeyOrdersGeopoints,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_HARDLINKS_LIST: StudioExperimentsExperimentKeyHardlinksList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_HARDLINKS: StudioExperimentsExperimentKeyHardlinks,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_HARDLINKS_ESSENCE_KEY: StudioExperimentsExperimentKeyHardlinksEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRIPS_LIST: StudioExperimentsExperimentKeyTripsList,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRIPS: StudioExperimentsExperimentKeyTrips,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRIPS_ESSENCE_KEY: StudioExperimentsExperimentKeyTripsEssenceKey,
        PathValues.STUDIO_EXPERIMENTS_EXPERIMENT_KEY_TRIPS_TRACKS: StudioExperimentsExperimentKeyTripsTracks,
        PathValues.STUDIO_SYSTEM_CHECK: StudioSystemCheck,
        PathValues.STUDIO_SYSTEM_VERSION: StudioSystemVersion,
        PathValues.STUDIO_FILE_FILENAME: StudioFileFilename,
    }
)
