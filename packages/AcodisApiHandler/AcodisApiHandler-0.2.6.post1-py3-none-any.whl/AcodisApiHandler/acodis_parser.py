from _acodis_logger import HandlerLog
from acodis_error import *
from acodis_handler import AcodisAPIHandler

log = HandlerLog().get_log(__name__)


def extract_tags(handler: AcodisAPIHandler, tags: list):
    """
    The extract_tags function takes a list of tags and returns a dictionary with the tag as key
    and the text associated with that tag as value. The function is used to extract data from an XML file.

    :param handler:AcodisAPIHandler: Access the xml object
    :param tags:list: Specify the tags that should be extracted from the xml file
    :return: A dictionary containing the tags passed as argument
    :doc-author: Ricardo Filipe dos Santos
    """
    dict_tags = {}
    for key in tags:
        try:
            dict_tags[key] = handler.xml.find('.//p/span[@class="{key}"]'.format(key=key)).text.strip()
        except KeyError:
            err = "Key {key} not found in dictionary".format(key=key)
            log.error(err)
            raise AcodisParsingError(err)
    return dict_tags
