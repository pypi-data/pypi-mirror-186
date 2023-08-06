# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMControl.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5 RecurDynCOMControl Type Library'
makepy_version = '0.5.01'
python_version = 0x3080af0

import win32com.client.CLSIDToClass, pythoncom, pywintypes
import win32com.client.util
from pywintypes import IID
from win32com.client import Dispatch
from enum import IntEnum

# The following 3 lines may need tweaking for the particular server
# Candidates are pythoncom.Missing, .Empty and .ArgNotFound
defaultNamedOptArg=pythoncom.Empty
defaultNamedNotOptArg=pythoncom.Empty
defaultUnnamedArg=pythoncom.Empty

CLSID = IID('{B24FA6EC-3A5D-4CAA-9580-B6315C74080B}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class ControlCoSimDataType(IntEnum):
	'''
	ControlCoSimDataType enumeration.
	'''
	ControlCoSimDataType_Double   =0         
	'''Constant value is 0.'''
class ControlCoSimFMIInterfaceTimeStepUnit(IntEnum):
	'''
	ControlCoSimFMIInterfaceTimeStepUnit enumeration.
	'''
	ControlCoSimFMIInterfaceTimeStepUnit_Millisecond=1         
	'''Constant value is 1.'''
	ControlCoSimFMIInterfaceTimeStepUnit_Second=0         
	'''Constant value is 0.'''
class ControlCoSimFMIType(IntEnum):
	'''
	ControlCoSimFMIType enumeration.
	'''
	ControlCoSimFMIType_Export    =1         
	'''Constant value is 1.'''
	ControlCoSimFMIType_Import    =0         
	'''Constant value is 0.'''
class ControlCoSimFMIVersion(IntEnum):
	'''
	ControlCoSimFMIVersion enumeration.
	'''
	ControlCoSimFMIVersion_V10    =0         
	'''Constant value is 0.'''
	ControlCoSimFMIVersion_V20    =1         
	'''Constant value is 1.'''
class ControlCoSimHostProgram(IntEnum):
	'''
	ControlCoSimHostProgram enumeration.
	'''
	ControlCoSimHostProgram_General=1         
	'''Constant value is 1.'''
	ControlCoSimHostProgram_RecurDyn=2         
	'''Constant value is 2.'''
	ControlCoSimHostProgram_Simulink=0         
	'''Constant value is 0.'''
class ControlCoSimInterfaceVersion(IntEnum):
	'''
	ControlCoSimInterfaceVersion enumeration.
	'''
	ControlCoSimInterfaceVersion_1_0=0         
	'''Constant value is 0.'''
	ControlCoSimInterfaceVersion_2_0=1         
	'''Constant value is 1.'''
	ControlCoSimInterfaceVersion_3_0=2         
	'''Constant value is 2.'''
class ControlCoSimType(IntEnum):
	'''
	ControlCoSimType enumeration.
	'''
	ControlCoSimType_AMESim       =3         
	'''Constant value is 3.'''
	ControlCoSimType_FMI          =4         
	'''Constant value is 4.'''
	ControlCoSimType_General      =1         
	'''Constant value is 1.'''
	ControlCoSimType_Simplorer    =2         
	'''Constant value is 2.'''
	ControlCoSimType_Simulink     =0         
	'''Constant value is 0.'''

from win32com.client import DispatchBaseClass
class IControlCoSim(DispatchBaseClass):
	'''Control CoSim'''
	CLSID = IID('{0C8DABD9-7480-48E0-A8BF-68076ACB5DD8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_HostProgram(self):
		return self._ApplyTypes_(*(4001, 2, (3, 0), (), "HostProgram", '{55D18C89-86D8-4FEC-8DED-5089814F6AC9}'))
	def _get_InterfaceVersion(self):
		return self._ApplyTypes_(*(4000, 2, (3, 0), (), "InterfaceVersion", '{F8C9332E-B812-479B-9E28-C61411BDC309}'))
	def _get_PlantFileName(self):
		return self._ApplyTypes_(*(4002, 2, (8, 0), (), "PlantFileName", None))
	def _get_SamplingPeriod(self):
		return self._ApplyTypes_(*(4003, 2, (5, 0), (), "SamplingPeriod", None))

	def _set_HostProgram(self, value):
		if "HostProgram" in self.__dict__: self.__dict__["HostProgram"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_InterfaceVersion(self, value):
		if "InterfaceVersion" in self.__dict__: self.__dict__["InterfaceVersion"] = value; return
		self._oleobj_.Invoke(*((4000, LCID, 4, 0) + (value,) + ()))
	def _set_SamplingPeriod(self, value):
		if "SamplingPeriod" in self.__dict__: self.__dict__["SamplingPeriod"] = value; return
		self._oleobj_.Invoke(*((4003, LCID, 4, 0) + (value,) + ()))

	HostProgram = property(_get_HostProgram, _set_HostProgram)
	'''
	Host Program

	:type: recurdyn.Control.ControlCoSimHostProgram
	'''
	InterfaceVersion = property(_get_InterfaceVersion, _set_InterfaceVersion)
	'''
	Interface Version

	:type: recurdyn.Control.ControlCoSimInterfaceVersion
	'''
	PlantFileName = property(_get_PlantFileName, None)
	'''
	Plant File Name

	:type: str
	'''
	SamplingPeriod = property(_get_SamplingPeriod, _set_SamplingPeriod)
	'''
	Sampling Period

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_HostProgram": _set_HostProgram,
		"_set_InterfaceVersion": _set_InterfaceVersion,
		"_set_SamplingPeriod": _set_SamplingPeriod,
	}
	_prop_map_get_ = {
		"HostProgram": (4001, 2, (3, 0), (), "HostProgram", '{55D18C89-86D8-4FEC-8DED-5089814F6AC9}'),
		"InterfaceVersion": (4000, 2, (3, 0), (), "InterfaceVersion", '{F8C9332E-B812-479B-9E28-C61411BDC309}'),
		"PlantFileName": (4002, 2, (8, 0), (), "PlantFileName", None),
		"SamplingPeriod": (4003, 2, (5, 0), (), "SamplingPeriod", None),
	}
	_prop_map_put_ = {
		"HostProgram": ((4001, LCID, 4, 0),()),
		"InterfaceVersion": ((4000, LCID, 4, 0),()),
		"SamplingPeriod": ((4003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlCoSimAMESim(DispatchBaseClass):
	'''Control CoSim AMESim'''
	CLSID = IID('{1BC86F13-0032-45C7-9A70-288D4BAE8AA5}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_InterfaceTimeStep(self):
		return self._ApplyTypes_(*(4000, 2, (5, 0), (), "InterfaceTimeStep", None))
	def _get_ModelFileName(self):
		return self._ApplyTypes_(*(4001, 2, (8, 0), (), "ModelFileName", None))

	def _set_InterfaceTimeStep(self, value):
		if "InterfaceTimeStep" in self.__dict__: self.__dict__["InterfaceTimeStep"] = value; return
		self._oleobj_.Invoke(*((4000, LCID, 4, 0) + (value,) + ()))
	def _set_ModelFileName(self, value):
		if "ModelFileName" in self.__dict__: self.__dict__["ModelFileName"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))

	InterfaceTimeStep = property(_get_InterfaceTimeStep, _set_InterfaceTimeStep)
	'''
	Interface Time Step

	:type: float
	'''
	ModelFileName = property(_get_ModelFileName, _set_ModelFileName)
	'''
	Model File Name

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_InterfaceTimeStep": _set_InterfaceTimeStep,
		"_set_ModelFileName": _set_ModelFileName,
	}
	_prop_map_get_ = {
		"InterfaceTimeStep": (4000, 2, (5, 0), (), "InterfaceTimeStep", None),
		"ModelFileName": (4001, 2, (8, 0), (), "ModelFileName", None),
	}
	_prop_map_put_ = {
		"InterfaceTimeStep": ((4000, LCID, 4, 0),()),
		"ModelFileName": ((4001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlCoSimFMI(DispatchBaseClass):
	'''Control CoSim FMI'''
	CLSID = IID('{D647397B-70C5-4703-8EB6-6723E1689F17}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def ExportFMUFile(self):
		'''
		Export a FMU File
		'''
		return self._oleobj_.InvokeTypes(4007, LCID, 1, (24, 0), (),)


	def _get_FMUFileName(self):
		return self._ApplyTypes_(*(4006, 2, (8, 0), (), "FMUFileName", None))
	def _get_InterfaceTimeStep(self):
		return self._ApplyTypes_(*(4004, 2, (5, 0), (), "InterfaceTimeStep", None))
	def _get_InterfaceTimeStepUnit(self):
		return self._ApplyTypes_(*(4011, 2, (3, 0), (), "InterfaceTimeStepUnit", '{C3AD468F-A8C5-4014-96D0-F9DC6DFDD28A}'))
	def _get_InterfaceVersion(self):
		return self._ApplyTypes_(*(4009, 2, (3, 0), (), "InterfaceVersion", '{EC8A3D9C-F40A-4EFC-9D2E-2514A1F87671}'))
	def _get_ModelFileName(self):
		return self._ApplyTypes_(*(4002, 2, (8, 0), (), "ModelFileName", None))
	def _get_PlantFileName(self):
		return self._ApplyTypes_(*(4003, 2, (8, 0), (), "PlantFileName", None))
	def _get_Type(self):
		return self._ApplyTypes_(*(4001, 2, (3, 0), (), "Type", '{B73478A9-7C5B-42CC-BC3F-EA2FAC1D6B68}'))
	def _get_UseFollowingInterfaceTimeOfMaster(self):
		return self._ApplyTypes_(*(4010, 2, (11, 0), (), "UseFollowingInterfaceTimeOfMaster", None))
	def _get_WaitingTime(self):
		return self._ApplyTypes_(*(4005, 2, (5, 0), (), "WaitingTime", None))

	def _set_FMUFileName(self, value):
		if "FMUFileName" in self.__dict__: self.__dict__["FMUFileName"] = value; return
		self._oleobj_.Invoke(*((4006, LCID, 4, 0) + (value,) + ()))
	def _set_InterfaceTimeStep(self, value):
		if "InterfaceTimeStep" in self.__dict__: self.__dict__["InterfaceTimeStep"] = value; return
		self._oleobj_.Invoke(*((4004, LCID, 4, 0) + (value,) + ()))
	def _set_InterfaceTimeStepUnit(self, value):
		if "InterfaceTimeStepUnit" in self.__dict__: self.__dict__["InterfaceTimeStepUnit"] = value; return
		self._oleobj_.Invoke(*((4011, LCID, 4, 0) + (value,) + ()))
	def _set_InterfaceVersion(self, value):
		if "InterfaceVersion" in self.__dict__: self.__dict__["InterfaceVersion"] = value; return
		self._oleobj_.Invoke(*((4009, LCID, 4, 0) + (value,) + ()))
	def _set_ModelFileName(self, value):
		if "ModelFileName" in self.__dict__: self.__dict__["ModelFileName"] = value; return
		self._oleobj_.Invoke(*((4002, LCID, 4, 0) + (value,) + ()))
	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_UseFollowingInterfaceTimeOfMaster(self, value):
		if "UseFollowingInterfaceTimeOfMaster" in self.__dict__: self.__dict__["UseFollowingInterfaceTimeOfMaster"] = value; return
		self._oleobj_.Invoke(*((4010, LCID, 4, 0) + (value,) + ()))
	def _set_WaitingTime(self, value):
		if "WaitingTime" in self.__dict__: self.__dict__["WaitingTime"] = value; return
		self._oleobj_.Invoke(*((4005, LCID, 4, 0) + (value,) + ()))

	FMUFileName = property(_get_FMUFileName, _set_FMUFileName)
	'''
	FMU File Name

	:type: str
	'''
	InterfaceTimeStep = property(_get_InterfaceTimeStep, _set_InterfaceTimeStep)
	'''
	Interface Time Step

	:type: float
	'''
	InterfaceTimeStepUnit = property(_get_InterfaceTimeStepUnit, _set_InterfaceTimeStepUnit)
	'''
	Interface Time Step Unit

	:type: recurdyn.Control.ControlCoSimFMIInterfaceTimeStepUnit
	'''
	InterfaceVersion = property(_get_InterfaceVersion, _set_InterfaceVersion)
	'''
	Interface Version

	:type: recurdyn.Control.ControlCoSimFMIVersion
	'''
	ModelFileName = property(_get_ModelFileName, _set_ModelFileName)
	'''
	Model File Name

	:type: str
	'''
	PlantFileName = property(_get_PlantFileName, None)
	'''
	Plant File Name

	:type: str
	'''
	Type = property(_get_Type, _set_Type)
	'''
	FMI Type

	:type: recurdyn.Control.ControlCoSimFMIType
	'''
	UseFollowingInterfaceTimeOfMaster = property(_get_UseFollowingInterfaceTimeOfMaster, _set_UseFollowingInterfaceTimeOfMaster)
	'''
	Use Following the Interface Time of Master (Host)

	:type: bool
	'''
	WaitingTime = property(_get_WaitingTime, _set_WaitingTime)
	'''
	Waiting Time

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_FMUFileName": _set_FMUFileName,
		"_set_InterfaceTimeStep": _set_InterfaceTimeStep,
		"_set_InterfaceTimeStepUnit": _set_InterfaceTimeStepUnit,
		"_set_InterfaceVersion": _set_InterfaceVersion,
		"_set_ModelFileName": _set_ModelFileName,
		"_set_Type": _set_Type,
		"_set_UseFollowingInterfaceTimeOfMaster": _set_UseFollowingInterfaceTimeOfMaster,
		"_set_WaitingTime": _set_WaitingTime,
	}
	_prop_map_get_ = {
		"FMUFileName": (4006, 2, (8, 0), (), "FMUFileName", None),
		"InterfaceTimeStep": (4004, 2, (5, 0), (), "InterfaceTimeStep", None),
		"InterfaceTimeStepUnit": (4011, 2, (3, 0), (), "InterfaceTimeStepUnit", '{C3AD468F-A8C5-4014-96D0-F9DC6DFDD28A}'),
		"InterfaceVersion": (4009, 2, (3, 0), (), "InterfaceVersion", '{EC8A3D9C-F40A-4EFC-9D2E-2514A1F87671}'),
		"ModelFileName": (4002, 2, (8, 0), (), "ModelFileName", None),
		"PlantFileName": (4003, 2, (8, 0), (), "PlantFileName", None),
		"Type": (4001, 2, (3, 0), (), "Type", '{B73478A9-7C5B-42CC-BC3F-EA2FAC1D6B68}'),
		"UseFollowingInterfaceTimeOfMaster": (4010, 2, (11, 0), (), "UseFollowingInterfaceTimeOfMaster", None),
		"WaitingTime": (4005, 2, (5, 0), (), "WaitingTime", None),
	}
	_prop_map_put_ = {
		"FMUFileName": ((4006, LCID, 4, 0),()),
		"InterfaceTimeStep": ((4004, LCID, 4, 0),()),
		"InterfaceTimeStepUnit": ((4011, LCID, 4, 0),()),
		"InterfaceVersion": ((4009, LCID, 4, 0),()),
		"ModelFileName": ((4002, LCID, 4, 0),()),
		"Type": ((4001, LCID, 4, 0),()),
		"UseFollowingInterfaceTimeOfMaster": ((4010, LCID, 4, 0),()),
		"WaitingTime": ((4005, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlCoSimGeneral(DispatchBaseClass):
	'''Control CoSim General'''
	CLSID = IID('{A596000B-668A-4A1B-84C8-9A1F1249D1F5}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ClientProgramPathName(self):
		return self._ApplyTypes_(*(4051, 2, (8, 0), (), "ClientProgramPathName", None))
	def _get_HostProgram(self):
		return self._ApplyTypes_(*(4001, 2, (3, 0), (), "HostProgram", '{55D18C89-86D8-4FEC-8DED-5089814F6AC9}'))
	def _get_InterfaceVersion(self):
		return self._ApplyTypes_(*(4000, 2, (3, 0), (), "InterfaceVersion", '{F8C9332E-B812-479B-9E28-C61411BDC309}'))
	def _get_PlantFileName(self):
		return self._ApplyTypes_(*(4002, 2, (8, 0), (), "PlantFileName", None))
	def _get_SamplingPeriod(self):
		return self._ApplyTypes_(*(4003, 2, (5, 0), (), "SamplingPeriod", None))
	def _get_WaitingTime(self):
		return self._ApplyTypes_(*(4050, 2, (5, 0), (), "WaitingTime", None))

	def _set_ClientProgramPathName(self, value):
		if "ClientProgramPathName" in self.__dict__: self.__dict__["ClientProgramPathName"] = value; return
		self._oleobj_.Invoke(*((4051, LCID, 4, 0) + (value,) + ()))
	def _set_HostProgram(self, value):
		if "HostProgram" in self.__dict__: self.__dict__["HostProgram"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_InterfaceVersion(self, value):
		if "InterfaceVersion" in self.__dict__: self.__dict__["InterfaceVersion"] = value; return
		self._oleobj_.Invoke(*((4000, LCID, 4, 0) + (value,) + ()))
	def _set_SamplingPeriod(self, value):
		if "SamplingPeriod" in self.__dict__: self.__dict__["SamplingPeriod"] = value; return
		self._oleobj_.Invoke(*((4003, LCID, 4, 0) + (value,) + ()))
	def _set_WaitingTime(self, value):
		if "WaitingTime" in self.__dict__: self.__dict__["WaitingTime"] = value; return
		self._oleobj_.Invoke(*((4050, LCID, 4, 0) + (value,) + ()))

	ClientProgramPathName = property(_get_ClientProgramPathName, _set_ClientProgramPathName)
	'''
	Client Program Path and Name

	:type: str
	'''
	HostProgram = property(_get_HostProgram, _set_HostProgram)
	'''
	Host Program

	:type: recurdyn.Control.ControlCoSimHostProgram
	'''
	InterfaceVersion = property(_get_InterfaceVersion, _set_InterfaceVersion)
	'''
	Interface Version

	:type: recurdyn.Control.ControlCoSimInterfaceVersion
	'''
	PlantFileName = property(_get_PlantFileName, None)
	'''
	Plant File Name

	:type: str
	'''
	SamplingPeriod = property(_get_SamplingPeriod, _set_SamplingPeriod)
	'''
	Sampling Period

	:type: float
	'''
	WaitingTime = property(_get_WaitingTime, _set_WaitingTime)
	'''
	Waiting Time

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_ClientProgramPathName": _set_ClientProgramPathName,
		"_set_HostProgram": _set_HostProgram,
		"_set_InterfaceVersion": _set_InterfaceVersion,
		"_set_SamplingPeriod": _set_SamplingPeriod,
		"_set_WaitingTime": _set_WaitingTime,
	}
	_prop_map_get_ = {
		"ClientProgramPathName": (4051, 2, (8, 0), (), "ClientProgramPathName", None),
		"HostProgram": (4001, 2, (3, 0), (), "HostProgram", '{55D18C89-86D8-4FEC-8DED-5089814F6AC9}'),
		"InterfaceVersion": (4000, 2, (3, 0), (), "InterfaceVersion", '{F8C9332E-B812-479B-9E28-C61411BDC309}'),
		"PlantFileName": (4002, 2, (8, 0), (), "PlantFileName", None),
		"SamplingPeriod": (4003, 2, (5, 0), (), "SamplingPeriod", None),
		"WaitingTime": (4050, 2, (5, 0), (), "WaitingTime", None),
	}
	_prop_map_put_ = {
		"ClientProgramPathName": ((4051, LCID, 4, 0),()),
		"HostProgram": ((4001, LCID, 4, 0),()),
		"InterfaceVersion": ((4000, LCID, 4, 0),()),
		"SamplingPeriod": ((4003, LCID, 4, 0),()),
		"WaitingTime": ((4050, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlCoSimSimplorer(DispatchBaseClass):
	'''Control CoSim Simplorer'''
	CLSID = IID('{7128F4FF-E1F1-4171-86B2-4AC5D5B12754}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_HostProgram(self):
		return self._ApplyTypes_(*(4001, 2, (3, 0), (), "HostProgram", '{55D18C89-86D8-4FEC-8DED-5089814F6AC9}'))
	def _get_InterfaceVersion(self):
		return self._ApplyTypes_(*(4000, 2, (3, 0), (), "InterfaceVersion", '{F8C9332E-B812-479B-9E28-C61411BDC309}'))
	def _get_PlantFileName(self):
		return self._ApplyTypes_(*(4002, 2, (8, 0), (), "PlantFileName", None))
	def _get_SamplingPeriod(self):
		return self._ApplyTypes_(*(4003, 2, (5, 0), (), "SamplingPeriod", None))

	def _set_HostProgram(self, value):
		if "HostProgram" in self.__dict__: self.__dict__["HostProgram"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_InterfaceVersion(self, value):
		if "InterfaceVersion" in self.__dict__: self.__dict__["InterfaceVersion"] = value; return
		self._oleobj_.Invoke(*((4000, LCID, 4, 0) + (value,) + ()))
	def _set_SamplingPeriod(self, value):
		if "SamplingPeriod" in self.__dict__: self.__dict__["SamplingPeriod"] = value; return
		self._oleobj_.Invoke(*((4003, LCID, 4, 0) + (value,) + ()))

	HostProgram = property(_get_HostProgram, _set_HostProgram)
	'''
	Host Program

	:type: recurdyn.Control.ControlCoSimHostProgram
	'''
	InterfaceVersion = property(_get_InterfaceVersion, _set_InterfaceVersion)
	'''
	Interface Version

	:type: recurdyn.Control.ControlCoSimInterfaceVersion
	'''
	PlantFileName = property(_get_PlantFileName, None)
	'''
	Plant File Name

	:type: str
	'''
	SamplingPeriod = property(_get_SamplingPeriod, _set_SamplingPeriod)
	'''
	Sampling Period

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_HostProgram": _set_HostProgram,
		"_set_InterfaceVersion": _set_InterfaceVersion,
		"_set_SamplingPeriod": _set_SamplingPeriod,
	}
	_prop_map_get_ = {
		"HostProgram": (4001, 2, (3, 0), (), "HostProgram", '{55D18C89-86D8-4FEC-8DED-5089814F6AC9}'),
		"InterfaceVersion": (4000, 2, (3, 0), (), "InterfaceVersion", '{F8C9332E-B812-479B-9E28-C61411BDC309}'),
		"PlantFileName": (4002, 2, (8, 0), (), "PlantFileName", None),
		"SamplingPeriod": (4003, 2, (5, 0), (), "SamplingPeriod", None),
	}
	_prop_map_put_ = {
		"HostProgram": ((4001, LCID, 4, 0),()),
		"InterfaceVersion": ((4000, LCID, 4, 0),()),
		"SamplingPeriod": ((4003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlCoSimSimulink(DispatchBaseClass):
	'''Control CoSim Simulink'''
	CLSID = IID('{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def ExportMFileToCreatePlantBlock(self, strName):
		'''
		Obsolete Function
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(4052, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def ExportMFileToCreatePlantBlock2(self):
		'''
		Export M-File to create Plant Block
		'''
		return self._oleobj_.InvokeTypes(4058, LCID, 1, (24, 0), (),)


	def ExportMFileToRunSimulinkModel(self, strName):
		'''
		Obsolete Function
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(4054, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def ExportMFileToRunSimulinkModel2(self):
		'''
		Export M-File to run Simulink Model
		'''
		return self._oleobj_.InvokeTypes(4060, LCID, 1, (24, 0), (),)


	def _get_HostProgram(self):
		return self._ApplyTypes_(*(4001, 2, (3, 0), (), "HostProgram", '{55D18C89-86D8-4FEC-8DED-5089814F6AC9}'))
	def _get_InterfaceVersion(self):
		return self._ApplyTypes_(*(4000, 2, (3, 0), (), "InterfaceVersion", '{F8C9332E-B812-479B-9E28-C61411BDC309}'))
	def _get_MFilePlantBlock(self):
		return self._ApplyTypes_(*(4057, 2, (8, 0), (), "MFilePlantBlock", None))
	def _get_MFileSimulinkModel(self):
		return self._ApplyTypes_(*(4059, 2, (8, 0), (), "MFileSimulinkModel", None))
	def _get_MatlabProgramPathName(self):
		return self._ApplyTypes_(*(4053, 2, (8, 0), (), "MatlabProgramPathName", None))
	def _get_OutputFileName(self):
		return self._ApplyTypes_(*(4051, 2, (8, 0), (), "OutputFileName", None))
	def _get_PlantFileName(self):
		return self._ApplyTypes_(*(4002, 2, (8, 0), (), "PlantFileName", None))
	def _get_SamplingPeriod(self):
		return self._ApplyTypes_(*(4003, 2, (5, 0), (), "SamplingPeriod", None))
	def _get_SimulinkModelPathName(self):
		return self._ApplyTypes_(*(4055, 2, (8, 0), (), "SimulinkModelPathName", None))
	def _get_UseFollowingInterfaceTimeOfMaster(self):
		return self._ApplyTypes_(*(4061, 2, (11, 0), (), "UseFollowingInterfaceTimeOfMaster", None))
	def _get_UseIdenticalSolutionofRDHost(self):
		return self._ApplyTypes_(*(4056, 2, (11, 0), (), "UseIdenticalSolutionofRDHost", None))
	def _get_WaitingTime(self):
		return self._ApplyTypes_(*(4050, 2, (5, 0), (), "WaitingTime", None))

	def _set_HostProgram(self, value):
		if "HostProgram" in self.__dict__: self.__dict__["HostProgram"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_InterfaceVersion(self, value):
		if "InterfaceVersion" in self.__dict__: self.__dict__["InterfaceVersion"] = value; return
		self._oleobj_.Invoke(*((4000, LCID, 4, 0) + (value,) + ()))
	def _set_MFilePlantBlock(self, value):
		if "MFilePlantBlock" in self.__dict__: self.__dict__["MFilePlantBlock"] = value; return
		self._oleobj_.Invoke(*((4057, LCID, 4, 0) + (value,) + ()))
	def _set_MFileSimulinkModel(self, value):
		if "MFileSimulinkModel" in self.__dict__: self.__dict__["MFileSimulinkModel"] = value; return
		self._oleobj_.Invoke(*((4059, LCID, 4, 0) + (value,) + ()))
	def _set_MatlabProgramPathName(self, value):
		if "MatlabProgramPathName" in self.__dict__: self.__dict__["MatlabProgramPathName"] = value; return
		self._oleobj_.Invoke(*((4053, LCID, 4, 0) + (value,) + ()))
	def _set_OutputFileName(self, value):
		if "OutputFileName" in self.__dict__: self.__dict__["OutputFileName"] = value; return
		self._oleobj_.Invoke(*((4051, LCID, 4, 0) + (value,) + ()))
	def _set_SamplingPeriod(self, value):
		if "SamplingPeriod" in self.__dict__: self.__dict__["SamplingPeriod"] = value; return
		self._oleobj_.Invoke(*((4003, LCID, 4, 0) + (value,) + ()))
	def _set_SimulinkModelPathName(self, value):
		if "SimulinkModelPathName" in self.__dict__: self.__dict__["SimulinkModelPathName"] = value; return
		self._oleobj_.Invoke(*((4055, LCID, 4, 0) + (value,) + ()))
	def _set_UseFollowingInterfaceTimeOfMaster(self, value):
		if "UseFollowingInterfaceTimeOfMaster" in self.__dict__: self.__dict__["UseFollowingInterfaceTimeOfMaster"] = value; return
		self._oleobj_.Invoke(*((4061, LCID, 4, 0) + (value,) + ()))
	def _set_UseIdenticalSolutionofRDHost(self, value):
		if "UseIdenticalSolutionofRDHost" in self.__dict__: self.__dict__["UseIdenticalSolutionofRDHost"] = value; return
		self._oleobj_.Invoke(*((4056, LCID, 4, 0) + (value,) + ()))
	def _set_WaitingTime(self, value):
		if "WaitingTime" in self.__dict__: self.__dict__["WaitingTime"] = value; return
		self._oleobj_.Invoke(*((4050, LCID, 4, 0) + (value,) + ()))

	HostProgram = property(_get_HostProgram, _set_HostProgram)
	'''
	Host Program

	:type: recurdyn.Control.ControlCoSimHostProgram
	'''
	InterfaceVersion = property(_get_InterfaceVersion, _set_InterfaceVersion)
	'''
	Interface Version

	:type: recurdyn.Control.ControlCoSimInterfaceVersion
	'''
	MFilePlantBlock = property(_get_MFilePlantBlock, _set_MFilePlantBlock)
	'''
	M-File to Create Plant Block

	:type: str
	'''
	MFileSimulinkModel = property(_get_MFileSimulinkModel, _set_MFileSimulinkModel)
	'''
	M-File to Run Simulink Model

	:type: str
	'''
	MatlabProgramPathName = property(_get_MatlabProgramPathName, _set_MatlabProgramPathName)
	'''
	Matlab Program Path and Name

	:type: str
	'''
	OutputFileName = property(_get_OutputFileName, _set_OutputFileName)
	'''
	Output File Name

	:type: str
	'''
	PlantFileName = property(_get_PlantFileName, None)
	'''
	Plant File Name

	:type: str
	'''
	SamplingPeriod = property(_get_SamplingPeriod, _set_SamplingPeriod)
	'''
	Sampling Period

	:type: float
	'''
	SimulinkModelPathName = property(_get_SimulinkModelPathName, _set_SimulinkModelPathName)
	'''
	Simulink Model Path and Name

	:type: str
	'''
	UseFollowingInterfaceTimeOfMaster = property(_get_UseFollowingInterfaceTimeOfMaster, _set_UseFollowingInterfaceTimeOfMaster)
	'''
	Use Following the Interface Time of Master (Host)

	:type: bool
	'''
	UseIdenticalSolutionofRDHost = property(_get_UseIdenticalSolutionofRDHost, _set_UseIdenticalSolutionofRDHost)
	'''
	Use Identical Solution of RDHost

	:type: bool
	'''
	WaitingTime = property(_get_WaitingTime, _set_WaitingTime)
	'''
	Waiting Time

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_HostProgram": _set_HostProgram,
		"_set_InterfaceVersion": _set_InterfaceVersion,
		"_set_MFilePlantBlock": _set_MFilePlantBlock,
		"_set_MFileSimulinkModel": _set_MFileSimulinkModel,
		"_set_MatlabProgramPathName": _set_MatlabProgramPathName,
		"_set_OutputFileName": _set_OutputFileName,
		"_set_SamplingPeriod": _set_SamplingPeriod,
		"_set_SimulinkModelPathName": _set_SimulinkModelPathName,
		"_set_UseFollowingInterfaceTimeOfMaster": _set_UseFollowingInterfaceTimeOfMaster,
		"_set_UseIdenticalSolutionofRDHost": _set_UseIdenticalSolutionofRDHost,
		"_set_WaitingTime": _set_WaitingTime,
	}
	_prop_map_get_ = {
		"HostProgram": (4001, 2, (3, 0), (), "HostProgram", '{55D18C89-86D8-4FEC-8DED-5089814F6AC9}'),
		"InterfaceVersion": (4000, 2, (3, 0), (), "InterfaceVersion", '{F8C9332E-B812-479B-9E28-C61411BDC309}'),
		"MFilePlantBlock": (4057, 2, (8, 0), (), "MFilePlantBlock", None),
		"MFileSimulinkModel": (4059, 2, (8, 0), (), "MFileSimulinkModel", None),
		"MatlabProgramPathName": (4053, 2, (8, 0), (), "MatlabProgramPathName", None),
		"OutputFileName": (4051, 2, (8, 0), (), "OutputFileName", None),
		"PlantFileName": (4002, 2, (8, 0), (), "PlantFileName", None),
		"SamplingPeriod": (4003, 2, (5, 0), (), "SamplingPeriod", None),
		"SimulinkModelPathName": (4055, 2, (8, 0), (), "SimulinkModelPathName", None),
		"UseFollowingInterfaceTimeOfMaster": (4061, 2, (11, 0), (), "UseFollowingInterfaceTimeOfMaster", None),
		"UseIdenticalSolutionofRDHost": (4056, 2, (11, 0), (), "UseIdenticalSolutionofRDHost", None),
		"WaitingTime": (4050, 2, (5, 0), (), "WaitingTime", None),
	}
	_prop_map_put_ = {
		"HostProgram": ((4001, LCID, 4, 0),()),
		"InterfaceVersion": ((4000, LCID, 4, 0),()),
		"MFilePlantBlock": ((4057, LCID, 4, 0),()),
		"MFileSimulinkModel": ((4059, LCID, 4, 0),()),
		"MatlabProgramPathName": ((4053, LCID, 4, 0),()),
		"OutputFileName": ((4051, LCID, 4, 0),()),
		"SamplingPeriod": ((4003, LCID, 4, 0),()),
		"SimulinkModelPathName": ((4055, LCID, 4, 0),()),
		"UseFollowingInterfaceTimeOfMaster": ((4061, LCID, 4, 0),()),
		"UseIdenticalSolutionofRDHost": ((4056, LCID, 4, 0),()),
		"WaitingTime": ((4050, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlGeneralCoSim(DispatchBaseClass):
	'''General CoSim'''
	CLSID = IID('{8B72016D-C4F4-4BCA-958E-3149CD4CE891}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddGeneralPlantInput(self, pVal):
		'''
		Add a General Plant Input
		
		:param pVal: IControlGeneralPlantInput
		'''
		return self._oleobj_.InvokeTypes(4003, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def AddGeneralPlantOutput(self, pVal):
		'''
		Add a General Plant Output
		
		:param pVal: IControlGeneralPlantOutput
		'''
		return self._oleobj_.InvokeTypes(4005, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeleteGeneralPlantInput(self, pVal):
		'''
		Delete a General Plant Input
		
		:param pVal: IControlGeneralPlantInput
		'''
		return self._oleobj_.InvokeTypes(4004, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeleteGeneralPlantOutput(self, pVal):
		'''
		Delete a General Plant Output
		
		:param pVal: IControlGeneralPlantOutput
		'''
		return self._oleobj_.InvokeTypes(4006, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(4001, 2, (11, 0), (), "Active", None))
	def _get_CoSimGeneralPlantInputCollection(self):
		return self._ApplyTypes_(*(4007, 2, (9, 0), (), "CoSimGeneralPlantInputCollection", '{1107C23B-D16E-4022-9D04-9C192701C03C}'))
	def _get_CoSimGeneralPlantOutputCollection(self):
		return self._ApplyTypes_(*(4008, 2, (9, 0), (), "CoSimGeneralPlantOutputCollection", '{8459A996-A7C2-4FD9-9B6E-0830F516F471}'))
	def _get_CoSimType(self):
		return self._ApplyTypes_(*(4002, 2, (3, 0), (), "CoSimType", '{CF31CB11-0C4E-4BFE-8C10-1729EB0FB94C}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FMI(self):
		return self._ApplyTypes_(*(4009, 2, (9, 0), (), "FMI", '{D647397B-70C5-4703-8EB6-6723E1689F17}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Simulink(self):
		return self._ApplyTypes_(*(4010, 2, (9, 0), (), "Simulink", '{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_CoSimType(self, value):
		if "CoSimType" in self.__dict__: self.__dict__["CoSimType"] = value; return
		self._oleobj_.Invoke(*((4002, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Use Flag

	:type: bool
	'''
	CoSimGeneralPlantInputCollection = property(_get_CoSimGeneralPlantInputCollection, None)
	CoSimGeneralPlantOutputCollection = property(_get_CoSimGeneralPlantOutputCollection, None)
	CoSimType = property(_get_CoSimType, _set_CoSimType)
	'''
	Data Type

	:type: recurdyn.Control.ControlCoSimType
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	FMI = property(_get_FMI, None)
	'''
	FMI

	:type: recurdyn.Control.IControlCoSimFMI
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	Owner = property(_get_Owner, None)
	'''
	Owner returns owning IGeneric interface, use Owner for IRFlexBody, IFFlexBody

	:type: recurdyn.ProcessNet.IGeneric
	'''
	OwnerBody = property(_get_OwnerBody, None)
	'''
	OwnerBody returns owning IBody interface

	:type: recurdyn.ProcessNet.IBody
	'''
	OwnerSubSystem = property(_get_OwnerSubSystem, None)
	'''
	OwnerSubSystem returns owning ISubSubSystem interface

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	Simulink = property(_get_Simulink, None)
	'''
	Simulink

	:type: recurdyn.Control.IControlCoSimSimulink
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_CoSimType": _set_CoSimType,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (4001, 2, (11, 0), (), "Active", None),
		"CoSimGeneralPlantInputCollection": (4007, 2, (9, 0), (), "CoSimGeneralPlantInputCollection", '{1107C23B-D16E-4022-9D04-9C192701C03C}'),
		"CoSimGeneralPlantOutputCollection": (4008, 2, (9, 0), (), "CoSimGeneralPlantOutputCollection", '{8459A996-A7C2-4FD9-9B6E-0830F516F471}'),
		"CoSimType": (4002, 2, (3, 0), (), "CoSimType", '{CF31CB11-0C4E-4BFE-8C10-1729EB0FB94C}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FMI": (4009, 2, (9, 0), (), "FMI", '{D647397B-70C5-4703-8EB6-6723E1689F17}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Simulink": (4010, 2, (9, 0), (), "Simulink", '{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((4001, LCID, 4, 0),()),
		"CoSimType": ((4002, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlGeneralCoSimCollection(DispatchBaseClass):
	'''Control General CoSim Collection'''
	CLSID = IID('{09115E35-81E3-463E-8E2E-188FFF462A06}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Item(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlGeneralCoSim
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8B72016D-C4F4-4BCA-958E-3149CD4CE891}')
		return ret

	def _get_Count(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))

	Count = property(_get_Count, None)
	'''
	Returns the number of items in the collection.

	:type: int
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"_NewEnum": (-4, 2, (13, 0), (), "_NewEnum", None),
	}
	_prop_map_put_ = {
	}
	def __call__(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlGeneralCoSim
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8B72016D-C4F4-4BCA-958E-3149CD4CE891}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{8B72016D-C4F4-4BCA-958E-3149CD4CE891}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{8B72016D-C4F4-4BCA-958E-3149CD4CE891}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IControlGeneralPlantInput(DispatchBaseClass):
	'''Plant Input'''
	CLSID = IID('{E11A152B-12FC-400C-920C-E84E1B62E375}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(4001, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DataType(self):
		return self._ApplyTypes_(*(4002, 2, (3, 0), (), "DataType", '{0816E1EE-6F14-4537-8A00-C806B4C36C9B}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InitialValue(self):
		return self._ApplyTypes_(*(4003, 2, (8, 0), (), "InitialValue", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DataType(self, value):
		if "DataType" in self.__dict__: self.__dict__["DataType"] = value; return
		self._oleobj_.Invoke(*((4002, LCID, 4, 0) + (value,) + ()))
	def _set_InitialValue(self, value):
		if "InitialValue" in self.__dict__: self.__dict__["InitialValue"] = value; return
		self._oleobj_.Invoke(*((4003, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Use Flag

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DataType = property(_get_DataType, _set_DataType)
	'''
	Data Type

	:type: recurdyn.Control.ControlCoSimDataType
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	InitialValue = property(_get_InitialValue, _set_InitialValue)
	'''
	Initial Value

	:type: str
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	Owner = property(_get_Owner, None)
	'''
	Owner returns owning IGeneric interface, use Owner for IRFlexBody, IFFlexBody

	:type: recurdyn.ProcessNet.IGeneric
	'''
	OwnerBody = property(_get_OwnerBody, None)
	'''
	OwnerBody returns owning IBody interface

	:type: recurdyn.ProcessNet.IBody
	'''
	OwnerSubSystem = property(_get_OwnerSubSystem, None)
	'''
	OwnerSubSystem returns owning ISubSubSystem interface

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_DataType": _set_DataType,
		"_set_InitialValue": _set_InitialValue,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (4001, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DataType": (4002, 2, (3, 0), (), "DataType", '{0816E1EE-6F14-4537-8A00-C806B4C36C9B}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InitialValue": (4003, 2, (8, 0), (), "InitialValue", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((4001, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DataType": ((4002, LCID, 4, 0),()),
		"InitialValue": ((4003, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlGeneralPlantInputCollection(DispatchBaseClass):
	'''Control General PlantInput Collection'''
	CLSID = IID('{1107C23B-D16E-4022-9D04-9C192701C03C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Item(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlGeneralPlantInput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E11A152B-12FC-400C-920C-E84E1B62E375}')
		return ret

	def _get_Count(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))

	Count = property(_get_Count, None)
	'''
	Returns the number of items in the collection.

	:type: int
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"_NewEnum": (-4, 2, (13, 0), (), "_NewEnum", None),
	}
	_prop_map_put_ = {
	}
	def __call__(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlGeneralPlantInput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E11A152B-12FC-400C-920C-E84E1B62E375}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{E11A152B-12FC-400C-920C-E84E1B62E375}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{E11A152B-12FC-400C-920C-E84E1B62E375}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IControlGeneralPlantOutput(DispatchBaseClass):
	'''Plant Output'''
	CLSID = IID('{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(4001, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DataType(self):
		return self._ApplyTypes_(*(4002, 2, (3, 0), (), "DataType", '{0816E1EE-6F14-4537-8A00-C806B4C36C9B}'))
	def _get_Expression(self):
		return self._ApplyTypes_(*(4003, 2, (9, 0), (), "Expression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DataType(self, value):
		if "DataType" in self.__dict__: self.__dict__["DataType"] = value; return
		self._oleobj_.Invoke(*((4002, LCID, 4, 0) + (value,) + ()))
	def _set_Expression(self, value):
		if "Expression" in self.__dict__: self.__dict__["Expression"] = value; return
		self._oleobj_.Invoke(*((4003, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Use Flag

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DataType = property(_get_DataType, _set_DataType)
	'''
	Data Type

	:type: recurdyn.Control.ControlCoSimDataType
	'''
	Expression = property(_get_Expression, _set_Expression)
	'''
	Expression

	:type: recurdyn.ProcessNet.IExpression
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	Owner = property(_get_Owner, None)
	'''
	Owner returns owning IGeneric interface, use Owner for IRFlexBody, IFFlexBody

	:type: recurdyn.ProcessNet.IGeneric
	'''
	OwnerBody = property(_get_OwnerBody, None)
	'''
	OwnerBody returns owning IBody interface

	:type: recurdyn.ProcessNet.IBody
	'''
	OwnerSubSystem = property(_get_OwnerSubSystem, None)
	'''
	OwnerSubSystem returns owning ISubSubSystem interface

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_DataType": _set_DataType,
		"_set_Expression": _set_Expression,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (4001, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DataType": (4002, 2, (3, 0), (), "DataType", '{0816E1EE-6F14-4537-8A00-C806B4C36C9B}'),
		"Expression": (4003, 2, (9, 0), (), "Expression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((4001, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DataType": ((4002, LCID, 4, 0),()),
		"Expression": ((4003, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlGeneralPlantOutputCollection(DispatchBaseClass):
	'''Control General PlantOutput Collection'''
	CLSID = IID('{8459A996-A7C2-4FD9-9B6E-0830F516F471}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Item(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlGeneralPlantOutput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')
		return ret

	def _get_Count(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))

	Count = property(_get_Count, None)
	'''
	Returns the number of items in the collection.

	:type: int
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"_NewEnum": (-4, 2, (13, 0), (), "_NewEnum", None),
	}
	_prop_map_put_ = {
	}
	def __call__(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlGeneralPlantOutput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IControlGeneralToolkit(DispatchBaseClass):
	'''Control Gerneral Toolkit'''
	CLSID = IID('{76073096-D8D8-49AF-8FE1-14A645234D0B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateGeneralCoSim(self, strName):
		'''
		Create a General CoSim
		
		:param strName: str
		:rtype: recurdyn.Control.IControlGeneralCoSim
		'''
		ret = self._oleobj_.InvokeTypes(4056, LCID, 1, (9, 0), ((8, 1),),strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGeneralCoSim', '{8B72016D-C4F4-4BCA-958E-3149CD4CE891}')
		return ret

	def CreateGeneralPlantInput(self, strName):
		'''
		Create a General Plant Input
		
		:param strName: str
		:rtype: recurdyn.Control.IControlGeneralPlantInput
		'''
		ret = self._oleobj_.InvokeTypes(4050, LCID, 1, (9, 0), ((8, 1),),strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGeneralPlantInput', '{E11A152B-12FC-400C-920C-E84E1B62E375}')
		return ret

	def CreateGeneralPlantOutput(self, strName, pExpression):
		'''
		Create a General Plant Output
		
		:param strName: str
		:param pExpression: IExpression
		:rtype: recurdyn.Control.IControlGeneralPlantOutput
		'''
		ret = self._oleobj_.InvokeTypes(4051, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pExpression)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGeneralPlantOutput', '{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')
		return ret

	def DeleteGeneralPlantInput(self, pVal):
		'''
		Delete a General Plant Input
		
		:param pVal: IControlGeneralPlantInput
		'''
		return self._oleobj_.InvokeTypes(4052, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeleteGeneralPlantOutput(self, pVal):
		'''
		Delete a General Plant Output
		
		:param pVal: IControlGeneralPlantOutput
		'''
		return self._oleobj_.InvokeTypes(4053, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ControlGeneralCoSimCollection(self):
		return self._ApplyTypes_(*(4057, 2, (9, 0), (), "ControlGeneralCoSimCollection", '{09115E35-81E3-463E-8E2E-188FFF462A06}'))
	def _get_ControlGeneralPlantInputCollection(self):
		return self._ApplyTypes_(*(4054, 2, (9, 0), (), "ControlGeneralPlantInputCollection", '{1107C23B-D16E-4022-9D04-9C192701C03C}'))
	def _get_ControlGeneralPlantOutputCollection(self):
		return self._ApplyTypes_(*(4055, 2, (9, 0), (), "ControlGeneralPlantOutputCollection", '{8459A996-A7C2-4FD9-9B6E-0830F516F471}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseCoSimInfo(self):
		return self._ApplyTypes_(*(4058, 2, (11, 0), (), "UseCoSimInfo", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ControlGeneralCoSimCollection = property(_get_ControlGeneralCoSimCollection, None)
	ControlGeneralPlantInputCollection = property(_get_ControlGeneralPlantInputCollection, None)
	ControlGeneralPlantOutputCollection = property(_get_ControlGeneralPlantOutputCollection, None)
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	Owner = property(_get_Owner, None)
	'''
	Owner returns owning IGeneric interface, use Owner for IRFlexBody, IFFlexBody

	:type: recurdyn.ProcessNet.IGeneric
	'''
	OwnerBody = property(_get_OwnerBody, None)
	'''
	OwnerBody returns owning IBody interface

	:type: recurdyn.ProcessNet.IBody
	'''
	OwnerSubSystem = property(_get_OwnerSubSystem, None)
	'''
	OwnerSubSystem returns owning ISubSubSystem interface

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	UseCoSimInfo = property(_get_UseCoSimInfo, None)
	'''
	Check whether the GCoSim information exists or not.

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ControlGeneralCoSimCollection": (4057, 2, (9, 0), (), "ControlGeneralCoSimCollection", '{09115E35-81E3-463E-8E2E-188FFF462A06}'),
		"ControlGeneralPlantInputCollection": (4054, 2, (9, 0), (), "ControlGeneralPlantInputCollection", '{1107C23B-D16E-4022-9D04-9C192701C03C}'),
		"ControlGeneralPlantOutputCollection": (4055, 2, (9, 0), (), "ControlGeneralPlantOutputCollection", '{8459A996-A7C2-4FD9-9B6E-0830F516F471}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseCoSimInfo": (4058, 2, (11, 0), (), "UseCoSimInfo", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlPlantInput(DispatchBaseClass):
	'''Plant Input'''
	CLSID = IID('{CDD83BF7-B2D9-4539-B292-200CE2259917}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(4001, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Use Flag

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	Owner = property(_get_Owner, None)
	'''
	Owner returns owning IGeneric interface, use Owner for IRFlexBody, IFFlexBody

	:type: recurdyn.ProcessNet.IGeneric
	'''
	OwnerBody = property(_get_OwnerBody, None)
	'''
	OwnerBody returns owning IBody interface

	:type: recurdyn.ProcessNet.IBody
	'''
	OwnerSubSystem = property(_get_OwnerSubSystem, None)
	'''
	OwnerSubSystem returns owning ISubSubSystem interface

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (4001, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((4001, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlPlantInputCollection(DispatchBaseClass):
	'''ControlPlantInputCollection'''
	CLSID = IID('{211EEA3E-CA4D-4C8E-B7AB-06240B3D2DF6}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Item(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlPlantInput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CDD83BF7-B2D9-4539-B292-200CE2259917}')
		return ret

	def _get_Count(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))

	Count = property(_get_Count, None)
	'''
	Returns the number of items in the collection.

	:type: int
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"_NewEnum": (-4, 2, (13, 0), (), "_NewEnum", None),
	}
	_prop_map_put_ = {
	}
	def __call__(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlPlantInput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CDD83BF7-B2D9-4539-B292-200CE2259917}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{CDD83BF7-B2D9-4539-B292-200CE2259917}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{CDD83BF7-B2D9-4539-B292-200CE2259917}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IControlPlantOutput(DispatchBaseClass):
	'''Plant Output'''
	CLSID = IID('{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(4001, 2, (11, 0), (), "Active", None))
	def _get_Arguments(self):
		return self._ApplyTypes_(*(4004, 2, (8200, 0), (), "Arguments", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InitialValue(self):
		return self._ApplyTypes_(*(4003, 2, (5, 0), (), "InitialValue", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Text(self):
		return self._ApplyTypes_(*(4002, 2, (8, 0), (), "Text", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((4001, LCID, 4, 0) + (value,) + ()))
	def _set_Arguments(self, value):
		if "Arguments" in self.__dict__: self.__dict__["Arguments"] = value; return
		variantValue = win32com.client.VARIANT(8200, value)
		self._oleobj_.Invoke(*((4004, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Text(self, value):
		if "Text" in self.__dict__: self.__dict__["Text"] = value; return
		self._oleobj_.Invoke(*((4002, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Use Flag

	:type: bool
	'''
	Arguments = property(_get_Arguments, _set_Arguments)
	'''
	Arguments list

	:type: list[str]
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	InitialValue = property(_get_InitialValue, None)
	'''
	Initial Value

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	Owner = property(_get_Owner, None)
	'''
	Owner returns owning IGeneric interface, use Owner for IRFlexBody, IFFlexBody

	:type: recurdyn.ProcessNet.IGeneric
	'''
	OwnerBody = property(_get_OwnerBody, None)
	'''
	OwnerBody returns owning IBody interface

	:type: recurdyn.ProcessNet.IBody
	'''
	OwnerSubSystem = property(_get_OwnerSubSystem, None)
	'''
	OwnerSubSystem returns owning ISubSubSystem interface

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	Text = property(_get_Text, _set_Text)
	'''
	Text

	:type: str
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Arguments": _set_Arguments,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_Text": _set_Text,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (4001, 2, (11, 0), (), "Active", None),
		"Arguments": (4004, 2, (8200, 0), (), "Arguments", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InitialValue": (4003, 2, (5, 0), (), "InitialValue", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Text": (4002, 2, (8, 0), (), "Text", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((4001, LCID, 4, 0),()),
		"Arguments": ((4004, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Text": ((4002, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IControlPlantOutputCollection(DispatchBaseClass):
	'''ControlPlantOutputCollection'''
	CLSID = IID('{0C380EF2-6F62-4DAF-9F8D-7DD372D41B46}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Item(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlPlantOutput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')
		return ret

	def _get_Count(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))

	Count = property(_get_Count, None)
	'''
	Returns the number of items in the collection.

	:type: int
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Count": (1, 2, (3, 0), (), "Count", None),
		"_NewEnum": (-4, 2, (13, 0), (), "_NewEnum", None),
	}
	_prop_map_put_ = {
	}
	def __call__(self, var):
		'''
		Returns a specific item.
		
		:param var: object
		:rtype: recurdyn.Control.IControlPlantOutput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')
		return ret

	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,2,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, '{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IControlToolkit(DispatchBaseClass):
	'''Control Toolkit'''
	CLSID = IID('{8B542970-81BF-49D6-B92A-60F4E17B88AE}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreatePlantInput(self, strName):
		'''
		Create a Plant Input
		
		:param strName: str
		:rtype: recurdyn.Control.IControlPlantInput
		'''
		ret = self._oleobj_.InvokeTypes(4050, LCID, 1, (9, 0), ((8, 1),),strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePlantInput', '{CDD83BF7-B2D9-4539-B292-200CE2259917}')
		return ret

	def CreatePlantOutput(self, strName, strExpression):
		'''
		Create a Plant Output
		
		:param strName: str
		:param strExpression: str
		:rtype: recurdyn.Control.IControlPlantOutput
		'''
		ret = self._oleobj_.InvokeTypes(4051, LCID, 1, (9, 0), ((8, 1), (8, 1)),strName
			, strExpression)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePlantOutput', '{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')
		return ret

	def CreatePlantOutputWithArguments(self, strName, strExpression, strArgument):
		'''
		Create a Plant Output with Arguments
		
		:param strName: str
		:param strExpression: str
		:param strArgument: list[str]
		:rtype: recurdyn.Control.IControlPlantOutput
		'''
		ret = self._oleobj_.InvokeTypes(4063, LCID, 1, (9, 0), ((8, 1), (8, 1), (8200, 1)),strName
			, strExpression, strArgument)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePlantOutputWithArguments', '{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')
		return ret

	def DeleteCoSimInfo(self):
		'''
		Delete CoSim Information
		'''
		return self._oleobj_.InvokeTypes(4058, LCID, 1, (24, 0), (),)


	def DeletePlantInput(self, pVal):
		'''
		Delete a Plant Input
		
		:param pVal: IControlPlantInput
		'''
		return self._oleobj_.InvokeTypes(4061, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePlantOutput(self, pVal):
		'''
		Delete a Plant Output
		
		:param pVal: IControlPlantOutput
		'''
		return self._oleobj_.InvokeTypes(4062, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_AMESim(self):
		return self._ApplyTypes_(*(4059, 2, (9, 0), (), "AMESim", '{1BC86F13-0032-45C7-9A70-288D4BAE8AA5}'))
	def _get_CoSimType(self):
		return self._ApplyTypes_(*(4054, 2, (3, 0), (), "CoSimType", '{CF31CB11-0C4E-4BFE-8C10-1729EB0FB94C}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ControlPlantInputCollection(self):
		return self._ApplyTypes_(*(4052, 2, (9, 0), (), "ControlPlantInputCollection", '{211EEA3E-CA4D-4C8E-B7AB-06240B3D2DF6}'))
	def _get_ControlPlantOutputCollection(self):
		return self._ApplyTypes_(*(4053, 2, (9, 0), (), "ControlPlantOutputCollection", '{0C380EF2-6F62-4DAF-9F8D-7DD372D41B46}'))
	def _get_FMI(self):
		return self._ApplyTypes_(*(4060, 2, (9, 0), (), "FMI", '{D647397B-70C5-4703-8EB6-6723E1689F17}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_General(self):
		return self._ApplyTypes_(*(4056, 2, (9, 0), (), "General", '{A596000B-668A-4A1B-84C8-9A1F1249D1F5}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Simplorer(self):
		return self._ApplyTypes_(*(4057, 2, (9, 0), (), "Simplorer", '{7128F4FF-E1F1-4171-86B2-4AC5D5B12754}'))
	def _get_Simulink(self):
		return self._ApplyTypes_(*(4055, 2, (9, 0), (), "Simulink", '{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}'))
	def _get_UseCoSimInfo(self):
		return self._ApplyTypes_(*(4064, 2, (11, 0), (), "UseCoSimInfo", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_CoSimType(self, value):
		if "CoSimType" in self.__dict__: self.__dict__["CoSimType"] = value; return
		self._oleobj_.Invoke(*((4054, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	AMESim = property(_get_AMESim, None)
	'''
	AMESim

	:type: recurdyn.Control.IControlCoSimAMESim
	'''
	CoSimType = property(_get_CoSimType, _set_CoSimType)
	'''
	CoSim Type

	:type: recurdyn.Control.ControlCoSimType
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ControlPlantInputCollection = property(_get_ControlPlantInputCollection, None)
	ControlPlantOutputCollection = property(_get_ControlPlantOutputCollection, None)
	FMI = property(_get_FMI, None)
	'''
	FMI

	:type: recurdyn.Control.IControlCoSimFMI
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	General = property(_get_General, None)
	'''
	General

	:type: recurdyn.Control.IControlCoSimGeneral
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	Owner = property(_get_Owner, None)
	'''
	Owner returns owning IGeneric interface, use Owner for IRFlexBody, IFFlexBody

	:type: recurdyn.ProcessNet.IGeneric
	'''
	OwnerBody = property(_get_OwnerBody, None)
	'''
	OwnerBody returns owning IBody interface

	:type: recurdyn.ProcessNet.IBody
	'''
	OwnerSubSystem = property(_get_OwnerSubSystem, None)
	'''
	OwnerSubSystem returns owning ISubSubSystem interface

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	Simplorer = property(_get_Simplorer, None)
	'''
	Simplorer

	:type: recurdyn.Control.IControlCoSimSimplorer
	'''
	Simulink = property(_get_Simulink, None)
	'''
	Simulink

	:type: recurdyn.Control.IControlCoSimSimulink
	'''
	UseCoSimInfo = property(_get_UseCoSimInfo, None)
	'''
	Check whether the cosim information exists or not.

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_CoSimType": _set_CoSimType,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"AMESim": (4059, 2, (9, 0), (), "AMESim", '{1BC86F13-0032-45C7-9A70-288D4BAE8AA5}'),
		"CoSimType": (4054, 2, (3, 0), (), "CoSimType", '{CF31CB11-0C4E-4BFE-8C10-1729EB0FB94C}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ControlPlantInputCollection": (4052, 2, (9, 0), (), "ControlPlantInputCollection", '{211EEA3E-CA4D-4C8E-B7AB-06240B3D2DF6}'),
		"ControlPlantOutputCollection": (4053, 2, (9, 0), (), "ControlPlantOutputCollection", '{0C380EF2-6F62-4DAF-9F8D-7DD372D41B46}'),
		"FMI": (4060, 2, (9, 0), (), "FMI", '{D647397B-70C5-4703-8EB6-6723E1689F17}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"General": (4056, 2, (9, 0), (), "General", '{A596000B-668A-4A1B-84C8-9A1F1249D1F5}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Simplorer": (4057, 2, (9, 0), (), "Simplorer", '{7128F4FF-E1F1-4171-86B2-4AC5D5B12754}'),
		"Simulink": (4055, 2, (9, 0), (), "Simulink", '{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}'),
		"UseCoSimInfo": (4064, 2, (11, 0), (), "UseCoSimInfo", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"CoSimType": ((4054, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

IControlCoSim_vtables_dispatch_ = 1
IControlCoSim_vtables_ = [
	(( 'InterfaceVersion' , 'pVal' , ), 4000, (4000, (), [ (3, 1, None, "IID('{F8C9332E-B812-479B-9E28-C61411BDC309}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceVersion' , 'pVal' , ), 4000, (4000, (), [ (16387, 10, None, "IID('{F8C9332E-B812-479B-9E28-C61411BDC309}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'HostProgram' , 'pVal' , ), 4001, (4001, (), [ (3, 1, None, "IID('{55D18C89-86D8-4FEC-8DED-5089814F6AC9}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'HostProgram' , 'pVal' , ), 4001, (4001, (), [ (16387, 10, None, "IID('{55D18C89-86D8-4FEC-8DED-5089814F6AC9}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PlantFileName' , 'strName' , ), 4002, (4002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SamplingPeriod' , 'pVal' , ), 4003, (4003, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SamplingPeriod' , 'pVal' , ), 4003, (4003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IControlCoSimAMESim_vtables_dispatch_ = 1
IControlCoSimAMESim_vtables_ = [
	(( 'ModelFileName' , 'strName' , ), 4001, (4001, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ModelFileName' , 'strName' , ), 4001, (4001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceTimeStep' , 'pVal' , ), 4000, (4000, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceTimeStep' , 'pVal' , ), 4000, (4000, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IControlCoSimFMI_vtables_dispatch_ = 1
IControlCoSimFMI_vtables_ = [
	(( 'Type' , 'pVal' , ), 4001, (4001, (), [ (3, 1, None, "IID('{B73478A9-7C5B-42CC-BC3F-EA2FAC1D6B68}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 4001, (4001, (), [ (16387, 10, None, "IID('{B73478A9-7C5B-42CC-BC3F-EA2FAC1D6B68}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ModelFileName' , 'strName' , ), 4002, (4002, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ModelFileName' , 'strName' , ), 4002, (4002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PlantFileName' , 'strName' , ), 4003, (4003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceTimeStep' , 'pVal' , ), 4004, (4004, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceTimeStep' , 'pVal' , ), 4004, (4004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'WaitingTime' , 'pVal' , ), 4005, (4005, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'WaitingTime' , 'pVal' , ), 4005, (4005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'FMUFileName' , 'strName' , ), 4006, (4006, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FMUFileName' , 'strName' , ), 4006, (4006, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ExportFMUFile' , ), 4007, (4007, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceVersion' , 'pVal' , ), 4009, (4009, (), [ (3, 1, None, "IID('{EC8A3D9C-F40A-4EFC-9D2E-2514A1F87671}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceVersion' , 'pVal' , ), 4009, (4009, (), [ (16387, 10, None, "IID('{EC8A3D9C-F40A-4EFC-9D2E-2514A1F87671}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseFollowingInterfaceTimeOfMaster' , 'pVal' , ), 4010, (4010, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseFollowingInterfaceTimeOfMaster' , 'pVal' , ), 4010, (4010, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceTimeStepUnit' , 'pVal' , ), 4011, (4011, (), [ (3, 1, None, "IID('{C3AD468F-A8C5-4014-96D0-F9DC6DFDD28A}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceTimeStepUnit' , 'pVal' , ), 4011, (4011, (), [ (16387, 10, None, "IID('{C3AD468F-A8C5-4014-96D0-F9DC6DFDD28A}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IControlCoSimGeneral_vtables_dispatch_ = 1
IControlCoSimGeneral_vtables_ = [
	(( 'WaitingTime' , 'pVal' , ), 4050, (4050, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'WaitingTime' , 'pVal' , ), 4050, (4050, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ClientProgramPathName' , 'strName' , ), 4051, (4051, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ClientProgramPathName' , 'strName' , ), 4051, (4051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IControlCoSimSimplorer_vtables_dispatch_ = 1
IControlCoSimSimplorer_vtables_ = [
]

IControlCoSimSimulink_vtables_dispatch_ = 1
IControlCoSimSimulink_vtables_ = [
	(( 'WaitingTime' , 'pVal' , ), 4050, (4050, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'WaitingTime' , 'pVal' , ), 4050, (4050, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'OutputFileName' , 'strName' , ), 4051, (4051, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'OutputFileName' , 'strName' , ), 4051, (4051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MatlabProgramPathName' , 'strName' , ), 4053, (4053, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'MatlabProgramPathName' , 'strName' , ), 4053, (4053, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SimulinkModelPathName' , 'strName' , ), 4055, (4055, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SimulinkModelPathName' , 'strName' , ), 4055, (4055, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseIdenticalSolutionofRDHost' , 'pVal' , ), 4056, (4056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseIdenticalSolutionofRDHost' , 'pVal' , ), 4056, (4056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'MFilePlantBlock' , 'strName' , ), 4057, (4057, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'MFilePlantBlock' , 'strName' , ), 4057, (4057, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ExportMFileToCreatePlantBlock2' , ), 4058, (4058, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'MFileSimulinkModel' , 'strName' , ), 4059, (4059, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'MFileSimulinkModel' , 'strName' , ), 4059, (4059, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ExportMFileToRunSimulinkModel2' , ), 4060, (4060, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseFollowingInterfaceTimeOfMaster' , 'pVal' , ), 4061, (4061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseFollowingInterfaceTimeOfMaster' , 'pVal' , ), 4061, (4061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ExportMFileToCreatePlantBlock' , 'strName' , ), 4052, (4052, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ExportMFileToRunSimulinkModel' , 'strName' , ), 4054, (4054, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IControlGeneralCoSim_vtables_dispatch_ = 1
IControlGeneralCoSim_vtables_ = [
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CoSimType' , 'pVal' , ), 4002, (4002, (), [ (3, 1, None, "IID('{CF31CB11-0C4E-4BFE-8C10-1729EB0FB94C}')") , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CoSimType' , 'pVal' , ), 4002, (4002, (), [ (16387, 10, None, "IID('{CF31CB11-0C4E-4BFE-8C10-1729EB0FB94C}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AddGeneralPlantInput' , 'pVal' , ), 4003, (4003, (), [ (9, 1, None, "IID('{E11A152B-12FC-400C-920C-E84E1B62E375}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DeleteGeneralPlantInput' , 'pVal' , ), 4004, (4004, (), [ (9, 1, None, "IID('{E11A152B-12FC-400C-920C-E84E1B62E375}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'AddGeneralPlantOutput' , 'pVal' , ), 4005, (4005, (), [ (9, 1, None, "IID('{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DeleteGeneralPlantOutput' , 'pVal' , ), 4006, (4006, (), [ (9, 1, None, "IID('{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CoSimGeneralPlantInputCollection' , 'ppVal' , ), 4007, (4007, (), [ (16393, 10, None, "IID('{1107C23B-D16E-4022-9D04-9C192701C03C}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CoSimGeneralPlantOutputCollection' , 'ppVal' , ), 4008, (4008, (), [ (16393, 10, None, "IID('{8459A996-A7C2-4FD9-9B6E-0830F516F471}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'FMI' , 'ppVal' , ), 4009, (4009, (), [ (16393, 10, None, "IID('{D647397B-70C5-4703-8EB6-6723E1689F17}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Simulink' , 'ppVal' , ), 4010, (4010, (), [ (16393, 10, None, "IID('{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
]

IControlGeneralCoSimCollection_vtables_dispatch_ = 1
IControlGeneralCoSimCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{8B72016D-C4F4-4BCA-958E-3149CD4CE891}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IControlGeneralPlantInput_vtables_dispatch_ = 1
IControlGeneralPlantInput_vtables_ = [
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DataType' , 'pVal' , ), 4002, (4002, (), [ (3, 1, None, "IID('{0816E1EE-6F14-4537-8A00-C806B4C36C9B}')") , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DataType' , 'pVal' , ), 4002, (4002, (), [ (16387, 10, None, "IID('{0816E1EE-6F14-4537-8A00-C806B4C36C9B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'InitialValue' , 'pVal' , ), 4003, (4003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'InitialValue' , 'pVal' , ), 4003, (4003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IControlGeneralPlantInputCollection_vtables_dispatch_ = 1
IControlGeneralPlantInputCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E11A152B-12FC-400C-920C-E84E1B62E375}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IControlGeneralPlantOutput_vtables_dispatch_ = 1
IControlGeneralPlantOutput_vtables_ = [
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DataType' , 'pVal' , ), 4002, (4002, (), [ (3, 1, None, "IID('{0816E1EE-6F14-4537-8A00-C806B4C36C9B}')") , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DataType' , 'pVal' , ), 4002, (4002, (), [ (16387, 10, None, "IID('{0816E1EE-6F14-4537-8A00-C806B4C36C9B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Expression' , 'ppVal' , ), 4003, (4003, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Expression' , 'ppVal' , ), 4003, (4003, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IControlGeneralPlantOutputCollection_vtables_dispatch_ = 1
IControlGeneralPlantOutputCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IControlGeneralToolkit_vtables_dispatch_ = 1
IControlGeneralToolkit_vtables_ = [
	(( 'CreateGeneralPlantInput' , 'strName' , 'ppVal' , ), 4050, (4050, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{E11A152B-12FC-400C-920C-E84E1B62E375}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreateGeneralPlantOutput' , 'strName' , 'pExpression' , 'ppVal' , ), 4051, (4051, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , (16393, 10, None, "IID('{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DeleteGeneralPlantInput' , 'pVal' , ), 4052, (4052, (), [ (9, 1, None, "IID('{E11A152B-12FC-400C-920C-E84E1B62E375}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DeleteGeneralPlantOutput' , 'pVal' , ), 4053, (4053, (), [ (9, 1, None, "IID('{48E89050-F3A8-4281-8CEA-F924B28CC4F3}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ControlGeneralPlantInputCollection' , 'ppVal' , ), 4054, (4054, (), [ (16393, 10, None, "IID('{1107C23B-D16E-4022-9D04-9C192701C03C}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ControlGeneralPlantOutputCollection' , 'ppVal' , ), 4055, (4055, (), [ (16393, 10, None, "IID('{8459A996-A7C2-4FD9-9B6E-0830F516F471}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateGeneralCoSim' , 'strName' , 'ppVal' , ), 4056, (4056, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{8B72016D-C4F4-4BCA-958E-3149CD4CE891}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ControlGeneralCoSimCollection' , 'colGCoSim' , ), 4057, (4057, (), [ (16393, 10, None, "IID('{09115E35-81E3-463E-8E2E-188FFF462A06}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseCoSimInfo' , 'bUse' , ), 4058, (4058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IControlPlantInput_vtables_dispatch_ = 1
IControlPlantInput_vtables_ = [
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IControlPlantInputCollection_vtables_dispatch_ = 1
IControlPlantInputCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{CDD83BF7-B2D9-4539-B292-200CE2259917}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IControlPlantOutput_vtables_dispatch_ = 1
IControlPlantOutput_vtables_ = [
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 4001, (4001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 4002, (4002, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'Text' , ), 4002, (4002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'InitialValue' , 'pVal' , ), 4003, (4003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Arguments' , 'ppSafeArray' , ), 4004, (4004, (), [ (8200, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Arguments' , 'ppSafeArray' , ), 4004, (4004, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IControlPlantOutputCollection_vtables_dispatch_ = 1
IControlPlantOutputCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IControlToolkit_vtables_dispatch_ = 1
IControlToolkit_vtables_ = [
	(( 'CreatePlantInput' , 'strName' , 'ppVal' , ), 4050, (4050, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{CDD83BF7-B2D9-4539-B292-200CE2259917}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreatePlantOutput' , 'strName' , 'strExpression' , 'ppVal' , ), 4051, (4051, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ControlPlantInputCollection' , 'ppVal' , ), 4052, (4052, (), [ (16393, 10, None, "IID('{211EEA3E-CA4D-4C8E-B7AB-06240B3D2DF6}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ControlPlantOutputCollection' , 'ppVal' , ), 4053, (4053, (), [ (16393, 10, None, "IID('{0C380EF2-6F62-4DAF-9F8D-7DD372D41B46}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CoSimType' , 'pVal' , ), 4054, (4054, (), [ (3, 1, None, "IID('{CF31CB11-0C4E-4BFE-8C10-1729EB0FB94C}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CoSimType' , 'pVal' , ), 4054, (4054, (), [ (16387, 10, None, "IID('{CF31CB11-0C4E-4BFE-8C10-1729EB0FB94C}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Simulink' , 'ppVal' , ), 4055, (4055, (), [ (16393, 10, None, "IID('{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'General' , 'ppVal' , ), 4056, (4056, (), [ (16393, 10, None, "IID('{A596000B-668A-4A1B-84C8-9A1F1249D1F5}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Simplorer' , 'ppVal' , ), 4057, (4057, (), [ (16393, 10, None, "IID('{7128F4FF-E1F1-4171-86B2-4AC5D5B12754}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DeleteCoSimInfo' , ), 4058, (4058, (), [ ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AMESim' , 'ppVal' , ), 4059, (4059, (), [ (16393, 10, None, "IID('{1BC86F13-0032-45C7-9A70-288D4BAE8AA5}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FMI' , 'ppVal' , ), 4060, (4060, (), [ (16393, 10, None, "IID('{D647397B-70C5-4703-8EB6-6723E1689F17}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DeletePlantInput' , 'pVal' , ), 4061, (4061, (), [ (9, 1, None, "IID('{CDD83BF7-B2D9-4539-B292-200CE2259917}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DeletePlantOutput' , 'pVal' , ), 4062, (4062, (), [ (9, 1, None, "IID('{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CreatePlantOutputWithArguments' , 'strName' , 'strExpression' , 'strArgument' , 'ppVal' , 
			 ), 4063, (4063, (), [ (8, 1, None, None) , (8, 1, None, None) , (8200, 1, None, None) , (16393, 10, None, "IID('{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseCoSimInfo' , 'pVal' , ), 4064, (4064, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{CDD83BF7-B2D9-4539-B292-200CE2259917}' : IControlPlantInput,
	'{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}' : IControlPlantOutput,
	'{211EEA3E-CA4D-4C8E-B7AB-06240B3D2DF6}' : IControlPlantInputCollection,
	'{0C380EF2-6F62-4DAF-9F8D-7DD372D41B46}' : IControlPlantOutputCollection,
	'{0C8DABD9-7480-48E0-A8BF-68076ACB5DD8}' : IControlCoSim,
	'{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}' : IControlCoSimSimulink,
	'{A596000B-668A-4A1B-84C8-9A1F1249D1F5}' : IControlCoSimGeneral,
	'{7128F4FF-E1F1-4171-86B2-4AC5D5B12754}' : IControlCoSimSimplorer,
	'{1BC86F13-0032-45C7-9A70-288D4BAE8AA5}' : IControlCoSimAMESim,
	'{D647397B-70C5-4703-8EB6-6723E1689F17}' : IControlCoSimFMI,
	'{8B542970-81BF-49D6-B92A-60F4E17B88AE}' : IControlToolkit,
	'{E11A152B-12FC-400C-920C-E84E1B62E375}' : IControlGeneralPlantInput,
	'{48E89050-F3A8-4281-8CEA-F924B28CC4F3}' : IControlGeneralPlantOutput,
	'{1107C23B-D16E-4022-9D04-9C192701C03C}' : IControlGeneralPlantInputCollection,
	'{8459A996-A7C2-4FD9-9B6E-0830F516F471}' : IControlGeneralPlantOutputCollection,
	'{8B72016D-C4F4-4BCA-958E-3149CD4CE891}' : IControlGeneralCoSim,
	'{09115E35-81E3-463E-8E2E-188FFF462A06}' : IControlGeneralCoSimCollection,
	'{76073096-D8D8-49AF-8FE1-14A645234D0B}' : IControlGeneralToolkit,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{CDD83BF7-B2D9-4539-B292-200CE2259917}' : 'IControlPlantInput',
	'{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}' : 'IControlPlantOutput',
	'{211EEA3E-CA4D-4C8E-B7AB-06240B3D2DF6}' : 'IControlPlantInputCollection',
	'{0C380EF2-6F62-4DAF-9F8D-7DD372D41B46}' : 'IControlPlantOutputCollection',
	'{0C8DABD9-7480-48E0-A8BF-68076ACB5DD8}' : 'IControlCoSim',
	'{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}' : 'IControlCoSimSimulink',
	'{A596000B-668A-4A1B-84C8-9A1F1249D1F5}' : 'IControlCoSimGeneral',
	'{7128F4FF-E1F1-4171-86B2-4AC5D5B12754}' : 'IControlCoSimSimplorer',
	'{1BC86F13-0032-45C7-9A70-288D4BAE8AA5}' : 'IControlCoSimAMESim',
	'{D647397B-70C5-4703-8EB6-6723E1689F17}' : 'IControlCoSimFMI',
	'{8B542970-81BF-49D6-B92A-60F4E17B88AE}' : 'IControlToolkit',
	'{E11A152B-12FC-400C-920C-E84E1B62E375}' : 'IControlGeneralPlantInput',
	'{48E89050-F3A8-4281-8CEA-F924B28CC4F3}' : 'IControlGeneralPlantOutput',
	'{1107C23B-D16E-4022-9D04-9C192701C03C}' : 'IControlGeneralPlantInputCollection',
	'{8459A996-A7C2-4FD9-9B6E-0830F516F471}' : 'IControlGeneralPlantOutputCollection',
	'{8B72016D-C4F4-4BCA-958E-3149CD4CE891}' : 'IControlGeneralCoSim',
	'{09115E35-81E3-463E-8E2E-188FFF462A06}' : 'IControlGeneralCoSimCollection',
	'{76073096-D8D8-49AF-8FE1-14A645234D0B}' : 'IControlGeneralToolkit',
}


NamesToIIDMap = {
	'IControlPlantInput' : '{CDD83BF7-B2D9-4539-B292-200CE2259917}',
	'IControlPlantOutput' : '{747FFCFC-EE5D-4F83-8E8F-AFC78279976A}',
	'IControlPlantInputCollection' : '{211EEA3E-CA4D-4C8E-B7AB-06240B3D2DF6}',
	'IControlPlantOutputCollection' : '{0C380EF2-6F62-4DAF-9F8D-7DD372D41B46}',
	'IControlCoSim' : '{0C8DABD9-7480-48E0-A8BF-68076ACB5DD8}',
	'IControlCoSimSimulink' : '{84D5B04D-6183-4AA5-9D3F-78ED0D21E3ED}',
	'IControlCoSimGeneral' : '{A596000B-668A-4A1B-84C8-9A1F1249D1F5}',
	'IControlCoSimSimplorer' : '{7128F4FF-E1F1-4171-86B2-4AC5D5B12754}',
	'IControlCoSimAMESim' : '{1BC86F13-0032-45C7-9A70-288D4BAE8AA5}',
	'IControlCoSimFMI' : '{D647397B-70C5-4703-8EB6-6723E1689F17}',
	'IControlToolkit' : '{8B542970-81BF-49D6-B92A-60F4E17B88AE}',
	'IControlGeneralPlantInput' : '{E11A152B-12FC-400C-920C-E84E1B62E375}',
	'IControlGeneralPlantOutput' : '{48E89050-F3A8-4281-8CEA-F924B28CC4F3}',
	'IControlGeneralPlantInputCollection' : '{1107C23B-D16E-4022-9D04-9C192701C03C}',
	'IControlGeneralPlantOutputCollection' : '{8459A996-A7C2-4FD9-9B6E-0830F516F471}',
	'IControlGeneralCoSim' : '{8B72016D-C4F4-4BCA-958E-3149CD4CE891}',
	'IControlGeneralCoSimCollection' : '{09115E35-81E3-463E-8E2E-188FFF462A06}',
	'IControlGeneralToolkit' : '{76073096-D8D8-49AF-8FE1-14A645234D0B}',
}


