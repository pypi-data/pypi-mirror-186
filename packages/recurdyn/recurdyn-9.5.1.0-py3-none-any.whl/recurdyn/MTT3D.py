# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMMTT3D.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5 RecurDynCOMMTT3D Type Library'
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

CLSID = IID('{E67CD7E0-293C-49B1-9132-5D2B3CCE0B25}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class AirResistanceType(IntEnum):
	'''
	AirResistanceType enumeration.
	'''
	AirResistanceType_Constant    =0         
	'''Constant value is 0.'''
	AirResistanceType_Expression  =1         
	'''Constant value is 1.'''
class ContactParameterType(IntEnum):
	'''
	ContactParameterType enumeration.
	'''
	ContactParameterType_BoundaryPenetration=0         
	'''Constant value is 0.'''
	ContactParameterType_IndentationExponent=1         
	'''Constant value is 1.'''
class MTT3DBCOrienationType(IntEnum):
	'''
	MTT3DBCOrienationType enumeration.
	'''
	MTT3DBCOrienationType_Inertia =1         
	'''Constant value is 1.'''
	MTT3DBCOrienationType_Node    =0         
	'''Constant value is 0.'''
class MTT3DFrictionType(IntEnum):
	'''
	MTT3DFrictionType enumeration.
	'''
	Linear                        =1         
	'''Constant value is 1.'''
	Step                          =0         
	'''Constant value is 0.'''
class RollerType(IntEnum):
	'''
	RollerType enumeration.
	'''
	RollerType_Crown              =1         
	'''Constant value is 1.'''
	RollerType_General            =0         
	'''Constant value is 0.'''
class SheetDirectionType(IntEnum):
	'''
	SheetDirectionType enumeration.
	'''
	Lateral                       =1         
	'''Constant value is 1.'''
	Longitudinal                  =0         
	'''Constant value is 0.'''
class SheetMeshType(IntEnum):
	'''
	SheetMeshType enumeration.
	'''
	Element                       =1         
	'''Constant value is 1.'''
	Node                          =0         
	'''Constant value is 0.'''
class SheetShapeType(IntEnum):
	'''
	SheetShapeType enumeration.
	'''
	Flat                          =0         
	'''Constant value is 0.'''
	Folding                       =1         
	'''Constant value is 1.'''
	SplineSurface                 =2         
	'''Constant value is 2.'''

from win32com.client import DispatchBaseClass
class IMTT3DAssembly(DispatchBaseClass):
	'''MTT3D assembly'''
	CLSID = IID('{5E4ADDAC-BBF0-49B3-B368-C7259CA3D07E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetContactedGeometry(self, pVal):
		'''
		Get a contacted geometry
		
		:param pVal: str
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(5052, LCID, 1, (11, 0), ((8, 1),),pVal
			)


	def GetContactedSheet(self, pVal):
		'''
		Get a contacted sheet
		
		:param pVal: str
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(5054, LCID, 1, (11, 0), ((8, 1),),pVal
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def SetContactedGeometry(self, pVal, vBool):
		'''
		Set a contacted geometry
		
		:param pVal: str
		:param vBool: bool
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(5051, LCID, 1, (11, 0), ((8, 1), (11, 1)),pVal
			, vBool)


	def SetContactedSheet(self, pVal, vBool):
		'''
		Set a contacted sheet
		
		:param pVal: str
		:param vBool: bool
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(5053, LCID, 1, (11, 0), ((8, 1), (11, 1)),pVal
			, vBool)


	def _get_BufferRadiusFactor(self):
		return self._ApplyTypes_(*(5058, 2, (9, 0), (), "BufferRadiusFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_MaximumNoOfSheetElements(self):
		return self._ApplyTypes_(*(5064, 2, (3, 0), (), "MaximumNoOfSheetElements", None))
	def _get_MaximumStepsizeFactor(self):
		return self._ApplyTypes_(*(5059, 2, (9, 0), (), "MaximumStepsizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PenetrationParameter(self):
		return self._ApplyTypes_(*(5060, 2, (9, 0), (), "PenetrationParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ReferencePosition(self):
		return self._ApplyTypes_(*(5056, 2, (9, 0), (), "ReferencePosition", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_Resolution(self):
		return self._ApplyTypes_(*(5062, 2, (8197, 0), (), "Resolution", None))
	def _get_SizeOfBoundary(self):
		return self._ApplyTypes_(*(5057, 2, (8197, 0), (), "SizeOfBoundary", None))
	def _get_UseMaximumNoOfSheetElements(self):
		return self._ApplyTypes_(*(5063, 2, (11, 0), (), "UseMaximumNoOfSheetElements", None))
	def _get_UseResolution(self):
		return self._ApplyTypes_(*(5061, 2, (11, 0), (), "UseResolution", None))
	def _get_UseSystemBoundary(self):
		return self._ApplyTypes_(*(5055, 2, (11, 0), (), "UseSystemBoundary", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_MaximumNoOfSheetElements(self, value):
		if "MaximumNoOfSheetElements" in self.__dict__: self.__dict__["MaximumNoOfSheetElements"] = value; return
		self._oleobj_.Invoke(*((5064, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Resolution(self, value):
		if "Resolution" in self.__dict__: self.__dict__["Resolution"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5062, LCID, 4, 0) + (variantValue,) + ()))
	def _set_SizeOfBoundary(self, value):
		if "SizeOfBoundary" in self.__dict__: self.__dict__["SizeOfBoundary"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5057, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseMaximumNoOfSheetElements(self, value):
		if "UseMaximumNoOfSheetElements" in self.__dict__: self.__dict__["UseMaximumNoOfSheetElements"] = value; return
		self._oleobj_.Invoke(*((5063, LCID, 4, 0) + (value,) + ()))
	def _set_UseResolution(self, value):
		if "UseResolution" in self.__dict__: self.__dict__["UseResolution"] = value; return
		self._oleobj_.Invoke(*((5061, LCID, 4, 0) + (value,) + ()))
	def _set_UseSystemBoundary(self, value):
		if "UseSystemBoundary" in self.__dict__: self.__dict__["UseSystemBoundary"] = value; return
		self._oleobj_.Invoke(*((5055, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BufferRadiusFactor = property(_get_BufferRadiusFactor, None)
	'''
	Buffer radius factor

	:type: recurdyn.ProcessNet.IDouble
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
	MaximumNoOfSheetElements = property(_get_MaximumNoOfSheetElements, _set_MaximumNoOfSheetElements)
	'''
	Maximum number of sheet's elements

	:type: int
	'''
	MaximumStepsizeFactor = property(_get_MaximumStepsizeFactor, None)
	'''
	Maximum stepsize factor

	:type: recurdyn.ProcessNet.IDouble
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
	PenetrationParameter = property(_get_PenetrationParameter, None)
	'''
	Penetration parameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	ReferencePosition = property(_get_ReferencePosition, None)
	'''
	Reference position

	:type: recurdyn.ProcessNet.IVector
	'''
	Resolution = property(_get_Resolution, _set_Resolution)
	'''
	Resolution

	:type: list[float]
	'''
	SizeOfBoundary = property(_get_SizeOfBoundary, _set_SizeOfBoundary)
	'''
	Size of boundary

	:type: list[float]
	'''
	UseMaximumNoOfSheetElements = property(_get_UseMaximumNoOfSheetElements, _set_UseMaximumNoOfSheetElements)
	'''
	Use maximum number of sheet's elements

	:type: bool
	'''
	UseResolution = property(_get_UseResolution, _set_UseResolution)
	'''
	Use resolution

	:type: bool
	'''
	UseSystemBoundary = property(_get_UseSystemBoundary, _set_UseSystemBoundary)
	'''
	Use system boundary

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_MaximumNoOfSheetElements": _set_MaximumNoOfSheetElements,
		"_set_Name": _set_Name,
		"_set_Resolution": _set_Resolution,
		"_set_SizeOfBoundary": _set_SizeOfBoundary,
		"_set_UseMaximumNoOfSheetElements": _set_UseMaximumNoOfSheetElements,
		"_set_UseResolution": _set_UseResolution,
		"_set_UseSystemBoundary": _set_UseSystemBoundary,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BufferRadiusFactor": (5058, 2, (9, 0), (), "BufferRadiusFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"MaximumNoOfSheetElements": (5064, 2, (3, 0), (), "MaximumNoOfSheetElements", None),
		"MaximumStepsizeFactor": (5059, 2, (9, 0), (), "MaximumStepsizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PenetrationParameter": (5060, 2, (9, 0), (), "PenetrationParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ReferencePosition": (5056, 2, (9, 0), (), "ReferencePosition", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"Resolution": (5062, 2, (8197, 0), (), "Resolution", None),
		"SizeOfBoundary": (5057, 2, (8197, 0), (), "SizeOfBoundary", None),
		"UseMaximumNoOfSheetElements": (5063, 2, (11, 0), (), "UseMaximumNoOfSheetElements", None),
		"UseResolution": (5061, 2, (11, 0), (), "UseResolution", None),
		"UseSystemBoundary": (5055, 2, (11, 0), (), "UseSystemBoundary", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"MaximumNoOfSheetElements": ((5064, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Resolution": ((5062, LCID, 4, 0),()),
		"SizeOfBoundary": ((5057, LCID, 4, 0),()),
		"UseMaximumNoOfSheetElements": ((5063, LCID, 4, 0),()),
		"UseResolution": ((5061, LCID, 4, 0),()),
		"UseSystemBoundary": ((5055, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DContact(DispatchBaseClass):
	'''MTT3D contact'''
	CLSID = IID('{2F8CA0C3-CE82-480F-A8D2-7B58899FC45C}')
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
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(5001, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
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
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(5004, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
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
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
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
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

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
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (5002, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ForceDisplay": (5001, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SpecialContactPoints": (5003, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseSpecialContactPoints": (5004, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((5001, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((5004, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DContactCollection(DispatchBaseClass):
	'''IMTT3DContactCollection'''
	CLSID = IID('{F032BD6E-8DA6-41D9-BE7E-6B6137E6221A}')
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
		:rtype: recurdyn.MTT3D.IMTT3DContact
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{2F8CA0C3-CE82-480F-A8D2-7B58899FC45C}')
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
		:rtype: recurdyn.MTT3D.IMTT3DContact
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{2F8CA0C3-CE82-480F-A8D2-7B58899FC45C}')
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
		return win32com.client.util.Iterator(ob, '{2F8CA0C3-CE82-480F-A8D2-7B58899FC45C}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{2F8CA0C3-CE82-480F-A8D2-7B58899FC45C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT3DContactProperty(DispatchBaseClass):
	'''MTT3D contact property'''
	CLSID = IID('{823B2FED-7C16-4336-A3D1-39241C0B06FB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BoundaryPenetration(self):
		return self._ApplyTypes_(*(5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(5024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(5025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(5008, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((5022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((5023, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((5024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((5014, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((5018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((5016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((5012, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((5025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((5008, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5010, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((5020, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT3D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT3D.MTT3DFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	Indentation exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumDamping = property(_get_MaximumDamping, None)
	'''
	Maximum damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	RDF = property(_get_RDF, None)
	'''
	RDF

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialBoundaryPenetration = property(_get_SpecialBoundaryPenetration, None)
	'''
	Special boundary penetration

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialFrictionCoefficient = property(_get_SpecialFrictionCoefficient, None)
	'''
	Special friction coefficient

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialIndentationExponent = property(_get_SpecialIndentationExponent, None)
	'''
	Special indentation exponent

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialMaximumDamping = property(_get_SpecialMaximumDamping, None)
	'''
	Special maximum damping

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialRDF = property(_get_SpecialRDF, None)
	'''
	Special RDF

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
	SpecialThresholdVelocity = property(_get_SpecialThresholdVelocity, None)
	'''
	Special threshold velocity

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	Stiffness = property(_get_Stiffness, None)
	'''
	Stiffness

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	Stiffness exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	ThresholdVelocity = property(_get_ThresholdVelocity, None)
	'''
	Threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseRDF = property(_get_UseRDF, _set_UseRDF)
	'''
	Use RDF

	:type: bool
	'''
	UseSpecialBoundaryPenetration = property(_get_UseSpecialBoundaryPenetration, _set_UseSpecialBoundaryPenetration)
	'''
	Use special boundary penetration

	:type: bool
	'''
	UseSpecialFrictionCoefficient = property(_get_UseSpecialFrictionCoefficient, _set_UseSpecialFrictionCoefficient)
	'''
	Use special friction coefficient

	:type: bool
	'''
	UseSpecialIndentationExponent = property(_get_UseSpecialIndentationExponent, _set_UseSpecialIndentationExponent)
	'''
	Use special indentation exponent

	:type: bool
	'''
	UseSpecialMaximumDamping = property(_get_UseSpecialMaximumDamping, _set_UseSpecialMaximumDamping)
	'''
	Use special maximum damping

	:type: bool
	'''
	UseSpecialRDF = property(_get_UseSpecialRDF, _set_UseSpecialRDF)
	'''
	Use special RDF

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
	UseSpecialThresholdVelocity = property(_get_UseSpecialThresholdVelocity, _set_UseSpecialThresholdVelocity)
	'''
	Use special threshold velocity

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactParameterType": _set_ContactParameterType,
		"_set_FrictionType": _set_FrictionType,
		"_set_UseRDF": _set_UseRDF,
		"_set_UseSpecialBoundaryPenetration": _set_UseSpecialBoundaryPenetration,
		"_set_UseSpecialFrictionCoefficient": _set_UseSpecialFrictionCoefficient,
		"_set_UseSpecialIndentationExponent": _set_UseSpecialIndentationExponent,
		"_set_UseSpecialMaximumDamping": _set_UseSpecialMaximumDamping,
		"_set_UseSpecialRDF": _set_UseSpecialRDF,
		"_set_UseSpecialStiffness": _set_UseSpecialStiffness,
		"_set_UseSpecialStiffnessExponent": _set_UseSpecialStiffnessExponent,
		"_set_UseSpecialThresholdVelocity": _set_UseSpecialThresholdVelocity,
	}
	_prop_map_get_ = {
		"BoundaryPenetration": (5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'),
		"FrictionCoefficient": (5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'),
		"IndentationExponent": (5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseRDF": (5024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (5025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (5008, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((5022, LCID, 4, 0),()),
		"FrictionType": ((5023, LCID, 4, 0),()),
		"UseRDF": ((5024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((5014, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((5018, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((5016, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((5012, LCID, 4, 0),()),
		"UseSpecialRDF": ((5025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((5008, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((5010, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((5020, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DContactPropertyCircularGuide(DispatchBaseClass):
	'''MTT3D circular guide contact property'''
	CLSID = IID('{3D9E9719-9BD8-4234-8A98-87D2975BB531}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BoundaryPenetration(self):
		return self._ApplyTypes_(*(5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'))
	def _get_GuideVelocity(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "GuideVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(5024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(5025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(5008, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((5022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((5023, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((5024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((5014, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((5018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((5016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((5012, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((5025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((5008, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5010, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((5020, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT3D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT3D.MTT3DFrictionType
	'''
	GuideVelocity = property(_get_GuideVelocity, None)
	'''
	Guide velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	Indentation exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumDamping = property(_get_MaximumDamping, None)
	'''
	Maximum damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	RDF = property(_get_RDF, None)
	'''
	RDF

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialBoundaryPenetration = property(_get_SpecialBoundaryPenetration, None)
	'''
	Special boundary penetration

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialFrictionCoefficient = property(_get_SpecialFrictionCoefficient, None)
	'''
	Special friction coefficient

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialIndentationExponent = property(_get_SpecialIndentationExponent, None)
	'''
	Special indentation exponent

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialMaximumDamping = property(_get_SpecialMaximumDamping, None)
	'''
	Special maximum damping

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialRDF = property(_get_SpecialRDF, None)
	'''
	Special RDF

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
	SpecialThresholdVelocity = property(_get_SpecialThresholdVelocity, None)
	'''
	Special threshold velocity

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	Stiffness = property(_get_Stiffness, None)
	'''
	Stiffness

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	Stiffness exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	ThresholdVelocity = property(_get_ThresholdVelocity, None)
	'''
	Threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseRDF = property(_get_UseRDF, _set_UseRDF)
	'''
	Use RDF

	:type: bool
	'''
	UseSpecialBoundaryPenetration = property(_get_UseSpecialBoundaryPenetration, _set_UseSpecialBoundaryPenetration)
	'''
	Use special boundary penetration

	:type: bool
	'''
	UseSpecialFrictionCoefficient = property(_get_UseSpecialFrictionCoefficient, _set_UseSpecialFrictionCoefficient)
	'''
	Use special friction coefficient

	:type: bool
	'''
	UseSpecialIndentationExponent = property(_get_UseSpecialIndentationExponent, _set_UseSpecialIndentationExponent)
	'''
	Use special indentation exponent

	:type: bool
	'''
	UseSpecialMaximumDamping = property(_get_UseSpecialMaximumDamping, _set_UseSpecialMaximumDamping)
	'''
	Use special maximum damping

	:type: bool
	'''
	UseSpecialRDF = property(_get_UseSpecialRDF, _set_UseSpecialRDF)
	'''
	Use special RDF

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
	UseSpecialThresholdVelocity = property(_get_UseSpecialThresholdVelocity, _set_UseSpecialThresholdVelocity)
	'''
	Use special threshold velocity

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactParameterType": _set_ContactParameterType,
		"_set_FrictionType": _set_FrictionType,
		"_set_UseRDF": _set_UseRDF,
		"_set_UseSpecialBoundaryPenetration": _set_UseSpecialBoundaryPenetration,
		"_set_UseSpecialFrictionCoefficient": _set_UseSpecialFrictionCoefficient,
		"_set_UseSpecialIndentationExponent": _set_UseSpecialIndentationExponent,
		"_set_UseSpecialMaximumDamping": _set_UseSpecialMaximumDamping,
		"_set_UseSpecialRDF": _set_UseSpecialRDF,
		"_set_UseSpecialStiffness": _set_UseSpecialStiffness,
		"_set_UseSpecialStiffnessExponent": _set_UseSpecialStiffnessExponent,
		"_set_UseSpecialThresholdVelocity": _set_UseSpecialThresholdVelocity,
	}
	_prop_map_get_ = {
		"BoundaryPenetration": (5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'),
		"FrictionCoefficient": (5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'),
		"GuideVelocity": (5051, 2, (9, 0), (), "GuideVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"IndentationExponent": (5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseRDF": (5024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (5025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (5008, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((5022, LCID, 4, 0),()),
		"FrictionType": ((5023, LCID, 4, 0),()),
		"UseRDF": ((5024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((5014, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((5018, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((5016, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((5012, LCID, 4, 0),()),
		"UseSpecialRDF": ((5025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((5008, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((5010, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((5020, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DContactPropertyGuide(DispatchBaseClass):
	'''MTT3D guide contact property'''
	CLSID = IID('{B805319E-24BB-4157-B46C-C40AD3B0F5C4}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BoundaryPenetration(self):
		return self._ApplyTypes_(*(5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionFactorVertexofSheet(self):
		return self._ApplyTypes_(*(5101, 2, (9, 0), (), "FrictionFactorVertexofSheet", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'))
	def _get_GuideVelocity(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "GuideVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(5024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(5025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(5008, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((5022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((5023, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((5024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((5014, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((5018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((5016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((5012, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((5025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((5008, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5010, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((5020, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT3D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionFactorVertexofSheet = property(_get_FrictionFactorVertexofSheet, None)
	'''
	Friction factor at vertex of sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT3D.MTT3DFrictionType
	'''
	GuideVelocity = property(_get_GuideVelocity, None)
	'''
	Guide velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	Indentation exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumDamping = property(_get_MaximumDamping, None)
	'''
	Maximum damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	RDF = property(_get_RDF, None)
	'''
	RDF

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialBoundaryPenetration = property(_get_SpecialBoundaryPenetration, None)
	'''
	Special boundary penetration

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialFrictionCoefficient = property(_get_SpecialFrictionCoefficient, None)
	'''
	Special friction coefficient

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialIndentationExponent = property(_get_SpecialIndentationExponent, None)
	'''
	Special indentation exponent

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialMaximumDamping = property(_get_SpecialMaximumDamping, None)
	'''
	Special maximum damping

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialRDF = property(_get_SpecialRDF, None)
	'''
	Special RDF

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
	SpecialThresholdVelocity = property(_get_SpecialThresholdVelocity, None)
	'''
	Special threshold velocity

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	Stiffness = property(_get_Stiffness, None)
	'''
	Stiffness

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	Stiffness exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	ThresholdVelocity = property(_get_ThresholdVelocity, None)
	'''
	Threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseRDF = property(_get_UseRDF, _set_UseRDF)
	'''
	Use RDF

	:type: bool
	'''
	UseSpecialBoundaryPenetration = property(_get_UseSpecialBoundaryPenetration, _set_UseSpecialBoundaryPenetration)
	'''
	Use special boundary penetration

	:type: bool
	'''
	UseSpecialFrictionCoefficient = property(_get_UseSpecialFrictionCoefficient, _set_UseSpecialFrictionCoefficient)
	'''
	Use special friction coefficient

	:type: bool
	'''
	UseSpecialIndentationExponent = property(_get_UseSpecialIndentationExponent, _set_UseSpecialIndentationExponent)
	'''
	Use special indentation exponent

	:type: bool
	'''
	UseSpecialMaximumDamping = property(_get_UseSpecialMaximumDamping, _set_UseSpecialMaximumDamping)
	'''
	Use special maximum damping

	:type: bool
	'''
	UseSpecialRDF = property(_get_UseSpecialRDF, _set_UseSpecialRDF)
	'''
	Use special RDF

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
	UseSpecialThresholdVelocity = property(_get_UseSpecialThresholdVelocity, _set_UseSpecialThresholdVelocity)
	'''
	Use special threshold velocity

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactParameterType": _set_ContactParameterType,
		"_set_FrictionType": _set_FrictionType,
		"_set_UseRDF": _set_UseRDF,
		"_set_UseSpecialBoundaryPenetration": _set_UseSpecialBoundaryPenetration,
		"_set_UseSpecialFrictionCoefficient": _set_UseSpecialFrictionCoefficient,
		"_set_UseSpecialIndentationExponent": _set_UseSpecialIndentationExponent,
		"_set_UseSpecialMaximumDamping": _set_UseSpecialMaximumDamping,
		"_set_UseSpecialRDF": _set_UseSpecialRDF,
		"_set_UseSpecialStiffness": _set_UseSpecialStiffness,
		"_set_UseSpecialStiffnessExponent": _set_UseSpecialStiffnessExponent,
		"_set_UseSpecialThresholdVelocity": _set_UseSpecialThresholdVelocity,
	}
	_prop_map_get_ = {
		"BoundaryPenetration": (5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'),
		"FrictionCoefficient": (5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionFactorVertexofSheet": (5101, 2, (9, 0), (), "FrictionFactorVertexofSheet", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'),
		"GuideVelocity": (5051, 2, (9, 0), (), "GuideVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"IndentationExponent": (5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseRDF": (5024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (5025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (5008, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((5022, LCID, 4, 0),()),
		"FrictionType": ((5023, LCID, 4, 0),()),
		"UseRDF": ((5024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((5014, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((5018, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((5016, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((5012, LCID, 4, 0),()),
		"UseSpecialRDF": ((5025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((5008, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((5010, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((5020, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DContactPropertyRollerMovableToFixed(DispatchBaseClass):
	'''MTT3D movable roller contact property'''
	CLSID = IID('{8FD0551D-5E3C-428A-9944-CEAC08A575A7}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BoundaryPenetration(self):
		return self._ApplyTypes_(*(5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_OffsetPenetration(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "OffsetPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(5024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(5025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(5008, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((5022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((5023, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((5024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((5014, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((5018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((5016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((5012, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((5025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((5008, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5010, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((5020, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT3D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT3D.MTT3DFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	Indentation exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumDamping = property(_get_MaximumDamping, None)
	'''
	Maximum damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	OffsetPenetration = property(_get_OffsetPenetration, None)
	'''
	Offset penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	RDF = property(_get_RDF, None)
	'''
	RDF

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialBoundaryPenetration = property(_get_SpecialBoundaryPenetration, None)
	'''
	Special boundary penetration

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialFrictionCoefficient = property(_get_SpecialFrictionCoefficient, None)
	'''
	Special friction coefficient

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialIndentationExponent = property(_get_SpecialIndentationExponent, None)
	'''
	Special indentation exponent

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialMaximumDamping = property(_get_SpecialMaximumDamping, None)
	'''
	Special maximum damping

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialRDF = property(_get_SpecialRDF, None)
	'''
	Special RDF

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
	SpecialThresholdVelocity = property(_get_SpecialThresholdVelocity, None)
	'''
	Special threshold velocity

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	Stiffness = property(_get_Stiffness, None)
	'''
	Stiffness

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	Stiffness exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	ThresholdVelocity = property(_get_ThresholdVelocity, None)
	'''
	Threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseRDF = property(_get_UseRDF, _set_UseRDF)
	'''
	Use RDF

	:type: bool
	'''
	UseSpecialBoundaryPenetration = property(_get_UseSpecialBoundaryPenetration, _set_UseSpecialBoundaryPenetration)
	'''
	Use special boundary penetration

	:type: bool
	'''
	UseSpecialFrictionCoefficient = property(_get_UseSpecialFrictionCoefficient, _set_UseSpecialFrictionCoefficient)
	'''
	Use special friction coefficient

	:type: bool
	'''
	UseSpecialIndentationExponent = property(_get_UseSpecialIndentationExponent, _set_UseSpecialIndentationExponent)
	'''
	Use special indentation exponent

	:type: bool
	'''
	UseSpecialMaximumDamping = property(_get_UseSpecialMaximumDamping, _set_UseSpecialMaximumDamping)
	'''
	Use special maximum damping

	:type: bool
	'''
	UseSpecialRDF = property(_get_UseSpecialRDF, _set_UseSpecialRDF)
	'''
	Use special RDF

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
	UseSpecialThresholdVelocity = property(_get_UseSpecialThresholdVelocity, _set_UseSpecialThresholdVelocity)
	'''
	Use special threshold velocity

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactParameterType": _set_ContactParameterType,
		"_set_FrictionType": _set_FrictionType,
		"_set_UseRDF": _set_UseRDF,
		"_set_UseSpecialBoundaryPenetration": _set_UseSpecialBoundaryPenetration,
		"_set_UseSpecialFrictionCoefficient": _set_UseSpecialFrictionCoefficient,
		"_set_UseSpecialIndentationExponent": _set_UseSpecialIndentationExponent,
		"_set_UseSpecialMaximumDamping": _set_UseSpecialMaximumDamping,
		"_set_UseSpecialRDF": _set_UseSpecialRDF,
		"_set_UseSpecialStiffness": _set_UseSpecialStiffness,
		"_set_UseSpecialStiffnessExponent": _set_UseSpecialStiffnessExponent,
		"_set_UseSpecialThresholdVelocity": _set_UseSpecialThresholdVelocity,
	}
	_prop_map_get_ = {
		"BoundaryPenetration": (5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'),
		"FrictionCoefficient": (5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'),
		"IndentationExponent": (5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"OffsetPenetration": (5051, 2, (9, 0), (), "OffsetPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseRDF": (5024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (5025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (5008, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((5022, LCID, 4, 0),()),
		"FrictionType": ((5023, LCID, 4, 0),()),
		"UseRDF": ((5024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((5014, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((5018, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((5016, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((5012, LCID, 4, 0),()),
		"UseSpecialRDF": ((5025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((5008, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((5010, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((5020, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DContactPropertyRollerToSheet(DispatchBaseClass):
	'''MTT3D fixed roller contact property'''
	CLSID = IID('{24331496-FF71-42BC-AE6C-5C675546329B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BoundaryPenetration(self):
		return self._ApplyTypes_(*(5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_OverdriveFactor(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "OverdriveFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialOverdriveFactor(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "SpecialOverdriveFactor", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(5024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialOverdriveFactor(self):
		return self._ApplyTypes_(*(5052, 2, (11, 0), (), "UseSpecialOverdriveFactor", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(5025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(5008, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((5022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((5023, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((5024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((5014, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((5018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((5016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((5012, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialOverdriveFactor(self, value):
		if "UseSpecialOverdriveFactor" in self.__dict__: self.__dict__["UseSpecialOverdriveFactor"] = value; return
		self._oleobj_.Invoke(*((5052, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((5025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((5008, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5010, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((5020, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT3D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT3D.MTT3DFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	Indentation exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumDamping = property(_get_MaximumDamping, None)
	'''
	Maximum damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	OverdriveFactor = property(_get_OverdriveFactor, None)
	'''
	Over drive factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	RDF = property(_get_RDF, None)
	'''
	RDF

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialBoundaryPenetration = property(_get_SpecialBoundaryPenetration, None)
	'''
	Special boundary penetration

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialFrictionCoefficient = property(_get_SpecialFrictionCoefficient, None)
	'''
	Special friction coefficient

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialIndentationExponent = property(_get_SpecialIndentationExponent, None)
	'''
	Special indentation exponent

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialMaximumDamping = property(_get_SpecialMaximumDamping, None)
	'''
	Special maximum damping

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialOverdriveFactor = property(_get_SpecialOverdriveFactor, None)
	'''
	Special over drive factor

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialRDF = property(_get_SpecialRDF, None)
	'''
	Special RDF

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
	SpecialThresholdVelocity = property(_get_SpecialThresholdVelocity, None)
	'''
	Special threshold velocity

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	Stiffness = property(_get_Stiffness, None)
	'''
	Stiffness

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	Stiffness exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	ThresholdVelocity = property(_get_ThresholdVelocity, None)
	'''
	Threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseRDF = property(_get_UseRDF, _set_UseRDF)
	'''
	Use RDF

	:type: bool
	'''
	UseSpecialBoundaryPenetration = property(_get_UseSpecialBoundaryPenetration, _set_UseSpecialBoundaryPenetration)
	'''
	Use special boundary penetration

	:type: bool
	'''
	UseSpecialFrictionCoefficient = property(_get_UseSpecialFrictionCoefficient, _set_UseSpecialFrictionCoefficient)
	'''
	Use special friction coefficient

	:type: bool
	'''
	UseSpecialIndentationExponent = property(_get_UseSpecialIndentationExponent, _set_UseSpecialIndentationExponent)
	'''
	Use special indentation exponent

	:type: bool
	'''
	UseSpecialMaximumDamping = property(_get_UseSpecialMaximumDamping, _set_UseSpecialMaximumDamping)
	'''
	Use special maximum damping

	:type: bool
	'''
	UseSpecialOverdriveFactor = property(_get_UseSpecialOverdriveFactor, _set_UseSpecialOverdriveFactor)
	'''
	Use special over drive factor

	:type: bool
	'''
	UseSpecialRDF = property(_get_UseSpecialRDF, _set_UseSpecialRDF)
	'''
	Use special RDF

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
	UseSpecialThresholdVelocity = property(_get_UseSpecialThresholdVelocity, _set_UseSpecialThresholdVelocity)
	'''
	Use special threshold velocity

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactParameterType": _set_ContactParameterType,
		"_set_FrictionType": _set_FrictionType,
		"_set_UseRDF": _set_UseRDF,
		"_set_UseSpecialBoundaryPenetration": _set_UseSpecialBoundaryPenetration,
		"_set_UseSpecialFrictionCoefficient": _set_UseSpecialFrictionCoefficient,
		"_set_UseSpecialIndentationExponent": _set_UseSpecialIndentationExponent,
		"_set_UseSpecialMaximumDamping": _set_UseSpecialMaximumDamping,
		"_set_UseSpecialOverdriveFactor": _set_UseSpecialOverdriveFactor,
		"_set_UseSpecialRDF": _set_UseSpecialRDF,
		"_set_UseSpecialStiffness": _set_UseSpecialStiffness,
		"_set_UseSpecialStiffnessExponent": _set_UseSpecialStiffnessExponent,
		"_set_UseSpecialThresholdVelocity": _set_UseSpecialThresholdVelocity,
	}
	_prop_map_get_ = {
		"BoundaryPenetration": (5004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (5022, 2, (3, 0), (), "ContactParameterType", '{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}'),
		"FrictionCoefficient": (5006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (5023, 2, (3, 0), (), "FrictionType", '{596CA79D-118A-40BD-A43E-9174A181B2D8}'),
		"IndentationExponent": (5005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (5003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"OverdriveFactor": (5051, 2, (9, 0), (), "OverdriveFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (5027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (5015, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (5019, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (5017, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (5013, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialOverdriveFactor": (5053, 2, (9, 0), (), "SpecialOverdriveFactor", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (5026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (5009, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (5011, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (5021, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (5001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (5002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (5007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseRDF": (5024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (5014, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (5018, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (5016, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (5012, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialOverdriveFactor": (5052, 2, (11, 0), (), "UseSpecialOverdriveFactor", None),
		"UseSpecialRDF": (5025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (5008, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (5010, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (5020, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((5022, LCID, 4, 0),()),
		"FrictionType": ((5023, LCID, 4, 0),()),
		"UseRDF": ((5024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((5014, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((5018, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((5016, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((5012, LCID, 4, 0),()),
		"UseSpecialOverdriveFactor": ((5052, LCID, 4, 0),()),
		"UseSpecialRDF": ((5025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((5008, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((5010, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((5020, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DContactSheetShellToSphere(DispatchBaseClass):
	'''MTT3D sheet shell to sphere contact'''
	CLSID = IID('{B191A3BA-81B7-49F6-98B6-82BCA52931E2}')
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


	def _get_ActionSheet(self):
		return self._ApplyTypes_(*(5052, 2, (9, 0), (), "ActionSheet", '{170EFC31-8F09-46F5-8500-F888697C0581}'))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseSphere(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "BaseSphere", '{2122DEE7-EE07-4A20-9B49-5A9AF4599906}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertySheetToSphere(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "ContactPropertySheetToSphere", '{823B2FED-7C16-4336-A3D1-39241C0B06FB}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(5001, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
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
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(5004, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionSheet(self, value):
		if "ActionSheet" in self.__dict__: self.__dict__["ActionSheet"] = value; return
		self._oleobj_.Invoke(*((5052, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseSphere(self, value):
		if "BaseSphere" in self.__dict__: self.__dict__["BaseSphere"] = value; return
		self._oleobj_.Invoke(*((5051, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionSheet = property(_get_ActionSheet, _set_ActionSheet)
	'''
	Action sheet

	:type: recurdyn.MTT3D.IMTT3DSheetShell
	'''
	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseSphere = property(_get_BaseSphere, _set_BaseSphere)
	'''
	Base entity

	:type: recurdyn.ProcessNet.IGeometrySphere
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPropertySheetToSphere = property(_get_ContactPropertySheetToSphere, None)
	'''
	The contact parameters of contact forces applied between sheet and sphere

	:type: recurdyn.MTT3D.IMTT3DContactProperty
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
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
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ActionSheet": _set_ActionSheet,
		"_set_Active": _set_Active,
		"_set_BaseSphere": _set_BaseSphere,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionSheet": (5052, 2, (9, 0), (), "ActionSheet", '{170EFC31-8F09-46F5-8500-F888697C0581}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseSphere": (5051, 2, (9, 0), (), "BaseSphere", '{2122DEE7-EE07-4A20-9B49-5A9AF4599906}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (5002, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertySheetToSphere": (5053, 2, (9, 0), (), "ContactPropertySheetToSphere", '{823B2FED-7C16-4336-A3D1-39241C0B06FB}'),
		"ForceDisplay": (5001, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SpecialContactPoints": (5003, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseSpecialContactPoints": (5004, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionSheet": ((5052, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseSphere": ((5051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((5001, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((5004, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DContactSheetShellToSurface(DispatchBaseClass):
	'''MTT3D sheet shell to surface contact'''
	CLSID = IID('{4D07ACD7-CCD0-4A1A-BA53-41F090095E0E}')
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


	def _get_ActionSheet(self):
		return self._ApplyTypes_(*(5055, 2, (9, 0), (), "ActionSheet", '{170EFC31-8F09-46F5-8500-F888697C0581}'))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BasePatchOption(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "BasePatchOption", '{ED5F7902-56FD-482D-AEF2-D898A1EBFF1B}'))
	def _get_BaseSurface(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "BaseSurface", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertySheetToSurface(self):
		return self._ApplyTypes_(*(5058, 2, (9, 0), (), "ContactPropertySheetToSurface", '{823B2FED-7C16-4336-A3D1-39241C0B06FB}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(5001, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
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
	def _get_SheetNormalDirection(self):
		return self._ApplyTypes_(*(5056, 2, (3, 0), (), "SheetNormalDirection", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SurfaceNormalDirection(self):
		return self._ApplyTypes_(*(5052, 2, (3, 0), (), "SurfaceNormalDirection", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}'))
	def _get_UseCheckVertex(self):
		return self._ApplyTypes_(*(5054, 2, (11, 0), (), "UseCheckVertex", None))
	def _get_UsePatchSetSearchAlgorithm(self):
		return self._ApplyTypes_(*(5057, 2, (11, 0), (), "UsePatchSetSearchAlgorithm", None))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(5004, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionSheet(self, value):
		if "ActionSheet" in self.__dict__: self.__dict__["ActionSheet"] = value; return
		self._oleobj_.Invoke(*((5055, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseSurface(self, value):
		if "BaseSurface" in self.__dict__: self.__dict__["BaseSurface"] = value; return
		self._oleobj_.Invoke(*((5051, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_SheetNormalDirection(self, value):
		if "SheetNormalDirection" in self.__dict__: self.__dict__["SheetNormalDirection"] = value; return
		self._oleobj_.Invoke(*((5056, LCID, 4, 0) + (value,) + ()))
	def _set_SurfaceNormalDirection(self, value):
		if "SurfaceNormalDirection" in self.__dict__: self.__dict__["SurfaceNormalDirection"] = value; return
		self._oleobj_.Invoke(*((5052, LCID, 4, 0) + (value,) + ()))
	def _set_UseCheckVertex(self, value):
		if "UseCheckVertex" in self.__dict__: self.__dict__["UseCheckVertex"] = value; return
		self._oleobj_.Invoke(*((5054, LCID, 4, 0) + (value,) + ()))
	def _set_UsePatchSetSearchAlgorithm(self, value):
		if "UsePatchSetSearchAlgorithm" in self.__dict__: self.__dict__["UsePatchSetSearchAlgorithm"] = value; return
		self._oleobj_.Invoke(*((5057, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionSheet = property(_get_ActionSheet, _set_ActionSheet)
	'''
	Action sheet

	:type: recurdyn.MTT3D.IMTT3DSheetShell
	'''
	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BasePatchOption = property(_get_BasePatchOption, None)
	'''
	Base Patch Option

	:type: recurdyn.ProcessNet.IContactExtendedSurfaceToSurfacePatchOption
	'''
	BaseSurface = property(_get_BaseSurface, _set_BaseSurface)
	'''
	Base entity

	:type: recurdyn.ProcessNet.IGeometry
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPropertySheetToSurface = property(_get_ContactPropertySheetToSurface, None)
	'''
	The contact parameters of contact forces applied between sheet and surface

	:type: recurdyn.MTT3D.IMTT3DContactProperty
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
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
	SheetNormalDirection = property(_get_SheetNormalDirection, _set_SheetNormalDirection)
	'''
	Sheet normal Direction

	:type: recurdyn.ProcessNet.NormalDirection
	'''
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SurfaceNormalDirection = property(_get_SurfaceNormalDirection, _set_SurfaceNormalDirection)
	'''
	Surface normal Direction

	:type: recurdyn.ProcessNet.NormalDirection
	'''
	UseCheckVertex = property(_get_UseCheckVertex, _set_UseCheckVertex)
	'''
	Use check vertex

	:type: bool
	'''
	UsePatchSetSearchAlgorithm = property(_get_UsePatchSetSearchAlgorithm, _set_UsePatchSetSearchAlgorithm)
	'''
	Use patch set search algorithm

	:type: bool
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ActionSheet": _set_ActionSheet,
		"_set_Active": _set_Active,
		"_set_BaseSurface": _set_BaseSurface,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_SheetNormalDirection": _set_SheetNormalDirection,
		"_set_SurfaceNormalDirection": _set_SurfaceNormalDirection,
		"_set_UseCheckVertex": _set_UseCheckVertex,
		"_set_UsePatchSetSearchAlgorithm": _set_UsePatchSetSearchAlgorithm,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionSheet": (5055, 2, (9, 0), (), "ActionSheet", '{170EFC31-8F09-46F5-8500-F888697C0581}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BasePatchOption": (5053, 2, (9, 0), (), "BasePatchOption", '{ED5F7902-56FD-482D-AEF2-D898A1EBFF1B}'),
		"BaseSurface": (5051, 2, (9, 0), (), "BaseSurface", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (5002, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertySheetToSurface": (5058, 2, (9, 0), (), "ContactPropertySheetToSurface", '{823B2FED-7C16-4336-A3D1-39241C0B06FB}'),
		"ForceDisplay": (5001, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SheetNormalDirection": (5056, 2, (3, 0), (), "SheetNormalDirection", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}'),
		"SpecialContactPoints": (5003, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SurfaceNormalDirection": (5052, 2, (3, 0), (), "SurfaceNormalDirection", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}'),
		"UseCheckVertex": (5054, 2, (11, 0), (), "UseCheckVertex", None),
		"UsePatchSetSearchAlgorithm": (5057, 2, (11, 0), (), "UsePatchSetSearchAlgorithm", None),
		"UseSpecialContactPoints": (5004, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionSheet": ((5055, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseSurface": ((5051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((5001, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"SheetNormalDirection": ((5056, LCID, 4, 0),()),
		"SurfaceNormalDirection": ((5052, LCID, 4, 0),()),
		"UseCheckVertex": ((5054, LCID, 4, 0),()),
		"UsePatchSetSearchAlgorithm": ((5057, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((5004, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DContactSheetShellToTorus(DispatchBaseClass):
	'''MTT3D sheet shell to torus contact'''
	CLSID = IID('{80C8B0D7-D377-4A6C-AB06-7DD13758F1EA}')
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


	def _get_ActionSheet(self):
		return self._ApplyTypes_(*(5052, 2, (9, 0), (), "ActionSheet", '{170EFC31-8F09-46F5-8500-F888697C0581}'))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseTorus(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "BaseTorus", '{92A1D6C1-1B9F-4A5A-AA3E-164073FAA5FB}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertySheetToTorus(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "ContactPropertySheetToTorus", '{823B2FED-7C16-4336-A3D1-39241C0B06FB}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(5001, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
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
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(5004, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionSheet(self, value):
		if "ActionSheet" in self.__dict__: self.__dict__["ActionSheet"] = value; return
		self._oleobj_.Invoke(*((5052, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseTorus(self, value):
		if "BaseTorus" in self.__dict__: self.__dict__["BaseTorus"] = value; return
		self._oleobj_.Invoke(*((5051, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionSheet = property(_get_ActionSheet, _set_ActionSheet)
	'''
	Action sheet

	:type: recurdyn.MTT3D.IMTT3DSheetShell
	'''
	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseTorus = property(_get_BaseTorus, _set_BaseTorus)
	'''
	Base entity

	:type: recurdyn.ProcessNet.IGeometryTorus
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPropertySheetToTorus = property(_get_ContactPropertySheetToTorus, None)
	'''
	The contact parameters of contact forces applied between sheet and torus

	:type: recurdyn.MTT3D.IMTT3DContactProperty
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
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
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ActionSheet": _set_ActionSheet,
		"_set_Active": _set_Active,
		"_set_BaseTorus": _set_BaseTorus,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionSheet": (5052, 2, (9, 0), (), "ActionSheet", '{170EFC31-8F09-46F5-8500-F888697C0581}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseTorus": (5051, 2, (9, 0), (), "BaseTorus", '{92A1D6C1-1B9F-4A5A-AA3E-164073FAA5FB}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (5002, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertySheetToTorus": (5053, 2, (9, 0), (), "ContactPropertySheetToTorus", '{823B2FED-7C16-4336-A3D1-39241C0B06FB}'),
		"ForceDisplay": (5001, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SpecialContactPoints": (5003, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseSpecialContactPoints": (5004, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionSheet": ((5052, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseTorus": ((5051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((5001, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((5004, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DCrownRollerProfile(DispatchBaseClass):
	'''MTT3D crown roller information'''
	CLSID = IID('{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Add(self, dX, dY, dR):
		'''
		Add data
		
		:param dX: float
		:param dY: float
		:param dR: float
		'''
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1)),dX
			, dY, dR)


	def Clear(self):
		'''
		Clear data
		'''
		return self._oleobj_.InvokeTypes(53, LCID, 1, (24, 0), (),)


	def Export(self, strFullPathName):
		'''
		Export a file
		
		:param strFullPathName: str
		'''
		return self._oleobj_.InvokeTypes(55, LCID, 1, (24, 0), ((8, 1),),strFullPathName
			)


	def Import(self, strFullPathName):
		'''
		Import a file
		
		:param strFullPathName: str
		'''
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), ((8, 1),),strFullPathName
			)


	def _get_ProfileCollection(self):
		return self._ApplyTypes_(*(51, 2, (9, 0), (), "ProfileCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	ProfileCollection = property(_get_ProfileCollection, None)
	'''
	Profile Collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"ProfileCollection": (51, 2, (9, 0), (), "ProfileCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DFixedRollerGroupCollection(DispatchBaseClass):
	'''IMTT3DFixedRollerGroupCollection'''
	CLSID = IID('{4DDDBBAF-DC04-42B6-B745-E8C5BB0CB2C2}')
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
		:rtype: recurdyn.MTT3D.IMTT3DGroupFixedRoller
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')
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
		:rtype: recurdyn.MTT3D.IMTT3DGroupFixedRoller
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')
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
		return win32com.client.util.Iterator(ob, '{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT3DForceNodal(DispatchBaseClass):
	'''MTT3D nodal force'''
	CLSID = IID('{0F707193-3BDD-4899-8FD9-E9C21739ECD0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetAppliedBody(self, uiID):
		'''
		Specifies whether nodal force is applied to a node
		
		:param uiID: int
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(5053, LCID, 1, (11, 0), ((19, 1),),uiID
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def SetAppliedBody(self, uiID, vBool):
		'''
		Applies nodal force to a node
		
		:param uiID: int
		:param vBool: bool
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(5052, LCID, 1, (11, 0), ((19, 1), (11, 1)),uiID
			, vBool)


	def SetAppliedBodyAll(self, flag):
		'''
		Applies nodal force to all nodes
		
		:param flag: bool
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(5054, LCID, 1, (11, 0), ((11, 1),),flag
			)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(5055, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
	def _get_ReportNodeIDs(self):
		return self._ApplyTypes_(*(5057, 2, (8195, 0), (), "ReportNodeIDs", None))
	def _get_UseReportNodes(self):
		return self._ApplyTypes_(*(5056, 2, (11, 0), (), "UseReportNodes", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_UserSubroutine(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((5055, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ReportNodeIDs(self, value):
		if "ReportNodeIDs" in self.__dict__: self.__dict__["ReportNodeIDs"] = value; return
		variantValue = win32com.client.VARIANT(8195, value)
		self._oleobj_.Invoke(*((5057, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseReportNodes(self, value):
		if "UseReportNodes" in self.__dict__: self.__dict__["UseReportNodes"] = value; return
		self._oleobj_.Invoke(*((5056, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_UserSubroutine(self, value):
		if "UserSubroutine" in self.__dict__: self.__dict__["UserSubroutine"] = value; return
		self._oleobj_.Invoke(*((5051, LCID, 4, 0) + (value,) + ()))

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
		"_set_ReportNodeIDs": _set_ReportNodeIDs,
		"_set_UseReportNodes": _set_UseReportNodes,
		"_set_UserData": _set_UserData,
		"_set_UserSubroutine": _set_UserSubroutine,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (5055, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ReportNodeIDs": (5057, 2, (8195, 0), (), "ReportNodeIDs", None),
		"UseReportNodes": (5056, 2, (11, 0), (), "UseReportNodes", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"UserSubroutine": (5051, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((5055, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ReportNodeIDs": ((5057, LCID, 4, 0),()),
		"UseReportNodes": ((5056, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"UserSubroutine": ((5051, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DForceNodalCollection(DispatchBaseClass):
	'''IForceNodalCollection'''
	CLSID = IID('{6B16FDF1-2281-424C-8A58-20633C8C31E6}')
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
		:rtype: recurdyn.MTT3D.IMTT3DForceNodal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0F707193-3BDD-4899-8FD9-E9C21739ECD0}')
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
		:rtype: recurdyn.MTT3D.IMTT3DForceNodal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0F707193-3BDD-4899-8FD9-E9C21739ECD0}')
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
		return win32com.client.util.Iterator(ob, '{0F707193-3BDD-4899-8FD9-E9C21739ECD0}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{0F707193-3BDD-4899-8FD9-E9C21739ECD0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT3DForceSpring(DispatchBaseClass):
	'''MTT3D spring force'''
	CLSID = IID('{1C0C8EF0-71D3-495B-BA60-3168D6F5F29A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CopyActionToBase(self, Type):
		'''
		Copy action to base
		
		:param Type: CopyMarkerType
		'''
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), ((3, 1),),Type
			)


	def CopyBaseToAction(self, Type):
		'''
		Copy base to action
		
		:param Type: CopyMarkerType
		'''
		return self._oleobj_.InvokeTypes(205, LCID, 1, (24, 0), ((3, 1),),Type
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_ActionMarker(self):
		return self._ApplyTypes_(*(203, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_BaseMarker(self):
		return self._ApplyTypes_(*(202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Damping(self):
		return self._ApplyTypes_(*(256, 2, (9, 0), (), "Damping", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayColor(self):
		return self._ApplyTypes_(*(207, 2, (19, 0), (), "ForceDisplayColor", None))
	def _get_ForceDisplayUse(self):
		return self._ApplyTypes_(*(209, 2, (11, 0), (), "ForceDisplayUse", None))
	def _get_FreeLength(self):
		return self._ApplyTypes_(*(253, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerName(self):
		return self._ApplyTypes_(*(204, 2, (8, 0), (), "LayerName", None))
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
	def _get_Preload(self):
		return self._ApplyTypes_(*(254, 2, (9, 0), (), "Preload", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialDamping(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPreload(self):
		return self._ApplyTypes_(*(5007, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpringGraphic(self):
		return self._ApplyTypes_(*(252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_UseSpecialDamping(self):
		return self._ApplyTypes_(*(5003, 2, (11, 0), (), "UseSpecialDamping", None))
	def _get_UseSpecialPreload(self):
		return self._ApplyTypes_(*(5004, 2, (11, 0), (), "UseSpecialPreload", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(5002, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionMarker(self, value):
		if "ActionMarker" in self.__dict__: self.__dict__["ActionMarker"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_BaseMarker(self, value):
		if "BaseMarker" in self.__dict__: self.__dict__["BaseMarker"] = value; return
		self._oleobj_.Invoke(*((202, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((201, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayColor(self, value):
		if "ForceDisplayColor" in self.__dict__: self.__dict__["ForceDisplayColor"] = value; return
		self._oleobj_.Invoke(*((207, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayUse(self, value):
		if "ForceDisplayUse" in self.__dict__: self.__dict__["ForceDisplayUse"] = value; return
		self._oleobj_.Invoke(*((209, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_TorqueDisplayColor(self, value):
		if "TorqueDisplayColor" in self.__dict__: self.__dict__["TorqueDisplayColor"] = value; return
		self._oleobj_.Invoke(*((208, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDamping(self, value):
		if "UseSpecialDamping" in self.__dict__: self.__dict__["UseSpecialDamping"] = value; return
		self._oleobj_.Invoke(*((5003, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPreload(self, value):
		if "UseSpecialPreload" in self.__dict__: self.__dict__["UseSpecialPreload"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((5002, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionMarker = property(_get_ActionMarker, _set_ActionMarker)
	'''
	Action marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseBody = property(_get_BaseBody, _set_BaseBody)
	'''
	Base body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	BaseMarker = property(_get_BaseMarker, _set_BaseMarker)
	'''
	Base marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Damping = property(_get_Damping, None)
	'''
	Damping

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	ForceDisplayColor = property(_get_ForceDisplayColor, _set_ForceDisplayColor)
	'''
	Force display color

	:type: int
	'''
	ForceDisplayUse = property(_get_ForceDisplayUse, _set_ForceDisplayUse)
	'''
	Force display use

	:type: bool
	'''
	FreeLength = property(_get_FreeLength, None)
	'''
	The free length of the spring

	:type: recurdyn.ProcessNet.IDouble
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	LayerName = property(_get_LayerName, None)
	'''
	Layer name

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
	Preload = property(_get_Preload, None)
	'''
	The preload of the spring

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialDamping = property(_get_SpecialDamping, None)
	'''
	Special damping

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialPreload = property(_get_SpecialPreload, None)
	'''
	Special preload

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialStiffness = property(_get_SpecialStiffness, None)
	'''
	Special stiffness

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpringGraphic = property(_get_SpringGraphic, None)
	'''
	Spring force graphic

	:type: recurdyn.ProcessNet.IForceSpringGraphic
	'''
	Stiffness = property(_get_Stiffness, None)
	'''
	Stiffness

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	TorqueDisplayColor = property(_get_TorqueDisplayColor, _set_TorqueDisplayColor)
	'''
	Torque display color

	:type: int
	'''
	UseSpecialDamping = property(_get_UseSpecialDamping, _set_UseSpecialDamping)
	'''
	Use special damping

	:type: bool
	'''
	UseSpecialPreload = property(_get_UseSpecialPreload, _set_UseSpecialPreload)
	'''
	Use special preload

	:type: bool
	'''
	UseSpecialStiffness = property(_get_UseSpecialStiffness, _set_UseSpecialStiffness)
	'''
	Use special stiffness

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ActionMarker": _set_ActionMarker,
		"_set_Active": _set_Active,
		"_set_BaseBody": _set_BaseBody,
		"_set_BaseMarker": _set_BaseMarker,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_ForceDisplayColor": _set_ForceDisplayColor,
		"_set_ForceDisplayUse": _set_ForceDisplayUse,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_TorqueDisplayColor": _set_TorqueDisplayColor,
		"_set_UseSpecialDamping": _set_UseSpecialDamping,
		"_set_UseSpecialPreload": _set_UseSpecialPreload,
		"_set_UseSpecialStiffness": _set_UseSpecialStiffness,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionMarker": (203, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (5001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"BaseMarker": (202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Damping": (256, 2, (9, 0), (), "Damping", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"ForceDisplay": (201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayColor": (207, 2, (19, 0), (), "ForceDisplayColor", None),
		"ForceDisplayUse": (209, 2, (11, 0), (), "ForceDisplayUse", None),
		"FreeLength": (253, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerName": (204, 2, (8, 0), (), "LayerName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Preload": (254, 2, (9, 0), (), "Preload", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialDamping": (5006, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPreload": (5007, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (5005, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpringGraphic": (252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'),
		"Stiffness": (255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TorqueDisplayColor": (208, 2, (19, 0), (), "TorqueDisplayColor", None),
		"UseSpecialDamping": (5003, 2, (11, 0), (), "UseSpecialDamping", None),
		"UseSpecialPreload": (5004, 2, (11, 0), (), "UseSpecialPreload", None),
		"UseSpecialStiffness": (5002, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionMarker": ((203, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((5001, LCID, 4, 0),()),
		"BaseMarker": ((202, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((207, LCID, 4, 0),()),
		"ForceDisplayUse": ((209, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((208, LCID, 4, 0),()),
		"UseSpecialDamping": ((5003, LCID, 4, 0),()),
		"UseSpecialPreload": ((5004, LCID, 4, 0),()),
		"UseSpecialStiffness": ((5002, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DForceSpringNip(DispatchBaseClass):
	'''MTT3D nip spring force'''
	CLSID = IID('{E8BD4F07-0B25-44C6-9B8E-0905A9EAE731}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CopyActionToBase(self, Type):
		'''
		Copy action to base
		
		:param Type: CopyMarkerType
		'''
		return self._oleobj_.InvokeTypes(206, LCID, 1, (24, 0), ((3, 1),),Type
			)


	def CopyBaseToAction(self, Type):
		'''
		Copy base to action
		
		:param Type: CopyMarkerType
		'''
		return self._oleobj_.InvokeTypes(205, LCID, 1, (24, 0), ((3, 1),),Type
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_ActionMarker(self):
		return self._ApplyTypes_(*(203, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_BaseMarker(self):
		return self._ApplyTypes_(*(202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_BasePoint(self):
		return self._ApplyTypes_(*(5051, 2, (8197, 0), (), "BasePoint", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Damping(self):
		return self._ApplyTypes_(*(256, 2, (9, 0), (), "Damping", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayColor(self):
		return self._ApplyTypes_(*(207, 2, (19, 0), (), "ForceDisplayColor", None))
	def _get_ForceDisplayUse(self):
		return self._ApplyTypes_(*(209, 2, (11, 0), (), "ForceDisplayUse", None))
	def _get_FreeLength(self):
		return self._ApplyTypes_(*(253, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerName(self):
		return self._ApplyTypes_(*(204, 2, (8, 0), (), "LayerName", None))
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
	def _get_Preload(self):
		return self._ApplyTypes_(*(254, 2, (9, 0), (), "Preload", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialDamping(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPreload(self):
		return self._ApplyTypes_(*(5007, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpringGraphic(self):
		return self._ApplyTypes_(*(252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_UseBasePoint(self):
		return self._ApplyTypes_(*(5052, 2, (11, 0), (), "UseBasePoint", None))
	def _get_UseSpecialDamping(self):
		return self._ApplyTypes_(*(5003, 2, (11, 0), (), "UseSpecialDamping", None))
	def _get_UseSpecialPreload(self):
		return self._ApplyTypes_(*(5004, 2, (11, 0), (), "UseSpecialPreload", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(5002, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionMarker(self, value):
		if "ActionMarker" in self.__dict__: self.__dict__["ActionMarker"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_BaseMarker(self, value):
		if "BaseMarker" in self.__dict__: self.__dict__["BaseMarker"] = value; return
		self._oleobj_.Invoke(*((202, LCID, 4, 0) + (value,) + ()))
	def _set_BasePoint(self, value):
		if "BasePoint" in self.__dict__: self.__dict__["BasePoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5051, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((201, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayColor(self, value):
		if "ForceDisplayColor" in self.__dict__: self.__dict__["ForceDisplayColor"] = value; return
		self._oleobj_.Invoke(*((207, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayUse(self, value):
		if "ForceDisplayUse" in self.__dict__: self.__dict__["ForceDisplayUse"] = value; return
		self._oleobj_.Invoke(*((209, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_TorqueDisplayColor(self, value):
		if "TorqueDisplayColor" in self.__dict__: self.__dict__["TorqueDisplayColor"] = value; return
		self._oleobj_.Invoke(*((208, LCID, 4, 0) + (value,) + ()))
	def _set_UseBasePoint(self, value):
		if "UseBasePoint" in self.__dict__: self.__dict__["UseBasePoint"] = value; return
		self._oleobj_.Invoke(*((5052, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDamping(self, value):
		if "UseSpecialDamping" in self.__dict__: self.__dict__["UseSpecialDamping"] = value; return
		self._oleobj_.Invoke(*((5003, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPreload(self, value):
		if "UseSpecialPreload" in self.__dict__: self.__dict__["UseSpecialPreload"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((5002, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionMarker = property(_get_ActionMarker, _set_ActionMarker)
	'''
	Action marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseBody = property(_get_BaseBody, _set_BaseBody)
	'''
	Base body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	BaseMarker = property(_get_BaseMarker, _set_BaseMarker)
	'''
	Base marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	BasePoint = property(_get_BasePoint, _set_BasePoint)
	'''
	Base point

	:type: list[float]
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Damping = property(_get_Damping, None)
	'''
	Damping

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	ForceDisplayColor = property(_get_ForceDisplayColor, _set_ForceDisplayColor)
	'''
	Force display color

	:type: int
	'''
	ForceDisplayUse = property(_get_ForceDisplayUse, _set_ForceDisplayUse)
	'''
	Force display use

	:type: bool
	'''
	FreeLength = property(_get_FreeLength, None)
	'''
	The free length of the spring

	:type: recurdyn.ProcessNet.IDouble
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	LayerName = property(_get_LayerName, None)
	'''
	Layer name

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
	Preload = property(_get_Preload, None)
	'''
	The preload of the spring

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialDamping = property(_get_SpecialDamping, None)
	'''
	Special damping

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialPreload = property(_get_SpecialPreload, None)
	'''
	Special preload

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialStiffness = property(_get_SpecialStiffness, None)
	'''
	Special stiffness

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpringGraphic = property(_get_SpringGraphic, None)
	'''
	Spring force graphic

	:type: recurdyn.ProcessNet.IForceSpringGraphic
	'''
	Stiffness = property(_get_Stiffness, None)
	'''
	Stiffness

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	TorqueDisplayColor = property(_get_TorqueDisplayColor, _set_TorqueDisplayColor)
	'''
	Torque display color

	:type: int
	'''
	UseBasePoint = property(_get_UseBasePoint, _set_UseBasePoint)
	'''
	Use base point

	:type: bool
	'''
	UseSpecialDamping = property(_get_UseSpecialDamping, _set_UseSpecialDamping)
	'''
	Use special damping

	:type: bool
	'''
	UseSpecialPreload = property(_get_UseSpecialPreload, _set_UseSpecialPreload)
	'''
	Use special preload

	:type: bool
	'''
	UseSpecialStiffness = property(_get_UseSpecialStiffness, _set_UseSpecialStiffness)
	'''
	Use special stiffness

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ActionMarker": _set_ActionMarker,
		"_set_Active": _set_Active,
		"_set_BaseBody": _set_BaseBody,
		"_set_BaseMarker": _set_BaseMarker,
		"_set_BasePoint": _set_BasePoint,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_ForceDisplayColor": _set_ForceDisplayColor,
		"_set_ForceDisplayUse": _set_ForceDisplayUse,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_TorqueDisplayColor": _set_TorqueDisplayColor,
		"_set_UseBasePoint": _set_UseBasePoint,
		"_set_UseSpecialDamping": _set_UseSpecialDamping,
		"_set_UseSpecialPreload": _set_UseSpecialPreload,
		"_set_UseSpecialStiffness": _set_UseSpecialStiffness,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionMarker": (203, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (5001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"BaseMarker": (202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"BasePoint": (5051, 2, (8197, 0), (), "BasePoint", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Damping": (256, 2, (9, 0), (), "Damping", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"ForceDisplay": (201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayColor": (207, 2, (19, 0), (), "ForceDisplayColor", None),
		"ForceDisplayUse": (209, 2, (11, 0), (), "ForceDisplayUse", None),
		"FreeLength": (253, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerName": (204, 2, (8, 0), (), "LayerName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Preload": (254, 2, (9, 0), (), "Preload", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialDamping": (5006, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPreload": (5007, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (5005, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpringGraphic": (252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'),
		"Stiffness": (255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TorqueDisplayColor": (208, 2, (19, 0), (), "TorqueDisplayColor", None),
		"UseBasePoint": (5052, 2, (11, 0), (), "UseBasePoint", None),
		"UseSpecialDamping": (5003, 2, (11, 0), (), "UseSpecialDamping", None),
		"UseSpecialPreload": (5004, 2, (11, 0), (), "UseSpecialPreload", None),
		"UseSpecialStiffness": (5002, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionMarker": ((203, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((5001, LCID, 4, 0),()),
		"BaseMarker": ((202, LCID, 4, 0),()),
		"BasePoint": ((5051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((207, LCID, 4, 0),()),
		"ForceDisplayUse": ((209, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((208, LCID, 4, 0),()),
		"UseBasePoint": ((5052, LCID, 4, 0),()),
		"UseSpecialDamping": ((5003, LCID, 4, 0),()),
		"UseSpecialPreload": ((5004, LCID, 4, 0),()),
		"UseSpecialStiffness": ((5002, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DGroupFixedRoller(DispatchBaseClass):
	'''MTT3D fixed roller group'''
	CLSID = IID('{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')
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


	def SetLayerNumber(self, iVal):
		'''
		Set layer Number
		
		:param iVal: int
		'''
		return self._oleobj_.InvokeTypes(202, LCID, 1, (24, 0), ((19, 1),),iVal
			)


	def UpdateActiveFlagOfAllEntities(self, Val):
		'''
		Update active flag of all entities
		
		:param Val: bool
		'''
		return self._oleobj_.InvokeTypes(204, LCID, 1, (24, 0), ((11, 1),),Val
			)


	def UpdateAllProperties(self):
		'''
		Update all properties
		'''
		return self._oleobj_.InvokeTypes(201, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_CenterPoint(self):
		return self._ApplyTypes_(*(5052, 2, (8197, 0), (), "CenterPoint", None))
	def _get_CenterPoint2(self):
		return self._ApplyTypes_(*(5074, 2, (9, 0), (), "CenterPoint2", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(5076, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(5065, 2, (9, 0), (), "ContactPropertyToSheet", '{24331496-FF71-42BC-AE6C-5C675546329B}'))
	def _get_CrownRollerProfile(self):
		return self._ApplyTypes_(*(5072, 2, (9, 0), (), "CrownRollerProfile", '{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}'))
	def _get_Depth(self):
		return self._ApplyTypes_(*(5058, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DepthDirection(self):
		return self._ApplyTypes_(*(5054, 2, (8197, 0), (), "DepthDirection", None))
	def _get_DirectionPoint(self):
		return self._ApplyTypes_(*(5055, 2, (8197, 0), (), "DirectionPoint", None))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(5075, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(5060, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(5061, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(5062, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Mass(self):
		return self._ApplyTypes_(*(5059, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Motion(self):
		return self._ApplyTypes_(*(5064, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'))
	def _get_MultipleRollerInfo(self):
		return self._ApplyTypes_(*(5073, 2, (9, 0), (), "MultipleRollerInfo", '{786C632D-A3A2-4FC7-9C31-F6EF4DB35EC7}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(5057, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ReferencePoint(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_RevJoint(self):
		return self._ApplyTypes_(*(5068, 2, (9, 0), (), "RevJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_RollerBody(self):
		return self._ApplyTypes_(*(5067, 2, (9, 0), (), "RollerBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_RollerType(self):
		return self._ApplyTypes_(*(5071, 2, (3, 0), (), "RollerType", '{4FD105DB-485D-4AC8-80FE-B163BDB06C37}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(5077, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseAutoCenterMarker(self):
		return self._ApplyTypes_(*(5066, 2, (11, 0), (), "UseAutoCenterMarker", None))
	def _get_UseAutoJointPosition(self):
		return self._ApplyTypes_(*(5069, 2, (11, 0), (), "UseAutoJointPosition", None))
	def _get_UseCenterPoint(self):
		return self._ApplyTypes_(*(5056, 2, (11, 0), (), "UseCenterPoint", None))
	def _get_UseCheckEdge(self):
		return self._ApplyTypes_(*(5070, 2, (11, 0), (), "UseCheckEdge", None))
	def _get_UseMotion(self):
		return self._ApplyTypes_(*(5063, 2, (11, 0), (), "UseMotion", None))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(5078, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((5051, LCID, 4, 0) + (value,) + ()))
	def _set_CenterPoint(self, value):
		if "CenterPoint" in self.__dict__: self.__dict__["CenterPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5052, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DepthDirection(self, value):
		if "DepthDirection" in self.__dict__: self.__dict__["DepthDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5054, LCID, 4, 0) + (variantValue,) + ()))
	def _set_DirectionPoint(self, value):
		if "DirectionPoint" in self.__dict__: self.__dict__["DirectionPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5055, LCID, 4, 0) + (variantValue,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((5075, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_RollerType(self, value):
		if "RollerType" in self.__dict__: self.__dict__["RollerType"] = value; return
		self._oleobj_.Invoke(*((5071, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoCenterMarker(self, value):
		if "UseAutoCenterMarker" in self.__dict__: self.__dict__["UseAutoCenterMarker"] = value; return
		self._oleobj_.Invoke(*((5066, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoJointPosition(self, value):
		if "UseAutoJointPosition" in self.__dict__: self.__dict__["UseAutoJointPosition"] = value; return
		self._oleobj_.Invoke(*((5069, LCID, 4, 0) + (value,) + ()))
	def _set_UseCenterPoint(self, value):
		if "UseCenterPoint" in self.__dict__: self.__dict__["UseCenterPoint"] = value; return
		self._oleobj_.Invoke(*((5056, LCID, 4, 0) + (value,) + ()))
	def _set_UseCheckEdge(self, value):
		if "UseCheckEdge" in self.__dict__: self.__dict__["UseCheckEdge"] = value; return
		self._oleobj_.Invoke(*((5070, LCID, 4, 0) + (value,) + ()))
	def _set_UseMotion(self, value):
		if "UseMotion" in self.__dict__: self.__dict__["UseMotion"] = value; return
		self._oleobj_.Invoke(*((5063, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((5078, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseBody = property(_get_BaseBody, _set_BaseBody)
	'''
	The base body of the revolute joint

	:type: recurdyn.ProcessNet.IGeneric
	'''
	CenterPoint = property(_get_CenterPoint, _set_CenterPoint)
	'''
	The center point of the fixed roller body

	:type: list[float]
	'''
	CenterPoint2 = property(_get_CenterPoint2, None)
	'''
	The center point of the fixed roller body

	:type: recurdyn.ProcessNet.IVector
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPropertyToSheet = property(_get_ContactPropertyToSheet, None)
	'''
	The parameters of contact forces applied between sheet and fixed roller

	:type: recurdyn.MTT3D.IMTT3DContactPropertyRollerToSheet
	'''
	CrownRollerProfile = property(_get_CrownRollerProfile, None)
	'''
	CrownRoller Profile

	:type: recurdyn.MTT3D.IMTT3DCrownRollerProfile
	'''
	Depth = property(_get_Depth, None)
	'''
	The depth of the fixed roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	DepthDirection = property(_get_DepthDirection, _set_DepthDirection)
	'''
	The depth direction at the center point of fixed roller

	:type: list[float]
	'''
	DirectionPoint = property(_get_DirectionPoint, _set_DirectionPoint)
	'''
	The direction point at the reference point of fixed roller

	:type: list[float]
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx, the mass moment of inertia in the x-axis of the roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy, the mass moment of inertia in the y-axis of the roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz, the mass moment of inertia in the z-axis of the roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	Mass = property(_get_Mass, None)
	'''
	The mass of the fixed roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	Motion = property(_get_Motion, None)
	'''
	The angular motion of the fixed roller

	:type: recurdyn.ProcessNet.IMotion
	'''
	MultipleRollerInfo = property(_get_MultipleRollerInfo, None)
	'''
	MultipleRoller Informatioin

	:type: recurdyn.MTT3D.IMTT3DMultipleRollerInfo
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
	The radius of the fixed roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	ReferencePoint = property(_get_ReferencePoint, None)
	'''
	The reference Point of the fixed roller body

	:type: recurdyn.ProcessNet.IVector
	'''
	RevJoint = property(_get_RevJoint, None)
	'''
	The revolute joint

	:type: recurdyn.ProcessNet.IGeneric
	'''
	RollerBody = property(_get_RollerBody, None)
	'''
	The roller body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	RollerType = property(_get_RollerType, _set_RollerType)
	'''
	Roller Type

	:type: recurdyn.MTT3D.RollerType
	'''
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseAutoCenterMarker = property(_get_UseAutoCenterMarker, _set_UseAutoCenterMarker)
	'''
	Match center marker automatically

	:type: bool
	'''
	UseAutoJointPosition = property(_get_UseAutoJointPosition, _set_UseAutoJointPosition)
	'''
	Match joint position automatically

	:type: bool
	'''
	UseCenterPoint = property(_get_UseCenterPoint, _set_UseCenterPoint)
	'''
	Use center point

	:type: bool
	'''
	UseCheckEdge = property(_get_UseCheckEdge, _set_UseCheckEdge)
	'''
	Check edge

	:type: bool
	'''
	UseMotion = property(_get_UseMotion, _set_UseMotion)
	'''
	Use motion

	:type: bool
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_BaseBody": _set_BaseBody,
		"_set_CenterPoint": _set_CenterPoint,
		"_set_Comment": _set_Comment,
		"_set_DepthDirection": _set_DepthDirection,
		"_set_DirectionPoint": _set_DirectionPoint,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_RollerType": _set_RollerType,
		"_set_UseAutoCenterMarker": _set_UseAutoCenterMarker,
		"_set_UseAutoJointPosition": _set_UseAutoJointPosition,
		"_set_UseCenterPoint": _set_UseCenterPoint,
		"_set_UseCheckEdge": _set_UseCheckEdge,
		"_set_UseMotion": _set_UseMotion,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (5051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"CenterPoint": (5052, 2, (8197, 0), (), "CenterPoint", None),
		"CenterPoint2": (5074, 2, (9, 0), (), "CenterPoint2", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (5076, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToSheet": (5065, 2, (9, 0), (), "ContactPropertyToSheet", '{24331496-FF71-42BC-AE6C-5C675546329B}'),
		"CrownRollerProfile": (5072, 2, (9, 0), (), "CrownRollerProfile", '{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}'),
		"Depth": (5058, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DepthDirection": (5054, 2, (8197, 0), (), "DepthDirection", None),
		"DirectionPoint": (5055, 2, (8197, 0), (), "DirectionPoint", None),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"ForceDisplay": (5075, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Ixx": (5060, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (5061, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (5062, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Mass": (5059, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Motion": (5064, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'),
		"MultipleRollerInfo": (5073, 2, (9, 0), (), "MultipleRollerInfo", '{786C632D-A3A2-4FC7-9C31-F6EF4DB35EC7}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (5057, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ReferencePoint": (5053, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"RevJoint": (5068, 2, (9, 0), (), "RevJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"RollerBody": (5067, 2, (9, 0), (), "RollerBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"RollerType": (5071, 2, (3, 0), (), "RollerType", '{4FD105DB-485D-4AC8-80FE-B163BDB06C37}'),
		"SpecialContactPoints": (5077, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseAutoCenterMarker": (5066, 2, (11, 0), (), "UseAutoCenterMarker", None),
		"UseAutoJointPosition": (5069, 2, (11, 0), (), "UseAutoJointPosition", None),
		"UseCenterPoint": (5056, 2, (11, 0), (), "UseCenterPoint", None),
		"UseCheckEdge": (5070, 2, (11, 0), (), "UseCheckEdge", None),
		"UseMotion": (5063, 2, (11, 0), (), "UseMotion", None),
		"UseSpecialContactPoints": (5078, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((5051, LCID, 4, 0),()),
		"CenterPoint": ((5052, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DepthDirection": ((5054, LCID, 4, 0),()),
		"DirectionPoint": ((5055, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"ForceDisplay": ((5075, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"RollerType": ((5071, LCID, 4, 0),()),
		"UseAutoCenterMarker": ((5066, LCID, 4, 0),()),
		"UseAutoJointPosition": ((5069, LCID, 4, 0),()),
		"UseCenterPoint": ((5056, LCID, 4, 0),()),
		"UseCheckEdge": ((5070, LCID, 4, 0),()),
		"UseMotion": ((5063, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((5078, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DGroupMovableRoller(DispatchBaseClass):
	'''MTT3D movable roller group'''
	CLSID = IID('{6E476EA6-E410-4EEB-A32A-5B24141617A3}')
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


	def SetLayerNumber(self, iVal):
		'''
		Set layer Number
		
		:param iVal: int
		'''
		return self._oleobj_.InvokeTypes(202, LCID, 1, (24, 0), ((19, 1),),iVal
			)


	def UpdateActiveFlagOfAllEntities(self, Val):
		'''
		Update active flag of all entities
		
		:param Val: bool
		'''
		return self._oleobj_.InvokeTypes(204, LCID, 1, (24, 0), ((11, 1),),Val
			)


	def UpdateAllProperties(self):
		'''
		Update all properties
		'''
		return self._oleobj_.InvokeTypes(201, LCID, 1, (24, 0), (),)


	def UpdateNonGeometricProperties(self):
		'''
		Update non-geometric properties
		'''
		return self._oleobj_.InvokeTypes(5085, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_CenterPoint(self):
		return self._ApplyTypes_(*(5052, 2, (8197, 0), (), "CenterPoint", None))
	def _get_CenterPoint2(self):
		return self._ApplyTypes_(*(5086, 2, (9, 0), (), "CenterPoint2", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPointsToRoller(self):
		return self._ApplyTypes_(*(5091, 2, (9, 0), (), "ContactPointsToRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPointsToSheet(self):
		return self._ApplyTypes_(*(5090, 2, (9, 0), (), "ContactPointsToSheet", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToFixedRoller(self):
		return self._ApplyTypes_(*(5066, 2, (9, 0), (), "ContactPropertyToFixedRoller", '{8FD0551D-5E3C-428A-9944-CEAC08A575A7}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(5065, 2, (9, 0), (), "ContactPropertyToSheet", '{24331496-FF71-42BC-AE6C-5C675546329B}'))
	def _get_CrownRollerProfile(self):
		return self._ApplyTypes_(*(5073, 2, (9, 0), (), "CrownRollerProfile", '{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}'))
	def _get_Depth(self):
		return self._ApplyTypes_(*(5058, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DepthDirection(self):
		return self._ApplyTypes_(*(5054, 2, (8197, 0), (), "DepthDirection", None))
	def _get_DirectionPoint(self):
		return self._ApplyTypes_(*(5055, 2, (8197, 0), (), "DirectionPoint", None))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_ForceDisplayToRoller(self):
		return self._ApplyTypes_(*(5089, 2, (3, 0), (), "ForceDisplayToRoller", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayToSheet(self):
		return self._ApplyTypes_(*(5088, 2, (3, 0), (), "ForceDisplayToSheet", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(5060, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(5061, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(5062, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Mass(self):
		return self._ApplyTypes_(*(5059, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumGap(self):
		return self._ApplyTypes_(*(5084, 2, (9, 0), (), "MaximumGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Motion(self):
		return self._ApplyTypes_(*(5080, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NipSpring(self):
		return self._ApplyTypes_(*(5064, 2, (9, 0), (), "NipSpring", '{E8BD4F07-0B25-44C6-9B8E-0905A9EAE731}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RARBody(self):
		return self._ApplyTypes_(*(5075, 2, (9, 0), (), "RARBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(5057, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ReferencePoint(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_RevJoint(self):
		return self._ApplyTypes_(*(5076, 2, (9, 0), (), "RevJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_RollerBody(self):
		return self._ApplyTypes_(*(5074, 2, (9, 0), (), "RollerBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_SoftNip(self):
		return self._ApplyTypes_(*(5082, 2, (9, 0), (), "SoftNip", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_SpecialContactPointsToRoller(self):
		return self._ApplyTypes_(*(5093, 2, (9, 0), (), "SpecialContactPointsToRoller", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialContactPointsToSheet(self):
		return self._ApplyTypes_(*(5092, 2, (9, 0), (), "SpecialContactPointsToSheet", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpringForce(self):
		return self._ApplyTypes_(*(5078, 2, (9, 0), (), "SpringForce", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_TraJoint(self):
		return self._ApplyTypes_(*(5077, 2, (9, 0), (), "TraJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_TranslationalDirectionAngle(self):
		return self._ApplyTypes_(*(5087, 2, (9, 0), (), "TranslationalDirectionAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseAutoCenterMarker(self):
		return self._ApplyTypes_(*(5067, 2, (11, 0), (), "UseAutoCenterMarker", None))
	def _get_UseAutoJointPosition(self):
		return self._ApplyTypes_(*(5068, 2, (11, 0), (), "UseAutoJointPosition", None))
	def _get_UseAutoUpdateGeometry(self):
		return self._ApplyTypes_(*(5069, 2, (11, 0), (), "UseAutoUpdateGeometry", None))
	def _get_UseCenterPoint(self):
		return self._ApplyTypes_(*(5056, 2, (11, 0), (), "UseCenterPoint", None))
	def _get_UseCheckEdge(self):
		return self._ApplyTypes_(*(5071, 2, (11, 0), (), "UseCheckEdge", None))
	def _get_UseCrownRollerProfile(self):
		return self._ApplyTypes_(*(5072, 2, (11, 0), (), "UseCrownRollerProfile", None))
	def _get_UseHigherNipForce(self):
		return self._ApplyTypes_(*(5070, 2, (11, 0), (), "UseHigherNipForce", None))
	def _get_UseMaximumGap(self):
		return self._ApplyTypes_(*(5083, 2, (11, 0), (), "UseMaximumGap", None))
	def _get_UseMotion(self):
		return self._ApplyTypes_(*(5079, 2, (11, 0), (), "UseMotion", None))
	def _get_UseNipSpring(self):
		return self._ApplyTypes_(*(5063, 2, (11, 0), (), "UseNipSpring", None))
	def _get_UseSoftNip(self):
		return self._ApplyTypes_(*(5081, 2, (11, 0), (), "UseSoftNip", None))
	def _get_UseSpecialContactPointsToRoller(self):
		return self._ApplyTypes_(*(5095, 2, (11, 0), (), "UseSpecialContactPointsToRoller", None))
	def _get_UseSpecialContactPointsToSheet(self):
		return self._ApplyTypes_(*(5094, 2, (11, 0), (), "UseSpecialContactPointsToSheet", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((5051, LCID, 4, 0) + (value,) + ()))
	def _set_CenterPoint(self, value):
		if "CenterPoint" in self.__dict__: self.__dict__["CenterPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5052, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DepthDirection(self, value):
		if "DepthDirection" in self.__dict__: self.__dict__["DepthDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5054, LCID, 4, 0) + (variantValue,) + ()))
	def _set_DirectionPoint(self, value):
		if "DirectionPoint" in self.__dict__: self.__dict__["DirectionPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5055, LCID, 4, 0) + (variantValue,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayToRoller(self, value):
		if "ForceDisplayToRoller" in self.__dict__: self.__dict__["ForceDisplayToRoller"] = value; return
		self._oleobj_.Invoke(*((5089, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayToSheet(self, value):
		if "ForceDisplayToSheet" in self.__dict__: self.__dict__["ForceDisplayToSheet"] = value; return
		self._oleobj_.Invoke(*((5088, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_SoftNip(self, value):
		if "SoftNip" in self.__dict__: self.__dict__["SoftNip"] = value; return
		self._oleobj_.Invoke(*((5082, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoCenterMarker(self, value):
		if "UseAutoCenterMarker" in self.__dict__: self.__dict__["UseAutoCenterMarker"] = value; return
		self._oleobj_.Invoke(*((5067, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoJointPosition(self, value):
		if "UseAutoJointPosition" in self.__dict__: self.__dict__["UseAutoJointPosition"] = value; return
		self._oleobj_.Invoke(*((5068, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoUpdateGeometry(self, value):
		if "UseAutoUpdateGeometry" in self.__dict__: self.__dict__["UseAutoUpdateGeometry"] = value; return
		self._oleobj_.Invoke(*((5069, LCID, 4, 0) + (value,) + ()))
	def _set_UseCenterPoint(self, value):
		if "UseCenterPoint" in self.__dict__: self.__dict__["UseCenterPoint"] = value; return
		self._oleobj_.Invoke(*((5056, LCID, 4, 0) + (value,) + ()))
	def _set_UseCheckEdge(self, value):
		if "UseCheckEdge" in self.__dict__: self.__dict__["UseCheckEdge"] = value; return
		self._oleobj_.Invoke(*((5071, LCID, 4, 0) + (value,) + ()))
	def _set_UseCrownRollerProfile(self, value):
		if "UseCrownRollerProfile" in self.__dict__: self.__dict__["UseCrownRollerProfile"] = value; return
		self._oleobj_.Invoke(*((5072, LCID, 4, 0) + (value,) + ()))
	def _set_UseHigherNipForce(self, value):
		if "UseHigherNipForce" in self.__dict__: self.__dict__["UseHigherNipForce"] = value; return
		self._oleobj_.Invoke(*((5070, LCID, 4, 0) + (value,) + ()))
	def _set_UseMaximumGap(self, value):
		if "UseMaximumGap" in self.__dict__: self.__dict__["UseMaximumGap"] = value; return
		self._oleobj_.Invoke(*((5083, LCID, 4, 0) + (value,) + ()))
	def _set_UseMotion(self, value):
		if "UseMotion" in self.__dict__: self.__dict__["UseMotion"] = value; return
		self._oleobj_.Invoke(*((5079, LCID, 4, 0) + (value,) + ()))
	def _set_UseNipSpring(self, value):
		if "UseNipSpring" in self.__dict__: self.__dict__["UseNipSpring"] = value; return
		self._oleobj_.Invoke(*((5063, LCID, 4, 0) + (value,) + ()))
	def _set_UseSoftNip(self, value):
		if "UseSoftNip" in self.__dict__: self.__dict__["UseSoftNip"] = value; return
		self._oleobj_.Invoke(*((5081, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPointsToRoller(self, value):
		if "UseSpecialContactPointsToRoller" in self.__dict__: self.__dict__["UseSpecialContactPointsToRoller"] = value; return
		self._oleobj_.Invoke(*((5095, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPointsToSheet(self, value):
		if "UseSpecialContactPointsToSheet" in self.__dict__: self.__dict__["UseSpecialContactPointsToSheet"] = value; return
		self._oleobj_.Invoke(*((5094, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseBody = property(_get_BaseBody, _set_BaseBody)
	'''
	The base body of the revolute joint

	:type: recurdyn.ProcessNet.IGeneric
	'''
	CenterPoint = property(_get_CenterPoint, _set_CenterPoint)
	'''
	The center point of the movable roller body

	:type: list[float]
	'''
	CenterPoint2 = property(_get_CenterPoint2, None)
	'''
	The center point of the movable roller body

	:type: recurdyn.ProcessNet.IVector
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactPointsToRoller = property(_get_ContactPointsToRoller, None)
	'''
	The number of max contact points to roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPointsToSheet = property(_get_ContactPointsToSheet, None)
	'''
	The number of max contact points to sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPropertyToFixedRoller = property(_get_ContactPropertyToFixedRoller, None)
	'''
	The parameters of contact forces applied between fixed roller and movable roller

	:type: recurdyn.MTT3D.IMTT3DContactPropertyRollerMovableToFixed
	'''
	ContactPropertyToSheet = property(_get_ContactPropertyToSheet, None)
	'''
	The parameters of contact forces applied between sheet and movable roller

	:type: recurdyn.MTT3D.IMTT3DContactPropertyRollerToSheet
	'''
	CrownRollerProfile = property(_get_CrownRollerProfile, None)
	'''
	CrownRoller Profile

	:type: recurdyn.MTT3D.IMTT3DCrownRollerProfile
	'''
	Depth = property(_get_Depth, None)
	'''
	The depth of the movable roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	DepthDirection = property(_get_DepthDirection, _set_DepthDirection)
	'''
	The depth direction at the center point of movable roller

	:type: list[float]
	'''
	DirectionPoint = property(_get_DirectionPoint, _set_DirectionPoint)
	'''
	The direction point at the reference point  of movable roller

	:type: list[float]
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	ForceDisplayToRoller = property(_get_ForceDisplayToRoller, _set_ForceDisplayToRoller)
	'''
	Force display to roller

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	ForceDisplayToSheet = property(_get_ForceDisplayToSheet, _set_ForceDisplayToSheet)
	'''
	Force display to sheet

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx, the mass moment of inertia in the x-axis of the roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy, the mass moment of inertia in the y-axis of the roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz, the mass moment of inertia in the z-axis of the roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	Mass = property(_get_Mass, None)
	'''
	The mass of the movable roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumGap = property(_get_MaximumGap, None)
	'''
	The maximum gap between movable roller and fixed roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	Motion = property(_get_Motion, None)
	'''
	The angular motion of the mixed roller

	:type: recurdyn.ProcessNet.IMotion
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NipSpring = property(_get_NipSpring, None)
	'''
	Nip spring

	:type: recurdyn.MTT3D.IMTT3DForceSpringNip
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
	RARBody = property(_get_RARBody, None)
	'''
	The rar body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	Radius = property(_get_Radius, None)
	'''
	The radius of the movable roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	ReferencePoint = property(_get_ReferencePoint, None)
	'''
	The reference Point of the movable roller body

	:type: recurdyn.ProcessNet.IVector
	'''
	RevJoint = property(_get_RevJoint, None)
	'''
	The revolute joint

	:type: recurdyn.ProcessNet.IGeneric
	'''
	RollerBody = property(_get_RollerBody, None)
	'''
	The roller body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	SoftNip = property(_get_SoftNip, _set_SoftNip)
	'''
	A spring that acts on movable roller

	:type: recurdyn.ProcessNet.IExpression
	'''
	SpecialContactPointsToRoller = property(_get_SpecialContactPointsToRoller, None)
	'''
	Special Number of max contact points to roller

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialContactPointsToSheet = property(_get_SpecialContactPointsToSheet, None)
	'''
	Special Number of max contact points to sheet

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpringForce = property(_get_SpringForce, None)
	'''
	The spring force

	:type: recurdyn.ProcessNet.IGeneric
	'''
	TraJoint = property(_get_TraJoint, None)
	'''
	The traslate joint

	:type: recurdyn.ProcessNet.IGeneric
	'''
	TranslationalDirectionAngle = property(_get_TranslationalDirectionAngle, None)
	'''
	The angle of translational direction

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseAutoCenterMarker = property(_get_UseAutoCenterMarker, _set_UseAutoCenterMarker)
	'''
	Match center marker automatically

	:type: bool
	'''
	UseAutoJointPosition = property(_get_UseAutoJointPosition, _set_UseAutoJointPosition)
	'''
	Match joint position automatically

	:type: bool
	'''
	UseAutoUpdateGeometry = property(_get_UseAutoUpdateGeometry, _set_UseAutoUpdateGeometry)
	'''
	Update geometry automatically

	:type: bool
	'''
	UseCenterPoint = property(_get_UseCenterPoint, _set_UseCenterPoint)
	'''
	Use center point

	:type: bool
	'''
	UseCheckEdge = property(_get_UseCheckEdge, _set_UseCheckEdge)
	'''
	Check edge

	:type: bool
	'''
	UseCrownRollerProfile = property(_get_UseCrownRollerProfile, _set_UseCrownRollerProfile)
	'''
	Use CrownRoller Profile

	:type: bool
	'''
	UseHigherNipForce = property(_get_UseHigherNipForce, _set_UseHigherNipForce)
	'''
	Higher Nip force

	:type: bool
	'''
	UseMaximumGap = property(_get_UseMaximumGap, _set_UseMaximumGap)
	'''
	Use maximum gap

	:type: bool
	'''
	UseMotion = property(_get_UseMotion, _set_UseMotion)
	'''
	Use motion

	:type: bool
	'''
	UseNipSpring = property(_get_UseNipSpring, _set_UseNipSpring)
	'''
	Use nip spring

	:type: bool
	'''
	UseSoftNip = property(_get_UseSoftNip, _set_UseSoftNip)
	'''
	Use soft nip

	:type: bool
	'''
	UseSpecialContactPointsToRoller = property(_get_UseSpecialContactPointsToRoller, _set_UseSpecialContactPointsToRoller)
	'''
	Use special Number of max contact points to roller

	:type: bool
	'''
	UseSpecialContactPointsToSheet = property(_get_UseSpecialContactPointsToSheet, _set_UseSpecialContactPointsToSheet)
	'''
	Use special Number of max contact points to sheet

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_BaseBody": _set_BaseBody,
		"_set_CenterPoint": _set_CenterPoint,
		"_set_Comment": _set_Comment,
		"_set_DepthDirection": _set_DepthDirection,
		"_set_DirectionPoint": _set_DirectionPoint,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_ForceDisplayToRoller": _set_ForceDisplayToRoller,
		"_set_ForceDisplayToSheet": _set_ForceDisplayToSheet,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_SoftNip": _set_SoftNip,
		"_set_UseAutoCenterMarker": _set_UseAutoCenterMarker,
		"_set_UseAutoJointPosition": _set_UseAutoJointPosition,
		"_set_UseAutoUpdateGeometry": _set_UseAutoUpdateGeometry,
		"_set_UseCenterPoint": _set_UseCenterPoint,
		"_set_UseCheckEdge": _set_UseCheckEdge,
		"_set_UseCrownRollerProfile": _set_UseCrownRollerProfile,
		"_set_UseHigherNipForce": _set_UseHigherNipForce,
		"_set_UseMaximumGap": _set_UseMaximumGap,
		"_set_UseMotion": _set_UseMotion,
		"_set_UseNipSpring": _set_UseNipSpring,
		"_set_UseSoftNip": _set_UseSoftNip,
		"_set_UseSpecialContactPointsToRoller": _set_UseSpecialContactPointsToRoller,
		"_set_UseSpecialContactPointsToSheet": _set_UseSpecialContactPointsToSheet,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (5051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"CenterPoint": (5052, 2, (8197, 0), (), "CenterPoint", None),
		"CenterPoint2": (5086, 2, (9, 0), (), "CenterPoint2", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPointsToRoller": (5091, 2, (9, 0), (), "ContactPointsToRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPointsToSheet": (5090, 2, (9, 0), (), "ContactPointsToSheet", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToFixedRoller": (5066, 2, (9, 0), (), "ContactPropertyToFixedRoller", '{8FD0551D-5E3C-428A-9944-CEAC08A575A7}'),
		"ContactPropertyToSheet": (5065, 2, (9, 0), (), "ContactPropertyToSheet", '{24331496-FF71-42BC-AE6C-5C675546329B}'),
		"CrownRollerProfile": (5073, 2, (9, 0), (), "CrownRollerProfile", '{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}'),
		"Depth": (5058, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DepthDirection": (5054, 2, (8197, 0), (), "DepthDirection", None),
		"DirectionPoint": (5055, 2, (8197, 0), (), "DirectionPoint", None),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"ForceDisplayToRoller": (5089, 2, (3, 0), (), "ForceDisplayToRoller", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayToSheet": (5088, 2, (3, 0), (), "ForceDisplayToSheet", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Ixx": (5060, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (5061, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (5062, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Mass": (5059, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumGap": (5084, 2, (9, 0), (), "MaximumGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Motion": (5080, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NipSpring": (5064, 2, (9, 0), (), "NipSpring", '{E8BD4F07-0B25-44C6-9B8E-0905A9EAE731}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RARBody": (5075, 2, (9, 0), (), "RARBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Radius": (5057, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ReferencePoint": (5053, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"RevJoint": (5076, 2, (9, 0), (), "RevJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"RollerBody": (5074, 2, (9, 0), (), "RollerBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"SoftNip": (5082, 2, (9, 0), (), "SoftNip", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"SpecialContactPointsToRoller": (5093, 2, (9, 0), (), "SpecialContactPointsToRoller", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialContactPointsToSheet": (5092, 2, (9, 0), (), "SpecialContactPointsToSheet", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpringForce": (5078, 2, (9, 0), (), "SpringForce", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"TraJoint": (5077, 2, (9, 0), (), "TraJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"TranslationalDirectionAngle": (5087, 2, (9, 0), (), "TranslationalDirectionAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseAutoCenterMarker": (5067, 2, (11, 0), (), "UseAutoCenterMarker", None),
		"UseAutoJointPosition": (5068, 2, (11, 0), (), "UseAutoJointPosition", None),
		"UseAutoUpdateGeometry": (5069, 2, (11, 0), (), "UseAutoUpdateGeometry", None),
		"UseCenterPoint": (5056, 2, (11, 0), (), "UseCenterPoint", None),
		"UseCheckEdge": (5071, 2, (11, 0), (), "UseCheckEdge", None),
		"UseCrownRollerProfile": (5072, 2, (11, 0), (), "UseCrownRollerProfile", None),
		"UseHigherNipForce": (5070, 2, (11, 0), (), "UseHigherNipForce", None),
		"UseMaximumGap": (5083, 2, (11, 0), (), "UseMaximumGap", None),
		"UseMotion": (5079, 2, (11, 0), (), "UseMotion", None),
		"UseNipSpring": (5063, 2, (11, 0), (), "UseNipSpring", None),
		"UseSoftNip": (5081, 2, (11, 0), (), "UseSoftNip", None),
		"UseSpecialContactPointsToRoller": (5095, 2, (11, 0), (), "UseSpecialContactPointsToRoller", None),
		"UseSpecialContactPointsToSheet": (5094, 2, (11, 0), (), "UseSpecialContactPointsToSheet", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((5051, LCID, 4, 0),()),
		"CenterPoint": ((5052, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DepthDirection": ((5054, LCID, 4, 0),()),
		"DirectionPoint": ((5055, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"ForceDisplayToRoller": ((5089, LCID, 4, 0),()),
		"ForceDisplayToSheet": ((5088, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"SoftNip": ((5082, LCID, 4, 0),()),
		"UseAutoCenterMarker": ((5067, LCID, 4, 0),()),
		"UseAutoJointPosition": ((5068, LCID, 4, 0),()),
		"UseAutoUpdateGeometry": ((5069, LCID, 4, 0),()),
		"UseCenterPoint": ((5056, LCID, 4, 0),()),
		"UseCheckEdge": ((5071, LCID, 4, 0),()),
		"UseCrownRollerProfile": ((5072, LCID, 4, 0),()),
		"UseHigherNipForce": ((5070, LCID, 4, 0),()),
		"UseMaximumGap": ((5083, LCID, 4, 0),()),
		"UseMotion": ((5079, LCID, 4, 0),()),
		"UseNipSpring": ((5063, LCID, 4, 0),()),
		"UseSoftNip": ((5081, LCID, 4, 0),()),
		"UseSpecialContactPointsToRoller": ((5095, LCID, 4, 0),()),
		"UseSpecialContactPointsToSheet": ((5094, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DGuide(DispatchBaseClass):
	'''MTT3D guide'''
	CLSID = IID('{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}')
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
		return self._oleobj_.InvokeTypes(5002, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(5004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(5007, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((5007, LCID, 4, 0) + (value,) + ()))
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
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
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
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

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
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (5005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ForceDisplay": (5004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (5003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (5001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SpecialContactPoints": (5006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseSpecialContactPoints": (5007, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((5004, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((5001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((5007, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DGuideArc(DispatchBaseClass):
	'''MTT3D arc guide'''
	CLSID = IID('{433E3A1C-9C7A-4426-9A79-26AF18A119D4}')
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
		return self._oleobj_.InvokeTypes(5002, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Angle(self):
		return self._ApplyTypes_(*(5052, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(5057, 2, (3, 0), (), "ContactDirection", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(5058, 2, (9, 0), (), "ContactPropertyToSheet", '{B805319E-24BB-4157-B46C-C40AD3B0F5C4}'))
	def _get_Depth(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ExtrudeDirection(self):
		return self._ApplyTypes_(*(5056, 2, (8197, 0), (), "ExtrudeDirection", None))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(5004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ReferenceDirection(self):
		return self._ApplyTypes_(*(5055, 2, (8197, 0), (), "ReferenceDirection", None))
	def _get_ReferencePoint(self):
		return self._ApplyTypes_(*(5054, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseCheckEdge(self):
		return self._ApplyTypes_(*(5059, 2, (11, 0), (), "UseCheckEdge", None))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(5007, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ContactDirection(self, value):
		if "ContactDirection" in self.__dict__: self.__dict__["ContactDirection"] = value; return
		self._oleobj_.Invoke(*((5057, LCID, 4, 0) + (value,) + ()))
	def _set_ExtrudeDirection(self, value):
		if "ExtrudeDirection" in self.__dict__: self.__dict__["ExtrudeDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5056, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceDirection(self, value):
		if "ReferenceDirection" in self.__dict__: self.__dict__["ReferenceDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5055, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseCheckEdge(self, value):
		if "UseCheckEdge" in self.__dict__: self.__dict__["UseCheckEdge"] = value; return
		self._oleobj_.Invoke(*((5059, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((5007, LCID, 4, 0) + (value,) + ()))
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
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactDirection = property(_get_ContactDirection, _set_ContactDirection)
	'''
	Contact Direction

	:type: recurdyn.ProcessNet.NormalDirection
	'''
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPropertyToSheet = property(_get_ContactPropertyToSheet, None)
	'''
	The contact parameters of contact forces applied between sheet and arc guide

	:type: recurdyn.MTT3D.IMTT3DContactPropertyGuide
	'''
	Depth = property(_get_Depth, None)
	'''
	The depth of arc

	:type: recurdyn.ProcessNet.IDouble
	'''
	ExtrudeDirection = property(_get_ExtrudeDirection, _set_ExtrudeDirection)
	'''
	The extrude direction of arc

	:type: list[float]
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
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
	ReferenceDirection = property(_get_ReferenceDirection, _set_ReferenceDirection)
	'''
	The reference direction of arc

	:type: list[float]
	'''
	ReferencePoint = property(_get_ReferencePoint, None)
	'''
	The reference point of arc

	:type: recurdyn.ProcessNet.IVector
	'''
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseCheckEdge = property(_get_UseCheckEdge, _set_UseCheckEdge)
	'''
	Use check edge

	:type: bool
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

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
		"_set_ContactDirection": _set_ContactDirection,
		"_set_ExtrudeDirection": _set_ExtrudeDirection,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_ReferenceDirection": _set_ReferenceDirection,
		"_set_UseCheckEdge": _set_UseCheckEdge,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Angle": (5052, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (5057, 2, (3, 0), (), "ContactDirection", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}'),
		"ContactPoints": (5005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToSheet": (5058, 2, (9, 0), (), "ContactPropertyToSheet", '{B805319E-24BB-4157-B46C-C40AD3B0F5C4}'),
		"Depth": (5053, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ExtrudeDirection": (5056, 2, (8197, 0), (), "ExtrudeDirection", None),
		"ForceDisplay": (5004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (5003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (5001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (5051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ReferenceDirection": (5055, 2, (8197, 0), (), "ReferenceDirection", None),
		"ReferencePoint": (5054, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"SpecialContactPoints": (5006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseCheckEdge": (5059, 2, (11, 0), (), "UseCheckEdge", None),
		"UseSpecialContactPoints": (5007, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ContactDirection": ((5057, LCID, 4, 0),()),
		"ExtrudeDirection": ((5056, LCID, 4, 0),()),
		"ForceDisplay": ((5004, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((5001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ReferenceDirection": ((5055, LCID, 4, 0),()),
		"UseCheckEdge": ((5059, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((5007, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DGuideCircular(DispatchBaseClass):
	'''MTT3D circular guide'''
	CLSID = IID('{10FA5037-8BC0-4293-AB5C-E81BD03C634E}')
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
		return self._oleobj_.InvokeTypes(5002, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(5055, 2, (9, 0), (), "ContactPropertyToSheet", '{3D9E9719-9BD8-4234-8A98-87D2975BB531}'))
	def _get_Depth(self):
		return self._ApplyTypes_(*(5052, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ExtrudeDirection(self):
		return self._ApplyTypes_(*(5054, 2, (8197, 0), (), "ExtrudeDirection", None))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(5004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ReferencePoint(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseCheckEdge(self):
		return self._ApplyTypes_(*(5056, 2, (11, 0), (), "UseCheckEdge", None))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(5007, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ExtrudeDirection(self, value):
		if "ExtrudeDirection" in self.__dict__: self.__dict__["ExtrudeDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5054, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseCheckEdge(self, value):
		if "UseCheckEdge" in self.__dict__: self.__dict__["UseCheckEdge"] = value; return
		self._oleobj_.Invoke(*((5056, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((5007, LCID, 4, 0) + (value,) + ()))
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
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPropertyToSheet = property(_get_ContactPropertyToSheet, None)
	'''
	The contact parameters of contact forces applied between sheet and circular guide

	:type: recurdyn.MTT3D.IMTT3DContactPropertyCircularGuide
	'''
	Depth = property(_get_Depth, None)
	'''
	The depth of circle

	:type: recurdyn.ProcessNet.IDouble
	'''
	ExtrudeDirection = property(_get_ExtrudeDirection, _set_ExtrudeDirection)
	'''
	The extrude direction of circle

	:type: list[float]
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
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
	ReferencePoint = property(_get_ReferencePoint, None)
	'''
	The reference point of circle

	:type: recurdyn.ProcessNet.IVector
	'''
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseCheckEdge = property(_get_UseCheckEdge, _set_UseCheckEdge)
	'''
	Use check edge

	:type: bool
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

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
		"_set_ExtrudeDirection": _set_ExtrudeDirection,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_UseCheckEdge": _set_UseCheckEdge,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (5005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToSheet": (5055, 2, (9, 0), (), "ContactPropertyToSheet", '{3D9E9719-9BD8-4234-8A98-87D2975BB531}'),
		"Depth": (5052, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ExtrudeDirection": (5054, 2, (8197, 0), (), "ExtrudeDirection", None),
		"ForceDisplay": (5004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (5003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (5001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (5051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ReferencePoint": (5053, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"SpecialContactPoints": (5006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseCheckEdge": (5056, 2, (11, 0), (), "UseCheckEdge", None),
		"UseSpecialContactPoints": (5007, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ExtrudeDirection": ((5054, LCID, 4, 0),()),
		"ForceDisplay": ((5004, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((5001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseCheckEdge": ((5056, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((5007, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DGuideCollection(DispatchBaseClass):
	'''IMTT3DGuideCollection'''
	CLSID = IID('{DAEA406F-55AF-4745-969A-9A3184D19D02}')
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
		:rtype: recurdyn.MTT3D.IMTT3DGuide
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}')
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
		:rtype: recurdyn.MTT3D.IMTT3DGuide
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}')
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
		return win32com.client.util.Iterator(ob, '{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT3DGuideLinear(DispatchBaseClass):
	'''MTT3D linear guide'''
	CLSID = IID('{80975616-6221-41FA-970F-09B25194E5FB}')
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
		return self._oleobj_.InvokeTypes(5002, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(5056, 2, (3, 0), (), "ContactDirection", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(5005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(5057, 2, (9, 0), (), "ContactPropertyToSheet", '{B805319E-24BB-4157-B46C-C40AD3B0F5C4}'))
	def _get_Depth(self):
		return self._ApplyTypes_(*(5055, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ExtrudeDirection(self):
		return self._ApplyTypes_(*(5052, 2, (8197, 0), (), "ExtrudeDirection", None))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(5004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Length(self):
		return self._ApplyTypes_(*(5054, 2, (9, 0), (), "Length", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LongitudinalDirection(self):
		return self._ApplyTypes_(*(5053, 2, (8197, 0), (), "LongitudinalDirection", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ReferencePoint(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseCheckVertex(self):
		return self._ApplyTypes_(*(5058, 2, (11, 0), (), "UseCheckVertex", None))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(5007, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ContactDirection(self, value):
		if "ContactDirection" in self.__dict__: self.__dict__["ContactDirection"] = value; return
		self._oleobj_.Invoke(*((5056, LCID, 4, 0) + (value,) + ()))
	def _set_ExtrudeDirection(self, value):
		if "ExtrudeDirection" in self.__dict__: self.__dict__["ExtrudeDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5052, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((5004, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_LongitudinalDirection(self, value):
		if "LongitudinalDirection" in self.__dict__: self.__dict__["LongitudinalDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5053, LCID, 4, 0) + (variantValue,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseCheckVertex(self, value):
		if "UseCheckVertex" in self.__dict__: self.__dict__["UseCheckVertex"] = value; return
		self._oleobj_.Invoke(*((5058, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((5007, LCID, 4, 0) + (value,) + ()))
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
	ContactDirection = property(_get_ContactDirection, _set_ContactDirection)
	'''
	Contact Direction

	:type: recurdyn.ProcessNet.NormalDirection
	'''
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPropertyToSheet = property(_get_ContactPropertyToSheet, None)
	'''
	The contact parameters of contact forces applied between sheet and linear guide

	:type: recurdyn.MTT3D.IMTT3DContactPropertyGuide
	'''
	Depth = property(_get_Depth, None)
	'''
	The depth of line

	:type: recurdyn.ProcessNet.IDouble
	'''
	ExtrudeDirection = property(_get_ExtrudeDirection, _set_ExtrudeDirection)
	'''
	The extrude direction of line

	:type: list[float]
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
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
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	Length = property(_get_Length, None)
	'''
	The length of line

	:type: recurdyn.ProcessNet.IDouble
	'''
	LongitudinalDirection = property(_get_LongitudinalDirection, _set_LongitudinalDirection)
	'''
	The longitudinal direction of line

	:type: list[float]
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
	ReferencePoint = property(_get_ReferencePoint, None)
	'''
	The reference point of line

	:type: recurdyn.ProcessNet.IVector
	'''
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseCheckVertex = property(_get_UseCheckVertex, _set_UseCheckVertex)
	'''
	Use check vertex

	:type: bool
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

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
		"_set_ContactDirection": _set_ContactDirection,
		"_set_ExtrudeDirection": _set_ExtrudeDirection,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_LongitudinalDirection": _set_LongitudinalDirection,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_UseCheckVertex": _set_UseCheckVertex,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (5056, 2, (3, 0), (), "ContactDirection", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}'),
		"ContactPoints": (5005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToSheet": (5057, 2, (9, 0), (), "ContactPropertyToSheet", '{B805319E-24BB-4157-B46C-C40AD3B0F5C4}'),
		"Depth": (5055, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ExtrudeDirection": (5052, 2, (8197, 0), (), "ExtrudeDirection", None),
		"ForceDisplay": (5004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (5003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Length": (5054, 2, (9, 0), (), "Length", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LongitudinalDirection": (5053, 2, (8197, 0), (), "LongitudinalDirection", None),
		"MotherBody": (5001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ReferencePoint": (5051, 2, (9, 0), (), "ReferencePoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"SpecialContactPoints": (5006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseCheckVertex": (5058, 2, (11, 0), (), "UseCheckVertex", None),
		"UseSpecialContactPoints": (5007, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ContactDirection": ((5056, LCID, 4, 0),()),
		"ExtrudeDirection": ((5052, LCID, 4, 0),()),
		"ForceDisplay": ((5004, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"LongitudinalDirection": ((5053, LCID, 4, 0),()),
		"MotherBody": ((5001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseCheckVertex": ((5058, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((5007, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DMovableRollerGroupCollection(DispatchBaseClass):
	'''IMTT3DMovableRollerGroupCollection'''
	CLSID = IID('{115B4437-C5DB-456D-885E-8F8F51A48C13}')
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
		:rtype: recurdyn.MTT3D.IMTT3DGroupMovableRoller
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6E476EA6-E410-4EEB-A32A-5B24141617A3}')
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
		:rtype: recurdyn.MTT3D.IMTT3DGroupMovableRoller
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6E476EA6-E410-4EEB-A32A-5B24141617A3}')
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
		return win32com.client.util.Iterator(ob, '{6E476EA6-E410-4EEB-A32A-5B24141617A3}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{6E476EA6-E410-4EEB-A32A-5B24141617A3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT3DMultipleRollerInfo(DispatchBaseClass):
	'''MTT3D multiple roller information'''
	CLSID = IID('{786C632D-A3A2-4FC7-9C31-F6EF4DB35EC7}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Add(self, dRadius, dDepth, dDistance):
		'''
		Add data
		
		:param dRadius: float
		:param dDepth: float
		:param dDistance: float
		'''
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1)),dRadius
			, dDepth, dDistance)


	def Clear(self):
		'''
		Clear data
		'''
		return self._oleobj_.InvokeTypes(53, LCID, 1, (24, 0), (),)


	def Export(self, strFullPathName):
		'''
		Export a file
		
		:param strFullPathName: str
		'''
		return self._oleobj_.InvokeTypes(55, LCID, 1, (24, 0), ((8, 1),),strFullPathName
			)


	def Import(self, strFullPathName):
		'''
		Import a file
		
		:param strFullPathName: str
		'''
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), ((8, 1),),strFullPathName
			)


	def _get_RollerInfoCollection(self):
		return self._ApplyTypes_(*(51, 2, (9, 0), (), "RollerInfoCollection", '{5E1955E3-FF59-4A71-BA6C-47152E76743B}'))

	RollerInfoCollection = property(_get_RollerInfoCollection, None)
	'''
	Roller info collection

	:type: recurdyn.MTT3D.IRollerInfoCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"RollerInfoCollection": (51, 2, (9, 0), (), "RollerInfoCollection", '{5E1955E3-FF59-4A71-BA6C-47152E76743B}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DNode(DispatchBaseClass):
	'''MTT3D sheet shell node'''
	CLSID = IID('{460C1F0E-80C4-4F4A-9E5B-DA282823C49E}')
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
	def _get_ID(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "ID", None))
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
	def _get_x(self):
		return self._ApplyTypes_(*(152, 2, (5, 0), (), "x", None))
	def _get_y(self):
		return self._ApplyTypes_(*(153, 2, (5, 0), (), "y", None))
	def _get_z(self):
		return self._ApplyTypes_(*(154, 2, (5, 0), (), "z", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ID(self, value):
		if "ID" in self.__dict__: self.__dict__["ID"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_x(self, value):
		if "x" in self.__dict__: self.__dict__["x"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_y(self, value):
		if "y" in self.__dict__: self.__dict__["y"] = value; return
		self._oleobj_.Invoke(*((153, LCID, 4, 0) + (value,) + ()))
	def _set_z(self, value):
		if "z" in self.__dict__: self.__dict__["z"] = value; return
		self._oleobj_.Invoke(*((154, LCID, 4, 0) + (value,) + ()))

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
	ID = property(_get_ID, _set_ID)
	'''
	ID

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
	x = property(_get_x, _set_x)
	'''
	Position X

	:type: float
	'''
	y = property(_get_y, _set_y)
	'''
	Position Y

	:type: float
	'''
	z = property(_get_z, _set_z)
	'''
	Position Z

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_ID": _set_ID,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
		"_set_x": _set_x,
		"_set_y": _set_y,
		"_set_z": _set_z,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"ID": (151, 2, (19, 0), (), "ID", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"x": (152, 2, (5, 0), (), "x", None),
		"y": (153, 2, (5, 0), (), "y", None),
		"z": (154, 2, (5, 0), (), "z", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ID": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"x": ((152, LCID, 4, 0),()),
		"y": ((153, LCID, 4, 0),()),
		"z": ((154, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DPointCollection(DispatchBaseClass):
	'''IMTT3DVectorCollection'''
	CLSID = IID('{112C4CA7-E0D7-429E-AC61-4697B7E49348}')
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
		
		:param var: int
		:rtype: recurdyn.ProcessNet.IPoint3D
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')
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
		
		:param var: int
		:rtype: recurdyn.ProcessNet.IPoint3D
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')
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
		return win32com.client.util.Iterator(ob, '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT3DRollerInfo(DispatchBaseClass):
	'''MTT3D roller information'''
	CLSID = IID('{08C957DF-3520-4486-B0F5-55EACA670727}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Depth(self):
		return self._ApplyTypes_(*(52, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Distance(self):
		return self._ApplyTypes_(*(53, 2, (9, 0), (), "Distance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(51, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	Depth = property(_get_Depth, None)
	'''
	Depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	Distance = property(_get_Distance, None)
	'''
	Distance

	:type: recurdyn.ProcessNet.IDouble
	'''
	Radius = property(_get_Radius, None)
	'''
	Radius

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Depth": (52, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Distance": (53, 2, (9, 0), (), "Distance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Radius": (51, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DSheet(DispatchBaseClass):
	'''MTT3D sheet'''
	CLSID = IID('{13A25611-C71D-4E62-84B3-7030679D96B7}')
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
		Update all properties
		'''
		return self._oleobj_.InvokeTypes(5057, LCID, 1, (24, 0), (),)


	def UpdateAllProperties2(self):
		'''
		Update all properties
		'''
		return self._oleobj_.InvokeTypes(5058, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_AllDampingRatio(self):
		return self._ApplyTypes_(*(5021, 2, (11, 0), (), "AllDampingRatio", None))
	def _get_AllDensity(self):
		return self._ApplyTypes_(*(5009, 2, (11, 0), (), "AllDensity", None))
	def _get_AllG11(self):
		return self._ApplyTypes_(*(5069, 2, (11, 0), (), "AllG11", None))
	def _get_AllG12(self):
		return self._ApplyTypes_(*(5073, 2, (11, 0), (), "AllG12", None))
	def _get_AllG13(self):
		return self._ApplyTypes_(*(5077, 2, (11, 0), (), "AllG13", None))
	def _get_AllG22(self):
		return self._ApplyTypes_(*(5081, 2, (11, 0), (), "AllG22", None))
	def _get_AllG23(self):
		return self._ApplyTypes_(*(5085, 2, (11, 0), (), "AllG23", None))
	def _get_AllG33(self):
		return self._ApplyTypes_(*(5089, 2, (11, 0), (), "AllG33", None))
	def _get_AllPoissonsRatio(self):
		return self._ApplyTypes_(*(5025, 2, (11, 0), (), "AllPoissonsRatio", None))
	def _get_AllPoissonsRatioXZ(self):
		return self._ApplyTypes_(*(5037, 2, (11, 0), (), "AllPoissonsRatioXZ", None))
	def _get_AllShearModulusXZ(self):
		return self._ApplyTypes_(*(5041, 2, (11, 0), (), "AllShearModulusXZ", None))
	def _get_AllTotalMass(self):
		return self._ApplyTypes_(*(5013, 2, (11, 0), (), "AllTotalMass", None))
	def _get_AllTransverseShearModulus1(self):
		return self._ApplyTypes_(*(5061, 2, (11, 0), (), "AllTransverseShearModulus1", None))
	def _get_AllTransverseShearModulus2(self):
		return self._ApplyTypes_(*(5065, 2, (11, 0), (), "AllTransverseShearModulus2", None))
	def _get_AllYoungsModulus(self):
		return self._ApplyTypes_(*(5017, 2, (11, 0), (), "AllYoungsModulus", None))
	def _get_AllYoungsModulusX(self):
		return self._ApplyTypes_(*(5029, 2, (11, 0), (), "AllYoungsModulusX", None))
	def _get_AllYoungsModulusZ(self):
		return self._ApplyTypes_(*(5033, 2, (11, 0), (), "AllYoungsModulusZ", None))
	def _get_Color(self):
		return self._ApplyTypes_(*(5056, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_CorrectionFactor(self):
		return self._ApplyTypes_(*(5045, 2, (9, 0), (), "CorrectionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CurlRadiusLateral(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "CurlRadiusLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CurlRadiusLongitudinal(self):
		return self._ApplyTypes_(*(5052, 2, (9, 0), (), "CurlRadiusLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(5023, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(5011, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DirectionLateral(self):
		return self._ApplyTypes_(*(5047, 2, (8197, 0), (), "DirectionLateral", None))
	def _get_DirectionLongitudinal(self):
		return self._ApplyTypes_(*(5046, 2, (8197, 0), (), "DirectionLongitudinal", None))
	def _get_FoldingDirection(self):
		return self._ApplyTypes_(*(5002, 2, (3, 0), (), "FoldingDirection", '{D3EFD1DD-14F8-4256-91A0-C1C3CF317F38}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_G11(self):
		return self._ApplyTypes_(*(5071, 2, (9, 0), (), "G11", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G12(self):
		return self._ApplyTypes_(*(5075, 2, (9, 0), (), "G12", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G13(self):
		return self._ApplyTypes_(*(5079, 2, (9, 0), (), "G13", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G22(self):
		return self._ApplyTypes_(*(5083, 2, (9, 0), (), "G22", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G23(self):
		return self._ApplyTypes_(*(5087, 2, (9, 0), (), "G23", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G33(self):
		return self._ApplyTypes_(*(5091, 2, (9, 0), (), "G33", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InitialVelocity(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "InitialVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InnerCPLateral(self):
		return self._ApplyTypes_(*(5055, 2, (19, 0), (), "InnerCPLateral", None))
	def _get_InnerCPLongitudinal(self):
		return self._ApplyTypes_(*(5054, 2, (19, 0), (), "InnerCPLongitudinal", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_LengthLateral(self):
		return self._ApplyTypes_(*(5049, 2, (9, 0), (), "LengthLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LengthLongitudinal(self):
		return self._ApplyTypes_(*(5048, 2, (9, 0), (), "LengthLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MassType(self):
		return self._ApplyTypes_(*(5008, 2, (3, 0), (), "MassType", '{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}'))
	def _get_MaterialDirectivity(self):
		return self._ApplyTypes_(*(5007, 2, (3, 0), (), "MaterialDirectivity", '{40184A33-144F-4805-BD66-92A3769EAF8C}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeNumberLateral(self):
		return self._ApplyTypes_(*(5051, 2, (19, 0), (), "NodeNumberLateral", None))
	def _get_NodeNumberLongitudinal(self):
		return self._ApplyTypes_(*(5050, 2, (19, 0), (), "NodeNumberLongitudinal", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PointList(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "PointList", '{6BEF9B6B-4708-445E-A3B5-0D65BA69F749}'))
	def _get_PoissonsRatio(self):
		return self._ApplyTypes_(*(5027, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PoissonsRatioXZ(self):
		return self._ApplyTypes_(*(5039, 2, (9, 0), (), "PoissonsRatioXZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearModulusXZ(self):
		return self._ApplyTypes_(*(5043, 2, (9, 0), (), "ShearModulusXZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialDampingRatio(self):
		return self._ApplyTypes_(*(5024, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialDensity(self):
		return self._ApplyTypes_(*(5012, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG11(self):
		return self._ApplyTypes_(*(5072, 2, (9, 0), (), "SpecialG11", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG12(self):
		return self._ApplyTypes_(*(5076, 2, (9, 0), (), "SpecialG12", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG13(self):
		return self._ApplyTypes_(*(5080, 2, (9, 0), (), "SpecialG13", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG22(self):
		return self._ApplyTypes_(*(5084, 2, (9, 0), (), "SpecialG22", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG23(self):
		return self._ApplyTypes_(*(5088, 2, (9, 0), (), "SpecialG23", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG33(self):
		return self._ApplyTypes_(*(5092, 2, (9, 0), (), "SpecialG33", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPoissonsRatio(self):
		return self._ApplyTypes_(*(5028, 2, (9, 0), (), "SpecialPoissonsRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPoissonsRatioXZ(self):
		return self._ApplyTypes_(*(5040, 2, (9, 0), (), "SpecialPoissonsRatioXZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialShearModulusXZ(self):
		return self._ApplyTypes_(*(5044, 2, (9, 0), (), "SpecialShearModulusXZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialTotalMass(self):
		return self._ApplyTypes_(*(5016, 2, (9, 0), (), "SpecialTotalMass", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialTransverseShearModulus1(self):
		return self._ApplyTypes_(*(5064, 2, (9, 0), (), "SpecialTransverseShearModulus1", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialTransverseShearModulus2(self):
		return self._ApplyTypes_(*(5068, 2, (9, 0), (), "SpecialTransverseShearModulus2", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialYoungsModulus(self):
		return self._ApplyTypes_(*(5020, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialYoungsModulusX(self):
		return self._ApplyTypes_(*(5032, 2, (9, 0), (), "SpecialYoungsModulusX", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialYoungsModulusZ(self):
		return self._ApplyTypes_(*(5036, 2, (9, 0), (), "SpecialYoungsModulusZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_StartPoint(self):
		return self._ApplyTypes_(*(5001, 2, (8197, 0), (), "StartPoint", None))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(5004, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(5015, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TransverseShearModulus1(self):
		return self._ApplyTypes_(*(5063, 2, (9, 0), (), "TransverseShearModulus1", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TransverseShearModulus2(self):
		return self._ApplyTypes_(*(5067, 2, (9, 0), (), "TransverseShearModulus2", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseInitialVelocity(self):
		return self._ApplyTypes_(*(5005, 2, (11, 0), (), "UseInitialVelocity", None))
	def _get_UseSpecialDampingRatio(self):
		return self._ApplyTypes_(*(5022, 2, (11, 0), (), "UseSpecialDampingRatio", None))
	def _get_UseSpecialDensity(self):
		return self._ApplyTypes_(*(5010, 2, (11, 0), (), "UseSpecialDensity", None))
	def _get_UseSpecialG11(self):
		return self._ApplyTypes_(*(5070, 2, (11, 0), (), "UseSpecialG11", None))
	def _get_UseSpecialG12(self):
		return self._ApplyTypes_(*(5074, 2, (11, 0), (), "UseSpecialG12", None))
	def _get_UseSpecialG13(self):
		return self._ApplyTypes_(*(5078, 2, (11, 0), (), "UseSpecialG13", None))
	def _get_UseSpecialG22(self):
		return self._ApplyTypes_(*(5082, 2, (11, 0), (), "UseSpecialG22", None))
	def _get_UseSpecialG23(self):
		return self._ApplyTypes_(*(5086, 2, (11, 0), (), "UseSpecialG23", None))
	def _get_UseSpecialG33(self):
		return self._ApplyTypes_(*(5090, 2, (11, 0), (), "UseSpecialG33", None))
	def _get_UseSpecialPoissonsRatio(self):
		return self._ApplyTypes_(*(5026, 2, (11, 0), (), "UseSpecialPoissonsRatio", None))
	def _get_UseSpecialPoissonsRatioXZ(self):
		return self._ApplyTypes_(*(5038, 2, (11, 0), (), "UseSpecialPoissonsRatioXZ", None))
	def _get_UseSpecialShearModulusXZ(self):
		return self._ApplyTypes_(*(5042, 2, (11, 0), (), "UseSpecialShearModulusXZ", None))
	def _get_UseSpecialTotalMass(self):
		return self._ApplyTypes_(*(5014, 2, (11, 0), (), "UseSpecialTotalMass", None))
	def _get_UseSpecialTransverseShearModulus1(self):
		return self._ApplyTypes_(*(5062, 2, (11, 0), (), "UseSpecialTransverseShearModulus1", None))
	def _get_UseSpecialTransverseShearModulus2(self):
		return self._ApplyTypes_(*(5066, 2, (11, 0), (), "UseSpecialTransverseShearModulus2", None))
	def _get_UseSpecialYoungsModulus(self):
		return self._ApplyTypes_(*(5018, 2, (11, 0), (), "UseSpecialYoungsModulus", None))
	def _get_UseSpecialYoungsModulusX(self):
		return self._ApplyTypes_(*(5030, 2, (11, 0), (), "UseSpecialYoungsModulusX", None))
	def _get_UseSpecialYoungsModulusZ(self):
		return self._ApplyTypes_(*(5034, 2, (11, 0), (), "UseSpecialYoungsModulusZ", None))
	def _get_UseUpdateGeometryAutomatically(self):
		return self._ApplyTypes_(*(5059, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None))
	def _get_UseUserDefinedTransverseShearModulus(self):
		return self._ApplyTypes_(*(5060, 2, (11, 0), (), "UseUserDefinedTransverseShearModulus", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(5019, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YoungsModulusX(self):
		return self._ApplyTypes_(*(5031, 2, (9, 0), (), "YoungsModulusX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YoungsModulusZ(self):
		return self._ApplyTypes_(*(5035, 2, (9, 0), (), "YoungsModulusZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_AllDampingRatio(self, value):
		if "AllDampingRatio" in self.__dict__: self.__dict__["AllDampingRatio"] = value; return
		self._oleobj_.Invoke(*((5021, LCID, 4, 0) + (value,) + ()))
	def _set_AllDensity(self, value):
		if "AllDensity" in self.__dict__: self.__dict__["AllDensity"] = value; return
		self._oleobj_.Invoke(*((5009, LCID, 4, 0) + (value,) + ()))
	def _set_AllG11(self, value):
		if "AllG11" in self.__dict__: self.__dict__["AllG11"] = value; return
		self._oleobj_.Invoke(*((5069, LCID, 4, 0) + (value,) + ()))
	def _set_AllG12(self, value):
		if "AllG12" in self.__dict__: self.__dict__["AllG12"] = value; return
		self._oleobj_.Invoke(*((5073, LCID, 4, 0) + (value,) + ()))
	def _set_AllG13(self, value):
		if "AllG13" in self.__dict__: self.__dict__["AllG13"] = value; return
		self._oleobj_.Invoke(*((5077, LCID, 4, 0) + (value,) + ()))
	def _set_AllG22(self, value):
		if "AllG22" in self.__dict__: self.__dict__["AllG22"] = value; return
		self._oleobj_.Invoke(*((5081, LCID, 4, 0) + (value,) + ()))
	def _set_AllG23(self, value):
		if "AllG23" in self.__dict__: self.__dict__["AllG23"] = value; return
		self._oleobj_.Invoke(*((5085, LCID, 4, 0) + (value,) + ()))
	def _set_AllG33(self, value):
		if "AllG33" in self.__dict__: self.__dict__["AllG33"] = value; return
		self._oleobj_.Invoke(*((5089, LCID, 4, 0) + (value,) + ()))
	def _set_AllPoissonsRatio(self, value):
		if "AllPoissonsRatio" in self.__dict__: self.__dict__["AllPoissonsRatio"] = value; return
		self._oleobj_.Invoke(*((5025, LCID, 4, 0) + (value,) + ()))
	def _set_AllPoissonsRatioXZ(self, value):
		if "AllPoissonsRatioXZ" in self.__dict__: self.__dict__["AllPoissonsRatioXZ"] = value; return
		self._oleobj_.Invoke(*((5037, LCID, 4, 0) + (value,) + ()))
	def _set_AllShearModulusXZ(self, value):
		if "AllShearModulusXZ" in self.__dict__: self.__dict__["AllShearModulusXZ"] = value; return
		self._oleobj_.Invoke(*((5041, LCID, 4, 0) + (value,) + ()))
	def _set_AllTotalMass(self, value):
		if "AllTotalMass" in self.__dict__: self.__dict__["AllTotalMass"] = value; return
		self._oleobj_.Invoke(*((5013, LCID, 4, 0) + (value,) + ()))
	def _set_AllTransverseShearModulus1(self, value):
		if "AllTransverseShearModulus1" in self.__dict__: self.__dict__["AllTransverseShearModulus1"] = value; return
		self._oleobj_.Invoke(*((5061, LCID, 4, 0) + (value,) + ()))
	def _set_AllTransverseShearModulus2(self, value):
		if "AllTransverseShearModulus2" in self.__dict__: self.__dict__["AllTransverseShearModulus2"] = value; return
		self._oleobj_.Invoke(*((5065, LCID, 4, 0) + (value,) + ()))
	def _set_AllYoungsModulus(self, value):
		if "AllYoungsModulus" in self.__dict__: self.__dict__["AllYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((5017, LCID, 4, 0) + (value,) + ()))
	def _set_AllYoungsModulusX(self, value):
		if "AllYoungsModulusX" in self.__dict__: self.__dict__["AllYoungsModulusX"] = value; return
		self._oleobj_.Invoke(*((5029, LCID, 4, 0) + (value,) + ()))
	def _set_AllYoungsModulusZ(self, value):
		if "AllYoungsModulusZ" in self.__dict__: self.__dict__["AllYoungsModulusZ"] = value; return
		self._oleobj_.Invoke(*((5033, LCID, 4, 0) + (value,) + ()))
	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((5056, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DirectionLateral(self, value):
		if "DirectionLateral" in self.__dict__: self.__dict__["DirectionLateral"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5047, LCID, 4, 0) + (variantValue,) + ()))
	def _set_DirectionLongitudinal(self, value):
		if "DirectionLongitudinal" in self.__dict__: self.__dict__["DirectionLongitudinal"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5046, LCID, 4, 0) + (variantValue,) + ()))
	def _set_FoldingDirection(self, value):
		if "FoldingDirection" in self.__dict__: self.__dict__["FoldingDirection"] = value; return
		self._oleobj_.Invoke(*((5002, LCID, 4, 0) + (value,) + ()))
	def _set_InnerCPLateral(self, value):
		if "InnerCPLateral" in self.__dict__: self.__dict__["InnerCPLateral"] = value; return
		self._oleobj_.Invoke(*((5055, LCID, 4, 0) + (value,) + ()))
	def _set_InnerCPLongitudinal(self, value):
		if "InnerCPLongitudinal" in self.__dict__: self.__dict__["InnerCPLongitudinal"] = value; return
		self._oleobj_.Invoke(*((5054, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MassType(self, value):
		if "MassType" in self.__dict__: self.__dict__["MassType"] = value; return
		self._oleobj_.Invoke(*((5008, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialDirectivity(self, value):
		if "MaterialDirectivity" in self.__dict__: self.__dict__["MaterialDirectivity"] = value; return
		self._oleobj_.Invoke(*((5007, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_StartPoint(self, value):
		if "StartPoint" in self.__dict__: self.__dict__["StartPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseInitialVelocity(self, value):
		if "UseInitialVelocity" in self.__dict__: self.__dict__["UseInitialVelocity"] = value; return
		self._oleobj_.Invoke(*((5005, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDampingRatio(self, value):
		if "UseSpecialDampingRatio" in self.__dict__: self.__dict__["UseSpecialDampingRatio"] = value; return
		self._oleobj_.Invoke(*((5022, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDensity(self, value):
		if "UseSpecialDensity" in self.__dict__: self.__dict__["UseSpecialDensity"] = value; return
		self._oleobj_.Invoke(*((5010, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG11(self, value):
		if "UseSpecialG11" in self.__dict__: self.__dict__["UseSpecialG11"] = value; return
		self._oleobj_.Invoke(*((5070, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG12(self, value):
		if "UseSpecialG12" in self.__dict__: self.__dict__["UseSpecialG12"] = value; return
		self._oleobj_.Invoke(*((5074, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG13(self, value):
		if "UseSpecialG13" in self.__dict__: self.__dict__["UseSpecialG13"] = value; return
		self._oleobj_.Invoke(*((5078, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG22(self, value):
		if "UseSpecialG22" in self.__dict__: self.__dict__["UseSpecialG22"] = value; return
		self._oleobj_.Invoke(*((5082, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG23(self, value):
		if "UseSpecialG23" in self.__dict__: self.__dict__["UseSpecialG23"] = value; return
		self._oleobj_.Invoke(*((5086, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG33(self, value):
		if "UseSpecialG33" in self.__dict__: self.__dict__["UseSpecialG33"] = value; return
		self._oleobj_.Invoke(*((5090, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPoissonsRatio(self, value):
		if "UseSpecialPoissonsRatio" in self.__dict__: self.__dict__["UseSpecialPoissonsRatio"] = value; return
		self._oleobj_.Invoke(*((5026, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPoissonsRatioXZ(self, value):
		if "UseSpecialPoissonsRatioXZ" in self.__dict__: self.__dict__["UseSpecialPoissonsRatioXZ"] = value; return
		self._oleobj_.Invoke(*((5038, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialShearModulusXZ(self, value):
		if "UseSpecialShearModulusXZ" in self.__dict__: self.__dict__["UseSpecialShearModulusXZ"] = value; return
		self._oleobj_.Invoke(*((5042, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialTotalMass(self, value):
		if "UseSpecialTotalMass" in self.__dict__: self.__dict__["UseSpecialTotalMass"] = value; return
		self._oleobj_.Invoke(*((5014, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialTransverseShearModulus1(self, value):
		if "UseSpecialTransverseShearModulus1" in self.__dict__: self.__dict__["UseSpecialTransverseShearModulus1"] = value; return
		self._oleobj_.Invoke(*((5062, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialTransverseShearModulus2(self, value):
		if "UseSpecialTransverseShearModulus2" in self.__dict__: self.__dict__["UseSpecialTransverseShearModulus2"] = value; return
		self._oleobj_.Invoke(*((5066, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialYoungsModulus(self, value):
		if "UseSpecialYoungsModulus" in self.__dict__: self.__dict__["UseSpecialYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((5018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialYoungsModulusX(self, value):
		if "UseSpecialYoungsModulusX" in self.__dict__: self.__dict__["UseSpecialYoungsModulusX"] = value; return
		self._oleobj_.Invoke(*((5030, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialYoungsModulusZ(self, value):
		if "UseSpecialYoungsModulusZ" in self.__dict__: self.__dict__["UseSpecialYoungsModulusZ"] = value; return
		self._oleobj_.Invoke(*((5034, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdateGeometryAutomatically(self, value):
		if "UseUpdateGeometryAutomatically" in self.__dict__: self.__dict__["UseUpdateGeometryAutomatically"] = value; return
		self._oleobj_.Invoke(*((5059, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserDefinedTransverseShearModulus(self, value):
		if "UseUserDefinedTransverseShearModulus" in self.__dict__: self.__dict__["UseUserDefinedTransverseShearModulus"] = value; return
		self._oleobj_.Invoke(*((5060, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	AllDampingRatio = property(_get_AllDampingRatio, _set_AllDampingRatio)
	'''
	Use all damping ratio

	:type: bool
	'''
	AllDensity = property(_get_AllDensity, _set_AllDensity)
	'''
	Use all density

	:type: bool
	'''
	AllG11 = property(_get_AllG11, _set_AllG11)
	'''
	Use all G11

	:type: bool
	'''
	AllG12 = property(_get_AllG12, _set_AllG12)
	'''
	Use all G12

	:type: bool
	'''
	AllG13 = property(_get_AllG13, _set_AllG13)
	'''
	Use all G13

	:type: bool
	'''
	AllG22 = property(_get_AllG22, _set_AllG22)
	'''
	Use all G22

	:type: bool
	'''
	AllG23 = property(_get_AllG23, _set_AllG23)
	'''
	Use all G23

	:type: bool
	'''
	AllG33 = property(_get_AllG33, _set_AllG33)
	'''
	Use all G33

	:type: bool
	'''
	AllPoissonsRatio = property(_get_AllPoissonsRatio, _set_AllPoissonsRatio)
	'''
	Use all poisson's ratio

	:type: bool
	'''
	AllPoissonsRatioXZ = property(_get_AllPoissonsRatioXZ, _set_AllPoissonsRatioXZ)
	'''
	Use all poisson's ratio of xz direction

	:type: bool
	'''
	AllShearModulusXZ = property(_get_AllShearModulusXZ, _set_AllShearModulusXZ)
	'''
	Use all shear modulus of xz direction

	:type: bool
	'''
	AllTotalMass = property(_get_AllTotalMass, _set_AllTotalMass)
	'''
	Use all total mass

	:type: bool
	'''
	AllTransverseShearModulus1 = property(_get_AllTransverseShearModulus1, _set_AllTransverseShearModulus1)
	'''
	Use all shear modulus of XY direction

	:type: bool
	'''
	AllTransverseShearModulus2 = property(_get_AllTransverseShearModulus2, _set_AllTransverseShearModulus2)
	'''
	Use all shear modulus of YZ direction

	:type: bool
	'''
	AllYoungsModulus = property(_get_AllYoungsModulus, _set_AllYoungsModulus)
	'''
	Use all young's modulus

	:type: bool
	'''
	AllYoungsModulusX = property(_get_AllYoungsModulusX, _set_AllYoungsModulusX)
	'''
	Use all young's modulus of x direction

	:type: bool
	'''
	AllYoungsModulusZ = property(_get_AllYoungsModulusZ, _set_AllYoungsModulusZ)
	'''
	Use all young's modulus of z direction

	:type: bool
	'''
	Color = property(_get_Color, _set_Color)
	'''
	Sheet color

	:type: int
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	CorrectionFactor = property(_get_CorrectionFactor, None)
	'''
	The correction factor of material property of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	CurlRadiusLateral = property(_get_CurlRadiusLateral, None)
	'''
	The lateral curl radius of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	CurlRadiusLongitudinal = property(_get_CurlRadiusLongitudinal, None)
	'''
	The longitudinal curl radius of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingRatio = property(_get_DampingRatio, None)
	'''
	The damping ratio of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	Density = property(_get_Density, None)
	'''
	The density of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	DirectionLateral = property(_get_DirectionLateral, _set_DirectionLateral)
	'''
	The lateral direction of the sheet

	:type: list[float]
	'''
	DirectionLongitudinal = property(_get_DirectionLongitudinal, _set_DirectionLongitudinal)
	'''
	The longitudinal direction of the sheet

	:type: list[float]
	'''
	FoldingDirection = property(_get_FoldingDirection, _set_FoldingDirection)
	'''
	The direction of folding

	:type: recurdyn.MTT3D.SheetDirectionType
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	G11 = property(_get_G11, None)
	'''
	The G11 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G12 = property(_get_G12, None)
	'''
	The G12 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G13 = property(_get_G13, None)
	'''
	The G13 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G22 = property(_get_G22, None)
	'''
	The G22 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G23 = property(_get_G23, None)
	'''
	The G23 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G33 = property(_get_G33, None)
	'''
	The G33 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	InitialVelocity = property(_get_InitialVelocity, None)
	'''
	The initial velocity of a sheet is in the direction of positive X axis of the markers on each sheet body

	:type: recurdyn.ProcessNet.IDouble
	'''
	InnerCPLateral = property(_get_InnerCPLateral, _set_InnerCPLateral)
	'''
	The number of lateral inner contact point of the sheet

	:type: int
	'''
	InnerCPLongitudinal = property(_get_InnerCPLongitudinal, _set_InnerCPLongitudinal)
	'''
	The number of longitudinal inner contact point of the sheet

	:type: int
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	LengthLateral = property(_get_LengthLateral, None)
	'''
	The lateral length of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	LengthLongitudinal = property(_get_LengthLongitudinal, None)
	'''
	The longitudinal length of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	MassType = property(_get_MassType, _set_MassType)
	'''
	The type of method to apply mass

	:type: recurdyn.ProcessNet.MassType
	'''
	MaterialDirectivity = property(_get_MaterialDirectivity, _set_MaterialDirectivity)
	'''
	The directivity of material property

	:type: recurdyn.ProcessNet.Directivity
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NodeNumberLateral = property(_get_NodeNumberLateral, None)
	'''
	The lateral node number of the sheet

	:type: int
	'''
	NodeNumberLongitudinal = property(_get_NodeNumberLongitudinal, None)
	'''
	The longitudinal node number of the sheet

	:type: int
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
	PointList = property(_get_PointList, None)
	'''
	A sheet folds through this points

	:type: recurdyn.ProcessNet.IPointCollection
	'''
	PoissonsRatio = property(_get_PoissonsRatio, None)
	'''
	The poisson's ratio of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	PoissonsRatioXZ = property(_get_PoissonsRatioXZ, None)
	'''
	The poisson's ratio of xz direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearModulusXZ = property(_get_ShearModulusXZ, None)
	'''
	The shear modulus of xz direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialDampingRatio = property(_get_SpecialDampingRatio, None)
	'''
	Special damping ratio

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialDensity = property(_get_SpecialDensity, None)
	'''
	Special density

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG11 = property(_get_SpecialG11, None)
	'''
	Special G11

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG12 = property(_get_SpecialG12, None)
	'''
	Special G12

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG13 = property(_get_SpecialG13, None)
	'''
	Special G13

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG22 = property(_get_SpecialG22, None)
	'''
	Special G22

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG23 = property(_get_SpecialG23, None)
	'''
	Special G23

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG33 = property(_get_SpecialG33, None)
	'''
	Special G33

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialPoissonsRatio = property(_get_SpecialPoissonsRatio, None)
	'''
	Special poisson's ratio

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialPoissonsRatioXZ = property(_get_SpecialPoissonsRatioXZ, None)
	'''
	Special poisson's ratio of xz direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialShearModulusXZ = property(_get_SpecialShearModulusXZ, None)
	'''
	Special shear modulus of xz direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialTotalMass = property(_get_SpecialTotalMass, None)
	'''
	Special total mass

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialTransverseShearModulus1 = property(_get_SpecialTransverseShearModulus1, None)
	'''
	Special shear modulus of XY direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialTransverseShearModulus2 = property(_get_SpecialTransverseShearModulus2, None)
	'''
	Special shear modulus of YZ direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialYoungsModulus = property(_get_SpecialYoungsModulus, None)
	'''
	Special young's modulus

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialYoungsModulusX = property(_get_SpecialYoungsModulusX, None)
	'''
	Special young's modulus of x direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialYoungsModulusZ = property(_get_SpecialYoungsModulusZ, None)
	'''
	Special young's modulus of z direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	StartPoint = property(_get_StartPoint, _set_StartPoint)
	'''
	The starting point of the sheet

	:type: list[float]
	'''
	Thickness = property(_get_Thickness, None)
	'''
	The thickness of a sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalMass = property(_get_TotalMass, None)
	'''
	The total mass of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	TransverseShearModulus1 = property(_get_TransverseShearModulus1, None)
	'''
	The shear modulus of XY direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	TransverseShearModulus2 = property(_get_TransverseShearModulus2, None)
	'''
	The shear modulus of YZ direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseInitialVelocity = property(_get_UseInitialVelocity, _set_UseInitialVelocity)
	'''
	Use initial velocity

	:type: bool
	'''
	UseSpecialDampingRatio = property(_get_UseSpecialDampingRatio, _set_UseSpecialDampingRatio)
	'''
	Use special damping ratio

	:type: bool
	'''
	UseSpecialDensity = property(_get_UseSpecialDensity, _set_UseSpecialDensity)
	'''
	Use special density

	:type: bool
	'''
	UseSpecialG11 = property(_get_UseSpecialG11, _set_UseSpecialG11)
	'''
	Use special G11

	:type: bool
	'''
	UseSpecialG12 = property(_get_UseSpecialG12, _set_UseSpecialG12)
	'''
	Use special G12

	:type: bool
	'''
	UseSpecialG13 = property(_get_UseSpecialG13, _set_UseSpecialG13)
	'''
	Use special G13

	:type: bool
	'''
	UseSpecialG22 = property(_get_UseSpecialG22, _set_UseSpecialG22)
	'''
	Use special G22

	:type: bool
	'''
	UseSpecialG23 = property(_get_UseSpecialG23, _set_UseSpecialG23)
	'''
	Use special G23

	:type: bool
	'''
	UseSpecialG33 = property(_get_UseSpecialG33, _set_UseSpecialG33)
	'''
	Use special G33

	:type: bool
	'''
	UseSpecialPoissonsRatio = property(_get_UseSpecialPoissonsRatio, _set_UseSpecialPoissonsRatio)
	'''
	Use special poisson's ratio

	:type: bool
	'''
	UseSpecialPoissonsRatioXZ = property(_get_UseSpecialPoissonsRatioXZ, _set_UseSpecialPoissonsRatioXZ)
	'''
	Use special poisson's ratio of xz direction

	:type: bool
	'''
	UseSpecialShearModulusXZ = property(_get_UseSpecialShearModulusXZ, _set_UseSpecialShearModulusXZ)
	'''
	Use special shear modulus of xz direction

	:type: bool
	'''
	UseSpecialTotalMass = property(_get_UseSpecialTotalMass, _set_UseSpecialTotalMass)
	'''
	Use special total mass

	:type: bool
	'''
	UseSpecialTransverseShearModulus1 = property(_get_UseSpecialTransverseShearModulus1, _set_UseSpecialTransverseShearModulus1)
	'''
	Use special shear modulus of XY direction

	:type: bool
	'''
	UseSpecialTransverseShearModulus2 = property(_get_UseSpecialTransverseShearModulus2, _set_UseSpecialTransverseShearModulus2)
	'''
	Use special shear modulus of YZ direction

	:type: bool
	'''
	UseSpecialYoungsModulus = property(_get_UseSpecialYoungsModulus, _set_UseSpecialYoungsModulus)
	'''
	Use special young's modulus

	:type: bool
	'''
	UseSpecialYoungsModulusX = property(_get_UseSpecialYoungsModulusX, _set_UseSpecialYoungsModulusX)
	'''
	Use special young's modulus of x direction

	:type: bool
	'''
	UseSpecialYoungsModulusZ = property(_get_UseSpecialYoungsModulusZ, _set_UseSpecialYoungsModulusZ)
	'''
	Use special young's modulus of z direction

	:type: bool
	'''
	UseUpdateGeometryAutomatically = property(_get_UseUpdateGeometryAutomatically, _set_UseUpdateGeometryAutomatically)
	'''
	Use Update Geometry Information Automatically

	:type: bool
	'''
	UseUserDefinedTransverseShearModulus = property(_get_UseUserDefinedTransverseShearModulus, _set_UseUserDefinedTransverseShearModulus)
	'''
	Use user-defined transverse shear modulus

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	The young's modulus of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	YoungsModulusX = property(_get_YoungsModulusX, None)
	'''
	The young's modulus of x direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	YoungsModulusZ = property(_get_YoungsModulusZ, None)
	'''
	The young's modulus of z direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_AllDampingRatio": _set_AllDampingRatio,
		"_set_AllDensity": _set_AllDensity,
		"_set_AllG11": _set_AllG11,
		"_set_AllG12": _set_AllG12,
		"_set_AllG13": _set_AllG13,
		"_set_AllG22": _set_AllG22,
		"_set_AllG23": _set_AllG23,
		"_set_AllG33": _set_AllG33,
		"_set_AllPoissonsRatio": _set_AllPoissonsRatio,
		"_set_AllPoissonsRatioXZ": _set_AllPoissonsRatioXZ,
		"_set_AllShearModulusXZ": _set_AllShearModulusXZ,
		"_set_AllTotalMass": _set_AllTotalMass,
		"_set_AllTransverseShearModulus1": _set_AllTransverseShearModulus1,
		"_set_AllTransverseShearModulus2": _set_AllTransverseShearModulus2,
		"_set_AllYoungsModulus": _set_AllYoungsModulus,
		"_set_AllYoungsModulusX": _set_AllYoungsModulusX,
		"_set_AllYoungsModulusZ": _set_AllYoungsModulusZ,
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_DirectionLateral": _set_DirectionLateral,
		"_set_DirectionLongitudinal": _set_DirectionLongitudinal,
		"_set_FoldingDirection": _set_FoldingDirection,
		"_set_InnerCPLateral": _set_InnerCPLateral,
		"_set_InnerCPLongitudinal": _set_InnerCPLongitudinal,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MassType": _set_MassType,
		"_set_MaterialDirectivity": _set_MaterialDirectivity,
		"_set_Name": _set_Name,
		"_set_StartPoint": _set_StartPoint,
		"_set_UseInitialVelocity": _set_UseInitialVelocity,
		"_set_UseSpecialDampingRatio": _set_UseSpecialDampingRatio,
		"_set_UseSpecialDensity": _set_UseSpecialDensity,
		"_set_UseSpecialG11": _set_UseSpecialG11,
		"_set_UseSpecialG12": _set_UseSpecialG12,
		"_set_UseSpecialG13": _set_UseSpecialG13,
		"_set_UseSpecialG22": _set_UseSpecialG22,
		"_set_UseSpecialG23": _set_UseSpecialG23,
		"_set_UseSpecialG33": _set_UseSpecialG33,
		"_set_UseSpecialPoissonsRatio": _set_UseSpecialPoissonsRatio,
		"_set_UseSpecialPoissonsRatioXZ": _set_UseSpecialPoissonsRatioXZ,
		"_set_UseSpecialShearModulusXZ": _set_UseSpecialShearModulusXZ,
		"_set_UseSpecialTotalMass": _set_UseSpecialTotalMass,
		"_set_UseSpecialTransverseShearModulus1": _set_UseSpecialTransverseShearModulus1,
		"_set_UseSpecialTransverseShearModulus2": _set_UseSpecialTransverseShearModulus2,
		"_set_UseSpecialYoungsModulus": _set_UseSpecialYoungsModulus,
		"_set_UseSpecialYoungsModulusX": _set_UseSpecialYoungsModulusX,
		"_set_UseSpecialYoungsModulusZ": _set_UseSpecialYoungsModulusZ,
		"_set_UseUpdateGeometryAutomatically": _set_UseUpdateGeometryAutomatically,
		"_set_UseUserDefinedTransverseShearModulus": _set_UseUserDefinedTransverseShearModulus,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"AllDampingRatio": (5021, 2, (11, 0), (), "AllDampingRatio", None),
		"AllDensity": (5009, 2, (11, 0), (), "AllDensity", None),
		"AllG11": (5069, 2, (11, 0), (), "AllG11", None),
		"AllG12": (5073, 2, (11, 0), (), "AllG12", None),
		"AllG13": (5077, 2, (11, 0), (), "AllG13", None),
		"AllG22": (5081, 2, (11, 0), (), "AllG22", None),
		"AllG23": (5085, 2, (11, 0), (), "AllG23", None),
		"AllG33": (5089, 2, (11, 0), (), "AllG33", None),
		"AllPoissonsRatio": (5025, 2, (11, 0), (), "AllPoissonsRatio", None),
		"AllPoissonsRatioXZ": (5037, 2, (11, 0), (), "AllPoissonsRatioXZ", None),
		"AllShearModulusXZ": (5041, 2, (11, 0), (), "AllShearModulusXZ", None),
		"AllTotalMass": (5013, 2, (11, 0), (), "AllTotalMass", None),
		"AllTransverseShearModulus1": (5061, 2, (11, 0), (), "AllTransverseShearModulus1", None),
		"AllTransverseShearModulus2": (5065, 2, (11, 0), (), "AllTransverseShearModulus2", None),
		"AllYoungsModulus": (5017, 2, (11, 0), (), "AllYoungsModulus", None),
		"AllYoungsModulusX": (5029, 2, (11, 0), (), "AllYoungsModulusX", None),
		"AllYoungsModulusZ": (5033, 2, (11, 0), (), "AllYoungsModulusZ", None),
		"Color": (5056, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"CorrectionFactor": (5045, 2, (9, 0), (), "CorrectionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CurlRadiusLateral": (5053, 2, (9, 0), (), "CurlRadiusLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CurlRadiusLongitudinal": (5052, 2, (9, 0), (), "CurlRadiusLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingRatio": (5023, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (5011, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DirectionLateral": (5047, 2, (8197, 0), (), "DirectionLateral", None),
		"DirectionLongitudinal": (5046, 2, (8197, 0), (), "DirectionLongitudinal", None),
		"FoldingDirection": (5002, 2, (3, 0), (), "FoldingDirection", '{D3EFD1DD-14F8-4256-91A0-C1C3CF317F38}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"G11": (5071, 2, (9, 0), (), "G11", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G12": (5075, 2, (9, 0), (), "G12", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G13": (5079, 2, (9, 0), (), "G13", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G22": (5083, 2, (9, 0), (), "G22", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G23": (5087, 2, (9, 0), (), "G23", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G33": (5091, 2, (9, 0), (), "G33", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InitialVelocity": (5006, 2, (9, 0), (), "InitialVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InnerCPLateral": (5055, 2, (19, 0), (), "InnerCPLateral", None),
		"InnerCPLongitudinal": (5054, 2, (19, 0), (), "InnerCPLongitudinal", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"LengthLateral": (5049, 2, (9, 0), (), "LengthLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LengthLongitudinal": (5048, 2, (9, 0), (), "LengthLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MassType": (5008, 2, (3, 0), (), "MassType", '{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}'),
		"MaterialDirectivity": (5007, 2, (3, 0), (), "MaterialDirectivity", '{40184A33-144F-4805-BD66-92A3769EAF8C}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeNumberLateral": (5051, 2, (19, 0), (), "NodeNumberLateral", None),
		"NodeNumberLongitudinal": (5050, 2, (19, 0), (), "NodeNumberLongitudinal", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PointList": (5003, 2, (9, 0), (), "PointList", '{6BEF9B6B-4708-445E-A3B5-0D65BA69F749}'),
		"PoissonsRatio": (5027, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PoissonsRatioXZ": (5039, 2, (9, 0), (), "PoissonsRatioXZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearModulusXZ": (5043, 2, (9, 0), (), "ShearModulusXZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialDampingRatio": (5024, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialDensity": (5012, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG11": (5072, 2, (9, 0), (), "SpecialG11", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG12": (5076, 2, (9, 0), (), "SpecialG12", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG13": (5080, 2, (9, 0), (), "SpecialG13", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG22": (5084, 2, (9, 0), (), "SpecialG22", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG23": (5088, 2, (9, 0), (), "SpecialG23", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG33": (5092, 2, (9, 0), (), "SpecialG33", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPoissonsRatio": (5028, 2, (9, 0), (), "SpecialPoissonsRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPoissonsRatioXZ": (5040, 2, (9, 0), (), "SpecialPoissonsRatioXZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialShearModulusXZ": (5044, 2, (9, 0), (), "SpecialShearModulusXZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialTotalMass": (5016, 2, (9, 0), (), "SpecialTotalMass", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialTransverseShearModulus1": (5064, 2, (9, 0), (), "SpecialTransverseShearModulus1", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialTransverseShearModulus2": (5068, 2, (9, 0), (), "SpecialTransverseShearModulus2", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialYoungsModulus": (5020, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialYoungsModulusX": (5032, 2, (9, 0), (), "SpecialYoungsModulusX", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialYoungsModulusZ": (5036, 2, (9, 0), (), "SpecialYoungsModulusZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"StartPoint": (5001, 2, (8197, 0), (), "StartPoint", None),
		"Thickness": (5004, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalMass": (5015, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TransverseShearModulus1": (5063, 2, (9, 0), (), "TransverseShearModulus1", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TransverseShearModulus2": (5067, 2, (9, 0), (), "TransverseShearModulus2", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseInitialVelocity": (5005, 2, (11, 0), (), "UseInitialVelocity", None),
		"UseSpecialDampingRatio": (5022, 2, (11, 0), (), "UseSpecialDampingRatio", None),
		"UseSpecialDensity": (5010, 2, (11, 0), (), "UseSpecialDensity", None),
		"UseSpecialG11": (5070, 2, (11, 0), (), "UseSpecialG11", None),
		"UseSpecialG12": (5074, 2, (11, 0), (), "UseSpecialG12", None),
		"UseSpecialG13": (5078, 2, (11, 0), (), "UseSpecialG13", None),
		"UseSpecialG22": (5082, 2, (11, 0), (), "UseSpecialG22", None),
		"UseSpecialG23": (5086, 2, (11, 0), (), "UseSpecialG23", None),
		"UseSpecialG33": (5090, 2, (11, 0), (), "UseSpecialG33", None),
		"UseSpecialPoissonsRatio": (5026, 2, (11, 0), (), "UseSpecialPoissonsRatio", None),
		"UseSpecialPoissonsRatioXZ": (5038, 2, (11, 0), (), "UseSpecialPoissonsRatioXZ", None),
		"UseSpecialShearModulusXZ": (5042, 2, (11, 0), (), "UseSpecialShearModulusXZ", None),
		"UseSpecialTotalMass": (5014, 2, (11, 0), (), "UseSpecialTotalMass", None),
		"UseSpecialTransverseShearModulus1": (5062, 2, (11, 0), (), "UseSpecialTransverseShearModulus1", None),
		"UseSpecialTransverseShearModulus2": (5066, 2, (11, 0), (), "UseSpecialTransverseShearModulus2", None),
		"UseSpecialYoungsModulus": (5018, 2, (11, 0), (), "UseSpecialYoungsModulus", None),
		"UseSpecialYoungsModulusX": (5030, 2, (11, 0), (), "UseSpecialYoungsModulusX", None),
		"UseSpecialYoungsModulusZ": (5034, 2, (11, 0), (), "UseSpecialYoungsModulusZ", None),
		"UseUpdateGeometryAutomatically": (5059, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None),
		"UseUserDefinedTransverseShearModulus": (5060, 2, (11, 0), (), "UseUserDefinedTransverseShearModulus", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"YoungsModulus": (5019, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YoungsModulusX": (5031, 2, (9, 0), (), "YoungsModulusX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YoungsModulusZ": (5035, 2, (9, 0), (), "YoungsModulusZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"AllDampingRatio": ((5021, LCID, 4, 0),()),
		"AllDensity": ((5009, LCID, 4, 0),()),
		"AllG11": ((5069, LCID, 4, 0),()),
		"AllG12": ((5073, LCID, 4, 0),()),
		"AllG13": ((5077, LCID, 4, 0),()),
		"AllG22": ((5081, LCID, 4, 0),()),
		"AllG23": ((5085, LCID, 4, 0),()),
		"AllG33": ((5089, LCID, 4, 0),()),
		"AllPoissonsRatio": ((5025, LCID, 4, 0),()),
		"AllPoissonsRatioXZ": ((5037, LCID, 4, 0),()),
		"AllShearModulusXZ": ((5041, LCID, 4, 0),()),
		"AllTotalMass": ((5013, LCID, 4, 0),()),
		"AllTransverseShearModulus1": ((5061, LCID, 4, 0),()),
		"AllTransverseShearModulus2": ((5065, LCID, 4, 0),()),
		"AllYoungsModulus": ((5017, LCID, 4, 0),()),
		"AllYoungsModulusX": ((5029, LCID, 4, 0),()),
		"AllYoungsModulusZ": ((5033, LCID, 4, 0),()),
		"Color": ((5056, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DirectionLateral": ((5047, LCID, 4, 0),()),
		"DirectionLongitudinal": ((5046, LCID, 4, 0),()),
		"FoldingDirection": ((5002, LCID, 4, 0),()),
		"InnerCPLateral": ((5055, LCID, 4, 0),()),
		"InnerCPLongitudinal": ((5054, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MassType": ((5008, LCID, 4, 0),()),
		"MaterialDirectivity": ((5007, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"StartPoint": ((5001, LCID, 4, 0),()),
		"UseInitialVelocity": ((5005, LCID, 4, 0),()),
		"UseSpecialDampingRatio": ((5022, LCID, 4, 0),()),
		"UseSpecialDensity": ((5010, LCID, 4, 0),()),
		"UseSpecialG11": ((5070, LCID, 4, 0),()),
		"UseSpecialG12": ((5074, LCID, 4, 0),()),
		"UseSpecialG13": ((5078, LCID, 4, 0),()),
		"UseSpecialG22": ((5082, LCID, 4, 0),()),
		"UseSpecialG23": ((5086, LCID, 4, 0),()),
		"UseSpecialG33": ((5090, LCID, 4, 0),()),
		"UseSpecialPoissonsRatio": ((5026, LCID, 4, 0),()),
		"UseSpecialPoissonsRatioXZ": ((5038, LCID, 4, 0),()),
		"UseSpecialShearModulusXZ": ((5042, LCID, 4, 0),()),
		"UseSpecialTotalMass": ((5014, LCID, 4, 0),()),
		"UseSpecialTransverseShearModulus1": ((5062, LCID, 4, 0),()),
		"UseSpecialTransverseShearModulus2": ((5066, LCID, 4, 0),()),
		"UseSpecialYoungsModulus": ((5018, LCID, 4, 0),()),
		"UseSpecialYoungsModulusX": ((5030, LCID, 4, 0),()),
		"UseSpecialYoungsModulusZ": ((5034, LCID, 4, 0),()),
		"UseUpdateGeometryAutomatically": ((5059, LCID, 4, 0),()),
		"UseUserDefinedTransverseShearModulus": ((5060, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DSheetShell(DispatchBaseClass):
	'''MTT3D sheet shell'''
	CLSID = IID('{170EFC31-8F09-46F5-8500-F888697C0581}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetNodeByID(self, nID):
		'''
		Get node by ID
		
		:param nID: int
		:rtype: recurdyn.MTT3D.IMTT3DNode
		'''
		ret = self._oleobj_.InvokeTypes(5158, LCID, 1, (9, 0), ((3, 1),),nID
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNodeByID', '{460C1F0E-80C4-4F4A-9E5B-DA282823C49E}')
		return ret

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
		return self._oleobj_.InvokeTypes(5057, LCID, 1, (24, 0), (),)


	def UpdateAllProperties2(self):
		'''
		Update all properties
		'''
		return self._oleobj_.InvokeTypes(5058, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_AirResistanceConstant(self):
		return self._ApplyTypes_(*(5111, 2, (9, 0), (), "AirResistanceConstant", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_AirResistanceExpression(self):
		return self._ApplyTypes_(*(5112, 2, (9, 0), (), "AirResistanceExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_AirResistanceType(self):
		return self._ApplyTypes_(*(5110, 2, (3, 0), (), "AirResistanceType", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C4}'))
	def _get_AllDampingRatio(self):
		return self._ApplyTypes_(*(5021, 2, (11, 0), (), "AllDampingRatio", None))
	def _get_AllDensity(self):
		return self._ApplyTypes_(*(5009, 2, (11, 0), (), "AllDensity", None))
	def _get_AllG11(self):
		return self._ApplyTypes_(*(5069, 2, (11, 0), (), "AllG11", None))
	def _get_AllG12(self):
		return self._ApplyTypes_(*(5073, 2, (11, 0), (), "AllG12", None))
	def _get_AllG13(self):
		return self._ApplyTypes_(*(5077, 2, (11, 0), (), "AllG13", None))
	def _get_AllG22(self):
		return self._ApplyTypes_(*(5081, 2, (11, 0), (), "AllG22", None))
	def _get_AllG23(self):
		return self._ApplyTypes_(*(5085, 2, (11, 0), (), "AllG23", None))
	def _get_AllG33(self):
		return self._ApplyTypes_(*(5089, 2, (11, 0), (), "AllG33", None))
	def _get_AllPoissonsRatio(self):
		return self._ApplyTypes_(*(5025, 2, (11, 0), (), "AllPoissonsRatio", None))
	def _get_AllPoissonsRatioXZ(self):
		return self._ApplyTypes_(*(5037, 2, (11, 0), (), "AllPoissonsRatioXZ", None))
	def _get_AllShearModulusXZ(self):
		return self._ApplyTypes_(*(5041, 2, (11, 0), (), "AllShearModulusXZ", None))
	def _get_AllTotalMass(self):
		return self._ApplyTypes_(*(5013, 2, (11, 0), (), "AllTotalMass", None))
	def _get_AllTransverseShearModulus1(self):
		return self._ApplyTypes_(*(5061, 2, (11, 0), (), "AllTransverseShearModulus1", None))
	def _get_AllTransverseShearModulus2(self):
		return self._ApplyTypes_(*(5065, 2, (11, 0), (), "AllTransverseShearModulus2", None))
	def _get_AllYoungsModulus(self):
		return self._ApplyTypes_(*(5017, 2, (11, 0), (), "AllYoungsModulus", None))
	def _get_AllYoungsModulusX(self):
		return self._ApplyTypes_(*(5029, 2, (11, 0), (), "AllYoungsModulusX", None))
	def _get_AllYoungsModulusZ(self):
		return self._ApplyTypes_(*(5033, 2, (11, 0), (), "AllYoungsModulusZ", None))
	def _get_BCOrienation(self):
		return self._ApplyTypes_(*(5160, 2, (3, 0), (), "BCOrienation", '{4FBFC632-BAF4-489E-89CE-DD64AA55D620}'))
	def _get_Color(self):
		return self._ApplyTypes_(*(5056, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_CorrectionFactor(self):
		return self._ApplyTypes_(*(5045, 2, (9, 0), (), "CorrectionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CurlRadiusLateral(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "CurlRadiusLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CurlRadiusLongitudinal(self):
		return self._ApplyTypes_(*(5052, 2, (9, 0), (), "CurlRadiusLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(5023, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(5011, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DirectionLateral(self):
		return self._ApplyTypes_(*(5047, 2, (8197, 0), (), "DirectionLateral", None))
	def _get_DirectionLongitudinal(self):
		return self._ApplyTypes_(*(5046, 2, (8197, 0), (), "DirectionLongitudinal", None))
	def _get_DrillingStiffnessFactor(self):
		return self._ApplyTypes_(*(5101, 2, (9, 0), (), "DrillingStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ElementLengthLateral(self):
		return self._ApplyTypes_(*(5106, 2, (9, 0), (), "ElementLengthLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ElementLengthLongitudinal(self):
		return self._ApplyTypes_(*(5105, 2, (9, 0), (), "ElementLengthLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ElementNumberLateral(self):
		return self._ApplyTypes_(*(5108, 2, (19, 0), (), "ElementNumberLateral", None))
	def _get_ElementNumberLongitudinal(self):
		return self._ApplyTypes_(*(5107, 2, (19, 0), (), "ElementNumberLongitudinal", None))
	def _get_FlexBody(self):
		return self._ApplyTypes_(*(5161, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'))
	def _get_FoldingDirection(self):
		return self._ApplyTypes_(*(5002, 2, (3, 0), (), "FoldingDirection", '{D3EFD1DD-14F8-4256-91A0-C1C3CF317F38}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_G11(self):
		return self._ApplyTypes_(*(5071, 2, (9, 0), (), "G11", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G12(self):
		return self._ApplyTypes_(*(5075, 2, (9, 0), (), "G12", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G13(self):
		return self._ApplyTypes_(*(5079, 2, (9, 0), (), "G13", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G22(self):
		return self._ApplyTypes_(*(5083, 2, (9, 0), (), "G22", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G23(self):
		return self._ApplyTypes_(*(5087, 2, (9, 0), (), "G23", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G33(self):
		return self._ApplyTypes_(*(5091, 2, (9, 0), (), "G33", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InitialVelocity(self):
		return self._ApplyTypes_(*(5006, 2, (9, 0), (), "InitialVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InnerCPLateral(self):
		return self._ApplyTypes_(*(5055, 2, (19, 0), (), "InnerCPLateral", None))
	def _get_InnerCPLongitudinal(self):
		return self._ApplyTypes_(*(5054, 2, (19, 0), (), "InnerCPLongitudinal", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_LengthLateral(self):
		return self._ApplyTypes_(*(5049, 2, (9, 0), (), "LengthLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LengthLongitudinal(self):
		return self._ApplyTypes_(*(5048, 2, (9, 0), (), "LengthLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MassType(self):
		return self._ApplyTypes_(*(5008, 2, (3, 0), (), "MassType", '{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}'))
	def _get_MaterialDirectivity(self):
		return self._ApplyTypes_(*(5007, 2, (3, 0), (), "MaterialDirectivity", '{40184A33-144F-4805-BD66-92A3769EAF8C}'))
	def _get_MeshType(self):
		return self._ApplyTypes_(*(5104, 2, (3, 0), (), "MeshType", '{8407A29C-89E9-48A8-B030-28EFA5125C51}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeNumberLateral(self):
		return self._ApplyTypes_(*(5051, 2, (19, 0), (), "NodeNumberLateral", None))
	def _get_NodeNumberLongitudinal(self):
		return self._ApplyTypes_(*(5050, 2, (19, 0), (), "NodeNumberLongitudinal", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PointList(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "PointList", '{6BEF9B6B-4708-445E-A3B5-0D65BA69F749}'))
	def _get_PoissonsRatio(self):
		return self._ApplyTypes_(*(5027, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PoissonsRatioXZ(self):
		return self._ApplyTypes_(*(5039, 2, (9, 0), (), "PoissonsRatioXZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShapeType(self):
		return self._ApplyTypes_(*(5102, 2, (3, 0), (), "ShapeType", '{A875895D-5F56-4ABB-81DF-DB853BFD27A7}'))
	def _get_ShearModulusXZ(self):
		return self._ApplyTypes_(*(5043, 2, (9, 0), (), "ShearModulusXZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialDampingRatio(self):
		return self._ApplyTypes_(*(5024, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialDensity(self):
		return self._ApplyTypes_(*(5012, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG11(self):
		return self._ApplyTypes_(*(5072, 2, (9, 0), (), "SpecialG11", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG12(self):
		return self._ApplyTypes_(*(5076, 2, (9, 0), (), "SpecialG12", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG13(self):
		return self._ApplyTypes_(*(5080, 2, (9, 0), (), "SpecialG13", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG22(self):
		return self._ApplyTypes_(*(5084, 2, (9, 0), (), "SpecialG22", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG23(self):
		return self._ApplyTypes_(*(5088, 2, (9, 0), (), "SpecialG23", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialG33(self):
		return self._ApplyTypes_(*(5092, 2, (9, 0), (), "SpecialG33", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPoissonsRatio(self):
		return self._ApplyTypes_(*(5028, 2, (9, 0), (), "SpecialPoissonsRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPoissonsRatioXZ(self):
		return self._ApplyTypes_(*(5040, 2, (9, 0), (), "SpecialPoissonsRatioXZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialShearModulusXZ(self):
		return self._ApplyTypes_(*(5044, 2, (9, 0), (), "SpecialShearModulusXZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialTotalMass(self):
		return self._ApplyTypes_(*(5016, 2, (9, 0), (), "SpecialTotalMass", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialTransverseShearModulus1(self):
		return self._ApplyTypes_(*(5064, 2, (9, 0), (), "SpecialTransverseShearModulus1", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialTransverseShearModulus2(self):
		return self._ApplyTypes_(*(5068, 2, (9, 0), (), "SpecialTransverseShearModulus2", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialYoungsModulus(self):
		return self._ApplyTypes_(*(5020, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialYoungsModulusX(self):
		return self._ApplyTypes_(*(5032, 2, (9, 0), (), "SpecialYoungsModulusX", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialYoungsModulusZ(self):
		return self._ApplyTypes_(*(5036, 2, (9, 0), (), "SpecialYoungsModulusZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SplineSurface(self):
		return self._ApplyTypes_(*(5103, 2, (9, 0), (), "SplineSurface", '{DB76B99A-A0F1-45CD-A2B1-6BC5EC75CD8F}'))
	def _get_StartPoint(self):
		return self._ApplyTypes_(*(5001, 2, (8197, 0), (), "StartPoint", None))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(5004, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(5015, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TransverseShearModulus1(self):
		return self._ApplyTypes_(*(5063, 2, (9, 0), (), "TransverseShearModulus1", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TransverseShearModulus2(self):
		return self._ApplyTypes_(*(5067, 2, (9, 0), (), "TransverseShearModulus2", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseAirResistance(self):
		return self._ApplyTypes_(*(5109, 2, (11, 0), (), "UseAirResistance", None))
	def _get_UseInitialVelocity(self):
		return self._ApplyTypes_(*(5005, 2, (11, 0), (), "UseInitialVelocity", None))
	def _get_UseSpecialDampingRatio(self):
		return self._ApplyTypes_(*(5022, 2, (11, 0), (), "UseSpecialDampingRatio", None))
	def _get_UseSpecialDensity(self):
		return self._ApplyTypes_(*(5010, 2, (11, 0), (), "UseSpecialDensity", None))
	def _get_UseSpecialG11(self):
		return self._ApplyTypes_(*(5070, 2, (11, 0), (), "UseSpecialG11", None))
	def _get_UseSpecialG12(self):
		return self._ApplyTypes_(*(5074, 2, (11, 0), (), "UseSpecialG12", None))
	def _get_UseSpecialG13(self):
		return self._ApplyTypes_(*(5078, 2, (11, 0), (), "UseSpecialG13", None))
	def _get_UseSpecialG22(self):
		return self._ApplyTypes_(*(5082, 2, (11, 0), (), "UseSpecialG22", None))
	def _get_UseSpecialG23(self):
		return self._ApplyTypes_(*(5086, 2, (11, 0), (), "UseSpecialG23", None))
	def _get_UseSpecialG33(self):
		return self._ApplyTypes_(*(5090, 2, (11, 0), (), "UseSpecialG33", None))
	def _get_UseSpecialPoissonsRatio(self):
		return self._ApplyTypes_(*(5026, 2, (11, 0), (), "UseSpecialPoissonsRatio", None))
	def _get_UseSpecialPoissonsRatioXZ(self):
		return self._ApplyTypes_(*(5038, 2, (11, 0), (), "UseSpecialPoissonsRatioXZ", None))
	def _get_UseSpecialShearModulusXZ(self):
		return self._ApplyTypes_(*(5042, 2, (11, 0), (), "UseSpecialShearModulusXZ", None))
	def _get_UseSpecialTotalMass(self):
		return self._ApplyTypes_(*(5014, 2, (11, 0), (), "UseSpecialTotalMass", None))
	def _get_UseSpecialTransverseShearModulus1(self):
		return self._ApplyTypes_(*(5062, 2, (11, 0), (), "UseSpecialTransverseShearModulus1", None))
	def _get_UseSpecialTransverseShearModulus2(self):
		return self._ApplyTypes_(*(5066, 2, (11, 0), (), "UseSpecialTransverseShearModulus2", None))
	def _get_UseSpecialYoungsModulus(self):
		return self._ApplyTypes_(*(5018, 2, (11, 0), (), "UseSpecialYoungsModulus", None))
	def _get_UseSpecialYoungsModulusX(self):
		return self._ApplyTypes_(*(5030, 2, (11, 0), (), "UseSpecialYoungsModulusX", None))
	def _get_UseSpecialYoungsModulusZ(self):
		return self._ApplyTypes_(*(5034, 2, (11, 0), (), "UseSpecialYoungsModulusZ", None))
	def _get_UseUpdateGeometryAutomatically(self):
		return self._ApplyTypes_(*(5059, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None))
	def _get_UseUserDefinedTransverseShearModulus(self):
		return self._ApplyTypes_(*(5060, 2, (11, 0), (), "UseUserDefinedTransverseShearModulus", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(5019, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YoungsModulusX(self):
		return self._ApplyTypes_(*(5031, 2, (9, 0), (), "YoungsModulusX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YoungsModulusZ(self):
		return self._ApplyTypes_(*(5035, 2, (9, 0), (), "YoungsModulusZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_AirResistanceExpression(self, value):
		if "AirResistanceExpression" in self.__dict__: self.__dict__["AirResistanceExpression"] = value; return
		self._oleobj_.Invoke(*((5112, LCID, 4, 0) + (value,) + ()))
	def _set_AirResistanceType(self, value):
		if "AirResistanceType" in self.__dict__: self.__dict__["AirResistanceType"] = value; return
		self._oleobj_.Invoke(*((5110, LCID, 4, 0) + (value,) + ()))
	def _set_AllDampingRatio(self, value):
		if "AllDampingRatio" in self.__dict__: self.__dict__["AllDampingRatio"] = value; return
		self._oleobj_.Invoke(*((5021, LCID, 4, 0) + (value,) + ()))
	def _set_AllDensity(self, value):
		if "AllDensity" in self.__dict__: self.__dict__["AllDensity"] = value; return
		self._oleobj_.Invoke(*((5009, LCID, 4, 0) + (value,) + ()))
	def _set_AllG11(self, value):
		if "AllG11" in self.__dict__: self.__dict__["AllG11"] = value; return
		self._oleobj_.Invoke(*((5069, LCID, 4, 0) + (value,) + ()))
	def _set_AllG12(self, value):
		if "AllG12" in self.__dict__: self.__dict__["AllG12"] = value; return
		self._oleobj_.Invoke(*((5073, LCID, 4, 0) + (value,) + ()))
	def _set_AllG13(self, value):
		if "AllG13" in self.__dict__: self.__dict__["AllG13"] = value; return
		self._oleobj_.Invoke(*((5077, LCID, 4, 0) + (value,) + ()))
	def _set_AllG22(self, value):
		if "AllG22" in self.__dict__: self.__dict__["AllG22"] = value; return
		self._oleobj_.Invoke(*((5081, LCID, 4, 0) + (value,) + ()))
	def _set_AllG23(self, value):
		if "AllG23" in self.__dict__: self.__dict__["AllG23"] = value; return
		self._oleobj_.Invoke(*((5085, LCID, 4, 0) + (value,) + ()))
	def _set_AllG33(self, value):
		if "AllG33" in self.__dict__: self.__dict__["AllG33"] = value; return
		self._oleobj_.Invoke(*((5089, LCID, 4, 0) + (value,) + ()))
	def _set_AllPoissonsRatio(self, value):
		if "AllPoissonsRatio" in self.__dict__: self.__dict__["AllPoissonsRatio"] = value; return
		self._oleobj_.Invoke(*((5025, LCID, 4, 0) + (value,) + ()))
	def _set_AllPoissonsRatioXZ(self, value):
		if "AllPoissonsRatioXZ" in self.__dict__: self.__dict__["AllPoissonsRatioXZ"] = value; return
		self._oleobj_.Invoke(*((5037, LCID, 4, 0) + (value,) + ()))
	def _set_AllShearModulusXZ(self, value):
		if "AllShearModulusXZ" in self.__dict__: self.__dict__["AllShearModulusXZ"] = value; return
		self._oleobj_.Invoke(*((5041, LCID, 4, 0) + (value,) + ()))
	def _set_AllTotalMass(self, value):
		if "AllTotalMass" in self.__dict__: self.__dict__["AllTotalMass"] = value; return
		self._oleobj_.Invoke(*((5013, LCID, 4, 0) + (value,) + ()))
	def _set_AllTransverseShearModulus1(self, value):
		if "AllTransverseShearModulus1" in self.__dict__: self.__dict__["AllTransverseShearModulus1"] = value; return
		self._oleobj_.Invoke(*((5061, LCID, 4, 0) + (value,) + ()))
	def _set_AllTransverseShearModulus2(self, value):
		if "AllTransverseShearModulus2" in self.__dict__: self.__dict__["AllTransverseShearModulus2"] = value; return
		self._oleobj_.Invoke(*((5065, LCID, 4, 0) + (value,) + ()))
	def _set_AllYoungsModulus(self, value):
		if "AllYoungsModulus" in self.__dict__: self.__dict__["AllYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((5017, LCID, 4, 0) + (value,) + ()))
	def _set_AllYoungsModulusX(self, value):
		if "AllYoungsModulusX" in self.__dict__: self.__dict__["AllYoungsModulusX"] = value; return
		self._oleobj_.Invoke(*((5029, LCID, 4, 0) + (value,) + ()))
	def _set_AllYoungsModulusZ(self, value):
		if "AllYoungsModulusZ" in self.__dict__: self.__dict__["AllYoungsModulusZ"] = value; return
		self._oleobj_.Invoke(*((5033, LCID, 4, 0) + (value,) + ()))
	def _set_BCOrienation(self, value):
		if "BCOrienation" in self.__dict__: self.__dict__["BCOrienation"] = value; return
		self._oleobj_.Invoke(*((5160, LCID, 4, 0) + (value,) + ()))
	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((5056, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DirectionLateral(self, value):
		if "DirectionLateral" in self.__dict__: self.__dict__["DirectionLateral"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5047, LCID, 4, 0) + (variantValue,) + ()))
	def _set_DirectionLongitudinal(self, value):
		if "DirectionLongitudinal" in self.__dict__: self.__dict__["DirectionLongitudinal"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5046, LCID, 4, 0) + (variantValue,) + ()))
	def _set_FoldingDirection(self, value):
		if "FoldingDirection" in self.__dict__: self.__dict__["FoldingDirection"] = value; return
		self._oleobj_.Invoke(*((5002, LCID, 4, 0) + (value,) + ()))
	def _set_InnerCPLateral(self, value):
		if "InnerCPLateral" in self.__dict__: self.__dict__["InnerCPLateral"] = value; return
		self._oleobj_.Invoke(*((5055, LCID, 4, 0) + (value,) + ()))
	def _set_InnerCPLongitudinal(self, value):
		if "InnerCPLongitudinal" in self.__dict__: self.__dict__["InnerCPLongitudinal"] = value; return
		self._oleobj_.Invoke(*((5054, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MassType(self, value):
		if "MassType" in self.__dict__: self.__dict__["MassType"] = value; return
		self._oleobj_.Invoke(*((5008, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialDirectivity(self, value):
		if "MaterialDirectivity" in self.__dict__: self.__dict__["MaterialDirectivity"] = value; return
		self._oleobj_.Invoke(*((5007, LCID, 4, 0) + (value,) + ()))
	def _set_MeshType(self, value):
		if "MeshType" in self.__dict__: self.__dict__["MeshType"] = value; return
		self._oleobj_.Invoke(*((5104, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ShapeType(self, value):
		if "ShapeType" in self.__dict__: self.__dict__["ShapeType"] = value; return
		self._oleobj_.Invoke(*((5102, LCID, 4, 0) + (value,) + ()))
	def _set_StartPoint(self, value):
		if "StartPoint" in self.__dict__: self.__dict__["StartPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5001, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseAirResistance(self, value):
		if "UseAirResistance" in self.__dict__: self.__dict__["UseAirResistance"] = value; return
		self._oleobj_.Invoke(*((5109, LCID, 4, 0) + (value,) + ()))
	def _set_UseExtractWithoutPreStress(self, value):
		if "UseExtractWithoutPreStress" in self.__dict__: self.__dict__["UseExtractWithoutPreStress"] = value; return
		self._oleobj_.Invoke(*((5159, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialVelocity(self, value):
		if "UseInitialVelocity" in self.__dict__: self.__dict__["UseInitialVelocity"] = value; return
		self._oleobj_.Invoke(*((5005, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDampingRatio(self, value):
		if "UseSpecialDampingRatio" in self.__dict__: self.__dict__["UseSpecialDampingRatio"] = value; return
		self._oleobj_.Invoke(*((5022, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDensity(self, value):
		if "UseSpecialDensity" in self.__dict__: self.__dict__["UseSpecialDensity"] = value; return
		self._oleobj_.Invoke(*((5010, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG11(self, value):
		if "UseSpecialG11" in self.__dict__: self.__dict__["UseSpecialG11"] = value; return
		self._oleobj_.Invoke(*((5070, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG12(self, value):
		if "UseSpecialG12" in self.__dict__: self.__dict__["UseSpecialG12"] = value; return
		self._oleobj_.Invoke(*((5074, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG13(self, value):
		if "UseSpecialG13" in self.__dict__: self.__dict__["UseSpecialG13"] = value; return
		self._oleobj_.Invoke(*((5078, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG22(self, value):
		if "UseSpecialG22" in self.__dict__: self.__dict__["UseSpecialG22"] = value; return
		self._oleobj_.Invoke(*((5082, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG23(self, value):
		if "UseSpecialG23" in self.__dict__: self.__dict__["UseSpecialG23"] = value; return
		self._oleobj_.Invoke(*((5086, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialG33(self, value):
		if "UseSpecialG33" in self.__dict__: self.__dict__["UseSpecialG33"] = value; return
		self._oleobj_.Invoke(*((5090, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPoissonsRatio(self, value):
		if "UseSpecialPoissonsRatio" in self.__dict__: self.__dict__["UseSpecialPoissonsRatio"] = value; return
		self._oleobj_.Invoke(*((5026, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPoissonsRatioXZ(self, value):
		if "UseSpecialPoissonsRatioXZ" in self.__dict__: self.__dict__["UseSpecialPoissonsRatioXZ"] = value; return
		self._oleobj_.Invoke(*((5038, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialShearModulusXZ(self, value):
		if "UseSpecialShearModulusXZ" in self.__dict__: self.__dict__["UseSpecialShearModulusXZ"] = value; return
		self._oleobj_.Invoke(*((5042, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialTotalMass(self, value):
		if "UseSpecialTotalMass" in self.__dict__: self.__dict__["UseSpecialTotalMass"] = value; return
		self._oleobj_.Invoke(*((5014, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialTransverseShearModulus1(self, value):
		if "UseSpecialTransverseShearModulus1" in self.__dict__: self.__dict__["UseSpecialTransverseShearModulus1"] = value; return
		self._oleobj_.Invoke(*((5062, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialTransverseShearModulus2(self, value):
		if "UseSpecialTransverseShearModulus2" in self.__dict__: self.__dict__["UseSpecialTransverseShearModulus2"] = value; return
		self._oleobj_.Invoke(*((5066, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialYoungsModulus(self, value):
		if "UseSpecialYoungsModulus" in self.__dict__: self.__dict__["UseSpecialYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((5018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialYoungsModulusX(self, value):
		if "UseSpecialYoungsModulusX" in self.__dict__: self.__dict__["UseSpecialYoungsModulusX"] = value; return
		self._oleobj_.Invoke(*((5030, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialYoungsModulusZ(self, value):
		if "UseSpecialYoungsModulusZ" in self.__dict__: self.__dict__["UseSpecialYoungsModulusZ"] = value; return
		self._oleobj_.Invoke(*((5034, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdateGeometryAutomatically(self, value):
		if "UseUpdateGeometryAutomatically" in self.__dict__: self.__dict__["UseUpdateGeometryAutomatically"] = value; return
		self._oleobj_.Invoke(*((5059, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserDefinedTransverseShearModulus(self, value):
		if "UseUserDefinedTransverseShearModulus" in self.__dict__: self.__dict__["UseUserDefinedTransverseShearModulus"] = value; return
		self._oleobj_.Invoke(*((5060, LCID, 4, 0) + (value,) + ()))
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
	AirResistanceType = property(_get_AirResistanceType, _set_AirResistanceType)
	'''
	Air Resistance Coefficient Type

	:type: recurdyn.MTT3D.AirResistanceType
	'''
	AllDampingRatio = property(_get_AllDampingRatio, _set_AllDampingRatio)
	'''
	Use all damping ratio

	:type: bool
	'''
	AllDensity = property(_get_AllDensity, _set_AllDensity)
	'''
	Use all density

	:type: bool
	'''
	AllG11 = property(_get_AllG11, _set_AllG11)
	'''
	Use all G11

	:type: bool
	'''
	AllG12 = property(_get_AllG12, _set_AllG12)
	'''
	Use all G12

	:type: bool
	'''
	AllG13 = property(_get_AllG13, _set_AllG13)
	'''
	Use all G13

	:type: bool
	'''
	AllG22 = property(_get_AllG22, _set_AllG22)
	'''
	Use all G22

	:type: bool
	'''
	AllG23 = property(_get_AllG23, _set_AllG23)
	'''
	Use all G23

	:type: bool
	'''
	AllG33 = property(_get_AllG33, _set_AllG33)
	'''
	Use all G33

	:type: bool
	'''
	AllPoissonsRatio = property(_get_AllPoissonsRatio, _set_AllPoissonsRatio)
	'''
	Use all poisson's ratio

	:type: bool
	'''
	AllPoissonsRatioXZ = property(_get_AllPoissonsRatioXZ, _set_AllPoissonsRatioXZ)
	'''
	Use all poisson's ratio of xz direction

	:type: bool
	'''
	AllShearModulusXZ = property(_get_AllShearModulusXZ, _set_AllShearModulusXZ)
	'''
	Use all shear modulus of xz direction

	:type: bool
	'''
	AllTotalMass = property(_get_AllTotalMass, _set_AllTotalMass)
	'''
	Use all total mass

	:type: bool
	'''
	AllTransverseShearModulus1 = property(_get_AllTransverseShearModulus1, _set_AllTransverseShearModulus1)
	'''
	Use all shear modulus of XY direction

	:type: bool
	'''
	AllTransverseShearModulus2 = property(_get_AllTransverseShearModulus2, _set_AllTransverseShearModulus2)
	'''
	Use all shear modulus of YZ direction

	:type: bool
	'''
	AllYoungsModulus = property(_get_AllYoungsModulus, _set_AllYoungsModulus)
	'''
	Use all young's modulus

	:type: bool
	'''
	AllYoungsModulusX = property(_get_AllYoungsModulusX, _set_AllYoungsModulusX)
	'''
	Use all young's modulus of x direction

	:type: bool
	'''
	AllYoungsModulusZ = property(_get_AllYoungsModulusZ, _set_AllYoungsModulusZ)
	'''
	Use all young's modulus of z direction

	:type: bool
	'''
	BCOrienation = property(_get_BCOrienation, _set_BCOrienation)
	'''
	BC Orienation

	:type: recurdyn.MTT3D.MTT3DBCOrienationType
	'''
	Color = property(_get_Color, _set_Color)
	'''
	Sheet color

	:type: int
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	CorrectionFactor = property(_get_CorrectionFactor, None)
	'''
	The correction factor of material property of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	CurlRadiusLateral = property(_get_CurlRadiusLateral, None)
	'''
	The lateral curl radius of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	CurlRadiusLongitudinal = property(_get_CurlRadiusLongitudinal, None)
	'''
	The longitudinal curl radius of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingRatio = property(_get_DampingRatio, None)
	'''
	The damping ratio of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	Density = property(_get_Density, None)
	'''
	The density of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	DirectionLateral = property(_get_DirectionLateral, _set_DirectionLateral)
	'''
	The lateral direction of the sheet

	:type: list[float]
	'''
	DirectionLongitudinal = property(_get_DirectionLongitudinal, _set_DirectionLongitudinal)
	'''
	The longitudinal direction of the sheet

	:type: list[float]
	'''
	DrillingStiffnessFactor = property(_get_DrillingStiffnessFactor, None)
	'''
	The drilling stiffness factor of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	ElementLengthLateral = property(_get_ElementLengthLateral, None)
	'''
	The lateral element length of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	ElementLengthLongitudinal = property(_get_ElementLengthLongitudinal, None)
	'''
	The longitudinal element length of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	ElementNumberLateral = property(_get_ElementNumberLateral, None)
	'''
	The lateral element number of the sheet

	:type: int
	'''
	ElementNumberLongitudinal = property(_get_ElementNumberLongitudinal, None)
	'''
	The longitudinal element number of the sheet

	:type: int
	'''
	FlexBody = property(_get_FlexBody, None)
	'''
	Flex body edit

	:type: recurdyn.FFlex.IFFlexToolkitBody
	'''
	FoldingDirection = property(_get_FoldingDirection, _set_FoldingDirection)
	'''
	The direction of folding

	:type: recurdyn.MTT3D.SheetDirectionType
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	G11 = property(_get_G11, None)
	'''
	The G11 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G12 = property(_get_G12, None)
	'''
	The G12 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G13 = property(_get_G13, None)
	'''
	The G13 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G22 = property(_get_G22, None)
	'''
	The G22 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G23 = property(_get_G23, None)
	'''
	The G23 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	G33 = property(_get_G33, None)
	'''
	The G33 of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	InitialVelocity = property(_get_InitialVelocity, None)
	'''
	The initial velocity of a sheet is in the direction of positive X axis of the markers on each sheet body

	:type: recurdyn.ProcessNet.IDouble
	'''
	InnerCPLateral = property(_get_InnerCPLateral, _set_InnerCPLateral)
	'''
	The number of lateral inner contact point of the sheet

	:type: int
	'''
	InnerCPLongitudinal = property(_get_InnerCPLongitudinal, _set_InnerCPLongitudinal)
	'''
	The number of longitudinal inner contact point of the sheet

	:type: int
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	LengthLateral = property(_get_LengthLateral, None)
	'''
	The lateral length of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	LengthLongitudinal = property(_get_LengthLongitudinal, None)
	'''
	The longitudinal length of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	MassType = property(_get_MassType, _set_MassType)
	'''
	The type of method to apply mass

	:type: recurdyn.ProcessNet.MassType
	'''
	MaterialDirectivity = property(_get_MaterialDirectivity, _set_MaterialDirectivity)
	'''
	The directivity of material property

	:type: recurdyn.ProcessNet.Directivity
	'''
	MeshType = property(_get_MeshType, _set_MeshType)
	'''
	The type of method to mesh sheet

	:type: recurdyn.MTT3D.SheetMeshType
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NodeNumberLateral = property(_get_NodeNumberLateral, None)
	'''
	The lateral node number of the sheet

	:type: int
	'''
	NodeNumberLongitudinal = property(_get_NodeNumberLongitudinal, None)
	'''
	The longitudinal node number of the sheet

	:type: int
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
	PointList = property(_get_PointList, None)
	'''
	A sheet folds through this points

	:type: recurdyn.ProcessNet.IPointCollection
	'''
	PoissonsRatio = property(_get_PoissonsRatio, None)
	'''
	The poisson's ratio of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	PoissonsRatioXZ = property(_get_PoissonsRatioXZ, None)
	'''
	The poisson's ratio of xz direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShapeType = property(_get_ShapeType, _set_ShapeType)
	'''
	Sheet type

	:type: recurdyn.MTT3D.SheetShapeType
	'''
	ShearModulusXZ = property(_get_ShearModulusXZ, None)
	'''
	The shear modulus of xz direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpecialDampingRatio = property(_get_SpecialDampingRatio, None)
	'''
	Special damping ratio

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialDensity = property(_get_SpecialDensity, None)
	'''
	Special density

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG11 = property(_get_SpecialG11, None)
	'''
	Special G11

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG12 = property(_get_SpecialG12, None)
	'''
	Special G12

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG13 = property(_get_SpecialG13, None)
	'''
	Special G13

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG22 = property(_get_SpecialG22, None)
	'''
	Special G22

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG23 = property(_get_SpecialG23, None)
	'''
	Special G23

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialG33 = property(_get_SpecialG33, None)
	'''
	Special G33

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialPoissonsRatio = property(_get_SpecialPoissonsRatio, None)
	'''
	Special poisson's ratio

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialPoissonsRatioXZ = property(_get_SpecialPoissonsRatioXZ, None)
	'''
	Special poisson's ratio of xz direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialShearModulusXZ = property(_get_SpecialShearModulusXZ, None)
	'''
	Special shear modulus of xz direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialTotalMass = property(_get_SpecialTotalMass, None)
	'''
	Special total mass

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialTransverseShearModulus1 = property(_get_SpecialTransverseShearModulus1, None)
	'''
	Special shear modulus of XY direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialTransverseShearModulus2 = property(_get_SpecialTransverseShearModulus2, None)
	'''
	Special shear modulus of YZ direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialYoungsModulus = property(_get_SpecialYoungsModulus, None)
	'''
	Special young's modulus

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialYoungsModulusX = property(_get_SpecialYoungsModulusX, None)
	'''
	Special young's modulus of x direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialYoungsModulusZ = property(_get_SpecialYoungsModulusZ, None)
	'''
	Special young's modulus of z direction

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SplineSurface = property(_get_SplineSurface, None)
	'''
	The surface spline data of the sheet

	:type: recurdyn.MTT3D.IMTT3DSurfaceSpline
	'''
	StartPoint = property(_get_StartPoint, _set_StartPoint)
	'''
	The starting point of the sheet

	:type: list[float]
	'''
	Thickness = property(_get_Thickness, None)
	'''
	The thickness of a sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalMass = property(_get_TotalMass, None)
	'''
	The total mass of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	TransverseShearModulus1 = property(_get_TransverseShearModulus1, None)
	'''
	The shear modulus of XY direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	TransverseShearModulus2 = property(_get_TransverseShearModulus2, None)
	'''
	The shear modulus of YZ direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseAirResistance = property(_get_UseAirResistance, _set_UseAirResistance)
	'''
	Use Air Resistance Coefficient

	:type: bool
	'''
	UseInitialVelocity = property(_get_UseInitialVelocity, _set_UseInitialVelocity)
	'''
	Use initial velocity

	:type: bool
	'''
	UseSpecialDampingRatio = property(_get_UseSpecialDampingRatio, _set_UseSpecialDampingRatio)
	'''
	Use special damping ratio

	:type: bool
	'''
	UseSpecialDensity = property(_get_UseSpecialDensity, _set_UseSpecialDensity)
	'''
	Use special density

	:type: bool
	'''
	UseSpecialG11 = property(_get_UseSpecialG11, _set_UseSpecialG11)
	'''
	Use special G11

	:type: bool
	'''
	UseSpecialG12 = property(_get_UseSpecialG12, _set_UseSpecialG12)
	'''
	Use special G12

	:type: bool
	'''
	UseSpecialG13 = property(_get_UseSpecialG13, _set_UseSpecialG13)
	'''
	Use special G13

	:type: bool
	'''
	UseSpecialG22 = property(_get_UseSpecialG22, _set_UseSpecialG22)
	'''
	Use special G22

	:type: bool
	'''
	UseSpecialG23 = property(_get_UseSpecialG23, _set_UseSpecialG23)
	'''
	Use special G23

	:type: bool
	'''
	UseSpecialG33 = property(_get_UseSpecialG33, _set_UseSpecialG33)
	'''
	Use special G33

	:type: bool
	'''
	UseSpecialPoissonsRatio = property(_get_UseSpecialPoissonsRatio, _set_UseSpecialPoissonsRatio)
	'''
	Use special poisson's ratio

	:type: bool
	'''
	UseSpecialPoissonsRatioXZ = property(_get_UseSpecialPoissonsRatioXZ, _set_UseSpecialPoissonsRatioXZ)
	'''
	Use special poisson's ratio of xz direction

	:type: bool
	'''
	UseSpecialShearModulusXZ = property(_get_UseSpecialShearModulusXZ, _set_UseSpecialShearModulusXZ)
	'''
	Use special shear modulus of xz direction

	:type: bool
	'''
	UseSpecialTotalMass = property(_get_UseSpecialTotalMass, _set_UseSpecialTotalMass)
	'''
	Use special total mass

	:type: bool
	'''
	UseSpecialTransverseShearModulus1 = property(_get_UseSpecialTransverseShearModulus1, _set_UseSpecialTransverseShearModulus1)
	'''
	Use special shear modulus of XY direction

	:type: bool
	'''
	UseSpecialTransverseShearModulus2 = property(_get_UseSpecialTransverseShearModulus2, _set_UseSpecialTransverseShearModulus2)
	'''
	Use special shear modulus of YZ direction

	:type: bool
	'''
	UseSpecialYoungsModulus = property(_get_UseSpecialYoungsModulus, _set_UseSpecialYoungsModulus)
	'''
	Use special young's modulus

	:type: bool
	'''
	UseSpecialYoungsModulusX = property(_get_UseSpecialYoungsModulusX, _set_UseSpecialYoungsModulusX)
	'''
	Use special young's modulus of x direction

	:type: bool
	'''
	UseSpecialYoungsModulusZ = property(_get_UseSpecialYoungsModulusZ, _set_UseSpecialYoungsModulusZ)
	'''
	Use special young's modulus of z direction

	:type: bool
	'''
	UseUpdateGeometryAutomatically = property(_get_UseUpdateGeometryAutomatically, _set_UseUpdateGeometryAutomatically)
	'''
	Use Update Geometry Information Automatically

	:type: bool
	'''
	UseUserDefinedTransverseShearModulus = property(_get_UseUserDefinedTransverseShearModulus, _set_UseUserDefinedTransverseShearModulus)
	'''
	Use user-defined transverse shear modulus

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	The young's modulus of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	YoungsModulusX = property(_get_YoungsModulusX, None)
	'''
	The young's modulus of x direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	YoungsModulusZ = property(_get_YoungsModulusZ, None)
	'''
	The young's modulus of z direction of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseExtractWithoutPreStress = property(None, _set_UseExtractWithoutPreStress)
	'''
	ExtractWithoutPreStress flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_AirResistanceExpression": _set_AirResistanceExpression,
		"_set_AirResistanceType": _set_AirResistanceType,
		"_set_AllDampingRatio": _set_AllDampingRatio,
		"_set_AllDensity": _set_AllDensity,
		"_set_AllG11": _set_AllG11,
		"_set_AllG12": _set_AllG12,
		"_set_AllG13": _set_AllG13,
		"_set_AllG22": _set_AllG22,
		"_set_AllG23": _set_AllG23,
		"_set_AllG33": _set_AllG33,
		"_set_AllPoissonsRatio": _set_AllPoissonsRatio,
		"_set_AllPoissonsRatioXZ": _set_AllPoissonsRatioXZ,
		"_set_AllShearModulusXZ": _set_AllShearModulusXZ,
		"_set_AllTotalMass": _set_AllTotalMass,
		"_set_AllTransverseShearModulus1": _set_AllTransverseShearModulus1,
		"_set_AllTransverseShearModulus2": _set_AllTransverseShearModulus2,
		"_set_AllYoungsModulus": _set_AllYoungsModulus,
		"_set_AllYoungsModulusX": _set_AllYoungsModulusX,
		"_set_AllYoungsModulusZ": _set_AllYoungsModulusZ,
		"_set_BCOrienation": _set_BCOrienation,
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_DirectionLateral": _set_DirectionLateral,
		"_set_DirectionLongitudinal": _set_DirectionLongitudinal,
		"_set_FoldingDirection": _set_FoldingDirection,
		"_set_InnerCPLateral": _set_InnerCPLateral,
		"_set_InnerCPLongitudinal": _set_InnerCPLongitudinal,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MassType": _set_MassType,
		"_set_MaterialDirectivity": _set_MaterialDirectivity,
		"_set_MeshType": _set_MeshType,
		"_set_Name": _set_Name,
		"_set_ShapeType": _set_ShapeType,
		"_set_StartPoint": _set_StartPoint,
		"_set_UseAirResistance": _set_UseAirResistance,
		"_set_UseExtractWithoutPreStress": _set_UseExtractWithoutPreStress,
		"_set_UseInitialVelocity": _set_UseInitialVelocity,
		"_set_UseSpecialDampingRatio": _set_UseSpecialDampingRatio,
		"_set_UseSpecialDensity": _set_UseSpecialDensity,
		"_set_UseSpecialG11": _set_UseSpecialG11,
		"_set_UseSpecialG12": _set_UseSpecialG12,
		"_set_UseSpecialG13": _set_UseSpecialG13,
		"_set_UseSpecialG22": _set_UseSpecialG22,
		"_set_UseSpecialG23": _set_UseSpecialG23,
		"_set_UseSpecialG33": _set_UseSpecialG33,
		"_set_UseSpecialPoissonsRatio": _set_UseSpecialPoissonsRatio,
		"_set_UseSpecialPoissonsRatioXZ": _set_UseSpecialPoissonsRatioXZ,
		"_set_UseSpecialShearModulusXZ": _set_UseSpecialShearModulusXZ,
		"_set_UseSpecialTotalMass": _set_UseSpecialTotalMass,
		"_set_UseSpecialTransverseShearModulus1": _set_UseSpecialTransverseShearModulus1,
		"_set_UseSpecialTransverseShearModulus2": _set_UseSpecialTransverseShearModulus2,
		"_set_UseSpecialYoungsModulus": _set_UseSpecialYoungsModulus,
		"_set_UseSpecialYoungsModulusX": _set_UseSpecialYoungsModulusX,
		"_set_UseSpecialYoungsModulusZ": _set_UseSpecialYoungsModulusZ,
		"_set_UseUpdateGeometryAutomatically": _set_UseUpdateGeometryAutomatically,
		"_set_UseUserDefinedTransverseShearModulus": _set_UseUserDefinedTransverseShearModulus,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"AirResistanceConstant": (5111, 2, (9, 0), (), "AirResistanceConstant", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"AirResistanceExpression": (5112, 2, (9, 0), (), "AirResistanceExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"AirResistanceType": (5110, 2, (3, 0), (), "AirResistanceType", '{E8F89F7E-4D38-476A-AB4B-E48FC39276C4}'),
		"AllDampingRatio": (5021, 2, (11, 0), (), "AllDampingRatio", None),
		"AllDensity": (5009, 2, (11, 0), (), "AllDensity", None),
		"AllG11": (5069, 2, (11, 0), (), "AllG11", None),
		"AllG12": (5073, 2, (11, 0), (), "AllG12", None),
		"AllG13": (5077, 2, (11, 0), (), "AllG13", None),
		"AllG22": (5081, 2, (11, 0), (), "AllG22", None),
		"AllG23": (5085, 2, (11, 0), (), "AllG23", None),
		"AllG33": (5089, 2, (11, 0), (), "AllG33", None),
		"AllPoissonsRatio": (5025, 2, (11, 0), (), "AllPoissonsRatio", None),
		"AllPoissonsRatioXZ": (5037, 2, (11, 0), (), "AllPoissonsRatioXZ", None),
		"AllShearModulusXZ": (5041, 2, (11, 0), (), "AllShearModulusXZ", None),
		"AllTotalMass": (5013, 2, (11, 0), (), "AllTotalMass", None),
		"AllTransverseShearModulus1": (5061, 2, (11, 0), (), "AllTransverseShearModulus1", None),
		"AllTransverseShearModulus2": (5065, 2, (11, 0), (), "AllTransverseShearModulus2", None),
		"AllYoungsModulus": (5017, 2, (11, 0), (), "AllYoungsModulus", None),
		"AllYoungsModulusX": (5029, 2, (11, 0), (), "AllYoungsModulusX", None),
		"AllYoungsModulusZ": (5033, 2, (11, 0), (), "AllYoungsModulusZ", None),
		"BCOrienation": (5160, 2, (3, 0), (), "BCOrienation", '{4FBFC632-BAF4-489E-89CE-DD64AA55D620}'),
		"Color": (5056, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"CorrectionFactor": (5045, 2, (9, 0), (), "CorrectionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CurlRadiusLateral": (5053, 2, (9, 0), (), "CurlRadiusLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CurlRadiusLongitudinal": (5052, 2, (9, 0), (), "CurlRadiusLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingRatio": (5023, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (5011, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DirectionLateral": (5047, 2, (8197, 0), (), "DirectionLateral", None),
		"DirectionLongitudinal": (5046, 2, (8197, 0), (), "DirectionLongitudinal", None),
		"DrillingStiffnessFactor": (5101, 2, (9, 0), (), "DrillingStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ElementLengthLateral": (5106, 2, (9, 0), (), "ElementLengthLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ElementLengthLongitudinal": (5105, 2, (9, 0), (), "ElementLengthLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ElementNumberLateral": (5108, 2, (19, 0), (), "ElementNumberLateral", None),
		"ElementNumberLongitudinal": (5107, 2, (19, 0), (), "ElementNumberLongitudinal", None),
		"FlexBody": (5161, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'),
		"FoldingDirection": (5002, 2, (3, 0), (), "FoldingDirection", '{D3EFD1DD-14F8-4256-91A0-C1C3CF317F38}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"G11": (5071, 2, (9, 0), (), "G11", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G12": (5075, 2, (9, 0), (), "G12", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G13": (5079, 2, (9, 0), (), "G13", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G22": (5083, 2, (9, 0), (), "G22", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G23": (5087, 2, (9, 0), (), "G23", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G33": (5091, 2, (9, 0), (), "G33", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InitialVelocity": (5006, 2, (9, 0), (), "InitialVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InnerCPLateral": (5055, 2, (19, 0), (), "InnerCPLateral", None),
		"InnerCPLongitudinal": (5054, 2, (19, 0), (), "InnerCPLongitudinal", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"LengthLateral": (5049, 2, (9, 0), (), "LengthLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LengthLongitudinal": (5048, 2, (9, 0), (), "LengthLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MassType": (5008, 2, (3, 0), (), "MassType", '{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}'),
		"MaterialDirectivity": (5007, 2, (3, 0), (), "MaterialDirectivity", '{40184A33-144F-4805-BD66-92A3769EAF8C}'),
		"MeshType": (5104, 2, (3, 0), (), "MeshType", '{8407A29C-89E9-48A8-B030-28EFA5125C51}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeNumberLateral": (5051, 2, (19, 0), (), "NodeNumberLateral", None),
		"NodeNumberLongitudinal": (5050, 2, (19, 0), (), "NodeNumberLongitudinal", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PointList": (5003, 2, (9, 0), (), "PointList", '{6BEF9B6B-4708-445E-A3B5-0D65BA69F749}'),
		"PoissonsRatio": (5027, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PoissonsRatioXZ": (5039, 2, (9, 0), (), "PoissonsRatioXZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShapeType": (5102, 2, (3, 0), (), "ShapeType", '{A875895D-5F56-4ABB-81DF-DB853BFD27A7}'),
		"ShearModulusXZ": (5043, 2, (9, 0), (), "ShearModulusXZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialDampingRatio": (5024, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialDensity": (5012, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG11": (5072, 2, (9, 0), (), "SpecialG11", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG12": (5076, 2, (9, 0), (), "SpecialG12", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG13": (5080, 2, (9, 0), (), "SpecialG13", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG22": (5084, 2, (9, 0), (), "SpecialG22", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG23": (5088, 2, (9, 0), (), "SpecialG23", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialG33": (5092, 2, (9, 0), (), "SpecialG33", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPoissonsRatio": (5028, 2, (9, 0), (), "SpecialPoissonsRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPoissonsRatioXZ": (5040, 2, (9, 0), (), "SpecialPoissonsRatioXZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialShearModulusXZ": (5044, 2, (9, 0), (), "SpecialShearModulusXZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialTotalMass": (5016, 2, (9, 0), (), "SpecialTotalMass", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialTransverseShearModulus1": (5064, 2, (9, 0), (), "SpecialTransverseShearModulus1", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialTransverseShearModulus2": (5068, 2, (9, 0), (), "SpecialTransverseShearModulus2", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialYoungsModulus": (5020, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialYoungsModulusX": (5032, 2, (9, 0), (), "SpecialYoungsModulusX", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialYoungsModulusZ": (5036, 2, (9, 0), (), "SpecialYoungsModulusZ", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SplineSurface": (5103, 2, (9, 0), (), "SplineSurface", '{DB76B99A-A0F1-45CD-A2B1-6BC5EC75CD8F}'),
		"StartPoint": (5001, 2, (8197, 0), (), "StartPoint", None),
		"Thickness": (5004, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalMass": (5015, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TransverseShearModulus1": (5063, 2, (9, 0), (), "TransverseShearModulus1", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TransverseShearModulus2": (5067, 2, (9, 0), (), "TransverseShearModulus2", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseAirResistance": (5109, 2, (11, 0), (), "UseAirResistance", None),
		"UseInitialVelocity": (5005, 2, (11, 0), (), "UseInitialVelocity", None),
		"UseSpecialDampingRatio": (5022, 2, (11, 0), (), "UseSpecialDampingRatio", None),
		"UseSpecialDensity": (5010, 2, (11, 0), (), "UseSpecialDensity", None),
		"UseSpecialG11": (5070, 2, (11, 0), (), "UseSpecialG11", None),
		"UseSpecialG12": (5074, 2, (11, 0), (), "UseSpecialG12", None),
		"UseSpecialG13": (5078, 2, (11, 0), (), "UseSpecialG13", None),
		"UseSpecialG22": (5082, 2, (11, 0), (), "UseSpecialG22", None),
		"UseSpecialG23": (5086, 2, (11, 0), (), "UseSpecialG23", None),
		"UseSpecialG33": (5090, 2, (11, 0), (), "UseSpecialG33", None),
		"UseSpecialPoissonsRatio": (5026, 2, (11, 0), (), "UseSpecialPoissonsRatio", None),
		"UseSpecialPoissonsRatioXZ": (5038, 2, (11, 0), (), "UseSpecialPoissonsRatioXZ", None),
		"UseSpecialShearModulusXZ": (5042, 2, (11, 0), (), "UseSpecialShearModulusXZ", None),
		"UseSpecialTotalMass": (5014, 2, (11, 0), (), "UseSpecialTotalMass", None),
		"UseSpecialTransverseShearModulus1": (5062, 2, (11, 0), (), "UseSpecialTransverseShearModulus1", None),
		"UseSpecialTransverseShearModulus2": (5066, 2, (11, 0), (), "UseSpecialTransverseShearModulus2", None),
		"UseSpecialYoungsModulus": (5018, 2, (11, 0), (), "UseSpecialYoungsModulus", None),
		"UseSpecialYoungsModulusX": (5030, 2, (11, 0), (), "UseSpecialYoungsModulusX", None),
		"UseSpecialYoungsModulusZ": (5034, 2, (11, 0), (), "UseSpecialYoungsModulusZ", None),
		"UseUpdateGeometryAutomatically": (5059, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None),
		"UseUserDefinedTransverseShearModulus": (5060, 2, (11, 0), (), "UseUserDefinedTransverseShearModulus", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"YoungsModulus": (5019, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YoungsModulusX": (5031, 2, (9, 0), (), "YoungsModulusX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YoungsModulusZ": (5035, 2, (9, 0), (), "YoungsModulusZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"AirResistanceExpression": ((5112, LCID, 4, 0),()),
		"AirResistanceType": ((5110, LCID, 4, 0),()),
		"AllDampingRatio": ((5021, LCID, 4, 0),()),
		"AllDensity": ((5009, LCID, 4, 0),()),
		"AllG11": ((5069, LCID, 4, 0),()),
		"AllG12": ((5073, LCID, 4, 0),()),
		"AllG13": ((5077, LCID, 4, 0),()),
		"AllG22": ((5081, LCID, 4, 0),()),
		"AllG23": ((5085, LCID, 4, 0),()),
		"AllG33": ((5089, LCID, 4, 0),()),
		"AllPoissonsRatio": ((5025, LCID, 4, 0),()),
		"AllPoissonsRatioXZ": ((5037, LCID, 4, 0),()),
		"AllShearModulusXZ": ((5041, LCID, 4, 0),()),
		"AllTotalMass": ((5013, LCID, 4, 0),()),
		"AllTransverseShearModulus1": ((5061, LCID, 4, 0),()),
		"AllTransverseShearModulus2": ((5065, LCID, 4, 0),()),
		"AllYoungsModulus": ((5017, LCID, 4, 0),()),
		"AllYoungsModulusX": ((5029, LCID, 4, 0),()),
		"AllYoungsModulusZ": ((5033, LCID, 4, 0),()),
		"BCOrienation": ((5160, LCID, 4, 0),()),
		"Color": ((5056, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DirectionLateral": ((5047, LCID, 4, 0),()),
		"DirectionLongitudinal": ((5046, LCID, 4, 0),()),
		"FoldingDirection": ((5002, LCID, 4, 0),()),
		"InnerCPLateral": ((5055, LCID, 4, 0),()),
		"InnerCPLongitudinal": ((5054, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MassType": ((5008, LCID, 4, 0),()),
		"MaterialDirectivity": ((5007, LCID, 4, 0),()),
		"MeshType": ((5104, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ShapeType": ((5102, LCID, 4, 0),()),
		"StartPoint": ((5001, LCID, 4, 0),()),
		"UseAirResistance": ((5109, LCID, 4, 0),()),
		"UseExtractWithoutPreStress": ((5159, LCID, 4, 0),()),
		"UseInitialVelocity": ((5005, LCID, 4, 0),()),
		"UseSpecialDampingRatio": ((5022, LCID, 4, 0),()),
		"UseSpecialDensity": ((5010, LCID, 4, 0),()),
		"UseSpecialG11": ((5070, LCID, 4, 0),()),
		"UseSpecialG12": ((5074, LCID, 4, 0),()),
		"UseSpecialG13": ((5078, LCID, 4, 0),()),
		"UseSpecialG22": ((5082, LCID, 4, 0),()),
		"UseSpecialG23": ((5086, LCID, 4, 0),()),
		"UseSpecialG33": ((5090, LCID, 4, 0),()),
		"UseSpecialPoissonsRatio": ((5026, LCID, 4, 0),()),
		"UseSpecialPoissonsRatioXZ": ((5038, LCID, 4, 0),()),
		"UseSpecialShearModulusXZ": ((5042, LCID, 4, 0),()),
		"UseSpecialTotalMass": ((5014, LCID, 4, 0),()),
		"UseSpecialTransverseShearModulus1": ((5062, LCID, 4, 0),()),
		"UseSpecialTransverseShearModulus2": ((5066, LCID, 4, 0),()),
		"UseSpecialYoungsModulus": ((5018, LCID, 4, 0),()),
		"UseSpecialYoungsModulusX": ((5030, LCID, 4, 0),()),
		"UseSpecialYoungsModulusZ": ((5034, LCID, 4, 0),()),
		"UseUpdateGeometryAutomatically": ((5059, LCID, 4, 0),()),
		"UseUserDefinedTransverseShearModulus": ((5060, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DSheetShellCollection(DispatchBaseClass):
	'''IMTT3DSheetShellCollection'''
	CLSID = IID('{2CDC1D3A-610A-4EA0-A8C5-FC4006CF2F69}')
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
		:rtype: recurdyn.MTT3D.IMTT3DSheetShell
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{170EFC31-8F09-46F5-8500-F888697C0581}')
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
		:rtype: recurdyn.MTT3D.IMTT3DSheetShell
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{170EFC31-8F09-46F5-8500-F888697C0581}')
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
		return win32com.client.util.Iterator(ob, '{170EFC31-8F09-46F5-8500-F888697C0581}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{170EFC31-8F09-46F5-8500-F888697C0581}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT3DSplineData(DispatchBaseClass):
	'''MTT3D surface spline'''
	CLSID = IID('{B9809206-DE89-4FA0-A409-ED2BEB4CAAEC}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Points(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "Points", '{112C4CA7-E0D7-429E-AC61-4697B7E49348}'))

	Points = property(_get_Points, None)
	'''
	Spline points

	:type: recurdyn.MTT3D.IMTT3DPointCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Points": (5001, 2, (9, 0), (), "Points", '{112C4CA7-E0D7-429E-AC61-4697B7E49348}'),
	}
	_prop_map_put_ = {
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT3DSplineDataCollection(DispatchBaseClass):
	'''IMTT3DSplineDataCollection'''
	CLSID = IID('{50C50C6D-C080-44EB-B5BA-465314CC96B7}')
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
		
		:param var: int
		:rtype: recurdyn.MTT3D.IMTT3DSplineData
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B9809206-DE89-4FA0-A409-ED2BEB4CAAEC}')
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
		
		:param var: int
		:rtype: recurdyn.MTT3D.IMTT3DSplineData
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B9809206-DE89-4FA0-A409-ED2BEB4CAAEC}')
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
		return win32com.client.util.Iterator(ob, '{B9809206-DE89-4FA0-A409-ED2BEB4CAAEC}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{B9809206-DE89-4FA0-A409-ED2BEB4CAAEC}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT3DSubSystem(DispatchBaseClass):
	'''MTT3D subsystem'''
	CLSID = IID('{8F13BEDA-A384-4D5C-97E7-7B5C85F2C470}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AlignSheetInRollers(self, pSheet, pMovableRoller):
		'''
		Aligns a sheet in rollers
		
		:param pSheet: IMTT3DSheetShell
		:param pMovableRoller: IMTT3DGroupMovableRoller
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(5018, LCID, 1, (11, 0), ((9, 1), (9, 1)),pSheet
			, pMovableRoller)


	def CreateContactSheetShellToSphere(self, strName, pBaseSphere, pActionEntity):
		'''
		Creates a sheet shell to sphere contact
		
		:param strName: str
		:param pBaseSphere: IGeometrySphere
		:param pActionEntity: IMTT3DSheetShell
		:rtype: recurdyn.MTT3D.IMTT3DContactSheetShellToSphere
		'''
		ret = self._oleobj_.InvokeTypes(5014, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pBaseSphere, pActionEntity)
		if ret is not None:
			ret = Dispatch(ret, 'CreateContactSheetShellToSphere', '{B191A3BA-81B7-49F6-98B6-82BCA52931E2}')
		return ret

	def CreateContactSheetShellToSphere2(self, strName, pBaseSphere, pActionEntity):
		'''
		Creates a sheet shell to sphere contact
		
		:param strName: str
		:param pBaseSphere: IGeometry
		:param pActionEntity: IMTT3DSheetShell
		:rtype: recurdyn.MTT3D.IMTT3DContactSheetShellToSphere
		'''
		ret = self._oleobj_.InvokeTypes(5025, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pBaseSphere, pActionEntity)
		if ret is not None:
			ret = Dispatch(ret, 'CreateContactSheetShellToSphere2', '{B191A3BA-81B7-49F6-98B6-82BCA52931E2}')
		return ret

	def CreateContactSheetShellToSurface(self, strName, pBaseSurface, pActionEntity):
		'''
		Creates a sheet shell to surface contact
		
		:param strName: str
		:param pBaseSurface: IGeometry
		:param pActionEntity: IMTT3DSheetShell
		:rtype: recurdyn.MTT3D.IMTT3DContactSheetShellToSurface
		'''
		ret = self._oleobj_.InvokeTypes(5013, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pBaseSurface, pActionEntity)
		if ret is not None:
			ret = Dispatch(ret, 'CreateContactSheetShellToSurface', '{4D07ACD7-CCD0-4A1A-BA53-41F090095E0E}')
		return ret

	def CreateContactSheetShellToTorus(self, strName, pBaseTorus, pActionEntity):
		'''
		Creates a sheet shell to torus contact
		
		:param strName: str
		:param pBaseTorus: IGeometryTorus
		:param pActionEntity: IMTT3DSheetShell
		:rtype: recurdyn.MTT3D.IMTT3DContactSheetShellToTorus
		'''
		ret = self._oleobj_.InvokeTypes(5015, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pBaseTorus, pActionEntity)
		if ret is not None:
			ret = Dispatch(ret, 'CreateContactSheetShellToTorus', '{80C8B0D7-D377-4A6C-AB06-7DD13758F1EA}')
		return ret

	def CreateContactSheetShellToTorus2(self, strName, pBaseTorus, pActionEntity):
		'''
		Creates a sheet shell to torus contact
		
		:param strName: str
		:param pBaseTorus: IGeometry
		:param pActionEntity: IMTT3DSheetShell
		:rtype: recurdyn.MTT3D.IMTT3DContactSheetShellToTorus
		'''
		ret = self._oleobj_.InvokeTypes(5026, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pBaseTorus, pActionEntity)
		if ret is not None:
			ret = Dispatch(ret, 'CreateContactSheetShellToTorus2', '{80C8B0D7-D377-4A6C-AB06-7DD13758F1EA}')
		return ret

	def CreateForceNodal(self, strName, pSheet):
		'''
		Creates a nodal force
		
		:param strName: str
		:param pSheet: IMTT3DSheetShell
		:rtype: recurdyn.MTT3D.IMTT3DForceNodal
		'''
		ret = self._oleobj_.InvokeTypes(5016, LCID, 1, (9, 0), ((8, 1), (9, 0)),strName
			, pSheet)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceNodal', '{0F707193-3BDD-4899-8FD9-E9C21739ECD0}')
		return ret

	def CreateGroupFixedRoller(self, strName, pPoint, dRadius):
		'''
		Creates a fixed roller
		
		:param strName: str
		:param pPoint: list[float]
		:param dRadius: float
		:rtype: recurdyn.MTT3D.IMTT3DGroupFixedRoller
		'''
		ret = self._oleobj_.InvokeTypes(5004, LCID, 1, (9, 0), ((8, 1), (8197, 1), (5, 1)),strName
			, pPoint, dRadius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupFixedRoller', '{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')
		return ret

	def CreateGroupMovableRoller(self, strName, pIFixedRoller, pDepthDirection, dRadius, dDistance):
		'''
		Creates a movable roller
		
		:param strName: str
		:param pIFixedRoller: IMTT3DGroupFixedRoller
		:param pDepthDirection: list[float]
		:param dRadius: float
		:param dDistance: float
		:rtype: recurdyn.MTT3D.IMTT3DGroupMovableRoller
		'''
		ret = self._oleobj_.InvokeTypes(5005, LCID, 1, (9, 0), ((8, 1), (9, 1), (8197, 1), (5, 1), (5, 1)),strName
			, pIFixedRoller, pDepthDirection, dRadius, dDistance)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupMovableRoller', '{6E476EA6-E410-4EEB-A32A-5B24141617A3}')
		return ret

	def CreateGroupRollerPair(self, strFixedRollerName, pPoint, dFixedRollerRadius, strMovableRollerName, pDirection, dMovableRollerRadius, dDistance):
		'''
		Creates a roller pair
		
		:param strFixedRollerName: str
		:param pPoint: list[float]
		:param dFixedRollerRadius: float
		:param strMovableRollerName: str
		:param pDirection: list[float]
		:param dMovableRollerRadius: float
		:param dDistance: float
		:rtype: recurdyn.MTT3D.IMTT3DGroupFixedRoller
		'''
		ret = self._oleobj_.InvokeTypes(5006, LCID, 1, (9, 0), ((8, 1), (8197, 1), (5, 1), (8, 1), (8197, 1), (5, 1), (5, 1)),strFixedRollerName
			, pPoint, dFixedRollerRadius, strMovableRollerName, pDirection, dMovableRollerRadius
			, dDistance)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupRollerPair', '{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')
		return ret

	def CreateGuideArc(self, strName, pFirstPoint, pSecondPoint, dAngle):
		'''
		Creates an arc guide
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param dAngle: float
		:rtype: recurdyn.MTT3D.IMTT3DGuideArc
		'''
		ret = self._oleobj_.InvokeTypes(5010, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1)),strName
			, pFirstPoint, pSecondPoint, dAngle)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideArc', '{433E3A1C-9C7A-4426-9A79-26AF18A119D4}')
		return ret

	def CreateGuideCircular(self, strName, pFirstPoint, dRadius):
		'''
		Creates method creates a circular guide
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param dRadius: float
		:rtype: recurdyn.MTT3D.IMTT3DGuideCircular
		'''
		ret = self._oleobj_.InvokeTypes(5012, LCID, 1, (9, 0), ((8, 1), (8197, 1), (5, 1)),strName
			, pFirstPoint, dRadius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideCircular', '{10FA5037-8BC0-4293-AB5C-E81BD03C634E}')
		return ret

	def CreateGuideCircularWithGuide(self, strName, pGuide, bStartPoint, bupDirection, dRadius):
		'''
		Creates method creates a circular guide with guide
		
		:param strName: str
		:param pGuide: IMTT3DGuide
		:param bStartPoint: bool
		:param bupDirection: bool
		:param dRadius: float
		:rtype: recurdyn.MTT3D.IMTT3DGuideCircular
		'''
		ret = self._oleobj_.InvokeTypes(5057, LCID, 1, (9, 0), ((8, 1), (9, 1), (11, 1), (11, 1), (5, 1)),strName
			, pGuide, bStartPoint, bupDirection, dRadius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideCircularWithGuide', '{10FA5037-8BC0-4293-AB5C-E81BD03C634E}')
		return ret

	def CreateGuideLinear(self, strName, pFirstPoint, pSecondPoint):
		'''
		Creates a linear guide
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:rtype: recurdyn.MTT3D.IMTT3DGuideLinear
		'''
		ret = self._oleobj_.InvokeTypes(5011, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1)),strName
			, pFirstPoint, pSecondPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideLinear', '{80975616-6221-41FA-970F-09B25194E5FB}')
		return ret

	def CreateSensorDistance(self, strName, pPosition, pDirection, dRange):
		'''
		Creates a distance sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pDirection: list[float]
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorDistance
		'''
		ret = self._oleobj_.InvokeTypes(5022, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1)),strName
			, pPosition, pDirection, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorDistance', '{0CC3861B-CC2A-4402-9135-C8BC804EABBD}')
		return ret

	def CreateSensorEvent(self, strName, pPosition, dRange):
		'''
		Creates an event sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorEvent
		'''
		ret = self._oleobj_.InvokeTypes(5023, LCID, 1, (9, 0), ((8, 1), (8197, 1), (5, 1)),strName
			, pPosition, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorEvent', '{FB0F1AE7-3A1E-4326-B1BF-8225DA2BF11E}')
		return ret

	def CreateSensorSpeed(self, strName, pPosition, pDirection, dRange):
		'''
		Creates a speed sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pDirection: list[float]
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorSpeed
		'''
		ret = self._oleobj_.InvokeTypes(5021, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1)),strName
			, pPosition, pDirection, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorSpeed', '{CCB7E742-F0DF-4F22-A377-04AA675FD281}')
		return ret

	def CreateSensorTension(self, name):
		'''
		Creates a tension sensor
		
		:param name: str
		:rtype: recurdyn.ProcessNet.ISensorTension
		'''
		ret = self._oleobj_.InvokeTypes(5024, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorTension', '{55C49622-A503-4651-BF1E-2A84CD9E27AB}')
		return ret

	def CreateSensorTension2(self, strName, pPosition, pEntity, dRange):
		'''
		Create a tension sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorTension
		'''
		ret = self._oleobj_.InvokeTypes(5027, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorTension2', '{55C49622-A503-4651-BF1E-2A84CD9E27AB}')
		return ret

	def CreateSheetShell(self, name, nodeNumberLogitudinal, NodeNumberLateral):
		'''
		Creates a flat sheet shell
		
		:param name: str
		:param nodeNumberLogitudinal: int
		:param NodeNumberLateral: int
		:rtype: recurdyn.MTT3D.IMTT3DSheetShell
		'''
		ret = self._oleobj_.InvokeTypes(5007, LCID, 1, (9, 0), ((8, 1), (19, 1), (19, 1)),name
			, nodeNumberLogitudinal, NodeNumberLateral)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSheetShell', '{170EFC31-8F09-46F5-8500-F888697C0581}')
		return ret

	def CreateSheetShellFolding(self, name, Points, nodeNumberLogitudinal, NodeNumberLateral):
		'''
		Creates a folding sheet shell
		
		:param name: str
		:param Points: list[object]
		:param nodeNumberLogitudinal: int
		:param NodeNumberLateral: int
		:rtype: recurdyn.MTT3D.IMTT3DSheetShell
		'''
		_Points_type = True if Points and isinstance(Points[0], win32com.client.VARIANT) else False
		if not _Points_type:
			Points = [win32com.client.VARIANT(12, _data) for _data in Points]

		ret = self._oleobj_.InvokeTypes(5008, LCID, 1, (9, 0), ((8, 1), (8204, 1), (19, 1), (19, 1)),name
			, Points, nodeNumberLogitudinal, NodeNumberLateral)

		if not _Points_type:
			Points = [_data.value for _data in Points]

		if ret is not None:
			ret = Dispatch(ret, 'CreateSheetShellFolding', '{170EFC31-8F09-46F5-8500-F888697C0581}')
		return ret

	def CreateSheetShellWithSplineSurface(self, name, surface, nodeNumberLogitudinal, NodeNumberLateral):
		'''
		Creates a sheet shell using spline surface
		
		:param name: str
		:param surface: IGeometrySplineSurface
		:param nodeNumberLogitudinal: int
		:param NodeNumberLateral: int
		:rtype: recurdyn.MTT3D.IMTT3DSheetShell
		'''
		ret = self._oleobj_.InvokeTypes(5009, LCID, 1, (9, 0), ((8, 1), (9, 1), (19, 1), (19, 1)),name
			, surface, nodeNumberLogitudinal, NodeNumberLateral)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSheetShellWithSplineSurface', '{170EFC31-8F09-46F5-8500-F888697C0581}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def GuideConvert(self, pMultiBodies):
		'''
		Converts guides
		
		:param pMultiBodies: list[object]
		:rtype: bool
		'''
		_pMultiBodies_type = True if pMultiBodies and isinstance(pMultiBodies[0], win32com.client.VARIANT) else False
		if not _pMultiBodies_type:
			pMultiBodies = [win32com.client.VARIANT(12, _data) for _data in pMultiBodies]

		ret = self._oleobj_.InvokeTypes(5017, LCID, 1, (11, 0), ((8204, 1),),pMultiBodies
			)

		if not _pMultiBodies_type:
			pMultiBodies = [_data.value for _data in pMultiBodies]

		return ret


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

		ret = self._oleobj_.InvokeTypes(5019, LCID, 1, (11, 0), ((8204, 1), (19, 1)),pMultiBodies
			, oleColor)

		if not _pMultiBodies_type:
			pMultiBodies = [_data.value for _data in pMultiBodies]

		return ret


	def _get_Assembly(self):
		return self._ApplyTypes_(*(5002, 2, (9, 0), (), "Assembly", '{5E4ADDAC-BBF0-49B3-B368-C7259CA3D07E}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactCollection(self):
		return self._ApplyTypes_(*(5055, 2, (9, 0), (), "ContactCollection", '{F032BD6E-8DA6-41D9-BE7E-6B6137E6221A}'))
	def _get_Contour(self):
		return self._ApplyTypes_(*(5056, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'))
	def _get_FixedRollerGroupCollection(self):
		return self._ApplyTypes_(*(5050, 2, (9, 0), (), "FixedRollerGroupCollection", '{4DDDBBAF-DC04-42B6-B745-E8C5BB0CB2C2}'))
	def _get_ForceNodalCollection(self):
		return self._ApplyTypes_(*(5054, 2, (9, 0), (), "ForceNodalCollection", '{6B16FDF1-2281-424C-8A58-20633C8C31E6}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_GuideCollection(self):
		return self._ApplyTypes_(*(5053, 2, (9, 0), (), "GuideCollection", '{DAEA406F-55AF-4745-969A-9A3184D19D02}'))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(5003, 2, (9, 0), (), "MotherBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_MovableRollerGroupCollection(self):
		return self._ApplyTypes_(*(5051, 2, (9, 0), (), "MovableRollerGroupCollection", '{115B4437-C5DB-456D-885E-8F8F51A48C13}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_SheetShellCollection(self):
		return self._ApplyTypes_(*(5052, 2, (9, 0), (), "SheetShellCollection", '{2CDC1D3A-610A-4EA0-A8C5-FC4006CF2F69}'))
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

	Assembly = property(_get_Assembly, None)
	'''
	Assembly

	:type: recurdyn.MTT3D.IMTT3DAssembly
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactCollection = property(_get_ContactCollection, None)
	Contour = property(_get_Contour, None)
	'''
	Get Contour

	:type: recurdyn.Flexible.IContour
	'''
	FixedRollerGroupCollection = property(_get_FixedRollerGroupCollection, None)
	ForceNodalCollection = property(_get_ForceNodalCollection, None)
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
	MotherBody = property(_get_MotherBody, None)
	'''
	Mother body in MTT3D subsystem

	:type: recurdyn.ProcessNet.IBody
	'''
	MovableRollerGroupCollection = property(_get_MovableRollerGroupCollection, None)
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
	SheetShellCollection = property(_get_SheetShellCollection, None)
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
		"Assembly": (5002, 2, (9, 0), (), "Assembly", '{5E4ADDAC-BBF0-49B3-B368-C7259CA3D07E}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactCollection": (5055, 2, (9, 0), (), "ContactCollection", '{F032BD6E-8DA6-41D9-BE7E-6B6137E6221A}'),
		"Contour": (5056, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'),
		"FixedRollerGroupCollection": (5050, 2, (9, 0), (), "FixedRollerGroupCollection", '{4DDDBBAF-DC04-42B6-B745-E8C5BB0CB2C2}'),
		"ForceNodalCollection": (5054, 2, (9, 0), (), "ForceNodalCollection", '{6B16FDF1-2281-424C-8A58-20633C8C31E6}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralSubSystem": (5001, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"GuideCollection": (5053, 2, (9, 0), (), "GuideCollection", '{DAEA406F-55AF-4745-969A-9A3184D19D02}'),
		"MotherBody": (5003, 2, (9, 0), (), "MotherBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"MovableRollerGroupCollection": (5051, 2, (9, 0), (), "MovableRollerGroupCollection", '{115B4437-C5DB-456D-885E-8F8F51A48C13}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SheetShellCollection": (5052, 2, (9, 0), (), "SheetShellCollection", '{2CDC1D3A-610A-4EA0-A8C5-FC4006CF2F69}'),
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

class IMTT3DSurfaceSpline(DispatchBaseClass):
	'''MTT3D surface spline'''
	CLSID = IID('{DB76B99A-A0F1-45CD-A2B1-6BC5EC75CD8F}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Clear(self):
		'''
		Clear spline data
		'''
		return self._oleobj_.InvokeTypes(5005, LCID, 1, (24, 0), (),)


	def Export(self, name):
		'''
		Export spline data to mat file
		
		:param name: str
		'''
		return self._oleobj_.InvokeTypes(5004, LCID, 1, (24, 0), ((8, 1),),name
			)


	def Import(self, name):
		'''
		Import spline data from mat file
		
		:param name: str
		'''
		return self._oleobj_.InvokeTypes(5003, LCID, 1, (24, 0), ((8, 1),),name
			)


	def _get_File(self):
		return self._ApplyTypes_(*(5002, 2, (8, 0), (), "File", None))
	def _get_SurfaceData(self):
		return self._ApplyTypes_(*(5001, 2, (9, 0), (), "SurfaceData", '{50C50C6D-C080-44EB-B5BA-465314CC96B7}'))

	def _set_File(self, value):
		if "File" in self.__dict__: self.__dict__["File"] = value; return
		self._oleobj_.Invoke(*((5002, LCID, 4, 0) + (value,) + ()))

	File = property(_get_File, _set_File)
	'''
	File name

	:type: str
	'''
	SurfaceData = property(_get_SurfaceData, None)
	'''
	Spline data

	:type: recurdyn.MTT3D.IMTT3DSplineDataCollection
	'''

	_prop_map_set_function_ = {
		"_set_File": _set_File,
	}
	_prop_map_get_ = {
		"File": (5002, 2, (8, 0), (), "File", None),
		"SurfaceData": (5001, 2, (9, 0), (), "SurfaceData", '{50C50C6D-C080-44EB-B5BA-465314CC96B7}'),
	}
	_prop_map_put_ = {
		"File": ((5002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRollerInfoCollection(DispatchBaseClass):
	'''IRollerInfoCollection'''
	CLSID = IID('{5E1955E3-FF59-4A71-BA6C-47152E76743B}')
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
		
		:param var: int
		:rtype: recurdyn.MTT3D.IMTT3DRollerInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{08C957DF-3520-4486-B0F5-55EACA670727}')
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
		
		:param var: int
		:rtype: recurdyn.MTT3D.IMTT3DRollerInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((3, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{08C957DF-3520-4486-B0F5-55EACA670727}')
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
		return win32com.client.util.Iterator(ob, '{08C957DF-3520-4486-B0F5-55EACA670727}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{08C957DF-3520-4486-B0F5-55EACA670727}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

IMTT3DAssembly_vtables_dispatch_ = 1
IMTT3DAssembly_vtables_ = [
	(( 'SetContactedGeometry' , 'pVal' , 'vBool' , 'pResult' , ), 5051, (5051, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GetContactedGeometry' , 'pVal' , 'pResult' , ), 5052, (5052, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SetContactedSheet' , 'pVal' , 'vBool' , 'pResult' , ), 5053, (5053, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetContactedSheet' , 'pVal' , 'pResult' , ), 5054, (5054, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseSystemBoundary' , 'pVal' , ), 5055, (5055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseSystemBoundary' , 'pVal' , ), 5055, (5055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ReferencePosition' , 'ppVal' , ), 5056, (5056, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SizeOfBoundary' , 'pVal' , ), 5057, (5057, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SizeOfBoundary' , 'pVal' , ), 5057, (5057, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BufferRadiusFactor' , 'ppVal' , ), 5058, (5058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'MaximumStepsizeFactor' , 'ppVal' , ), 5059, (5059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'PenetrationParameter' , 'ppVal' , ), 5060, (5060, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseResolution' , 'pVal' , ), 5061, (5061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseResolution' , 'pVal' , ), 5061, (5061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Resolution' , 'pVal' , ), 5062, (5062, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Resolution' , 'pVal' , ), 5062, (5062, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumNoOfSheetElements' , 'pVal' , ), 5063, (5063, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumNoOfSheetElements' , 'pVal' , ), 5063, (5063, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'MaximumNoOfSheetElements' , 'pVal' , ), 5064, (5064, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'MaximumNoOfSheetElements' , 'pVal' , ), 5064, (5064, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
]

IMTT3DContact_vtables_dispatch_ = 1
IMTT3DContact_vtables_ = [
	(( 'ForceDisplay' , 'pVal' , ), 5001, (5001, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 5001, (5001, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoints' , 'ppVal' , ), 5002, (5002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPoints' , 'ppVal' , ), 5003, (5003, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 5004, (5004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 5004, (5004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IMTT3DContactCollection_vtables_dispatch_ = 1
IMTT3DContactCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{2F8CA0C3-CE82-480F-A8D2-7B58899FC45C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT3DContactProperty_vtables_dispatch_ = 1
IMTT3DContactProperty_vtables_ = [
	(( 'Stiffness' , 'ppVal' , ), 5001, (5001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 5002, (5002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MaximumDamping' , 'ppVal' , ), 5003, (5003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BoundaryPenetration' , 'ppVal' , ), 5004, (5004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 5005, (5005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 5006, (5006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ThresholdVelocity' , 'ppVal' , ), 5007, (5007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 5008, (5008, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 5008, (5008, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStiffness' , 'ppVal' , ), 5009, (5009, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffnessExponent' , 'pVal' , ), 5010, (5010, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffnessExponent' , 'pVal' , ), 5010, (5010, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStiffnessExponent' , 'ppVal' , ), 5011, (5011, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialMaximumDamping' , 'pVal' , ), 5012, (5012, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialMaximumDamping' , 'pVal' , ), 5012, (5012, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SpecialMaximumDamping' , 'ppVal' , ), 5013, (5013, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialBoundaryPenetration' , 'pVal' , ), 5014, (5014, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialBoundaryPenetration' , 'pVal' , ), 5014, (5014, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SpecialBoundaryPenetration' , 'ppVal' , ), 5015, (5015, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialIndentationExponent' , 'pVal' , ), 5016, (5016, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialIndentationExponent' , 'pVal' , ), 5016, (5016, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'SpecialIndentationExponent' , 'ppVal' , ), 5017, (5017, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialFrictionCoefficient' , 'pVal' , ), 5018, (5018, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialFrictionCoefficient' , 'pVal' , ), 5018, (5018, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SpecialFrictionCoefficient' , 'ppVal' , ), 5019, (5019, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialThresholdVelocity' , 'pVal' , ), 5020, (5020, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialThresholdVelocity' , 'pVal' , ), 5020, (5020, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'SpecialThresholdVelocity' , 'ppVal' , ), 5021, (5021, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameterType' , 'pVal' , ), 5022, (5022, (), [ (16387, 10, None, "IID('{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameterType' , 'pVal' , ), 5022, (5022, (), [ (3, 1, None, "IID('{94E5B1A4-CB3A-4DEE-A504-5C1E708D9C1C}')") , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 5023, (5023, (), [ (16387, 10, None, "IID('{596CA79D-118A-40BD-A43E-9174A181B2D8}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 5023, (5023, (), [ (3, 1, None, "IID('{596CA79D-118A-40BD-A43E-9174A181B2D8}')") , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseRDF' , 'pVal' , ), 5024, (5024, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseRDF' , 'pVal' , ), 5024, (5024, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRDF' , 'pVal' , ), 5025, (5025, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRDF' , 'pVal' , ), 5025, (5025, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'SpecialRDF' , 'ppVal' , ), 5026, (5026, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RDF' , 'ppVal' , ), 5027, (5027, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
]

IMTT3DContactPropertyCircularGuide_vtables_dispatch_ = 1
IMTT3DContactPropertyCircularGuide_vtables_ = [
	(( 'GuideVelocity' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

IMTT3DContactPropertyGuide_vtables_dispatch_ = 1
IMTT3DContactPropertyGuide_vtables_ = [
	(( 'FrictionFactorVertexofSheet' , 'ppVal' , ), 5101, (5101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
]

IMTT3DContactPropertyRollerMovableToFixed_vtables_dispatch_ = 1
IMTT3DContactPropertyRollerMovableToFixed_vtables_ = [
	(( 'OffsetPenetration' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

IMTT3DContactPropertyRollerToSheet_vtables_dispatch_ = 1
IMTT3DContactPropertyRollerToSheet_vtables_ = [
	(( 'OverdriveFactor' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialOverdriveFactor' , 'pVal' , ), 5052, (5052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialOverdriveFactor' , 'pVal' , ), 5052, (5052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'SpecialOverdriveFactor' , 'ppVal' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
]

IMTT3DContactSheetShellToSphere_vtables_dispatch_ = 1
IMTT3DContactSheetShellToSphere_vtables_ = [
	(( 'BaseSphere' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{2122DEE7-EE07-4A20-9B49-5A9AF4599906}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BaseSphere' , 'ppVal' , ), 5051, (5051, (), [ (9, 1, None, "IID('{2122DEE7-EE07-4A20-9B49-5A9AF4599906}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ActionSheet' , 'ppVal' , ), 5052, (5052, (), [ (16393, 10, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ActionSheet' , 'ppVal' , ), 5052, (5052, (), [ (9, 1, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertySheetToSphere' , 'ppVal' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{823B2FED-7C16-4336-A3D1-39241C0B06FB}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IMTT3DContactSheetShellToSurface_vtables_dispatch_ = 1
IMTT3DContactSheetShellToSurface_vtables_ = [
	(( 'BaseSurface' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BaseSurface' , 'ppVal' , ), 5051, (5051, (), [ (9, 1, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SurfaceNormalDirection' , 'pVal' , ), 5052, (5052, (), [ (16387, 10, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SurfaceNormalDirection' , 'pVal' , ), 5052, (5052, (), [ (3, 1, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'BasePatchOption' , 'pVal' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{ED5F7902-56FD-482D-AEF2-D898A1EBFF1B}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckVertex' , 'pVal' , ), 5054, (5054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckVertex' , 'pVal' , ), 5054, (5054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ActionSheet' , 'ppVal' , ), 5055, (5055, (), [ (16393, 10, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ActionSheet' , 'ppVal' , ), 5055, (5055, (), [ (9, 1, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'SheetNormalDirection' , 'pVal' , ), 5056, (5056, (), [ (16387, 10, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'SheetNormalDirection' , 'pVal' , ), 5056, (5056, (), [ (3, 1, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}')") , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UsePatchSetSearchAlgorithm' , 'pVal' , ), 5057, (5057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UsePatchSetSearchAlgorithm' , 'pVal' , ), 5057, (5057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertySheetToSurface' , 'ppVal' , ), 5058, (5058, (), [ (16393, 10, None, "IID('{823B2FED-7C16-4336-A3D1-39241C0B06FB}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

IMTT3DContactSheetShellToTorus_vtables_dispatch_ = 1
IMTT3DContactSheetShellToTorus_vtables_ = [
	(( 'BaseTorus' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{92A1D6C1-1B9F-4A5A-AA3E-164073FAA5FB}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BaseTorus' , 'ppVal' , ), 5051, (5051, (), [ (9, 1, None, "IID('{92A1D6C1-1B9F-4A5A-AA3E-164073FAA5FB}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ActionSheet' , 'ppVal' , ), 5052, (5052, (), [ (16393, 10, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ActionSheet' , 'ppVal' , ), 5052, (5052, (), [ (9, 1, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertySheetToTorus' , 'ppVal' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{823B2FED-7C16-4336-A3D1-39241C0B06FB}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IMTT3DCrownRollerProfile_vtables_dispatch_ = 1
IMTT3DCrownRollerProfile_vtables_ = [
	(( 'ProfileCollection' , 'ppVal' , ), 51, (51, (), [ (16393, 10, None, "IID('{2C0D70A3-D197-4781-940A-1672F3B420B9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'dX' , 'dY' , 'dR' , ), 52, (52, (), [ 
			 (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 53, (53, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strFullPathName' , ), 54, (54, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strFullPathName' , ), 55, (55, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IMTT3DFixedRollerGroupCollection_vtables_dispatch_ = 1
IMTT3DFixedRollerGroupCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT3DForceNodal_vtables_dispatch_ = 1
IMTT3DForceNodal_vtables_ = [
	(( 'UserSubroutine' , 'ppVal' , ), 5051, (5051, (), [ (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SetAppliedBody' , 'uiID' , 'vBool' , 'pResult' , ), 5052, (5052, (), [ 
			 (19, 1, None, None) , (11, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetAppliedBody' , 'uiID' , 'pResult' , ), 5053, (5053, (), [ (19, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SetAppliedBodyAll' , 'flag' , 'result' , ), 5054, (5054, (), [ (11, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 5055, (5055, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 5055, (5055, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseReportNodes' , 'pVal' , ), 5056, (5056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseReportNodes' , 'pVal' , ), 5056, (5056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReportNodeIDs' , 'arrNodeIDs' , ), 5057, (5057, (), [ (8195, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ReportNodeIDs' , 'arrNodeIDs' , ), 5057, (5057, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IMTT3DForceNodalCollection_vtables_dispatch_ = 1
IMTT3DForceNodalCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{0F707193-3BDD-4899-8FD9-E9C21739ECD0}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT3DForceSpring_vtables_dispatch_ = 1
IMTT3DForceSpring_vtables_ = [
	(( 'BaseBody' , 'ppVal' , ), 5001, (5001, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 5001, (5001, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 5002, (5002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 5002, (5002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDamping' , 'pVal' , ), 5003, (5003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDamping' , 'pVal' , ), 5003, (5003, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPreload' , 'pVal' , ), 5004, (5004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPreload' , 'pVal' , ), 5004, (5004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStiffness' , 'ppVal' , ), 5005, (5005, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDamping' , 'ppVal' , ), 5006, (5006, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'SpecialPreload' , 'ppVal' , ), 5007, (5007, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
]

IMTT3DForceSpringNip_vtables_dispatch_ = 1
IMTT3DForceSpringNip_vtables_ = [
	(( 'BasePoint' , 'pVal' , ), 5051, (5051, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'BasePoint' , 'pVal' , ), 5051, (5051, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UseBasePoint' , 'pVal' , ), 5052, (5052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseBasePoint' , 'pVal' , ), 5052, (5052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
]

IMTT3DGroupFixedRoller_vtables_dispatch_ = 1
IMTT3DGroupFixedRoller_vtables_ = [
	(( 'BaseBody' , 'pStr' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'pStr' , ), 5051, (5051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'pVal' , ), 5052, (5052, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'pVal' , ), 5052, (5052, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReferencePoint' , 'ppVal' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DepthDirection' , 'pVal' , ), 5054, (5054, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'DepthDirection' , 'pVal' , ), 5054, (5054, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 5055, (5055, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 5055, (5055, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseCenterPoint' , 'pVal' , ), 5056, (5056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseCenterPoint' , 'pVal' , ), 5056, (5056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'ppVal' , ), 5057, (5057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 5058, (5058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 5059, (5059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'ppVal' , ), 5060, (5060, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'ppVal' , ), 5061, (5061, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'ppVal' , ), 5062, (5062, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 5063, (5063, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 5063, (5063, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'Motion' , 'ppVal' , ), 5064, (5064, (), [ (16393, 10, None, "IID('{47F4E55C-4291-4251-866A-98A74112D266}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 5065, (5065, (), [ (16393, 10, None, "IID('{24331496-FF71-42BC-AE6C-5C675546329B}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 5066, (5066, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 5066, (5066, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'RollerBody' , 'pVal' , ), 5067, (5067, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'RevJoint' , 'pVal' , ), 5068, (5068, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoJointPosition' , 'pVal' , ), 5069, (5069, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoJointPosition' , 'pVal' , ), 5069, (5069, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckEdge' , 'pVal' , ), 5070, (5070, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckEdge' , 'pVal' , ), 5070, (5070, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'RollerType' , 'type' , ), 5071, (5071, (), [ (16387, 10, None, "IID('{4FD105DB-485D-4AC8-80FE-B163BDB06C37}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'RollerType' , 'type' , ), 5071, (5071, (), [ (3, 1, None, "IID('{4FD105DB-485D-4AC8-80FE-B163BDB06C37}')") , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'CrownRollerProfile' , 'pVal' , ), 5072, (5072, (), [ (16393, 10, None, "IID('{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'MultipleRollerInfo' , 'pVal' , ), 5073, (5073, (), [ (16393, 10, None, "IID('{786C632D-A3A2-4FC7-9C31-F6EF4DB35EC7}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint2' , 'ppVal' , ), 5074, (5074, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 5075, (5075, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 5075, (5075, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoints' , 'ppVal' , ), 5076, (5076, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPoints' , 'ppVal' , ), 5077, (5077, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 5078, (5078, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 5078, (5078, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
]

IMTT3DGroupMovableRoller_vtables_dispatch_ = 1
IMTT3DGroupMovableRoller_vtables_ = [
	(( 'BaseBody' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 5051, (5051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'pVal' , ), 5052, (5052, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'pVal' , ), 5052, (5052, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReferencePoint' , 'ppVal' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DepthDirection' , 'pVal' , ), 5054, (5054, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'DepthDirection' , 'pVal' , ), 5054, (5054, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 5055, (5055, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 5055, (5055, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseCenterPoint' , 'pVal' , ), 5056, (5056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseCenterPoint' , 'pVal' , ), 5056, (5056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'ppVal' , ), 5057, (5057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 5058, (5058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 5059, (5059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'ppVal' , ), 5060, (5060, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'ppVal' , ), 5061, (5061, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'ppVal' , ), 5062, (5062, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseNipSpring' , 'pVal' , ), 5063, (5063, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UseNipSpring' , 'pVal' , ), 5063, (5063, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'NipSpring' , 'ppVal' , ), 5064, (5064, (), [ (16393, 10, None, "IID('{E8BD4F07-0B25-44C6-9B8E-0905A9EAE731}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 5065, (5065, (), [ (16393, 10, None, "IID('{24331496-FF71-42BC-AE6C-5C675546329B}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToFixedRoller' , 'ppVal' , ), 5066, (5066, (), [ (16393, 10, None, "IID('{8FD0551D-5E3C-428A-9944-CEAC08A575A7}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 5067, (5067, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 5067, (5067, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoJointPosition' , 'pVal' , ), 5068, (5068, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoJointPosition' , 'pVal' , ), 5068, (5068, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoUpdateGeometry' , 'pVal' , ), 5069, (5069, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoUpdateGeometry' , 'pVal' , ), 5069, (5069, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UseHigherNipForce' , 'pVal' , ), 5070, (5070, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseHigherNipForce' , 'pVal' , ), 5070, (5070, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckEdge' , 'pVal' , ), 5071, (5071, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckEdge' , 'pVal' , ), 5071, (5071, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'UseCrownRollerProfile' , 'pVal' , ), 5072, (5072, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'UseCrownRollerProfile' , 'pVal' , ), 5072, (5072, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'CrownRollerProfile' , 'pVal' , ), 5073, (5073, (), [ (16393, 10, None, "IID('{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'RollerBody' , 'pVal' , ), 5074, (5074, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'RARBody' , 'pVal' , ), 5075, (5075, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'RevJoint' , 'pVal' , ), 5076, (5076, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'TraJoint' , 'pVal' , ), 5077, (5077, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'SpringForce' , 'pVal' , ), 5078, (5078, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 5079, (5079, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 5079, (5079, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'Motion' , 'ppVal' , ), 5080, (5080, (), [ (16393, 10, None, "IID('{47F4E55C-4291-4251-866A-98A74112D266}')") , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'UseSoftNip' , 'pVal' , ), 5081, (5081, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'UseSoftNip' , 'pVal' , ), 5081, (5081, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'SoftNip' , 'ppVal' , ), 5082, (5082, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'SoftNip' , 'ppVal' , ), 5082, (5082, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumGap' , 'pVal' , ), 5083, (5083, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumGap' , 'pVal' , ), 5083, (5083, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'MaximumGap' , 'ppVal' , ), 5084, (5084, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'UpdateNonGeometricProperties' , ), 5085, (5085, (), [ ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint2' , 'ppVal' , ), 5086, (5086, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDirectionAngle' , 'ppVal' , ), 5087, (5087, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToSheet' , 'pVal' , ), 5088, (5088, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToSheet' , 'pVal' , ), 5088, (5088, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToRoller' , 'pVal' , ), 5089, (5089, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToRoller' , 'pVal' , ), 5089, (5089, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'ContactPointsToSheet' , 'ppVal' , ), 5090, (5090, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'ContactPointsToRoller' , 'ppVal' , ), 5091, (5091, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPointsToSheet' , 'ppVal' , ), 5092, (5092, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPointsToRoller' , 'ppVal' , ), 5093, (5093, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToSheet' , 'pVal' , ), 5094, (5094, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToSheet' , 'pVal' , ), 5094, (5094, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToRoller' , 'pVal' , ), 5095, (5095, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToRoller' , 'pVal' , ), 5095, (5095, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
]

IMTT3DGuide_vtables_dispatch_ = 1
IMTT3DGuide_vtables_ = [
	(( 'MotherBody' , 'ppVal' , ), 5001, (5001, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MotherBody' , 'ppVal' , ), 5001, (5001, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAllProperties' , ), 5002, (5002, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 5003, (5003, (), [ (16393, 10, None, "IID('{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 5004, (5004, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 5004, (5004, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoints' , 'ppVal' , ), 5005, (5005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPoints' , 'ppVal' , ), 5006, (5006, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 5007, (5007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 5007, (5007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IMTT3DGuideArc_vtables_dispatch_ = 1
IMTT3DGuideArc_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 5052, (5052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ReferencePoint' , 'ppVal' , ), 5054, (5054, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'pVal' , ), 5055, (5055, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'pVal' , ), 5055, (5055, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ExtrudeDirection' , 'pVal' , ), 5056, (5056, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ExtrudeDirection' , 'pVal' , ), 5056, (5056, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ContactDirection' , 'pVal' , ), 5057, (5057, (), [ (16387, 10, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ContactDirection' , 'pVal' , ), 5057, (5057, (), [ (3, 1, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}')") , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 5058, (5058, (), [ (16393, 10, None, "IID('{B805319E-24BB-4157-B46C-C40AD3B0F5C4}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckEdge' , 'pVal' , ), 5059, (5059, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckEdge' , 'pVal' , ), 5059, (5059, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
]

IMTT3DGuideCircular_vtables_dispatch_ = 1
IMTT3DGuideCircular_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 5052, (5052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ReferencePoint' , 'ppVal' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ExtrudeDirection' , 'pVal' , ), 5054, (5054, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ExtrudeDirection' , 'pVal' , ), 5054, (5054, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 5055, (5055, (), [ (16393, 10, None, "IID('{3D9E9719-9BD8-4234-8A98-87D2975BB531}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckEdge' , 'pVal' , ), 5056, (5056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckEdge' , 'pVal' , ), 5056, (5056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IMTT3DGuideCollection_vtables_dispatch_ = 1
IMTT3DGuideCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT3DGuideLinear_vtables_dispatch_ = 1
IMTT3DGuideLinear_vtables_ = [
	(( 'ReferencePoint' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ExtrudeDirection' , 'pVal' , ), 5052, (5052, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ExtrudeDirection' , 'pVal' , ), 5052, (5052, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'LongitudinalDirection' , 'pVal' , ), 5053, (5053, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'LongitudinalDirection' , 'pVal' , ), 5053, (5053, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'ppVal' , ), 5054, (5054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 5055, (5055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ContactDirection' , 'pVal' , ), 5056, (5056, (), [ (16387, 10, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ContactDirection' , 'pVal' , ), 5056, (5056, (), [ (3, 1, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C5}')") , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 5057, (5057, (), [ (16393, 10, None, "IID('{B805319E-24BB-4157-B46C-C40AD3B0F5C4}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckVertex' , 'pVal' , ), 5058, (5058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseCheckVertex' , 'pVal' , ), 5058, (5058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
]

IMTT3DMovableRollerGroupCollection_vtables_dispatch_ = 1
IMTT3DMovableRollerGroupCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{6E476EA6-E410-4EEB-A32A-5B24141617A3}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT3DMultipleRollerInfo_vtables_dispatch_ = 1
IMTT3DMultipleRollerInfo_vtables_ = [
	(( 'RollerInfoCollection' , 'ppVal' , ), 51, (51, (), [ (16393, 10, None, "IID('{5E1955E3-FF59-4A71-BA6C-47152E76743B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'dRadius' , 'dDepth' , 'dDistance' , ), 52, (52, (), [ 
			 (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 53, (53, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strFullPathName' , ), 54, (54, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strFullPathName' , ), 55, (55, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IMTT3DNode_vtables_dispatch_ = 1
IMTT3DNode_vtables_ = [
]

IMTT3DPointCollection_vtables_dispatch_ = 1
IMTT3DPointCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT3DRollerInfo_vtables_dispatch_ = 1
IMTT3DRollerInfo_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 51, (51, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 52, (52, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Distance' , 'ppVal' , ), 53, (53, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IMTT3DSheet_vtables_dispatch_ = 1
IMTT3DSheet_vtables_ = [
	(( 'StartPoint' , 'vector' , ), 5001, (5001, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'StartPoint' , 'vector' , ), 5001, (5001, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'FoldingDirection' , 'type' , ), 5002, (5002, (), [ (3, 1, None, "IID('{D3EFD1DD-14F8-4256-91A0-C1C3CF317F38}')") , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'FoldingDirection' , 'type' , ), 5002, (5002, (), [ (16387, 10, None, "IID('{D3EFD1DD-14F8-4256-91A0-C1C3CF317F38}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PointList' , 'vectors' , ), 5003, (5003, (), [ (16393, 10, None, "IID('{6BEF9B6B-4708-445E-A3B5-0D65BA69F749}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'value' , ), 5004, (5004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'flag' , ), 5005, (5005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'flag' , ), 5005, (5005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'InitialVelocity' , 'value' , ), 5006, (5006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MaterialDirectivity' , 'type' , ), 5007, (5007, (), [ (3, 1, None, "IID('{40184A33-144F-4805-BD66-92A3769EAF8C}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'MaterialDirectivity' , 'type' , ), 5007, (5007, (), [ (16387, 10, None, "IID('{40184A33-144F-4805-BD66-92A3769EAF8C}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'MassType' , 'type' , ), 5008, (5008, (), [ (3, 1, None, "IID('{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'MassType' , 'type' , ), 5008, (5008, (), [ (16387, 10, None, "IID('{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'AllDensity' , 'flag' , ), 5009, (5009, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'AllDensity' , 'flag' , ), 5009, (5009, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDensity' , 'flag' , ), 5010, (5010, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDensity' , 'flag' , ), 5010, (5010, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'value' , ), 5011, (5011, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDensity' , 'spv' , ), 5012, (5012, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'AllTotalMass' , 'flag' , ), 5013, (5013, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'AllTotalMass' , 'flag' , ), 5013, (5013, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialTotalMass' , 'flag' , ), 5014, (5014, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialTotalMass' , 'flag' , ), 5014, (5014, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'TotalMass' , 'value' , ), 5015, (5015, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'SpecialTotalMass' , 'spv' , ), 5016, (5016, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulus' , 'flag' , ), 5017, (5017, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulus' , 'flag' , ), 5017, (5017, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulus' , 'flag' , ), 5018, (5018, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulus' , 'flag' , ), 5018, (5018, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus' , 'value' , ), 5019, (5019, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'SpecialYoungsModulus' , 'spv' , ), 5020, (5020, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'AllDampingRatio' , 'flag' , ), 5021, (5021, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'AllDampingRatio' , 'flag' , ), 5021, (5021, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDampingRatio' , 'flag' , ), 5022, (5022, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDampingRatio' , 'flag' , ), 5022, (5022, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'DampingRatio' , 'value' , ), 5023, (5023, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDampingRatio' , 'spv' , ), 5024, (5024, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'AllPoissonsRatio' , 'flag' , ), 5025, (5025, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'AllPoissonsRatio' , 'flag' , ), 5025, (5025, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPoissonsRatio' , 'flag' , ), 5026, (5026, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPoissonsRatio' , 'flag' , ), 5026, (5026, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'PoissonsRatio' , 'value' , ), 5027, (5027, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'SpecialPoissonsRatio' , 'spv' , ), 5028, (5028, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulusX' , 'flag' , ), 5029, (5029, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulusX' , 'flag' , ), 5029, (5029, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulusX' , 'flag' , ), 5030, (5030, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulusX' , 'flag' , ), 5030, (5030, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulusX' , 'value' , ), 5031, (5031, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'SpecialYoungsModulusX' , 'spv' , ), 5032, (5032, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulusZ' , 'flag' , ), 5033, (5033, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulusZ' , 'flag' , ), 5033, (5033, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulusZ' , 'flag' , ), 5034, (5034, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulusZ' , 'flag' , ), 5034, (5034, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulusZ' , 'value' , ), 5035, (5035, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'SpecialYoungsModulusZ' , 'spv' , ), 5036, (5036, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'AllPoissonsRatioXZ' , 'flag' , ), 5037, (5037, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'AllPoissonsRatioXZ' , 'flag' , ), 5037, (5037, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPoissonsRatioXZ' , 'flag' , ), 5038, (5038, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPoissonsRatioXZ' , 'flag' , ), 5038, (5038, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'PoissonsRatioXZ' , 'value' , ), 5039, (5039, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'SpecialPoissonsRatioXZ' , 'spv' , ), 5040, (5040, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'AllShearModulusXZ' , 'flag' , ), 5041, (5041, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'AllShearModulusXZ' , 'flag' , ), 5041, (5041, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialShearModulusXZ' , 'flag' , ), 5042, (5042, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialShearModulusXZ' , 'flag' , ), 5042, (5042, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulusXZ' , 'value' , ), 5043, (5043, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'SpecialShearModulusXZ' , 'spv' , ), 5044, (5044, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'CorrectionFactor' , 'value' , ), 5045, (5045, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'DirectionLongitudinal' , 'vector' , ), 5046, (5046, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'DirectionLongitudinal' , 'vector' , ), 5046, (5046, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'DirectionLateral' , 'vector' , ), 5047, (5047, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'DirectionLateral' , 'vector' , ), 5047, (5047, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'LengthLongitudinal' , 'value' , ), 5048, (5048, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'LengthLateral' , 'value' , ), 5049, (5049, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'NodeNumberLongitudinal' , 'value' , ), 5050, (5050, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'NodeNumberLateral' , 'value' , ), 5051, (5051, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'CurlRadiusLongitudinal' , 'value' , ), 5052, (5052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'CurlRadiusLateral' , 'value' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'InnerCPLongitudinal' , 'value' , ), 5054, (5054, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'InnerCPLongitudinal' , 'value' , ), 5054, (5054, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'InnerCPLateral' , 'value' , ), 5055, (5055, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'InnerCPLateral' , 'value' , ), 5055, (5055, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 5056, (5056, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 832 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 5056, (5056, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 840 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAllProperties' , ), 5057, (5057, (), [ ], 1 , 1 , 4 , 0 , 848 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAllProperties2' , ), 5058, (5058, (), [ ], 1 , 1 , 4 , 0 , 856 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryAutomatically' , 'flag' , ), 5059, (5059, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 864 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryAutomatically' , 'flag' , ), 5059, (5059, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 872 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedTransverseShearModulus' , 'flag' , ), 5060, (5060, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 880 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedTransverseShearModulus' , 'flag' , ), 5060, (5060, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 888 , (3, 0, None, None) , 0 , )),
	(( 'AllTransverseShearModulus1' , 'flag' , ), 5061, (5061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 896 , (3, 0, None, None) , 0 , )),
	(( 'AllTransverseShearModulus1' , 'flag' , ), 5061, (5061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 904 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialTransverseShearModulus1' , 'flag' , ), 5062, (5062, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 912 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialTransverseShearModulus1' , 'flag' , ), 5062, (5062, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 920 , (3, 0, None, None) , 0 , )),
	(( 'TransverseShearModulus1' , 'value' , ), 5063, (5063, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 928 , (3, 0, None, None) , 0 , )),
	(( 'SpecialTransverseShearModulus1' , 'spv' , ), 5064, (5064, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 936 , (3, 0, None, None) , 0 , )),
	(( 'AllTransverseShearModulus2' , 'flag' , ), 5065, (5065, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 944 , (3, 0, None, None) , 0 , )),
	(( 'AllTransverseShearModulus2' , 'flag' , ), 5065, (5065, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 952 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialTransverseShearModulus2' , 'flag' , ), 5066, (5066, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 960 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialTransverseShearModulus2' , 'flag' , ), 5066, (5066, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 968 , (3, 0, None, None) , 0 , )),
	(( 'TransverseShearModulus2' , 'value' , ), 5067, (5067, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 976 , (3, 0, None, None) , 0 , )),
	(( 'SpecialTransverseShearModulus2' , 'spv' , ), 5068, (5068, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 984 , (3, 0, None, None) , 0 , )),
	(( 'AllG11' , 'flag' , ), 5069, (5069, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 992 , (3, 0, None, None) , 0 , )),
	(( 'AllG11' , 'flag' , ), 5069, (5069, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1000 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG11' , 'flag' , ), 5070, (5070, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1008 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG11' , 'flag' , ), 5070, (5070, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1016 , (3, 0, None, None) , 0 , )),
	(( 'G11' , 'value' , ), 5071, (5071, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1024 , (3, 0, None, None) , 0 , )),
	(( 'SpecialG11' , 'spv' , ), 5072, (5072, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 1032 , (3, 0, None, None) , 0 , )),
	(( 'AllG12' , 'flag' , ), 5073, (5073, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1040 , (3, 0, None, None) , 0 , )),
	(( 'AllG12' , 'flag' , ), 5073, (5073, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1048 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG12' , 'flag' , ), 5074, (5074, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1056 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG12' , 'flag' , ), 5074, (5074, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1064 , (3, 0, None, None) , 0 , )),
	(( 'G12' , 'value' , ), 5075, (5075, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1072 , (3, 0, None, None) , 0 , )),
	(( 'SpecialG12' , 'spv' , ), 5076, (5076, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 1080 , (3, 0, None, None) , 0 , )),
	(( 'AllG13' , 'flag' , ), 5077, (5077, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1088 , (3, 0, None, None) , 0 , )),
	(( 'AllG13' , 'flag' , ), 5077, (5077, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1096 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG13' , 'flag' , ), 5078, (5078, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1104 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG13' , 'flag' , ), 5078, (5078, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1112 , (3, 0, None, None) , 0 , )),
	(( 'G13' , 'value' , ), 5079, (5079, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1120 , (3, 0, None, None) , 0 , )),
	(( 'SpecialG13' , 'spv' , ), 5080, (5080, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 1128 , (3, 0, None, None) , 0 , )),
	(( 'AllG22' , 'flag' , ), 5081, (5081, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1136 , (3, 0, None, None) , 0 , )),
	(( 'AllG22' , 'flag' , ), 5081, (5081, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1144 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG22' , 'flag' , ), 5082, (5082, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1152 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG22' , 'flag' , ), 5082, (5082, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1160 , (3, 0, None, None) , 0 , )),
	(( 'G22' , 'value' , ), 5083, (5083, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1168 , (3, 0, None, None) , 0 , )),
	(( 'SpecialG22' , 'spv' , ), 5084, (5084, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 1176 , (3, 0, None, None) , 0 , )),
	(( 'AllG23' , 'flag' , ), 5085, (5085, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1184 , (3, 0, None, None) , 0 , )),
	(( 'AllG23' , 'flag' , ), 5085, (5085, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1192 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG23' , 'flag' , ), 5086, (5086, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1200 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG23' , 'flag' , ), 5086, (5086, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1208 , (3, 0, None, None) , 0 , )),
	(( 'G23' , 'value' , ), 5087, (5087, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1216 , (3, 0, None, None) , 0 , )),
	(( 'SpecialG23' , 'spv' , ), 5088, (5088, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 1224 , (3, 0, None, None) , 0 , )),
	(( 'AllG33' , 'flag' , ), 5089, (5089, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1232 , (3, 0, None, None) , 0 , )),
	(( 'AllG33' , 'flag' , ), 5089, (5089, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1240 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG33' , 'flag' , ), 5090, (5090, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1248 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialG33' , 'flag' , ), 5090, (5090, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1256 , (3, 0, None, None) , 0 , )),
	(( 'G33' , 'value' , ), 5091, (5091, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1264 , (3, 0, None, None) , 0 , )),
	(( 'SpecialG33' , 'spv' , ), 5092, (5092, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 1272 , (3, 0, None, None) , 0 , )),
]

IMTT3DSheetShell_vtables_dispatch_ = 1
IMTT3DSheetShell_vtables_ = [
	(( 'DrillingStiffnessFactor' , 'value' , ), 5101, (5101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1280 , (3, 0, None, None) , 0 , )),
	(( 'ShapeType' , 'type' , ), 5102, (5102, (), [ (3, 1, None, "IID('{A875895D-5F56-4ABB-81DF-DB853BFD27A7}')") , ], 1 , 4 , 4 , 0 , 1288 , (3, 0, None, None) , 0 , )),
	(( 'ShapeType' , 'type' , ), 5102, (5102, (), [ (16387, 10, None, "IID('{A875895D-5F56-4ABB-81DF-DB853BFD27A7}')") , ], 1 , 2 , 4 , 0 , 1296 , (3, 0, None, None) , 0 , )),
	(( 'SplineSurface' , 'data' , ), 5103, (5103, (), [ (16393, 10, None, "IID('{DB76B99A-A0F1-45CD-A2B1-6BC5EC75CD8F}')") , ], 1 , 2 , 4 , 0 , 1304 , (3, 0, None, None) , 0 , )),
	(( 'MeshType' , 'type' , ), 5104, (5104, (), [ (3, 1, None, "IID('{8407A29C-89E9-48A8-B030-28EFA5125C51}')") , ], 1 , 4 , 4 , 0 , 1312 , (3, 0, None, None) , 0 , )),
	(( 'MeshType' , 'type' , ), 5104, (5104, (), [ (16387, 10, None, "IID('{8407A29C-89E9-48A8-B030-28EFA5125C51}')") , ], 1 , 2 , 4 , 0 , 1320 , (3, 0, None, None) , 0 , )),
	(( 'ElementLengthLongitudinal' , 'value' , ), 5105, (5105, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1328 , (3, 0, None, None) , 0 , )),
	(( 'ElementLengthLateral' , 'value' , ), 5106, (5106, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1336 , (3, 0, None, None) , 0 , )),
	(( 'ElementNumberLongitudinal' , 'value' , ), 5107, (5107, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 1344 , (3, 0, None, None) , 0 , )),
	(( 'ElementNumberLateral' , 'value' , ), 5108, (5108, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 1352 , (3, 0, None, None) , 0 , )),
	(( 'UseAirResistance' , 'flag' , ), 5109, (5109, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1360 , (3, 0, None, None) , 0 , )),
	(( 'UseAirResistance' , 'flag' , ), 5109, (5109, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 1368 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceType' , 'type' , ), 5110, (5110, (), [ (3, 1, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C4}')") , ], 1 , 4 , 4 , 0 , 1376 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceType' , 'type' , ), 5110, (5110, (), [ (16387, 10, None, "IID('{E8F89F7E-4D38-476A-AB4B-E48FC39276C4}')") , ], 1 , 2 , 4 , 0 , 1384 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceConstant' , 'ppVal' , ), 5111, (5111, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 1392 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceExpression' , 'expression' , ), 5112, (5112, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 1400 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceExpression' , 'expression' , ), 5112, (5112, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 1408 , (3, 0, None, None) , 0 , )),
	(( 'GetNodeByID' , 'nID' , 'ppVal' , ), 5158, (5158, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{460C1F0E-80C4-4F4A-9E5B-DA282823C49E}')") , ], 1 , 1 , 4 , 0 , 1416 , (3, 0, None, None) , 0 , )),
	(( 'UseExtractWithoutPreStress' , ), 5159, (5159, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 1424 , (3, 0, None, None) , 0 , )),
	(( 'BCOrienation' , 'pVal' , ), 5160, (5160, (), [ (3, 1, None, "IID('{4FBFC632-BAF4-489E-89CE-DD64AA55D620}')") , ], 1 , 4 , 4 , 0 , 1432 , (3, 0, None, None) , 0 , )),
	(( 'BCOrienation' , 'pVal' , ), 5160, (5160, (), [ (16387, 10, None, "IID('{4FBFC632-BAF4-489E-89CE-DD64AA55D620}')") , ], 1 , 2 , 4 , 0 , 1440 , (3, 0, None, None) , 0 , )),
	(( 'FlexBody' , 'ppVal' , ), 5161, (5161, (), [ (16393, 10, None, "IID('{9257FD72-F3D0-4E57-A114-2045356D78CD}')") , ], 1 , 2 , 4 , 0 , 1448 , (3, 0, None, None) , 0 , )),
]

IMTT3DSheetShellCollection_vtables_dispatch_ = 1
IMTT3DSheetShellCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT3DSplineData_vtables_dispatch_ = 1
IMTT3DSplineData_vtables_ = [
	(( 'Points' , 'data' , ), 5001, (5001, (), [ (16393, 10, None, "IID('{112C4CA7-E0D7-429E-AC61-4697B7E49348}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IMTT3DSplineDataCollection_vtables_dispatch_ = 1
IMTT3DSplineDataCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{B9809206-DE89-4FA0-A409-ED2BEB4CAAEC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT3DSubSystem_vtables_dispatch_ = 1
IMTT3DSubSystem_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 5001, (5001, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Assembly' , 'ppAssembly' , ), 5002, (5002, (), [ (16393, 10, None, "IID('{5E4ADDAC-BBF0-49B3-B368-C7259CA3D07E}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'MotherBody' , 'ppVal' , ), 5003, (5003, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupFixedRoller' , 'strName' , 'pPoint' , 'dRadius' , 'ppResult' , 
			 ), 5004, (5004, (), [ (8, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupMovableRoller' , 'strName' , 'pIFixedRoller' , 'pDepthDirection' , 'dRadius' , 
			 'dDistance' , 'ppResult' , ), 5005, (5005, (), [ (8, 1, None, None) , (9, 1, None, "IID('{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')") , 
			 (8197, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{6E476EA6-E410-4EEB-A32A-5B24141617A3}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupRollerPair' , 'strFixedRollerName' , 'pPoint' , 'dFixedRollerRadius' , 'strMovableRollerName' , 
			 'pDirection' , 'dMovableRollerRadius' , 'dDistance' , 'ppResult' , ), 5006, (5006, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , 
			 (5, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateSheetShell' , 'name' , 'nodeNumberLogitudinal' , 'NodeNumberLateral' , 'sheet' , 
			 ), 5007, (5007, (), [ (8, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateSheetShellFolding' , 'name' , 'Points' , 'nodeNumberLogitudinal' , 'NodeNumberLateral' , 
			 'sheet' , ), 5008, (5008, (), [ (8, 1, None, None) , (8204, 1, None, None) , (19, 1, None, None) , 
			 (19, 1, None, None) , (16393, 10, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CreateSheetShellWithSplineSurface' , 'name' , 'surface' , 'nodeNumberLogitudinal' , 'NodeNumberLateral' , 
			 'sheet' , ), 5009, (5009, (), [ (8, 1, None, None) , (9, 1, None, "IID('{CC8BC813-F31C-4B25-A652-7B110AF60394}')") , (19, 1, None, None) , 
			 (19, 1, None, None) , (16393, 10, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideArc' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'dAngle' , 
			 'ppResult' , ), 5010, (5010, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{433E3A1C-9C7A-4426-9A79-26AF18A119D4}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideLinear' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'ppResult' , 
			 ), 5011, (5011, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{80975616-6221-41FA-970F-09B25194E5FB}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideCircular' , 'strName' , 'pFirstPoint' , 'dRadius' , 'ppResult' , 
			 ), 5012, (5012, (), [ (8, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{10FA5037-8BC0-4293-AB5C-E81BD03C634E}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactSheetShellToSurface' , 'strName' , 'pBaseSurface' , 'pActionEntity' , 'ppResult' , 
			 ), 5013, (5013, (), [ (8, 1, None, None) , (9, 1, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , (9, 1, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , (16393, 10, None, "IID('{4D07ACD7-CCD0-4A1A-BA53-41F090095E0E}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactSheetShellToSphere' , 'strName' , 'pBaseSphere' , 'pActionEntity' , 'ppResult' , 
			 ), 5014, (5014, (), [ (8, 1, None, None) , (9, 1, None, "IID('{2122DEE7-EE07-4A20-9B49-5A9AF4599906}')") , (9, 1, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , (16393, 10, None, "IID('{B191A3BA-81B7-49F6-98B6-82BCA52931E2}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactSheetShellToTorus' , 'strName' , 'pBaseTorus' , 'pActionEntity' , 'ppResult' , 
			 ), 5015, (5015, (), [ (8, 1, None, None) , (9, 1, None, "IID('{92A1D6C1-1B9F-4A5A-AA3E-164073FAA5FB}')") , (9, 1, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , (16393, 10, None, "IID('{80C8B0D7-D377-4A6C-AB06-7DD13758F1EA}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceNodal' , 'strName' , 'pSheet' , 'ppResult' , ), 5016, (5016, (), [ 
			 (8, 1, None, None) , (9, 0, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , (16393, 10, None, "IID('{0F707193-3BDD-4899-8FD9-E9C21739ECD0}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'GuideConvert' , 'pMultiBodies' , 'pResult' , ), 5017, (5017, (), [ (8204, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'AlignSheetInRollers' , 'pSheet' , 'pMovableRoller' , 'pResult' , ), 5018, (5018, (), [ 
			 (9, 1, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , (9, 1, None, "IID('{6E476EA6-E410-4EEB-A32A-5B24141617A3}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GuideConvertWithColor' , 'pMultiBodies' , 'oleColor' , 'pResult' , ), 5019, (5019, (), [ 
			 (8204, 1, None, None) , (19, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorSpeed' , 'strName' , 'pPosition' , 'pDirection' , 'dRange' , 
			 'ppVal' , ), 5021, (5021, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{CCB7E742-F0DF-4F22-A377-04AA675FD281}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorDistance' , 'strName' , 'pPosition' , 'pDirection' , 'dRange' , 
			 'ppVal' , ), 5022, (5022, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{0CC3861B-CC2A-4402-9135-C8BC804EABBD}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorEvent' , 'strName' , 'pPosition' , 'dRange' , 'ppVal' , 
			 ), 5023, (5023, (), [ (8, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{FB0F1AE7-3A1E-4326-B1BF-8225DA2BF11E}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorTension' , 'name' , 'ppVal' , ), 5024, (5024, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{55C49622-A503-4651-BF1E-2A84CD9E27AB}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactSheetShellToSphere2' , 'strName' , 'pBaseSphere' , 'pActionEntity' , 'ppResult' , 
			 ), 5025, (5025, (), [ (8, 1, None, None) , (9, 1, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , (9, 1, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , (16393, 10, None, "IID('{B191A3BA-81B7-49F6-98B6-82BCA52931E2}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactSheetShellToTorus2' , 'strName' , 'pBaseTorus' , 'pActionEntity' , 'ppResult' , 
			 ), 5026, (5026, (), [ (8, 1, None, None) , (9, 1, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , (9, 1, None, "IID('{170EFC31-8F09-46F5-8500-F888697C0581}')") , (16393, 10, None, "IID('{80C8B0D7-D377-4A6C-AB06-7DD13758F1EA}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorTension2' , 'strName' , 'pPosition' , 'pEntity' , 'dRange' , 
			 'ppVal' , ), 5027, (5027, (), [ (8, 1, None, None) , (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{55C49622-A503-4651-BF1E-2A84CD9E27AB}')") , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'FixedRollerGroupCollection' , 'ppVal' , ), 5050, (5050, (), [ (16393, 10, None, "IID('{4DDDBBAF-DC04-42B6-B745-E8C5BB0CB2C2}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'MovableRollerGroupCollection' , 'ppVal' , ), 5051, (5051, (), [ (16393, 10, None, "IID('{115B4437-C5DB-456D-885E-8F8F51A48C13}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'SheetShellCollection' , 'ppVal' , ), 5052, (5052, (), [ (16393, 10, None, "IID('{2CDC1D3A-610A-4EA0-A8C5-FC4006CF2F69}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'GuideCollection' , 'ppVal' , ), 5053, (5053, (), [ (16393, 10, None, "IID('{DAEA406F-55AF-4745-969A-9A3184D19D02}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ForceNodalCollection' , 'ppVal' , ), 5054, (5054, (), [ (16393, 10, None, "IID('{6B16FDF1-2281-424C-8A58-20633C8C31E6}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'ContactCollection' , 'ppVal' , ), 5055, (5055, (), [ (16393, 10, None, "IID('{F032BD6E-8DA6-41D9-BE7E-6B6137E6221A}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Contour' , 'ppVal' , ), 5056, (5056, (), [ (16393, 10, None, "IID('{BDF4F979-28B7-48D2-BF06-9C59B70D467B}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideCircularWithGuide' , 'strName' , 'pGuide' , 'bStartPoint' , 'bupDirection' , 
			 'dRadius' , 'ppResult' , ), 5057, (5057, (), [ (8, 1, None, None) , (9, 1, None, "IID('{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}')") , 
			 (11, 1, None, None) , (11, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{10FA5037-8BC0-4293-AB5C-E81BD03C634E}')") , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
]

IMTT3DSurfaceSpline_vtables_dispatch_ = 1
IMTT3DSurfaceSpline_vtables_ = [
	(( 'SurfaceData' , 'data' , ), 5001, (5001, (), [ (16393, 10, None, "IID('{50C50C6D-C080-44EB-B5BA-465314CC96B7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'File' , 'name' , ), 5002, (5002, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'File' , 'name' , ), 5002, (5002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'name' , ), 5003, (5003, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'name' , ), 5004, (5004, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 5005, (5005, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IRollerInfoCollection_vtables_dispatch_ = 1
IRollerInfoCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{08C957DF-3520-4486-B0F5-55EACA670727}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{460C1F0E-80C4-4F4A-9E5B-DA282823C49E}' : IMTT3DNode,
	'{823B2FED-7C16-4336-A3D1-39241C0B06FB}' : IMTT3DContactProperty,
	'{24331496-FF71-42BC-AE6C-5C675546329B}' : IMTT3DContactPropertyRollerToSheet,
	'{8FD0551D-5E3C-428A-9944-CEAC08A575A7}' : IMTT3DContactPropertyRollerMovableToFixed,
	'{3D9E9719-9BD8-4234-8A98-87D2975BB531}' : IMTT3DContactPropertyCircularGuide,
	'{B805319E-24BB-4157-B46C-C40AD3B0F5C4}' : IMTT3DContactPropertyGuide,
	'{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}' : IMTT3DCrownRollerProfile,
	'{08C957DF-3520-4486-B0F5-55EACA670727}' : IMTT3DRollerInfo,
	'{5E1955E3-FF59-4A71-BA6C-47152E76743B}' : IRollerInfoCollection,
	'{786C632D-A3A2-4FC7-9C31-F6EF4DB35EC7}' : IMTT3DMultipleRollerInfo,
	'{1C0C8EF0-71D3-495B-BA60-3168D6F5F29A}' : IMTT3DForceSpring,
	'{E8BD4F07-0B25-44C6-9B8E-0905A9EAE731}' : IMTT3DForceSpringNip,
	'{13A25611-C71D-4E62-84B3-7030679D96B7}' : IMTT3DSheet,
	'{112C4CA7-E0D7-429E-AC61-4697B7E49348}' : IMTT3DPointCollection,
	'{B9809206-DE89-4FA0-A409-ED2BEB4CAAEC}' : IMTT3DSplineData,
	'{50C50C6D-C080-44EB-B5BA-465314CC96B7}' : IMTT3DSplineDataCollection,
	'{DB76B99A-A0F1-45CD-A2B1-6BC5EC75CD8F}' : IMTT3DSurfaceSpline,
	'{170EFC31-8F09-46F5-8500-F888697C0581}' : IMTT3DSheetShell,
	'{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}' : IMTT3DGroupFixedRoller,
	'{6E476EA6-E410-4EEB-A32A-5B24141617A3}' : IMTT3DGroupMovableRoller,
	'{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}' : IMTT3DGuide,
	'{433E3A1C-9C7A-4426-9A79-26AF18A119D4}' : IMTT3DGuideArc,
	'{80975616-6221-41FA-970F-09B25194E5FB}' : IMTT3DGuideLinear,
	'{10FA5037-8BC0-4293-AB5C-E81BD03C634E}' : IMTT3DGuideCircular,
	'{2F8CA0C3-CE82-480F-A8D2-7B58899FC45C}' : IMTT3DContact,
	'{4D07ACD7-CCD0-4A1A-BA53-41F090095E0E}' : IMTT3DContactSheetShellToSurface,
	'{B191A3BA-81B7-49F6-98B6-82BCA52931E2}' : IMTT3DContactSheetShellToSphere,
	'{80C8B0D7-D377-4A6C-AB06-7DD13758F1EA}' : IMTT3DContactSheetShellToTorus,
	'{0F707193-3BDD-4899-8FD9-E9C21739ECD0}' : IMTT3DForceNodal,
	'{5E4ADDAC-BBF0-49B3-B368-C7259CA3D07E}' : IMTT3DAssembly,
	'{4DDDBBAF-DC04-42B6-B745-E8C5BB0CB2C2}' : IMTT3DFixedRollerGroupCollection,
	'{115B4437-C5DB-456D-885E-8F8F51A48C13}' : IMTT3DMovableRollerGroupCollection,
	'{2CDC1D3A-610A-4EA0-A8C5-FC4006CF2F69}' : IMTT3DSheetShellCollection,
	'{6B16FDF1-2281-424C-8A58-20633C8C31E6}' : IMTT3DForceNodalCollection,
	'{F032BD6E-8DA6-41D9-BE7E-6B6137E6221A}' : IMTT3DContactCollection,
	'{DAEA406F-55AF-4745-969A-9A3184D19D02}' : IMTT3DGuideCollection,
	'{8F13BEDA-A384-4D5C-97E7-7B5C85F2C470}' : IMTT3DSubSystem,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{460C1F0E-80C4-4F4A-9E5B-DA282823C49E}' : 'IMTT3DNode',
	'{823B2FED-7C16-4336-A3D1-39241C0B06FB}' : 'IMTT3DContactProperty',
	'{24331496-FF71-42BC-AE6C-5C675546329B}' : 'IMTT3DContactPropertyRollerToSheet',
	'{8FD0551D-5E3C-428A-9944-CEAC08A575A7}' : 'IMTT3DContactPropertyRollerMovableToFixed',
	'{3D9E9719-9BD8-4234-8A98-87D2975BB531}' : 'IMTT3DContactPropertyCircularGuide',
	'{B805319E-24BB-4157-B46C-C40AD3B0F5C4}' : 'IMTT3DContactPropertyGuide',
	'{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}' : 'IMTT3DCrownRollerProfile',
	'{08C957DF-3520-4486-B0F5-55EACA670727}' : 'IMTT3DRollerInfo',
	'{5E1955E3-FF59-4A71-BA6C-47152E76743B}' : 'IRollerInfoCollection',
	'{786C632D-A3A2-4FC7-9C31-F6EF4DB35EC7}' : 'IMTT3DMultipleRollerInfo',
	'{1C0C8EF0-71D3-495B-BA60-3168D6F5F29A}' : 'IMTT3DForceSpring',
	'{E8BD4F07-0B25-44C6-9B8E-0905A9EAE731}' : 'IMTT3DForceSpringNip',
	'{13A25611-C71D-4E62-84B3-7030679D96B7}' : 'IMTT3DSheet',
	'{112C4CA7-E0D7-429E-AC61-4697B7E49348}' : 'IMTT3DPointCollection',
	'{B9809206-DE89-4FA0-A409-ED2BEB4CAAEC}' : 'IMTT3DSplineData',
	'{50C50C6D-C080-44EB-B5BA-465314CC96B7}' : 'IMTT3DSplineDataCollection',
	'{DB76B99A-A0F1-45CD-A2B1-6BC5EC75CD8F}' : 'IMTT3DSurfaceSpline',
	'{170EFC31-8F09-46F5-8500-F888697C0581}' : 'IMTT3DSheetShell',
	'{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}' : 'IMTT3DGroupFixedRoller',
	'{6E476EA6-E410-4EEB-A32A-5B24141617A3}' : 'IMTT3DGroupMovableRoller',
	'{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}' : 'IMTT3DGuide',
	'{433E3A1C-9C7A-4426-9A79-26AF18A119D4}' : 'IMTT3DGuideArc',
	'{80975616-6221-41FA-970F-09B25194E5FB}' : 'IMTT3DGuideLinear',
	'{10FA5037-8BC0-4293-AB5C-E81BD03C634E}' : 'IMTT3DGuideCircular',
	'{2F8CA0C3-CE82-480F-A8D2-7B58899FC45C}' : 'IMTT3DContact',
	'{4D07ACD7-CCD0-4A1A-BA53-41F090095E0E}' : 'IMTT3DContactSheetShellToSurface',
	'{B191A3BA-81B7-49F6-98B6-82BCA52931E2}' : 'IMTT3DContactSheetShellToSphere',
	'{80C8B0D7-D377-4A6C-AB06-7DD13758F1EA}' : 'IMTT3DContactSheetShellToTorus',
	'{0F707193-3BDD-4899-8FD9-E9C21739ECD0}' : 'IMTT3DForceNodal',
	'{5E4ADDAC-BBF0-49B3-B368-C7259CA3D07E}' : 'IMTT3DAssembly',
	'{4DDDBBAF-DC04-42B6-B745-E8C5BB0CB2C2}' : 'IMTT3DFixedRollerGroupCollection',
	'{115B4437-C5DB-456D-885E-8F8F51A48C13}' : 'IMTT3DMovableRollerGroupCollection',
	'{2CDC1D3A-610A-4EA0-A8C5-FC4006CF2F69}' : 'IMTT3DSheetShellCollection',
	'{6B16FDF1-2281-424C-8A58-20633C8C31E6}' : 'IMTT3DForceNodalCollection',
	'{F032BD6E-8DA6-41D9-BE7E-6B6137E6221A}' : 'IMTT3DContactCollection',
	'{DAEA406F-55AF-4745-969A-9A3184D19D02}' : 'IMTT3DGuideCollection',
	'{8F13BEDA-A384-4D5C-97E7-7B5C85F2C470}' : 'IMTT3DSubSystem',
}


NamesToIIDMap = {
	'IMTT3DNode' : '{460C1F0E-80C4-4F4A-9E5B-DA282823C49E}',
	'IMTT3DContactProperty' : '{823B2FED-7C16-4336-A3D1-39241C0B06FB}',
	'IMTT3DContactPropertyRollerToSheet' : '{24331496-FF71-42BC-AE6C-5C675546329B}',
	'IMTT3DContactPropertyRollerMovableToFixed' : '{8FD0551D-5E3C-428A-9944-CEAC08A575A7}',
	'IMTT3DContactPropertyCircularGuide' : '{3D9E9719-9BD8-4234-8A98-87D2975BB531}',
	'IMTT3DContactPropertyGuide' : '{B805319E-24BB-4157-B46C-C40AD3B0F5C4}',
	'IMTT3DCrownRollerProfile' : '{85668DBE-04E6-4EFC-A996-F4E123CF2AC5}',
	'IMTT3DRollerInfo' : '{08C957DF-3520-4486-B0F5-55EACA670727}',
	'IRollerInfoCollection' : '{5E1955E3-FF59-4A71-BA6C-47152E76743B}',
	'IMTT3DMultipleRollerInfo' : '{786C632D-A3A2-4FC7-9C31-F6EF4DB35EC7}',
	'IMTT3DForceSpring' : '{1C0C8EF0-71D3-495B-BA60-3168D6F5F29A}',
	'IMTT3DForceSpringNip' : '{E8BD4F07-0B25-44C6-9B8E-0905A9EAE731}',
	'IMTT3DSheet' : '{13A25611-C71D-4E62-84B3-7030679D96B7}',
	'IMTT3DPointCollection' : '{112C4CA7-E0D7-429E-AC61-4697B7E49348}',
	'IMTT3DSplineData' : '{B9809206-DE89-4FA0-A409-ED2BEB4CAAEC}',
	'IMTT3DSplineDataCollection' : '{50C50C6D-C080-44EB-B5BA-465314CC96B7}',
	'IMTT3DSurfaceSpline' : '{DB76B99A-A0F1-45CD-A2B1-6BC5EC75CD8F}',
	'IMTT3DSheetShell' : '{170EFC31-8F09-46F5-8500-F888697C0581}',
	'IMTT3DGroupFixedRoller' : '{B4152AA3-6073-4EFE-9FAF-B9EF18C6A334}',
	'IMTT3DGroupMovableRoller' : '{6E476EA6-E410-4EEB-A32A-5B24141617A3}',
	'IMTT3DGuide' : '{D5C4FE27-848B-4ED0-AAB4-7EABC04EE6A0}',
	'IMTT3DGuideArc' : '{433E3A1C-9C7A-4426-9A79-26AF18A119D4}',
	'IMTT3DGuideLinear' : '{80975616-6221-41FA-970F-09B25194E5FB}',
	'IMTT3DGuideCircular' : '{10FA5037-8BC0-4293-AB5C-E81BD03C634E}',
	'IMTT3DContact' : '{2F8CA0C3-CE82-480F-A8D2-7B58899FC45C}',
	'IMTT3DContactSheetShellToSurface' : '{4D07ACD7-CCD0-4A1A-BA53-41F090095E0E}',
	'IMTT3DContactSheetShellToSphere' : '{B191A3BA-81B7-49F6-98B6-82BCA52931E2}',
	'IMTT3DContactSheetShellToTorus' : '{80C8B0D7-D377-4A6C-AB06-7DD13758F1EA}',
	'IMTT3DForceNodal' : '{0F707193-3BDD-4899-8FD9-E9C21739ECD0}',
	'IMTT3DAssembly' : '{5E4ADDAC-BBF0-49B3-B368-C7259CA3D07E}',
	'IMTT3DFixedRollerGroupCollection' : '{4DDDBBAF-DC04-42B6-B745-E8C5BB0CB2C2}',
	'IMTT3DMovableRollerGroupCollection' : '{115B4437-C5DB-456D-885E-8F8F51A48C13}',
	'IMTT3DSheetShellCollection' : '{2CDC1D3A-610A-4EA0-A8C5-FC4006CF2F69}',
	'IMTT3DForceNodalCollection' : '{6B16FDF1-2281-424C-8A58-20633C8C31E6}',
	'IMTT3DContactCollection' : '{F032BD6E-8DA6-41D9-BE7E-6B6137E6221A}',
	'IMTT3DGuideCollection' : '{DAEA406F-55AF-4745-969A-9A3184D19D02}',
	'IMTT3DSubSystem' : '{8F13BEDA-A384-4D5C-97E7-7B5C85F2C470}',
}


