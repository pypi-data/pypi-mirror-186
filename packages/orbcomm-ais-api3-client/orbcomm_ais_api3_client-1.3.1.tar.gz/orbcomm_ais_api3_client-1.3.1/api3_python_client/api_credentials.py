"""Credentials and host name for API V3 end points access
"""

from pathlib import Path

class ApiCredentials:
    """ Elements of the credentials used to access the API 3

    All arguments are optional; however if no init_filepath is provided, 
    username and password must be provided.

    Args:
        protocol: "https" is the default and the only acceptable value
        host: "globalais3.orbcomm.net" is the default
        url_path: "" is the default
        username: Username used for server login
        password: Password used for server login
        init_filepath: If present, credentials are read from this file

    """
    # Constants
    # Only for ORBCOMM internal usage
    #: :meta private:
    AISVDS1_IP = "10.203.9.27"      #MW8
    # Only for ORBCOMM internal usage
    #: :meta private:
    AISVDS2_IP = "10.203.9.52"      #MW8
    # Main ORBCOMM domain name
    #: :meta private:
    GLOBALAIS3 = "globalais3.orbcomm.net"  #MW8

    # Default instance values
    #: :meta private:
    protocol = "https"
    #: :meta private:
    host = GLOBALAIS3
    #: :meta private: 
    url_path = ""
    #: :meta private:
    username = ""
    #: :meta private:
    password = ""

    def __init__(self,**kwargs):
        """ Modify the default parameters. Accept only keyword parameters 

        """
        # Verify that all keyword argument passed are valid
        for key in kwargs:
            assert(key in ["protocol","host", "url_path", "username", "password","init_filepath"])
        # Handle the case when a configuration file is provided
        if "init_filepath" in kwargs:
            try:
                self.load(kwargs["init_filepath"])
            except FileNotFoundError:
                print (f"WARNING: Credentials initialization file {kwargs['init_filepath']} was not found")
                pass
        else:         
            # Process keyword arguments individually
            for key in kwargs:
                setattr(self,key,kwargs[key])
                        

    def __eq__(self,other):
        """ Compare 2 instances of credentials """
        assert(isinstance(other,ApiCredentials))
        return(self.password==other.password and 
                self.username == other.username and
                self.host == other.host and
                self.url_path == other.url_path and
                self.protocol == other.protocol)            

    def get_full_url(self) -> str:
        """ Concatenates the components of the full url (protocol, host, url_path)

        Returns: Full URL to access the server
        """
        return self.protocol + "://" + self.host + "/" + self.url_path

    def is_valid(self) -> bool:
        """Checks whether the Credentials instance has syntactically valid
        entries.

        The check verify that both the username and password are not empty

        Returns: True if the :class:ApiCredentials instance is valid

        """
        if not self.username or not self.password:
            return False
        # TODO Check that the full url_path has a correct syntax
        return True

    def pretty_string(self, nbr_tabs:int=0, hide_password:bool=True) -> str:
        """ Returns a pretty string containing the different parameters
        of the object. The password is hidden by default.

        Args:
            nbr_tabs: Number of tab characters in front of the text (default = 0)
            hide_password: If True, password value is displayed as '**********'

        Returns: Text representation of the :class:`ApiCredentials` instance            
        """
        spaces = "\t"*nbr_tabs
        if hide_password:
            password_string = "**********"
        else:
            password_string = self.password

        pp = (
            f"{spaces}Username: {self.username}\n"
            f"{spaces}Password: {password_string}\n"
            f"{spaces}Host: {self.host}\n"
            f"{spaces}URL Path: {self.url_path}\n"
            f"{spaces}Protocol: {self.protocol}\n"
        ) 
        return pp 

    def save(self, filepath:Path) -> None:
        """ Saves the credentials in a file.
    
        The file can be read later with :func:`ApiCredentials.load`.
        
        Args:
            filepath: Path of the file where credentials should be saved
        
        """
        assert(isinstance(filepath,Path))
        import json
        with open(filepath, "w") as fp:
            json.dump(self.__dict__,fp,indent=1)

    def load(self, filepath:Path) -> None:
        """ Read the credentials from a file 
        
        The file read must have been saved with :func:`ApiCredentials.save`
        
        Args:
            filepath: Path of the file from which the credentials should be read.
        
        """
        assert(isinstance(filepath, Path))
        import json
        with open(filepath,"r") as fp:
            val = json.load(fp)
        self.__dict__ = val

    @staticmethod
    def get_host_list():
        """ Return a list of server where each server is a string

        :meta private:
        """
        return ["globalais3", "aisvds1 ip", "aisvds2 ip"]

    def set_host(self, host_name):
        """ Sets the host based on the host name passed. The host name must
        be one of the values returned by get_host_list()

        :meta private:
        """
        assert(host_name in self.get_host_list())

        if host_name == "globalais3":
            self.host = ApiCredentials.GLOBALAIS3
        elif host_name == "aisvds1 ip":
            self.host = ApiCredentials.AISVDS1_IP
        elif host_name == "aisvds2 ip":
            self.host = ApiCredentials.AISVDS2_IP
        


