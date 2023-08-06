"""Constants for PBN and LIN files conversions."""
import datetime

PBN_VULNERABILITY_CONVERSION = {'Z': 'None', 'N': 'NS', 'E': 'EW',
                                'B': 'Both', '?': '',
                                'None': 'Z', 'NS': 'N', 'EW': 'E',
                                'Both': 'B', '': '?'}

LIN_VULNERABILITY_CONVERSION = {'O': 'None', 'N': 'NS', 'E': 'EW',
                                'B': 'Both', '?': '',
                                'None': 'O', 'NS': 'N', 'EW': 'E',
                                'Both': 'B', '': '?'}

PBN_CALL_CONVERSION = {'P': 'Pass', 'D': 'X', 'R': 'XX', 'A': 'AP',
                       'Pass': 'P', 'X': 'D', 'XX': 'R', 'AP': 'A'}

PBN_VERSION_TEXT = '% PBN 2.1'
PBN_FORMAT_TEXT = '% EXPORT'
PBN_CONTENT_TEXT = '% Content-type: text/pbn; charset=ISO-8859-1'
PBN_CREATOR_TEXT = '% Creator: bridgeobjects'

RBN_VERSION_TEXT = '% RBN version 3.2'
RBN_CREATOR_TEXT = '% Created by bridgeobjects'

DEFAULT_EVENT_NAME = 'BfG default event name'
DEFAULT_EVENT_DATE = datetime.date(1980, 1, 1)