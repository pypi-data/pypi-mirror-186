""" Main interface to the ORBCOMM API V3

This modules provides the following classes:

    * Classes which represents configurable entities like area or list
    * Classes which defines vessel search criteria
    * Class which provides a functional interface to all the api end points
    * Class which contains the result of an api search
    * Class which represents exceptions which can be raised during an API call
    * Support classes. These classes should be used only for low level interfacing
"""

from email.errors import StartBoundaryNotFoundDefect
from http.client import TOO_MANY_REQUESTS, UNAUTHORIZED
from inspect import isclass
from itertools import starmap
import requests
from typing import List, Dict, Any, cast, Union, Tuple, IO, Optional,NamedTuple
from datetime import datetime, timedelta
import os.path
from pathlib import Path
from os import makedirs
import csv
import re
import enum
from collections import namedtuple
from .api_credentials import ApiCredentials
import time
import tempfile
from dataclasses import dataclass, field
import pdb


# Disable the warnings related to unsecure connection
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning) 


# Defines the parameters of an area
#AreaData = namedtuple('AreaData', ['mode', 'name', 'vertices'])
class AreaData(NamedTuple):
    """Definition of an area which can be used to retrieve vessels.

    After the object creation, the area can be entered in the system by calling :func:`AreaEndPoints.put_area` 
    
    Args:
        name: Name of the area. This is the name to use to retrieve vessels from the area
            Must be less than 40 characters
        vertices: List of vertices in (lat, lon) format in decimal degrees
            May have up to 25 vertices
        mode: Reserved - Do not use

    Attributes:
        name: Name of the area. This is the name to use to retrieve vessels from the area
            Must be less than 40 characters
        vertices: List of vertices in (lat, lon) format in decimal degrees
            May have up to 25 vertices
        mode: Do not use
    

    """
    #: Name of the area. Must be less than 40 characters
    name:str
    #: List of vertices
    vertices:List[Tuple[float,float]]
    # Mode in which the area is used must be "inclusive" or "exclusive"
    mode:str = "inclusive"

class VesselListData(NamedTuple):
    """Definition of a vessel list which can then be used to retrieve vessel information

    After object creation, the list can be entered in the remote host by calling :func:`ApiEndPoints.put_vessel_list`

    Args:
        name: Name of the vessel list. This is the name to use to retrieve information on the
            vessels of this list
        vessels: List of MMSI or IMO. Each IMO or MMSI must be a string
        type: Must be 'mmsi_list' or 'imo_list'
    
    """
    # name of the list of vessels
    name:str
    vessels:List[str]
    # Type of vessel list. Must be "mmsi_list" or "imo_list"
    type:str = "mmsi_list"

class SearchCriteria(NamedTuple):
    """ Define the criteria to be used for searches 

    The date range of the search can be specified either by a lookBack value
    or a startDate, endDate pair.

    **This class has an attribute for each of its parameters (with the same name as the parameter)**
    
    Args:
        startDate: Indicates the start date of the query
                    Can only be set if the value of lookBack is 0
        stopDate: Indicates the stop date of the query
                    Can only be set if the value of lookBack is 0
        format: Indicates the format of the results (tsv or json)
        latestPosition: if True, only the last position of each vessel is returned
        listName: Name of the IMO or MMSI list to search for
                    Cannot be combined with vesselType or vesselCategory
        areaName: Name of the area in which to search vessels
                    Can be combined with one of listName, vesselType, vesselCategory
        vesselType: Type of vessels to search for
                    Cannot be combined with listName or vesselCategory
        vesselCategory: Category of vessels to search for
                    Cannot be combined with listName or vesselType
        lookBack: Indicates how long to look back from the current time
                    Not compatible with startDate and stopDate
                    A value of 0 means that lookBack is not used
        lookBackUnit: Unit for the lookBack field (days,hours,minutes)
                    Default value is 'minutes'
        forcePending: if True the query is always returned as a pending query for which the 
                    result file must be downloaded
        label: Used for code documentation. Provides a short description of the search criteria

    """
    startDate:Optional[datetime] = None
    stopDate:Optional[datetime] = None
    format:str = "json" 
    latestPosition:bool = True
    listName:str = ""
    areaName:str = ""
    vesselType:str = ""
    vesselCategory:str = ""
    lookBack:int = 0
    lookBackUnit:str = 'minutes'
    forcePending:bool = False
    label:str='' #Only for documentation

    def __str__(self):
        """ Returns a human readables string of the content of the object
        
        Return (str): Object description
        
        """
        pretty_string = ""
        if self.label:
            pretty_string += f"Query: {self.label}\n"
        if self.startDate and self.stopDate:
            if pretty_string: pretty_string += "\n"
            pretty_string += f"Query from {self.startDate} to {self.stopDate}"
        if self.lookBack:
            if pretty_string: pretty_string += "\n"
            pretty_string += f"Query for the last {self.lookBack} {self.lookBackUnit}"
        if self.latestPosition:
            if pretty_string: pretty_string += "\n"
            pretty_string += f"Only latest positions"
        if self.listName:
            if pretty_string: pretty_string += "\n"
            pretty_string += f"Searching for vessels in list {self.listName}"
        if self.areaName:
            if pretty_string: pretty_string += "\n"
            pretty_string += f"Searching for vessels in area {self.areaName}"
        if self.vesselType:
            if pretty_string: pretty_string += "\n"
            pretty_string += f"Searching for vessel of type {self.vesselType}"
        if self.vesselCategory:
            if pretty_string: pretty_string += "\n"
            pretty_string += f"Searching for vessel of category {self.vesselCategory}"
        if self.forcePending:
            if pretty_string: pretty_string += "\n"
            pretty_string += f"Pending search was forced"
        if self.format:
            if pretty_string: pretty_string += "\n"
            pretty_string += f"Output format is {self.format}"
        return pretty_string


class QueryStatus(enum.Enum):
    """ Possible values of the ``queryStatus`` field of a :class:`PendingQueryInfo` 
    instance

    Args:
        value: One of the enumeration value
    """
    #: The query is still being processed
    in_process = 'in process'
    #: The query has been aborted by the user
    aborted_by_user = 'aborted by user'
    #: The query has completed and is ready for download
    ready = 'ready for download'
    aborted_by_error = 'aborted due to error'


