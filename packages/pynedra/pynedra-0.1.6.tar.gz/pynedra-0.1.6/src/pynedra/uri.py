"""
Utilities for DICOMweb URI manipulation.
"""
from __future__ import annotations

from enum import Enum
from typing import Optional
from dataclasses import dataclass

from .options import Settings


class URISuffix(Enum):
    XML = 'xml'
    XML_DUMP = 'xml?dump=1'
    XML_NO_PIXEL = 'xml?no_pixel_data=1'
    XML_NO_PIXEL_DUMP = 'xml?no_pixel_data=1&dump=1'
    DUMP = '?dump=1'
    NO_PIXEL = '?no_pixel_data=1'
    NO_PIXEL_DUMP = '?no_pixel_data=1&dump=1'


@dataclass
class URI:
    base_url: str
    study_uid: Optional[str] = None
    series_uid: Optional[str] = None
    sop_uid: Optional[str] = None
    suffix: Optional[URISuffix] = None
    aim_id: Optional[str] = None

    def __post_init__(self):
        self.root_url = self.base_url.split('/refptr')[0]

    def __str__(self) -> str:
        """
        Returns the object as a DICOMweb URI string.
        """
        if self.aim_id is None:
            parts = (self.study_uid, self.series_uid, self.sop_uid)
            dicomweb_suffix = ''.join(f'{part}-' for part in parts if part is not None).rstrip('-')

            # URI for metadata
            if self.suffix is not None:
                dicomweb_suffix = f"{dicomweb_suffix}.{self.suffix.value}"

            return f'{self.base_url}{dicomweb_suffix}'

        else:
            # URI for image extraction
            if self.suffix is not None:
                return f'{self.root_url}/{Settings.file_type}/{self.aim_id}.{self.suffix.value}'

            return f'{self.root_url}/{Settings.file_type}/{self.aim_id}'
