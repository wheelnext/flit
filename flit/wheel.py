import logging

import flit_core.wheel as core_wheel

log = logging.getLogger(__name__)

def make_wheel_in(ini_path, wheel_directory, editable=False, vprops: list[str] | None = None):
    return core_wheel.make_wheel_in(ini_path, wheel_directory, editable, vprops)

class WheelBuilder(core_wheel.WheelBuilder):
    pass
