# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMR2R2D.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMR2R2D Type Library'
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

CLSID = IID('{B1E504C4-80D4-4763-8E70-F896FE1E80E3}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class AirResistanceForceDirection(IntEnum):
	'''
	AirResistanceForceDirection enumeration.
	'''
	DirectionType_ElementNormal   =0         
	'''Constant value is 0.'''
	DirectionType_Velocity        =1         
	'''Constant value is 1.'''
class R2R2DAirResistanceType(IntEnum):
	'''
	R2R2DAirResistanceType enumeration.
	'''
	R2R2DAirResistanceType_Constant=0         
	'''Constant value is 0.'''
	R2R2DAirResistanceType_Expression=1         
	'''Constant value is 1.'''
class R2R2DDisplayNodeIDType(IntEnum):
	'''
	R2R2DDisplayNodeIDType enumeration.
	'''
	R2R2DDisplayNodeIDType_All    =1         
	'''Constant value is 1.'''
	R2R2DDisplayNodeIDType_None   =0         
	'''Constant value is 0.'''
	R2R2DDisplayNodeIDType_StartEnd=2         
	'''Constant value is 2.'''
class R2R2DInOutType(IntEnum):
	'''
	R2R2DInOutType enumeration.
	'''
	R2R2DInOutType_In             =0         
	'''Constant value is 0.'''
	R2R2DInOutType_None           =2         
	'''Constant value is 2.'''
	R2R2DInOutType_Out            =1         
	'''Constant value is 1.'''
class R2R2DMassType(IntEnum):
	'''
	R2R2DMassType enumeration.
	'''
	R2R2DMassType_Density         =0         
	'''Constant value is 0.'''
	R2R2DMassType_TotalMass       =1         
	'''Constant value is 1.'''
class R2R2DWinderConectedNodeType(IntEnum):
	'''
	R2R2DWinderConectedNodeType enumeration.
	'''
	R2R2DWinderConectedNodeType_End=1         
	'''Constant value is 1.'''
	R2R2DWinderConectedNodeType_Start=0         
	'''Constant value is 0.'''

from win32com.client import DispatchBaseClass
class IR2R2DBody(DispatchBaseClass):
	'''R2R2D body'''
	CLSID = IID('{9FC90B1C-92BE-4F20-99A2-144915D51DD4}')
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


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
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
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10001, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
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

class IR2R2DBodyBeam(DispatchBaseClass):
	'''R2R2D Beam Assembly'''
	CLSID = IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddPassingBody(self, pVal):
		'''
		Add a passing body
		
		:param pVal: IGeneric
		'''
		return self._oleobj_.InvokeTypes(10054, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody(self, pVal):
		'''
		Delete a passing body
		
		:param pVal: IGeneric
		'''
		return self._oleobj_.InvokeTypes(10055, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def UpdateAllProperties(self):
		'''
		Update all properties
		'''
		return self._oleobj_.InvokeTypes(10068, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_AirResistanceConstant(self):
		return self._ApplyTypes_(*(10062, 2, (9, 0), (), "AirResistanceConstant", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_AirResistanceExpression(self):
		return self._ApplyTypes_(*(10063, 2, (9, 0), (), "AirResistanceExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_AirResistanceForceDirection(self):
		return self._ApplyTypes_(*(10070, 2, (3, 0), (), "AirResistanceForceDirection", '{30A70529-402F-4740-B3A3-60A2037CF826}'))
	def _get_AirResistanceType(self):
		return self._ApplyTypes_(*(10061, 2, (3, 0), (), "AirResistanceType", '{7728E324-B286-4061-8A1C-2B2559F79CB4}'))
	def _get_BCCollection(self):
		return self._ApplyTypes_(*(10066, 2, (9, 0), (), "BCCollection", '{7F035946-EE7C-4557-BAFC-000BDD366EDF}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ConnectingParameters(self):
		return self._ApplyTypes_(*(10065, 2, (9, 0), (), "ConnectingParameters", '{21DDE70D-AD2A-48B1-9645-92F4E8A8BD14}'))
	def _get_FlexBody(self):
		return self._ApplyTypes_(*(10069, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10051, 2, (9, 0), (), "Geometry", '{22E7FECE-90EC-4649-A335-CD1139004817}'))
	def _get_InitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(10059, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MaterialProperty(self):
		return self._ApplyTypes_(*(10052, 2, (9, 0), (), "MaterialProperty", '{7474063C-637A-4F9E-ABC0-11F074027153}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_OutputCollection(self):
		return self._ApplyTypes_(*(10067, 2, (9, 0), (), "OutputCollection", '{4549131A-72B6-45B1-9ABE-C2A32F250FED}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PassingBodyCollection(self):
		return self._ApplyTypes_(*(10053, 2, (9, 0), (), "PassingBodyCollection", '{E5EED844-E317-49B8-B8F8-42DF2D16E4EC}'))
	def _get_SelfContact(self):
		return self._ApplyTypes_(*(10057, 2, (9, 0), (), "SelfContact", '{9AC66E9B-1D93-434B-BCD2-1F54446A3687}'))
	def _get_UseAirResistance(self):
		return self._ApplyTypes_(*(10060, 2, (11, 0), (), "UseAirResistance", None))
	def _get_UseInitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(10058, 2, (11, 0), (), "UseInitialLongitudinalVelocity", None))
	def _get_UseSelfContact(self):
		return self._ApplyTypes_(*(10056, 2, (11, 0), (), "UseSelfContact", None))
	def _get_UseUpdateGeometryAutomatically(self):
		return self._ApplyTypes_(*(10064, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_AirResistanceExpression(self, value):
		if "AirResistanceExpression" in self.__dict__: self.__dict__["AirResistanceExpression"] = value; return
		self._oleobj_.Invoke(*((10063, LCID, 4, 0) + (value,) + ()))
	def _set_AirResistanceForceDirection(self, value):
		if "AirResistanceForceDirection" in self.__dict__: self.__dict__["AirResistanceForceDirection"] = value; return
		self._oleobj_.Invoke(*((10070, LCID, 4, 0) + (value,) + ()))
	def _set_AirResistanceType(self, value):
		if "AirResistanceType" in self.__dict__: self.__dict__["AirResistanceType"] = value; return
		self._oleobj_.Invoke(*((10061, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseAirResistance(self, value):
		if "UseAirResistance" in self.__dict__: self.__dict__["UseAirResistance"] = value; return
		self._oleobj_.Invoke(*((10060, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialLongitudinalVelocity(self, value):
		if "UseInitialLongitudinalVelocity" in self.__dict__: self.__dict__["UseInitialLongitudinalVelocity"] = value; return
		self._oleobj_.Invoke(*((10058, LCID, 4, 0) + (value,) + ()))
	def _set_UseSelfContact(self, value):
		if "UseSelfContact" in self.__dict__: self.__dict__["UseSelfContact"] = value; return
		self._oleobj_.Invoke(*((10056, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdateGeometryAutomatically(self, value):
		if "UseUpdateGeometryAutomatically" in self.__dict__: self.__dict__["UseUpdateGeometryAutomatically"] = value; return
		self._oleobj_.Invoke(*((10064, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	AirResistanceConstant = property(_get_AirResistanceConstant, None)
	'''
	Air Resistance Coefficient Constant

	:type: recurdyn.ProcessNet.IDouble
	'''
	AirResistanceExpression = property(_get_AirResistanceExpression, _set_AirResistanceExpression)
	'''
	Air Resistance Coefficient Expression

	:type: recurdyn.ProcessNet.IExpression
	'''
	AirResistanceForceDirection = property(_get_AirResistanceForceDirection, _set_AirResistanceForceDirection)
	'''
	Air resistance force direction

	:type: recurdyn.R2R2D.AirResistanceForceDirection
	'''
	AirResistanceType = property(_get_AirResistanceType, _set_AirResistanceType)
	'''
	Air Resistance Coefficient Type

	:type: recurdyn.R2R2D.R2R2DAirResistanceType
	'''
	BCCollection = property(_get_BCCollection, None)
	'''
	Node boundary condition collection

	:type: recurdyn.ProcessNet.INodeBCCollection
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ConnectingParameters = property(_get_ConnectingParameters, None)
	'''
	Connecting parameters

	:type: recurdyn.R2R2D.IR2R2DConnectingParameters
	'''
	FlexBody = property(_get_FlexBody, None)
	'''
	Flex body edit

	:type: recurdyn.FFlex.IFFlexToolkitBody
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.R2R2D.IR2R2DGeometryBeam
	'''
	InitialLongitudinalVelocity = property(_get_InitialLongitudinalVelocity, None)
	'''
	Initial longitudinal velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	MaterialProperty = property(_get_MaterialProperty, None)
	'''
	Material property

	:type: recurdyn.R2R2D.IR2R2DMaterialPropertyBeam
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	OutputCollection = property(_get_OutputCollection, None)
	'''
	Node output collection

	:type: recurdyn.ProcessNet.INodeOutputCollection
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
	PassingBodyCollection = property(_get_PassingBodyCollection, None)
	'''
	Passing body collection

	:type: recurdyn.R2R2D.IR2R2DPassingBodyCollection
	'''
	SelfContact = property(_get_SelfContact, None)
	'''
	Self contact

	:type: recurdyn.R2R2D.IR2R2DSelfContact
	'''
	UseAirResistance = property(_get_UseAirResistance, _set_UseAirResistance)
	'''
	Use Air Resistance Coefficient

	:type: bool
	'''
	UseInitialLongitudinalVelocity = property(_get_UseInitialLongitudinalVelocity, _set_UseInitialLongitudinalVelocity)
	'''
	Use initial longitudinal velocity

	:type: bool
	'''
	UseSelfContact = property(_get_UseSelfContact, _set_UseSelfContact)
	'''
	Use self contact

	:type: bool
	'''
	UseUpdateGeometryAutomatically = property(_get_UseUpdateGeometryAutomatically, _set_UseUpdateGeometryAutomatically)
	'''
	Use Update Geometry Information Automatically

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_AirResistanceExpression": _set_AirResistanceExpression,
		"_set_AirResistanceForceDirection": _set_AirResistanceForceDirection,
		"_set_AirResistanceType": _set_AirResistanceType,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseAirResistance": _set_UseAirResistance,
		"_set_UseInitialLongitudinalVelocity": _set_UseInitialLongitudinalVelocity,
		"_set_UseSelfContact": _set_UseSelfContact,
		"_set_UseUpdateGeometryAutomatically": _set_UseUpdateGeometryAutomatically,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"AirResistanceConstant": (10062, 2, (9, 0), (), "AirResistanceConstant", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"AirResistanceExpression": (10063, 2, (9, 0), (), "AirResistanceExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"AirResistanceForceDirection": (10070, 2, (3, 0), (), "AirResistanceForceDirection", '{30A70529-402F-4740-B3A3-60A2037CF826}'),
		"AirResistanceType": (10061, 2, (3, 0), (), "AirResistanceType", '{7728E324-B286-4061-8A1C-2B2559F79CB4}'),
		"BCCollection": (10066, 2, (9, 0), (), "BCCollection", '{7F035946-EE7C-4557-BAFC-000BDD366EDF}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConnectingParameters": (10065, 2, (9, 0), (), "ConnectingParameters", '{21DDE70D-AD2A-48B1-9645-92F4E8A8BD14}'),
		"FlexBody": (10069, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (10051, 2, (9, 0), (), "Geometry", '{22E7FECE-90EC-4649-A335-CD1139004817}'),
		"InitialLongitudinalVelocity": (10059, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MaterialProperty": (10052, 2, (9, 0), (), "MaterialProperty", '{7474063C-637A-4F9E-ABC0-11F074027153}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"OutputCollection": (10067, 2, (9, 0), (), "OutputCollection", '{4549131A-72B6-45B1-9ABE-C2A32F250FED}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PassingBodyCollection": (10053, 2, (9, 0), (), "PassingBodyCollection", '{E5EED844-E317-49B8-B8F8-42DF2D16E4EC}'),
		"SelfContact": (10057, 2, (9, 0), (), "SelfContact", '{9AC66E9B-1D93-434B-BCD2-1F54446A3687}'),
		"UseAirResistance": (10060, 2, (11, 0), (), "UseAirResistance", None),
		"UseInitialLongitudinalVelocity": (10058, 2, (11, 0), (), "UseInitialLongitudinalVelocity", None),
		"UseSelfContact": (10056, 2, (11, 0), (), "UseSelfContact", None),
		"UseUpdateGeometryAutomatically": (10064, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"AirResistanceExpression": ((10063, LCID, 4, 0),()),
		"AirResistanceForceDirection": ((10070, LCID, 4, 0),()),
		"AirResistanceType": ((10061, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseAirResistance": ((10060, LCID, 4, 0),()),
		"UseInitialLongitudinalVelocity": ((10058, LCID, 4, 0),()),
		"UseSelfContact": ((10056, LCID, 4, 0),()),
		"UseUpdateGeometryAutomatically": ((10064, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DBodyBeamCollection(DispatchBaseClass):
	'''IR2R2DBodyBeamCollection'''
	CLSID = IID('{D51B4A60-30FE-4A2C-89CE-6DE904CD7771}')
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
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
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
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
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
		return win32com.client.util.Iterator(ob, '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IR2R2DBodyCollection(DispatchBaseClass):
	'''IR2R2DBodyCollection'''
	CLSID = IID('{F66AB8D5-E20C-437F-BD61-982CCD09B711}')
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
		:rtype: recurdyn.R2R2D.IR2R2DBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9FC90B1C-92BE-4F20-99A2-144915D51DD4}')
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
		:rtype: recurdyn.R2R2D.IR2R2DBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9FC90B1C-92BE-4F20-99A2-144915D51DD4}')
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
		return win32com.client.util.Iterator(ob, '{9FC90B1C-92BE-4F20-99A2-144915D51DD4}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{9FC90B1C-92BE-4F20-99A2-144915D51DD4}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IR2R2DBodyRoller(DispatchBaseClass):
	'''R2R2D body roller'''
	CLSID = IID('{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}')
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


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(10052, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_InnerContactPoints(self):
		return self._ApplyTypes_(*(10051, 2, (19, 0), (), "InnerContactPoints", None))
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

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_InnerContactPoints(self, value):
		if "InnerContactPoints" in self.__dict__: self.__dict__["InnerContactPoints"] = value; return
		self._oleobj_.Invoke(*((10051, LCID, 4, 0) + (value,) + ()))
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
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact Parameter

	:type: recurdyn.R2R2D.IR2R2DContactParameter
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	InnerContactPoints = property(_get_InnerContactPoints, _set_InnerContactPoints)
	'''
	The number of inner contat points

	:type: int
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
		"_set_Comment": _set_Comment,
		"_set_InnerContactPoints": _set_InnerContactPoints,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (10052, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10001, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"InnerContactPoints": (10051, 2, (19, 0), (), "InnerContactPoints", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"InnerContactPoints": ((10051, LCID, 4, 0),()),
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

class IR2R2DBodyRollerCircle(DispatchBaseClass):
	'''R2R2D circle roller body'''
	CLSID = IID('{33938809-28E5-4D14-B044-B074F7C7645B}')
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


	def _get_AssembledRadius(self):
		return self._ApplyTypes_(*(10101, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(10052, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10102, 2, (9, 0), (), "Geometry", '{87F304FE-B89E-4306-8454-35E94D2B1360}'))
	def _get_InnerContactPoints(self):
		return self._ApplyTypes_(*(10051, 2, (19, 0), (), "InnerContactPoints", None))
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

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_InnerContactPoints(self, value):
		if "InnerContactPoints" in self.__dict__: self.__dict__["InnerContactPoints"] = value; return
		self._oleobj_.Invoke(*((10051, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	AssembledRadius = property(_get_AssembledRadius, None)
	'''
	The assembled radius of circle roller.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact Parameter

	:type: recurdyn.R2R2D.IR2R2DContactParameter
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.R2R2D.IR2R2DGeometryRollerCircle
	'''
	InnerContactPoints = property(_get_InnerContactPoints, _set_InnerContactPoints)
	'''
	The number of inner contat points

	:type: int
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
		"_set_Comment": _set_Comment,
		"_set_InnerContactPoints": _set_InnerContactPoints,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"AssembledRadius": (10101, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (10052, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10001, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10102, 2, (9, 0), (), "Geometry", '{87F304FE-B89E-4306-8454-35E94D2B1360}'),
		"InnerContactPoints": (10051, 2, (19, 0), (), "InnerContactPoints", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"InnerContactPoints": ((10051, LCID, 4, 0),()),
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

class IR2R2DBodyRollerGeneral(DispatchBaseClass):
	'''R2R2D general roller body'''
	CLSID = IID('{E60EA1F3-9C5B-4411-9C9E-715C89C5F2D5}')
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


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(10052, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10101, 2, (9, 0), (), "Geometry", '{DC36087F-FBDD-42C4-ABD6-7D1FB7F00B09}'))
	def _get_InnerContactPoints(self):
		return self._ApplyTypes_(*(10051, 2, (19, 0), (), "InnerContactPoints", None))
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

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_InnerContactPoints(self, value):
		if "InnerContactPoints" in self.__dict__: self.__dict__["InnerContactPoints"] = value; return
		self._oleobj_.Invoke(*((10051, LCID, 4, 0) + (value,) + ()))
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
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact Parameter

	:type: recurdyn.R2R2D.IR2R2DContactParameter
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.R2R2D.IR2R2DGeometryRollerGeneral
	'''
	InnerContactPoints = property(_get_InnerContactPoints, _set_InnerContactPoints)
	'''
	The number of inner contat points

	:type: int
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
		"_set_Comment": _set_Comment,
		"_set_InnerContactPoints": _set_InnerContactPoints,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (10052, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10001, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10101, 2, (9, 0), (), "Geometry", '{DC36087F-FBDD-42C4-ABD6-7D1FB7F00B09}'),
		"InnerContactPoints": (10051, 2, (19, 0), (), "InnerContactPoints", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"InnerContactPoints": ((10051, LCID, 4, 0),()),
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

class IR2R2DConcentratedLoadUSUBCollection(DispatchBaseClass):
	'''IR2R2DConcentratedLoadUSUBCollection'''
	CLSID = IID('{4EEF5BEB-2CCF-4BD9-8159-CF6A337F2581}')
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
		:rtype: recurdyn.R2R2D.IR2R2DLoadConcentratedUSUB
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}')
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
		:rtype: recurdyn.R2R2D.IR2R2DLoadConcentratedUSUB
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}')
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
		return win32com.client.util.Iterator(ob, '{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IR2R2DConnectingParameters(DispatchBaseClass):
	'''R2R2D connecting parameters'''
	CLSID = IID('{21DDE70D-AD2A-48B1-9645-92F4E8A8BD14}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Mass(self):
		return self._ApplyTypes_(*(10102, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MomentOfInertia(self):
		return self._ApplyTypes_(*(10103, 2, (9, 0), (), "MomentOfInertia", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationnalDampingRatio(self):
		return self._ApplyTypes_(*(10107, 2, (9, 0), (), "RotationnalDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationnalStiffness(self):
		return self._ApplyTypes_(*(10106, 2, (9, 0), (), "RotationnalStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationalDampingRatio(self):
		return self._ApplyTypes_(*(10105, 2, (9, 0), (), "TranslationalDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationalStiffness(self):
		return self._ApplyTypes_(*(10104, 2, (9, 0), (), "TranslationalStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseForceConnector(self):
		return self._ApplyTypes_(*(10100, 2, (11, 0), (), "UseForceConnector", None))
	def _get_UseSyncFDR(self):
		return self._ApplyTypes_(*(10101, 2, (11, 0), (), "UseSyncFDR", None))

	def _set_UseForceConnector(self, value):
		if "UseForceConnector" in self.__dict__: self.__dict__["UseForceConnector"] = value; return
		self._oleobj_.Invoke(*((10100, LCID, 4, 0) + (value,) + ()))
	def _set_UseSyncFDR(self, value):
		if "UseSyncFDR" in self.__dict__: self.__dict__["UseSyncFDR"] = value; return
		self._oleobj_.Invoke(*((10101, LCID, 4, 0) + (value,) + ()))

	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	MomentOfInertia = property(_get_MomentOfInertia, None)
	'''
	Moment of inertia

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationnalDampingRatio = property(_get_RotationnalDampingRatio, None)
	'''
	Rotationnal damping ratio

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationnalStiffness = property(_get_RotationnalStiffness, None)
	'''
	Rotationnal stiffness

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationalDampingRatio = property(_get_TranslationalDampingRatio, None)
	'''
	Translational damping ratio

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationalStiffness = property(_get_TranslationalStiffness, None)
	'''
	Translational stiffness

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseForceConnector = property(_get_UseForceConnector, _set_UseForceConnector)
	'''
	Use force connector

	:type: bool
	'''
	UseSyncFDR = property(_get_UseSyncFDR, _set_UseSyncFDR)
	'''
	Use Sync. FDR

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_UseForceConnector": _set_UseForceConnector,
		"_set_UseSyncFDR": _set_UseSyncFDR,
	}
	_prop_map_get_ = {
		"Mass": (10102, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MomentOfInertia": (10103, 2, (9, 0), (), "MomentOfInertia", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationnalDampingRatio": (10107, 2, (9, 0), (), "RotationnalDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationnalStiffness": (10106, 2, (9, 0), (), "RotationnalStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationalDampingRatio": (10105, 2, (9, 0), (), "TranslationalDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationalStiffness": (10104, 2, (9, 0), (), "TranslationalStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseForceConnector": (10100, 2, (11, 0), (), "UseForceConnector", None),
		"UseSyncFDR": (10101, 2, (11, 0), (), "UseSyncFDR", None),
	}
	_prop_map_put_ = {
		"UseForceConnector": ((10100, LCID, 4, 0),()),
		"UseSyncFDR": ((10101, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DContact(DispatchBaseClass):
	'''R2R2D Contact'''
	CLSID = IID('{D72D730B-3E34-4ADB-B946-689EC685D591}')
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
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
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
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

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
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
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
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
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

class IR2R2DContactFriction(DispatchBaseClass):
	'''R2R2D contact friction'''
	CLSID = IID('{A70AF86B-7730-485D-880F-2B35DBE7D73E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DynamicThresholdVelocity(self):
		return self._ApplyTypes_(*(10054, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumFrictionForce(self):
		return self._ApplyTypes_(*(10061, 2, (9, 0), (), "MaximumFrictionForce", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialDynamicThresholdVelocity(self):
		return self._ApplyTypes_(*(10056, 2, (9, 0), (), "SpecialDynamicThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumFrictionForce(self):
		return self._ApplyTypes_(*(10063, 2, (9, 0), (), "SpecialMaximumFrictionForce", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStaticFrictionCoefficient(self):
		return self._ApplyTypes_(*(10059, 2, (9, 0), (), "SpecialStaticFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStaticThresholdVelocity(self):
		return self._ApplyTypes_(*(10053, 2, (9, 0), (), "SpecialStaticThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_StaticFrictionCoefficient(self):
		return self._ApplyTypes_(*(10057, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticThresholdVelocity(self):
		return self._ApplyTypes_(*(10051, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseMaximumFrictionForce(self):
		return self._ApplyTypes_(*(10060, 2, (11, 0), (), "UseMaximumFrictionForce", None))
	def _get_UseSpecialDynamicThresholdVelocity(self):
		return self._ApplyTypes_(*(10055, 2, (11, 0), (), "UseSpecialDynamicThresholdVelocity", None))
	def _get_UseSpecialMaximumFrictionForce(self):
		return self._ApplyTypes_(*(10062, 2, (11, 0), (), "UseSpecialMaximumFrictionForce", None))
	def _get_UseSpecialStaticFrictionCoefficient(self):
		return self._ApplyTypes_(*(10058, 2, (11, 0), (), "UseSpecialStaticFrictionCoefficient", None))
	def _get_UseSpecialStaticThresholdVelocity(self):
		return self._ApplyTypes_(*(10052, 2, (11, 0), (), "UseSpecialStaticThresholdVelocity", None))

	def _set_UseMaximumFrictionForce(self, value):
		if "UseMaximumFrictionForce" in self.__dict__: self.__dict__["UseMaximumFrictionForce"] = value; return
		self._oleobj_.Invoke(*((10060, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDynamicThresholdVelocity(self, value):
		if "UseSpecialDynamicThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialDynamicThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((10055, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumFrictionForce(self, value):
		if "UseSpecialMaximumFrictionForce" in self.__dict__: self.__dict__["UseSpecialMaximumFrictionForce"] = value; return
		self._oleobj_.Invoke(*((10062, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStaticFrictionCoefficient(self, value):
		if "UseSpecialStaticFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialStaticFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((10058, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStaticThresholdVelocity(self, value):
		if "UseSpecialStaticThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialStaticThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((10052, LCID, 4, 0) + (value,) + ()))

	DynamicThresholdVelocity = property(_get_DynamicThresholdVelocity, None)
	'''
	Dynamic threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumFrictionForce = property(_get_MaximumFrictionForce, None)
	'''
	Maximum friction force

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialDynamicThresholdVelocity = property(_get_SpecialDynamicThresholdVelocity, None)
	'''
	Special dynamic threshold velocity

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialMaximumFrictionForce = property(_get_SpecialMaximumFrictionForce, None)
	'''
	Special maximum friction force

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialStaticFrictionCoefficient = property(_get_SpecialStaticFrictionCoefficient, None)
	'''
	Special static friction coefficient

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialStaticThresholdVelocity = property(_get_SpecialStaticThresholdVelocity, None)
	'''
	Special static threshold velocity

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	StaticFrictionCoefficient = property(_get_StaticFrictionCoefficient, None)
	'''
	Static friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	StaticThresholdVelocity = property(_get_StaticThresholdVelocity, None)
	'''
	Static threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseMaximumFrictionForce = property(_get_UseMaximumFrictionForce, _set_UseMaximumFrictionForce)
	'''
	Use maximum friction force

	:type: bool
	'''
	UseSpecialDynamicThresholdVelocity = property(_get_UseSpecialDynamicThresholdVelocity, _set_UseSpecialDynamicThresholdVelocity)
	'''
	Use special dynamic threshold velocity

	:type: bool
	'''
	UseSpecialMaximumFrictionForce = property(_get_UseSpecialMaximumFrictionForce, _set_UseSpecialMaximumFrictionForce)
	'''
	Use special maximum friction force

	:type: bool
	'''
	UseSpecialStaticFrictionCoefficient = property(_get_UseSpecialStaticFrictionCoefficient, _set_UseSpecialStaticFrictionCoefficient)
	'''
	Use special static friction coefficient

	:type: bool
	'''
	UseSpecialStaticThresholdVelocity = property(_get_UseSpecialStaticThresholdVelocity, _set_UseSpecialStaticThresholdVelocity)
	'''
	Use special static threshold velocity

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_UseMaximumFrictionForce": _set_UseMaximumFrictionForce,
		"_set_UseSpecialDynamicThresholdVelocity": _set_UseSpecialDynamicThresholdVelocity,
		"_set_UseSpecialMaximumFrictionForce": _set_UseSpecialMaximumFrictionForce,
		"_set_UseSpecialStaticFrictionCoefficient": _set_UseSpecialStaticFrictionCoefficient,
		"_set_UseSpecialStaticThresholdVelocity": _set_UseSpecialStaticThresholdVelocity,
	}
	_prop_map_get_ = {
		"DynamicThresholdVelocity": (10054, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumFrictionForce": (10061, 2, (9, 0), (), "MaximumFrictionForce", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialDynamicThresholdVelocity": (10056, 2, (9, 0), (), "SpecialDynamicThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumFrictionForce": (10063, 2, (9, 0), (), "SpecialMaximumFrictionForce", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStaticFrictionCoefficient": (10059, 2, (9, 0), (), "SpecialStaticFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStaticThresholdVelocity": (10053, 2, (9, 0), (), "SpecialStaticThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"StaticFrictionCoefficient": (10057, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticThresholdVelocity": (10051, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseMaximumFrictionForce": (10060, 2, (11, 0), (), "UseMaximumFrictionForce", None),
		"UseSpecialDynamicThresholdVelocity": (10055, 2, (11, 0), (), "UseSpecialDynamicThresholdVelocity", None),
		"UseSpecialMaximumFrictionForce": (10062, 2, (11, 0), (), "UseSpecialMaximumFrictionForce", None),
		"UseSpecialStaticFrictionCoefficient": (10058, 2, (11, 0), (), "UseSpecialStaticFrictionCoefficient", None),
		"UseSpecialStaticThresholdVelocity": (10052, 2, (11, 0), (), "UseSpecialStaticThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"UseMaximumFrictionForce": ((10060, LCID, 4, 0),()),
		"UseSpecialDynamicThresholdVelocity": ((10055, LCID, 4, 0),()),
		"UseSpecialMaximumFrictionForce": ((10062, LCID, 4, 0),()),
		"UseSpecialStaticFrictionCoefficient": ((10058, LCID, 4, 0),()),
		"UseSpecialStaticThresholdVelocity": ((10052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DContactParameter(DispatchBaseClass):
	'''R2R2D contact property'''
	CLSID = IID('{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ContactFrictionType(self):
		return self._ApplyTypes_(*(10011, 2, (3, 0), (), "ContactFrictionType", '{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}'))
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(10006, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(10022, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(10008, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(10012, 2, (9, 0), (), "Friction", '{A70AF86B-7730-485D-880F-2B35DBE7D73E}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(10013, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(10014, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(10026, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaxPenetration(self):
		return self._ApplyTypes_(*(10030, 2, (9, 0), (), "MaxPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(10034, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialDamping(self):
		return self._ApplyTypes_(*(10010, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialDampingExponent(self):
		return self._ApplyTypes_(*(10024, 2, (9, 0), (), "SpecialDampingExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFriction(self):
		return self._ApplyTypes_(*(10016, 2, (9, 0), (), "SpecialFriction", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(10028, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaxPenetration(self):
		return self._ApplyTypes_(*(10032, 2, (9, 0), (), "SpecialMaxPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(10036, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(10005, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(10020, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(10018, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(10003, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(10021, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(10007, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(10025, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseMaxPenetration(self):
		return self._ApplyTypes_(*(10029, 2, (11, 0), (), "UseMaxPenetration", None))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(10033, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialDamping(self):
		return self._ApplyTypes_(*(10009, 2, (11, 0), (), "UseSpecialDamping", None))
	def _get_UseSpecialDampingExponent(self):
		return self._ApplyTypes_(*(10023, 2, (11, 0), (), "UseSpecialDampingExponent", None))
	def _get_UseSpecialFriction(self):
		return self._ApplyTypes_(*(10015, 2, (11, 0), (), "UseSpecialFriction", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(10027, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaxPenetration(self):
		return self._ApplyTypes_(*(10031, 2, (11, 0), (), "UseSpecialMaxPenetration", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(10035, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(10004, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(10019, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(10017, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(10002, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_ContactFrictionType(self, value):
		if "ContactFrictionType" in self.__dict__: self.__dict__["ContactFrictionType"] = value; return
		self._oleobj_.Invoke(*((10011, LCID, 4, 0) + (value,) + ()))
	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((10008, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((10014, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10003, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((10021, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((10007, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((10025, LCID, 4, 0) + (value,) + ()))
	def _set_UseMaxPenetration(self, value):
		if "UseMaxPenetration" in self.__dict__: self.__dict__["UseMaxPenetration"] = value; return
		self._oleobj_.Invoke(*((10029, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((10033, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDamping(self, value):
		if "UseSpecialDamping" in self.__dict__: self.__dict__["UseSpecialDamping"] = value; return
		self._oleobj_.Invoke(*((10009, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDampingExponent(self, value):
		if "UseSpecialDampingExponent" in self.__dict__: self.__dict__["UseSpecialDampingExponent"] = value; return
		self._oleobj_.Invoke(*((10023, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFriction(self, value):
		if "UseSpecialFriction" in self.__dict__: self.__dict__["UseSpecialFriction"] = value; return
		self._oleobj_.Invoke(*((10015, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((10027, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaxPenetration(self, value):
		if "UseSpecialMaxPenetration" in self.__dict__: self.__dict__["UseSpecialMaxPenetration"] = value; return
		self._oleobj_.Invoke(*((10031, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((10035, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((10004, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((10019, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((10017, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10002, LCID, 4, 0) + (value,) + ()))

	ContactFrictionType = property(_get_ContactFrictionType, _set_ContactFrictionType)
	'''
	Contact friction type

	:type: recurdyn.ProcessNet.ContactFrictionType
	'''
	DampingCoefficient = property(_get_DampingCoefficient, None)
	'''
	The viscous damping coefficient for the contact normal force

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingExponent = property(_get_DampingExponent, None)
	'''
	The damping exponent for a non-linear contact normal force

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingSpline = property(_get_DampingSpline, _set_DampingSpline)
	'''
	Damping spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	Friction = property(_get_Friction, None)
	'''
	Friction

	:type: recurdyn.R2R2D.IR2R2DContactFriction
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	The friction coefficient for the contact normal force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionSpline = property(_get_FrictionSpline, _set_FrictionSpline)
	'''
	The spline which shows relative velocity to the friction coefficient or the friction force.

	:type: recurdyn.ProcessNet.ISpline
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	The indentation exponent yields an indentation damping effect.

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaxPenetration = property(_get_MaxPenetration, None)
	'''
	Maximum penetration, use only for linear guide

	:type: recurdyn.ProcessNet.IDouble
	'''
	RDF = property(_get_RDF, None)
	'''
	Rebound damping factor(RDF)

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialDamping = property(_get_SpecialDamping, None)
	'''
	Special damping

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialDampingExponent = property(_get_SpecialDampingExponent, None)
	'''
	Special damping exponent

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialFriction = property(_get_SpecialFriction, None)
	'''
	Special friction coefficient

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialIndentationExponent = property(_get_SpecialIndentationExponent, None)
	'''
	Special indentation exponent

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialMaxPenetration = property(_get_SpecialMaxPenetration, None)
	'''
	Special maximum penetration, use only for linear guide

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialRDF = property(_get_SpecialRDF, None)
	'''
	Special rebound damping factor(RDF)

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialStiffness = property(_get_SpecialStiffness, None)
	'''
	Special stiffness

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialStiffnessExponent = property(_get_SpecialStiffnessExponent, None)
	'''
	Special stiffness exponent

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	StiffnessCoefficient = property(_get_StiffnessCoefficient, None)
	'''
	The stiffness coefficient for the contact normal force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	The stiffness exponent for a non-linear contact normal force

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessSpline = property(_get_StiffnessSpline, _set_StiffnessSpline)
	'''
	Stiffness spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	UseDampingExponent = property(_get_UseDampingExponent, _set_UseDampingExponent)
	'''
	Use damping exponent

	:type: bool
	'''
	UseDampingSpline = property(_get_UseDampingSpline, _set_UseDampingSpline)
	'''
	Use damping spline

	:type: bool
	'''
	UseIndentationExponent = property(_get_UseIndentationExponent, _set_UseIndentationExponent)
	'''
	Use indentation exponent

	:type: bool
	'''
	UseMaxPenetration = property(_get_UseMaxPenetration, _set_UseMaxPenetration)
	'''
	Use maximum penetration, use only for linear guide

	:type: bool
	'''
	UseRDF = property(_get_UseRDF, _set_UseRDF)
	'''
	Use rebound damping factor(RDF)

	:type: bool
	'''
	UseSpecialDamping = property(_get_UseSpecialDamping, _set_UseSpecialDamping)
	'''
	Use special damping

	:type: bool
	'''
	UseSpecialDampingExponent = property(_get_UseSpecialDampingExponent, _set_UseSpecialDampingExponent)
	'''
	Use special damping exponent

	:type: bool
	'''
	UseSpecialFriction = property(_get_UseSpecialFriction, _set_UseSpecialFriction)
	'''
	Use special friction coefficient

	:type: bool
	'''
	UseSpecialIndentationExponent = property(_get_UseSpecialIndentationExponent, _set_UseSpecialIndentationExponent)
	'''
	Use special indentation exponent

	:type: bool
	'''
	UseSpecialMaxPenetration = property(_get_UseSpecialMaxPenetration, _set_UseSpecialMaxPenetration)
	'''
	Use special maximum penetration, use only for linear guide

	:type: bool
	'''
	UseSpecialRDF = property(_get_UseSpecialRDF, _set_UseSpecialRDF)
	'''
	Use special rebound damping factor(RDF)

	:type: bool
	'''
	UseSpecialStiffness = property(_get_UseSpecialStiffness, _set_UseSpecialStiffness)
	'''
	Use special stiffness

	:type: bool
	'''
	UseSpecialStiffnessExponent = property(_get_UseSpecialStiffnessExponent, _set_UseSpecialStiffnessExponent)
	'''
	Use special stiffness exponent

	:type: bool
	'''
	UseStiffnessExponent = property(_get_UseStiffnessExponent, _set_UseStiffnessExponent)
	'''
	Use stiffness exponent

	:type: bool
	'''
	UseStiffnessSpline = property(_get_UseStiffnessSpline, _set_UseStiffnessSpline)
	'''
	Use stiffness spline

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactFrictionType": _set_ContactFrictionType,
		"_set_DampingSpline": _set_DampingSpline,
		"_set_FrictionSpline": _set_FrictionSpline,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseIndentationExponent": _set_UseIndentationExponent,
		"_set_UseMaxPenetration": _set_UseMaxPenetration,
		"_set_UseRDF": _set_UseRDF,
		"_set_UseSpecialDamping": _set_UseSpecialDamping,
		"_set_UseSpecialDampingExponent": _set_UseSpecialDampingExponent,
		"_set_UseSpecialFriction": _set_UseSpecialFriction,
		"_set_UseSpecialIndentationExponent": _set_UseSpecialIndentationExponent,
		"_set_UseSpecialMaxPenetration": _set_UseSpecialMaxPenetration,
		"_set_UseSpecialRDF": _set_UseSpecialRDF,
		"_set_UseSpecialStiffness": _set_UseSpecialStiffness,
		"_set_UseSpecialStiffnessExponent": _set_UseSpecialStiffnessExponent,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
	}
	_prop_map_get_ = {
		"ContactFrictionType": (10011, 2, (3, 0), (), "ContactFrictionType", '{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}'),
		"DampingCoefficient": (10006, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (10022, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (10008, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"Friction": (10012, 2, (9, 0), (), "Friction", '{A70AF86B-7730-485D-880F-2B35DBE7D73E}'),
		"FrictionCoefficient": (10013, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (10014, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"IndentationExponent": (10026, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaxPenetration": (10030, 2, (9, 0), (), "MaxPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (10034, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialDamping": (10010, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialDampingExponent": (10024, 2, (9, 0), (), "SpecialDampingExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFriction": (10016, 2, (9, 0), (), "SpecialFriction", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (10028, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaxPenetration": (10032, 2, (9, 0), (), "SpecialMaxPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (10036, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (10005, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (10020, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"StiffnessCoefficient": (10001, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (10018, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (10003, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (10021, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (10007, 2, (11, 0), (), "UseDampingSpline", None),
		"UseIndentationExponent": (10025, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseMaxPenetration": (10029, 2, (11, 0), (), "UseMaxPenetration", None),
		"UseRDF": (10033, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialDamping": (10009, 2, (11, 0), (), "UseSpecialDamping", None),
		"UseSpecialDampingExponent": (10023, 2, (11, 0), (), "UseSpecialDampingExponent", None),
		"UseSpecialFriction": (10015, 2, (11, 0), (), "UseSpecialFriction", None),
		"UseSpecialIndentationExponent": (10027, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaxPenetration": (10031, 2, (11, 0), (), "UseSpecialMaxPenetration", None),
		"UseSpecialRDF": (10035, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (10004, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (10019, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseStiffnessExponent": (10017, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (10002, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"ContactFrictionType": ((10011, LCID, 4, 0),()),
		"DampingSpline": ((10008, LCID, 4, 0),()),
		"FrictionSpline": ((10014, LCID, 4, 0),()),
		"StiffnessSpline": ((10003, LCID, 4, 0),()),
		"UseDampingExponent": ((10021, LCID, 4, 0),()),
		"UseDampingSpline": ((10007, LCID, 4, 0),()),
		"UseIndentationExponent": ((10025, LCID, 4, 0),()),
		"UseMaxPenetration": ((10029, LCID, 4, 0),()),
		"UseRDF": ((10033, LCID, 4, 0),()),
		"UseSpecialDamping": ((10009, LCID, 4, 0),()),
		"UseSpecialDampingExponent": ((10023, LCID, 4, 0),()),
		"UseSpecialFriction": ((10015, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((10027, LCID, 4, 0),()),
		"UseSpecialMaxPenetration": ((10031, LCID, 4, 0),()),
		"UseSpecialRDF": ((10035, LCID, 4, 0),()),
		"UseSpecialStiffness": ((10004, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((10019, LCID, 4, 0),()),
		"UseStiffnessExponent": ((10017, LCID, 4, 0),()),
		"UseStiffnessSpline": ((10002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DContactWorkpieceToWorkpiece(DispatchBaseClass):
	'''R2R2D Workpiece to Workpiece Contact'''
	CLSID = IID('{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}')
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


	def _get_ActionBeamAssembly(self):
		return self._ApplyTypes_(*(10052, 2, (9, 0), (), "ActionBeamAssembly", '{FF337086-F852-42E3-BF88-2795D0BBCB31}'))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBeamAssembly(self):
		return self._ApplyTypes_(*(10051, 2, (9, 0), (), "BaseBeamAssembly", '{FF337086-F852-42E3-BF88-2795D0BBCB31}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(10054, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InnerContactPoints(self):
		return self._ApplyTypes_(*(10053, 2, (19, 0), (), "InnerContactPoints", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
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

	def _set_ActionBeamAssembly(self, value):
		if "ActionBeamAssembly" in self.__dict__: self.__dict__["ActionBeamAssembly"] = value; return
		self._oleobj_.Invoke(*((10052, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBeamAssembly(self, value):
		if "BaseBeamAssembly" in self.__dict__: self.__dict__["BaseBeamAssembly"] = value; return
		self._oleobj_.Invoke(*((10051, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_InnerContactPoints(self, value):
		if "InnerContactPoints" in self.__dict__: self.__dict__["InnerContactPoints"] = value; return
		self._oleobj_.Invoke(*((10053, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionBeamAssembly = property(_get_ActionBeamAssembly, _set_ActionBeamAssembly)
	'''
	Action Beam Assembly

	:type: recurdyn.R2R2D.IR2R2DBodyBeam
	'''
	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseBeamAssembly = property(_get_BaseBeamAssembly, _set_BaseBeamAssembly)
	'''
	Base Beam Assembly

	:type: recurdyn.R2R2D.IR2R2DBodyBeam
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact Parameter

	:type: recurdyn.R2R2D.IR2R2DContactParameter
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	InnerContactPoints = property(_get_InnerContactPoints, _set_InnerContactPoints)
	'''
	The number of inner contat points

	:type: int
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
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
		"_set_ActionBeamAssembly": _set_ActionBeamAssembly,
		"_set_Active": _set_Active,
		"_set_BaseBeamAssembly": _set_BaseBeamAssembly,
		"_set_Comment": _set_Comment,
		"_set_InnerContactPoints": _set_InnerContactPoints,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionBeamAssembly": (10052, 2, (9, 0), (), "ActionBeamAssembly", '{FF337086-F852-42E3-BF88-2795D0BBCB31}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBeamAssembly": (10051, 2, (9, 0), (), "BaseBeamAssembly", '{FF337086-F852-42E3-BF88-2795D0BBCB31}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (10054, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InnerContactPoints": (10053, 2, (19, 0), (), "InnerContactPoints", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionBeamAssembly": ((10052, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseBeamAssembly": ((10051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"InnerContactPoints": ((10053, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
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

class IR2R2DContactWorkpieceToWorkpieceCollection(DispatchBaseClass):
	'''IR2R2DContactWorkpieceToWorkpieceCollection'''
	CLSID = IID('{3AC2E0DA-1DEA-4818-B371-A35C8E858CAE}')
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
		:rtype: recurdyn.R2R2D.IR2R2DContactWorkpieceToWorkpiece
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}')
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
		:rtype: recurdyn.R2R2D.IR2R2DContactWorkpieceToWorkpiece
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}')
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
		return win32com.client.util.Iterator(ob, '{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IR2R2DGeometryBeam(DispatchBaseClass):
	'''R2R2D Beam geometry'''
	CLSID = IID('{22E7FECE-90EC-4649-A335-CD1139004817}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Color(self):
		return self._ApplyTypes_(*(10100, 2, (19, 0), (), "Color", None))
	def _get_Depth(self):
		return self._ApplyTypes_(*(10106, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DisplayGeometry(self):
		return self._ApplyTypes_(*(10101, 2, (11, 0), (), "DisplayGeometry", None))
	def _get_DisplayNodeID(self):
		return self._ApplyTypes_(*(10102, 2, (11, 0), (), "DisplayNodeID", None))
	def _get_DisplayNodeIDType(self):
		return self._ApplyTypes_(*(10112, 2, (3, 0), (), "DisplayNodeIDType", '{E009C436-BA56-4876-B240-53635C5A6AF2}'))
	def _get_ElementLength(self):
		return self._ApplyTypes_(*(10110, 2, (5, 0), (), "ElementLength", None))
	def _get_NumberOfElements(self):
		return self._ApplyTypes_(*(10109, 2, (19, 0), (), "NumberOfElements", None))
	def _get_SpecialDepth(self):
		return self._ApplyTypes_(*(10108, 2, (9, 0), (), "SpecialDepth", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThickness(self):
		return self._ApplyTypes_(*(10105, 2, (9, 0), (), "SpecialThickness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_StretchedLength(self):
		return self._ApplyTypes_(*(10111, 2, (9, 0), (), "StretchedLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(10103, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseSpecialDepth(self):
		return self._ApplyTypes_(*(10107, 2, (11, 0), (), "UseSpecialDepth", None))
	def _get_UseSpecialThickness(self):
		return self._ApplyTypes_(*(10104, 2, (11, 0), (), "UseSpecialThickness", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((10100, LCID, 4, 0) + (value,) + ()))
	def _set_DisplayGeometry(self, value):
		if "DisplayGeometry" in self.__dict__: self.__dict__["DisplayGeometry"] = value; return
		self._oleobj_.Invoke(*((10101, LCID, 4, 0) + (value,) + ()))
	def _set_DisplayNodeID(self, value):
		if "DisplayNodeID" in self.__dict__: self.__dict__["DisplayNodeID"] = value; return
		self._oleobj_.Invoke(*((10102, LCID, 4, 0) + (value,) + ()))
	def _set_DisplayNodeIDType(self, value):
		if "DisplayNodeIDType" in self.__dict__: self.__dict__["DisplayNodeIDType"] = value; return
		self._oleobj_.Invoke(*((10112, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDepth(self, value):
		if "UseSpecialDepth" in self.__dict__: self.__dict__["UseSpecialDepth"] = value; return
		self._oleobj_.Invoke(*((10107, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThickness(self, value):
		if "UseSpecialThickness" in self.__dict__: self.__dict__["UseSpecialThickness"] = value; return
		self._oleobj_.Invoke(*((10104, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Belt color

	:type: int
	'''
	Depth = property(_get_Depth, None)
	'''
	Depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	DisplayGeometry = property(_get_DisplayGeometry, _set_DisplayGeometry)
	'''
	Display geometry

	:type: bool
	'''
	DisplayNodeID = property(_get_DisplayNodeID, _set_DisplayNodeID)
	'''
	This is an obsolete property. Use DisplayNodeIDType.

	:type: bool
	'''
	DisplayNodeIDType = property(_get_DisplayNodeIDType, _set_DisplayNodeIDType)
	'''
	Display Node ID type

	:type: recurdyn.R2R2D.R2R2DDisplayNodeIDType
	'''
	ElementLength = property(_get_ElementLength, None)
	'''
	Element length

	:type: float
	'''
	NumberOfElements = property(_get_NumberOfElements, None)
	'''
	Number of elements

	:type: int
	'''
	SpecialDepth = property(_get_SpecialDepth, None)
	'''
	Special depth

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialThickness = property(_get_SpecialThickness, None)
	'''
	Special thickness

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	StretchedLength = property(_get_StretchedLength, None)
	'''
	Stretched length

	:type: recurdyn.ProcessNet.IDouble
	'''
	Thickness = property(_get_Thickness, None)
	'''
	Thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseSpecialDepth = property(_get_UseSpecialDepth, _set_UseSpecialDepth)
	'''
	Use special depth

	:type: bool
	'''
	UseSpecialThickness = property(_get_UseSpecialThickness, _set_UseSpecialThickness)
	'''
	Use special thickness

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_DisplayGeometry": _set_DisplayGeometry,
		"_set_DisplayNodeID": _set_DisplayNodeID,
		"_set_DisplayNodeIDType": _set_DisplayNodeIDType,
		"_set_UseSpecialDepth": _set_UseSpecialDepth,
		"_set_UseSpecialThickness": _set_UseSpecialThickness,
	}
	_prop_map_get_ = {
		"Color": (10100, 2, (19, 0), (), "Color", None),
		"Depth": (10106, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DisplayGeometry": (10101, 2, (11, 0), (), "DisplayGeometry", None),
		"DisplayNodeID": (10102, 2, (11, 0), (), "DisplayNodeID", None),
		"DisplayNodeIDType": (10112, 2, (3, 0), (), "DisplayNodeIDType", '{E009C436-BA56-4876-B240-53635C5A6AF2}'),
		"ElementLength": (10110, 2, (5, 0), (), "ElementLength", None),
		"NumberOfElements": (10109, 2, (19, 0), (), "NumberOfElements", None),
		"SpecialDepth": (10108, 2, (9, 0), (), "SpecialDepth", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThickness": (10105, 2, (9, 0), (), "SpecialThickness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"StretchedLength": (10111, 2, (9, 0), (), "StretchedLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Thickness": (10103, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseSpecialDepth": (10107, 2, (11, 0), (), "UseSpecialDepth", None),
		"UseSpecialThickness": (10104, 2, (11, 0), (), "UseSpecialThickness", None),
	}
	_prop_map_put_ = {
		"Color": ((10100, LCID, 4, 0),()),
		"DisplayGeometry": ((10101, LCID, 4, 0),()),
		"DisplayNodeID": ((10102, LCID, 4, 0),()),
		"DisplayNodeIDType": ((10112, LCID, 4, 0),()),
		"UseSpecialDepth": ((10107, LCID, 4, 0),()),
		"UseSpecialThickness": ((10104, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DGeometryRollerCircle(DispatchBaseClass):
	'''R2R2D circle roller body geometry'''
	CLSID = IID('{87F304FE-B89E-4306-8454-35E94D2B1360}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetBoundingBox(self):
		'''
		Get bounding box, internal use only
		
		:rtype: (float, float, float, float, float, float)
		'''
		return self._ApplyTypes_(152, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetBoundingBox', None,pythoncom.Missing
			, pythoncom.Missing, pythoncom.Missing, pythoncom.Missing, pythoncom.Missing, pythoncom.Missing
			)


	def GetBoundingBoxWithRefFrame(self, RefFrame):
		'''
		Get bounding box with reference frame 
		
		:param RefFrame: IReferenceFrame
		:rtype: list[float]
		'''
		return self._ApplyTypes_(154, 1, (8197, 0), ((9, 1),), 'GetBoundingBoxWithRefFrame', None,RefFrame
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Depth(self):
		return self._ApplyTypes_(*(10102, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(10101, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))

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
	Depth = property(_get_Depth, None)
	'''
	The depth of circle roller.

	:type: recurdyn.ProcessNet.IDouble
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyGeometry
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
	Radius = property(_get_Radius, None)
	'''
	The radius of circle roller.

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Depth": (10102, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (10101, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
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

class IR2R2DGeometryRollerGeneral(DispatchBaseClass):
	'''R2R2D general roller body geometry'''
	CLSID = IID('{DC36087F-FBDD-42C4-ABD6-7D1FB7F00B09}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Export(self, strName, val):
		'''
		Export method
		
		:param strName: str
		:param val: bool
		'''
		return self._oleobj_.InvokeTypes(10103, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def GetBoundingBox(self):
		'''
		Get bounding box, internal use only
		
		:rtype: (float, float, float, float, float, float)
		'''
		return self._ApplyTypes_(152, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2), (16389, 2)), 'GetBoundingBox', None,pythoncom.Missing
			, pythoncom.Missing, pythoncom.Missing, pythoncom.Missing, pythoncom.Missing, pythoncom.Missing
			)


	def GetBoundingBoxWithRefFrame(self, RefFrame):
		'''
		Get bounding box with reference frame 
		
		:param RefFrame: IReferenceFrame
		:rtype: list[float]
		'''
		return self._ApplyTypes_(154, 1, (8197, 0), ((9, 1),), 'GetBoundingBoxWithRefFrame', None,RefFrame
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(10104, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Depth(self):
		return self._ApplyTypes_(*(10101, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PointCollection(self):
		return self._ApplyTypes_(*(10102, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))

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
	Depth = property(_get_Depth, None)
	'''
	The depth of general roller.

	:type: recurdyn.ProcessNet.IDouble
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyGeometry
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
	PointCollection = property(_get_PointCollection, None)
	'''
	Point with radius collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Depth": (10101, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PointCollection": (10102, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
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

class IR2R2DGuide(DispatchBaseClass):
	'''R2R2D guide'''
	CLSID = IID('{11C08FE6-98DF-4121-8503-4691765A0DAB}')
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


	def UpdateAllProperties(self):
		'''
		Update All Properties
		'''
		return self._oleobj_.InvokeTypes(10004, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(10002, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InnerContactPoints(self):
		return self._ApplyTypes_(*(10003, 2, (19, 0), (), "InnerContactPoints", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
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
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_InnerContactPoints(self, value):
		if "InnerContactPoints" in self.__dict__: self.__dict__["InnerContactPoints"] = value; return
		self._oleobj_.Invoke(*((10003, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((10001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact Parameter

	:type: recurdyn.R2R2D.IR2R2DContactParameter
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	InnerContactPoints = property(_get_InnerContactPoints, _set_InnerContactPoints)
	'''
	The number of inner contat points

	:type: int
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	MotherBody = property(_get_MotherBody, _set_MotherBody)
	'''
	The mother body of guide

	:type: recurdyn.ProcessNet.IGeneric
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
		"_set_InnerContactPoints": _set_InnerContactPoints,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (10002, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InnerContactPoints": (10003, 2, (19, 0), (), "InnerContactPoints", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (10001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"InnerContactPoints": ((10003, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((10001, LCID, 4, 0),()),
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

class IR2R2DGuideArc(DispatchBaseClass):
	'''R2R2D arc guide'''
	CLSID = IID('{6213B8B2-5B65-4259-8783-30AF5BAE2F10}')
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


	def UpdateAllProperties(self):
		'''
		Update All Properties
		'''
		return self._oleobj_.InvokeTypes(10004, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Angle(self):
		return self._ApplyTypes_(*(10052, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CenterPoint(self):
		return self._ApplyTypes_(*(10053, 2, (9, 0), (), "CenterPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_CircleEdgeRadius(self):
		return self._ApplyTypes_(*(10059, 2, (9, 0), (), "CircleEdgeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(10002, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'))
	def _get_DirectionPoint(self):
		return self._ApplyTypes_(*(10054, 2, (8197, 0), (), "DirectionPoint", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_ImaginaryCircleEdgeEnd(self):
		return self._ApplyTypes_(*(10056, 2, (11, 0), (), "ImaginaryCircleEdgeEnd", None))
	def _get_ImaginaryCircleEdgeStart(self):
		return self._ApplyTypes_(*(10055, 2, (11, 0), (), "ImaginaryCircleEdgeStart", None))
	def _get_InnerContactPoints(self):
		return self._ApplyTypes_(*(10003, 2, (19, 0), (), "InnerContactPoints", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(10051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialCircleEdgeRadius(self):
		return self._ApplyTypes_(*(10058, 2, (9, 0), (), "SpecialCircleEdgeRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseSpecialCircleEdgeRadius(self):
		return self._ApplyTypes_(*(10057, 2, (11, 0), (), "UseSpecialCircleEdgeRadius", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DirectionPoint(self, value):
		if "DirectionPoint" in self.__dict__: self.__dict__["DirectionPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10054, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ImaginaryCircleEdgeEnd(self, value):
		if "ImaginaryCircleEdgeEnd" in self.__dict__: self.__dict__["ImaginaryCircleEdgeEnd"] = value; return
		self._oleobj_.Invoke(*((10056, LCID, 4, 0) + (value,) + ()))
	def _set_ImaginaryCircleEdgeStart(self, value):
		if "ImaginaryCircleEdgeStart" in self.__dict__: self.__dict__["ImaginaryCircleEdgeStart"] = value; return
		self._oleobj_.Invoke(*((10055, LCID, 4, 0) + (value,) + ()))
	def _set_InnerContactPoints(self, value):
		if "InnerContactPoints" in self.__dict__: self.__dict__["InnerContactPoints"] = value; return
		self._oleobj_.Invoke(*((10003, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((10001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialCircleEdgeRadius(self, value):
		if "UseSpecialCircleEdgeRadius" in self.__dict__: self.__dict__["UseSpecialCircleEdgeRadius"] = value; return
		self._oleobj_.Invoke(*((10057, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	Angle = property(_get_Angle, None)
	'''
	The angle of arc

	:type: recurdyn.ProcessNet.IDouble
	'''
	CenterPoint = property(_get_CenterPoint, None)
	'''
	The center point of arc

	:type: recurdyn.ProcessNet.IVector
	'''
	CircleEdgeRadius = property(_get_CircleEdgeRadius, None)
	'''
	The radius of imaginary circle edge

	:type: recurdyn.ProcessNet.IDouble
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact Parameter

	:type: recurdyn.R2R2D.IR2R2DContactParameter
	'''
	DirectionPoint = property(_get_DirectionPoint, _set_DirectionPoint)
	'''
	The direction of arc

	:type: list[float]
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	ImaginaryCircleEdgeEnd = property(_get_ImaginaryCircleEdgeEnd, _set_ImaginaryCircleEdgeEnd)
	'''
	End point of imaginary circle edge

	:type: bool
	'''
	ImaginaryCircleEdgeStart = property(_get_ImaginaryCircleEdgeStart, _set_ImaginaryCircleEdgeStart)
	'''
	Start point of imaginary circle edge

	:type: bool
	'''
	InnerContactPoints = property(_get_InnerContactPoints, _set_InnerContactPoints)
	'''
	The number of inner contat points

	:type: int
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	MotherBody = property(_get_MotherBody, _set_MotherBody)
	'''
	The mother body of guide

	:type: recurdyn.ProcessNet.IGeneric
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
	Radius = property(_get_Radius, None)
	'''
	The radius of arc

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialCircleEdgeRadius = property(_get_SpecialCircleEdgeRadius, None)
	'''
	The special radius of imaginary circle edge

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseSpecialCircleEdgeRadius = property(_get_UseSpecialCircleEdgeRadius, _set_UseSpecialCircleEdgeRadius)
	'''
	Use special radius of imaginary circle edge

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_DirectionPoint": _set_DirectionPoint,
		"_set_ImaginaryCircleEdgeEnd": _set_ImaginaryCircleEdgeEnd,
		"_set_ImaginaryCircleEdgeStart": _set_ImaginaryCircleEdgeStart,
		"_set_InnerContactPoints": _set_InnerContactPoints,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_UseSpecialCircleEdgeRadius": _set_UseSpecialCircleEdgeRadius,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Angle": (10052, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CenterPoint": (10053, 2, (9, 0), (), "CenterPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"CircleEdgeRadius": (10059, 2, (9, 0), (), "CircleEdgeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (10002, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'),
		"DirectionPoint": (10054, 2, (8197, 0), (), "DirectionPoint", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"ImaginaryCircleEdgeEnd": (10056, 2, (11, 0), (), "ImaginaryCircleEdgeEnd", None),
		"ImaginaryCircleEdgeStart": (10055, 2, (11, 0), (), "ImaginaryCircleEdgeStart", None),
		"InnerContactPoints": (10003, 2, (19, 0), (), "InnerContactPoints", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (10001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (10051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialCircleEdgeRadius": (10058, 2, (9, 0), (), "SpecialCircleEdgeRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseSpecialCircleEdgeRadius": (10057, 2, (11, 0), (), "UseSpecialCircleEdgeRadius", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DirectionPoint": ((10054, LCID, 4, 0),()),
		"ImaginaryCircleEdgeEnd": ((10056, LCID, 4, 0),()),
		"ImaginaryCircleEdgeStart": ((10055, LCID, 4, 0),()),
		"InnerContactPoints": ((10003, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((10001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialCircleEdgeRadius": ((10057, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DGuideCircle(DispatchBaseClass):
	'''R2R2D circle guide'''
	CLSID = IID('{A5D8C80B-2C7A-4C35-9393-7ADBB640A5F6}')
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


	def UpdateAllProperties(self):
		'''
		Update All Properties
		'''
		return self._oleobj_.InvokeTypes(10004, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_CenterPoint(self):
		return self._ApplyTypes_(*(10052, 2, (9, 0), (), "CenterPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(10002, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InnerContactPoints(self):
		return self._ApplyTypes_(*(10003, 2, (19, 0), (), "InnerContactPoints", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(10051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_InnerContactPoints(self, value):
		if "InnerContactPoints" in self.__dict__: self.__dict__["InnerContactPoints"] = value; return
		self._oleobj_.Invoke(*((10003, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((10001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	CenterPoint = property(_get_CenterPoint, None)
	'''
	The center point of circle

	:type: recurdyn.ProcessNet.IVector
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact Parameter

	:type: recurdyn.R2R2D.IR2R2DContactParameter
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	InnerContactPoints = property(_get_InnerContactPoints, _set_InnerContactPoints)
	'''
	The number of inner contat points

	:type: int
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	MotherBody = property(_get_MotherBody, _set_MotherBody)
	'''
	The mother body of guide

	:type: recurdyn.ProcessNet.IGeneric
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
	Radius = property(_get_Radius, None)
	'''
	The radius of circle

	:type: recurdyn.ProcessNet.IDouble
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_InnerContactPoints": _set_InnerContactPoints,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"CenterPoint": (10052, 2, (9, 0), (), "CenterPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (10002, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InnerContactPoints": (10003, 2, (19, 0), (), "InnerContactPoints", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (10001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (10051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"InnerContactPoints": ((10003, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((10001, LCID, 4, 0),()),
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

class IR2R2DGuideCollection(DispatchBaseClass):
	'''IR2R2DGuideCollection'''
	CLSID = IID('{2185E9C9-D7B1-4AE5-A0BE-A49CA236280A}')
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
		:rtype: recurdyn.R2R2D.IR2R2DGuide
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{11C08FE6-98DF-4121-8503-4691765A0DAB}')
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
		:rtype: recurdyn.R2R2D.IR2R2DGuide
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{11C08FE6-98DF-4121-8503-4691765A0DAB}')
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
		return win32com.client.util.Iterator(ob, '{11C08FE6-98DF-4121-8503-4691765A0DAB}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{11C08FE6-98DF-4121-8503-4691765A0DAB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IR2R2DGuideLinear(DispatchBaseClass):
	'''R2R2D linear guide'''
	CLSID = IID('{B245F42C-B731-48DE-BAD5-3D5D646C6A76}')
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


	def UpdateAllProperties(self):
		'''
		Update All Properties
		'''
		return self._oleobj_.InvokeTypes(10004, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_CircleEdgeRadius(self):
		return self._ApplyTypes_(*(10058, 2, (9, 0), (), "CircleEdgeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(10002, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'))
	def _get_ContactUpDirection(self):
		return self._ApplyTypes_(*(10053, 2, (11, 0), (), "ContactUpDirection", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_ImaginaryCircleEdgeEnd(self):
		return self._ApplyTypes_(*(10055, 2, (11, 0), (), "ImaginaryCircleEdgeEnd", None))
	def _get_ImaginaryCircleEdgeStart(self):
		return self._ApplyTypes_(*(10054, 2, (11, 0), (), "ImaginaryCircleEdgeStart", None))
	def _get_InnerContactPoints(self):
		return self._ApplyTypes_(*(10003, 2, (19, 0), (), "InnerContactPoints", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_SecondPoint(self):
		return self._ApplyTypes_(*(10052, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_SpecialCircleEdgeRadius(self):
		return self._ApplyTypes_(*(10057, 2, (9, 0), (), "SpecialCircleEdgeRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_StartPoint(self):
		return self._ApplyTypes_(*(10051, 2, (9, 0), (), "StartPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_UseSpecialCircleEdgeRadius(self):
		return self._ApplyTypes_(*(10056, 2, (11, 0), (), "UseSpecialCircleEdgeRadius", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ContactUpDirection(self, value):
		if "ContactUpDirection" in self.__dict__: self.__dict__["ContactUpDirection"] = value; return
		self._oleobj_.Invoke(*((10053, LCID, 4, 0) + (value,) + ()))
	def _set_ImaginaryCircleEdgeEnd(self, value):
		if "ImaginaryCircleEdgeEnd" in self.__dict__: self.__dict__["ImaginaryCircleEdgeEnd"] = value; return
		self._oleobj_.Invoke(*((10055, LCID, 4, 0) + (value,) + ()))
	def _set_ImaginaryCircleEdgeStart(self, value):
		if "ImaginaryCircleEdgeStart" in self.__dict__: self.__dict__["ImaginaryCircleEdgeStart"] = value; return
		self._oleobj_.Invoke(*((10054, LCID, 4, 0) + (value,) + ()))
	def _set_InnerContactPoints(self, value):
		if "InnerContactPoints" in self.__dict__: self.__dict__["InnerContactPoints"] = value; return
		self._oleobj_.Invoke(*((10003, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((10001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialCircleEdgeRadius(self, value):
		if "UseSpecialCircleEdgeRadius" in self.__dict__: self.__dict__["UseSpecialCircleEdgeRadius"] = value; return
		self._oleobj_.Invoke(*((10056, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	CircleEdgeRadius = property(_get_CircleEdgeRadius, None)
	'''
	The radius of imaginary circle edge

	:type: recurdyn.ProcessNet.IDouble
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact Parameter

	:type: recurdyn.R2R2D.IR2R2DContactParameter
	'''
	ContactUpDirection = property(_get_ContactUpDirection, _set_ContactUpDirection)
	'''
	True: upside, False: downside

	:type: bool
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	ImaginaryCircleEdgeEnd = property(_get_ImaginaryCircleEdgeEnd, _set_ImaginaryCircleEdgeEnd)
	'''
	End point of imaginary circle edge

	:type: bool
	'''
	ImaginaryCircleEdgeStart = property(_get_ImaginaryCircleEdgeStart, _set_ImaginaryCircleEdgeStart)
	'''
	Start point of imaginary circle edge

	:type: bool
	'''
	InnerContactPoints = property(_get_InnerContactPoints, _set_InnerContactPoints)
	'''
	The number of inner contat points

	:type: int
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	MotherBody = property(_get_MotherBody, _set_MotherBody)
	'''
	The mother body of guide

	:type: recurdyn.ProcessNet.IGeneric
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
	SecondPoint = property(_get_SecondPoint, None)
	'''
	The end point of line

	:type: recurdyn.ProcessNet.IVector
	'''
	SpecialCircleEdgeRadius = property(_get_SpecialCircleEdgeRadius, None)
	'''
	The special radius of imaginary circle edge

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	StartPoint = property(_get_StartPoint, None)
	'''
	The start point of line

	:type: recurdyn.ProcessNet.IVector
	'''
	UseSpecialCircleEdgeRadius = property(_get_UseSpecialCircleEdgeRadius, _set_UseSpecialCircleEdgeRadius)
	'''
	Use special radius of imaginary circle edge

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_ContactUpDirection": _set_ContactUpDirection,
		"_set_ImaginaryCircleEdgeEnd": _set_ImaginaryCircleEdgeEnd,
		"_set_ImaginaryCircleEdgeStart": _set_ImaginaryCircleEdgeStart,
		"_set_InnerContactPoints": _set_InnerContactPoints,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_UseSpecialCircleEdgeRadius": _set_UseSpecialCircleEdgeRadius,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"CircleEdgeRadius": (10058, 2, (9, 0), (), "CircleEdgeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (10002, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'),
		"ContactUpDirection": (10053, 2, (11, 0), (), "ContactUpDirection", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"ImaginaryCircleEdgeEnd": (10055, 2, (11, 0), (), "ImaginaryCircleEdgeEnd", None),
		"ImaginaryCircleEdgeStart": (10054, 2, (11, 0), (), "ImaginaryCircleEdgeStart", None),
		"InnerContactPoints": (10003, 2, (19, 0), (), "InnerContactPoints", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (10001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SecondPoint": (10052, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"SpecialCircleEdgeRadius": (10057, 2, (9, 0), (), "SpecialCircleEdgeRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"StartPoint": (10051, 2, (9, 0), (), "StartPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"UseSpecialCircleEdgeRadius": (10056, 2, (11, 0), (), "UseSpecialCircleEdgeRadius", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ContactUpDirection": ((10053, LCID, 4, 0),()),
		"ImaginaryCircleEdgeEnd": ((10055, LCID, 4, 0),()),
		"ImaginaryCircleEdgeStart": ((10054, LCID, 4, 0),()),
		"InnerContactPoints": ((10003, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((10001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialCircleEdgeRadius": ((10056, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DLoadConcentratedUSUB(DispatchBaseClass):
	'''R2R2D Load Concentrated USUB'''
	CLSID = IID('{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}')
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
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(10003, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeSet(self):
		return self._ApplyTypes_(*(10001, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ReportNodeIDs(self):
		return self._ApplyTypes_(*(10006, 2, (8195, 0), (), "ReportNodeIDs", None))
	def _get_UseReportNodes(self):
		return self._ApplyTypes_(*(10005, 2, (11, 0), (), "UseReportNodes", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_UserSubroutine(self):
		return self._ApplyTypes_(*(10002, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((10003, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NodeSet(self, value):
		if "NodeSet" in self.__dict__: self.__dict__["NodeSet"] = value; return
		self._oleobj_.Invoke(*((10001, LCID, 4, 0) + (value,) + ()))
	def _set_ReportNodeIDs(self, value):
		if "ReportNodeIDs" in self.__dict__: self.__dict__["ReportNodeIDs"] = value; return
		variantValue = win32com.client.VARIANT(8195, value)
		self._oleobj_.Invoke(*((10006, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseReportNodes(self, value):
		if "UseReportNodes" in self.__dict__: self.__dict__["UseReportNodes"] = value; return
		self._oleobj_.Invoke(*((10005, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_UserSubroutine(self, value):
		if "UserSubroutine" in self.__dict__: self.__dict__["UserSubroutine"] = value; return
		self._oleobj_.Invoke(*((10002, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseBody = property(_get_BaseBody, _set_BaseBody)
	'''
	Base Body

	:type: recurdyn.ProcessNet.IBody
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
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NodeSet = property(_get_NodeSet, _set_NodeSet)
	'''
	Node set

	:type: recurdyn.ProcessNet.IGeneric
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
	ReportNodeIDs = property(_get_ReportNodeIDs, _set_ReportNodeIDs)
	'''
	Report node IDs

	:type: list[int]
	'''
	UseReportNodes = property(_get_UseReportNodes, _set_UseReportNodes)
	'''
	Use report nNodes

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	UserSubroutine = property(_get_UserSubroutine, _set_UserSubroutine)
	'''
	User subroutine

	:type: recurdyn.ProcessNet.IUserSubroutine
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_BaseBody": _set_BaseBody,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_NodeSet": _set_NodeSet,
		"_set_ReportNodeIDs": _set_ReportNodeIDs,
		"_set_UseReportNodes": _set_UseReportNodes,
		"_set_UserData": _set_UserData,
		"_set_UserSubroutine": _set_UserSubroutine,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (10003, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeSet": (10001, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ReportNodeIDs": (10006, 2, (8195, 0), (), "ReportNodeIDs", None),
		"UseReportNodes": (10005, 2, (11, 0), (), "UseReportNodes", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"UserSubroutine": (10002, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((10003, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NodeSet": ((10001, LCID, 4, 0),()),
		"ReportNodeIDs": ((10006, LCID, 4, 0),()),
		"UseReportNodes": ((10005, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"UserSubroutine": ((10002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DMaterialPropertyBeam(DispatchBaseClass):
	'''R2R2D Beam material property'''
	CLSID = IID('{7474063C-637A-4F9E-ABC0-11F074027153}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def UpdateProperties(self):
		'''
		Update Properties
		'''
		return self._oleobj_.InvokeTypes(10115, LCID, 1, (24, 0), (),)


	def UpdateShearModulus(self):
		'''
		Update Shear Modulus
		'''
		return self._oleobj_.InvokeTypes(10114, LCID, 1, (24, 0), (),)


	def _get_Asy(self):
		return self._ApplyTypes_(*(10116, 2, (5, 0), (), "Asy", None))
	def _get_Asz(self):
		return self._ApplyTypes_(*(10117, 2, (5, 0), (), "Asz", None))
	def _get_CZ(self):
		return self._ApplyTypes_(*(10111, 2, (5, 0), (), "CZ", None))
	def _get_CrossSectionArea(self):
		return self._ApplyTypes_(*(10110, 2, (9, 0), (), "CrossSectionArea", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(10103, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(10101, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FZ(self):
		return self._ApplyTypes_(*(10112, 2, (5, 0), (), "FZ", None))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10107, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10108, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10109, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MassType(self):
		return self._ApplyTypes_(*(10100, 2, (3, 0), (), "MassType", '{89A46801-0658-4972-88F2-E8C0F422D1F4}'))
	def _get_PoissonsRatio(self):
		return self._ApplyTypes_(*(10106, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearModulus(self):
		return self._ApplyTypes_(*(10105, 2, (5, 0), (), "ShearModulus", None))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(10102, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UpdateCrossSectionPropertyAutomaticallyFlag(self):
		return self._ApplyTypes_(*(10113, 2, (11, 0), (), "UpdateCrossSectionPropertyAutomaticallyFlag", None))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(10104, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Asy(self, value):
		if "Asy" in self.__dict__: self.__dict__["Asy"] = value; return
		self._oleobj_.Invoke(*((10116, LCID, 4, 0) + (value,) + ()))
	def _set_Asz(self, value):
		if "Asz" in self.__dict__: self.__dict__["Asz"] = value; return
		self._oleobj_.Invoke(*((10117, LCID, 4, 0) + (value,) + ()))
	def _set_CZ(self, value):
		if "CZ" in self.__dict__: self.__dict__["CZ"] = value; return
		self._oleobj_.Invoke(*((10111, LCID, 4, 0) + (value,) + ()))
	def _set_FZ(self, value):
		if "FZ" in self.__dict__: self.__dict__["FZ"] = value; return
		self._oleobj_.Invoke(*((10112, LCID, 4, 0) + (value,) + ()))
	def _set_MassType(self, value):
		if "MassType" in self.__dict__: self.__dict__["MassType"] = value; return
		self._oleobj_.Invoke(*((10100, LCID, 4, 0) + (value,) + ()))
	def _set_UpdateCrossSectionPropertyAutomaticallyFlag(self, value):
		if "UpdateCrossSectionPropertyAutomaticallyFlag" in self.__dict__: self.__dict__["UpdateCrossSectionPropertyAutomaticallyFlag"] = value; return
		self._oleobj_.Invoke(*((10113, LCID, 4, 0) + (value,) + ()))

	Asy = property(_get_Asy, _set_Asy)
	'''
	Shear Area Factor Asy

	:type: float
	'''
	Asz = property(_get_Asz, _set_Asz)
	'''
	Shear Area Factor Asz

	:type: float
	'''
	CZ = property(_get_CZ, _set_CZ)
	'''
	Stress Recovery Points CY, DY

	:type: float
	'''
	CrossSectionArea = property(_get_CrossSectionArea, None)
	'''
	Cross section area

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingRatio = property(_get_DampingRatio, None)
	'''
	Damping ratio

	:type: recurdyn.ProcessNet.IDouble
	'''
	Density = property(_get_Density, None)
	'''
	Density

	:type: recurdyn.ProcessNet.IDouble
	'''
	FZ = property(_get_FZ, _set_FZ)
	'''
	Stress Recovery Points EY, FY

	:type: float
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Moment of area, Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Moment of area, Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Moment of area, Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	MassType = property(_get_MassType, _set_MassType)
	'''
	MassType

	:type: recurdyn.R2R2D.R2R2DMassType
	'''
	PoissonsRatio = property(_get_PoissonsRatio, None)
	'''
	Poisson's ratio

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearModulus = property(_get_ShearModulus, None)
	'''
	Shere Modulus

	:type: float
	'''
	TotalMass = property(_get_TotalMass, None)
	'''
	Totoal mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	UpdateCrossSectionPropertyAutomaticallyFlag = property(_get_UpdateCrossSectionPropertyAutomaticallyFlag, _set_UpdateCrossSectionPropertyAutomaticallyFlag)
	'''
	Update Cross Section Property Automatically Flag

	:type: bool
	'''
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	Young's Modulus

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Asy": _set_Asy,
		"_set_Asz": _set_Asz,
		"_set_CZ": _set_CZ,
		"_set_FZ": _set_FZ,
		"_set_MassType": _set_MassType,
		"_set_UpdateCrossSectionPropertyAutomaticallyFlag": _set_UpdateCrossSectionPropertyAutomaticallyFlag,
	}
	_prop_map_get_ = {
		"Asy": (10116, 2, (5, 0), (), "Asy", None),
		"Asz": (10117, 2, (5, 0), (), "Asz", None),
		"CZ": (10111, 2, (5, 0), (), "CZ", None),
		"CrossSectionArea": (10110, 2, (9, 0), (), "CrossSectionArea", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingRatio": (10103, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (10101, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FZ": (10112, 2, (5, 0), (), "FZ", None),
		"Ixx": (10107, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10108, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10109, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MassType": (10100, 2, (3, 0), (), "MassType", '{89A46801-0658-4972-88F2-E8C0F422D1F4}'),
		"PoissonsRatio": (10106, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearModulus": (10105, 2, (5, 0), (), "ShearModulus", None),
		"TotalMass": (10102, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UpdateCrossSectionPropertyAutomaticallyFlag": (10113, 2, (11, 0), (), "UpdateCrossSectionPropertyAutomaticallyFlag", None),
		"YoungsModulus": (10104, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Asy": ((10116, LCID, 4, 0),()),
		"Asz": ((10117, LCID, 4, 0),()),
		"CZ": ((10111, LCID, 4, 0),()),
		"FZ": ((10112, LCID, 4, 0),()),
		"MassType": ((10100, LCID, 4, 0),()),
		"UpdateCrossSectionPropertyAutomaticallyFlag": ((10113, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DPassingBodyCollection(DispatchBaseClass):
	'''IR2R2DPassingBodyCollection'''
	CLSID = IID('{E5EED844-E317-49B8-B8F8-42DF2D16E4EC}')
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
		:rtype: recurdyn.ProcessNet.IGeneric
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{27A86788-8B85-40CF-BE7F-BA915103A7DB}')
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
		:rtype: recurdyn.ProcessNet.IGeneric
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{27A86788-8B85-40CF-BE7F-BA915103A7DB}')
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
		return win32com.client.util.Iterator(ob, '{27A86788-8B85-40CF-BE7F-BA915103A7DB}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IR2R2DSelfContact(DispatchBaseClass):
	'''R2R2D self contact'''
	CLSID = IID('{9AC66E9B-1D93-434B-BCD2-1F54446A3687}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(10108, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'))
	def _get_UnWinderConectedNodeType(self):
		return self._ApplyTypes_(*(10106, 2, (3, 0), (), "UnWinderConectedNodeType", '{71275134-C835-44E2-84F2-E9A37A5B6ADD}'))
	def _get_UnWinderRoller(self):
		return self._ApplyTypes_(*(10105, 2, (9, 0), (), "UnWinderRoller", '{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}'))
	def _get_UnWinderSearchBoundaryFactor(self):
		return self._ApplyTypes_(*(10107, 2, (9, 0), (), "UnWinderSearchBoundaryFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseUnWinder(self):
		return self._ApplyTypes_(*(10104, 2, (11, 0), (), "UseUnWinder", None))
	def _get_UseWinder(self):
		return self._ApplyTypes_(*(10100, 2, (11, 0), (), "UseWinder", None))
	def _get_WinderConectedNodeType(self):
		return self._ApplyTypes_(*(10102, 2, (3, 0), (), "WinderConectedNodeType", '{71275134-C835-44E2-84F2-E9A37A5B6ADD}'))
	def _get_WinderRoller(self):
		return self._ApplyTypes_(*(10101, 2, (9, 0), (), "WinderRoller", '{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}'))
	def _get_WinderSearchBoundaryFactor(self):
		return self._ApplyTypes_(*(10103, 2, (9, 0), (), "WinderSearchBoundaryFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_UnWinderConectedNodeType(self, value):
		if "UnWinderConectedNodeType" in self.__dict__: self.__dict__["UnWinderConectedNodeType"] = value; return
		self._oleobj_.Invoke(*((10106, LCID, 4, 0) + (value,) + ()))
	def _set_UnWinderRoller(self, value):
		if "UnWinderRoller" in self.__dict__: self.__dict__["UnWinderRoller"] = value; return
		self._oleobj_.Invoke(*((10105, LCID, 4, 0) + (value,) + ()))
	def _set_UseUnWinder(self, value):
		if "UseUnWinder" in self.__dict__: self.__dict__["UseUnWinder"] = value; return
		self._oleobj_.Invoke(*((10104, LCID, 4, 0) + (value,) + ()))
	def _set_UseWinder(self, value):
		if "UseWinder" in self.__dict__: self.__dict__["UseWinder"] = value; return
		self._oleobj_.Invoke(*((10100, LCID, 4, 0) + (value,) + ()))
	def _set_WinderConectedNodeType(self, value):
		if "WinderConectedNodeType" in self.__dict__: self.__dict__["WinderConectedNodeType"] = value; return
		self._oleobj_.Invoke(*((10102, LCID, 4, 0) + (value,) + ()))
	def _set_WinderRoller(self, value):
		if "WinderRoller" in self.__dict__: self.__dict__["WinderRoller"] = value; return
		self._oleobj_.Invoke(*((10101, LCID, 4, 0) + (value,) + ()))

	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact Parameter

	:type: recurdyn.R2R2D.IR2R2DContactParameter
	'''
	UnWinderConectedNodeType = property(_get_UnWinderConectedNodeType, _set_UnWinderConectedNodeType)
	'''
	UnWinder conected node type

	:type: recurdyn.R2R2D.R2R2DWinderConectedNodeType
	'''
	UnWinderRoller = property(_get_UnWinderRoller, _set_UnWinderRoller)
	'''
	UnWinder roller

	:type: recurdyn.R2R2D.IR2R2DBodyRoller
	'''
	UnWinderSearchBoundaryFactor = property(_get_UnWinderSearchBoundaryFactor, None)
	'''
	UnWinder search boundary factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseUnWinder = property(_get_UseUnWinder, _set_UseUnWinder)
	'''
	Use unwinder

	:type: bool
	'''
	UseWinder = property(_get_UseWinder, _set_UseWinder)
	'''
	Use winder

	:type: bool
	'''
	WinderConectedNodeType = property(_get_WinderConectedNodeType, _set_WinderConectedNodeType)
	'''
	Winder conected node type

	:type: recurdyn.R2R2D.R2R2DWinderConectedNodeType
	'''
	WinderRoller = property(_get_WinderRoller, _set_WinderRoller)
	'''
	Winder roller

	:type: recurdyn.R2R2D.IR2R2DBodyRoller
	'''
	WinderSearchBoundaryFactor = property(_get_WinderSearchBoundaryFactor, None)
	'''
	Winder search boundary factor

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_UnWinderConectedNodeType": _set_UnWinderConectedNodeType,
		"_set_UnWinderRoller": _set_UnWinderRoller,
		"_set_UseUnWinder": _set_UseUnWinder,
		"_set_UseWinder": _set_UseWinder,
		"_set_WinderConectedNodeType": _set_WinderConectedNodeType,
		"_set_WinderRoller": _set_WinderRoller,
	}
	_prop_map_get_ = {
		"ContactParameter": (10108, 2, (9, 0), (), "ContactParameter", '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}'),
		"UnWinderConectedNodeType": (10106, 2, (3, 0), (), "UnWinderConectedNodeType", '{71275134-C835-44E2-84F2-E9A37A5B6ADD}'),
		"UnWinderRoller": (10105, 2, (9, 0), (), "UnWinderRoller", '{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}'),
		"UnWinderSearchBoundaryFactor": (10107, 2, (9, 0), (), "UnWinderSearchBoundaryFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseUnWinder": (10104, 2, (11, 0), (), "UseUnWinder", None),
		"UseWinder": (10100, 2, (11, 0), (), "UseWinder", None),
		"WinderConectedNodeType": (10102, 2, (3, 0), (), "WinderConectedNodeType", '{71275134-C835-44E2-84F2-E9A37A5B6ADD}'),
		"WinderRoller": (10101, 2, (9, 0), (), "WinderRoller", '{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}'),
		"WinderSearchBoundaryFactor": (10103, 2, (9, 0), (), "WinderSearchBoundaryFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"UnWinderConectedNodeType": ((10106, LCID, 4, 0),()),
		"UnWinderRoller": ((10105, LCID, 4, 0),()),
		"UseUnWinder": ((10104, LCID, 4, 0),()),
		"UseWinder": ((10100, LCID, 4, 0),()),
		"WinderConectedNodeType": ((10102, LCID, 4, 0),()),
		"WinderRoller": ((10101, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IR2R2DSubSystem(DispatchBaseClass):
	'''R2R2D subsystem'''
	CLSID = IID('{08ABAC6E-D10A-486E-B921-52DAFE7D7A45}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateBodyBeam(self, strName, pBodyList, pInOutList, uiNumberOfElements, Thickness):
		'''
		CreateBodyBeam is obsoleted. Use CreateBodyBeam2
		
		:param strName: str
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfElements: int
		:param Thickness: float
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10010, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (19, 1), (5, 1)),strName
			, pBodyList, pInOutList, uiNumberOfElements, Thickness)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeam', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
		return ret

	def CreateBodyBeam2(self, strName, pBodyList, pInOutList, uiNumberOfElements):
		'''
		Create a beam assembly
		
		:param strName: str
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfElements: int
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10037, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (19, 1)),strName
			, pBodyList, pInOutList, uiNumberOfElements)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeam2', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
		return ret

	def CreateBodyBeamWithOpenLoop(self, strName, pBodyList, pInOutList, pStartDir, pStartOrthoDir, pEndDir, uiNumberOfElements, Thickness):
		'''
		CreateBodyBeamWithOpenLoop is obsoleted. Use CreateBodyBeamWithOpenLoop2
		
		:param strName: str
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param pStartDir: list[float]
		:param pStartOrthoDir: list[float]
		:param pEndDir: list[float]
		:param uiNumberOfElements: int
		:param Thickness: float
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10011, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (8197, 1), (8197, 1), (8197, 1), (19, 1), (5, 1)),strName
			, pBodyList, pInOutList, pStartDir, pStartOrthoDir, pEndDir
			, uiNumberOfElements, Thickness)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeamWithOpenLoop', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
		return ret

	def CreateBodyBeamWithOpenLoop2(self, strName, pBodyList, pInOutList, pStartDir, pStartOrthoDir, pEndDir, uiNumberOfElements):
		'''
		Create a beam assembly using open-loop
		
		:param strName: str
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param pStartDir: list[float]
		:param pStartOrthoDir: list[float]
		:param pEndDir: list[float]
		:param uiNumberOfElements: int
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10038, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (8197, 1), (8197, 1), (8197, 1), (19, 1)),strName
			, pBodyList, pInOutList, pStartDir, pStartOrthoDir, pEndDir
			, uiNumberOfElements)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeamWithOpenLoop2', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
		return ret

	def CreateBodyBeamWithPreWinding(self, strName, pBodyList, pInOutList, pStartDir, pStartOrthoDir, uiNumberOfElements, Thickness, uiNumberOfStartWindings, uiNumberOfEndWindings, offsetFactor):
		'''
		CreateBodyBeamWithPreWinding is obsoleted. Use CreateBodyBeamWithPreWinding3
		
		:param strName: str
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param pStartDir: list[float]
		:param pStartOrthoDir: list[float]
		:param uiNumberOfElements: int
		:param Thickness: float
		:param uiNumberOfStartWindings: int
		:param uiNumberOfEndWindings: int
		:param offsetFactor: float
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10012, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (8197, 1), (8197, 1), (19, 1), (5, 1), (19, 1), (19, 1), (5, 1)),strName
			, pBodyList, pInOutList, pStartDir, pStartOrthoDir, uiNumberOfElements
			, Thickness, uiNumberOfStartWindings, uiNumberOfEndWindings, offsetFactor)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeamWithPreWinding', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
		return ret

	def CreateBodyBeamWithPreWinding2(self, strName, pBodyList, pInOutList, pStartDir, pStartOrthoDir, uiNumberOfElements, Thickness, startThicknessflag, endThicknessflag, uiNumberOfStartWindings, uiNumberOfEndWindings, offsetFactor):
		'''
		CreateBodyBeamWithPreWinding2 is obsoleted. Use CreateBodyBeamWithPreWinding4
		
		:param strName: str
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param pStartDir: list[float]
		:param pStartOrthoDir: list[float]
		:param uiNumberOfElements: int
		:param Thickness: float
		:param startThicknessflag: bool
		:param endThicknessflag: bool
		:param uiNumberOfStartWindings: int
		:param uiNumberOfEndWindings: int
		:param offsetFactor: float
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10036, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (8197, 1), (8197, 1), (19, 1), (5, 1), (11, 1), (11, 1), (19, 1), (19, 1), (5, 1)),strName
			, pBodyList, pInOutList, pStartDir, pStartOrthoDir, uiNumberOfElements
			, Thickness, startThicknessflag, endThicknessflag, uiNumberOfStartWindings, uiNumberOfEndWindings
			, offsetFactor)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeamWithPreWinding2', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
		return ret

	def CreateBodyBeamWithPreWinding3(self, strName, pBodyList, pInOutList, pStartDir, pStartOrthoDir, uiNumberOfElements, uiNumberOfStartWindings, uiNumberOfEndWindings, offsetFactor):
		'''
		Create a beam assembly using pre-winding
		
		:param strName: str
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param pStartDir: list[float]
		:param pStartOrthoDir: list[float]
		:param uiNumberOfElements: int
		:param uiNumberOfStartWindings: int
		:param uiNumberOfEndWindings: int
		:param offsetFactor: float
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10039, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (8197, 1), (8197, 1), (19, 1), (19, 1), (19, 1), (5, 1)),strName
			, pBodyList, pInOutList, pStartDir, pStartOrthoDir, uiNumberOfElements
			, uiNumberOfStartWindings, uiNumberOfEndWindings, offsetFactor)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeamWithPreWinding3', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
		return ret

	def CreateBodyBeamWithPreWinding4(self, strName, pBodyList, pInOutList, pStartDir, pStartOrthoDir, uiNumberOfElements, startThicknessflag, endThicknessflag, uiNumberOfStartWindings, uiNumberOfEndWindings, offsetFactor):
		'''
		Create a beam assembly using pre-winding with option
		
		:param strName: str
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param pStartDir: list[float]
		:param pStartOrthoDir: list[float]
		:param uiNumberOfElements: int
		:param startThicknessflag: bool
		:param endThicknessflag: bool
		:param uiNumberOfStartWindings: int
		:param uiNumberOfEndWindings: int
		:param offsetFactor: float
		:rtype: recurdyn.R2R2D.IR2R2DBodyBeam
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10040, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (8197, 1), (8197, 1), (19, 1), (11, 1), (11, 1), (19, 1), (19, 1), (5, 1)),strName
			, pBodyList, pInOutList, pStartDir, pStartOrthoDir, uiNumberOfElements
			, startThicknessflag, endThicknessflag, uiNumberOfStartWindings, uiNumberOfEndWindings, offsetFactor
			)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeamWithPreWinding4', '{FF337086-F852-42E3-BF88-2795D0BBCB31}')
		return ret

	def CreateBodyRollerCircle(self, strName, pPoint):
		'''
		Create a circle roller body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.R2R2D.IR2R2DBodyRollerCircle
		'''
		ret = self._oleobj_.InvokeTypes(10001, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyRollerCircle', '{33938809-28E5-4D14-B044-B074F7C7645B}')
		return ret

	def CreateBodyRollerGeneral(self, strName, pPoint):
		'''
		Create a general roller body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.R2R2D.IR2R2DBodyRollerGeneral
		'''
		ret = self._oleobj_.InvokeTypes(10002, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyRollerGeneral', '{E60EA1F3-9C5B-4411-9C9E-715C89C5F2D5}')
		return ret

	def CreateContactWorkpieceToWorkpiece(self, strName, pBaseBeamAssembly, pActionBeamAssembly):
		'''
		Creates a workpiece to workpiece contact
		
		:param strName: str
		:param pBaseBeamAssembly: IR2R2DBodyBeam
		:param pActionBeamAssembly: IR2R2DBodyBeam
		:rtype: recurdyn.R2R2D.IR2R2DContactWorkpieceToWorkpiece
		'''
		ret = self._oleobj_.InvokeTypes(10017, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pBaseBeamAssembly, pActionBeamAssembly)
		if ret is not None:
			ret = Dispatch(ret, 'CreateContactWorkpieceToWorkpiece', '{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}')
		return ret

	def CreateForceConcentratedLoadUSUB(self, strName, pNodeSet, pUsub):
		'''
		Creates a Concentrated LoadU SUB
		
		:param strName: str
		:param pNodeSet: IGeneric
		:param pUsub: IUserSubroutine
		:rtype: recurdyn.R2R2D.IR2R2DLoadConcentratedUSUB
		'''
		ret = self._oleobj_.InvokeTypes(10018, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pNodeSet, pUsub)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConcentratedLoadUSUB', '{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}')
		return ret

	def CreateGuideArc(self, strName, pFirstPoint, pSecondPoint, dAngle):
		'''
		Creates an arc guide
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param dAngle: float
		:rtype: recurdyn.R2R2D.IR2R2DGuideArc
		'''
		ret = self._oleobj_.InvokeTypes(10003, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1)),strName
			, pFirstPoint, pSecondPoint, dAngle)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideArc', '{6213B8B2-5B65-4259-8783-30AF5BAE2F10}')
		return ret

	def CreateGuideArcWithEndPoint(self, strName, pCenterPoint, pStartPoint, pEndPoint, bDirection):
		'''
		Creates an arc guide with end point
		
		:param strName: str
		:param pCenterPoint: list[float]
		:param pStartPoint: list[float]
		:param pEndPoint: list[float]
		:param bDirection: bool
		:rtype: recurdyn.R2R2D.IR2R2DGuideArc
		'''
		ret = self._oleobj_.InvokeTypes(10004, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (8197, 1), (11, 1)),strName
			, pCenterPoint, pStartPoint, pEndPoint, bDirection)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideArcWithEndPoint', '{6213B8B2-5B65-4259-8783-30AF5BAE2F10}')
		return ret

	def CreateGuideArcWithThreePoints(self, strName, pThreePoint):
		'''
		Creates an arc guide with three points
		
		:param strName: str
		:param pThreePoint: list[object]
		:rtype: recurdyn.R2R2D.IR2R2DGuideArc
		'''
		_pThreePoint_type = True if pThreePoint and isinstance(pThreePoint[0], win32com.client.VARIANT) else False
		if not _pThreePoint_type:
			pThreePoint = [win32com.client.VARIANT(12, _data) for _data in pThreePoint]

		ret = self._oleobj_.InvokeTypes(10005, LCID, 1, (9, 0), ((8, 1), (8204, 1)),strName
			, pThreePoint)

		if not _pThreePoint_type:
			pThreePoint = [_data.value for _data in pThreePoint]

		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideArcWithThreePoints', '{6213B8B2-5B65-4259-8783-30AF5BAE2F10}')
		return ret

	def CreateGuideCircle(self, strName, pFirstPoint, dRadius):
		'''
		Creates a circle guide
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param dRadius: float
		:rtype: recurdyn.R2R2D.IR2R2DGuideCircle
		'''
		ret = self._oleobj_.InvokeTypes(10007, LCID, 1, (9, 0), ((8, 1), (8197, 1), (5, 1)),strName
			, pFirstPoint, dRadius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideCircle', '{A5D8C80B-2C7A-4C35-9393-7ADBB640A5F6}')
		return ret

	def CreateGuideCircleWithThreePoints(self, strName, pThreePoint):
		'''
		Creates a circle guide with three points
		
		:param strName: str
		:param pThreePoint: list[object]
		:rtype: recurdyn.R2R2D.IR2R2DGuideCircle
		'''
		_pThreePoint_type = True if pThreePoint and isinstance(pThreePoint[0], win32com.client.VARIANT) else False
		if not _pThreePoint_type:
			pThreePoint = [win32com.client.VARIANT(12, _data) for _data in pThreePoint]

		ret = self._oleobj_.InvokeTypes(10008, LCID, 1, (9, 0), ((8, 1), (8204, 1)),strName
			, pThreePoint)

		if not _pThreePoint_type:
			pThreePoint = [_data.value for _data in pThreePoint]

		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideCircleWithThreePoints', '{A5D8C80B-2C7A-4C35-9393-7ADBB640A5F6}')
		return ret

	def CreateGuideLinear(self, strName, pFirstPoint, pSecondPoint):
		'''
		Creates a linear guide
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:rtype: recurdyn.R2R2D.IR2R2DGuideLinear
		'''
		ret = self._oleobj_.InvokeTypes(10006, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1)),strName
			, pFirstPoint, pSecondPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideLinear', '{B245F42C-B731-48DE-BAD5-3D5D646C6A76}')
		return ret

	def CreateSensorDistance(self, strName, pPosition, pDirection, pEntity, dRange):
		'''
		Create a distance sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pDirection: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorDistance
		'''
		ret = self._oleobj_.InvokeTypes(10014, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pDirection, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorDistance', '{0CC3861B-CC2A-4402-9135-C8BC804EABBD}')
		return ret

	def CreateSensorSlip(self, strName, pPosition, pSlipEntity, pEntity, dRange):
		'''
		Create a slip sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pSlipEntity: IGeneric
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorSlip
		'''
		ret = self._oleobj_.InvokeTypes(10015, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1), (9, 1), (5, 1)),strName
			, pPosition, pSlipEntity, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorSlip', '{08675B12-6A90-4082-BAED-E54382FDF107}')
		return ret

	def CreateSensorSpeed(self, strName, pPosition, pDirection, pEntity, dRange):
		'''
		Create a speed sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pDirection: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorSpeed
		'''
		ret = self._oleobj_.InvokeTypes(10013, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pDirection, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorSpeed', '{CCB7E742-F0DF-4F22-A377-04AA675FD281}')
		return ret

	def CreateSensorTension(self, strName, pPosition, pEntity, dRange):
		'''
		Create a tension sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorTension
		'''
		ret = self._oleobj_.InvokeTypes(10016, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorTension', '{55C49622-A503-4651-BF1E-2A84CD9E27AB}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def GuideConvertWithColor(self, pMultiBodies, oleColor):
		'''
		Converts guides with color
		
		:param pMultiBodies: list[object]
		:param oleColor: int
		:rtype: bool
		'''
		_pMultiBodies_type = True if pMultiBodies and isinstance(pMultiBodies[0], win32com.client.VARIANT) else False
		if not _pMultiBodies_type:
			pMultiBodies = [win32com.client.VARIANT(12, _data) for _data in pMultiBodies]

		ret = self._oleobj_.InvokeTypes(10009, LCID, 1, (11, 0), ((8204, 1), (19, 1)),pMultiBodies
			, oleColor)

		if not _pMultiBodies_type:
			pMultiBodies = [_data.value for _data in pMultiBodies]

		return ret


	def _get_BodyBeamCollection(self):
		return self._ApplyTypes_(*(10030, 2, (9, 0), (), "BodyBeamCollection", '{D51B4A60-30FE-4A2C-89CE-6DE904CD7771}'))
	def _get_BodyCollection(self):
		return self._ApplyTypes_(*(10031, 2, (9, 0), (), "BodyCollection", '{F66AB8D5-E20C-437F-BD61-982CCD09B711}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ConcentratedLoadUSUBCollection(self):
		return self._ApplyTypes_(*(10035, 2, (9, 0), (), "ConcentratedLoadUSUBCollection", '{4EEF5BEB-2CCF-4BD9-8159-CF6A337F2581}'))
	def _get_ContacttWorkpieceToWorkpieceCollection(self):
		return self._ApplyTypes_(*(10033, 2, (9, 0), (), "ContacttWorkpieceToWorkpieceCollection", '{3AC2E0DA-1DEA-4818-B371-A35C8E858CAE}'))
	def _get_Contour(self):
		return self._ApplyTypes_(*(10034, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(10000, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_GuideCollection(self):
		return self._ApplyTypes_(*(10032, 2, (9, 0), (), "GuideCollection", '{2185E9C9-D7B1-4AE5-A0BE-A49CA236280A}'))
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

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BodyBeamCollection = property(_get_BodyBeamCollection, None)
	'''
	Get the collection of beam assembly

	:type: recurdyn.R2R2D.IR2R2DBodyBeamCollection
	'''
	BodyCollection = property(_get_BodyCollection, None)
	'''
	Get the collection of roller body

	:type: recurdyn.R2R2D.IR2R2DBodyCollection
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ConcentratedLoadUSUBCollection = property(_get_ConcentratedLoadUSUBCollection, None)
	'''
	Get the collection of Concentrated LoadU SUB

	:type: recurdyn.R2R2D.IR2R2DConcentratedLoadUSUBCollection
	'''
	ContacttWorkpieceToWorkpieceCollection = property(_get_ContacttWorkpieceToWorkpieceCollection, None)
	'''
	Get the collection of workpiece to workpiece contact

	:type: recurdyn.R2R2D.IR2R2DContactWorkpieceToWorkpieceCollection
	'''
	Contour = property(_get_Contour, None)
	'''
	Get contour

	:type: recurdyn.Flexible.IContour
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralSubSystem = property(_get_GeneralSubSystem, None)
	'''
	General subsystem

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	GuideCollection = property(_get_GuideCollection, None)
	'''
	Get the collection of guide

	:type: recurdyn.R2R2D.IR2R2DGuideCollection
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
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BodyBeamCollection": (10030, 2, (9, 0), (), "BodyBeamCollection", '{D51B4A60-30FE-4A2C-89CE-6DE904CD7771}'),
		"BodyCollection": (10031, 2, (9, 0), (), "BodyCollection", '{F66AB8D5-E20C-437F-BD61-982CCD09B711}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConcentratedLoadUSUBCollection": (10035, 2, (9, 0), (), "ConcentratedLoadUSUBCollection", '{4EEF5BEB-2CCF-4BD9-8159-CF6A337F2581}'),
		"ContacttWorkpieceToWorkpieceCollection": (10033, 2, (9, 0), (), "ContacttWorkpieceToWorkpieceCollection", '{3AC2E0DA-1DEA-4818-B371-A35C8E858CAE}'),
		"Contour": (10034, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralSubSystem": (10000, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"GuideCollection": (10032, 2, (9, 0), (), "GuideCollection", '{2185E9C9-D7B1-4AE5-A0BE-A49CA236280A}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
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

IR2R2DBody_vtables_dispatch_ = 1
IR2R2DBody_vtables_ = [
	(( 'GeneralBody' , 'ppVal' , ), 10001, (10001, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IR2R2DBodyBeam_vtables_dispatch_ = 1
IR2R2DBodyBeam_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10051, (10051, (), [ (16393, 10, None, "IID('{22E7FECE-90EC-4649-A335-CD1139004817}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MaterialProperty' , 'ppVal' , ), 10052, (10052, (), [ (16393, 10, None, "IID('{7474063C-637A-4F9E-ABC0-11F074027153}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PassingBodyCollection' , 'ppVal' , ), 10053, (10053, (), [ (16393, 10, None, "IID('{E5EED844-E317-49B8-B8F8-42DF2D16E4EC}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody' , 'pVal' , ), 10054, (10054, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody' , 'pVal' , ), 10055, (10055, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UseSelfContact' , 'pVal' , ), 10056, (10056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseSelfContact' , 'pVal' , ), 10056, (10056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SelfContact' , 'ppVal' , ), 10057, (10057, (), [ (16393, 10, None, "IID('{9AC66E9B-1D93-434B-BCD2-1F54446A3687}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialLongitudinalVelocity' , 'pVal' , ), 10058, (10058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialLongitudinalVelocity' , 'pVal' , ), 10058, (10058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'InitialLongitudinalVelocity' , 'ppVal' , ), 10059, (10059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseAirResistance' , 'pVal' , ), 10060, (10060, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseAirResistance' , 'pVal' , ), 10060, (10060, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceType' , 'pVal' , ), 10061, (10061, (), [ (16387, 10, None, "IID('{7728E324-B286-4061-8A1C-2B2559F79CB4}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceType' , 'pVal' , ), 10061, (10061, (), [ (3, 1, None, "IID('{7728E324-B286-4061-8A1C-2B2559F79CB4}')") , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceConstant' , 'ppVal' , ), 10062, (10062, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceExpression' , 'ppVal' , ), 10063, (10063, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceExpression' , 'ppVal' , ), 10063, (10063, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryAutomatically' , 'pVal' , ), 10064, (10064, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryAutomatically' , 'pVal' , ), 10064, (10064, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ConnectingParameters' , 'ppConnectingParameters' , ), 10065, (10065, (), [ (16393, 10, None, "IID('{21DDE70D-AD2A-48B1-9645-92F4E8A8BD14}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'BCCollection' , 'ppCollection' , ), 10066, (10066, (), [ (16393, 10, None, "IID('{7F035946-EE7C-4557-BAFC-000BDD366EDF}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'OutputCollection' , 'ppCollection' , ), 10067, (10067, (), [ (16393, 10, None, "IID('{4549131A-72B6-45B1-9ABE-C2A32F250FED}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAllProperties' , ), 10068, (10068, (), [ ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'FlexBody' , 'ppVal' , ), 10069, (10069, (), [ (16393, 10, None, "IID('{9257FD72-F3D0-4E57-A114-2045356D78CD}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceForceDirection' , 'enumType' , ), 10070, (10070, (), [ (3, 1, None, "IID('{30A70529-402F-4740-B3A3-60A2037CF826}')") , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceForceDirection' , 'enumType' , ), 10070, (10070, (), [ (16387, 10, None, "IID('{30A70529-402F-4740-B3A3-60A2037CF826}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
]

IR2R2DBodyBeamCollection_vtables_dispatch_ = 1
IR2R2DBodyBeamCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IR2R2DBodyCollection_vtables_dispatch_ = 1
IR2R2DBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{9FC90B1C-92BE-4F20-99A2-144915D51DD4}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IR2R2DBodyRoller_vtables_dispatch_ = 1
IR2R2DBodyRoller_vtables_ = [
	(( 'InnerContactPoints' , 'pVal' , ), 10051, (10051, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'InnerContactPoints' , 'pVal' , ), 10051, (10051, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameter' , 'ppVal' , ), 10052, (10052, (), [ (16393, 10, None, "IID('{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IR2R2DBodyRollerCircle_vtables_dispatch_ = 1
IR2R2DBodyRollerCircle_vtables_ = [
	(( 'AssembledRadius' , 'ppVal' , ), 10101, (10101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppGeometry' , ), 10102, (10102, (), [ (16393, 10, None, "IID('{87F304FE-B89E-4306-8454-35E94D2B1360}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IR2R2DBodyRollerGeneral_vtables_dispatch_ = 1
IR2R2DBodyRollerGeneral_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10101, (10101, (), [ (16393, 10, None, "IID('{DC36087F-FBDD-42C4-ABD6-7D1FB7F00B09}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IR2R2DConcentratedLoadUSUBCollection_vtables_dispatch_ = 1
IR2R2DConcentratedLoadUSUBCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IR2R2DConnectingParameters_vtables_dispatch_ = 1
IR2R2DConnectingParameters_vtables_ = [
	(( 'UseForceConnector' , 'pVal' , ), 10100, (10100, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseForceConnector' , 'pVal' , ), 10100, (10100, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseSyncFDR' , 'pVal' , ), 10101, (10101, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseSyncFDR' , 'pVal' , ), 10101, (10101, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 10102, (10102, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MomentOfInertia' , 'ppVal' , ), 10103, (10103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalStiffness' , 'ppVal' , ), 10104, (10104, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDampingRatio' , 'ppVal' , ), 10105, (10105, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RotationnalStiffness' , 'ppVal' , ), 10106, (10106, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RotationnalDampingRatio' , 'ppVal' , ), 10107, (10107, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IR2R2DContact_vtables_dispatch_ = 1
IR2R2DContact_vtables_ = [
]

IR2R2DContactFriction_vtables_dispatch_ = 1
IR2R2DContactFriction_vtables_ = [
	(( 'StaticThresholdVelocity' , 'ppVal' , ), 10051, (10051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStaticThresholdVelocity' , 'pVal' , ), 10052, (10052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStaticThresholdVelocity' , 'pVal' , ), 10052, (10052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStaticThresholdVelocity' , 'ppVal' , ), 10053, (10053, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DynamicThresholdVelocity' , 'ppVal' , ), 10054, (10054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDynamicThresholdVelocity' , 'pVal' , ), 10055, (10055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDynamicThresholdVelocity' , 'pVal' , ), 10055, (10055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDynamicThresholdVelocity' , 'ppVal' , ), 10056, (10056, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StaticFrictionCoefficient' , 'ppVal' , ), 10057, (10057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStaticFrictionCoefficient' , 'pVal' , ), 10058, (10058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStaticFrictionCoefficient' , 'pVal' , ), 10058, (10058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStaticFrictionCoefficient' , 'ppVal' , ), 10059, (10059, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumFrictionForce' , 'pVal' , ), 10060, (10060, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumFrictionForce' , 'pVal' , ), 10060, (10060, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'MaximumFrictionForce' , 'ppVal' , ), 10061, (10061, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialMaximumFrictionForce' , 'pVal' , ), 10062, (10062, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialMaximumFrictionForce' , 'pVal' , ), 10062, (10062, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SpecialMaximumFrictionForce' , 'ppVal' , ), 10063, (10063, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IR2R2DContactParameter_vtables_dispatch_ = 1
IR2R2DContactParameter_vtables_ = [
	(( 'StiffnessCoefficient' , 'ppVal' , ), 10001, (10001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 10002, (10002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 10002, (10002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 10003, (10003, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 10003, (10003, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 10004, (10004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 10004, (10004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStiffness' , 'ppVal' , ), 10005, (10005, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 10006, (10006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 10007, (10007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 10007, (10007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 10008, (10008, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 10008, (10008, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDamping' , 'pVal' , ), 10009, (10009, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDamping' , 'pVal' , ), 10009, (10009, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDamping' , 'ppVal' , ), 10010, (10010, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ContactFrictionType' , 'ContactFrictionType' , ), 10011, (10011, (), [ (16387, 10, None, "IID('{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ContactFrictionType' , 'ContactFrictionType' , ), 10011, (10011, (), [ (3, 1, None, "IID('{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}')") , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Friction' , 'ppVal' , ), 10012, (10012, (), [ (16393, 10, None, "IID('{A70AF86B-7730-485D-880F-2B35DBE7D73E}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 10013, (10013, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 10014, (10014, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 10014, (10014, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialFriction' , 'pVal' , ), 10015, (10015, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialFriction' , 'pVal' , ), 10015, (10015, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SpecialFriction' , 'ppVal' , ), 10016, (10016, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 10017, (10017, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 10017, (10017, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 10018, (10018, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffnessExponent' , 'pVal' , ), 10019, (10019, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffnessExponent' , 'pVal' , ), 10019, (10019, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStiffnessExponent' , 'ppVal' , ), 10020, (10020, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 10021, (10021, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 10021, (10021, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 10022, (10022, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDampingExponent' , 'pVal' , ), 10023, (10023, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDampingExponent' , 'pVal' , ), 10023, (10023, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDampingExponent' , 'ppVal' , ), 10024, (10024, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 10025, (10025, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 10025, (10025, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 10026, (10026, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialIndentationExponent' , 'pVal' , ), 10027, (10027, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialIndentationExponent' , 'pVal' , ), 10027, (10027, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'SpecialIndentationExponent' , 'ppVal' , ), 10028, (10028, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseMaxPenetration' , 'pVal' , ), 10029, (10029, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseMaxPenetration' , 'pVal' , ), 10029, (10029, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'MaxPenetration' , 'ppVal' , ), 10030, (10030, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialMaxPenetration' , 'pVal' , ), 10031, (10031, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialMaxPenetration' , 'pVal' , ), 10031, (10031, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'SpecialMaxPenetration' , 'ppVal' , ), 10032, (10032, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseRDF' , 'pVal' , ), 10033, (10033, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'UseRDF' , 'pVal' , ), 10033, (10033, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'RDF' , 'ppVal' , ), 10034, (10034, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRDF' , 'pVal' , ), 10035, (10035, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRDF' , 'pVal' , ), 10035, (10035, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'SpecialRDF' , 'ppVal' , ), 10036, (10036, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
]

IR2R2DContactWorkpieceToWorkpiece_vtables_dispatch_ = 1
IR2R2DContactWorkpieceToWorkpiece_vtables_ = [
	(( 'BaseBeamAssembly' , 'ppVal' , ), 10051, (10051, (), [ (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BaseBeamAssembly' , 'ppVal' , ), 10051, (10051, (), [ (9, 1, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActionBeamAssembly' , 'ppVal' , ), 10052, (10052, (), [ (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ActionBeamAssembly' , 'ppVal' , ), 10052, (10052, (), [ (9, 1, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'InnerContactPoints' , 'pVal' , ), 10053, (10053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'InnerContactPoints' , 'pVal' , ), 10053, (10053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameter' , 'ppVal' , ), 10054, (10054, (), [ (16393, 10, None, "IID('{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IR2R2DContactWorkpieceToWorkpieceCollection_vtables_dispatch_ = 1
IR2R2DContactWorkpieceToWorkpieceCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IR2R2DGeometryBeam_vtables_dispatch_ = 1
IR2R2DGeometryBeam_vtables_ = [
	(( 'Color' , 'pVal' , ), 10100, (10100, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 10100, (10100, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DisplayGeometry' , 'pVal' , ), 10101, (10101, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DisplayGeometry' , 'pVal' , ), 10101, (10101, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeID' , 'pVal' , ), 10102, (10102, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeID' , 'pVal' , ), 10102, (10102, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'ppVal' , ), 10103, (10103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialThickness' , 'pVal' , ), 10104, (10104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialThickness' , 'pVal' , ), 10104, (10104, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SpecialThickness' , 'ppVal' , ), 10105, (10105, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 10106, (10106, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDepth' , 'pVal' , ), 10107, (10107, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDepth' , 'pVal' , ), 10107, (10107, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDepth' , 'ppVal' , ), 10108, (10108, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfElements' , 'pVal' , ), 10109, (10109, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ElementLength' , 'pVal' , ), 10110, (10110, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'StretchedLength' , 'ppVal' , ), 10111, (10111, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeIDType' , 'pVal' , ), 10112, (10112, (), [ (3, 1, None, "IID('{E009C436-BA56-4876-B240-53635C5A6AF2}')") , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeIDType' , 'pVal' , ), 10112, (10112, (), [ (16387, 10, None, "IID('{E009C436-BA56-4876-B240-53635C5A6AF2}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IR2R2DGeometryRollerCircle_vtables_dispatch_ = 1
IR2R2DGeometryRollerCircle_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 10101, (10101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 10102, (10102, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IR2R2DGeometryRollerGeneral_vtables_dispatch_ = 1
IR2R2DGeometryRollerGeneral_vtables_ = [
	(( 'Depth' , 'ppVal' , ), 10101, (10101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PointCollection' , 'ppVal' , ), 10102, (10102, (), [ (16393, 10, None, "IID('{2C0D70A3-D197-4781-940A-1672F3B420B9}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 10103, (10103, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 10104, (10104, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IR2R2DGuide_vtables_dispatch_ = 1
IR2R2DGuide_vtables_ = [
	(( 'MotherBody' , 'ppVal' , ), 10001, (10001, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MotherBody' , 'ppVal' , ), 10001, (10001, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameter' , 'ppVal' , ), 10002, (10002, (), [ (16393, 10, None, "IID('{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'InnerContactPoints' , 'pVal' , ), 10003, (10003, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'InnerContactPoints' , 'pVal' , ), 10003, (10003, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAllProperties' , ), 10004, (10004, (), [ ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IR2R2DGuideArc_vtables_dispatch_ = 1
IR2R2DGuideArc_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 10051, (10051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 10052, (10052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'ppVal' , ), 10053, (10053, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 10054, (10054, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 10054, (10054, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryCircleEdgeStart' , 'pVal' , ), 10055, (10055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryCircleEdgeStart' , 'pVal' , ), 10055, (10055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryCircleEdgeEnd' , 'pVal' , ), 10056, (10056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryCircleEdgeEnd' , 'pVal' , ), 10056, (10056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialCircleEdgeRadius' , 'pVal' , ), 10057, (10057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialCircleEdgeRadius' , 'pVal' , ), 10057, (10057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SpecialCircleEdgeRadius' , 'ppVal' , ), 10058, (10058, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CircleEdgeRadius' , 'ppVal' , ), 10059, (10059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IR2R2DGuideCircle_vtables_dispatch_ = 1
IR2R2DGuideCircle_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 10051, (10051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'ppVal' , ), 10052, (10052, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
]

IR2R2DGuideCollection_vtables_dispatch_ = 1
IR2R2DGuideCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{11C08FE6-98DF-4121-8503-4691765A0DAB}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IR2R2DGuideLinear_vtables_dispatch_ = 1
IR2R2DGuideLinear_vtables_ = [
	(( 'StartPoint' , 'ppVal' , ), 10051, (10051, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SecondPoint' , 'ppVal' , ), 10052, (10052, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ContactUpDirection' , 'pVal' , ), 10053, (10053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ContactUpDirection' , 'pVal' , ), 10053, (10053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryCircleEdgeStart' , 'pVal' , ), 10054, (10054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryCircleEdgeStart' , 'pVal' , ), 10054, (10054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryCircleEdgeEnd' , 'pVal' , ), 10055, (10055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryCircleEdgeEnd' , 'pVal' , ), 10055, (10055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialCircleEdgeRadius' , 'pVal' , ), 10056, (10056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialCircleEdgeRadius' , 'pVal' , ), 10056, (10056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'SpecialCircleEdgeRadius' , 'ppVal' , ), 10057, (10057, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'CircleEdgeRadius' , 'ppVal' , ), 10058, (10058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IR2R2DLoadConcentratedUSUB_vtables_dispatch_ = 1
IR2R2DLoadConcentratedUSUB_vtables_ = [
	(( 'NodeSet' , 'ppVal' , ), 10001, (10001, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'NodeSet' , 'ppVal' , ), 10001, (10001, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'ppVal' , ), 10002, (10002, (), [ (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'ppVal' , ), 10002, (10002, (), [ (16393, 10, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 10003, (10003, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 10003, (10003, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseReportNodes' , 'pVal' , ), 10005, (10005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseReportNodes' , 'pVal' , ), 10005, (10005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ReportNodeIDs' , 'arrNodeIDs' , ), 10006, (10006, (), [ (8195, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReportNodeIDs' , 'arrNodeIDs' , ), 10006, (10006, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IR2R2DMaterialPropertyBeam_vtables_dispatch_ = 1
IR2R2DMaterialPropertyBeam_vtables_ = [
	(( 'MassType' , 'pVal' , ), 10100, (10100, (), [ (3, 1, None, "IID('{89A46801-0658-4972-88F2-E8C0F422D1F4}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MassType' , 'pVal' , ), 10100, (10100, (), [ (16387, 10, None, "IID('{89A46801-0658-4972-88F2-E8C0F422D1F4}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'ppVal' , ), 10101, (10101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TotalMass' , 'ppVal' , ), 10102, (10102, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DampingRatio' , 'ppVal' , ), 10103, (10103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus' , 'ppVal' , ), 10104, (10104, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulus' , 'pVal' , ), 10105, (10105, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PoissonsRatio' , 'ppVal' , ), 10106, (10106, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'ppVal' , ), 10107, (10107, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'ppVal' , ), 10108, (10108, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'ppVal' , ), 10109, (10109, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'CrossSectionArea' , 'ppVal' , ), 10110, (10110, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CZ' , 'pVal' , ), 10111, (10111, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CZ' , 'pVal' , ), 10111, (10111, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FZ' , 'pVal' , ), 10112, (10112, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'FZ' , 'pVal' , ), 10112, (10112, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UpdateCrossSectionPropertyAutomaticallyFlag' , 'updateFlag' , ), 10113, (10113, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UpdateCrossSectionPropertyAutomaticallyFlag' , 'updateFlag' , ), 10113, (10113, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UpdateShearModulus' , ), 10114, (10114, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UpdateProperties' , ), 10115, (10115, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Asy' , 'dFactor' , ), 10116, (10116, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Asy' , 'dFactor' , ), 10116, (10116, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Asz' , 'dFactor' , ), 10117, (10117, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Asz' , 'dFactor' , ), 10117, (10117, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IR2R2DPassingBodyCollection_vtables_dispatch_ = 1
IR2R2DPassingBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IR2R2DSelfContact_vtables_dispatch_ = 1
IR2R2DSelfContact_vtables_ = [
	(( 'UseWinder' , 'pVal' , ), 10100, (10100, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseWinder' , 'pVal' , ), 10100, (10100, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'WinderRoller' , 'ppVal' , ), 10101, (10101, (), [ (16393, 10, None, "IID('{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'WinderRoller' , 'ppVal' , ), 10101, (10101, (), [ (9, 1, None, "IID('{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'WinderConectedNodeType' , 'pVal' , ), 10102, (10102, (), [ (3, 1, None, "IID('{71275134-C835-44E2-84F2-E9A37A5B6ADD}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'WinderConectedNodeType' , 'pVal' , ), 10102, (10102, (), [ (16387, 10, None, "IID('{71275134-C835-44E2-84F2-E9A37A5B6ADD}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'WinderSearchBoundaryFactor' , 'ppVal' , ), 10103, (10103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseUnWinder' , 'pVal' , ), 10104, (10104, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UseUnWinder' , 'pVal' , ), 10104, (10104, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'UnWinderRoller' , 'ppVal' , ), 10105, (10105, (), [ (16393, 10, None, "IID('{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UnWinderRoller' , 'ppVal' , ), 10105, (10105, (), [ (9, 1, None, "IID('{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}')") , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UnWinderConectedNodeType' , 'pVal' , ), 10106, (10106, (), [ (3, 1, None, "IID('{71275134-C835-44E2-84F2-E9A37A5B6ADD}')") , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UnWinderConectedNodeType' , 'pVal' , ), 10106, (10106, (), [ (16387, 10, None, "IID('{71275134-C835-44E2-84F2-E9A37A5B6ADD}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UnWinderSearchBoundaryFactor' , 'ppVal' , ), 10107, (10107, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameter' , 'ppVal' , ), 10108, (10108, (), [ (16393, 10, None, "IID('{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IR2R2DSubSystem_vtables_dispatch_ = 1
IR2R2DSubSystem_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 10000, (10000, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyRollerCircle' , 'strName' , 'pPoint' , 'ppResult' , ), 10001, (10001, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{33938809-28E5-4D14-B044-B074F7C7645B}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyRollerGeneral' , 'strName' , 'pPoint' , 'ppResult' , ), 10002, (10002, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{E60EA1F3-9C5B-4411-9C9E-715C89C5F2D5}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideArc' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'dAngle' , 
			 'ppResult' , ), 10003, (10003, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{6213B8B2-5B65-4259-8783-30AF5BAE2F10}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideArcWithEndPoint' , 'strName' , 'pCenterPoint' , 'pStartPoint' , 'pEndPoint' , 
			 'bDirection' , 'ppResult' , ), 10004, (10004, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (8197, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{6213B8B2-5B65-4259-8783-30AF5BAE2F10}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideArcWithThreePoints' , 'strName' , 'pThreePoint' , 'ppResult' , ), 10005, (10005, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{6213B8B2-5B65-4259-8783-30AF5BAE2F10}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideLinear' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'ppResult' , 
			 ), 10006, (10006, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{B245F42C-B731-48DE-BAD5-3D5D646C6A76}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideCircle' , 'strName' , 'pFirstPoint' , 'dRadius' , 'ppResult' , 
			 ), 10007, (10007, (), [ (8, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{A5D8C80B-2C7A-4C35-9393-7ADBB640A5F6}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideCircleWithThreePoints' , 'strName' , 'pThreePoint' , 'ppResult' , ), 10008, (10008, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{A5D8C80B-2C7A-4C35-9393-7ADBB640A5F6}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'GuideConvertWithColor' , 'pMultiBodies' , 'oleColor' , 'pResult' , ), 10009, (10009, (), [ 
			 (8204, 1, None, None) , (19, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorSpeed' , 'strName' , 'pPosition' , 'pDirection' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 10013, (10013, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{CCB7E742-F0DF-4F22-A377-04AA675FD281}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorDistance' , 'strName' , 'pPosition' , 'pDirection' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 10014, (10014, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{0CC3861B-CC2A-4402-9135-C8BC804EABBD}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorSlip' , 'strName' , 'pPosition' , 'pSlipEntity' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 10015, (10015, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{08675B12-6A90-4082-BAED-E54382FDF107}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorTension' , 'strName' , 'pPosition' , 'pEntity' , 'dRange' , 
			 'ppVal' , ), 10016, (10016, (), [ (8, 1, None, None) , (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{55C49622-A503-4651-BF1E-2A84CD9E27AB}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactWorkpieceToWorkpiece' , 'strName' , 'pBaseBeamAssembly' , 'pActionBeamAssembly' , 'ppResult' , 
			 ), 10017, (10017, (), [ (8, 1, None, None) , (9, 1, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , (9, 1, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , (16393, 10, None, "IID('{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConcentratedLoadUSUB' , 'strName' , 'pNodeSet' , 'pUsub' , 'ppVal' , 
			 ), 10018, (10018, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , (16393, 10, None, "IID('{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'BodyBeamCollection' , 'ppVal' , ), 10030, (10030, (), [ (16393, 10, None, "IID('{D51B4A60-30FE-4A2C-89CE-6DE904CD7771}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'BodyCollection' , 'ppVal' , ), 10031, (10031, (), [ (16393, 10, None, "IID('{F66AB8D5-E20C-437F-BD61-982CCD09B711}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GuideCollection' , 'ppVal' , ), 10032, (10032, (), [ (16393, 10, None, "IID('{2185E9C9-D7B1-4AE5-A0BE-A49CA236280A}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ContacttWorkpieceToWorkpieceCollection' , 'ppVal' , ), 10033, (10033, (), [ (16393, 10, None, "IID('{3AC2E0DA-1DEA-4818-B371-A35C8E858CAE}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Contour' , 'ppVal' , ), 10034, (10034, (), [ (16393, 10, None, "IID('{BDF4F979-28B7-48D2-BF06-9C59B70D467B}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ConcentratedLoadUSUBCollection' , 'ppVal' , ), 10035, (10035, (), [ (16393, 10, None, "IID('{4EEF5BEB-2CCF-4BD9-8159-CF6A337F2581}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeam2' , 'strName' , 'pBodyList' , 'pInOutList' , 'uiNumberOfElements' , 
			 'ppResult' , ), 10037, (10037, (), [ (8, 1, None, None) , (8204, 1, None, None) , (8204, 1, None, None) , 
			 (19, 1, None, None) , (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeamWithOpenLoop2' , 'strName' , 'pBodyList' , 'pInOutList' , 'pStartDir' , 
			 'pStartOrthoDir' , 'pEndDir' , 'uiNumberOfElements' , 'ppResult' , ), 10038, (10038, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (8204, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeamWithPreWinding3' , 'strName' , 'pBodyList' , 'pInOutList' , 'pStartDir' , 
			 'pStartOrthoDir' , 'uiNumberOfElements' , 'uiNumberOfStartWindings' , 'uiNumberOfEndWindings' , 'offsetFactor' , 
			 'ppResult' , ), 10039, (10039, (), [ (8, 1, None, None) , (8204, 1, None, None) , (8204, 1, None, None) , 
			 (8197, 1, None, None) , (8197, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeamWithPreWinding4' , 'strName' , 'pBodyList' , 'pInOutList' , 'pStartDir' , 
			 'pStartOrthoDir' , 'uiNumberOfElements' , 'startThicknessflag' , 'endThicknessflag' , 'uiNumberOfStartWindings' , 
			 'uiNumberOfEndWindings' , 'offsetFactor' , 'ppResult' , ), 10040, (10040, (), [ (8, 1, None, None) , 
			 (8204, 1, None, None) , (8204, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , (19, 1, None, None) , 
			 (11, 1, None, None) , (11, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (5, 1, None, None) , 
			 (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeam' , 'strName' , 'pBodyList' , 'pInOutList' , 'uiNumberOfElements' , 
			 'Thickness' , 'ppResult' , ), 10010, (10010, (), [ (8, 1, None, None) , (8204, 1, None, None) , 
			 (8204, 1, None, None) , (19, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeamWithOpenLoop' , 'strName' , 'pBodyList' , 'pInOutList' , 'pStartDir' , 
			 'pStartOrthoDir' , 'pEndDir' , 'uiNumberOfElements' , 'Thickness' , 'ppResult' , 
			 ), 10011, (10011, (), [ (8, 1, None, None) , (8204, 1, None, None) , (8204, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (8197, 1, None, None) , (19, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeamWithPreWinding' , 'strName' , 'pBodyList' , 'pInOutList' , 'pStartDir' , 
			 'pStartOrthoDir' , 'uiNumberOfElements' , 'Thickness' , 'uiNumberOfStartWindings' , 'uiNumberOfEndWindings' , 
			 'offsetFactor' , 'ppResult' , ), 10012, (10012, (), [ (8, 1, None, None) , (8204, 1, None, None) , 
			 (8204, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , (19, 1, None, None) , (5, 1, None, None) , 
			 (19, 1, None, None) , (19, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeamWithPreWinding2' , 'strName' , 'pBodyList' , 'pInOutList' , 'pStartDir' , 
			 'pStartOrthoDir' , 'uiNumberOfElements' , 'Thickness' , 'startThicknessflag' , 'endThicknessflag' , 
			 'uiNumberOfStartWindings' , 'uiNumberOfEndWindings' , 'offsetFactor' , 'ppResult' , ), 10036, (10036, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (8204, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , 
			 (19, 1, None, None) , (5, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , (19, 1, None, None) , 
			 (19, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{FF337086-F852-42E3-BF88-2795D0BBCB31}')") , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{A70AF86B-7730-485D-880F-2B35DBE7D73E}' : IR2R2DContactFriction,
	'{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}' : IR2R2DContactParameter,
	'{87F304FE-B89E-4306-8454-35E94D2B1360}' : IR2R2DGeometryRollerCircle,
	'{DC36087F-FBDD-42C4-ABD6-7D1FB7F00B09}' : IR2R2DGeometryRollerGeneral,
	'{9FC90B1C-92BE-4F20-99A2-144915D51DD4}' : IR2R2DBody,
	'{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}' : IR2R2DBodyRoller,
	'{33938809-28E5-4D14-B044-B074F7C7645B}' : IR2R2DBodyRollerCircle,
	'{E60EA1F3-9C5B-4411-9C9E-715C89C5F2D5}' : IR2R2DBodyRollerGeneral,
	'{11C08FE6-98DF-4121-8503-4691765A0DAB}' : IR2R2DGuide,
	'{B245F42C-B731-48DE-BAD5-3D5D646C6A76}' : IR2R2DGuideLinear,
	'{6213B8B2-5B65-4259-8783-30AF5BAE2F10}' : IR2R2DGuideArc,
	'{A5D8C80B-2C7A-4C35-9393-7ADBB640A5F6}' : IR2R2DGuideCircle,
	'{9AC66E9B-1D93-434B-BCD2-1F54446A3687}' : IR2R2DSelfContact,
	'{21DDE70D-AD2A-48B1-9645-92F4E8A8BD14}' : IR2R2DConnectingParameters,
	'{22E7FECE-90EC-4649-A335-CD1139004817}' : IR2R2DGeometryBeam,
	'{7474063C-637A-4F9E-ABC0-11F074027153}' : IR2R2DMaterialPropertyBeam,
	'{E5EED844-E317-49B8-B8F8-42DF2D16E4EC}' : IR2R2DPassingBodyCollection,
	'{FF337086-F852-42E3-BF88-2795D0BBCB31}' : IR2R2DBodyBeam,
	'{D72D730B-3E34-4ADB-B946-689EC685D591}' : IR2R2DContact,
	'{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}' : IR2R2DContactWorkpieceToWorkpiece,
	'{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}' : IR2R2DLoadConcentratedUSUB,
	'{D51B4A60-30FE-4A2C-89CE-6DE904CD7771}' : IR2R2DBodyBeamCollection,
	'{F66AB8D5-E20C-437F-BD61-982CCD09B711}' : IR2R2DBodyCollection,
	'{2185E9C9-D7B1-4AE5-A0BE-A49CA236280A}' : IR2R2DGuideCollection,
	'{3AC2E0DA-1DEA-4818-B371-A35C8E858CAE}' : IR2R2DContactWorkpieceToWorkpieceCollection,
	'{4EEF5BEB-2CCF-4BD9-8159-CF6A337F2581}' : IR2R2DConcentratedLoadUSUBCollection,
	'{08ABAC6E-D10A-486E-B921-52DAFE7D7A45}' : IR2R2DSubSystem,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{A70AF86B-7730-485D-880F-2B35DBE7D73E}' : 'IR2R2DContactFriction',
	'{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}' : 'IR2R2DContactParameter',
	'{87F304FE-B89E-4306-8454-35E94D2B1360}' : 'IR2R2DGeometryRollerCircle',
	'{DC36087F-FBDD-42C4-ABD6-7D1FB7F00B09}' : 'IR2R2DGeometryRollerGeneral',
	'{9FC90B1C-92BE-4F20-99A2-144915D51DD4}' : 'IR2R2DBody',
	'{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}' : 'IR2R2DBodyRoller',
	'{33938809-28E5-4D14-B044-B074F7C7645B}' : 'IR2R2DBodyRollerCircle',
	'{E60EA1F3-9C5B-4411-9C9E-715C89C5F2D5}' : 'IR2R2DBodyRollerGeneral',
	'{11C08FE6-98DF-4121-8503-4691765A0DAB}' : 'IR2R2DGuide',
	'{B245F42C-B731-48DE-BAD5-3D5D646C6A76}' : 'IR2R2DGuideLinear',
	'{6213B8B2-5B65-4259-8783-30AF5BAE2F10}' : 'IR2R2DGuideArc',
	'{A5D8C80B-2C7A-4C35-9393-7ADBB640A5F6}' : 'IR2R2DGuideCircle',
	'{9AC66E9B-1D93-434B-BCD2-1F54446A3687}' : 'IR2R2DSelfContact',
	'{21DDE70D-AD2A-48B1-9645-92F4E8A8BD14}' : 'IR2R2DConnectingParameters',
	'{22E7FECE-90EC-4649-A335-CD1139004817}' : 'IR2R2DGeometryBeam',
	'{7474063C-637A-4F9E-ABC0-11F074027153}' : 'IR2R2DMaterialPropertyBeam',
	'{E5EED844-E317-49B8-B8F8-42DF2D16E4EC}' : 'IR2R2DPassingBodyCollection',
	'{FF337086-F852-42E3-BF88-2795D0BBCB31}' : 'IR2R2DBodyBeam',
	'{D72D730B-3E34-4ADB-B946-689EC685D591}' : 'IR2R2DContact',
	'{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}' : 'IR2R2DContactWorkpieceToWorkpiece',
	'{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}' : 'IR2R2DLoadConcentratedUSUB',
	'{D51B4A60-30FE-4A2C-89CE-6DE904CD7771}' : 'IR2R2DBodyBeamCollection',
	'{F66AB8D5-E20C-437F-BD61-982CCD09B711}' : 'IR2R2DBodyCollection',
	'{2185E9C9-D7B1-4AE5-A0BE-A49CA236280A}' : 'IR2R2DGuideCollection',
	'{3AC2E0DA-1DEA-4818-B371-A35C8E858CAE}' : 'IR2R2DContactWorkpieceToWorkpieceCollection',
	'{4EEF5BEB-2CCF-4BD9-8159-CF6A337F2581}' : 'IR2R2DConcentratedLoadUSUBCollection',
	'{08ABAC6E-D10A-486E-B921-52DAFE7D7A45}' : 'IR2R2DSubSystem',
}


NamesToIIDMap = {
	'IR2R2DContactFriction' : '{A70AF86B-7730-485D-880F-2B35DBE7D73E}',
	'IR2R2DContactParameter' : '{3DE6CBD0-34ED-42A0-99A6-F7B41667F6E7}',
	'IR2R2DGeometryRollerCircle' : '{87F304FE-B89E-4306-8454-35E94D2B1360}',
	'IR2R2DGeometryRollerGeneral' : '{DC36087F-FBDD-42C4-ABD6-7D1FB7F00B09}',
	'IR2R2DBody' : '{9FC90B1C-92BE-4F20-99A2-144915D51DD4}',
	'IR2R2DBodyRoller' : '{AFCA7C46-7C5E-48F7-8117-37F2BB1222DD}',
	'IR2R2DBodyRollerCircle' : '{33938809-28E5-4D14-B044-B074F7C7645B}',
	'IR2R2DBodyRollerGeneral' : '{E60EA1F3-9C5B-4411-9C9E-715C89C5F2D5}',
	'IR2R2DGuide' : '{11C08FE6-98DF-4121-8503-4691765A0DAB}',
	'IR2R2DGuideLinear' : '{B245F42C-B731-48DE-BAD5-3D5D646C6A76}',
	'IR2R2DGuideArc' : '{6213B8B2-5B65-4259-8783-30AF5BAE2F10}',
	'IR2R2DGuideCircle' : '{A5D8C80B-2C7A-4C35-9393-7ADBB640A5F6}',
	'IR2R2DSelfContact' : '{9AC66E9B-1D93-434B-BCD2-1F54446A3687}',
	'IR2R2DConnectingParameters' : '{21DDE70D-AD2A-48B1-9645-92F4E8A8BD14}',
	'IR2R2DGeometryBeam' : '{22E7FECE-90EC-4649-A335-CD1139004817}',
	'IR2R2DMaterialPropertyBeam' : '{7474063C-637A-4F9E-ABC0-11F074027153}',
	'IR2R2DPassingBodyCollection' : '{E5EED844-E317-49B8-B8F8-42DF2D16E4EC}',
	'IR2R2DBodyBeam' : '{FF337086-F852-42E3-BF88-2795D0BBCB31}',
	'IR2R2DContact' : '{D72D730B-3E34-4ADB-B946-689EC685D591}',
	'IR2R2DContactWorkpieceToWorkpiece' : '{F40C22AF-8635-4E5D-9CDD-D7E4C4697EFD}',
	'IR2R2DLoadConcentratedUSUB' : '{6643BA23-1926-4BEB-8F25-DA51C7AF1C47}',
	'IR2R2DBodyBeamCollection' : '{D51B4A60-30FE-4A2C-89CE-6DE904CD7771}',
	'IR2R2DBodyCollection' : '{F66AB8D5-E20C-437F-BD61-982CCD09B711}',
	'IR2R2DGuideCollection' : '{2185E9C9-D7B1-4AE5-A0BE-A49CA236280A}',
	'IR2R2DContactWorkpieceToWorkpieceCollection' : '{3AC2E0DA-1DEA-4818-B371-A35C8E858CAE}',
	'IR2R2DConcentratedLoadUSUBCollection' : '{4EEF5BEB-2CCF-4BD9-8159-CF6A337F2581}',
	'IR2R2DSubSystem' : '{08ABAC6E-D10A-486E-B921-52DAFE7D7A45}',
}


