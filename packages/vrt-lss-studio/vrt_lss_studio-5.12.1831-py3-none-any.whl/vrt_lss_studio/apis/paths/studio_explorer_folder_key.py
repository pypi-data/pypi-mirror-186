from vrt_lss_studio.paths.studio_explorer_folder_key.get import ApiForget
from vrt_lss_studio.paths.studio_explorer_folder_key.put import ApiForput
from vrt_lss_studio.paths.studio_explorer_folder_key.delete import ApiFordelete


class StudioExplorerFolderKey(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
