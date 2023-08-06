"""
Options with default values
"""
from dataclasses import dataclass, field


@dataclass
class Options:
    """
    Can be changed with e.g. Options.aim_id = False
    """
    xml_header: bool = field(default=False)
    dump: bool = field(default=False)
    no_pixel_data: bool = field(default=False)


@dataclass
class Settings:
    """
    Can be changed with e.g. Settings.total_retries = 5
    """
    total_retries: int = field(default=10)
    timeout_seconds: int = field(default=2)
    backoff_factor: int = field(default=5)
    file_type: str = field(default='image')
