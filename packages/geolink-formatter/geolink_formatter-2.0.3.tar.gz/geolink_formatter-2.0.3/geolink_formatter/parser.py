# -*- coding: utf-8 -*-
import datetime
import pkg_resources
import requests
from lxml.etree import DTD, DocumentInvalid, fromstring
from xmlschema import XMLSchema11
from geolink_formatter.entity import Document, File


class SCHEMA(object):
    """Provides the available geoLink schema versions."""

    V1_0_0 = '1.0.0'
    """str: geoLink schema version 1.0.0"""

    V1_1_0 = '1.1.0'
    """str: geoLink schema version 1.1.0"""

    V1_1_1 = '1.1.1'
    """str: geoLink schema version 1.1.1"""

    V1_2_0 = '1.2.0'
    """str: geoLink schema version 1.2.0"""

    V1_2_1 = '1.2.1'
    """str: geoLink schema version 1.2.1"""

    V1_2_2 = '1.2.2'
    """str: geoLink schema version 1.2.2"""


class XML(object):

    _date_format = '%Y-%m-%d'
    """str: Format of date values in XML."""

    def __init__(self, host_url=None, version='1.2.2', dtd_validation=False, xsd_validation=True):
        """Create a new XML parser instance containing the geoLink XSD for validation.

        Args:
            host_url (str): URL of the OEREBlex host to resolve relative URLs. The complete URL until but
                without the */api* part has to be set, starting with *http://* or *https://*.
            version (str): The version of the geoLink schema to be used. Defaults to `1.2.0`.
            dtd_validation (bool): Enable/disable validation of document type definition (DTD).
                Optional, defaults to False.
            xsd_validation (bool): Enable/disable validation against XML schema (XSD).
                Optional, defaults to True.

        """
        self._host_url = host_url
        self._version = version
        self._dtd_validation = dtd_validation
        self._xsd_validation = xsd_validation
        xsd = pkg_resources.resource_filename('geolink_formatter', 'schema/v{0}.xsd'.format(version))
        if self._xsd_validation:
            with open(xsd, encoding='utf-8') as f:
                self._schema = XMLSchema11(f.read())

    @property
    def host_url(self):
        """str: The OEREBlex host URL to resolve relative URLs."""
        return self._host_url

    def _parse_xml(self, xml):
        """Parses the specified XML string and validates it against the geoLink XSD.

        Args:
            xml (str or bytes): The XML to be parsed.

        Returns:
            lxml.etree._Element: The root element of the parsed geoLink XML.

        Raises:
            lxml.etree.XMLSyntaxError: Raised on failed validation.

        """
        if isinstance(xml, bytes):
            content = fromstring(xml)
        else:
            content = fromstring(xml.encode('utf-16be'))
        if self._xsd_validation:
            self._schema.validate(content)
        if self._dtd_validation:
            dtd = content.getroottree().docinfo.internalDTD
            if isinstance(dtd, DTD):
                dtd.assertValid(content)
            else:
                raise DocumentInvalid('Missing DTD in parsed content')
        return content

    def from_string(self, xml):
        """Parses XML into internal structure.

        The specified XML string is gets validated against the geoLink XSD on parsing.

        Args:
            xml (str or bytes): The XML to be parsed.

        Returns:
            list[geolink_formatter.entity.Document]: A list containing the parsed document elements.

        Raises:
            lxml.etree.XMLSyntaxError: Raised on failed validation.
        """
        root = self._parse_xml(xml)
        documents = list()

        for document_el in root.iter('document'):
            doc_id = document_el.attrib.get('id')
            doctype = document_el.attrib.get('doctype')

            # Mangle doc_id for notices. While IDs are unique between decrees
            # and edicts, this is not the case when adding notices to the mix.
            if doctype == 'notice':
                doc_id += doctype

            if doc_id and doc_id not in [doc.id for doc in documents]:
                files = list()
                for file_el in document_el.iter('file'):
                    href = file_el.attrib.get('href')
                    if self.host_url and not href.startswith(u'http://') and not href.startswith(u'https://'):
                        href = u'{host}{href}'.format(host=self.host_url, href=href)
                    files.append(File(
                        title=file_el.attrib.get('title'),
                        description=file_el.attrib.get('description'),
                        href=href,
                        category=file_el.attrib.get('category')
                    ))
                enactment_date = document_el.attrib.get('enactment_date')
                if enactment_date:
                    enactment_date = datetime.datetime.strptime(enactment_date, self._date_format).date()
                decree_date = document_el.attrib.get('decree_date')
                if decree_date:
                    decree_date = datetime.datetime.strptime(decree_date, self._date_format).date()
                abrogation_date = document_el.attrib.get('abrogation_date')
                if abrogation_date:
                    abrogation_date = datetime.datetime.strptime(abrogation_date, self._date_format).date()
                status_start_date = document_el.attrib.get('status_start_date')
                if status_start_date:
                    status_start_date = datetime.datetime.strptime(status_start_date, self._date_format)\
                                                         .date()
                status_end_date = document_el.attrib.get('status_end_date')
                if status_end_date:
                    status_end_date = datetime.datetime.strptime(status_end_date, self._date_format)\
                                                        .date()

                documents.append(Document(
                    files=files,
                    id=doc_id,
                    category=document_el.attrib.get('category'),
                    doctype=document_el.attrib.get('doctype'),
                    federal_level=document_el.attrib.get('federal_level'),
                    authority=document_el.attrib.get('authority'),
                    authority_url=document_el.attrib.get('authority_url'),
                    title=document_el.attrib.get('title'),
                    number=document_el.attrib.get('number'),
                    abbreviation=document_el.attrib.get('abbreviation'),
                    instance=document_el.attrib.get('instance'),
                    type=document_el.attrib.get('type'),
                    subtype=document_el.attrib.get('subtype'),
                    decree_date=decree_date,
                    enactment_date=enactment_date,
                    abrogation_date=abrogation_date,
                    cycle=document_el.attrib.get('cycle'),
                    municipality=document_el.attrib.get('municipality'),
                    index=document_el.attrib.get('index'),
                    status=document_el.attrib.get('status'),
                    status_start_date=status_start_date,
                    status_end_date=status_end_date
                ))

        return documents

    def from_url(self, url, params=None, **kwargs):
        """Loads the geoLink of the specified URL and parses it into the internal structure.

        Args:
            url (str): The URL of the geoLink to be parsed.
            params (dict): Dictionary or bytes to be sent in the query string for the
                :class:`requests.models.Request`.
            **kwargs: Optional arguments that ``requests.api.request`` takes.

        Returns:
            list[geolink_formatter.entity.Document]: A list containing the parsed document elements.

        Raises:
            lxml.etree.XMLSyntaxError: Raised on failed validation.
            requests.HTTPError: Raised on failed HTTP request.

        """
        response = requests.get(url, params=params, **kwargs)
        if response.status_code == 200:
            return self.from_string(response.content)
        else:
            response.raise_for_status()
