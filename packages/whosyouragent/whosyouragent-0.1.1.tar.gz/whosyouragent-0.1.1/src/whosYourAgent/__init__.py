import os
import time
from pathlib import Path

from .whosYourAgent import VersionUpdater, getAgent

browsersPath = Path(__file__).parent / "browserVersions.json"
if (
    not browsersPath.exists()
    or time.time() - os.stat(str(browsersPath)).st_mtime > 604800
):  # 1 week
    updater = VersionUpdater()
    updater.updateAll()
