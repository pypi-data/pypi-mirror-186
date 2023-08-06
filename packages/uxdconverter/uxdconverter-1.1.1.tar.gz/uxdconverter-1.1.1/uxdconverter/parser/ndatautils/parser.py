# -*- coding: utf-8 -*-
# *****************************************************************************
# Copyright (c) 2017 by the ndatautils contributors (see AUTHORS)
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Module authors:
#   Lukas Beddrich <lukas.beddrich@frm2.tum.de>
#
# *****************************************************************************

import numpy as np
import re

from os import path


class DataPath:
    """
    Class to generate the appropriate path to a data file condidering instrument, proposal and file type
    as used by NICOS instrument control software
    """

    def __init__(self, instrument, proposalnum, root, ending=".dat"):
        """
        Initializes a DataPath instance.
        """
        if instrument.upper() == "MIRA":
            self.instrument = "MIRA"
        elif instrument.upper() == "RESEDA":
            self.instrument = "RESEDA"
        elif instrument.upper() == "KOMPASS":
            self.instrument = "KOMPASS"
        elif instrument.upper() == "PANDA":
            self.instrument = "PANDA"
        elif instrument.upper() == "NLAUE":
            self.instrument = "NLAUE"
        else:
            print(
                "The specified instrument is not recognized. Expected inputs are:\n\t'MIRA' \n\t'RESEDA' \n\t'KOMPASS' \ņ\t'NLAUE'")

        self.root = root
        self.proposalnum = proposalnum
        self.ending = ending

    # ---------------------------------------------------------------------------------------------------

    def __call__(self, fnum):
        """
        Calls the 'gen_path' method.
        """

        return self.gen_path(fnum)

    # ---------------------------------------------------------------------------------------------------

    def gen_path(self, fnum):
        """
        Returns the path of a specified datafile by its filenumber. Hands task to correct path generator
        """

        if self.instrument == "MIRA":
            return self.__gen_path_MIRA(fnum)

        elif self.instrument == "RESEDA":
            return self.__gen_path_RESEDA(fnum)

        elif self.instrument == "KOMPASS":
            return self.__gen_path_KOMPASS(fnum)

        elif self.instrument == "PANDA":
            return self.__gen_path_PANDA(fnum)

        elif self.instrument == "NLAUE":
            return self.__gen_path_NLAUE(fnum)

    # ---------------------------------------------------------------------------------------------------

    def __gen_path_MIRA(self, fnum):
        """
        Generates the path for a MIRA-type ASCII data file or MIEZE-TOF file.
        """

        if self.ending == ".dat":
            return path.join(self.root, str(self.proposalnum), "data",
                             str(self.proposalnum) + "_%08d" % (fnum) + ".dat")

        elif self.ending == ".tof":
            return path.join(self.root, str(self.proposalnum), "data", "cascade", "%08d" % (fnum) + ".tof")

        elif self.ending == ".pad":
            return path.join(self.root, str(self.proposalnum), "data", "cascade", "%08d" % (fnum) + ".pad")

        else:
            print("No valid file ending!")
            return None

    # ---------------------------------------------------------------------------------------------------

    def __gen_path_RESEDA(self, fnum):
        """
        Generates the path for a RESEDA-type ASCII data file, MIEZE-TOF file, CASCADE-PAD file.
        """

        if self.ending == ".dat":
            return path.join(self.root, "p{}".format(self.proposalnum), "data",
                             "p{}".format(self.proposalnum) + "_%08d" % (fnum) + ".dat")

        elif self.ending == ".tof":
            return path.join(self.root, "p{}".format(self.proposalnum), "data", "cascade", "%08d" % (fnum) + ".tof")

        elif self.ending == ".pad":
            return path.join(self.root, "p{}".format(self.proposalnum), "data", "cascade", "%08d" % (fnum) + ".pad")

        else:
            print("No valid file ending!")
            return None

    # ---------------------------------------------------------------------------------------------------

    def __gen_path_KOMPASS(self, fnum):
        """
        Not yet implemented
        Generates the path for a KOMPASS-type ASCII data file
        """

        print("Path generation for KOMPASS data is not yet implemented.")
        return None

    # ---------------------------------------------------------------------------------------------------

    def __gen_path_PANDA(self, fnum):
        """
        Generates the path for a RESEDA-type ASCII data file, MIEZE-TOF file, CASCADE-PAD file.
        """

        if self.ending == ".dat":
            return path.join(self.root, "p{}".format(self.proposalnum), "data",
                             "p{}".format(self.proposalnum) + "_%08d" % (fnum) + ".dat")

        else:
            print("No valid file ending!")
            return None

    # ---------------------------------------------------------------------------------------------------

    def __gen_path_NLAUE(self, fnum):
        """
        Not yet implemented
        Generates the path for a NLAUE-type
        """

        print("Path generation for NLAUE data is not yet implemented.")
        return None

