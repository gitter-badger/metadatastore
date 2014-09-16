
__author__ = 'arkilic'

import getpass
from metadataStore.database.utility import validate_dict, validate_string, validate_end_time, \
    validate_start_time, validate_int, validate_list
from metadataStore.sessionManager.databaseInit import db


class Header(object):
    """
    Run Header that captures all aspects of a given run using its keys and other collections
    """
    def __init__(self, start_time, scan_id, beamline_id=None, header_versions=list(), status='In Progress', owner=getpass.getuser(),
                 end_time=None, tags=list(), custom=dict()):
        """
        :param start_time: run header initialization timestamp
        :type start_time: datetime object
        :param end_time: run header close timestamp
        :type  end_time: datetime object
        :param owner: data collection or system defined user info
        :type owner: string
        :param scan_id: unique identifier describing a given run
        :type scan_id: str or int
        :param beamline_id: descriptor for beamline
        :type beamline_id: string
        :param custom: dictionary field for custom information
        :type custom: dictionary
        """
        self.start_time = validate_start_time(start_time)
        self.end_time = validate_end_time(end_time)
        self.owner = validate_string(owner)
        self.header_versions = validate_list(header_versions)
        self.scan_id = scan_id
        self.tags = validate_list(tags)
        self.status = validate_string(status)
        self.beamline_id = validate_string(beamline_id)
        self.custom = validate_dict(custom)

    def __compose_document(self):
        """
        Composes a python dictionary used in order to insert into 'header' collection
        """
        document_template = dict()
        document_template['start_time'] = self.start_time
        document_template['end_time'] = self.end_time
        document_template['owner'] = self.owner
        document_template['scan_id'] = self.scan_id
        document_template['status'] = self.status
        document_template['beamline_id'] = self.beamline_id
        document_template['header_versions'] = self.header_versions
        document_template['custom'] = self.custom
        document_template['tags'] = self.tags
        return document_template

    def save(self, **kwargs):
        """
        Inserts a header into metadataStore.header collection. Also, handles uniqueness and indexing.
        """
        composed_dict = self.__compose_document()
        _id = db['header'].insert(composed_dict, **kwargs)
        db['header'].ensure_index([('scan_id', -1)], unique=True)
        db['header'].ensure_index([('owner', -1), ('start_time', -1)])
        return _id

    def get_collection(self):
        return db['header']


class EventDescriptor(object):
    """
    :param header_id: foreign key pointing back to header
    :type header_id: integer
    :param event_type_id: event type integer descriptor generated by
    :type event_type_id: integer
    :param descriptor_name: event type string descriptor
    :type descriptor_name: string
    :param event_type_descriptor: dictionary that defines fields and field data types for a given event type
    :type event_type_descriptor: dictionary
    """
    def __init__(self, header_id, event_type_id, descriptor_name, tag=None, type_descriptor=dict()):
        """
        Constructor
        """
        self.header_id = header_id
        self.event_type_id = event_type_id
        self.tag = tag
        self.descriptor_name = validate_string(descriptor_name)
        self.type_descriptor = validate_dict(type_descriptor)

    def __compose_document(self):
        """
        Composes a python dictionary used in order to insert into 'header' collection
        """
        document_template = dict()
        document_template['header_id'] = self.header_id
        document_template['event_type_id'] = self.event_type_id
        document_template['descriptor_name'] = self.descriptor_name
        document_template['tag'] = self.tag
        document_template['type_descriptor'] = self.type_descriptor
        return document_template

    def save(self, **kwargs):
        composed_dict = self.__compose_document()
        _id = db['event_type_descriptor'].insert(composed_dict, **kwargs)
        db['event_type_descriptor'].ensure_index([('header_id', -1), ('descriptor_name', -1)])
        return _id


class Event(object):
    def __init__(self, header_id, event_descriptor_id, seq_no, owner=getpass.getuser(), description=None, data=dict()):
        """
        Constructor
        :param even_descriptor_id: foreign key pointing back to event_descriptor

        :type event_descriptor_id: integer

        :param description: User generated text field

        :type description: string

        :param seq_no: sequence number for the data collected

        :type seq_no: integer

        :param owner: data collection or system defined user info

        :type owner: string

        :param data: data point name-value pair container

        :type data: dictionary

        :returns: None
        """
        self.header_id = header_id
        self.event_descriptor_id = event_descriptor_id
        self.seq_no = validate_int(seq_no)
        self.owner = validate_string(owner)
        self.description = validate_string(description)
        self.data = validate_dict(data)

    def __compose_document(self):
        document_template = dict()
        document_template['header_id'] = self.header_id
        document_template['event_descriptor_id'] = self.event_descriptor_id
        document_template['seq_no'] = self.seq_no
        document_template['owner'] = self.owner
        document_template['description'] = self.description
        document_template['data'] = self.data
        return document_template

    def save(self, **kwargs):
        composed_dict = self.__compose_document()
        _id = db['event'].insert(composed_dict, **kwargs)
        db['event'].ensure_index([('event_descriptor_id', -1), ('header_id', 1), ('data', -1)])
        return _id


class BeamlineConfig(object):
    def __init__(self, header_id, config_params=dict()):
        """
        :param beamline_id: beamline descriptor
        :type beamline_id: string

        :param header_id: foreign key pointing back to header
        :type header_id: integer

        :param config_params: configuration parameter name-value container
        :type config_params: dictionary

        """
        self.header_id = header_id
        self.config_params = validate_dict(config_params)
    def __compose_document(self):
        document_template = dict()
        document_template['header_id'] = self.header_id
        document_template['config_params'] = self.config_params
        return document_template

    def save(self, **kwargs):
        composed_dict = self.__compose_document()
        _id = db['beamline_config'].insert(composed_dict, **kwargs)
        db['beamline_config'].ensure_index([('header_id', -1)])
        return _id
