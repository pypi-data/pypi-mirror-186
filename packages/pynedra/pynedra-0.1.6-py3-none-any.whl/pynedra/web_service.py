"""
Pynedra

This module provides a set of functions to communicate with the
webservice of the long-term storage and archiving solution of Synedra.

The module requires valid certificate and certificate key *.pem files
to establish a connection to the server.
"""
import io
from dataclasses import dataclass, field
from typing import Optional, Tuple
import xmltodict
from pydicom import dcmread
from pydicom.dataset import Dataset
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from requests import Session
import xml.etree.ElementTree as ET

from .options import Options, Settings
from .uri import URI, URISuffix


class AlreadyConnected(Exception):
    pass


class CannotConnectError(Exception):
    pass


@dataclass
class Pynedra:
    """
    Class for Synedra Webservice
    """
    uid_tuple: tuple
    base_url: str
    certificate_bundle: Optional[Tuple[str, str]]
    session: Session() = field(init=False, default=None)
    url: URI = field(init=False)

    def __post_init__(self):
        self._start_session()
        self.url = URI(f'{self.base_url}',
                       self.uid_tuple[0],
                       self.uid_tuple[1],
                       self.uid_tuple[2],
                       URISuffix.XML)

    def _start_session(self):
        """
        Custom adapter with timeout properties / options - see implementation in class below

        Setup session and mount the adapter to both the http:// and https:// endpoint
        """
        if self.session is None:
            self.session = Session()
            self.session.cert = self.certificate_bundle
            self.session.verify = False       # should be True!!!
            self.session.stream = False

            try:
                if Settings.total_retries > 0:
                    adapter = HTTPAdapter(
                        max_retries=Retry(total=Settings.total_retries,
                                          backoff_factor=Settings.backoff_factor,
                                          status_forcelist=[413, 429, 500, 502, 503, 504],
                                          allowed_methods=["HEAD", "GET", "OPTIONS"],
                                          ),
                    )
                    for prefix in "http://", "https://":
                        self.session.mount(prefix, adapter)
            except CannotConnectError as ex:
                raise CannotConnectError('Connection not possible!') from ex
        else:
            raise AlreadyConnected('Transport is already connected')

    def get_metadata(self) -> dict:
        """
        Get meta data of dicom image as dictionary.
        """
        with self.session.get(str(self.url)) as results:
            if results.status_code == 200:
                dict_result = xmltodict.parse(results.text)
                return dict_result
            return {}

    def get_dicom(self) -> Optional[Dataset]:
        """
        Get dicom image.
        """
        dicom_content = None
        with self.session.get(str(self.get_url())) as results:
            if results.status_code == 200:
                for chunk in results.iter_content(chunk_size=None, decode_unicode=True):
                    if chunk:
                        dicom_content = dcmread(io.BytesIO(chunk), force=True)
            return dicom_content

    def get_url(self) -> URI:
        """
        Get URI out of different options.
        """
        aim_id = self.get_metadata()['aimInfo']['dicomStudy']['dicomSeries']['dicomImage']['@aimId']
        if Options.xml_header:
            if Options.no_pixel_data and Options.dump:
                return URI(self.base_url, aim_id=aim_id, suffix=URISuffix.XML_NO_PIXEL_DUMP)
            if Options.no_pixel_data:
                return URI(self.base_url, aim_id=aim_id, suffix=URISuffix.XML_NO_PIXEL)
            if Options.dump:
                return URI(self.base_url, aim_id=aim_id, suffix=URISuffix.XML_DUMP)
            return URI(self.base_url, aim_id=aim_id, suffix=URISuffix.XML)

        else:
            if Options.no_pixel_data and Options.dump:
                return URI(self.base_url, aim_id=aim_id, suffix=URISuffix.NO_PIXEL_DUMP)
            if Options.no_pixel_data:
                return URI(self.base_url, aim_id=aim_id, suffix=URISuffix.NO_PIXEL)
            if Options.dump:
                return URI(self.base_url, aim_id=aim_id, suffix=URISuffix.DUMP)
            return URI(self.base_url, aim_id=aim_id)

    def get_xml_file(self) -> ET:
        """
        Get xml header.
        """
        with self.session.get(str(self.get_url())) as results:
            if results.status_code == 200:
                start = results.text.find('<?xml')
                end = results.text.find('</textarea>')
                return ET.fromstring(results.text[start:end])

    def get_file(self):
        """
        Get a file - implementation not yet finished.
        """
        with self.session.get(str(self.get_url())) as results:
            if results.status_code == 200:
                return results