class FileLoaderBase:
    """
    Base class for loading the data from specified file
    """

    def __init__(self, datapath, instrumentloader=None):
        """
        Initializes a FileLoaderBase instance

        Parameters
        ----------
        datapath : DataPath
            DataPath object to retrieve the required file name via datapath(fnum)
            The file needs to be a '.tof' or '.pad' file as created by NICOS from
            a CASCADE detector's output.
        instrumentloader: InstrumentLoader, a subclass
            Not yet implemented

        Returns
        -------

        Notes
        -----
        """

        self.datadict = {}
        self.datapath = datapath
        if instrumentloader == None:
            self.metadata = True  # Workaround until InstrumentLoader(s) are implemented
            self.rawdata = True  # Workaround until InstrumentLoader(s) are implemented
            self.instrumentloader = None
        else:
            self.instrumentloader = instrumentloader

    # ---------------------------------------------------------------------------------------------------

    def __call__(self, fnum, metadata=True, rawdata=True):
        """
        Instance calls the read_out_data method
        """

        return self.read_out_data(fnum)

    # ---------------------------------------------------------------------------------------------------

    def _meta_data(self, fnum):
        """
        Extracts metadata from a ".pad" or ".tof" file. If some quantities are specified in a
        self.metadata dictionary, only their values are retrieved
        Dictionary key formating is possible if necesary information is provided

        Parameters
        ----------
        fnum : int
            passed to the self.datapath instance to get path of the data file

        NOT (YET) IMPLEMENTED
        ---------------------
        --> Specification of retrieved metadata
        --> providing aliases for formating klunky key-strings in metadict
        """

        print("This is the FileLoaderBase._meta_data function, which does not provide functionality.\
              The function needs to be overloaded by a subclass")
        return {'requested data': 'None'}

    # ---------------------------------------------------------------------------------------------------

    def _raw_data(self, fnum):
        """
        Extracts rawdata from a ".pad" or ".tof" file. If a array shape is specified in a
        self.rawdata tuple, and the returned array is shaped accordingly
        MAYBE a fucntionality for summation over some axis will be added here as well

        Parameters
        ----------
        fnum : int
            passed to the self.datapath instance to get path of the data file

        NOT (YET) IMPLEMENTED
        ---------------------
        --> summation or mean calculation on the raw data
        """

        print("This is the FileLoaderBase._raw_data function, which does not provide functionality.\
              The function needs to be overloaded by a subclass")
        return {'requested data': 'None'}

    # ---------------------------------------------------------------------------------------------------

    def format_metadata(self):
        """
        Restructures self.datadict["metadata"]. Selects and possibly renames the metadata keys
        according to specifications in self.instrumentloader.instance_dict['metadata'].

        Notes
        -----
        self.instrumentloader.get_Loader_settings('metadata') --> {'mainkey1' : [[subkey1, None], [subkey2, alias2],
                                                                                 [subkey3, alias3], ...],
                                                                   'mainkey2' : [[subkey1, alias1], [subkey2, None],
                                                                                 [subkey3, alias3], ...], ...}
        """

        tempdict = {}
        for mainkey in self.instrumentloader.get_Loader_settings('metadata'):
            tempdict[mainkey] = {}
            for subkey, alias in self.instrumentloader.get_Loader_settings('metadata')[mainkey]:
                if alias != None:
                    tempdict[mainkey][alias] = self.datadict[mainkey][subkey]
                else:
                    tempdict[mainkey][subkey] = self.datadict[mainkey][subkey]

        self.datadict['metadict'] = tempdict

    # ---------------------------------------------------------------------------------------------------

    def read_out_data(self, fnum):
        """
        Updates the datadict with the metadata and rawdata (as specified via instrumentloader) for a
        file with number fnum.
        For specifics refer to subclass._meta_data and subclass._raw_data
        """

        if self.instrumentloader is not None:
            if isinstance(self.instrumentloader.get_Loader_settings('metadata'), dict):
                self.datadict.update({'metadata': self._meta_data(fnum)})
                self.format_metadata()
            elif self.instrumentloader.get_Loader_settings('metadata'):
                self.datadict.update({'metadata': self._meta_data(fnum)})
            else:
                self.datadict.update({'metadata': {'requested data': 'None'}})

            if isinstance(self.instrumentloader.get_Loader_settings('rawdata'), tuple):
                self.datadict.update({'rawdata': self._raw_data(fnum)})
            elif self.instrumentloader.get_Loader_settings('rawdata'):
                self.datadict.update({'rawdata': self._raw_data(fnum)})
            else:
                self.datadict.update({'rawdata': {'requested data': 'None'}})


        else:
            if self.metadata:
                self.datadict.update({'metadata': self._meta_data(fnum)})
            else:
                self.datadict.update({'metadata': {'requested data': 'None'}})

            # THIS PART NEEDS MAJOR REWORKS DUE TO USAGE OF STRUCTURED ARRAYS
            if self.rawdata:
                self.datadict.update({'rawdata': self._raw_data(fnum)})
            else:
                self.datadict.update({'rawdata': {'requested data': 'None'}})


