# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMMMS.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5RecurDynCOMMMS Type Library'
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

CLSID = IID('{F36F54FB-9817-4298-9466-35A89927ECB6}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class MMSCrossSectionType(IntEnum):
	'''
	MMSCrossSectionType enumeration.
	'''
	Circle                        =0         
	'''Constant value is 0.'''
	SubOval                       =1         
	'''Constant value is 1.'''
class MMSDirectionHelixType(IntEnum):
	'''
	MMSDirectionHelixType enumeration.
	'''
	LefttHand                     =1         
	'''Constant value is 1.'''
	RightHand                     =0         
	'''Constant value is 0.'''
class MMSProfileType(IntEnum):
	'''
	MMSProfileType enumeration.
	'''
	MMSProfile_Data               =0         
	'''Constant value is 0.'''
	MMSProfile_File               =1         
	'''Constant value is 1.'''
class SpringType(IntEnum):
	'''
	SpringType enumeration.
	'''
	One_Step                      =0         
	'''Constant value is 0.'''
	Two_Step                      =1         
	'''Constant value is 1.'''

from win32com.client import DispatchBaseClass
class IMMSGroup(DispatchBaseClass):
	'''MMS'''
	CLSID = IID('{BA66ACB4-A495-47FE-8F6F-25C7A5ED6D18}')
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
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
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
	def _get_UseAutoUpdateGeometry(self):
		return self._ApplyTypes_(*(11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoUpdateGeometry(self, value):
		if "UseAutoUpdateGeometry" in self.__dict__: self.__dict__["UseAutoUpdateGeometry"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
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
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
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
	UseAutoUpdateGeometry = property(_get_UseAutoUpdateGeometry, _set_UseAutoUpdateGeometry)
	'''
	Use Update Geometry Automatically

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
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseAutoUpdateGeometry": _set_UseAutoUpdateGeometry,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseAutoUpdateGeometry": (11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseAutoUpdateGeometry": ((11001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeA(DispatchBaseClass):
	'''MMS TypeA'''
	CLSID = IID('{7101723B-18D0-4B5A-8298-A0243B1815F4}')
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
	def _get_CoilClash(self):
		return self._ApplyTypes_(*(11061, 2, (9, 0), (), "CoilClash", '{F1E65DC1-6537-4755-95CE-87512C867DB8}'))
	def _get_Color(self):
		return self._ApplyTypes_(*(11059, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_FirstPoint(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "FirstPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_FreeLength(self):
		return self._ApplyTypes_(*(11058, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_HorizontalRadiusOfSection(self):
		return self._ApplyTypes_(*(11054, 2, (9, 0), (), "HorizontalRadiusOfSection", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MeanCoilRadius(self):
		return self._ApplyTypes_(*(11056, 2, (9, 0), (), "MeanCoilRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ReferenceDirection(self):
		return self._ApplyTypes_(*(11053, 2, (8197, 0), (), "ReferenceDirection", None))
	def _get_SecondPoint(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_SolidHeight(self):
		return self._ApplyTypes_(*(11057, 2, (9, 0), (), "SolidHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpringProperty(self):
		return self._ApplyTypes_(*(11060, 2, (9, 0), (), "SpringProperty", '{7A99C466-6C65-4914-A397-BB4FF286C8B9}'))
	def _get_UseAutoUpdateGeometry(self):
		return self._ApplyTypes_(*(11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VerticalRadiusOfSection(self):
		return self._ApplyTypes_(*(11055, 2, (9, 0), (), "VerticalRadiusOfSection", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((11059, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceDirection(self, value):
		if "ReferenceDirection" in self.__dict__: self.__dict__["ReferenceDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseAutoUpdateGeometry(self, value):
		if "UseAutoUpdateGeometry" in self.__dict__: self.__dict__["UseAutoUpdateGeometry"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	CoilClash = property(_get_CoilClash, None)
	'''
	Spring Property

	:type: recurdyn.MMS.IMMSGroupTypeACoilClash
	'''
	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	FirstPoint = property(_get_FirstPoint, None)
	'''
	First point

	:type: recurdyn.ProcessNet.IVector
	'''
	FreeLength = property(_get_FreeLength, None)
	'''
	Free Length

	:type: recurdyn.ProcessNet.IDouble
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	HorizontalRadiusOfSection = property(_get_HorizontalRadiusOfSection, None)
	'''
	Horizontal Radius of Section

	:type: recurdyn.ProcessNet.IDouble
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	MeanCoilRadius = property(_get_MeanCoilRadius, None)
	'''
	Mean Coil Radius

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
	ReferenceDirection = property(_get_ReferenceDirection, _set_ReferenceDirection)
	'''
	Reference direction

	:type: list[float]
	'''
	SecondPoint = property(_get_SecondPoint, None)
	'''
	Second point

	:type: recurdyn.ProcessNet.IVector
	'''
	SolidHeight = property(_get_SolidHeight, None)
	'''
	Solid Height

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpringProperty = property(_get_SpringProperty, None)
	'''
	Spring Property

	:type: recurdyn.MMS.IMMSGroupTypeASpringProperty
	'''
	UseAutoUpdateGeometry = property(_get_UseAutoUpdateGeometry, _set_UseAutoUpdateGeometry)
	'''
	Use Update Geometry Automatically

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VerticalRadiusOfSection = property(_get_VerticalRadiusOfSection, None)
	'''
	Vertical Radius of Section

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_ReferenceDirection": _set_ReferenceDirection,
		"_set_UseAutoUpdateGeometry": _set_UseAutoUpdateGeometry,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"CoilClash": (11061, 2, (9, 0), (), "CoilClash", '{F1E65DC1-6537-4755-95CE-87512C867DB8}'),
		"Color": (11059, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FirstPoint": (11051, 2, (9, 0), (), "FirstPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"FreeLength": (11058, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"HorizontalRadiusOfSection": (11054, 2, (9, 0), (), "HorizontalRadiusOfSection", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MeanCoilRadius": (11056, 2, (9, 0), (), "MeanCoilRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ReferenceDirection": (11053, 2, (8197, 0), (), "ReferenceDirection", None),
		"SecondPoint": (11052, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"SolidHeight": (11057, 2, (9, 0), (), "SolidHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpringProperty": (11060, 2, (9, 0), (), "SpringProperty", '{7A99C466-6C65-4914-A397-BB4FF286C8B9}'),
		"UseAutoUpdateGeometry": (11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VerticalRadiusOfSection": (11055, 2, (9, 0), (), "VerticalRadiusOfSection", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Color": ((11059, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ReferenceDirection": ((11053, LCID, 4, 0),()),
		"UseAutoUpdateGeometry": ((11001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeACoilClash(DispatchBaseClass):
	'''MMS TypeA Coil Clash Property'''
	CLSID = IID('{F1E65DC1-6537-4755-95CE-87512C867DB8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Damping(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "Damping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PenetrationDepth(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "PenetrationDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(11001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	Damping = property(_get_Damping, None)
	'''
	Damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	PenetrationDepth = property(_get_PenetrationDepth, None)
	'''
	Penetration depth

	:type: recurdyn.ProcessNet.IDouble
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

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Damping": (11003, 2, (9, 0), (), "Damping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PenetrationDepth": (11004, 2, (9, 0), (), "PenetrationDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Stiffness": (11001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (11002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IMMSGroupTypeASpringProperty(DispatchBaseClass):
	'''MMS TypeA Additional Spring Information'''
	CLSID = IID('{7A99C466-6C65-4914-A397-BB4FF286C8B9}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Damping(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "Damping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(11001, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_ShearModulus(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseAutoCalcShearModulus(self):
		return self._ApplyTypes_(*(11002, 2, (11, 0), (), "UseAutoCalcShearModulus", None))
	def _get_UseAutoCalcTSDAStiffness(self):
		return self._ApplyTypes_(*(11004, 2, (11, 0), (), "UseAutoCalcTSDAStiffness", None))

	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoCalcShearModulus(self, value):
		if "UseAutoCalcShearModulus" in self.__dict__: self.__dict__["UseAutoCalcShearModulus"] = value; return
		self._oleobj_.Invoke(*((11002, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoCalcTSDAStiffness(self, value):
		if "UseAutoCalcTSDAStiffness" in self.__dict__: self.__dict__["UseAutoCalcTSDAStiffness"] = value; return
		self._oleobj_.Invoke(*((11004, LCID, 4, 0) + (value,) + ()))

	Damping = property(_get_Damping, None)
	'''
	Damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	ShearModulus = property(_get_ShearModulus, None)
	'''
	Shear modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	Stiffness = property(_get_Stiffness, None)
	'''
	Stiffness

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseAutoCalcShearModulus = property(_get_UseAutoCalcShearModulus, _set_UseAutoCalcShearModulus)
	'''
	Use auto calc. for shear modulus

	:type: bool
	'''
	UseAutoCalcTSDAStiffness = property(_get_UseAutoCalcTSDAStiffness, _set_UseAutoCalcTSDAStiffness)
	'''
	Use auto calc. for TSDA stiffness

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Material": _set_Material,
		"_set_UseAutoCalcShearModulus": _set_UseAutoCalcShearModulus,
		"_set_UseAutoCalcTSDAStiffness": _set_UseAutoCalcTSDAStiffness,
	}
	_prop_map_get_ = {
		"Damping": (11005, 2, (9, 0), (), "Damping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (11001, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"ShearModulus": (11003, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Stiffness": (11006, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseAutoCalcShearModulus": (11002, 2, (11, 0), (), "UseAutoCalcShearModulus", None),
		"UseAutoCalcTSDAStiffness": (11004, 2, (11, 0), (), "UseAutoCalcTSDAStiffness", None),
	}
	_prop_map_put_ = {
		"Material": ((11001, LCID, 4, 0),()),
		"UseAutoCalcShearModulus": ((11002, LCID, 4, 0),()),
		"UseAutoCalcTSDAStiffness": ((11004, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeB(DispatchBaseClass):
	'''MMS TypeB'''
	CLSID = IID('{43A3CDF3-CF97-4C22-B8B8-33F63EFBCE05}')
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
	def _get_Color(self):
		return self._ApplyTypes_(*(11057, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_FirstPoint(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "FirstPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_FreeLength(self):
		return self._ApplyTypes_(*(11054, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InactiveCoils(self):
		return self._ApplyTypes_(*(11056, 2, (9, 0), (), "InactiveCoils", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InstalledLength(self):
		return self._ApplyTypes_(*(11055, 2, (9, 0), (), "InstalledLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NormalDirection(self):
		return self._ApplyTypes_(*(11052, 2, (8197, 0), (), "NormalDirection", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ReferenceDirection(self):
		return self._ApplyTypes_(*(11053, 2, (8197, 0), (), "ReferenceDirection", None))
	def _get_SkeletonProfile(self):
		return self._ApplyTypes_(*(11059, 2, (9, 0), (), "SkeletonProfile", '{C0487899-3698-44DE-AD71-05A3C5D8EF8C}'))
	def _get_SpringProperty(self):
		return self._ApplyTypes_(*(11058, 2, (9, 0), (), "SpringProperty", '{3A657711-810D-47EE-BF91-27F7B0A1C579}'))
	def _get_UseAutoUpdateGeometry(self):
		return self._ApplyTypes_(*(11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_WireProfile(self):
		return self._ApplyTypes_(*(11060, 2, (9, 0), (), "WireProfile", '{C8CAFFBB-25E4-40DB-9405-F14E39BD2A83}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((11057, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NormalDirection(self, value):
		if "NormalDirection" in self.__dict__: self.__dict__["NormalDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((11052, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ReferenceDirection(self, value):
		if "ReferenceDirection" in self.__dict__: self.__dict__["ReferenceDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseAutoUpdateGeometry(self, value):
		if "UseAutoUpdateGeometry" in self.__dict__: self.__dict__["UseAutoUpdateGeometry"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	FirstPoint = property(_get_FirstPoint, None)
	'''
	First point

	:type: recurdyn.ProcessNet.IVector
	'''
	FreeLength = property(_get_FreeLength, None)
	'''
	Free Length

	:type: recurdyn.ProcessNet.IDouble
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	InactiveCoils = property(_get_InactiveCoils, None)
	'''
	Inactive Coils

	:type: recurdyn.ProcessNet.IDouble
	'''
	InstalledLength = property(_get_InstalledLength, None)
	'''
	Installed Length

	:type: recurdyn.ProcessNet.IDouble
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
	NormalDirection = property(_get_NormalDirection, _set_NormalDirection)
	'''
	Normal direction

	:type: list[float]
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
	ReferenceDirection = property(_get_ReferenceDirection, _set_ReferenceDirection)
	'''
	Reference direction

	:type: list[float]
	'''
	SkeletonProfile = property(_get_SkeletonProfile, None)
	'''
	Skeleton Profile

	:type: recurdyn.MMS.IMMSGroupTypeBSkeletonProfile
	'''
	SpringProperty = property(_get_SpringProperty, None)
	'''
	Spring Property

	:type: recurdyn.MMS.IMMSGroupTypeBSpringProperty
	'''
	UseAutoUpdateGeometry = property(_get_UseAutoUpdateGeometry, _set_UseAutoUpdateGeometry)
	'''
	Use Update Geometry Automatically

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	WireProfile = property(_get_WireProfile, None)
	'''
	Wire Profile

	:type: recurdyn.MMS.IMMSGroupTypeBWireProfile
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_NormalDirection": _set_NormalDirection,
		"_set_ReferenceDirection": _set_ReferenceDirection,
		"_set_UseAutoUpdateGeometry": _set_UseAutoUpdateGeometry,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Color": (11057, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FirstPoint": (11051, 2, (9, 0), (), "FirstPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"FreeLength": (11054, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InactiveCoils": (11056, 2, (9, 0), (), "InactiveCoils", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InstalledLength": (11055, 2, (9, 0), (), "InstalledLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NormalDirection": (11052, 2, (8197, 0), (), "NormalDirection", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ReferenceDirection": (11053, 2, (8197, 0), (), "ReferenceDirection", None),
		"SkeletonProfile": (11059, 2, (9, 0), (), "SkeletonProfile", '{C0487899-3698-44DE-AD71-05A3C5D8EF8C}'),
		"SpringProperty": (11058, 2, (9, 0), (), "SpringProperty", '{3A657711-810D-47EE-BF91-27F7B0A1C579}'),
		"UseAutoUpdateGeometry": (11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"WireProfile": (11060, 2, (9, 0), (), "WireProfile", '{C8CAFFBB-25E4-40DB-9405-F14E39BD2A83}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Color": ((11057, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NormalDirection": ((11052, LCID, 4, 0),()),
		"ReferenceDirection": ((11053, LCID, 4, 0),()),
		"UseAutoUpdateGeometry": ((11001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeBSkeletonProfile(DispatchBaseClass):
	'''MMS TypeB Skeleton Profile'''
	CLSID = IID('{C0487899-3698-44DE-AD71-05A3C5D8EF8C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def ExportSkeletonProfile(self, strFileName):
		'''
		Export Skeleton Profile
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11007, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def GetSizeSkeletonProfile(self):
		'''
		Get index size of Skeleton Profile
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(11004, LCID, 1, (19, 0), (),)


	def GetSkeletonProfile(self, nIndex):
		'''
		Get Skeleton Profile
		
		:param nIndex: int
		:rtype: list[float]
		'''
		return self._ApplyTypes_(11003, 1, (8197, 0), ((19, 1),), 'GetSkeletonProfile', None,nIndex
			)


	def ImportSkeletonProfile(self, strFileName):
		'''
		Import Skeleton Profile
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11006, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def SetSkeletonProfile(self, nIndex, pSafeArray):
		'''
		Set Skeleton Profile
		
		:param nIndex: int
		:param pSafeArray: list[float]
		'''
		return self._oleobj_.InvokeTypes(11002, LCID, 1, (24, 0), ((19, 1), (8197, 1)),nIndex
			, pSafeArray)


	def _get_SkeletonProfileFileName(self):
		return self._ApplyTypes_(*(11005, 2, (8, 0), (), "SkeletonProfileFileName", None))
	def _get_SkeletonProfileType(self):
		return self._ApplyTypes_(*(11001, 2, (3, 0), (), "SkeletonProfileType", '{1616B733-CBF9-4070-AC39-D70D8084103B}'))

	def _set_SkeletonProfileFileName(self, value):
		if "SkeletonProfileFileName" in self.__dict__: self.__dict__["SkeletonProfileFileName"] = value; return
		self._oleobj_.Invoke(*((11005, LCID, 4, 0) + (value,) + ()))

	SkeletonProfileFileName = property(_get_SkeletonProfileFileName, _set_SkeletonProfileFileName)
	'''
	Skeleton Profile File name

	:type: str
	'''
	SkeletonProfileType = property(_get_SkeletonProfileType, None)
	'''
	Skeleton Profile Type

	:type: recurdyn.MMS.MMSProfileType
	'''

	_prop_map_set_function_ = {
		"_set_SkeletonProfileFileName": _set_SkeletonProfileFileName,
	}
	_prop_map_get_ = {
		"SkeletonProfileFileName": (11005, 2, (8, 0), (), "SkeletonProfileFileName", None),
		"SkeletonProfileType": (11001, 2, (3, 0), (), "SkeletonProfileType", '{1616B733-CBF9-4070-AC39-D70D8084103B}'),
	}
	_prop_map_put_ = {
		"SkeletonProfileFileName": ((11005, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeBSpringProperty(DispatchBaseClass):
	'''MMS TypeB Spring Property'''
	CLSID = IID('{3A657711-810D-47EE-BF91-27F7B0A1C579}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BlockDamping(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "BlockDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FreeDamping(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "FreeDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearModulus(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(11001, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	BlockDamping = property(_get_BlockDamping, None)
	'''
	Block damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingExponent = property(_get_DampingExponent, None)
	'''
	Damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	FreeDamping = property(_get_FreeDamping, None)
	'''
	Free damping

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearModulus = property(_get_ShearModulus, None)
	'''
	Shear modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalMass = property(_get_TotalMass, None)
	'''
	Total mass

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"BlockDamping": (11004, 2, (9, 0), (), "BlockDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (11005, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FreeDamping": (11003, 2, (9, 0), (), "FreeDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearModulus": (11002, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalMass": (11001, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IMMSGroupTypeBWireProfile(DispatchBaseClass):
	'''MMS TypeB Wire Profile'''
	CLSID = IID('{C8CAFFBB-25E4-40DB-9405-F14E39BD2A83}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def ExportWireProfile(self, strFileName):
		'''
		Export Wire Profile
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11007, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def GetSizeWireProfile(self):
		'''
		Get index size of Wire Profile
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(11004, LCID, 1, (19, 0), (),)


	def GetWireProfile(self, nIndex):
		'''
		Get Wire Profile
		
		:param nIndex: int
		:rtype: list[float]
		'''
		return self._ApplyTypes_(11003, 1, (8197, 0), ((19, 1),), 'GetWireProfile', None,nIndex
			)


	def ImportWireProfile(self, strFileName):
		'''
		Import Wire Profile
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11006, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def SetWireProfile(self, nIndex, pSafeArray):
		'''
		Set Wire Profile
		
		:param nIndex: int
		:param pSafeArray: list[float]
		'''
		return self._oleobj_.InvokeTypes(11002, LCID, 1, (24, 0), ((19, 1), (8197, 1)),nIndex
			, pSafeArray)


	def _get_HorizontalRadius(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "HorizontalRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_NumOfSegments(self):
		return self._ApplyTypes_(*(11010, 2, (9, 0), (), "NumOfSegments", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_VerticalRadius(self):
		return self._ApplyTypes_(*(11009, 2, (9, 0), (), "VerticalRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WireProfileFileName(self):
		return self._ApplyTypes_(*(11005, 2, (8, 0), (), "WireProfileFileName", None))
	def _get_WireProfileType(self):
		return self._ApplyTypes_(*(11001, 2, (3, 0), (), "WireProfileType", '{1616B733-CBF9-4070-AC39-D70D8084103B}'))

	def _set_WireProfileFileName(self, value):
		if "WireProfileFileName" in self.__dict__: self.__dict__["WireProfileFileName"] = value; return
		self._oleobj_.Invoke(*((11005, LCID, 4, 0) + (value,) + ()))

	HorizontalRadius = property(_get_HorizontalRadius, None)
	'''
	Horizontal radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	NumOfSegments = property(_get_NumOfSegments, None)
	'''
	Number of segments

	:type: recurdyn.ProcessNet.IDouble
	'''
	VerticalRadius = property(_get_VerticalRadius, None)
	'''
	Vertical radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	WireProfileFileName = property(_get_WireProfileFileName, _set_WireProfileFileName)
	'''
	Wire Profile File name

	:type: str
	'''
	WireProfileType = property(_get_WireProfileType, None)
	'''
	Wire Profile Type

	:type: recurdyn.MMS.MMSProfileType
	'''

	_prop_map_set_function_ = {
		"_set_WireProfileFileName": _set_WireProfileFileName,
	}
	_prop_map_get_ = {
		"HorizontalRadius": (11008, 2, (9, 0), (), "HorizontalRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"NumOfSegments": (11010, 2, (9, 0), (), "NumOfSegments", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"VerticalRadius": (11009, 2, (9, 0), (), "VerticalRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WireProfileFileName": (11005, 2, (8, 0), (), "WireProfileFileName", None),
		"WireProfileType": (11001, 2, (3, 0), (), "WireProfileType", '{1616B733-CBF9-4070-AC39-D70D8084103B}'),
	}
	_prop_map_put_ = {
		"WireProfileFileName": ((11005, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeC(DispatchBaseClass):
	'''MMS TypeC'''
	CLSID = IID('{FA1C1DD1-7A02-499A-88C2-49565A037C3E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CopyActionToBase(self, type):
		'''
		Copy action to base
		
		:param type: CopyMarkerType
		'''
		return self._oleobj_.InvokeTypes(11065, LCID, 1, (24, 0), ((3, 1),),type
			)


	def CopyBaseToAction(self, type):
		'''
		Copy base to action
		
		:param type: CopyMarkerType
		'''
		return self._oleobj_.InvokeTypes(11064, LCID, 1, (24, 0), ((3, 1),),type
			)


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


	def _get_ActionMarker(self):
		return self._ApplyTypes_(*(11063, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseMarker(self):
		return self._ApplyTypes_(*(11062, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Color(self):
		return self._ApplyTypes_(*(11066, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_FreeLength(self):
		return self._ApplyTypes_(*(11055, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumOfWindingForHighPitchPart(self):
		return self._ApplyTypes_(*(11059, 2, (9, 0), (), "NumOfWindingForHighPitchPart", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_NumOfWindingForLowPitchPart(self):
		return self._ApplyTypes_(*(11058, 2, (9, 0), (), "NumOfWindingForLowPitchPart", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_NumOfWindingForSeatContactPart(self):
		return self._ApplyTypes_(*(11057, 2, (9, 0), (), "NumOfWindingForSeatContactPart", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RatioOfDiameter(self):
		return self._ApplyTypes_(*(11054, 2, (9, 0), (), "RatioOfDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SetupLength(self):
		return self._ApplyTypes_(*(11056, 2, (9, 0), (), "SetupLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpringDiameter(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "SpringDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpringProperty(self):
		return self._ApplyTypes_(*(11060, 2, (9, 0), (), "SpringProperty", '{4ED0F6FA-42EA-4CEB-857B-96B5B2EB28CC}'))
	def _get_SpringType(self):
		return self._ApplyTypes_(*(11051, 2, (3, 0), (), "SpringType", '{E1A446BD-4BDF-41B1-B9FB-648CD06C57BA}'))
	def _get_UseAutoUpdateGeometry(self):
		return self._ApplyTypes_(*(11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None))
	def _get_UseSimpleGraphic(self):
		return self._ApplyTypes_(*(11061, 2, (11, 0), (), "UseSimpleGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_WireDiameter(self):
		return self._ApplyTypes_(*(11053, 2, (9, 0), (), "WireDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_ActionMarker(self, value):
		if "ActionMarker" in self.__dict__: self.__dict__["ActionMarker"] = value; return
		self._oleobj_.Invoke(*((11063, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseMarker(self, value):
		if "BaseMarker" in self.__dict__: self.__dict__["BaseMarker"] = value; return
		self._oleobj_.Invoke(*((11062, LCID, 4, 0) + (value,) + ()))
	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((11066, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_SpringType(self, value):
		if "SpringType" in self.__dict__: self.__dict__["SpringType"] = value; return
		self._oleobj_.Invoke(*((11051, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoUpdateGeometry(self, value):
		if "UseAutoUpdateGeometry" in self.__dict__: self.__dict__["UseAutoUpdateGeometry"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
	def _set_UseSimpleGraphic(self, value):
		if "UseSimpleGraphic" in self.__dict__: self.__dict__["UseSimpleGraphic"] = value; return
		self._oleobj_.Invoke(*((11061, LCID, 4, 0) + (value,) + ()))
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
	BaseMarker = property(_get_BaseMarker, _set_BaseMarker)
	'''
	Base marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	FreeLength = property(_get_FreeLength, None)
	'''
	Free Length

	:type: recurdyn.ProcessNet.IDouble
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
	NumOfWindingForHighPitchPart = property(_get_NumOfWindingForHighPitchPart, None)
	'''
	Number of winding for High Pitch Part

	:type: recurdyn.ProcessNet.IDouble
	'''
	NumOfWindingForLowPitchPart = property(_get_NumOfWindingForLowPitchPart, None)
	'''
	Number of winding for Low Pitch Part

	:type: recurdyn.ProcessNet.IDouble
	'''
	NumOfWindingForSeatContactPart = property(_get_NumOfWindingForSeatContactPart, None)
	'''
	Number of winding for Seat Contact Part

	:type: recurdyn.ProcessNet.IDouble
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
	RatioOfDiameter = property(_get_RatioOfDiameter, None)
	'''
	Ratio of Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	SetupLength = property(_get_SetupLength, None)
	'''
	Setup Length

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpringDiameter = property(_get_SpringDiameter, None)
	'''
	Spring Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	SpringProperty = property(_get_SpringProperty, None)
	'''
	Spring Property

	:type: recurdyn.MMS.IMMSGroupTypeCSpringProperty
	'''
	SpringType = property(_get_SpringType, _set_SpringType)
	'''
	Spring Type

	:type: recurdyn.MMS.SpringType
	'''
	UseAutoUpdateGeometry = property(_get_UseAutoUpdateGeometry, _set_UseAutoUpdateGeometry)
	'''
	Use Update Geometry Automatically

	:type: bool
	'''
	UseSimpleGraphic = property(_get_UseSimpleGraphic, _set_UseSimpleGraphic)
	'''
	Use maximum force

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	WireDiameter = property(_get_WireDiameter, None)
	'''
	Wire Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_ActionMarker": _set_ActionMarker,
		"_set_Active": _set_Active,
		"_set_BaseMarker": _set_BaseMarker,
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_SpringType": _set_SpringType,
		"_set_UseAutoUpdateGeometry": _set_UseAutoUpdateGeometry,
		"_set_UseSimpleGraphic": _set_UseSimpleGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionMarker": (11063, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseMarker": (11062, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Color": (11066, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FreeLength": (11055, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumOfWindingForHighPitchPart": (11059, 2, (9, 0), (), "NumOfWindingForHighPitchPart", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"NumOfWindingForLowPitchPart": (11058, 2, (9, 0), (), "NumOfWindingForLowPitchPart", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"NumOfWindingForSeatContactPart": (11057, 2, (9, 0), (), "NumOfWindingForSeatContactPart", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RatioOfDiameter": (11054, 2, (9, 0), (), "RatioOfDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SetupLength": (11056, 2, (9, 0), (), "SetupLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpringDiameter": (11052, 2, (9, 0), (), "SpringDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpringProperty": (11060, 2, (9, 0), (), "SpringProperty", '{4ED0F6FA-42EA-4CEB-857B-96B5B2EB28CC}'),
		"SpringType": (11051, 2, (3, 0), (), "SpringType", '{E1A446BD-4BDF-41B1-B9FB-648CD06C57BA}'),
		"UseAutoUpdateGeometry": (11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None),
		"UseSimpleGraphic": (11061, 2, (11, 0), (), "UseSimpleGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"WireDiameter": (11053, 2, (9, 0), (), "WireDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"ActionMarker": ((11063, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseMarker": ((11062, LCID, 4, 0),()),
		"Color": ((11066, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"SpringType": ((11051, LCID, 4, 0),()),
		"UseAutoUpdateGeometry": ((11001, LCID, 4, 0),()),
		"UseSimpleGraphic": ((11061, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeCSpringProperty(DispatchBaseClass):
	'''MMS TypeC Spring Property'''
	CLSID = IID('{4ED0F6FA-42EA-4CEB-857B-96B5B2EB28CC}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearModulus(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(11001, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

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
	ShearModulus = property(_get_ShearModulus, None)
	'''
	Shear modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	Young's modulus

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DampingRatio": (11004, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (11003, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearModulus": (11002, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YoungsModulus": (11001, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IMMSGroupTypeD(DispatchBaseClass):
	'''MMS TypeD'''
	CLSID = IID('{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')
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
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11058, 2, (9, 0), (), "ContactProperty", '{47D76536-2593-45BB-A395-7F3172FEFE73}'))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_FirstPoint(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "FirstPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11057, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11060, 2, (9, 0), (), "Geometry", '{8511DE02-96EB-46A6-BFEF-4ED5B3008310}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Material(self):
		return self._ApplyTypes_(*(11059, 2, (9, 0), (), "Material", '{C9DF98FE-41B7-4E04-B011-F22647D193EC}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ReferenceDirection(self):
		return self._ApplyTypes_(*(11053, 2, (8197, 0), (), "ReferenceDirection", None))
	def _get_SecondPoint(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_UseAutoCalculationBEAMProperty(self):
		return self._ApplyTypes_(*(11056, 2, (11, 0), (), "UseAutoCalculationBEAMProperty", None))
	def _get_UseAutoUpdateGeometry(self):
		return self._ApplyTypes_(*(11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None))
	def _get_UseBeamForceDisplay(self):
		return self._ApplyTypes_(*(11055, 2, (11, 0), (), "UseBeamForceDisplay", None))
	def _get_UseInactiveAllContacts(self):
		return self._ApplyTypes_(*(11061, 2, (11, 0), (), "UseInactiveAllContacts", None))
	def _get_UseUpdateContactProperty(self):
		return self._ApplyTypes_(*(11054, 2, (11, 0), (), "UseUpdateContactProperty", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11057, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceDirection(self, value):
		if "ReferenceDirection" in self.__dict__: self.__dict__["ReferenceDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseAutoCalculationBEAMProperty(self, value):
		if "UseAutoCalculationBEAMProperty" in self.__dict__: self.__dict__["UseAutoCalculationBEAMProperty"] = value; return
		self._oleobj_.Invoke(*((11056, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoUpdateGeometry(self, value):
		if "UseAutoUpdateGeometry" in self.__dict__: self.__dict__["UseAutoUpdateGeometry"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
	def _set_UseBeamForceDisplay(self, value):
		if "UseBeamForceDisplay" in self.__dict__: self.__dict__["UseBeamForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11055, LCID, 4, 0) + (value,) + ()))
	def _set_UseInactiveAllContacts(self, value):
		if "UseInactiveAllContacts" in self.__dict__: self.__dict__["UseInactiveAllContacts"] = value; return
		self._oleobj_.Invoke(*((11061, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdateContactProperty(self, value):
		if "UseUpdateContactProperty" in self.__dict__: self.__dict__["UseUpdateContactProperty"] = value; return
		self._oleobj_.Invoke(*((11054, LCID, 4, 0) + (value,) + ()))
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
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Group Type D Contact Property

	:type: recurdyn.MMS.IMMSGroupTypeDContactProperty
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	FirstPoint = property(_get_FirstPoint, None)
	'''
	First point

	:type: recurdyn.ProcessNet.IVector
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
	Geometry = property(_get_Geometry, None)
	'''
	Group Type D Geometry

	:type: recurdyn.MMS.IMMSGroupTypeDGeometry
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	Material = property(_get_Material, None)
	'''
	Group Type D Material

	:type: recurdyn.MMS.IMMSGroupTypeDMaterial
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
	ReferenceDirection = property(_get_ReferenceDirection, _set_ReferenceDirection)
	'''
	Reference direction

	:type: list[float]
	'''
	SecondPoint = property(_get_SecondPoint, None)
	'''
	Second point

	:type: recurdyn.ProcessNet.IVector
	'''
	UseAutoCalculationBEAMProperty = property(_get_UseAutoCalculationBEAMProperty, _set_UseAutoCalculationBEAMProperty)
	'''
	Use auto-calculation for the BEAM property

	:type: bool
	'''
	UseAutoUpdateGeometry = property(_get_UseAutoUpdateGeometry, _set_UseAutoUpdateGeometry)
	'''
	Use Update Geometry Automatically

	:type: bool
	'''
	UseBeamForceDisplay = property(_get_UseBeamForceDisplay, _set_UseBeamForceDisplay)
	'''
	Use beam force display

	:type: bool
	'''
	UseInactiveAllContacts = property(_get_UseInactiveAllContacts, _set_UseInactiveAllContacts)
	'''
	Use inactive all contacts

	:type: bool
	'''
	UseUpdateContactProperty = property(_get_UseUpdateContactProperty, _set_UseUpdateContactProperty)
	'''
	Use update contact property

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
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_ReferenceDirection": _set_ReferenceDirection,
		"_set_UseAutoCalculationBEAMProperty": _set_UseAutoCalculationBEAMProperty,
		"_set_UseAutoUpdateGeometry": _set_UseAutoUpdateGeometry,
		"_set_UseBeamForceDisplay": _set_UseBeamForceDisplay,
		"_set_UseInactiveAllContacts": _set_UseInactiveAllContacts,
		"_set_UseUpdateContactProperty": _set_UseUpdateContactProperty,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactProperty": (11058, 2, (9, 0), (), "ContactProperty", '{47D76536-2593-45BB-A395-7F3172FEFE73}'),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FirstPoint": (11051, 2, (9, 0), (), "FirstPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"ForceDisplay": (11057, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (11060, 2, (9, 0), (), "Geometry", '{8511DE02-96EB-46A6-BFEF-4ED5B3008310}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Material": (11059, 2, (9, 0), (), "Material", '{C9DF98FE-41B7-4E04-B011-F22647D193EC}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ReferenceDirection": (11053, 2, (8197, 0), (), "ReferenceDirection", None),
		"SecondPoint": (11052, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"UseAutoCalculationBEAMProperty": (11056, 2, (11, 0), (), "UseAutoCalculationBEAMProperty", None),
		"UseAutoUpdateGeometry": (11001, 2, (11, 0), (), "UseAutoUpdateGeometry", None),
		"UseBeamForceDisplay": (11055, 2, (11, 0), (), "UseBeamForceDisplay", None),
		"UseInactiveAllContacts": (11061, 2, (11, 0), (), "UseInactiveAllContacts", None),
		"UseUpdateContactProperty": (11054, 2, (11, 0), (), "UseUpdateContactProperty", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"ForceDisplay": ((11057, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ReferenceDirection": ((11053, LCID, 4, 0),()),
		"UseAutoCalculationBEAMProperty": ((11056, LCID, 4, 0),()),
		"UseAutoUpdateGeometry": ((11001, LCID, 4, 0),()),
		"UseBeamForceDisplay": ((11055, LCID, 4, 0),()),
		"UseInactiveAllContacts": ((11061, LCID, 4, 0),()),
		"UseUpdateContactProperty": ((11054, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeDContactFriction(DispatchBaseClass):
	'''MMS TypeD Contact friction'''
	CLSID = IID('{0A109CF4-FF09-40DA-B076-EA8E0BD207FD}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Coefficient(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "Coefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactFrictionType(self):
		return self._ApplyTypes_(*(11001, 2, (3, 0), (), "ContactFrictionType", '{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}'))
	def _get_DynamicThresholdVelocity(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumForce(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "MaximumForce", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Spline(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "Spline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_StaticCoefficient(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "StaticCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticThresholdVelocity(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseMaximumForce(self):
		return self._ApplyTypes_(*(11008, 2, (11, 0), (), "UseMaximumForce", None))

	def _set_ContactFrictionType(self, value):
		if "ContactFrictionType" in self.__dict__: self.__dict__["ContactFrictionType"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
	def _set_Spline(self, value):
		if "Spline" in self.__dict__: self.__dict__["Spline"] = value; return
		self._oleobj_.Invoke(*((11003, LCID, 4, 0) + (value,) + ()))
	def _set_UseMaximumForce(self, value):
		if "UseMaximumForce" in self.__dict__: self.__dict__["UseMaximumForce"] = value; return
		self._oleobj_.Invoke(*((11008, LCID, 4, 0) + (value,) + ()))

	Coefficient = property(_get_Coefficient, None)
	'''
	The constant dynamic friction coefficient for the contact friction force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactFrictionType = property(_get_ContactFrictionType, _set_ContactFrictionType)
	'''
	Contact friction type

	:type: recurdyn.ProcessNet.ContactFrictionType
	'''
	DynamicThresholdVelocity = property(_get_DynamicThresholdVelocity, None)
	'''
	Dynamic threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumForce = property(_get_MaximumForce, None)
	'''
	Maximum force

	:type: recurdyn.ProcessNet.IDouble
	'''
	Spline = property(_get_Spline, _set_Spline)
	'''
	The spline which shows relative velocity to the friction coefficient or the friction force.

	:type: recurdyn.ProcessNet.ISpline
	'''
	StaticCoefficient = property(_get_StaticCoefficient, None)
	'''
	Static coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	StaticThresholdVelocity = property(_get_StaticThresholdVelocity, None)
	'''
	Static threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseMaximumForce = property(_get_UseMaximumForce, _set_UseMaximumForce)
	'''
	Use maximum force

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactFrictionType": _set_ContactFrictionType,
		"_set_Spline": _set_Spline,
		"_set_UseMaximumForce": _set_UseMaximumForce,
	}
	_prop_map_get_ = {
		"Coefficient": (11002, 2, (9, 0), (), "Coefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactFrictionType": (11001, 2, (3, 0), (), "ContactFrictionType", '{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}'),
		"DynamicThresholdVelocity": (11005, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumForce": (11007, 2, (9, 0), (), "MaximumForce", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Spline": (11003, 2, (9, 0), (), "Spline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"StaticCoefficient": (11006, 2, (9, 0), (), "StaticCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticThresholdVelocity": (11004, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseMaximumForce": (11008, 2, (11, 0), (), "UseMaximumForce", None),
	}
	_prop_map_put_ = {
		"ContactFrictionType": ((11001, LCID, 4, 0),()),
		"Spline": ((11003, LCID, 4, 0),()),
		"UseMaximumForce": ((11008, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeDContactProperty(DispatchBaseClass):
	'''MMS TypeD Contact property'''
	CLSID = IID('{47D76536-2593-45BB-A395-7F3172FEFE73}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BufferRadiusFactor(self):
		return self._ApplyTypes_(*(11016, 2, (9, 0), (), "BufferRadiusFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(11010, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11018, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(11013, 2, (9, 0), (), "Friction", '{0A109CF4-FF09-40DA-B076-EA8E0BD207FD}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(11012, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaxStepSizeFactor(self):
		return self._ApplyTypes_(*(11017, 2, (9, 0), (), "MaxStepSizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(11001, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(11009, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(11005, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(11011, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(11007, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(11002, 2, (11, 0), (), "UseStiffnessSpline", None))
	def _get_UseUserSubroutine(self):
		return self._ApplyTypes_(*(11014, 2, (11, 0), (), "UseUserSubroutine", None))
	def _get_UserSubroutine(self):
		return self._ApplyTypes_(*(11015, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((11006, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11018, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((11003, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((11009, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((11005, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((11011, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((11007, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((11002, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserSubroutine(self, value):
		if "UseUserSubroutine" in self.__dict__: self.__dict__["UseUserSubroutine"] = value; return
		self._oleobj_.Invoke(*((11014, LCID, 4, 0) + (value,) + ()))
	def _set_UserSubroutine(self, value):
		if "UserSubroutine" in self.__dict__: self.__dict__["UserSubroutine"] = value; return
		self._oleobj_.Invoke(*((11015, LCID, 4, 0) + (value,) + ()))

	BufferRadiusFactor = property(_get_BufferRadiusFactor, None)
	'''
	Buffer radius factor. Numerical integrator reduces the step size by the maximum stepsize factor if the action body come closer than buffer radius factor*action body radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingCoefficient = property(_get_DampingCoefficient, None)
	'''
	The viscous damping coefficient for the contact normal force.

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
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	Friction = property(_get_Friction, None)
	'''
	Friction

	:type: recurdyn.MMS.IMMSGroupTypeDContactFriction
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	The indentation exponent yields an indentation damping effect.

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaxStepSizeFactor = property(_get_MaxStepSizeFactor, None)
	'''
	Maximum step size factor. The maximum step size is reduced by a factor of maximum step size factor.

	:type: recurdyn.ProcessNet.IDouble
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
	UseUserSubroutine = property(_get_UseUserSubroutine, _set_UseUserSubroutine)
	'''
	Use user subroutine

	:type: bool
	'''
	UserSubroutine = property(_get_UserSubroutine, _set_UserSubroutine)
	'''
	User subroutine

	:type: recurdyn.ProcessNet.IUserSubroutine
	'''

	_prop_map_set_function_ = {
		"_set_DampingSpline": _set_DampingSpline,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseIndentationExponent": _set_UseIndentationExponent,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
		"_set_UseUserSubroutine": _set_UseUserSubroutine,
		"_set_UserSubroutine": _set_UserSubroutine,
	}
	_prop_map_get_ = {
		"BufferRadiusFactor": (11016, 2, (9, 0), (), "BufferRadiusFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingCoefficient": (11004, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (11010, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (11006, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"ForceDisplay": (11018, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"Friction": (11013, 2, (9, 0), (), "Friction", '{0A109CF4-FF09-40DA-B076-EA8E0BD207FD}'),
		"IndentationExponent": (11012, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaxStepSizeFactor": (11017, 2, (9, 0), (), "MaxStepSizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (11001, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (11008, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (11003, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (11009, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (11005, 2, (11, 0), (), "UseDampingSpline", None),
		"UseIndentationExponent": (11011, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseStiffnessExponent": (11007, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (11002, 2, (11, 0), (), "UseStiffnessSpline", None),
		"UseUserSubroutine": (11014, 2, (11, 0), (), "UseUserSubroutine", None),
		"UserSubroutine": (11015, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'),
	}
	_prop_map_put_ = {
		"DampingSpline": ((11006, LCID, 4, 0),()),
		"ForceDisplay": ((11018, LCID, 4, 0),()),
		"StiffnessSpline": ((11003, LCID, 4, 0),()),
		"UseDampingExponent": ((11009, LCID, 4, 0),()),
		"UseDampingSpline": ((11005, LCID, 4, 0),()),
		"UseIndentationExponent": ((11011, LCID, 4, 0),()),
		"UseStiffnessExponent": ((11007, LCID, 4, 0),()),
		"UseStiffnessSpline": ((11002, LCID, 4, 0),()),
		"UseUserSubroutine": ((11014, LCID, 4, 0),()),
		"UserSubroutine": ((11015, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeDGeometry(DispatchBaseClass):
	'''MMS TypeD Geometry'''
	CLSID = IID('{8511DE02-96EB-46A6-BFEF-4ED5B3008310}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddCenterLineProfile(self, pSafeArray):
		'''
		Insert Center Line Profile
		
		:param pSafeArray: list[float]
		'''
		return self._oleobj_.InvokeTypes(11018, LCID, 1, (24, 0), ((8197, 1),),pSafeArray
			)


	def DeleteAllCenterLineProfile(self):
		'''
		Delete Center Line Profile
		'''
		return self._oleobj_.InvokeTypes(11020, LCID, 1, (24, 0), (),)


	def DeleteCenterLineProfile(self, nIndex):
		'''
		Delete Center Line Profile
		
		:param nIndex: int
		'''
		return self._oleobj_.InvokeTypes(11019, LCID, 1, (24, 0), ((19, 1),),nIndex
			)


	def ExportCenterLineProfile(self, strFileName):
		'''
		Export Center Line Profile
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11026, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def GetCenterLineProfile(self, nIndex):
		'''
		Get Center Line Profile
		
		:param nIndex: int
		:rtype: list[float]
		'''
		return self._ApplyTypes_(11022, 1, (8197, 0), ((19, 1),), 'GetCenterLineProfile', None,nIndex
			)


	def GetSizeCenterLineProfile(self):
		'''
		Get index size of Center Line Profile
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(11023, LCID, 1, (19, 0), (),)


	def ImportCenterLineProfile(self, strFileName):
		'''
		Import Center Line Profile
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11025, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def SetCenterLineProfile(self, nIndex, pSafeArray):
		'''
		Set Center Line Profile
		
		:param nIndex: int
		:param pSafeArray: list[float]
		'''
		return self._oleobj_.InvokeTypes(11021, LCID, 1, (24, 0), ((19, 1), (8197, 1)),nIndex
			, pSafeArray)


	def _get_CenterLineProfileFileName(self):
		return self._ApplyTypes_(*(11024, 2, (8, 0), (), "CenterLineProfileFileName", None))
	def _get_CenterLineProfileType(self):
		return self._ApplyTypes_(*(11017, 2, (3, 0), (), "CenterLineProfileType", '{1616B733-CBF9-4070-AC39-D70D8084103B}'))
	def _get_CrossSectionType(self):
		return self._ApplyTypes_(*(11001, 2, (3, 0), (), "CrossSectionType", '{47916431-C6E6-4880-B7AD-7E114B5BFE1C}'))
	def _get_Diameter(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "Diameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DirectionHelixType(self):
		return self._ApplyTypes_(*(11002, 2, (3, 0), (), "DirectionHelixType", '{181F3A0D-D841-4783-8F0D-25CEC6EBEE20}'))
	def _get_EffectiveNoOfHelix(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "EffectiveNoOfHelix", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Exponent(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "Exponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InsideDiameter(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "InsideDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_NoOfHelixInBDivision(self):
		return self._ApplyTypes_(*(11011, 2, (9, 0), (), "NoOfHelixInBDivision", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PitchAngleInBDivision(self):
		return self._ApplyTypes_(*(11010, 2, (9, 0), (), "PitchAngleInBDivision", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SplineInterpolationCoefficient1(self):
		return self._ApplyTypes_(*(11014, 2, (9, 0), (), "SplineInterpolationCoefficient1", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SplineInterpolationCoefficient2(self):
		return self._ApplyTypes_(*(11015, 2, (9, 0), (), "SplineInterpolationCoefficient2", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SplineInterpolationCoefficient3(self):
		return self._ApplyTypes_(*(11016, 2, (9, 0), (), "SplineInterpolationCoefficient3", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThicknessOfAEdgeGap(self):
		return self._ApplyTypes_(*(11012, 2, (9, 0), (), "ThicknessOfAEdgeGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThicknessOfBEdgeGap(self):
		return self._ApplyTypes_(*(11013, 2, (9, 0), (), "ThicknessOfBEdgeGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseProfile(self):
		return self._ApplyTypes_(*(11009, 2, (11, 0), (), "UseProfile", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_CenterLineProfileFileName(self, value):
		if "CenterLineProfileFileName" in self.__dict__: self.__dict__["CenterLineProfileFileName"] = value; return
		self._oleobj_.Invoke(*((11024, LCID, 4, 0) + (value,) + ()))
	def _set_CrossSectionType(self, value):
		if "CrossSectionType" in self.__dict__: self.__dict__["CrossSectionType"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
	def _set_DirectionHelixType(self, value):
		if "DirectionHelixType" in self.__dict__: self.__dict__["DirectionHelixType"] = value; return
		self._oleobj_.Invoke(*((11002, LCID, 4, 0) + (value,) + ()))
	def _set_UseProfile(self, value):
		if "UseProfile" in self.__dict__: self.__dict__["UseProfile"] = value; return
		self._oleobj_.Invoke(*((11009, LCID, 4, 0) + (value,) + ()))

	CenterLineProfileFileName = property(_get_CenterLineProfileFileName, _set_CenterLineProfileFileName)
	'''
	Center Line Profile File name

	:type: str
	'''
	CenterLineProfileType = property(_get_CenterLineProfileType, None)
	'''
	Center Line Profile Type

	:type: recurdyn.MMS.MMSProfileType
	'''
	CrossSectionType = property(_get_CrossSectionType, _set_CrossSectionType)
	'''
	Cross Section Type

	:type: recurdyn.MMS.MMSCrossSectionType
	'''
	Diameter = property(_get_Diameter, None)
	'''
	Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	DirectionHelixType = property(_get_DirectionHelixType, _set_DirectionHelixType)
	'''
	Direction of Helix Type

	:type: recurdyn.MMS.MMSDirectionHelixType
	'''
	EffectiveNoOfHelix = property(_get_EffectiveNoOfHelix, None)
	'''
	Effective num of helix

	:type: recurdyn.ProcessNet.IDouble
	'''
	Exponent = property(_get_Exponent, None)
	'''
	Exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	InsideDiameter = property(_get_InsideDiameter, None)
	'''
	Inside Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	NoOfHelixInBDivision = property(_get_NoOfHelixInBDivision, None)
	'''
	Num of helix in B division

	:type: recurdyn.ProcessNet.IDouble
	'''
	PitchAngleInBDivision = property(_get_PitchAngleInBDivision, None)
	'''
	Pitch angle in B division

	:type: recurdyn.ProcessNet.IDouble
	'''
	SplineInterpolationCoefficient1 = property(_get_SplineInterpolationCoefficient1, None)
	'''
	Spline interpolation coefficient 1

	:type: recurdyn.ProcessNet.IDouble
	'''
	SplineInterpolationCoefficient2 = property(_get_SplineInterpolationCoefficient2, None)
	'''
	Spline interpolation coefficient 2

	:type: recurdyn.ProcessNet.IDouble
	'''
	SplineInterpolationCoefficient3 = property(_get_SplineInterpolationCoefficient3, None)
	'''
	Spline interpolation coefficient 3

	:type: recurdyn.ProcessNet.IDouble
	'''
	Thickness = property(_get_Thickness, None)
	'''
	Thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	ThicknessOfAEdgeGap = property(_get_ThicknessOfAEdgeGap, None)
	'''
	Thickness of A edge gap

	:type: recurdyn.ProcessNet.IDouble
	'''
	ThicknessOfBEdgeGap = property(_get_ThicknessOfBEdgeGap, None)
	'''
	Thickness of B edge gap

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseProfile = property(_get_UseProfile, _set_UseProfile)
	'''
	Use Profile

	:type: bool
	'''
	Width = property(_get_Width, None)
	'''
	Width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_CenterLineProfileFileName": _set_CenterLineProfileFileName,
		"_set_CrossSectionType": _set_CrossSectionType,
		"_set_DirectionHelixType": _set_DirectionHelixType,
		"_set_UseProfile": _set_UseProfile,
	}
	_prop_map_get_ = {
		"CenterLineProfileFileName": (11024, 2, (8, 0), (), "CenterLineProfileFileName", None),
		"CenterLineProfileType": (11017, 2, (3, 0), (), "CenterLineProfileType", '{1616B733-CBF9-4070-AC39-D70D8084103B}'),
		"CrossSectionType": (11001, 2, (3, 0), (), "CrossSectionType", '{47916431-C6E6-4880-B7AD-7E114B5BFE1C}'),
		"Diameter": (11006, 2, (9, 0), (), "Diameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DirectionHelixType": (11002, 2, (3, 0), (), "DirectionHelixType", '{181F3A0D-D841-4783-8F0D-25CEC6EBEE20}'),
		"EffectiveNoOfHelix": (11008, 2, (9, 0), (), "EffectiveNoOfHelix", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Exponent": (11005, 2, (9, 0), (), "Exponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InsideDiameter": (11007, 2, (9, 0), (), "InsideDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"NoOfHelixInBDivision": (11011, 2, (9, 0), (), "NoOfHelixInBDivision", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PitchAngleInBDivision": (11010, 2, (9, 0), (), "PitchAngleInBDivision", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SplineInterpolationCoefficient1": (11014, 2, (9, 0), (), "SplineInterpolationCoefficient1", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SplineInterpolationCoefficient2": (11015, 2, (9, 0), (), "SplineInterpolationCoefficient2", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SplineInterpolationCoefficient3": (11016, 2, (9, 0), (), "SplineInterpolationCoefficient3", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Thickness": (11004, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThicknessOfAEdgeGap": (11012, 2, (9, 0), (), "ThicknessOfAEdgeGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThicknessOfBEdgeGap": (11013, 2, (9, 0), (), "ThicknessOfBEdgeGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseProfile": (11009, 2, (11, 0), (), "UseProfile", None),
		"Width": (11003, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"CenterLineProfileFileName": ((11024, LCID, 4, 0),()),
		"CrossSectionType": ((11001, LCID, 4, 0),()),
		"DirectionHelixType": ((11002, LCID, 4, 0),()),
		"UseProfile": ((11009, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSGroupTypeDMaterial(DispatchBaseClass):
	'''MMS TypeD Material'''
	CLSID = IID('{C9DF98FE-41B7-4E04-B011-F22647D193EC}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def DampingMatrix(self, i, j):
		'''
		Damping matrix
		
		:param i: int
		:param j: int
		:rtype: recurdyn.ProcessNet.IDouble
		'''
		ret = self._oleobj_.InvokeTypes(11006, LCID, 1, (9, 0), ((3, 1), (3, 1)),i
			, j)
		if ret is not None:
			ret = Dispatch(ret, 'DampingMatrix', '{2B5166E3-4B31-4607-B157-BE237A670336}')
		return ret

	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PoissonRatio(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "PoissonRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearModulus(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(11001, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseDampingMatrix(self):
		return self._ApplyTypes_(*(11005, 2, (11, 0), (), "UseDampingMatrix", None))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_UseDampingMatrix(self, value):
		if "UseDampingMatrix" in self.__dict__: self.__dict__["UseDampingMatrix"] = value; return
		self._oleobj_.Invoke(*((11005, LCID, 4, 0) + (value,) + ()))

	DampingRatio = property(_get_DampingRatio, None)
	'''
	Damping ratio

	:type: recurdyn.ProcessNet.IDouble
	'''
	PoissonRatio = property(_get_PoissonRatio, None)
	'''
	Poisson's ratio

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearModulus = property(_get_ShearModulus, None)
	'''
	Shear modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalMass = property(_get_TotalMass, None)
	'''
	Total Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseDampingMatrix = property(_get_UseDampingMatrix, _set_UseDampingMatrix)
	'''
	Use damping matrix

	:type: bool
	'''
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	Young's modulus

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_UseDampingMatrix": _set_UseDampingMatrix,
	}
	_prop_map_get_ = {
		"DampingRatio": (11007, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PoissonRatio": (11003, 2, (9, 0), (), "PoissonRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearModulus": (11004, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalMass": (11001, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseDampingMatrix": (11005, 2, (11, 0), (), "UseDampingMatrix", None),
		"YoungsModulus": (11002, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"UseDampingMatrix": ((11005, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSIOTypeD(DispatchBaseClass):
	'''MMS Contact TypeD I/O'''
	CLSID = IID('{436E38BE-FFA6-4E99-AAE9-133B6E3A66EB}')
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


	def _get_ActionEntity(self):
		return self._ApplyTypes_(*(203, 2, (9, 0), (), "ActionEntity", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'))
	def _get_ActionEntityIGeneric(self):
		return self._ApplyTypes_(*(211, 2, (9, 0), (), "ActionEntityIGeneric", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_ActionSpringGroup(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "ActionSpringGroup", '{F6D5A583-7A62-4112-8BF3-BB69C99A0406}'))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseEntity(self):
		return self._ApplyTypes_(*(202, 2, (9, 0), (), "BaseEntity", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'))
	def _get_BaseEntityIGeneric(self):
		return self._ApplyTypes_(*(210, 2, (9, 0), (), "BaseEntityIGeneric", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_BaseSpringGroup(self):
		return self._ApplyTypes_(*(11001, 2, (9, 0), (), "BaseSpringGroup", '{F6D5A583-7A62-4112-8BF3-BB69C99A0406}'))
	def _get_BufferRadiusFactor(self):
		return self._ApplyTypes_(*(204, 2, (9, 0), (), "BufferRadiusFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(206, 2, (9, 0), (), "ContactProperty", '{E1DBBE0C-5542-4AB1-A7EB-C8E1FAE51DC1}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "ForceDisplayColor", None))
	def _get_ForceDisplayUse(self):
		return self._ApplyTypes_(*(212, 2, (11, 0), (), "ForceDisplayUse", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerName(self):
		return self._ApplyTypes_(*(207, 2, (8, 0), (), "LayerName", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MaxStepSizeFactor(self):
		return self._ApplyTypes_(*(205, 2, (9, 0), (), "MaxStepSizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(209, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionEntity(self, value):
		if "ActionEntity" in self.__dict__: self.__dict__["ActionEntity"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_ActionEntityIGeneric(self, value):
		if "ActionEntityIGeneric" in self.__dict__: self.__dict__["ActionEntityIGeneric"] = value; return
		self._oleobj_.Invoke(*((211, LCID, 4, 0) + (value,) + ()))
	def _set_ActionSpringGroup(self, value):
		if "ActionSpringGroup" in self.__dict__: self.__dict__["ActionSpringGroup"] = value; return
		self._oleobj_.Invoke(*((11002, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseEntity(self, value):
		if "BaseEntity" in self.__dict__: self.__dict__["BaseEntity"] = value; return
		self._oleobj_.Invoke(*((202, LCID, 4, 0) + (value,) + ()))
	def _set_BaseEntityIGeneric(self, value):
		if "BaseEntityIGeneric" in self.__dict__: self.__dict__["BaseEntityIGeneric"] = value; return
		self._oleobj_.Invoke(*((210, LCID, 4, 0) + (value,) + ()))
	def _set_BaseSpringGroup(self, value):
		if "BaseSpringGroup" in self.__dict__: self.__dict__["BaseSpringGroup"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((201, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayColor(self, value):
		if "ForceDisplayColor" in self.__dict__: self.__dict__["ForceDisplayColor"] = value; return
		self._oleobj_.Invoke(*((208, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayUse(self, value):
		if "ForceDisplayUse" in self.__dict__: self.__dict__["ForceDisplayUse"] = value; return
		self._oleobj_.Invoke(*((212, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_TorqueDisplayColor(self, value):
		if "TorqueDisplayColor" in self.__dict__: self.__dict__["TorqueDisplayColor"] = value; return
		self._oleobj_.Invoke(*((209, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionEntity = property(_get_ActionEntity, _set_ActionEntity)
	'''
	Action entity

	:type: recurdyn.ProcessNet.IGeometry
	'''
	ActionEntityIGeneric = property(_get_ActionEntityIGeneric, _set_ActionEntityIGeneric)
	'''
	Action entity

	:type: recurdyn.ProcessNet.IGeneric
	'''
	ActionSpringGroup = property(_get_ActionSpringGroup, _set_ActionSpringGroup)
	'''
	Action entity

	:type: recurdyn.MMS.IMMSGroupTypeD
	'''
	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseEntity = property(_get_BaseEntity, _set_BaseEntity)
	'''
	Base entity

	:type: recurdyn.ProcessNet.IGeometry
	'''
	BaseEntityIGeneric = property(_get_BaseEntityIGeneric, _set_BaseEntityIGeneric)
	'''
	Base entity

	:type: recurdyn.ProcessNet.IGeneric
	'''
	BaseSpringGroup = property(_get_BaseSpringGroup, _set_BaseSpringGroup)
	'''
	Base entity

	:type: recurdyn.MMS.IMMSGroupTypeD
	'''
	BufferRadiusFactor = property(_get_BufferRadiusFactor, None)
	'''
	Buffer radius factor. Numerical integrator reduces the step size by the maximum stepsize factor if the action body come closer than buffer radius factor*action body radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.ProcessNet.IContactProperty
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
	MaxStepSizeFactor = property(_get_MaxStepSizeFactor, None)
	'''
	Maximum step size factor. The maximum step size is reduced by a factor of maximum step size factor.

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
	TorqueDisplayColor = property(_get_TorqueDisplayColor, _set_TorqueDisplayColor)
	'''
	Torque display color

	:type: int
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ActionEntity": _set_ActionEntity,
		"_set_ActionEntityIGeneric": _set_ActionEntityIGeneric,
		"_set_ActionSpringGroup": _set_ActionSpringGroup,
		"_set_Active": _set_Active,
		"_set_BaseEntity": _set_BaseEntity,
		"_set_BaseEntityIGeneric": _set_BaseEntityIGeneric,
		"_set_BaseSpringGroup": _set_BaseSpringGroup,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_ForceDisplayColor": _set_ForceDisplayColor,
		"_set_ForceDisplayUse": _set_ForceDisplayUse,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_TorqueDisplayColor": _set_TorqueDisplayColor,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionEntity": (203, 2, (9, 0), (), "ActionEntity", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'),
		"ActionEntityIGeneric": (211, 2, (9, 0), (), "ActionEntityIGeneric", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"ActionSpringGroup": (11002, 2, (9, 0), (), "ActionSpringGroup", '{F6D5A583-7A62-4112-8BF3-BB69C99A0406}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseEntity": (202, 2, (9, 0), (), "BaseEntity", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'),
		"BaseEntityIGeneric": (210, 2, (9, 0), (), "BaseEntityIGeneric", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"BaseSpringGroup": (11001, 2, (9, 0), (), "BaseSpringGroup", '{F6D5A583-7A62-4112-8BF3-BB69C99A0406}'),
		"BufferRadiusFactor": (204, 2, (9, 0), (), "BufferRadiusFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactProperty": (206, 2, (9, 0), (), "ContactProperty", '{E1DBBE0C-5542-4AB1-A7EB-C8E1FAE51DC1}'),
		"ForceDisplay": (201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayColor": (208, 2, (19, 0), (), "ForceDisplayColor", None),
		"ForceDisplayUse": (212, 2, (11, 0), (), "ForceDisplayUse", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerName": (207, 2, (8, 0), (), "LayerName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MaxStepSizeFactor": (205, 2, (9, 0), (), "MaxStepSizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"TorqueDisplayColor": (209, 2, (19, 0), (), "TorqueDisplayColor", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionEntity": ((203, LCID, 4, 0),()),
		"ActionEntityIGeneric": ((211, LCID, 4, 0),()),
		"ActionSpringGroup": ((11002, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseEntity": ((202, LCID, 4, 0),()),
		"BaseEntityIGeneric": ((210, LCID, 4, 0),()),
		"BaseSpringGroup": ((11001, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((208, LCID, 4, 0),()),
		"ForceDisplayUse": ((212, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((209, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMMSToolkit(DispatchBaseClass):
	'''MMS Toolkit'''
	CLSID = IID('{CF0E6EBB-7784-4445-B2B2-A5948BF68CF8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateMMSGroupTypeA(self, strName, pFirstPoint, pSecondPoint, dActiveCoil, numSegment):
		'''
		Creates a MMS type A Group
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param dActiveCoil: float
		:param numSegment: int
		:rtype: recurdyn.MMS.IMMSGroupTypeA
		'''
		ret = self._oleobj_.InvokeTypes(11052, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1), (19, 1)),strName
			, pFirstPoint, pSecondPoint, dActiveCoil, numSegment)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMMSGroupTypeA', '{7101723B-18D0-4B5A-8298-A0243B1815F4}')
		return ret

	def CreateMMSGroupTypeB(self, strName, pFirstPoint, pSecondPoint, numSegment):
		'''
		Creates a MMS type B Group
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param numSegment: int
		:rtype: recurdyn.MMS.IMMSGroupTypeB
		'''
		ret = self._oleobj_.InvokeTypes(11053, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (19, 1)),strName
			, pFirstPoint, pSecondPoint, numSegment)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMMSGroupTypeB', '{43A3CDF3-CF97-4C22-B8B8-33F63EFBCE05}')
		return ret

	def CreateMMSGroupTypeC(self, strName, pBaseBody, pActionBody, pBaseOriginPoint, pActionOriginPoint):
		'''
		Creates a MMS type C Group
		
		:param strName: str
		:param pBaseBody: IBody
		:param pActionBody: IBody
		:param pBaseOriginPoint: list[float]
		:param pActionOriginPoint: list[float]
		:rtype: recurdyn.MMS.IMMSGroupTypeC
		'''
		ret = self._oleobj_.InvokeTypes(11054, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (8197, 1), (8197, 1)),strName
			, pBaseBody, pActionBody, pBaseOriginPoint, pActionOriginPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMMSGroupTypeC', '{FA1C1DD1-7A02-499A-88C2-49565A037C3E}')
		return ret

	def CreateMMSGroupTypeD(self, strName, pFirstPoint, pSecondPoint, dHelix, numSegment):
		'''
		Creates a MMS type D Group
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param dHelix: float
		:param numSegment: int
		:rtype: recurdyn.MMS.IMMSGroupTypeD
		'''
		ret = self._oleobj_.InvokeTypes(11055, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1), (19, 1)),strName
			, pFirstPoint, pSecondPoint, dHelix, numSegment)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMMSGroupTypeD', '{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')
		return ret

	def CreateMMSGroupTypeD2(self, strName, pFirstPoint, pSecondPoint, dHelix, dEffectiveHelix, numSegment):
		'''
		Creates a MMS type D Group
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param dHelix: float
		:param dEffectiveHelix: float
		:param numSegment: int
		:rtype: recurdyn.MMS.IMMSGroupTypeD
		'''
		ret = self._oleobj_.InvokeTypes(11057, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1), (5, 1), (19, 1)),strName
			, pFirstPoint, pSecondPoint, dHelix, dEffectiveHelix, numSegment
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMMSGroupTypeD2', '{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')
		return ret

	def CreateMMSIOTypeD(self, strName, pOuterGroup, pInnerGroup):
		'''
		Creates a MMS type D IO
		
		:param strName: str
		:param pOuterGroup: IMMSGroupTypeD
		:param pInnerGroup: IMMSGroupTypeD
		:rtype: recurdyn.MMS.IMMSIOTypeD
		'''
		ret = self._oleobj_.InvokeTypes(11056, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pOuterGroup, pInnerGroup)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMMSIOTypeD', '{436E38BE-FFA6-4E99-AAE9-133B6E3A66EB}')
		return ret

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
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
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
	GeneralSubSystem = property(_get_GeneralSubSystem, None)
	'''
	Access general SubSystem

	:type: recurdyn.ProcessNet.ISubSystem
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
		"GeneralSubSystem": (11051, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
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

IMMSGroup_vtables_dispatch_ = 1
IMMSGroup_vtables_ = [
	(( 'UseAutoUpdateGeometry' , 'pVal' , ), 11001, (11001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoUpdateGeometry' , 'pVal' , ), 11001, (11001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeA_vtables_dispatch_ = 1
IMMSGroupTypeA_vtables_ = [
	(( 'FirstPoint' , 'ppVal' , ), 11051, (11051, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SecondPoint' , 'ppVal' , ), 11052, (11052, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'pVal' , ), 11053, (11053, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'pVal' , ), 11053, (11053, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'HorizontalRadiusOfSection' , 'ppVal' , ), 11054, (11054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'VerticalRadiusOfSection' , 'ppVal' , ), 11055, (11055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'MeanCoilRadius' , 'ppVal' , ), 11056, (11056, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'SolidHeight' , 'ppVal' , ), 11057, (11057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'FreeLength' , 'ppVal' , ), 11058, (11058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 11059, (11059, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 11059, (11059, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'SpringProperty' , 'ppVal' , ), 11060, (11060, (), [ (16393, 10, None, "IID('{7A99C466-6C65-4914-A397-BB4FF286C8B9}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'CoilClash' , 'ppVal' , ), 11061, (11061, (), [ (16393, 10, None, "IID('{F1E65DC1-6537-4755-95CE-87512C867DB8}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeACoilClash_vtables_dispatch_ = 1
IMMSGroupTypeACoilClash_vtables_ = [
	(( 'Stiffness' , 'pVal' , ), 11001, (11001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'pVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Damping' , 'pVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PenetrationDepth' , 'ppVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeASpringProperty_vtables_dispatch_ = 1
IMMSGroupTypeASpringProperty_vtables_ = [
	(( 'Material' , 'pVal' , ), 11001, (11001, (), [ (3, 1, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'pVal' , ), 11001, (11001, (), [ (16387, 10, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCalcShearModulus' , 'pVal' , ), 11002, (11002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCalcShearModulus' , 'pVal' , ), 11002, (11002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulus' , 'pVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCalcTSDAStiffness' , 'pVal' , ), 11004, (11004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCalcTSDAStiffness' , 'pVal' , ), 11004, (11004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Damping' , 'ppVal' , ), 11005, (11005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Stiffness' , 'ppVal' , ), 11006, (11006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeB_vtables_dispatch_ = 1
IMMSGroupTypeB_vtables_ = [
	(( 'FirstPoint' , 'ppVal' , ), 11051, (11051, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'pVal' , ), 11052, (11052, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'pVal' , ), 11052, (11052, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'pVal' , ), 11053, (11053, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'pVal' , ), 11053, (11053, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'FreeLength' , 'ppVal' , ), 11054, (11054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'InstalledLength' , 'ppVal' , ), 11055, (11055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'InactiveCoils' , 'ppVal' , ), 11056, (11056, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 11057, (11057, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 11057, (11057, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SpringProperty' , 'ppVal' , ), 11058, (11058, (), [ (16393, 10, None, "IID('{3A657711-810D-47EE-BF91-27F7B0A1C579}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'SkeletonProfile' , 'ppVal' , ), 11059, (11059, (), [ (16393, 10, None, "IID('{C0487899-3698-44DE-AD71-05A3C5D8EF8C}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'WireProfile' , 'ppVal' , ), 11060, (11060, (), [ (16393, 10, None, "IID('{C8CAFFBB-25E4-40DB-9405-F14E39BD2A83}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeBSkeletonProfile_vtables_dispatch_ = 1
IMMSGroupTypeBSkeletonProfile_vtables_ = [
	(( 'SkeletonProfileType' , 'pVal' , ), 11001, (11001, (), [ (16387, 10, None, "IID('{1616B733-CBF9-4070-AC39-D70D8084103B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SetSkeletonProfile' , 'nIndex' , 'pSafeArray' , ), 11002, (11002, (), [ (19, 1, None, None) , 
			 (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetSkeletonProfile' , 'nIndex' , 'ppSafeArray' , ), 11003, (11003, (), [ (19, 1, None, None) , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetSizeSkeletonProfile' , 'nSize' , ), 11004, (11004, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SkeletonProfileFileName' , 'pVal' , ), 11005, (11005, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SkeletonProfileFileName' , 'pVal' , ), 11005, (11005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ImportSkeletonProfile' , 'strFileName' , ), 11006, (11006, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ExportSkeletonProfile' , 'strFileName' , ), 11007, (11007, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeBSpringProperty_vtables_dispatch_ = 1
IMMSGroupTypeBSpringProperty_vtables_ = [
	(( 'TotalMass' , 'pVal' , ), 11001, (11001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulus' , 'pVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FreeDamping' , 'pVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BlockDamping' , 'ppVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 11005, (11005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeBWireProfile_vtables_dispatch_ = 1
IMMSGroupTypeBWireProfile_vtables_ = [
	(( 'WireProfileType' , 'pVal' , ), 11001, (11001, (), [ (16387, 10, None, "IID('{1616B733-CBF9-4070-AC39-D70D8084103B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SetWireProfile' , 'nIndex' , 'pSafeArray' , ), 11002, (11002, (), [ (19, 1, None, None) , 
			 (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GetWireProfile' , 'nIndex' , 'ppSafeArray' , ), 11003, (11003, (), [ (19, 1, None, None) , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GetSizeWireProfile' , 'nSize' , ), 11004, (11004, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'WireProfileFileName' , 'pVal' , ), 11005, (11005, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'WireProfileFileName' , 'pVal' , ), 11005, (11005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ImportWireProfile' , 'strFileName' , ), 11006, (11006, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ExportWireProfile' , 'strFileName' , ), 11007, (11007, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'HorizontalRadius' , 'ppVal' , ), 11008, (11008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'VerticalRadius' , 'ppVal' , ), 11009, (11009, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NumOfSegments' , 'ppVal' , ), 11010, (11010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeC_vtables_dispatch_ = 1
IMMSGroupTypeC_vtables_ = [
	(( 'SpringType' , 'pVal' , ), 11051, (11051, (), [ (3, 1, None, "IID('{E1A446BD-4BDF-41B1-B9FB-648CD06C57BA}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SpringType' , 'pVal' , ), 11051, (11051, (), [ (16387, 10, None, "IID('{E1A446BD-4BDF-41B1-B9FB-648CD06C57BA}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'SpringDiameter' , 'ppVal' , ), 11052, (11052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'WireDiameter' , 'ppVal' , ), 11053, (11053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RatioOfDiameter' , 'ppVal' , ), 11054, (11054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'FreeLength' , 'ppVal' , ), 11055, (11055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'SetupLength' , 'ppVal' , ), 11056, (11056, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'NumOfWindingForSeatContactPart' , 'ppVal' , ), 11057, (11057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'NumOfWindingForLowPitchPart' , 'ppVal' , ), 11058, (11058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'NumOfWindingForHighPitchPart' , 'ppVal' , ), 11059, (11059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SpringProperty' , 'ppVal' , ), 11060, (11060, (), [ (16393, 10, None, "IID('{4ED0F6FA-42EA-4CEB-857B-96B5B2EB28CC}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseSimpleGraphic' , 'pVal' , ), 11061, (11061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseSimpleGraphic' , 'pVal' , ), 11061, (11061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'BaseMarker' , 'ppVal' , ), 11062, (11062, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'BaseMarker' , 'ppVal' , ), 11062, (11062, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ActionMarker' , 'ppVal' , ), 11063, (11063, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ActionMarker' , 'ppVal' , ), 11063, (11063, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'CopyBaseToAction' , 'type' , ), 11064, (11064, (), [ (3, 1, None, "IID('{2F145D21-8E9A-44D4-9BAC-1EFBCB32570B}')") , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'CopyActionToBase' , 'type' , ), 11065, (11065, (), [ (3, 1, None, "IID('{2F145D21-8E9A-44D4-9BAC-1EFBCB32570B}')") , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 11066, (11066, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 11066, (11066, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeCSpringProperty_vtables_dispatch_ = 1
IMMSGroupTypeCSpringProperty_vtables_ = [
	(( 'YoungsModulus' , 'pVal' , ), 11001, (11001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulus' , 'pVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DampingRatio' , 'ppVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeD_vtables_dispatch_ = 1
IMMSGroupTypeD_vtables_ = [
	(( 'FirstPoint' , 'ppVal' , ), 11051, (11051, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SecondPoint' , 'ppVal' , ), 11052, (11052, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'pVal' , ), 11053, (11053, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'pVal' , ), 11053, (11053, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateContactProperty' , 'pVal' , ), 11054, (11054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateContactProperty' , 'pVal' , ), 11054, (11054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseBeamForceDisplay' , 'pVal' , ), 11055, (11055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseBeamForceDisplay' , 'pVal' , ), 11055, (11055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCalculationBEAMProperty' , 'pVal' , ), 11056, (11056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCalculationBEAMProperty' , 'pVal' , ), 11056, (11056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 11057, (11057, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 11057, (11057, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ContactProperty' , 'ppVal' , ), 11058, (11058, (), [ (16393, 10, None, "IID('{47D76536-2593-45BB-A395-7F3172FEFE73}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'ppVal' , ), 11059, (11059, (), [ (16393, 10, None, "IID('{C9DF98FE-41B7-4E04-B011-F22647D193EC}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 11060, (11060, (), [ (16393, 10, None, "IID('{8511DE02-96EB-46A6-BFEF-4ED5B3008310}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveAllContacts' , 'pVal' , ), 11061, (11061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveAllContacts' , 'pVal' , ), 11061, (11061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeDContactFriction_vtables_dispatch_ = 1
IMMSGroupTypeDContactFriction_vtables_ = [
	(( 'ContactFrictionType' , 'ContactFrictionType' , ), 11001, (11001, (), [ (3, 1, None, "IID('{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ContactFrictionType' , 'ContactFrictionType' , ), 11001, (11001, (), [ (16387, 10, None, "IID('{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Coefficient' , 'ppVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Spline' , 'ppVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Spline' , 'ppVal' , ), 11003, (11003, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'StaticThresholdVelocity' , 'ppVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DynamicThresholdVelocity' , 'ppVal' , ), 11005, (11005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StaticCoefficient' , 'ppVal' , ), 11006, (11006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'MaximumForce' , 'ppVal' , ), 11007, (11007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumForce' , 'pVal' , ), 11008, (11008, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumForce' , 'pVal' , ), 11008, (11008, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeDContactProperty_vtables_dispatch_ = 1
IMMSGroupTypeDContactProperty_vtables_ = [
	(( 'StiffnessCoefficient' , 'ppVal' , ), 11001, (11001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 11002, (11002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 11002, (11002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 11003, (11003, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 11005, (11005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 11005, (11005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 11006, (11006, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 11006, (11006, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 11007, (11007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 11007, (11007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 11008, (11008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 11009, (11009, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 11009, (11009, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 11010, (11010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 11011, (11011, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 11011, (11011, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 11012, (11012, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Friction' , 'ppVal' , ), 11013, (11013, (), [ (16393, 10, None, "IID('{0A109CF4-FF09-40DA-B076-EA8E0BD207FD}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UseUserSubroutine' , 'pVal' , ), 11014, (11014, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseUserSubroutine' , 'pVal' , ), 11014, (11014, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'ppVal' , ), 11015, (11015, (), [ (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'ppVal' , ), 11015, (11015, (), [ (16393, 10, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'BufferRadiusFactor' , 'ppVal' , ), 11016, (11016, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'MaxStepSizeFactor' , 'ppVal' , ), 11017, (11017, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 11018, (11018, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 11018, (11018, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeDGeometry_vtables_dispatch_ = 1
IMMSGroupTypeDGeometry_vtables_ = [
	(( 'CrossSectionType' , 'pVal' , ), 11001, (11001, (), [ (3, 1, None, "IID('{47916431-C6E6-4880-B7AD-7E114B5BFE1C}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'CrossSectionType' , 'pVal' , ), 11001, (11001, (), [ (16387, 10, None, "IID('{47916431-C6E6-4880-B7AD-7E114B5BFE1C}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DirectionHelixType' , 'pVal' , ), 11002, (11002, (), [ (3, 1, None, "IID('{181F3A0D-D841-4783-8F0D-25CEC6EBEE20}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DirectionHelixType' , 'pVal' , ), 11002, (11002, (), [ (16387, 10, None, "IID('{181F3A0D-D841-4783-8F0D-25CEC6EBEE20}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'pVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Exponent' , 'pVal' , ), 11005, (11005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Diameter' , 'pVal' , ), 11006, (11006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'InsideDiameter' , 'pVal' , ), 11007, (11007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'EffectiveNoOfHelix' , 'pVal' , ), 11008, (11008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseProfile' , 'pVal' , ), 11009, (11009, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseProfile' , 'pVal' , ), 11009, (11009, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PitchAngleInBDivision' , 'pVal' , ), 11010, (11010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NoOfHelixInBDivision' , 'pVal' , ), 11011, (11011, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ThicknessOfAEdgeGap' , 'pVal' , ), 11012, (11012, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ThicknessOfBEdgeGap' , 'pVal' , ), 11013, (11013, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SplineInterpolationCoefficient1' , 'pVal' , ), 11014, (11014, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SplineInterpolationCoefficient2' , 'pVal' , ), 11015, (11015, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SplineInterpolationCoefficient3' , 'pVal' , ), 11016, (11016, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CenterLineProfileType' , 'pVal' , ), 11017, (11017, (), [ (16387, 10, None, "IID('{1616B733-CBF9-4070-AC39-D70D8084103B}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AddCenterLineProfile' , 'pSafeArray' , ), 11018, (11018, (), [ (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'DeleteCenterLineProfile' , 'nIndex' , ), 11019, (11019, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'DeleteAllCenterLineProfile' , ), 11020, (11020, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SetCenterLineProfile' , 'nIndex' , 'pSafeArray' , ), 11021, (11021, (), [ (19, 1, None, None) , 
			 (8197, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetCenterLineProfile' , 'nIndex' , 'ppSafeArray' , ), 11022, (11022, (), [ (19, 1, None, None) , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetSizeCenterLineProfile' , 'nSize' , ), 11023, (11023, (), [ (16403, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CenterLineProfileFileName' , 'pVal' , ), 11024, (11024, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CenterLineProfileFileName' , 'pVal' , ), 11024, (11024, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ImportCenterLineProfile' , 'strFileName' , ), 11025, (11025, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ExportCenterLineProfile' , 'strFileName' , ), 11026, (11026, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IMMSGroupTypeDMaterial_vtables_dispatch_ = 1
IMMSGroupTypeDMaterial_vtables_ = [
	(( 'TotalMass' , 'pVal' , ), 11001, (11001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus' , 'pVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PoissonRatio' , 'ppVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulus' , 'pVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingMatrix' , 'pVal' , ), 11005, (11005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingMatrix' , 'pVal' , ), 11005, (11005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DampingMatrix' , 'i' , 'j' , 'ppVal' , ), 11006, (11006, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'DampingRatio' , 'ppVal' , ), 11007, (11007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IMMSIOTypeD_vtables_dispatch_ = 1
IMMSIOTypeD_vtables_ = [
	(( 'BaseSpringGroup' , 'ppVal' , ), 11001, (11001, (), [ (9, 1, None, "IID('{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'BaseSpringGroup' , 'ppVal' , ), 11001, (11001, (), [ (16393, 10, None, "IID('{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ActionSpringGroup' , 'ppVal' , ), 11002, (11002, (), [ (9, 1, None, "IID('{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')") , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ActionSpringGroup' , 'ppVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

IMMSToolkit_vtables_dispatch_ = 1
IMMSToolkit_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 11051, (11051, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreateMMSGroupTypeA' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'dActiveCoil' , 
			 'numSegment' , 'ppResult' , ), 11052, (11052, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (5, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{7101723B-18D0-4B5A-8298-A0243B1815F4}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CreateMMSGroupTypeB' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'numSegment' , 
			 'ppResult' , ), 11053, (11053, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , 
			 (19, 1, None, None) , (16393, 10, None, "IID('{43A3CDF3-CF97-4C22-B8B8-33F63EFBCE05}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CreateMMSGroupTypeC' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pBaseOriginPoint' , 
			 'pActionOriginPoint' , 'ppResult' , ), 11054, (11054, (), [ (8, 1, None, None) , (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , 
			 (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , (8197, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{FA1C1DD1-7A02-499A-88C2-49565A037C3E}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateMMSGroupTypeD' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'dHelix' , 
			 'numSegment' , 'ppResult' , ), 11055, (11055, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (5, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateMMSIOTypeD' , 'strName' , 'pOuterGroup' , 'pInnerGroup' , 'ppResult' , 
			 ), 11056, (11056, (), [ (8, 1, None, None) , (9, 1, None, "IID('{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')") , (9, 1, None, "IID('{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')") , (16393, 10, None, "IID('{436E38BE-FFA6-4E99-AAE9-133B6E3A66EB}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateMMSGroupTypeD2' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'dHelix' , 
			 'dEffectiveHelix' , 'numSegment' , 'ppResult' , ), 11057, (11057, (), [ (8, 1, None, None) , 
			 (8197, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (19, 1, None, None) , 
			 (16393, 10, None, "IID('{F6D5A583-7A62-4112-8BF3-BB69C99A0406}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{7A99C466-6C65-4914-A397-BB4FF286C8B9}' : IMMSGroupTypeASpringProperty,
	'{F1E65DC1-6537-4755-95CE-87512C867DB8}' : IMMSGroupTypeACoilClash,
	'{3A657711-810D-47EE-BF91-27F7B0A1C579}' : IMMSGroupTypeBSpringProperty,
	'{C0487899-3698-44DE-AD71-05A3C5D8EF8C}' : IMMSGroupTypeBSkeletonProfile,
	'{C8CAFFBB-25E4-40DB-9405-F14E39BD2A83}' : IMMSGroupTypeBWireProfile,
	'{4ED0F6FA-42EA-4CEB-857B-96B5B2EB28CC}' : IMMSGroupTypeCSpringProperty,
	'{0A109CF4-FF09-40DA-B076-EA8E0BD207FD}' : IMMSGroupTypeDContactFriction,
	'{47D76536-2593-45BB-A395-7F3172FEFE73}' : IMMSGroupTypeDContactProperty,
	'{C9DF98FE-41B7-4E04-B011-F22647D193EC}' : IMMSGroupTypeDMaterial,
	'{8511DE02-96EB-46A6-BFEF-4ED5B3008310}' : IMMSGroupTypeDGeometry,
	'{BA66ACB4-A495-47FE-8F6F-25C7A5ED6D18}' : IMMSGroup,
	'{7101723B-18D0-4B5A-8298-A0243B1815F4}' : IMMSGroupTypeA,
	'{43A3CDF3-CF97-4C22-B8B8-33F63EFBCE05}' : IMMSGroupTypeB,
	'{FA1C1DD1-7A02-499A-88C2-49565A037C3E}' : IMMSGroupTypeC,
	'{F6D5A583-7A62-4112-8BF3-BB69C99A0406}' : IMMSGroupTypeD,
	'{436E38BE-FFA6-4E99-AAE9-133B6E3A66EB}' : IMMSIOTypeD,
	'{CF0E6EBB-7784-4445-B2B2-A5948BF68CF8}' : IMMSToolkit,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{7A99C466-6C65-4914-A397-BB4FF286C8B9}' : 'IMMSGroupTypeASpringProperty',
	'{F1E65DC1-6537-4755-95CE-87512C867DB8}' : 'IMMSGroupTypeACoilClash',
	'{3A657711-810D-47EE-BF91-27F7B0A1C579}' : 'IMMSGroupTypeBSpringProperty',
	'{C0487899-3698-44DE-AD71-05A3C5D8EF8C}' : 'IMMSGroupTypeBSkeletonProfile',
	'{C8CAFFBB-25E4-40DB-9405-F14E39BD2A83}' : 'IMMSGroupTypeBWireProfile',
	'{4ED0F6FA-42EA-4CEB-857B-96B5B2EB28CC}' : 'IMMSGroupTypeCSpringProperty',
	'{0A109CF4-FF09-40DA-B076-EA8E0BD207FD}' : 'IMMSGroupTypeDContactFriction',
	'{47D76536-2593-45BB-A395-7F3172FEFE73}' : 'IMMSGroupTypeDContactProperty',
	'{C9DF98FE-41B7-4E04-B011-F22647D193EC}' : 'IMMSGroupTypeDMaterial',
	'{8511DE02-96EB-46A6-BFEF-4ED5B3008310}' : 'IMMSGroupTypeDGeometry',
	'{BA66ACB4-A495-47FE-8F6F-25C7A5ED6D18}' : 'IMMSGroup',
	'{7101723B-18D0-4B5A-8298-A0243B1815F4}' : 'IMMSGroupTypeA',
	'{43A3CDF3-CF97-4C22-B8B8-33F63EFBCE05}' : 'IMMSGroupTypeB',
	'{FA1C1DD1-7A02-499A-88C2-49565A037C3E}' : 'IMMSGroupTypeC',
	'{F6D5A583-7A62-4112-8BF3-BB69C99A0406}' : 'IMMSGroupTypeD',
	'{436E38BE-FFA6-4E99-AAE9-133B6E3A66EB}' : 'IMMSIOTypeD',
	'{CF0E6EBB-7784-4445-B2B2-A5948BF68CF8}' : 'IMMSToolkit',
}


NamesToIIDMap = {
	'IMMSGroupTypeASpringProperty' : '{7A99C466-6C65-4914-A397-BB4FF286C8B9}',
	'IMMSGroupTypeACoilClash' : '{F1E65DC1-6537-4755-95CE-87512C867DB8}',
	'IMMSGroupTypeBSpringProperty' : '{3A657711-810D-47EE-BF91-27F7B0A1C579}',
	'IMMSGroupTypeBSkeletonProfile' : '{C0487899-3698-44DE-AD71-05A3C5D8EF8C}',
	'IMMSGroupTypeBWireProfile' : '{C8CAFFBB-25E4-40DB-9405-F14E39BD2A83}',
	'IMMSGroupTypeCSpringProperty' : '{4ED0F6FA-42EA-4CEB-857B-96B5B2EB28CC}',
	'IMMSGroupTypeDContactFriction' : '{0A109CF4-FF09-40DA-B076-EA8E0BD207FD}',
	'IMMSGroupTypeDContactProperty' : '{47D76536-2593-45BB-A395-7F3172FEFE73}',
	'IMMSGroupTypeDMaterial' : '{C9DF98FE-41B7-4E04-B011-F22647D193EC}',
	'IMMSGroupTypeDGeometry' : '{8511DE02-96EB-46A6-BFEF-4ED5B3008310}',
	'IMMSGroup' : '{BA66ACB4-A495-47FE-8F6F-25C7A5ED6D18}',
	'IMMSGroupTypeA' : '{7101723B-18D0-4B5A-8298-A0243B1815F4}',
	'IMMSGroupTypeB' : '{43A3CDF3-CF97-4C22-B8B8-33F63EFBCE05}',
	'IMMSGroupTypeC' : '{FA1C1DD1-7A02-499A-88C2-49565A037C3E}',
	'IMMSGroupTypeD' : '{F6D5A583-7A62-4112-8BF3-BB69C99A0406}',
	'IMMSIOTypeD' : '{436E38BE-FFA6-4E99-AAE9-133B6E3A66EB}',
	'IMMSToolkit' : '{CF0E6EBB-7784-4445-B2B2-A5948BF68CF8}',
}