#---------------------------------------------------------------------------------------------------
#                       TEST SECTION
#---------------------------------------------------------------------------------------------------

import unittest
import os

class TestApiCredentials(unittest.TestCase):
    """ Test the Api10Credential class 
    
    :meta private: 
    """

    @classmethod
    def setUpClass(cls):
        """ Text fixtures and parameters """
        cls.credential_filepath= Path("tests/credentials.json")
        parent_dir = cls.credential_filepath.parent
        # Make sure that tests directory exists
        try:
            os.makedirs(parent_dir)
        except FileExistsError:
            pass
        assert(parent_dir.exists() and parent_dir.is_dir())

    def test01_init(self):
        """ __init__ test """
        # Correct key names
        tmp = ApiCredentials(host="hello", url_path="this/is/me", protocol="wert", username="test", password="pwd")
        self.assertEqual(tmp.host, "hello")
        self.assertEqual(tmp.url_path, "this/is/me")
        self.assertEqual(tmp.protocol, "wert")
        self.assertEqual(tmp.username, "test")
        self.assertEqual(tmp.password, "pwd")
        # Invalid key name
        with self.assertRaises(AssertionError):
            tmp = ApiCredentials(host="hello", url_path="this/is/me", protocol="wert", username_wrong="test", password="pwd")  

    def test02_get_full_url(self):
        """ Full url construction test """
        tmp = ApiCredentials(host="hello", url_path="this/is/me", protocol="http")
        self.assertEqual(tmp.get_full_url(), "http://hello/this/is/me")

    def test03_is_valid(self):
        """ Validity verification test """
        tmp = ApiCredentials(username="test", password="pwd")
        self.assertTrue(tmp.is_valid(), "A valid credential set is marked as invalid")
        tmp = ApiCredentials(username="", password="pwd")
        self.assertFalse(tmp.is_valid(), "An invalid credential set is marked as valid")
        tmp = ApiCredentials(username="name", password="")
        self.assertFalse(tmp.is_valid(), "An invalid credential set is marked as valid")

    def test05_get_host_list(self):
        tmp = ApiCredentials.get_host_list()
        self.assertEqual(len(tmp),3)

    def test06_set_host_list(self):
        #tmp = ApiCredentials.test_credentials('generic')
        tmp = ApiCredentials()
        hosts = { "globalais3":"globalais3.orbcomm.net",
                "aisvds1 ip":"10.203.9.27",
                "aisvds2 ip":"10.203.9.52"}
        for host_tag in ApiCredentials.get_host_list():
            tmp.set_host(host_tag)
            self.assertTrue(tmp.host == hosts[host_tag])


    def test08_equality(self):
        """ Equality comparison test """
        A = ApiCredentials(username="hello", password="good", host="me", url_path="you")
        B = ApiCredentials(username="hello", password="good", host="me", url_path="you")
        C = ApiCredentials(username="hello", password="good", host="him", url_path="you")
        self.assertIsNot(A,B)
        self.assertIsNot(B,C)
        self.assertEqual(A,B)
        self.assertNotEqual(A,C)

    def test09_save_restore(self):
        """ Saving and Reading credentials from file """
        tmp = ApiCredentials(host="hello", url_path="this/is/me", protocol="wert", username="test", password="pwd")
        tmp.save(self.credential_filepath)
        new = ApiCredentials()
        new.load(self.credential_filepath)
        self.assertEqual(new,tmp)

    def test10_init_from_file(self):
        """ Creation of object from init file """
        ref = ApiCredentials(host="hello", url_path="this/is/me", protocol="wert", username="test", password="pwd")
        # File exists
        tmp = ApiCredentials(init_filepath=self.credential_filepath)     
        self.assertEqual(tmp, ref, "Object created from init file is not as expected")   
        # File does not exists
        tmp = ApiCredentials(init_filepath=Path("tests/doesnotexist.json")) 





if __name__ == "__main__":
    unittest.main(verbosity=2)