class ASCIILoader(FileLoaderBase):
    """
    Loads data from '.tof' and '.pad' files from the CASCADE detector used at MIRA and RESEDA.
    """

    # =============================================================================
    #     def __init__(self, datapath, instrumentloader = None):
    #         """
    #         Initializes a CascadeLoader instance
    #
    #         Parameters
    #         ----------
    #         datapath : DataPath
    #             DataPath object to retrieve the required file name via datapath(fnum)
    #             The file needs to be a '.tof' or '.pad' file as created by NICOS from
    #             a CASCADE detector's output.
    #         instrumentloader: InstrumentLoader, a subclass
    #             Not yet implemented
    #
    #         Returns
    #         -------
    #
    #         Notes
    #         -----
    #         """
    #
    #         self.datadict = {}
    #         self.datapath = datapath
    #         if instrumentloader == None:
    #             self.metadata = True                    # Workaround until InstrumentLoader(s) are implemented
    #             self.rawdata = True                     # Workaround until InstrumentLoader(s) are implemented
    #             self.instrumentloader = None
    #         else:
    #             self.instrumentloader = instrumentloader
    # =============================================================================

    # ---------------------------------------------------------------------------------------------------

    # =============================================================================
    #     def __call__(self, fnum, metadata = True, rawdata = True):
    #         """
    #         Instance calls the read_out_data method
    #         """
    #
    #         return self.read_out_data(fnum)
    # =============================================================================

    # ---------------------------------------------------------------------------------------------------

    def _meta_data(self, fnum):
        """
        Extracts metadata from a ".pad" or ".tof" file. If some quantities are specified in a
        self.metadata dictionary, only their values are retrieved
        Dictionary key formating is possible if necesary information is provided

        Parameters
        ----------
        fnum : int
            passed to the self.datapath instance to get path of the data file

        NOT (YET) IMPLEMENTED
        ---------------------
        --> Specification of retrieved metadata
        --> providing aliases for formating klunky key-strings in metadict
        """

        valuereo = re.compile("[+-]?\d+[\.e+-]{0,2}\d*")
        unitreo = re.compile("\s[A-Za-z]{1,4}[\-\d]{0,2}$")  # strip " "

        currentkey = "binarydump"
        metadict = {currentkey: {}}
        with open(self.datapath(fnum), "rb") as f:

            for line in f.readlines():
                try:
                    temp = line.decode("utf-8")[1:].strip().split(':')  # [1:] omits the first '#'
                except:
                    pass

                if len(temp) == 1 and temp[0][:2] == "##":  # find only '##' because the first one was omitted earlier
                    currentkey = temp[0][2:].strip()
                    metadict[currentkey] = {}

                elif len(temp) == 1 and currentkey == "Scan data":
                    data_aquisition_setting = tuple(re.findall('[A-Za-z0-9\._\-;]+', temp[0]))
                    if len(metadict[currentkey]) == 0:
                        metadict[currentkey]['names'] = data_aquisition_setting
                    elif len(metadict[currentkey]) == 1:
                        metadict[currentkey]['units'] = data_aquisition_setting

                elif len(temp) == 2:
                    val_result = valuereo.findall(temp[1])
                    unit_result = unitreo.findall(temp[1])

                    if len(val_result) == 1 and len(unit_result) != 0:
                        metadict[currentkey][temp[0].strip()] = (float(val_result[0]), unit_result[0].strip())

                    elif len(val_result) > 1 and len(unit_result) != 0:
                        metadict[currentkey][temp[0].strip()] = (
                        tuple((float(val) for val in val_result)), unit_result[0].strip())

                    elif len(val_result) > 1 and len(unit_result) == 0:
                        metadict[currentkey][temp[0].strip()] = tuple((float(val) for val in val_result))

                    elif len(val_result) == 1 and len(unit_result) == 0:
                        try:
                            metadict[currentkey][temp[0].strip()] = int(val_result[0])
                        except ValueError:
                            try:
                                metadict[currentkey][temp[0].strip()] = float(val_result[0])
                            except:
                                print(
                                    "The encountered 'val_result' was neither a integer as string, nor a flaotable string")
                                raise

                    else:
                        metadict[currentkey][temp[0].strip()] = temp[1].strip()

                elif len(temp) == 3:
                    if temp[1].strip() == "http" or temp[1].strip() == "https":
                        metadict[currentkey][temp[0].strip()] = ":".join((temp[1], temp[2]))
                    else:
                        metadict[currentkey][temp[0].strip()] = (temp[1].strip(), temp[2].strip())

                elif len(temp) == 4:
                    metadict[currentkey][temp[0].strip()] = (
                    temp[1].strip(), " : ".join((temp[2].strip(), temp[3].strip())))

        del metadict["binarydump"]
        return metadict

    # ---------------------------------------------------------------------------------------------------

    def _raw_data(self, fnum):
        """
        Extracts array data from '.dat' file

        Parameters
        ----------
        fnum : int
            passed to the self.datapath instance to get path of the data file

        NOT (YET) IMPLEMENTED
        ---------------------
        --> shaping of the data array
        --> summation or mean calculation on the raw data
        """

        data_as_string = np.genfromtxt(self.datapath(fnum), dtype=str)

        if self.instrumentloader != None and self.instrumentloader.get_Loader_settings('array_format') != None:
            #            print("For debugging purposes: ",data_as_string[:3]) #DEBUGGING
            return np.array(list(zip(*data_as_string.T)),
                            dtype=self.instrumentloader.get_Loader_settings('array_format'))
        elif self.instrumentloader:
            try:
                names = self.datadict['metadata']['Scan data']['names']
            except KeyError:
                self.datadict.update({'metadata': self._meta_data(fnum)})
                names = self.datadict['metadata']['Scan data']['names']

            dtype = self.instrumentloader.dtype_from_string_array(data_as_string[0], names)

            return np.array(list(zip(*data_as_string.T)), dtype=dtype)
        else:
            raise IOError("The data format is not correctly specified!")

    # ---------------------------------------------------------------------------------------------------

    # =============================================================================
    #     def read_out_data(self, fnum):
    #         """
    #         Updates the datadict with the metadata and rawdata (as specified via instrumentloader) for a
    #         file with number fnum.
    #         For specifics refer to ASCIILoader._meta_data and ASCIILoader._raw_data
    #         """
    #
    #         if self.instrumentloader is not None:
    #             if isinstance(self.instrumentloader.get_Loader_settings('metadata'), dict):
    #                 self.datadict.update({'metadata' : self._meta_data(fnum)})
    #             elif self.instrumentloader.get_Loader_settings('metadata'):
    #                 self.datadict.update({'metadata' : self._meta_data(fnum)})
    #             else:
    #                 self.datadict.update({'metadata' : {'requested data' : 'None'}})
    #
    #             if isinstance(self.instrumentloader.get_Loader_settings('rawdata'), tuple):
    #                 self.datadict.update({'rawdata'  : self._raw_data(fnum)})
    #             elif self.instrumentloader.get_Loader_settings('rawdata'):
    #                 self.datadict.update({'rawdata'  : self._raw_data(fnum)})
    #             else:
    #                 self.datadict.update({'rawdata' : {'requested data' : 'None'}})
    #
    #
    #         else:
    #             if self.metadata:
    #                 self.datadict.update({'metadata' : self._meta_data(fnum)})
    #             else:
    #                 self.datadict.update({'metadata' : {'requested data' : 'None'}})
    #
    #         # THIS PART NEEDS MAJOR REWORKS DUE TO USAGE OF STRUCTURED ARRAYS
    #             if self.rawdata:
    #                 self.datadict.update({'rawdata'  : self._raw_data(fnum)})
    #             else:
    #                 self.datadict.update({'rawdata' : {'requested data' : 'None'}})
    # =============================================================================

    # ---------------------------------------------------------------------------------------------------

    def fnums_from_structured_array(self):
        """
        Returns the file numbers 'fnum' gathered in a ASCII file's strucutred array
        """

        if self.datadict:
            try:
                return [int(re.findall('\d+', struct_line[-1].decode("utf-8"))[0]) for struct_line in
                        self.datadict['rawdata']]
            except KeyError:
                print("Probaly self.datadict['rawdata'] is non-exsistant!")
            except AttributeError:
                print("Probaly no proper entries in self.datadict['rawdata'] for decoding or conversion to integer!")

        else:
            print("So far no data was loaded in the self.datadict variable.")


