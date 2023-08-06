from vrt_lss_studio.paths.studio_experiments_experiment_key.get import ApiForget
from vrt_lss_studio.paths.studio_experiments_experiment_key.put import ApiForput
from vrt_lss_studio.paths.studio_experiments_experiment_key.delete import ApiFordelete


class StudioExperimentsExperimentKey(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