@enum.unique
class ErrorCategory(enum.IntFlag):
    """ List of identifiers which characterizes an API Access Error"""
    #: No error
    NO_ERROR = 0
    #: The connection could not be made (DNS issues, refused connection...)
    CONNECTION_ERROR = 1
    #: HTTP protocol error
    HTTP_ERROR = 2
    #: The establishment of the TCP connection with the server
    #: has timed out
    CONNECT_TIMEOUT = 4
    #: The wait for the first byte of the response from the server
    #: has timed out
    READ_TIMEOUT = 8
    #: The body of the responsed was expected to be valid json
    #: but it is not
    NO_JSON_BODY = 16
    #: Unknown error occurred
    UNKNOWN_ERROR = 32
    #: The server did not recognize the api_key provided or the
    #: key has expired
    UNAUTHORIZED = 64
    #: The body of the request could not be identified as valid
    #: by the server
    BODY_VALIDATION_ERROR = 128
    #: A json body was in the response, but it was unexpected
    #: Or the JSON response does not follow the API specification
    UNKNOWN_JSON_RESPONSE = 256
    #: An areaname or list name or any other criteria parameter was not found
    NOT_FOUND = 512
    #: A server error occurred. 
    SERVER_ERROR = 1024
    #: The server could not accomplish the request because of account limits
    #: reached
    FORBIDDEN = 2048
    #: Error mostly caused by erroneous file operation
    OS_ERROR = 4096
    #: Error caused by a bad request, list too long, exceeds limit
    BAD_REQUEST = 8192
    #: Content type is not as expected
    UNEXPECTED_CONTENT_TYPE = 8192 * 2
    #: Too many requeests (pending queries or calls)
    TOO_MANY_REQUESTS = 8192 * 4

class PendingQueryInfo(NamedTuple):
    """Return value of a :func:`ApiEndPoints.query_status` call

    Instances of this type are created automatically by the methods of :class:`ApiEndPoints`
    """
    #:Time at which the server generated this answer
    serverTime:datetime
    #:Token of the query associated with the answer
    queryToken:str
    #:Minimum time to respect between :func:`ApiEndPoints.query_status` calls
    statusQueryInterval:int
    #:Query Status reported by the server 
    queryStatus: str
    #:Elapsed time from the initial request until completion of the query
    elapsedTime: int
    #:Error message. Empty if no error occurred
    errorMsg:str =  ''

class SearchResult(NamedTuple):
    """Contains the result of a low level :func:`ApiEndPoints.vessel_search` call
    
    Depending upon the mode of the query (immediate or pending) and the desired output format, 
    it contains one of:

        * a valid PendingQueryInfo if the query was executed as 'pending'
        * a list of vessels information where each vessel information is a dictionary 
          if the format is json and the query was immediately executed
        * a tsv string if the format is 'tsv' and the query was immediately executed

    """
    #: Vessels information represented as a list of dictionaries. Each dictionary is the python representation
    #: of the content of the json string returned by the server
    vesselData:List[Any] = []
    #: Results when a pending query is executed
    pendingQueryInfo:Optional[PendingQueryInfo] = None
    #: TSV (tab separated) data returned by the server.
    #: Each vessel is on a separate line and fields are separated by tab characters
    vesselTsvData:str = ""

@dataclass
class ExecuteQueryResult:
    """ Output of the high-level method :func:`ApiEndPoints.execute_query`

    """ 
    #: Indicates if query was executed without the occurent of a timeout. This is mainly used to detect
    #: timeout when the library is used in an async protocol by higher layer code
    runToCompletion:bool = False
    #: Start of execution of the query 
    executionStart:datetime = field(default_factory=datetime.utcnow)
    #: Total Execution duration of the query (query processing + download)
    executionDuration:timedelta = timedelta(0)
    #: Error message if the query failed
    errorMsg:str = '' 
    #: Indicates the execution mode of the query
    executedAsPending:bool = False

    # --- Non Pending queries only

    #: If the query was not pending, a list of dictionary if 'json' output format was requested
    vesselData:List[Dict[str,Any]] = field(default_factory=list) 
    #: If the query was not pending, a string containing tsv data if 'tsv' output format was requested
    vesselTsvData:str = ''
    #: Nbr of messages retrieved. (Number of elements for a json array, number of lines for a tsv string)
    nbrMsgs:Optional[int] = None 

    # --- Pending queries only

    #: Duration of the processing of the query by the server. Only available for pending queries
    serverProcessingDuration:Optional[timedelta] = None
    #: Duration of the download. Only available for pending queries
    downloadDuration: Optional[timedelta] = None
    #: Interval used to inquire about the status of the query in minutes
    queryStatusInterval: Optional[int] = None 
    #: Name of the file if the query was pending and returned a file
    filepath:Optional[Path] = None
    #: Token which was associated with the query
    token:Optional[str] = None

    def __str__(self): 
        """ Create a pretty string from the content of the object """
        pretty_string = ( 
            f"Query Stats -->:\n"
            f"\tExecution Start: {self.executionStart}\n"
            f"\tServer Processing Duration: {self.serverProcessingDuration if self.serverProcessingDuration is not None else 'na'}\n"
            f"\tDownload Duration: :{self.downloadDuration if self.downloadDuration is not None else 'na'}\n"
            f"\tTotal Execution Duration: {self.executionDuration}\n"
            f"\tExecuted as Pending: {self.executedAsPending}\n"
            f"\tQuery Status Interval: {self.queryStatusInterval if self.queryStatusInterval is not None else 'na'}\n"
            f"\tNumber of Messages: {self.nbrMsgs if self.nbrMsgs is not None else 'na'}\n"
            f"\tError Msg: {self.errorMsg}\n"
            f"\tFilepath: {self.filepath if self.filepath is not None else 'na'}\n"
            f"\tToken: {self.token if self.token is not None else 'na'}\n"
            )
        return pretty_string