class InstrumentLoader(object):
    """
    Base class for specialized InstrumentLoader classes (MIRALoader, RESEDALoader, ...)
    """

    def __init__(self, metadata=True, rawdata=True, array_format=None, **kwargs):
        """
        Initializes a InstumentLoader instance

        Parameters
        ----------
        metadata : bool, dict, str
            bool -> values trigger return of all metadata values (True) or none (False)
            dict -> has to specify which values to select, by specifying the
            correct main and subkeys of a "loader-object".datadict["metadata"]
            str -> path to a json-formatted metadata_alias file from which the dictionary
            can be recovered
        rawdata : bool
            triggers return of all metadata values (True) or none (False)
        array_format : None, tuple, "Whatever is necessary to define a structured array"
        kwargs : additional settings to specify a loader-objects output

        Returns
        -------

        Notes
        -----
        """

        self.instance_dict = {"metadata": self.__process_metadata(metadata),
                              "rawdata": rawdata,
                              "array_format": array_format}
        self.set_Loader_settings(**kwargs)

    # ---------------------------------------------------------------------------------------------------

    def __process_metadata(self, metadata):
        """
        Checks for validity of the passed metadata. Loads dict from json-formatted metadata_alias file.

        Parameters
        ----------
        metadata : bool, dict, str
            bool -> values trigger return of all metadata values (True) or none (False)
            dict -> has to specify which values to select, by specifying the
            correct main and subkeys of a "loader-object".datadict["metadata"]
            str -> path to a json-formatted metadata_alias file from which the dictionary
            can be recovered

        Returns
        -------
        ret : bool, dict
            bool -> values trigger return of all metadata values (True) or none (False)
            dict -> specifies which values to select, by specifying the
            correct main- and subkeys of a "loader-object".datadict["metadata"]
        """

        if isinstance(metadata, bool):
            return metadata
        elif isinstance(metadata, dict):  # Possibility to check the dictionary for having a valid structure
            return metadata
        elif isinstance(metadata, str):
            with open(metadata, 'r') as jsonfile:
                meta_aliases = json.load(jsonfile)
            return meta_aliases
        else:
            print("No valid Input was provided as setting for metadata. 'False' was returned!")
            return False

    # ---------------------------------------------------------------------------------------------------

    def __call__(self, *args):
        """
        Returns the values corresponding to the keys supplied by args

        Parameters
        ----------
        args : str
            keys to querry the instances_dictionary for associated values

        Returns
        -------
        querried : dict
            dictionary of the querried values
        """

        return self.get_Loader_settings(*args)

    # ---------------------------------------------------------------------------------------------------

    def get_Loader_settings(self, *args):
        """
        Returns the values corresponding to the keys supplied by args

        Parameters
        ----------
        args : str
            keys to querry the instances_dictionary for associated values

        Returns
        -------
        querried : dict
            dictionary of the querried values
        """

        querried = []

        for key in args:
            try:
                querried.append((key, self.instance_dict[key]))
            except KeyError:
                print("No value can be found for key: '{}'".format(key))
                querried.append((key, None))

        if len(querried) == 1:
            return querried[0][1]  # returnind only the value seems more sensible...
        else:
            return dict(querried)

    # ---------------------------------------------------------------------------------------------------

    def set_Loader_settings(self, **kwargs):
        """
        Updates the settings (entries) in the self.instance_dict

        Parameters
        ----------
        kwargs : additional settings to specify a loader-objects output
        """

        self.instance_dict.update(dict(kwargs))

    # ---------------------------------------------------------------------------------------------------

    def dtype_from_string_array(self, first_line, scan_data_names):
        """
        Generates a numpy.dtype object from the first line of the ".dat" file data set.

        Parameters
        ----------
        first_line : numpy.ndarray with dtype = bytes
        scan_data_names : list (with strings)

        Returns
        -------
        dt : numpy.dtype
            specifies the format of the data read by a ASCIILoader

        Notes
        -----
        """

        formats = []
        for val in first_line:
            if re.match("[+-]?\d+$", val) is not None:  # if re.match("[+-]?\d+$", val.decode("utf-8")) is not None:
                formats.append("i8")
            elif re.match("[+-]?\d+[\.e+-]{0,2}\d*",
                          val) is not None:  # elif re.match("[+-]?\d+[\.e+-]{0,2}\d*", val.decode("utf-8")) is not None:
                formats.append('f8')
            else:
                formats.append('S{}'.format(len(val)))
        #        print("formats for dtype : {} (type = {})\t\t DEBUGGING".format(formats, type(formats)))
        self.instance_dict['array_format'] = np.dtype({'names': scan_data_names,
                                                       'formats': formats})
        return self.instance_dict['array_format']