class ApiAccessError(Exception):
    """ Exception raised by any error occurring in the API

    Args:
        error_text: Human readable string describing the exception. The text provided must
            be an interesting text for the user. He must not be bored when he reads it. It is not simple 
            to do well.
        error_category: Indicates the category of error (for example SERVER_ERROR)

    """
    def __init__(self, error_text:str, error_category:ErrorCategory):
        self.error_text = error_text #: str: Copy of the input argument `error_text`
        #: str: Copy of the input argument `error_category``
        self.error_category = error_category


class ApiEndPoints:
    """ This class contains methods to access all the different api end points 

    It creates its own log file which records all transactions.
    The name of the log file is api_end_points_YYYYMMDD_HHMM_XXXX.log where:
    
        . YYYYMMDD_HHMM is the date of creation of the file
        . XXXX is the ID of the class instance which created the file
    
    Usage:
        1- Create an instance
            obj = ApiEndPoints(credentials, log_file_directory, verify_certificate = True)
        2- Call the methods to perform api calls
            An ApiAccessError is raised if an error occurs 

    Args:
        credentials: Provides host name, username and password to access the server
        logDirectory: Directory where the log file will be located. The directory is created if it
            does not exist 
        verify_certificate: If True, the server certificates is verified for authenticity

    """
    # Creates a separate Id for each instance created. The id is used to create
    # the log file
    nextInstanceId = 1

    def __init__(self, credentials:ApiCredentials, logDirectory:Path , verify_certificate:bool=True):
        """ Initialize the class with the api parameters common to all endpoint
        calls 
        
        --- Parameters ---
           credentials: object which contains host, url path, username, password...
           logDirectory: Directory where the log files should be created. One log file is created for each instance of
                        the class. The directory is created if it does not exist
            verify_certificate: If false server certificate are not verified
        """

        #--- Pre-conditions
        assert isinstance(logDirectory,Path), "logDirectory must be a Path object"
        assert isinstance(credentials, ApiCredentials), "credentials should be an ApiCredentials object"
        assert credentials.is_valid(), "Credential set is not valid"

        self.instanceId = ApiEndPoints.nextInstanceId
        ApiEndPoints.nextInstanceId += 1

        self.credentials = credentials
        self.base_url = credentials.get_full_url()
        self.verify_certificate = verify_certificate
        # Used to dynamically change the password for testing purposes
        self.active_password = credentials.password
        # body to be transferred at each request
        self.dict: Dict[str,Any] = {}
        # Access token to be user for each transfer after authentication 
        self.api_key = ""
        log_file_name = f'api_end_points_{datetime.utcnow().strftime("%Y%m%d_%H%M")}_{self.instanceId:04d}.log' 
        logDirectory.mkdir(parents=True, exist_ok=True)
        log_path = logDirectory / log_file_name
        self.log = open(log_path, 'wb')


    # The password property is used to be able to change the password for testing purposes 
    # and modify the dict property when the password is modified.           
    @property
    def password(self):
        # Get the active password
        return self.active_password

    @password.setter
    def password(self, _password):
        # Dynamically change the password
        self.active_password = _password            

    @password.deleter
    def password(self):
        # Restore the password to its intended value
        self.active_password = self.credentials.password

    def __del__(self):
        # Called when the object is deleted
        self.log.close()

    def __basic_query(self, url, dict, verb='POST', stream=False, 
                        filepath:Optional[Path]= None)->Any:
        """ Basic handling of a request. It handles all internal exceptions and can 
        only raise ApiAccessError

        Parameters:
            url: full url to reach
            dict: json body as a dictionary
            verb: One of the valid http verbs
            stream: True when downloading a file, so that the file is read by chunks
            filepath: Destination of the downloaded file. Only required if a file download
                is performed. The parent directory of the file must exist 
        Returns: 
            dictionary representing the Json body of the response (application/json)
            string if  the response is TSV data (text/plain)
        Raises: ApiAccessError if any error occurs. This contains a description of the error
            as well as a tag identifying the category of the error
        """
        CONNECT_TIMEOUT = 20
        READ_TIMEOUT = 120

        assert(verb in ['PUT','POST','GET','DELETE'])
        try:
            headers:Dict[str,Any] = {}
            if self.api_key:
                headers = {"authentication": self.api_key}
            with requests.request(verb, url, verify=self.verify_certificate, json = dict, headers=headers,stream=stream ) as r:
                # Process the different answers
                if r.status_code == requests.codes['ok'] \
                        and (r.headers['Content-Type']== 'application/gzip'  \
                        or r.headers['Content-Type'] == 'application/force-download'):
                    # This is a file to download
                    self.write_url_and_headers_to_log(r)
                    disposition = r.headers["Content-Disposition"]
                    # We download and save the file block by block
                    assert filepath is not None, "No filepath was provided for file download"
                    #filepath.parent.mkdir(parents=True,exist_ok=True)  #Creates the directory
                    with open(filepath, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=10000):
                            if chunk:
                                f.write(chunk)
                else:
                    self.write_response_to_log(r)
                    if r.status_code == requests.codes["ok"] or r.status_code == requests.codes["created"] :
                        # We can either have a text/plain or application/json content type
                        if 'text/csv' in r.headers['Content-Type']:
                            # This is tsv data. A string is returned
                            tmp = r.text
                            return tmp
                        elif r.headers['Content-Type'] == 'application/json':
                            # This is json data . A dictionary is returned 
                            tmp = r.json()
                            return tmp
                        else:
                            # Unexpected content type
                            raise ApiAccessError("Unexpected content type", ErrorCategory.UNEXPECTED_CONTENT_TYPE)
                            pass
                    elif r.status_code == requests.codes["bad_gateway"]:
                        raise ApiAccessError("Bad Gateway", ErrorCategory.SERVER_ERROR)
                    elif r.status_code == requests.codes["bad_request"]:
                        raise ApiAccessError("Bad Request", ErrorCategory.BAD_REQUEST)
                    elif r.status_code == requests.codes["forbidden"]:
                        # Status code of 503
                        tmp = r.json()
                        raise ApiAccessError("Forbidden: " + str(tmp), ErrorCategory.FORBIDDEN)
                    elif r.status_code == requests.codes["gateway_timeout"]:
                        # Status code of 504
                        raise ApiAccessError("Server timed out", ErrorCategory.SERVER_ERROR)
                    elif r.status_code == requests.codes["too_many_requests"]:
                        # Status code of 429
                        tmp = r.json()
                        raise ApiAccessError("Too many requests" + str(tmp), ErrorCategory.TOO_MANY_REQUESTS)
                    elif r.status_code == requests.codes["unprocessable"]:
                        # Status code of 422
                        tmp = r.json()
                        raise ApiAccessError("Body Validation error" + str(tmp),ErrorCategory.BODY_VALIDATION_ERROR)
                    elif r.status_code == requests.codes["unauthorized"]:
                        raise ApiAccessError("Unauthorized Access", ErrorCategory.UNAUTHORIZED)
                    elif r.status_code == requests.codes["not_found"]:
                        tmp = r.json()
                        raise ApiAccessError("not found " + str(tmp), ErrorCategory.NOT_FOUND)
                    elif r.status_code == requests.codes["internal_server_error"]:
                        raise ApiAccessError("Internal Server Error", ErrorCategory.SERVER_ERROR)
                    else:
                        tmp = r.json()
                        raise ApiAccessError("Unknown json text " + str(tmp), ErrorCategory.UNKNOWN_JSON_RESPONSE)
        except ApiAccessError :
            raise 
        except requests.exceptions.ConnectTimeout as ex:
            raise ApiAccessError("Connnection Timeout" + str(ex),ErrorCategory.CONNECT_TIMEOUT)
        except requests.exceptions.ConnectionError as ex:
            raise ApiAccessError("Connection Error" + str(ex),ErrorCategory.CONNECTION_ERROR)
        except requests.exceptions.ReadTimeout as ex:
            raise ApiAccessError("Read Timeout" + str(ex),ErrorCategory.READ_TIMEOUT)
        except requests.exceptions.RequestException as ex:
            raise ApiAccessError("Request Module Error: " + str(ex),ErrorCategory.UNKNOWN_ERROR)
        except ValueError:
            raise ApiAccessError("Response body is not JSON", ErrorCategory.NO_JSON_BODY)
        except OSError as ex:
            raise ApiAccessError("OsError" + ex.strerror, ErrorCategory.OS_ERROR)
        except Exception as ex:
            raise ApiAccessError("Unknown Error: " + str(ex),ErrorCategory.UNKNOWN_ERROR)
        except :
            raise ApiAccessError("Unknown Error: " , ErrorCategory.UNKNOWN_ERROR)
    

    def login(self) -> None:
        """ Get an API key from the system by providing a username and password

        The key will be stored inside the instance until a call to :func:`ApiEndPoints.logout` is made or
        an 'Unauthorized' error code is reported by the server

        Raises: :class:`ApiAccessError` is raised if any error occurs
        """
        tmp_url = self.base_url + "login"
        # Reset the dictionary instance
        tmp_dict = self.dict.copy()
        tmp_dict.update({"username": self.credentials.username})
        tmp_dict.update({"password": self.active_password})
        json_data = self.__basic_query(tmp_url,tmp_dict,"POST")
        # Store the key locally in the system
        if json_data:
            self.api_key = json_data["apiKey"]
        
    def logout(self,ignore_unauthorized:bool=True) -> None:
        """ Releases the API key if it exists 
        
        If an 'Unauthorized' error occurs, this means that the key has already expired;
        it is then erased from the instance

        Raises: :class:`ApiAccessError` is raised if any error except 'Unauthorized' occurs
        
        Note: The api_key is not erased from the instance if any other error but 'Unauthorized' occurs
        """ 
        if not self.api_key:
            # No exist. No point to logout
            return
        tmp_url = self.base_url + "logout"
        tmp_dict = self.dict.copy()  # Already contains username and password
        try:
            self.__basic_query(tmp_url,tmp_dict, "POST")
        except ApiAccessError as ex:
            if ignore_unauthorized and ex.error_category == ErrorCategory.UNAUTHORIZED:
                self.api_key = ""
                pass
            else:
                raise ex
        else:
            self.api_key = ""

    #-------------------------------------------------------------
    #   Vessel List API
    #-------------------------------------------------------------

    def vessel_lists(self)->List[str]:
        """Inquire the server for all the names of the different vessel list which are
        currently stored

        Returns: List of the names of all vessel lists currently stored in the server

        Raises: ApiAccessError if an erro occurs
        """
        tmp_url = self.base_url + "vesselList"
        tmp_dict = self.dict.copy() # Not used for a get
        json_data = self.__basic_query(tmp_url,None,"GET")
        # validates the json response
        if not isinstance(json_data,List) or any([not isinstance(x,str) for x in json_data]):
            raise ApiAccessError("Invalid response to 'vessel_lists' request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        return json_data

    def get_vessel_list(self, list_name:str)->VesselListData: 
        """ Returns the content of a vessel list "list_name" 
        
        Args:
            list_name: name of the list to be retrieved
        Returns:
            :class:`VesselListData` instance

        Raises: ApiAccessError if any error occurs
        """
        tmp_url = self.base_url + "vesselList/" + list_name
        tmp_dict = self.dict.copy() # Not used for a get
        json_data = self.__basic_query(tmp_url,None,"GET")
        # Validate json
        if any([key not in ["mmsiList","imoList"] for key in json_data.keys()]):
            raise ApiAccessError("Invalid response to 'get_vessel_list' request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        # TODO: validate that the lists contains string of numbers
        # Return the response
        # Hack due to server changes
        resp_type = "mmsiList" if "mmsiList" in json_data else "imoList"
        type = "mmsi_list" if "mmsiList" in json_data else "imo_list"
        return VesselListData(name=list_name,type=type,vessels=json_data[resp_type])
        
    def put_vessel_list(self, vesselListData: VesselListData)->List[str]:
        """ Add a new vessel list in the system or fully update an existing
        vessel list.

        Args:
            vesselListData: parameters of the vessel List 

        Returns:
            List of all vessel lists in the system
        
        Raises: ApiAccessError if any error occurs
        """
        assert vesselListData.type in ["imo_list", "mmsi_list"]
        tmp_url = self.base_url + "vesselList/" + vesselListData.name
        tmp_dict = self.dict.copy()
        listType="mmsiList" if vesselListData.type == "mmsi_list" else "imoList"
        tmp_dict.update({listType:vesselListData.vessels})
        json_data = self.__basic_query(tmp_url,tmp_dict,"PUT")
        # validates the json response
        if not isinstance(json_data,List) or any([not isinstance(x,str) for x in json_data]):
            raise ApiAccessError("Invalid response to 'vessel_lists' request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        # return the result
        return json_data

    def del_vessel_list(self, list_name:str)->List[str]:
        """ Delete a vessel list

        Args:
            list_name: name of the list

        Returns:
            List of all the vessel lists existing in the system 

        Raises: ApiAccessError if any error occurs
        """
        tmp_url = self.base_url + "vesselList/" + list_name
        tmp_dict = self.dict.copy()
        json_data = self.__basic_query(tmp_url,tmp_dict,"DELETE")
        # validates the json response
        if not isinstance(json_data,List) or any([not isinstance(x,str) for x in json_data]):
            raise ApiAccessError("Invalid response to 'vessel_lists' request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        # return the result
        return json_data

    #-------------------------------------------------------------
    #   Areas  API
    #-------------------------------------------------------------

    def area_list(self)-> List[str]:
        """Inquire the server about the names of all the areas stored in the server
        
        Returns: list which includes the names of all the areas currently stored in the server

        Raises: ApiAccessError if any error occurs

        """
        tmp_url = self.base_url + "area"
        tmp_dict = self.dict.copy() # Not used for a get
        json_data = self.__basic_query(tmp_url,None,"GET")
        # validates the json response
        if not isinstance(json_data,List):
            raise ApiAccessError("Invalid response from DEL area request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        # return the list of area names
        return json_data

    def get_area(self, area_name:str)->AreaData:
        """ Inquire the server for the information about a specific area

        Args:
            area_name: Name of the area 
        
        Returns: :class:`AreaData` instance  

        Raises: ApiAccessError if any error occurs
        """
        tmp_url = self.base_url + "area/" + area_name
        tmp_dict = self.dict.copy() #  Not  used for a get
        json_data = self.__basic_query(tmp_url,None,"GET")
        # Validate the response
        #if "inclusive" not in json_data or "vertices" not in json_data:
        if "vertices" not in json_data:
            raise ApiAccessError("Invalid response to 'GET area' request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        #if not json_data["inclusive"] in [True,False]:
        #    raise ApiAccessError("Invalid response to 'GET area' request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        if not isinstance(json_data["vertices"],List):
            raise ApiAccessError("Invalid response to 'GET area' request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        # Return the result
        mode = "inclusive"
        #mode = "inclusive" if json_data["inclusive"] == True else "exclusive"
        # Transform the list of dictionary into a list of (lat,lon) tuples
        vertices = [(x["lat"],x["lon"]) for x in json_data["vertices"]]
        return AreaData(name=area_name, mode=mode, vertices=vertices) 
        
    def put_area(self, areaData:AreaData)->List[str]:
        """ Add a new area in the server or fully update an existing
        area.

        Args:
            areaData: Description of the area to add / update

        Returns: List of all the names of the areas currently stored in the server

        Raises: ApiAccessError if any error occurs
        """
        assert(areaData.mode in ["inclusive", "exclusive"])
        tmp_url = self.base_url + "area/" + areaData.name
        # convert the (lat,lon) tuples into a list of dictionary
        keys = ("lat", "lon")
        vertices = [dict(zip(keys,values)) for values in areaData.vertices]
        # Create the json body
        tmp_dict = self.dict.copy()
        tmp_dict.update(inclusive = True if areaData.mode == "inclusive" else False)
        tmp_dict.update(vertices = vertices)
        json_data = self.__basic_query(tmp_url,tmp_dict,"PUT")
        # validates the json response
        if not isinstance(json_data,List):
            raise ApiAccessError("Invalid response from put_area request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        # return the list of area names
        return json_data

    def del_area(self, area_name:str)-> List[str]:
        """ Delete an area from the server
        
        Args:
            area_name: name of the area to delete
        
        Returns: List of all the names of the areas currently stored in the server

        Raises: ApiAccessError if any error occurs

        """
        tmp_url = self.base_url + "area/" + area_name
        tmp_dict = self.dict.copy()
        json_data = self.__basic_query(tmp_url,tmp_dict,"DELETE")
        # validates the json response
        if not isinstance(json_data,List):
            raise ApiAccessError("Invalid response from del_area request", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        # return the list of area names
        return json_data

    #-------------------------------------------------------------
    #  Vessel Search
    #-------------------------------------------------------------

    def vessel_search(self,criteria:SearchCriteria)->SearchResult:
        """ Searches for vessel with a specific criteria

        Args:
            criteria: :class:`SearchCriteria` instance which defines the criteria of the search

        Returns:
            :class:`SearchResult` instance which contains either a QueryStatus instance or the final
            result of a search

        Raises: ApiAccessError if any error occurs
        """ 
        errors = self.validate_search_criteria(criteria)
        if errors:
            # The search criteria is invalid. Description of errors
            # is provided to user
            raise ApiAccessError("\n".join(errors),ErrorCategory.BODY_VALIDATION_ERROR)
        else:
            # Perform the search
            tmp_url = self.base_url + "vessels/search"
            tmp_dict = self.dict.copy()
            tmp_dict.update(self.__search_criteria_to_dictionary(criteria))
            result = self.__basic_query(tmp_url,tmp_dict,"POST")
            if isinstance(result,dict):
                # The query returned json data
                json_data = result
                # Validate the json response
                if "resultType" not in json_data.keys() or "result" not in json_data.keys():
                    raise ApiAccessError("Invalid JSON from a vessel_search query", ErrorCategory.UNKNOWN_JSON_RESPONSE)
                if json_data["resultType"] == "completed":
                    return SearchResult(vesselData=json_data["result"])
                elif json_data["resultType"] == "pending":
                    if self.__validate_pending_query_info(json_data["result"]):
                        return SearchResult(pendingQueryInfo=self.__convert_dict_to_pending_query_tuple(json_data["result"]))
                    else:
                        raise ApiAccessError("Invalid PendingQueryInfo from a vessel_search query", ErrorCategory.UNKNOWN_JSON_RESPONSE)
                else:
                    raise ApiAccessError("Invalid JSON from a vessel_search query", ErrorCategory.UNKNOWN_JSON_RESPONSE)
            elif isinstance(result, str):
                # The query returned plain text
                tsv_data = result
                return SearchResult(vesselTsvData=tsv_data)
            else:
                # Unexpected result from the query
                raise ApiAccessError("Unexpected result from query", ErrorCategory.UNKNOWN_ERROR)
    #-------------------------------------------------------------
    #  Pending Queries
    #-------------------------------------------------------------

    def query_status(self, token:str)->PendingQueryInfo:
        """ Return the status of the query specified as a parameter
        
        Args:
            token: Token identifying the query for which the status is required
            
        Returns:
            :class:`PendingQueryInfo` instance

        Raises: :class:`ApiAccessError` instance if any error occurs
            
        """
        tmp_url = self.base_url + "vessels/queryStatus/" + token
        tmp_dict = self.dict.copy() # Not used for a get
        json_data = self.__basic_query(tmp_url,None,"GET")
        # validates the json response
        if not self.__validate_pending_query_info(json_data):
            raise ApiAccessError("Expected a pending query response", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        else:
            return self.__convert_dict_to_pending_query_tuple(json_data)

    def delete_query(self, token:str)->PendingQueryInfo:
        """ Return the status of the query specified as a parameter

        Args:
            token: token of the query that we want to delete
        
        Returns:
            :class:`PendingQuery` object

        Raises: :class:`ApiAccessError` instance if any error occurs
        """
        tmp_url = self.base_url + "vessels/queryDelete/" + token
        tmp_dict = self.dict.copy() # Not used for a get
        json_data = self.__basic_query(tmp_url,None,"GET")
        # validates the json response
        if not self.__validate_pending_query_info(json_data):
            raise ApiAccessError("Expected a pending query response", ErrorCategory.UNKNOWN_JSON_RESPONSE)
        else:
            return self.__convert_dict_to_pending_query_tuple(json_data)

    def chunked_test(self):
        """ Test routine to perform chunked downloads 

        :meta private:
        """
        tmp_url = self.base_url + "stream" 
        tmp_dict:Dict[str,Any] = self.dict.copy()
        headers:Dict[str,Any] = {}
        if self.api_key:
            headers = {"authentication": self.api_key}

        try:
            with requests.request('POST', tmp_url, verify=self.verify_certificate, json = tmp_dict, headers=headers, stream=True) as r:
                #print(r.headers)
                # The headers are expected when a file is effectively downloaded
                # {'Server': 'nginx/1.12.1', 'Date': 'Wed, 08 Apr 2020 22:15:19 GMT',
                #  'Content-Type': 'application/x-gzip', 'Content-Length': '19656',
                #  'Connection': 'keep-alive', 'Last-Modified': 'Wed, 08 Apr 2020 22:15:11 GMT',
                #  'Set-Cookie': 'mw_lang=EN; path=/; httponly', 'Expires': 'Mon, 26 Jul 1997 05:00:00 GMT',
                #  'Cache-Control': 'private',
                #  'Content-Disposition': 'attachment; filename=query_20200408_221456_15863840960924_PDF.tar.gz',
                #  'ETag': '"5e8e4cef-4cc8"',
                #  'Accept-Ranges': 'bytes',
                #  'Strict-Transport-Security': 'max-age=63072000; includeSubdomains; preload'}
                print(f"request headers: {r.request.headers}")
                print(f"response headers: {r.headers}")
                for chunk in r.iter_content(chunk_size=None):
                    if chunk:
                        print(chunk)

        except ValueError as ex:
            print(ex)

    def download_file(self, token:str, filepath:Path)->None:
        """ Download a file created on the system 

        The file is identify by the token of the query which created it

        Args:
            token: token of the query result to be downloaded
            filepath: full path of the file where the results will be written
                        The directory to contain the file should exist

        Returns:
            None

        Raises: :class:`ApiAccessError` instance if any error occurs
        """
        tmp_url = self.base_url + "vessels/download/" + token
        tmp_dict:Dict[str,Any] = self.dict.copy() # Not used for a GET
        self.__basic_query(tmp_url,None,'GET',True,filepath)


    def _extract_filename(self, text):
        """ Extract and return the value of the filename is a string of the type
        'attachment; filename=query_20200401_204506_15857739062551_CSV.tar.gz'

        :meta private:
        """
        pattern = r'.*filename=([^\s;]*).*'
        compiled_regex = re.compile(pattern)
        match = compiled_regex.search(text)
        if match:
            #print(match.group(1))
            return match.group(1)
        else:
            return None

    #-------------------------------------------------------------
    #  Top Level Functions
    #-------------------------------------------------------------

    def execute_query(self, 
                        criteria:SearchCriteria,
                        resultDirectory:Path,
                        _queryResult:Optional[ExecuteQueryResult] = None
                        )->ExecuteQueryResult:
        """ Executes a query to completion. 

        This is a high level function which handles immediate and pending queries automatically.
        
        If the result is a pending query, the results are written in a file with a random name 
        to the specified directory 

        Args:
            criteria: List of criteria for the search
            resultDirectory: Directory where files will be located in the case of pending queries
                        Directory will be created if it does not exist
            queryResult: An optional object in which the results are returned. If none a new object
                        is created and returned. This is done to allow to pass a derived class of ExecuteQueryResult for 
                        the function to fill

        Returns:
            :class:`ApiEndPoints.ExecuteQueryResult` instance. Some fields may be set to None when not applicable.

            If an error occurred during execution, the attribute :code:`ExecuteQueryResult.errorMsg` will contain a description of
            the error. If there are no error it is ""
        """
        # Convert the input parameters into a SearchCriteria and verify
        # that it is valid
        if _queryResult is None:
            queryResult:ExecuteQueryResult = ExecuteQueryResult()
        else:
            queryResult = _queryResult

        errors = self.validate_search_criteria(criteria)
        if errors:
            queryResult.errorMsg = "Criteria not valid: " + "\n".join(errors)
            queryResult.runToCompletion = True
            return queryResult
        
        # The criteria is valid
        if not self.api_key:
            try:
                self.login()
            except Exception as ex:
                queryResult.errorMsg = f"Login failed {ex}"
                queryResult.runToCompletion = True
                return queryResult

        # The criteria is valid and we were able to login                
        try:
            sr = self.vessel_search(criteria)
            if sr.pendingQueryInfo:
                # The query is pending
                queryResult.executedAsPending = True
                queryResult.queryStatusInterval = sr.pendingQueryInfo.statusQueryInterval
                queryResult.token = sr.pendingQueryInfo.queryToken
                pqi = self.__wait_pending_query_completion(sr.pendingQueryInfo)
                if pqi.queryStatus != QueryStatus.ready.value:
                    # The query aborted
                    queryResult.errorMsg = "Query was aborted" + pqi.errorMsg
                else:
                    # The query has completed, we extract the file
                    queryResult.serverProcessingDuration = datetime.utcnow() - queryResult.executionStart
                    resultDirectory.mkdir(parents=True,exist_ok=True)  #Creates the directory - ok if exists
                    beforeDownloadTime = time.monotonic() 
                    fd, filepath = tempfile.mkstemp(prefix='query_', suffix='.gz', dir=resultDirectory)
                    os.close(fd)
                    self.download_file(sr.pendingQueryInfo.queryToken,Path(filepath))
                    afterDownloadTime = time.monotonic() 
                    queryResult.downloadDuration = timedelta(seconds = afterDownloadTime - beforeDownloadTime) 
                    queryResult.filepath = Path(filepath)
            else:
                # The query results are immediately available
                queryResult.executedAsPending = False
                if criteria.format == 'json':
                    queryResult.vesselData = sr.vesselData
                    queryResult.nbrMsgs = len(queryResult.vesselData)
                else:
                    queryResult.vesselTsvData = sr.vesselTsvData
                    queryResult.nbrMsgs = len(queryResult.vesselTsvData.split("\n"))
        except ApiAccessError as ex:
            queryResult.errorMsg = ex.error_text 
        except OSError as ex:
            queryResult.errorMsg = ex.strerror

        queryResult.executionDuration = datetime.utcnow() - queryResult.executionStart
        queryResult.runToCompletion = True
        return queryResult

    def __wait_pending_query_completion(self, pq:PendingQueryInfo)->PendingQueryInfo:
        """ Continually queries the server for the status of a query until the query status is different from 'in process' 

        Args:
            pq: PendingQueryInfo instance returned by the original call to :fun:`vessel_search`

        Returns: New PendingQueryInfo instance. The queryStatus member will be different than 'in process'
            and may indicate that the query is completed or aborted

        """
        tmp_pq = pq
        while tmp_pq.queryStatus == QueryStatus.in_process.value:
            #DEBUG
            time.sleep(tmp_pq.statusQueryInterval) # statusQueryInterval is in seconds
            #time.sleep(15)
            tmp_pq = self.query_status(tmp_pq.queryToken)
        return tmp_pq 


    #-------------------------------------------------------------
    #  Utilities 
    #-------------------------------------------------------------

    @staticmethod
    def valid_vessel_types()->List[str]:
        """ Return a list of the valid vessel types. Only these types
        can be inserted as a search criteria"""
        vesselTypes = ['wig', 'fishing','towing','dredging','diving','military','sailing','pleasure','high speed',
                        'pilot', 'sar', 'tug', 'port tender', 'anti pollution', 'law enforcement', 'medical',
                        'non combattant', 'passenger', 'cargo', 'tanker', 'other']
        return vesselTypes

    @staticmethod
    def valid_vessel_categories()->List[str]:
        """ Return a list of the valid vessel categories
        Only these categories can be inserted in a search criteria
        """
        vesselCategories = ['class A', 'class B', 'sar', 'aton', 'base station', 'lr ais']
        return vesselCategories

    @staticmethod
    def validate_search_criteria(criteria:SearchCriteria)->List[str]:
        """ Validates if the search criteria complies with the API
        restrictions. It returns an array of strings which is empty if there
        are no error or which contains a string for each detected error.

        :note: The API end points restriction implemented by the server may be
             more constraining than the checks done in this routine

        """
        errors:List[str] = []
        # StartDate and StopDate or lookBack must be specified
        if not criteria.startDate and not criteria.stopDate and not criteria.lookBack:
            errors.append("startDate and stopDate or lookBack must be specified")
        elif (criteria.startDate or criteria.stopDate) and criteria.lookBack:
            errors.append("startDate,stopDate cannot be specified together with lookBack")
        elif criteria.startDate and not criteria.stopDate:
            errors.append("both startDate and stopDate must be specified")
        elif criteria.stopDate and not criteria.startDate:
            errors.append("both startDate and stopDate must be specified")
        elif (criteria.startDate is not None and not isinstance(criteria.startDate,datetime)) or  \
                (criteria.stopDate is not None and not isinstance(criteria.stopDate,datetime)):
            errors.append("startDate and stopDate must be datetime object")
        elif criteria.startDate is not None and criteria.stopDate is not None and criteria.startDate >= criteria.stopDate:
            errors.append("startDate must be earlier than stopDate")

        if criteria.format != "json" and criteria.format != "tsv":
            errors.append("format must be json or tsv")

        if not isinstance(criteria.latestPosition,bool):
            errors.append("latestPosition must be True or False")

        if not isinstance(criteria.lookBackUnit,str):
            errors.append("lookBackUnit must be one of the string 'minutes','hours','days'")
        elif criteria.lookBackUnit not in ['minutes','hours','days']:
            errors.append("lookBackUnit must be one of the string 'minutes','hours','days'")

        if criteria.lookBack:
            if not isinstance(criteria.lookBack,int):
                errors.append("lookBack must be a positive integer value")
            elif criteria.lookBack <=0:
                errors.append("lookBack must be a positive integer value")

        if bool(criteria.areaName) + bool(criteria.listName) + bool(criteria.vesselCategory) \
                + bool(criteria.vesselType) == 0: 
            errors.append("At least one of the criteria: areaName, listName, vesselCategory, vesselType must be specified")
        elif  bool(criteria.listName) + bool(criteria.vesselCategory) + bool(criteria.vesselType) > 1:
            errors.append("No more than one of the criteria listname, vesselCategory and vesselType must be specified")

        if criteria.areaName and not isinstance(criteria.areaName,str):
            errors.append("areaName must be a string")
        
        if criteria.listName and not isinstance(criteria.listName,str):
            errors.append("listName must be a string")

        if criteria.vesselCategory:
            vc_str = ", ".join(ApiEndPoints.valid_vessel_categories())
            if criteria.vesselCategory and not isinstance(criteria.vesselCategory,str):
                errors.append("vesselCategory must be one of the strings " + vc_str )
            elif criteria.vesselCategory not in ApiEndPoints.valid_vessel_categories(): 
                errors.append("vesselCategory must be one of the strings " + vc_str )
        
        if criteria.vesselType:
            vt_str = ", ".join(ApiEndPoints.valid_vessel_types())
            if criteria.vesselType and not isinstance(criteria.vesselType,str):
                errors.append("vesselType must be one of the strings " + vt_str )
            elif criteria.vesselType not in ApiEndPoints.valid_vessel_types():
                errors.append("vesselType must be one of the strings " + vt_str )
        
        return errors

    def __validate_pending_query_info(self,pq:Dict[str,Any])->bool:
        """ Validate the content of the PendingQueryInfo object returned
        by a search query,
        Return True if valid
        """
        if "serverTime" not in pq or \
            "queryToken" not in pq or \
            "statusQueryInterval" not in pq or \
            "queryStatus" not in pq or \
            "elapsedTime" not in pq:
            return False
        return True


    def __convert_dict_to_pending_query_tuple(self,pq:Dict[str,Any])->PendingQueryInfo:
        """ Convert a PendingQueryInfo object returned from a search query
        into a PendingQueryInfo NamedTuple"""
        tmp = PendingQueryInfo(serverTime=pq["serverTime"],
                            queryToken=pq.get("queryToken",""),
                            statusQueryInterval=pq.get("statusQueryInterval",0),
                            queryStatus=pq.get("queryStatus",""),
                            elapsedTime=pq.get("elapsedTime",0),
                            #estimatedCompletionTime=pq.get("estimatedCompletionTime",None),
                            errorMsg=pq.get("errorMsg",""))
        return tmp



    def __search_criteria_to_dictionary(self, criteria:SearchCriteria)->Dict[str,Any]:
        """ Converts the search criteria object into a dictionary which can
        be converted to json for inclusion in the body of the request.
        The criteria object is assumed to be VALID
        """
        tmp_dict:Dict[str,Any] = dict()
        tmp_dict["outputFormat"] = criteria.format
        tmp_dict["latestPosition"] = criteria.latestPosition
        if criteria.listName:
            tmp_dict["listName"] = criteria.listName
        if criteria.areaName:
            tmp_dict["areaName"] = criteria.areaName
        if criteria.vesselCategory:
            tmp_dict["vesselCategory"] = criteria.vesselCategory
        if criteria.vesselType:
            tmp_dict["vesselType"] = criteria.vesselType
        if criteria.forcePending:
            tmp_dict["forcePending"] = True
        if criteria.lookBack:
            tmp_dict["dates"] = {"lookBack": criteria.lookBack, "unit": criteria.lookBackUnit}
        elif isinstance(criteria.startDate,datetime) and isinstance(criteria.stopDate,datetime):
            # the condition above removes the linter error
            tmp_dict["dates"] = {"startDate": criteria.startDate.strftime("%Y-%m-%dT%H:%M:%SZ") , "stopDate": criteria.stopDate.strftime("%Y-%m-%dT%H:%M:%SZ")}
        else:
            # This should never be reached
            assert(False)
        return tmp_dict

    #-------------------------------------------------------------
    #  Logging Utilities 
    #-------------------------------------------------------------
    def write_url_and_headers_to_log(self, r:requests.Response):
        """ Write the raw request and response to the log file
            They are preceded by the current date.
        """
        # Write the date on its own line
        dt = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S.%f")
        dt = '\n---------------- ' + dt + '-------------------------'
        self.log.write(dt.encode())
        self.log.write(b"\n")
        # Write the status code
        self.log.write(b"StatusCode: ")
        code = str(r.status_code)
        self.log.write(code.encode())
        self.log.write(b"\n")
        # Method and headers
        self._write_method_and_headers(r)
        # Write the URL
        if r.request.url:
            self.log.write(r.request.url.encode())
        else:
            self.log.write(b"No Url")
        self.log.write(b"\n")


    def write_response_to_log(self, r:requests.Response):
        """ Write the raw request and response to the log file
            They are preceded by the current date.
        """
        # Write the date on its own line
        dt = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S.%f")
        dt = '\n---------------- ' + dt + '-------------------------'
        self.log.write(dt.encode())
        self.log.write(b"\n")
        # Write the status code
        self.log.write(b"StatusCode: ")
        code = str(r.status_code)
        self.log.write(code.encode())
        self.log.write(b"\n")
        # headers
        self._write_method_and_headers(r)
        # Write the URL
        if r.request.url:
            self.log.write(r.request.url.encode())
        else:
            self.log.write(b"No Url")
        self.log.write(b"\n")
        # Write the body of the request. Truncated if too long
        if isinstance(r.request.body, str):
            self.log.write(r.request.body[0:10000].encode())
        elif isinstance(r.request.body, bytes):
            self.log.write(r.request.body[0:10000])
        else:
            self.log.write(b"Request has no body")
        self.log.write(b"\n")
        # Write the body of the answer. Truncated if too long
        self.log.write(r.content[0:10000])
        self.log.write(b"\n")

    def _write_method_and_headers(self, r:requests.Response)->None:
        """Write the request method and headers and the response headers to the log
        
        Args:
            r: Response object
            
        """
        # Write the HTTP verb
        self.log.write(f"-- HTTP Verb: {r.request.method}\n".encode('utf8'))
        # Write the headers
        self.log.write(b"-- Request Headers\n")
        #self.log.write(str(r.request.headers).encode('utf8'))
        for key,val in r.request.headers.items():
            self.log.write(f"\t{key}: {val}\n".encode('utf8'))
        self.log.write(b"-- Response Headers:\n")
        #self.log.write(str(r.headers).encode('utf8'))
        for key,val in r.headers.items():
            self.log.write(f"\t{key}: {val}\n".encode('utf8'))
        self.log.write(b"\n")
