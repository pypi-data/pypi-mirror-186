# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMMTT2D.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5 RecurDynCOMMTT2D Type Library'
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

CLSID = IID('{D292C294-1466-4CB6-B540-B15BB41B218D}')
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
class GuideVelocityType(IntEnum):
	'''
	GuideVelocityType enumeration.
	'''
	GuideVelocityType_Constant    =0         
	'''Constant value is 0.'''
	GuideVelocityType_Expression  =1         
	'''Constant value is 1.'''
class MTT2DFrictionType(IntEnum):
	'''
	MTT2DFrictionType enumeration.
	'''
	Linear                        =1         
	'''Constant value is 1.'''
	Step                          =0         
	'''Constant value is 0.'''
class MovableRollerDirectionType(IntEnum):
	'''
	MovableRollerDirectionType enumeration.
	'''
	MovableRollerDirectionType_Angle=2         
	'''Constant value is 2.'''
	MovableRollerDirectionType_Point=1         
	'''Constant value is 1.'''
class RollerBodyType(IntEnum):
	'''
	RollerBodyType enumeration.
	'''
	RollerBodyType_Flexible       =1         
	'''Constant value is 1.'''
	RollerBodyType_Rigid          =0         
	'''Constant value is 0.'''

from win32com.client import DispatchBaseClass
class IMTT2DAssembly(DispatchBaseClass):
	'''MTT2D assembly'''
	CLSID = IID('{24C00315-36B5-498A-99A5-A3D3074E24DF}')
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
		return self._oleobj_.InvokeTypes(1052, LCID, 1, (11, 0), ((8, 1),),pVal
			)


	def GetContactedSheet(self, pVal):
		'''
		Get a contacted sheet
		
		:param pVal: str
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(1054, LCID, 1, (11, 0), ((8, 1),),pVal
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
		return self._oleobj_.InvokeTypes(1051, LCID, 1, (11, 0), ((8, 1), (11, 1)),pVal
			, vBool)


	def SetContactedSheet(self, pVal, vBool):
		'''
		Set a contacted sheet
		
		:param pVal: str
		:param vBool: bool
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(1053, LCID, 1, (11, 0), ((8, 1), (11, 1)),pVal
			, vBool)


	def _get_BufferRadiusFactor(self):
		return self._ApplyTypes_(*(1058, 2, (9, 0), (), "BufferRadiusFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_MaximumNoOfSheetSegments(self):
		return self._ApplyTypes_(*(1064, 2, (3, 0), (), "MaximumNoOfSheetSegments", None))
	def _get_MaximumStepsizeFactor(self):
		return self._ApplyTypes_(*(1059, 2, (9, 0), (), "MaximumStepsizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PenetrationParameter(self):
		return self._ApplyTypes_(*(1060, 2, (9, 0), (), "PenetrationParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ReferencePosition(self):
		return self._ApplyTypes_(*(1056, 2, (9, 0), (), "ReferencePosition", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_Resolution(self):
		return self._ApplyTypes_(*(1062, 2, (8197, 0), (), "Resolution", None))
	def _get_SizeOfBoundary(self):
		return self._ApplyTypes_(*(1057, 2, (8197, 0), (), "SizeOfBoundary", None))
	def _get_UseMaximumNoOfSheetSegments(self):
		return self._ApplyTypes_(*(1063, 2, (11, 0), (), "UseMaximumNoOfSheetSegments", None))
	def _get_UseResolution(self):
		return self._ApplyTypes_(*(1061, 2, (11, 0), (), "UseResolution", None))
	def _get_UseSystemBoundary(self):
		return self._ApplyTypes_(*(1055, 2, (11, 0), (), "UseSystemBoundary", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_MaximumNoOfSheetSegments(self, value):
		if "MaximumNoOfSheetSegments" in self.__dict__: self.__dict__["MaximumNoOfSheetSegments"] = value; return
		self._oleobj_.Invoke(*((1064, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Resolution(self, value):
		if "Resolution" in self.__dict__: self.__dict__["Resolution"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1062, LCID, 4, 0) + (variantValue,) + ()))
	def _set_SizeOfBoundary(self, value):
		if "SizeOfBoundary" in self.__dict__: self.__dict__["SizeOfBoundary"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1057, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseMaximumNoOfSheetSegments(self, value):
		if "UseMaximumNoOfSheetSegments" in self.__dict__: self.__dict__["UseMaximumNoOfSheetSegments"] = value; return
		self._oleobj_.Invoke(*((1063, LCID, 4, 0) + (value,) + ()))
	def _set_UseResolution(self, value):
		if "UseResolution" in self.__dict__: self.__dict__["UseResolution"] = value; return
		self._oleobj_.Invoke(*((1061, LCID, 4, 0) + (value,) + ()))
	def _set_UseSystemBoundary(self, value):
		if "UseSystemBoundary" in self.__dict__: self.__dict__["UseSystemBoundary"] = value; return
		self._oleobj_.Invoke(*((1055, LCID, 4, 0) + (value,) + ()))
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
	MaximumNoOfSheetSegments = property(_get_MaximumNoOfSheetSegments, _set_MaximumNoOfSheetSegments)
	'''
	Maximum number of sheet's segments

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
	UseMaximumNoOfSheetSegments = property(_get_UseMaximumNoOfSheetSegments, _set_UseMaximumNoOfSheetSegments)
	'''
	Use maximum number of sheet's segments

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
		"_set_MaximumNoOfSheetSegments": _set_MaximumNoOfSheetSegments,
		"_set_Name": _set_Name,
		"_set_Resolution": _set_Resolution,
		"_set_SizeOfBoundary": _set_SizeOfBoundary,
		"_set_UseMaximumNoOfSheetSegments": _set_UseMaximumNoOfSheetSegments,
		"_set_UseResolution": _set_UseResolution,
		"_set_UseSystemBoundary": _set_UseSystemBoundary,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BufferRadiusFactor": (1058, 2, (9, 0), (), "BufferRadiusFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"MaximumNoOfSheetSegments": (1064, 2, (3, 0), (), "MaximumNoOfSheetSegments", None),
		"MaximumStepsizeFactor": (1059, 2, (9, 0), (), "MaximumStepsizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PenetrationParameter": (1060, 2, (9, 0), (), "PenetrationParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ReferencePosition": (1056, 2, (9, 0), (), "ReferencePosition", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"Resolution": (1062, 2, (8197, 0), (), "Resolution", None),
		"SizeOfBoundary": (1057, 2, (8197, 0), (), "SizeOfBoundary", None),
		"UseMaximumNoOfSheetSegments": (1063, 2, (11, 0), (), "UseMaximumNoOfSheetSegments", None),
		"UseResolution": (1061, 2, (11, 0), (), "UseResolution", None),
		"UseSystemBoundary": (1055, 2, (11, 0), (), "UseSystemBoundary", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"MaximumNoOfSheetSegments": ((1064, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Resolution": ((1062, LCID, 4, 0),()),
		"SizeOfBoundary": ((1057, LCID, 4, 0),()),
		"UseMaximumNoOfSheetSegments": ((1063, LCID, 4, 0),()),
		"UseResolution": ((1061, LCID, 4, 0),()),
		"UseSystemBoundary": ((1055, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DContactProperty(DispatchBaseClass):
	'''MTT2D contact property'''
	CLSID = IID('{3641A1D2-6FCC-40AA-A4AA-8176CF6C755E}')
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
		return self._ApplyTypes_(*(1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(1024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(1025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(1015, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((1022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((1023, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((1024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((1018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((1020, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((1019, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((1017, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((1015, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((1016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((1021, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT2D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT2D.MTT2DFrictionType
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
		"BoundaryPenetration": (1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'),
		"FrictionCoefficient": (1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'),
		"IndentationExponent": (1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseRDF": (1024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (1025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (1015, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((1022, LCID, 4, 0),()),
		"FrictionType": ((1023, LCID, 4, 0),()),
		"UseRDF": ((1024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((1018, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((1020, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((1019, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((1017, LCID, 4, 0),()),
		"UseSpecialRDF": ((1025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((1015, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((1016, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((1021, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DContactPropertyGuide(DispatchBaseClass):
	'''MTT2D guide contact property'''
	CLSID = IID('{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}')
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
		return self._ApplyTypes_(*(1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'))
	def _get_GuideTolerance(self):
		return self._ApplyTypes_(*(1103, 2, (9, 0), (), "GuideTolerance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_GuideVelocity(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "GuideVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_GuideVelocityExpression(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "GuideVelocityExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_GuideVelocityType(self):
		return self._ApplyTypes_(*(1052, 2, (3, 0), (), "GuideVelocityType", '{E92AC4EA-B94E-47DB-A4DD-39C954D07299}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialGuideTolerance(self):
		return self._ApplyTypes_(*(1104, 2, (9, 0), (), "SpecialGuideTolerance", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseGuideTolerance(self):
		return self._ApplyTypes_(*(1101, 2, (11, 0), (), "UseGuideTolerance", None))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(1024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialGuideTolerance(self):
		return self._ApplyTypes_(*(1102, 2, (11, 0), (), "UseSpecialGuideTolerance", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(1025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(1015, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((1022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((1023, LCID, 4, 0) + (value,) + ()))
	def _set_GuideVelocityExpression(self, value):
		if "GuideVelocityExpression" in self.__dict__: self.__dict__["GuideVelocityExpression"] = value; return
		self._oleobj_.Invoke(*((1053, LCID, 4, 0) + (value,) + ()))
	def _set_GuideVelocityType(self, value):
		if "GuideVelocityType" in self.__dict__: self.__dict__["GuideVelocityType"] = value; return
		self._oleobj_.Invoke(*((1052, LCID, 4, 0) + (value,) + ()))
	def _set_UseGuideTolerance(self, value):
		if "UseGuideTolerance" in self.__dict__: self.__dict__["UseGuideTolerance"] = value; return
		self._oleobj_.Invoke(*((1101, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((1024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((1018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((1020, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialGuideTolerance(self, value):
		if "UseSpecialGuideTolerance" in self.__dict__: self.__dict__["UseSpecialGuideTolerance"] = value; return
		self._oleobj_.Invoke(*((1102, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((1019, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((1017, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((1015, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((1016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((1021, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT2D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT2D.MTT2DFrictionType
	'''
	GuideTolerance = property(_get_GuideTolerance, None)
	'''
	Guide tolerance

	:type: recurdyn.ProcessNet.IDouble
	'''
	GuideVelocity = property(_get_GuideVelocity, None)
	'''
	Guide velocity constant value

	:type: recurdyn.ProcessNet.IDouble
	'''
	GuideVelocityExpression = property(_get_GuideVelocityExpression, _set_GuideVelocityExpression)
	'''
	Guide velocity expression

	:type: recurdyn.ProcessNet.IExpression
	'''
	GuideVelocityType = property(_get_GuideVelocityType, _set_GuideVelocityType)
	'''
	Guide velocity type

	:type: recurdyn.MTT2D.GuideVelocityType
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
	SpecialGuideTolerance = property(_get_SpecialGuideTolerance, None)
	'''
	Special guide tolerance

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
	UseGuideTolerance = property(_get_UseGuideTolerance, _set_UseGuideTolerance)
	'''
	Use guide tolerance

	:type: bool
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
	UseSpecialGuideTolerance = property(_get_UseSpecialGuideTolerance, _set_UseSpecialGuideTolerance)
	'''
	Use special guide tolerance

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
		"_set_GuideVelocityExpression": _set_GuideVelocityExpression,
		"_set_GuideVelocityType": _set_GuideVelocityType,
		"_set_UseGuideTolerance": _set_UseGuideTolerance,
		"_set_UseRDF": _set_UseRDF,
		"_set_UseSpecialBoundaryPenetration": _set_UseSpecialBoundaryPenetration,
		"_set_UseSpecialFrictionCoefficient": _set_UseSpecialFrictionCoefficient,
		"_set_UseSpecialGuideTolerance": _set_UseSpecialGuideTolerance,
		"_set_UseSpecialIndentationExponent": _set_UseSpecialIndentationExponent,
		"_set_UseSpecialMaximumDamping": _set_UseSpecialMaximumDamping,
		"_set_UseSpecialRDF": _set_UseSpecialRDF,
		"_set_UseSpecialStiffness": _set_UseSpecialStiffness,
		"_set_UseSpecialStiffnessExponent": _set_UseSpecialStiffnessExponent,
		"_set_UseSpecialThresholdVelocity": _set_UseSpecialThresholdVelocity,
	}
	_prop_map_get_ = {
		"BoundaryPenetration": (1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'),
		"FrictionCoefficient": (1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'),
		"GuideTolerance": (1103, 2, (9, 0), (), "GuideTolerance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"GuideVelocity": (1051, 2, (9, 0), (), "GuideVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"GuideVelocityExpression": (1053, 2, (9, 0), (), "GuideVelocityExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"GuideVelocityType": (1052, 2, (3, 0), (), "GuideVelocityType", '{E92AC4EA-B94E-47DB-A4DD-39C954D07299}'),
		"IndentationExponent": (1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialGuideTolerance": (1104, 2, (9, 0), (), "SpecialGuideTolerance", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseGuideTolerance": (1101, 2, (11, 0), (), "UseGuideTolerance", None),
		"UseRDF": (1024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialGuideTolerance": (1102, 2, (11, 0), (), "UseSpecialGuideTolerance", None),
		"UseSpecialIndentationExponent": (1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (1025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (1015, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((1022, LCID, 4, 0),()),
		"FrictionType": ((1023, LCID, 4, 0),()),
		"GuideVelocityExpression": ((1053, LCID, 4, 0),()),
		"GuideVelocityType": ((1052, LCID, 4, 0),()),
		"UseGuideTolerance": ((1101, LCID, 4, 0),()),
		"UseRDF": ((1024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((1018, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((1020, LCID, 4, 0),()),
		"UseSpecialGuideTolerance": ((1102, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((1019, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((1017, LCID, 4, 0),()),
		"UseSpecialRDF": ((1025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((1015, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((1016, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((1021, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DContactPropertyPGuide(DispatchBaseClass):
	'''MTT2D circular guide contact property'''
	CLSID = IID('{B4F3A991-0483-415B-820F-A8B4116A3C9A}')
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
		return self._ApplyTypes_(*(1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'))
	def _get_GuideVelocity(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "GuideVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_GuideVelocityExpression(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "GuideVelocityExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_GuideVelocityType(self):
		return self._ApplyTypes_(*(1052, 2, (3, 0), (), "GuideVelocityType", '{E92AC4EA-B94E-47DB-A4DD-39C954D07299}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(1024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(1025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(1015, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((1022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((1023, LCID, 4, 0) + (value,) + ()))
	def _set_GuideVelocityExpression(self, value):
		if "GuideVelocityExpression" in self.__dict__: self.__dict__["GuideVelocityExpression"] = value; return
		self._oleobj_.Invoke(*((1053, LCID, 4, 0) + (value,) + ()))
	def _set_GuideVelocityType(self, value):
		if "GuideVelocityType" in self.__dict__: self.__dict__["GuideVelocityType"] = value; return
		self._oleobj_.Invoke(*((1052, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((1024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((1018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((1020, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((1019, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((1017, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((1015, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((1016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((1021, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT2D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT2D.MTT2DFrictionType
	'''
	GuideVelocity = property(_get_GuideVelocity, None)
	'''
	Guide velocity constant value

	:type: recurdyn.ProcessNet.IDouble
	'''
	GuideVelocityExpression = property(_get_GuideVelocityExpression, _set_GuideVelocityExpression)
	'''
	Guide velocity expression

	:type: recurdyn.ProcessNet.IExpression
	'''
	GuideVelocityType = property(_get_GuideVelocityType, _set_GuideVelocityType)
	'''
	Guide velocity type

	:type: recurdyn.MTT2D.GuideVelocityType
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
		"_set_GuideVelocityExpression": _set_GuideVelocityExpression,
		"_set_GuideVelocityType": _set_GuideVelocityType,
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
		"BoundaryPenetration": (1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'),
		"FrictionCoefficient": (1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'),
		"GuideVelocity": (1051, 2, (9, 0), (), "GuideVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"GuideVelocityExpression": (1053, 2, (9, 0), (), "GuideVelocityExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"GuideVelocityType": (1052, 2, (3, 0), (), "GuideVelocityType", '{E92AC4EA-B94E-47DB-A4DD-39C954D07299}'),
		"IndentationExponent": (1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseRDF": (1024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (1025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (1015, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((1022, LCID, 4, 0),()),
		"FrictionType": ((1023, LCID, 4, 0),()),
		"GuideVelocityExpression": ((1053, LCID, 4, 0),()),
		"GuideVelocityType": ((1052, LCID, 4, 0),()),
		"UseRDF": ((1024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((1018, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((1020, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((1019, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((1017, LCID, 4, 0),()),
		"UseSpecialRDF": ((1025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((1015, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((1016, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((1021, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DContactPropertyRoller(DispatchBaseClass):
	'''MTT2D contact property'''
	CLSID = IID('{5FC1140C-915D-4378-A514-4E5D374B9D29}')
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
		return self._ApplyTypes_(*(1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaxStictionDeformation(self):
		return self._ApplyTypes_(*(1052, 2, (9, 0), (), "MaxStictionDeformation", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseMaxStictionDeformation(self):
		return self._ApplyTypes_(*(1051, 2, (11, 0), (), "UseMaxStictionDeformation", None))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(1024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(1025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(1015, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((1022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((1023, LCID, 4, 0) + (value,) + ()))
	def _set_UseMaxStictionDeformation(self, value):
		if "UseMaxStictionDeformation" in self.__dict__: self.__dict__["UseMaxStictionDeformation"] = value; return
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((1024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((1018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((1020, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((1019, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((1017, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((1015, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((1016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((1021, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT2D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT2D.MTT2DFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	Indentation exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaxStictionDeformation = property(_get_MaxStictionDeformation, None)
	'''
	Maximum stiction deformation

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
	UseMaxStictionDeformation = property(_get_UseMaxStictionDeformation, _set_UseMaxStictionDeformation)
	'''
	Use maximum stiction deformation

	:type: bool
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
		"_set_UseMaxStictionDeformation": _set_UseMaxStictionDeformation,
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
		"BoundaryPenetration": (1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'),
		"FrictionCoefficient": (1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'),
		"IndentationExponent": (1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaxStictionDeformation": (1052, 2, (9, 0), (), "MaxStictionDeformation", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseMaxStictionDeformation": (1051, 2, (11, 0), (), "UseMaxStictionDeformation", None),
		"UseRDF": (1024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (1025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (1015, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((1022, LCID, 4, 0),()),
		"FrictionType": ((1023, LCID, 4, 0),()),
		"UseMaxStictionDeformation": ((1051, LCID, 4, 0),()),
		"UseRDF": ((1024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((1018, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((1020, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((1019, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((1017, LCID, 4, 0),()),
		"UseSpecialRDF": ((1025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((1015, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((1016, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((1021, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DContactPropertyRollerMovableToFixed(DispatchBaseClass):
	'''MTT2D movable roller contact property'''
	CLSID = IID('{B006CA26-0F57-4100-9224-D3D62429E8F6}')
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
		return self._ApplyTypes_(*(1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaxStictionDeformation(self):
		return self._ApplyTypes_(*(1052, 2, (9, 0), (), "MaxStictionDeformation", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_OffsetPenetration(self):
		return self._ApplyTypes_(*(1101, 2, (9, 0), (), "OffsetPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseMaxStictionDeformation(self):
		return self._ApplyTypes_(*(1051, 2, (11, 0), (), "UseMaxStictionDeformation", None))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(1024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(1025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(1015, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((1022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((1023, LCID, 4, 0) + (value,) + ()))
	def _set_UseMaxStictionDeformation(self, value):
		if "UseMaxStictionDeformation" in self.__dict__: self.__dict__["UseMaxStictionDeformation"] = value; return
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((1024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((1018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((1020, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((1019, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((1017, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((1015, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((1016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((1021, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT2D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT2D.MTT2DFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	Indentation exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaxStictionDeformation = property(_get_MaxStictionDeformation, None)
	'''
	Maximum stiction deformation

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
	UseMaxStictionDeformation = property(_get_UseMaxStictionDeformation, _set_UseMaxStictionDeformation)
	'''
	Use maximum stiction deformation

	:type: bool
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
		"_set_UseMaxStictionDeformation": _set_UseMaxStictionDeformation,
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
		"BoundaryPenetration": (1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'),
		"FrictionCoefficient": (1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'),
		"IndentationExponent": (1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaxStictionDeformation": (1052, 2, (9, 0), (), "MaxStictionDeformation", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"OffsetPenetration": (1101, 2, (9, 0), (), "OffsetPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseMaxStictionDeformation": (1051, 2, (11, 0), (), "UseMaxStictionDeformation", None),
		"UseRDF": (1024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (1025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (1015, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((1022, LCID, 4, 0),()),
		"FrictionType": ((1023, LCID, 4, 0),()),
		"UseMaxStictionDeformation": ((1051, LCID, 4, 0),()),
		"UseRDF": ((1024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((1018, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((1020, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((1019, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((1017, LCID, 4, 0),()),
		"UseSpecialRDF": ((1025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((1015, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((1016, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((1021, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DContactPropertyRollerToSheet(DispatchBaseClass):
	'''MTT2D fixed roller contact property'''
	CLSID = IID('{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}')
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
		return self._ApplyTypes_(*(1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactParameterType(self):
		return self._ApplyTypes_(*(1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaxStictionDeformation(self):
		return self._ApplyTypes_(*(1052, 2, (9, 0), (), "MaxStictionDeformation", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumDamping(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RDF(self):
		return self._ApplyTypes_(*(1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRDF(self):
		return self._ApplyTypes_(*(1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ThresholdVelocity(self):
		return self._ApplyTypes_(*(1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseMaxStictionDeformation(self):
		return self._ApplyTypes_(*(1051, 2, (11, 0), (), "UseMaxStictionDeformation", None))
	def _get_UseRDF(self):
		return self._ApplyTypes_(*(1024, 2, (11, 0), (), "UseRDF", None))
	def _get_UseSpecialBoundaryPenetration(self):
		return self._ApplyTypes_(*(1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None))
	def _get_UseSpecialFrictionCoefficient(self):
		return self._ApplyTypes_(*(1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None))
	def _get_UseSpecialIndentationExponent(self):
		return self._ApplyTypes_(*(1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None))
	def _get_UseSpecialMaximumDamping(self):
		return self._ApplyTypes_(*(1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None))
	def _get_UseSpecialRDF(self):
		return self._ApplyTypes_(*(1025, 2, (11, 0), (), "UseSpecialRDF", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(1015, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseSpecialStiffnessExponent(self):
		return self._ApplyTypes_(*(1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None))
	def _get_UseSpecialThresholdVelocity(self):
		return self._ApplyTypes_(*(1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None))

	def _set_ContactParameterType(self, value):
		if "ContactParameterType" in self.__dict__: self.__dict__["ContactParameterType"] = value; return
		self._oleobj_.Invoke(*((1022, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((1023, LCID, 4, 0) + (value,) + ()))
	def _set_UseMaxStictionDeformation(self, value):
		if "UseMaxStictionDeformation" in self.__dict__: self.__dict__["UseMaxStictionDeformation"] = value; return
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (value,) + ()))
	def _set_UseRDF(self, value):
		if "UseRDF" in self.__dict__: self.__dict__["UseRDF"] = value; return
		self._oleobj_.Invoke(*((1024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialBoundaryPenetration(self, value):
		if "UseSpecialBoundaryPenetration" in self.__dict__: self.__dict__["UseSpecialBoundaryPenetration"] = value; return
		self._oleobj_.Invoke(*((1018, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialFrictionCoefficient(self, value):
		if "UseSpecialFrictionCoefficient" in self.__dict__: self.__dict__["UseSpecialFrictionCoefficient"] = value; return
		self._oleobj_.Invoke(*((1020, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialIndentationExponent(self, value):
		if "UseSpecialIndentationExponent" in self.__dict__: self.__dict__["UseSpecialIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((1019, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialMaximumDamping(self, value):
		if "UseSpecialMaximumDamping" in self.__dict__: self.__dict__["UseSpecialMaximumDamping"] = value; return
		self._oleobj_.Invoke(*((1017, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRDF(self, value):
		if "UseSpecialRDF" in self.__dict__: self.__dict__["UseSpecialRDF"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((1015, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffnessExponent(self, value):
		if "UseSpecialStiffnessExponent" in self.__dict__: self.__dict__["UseSpecialStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((1016, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThresholdVelocity(self, value):
		if "UseSpecialThresholdVelocity" in self.__dict__: self.__dict__["UseSpecialThresholdVelocity"] = value; return
		self._oleobj_.Invoke(*((1021, LCID, 4, 0) + (value,) + ()))

	BoundaryPenetration = property(_get_BoundaryPenetration, None)
	'''
	Boundary penetration

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactParameterType = property(_get_ContactParameterType, _set_ContactParameterType)
	'''
	Contact parameter type

	:type: recurdyn.MTT2D.ContactParameterType
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	Friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.MTT2D.MTT2DFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	Indentation exponent

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaxStictionDeformation = property(_get_MaxStictionDeformation, None)
	'''
	Maximum stiction deformation

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
	UseMaxStictionDeformation = property(_get_UseMaxStictionDeformation, _set_UseMaxStictionDeformation)
	'''
	Use maximum stiction deformation

	:type: bool
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
		"_set_UseMaxStictionDeformation": _set_UseMaxStictionDeformation,
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
		"BoundaryPenetration": (1004, 2, (9, 0), (), "BoundaryPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactParameterType": (1022, 2, (3, 0), (), "ContactParameterType", '{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}'),
		"FrictionCoefficient": (1006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionType": (1023, 2, (3, 0), (), "FrictionType", '{C2680614-B10F-47FA-8127-29C03A89BDA7}'),
		"IndentationExponent": (1005, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaxStictionDeformation": (1052, 2, (9, 0), (), "MaxStictionDeformation", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumDamping": (1003, 2, (9, 0), (), "MaximumDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RDF": (1027, 2, (9, 0), (), "RDF", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialBoundaryPenetration": (1011, 2, (9, 0), (), "SpecialBoundaryPenetration", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialFrictionCoefficient": (1013, 2, (9, 0), (), "SpecialFrictionCoefficient", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialIndentationExponent": (1012, 2, (9, 0), (), "SpecialIndentationExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialMaximumDamping": (1010, 2, (9, 0), (), "SpecialMaximumDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRDF": (1026, 2, (9, 0), (), "SpecialRDF", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffnessExponent": (1009, 2, (9, 0), (), "SpecialStiffnessExponent", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThresholdVelocity": (1014, 2, (9, 0), (), "SpecialThresholdVelocity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"Stiffness": (1001, 2, (9, 0), (), "Stiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (1002, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ThresholdVelocity": (1007, 2, (9, 0), (), "ThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseMaxStictionDeformation": (1051, 2, (11, 0), (), "UseMaxStictionDeformation", None),
		"UseRDF": (1024, 2, (11, 0), (), "UseRDF", None),
		"UseSpecialBoundaryPenetration": (1018, 2, (11, 0), (), "UseSpecialBoundaryPenetration", None),
		"UseSpecialFrictionCoefficient": (1020, 2, (11, 0), (), "UseSpecialFrictionCoefficient", None),
		"UseSpecialIndentationExponent": (1019, 2, (11, 0), (), "UseSpecialIndentationExponent", None),
		"UseSpecialMaximumDamping": (1017, 2, (11, 0), (), "UseSpecialMaximumDamping", None),
		"UseSpecialRDF": (1025, 2, (11, 0), (), "UseSpecialRDF", None),
		"UseSpecialStiffness": (1015, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseSpecialStiffnessExponent": (1016, 2, (11, 0), (), "UseSpecialStiffnessExponent", None),
		"UseSpecialThresholdVelocity": (1021, 2, (11, 0), (), "UseSpecialThresholdVelocity", None),
	}
	_prop_map_put_ = {
		"ContactParameterType": ((1022, LCID, 4, 0),()),
		"FrictionType": ((1023, LCID, 4, 0),()),
		"UseMaxStictionDeformation": ((1051, LCID, 4, 0),()),
		"UseRDF": ((1024, LCID, 4, 0),()),
		"UseSpecialBoundaryPenetration": ((1018, LCID, 4, 0),()),
		"UseSpecialFrictionCoefficient": ((1020, LCID, 4, 0),()),
		"UseSpecialIndentationExponent": ((1019, LCID, 4, 0),()),
		"UseSpecialMaximumDamping": ((1017, LCID, 4, 0),()),
		"UseSpecialRDF": ((1025, LCID, 4, 0),()),
		"UseSpecialStiffness": ((1015, LCID, 4, 0),()),
		"UseSpecialStiffnessExponent": ((1016, LCID, 4, 0),()),
		"UseSpecialThresholdVelocity": ((1021, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DContactSheetToSheet(DispatchBaseClass):
	'''MTT2D sheet to sheet contact'''
	CLSID = IID('{AB78805A-064A-4015-812D-1332288F5789}')
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


	def _get_ActionSheetGroup(self):
		return self._ApplyTypes_(*(1052, 2, (9, 0), (), "ActionSheetGroup", '{59FE2E3A-2043-4651-8D6E-A58D8800205A}'))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseSheetGroup(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "BaseSheetGroup", '{59FE2E3A-2043-4651-8D6E-A58D8800205A}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(1055, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertySheetToSheet(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "ContactPropertySheetToSheet", '{3641A1D2-6FCC-40AA-A4AA-8176CF6C755E}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(1054, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
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
		return self._ApplyTypes_(*(1056, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(1057, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionSheetGroup(self, value):
		if "ActionSheetGroup" in self.__dict__: self.__dict__["ActionSheetGroup"] = value; return
		self._oleobj_.Invoke(*((1052, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseSheetGroup(self, value):
		if "BaseSheetGroup" in self.__dict__: self.__dict__["BaseSheetGroup"] = value; return
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((1054, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((1057, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionSheetGroup = property(_get_ActionSheetGroup, _set_ActionSheetGroup)
	'''
	Action sheet group

	:type: recurdyn.MTT2D.IMTT2DGroupSheet
	'''
	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseSheetGroup = property(_get_BaseSheetGroup, _set_BaseSheetGroup)
	'''
	Base sheet group

	:type: recurdyn.MTT2D.IMTT2DGroupSheet
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
	ContactPropertySheetToSheet = property(_get_ContactPropertySheetToSheet, None)
	'''
	The contact parameters of contact forces applied between the sheets

	:type: recurdyn.MTT2D.IMTT2DContactProperty
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
		"_set_ActionSheetGroup": _set_ActionSheetGroup,
		"_set_Active": _set_Active,
		"_set_BaseSheetGroup": _set_BaseSheetGroup,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionSheetGroup": (1052, 2, (9, 0), (), "ActionSheetGroup", '{59FE2E3A-2043-4651-8D6E-A58D8800205A}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseSheetGroup": (1051, 2, (9, 0), (), "BaseSheetGroup", '{59FE2E3A-2043-4651-8D6E-A58D8800205A}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (1055, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertySheetToSheet": (1053, 2, (9, 0), (), "ContactPropertySheetToSheet", '{3641A1D2-6FCC-40AA-A4AA-8176CF6C755E}'),
		"ForceDisplay": (1054, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SpecialContactPoints": (1056, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseSpecialContactPoints": (1057, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionSheetGroup": ((1052, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseSheetGroup": ((1051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((1054, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((1057, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DContactSheetToSheetCollection(DispatchBaseClass):
	'''IMTT2DContactSheetToSheetCollection'''
	CLSID = IID('{9538383C-C3C2-463F-B9D5-9017468026D1}')
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
		:rtype: recurdyn.MTT2D.IMTT2DContactSheetToSheet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{AB78805A-064A-4015-812D-1332288F5789}')
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
		:rtype: recurdyn.MTT2D.IMTT2DContactSheetToSheet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{AB78805A-064A-4015-812D-1332288F5789}')
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
		return win32com.client.util.Iterator(ob, '{AB78805A-064A-4015-812D-1332288F5789}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{AB78805A-064A-4015-812D-1332288F5789}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT2DFixedRollerGroupCollection(DispatchBaseClass):
	'''IMTT2DFixedRollerGroupCollection'''
	CLSID = IID('{8393C52E-FB87-4F44-AA3B-CF6BE4045DEA}')
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
		:rtype: recurdyn.MTT2D.IMTT2DGroupFixedRoller
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0E7F0C51-106B-446A-93A5-1912034EA1A7}')
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
		:rtype: recurdyn.MTT2D.IMTT2DGroupFixedRoller
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0E7F0C51-106B-446A-93A5-1912034EA1A7}')
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
		return win32com.client.util.Iterator(ob, '{0E7F0C51-106B-446A-93A5-1912034EA1A7}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{0E7F0C51-106B-446A-93A5-1912034EA1A7}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT2DFlexibleRollerProperty(DispatchBaseClass):
	'''MTT2D flexible roller property'''
	CLSID = IID('{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AllDampingRatio(self):
		return self._ApplyTypes_(*(1018, 2, (11, 0), (), "AllDampingRatio", None))
	def _get_AllDensity(self):
		return self._ApplyTypes_(*(1016, 2, (11, 0), (), "AllDensity", None))
	def _get_AllPoissonsRatio(self):
		return self._ApplyTypes_(*(1020, 2, (11, 0), (), "AllPoissonsRatio", None))
	def _get_AllTotalMass(self):
		return self._ApplyTypes_(*(1017, 2, (11, 0), (), "AllTotalMass", None))
	def _get_AllYoungsModulus(self):
		return self._ApplyTypes_(*(1019, 2, (11, 0), (), "AllYoungsModulus", None))
	def _get_Color(self):
		return self._ApplyTypes_(*(1027, 2, (19, 0), (), "Color", None))
	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Depth(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DrillingStiffnessFactor(self):
		return self._ApplyTypes_(*(1026, 2, (9, 0), (), "DrillingStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FDRRadius(self):
		return self._ApplyTypes_(*(1002, 2, (9, 0), (), "FDRRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MassType(self):
		return self._ApplyTypes_(*(1005, 2, (3, 0), (), "MassType", '{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}'))
	def _get_NoOfNodesCircumference(self):
		return self._ApplyTypes_(*(1003, 2, (3, 0), (), "NoOfNodesCircumference", None))
	def _get_NoOfNodesRadial(self):
		return self._ApplyTypes_(*(1004, 2, (3, 0), (), "NoOfNodesRadial", None))
	def _get_PoissonsRatio(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialDampingRatio(self):
		return self._ApplyTypes_(*(1013, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialDensity(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPoissonsRatio(self):
		return self._ApplyTypes_(*(1015, 2, (9, 0), (), "SpecialPoissonsRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialTotalMass(self):
		return self._ApplyTypes_(*(1012, 2, (9, 0), (), "SpecialTotalMass", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialYoungsModulus(self):
		return self._ApplyTypes_(*(1014, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(1007, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseSpecialDampingRatio(self):
		return self._ApplyTypes_(*(1023, 2, (11, 0), (), "UseSpecialDampingRatio", None))
	def _get_UseSpecialDensity(self):
		return self._ApplyTypes_(*(1021, 2, (11, 0), (), "UseSpecialDensity", None))
	def _get_UseSpecialPoissonsRatio(self):
		return self._ApplyTypes_(*(1025, 2, (11, 0), (), "UseSpecialPoissonsRatio", None))
	def _get_UseSpecialTotalMass(self):
		return self._ApplyTypes_(*(1022, 2, (11, 0), (), "UseSpecialTotalMass", None))
	def _get_UseSpecialYoungsModulus(self):
		return self._ApplyTypes_(*(1024, 2, (11, 0), (), "UseSpecialYoungsModulus", None))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_AllDampingRatio(self, value):
		if "AllDampingRatio" in self.__dict__: self.__dict__["AllDampingRatio"] = value; return
		self._oleobj_.Invoke(*((1018, LCID, 4, 0) + (value,) + ()))
	def _set_AllDensity(self, value):
		if "AllDensity" in self.__dict__: self.__dict__["AllDensity"] = value; return
		self._oleobj_.Invoke(*((1016, LCID, 4, 0) + (value,) + ()))
	def _set_AllPoissonsRatio(self, value):
		if "AllPoissonsRatio" in self.__dict__: self.__dict__["AllPoissonsRatio"] = value; return
		self._oleobj_.Invoke(*((1020, LCID, 4, 0) + (value,) + ()))
	def _set_AllTotalMass(self, value):
		if "AllTotalMass" in self.__dict__: self.__dict__["AllTotalMass"] = value; return
		self._oleobj_.Invoke(*((1017, LCID, 4, 0) + (value,) + ()))
	def _set_AllYoungsModulus(self, value):
		if "AllYoungsModulus" in self.__dict__: self.__dict__["AllYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((1019, LCID, 4, 0) + (value,) + ()))
	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((1027, LCID, 4, 0) + (value,) + ()))
	def _set_MassType(self, value):
		if "MassType" in self.__dict__: self.__dict__["MassType"] = value; return
		self._oleobj_.Invoke(*((1005, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDampingRatio(self, value):
		if "UseSpecialDampingRatio" in self.__dict__: self.__dict__["UseSpecialDampingRatio"] = value; return
		self._oleobj_.Invoke(*((1023, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDensity(self, value):
		if "UseSpecialDensity" in self.__dict__: self.__dict__["UseSpecialDensity"] = value; return
		self._oleobj_.Invoke(*((1021, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPoissonsRatio(self, value):
		if "UseSpecialPoissonsRatio" in self.__dict__: self.__dict__["UseSpecialPoissonsRatio"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialTotalMass(self, value):
		if "UseSpecialTotalMass" in self.__dict__: self.__dict__["UseSpecialTotalMass"] = value; return
		self._oleobj_.Invoke(*((1022, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialYoungsModulus(self, value):
		if "UseSpecialYoungsModulus" in self.__dict__: self.__dict__["UseSpecialYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((1024, LCID, 4, 0) + (value,) + ()))

	AllDampingRatio = property(_get_AllDampingRatio, _set_AllDampingRatio)
	'''
	All damping ratio

	:type: bool
	'''
	AllDensity = property(_get_AllDensity, _set_AllDensity)
	'''
	All density

	:type: bool
	'''
	AllPoissonsRatio = property(_get_AllPoissonsRatio, _set_AllPoissonsRatio)
	'''
	All Poisson's ratio

	:type: bool
	'''
	AllTotalMass = property(_get_AllTotalMass, _set_AllTotalMass)
	'''
	All total mass

	:type: bool
	'''
	AllYoungsModulus = property(_get_AllYoungsModulus, _set_AllYoungsModulus)
	'''
	All Young's modulus

	:type: bool
	'''
	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
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
	Depth = property(_get_Depth, None)
	'''
	The depth of the fixed roller body

	:type: recurdyn.ProcessNet.IDouble
	'''
	DrillingStiffnessFactor = property(_get_DrillingStiffnessFactor, None)
	'''
	Drilling stiffness factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	FDRRadius = property(_get_FDRRadius, None)
	'''
	The FDR radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	MassType = property(_get_MassType, _set_MassType)
	'''
	The type of method to apply mass

	:type: recurdyn.ProcessNet.MassType
	'''
	NoOfNodesCircumference = property(_get_NoOfNodesCircumference, None)
	'''
	Number of nodes at circumference

	:type: int
	'''
	NoOfNodesRadial = property(_get_NoOfNodesRadial, None)
	'''
	Number of nodes at radial

	:type: int
	'''
	PoissonsRatio = property(_get_PoissonsRatio, None)
	'''
	Poisson's ratio

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
	SpecialPoissonsRatio = property(_get_SpecialPoissonsRatio, None)
	'''
	Special Poisson's ratio

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialTotalMass = property(_get_SpecialTotalMass, None)
	'''
	Special total mass

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialYoungsModulus = property(_get_SpecialYoungsModulus, None)
	'''
	Special Young's modulus

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	TotalMass = property(_get_TotalMass, None)
	'''
	Total mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseSpecialDampingRatio = property(_get_UseSpecialDampingRatio, _set_UseSpecialDampingRatio)
	'''
	Special damping ratio

	:type: bool
	'''
	UseSpecialDensity = property(_get_UseSpecialDensity, _set_UseSpecialDensity)
	'''
	Special density

	:type: bool
	'''
	UseSpecialPoissonsRatio = property(_get_UseSpecialPoissonsRatio, _set_UseSpecialPoissonsRatio)
	'''
	Special Poisson's ratio

	:type: bool
	'''
	UseSpecialTotalMass = property(_get_UseSpecialTotalMass, _set_UseSpecialTotalMass)
	'''
	Special total mass

	:type: bool
	'''
	UseSpecialYoungsModulus = property(_get_UseSpecialYoungsModulus, _set_UseSpecialYoungsModulus)
	'''
	Special Young's modulus

	:type: bool
	'''
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	Young's modulus

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_AllDampingRatio": _set_AllDampingRatio,
		"_set_AllDensity": _set_AllDensity,
		"_set_AllPoissonsRatio": _set_AllPoissonsRatio,
		"_set_AllTotalMass": _set_AllTotalMass,
		"_set_AllYoungsModulus": _set_AllYoungsModulus,
		"_set_Color": _set_Color,
		"_set_MassType": _set_MassType,
		"_set_UseSpecialDampingRatio": _set_UseSpecialDampingRatio,
		"_set_UseSpecialDensity": _set_UseSpecialDensity,
		"_set_UseSpecialPoissonsRatio": _set_UseSpecialPoissonsRatio,
		"_set_UseSpecialTotalMass": _set_UseSpecialTotalMass,
		"_set_UseSpecialYoungsModulus": _set_UseSpecialYoungsModulus,
	}
	_prop_map_get_ = {
		"AllDampingRatio": (1018, 2, (11, 0), (), "AllDampingRatio", None),
		"AllDensity": (1016, 2, (11, 0), (), "AllDensity", None),
		"AllPoissonsRatio": (1020, 2, (11, 0), (), "AllPoissonsRatio", None),
		"AllTotalMass": (1017, 2, (11, 0), (), "AllTotalMass", None),
		"AllYoungsModulus": (1019, 2, (11, 0), (), "AllYoungsModulus", None),
		"Color": (1027, 2, (19, 0), (), "Color", None),
		"DampingRatio": (1008, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (1006, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Depth": (1001, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DrillingStiffnessFactor": (1026, 2, (9, 0), (), "DrillingStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FDRRadius": (1002, 2, (9, 0), (), "FDRRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MassType": (1005, 2, (3, 0), (), "MassType", '{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}'),
		"NoOfNodesCircumference": (1003, 2, (3, 0), (), "NoOfNodesCircumference", None),
		"NoOfNodesRadial": (1004, 2, (3, 0), (), "NoOfNodesRadial", None),
		"PoissonsRatio": (1010, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialDampingRatio": (1013, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialDensity": (1011, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPoissonsRatio": (1015, 2, (9, 0), (), "SpecialPoissonsRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialTotalMass": (1012, 2, (9, 0), (), "SpecialTotalMass", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialYoungsModulus": (1014, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"TotalMass": (1007, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseSpecialDampingRatio": (1023, 2, (11, 0), (), "UseSpecialDampingRatio", None),
		"UseSpecialDensity": (1021, 2, (11, 0), (), "UseSpecialDensity", None),
		"UseSpecialPoissonsRatio": (1025, 2, (11, 0), (), "UseSpecialPoissonsRatio", None),
		"UseSpecialTotalMass": (1022, 2, (11, 0), (), "UseSpecialTotalMass", None),
		"UseSpecialYoungsModulus": (1024, 2, (11, 0), (), "UseSpecialYoungsModulus", None),
		"YoungsModulus": (1009, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"AllDampingRatio": ((1018, LCID, 4, 0),()),
		"AllDensity": ((1016, LCID, 4, 0),()),
		"AllPoissonsRatio": ((1020, LCID, 4, 0),()),
		"AllTotalMass": ((1017, LCID, 4, 0),()),
		"AllYoungsModulus": ((1019, LCID, 4, 0),()),
		"Color": ((1027, LCID, 4, 0),()),
		"MassType": ((1005, LCID, 4, 0),()),
		"UseSpecialDampingRatio": ((1023, LCID, 4, 0),()),
		"UseSpecialDensity": ((1021, LCID, 4, 0),()),
		"UseSpecialPoissonsRatio": ((1025, LCID, 4, 0),()),
		"UseSpecialTotalMass": ((1022, LCID, 4, 0),()),
		"UseSpecialYoungsModulus": ((1024, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DForceNodal(DispatchBaseClass):
	'''MTT2D nodal force'''
	CLSID = IID('{0F707193-3BDD-4899-8FD9-E9C21739ECCB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetAppliedBody(self, pVal):
		'''
		Specifies whether nodal force is applied to a body.
		
		:param pVal: str
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(1053, LCID, 1, (11, 0), ((8, 1),),pVal
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def SetAppliedBody(self, pVal, vBool):
		'''
		Applies nodal force to a body
		
		:param pVal: str
		:param vBool: bool
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(1052, LCID, 1, (11, 0), ((8, 1), (11, 1)),pVal
			, vBool)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(1054, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
	def _get_UserSubroutine(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((1054, LCID, 4, 0) + (value,) + ()))
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
	def _set_UserSubroutine(self, value):
		if "UserSubroutine" in self.__dict__: self.__dict__["UserSubroutine"] = value; return
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (value,) + ()))

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
		"_set_UserData": _set_UserData,
		"_set_UserSubroutine": _set_UserSubroutine,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (1054, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"UserSubroutine": (1051, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((1054, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"UserSubroutine": ((1051, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DForceNodalCollection(DispatchBaseClass):
	'''IForceNodalCollection'''
	CLSID = IID('{E3BB5B6C-23F0-4038-8466-36B8782CC65A}')
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
		:rtype: recurdyn.MTT2D.IMTT2DForceNodal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0F707193-3BDD-4899-8FD9-E9C21739ECCB}')
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
		:rtype: recurdyn.MTT2D.IMTT2DForceNodal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0F707193-3BDD-4899-8FD9-E9C21739ECCB}')
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
		return win32com.client.util.Iterator(ob, '{0F707193-3BDD-4899-8FD9-E9C21739ECCB}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{0F707193-3BDD-4899-8FD9-E9C21739ECCB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT2DForceSpring(DispatchBaseClass):
	'''MTT2D spring force'''
	CLSID = IID('{5AB3349F-401D-4ED1-88E3-0A300C0C6B94}')
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
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
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
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPreload(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpringGraphic(self):
		return self._ApplyTypes_(*(252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_UseSpecialDamping(self):
		return self._ApplyTypes_(*(1003, 2, (11, 0), (), "UseSpecialDamping", None))
	def _get_UseSpecialPreload(self):
		return self._ApplyTypes_(*(1004, 2, (11, 0), (), "UseSpecialPreload", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(1002, 2, (11, 0), (), "UseSpecialStiffness", None))
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
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
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
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPreload(self, value):
		if "UseSpecialPreload" in self.__dict__: self.__dict__["UseSpecialPreload"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
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
		"BaseBody": (1001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
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
		"SpecialDamping": (1009, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPreload": (1010, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpringGraphic": (252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'),
		"Stiffness": (255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TorqueDisplayColor": (208, 2, (19, 0), (), "TorqueDisplayColor", None),
		"UseSpecialDamping": (1003, 2, (11, 0), (), "UseSpecialDamping", None),
		"UseSpecialPreload": (1004, 2, (11, 0), (), "UseSpecialPreload", None),
		"UseSpecialStiffness": (1002, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionMarker": ((203, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((1001, LCID, 4, 0),()),
		"BaseMarker": ((202, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((207, LCID, 4, 0),()),
		"ForceDisplayUse": ((209, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((208, LCID, 4, 0),()),
		"UseSpecialDamping": ((1003, LCID, 4, 0),()),
		"UseSpecialPreload": ((1004, LCID, 4, 0),()),
		"UseSpecialStiffness": ((1002, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DForceSpringNip(DispatchBaseClass):
	'''MTT2D nip spring force'''
	CLSID = IID('{4A4DE5B0-59EF-4CD2-B669-93768E326904}')
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
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_BaseMarker(self):
		return self._ApplyTypes_(*(202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_BasePoint(self):
		return self._ApplyTypes_(*(1051, 2, (8197, 0), (), "BasePoint", None))
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
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPreload(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpringGraphic(self):
		return self._ApplyTypes_(*(252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_UseBasePoint(self):
		return self._ApplyTypes_(*(1052, 2, (11, 0), (), "UseBasePoint", None))
	def _get_UseSpecialDamping(self):
		return self._ApplyTypes_(*(1003, 2, (11, 0), (), "UseSpecialDamping", None))
	def _get_UseSpecialPreload(self):
		return self._ApplyTypes_(*(1004, 2, (11, 0), (), "UseSpecialPreload", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(1002, 2, (11, 0), (), "UseSpecialStiffness", None))
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
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_BaseMarker(self, value):
		if "BaseMarker" in self.__dict__: self.__dict__["BaseMarker"] = value; return
		self._oleobj_.Invoke(*((202, LCID, 4, 0) + (value,) + ()))
	def _set_BasePoint(self, value):
		if "BasePoint" in self.__dict__: self.__dict__["BasePoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (variantValue,) + ()))
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
		self._oleobj_.Invoke(*((1052, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDamping(self, value):
		if "UseSpecialDamping" in self.__dict__: self.__dict__["UseSpecialDamping"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPreload(self, value):
		if "UseSpecialPreload" in self.__dict__: self.__dict__["UseSpecialPreload"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
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
		"BaseBody": (1001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"BaseMarker": (202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"BasePoint": (1051, 2, (8197, 0), (), "BasePoint", None),
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
		"SpecialDamping": (1009, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPreload": (1010, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpringGraphic": (252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'),
		"Stiffness": (255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TorqueDisplayColor": (208, 2, (19, 0), (), "TorqueDisplayColor", None),
		"UseBasePoint": (1052, 2, (11, 0), (), "UseBasePoint", None),
		"UseSpecialDamping": (1003, 2, (11, 0), (), "UseSpecialDamping", None),
		"UseSpecialPreload": (1004, 2, (11, 0), (), "UseSpecialPreload", None),
		"UseSpecialStiffness": (1002, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionMarker": ((203, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((1001, LCID, 4, 0),()),
		"BaseMarker": ((202, LCID, 4, 0),()),
		"BasePoint": ((1051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((207, LCID, 4, 0),()),
		"ForceDisplayUse": ((209, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((208, LCID, 4, 0),()),
		"UseBasePoint": ((1052, LCID, 4, 0),()),
		"UseSpecialDamping": ((1003, LCID, 4, 0),()),
		"UseSpecialPreload": ((1004, LCID, 4, 0),()),
		"UseSpecialStiffness": ((1002, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DForceSpringTSD(DispatchBaseClass):
	'''MTT2D TSD spring force'''
	CLSID = IID('{66947C3A-68E2-406E-9491-42952BD66A96}')
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
	def _get_ActionPoint(self):
		return self._ApplyTypes_(*(1051, 2, (8197, 0), (), "ActionPoint", None))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
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
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialPreload(self):
		return self._ApplyTypes_(*(1010, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialStiffness(self):
		return self._ApplyTypes_(*(1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpringGraphic(self):
		return self._ApplyTypes_(*(252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_StopperDistance(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "StopperDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StopperFactor(self):
		return self._ApplyTypes_(*(1054, 2, (9, 0), (), "StopperFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_UseSpecialDamping(self):
		return self._ApplyTypes_(*(1003, 2, (11, 0), (), "UseSpecialDamping", None))
	def _get_UseSpecialPreload(self):
		return self._ApplyTypes_(*(1004, 2, (11, 0), (), "UseSpecialPreload", None))
	def _get_UseSpecialStiffness(self):
		return self._ApplyTypes_(*(1002, 2, (11, 0), (), "UseSpecialStiffness", None))
	def _get_UseStopperDistance(self):
		return self._ApplyTypes_(*(1052, 2, (11, 0), (), "UseStopperDistance", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionMarker(self, value):
		if "ActionMarker" in self.__dict__: self.__dict__["ActionMarker"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_ActionPoint(self, value):
		if "ActionPoint" in self.__dict__: self.__dict__["ActionPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
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
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialPreload(self, value):
		if "UseSpecialPreload" in self.__dict__: self.__dict__["UseSpecialPreload"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialStiffness(self, value):
		if "UseSpecialStiffness" in self.__dict__: self.__dict__["UseSpecialStiffness"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_UseStopperDistance(self, value):
		if "UseStopperDistance" in self.__dict__: self.__dict__["UseStopperDistance"] = value; return
		self._oleobj_.Invoke(*((1052, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionMarker = property(_get_ActionMarker, _set_ActionMarker)
	'''
	Action marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	ActionPoint = property(_get_ActionPoint, _set_ActionPoint)
	'''
	Action point

	:type: list[float]
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
	StopperDistance = property(_get_StopperDistance, None)
	'''
	Stopper distance

	:type: recurdyn.ProcessNet.IDouble
	'''
	StopperFactor = property(_get_StopperFactor, None)
	'''
	Stopper factor

	:type: recurdyn.ProcessNet.IDouble
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
	UseStopperDistance = property(_get_UseStopperDistance, _set_UseStopperDistance)
	'''
	Use stopper distance

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ActionMarker": _set_ActionMarker,
		"_set_ActionPoint": _set_ActionPoint,
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
		"_set_UseStopperDistance": _set_UseStopperDistance,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionMarker": (203, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"ActionPoint": (1051, 2, (8197, 0), (), "ActionPoint", None),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (1001, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
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
		"SpecialDamping": (1009, 2, (9, 0), (), "SpecialDamping", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialPreload": (1010, 2, (9, 0), (), "SpecialPreload", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialStiffness": (1008, 2, (9, 0), (), "SpecialStiffness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpringGraphic": (252, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'),
		"Stiffness": (255, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"StopperDistance": (1053, 2, (9, 0), (), "StopperDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StopperFactor": (1054, 2, (9, 0), (), "StopperFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TorqueDisplayColor": (208, 2, (19, 0), (), "TorqueDisplayColor", None),
		"UseSpecialDamping": (1003, 2, (11, 0), (), "UseSpecialDamping", None),
		"UseSpecialPreload": (1004, 2, (11, 0), (), "UseSpecialPreload", None),
		"UseSpecialStiffness": (1002, 2, (11, 0), (), "UseSpecialStiffness", None),
		"UseStopperDistance": (1052, 2, (11, 0), (), "UseStopperDistance", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionMarker": ((203, LCID, 4, 0),()),
		"ActionPoint": ((1051, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((1001, LCID, 4, 0),()),
		"BaseMarker": ((202, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((207, LCID, 4, 0),()),
		"ForceDisplayUse": ((209, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((208, LCID, 4, 0),()),
		"UseSpecialDamping": ((1003, LCID, 4, 0),()),
		"UseSpecialPreload": ((1004, LCID, 4, 0),()),
		"UseSpecialStiffness": ((1002, LCID, 4, 0),()),
		"UseStopperDistance": ((1052, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGroupFixedRoller(DispatchBaseClass):
	'''MTT2D fixed roller group'''
	CLSID = IID('{0E7F0C51-106B-446A-93A5-1912034EA1A7}')
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
		return self._oleobj_.InvokeTypes(1063, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_CenterPoint(self):
		return self._ApplyTypes_(*(1052, 2, (8197, 0), (), "CenterPoint", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(1067, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(1058, 2, (9, 0), (), "ContactPropertyToSheet", '{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}'))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(1066, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Inertia(self):
		return self._ApplyTypes_(*(1055, 2, (9, 0), (), "Inertia", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Mass(self):
		return self._ApplyTypes_(*(1054, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Motion(self):
		return self._ApplyTypes_(*(1057, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RevJoint(self):
		return self._ApplyTypes_(*(1065, 2, (9, 0), (), "RevJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_RollerBody(self):
		return self._ApplyTypes_(*(1064, 2, (9, 0), (), "RollerBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_RollerBodyType(self):
		return self._ApplyTypes_(*(1060, 2, (3, 0), (), "RollerBodyType", '{965EA0D7-3B24-4C39-87DD-0E6C1EA1CA47}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(1068, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseAutoCenterMarker(self):
		return self._ApplyTypes_(*(1059, 2, (11, 0), (), "UseAutoCenterMarker", None))
	def _get_UseMotion(self):
		return self._ApplyTypes_(*(1056, 2, (11, 0), (), "UseMotion", None))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(1069, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (value,) + ()))
	def _set_CenterPoint(self, value):
		if "CenterPoint" in self.__dict__: self.__dict__["CenterPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1052, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((1066, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoCenterMarker(self, value):
		if "UseAutoCenterMarker" in self.__dict__: self.__dict__["UseAutoCenterMarker"] = value; return
		self._oleobj_.Invoke(*((1059, LCID, 4, 0) + (value,) + ()))
	def _set_UseMotion(self, value):
		if "UseMotion" in self.__dict__: self.__dict__["UseMotion"] = value; return
		self._oleobj_.Invoke(*((1056, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((1069, LCID, 4, 0) + (value,) + ()))
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

	:type: recurdyn.MTT2D.IMTT2DContactPropertyRollerToSheet
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
	Inertia = property(_get_Inertia, None)
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
	RollerBodyType = property(_get_RollerBodyType, None)
	'''
	Roller body type

	:type: recurdyn.MTT2D.RollerBodyType
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
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseAutoCenterMarker": _set_UseAutoCenterMarker,
		"_set_UseMotion": _set_UseMotion,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (1051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"CenterPoint": (1052, 2, (8197, 0), (), "CenterPoint", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (1067, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToSheet": (1058, 2, (9, 0), (), "ContactPropertyToSheet", '{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}'),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"ForceDisplay": (1066, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Inertia": (1055, 2, (9, 0), (), "Inertia", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Mass": (1054, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Motion": (1057, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (1053, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RevJoint": (1065, 2, (9, 0), (), "RevJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"RollerBody": (1064, 2, (9, 0), (), "RollerBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"RollerBodyType": (1060, 2, (3, 0), (), "RollerBodyType", '{965EA0D7-3B24-4C39-87DD-0E6C1EA1CA47}'),
		"SpecialContactPoints": (1068, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseAutoCenterMarker": (1059, 2, (11, 0), (), "UseAutoCenterMarker", None),
		"UseMotion": (1056, 2, (11, 0), (), "UseMotion", None),
		"UseSpecialContactPoints": (1069, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((1051, LCID, 4, 0),()),
		"CenterPoint": ((1052, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"ForceDisplay": ((1066, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseAutoCenterMarker": ((1059, LCID, 4, 0),()),
		"UseMotion": ((1056, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((1069, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGroupFixedRollerShell(DispatchBaseClass):
	'''MTT2D fixed shell roller group'''
	CLSID = IID('{91034068-E6A9-4616-9D41-9B666E4018AB}')
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
		return self._oleobj_.InvokeTypes(1059, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_CenterPoint(self):
		return self._ApplyTypes_(*(1052, 2, (8197, 0), (), "CenterPoint", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(1063, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(1056, 2, (9, 0), (), "ContactPropertyToSheet", '{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}'))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_FlexBody(self):
		return self._ApplyTypes_(*(1061, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'))
	def _get_FlexibleRollerProperty(self):
		return self._ApplyTypes_(*(1058, 2, (9, 0), (), "FlexibleRollerProperty", '{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(1062, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Motion(self):
		return self._ApplyTypes_(*(1055, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(1064, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseAutoCenterMarker(self):
		return self._ApplyTypes_(*(1057, 2, (11, 0), (), "UseAutoCenterMarker", None))
	def _get_UseMotion(self):
		return self._ApplyTypes_(*(1054, 2, (11, 0), (), "UseMotion", None))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(1065, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (value,) + ()))
	def _set_CenterPoint(self, value):
		if "CenterPoint" in self.__dict__: self.__dict__["CenterPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1052, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((1062, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoCenterMarker(self, value):
		if "UseAutoCenterMarker" in self.__dict__: self.__dict__["UseAutoCenterMarker"] = value; return
		self._oleobj_.Invoke(*((1057, LCID, 4, 0) + (value,) + ()))
	def _set_UseExtractWithoutPreStress(self, value):
		if "UseExtractWithoutPreStress" in self.__dict__: self.__dict__["UseExtractWithoutPreStress"] = value; return
		self._oleobj_.Invoke(*((1060, LCID, 4, 0) + (value,) + ()))
	def _set_UseMotion(self, value):
		if "UseMotion" in self.__dict__: self.__dict__["UseMotion"] = value; return
		self._oleobj_.Invoke(*((1054, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((1065, LCID, 4, 0) + (value,) + ()))
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

	:type: recurdyn.MTT2D.IMTT2DContactPropertyRollerToSheet
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	FlexBody = property(_get_FlexBody, None)
	'''
	Flex body edit

	:type: recurdyn.FFlex.IFFlexToolkitBody
	'''
	FlexibleRollerProperty = property(_get_FlexibleRollerProperty, None)
	'''
	Flexible roller property

	:type: recurdyn.MTT2D.IMTT2DFlexibleRollerProperty
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
	Motion = property(_get_Motion, None)
	'''
	The angular motion of the fixed roller

	:type: recurdyn.ProcessNet.IMotion
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
	UseExtractWithoutPreStress = property(None, _set_UseExtractWithoutPreStress)
	'''
	ExtractWithoutPreStress flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_BaseBody": _set_BaseBody,
		"_set_CenterPoint": _set_CenterPoint,
		"_set_Comment": _set_Comment,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseAutoCenterMarker": _set_UseAutoCenterMarker,
		"_set_UseExtractWithoutPreStress": _set_UseExtractWithoutPreStress,
		"_set_UseMotion": _set_UseMotion,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (1051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"CenterPoint": (1052, 2, (8197, 0), (), "CenterPoint", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (1063, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToSheet": (1056, 2, (9, 0), (), "ContactPropertyToSheet", '{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}'),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FlexBody": (1061, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'),
		"FlexibleRollerProperty": (1058, 2, (9, 0), (), "FlexibleRollerProperty", '{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}'),
		"ForceDisplay": (1062, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Motion": (1055, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (1053, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialContactPoints": (1064, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseAutoCenterMarker": (1057, 2, (11, 0), (), "UseAutoCenterMarker", None),
		"UseMotion": (1054, 2, (11, 0), (), "UseMotion", None),
		"UseSpecialContactPoints": (1065, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((1051, LCID, 4, 0),()),
		"CenterPoint": ((1052, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"ForceDisplay": ((1062, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseAutoCenterMarker": ((1057, LCID, 4, 0),()),
		"UseExtractWithoutPreStress": ((1060, LCID, 4, 0),()),
		"UseMotion": ((1054, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((1065, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGroupGuideBody(DispatchBaseClass):
	'''MTT2D guide body group'''
	CLSID = IID('{1AB7F0EE-74C9-4EF7-89BF-14AAF15EF35E}')
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


	def SetSecondParametricPoint(self, pVal):
		'''
		Set second point
		
		:param pVal: IParametricPoint
		'''
		return self._oleobj_.InvokeTypes(1064, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def SetSecondPoint(self, dX, dY, dZ):
		'''
		Set second point
		
		:param dX: float
		:param dY: float
		:param dZ: float
		'''
		return self._oleobj_.InvokeTypes(1063, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1)),dX
			, dY, dZ)


	def SetStartParametricPoint(self, pVal):
		'''
		Set start point
		
		:param pVal: IParametricPoint
		'''
		return self._oleobj_.InvokeTypes(1062, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def SetStartPoint(self, dX, dY, dZ):
		'''
		Set start point
		
		:param dX: float
		:param dY: float
		:param dZ: float
		'''
		return self._oleobj_.InvokeTypes(1061, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1)),dX
			, dY, dZ)


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
	def _get_InertiaMoment(self):
		return self._ApplyTypes_(*(1055, 2, (9, 0), (), "InertiaMoment", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_JointPoint(self):
		return self._ApplyTypes_(*(1057, 2, (8197, 0), (), "JointPoint", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Mass(self):
		return self._ApplyTypes_(*(1054, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SecondPoint(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_StartPoint(self):
		return self._ApplyTypes_(*(1052, 2, (9, 0), (), "StartPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_TSD(self):
		return self._ApplyTypes_(*(1059, 2, (9, 0), (), "TSD", '{66947C3A-68E2-406E-9491-42952BD66A96}'))
	def _get_UseAutoCenterMarker(self):
		return self._ApplyTypes_(*(1060, 2, (11, 0), (), "UseAutoCenterMarker", None))
	def _get_UseJointPoint(self):
		return self._ApplyTypes_(*(1056, 2, (11, 0), (), "UseJointPoint", None))
	def _get_UseTSD(self):
		return self._ApplyTypes_(*(1058, 2, (11, 0), (), "UseTSD", None))
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
	def _set_JointPoint(self, value):
		if "JointPoint" in self.__dict__: self.__dict__["JointPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1057, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoCenterMarker(self, value):
		if "UseAutoCenterMarker" in self.__dict__: self.__dict__["UseAutoCenterMarker"] = value; return
		self._oleobj_.Invoke(*((1060, LCID, 4, 0) + (value,) + ()))
	def _set_UseJointPoint(self, value):
		if "UseJointPoint" in self.__dict__: self.__dict__["UseJointPoint"] = value; return
		self._oleobj_.Invoke(*((1056, LCID, 4, 0) + (value,) + ()))
	def _set_UseTSD(self, value):
		if "UseTSD" in self.__dict__: self.__dict__["UseTSD"] = value; return
		self._oleobj_.Invoke(*((1058, LCID, 4, 0) + (value,) + ()))
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
	InertiaMoment = property(_get_InertiaMoment, None)
	'''
	Izz, the mass moment of inertia in the z-axis of the roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	JointPoint = property(_get_JointPoint, _set_JointPoint)
	'''
	The position of revolute joint

	:type: list[float]
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	Mass = property(_get_Mass, None)
	'''
	The mass of guide body

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
	Radius = property(_get_Radius, None)
	'''
	The radius of guide body

	:type: recurdyn.ProcessNet.IDouble
	'''
	SecondPoint = property(_get_SecondPoint, None)
	'''
	The end point of guide body

	:type: recurdyn.ProcessNet.IVector
	'''
	StartPoint = property(_get_StartPoint, None)
	'''
	The start point of guide body

	:type: recurdyn.ProcessNet.IVector
	'''
	TSD = property(_get_TSD, None)
	'''
	Translational spring damper force

	:type: recurdyn.MTT2D.IMTT2DForceSpringTSD
	'''
	UseAutoCenterMarker = property(_get_UseAutoCenterMarker, _set_UseAutoCenterMarker)
	'''
	Match center marker automatically

	:type: bool
	'''
	UseJointPoint = property(_get_UseJointPoint, _set_UseJointPoint)
	'''
	Use joint point

	:type: bool
	'''
	UseTSD = property(_get_UseTSD, _set_UseTSD)
	'''
	Use TSD

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
		"_set_JointPoint": _set_JointPoint,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseAutoCenterMarker": _set_UseAutoCenterMarker,
		"_set_UseJointPoint": _set_UseJointPoint,
		"_set_UseTSD": _set_UseTSD,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InertiaMoment": (1055, 2, (9, 0), (), "InertiaMoment", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"JointPoint": (1057, 2, (8197, 0), (), "JointPoint", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Mass": (1054, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (1051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SecondPoint": (1053, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"StartPoint": (1052, 2, (9, 0), (), "StartPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"TSD": (1059, 2, (9, 0), (), "TSD", '{66947C3A-68E2-406E-9491-42952BD66A96}'),
		"UseAutoCenterMarker": (1060, 2, (11, 0), (), "UseAutoCenterMarker", None),
		"UseJointPoint": (1056, 2, (11, 0), (), "UseJointPoint", None),
		"UseTSD": (1058, 2, (11, 0), (), "UseTSD", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"JointPoint": ((1057, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseAutoCenterMarker": ((1060, LCID, 4, 0),()),
		"UseJointPoint": ((1056, LCID, 4, 0),()),
		"UseTSD": ((1058, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGroupMovableRoller(DispatchBaseClass):
	'''MTT2D movable roller group'''
	CLSID = IID('{D4F728AD-8867-4AA8-B319-88687F79C526}')
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
		return self._oleobj_.InvokeTypes(1073, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Angle(self):
		return self._ApplyTypes_(*(1075, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPointsToRoller(self):
		return self._ApplyTypes_(*(1088, 2, (9, 0), (), "ContactPointsToRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPointsToSheet(self):
		return self._ApplyTypes_(*(1087, 2, (9, 0), (), "ContactPointsToSheet", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToFixedRoller(self):
		return self._ApplyTypes_(*(1061, 2, (9, 0), (), "ContactPropertyToFixedRoller", '{B006CA26-0F57-4100-9224-D3D62429E8F6}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(1060, 2, (9, 0), (), "ContactPropertyToSheet", '{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}'))
	def _get_Direction(self):
		return self._ApplyTypes_(*(1052, 2, (8197, 0), (), "Direction", None))
	def _get_DirectionEx(self):
		return self._ApplyTypes_(*(1074, 2, (9, 0), (), "DirectionEx", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_DirectionType(self):
		return self._ApplyTypes_(*(1076, 2, (3, 0), (), "DirectionType", '{21BC4DDF-6454-4049-A7E7-797B0FD7A54F}'))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_ForceDisplayToRoller(self):
		return self._ApplyTypes_(*(1086, 2, (3, 0), (), "ForceDisplayToRoller", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayToSheet(self):
		return self._ApplyTypes_(*(1085, 2, (3, 0), (), "ForceDisplayToSheet", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupFixedRoller(self):
		return self._ApplyTypes_(*(1083, 2, (9, 0), (), "GroupFixedRoller", '{979CB058-D7B2-4D8B-9EA5-26C16B8C5547}'))
	def _get_Inertia(self):
		return self._ApplyTypes_(*(1055, 2, (9, 0), (), "Inertia", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InitialGap(self):
		return self._ApplyTypes_(*(1057, 2, (5, 0), (), "InitialGap", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_Mass(self):
		return self._ApplyTypes_(*(1054, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumGap(self):
		return self._ApplyTypes_(*(1067, 2, (9, 0), (), "MaximumGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Motion(self):
		return self._ApplyTypes_(*(1059, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NipSpring(self):
		return self._ApplyTypes_(*(1063, 2, (9, 0), (), "NipSpring", '{4A4DE5B0-59EF-4CD2-B669-93768E326904}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RARBody(self):
		return self._ApplyTypes_(*(1079, 2, (9, 0), (), "RARBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RevJoint(self):
		return self._ApplyTypes_(*(1080, 2, (9, 0), (), "RevJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_RollerBody(self):
		return self._ApplyTypes_(*(1078, 2, (9, 0), (), "RollerBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_RollerBodyType(self):
		return self._ApplyTypes_(*(1070, 2, (3, 0), (), "RollerBodyType", '{965EA0D7-3B24-4C39-87DD-0E6C1EA1CA47}'))
	def _get_SoftNip(self):
		return self._ApplyTypes_(*(1065, 2, (9, 0), (), "SoftNip", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_SpecialContactPointsToRoller(self):
		return self._ApplyTypes_(*(1090, 2, (9, 0), (), "SpecialContactPointsToRoller", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialContactPointsToSheet(self):
		return self._ApplyTypes_(*(1089, 2, (9, 0), (), "SpecialContactPointsToSheet", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpringForce(self):
		return self._ApplyTypes_(*(1082, 2, (9, 0), (), "SpringForce", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_TraJoint(self):
		return self._ApplyTypes_(*(1081, 2, (9, 0), (), "TraJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_TranslationalDirectionAngle(self):
		return self._ApplyTypes_(*(1084, 2, (9, 0), (), "TranslationalDirectionAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseAutoCenterMarker(self):
		return self._ApplyTypes_(*(1068, 2, (11, 0), (), "UseAutoCenterMarker", None))
	def _get_UseAutoUpdateGeometry(self):
		return self._ApplyTypes_(*(1077, 2, (11, 0), (), "UseAutoUpdateGeometry", None))
	def _get_UseInitialGap(self):
		return self._ApplyTypes_(*(1056, 2, (11, 0), (), "UseInitialGap", None))
	def _get_UseMaximumGap(self):
		return self._ApplyTypes_(*(1066, 2, (11, 0), (), "UseMaximumGap", None))
	def _get_UseMotion(self):
		return self._ApplyTypes_(*(1058, 2, (11, 0), (), "UseMotion", None))
	def _get_UseNipSpring(self):
		return self._ApplyTypes_(*(1062, 2, (11, 0), (), "UseNipSpring", None))
	def _get_UseSoftNip(self):
		return self._ApplyTypes_(*(1064, 2, (11, 0), (), "UseSoftNip", None))
	def _get_UseSpecialContactPointsToRoller(self):
		return self._ApplyTypes_(*(1092, 2, (11, 0), (), "UseSpecialContactPointsToRoller", None))
	def _get_UseSpecialContactPointsToSheet(self):
		return self._ApplyTypes_(*(1091, 2, (11, 0), (), "UseSpecialContactPointsToSheet", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Direction(self, value):
		if "Direction" in self.__dict__: self.__dict__["Direction"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1052, LCID, 4, 0) + (variantValue,) + ()))
	def _set_DirectionType(self, value):
		if "DirectionType" in self.__dict__: self.__dict__["DirectionType"] = value; return
		self._oleobj_.Invoke(*((1076, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayToRoller(self, value):
		if "ForceDisplayToRoller" in self.__dict__: self.__dict__["ForceDisplayToRoller"] = value; return
		self._oleobj_.Invoke(*((1086, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayToSheet(self, value):
		if "ForceDisplayToSheet" in self.__dict__: self.__dict__["ForceDisplayToSheet"] = value; return
		self._oleobj_.Invoke(*((1085, LCID, 4, 0) + (value,) + ()))
	def _set_InitialGap(self, value):
		if "InitialGap" in self.__dict__: self.__dict__["InitialGap"] = value; return
		self._oleobj_.Invoke(*((1057, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_SoftNip(self, value):
		if "SoftNip" in self.__dict__: self.__dict__["SoftNip"] = value; return
		self._oleobj_.Invoke(*((1065, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoCenterMarker(self, value):
		if "UseAutoCenterMarker" in self.__dict__: self.__dict__["UseAutoCenterMarker"] = value; return
		self._oleobj_.Invoke(*((1068, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoUpdateGeometry(self, value):
		if "UseAutoUpdateGeometry" in self.__dict__: self.__dict__["UseAutoUpdateGeometry"] = value; return
		self._oleobj_.Invoke(*((1077, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialGap(self, value):
		if "UseInitialGap" in self.__dict__: self.__dict__["UseInitialGap"] = value; return
		self._oleobj_.Invoke(*((1056, LCID, 4, 0) + (value,) + ()))
	def _set_UseMaximumGap(self, value):
		if "UseMaximumGap" in self.__dict__: self.__dict__["UseMaximumGap"] = value; return
		self._oleobj_.Invoke(*((1066, LCID, 4, 0) + (value,) + ()))
	def _set_UseMotion(self, value):
		if "UseMotion" in self.__dict__: self.__dict__["UseMotion"] = value; return
		self._oleobj_.Invoke(*((1058, LCID, 4, 0) + (value,) + ()))
	def _set_UseNipSpring(self, value):
		if "UseNipSpring" in self.__dict__: self.__dict__["UseNipSpring"] = value; return
		self._oleobj_.Invoke(*((1062, LCID, 4, 0) + (value,) + ()))
	def _set_UseSoftNip(self, value):
		if "UseSoftNip" in self.__dict__: self.__dict__["UseSoftNip"] = value; return
		self._oleobj_.Invoke(*((1064, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPointsToRoller(self, value):
		if "UseSpecialContactPointsToRoller" in self.__dict__: self.__dict__["UseSpecialContactPointsToRoller"] = value; return
		self._oleobj_.Invoke(*((1092, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPointsToSheet(self, value):
		if "UseSpecialContactPointsToSheet" in self.__dict__: self.__dict__["UseSpecialContactPointsToSheet"] = value; return
		self._oleobj_.Invoke(*((1091, LCID, 4, 0) + (value,) + ()))
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
	The angle of movable roller at the center point of fixed roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	BaseBody = property(_get_BaseBody, _set_BaseBody)
	'''
	The base body of the revolute joint

	:type: recurdyn.ProcessNet.IGeneric
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

	:type: recurdyn.MTT2D.IMTT2DContactPropertyRollerMovableToFixed
	'''
	ContactPropertyToSheet = property(_get_ContactPropertyToSheet, None)
	'''
	The parameters of contact forces applied between sheet and movable roller

	:type: recurdyn.MTT2D.IMTT2DContactPropertyRollerToSheet
	'''
	Direction = property(_get_Direction, _set_Direction)
	'''
	The direction of movable roller at the center point of fixed roller

	:type: list[float]
	'''
	DirectionEx = property(_get_DirectionEx, None)
	'''
	The direction of movable roller at the center point of fixed roller

	:type: recurdyn.ProcessNet.IVector
	'''
	DirectionType = property(_get_DirectionType, _set_DirectionType)
	'''
	Direction type

	:type: recurdyn.MTT2D.MovableRollerDirectionType
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
	GroupFixedRoller = property(_get_GroupFixedRoller, None)
	'''
	Get group fixed roller

	:type: recurdyn.ProcessNet.IGroup
	'''
	Inertia = property(_get_Inertia, None)
	'''
	Izz, the mass moment of inertia in the z-axis of the roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	InitialGap = property(_get_InitialGap, _set_InitialGap)
	'''
	The initial gap between fixed roller and movable roller

	:type: float
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

	:type: recurdyn.MTT2D.IMTT2DForceSpringNip
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
	RollerBodyType = property(_get_RollerBodyType, None)
	'''
	Roller body type

	:type: recurdyn.MTT2D.RollerBodyType
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
	UseAutoUpdateGeometry = property(_get_UseAutoUpdateGeometry, _set_UseAutoUpdateGeometry)
	'''
	Update geometry automatically

	:type: bool
	'''
	UseInitialGap = property(_get_UseInitialGap, _set_UseInitialGap)
	'''
	Use initial gap

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
		"_set_Comment": _set_Comment,
		"_set_Direction": _set_Direction,
		"_set_DirectionType": _set_DirectionType,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_ForceDisplayToRoller": _set_ForceDisplayToRoller,
		"_set_ForceDisplayToSheet": _set_ForceDisplayToSheet,
		"_set_InitialGap": _set_InitialGap,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_SoftNip": _set_SoftNip,
		"_set_UseAutoCenterMarker": _set_UseAutoCenterMarker,
		"_set_UseAutoUpdateGeometry": _set_UseAutoUpdateGeometry,
		"_set_UseInitialGap": _set_UseInitialGap,
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
		"Angle": (1075, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"BaseBody": (1051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPointsToRoller": (1088, 2, (9, 0), (), "ContactPointsToRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPointsToSheet": (1087, 2, (9, 0), (), "ContactPointsToSheet", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToFixedRoller": (1061, 2, (9, 0), (), "ContactPropertyToFixedRoller", '{B006CA26-0F57-4100-9224-D3D62429E8F6}'),
		"ContactPropertyToSheet": (1060, 2, (9, 0), (), "ContactPropertyToSheet", '{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}'),
		"Direction": (1052, 2, (8197, 0), (), "Direction", None),
		"DirectionEx": (1074, 2, (9, 0), (), "DirectionEx", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"DirectionType": (1076, 2, (3, 0), (), "DirectionType", '{21BC4DDF-6454-4049-A7E7-797B0FD7A54F}'),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"ForceDisplayToRoller": (1086, 2, (3, 0), (), "ForceDisplayToRoller", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayToSheet": (1085, 2, (3, 0), (), "ForceDisplayToSheet", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupFixedRoller": (1083, 2, (9, 0), (), "GroupFixedRoller", '{979CB058-D7B2-4D8B-9EA5-26C16B8C5547}'),
		"Inertia": (1055, 2, (9, 0), (), "Inertia", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InitialGap": (1057, 2, (5, 0), (), "InitialGap", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Mass": (1054, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumGap": (1067, 2, (9, 0), (), "MaximumGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Motion": (1059, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NipSpring": (1063, 2, (9, 0), (), "NipSpring", '{4A4DE5B0-59EF-4CD2-B669-93768E326904}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RARBody": (1079, 2, (9, 0), (), "RARBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Radius": (1053, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RevJoint": (1080, 2, (9, 0), (), "RevJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"RollerBody": (1078, 2, (9, 0), (), "RollerBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"RollerBodyType": (1070, 2, (3, 0), (), "RollerBodyType", '{965EA0D7-3B24-4C39-87DD-0E6C1EA1CA47}'),
		"SoftNip": (1065, 2, (9, 0), (), "SoftNip", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"SpecialContactPointsToRoller": (1090, 2, (9, 0), (), "SpecialContactPointsToRoller", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialContactPointsToSheet": (1089, 2, (9, 0), (), "SpecialContactPointsToSheet", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpringForce": (1082, 2, (9, 0), (), "SpringForce", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"TraJoint": (1081, 2, (9, 0), (), "TraJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"TranslationalDirectionAngle": (1084, 2, (9, 0), (), "TranslationalDirectionAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseAutoCenterMarker": (1068, 2, (11, 0), (), "UseAutoCenterMarker", None),
		"UseAutoUpdateGeometry": (1077, 2, (11, 0), (), "UseAutoUpdateGeometry", None),
		"UseInitialGap": (1056, 2, (11, 0), (), "UseInitialGap", None),
		"UseMaximumGap": (1066, 2, (11, 0), (), "UseMaximumGap", None),
		"UseMotion": (1058, 2, (11, 0), (), "UseMotion", None),
		"UseNipSpring": (1062, 2, (11, 0), (), "UseNipSpring", None),
		"UseSoftNip": (1064, 2, (11, 0), (), "UseSoftNip", None),
		"UseSpecialContactPointsToRoller": (1092, 2, (11, 0), (), "UseSpecialContactPointsToRoller", None),
		"UseSpecialContactPointsToSheet": (1091, 2, (11, 0), (), "UseSpecialContactPointsToSheet", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((1051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Direction": ((1052, LCID, 4, 0),()),
		"DirectionType": ((1076, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"ForceDisplayToRoller": ((1086, LCID, 4, 0),()),
		"ForceDisplayToSheet": ((1085, LCID, 4, 0),()),
		"InitialGap": ((1057, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"SoftNip": ((1065, LCID, 4, 0),()),
		"UseAutoCenterMarker": ((1068, LCID, 4, 0),()),
		"UseAutoUpdateGeometry": ((1077, LCID, 4, 0),()),
		"UseInitialGap": ((1056, LCID, 4, 0),()),
		"UseMaximumGap": ((1066, LCID, 4, 0),()),
		"UseMotion": ((1058, LCID, 4, 0),()),
		"UseNipSpring": ((1062, LCID, 4, 0),()),
		"UseSoftNip": ((1064, LCID, 4, 0),()),
		"UseSpecialContactPointsToRoller": ((1092, LCID, 4, 0),()),
		"UseSpecialContactPointsToSheet": ((1091, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGroupMovableRollerShell(DispatchBaseClass):
	'''MTT2D movable shell roller group'''
	CLSID = IID('{2310F73F-2BE6-4338-93FF-609E572F4802}')
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
		return self._oleobj_.InvokeTypes(1070, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPointsToRoller(self):
		return self._ApplyTypes_(*(1078, 2, (9, 0), (), "ContactPointsToRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPointsToSheet(self):
		return self._ApplyTypes_(*(1077, 2, (9, 0), (), "ContactPointsToSheet", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToFixedRoller(self):
		return self._ApplyTypes_(*(1061, 2, (9, 0), (), "ContactPropertyToFixedRoller", '{B006CA26-0F57-4100-9224-D3D62429E8F6}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(1060, 2, (9, 0), (), "ContactPropertyToSheet", '{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}'))
	def _get_DirectionAngle(self):
		return self._ApplyTypes_(*(1054, 2, (9, 0), (), "DirectionAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DirectionPoint(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "DirectionPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_DirectionType(self):
		return self._ApplyTypes_(*(1052, 2, (3, 0), (), "DirectionType", '{21BC4DDF-6454-4049-A7E7-797B0FD7A54F}'))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_FlexBody(self):
		return self._ApplyTypes_(*(1074, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'))
	def _get_FlexibleRollerProperty(self):
		return self._ApplyTypes_(*(1069, 2, (9, 0), (), "FlexibleRollerProperty", '{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}'))
	def _get_ForceDisplayToRoller(self):
		return self._ApplyTypes_(*(1076, 2, (3, 0), (), "ForceDisplayToRoller", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayToSheet(self):
		return self._ApplyTypes_(*(1075, 2, (3, 0), (), "ForceDisplayToSheet", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupFixedRoller(self):
		return self._ApplyTypes_(*(1071, 2, (9, 0), (), "GroupFixedRoller", '{979CB058-D7B2-4D8B-9EA5-26C16B8C5547}'))
	def _get_InitialGap(self):
		return self._ApplyTypes_(*(1057, 2, (5, 0), (), "InitialGap", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MaximumGap(self):
		return self._ApplyTypes_(*(1067, 2, (9, 0), (), "MaximumGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Motion(self):
		return self._ApplyTypes_(*(1059, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NipSpring(self):
		return self._ApplyTypes_(*(1063, 2, (9, 0), (), "NipSpring", '{4A4DE5B0-59EF-4CD2-B669-93768E326904}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(1055, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SoftNip(self):
		return self._ApplyTypes_(*(1065, 2, (9, 0), (), "SoftNip", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_SpecialContactPointsToRoller(self):
		return self._ApplyTypes_(*(1080, 2, (9, 0), (), "SpecialContactPointsToRoller", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialContactPointsToSheet(self):
		return self._ApplyTypes_(*(1079, 2, (9, 0), (), "SpecialContactPointsToSheet", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_TranslationalDirectionAngle(self):
		return self._ApplyTypes_(*(1073, 2, (9, 0), (), "TranslationalDirectionAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseAutoCenterMarker(self):
		return self._ApplyTypes_(*(1068, 2, (11, 0), (), "UseAutoCenterMarker", None))
	def _get_UseInitialGap(self):
		return self._ApplyTypes_(*(1056, 2, (11, 0), (), "UseInitialGap", None))
	def _get_UseMaximumGap(self):
		return self._ApplyTypes_(*(1066, 2, (11, 0), (), "UseMaximumGap", None))
	def _get_UseMotion(self):
		return self._ApplyTypes_(*(1058, 2, (11, 0), (), "UseMotion", None))
	def _get_UseNipSpring(self):
		return self._ApplyTypes_(*(1062, 2, (11, 0), (), "UseNipSpring", None))
	def _get_UseSoftNip(self):
		return self._ApplyTypes_(*(1064, 2, (11, 0), (), "UseSoftNip", None))
	def _get_UseSpecialContactPointsToRoller(self):
		return self._ApplyTypes_(*(1082, 2, (11, 0), (), "UseSpecialContactPointsToRoller", None))
	def _get_UseSpecialContactPointsToSheet(self):
		return self._ApplyTypes_(*(1081, 2, (11, 0), (), "UseSpecialContactPointsToSheet", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((1051, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DirectionType(self, value):
		if "DirectionType" in self.__dict__: self.__dict__["DirectionType"] = value; return
		self._oleobj_.Invoke(*((1052, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayToRoller(self, value):
		if "ForceDisplayToRoller" in self.__dict__: self.__dict__["ForceDisplayToRoller"] = value; return
		self._oleobj_.Invoke(*((1076, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplayToSheet(self, value):
		if "ForceDisplayToSheet" in self.__dict__: self.__dict__["ForceDisplayToSheet"] = value; return
		self._oleobj_.Invoke(*((1075, LCID, 4, 0) + (value,) + ()))
	def _set_InitialGap(self, value):
		if "InitialGap" in self.__dict__: self.__dict__["InitialGap"] = value; return
		self._oleobj_.Invoke(*((1057, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_SoftNip(self, value):
		if "SoftNip" in self.__dict__: self.__dict__["SoftNip"] = value; return
		self._oleobj_.Invoke(*((1065, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoCenterMarker(self, value):
		if "UseAutoCenterMarker" in self.__dict__: self.__dict__["UseAutoCenterMarker"] = value; return
		self._oleobj_.Invoke(*((1068, LCID, 4, 0) + (value,) + ()))
	def _set_UseExtractWithoutPreStress(self, value):
		if "UseExtractWithoutPreStress" in self.__dict__: self.__dict__["UseExtractWithoutPreStress"] = value; return
		self._oleobj_.Invoke(*((1072, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialGap(self, value):
		if "UseInitialGap" in self.__dict__: self.__dict__["UseInitialGap"] = value; return
		self._oleobj_.Invoke(*((1056, LCID, 4, 0) + (value,) + ()))
	def _set_UseMaximumGap(self, value):
		if "UseMaximumGap" in self.__dict__: self.__dict__["UseMaximumGap"] = value; return
		self._oleobj_.Invoke(*((1066, LCID, 4, 0) + (value,) + ()))
	def _set_UseMotion(self, value):
		if "UseMotion" in self.__dict__: self.__dict__["UseMotion"] = value; return
		self._oleobj_.Invoke(*((1058, LCID, 4, 0) + (value,) + ()))
	def _set_UseNipSpring(self, value):
		if "UseNipSpring" in self.__dict__: self.__dict__["UseNipSpring"] = value; return
		self._oleobj_.Invoke(*((1062, LCID, 4, 0) + (value,) + ()))
	def _set_UseSoftNip(self, value):
		if "UseSoftNip" in self.__dict__: self.__dict__["UseSoftNip"] = value; return
		self._oleobj_.Invoke(*((1064, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPointsToRoller(self, value):
		if "UseSpecialContactPointsToRoller" in self.__dict__: self.__dict__["UseSpecialContactPointsToRoller"] = value; return
		self._oleobj_.Invoke(*((1082, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPointsToSheet(self, value):
		if "UseSpecialContactPointsToSheet" in self.__dict__: self.__dict__["UseSpecialContactPointsToSheet"] = value; return
		self._oleobj_.Invoke(*((1081, LCID, 4, 0) + (value,) + ()))
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

	:type: recurdyn.MTT2D.IMTT2DContactPropertyRollerMovableToFixed
	'''
	ContactPropertyToSheet = property(_get_ContactPropertyToSheet, None)
	'''
	The parameters of contact forces applied between sheet and movable roller

	:type: recurdyn.MTT2D.IMTT2DContactPropertyRollerToSheet
	'''
	DirectionAngle = property(_get_DirectionAngle, None)
	'''
	The angle of movable roller at the center point of fixed roller

	:type: recurdyn.ProcessNet.IDouble
	'''
	DirectionPoint = property(_get_DirectionPoint, None)
	'''
	The direction of movable roller at the center point of fixed roller

	:type: recurdyn.ProcessNet.IVector
	'''
	DirectionType = property(_get_DirectionType, _set_DirectionType)
	'''
	Direction type

	:type: recurdyn.MTT2D.MovableRollerDirectionType
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	FlexBody = property(_get_FlexBody, None)
	'''
	Flex body edit

	:type: recurdyn.FFlex.IFFlexToolkitBody
	'''
	FlexibleRollerProperty = property(_get_FlexibleRollerProperty, None)
	'''
	Flexible roller property

	:type: recurdyn.MTT2D.IMTT2DFlexibleRollerProperty
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
	GroupFixedRoller = property(_get_GroupFixedRoller, None)
	'''
	Get group fixed roller

	:type: recurdyn.ProcessNet.IGroup
	'''
	InitialGap = property(_get_InitialGap, _set_InitialGap)
	'''
	The initial gap between fixed roller and movable roller

	:type: float
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
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

	:type: recurdyn.MTT2D.IMTT2DForceSpringNip
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
	The radius of the movable roller

	:type: recurdyn.ProcessNet.IDouble
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
	UseInitialGap = property(_get_UseInitialGap, _set_UseInitialGap)
	'''
	Use initial gap

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
	UseExtractWithoutPreStress = property(None, _set_UseExtractWithoutPreStress)
	'''
	ExtractWithoutPreStress flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_BaseBody": _set_BaseBody,
		"_set_Comment": _set_Comment,
		"_set_DirectionType": _set_DirectionType,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_ForceDisplayToRoller": _set_ForceDisplayToRoller,
		"_set_ForceDisplayToSheet": _set_ForceDisplayToSheet,
		"_set_InitialGap": _set_InitialGap,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_SoftNip": _set_SoftNip,
		"_set_UseAutoCenterMarker": _set_UseAutoCenterMarker,
		"_set_UseExtractWithoutPreStress": _set_UseExtractWithoutPreStress,
		"_set_UseInitialGap": _set_UseInitialGap,
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
		"BaseBody": (1051, 2, (9, 0), (), "BaseBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPointsToRoller": (1078, 2, (9, 0), (), "ContactPointsToRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPointsToSheet": (1077, 2, (9, 0), (), "ContactPointsToSheet", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToFixedRoller": (1061, 2, (9, 0), (), "ContactPropertyToFixedRoller", '{B006CA26-0F57-4100-9224-D3D62429E8F6}'),
		"ContactPropertyToSheet": (1060, 2, (9, 0), (), "ContactPropertyToSheet", '{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}'),
		"DirectionAngle": (1054, 2, (9, 0), (), "DirectionAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DirectionPoint": (1053, 2, (9, 0), (), "DirectionPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"DirectionType": (1052, 2, (3, 0), (), "DirectionType", '{21BC4DDF-6454-4049-A7E7-797B0FD7A54F}'),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FlexBody": (1074, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'),
		"FlexibleRollerProperty": (1069, 2, (9, 0), (), "FlexibleRollerProperty", '{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}'),
		"ForceDisplayToRoller": (1076, 2, (3, 0), (), "ForceDisplayToRoller", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayToSheet": (1075, 2, (3, 0), (), "ForceDisplayToSheet", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupFixedRoller": (1071, 2, (9, 0), (), "GroupFixedRoller", '{979CB058-D7B2-4D8B-9EA5-26C16B8C5547}'),
		"InitialGap": (1057, 2, (5, 0), (), "InitialGap", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MaximumGap": (1067, 2, (9, 0), (), "MaximumGap", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Motion": (1059, 2, (9, 0), (), "Motion", '{47F4E55C-4291-4251-866A-98A74112D266}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NipSpring": (1063, 2, (9, 0), (), "NipSpring", '{4A4DE5B0-59EF-4CD2-B669-93768E326904}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (1055, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SoftNip": (1065, 2, (9, 0), (), "SoftNip", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"SpecialContactPointsToRoller": (1080, 2, (9, 0), (), "SpecialContactPointsToRoller", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialContactPointsToSheet": (1079, 2, (9, 0), (), "SpecialContactPointsToSheet", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"TranslationalDirectionAngle": (1073, 2, (9, 0), (), "TranslationalDirectionAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseAutoCenterMarker": (1068, 2, (11, 0), (), "UseAutoCenterMarker", None),
		"UseInitialGap": (1056, 2, (11, 0), (), "UseInitialGap", None),
		"UseMaximumGap": (1066, 2, (11, 0), (), "UseMaximumGap", None),
		"UseMotion": (1058, 2, (11, 0), (), "UseMotion", None),
		"UseNipSpring": (1062, 2, (11, 0), (), "UseNipSpring", None),
		"UseSoftNip": (1064, 2, (11, 0), (), "UseSoftNip", None),
		"UseSpecialContactPointsToRoller": (1082, 2, (11, 0), (), "UseSpecialContactPointsToRoller", None),
		"UseSpecialContactPointsToSheet": (1081, 2, (11, 0), (), "UseSpecialContactPointsToSheet", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((1051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DirectionType": ((1052, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"ForceDisplayToRoller": ((1076, LCID, 4, 0),()),
		"ForceDisplayToSheet": ((1075, LCID, 4, 0),()),
		"InitialGap": ((1057, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"SoftNip": ((1065, LCID, 4, 0),()),
		"UseAutoCenterMarker": ((1068, LCID, 4, 0),()),
		"UseExtractWithoutPreStress": ((1072, LCID, 4, 0),()),
		"UseInitialGap": ((1056, LCID, 4, 0),()),
		"UseMaximumGap": ((1066, LCID, 4, 0),()),
		"UseMotion": ((1058, LCID, 4, 0),()),
		"UseNipSpring": ((1062, LCID, 4, 0),()),
		"UseSoftNip": ((1064, LCID, 4, 0),()),
		"UseSpecialContactPointsToRoller": ((1082, LCID, 4, 0),()),
		"UseSpecialContactPointsToSheet": ((1081, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGroupSheet(DispatchBaseClass):
	'''MTT2D sheet group'''
	CLSID = IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddAllOutputSheet(self):
		'''
		Add all the sheet body to output list
		'''
		return self._oleobj_.InvokeTypes(1069, LCID, 1, (24, 0), (),)


	def AddOutputSheet(self, strFileName):
		'''
		Add a sheet body to output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(1067, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def GetOutputSheetList(self):
		'''
		Sheet body output list
		
		:rtype: list[str]
		'''
		return self._ApplyTypes_(1066, 1, (8200, 0), (), 'GetOutputSheetList', None,)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def RemoveAllOutputSheet(self):
		'''
		Remove all the sheet body from output list
		'''
		return self._oleobj_.InvokeTypes(1070, LCID, 1, (24, 0), (),)


	def RemoveOutputSheet(self, strFileName):
		'''
		Remove a sheet body from output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(1068, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def SetLayerNumber(self, iVal):
		'''
		Set layer number
		
		:param iVal: int
		'''
		return self._oleobj_.InvokeTypes(1025, LCID, 1, (24, 0), ((19, 1),),iVal
			)


	def UpdateActiveFlagOfAllEntities(self, val):
		'''
		Update active flag of all entities
		
		:param val: bool
		'''
		return self._oleobj_.InvokeTypes(1071, LCID, 1, (24, 0), ((11, 1),),val
			)


	def UpdateAllProperties(self):
		'''
		Update all properties
		'''
		return self._oleobj_.InvokeTypes(1054, LCID, 1, (24, 0), (),)


	def UpdateAllProperties2(self):
		'''
		Update all properties
		'''
		return self._oleobj_.InvokeTypes(1064, LCID, 1, (24, 0), (),)


	def UpdateNonGeometricProperties(self):
		'''
		Update non-geometric properties
		'''
		return self._oleobj_.InvokeTypes(1055, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_AirResistanceConstant(self):
		return self._ApplyTypes_(*(1058, 2, (9, 0), (), "AirResistanceConstant", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_AirResistanceExpression(self):
		return self._ApplyTypes_(*(1059, 2, (9, 0), (), "AirResistanceExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_AirResistanceType(self):
		return self._ApplyTypes_(*(1057, 2, (3, 0), (), "AirResistanceType", '{30770DB1-361B-40D9-895D-32D0523B640B}'))
	def _get_AllCurlRadius(self):
		return self._ApplyTypes_(*(1011, 2, (11, 0), (), "AllCurlRadius", None))
	def _get_AllDampingRatio(self):
		return self._ApplyTypes_(*(1010, 2, (11, 0), (), "AllDampingRatio", None))
	def _get_AllDensity(self):
		return self._ApplyTypes_(*(1008, 2, (11, 0), (), "AllDensity", None))
	def _get_AllYoungsModulus(self):
		return self._ApplyTypes_(*(1009, 2, (11, 0), (), "AllYoungsModulus", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_CurlRadius(self):
		return self._ApplyTypes_(*(1019, 2, (9, 0), (), "CurlRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(1018, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(1016, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DirectionPoint(self):
		return self._ApplyTypes_(*(1002, 2, (8197, 0), (), "DirectionPoint", None))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(1065, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_Fold(self):
		return self._ApplyTypes_(*(1003, 2, (11, 0), (), "Fold", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_HoldNoise(self):
		return self._ApplyTypes_(*(1053, 2, (11, 0), (), "HoldNoise", None))
	def _get_InitialVelocity(self):
		return self._ApplyTypes_(*(1007, 2, (9, 0), (), "InitialVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
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
	def _get_PlanarJoint(self):
		return self._ApplyTypes_(*(1062, 2, (9, 0), (), "PlanarJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_PointList(self):
		return self._ApplyTypes_(*(1004, 2, (8204, 0), (), "PointList", None))
	def _get_RevoluteJointCollection(self):
		return self._ApplyTypes_(*(1061, 2, (9, 0), (), "RevoluteJointCollection", '{AFC279E7-53CD-4DA1-96E2-3833740C410A}'))
	def _get_RotationalSpringCollection(self):
		return self._ApplyTypes_(*(1063, 2, (9, 0), (), "RotationalSpringCollection", '{F38F6090-E64E-4BA5-96B1-9865E77C4B31}'))
	def _get_SegmentLength(self):
		return self._ApplyTypes_(*(1052, 2, (9, 0), (), "SegmentLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SegmentNumber(self):
		return self._ApplyTypes_(*(1051, 2, (3, 0), (), "SegmentNumber", None))
	def _get_SheetBodyCollection(self):
		return self._ApplyTypes_(*(1060, 2, (9, 0), (), "SheetBodyCollection", '{767F4D3F-26B8-4F0A-B982-9A7FAC6CD1B2}'))
	def _get_SpecialCurlRadius(self):
		return self._ApplyTypes_(*(1023, 2, (9, 0), (), "SpecialCurlRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialDampingRatio(self):
		return self._ApplyTypes_(*(1022, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialDensity(self):
		return self._ApplyTypes_(*(1020, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThickness(self):
		return self._ApplyTypes_(*(1026, 2, (9, 0), (), "SpecialThickness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialYoungsModulus(self):
		return self._ApplyTypes_(*(1021, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_StartPoint(self):
		return self._ApplyTypes_(*(1001, 2, (8197, 0), (), "StartPoint", None))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseAirResistance(self):
		return self._ApplyTypes_(*(1056, 2, (11, 0), (), "UseAirResistance", None))
	def _get_UseInitialVelocity(self):
		return self._ApplyTypes_(*(1006, 2, (11, 0), (), "UseInitialVelocity", None))
	def _get_UseSpecialCurlRadius(self):
		return self._ApplyTypes_(*(1015, 2, (11, 0), (), "UseSpecialCurlRadius", None))
	def _get_UseSpecialDampingRatio(self):
		return self._ApplyTypes_(*(1014, 2, (11, 0), (), "UseSpecialDampingRatio", None))
	def _get_UseSpecialDensity(self):
		return self._ApplyTypes_(*(1012, 2, (11, 0), (), "UseSpecialDensity", None))
	def _get_UseSpecialThickness(self):
		return self._ApplyTypes_(*(1024, 2, (11, 0), (), "UseSpecialThickness", None))
	def _get_UseSpecialYoungsModulus(self):
		return self._ApplyTypes_(*(1013, 2, (11, 0), (), "UseSpecialYoungsModulus", None))
	def _get_UseUpdateGeometryAutomatically(self):
		return self._ApplyTypes_(*(1027, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(1017, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_AirResistanceExpression(self, value):
		if "AirResistanceExpression" in self.__dict__: self.__dict__["AirResistanceExpression"] = value; return
		self._oleobj_.Invoke(*((1059, LCID, 4, 0) + (value,) + ()))
	def _set_AirResistanceType(self, value):
		if "AirResistanceType" in self.__dict__: self.__dict__["AirResistanceType"] = value; return
		self._oleobj_.Invoke(*((1057, LCID, 4, 0) + (value,) + ()))
	def _set_AllCurlRadius(self, value):
		if "AllCurlRadius" in self.__dict__: self.__dict__["AllCurlRadius"] = value; return
		self._oleobj_.Invoke(*((1011, LCID, 4, 0) + (value,) + ()))
	def _set_AllDampingRatio(self, value):
		if "AllDampingRatio" in self.__dict__: self.__dict__["AllDampingRatio"] = value; return
		self._oleobj_.Invoke(*((1010, LCID, 4, 0) + (value,) + ()))
	def _set_AllDensity(self, value):
		if "AllDensity" in self.__dict__: self.__dict__["AllDensity"] = value; return
		self._oleobj_.Invoke(*((1008, LCID, 4, 0) + (value,) + ()))
	def _set_AllYoungsModulus(self, value):
		if "AllYoungsModulus" in self.__dict__: self.__dict__["AllYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((1009, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DirectionPoint(self, value):
		if "DirectionPoint" in self.__dict__: self.__dict__["DirectionPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (variantValue,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((1065, LCID, 4, 0) + (value,) + ()))
	def _set_HoldNoise(self, value):
		if "HoldNoise" in self.__dict__: self.__dict__["HoldNoise"] = value; return
		self._oleobj_.Invoke(*((1053, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_PointList(self, value):
		if "PointList" in self.__dict__: self.__dict__["PointList"] = value; return
		_value_type = True if value and isinstance(value[0], win32com.client.VARIANT) else False
		if not _value_type:
			value = [win32com.client.VARIANT(12, _data) for _data in value]
		variantValue = win32com.client.VARIANT(8204, value)
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (variantValue,) + ()))
		if not _value_type:
			value = [_data.value for _data in value]
	def _set_StartPoint(self, value):
		if "StartPoint" in self.__dict__: self.__dict__["StartPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseAirResistance(self, value):
		if "UseAirResistance" in self.__dict__: self.__dict__["UseAirResistance"] = value; return
		self._oleobj_.Invoke(*((1056, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialVelocity(self, value):
		if "UseInitialVelocity" in self.__dict__: self.__dict__["UseInitialVelocity"] = value; return
		self._oleobj_.Invoke(*((1006, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialCurlRadius(self, value):
		if "UseSpecialCurlRadius" in self.__dict__: self.__dict__["UseSpecialCurlRadius"] = value; return
		self._oleobj_.Invoke(*((1015, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDampingRatio(self, value):
		if "UseSpecialDampingRatio" in self.__dict__: self.__dict__["UseSpecialDampingRatio"] = value; return
		self._oleobj_.Invoke(*((1014, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDensity(self, value):
		if "UseSpecialDensity" in self.__dict__: self.__dict__["UseSpecialDensity"] = value; return
		self._oleobj_.Invoke(*((1012, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThickness(self, value):
		if "UseSpecialThickness" in self.__dict__: self.__dict__["UseSpecialThickness"] = value; return
		self._oleobj_.Invoke(*((1024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialYoungsModulus(self, value):
		if "UseSpecialYoungsModulus" in self.__dict__: self.__dict__["UseSpecialYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((1013, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdateGeometryAutomatically(self, value):
		if "UseUpdateGeometryAutomatically" in self.__dict__: self.__dict__["UseUpdateGeometryAutomatically"] = value; return
		self._oleobj_.Invoke(*((1027, LCID, 4, 0) + (value,) + ()))
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

	:type: recurdyn.MTT2D.AirResistanceType
	'''
	AllCurlRadius = property(_get_AllCurlRadius, _set_AllCurlRadius)
	'''
	Use all curl radius

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
	AllYoungsModulus = property(_get_AllYoungsModulus, _set_AllYoungsModulus)
	'''
	Use all young's modulus

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	CurlRadius = property(_get_CurlRadius, None)
	'''
	The sheet bends with a curvature that matches the curl radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingRatio = property(_get_DampingRatio, None)
	'''
	Damping ratio of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	Density = property(_get_Density, None)
	'''
	The area density of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	DirectionPoint = property(_get_DirectionPoint, _set_DirectionPoint)
	'''
	The direction point of the sheet

	:type: list[float]
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	Fold = property(_get_Fold, None)
	'''
	True: folding sheet, False: flat sheet

	:type: bool
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	HoldNoise = property(_get_HoldNoise, _set_HoldNoise)
	'''
	Hold down the noise of sheet contact forces

	:type: bool
	'''
	InitialVelocity = property(_get_InitialVelocity, None)
	'''
	The initial velocity of a sheet is in the direction of positive X axis of the markers on each sheet body

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
	PlanarJoint = property(_get_PlanarJoint, None)
	'''
	The planar joint

	:type: recurdyn.ProcessNet.IGeneric
	'''
	PointList = property(_get_PointList, _set_PointList)
	'''
	A sheet folds through this points

	:type: list[object]
	'''
	RevoluteJointCollection = property(_get_RevoluteJointCollection, None)
	'''
	Revolute joints

	:type: recurdyn.MTT2D.IMTT2DSheetRevJointCollection
	'''
	RotationalSpringCollection = property(_get_RotationalSpringCollection, None)
	'''
	Rotational spring forces

	:type: recurdyn.MTT2D.IMTT2DSheetRotSpringCollection
	'''
	SegmentLength = property(_get_SegmentLength, None)
	'''
	The length of each sheet segment

	:type: recurdyn.ProcessNet.IDouble
	'''
	SegmentNumber = property(_get_SegmentNumber, None)
	'''
	The number of segments in a sheet

	:type: int
	'''
	SheetBodyCollection = property(_get_SheetBodyCollection, None)
	'''
	Sheet bodies

	:type: recurdyn.MTT2D.IMTT2DSheetBodyCollection
	'''
	SpecialCurlRadius = property(_get_SpecialCurlRadius, None)
	'''
	Special curl radius

	:type: recurdyn.ProcessNet.ISpecialParametricValue
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
	SpecialThickness = property(_get_SpecialThickness, None)
	'''
	Special Thickness

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialYoungsModulus = property(_get_SpecialYoungsModulus, None)
	'''
	Special young's modulus

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
	UseSpecialCurlRadius = property(_get_UseSpecialCurlRadius, _set_UseSpecialCurlRadius)
	'''
	Use special curl radius

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
	UseSpecialThickness = property(_get_UseSpecialThickness, _set_UseSpecialThickness)
	'''
	Use special thickness

	:type: bool
	'''
	UseSpecialYoungsModulus = property(_get_UseSpecialYoungsModulus, _set_UseSpecialYoungsModulus)
	'''
	Use special young's modulus

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
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	Young's modulus of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_AirResistanceExpression": _set_AirResistanceExpression,
		"_set_AirResistanceType": _set_AirResistanceType,
		"_set_AllCurlRadius": _set_AllCurlRadius,
		"_set_AllDampingRatio": _set_AllDampingRatio,
		"_set_AllDensity": _set_AllDensity,
		"_set_AllYoungsModulus": _set_AllYoungsModulus,
		"_set_Comment": _set_Comment,
		"_set_DirectionPoint": _set_DirectionPoint,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_HoldNoise": _set_HoldNoise,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_PointList": _set_PointList,
		"_set_StartPoint": _set_StartPoint,
		"_set_UseAirResistance": _set_UseAirResistance,
		"_set_UseInitialVelocity": _set_UseInitialVelocity,
		"_set_UseSpecialCurlRadius": _set_UseSpecialCurlRadius,
		"_set_UseSpecialDampingRatio": _set_UseSpecialDampingRatio,
		"_set_UseSpecialDensity": _set_UseSpecialDensity,
		"_set_UseSpecialThickness": _set_UseSpecialThickness,
		"_set_UseSpecialYoungsModulus": _set_UseSpecialYoungsModulus,
		"_set_UseUpdateGeometryAutomatically": _set_UseUpdateGeometryAutomatically,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"AirResistanceConstant": (1058, 2, (9, 0), (), "AirResistanceConstant", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"AirResistanceExpression": (1059, 2, (9, 0), (), "AirResistanceExpression", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"AirResistanceType": (1057, 2, (3, 0), (), "AirResistanceType", '{30770DB1-361B-40D9-895D-32D0523B640B}'),
		"AllCurlRadius": (1011, 2, (11, 0), (), "AllCurlRadius", None),
		"AllDampingRatio": (1010, 2, (11, 0), (), "AllDampingRatio", None),
		"AllDensity": (1008, 2, (11, 0), (), "AllDensity", None),
		"AllYoungsModulus": (1009, 2, (11, 0), (), "AllYoungsModulus", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"CurlRadius": (1019, 2, (9, 0), (), "CurlRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingRatio": (1018, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (1016, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DirectionPoint": (1002, 2, (8197, 0), (), "DirectionPoint", None),
		"EachRenderMode": (1065, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"Fold": (1003, 2, (11, 0), (), "Fold", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"HoldNoise": (1053, 2, (11, 0), (), "HoldNoise", None),
		"InitialVelocity": (1007, 2, (9, 0), (), "InitialVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PlanarJoint": (1062, 2, (9, 0), (), "PlanarJoint", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"PointList": (1004, 2, (8204, 0), (), "PointList", None),
		"RevoluteJointCollection": (1061, 2, (9, 0), (), "RevoluteJointCollection", '{AFC279E7-53CD-4DA1-96E2-3833740C410A}'),
		"RotationalSpringCollection": (1063, 2, (9, 0), (), "RotationalSpringCollection", '{F38F6090-E64E-4BA5-96B1-9865E77C4B31}'),
		"SegmentLength": (1052, 2, (9, 0), (), "SegmentLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SegmentNumber": (1051, 2, (3, 0), (), "SegmentNumber", None),
		"SheetBodyCollection": (1060, 2, (9, 0), (), "SheetBodyCollection", '{767F4D3F-26B8-4F0A-B982-9A7FAC6CD1B2}'),
		"SpecialCurlRadius": (1023, 2, (9, 0), (), "SpecialCurlRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialDampingRatio": (1022, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialDensity": (1020, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThickness": (1026, 2, (9, 0), (), "SpecialThickness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialYoungsModulus": (1021, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"StartPoint": (1001, 2, (8197, 0), (), "StartPoint", None),
		"Thickness": (1005, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseAirResistance": (1056, 2, (11, 0), (), "UseAirResistance", None),
		"UseInitialVelocity": (1006, 2, (11, 0), (), "UseInitialVelocity", None),
		"UseSpecialCurlRadius": (1015, 2, (11, 0), (), "UseSpecialCurlRadius", None),
		"UseSpecialDampingRatio": (1014, 2, (11, 0), (), "UseSpecialDampingRatio", None),
		"UseSpecialDensity": (1012, 2, (11, 0), (), "UseSpecialDensity", None),
		"UseSpecialThickness": (1024, 2, (11, 0), (), "UseSpecialThickness", None),
		"UseSpecialYoungsModulus": (1013, 2, (11, 0), (), "UseSpecialYoungsModulus", None),
		"UseUpdateGeometryAutomatically": (1027, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"YoungsModulus": (1017, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"AirResistanceExpression": ((1059, LCID, 4, 0),()),
		"AirResistanceType": ((1057, LCID, 4, 0),()),
		"AllCurlRadius": ((1011, LCID, 4, 0),()),
		"AllDampingRatio": ((1010, LCID, 4, 0),()),
		"AllDensity": ((1008, LCID, 4, 0),()),
		"AllYoungsModulus": ((1009, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DirectionPoint": ((1002, LCID, 4, 0),()),
		"EachRenderMode": ((1065, LCID, 4, 0),()),
		"HoldNoise": ((1053, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"PointList": ((1004, LCID, 4, 0),()),
		"StartPoint": ((1001, LCID, 4, 0),()),
		"UseAirResistance": ((1056, LCID, 4, 0),()),
		"UseInitialVelocity": ((1006, LCID, 4, 0),()),
		"UseSpecialCurlRadius": ((1015, LCID, 4, 0),()),
		"UseSpecialDampingRatio": ((1014, LCID, 4, 0),()),
		"UseSpecialDensity": ((1012, LCID, 4, 0),()),
		"UseSpecialThickness": ((1024, LCID, 4, 0),()),
		"UseSpecialYoungsModulus": ((1013, LCID, 4, 0),()),
		"UseUpdateGeometryAutomatically": ((1027, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGroupSheetCollection(DispatchBaseClass):
	'''IMTT2DGroupSheetCollection'''
	CLSID = IID('{6DAA417B-BEE4-49CE-AD91-195F1AA003EF}')
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
		:rtype: recurdyn.MTT2D.IMTT2DGroupSheet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
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
		:rtype: recurdyn.MTT2D.IMTT2DGroupSheet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
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
		return win32com.client.util.Iterator(ob, '{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT2DGuide(DispatchBaseClass):
	'''MTT2D guide'''
	CLSID = IID('{333258BF-4C43-4C96-9079-6A4D54A4703C}')
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
		return self._oleobj_.InvokeTypes(1002, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(1004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(1007, 2, (11, 0), (), "UseSpecialContactPoints", None))
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
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((1007, LCID, 4, 0) + (value,) + ()))
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
		"ContactPoints": (1005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ForceDisplay": (1004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (1003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (1001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SpecialContactPoints": (1006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseSpecialContactPoints": (1007, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((1004, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((1001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((1007, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGuideArc(DispatchBaseClass):
	'''MTT2D arc guide'''
	CLSID = IID('{13439214-7EB0-439C-8C42-A2D55F1CC798}')
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
		return self._oleobj_.InvokeTypes(1002, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Angle(self):
		return self._ApplyTypes_(*(1052, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CenterPoint(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "CenterPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(1056, 2, (9, 0), (), "ContactPropertyToSheet", '{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}'))
	def _get_ContactUpDirection(self):
		return self._ApplyTypes_(*(1055, 2, (11, 0), (), "ContactUpDirection", None))
	def _get_DirectionPoint(self):
		return self._ApplyTypes_(*(1054, 2, (8197, 0), (), "DirectionPoint", None))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(1004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_ImaginaryPEdgeEnd(self):
		return self._ApplyTypes_(*(1058, 2, (11, 0), (), "ImaginaryPEdgeEnd", None))
	def _get_ImaginaryPEdgeRadius(self):
		return self._ApplyTypes_(*(1061, 2, (9, 0), (), "ImaginaryPEdgeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ImaginaryPEdgeStart(self):
		return self._ApplyTypes_(*(1057, 2, (11, 0), (), "ImaginaryPEdgeStart", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRadius(self):
		return self._ApplyTypes_(*(1060, 2, (9, 0), (), "SpecialRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(1007, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UseSpecialRadius(self):
		return self._ApplyTypes_(*(1059, 2, (11, 0), (), "UseSpecialRadius", None))
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
		self._oleobj_.Invoke(*((1055, LCID, 4, 0) + (value,) + ()))
	def _set_DirectionPoint(self, value):
		if "DirectionPoint" in self.__dict__: self.__dict__["DirectionPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1054, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_ImaginaryPEdgeEnd(self, value):
		if "ImaginaryPEdgeEnd" in self.__dict__: self.__dict__["ImaginaryPEdgeEnd"] = value; return
		self._oleobj_.Invoke(*((1058, LCID, 4, 0) + (value,) + ()))
	def _set_ImaginaryPEdgeStart(self, value):
		if "ImaginaryPEdgeStart" in self.__dict__: self.__dict__["ImaginaryPEdgeStart"] = value; return
		self._oleobj_.Invoke(*((1057, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((1007, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRadius(self, value):
		if "UseSpecialRadius" in self.__dict__: self.__dict__["UseSpecialRadius"] = value; return
		self._oleobj_.Invoke(*((1059, LCID, 4, 0) + (value,) + ()))
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
	The contact parameters of contact forces applied between sheet and arc guide

	:type: recurdyn.MTT2D.IMTT2DContactPropertyGuide
	'''
	ContactUpDirection = property(_get_ContactUpDirection, _set_ContactUpDirection)
	'''
	True: upside, False: downside

	:type: bool
	'''
	DirectionPoint = property(_get_DirectionPoint, _set_DirectionPoint)
	'''
	The direction of arc

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
	ImaginaryPEdgeEnd = property(_get_ImaginaryPEdgeEnd, _set_ImaginaryPEdgeEnd)
	'''
	End Point of Imaginary PEdge

	:type: bool
	'''
	ImaginaryPEdgeRadius = property(_get_ImaginaryPEdgeRadius, None)
	'''
	The radius of Imaginary PEdge

	:type: recurdyn.ProcessNet.IDouble
	'''
	ImaginaryPEdgeStart = property(_get_ImaginaryPEdgeStart, _set_ImaginaryPEdgeStart)
	'''
	Start Point of Imaginary PEdge

	:type: bool
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
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialRadius = property(_get_SpecialRadius, None)
	'''
	Special stiffness

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

	:type: bool
	'''
	UseSpecialRadius = property(_get_UseSpecialRadius, _set_UseSpecialRadius)
	'''
	Use special radius

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
		"_set_DirectionPoint": _set_DirectionPoint,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_ImaginaryPEdgeEnd": _set_ImaginaryPEdgeEnd,
		"_set_ImaginaryPEdgeStart": _set_ImaginaryPEdgeStart,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UseSpecialRadius": _set_UseSpecialRadius,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Angle": (1052, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CenterPoint": (1053, 2, (9, 0), (), "CenterPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (1005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToSheet": (1056, 2, (9, 0), (), "ContactPropertyToSheet", '{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}'),
		"ContactUpDirection": (1055, 2, (11, 0), (), "ContactUpDirection", None),
		"DirectionPoint": (1054, 2, (8197, 0), (), "DirectionPoint", None),
		"ForceDisplay": (1004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (1003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"ImaginaryPEdgeEnd": (1058, 2, (11, 0), (), "ImaginaryPEdgeEnd", None),
		"ImaginaryPEdgeRadius": (1061, 2, (9, 0), (), "ImaginaryPEdgeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ImaginaryPEdgeStart": (1057, 2, (11, 0), (), "ImaginaryPEdgeStart", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (1001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (1051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialContactPoints": (1006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRadius": (1060, 2, (9, 0), (), "SpecialRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseSpecialContactPoints": (1007, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UseSpecialRadius": (1059, 2, (11, 0), (), "UseSpecialRadius", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ContactUpDirection": ((1055, LCID, 4, 0),()),
		"DirectionPoint": ((1054, LCID, 4, 0),()),
		"ForceDisplay": ((1004, LCID, 4, 0),()),
		"ImaginaryPEdgeEnd": ((1058, LCID, 4, 0),()),
		"ImaginaryPEdgeStart": ((1057, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((1001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((1007, LCID, 4, 0),()),
		"UseSpecialRadius": ((1059, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGuideCircular(DispatchBaseClass):
	'''MTT2D circular guide'''
	CLSID = IID('{2AEBA258-C4AC-4EAA-ADF1-BAF8730E6E99}')
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
		return self._oleobj_.InvokeTypes(1002, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_CenterPoint(self):
		return self._ApplyTypes_(*(1052, 2, (9, 0), (), "CenterPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(1053, 2, (9, 0), (), "ContactPropertyToSheet", '{B4F3A991-0483-415B-820F-A8B4116A3C9A}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(1004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(1007, 2, (11, 0), (), "UseSpecialContactPoints", None))
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
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((1007, LCID, 4, 0) + (value,) + ()))
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
	ContactPoints = property(_get_ContactPoints, None)
	'''
	The number of max contact points

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactPropertyToSheet = property(_get_ContactPropertyToSheet, None)
	'''
	The contact parameters of contact forces applied between sheet and circular guide

	:type: recurdyn.MTT2D.IMTT2DContactPropertyPGuide
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
		"CenterPoint": (1052, 2, (9, 0), (), "CenterPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (1005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToSheet": (1053, 2, (9, 0), (), "ContactPropertyToSheet", '{B4F3A991-0483-415B-820F-A8B4116A3C9A}'),
		"ForceDisplay": (1004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (1003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (1001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Radius": (1051, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpecialContactPoints": (1006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"UseSpecialContactPoints": (1007, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((1004, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((1001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((1007, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DGuideCollection(DispatchBaseClass):
	'''IMTT2DGuideCollection'''
	CLSID = IID('{18DD760B-C7E8-4BCF-BAE7-EC87A7D22B42}')
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
		:rtype: recurdyn.MTT2D.IMTT2DGuide
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{333258BF-4C43-4C96-9079-6A4D54A4703C}')
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
		:rtype: recurdyn.MTT2D.IMTT2DGuide
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{333258BF-4C43-4C96-9079-6A4D54A4703C}')
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
		return win32com.client.util.Iterator(ob, '{333258BF-4C43-4C96-9079-6A4D54A4703C}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{333258BF-4C43-4C96-9079-6A4D54A4703C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT2DGuideLinear(DispatchBaseClass):
	'''MTT2D linear guide'''
	CLSID = IID('{F4AE0FC8-97F2-4BA3-B061-799E91800B51}')
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
		return self._oleobj_.InvokeTypes(1002, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactPropertyToSheet(self):
		return self._ApplyTypes_(*(1054, 2, (9, 0), (), "ContactPropertyToSheet", '{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}'))
	def _get_ContactUpDirection(self):
		return self._ApplyTypes_(*(1053, 2, (11, 0), (), "ContactUpDirection", None))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(1004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(1003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_ImaginaryPEdgeEnd(self):
		return self._ApplyTypes_(*(1056, 2, (11, 0), (), "ImaginaryPEdgeEnd", None))
	def _get_ImaginaryPEdgeRadius(self):
		return self._ApplyTypes_(*(1059, 2, (9, 0), (), "ImaginaryPEdgeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ImaginaryPEdgeStart(self):
		return self._ApplyTypes_(*(1055, 2, (11, 0), (), "ImaginaryPEdgeStart", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MotherBody(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_SecondPoint(self):
		return self._ApplyTypes_(*(1052, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_SpecialContactPoints(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialRadius(self):
		return self._ApplyTypes_(*(1058, 2, (9, 0), (), "SpecialRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_StartPoint(self):
		return self._ApplyTypes_(*(1051, 2, (9, 0), (), "StartPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_UseSpecialContactPoints(self):
		return self._ApplyTypes_(*(1007, 2, (11, 0), (), "UseSpecialContactPoints", None))
	def _get_UseSpecialRadius(self):
		return self._ApplyTypes_(*(1057, 2, (11, 0), (), "UseSpecialRadius", None))
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
		self._oleobj_.Invoke(*((1053, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_ImaginaryPEdgeEnd(self, value):
		if "ImaginaryPEdgeEnd" in self.__dict__: self.__dict__["ImaginaryPEdgeEnd"] = value; return
		self._oleobj_.Invoke(*((1056, LCID, 4, 0) + (value,) + ()))
	def _set_ImaginaryPEdgeStart(self, value):
		if "ImaginaryPEdgeStart" in self.__dict__: self.__dict__["ImaginaryPEdgeStart"] = value; return
		self._oleobj_.Invoke(*((1055, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_MotherBody(self, value):
		if "MotherBody" in self.__dict__: self.__dict__["MotherBody"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialContactPoints(self, value):
		if "UseSpecialContactPoints" in self.__dict__: self.__dict__["UseSpecialContactPoints"] = value; return
		self._oleobj_.Invoke(*((1007, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialRadius(self, value):
		if "UseSpecialRadius" in self.__dict__: self.__dict__["UseSpecialRadius"] = value; return
		self._oleobj_.Invoke(*((1057, LCID, 4, 0) + (value,) + ()))
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
	The contact parameters of contact forces applied between sheet and linear guide

	:type: recurdyn.MTT2D.IMTT2DContactPropertyGuide
	'''
	ContactUpDirection = property(_get_ContactUpDirection, _set_ContactUpDirection)
	'''
	True: upside, False: downside

	:type: bool
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
	ImaginaryPEdgeEnd = property(_get_ImaginaryPEdgeEnd, _set_ImaginaryPEdgeEnd)
	'''
	End Point of Imaginary PEdge

	:type: bool
	'''
	ImaginaryPEdgeRadius = property(_get_ImaginaryPEdgeRadius, None)
	'''
	The radius of Imaginary PEdge

	:type: recurdyn.ProcessNet.IDouble
	'''
	ImaginaryPEdgeStart = property(_get_ImaginaryPEdgeStart, _set_ImaginaryPEdgeStart)
	'''
	Start Point of Imaginary PEdge

	:type: bool
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
	SpecialContactPoints = property(_get_SpecialContactPoints, None)
	'''
	Special Number of max contact points

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialRadius = property(_get_SpecialRadius, None)
	'''
	Special stiffness

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	StartPoint = property(_get_StartPoint, None)
	'''
	The start point of line

	:type: recurdyn.ProcessNet.IVector
	'''
	UseSpecialContactPoints = property(_get_UseSpecialContactPoints, _set_UseSpecialContactPoints)
	'''
	Use special Number of max contact points

	:type: bool
	'''
	UseSpecialRadius = property(_get_UseSpecialRadius, _set_UseSpecialRadius)
	'''
	Use special radius

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
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_ImaginaryPEdgeEnd": _set_ImaginaryPEdgeEnd,
		"_set_ImaginaryPEdgeStart": _set_ImaginaryPEdgeStart,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MotherBody": _set_MotherBody,
		"_set_Name": _set_Name,
		"_set_UseSpecialContactPoints": _set_UseSpecialContactPoints,
		"_set_UseSpecialRadius": _set_UseSpecialRadius,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoints": (1005, 2, (9, 0), (), "ContactPoints", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactPropertyToSheet": (1054, 2, (9, 0), (), "ContactPropertyToSheet", '{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}'),
		"ContactUpDirection": (1053, 2, (11, 0), (), "ContactUpDirection", None),
		"ForceDisplay": (1004, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (1003, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"ImaginaryPEdgeEnd": (1056, 2, (11, 0), (), "ImaginaryPEdgeEnd", None),
		"ImaginaryPEdgeRadius": (1059, 2, (9, 0), (), "ImaginaryPEdgeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ImaginaryPEdgeStart": (1055, 2, (11, 0), (), "ImaginaryPEdgeStart", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MotherBody": (1001, 2, (9, 0), (), "MotherBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SecondPoint": (1052, 2, (9, 0), (), "SecondPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"SpecialContactPoints": (1006, 2, (9, 0), (), "SpecialContactPoints", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialRadius": (1058, 2, (9, 0), (), "SpecialRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"StartPoint": (1051, 2, (9, 0), (), "StartPoint", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"UseSpecialContactPoints": (1007, 2, (11, 0), (), "UseSpecialContactPoints", None),
		"UseSpecialRadius": (1057, 2, (11, 0), (), "UseSpecialRadius", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ContactUpDirection": ((1053, LCID, 4, 0),()),
		"ForceDisplay": ((1004, LCID, 4, 0),()),
		"ImaginaryPEdgeEnd": ((1056, LCID, 4, 0),()),
		"ImaginaryPEdgeStart": ((1055, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"MotherBody": ((1001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseSpecialContactPoints": ((1007, LCID, 4, 0),()),
		"UseSpecialRadius": ((1057, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DMovableRollerGroupCollection(DispatchBaseClass):
	'''IMTT2DMovableRollerGroupCollection'''
	CLSID = IID('{1F97796F-D817-4F6D-BDD4-057FAB6AB0C1}')
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
		:rtype: recurdyn.MTT2D.IMTT2DGroupMovableRoller
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D4F728AD-8867-4AA8-B319-88687F79C526}')
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
		:rtype: recurdyn.MTT2D.IMTT2DGroupMovableRoller
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D4F728AD-8867-4AA8-B319-88687F79C526}')
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
		return win32com.client.util.Iterator(ob, '{D4F728AD-8867-4AA8-B319-88687F79C526}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{D4F728AD-8867-4AA8-B319-88687F79C526}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT2DSheet(DispatchBaseClass):
	'''MTT2D sheet'''
	CLSID = IID('{B6148C63-C63E-4B91-8051-EDCA38242816}')
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
		Set layer number
		
		:param iVal: int
		'''
		return self._oleobj_.InvokeTypes(1025, LCID, 1, (24, 0), ((19, 1),),iVal
			)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_AllCurlRadius(self):
		return self._ApplyTypes_(*(1011, 2, (11, 0), (), "AllCurlRadius", None))
	def _get_AllDampingRatio(self):
		return self._ApplyTypes_(*(1010, 2, (11, 0), (), "AllDampingRatio", None))
	def _get_AllDensity(self):
		return self._ApplyTypes_(*(1008, 2, (11, 0), (), "AllDensity", None))
	def _get_AllYoungsModulus(self):
		return self._ApplyTypes_(*(1009, 2, (11, 0), (), "AllYoungsModulus", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_CurlRadius(self):
		return self._ApplyTypes_(*(1019, 2, (9, 0), (), "CurlRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(1018, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(1016, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DirectionPoint(self):
		return self._ApplyTypes_(*(1002, 2, (8197, 0), (), "DirectionPoint", None))
	def _get_Fold(self):
		return self._ApplyTypes_(*(1003, 2, (11, 0), (), "Fold", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InitialVelocity(self):
		return self._ApplyTypes_(*(1007, 2, (9, 0), (), "InitialVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
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
	def _get_PointList(self):
		return self._ApplyTypes_(*(1004, 2, (8204, 0), (), "PointList", None))
	def _get_SpecialCurlRadius(self):
		return self._ApplyTypes_(*(1023, 2, (9, 0), (), "SpecialCurlRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialDampingRatio(self):
		return self._ApplyTypes_(*(1022, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialDensity(self):
		return self._ApplyTypes_(*(1020, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialThickness(self):
		return self._ApplyTypes_(*(1026, 2, (9, 0), (), "SpecialThickness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_SpecialYoungsModulus(self):
		return self._ApplyTypes_(*(1021, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'))
	def _get_StartPoint(self):
		return self._ApplyTypes_(*(1001, 2, (8197, 0), (), "StartPoint", None))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseInitialVelocity(self):
		return self._ApplyTypes_(*(1006, 2, (11, 0), (), "UseInitialVelocity", None))
	def _get_UseSpecialCurlRadius(self):
		return self._ApplyTypes_(*(1015, 2, (11, 0), (), "UseSpecialCurlRadius", None))
	def _get_UseSpecialDampingRatio(self):
		return self._ApplyTypes_(*(1014, 2, (11, 0), (), "UseSpecialDampingRatio", None))
	def _get_UseSpecialDensity(self):
		return self._ApplyTypes_(*(1012, 2, (11, 0), (), "UseSpecialDensity", None))
	def _get_UseSpecialThickness(self):
		return self._ApplyTypes_(*(1024, 2, (11, 0), (), "UseSpecialThickness", None))
	def _get_UseSpecialYoungsModulus(self):
		return self._ApplyTypes_(*(1013, 2, (11, 0), (), "UseSpecialYoungsModulus", None))
	def _get_UseUpdateGeometryAutomatically(self):
		return self._ApplyTypes_(*(1027, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(1017, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_AllCurlRadius(self, value):
		if "AllCurlRadius" in self.__dict__: self.__dict__["AllCurlRadius"] = value; return
		self._oleobj_.Invoke(*((1011, LCID, 4, 0) + (value,) + ()))
	def _set_AllDampingRatio(self, value):
		if "AllDampingRatio" in self.__dict__: self.__dict__["AllDampingRatio"] = value; return
		self._oleobj_.Invoke(*((1010, LCID, 4, 0) + (value,) + ()))
	def _set_AllDensity(self, value):
		if "AllDensity" in self.__dict__: self.__dict__["AllDensity"] = value; return
		self._oleobj_.Invoke(*((1008, LCID, 4, 0) + (value,) + ()))
	def _set_AllYoungsModulus(self, value):
		if "AllYoungsModulus" in self.__dict__: self.__dict__["AllYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((1009, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DirectionPoint(self, value):
		if "DirectionPoint" in self.__dict__: self.__dict__["DirectionPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_PointList(self, value):
		if "PointList" in self.__dict__: self.__dict__["PointList"] = value; return
		_value_type = True if value and isinstance(value[0], win32com.client.VARIANT) else False
		if not _value_type:
			value = [win32com.client.VARIANT(12, _data) for _data in value]
		variantValue = win32com.client.VARIANT(8204, value)
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (variantValue,) + ()))
		if not _value_type:
			value = [_data.value for _data in value]
	def _set_StartPoint(self, value):
		if "StartPoint" in self.__dict__: self.__dict__["StartPoint"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseInitialVelocity(self, value):
		if "UseInitialVelocity" in self.__dict__: self.__dict__["UseInitialVelocity"] = value; return
		self._oleobj_.Invoke(*((1006, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialCurlRadius(self, value):
		if "UseSpecialCurlRadius" in self.__dict__: self.__dict__["UseSpecialCurlRadius"] = value; return
		self._oleobj_.Invoke(*((1015, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDampingRatio(self, value):
		if "UseSpecialDampingRatio" in self.__dict__: self.__dict__["UseSpecialDampingRatio"] = value; return
		self._oleobj_.Invoke(*((1014, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialDensity(self, value):
		if "UseSpecialDensity" in self.__dict__: self.__dict__["UseSpecialDensity"] = value; return
		self._oleobj_.Invoke(*((1012, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialThickness(self, value):
		if "UseSpecialThickness" in self.__dict__: self.__dict__["UseSpecialThickness"] = value; return
		self._oleobj_.Invoke(*((1024, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpecialYoungsModulus(self, value):
		if "UseSpecialYoungsModulus" in self.__dict__: self.__dict__["UseSpecialYoungsModulus"] = value; return
		self._oleobj_.Invoke(*((1013, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdateGeometryAutomatically(self, value):
		if "UseUpdateGeometryAutomatically" in self.__dict__: self.__dict__["UseUpdateGeometryAutomatically"] = value; return
		self._oleobj_.Invoke(*((1027, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	AllCurlRadius = property(_get_AllCurlRadius, _set_AllCurlRadius)
	'''
	Use all curl radius

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
	AllYoungsModulus = property(_get_AllYoungsModulus, _set_AllYoungsModulus)
	'''
	Use all young's modulus

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	CurlRadius = property(_get_CurlRadius, None)
	'''
	The sheet bends with a curvature that matches the curl radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingRatio = property(_get_DampingRatio, None)
	'''
	Damping ratio of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	Density = property(_get_Density, None)
	'''
	The area density of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''
	DirectionPoint = property(_get_DirectionPoint, _set_DirectionPoint)
	'''
	The direction point of the sheet

	:type: list[float]
	'''
	Fold = property(_get_Fold, None)
	'''
	True: folding sheet, False: flat sheet

	:type: bool
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	InitialVelocity = property(_get_InitialVelocity, None)
	'''
	The initial velocity of a sheet is in the direction of positive X axis of the markers on each sheet body

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
	PointList = property(_get_PointList, _set_PointList)
	'''
	A sheet folds through this points

	:type: list[object]
	'''
	SpecialCurlRadius = property(_get_SpecialCurlRadius, None)
	'''
	Special curl radius

	:type: recurdyn.ProcessNet.ISpecialParametricValue
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
	SpecialThickness = property(_get_SpecialThickness, None)
	'''
	Special Thickness

	:type: recurdyn.ProcessNet.ISpecialParametricValue
	'''
	SpecialYoungsModulus = property(_get_SpecialYoungsModulus, None)
	'''
	Special young's modulus

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
	UseInitialVelocity = property(_get_UseInitialVelocity, _set_UseInitialVelocity)
	'''
	Use initial velocity

	:type: bool
	'''
	UseSpecialCurlRadius = property(_get_UseSpecialCurlRadius, _set_UseSpecialCurlRadius)
	'''
	Use special curl radius

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
	UseSpecialThickness = property(_get_UseSpecialThickness, _set_UseSpecialThickness)
	'''
	Use special thickness

	:type: bool
	'''
	UseSpecialYoungsModulus = property(_get_UseSpecialYoungsModulus, _set_UseSpecialYoungsModulus)
	'''
	Use special young's modulus

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
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	Young's modulus of the sheet

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_AllCurlRadius": _set_AllCurlRadius,
		"_set_AllDampingRatio": _set_AllDampingRatio,
		"_set_AllDensity": _set_AllDensity,
		"_set_AllYoungsModulus": _set_AllYoungsModulus,
		"_set_Comment": _set_Comment,
		"_set_DirectionPoint": _set_DirectionPoint,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_PointList": _set_PointList,
		"_set_StartPoint": _set_StartPoint,
		"_set_UseInitialVelocity": _set_UseInitialVelocity,
		"_set_UseSpecialCurlRadius": _set_UseSpecialCurlRadius,
		"_set_UseSpecialDampingRatio": _set_UseSpecialDampingRatio,
		"_set_UseSpecialDensity": _set_UseSpecialDensity,
		"_set_UseSpecialThickness": _set_UseSpecialThickness,
		"_set_UseSpecialYoungsModulus": _set_UseSpecialYoungsModulus,
		"_set_UseUpdateGeometryAutomatically": _set_UseUpdateGeometryAutomatically,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"AllCurlRadius": (1011, 2, (11, 0), (), "AllCurlRadius", None),
		"AllDampingRatio": (1010, 2, (11, 0), (), "AllDampingRatio", None),
		"AllDensity": (1008, 2, (11, 0), (), "AllDensity", None),
		"AllYoungsModulus": (1009, 2, (11, 0), (), "AllYoungsModulus", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"CurlRadius": (1019, 2, (9, 0), (), "CurlRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingRatio": (1018, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (1016, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DirectionPoint": (1002, 2, (8197, 0), (), "DirectionPoint", None),
		"Fold": (1003, 2, (11, 0), (), "Fold", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InitialVelocity": (1007, 2, (9, 0), (), "InitialVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PointList": (1004, 2, (8204, 0), (), "PointList", None),
		"SpecialCurlRadius": (1023, 2, (9, 0), (), "SpecialCurlRadius", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialDampingRatio": (1022, 2, (9, 0), (), "SpecialDampingRatio", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialDensity": (1020, 2, (9, 0), (), "SpecialDensity", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialThickness": (1026, 2, (9, 0), (), "SpecialThickness", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"SpecialYoungsModulus": (1021, 2, (9, 0), (), "SpecialYoungsModulus", '{B58006F8-C5AC-4B97-8096-AF292F9DBE55}'),
		"StartPoint": (1001, 2, (8197, 0), (), "StartPoint", None),
		"Thickness": (1005, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseInitialVelocity": (1006, 2, (11, 0), (), "UseInitialVelocity", None),
		"UseSpecialCurlRadius": (1015, 2, (11, 0), (), "UseSpecialCurlRadius", None),
		"UseSpecialDampingRatio": (1014, 2, (11, 0), (), "UseSpecialDampingRatio", None),
		"UseSpecialDensity": (1012, 2, (11, 0), (), "UseSpecialDensity", None),
		"UseSpecialThickness": (1024, 2, (11, 0), (), "UseSpecialThickness", None),
		"UseSpecialYoungsModulus": (1013, 2, (11, 0), (), "UseSpecialYoungsModulus", None),
		"UseUpdateGeometryAutomatically": (1027, 2, (11, 0), (), "UseUpdateGeometryAutomatically", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"YoungsModulus": (1017, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"AllCurlRadius": ((1011, LCID, 4, 0),()),
		"AllDampingRatio": ((1010, LCID, 4, 0),()),
		"AllDensity": ((1008, LCID, 4, 0),()),
		"AllYoungsModulus": ((1009, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DirectionPoint": ((1002, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"PointList": ((1004, LCID, 4, 0),()),
		"StartPoint": ((1001, LCID, 4, 0),()),
		"UseInitialVelocity": ((1006, LCID, 4, 0),()),
		"UseSpecialCurlRadius": ((1015, LCID, 4, 0),()),
		"UseSpecialDampingRatio": ((1014, LCID, 4, 0),()),
		"UseSpecialDensity": ((1012, LCID, 4, 0),()),
		"UseSpecialThickness": ((1024, LCID, 4, 0),()),
		"UseSpecialYoungsModulus": ((1013, LCID, 4, 0),()),
		"UseUpdateGeometryAutomatically": ((1027, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMTT2DSheetBodyCollection(DispatchBaseClass):
	'''IMTT2DSheetBodyCollection'''
	CLSID = IID('{767F4D3F-26B8-4F0A-B982-9A7FAC6CD1B2}')
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
		:rtype: recurdyn.ProcessNet.IBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')
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
		:rtype: recurdyn.ProcessNet.IBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')
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
		return win32com.client.util.Iterator(ob, '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT2DSheetRevJointCollection(DispatchBaseClass):
	'''IMTT2DSheetRevJointCollection'''
	CLSID = IID('{AFC279E7-53CD-4DA1-96E2-3833740C410A}')
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
		:rtype: recurdyn.ProcessNet.IJoint
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B9173DAD-05DD-4037-9367-726DDDEE988E}')
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
		:rtype: recurdyn.ProcessNet.IJoint
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B9173DAD-05DD-4037-9367-726DDDEE988E}')
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
		return win32com.client.util.Iterator(ob, '{B9173DAD-05DD-4037-9367-726DDDEE988E}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{B9173DAD-05DD-4037-9367-726DDDEE988E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT2DSheetRotSpringCollection(DispatchBaseClass):
	'''IMTT2DSheetRotSpringCollection'''
	CLSID = IID('{F38F6090-E64E-4BA5-96B1-9865E77C4B31}')
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
		:rtype: recurdyn.ProcessNet.IForce
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{EB73DE47-2BB8-46BD-A904-F61BCBC59D1F}')
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
		:rtype: recurdyn.ProcessNet.IForce
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{EB73DE47-2BB8-46BD-A904-F61BCBC59D1F}')
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
		return win32com.client.util.Iterator(ob, '{EB73DE47-2BB8-46BD-A904-F61BCBC59D1F}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{EB73DE47-2BB8-46BD-A904-F61BCBC59D1F}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMTT2DSubSystem(DispatchBaseClass):
	'''MTT2D subsystem'''
	CLSID = IID('{4946A10D-6F44-45BC-B3F1-F1AA0CDA2C83}')
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
		
		:param pSheet: IMTT2DGroupSheet
		:param pMovableRoller: IMTT2DGroupMovableRoller
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(1013, LCID, 1, (11, 0), ((9, 1), (9, 1)),pSheet
			, pMovableRoller)


	def CreateContactSheetToSheet(self, strName, pBaseSheet, pActionSheet):
		'''
		Creates a sheet-to-sheet contact
		
		:param strName: str
		:param pBaseSheet: IMTT2DGroupSheet
		:param pActionSheet: IMTT2DGroupSheet
		:rtype: recurdyn.MTT2D.IMTT2DContactSheetToSheet
		'''
		ret = self._oleobj_.InvokeTypes(1010, LCID, 1, (9, 0), ((8, 1), (9, 0), (9, 0)),strName
			, pBaseSheet, pActionSheet)
		if ret is not None:
			ret = Dispatch(ret, 'CreateContactSheetToSheet', '{AB78805A-064A-4015-812D-1332288F5789}')
		return ret

	def CreateForceNodal(self, strName, pSheet):
		'''
		Creates a nodal force
		
		:param strName: str
		:param pSheet: IMTT2DGroupSheet
		:rtype: recurdyn.MTT2D.IMTT2DForceNodal
		'''
		ret = self._oleobj_.InvokeTypes(1011, LCID, 1, (9, 0), ((8, 1), (9, 0)),strName
			, pSheet)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceNodal', '{0F707193-3BDD-4899-8FD9-E9C21739ECCB}')
		return ret

	def CreateGroupFixedRoller(self, strName, pPoint, dRadius):
		'''
		Creates a fixed roller
		
		:param strName: str
		:param pPoint: list[float]
		:param dRadius: float
		:rtype: recurdyn.MTT2D.IMTT2DGroupFixedRoller
		'''
		ret = self._oleobj_.InvokeTypes(1003, LCID, 1, (9, 0), ((8, 1), (8197, 1), (5, 1)),strName
			, pPoint, dRadius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupFixedRoller', '{0E7F0C51-106B-446A-93A5-1912034EA1A7}')
		return ret

	def CreateGroupFlexibleFixedRoller(self, name, numNodesCircumference, numNodesRadial):
		'''
		Creates a flexible fixed roller
		
		:param name: str
		:param numNodesCircumference: int
		:param numNodesRadial: int
		:rtype: recurdyn.MTT2D.IMTT2DGroupFixedRollerShell
		'''
		ret = self._oleobj_.InvokeTypes(1014, LCID, 1, (9, 0), ((8, 1), (19, 1), (19, 1)),name
			, numNodesCircumference, numNodesRadial)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupFlexibleFixedRoller', '{91034068-E6A9-4616-9D41-9B666E4018AB}')
		return ret

	def CreateGroupFlexibleMovableRoller(self, name, numNodesCircumference, numNodesRadial, rollerFixed):
		'''
		Creates a flexible movable roller
		
		:param name: str
		:param numNodesCircumference: int
		:param numNodesRadial: int
		:param rollerFixed: IGroup
		:rtype: recurdyn.MTT2D.IMTT2DGroupMovableRollerShell
		'''
		ret = self._oleobj_.InvokeTypes(1015, LCID, 1, (9, 0), ((8, 1), (19, 1), (19, 1), (9, 1)),name
			, numNodesCircumference, numNodesRadial, rollerFixed)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupFlexibleMovableRoller', '{2310F73F-2BE6-4338-93FF-609E572F4802}')
		return ret

	def CreateGroupGuideBody(self, strName, pFirstPoint, pSecondPoint, dRadius):
		'''
		Creates a guide body
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param dRadius: float
		:rtype: recurdyn.MTT2D.IMTT2DGroupGuideBody
		'''
		ret = self._oleobj_.InvokeTypes(1006, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1)),strName
			, pFirstPoint, pSecondPoint, dRadius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupGuideBody', '{1AB7F0EE-74C9-4EF7-89BF-14AAF15EF35E}')
		return ret

	def CreateGroupMovableRoller(self, strName, pIFixedRoller, pDirection, dRadius, dDistance):
		'''
		Creates a movable roller
		
		:param strName: str
		:param pIFixedRoller: IMTT2DGroupFixedRoller
		:param pDirection: list[float]
		:param dRadius: float
		:param dDistance: float
		:rtype: recurdyn.MTT2D.IMTT2DGroupMovableRoller
		'''
		ret = self._oleobj_.InvokeTypes(1004, LCID, 1, (9, 0), ((8, 1), (9, 1), (8197, 1), (5, 1), (5, 1)),strName
			, pIFixedRoller, pDirection, dRadius, dDistance)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupMovableRoller', '{D4F728AD-8867-4AA8-B319-88687F79C526}')
		return ret

	def CreateGroupMovableRollerWithAngle(self, strName, pIFixedRoller, dAngle, dRadius, dDistance):
		'''
		Creates a movable roller with angle
		
		:param strName: str
		:param pIFixedRoller: IMTT2DGroupFixedRoller
		:param dAngle: float
		:param dRadius: float
		:param dDistance: float
		:rtype: recurdyn.MTT2D.IMTT2DGroupMovableRoller
		'''
		ret = self._oleobj_.InvokeTypes(1026, LCID, 1, (9, 0), ((8, 1), (9, 1), (5, 1), (5, 1), (5, 1)),strName
			, pIFixedRoller, dAngle, dRadius, dDistance)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupMovableRollerWithAngle', '{D4F728AD-8867-4AA8-B319-88687F79C526}')
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
		:rtype: recurdyn.MTT2D.IMTT2DGroupFixedRoller
		'''
		ret = self._oleobj_.InvokeTypes(1005, LCID, 1, (9, 0), ((8, 1), (8197, 1), (5, 1), (8, 1), (8197, 1), (5, 1), (5, 1)),strFixedRollerName
			, pPoint, dFixedRollerRadius, strMovableRollerName, pDirection, dMovableRollerRadius
			, dDistance)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupRollerPair', '{0E7F0C51-106B-446A-93A5-1912034EA1A7}')
		return ret

	def CreateGroupSheet(self, strName, pFirstPoint, pSecondPoint, iNoOfSegments, dSegmentLength, dSheetThickness):
		'''
		Creates a flat sheet
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param iNoOfSegments: int
		:param dSegmentLength: float
		:param dSheetThickness: float
		:rtype: recurdyn.MTT2D.IMTT2DGroupSheet
		'''
		ret = self._oleobj_.InvokeTypes(1001, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (3, 1), (5, 1), (5, 1)),strName
			, pFirstPoint, pSecondPoint, iNoOfSegments, dSegmentLength, dSheetThickness
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupSheet', '{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
		return ret

	def CreateGroupSheet2(self, strName, pFirstPoint, pSecondPoint, iNoOfSegments, dSegmentLength):
		'''
		Creates a flat sheet
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param iNoOfSegments: int
		:param dSegmentLength: float
		:rtype: recurdyn.MTT2D.IMTT2DGroupSheet
		'''
		ret = self._oleobj_.InvokeTypes(1027, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (3, 1), (5, 1)),strName
			, pFirstPoint, pSecondPoint, iNoOfSegments, dSegmentLength)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupSheet2', '{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
		return ret

	def CreateGroupSheetFolding(self, strName, pMultiPoints, iNoOfSegments, dSegmentLength, dSheetThickness):
		'''
		Creates a folding sheet
		
		:param strName: str
		:param pMultiPoints: list[object]
		:param iNoOfSegments: int
		:param dSegmentLength: float
		:param dSheetThickness: float
		:rtype: recurdyn.MTT2D.IMTT2DGroupSheet
		'''
		_pMultiPoints_type = True if pMultiPoints and isinstance(pMultiPoints[0], win32com.client.VARIANT) else False
		if not _pMultiPoints_type:
			pMultiPoints = [win32com.client.VARIANT(12, _data) for _data in pMultiPoints]

		ret = self._oleobj_.InvokeTypes(1002, LCID, 1, (9, 0), ((8, 1), (8204, 1), (3, 1), (5, 1), (5, 1)),strName
			, pMultiPoints, iNoOfSegments, dSegmentLength, dSheetThickness)

		if not _pMultiPoints_type:
			pMultiPoints = [_data.value for _data in pMultiPoints]

		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupSheetFolding', '{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
		return ret

	def CreateGroupSheetFoldingWithPointList(self, strName, strFile, iNoOfSegments, dSegmentLength, dSheetThickness):
		'''
		Creates a folding sheet with point list file
		
		:param strName: str
		:param strFile: str
		:param iNoOfSegments: int
		:param dSegmentLength: float
		:param dSheetThickness: float
		:rtype: recurdyn.MTT2D.IMTT2DGroupSheet
		'''
		ret = self._oleobj_.InvokeTypes(1028, LCID, 1, (9, 0), ((8, 1), (8, 1), (3, 1), (5, 1), (5, 1)),strName
			, strFile, iNoOfSegments, dSegmentLength, dSheetThickness)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupSheetFoldingWithPointList', '{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
		return ret

	def CreateGroupSheetWithCurve(self, strName, pCurve, iNoOfSegments, dSheetThickness):
		'''
		Creates a folding sheet with curve
		
		:param strName: str
		:param pCurve: IGeometry
		:param iNoOfSegments: int
		:param dSheetThickness: float
		:rtype: recurdyn.MTT2D.IMTT2DGroupSheet
		'''
		ret = self._oleobj_.InvokeTypes(1030, LCID, 1, (9, 0), ((8, 1), (9, 1), (3, 1), (5, 1)),strName
			, pCurve, iNoOfSegments, dSheetThickness)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupSheetWithCurve', '{59FE2E3A-2043-4651-8D6E-A58D8800205A}')
		return ret

	def CreateGuideArc(self, strName, pFirstPoint, pSecondPoint, dAngle):
		'''
		Creates an arc guide
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param dAngle: float
		:rtype: recurdyn.MTT2D.IMTT2DGuideArc
		'''
		ret = self._oleobj_.InvokeTypes(1007, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1)),strName
			, pFirstPoint, pSecondPoint, dAngle)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideArc', '{13439214-7EB0-439C-8C42-A2D55F1CC798}')
		return ret

	def CreateGuideArcWithEndPoint(self, strName, pCenterPoint, pStartPoint, pEndPoint, bDirection):
		'''
		Creates an Arc Geometry with End Point
		
		:param strName: str
		:param pCenterPoint: list[float]
		:param pStartPoint: list[float]
		:param pEndPoint: list[float]
		:param bDirection: bool
		:rtype: recurdyn.MTT2D.IMTT2DGuideArc
		'''
		ret = self._oleobj_.InvokeTypes(1025, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (8197, 1), (11, 1)),strName
			, pCenterPoint, pStartPoint, pEndPoint, bDirection)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideArcWithEndPoint', '{13439214-7EB0-439C-8C42-A2D55F1CC798}')
		return ret

	def CreateGuideCircular(self, strName, pFirstPoint, dRadius):
		'''
		Creates method creates a circular guide
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param dRadius: float
		:rtype: recurdyn.MTT2D.IMTT2DGuideCircular
		'''
		ret = self._oleobj_.InvokeTypes(1009, LCID, 1, (9, 0), ((8, 1), (8197, 1), (5, 1)),strName
			, pFirstPoint, dRadius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideCircular', '{2AEBA258-C4AC-4EAA-ADF1-BAF8730E6E99}')
		return ret

	def CreateGuideCircularWithGuide(self, strName, pGuide, bStartPoint, bupDirection, dRadius):
		'''
		Creates a circular guide with guide
		
		:param strName: str
		:param pGuide: IMTT2DGuide
		:param bStartPoint: bool
		:param bupDirection: bool
		:param dRadius: float
		:rtype: recurdyn.MTT2D.IMTT2DGuideCircular
		'''
		ret = self._oleobj_.InvokeTypes(1039, LCID, 1, (9, 0), ((8, 1), (9, 1), (11, 1), (11, 1), (5, 1)),strName
			, pGuide, bStartPoint, bupDirection, dRadius)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideCircularWithGuide', '{2AEBA258-C4AC-4EAA-ADF1-BAF8730E6E99}')
		return ret

	def CreateGuideLinear(self, strName, pFirstPoint, pSecondPoint):
		'''
		Creates a linear guide
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:rtype: recurdyn.MTT2D.IMTT2DGuideLinear
		'''
		ret = self._oleobj_.InvokeTypes(1008, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1)),strName
			, pFirstPoint, pSecondPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGuideLinear', '{F4AE0FC8-97F2-4BA3-B061-799E91800B51}')
		return ret

	def CreateSensorDistance(self, strName, pPosition, pDirection, pEntity, dRange):
		'''
		Creates a distance sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pDirection: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorDistance
		'''
		ret = self._oleobj_.InvokeTypes(1022, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pDirection, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorDistance', '{0CC3861B-CC2A-4402-9135-C8BC804EABBD}')
		return ret

	def CreateSensorEvent(self, strName, pPosition, pEntity, dRange):
		'''
		Creates an event sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorEvent
		'''
		ret = self._oleobj_.InvokeTypes(1023, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorEvent', '{FB0F1AE7-3A1E-4326-B1BF-8225DA2BF11E}')
		return ret

	def CreateSensorSpeed(self, strName, pPosition, pDirection, pEntity, dRange):
		'''
		Creates a speed sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pDirection: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorSpeed
		'''
		ret = self._oleobj_.InvokeTypes(1021, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pDirection, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorSpeed', '{CCB7E742-F0DF-4F22-A377-04AA675FD281}')
		return ret

	def CreateSensorTension(self, name):
		'''
		Creates an tension sensor
		
		:param name: str
		:rtype: recurdyn.ProcessNet.ISensorTension
		'''
		ret = self._oleobj_.InvokeTypes(1029, LCID, 1, (9, 0), ((8, 1),),name
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
		ret = self._oleobj_.InvokeTypes(1038, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorTension2', '{55C49622-A503-4651-BF1E-2A84CD9E27AB}')
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

		ret = self._oleobj_.InvokeTypes(1012, LCID, 1, (11, 0), ((8204, 1),),pMultiBodies
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

		ret = self._oleobj_.InvokeTypes(1016, LCID, 1, (11, 0), ((8204, 1), (19, 1)),pMultiBodies
			, oleColor)

		if not _pMultiBodies_type:
			pMultiBodies = [_data.value for _data in pMultiBodies]

		return ret


	def _get_Assembly(self):
		return self._ApplyTypes_(*(1020, 2, (9, 0), (), "Assembly", '{24C00315-36B5-498A-99A5-A3D3074E24DF}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactSheetToSheetCollection(self):
		return self._ApplyTypes_(*(1035, 2, (9, 0), (), "ContactSheetToSheetCollection", '{9538383C-C3C2-463F-B9D5-9017468026D1}'))
	def _get_Contour(self):
		return self._ApplyTypes_(*(1037, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'))
	def _get_FixedRollerGroupCollection(self):
		return self._ApplyTypes_(*(1031, 2, (9, 0), (), "FixedRollerGroupCollection", '{8393C52E-FB87-4F44-AA3B-CF6BE4045DEA}'))
	def _get_ForceNodalCollection(self):
		return self._ApplyTypes_(*(1034, 2, (9, 0), (), "ForceNodalCollection", '{E3BB5B6C-23F0-4038-8466-36B8782CC65A}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(1000, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_GroupSheetCollection(self):
		return self._ApplyTypes_(*(1033, 2, (9, 0), (), "GroupSheetCollection", '{6DAA417B-BEE4-49CE-AD91-195F1AA003EF}'))
	def _get_GuideCollection(self):
		return self._ApplyTypes_(*(1036, 2, (9, 0), (), "GuideCollection", '{18DD760B-C7E8-4BCF-BAE7-EC87A7D22B42}'))
	def _get_MovableRollerGroupCollection(self):
		return self._ApplyTypes_(*(1032, 2, (9, 0), (), "MovableRollerGroupCollection", '{1F97796F-D817-4F6D-BDD4-057FAB6AB0C1}'))
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

	Assembly = property(_get_Assembly, None)
	'''
	Assembly

	:type: recurdyn.MTT2D.IMTT2DAssembly
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactSheetToSheetCollection = property(_get_ContactSheetToSheetCollection, None)
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
	GroupSheetCollection = property(_get_GroupSheetCollection, None)
	GuideCollection = property(_get_GuideCollection, None)
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
		"Assembly": (1020, 2, (9, 0), (), "Assembly", '{24C00315-36B5-498A-99A5-A3D3074E24DF}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactSheetToSheetCollection": (1035, 2, (9, 0), (), "ContactSheetToSheetCollection", '{9538383C-C3C2-463F-B9D5-9017468026D1}'),
		"Contour": (1037, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'),
		"FixedRollerGroupCollection": (1031, 2, (9, 0), (), "FixedRollerGroupCollection", '{8393C52E-FB87-4F44-AA3B-CF6BE4045DEA}'),
		"ForceNodalCollection": (1034, 2, (9, 0), (), "ForceNodalCollection", '{E3BB5B6C-23F0-4038-8466-36B8782CC65A}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralSubSystem": (1000, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"GroupSheetCollection": (1033, 2, (9, 0), (), "GroupSheetCollection", '{6DAA417B-BEE4-49CE-AD91-195F1AA003EF}'),
		"GuideCollection": (1036, 2, (9, 0), (), "GuideCollection", '{18DD760B-C7E8-4BCF-BAE7-EC87A7D22B42}'),
		"MovableRollerGroupCollection": (1032, 2, (9, 0), (), "MovableRollerGroupCollection", '{1F97796F-D817-4F6D-BDD4-057FAB6AB0C1}'),
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

IMTT2DAssembly_vtables_dispatch_ = 1
IMTT2DAssembly_vtables_ = [
	(( 'SetContactedGeometry' , 'pVal' , 'vBool' , 'pResult' , ), 1051, (1051, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GetContactedGeometry' , 'pVal' , 'pResult' , ), 1052, (1052, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SetContactedSheet' , 'pVal' , 'vBool' , 'pResult' , ), 1053, (1053, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetContactedSheet' , 'pVal' , 'pResult' , ), 1054, (1054, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseSystemBoundary' , 'pVal' , ), 1055, (1055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseSystemBoundary' , 'pVal' , ), 1055, (1055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ReferencePosition' , 'ppVal' , ), 1056, (1056, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'SizeOfBoundary' , 'pVal' , ), 1057, (1057, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SizeOfBoundary' , 'pVal' , ), 1057, (1057, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BufferRadiusFactor' , 'ppVal' , ), 1058, (1058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'MaximumStepsizeFactor' , 'ppVal' , ), 1059, (1059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'PenetrationParameter' , 'ppVal' , ), 1060, (1060, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseResolution' , 'pVal' , ), 1061, (1061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseResolution' , 'pVal' , ), 1061, (1061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Resolution' , 'pVal' , ), 1062, (1062, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Resolution' , 'pVal' , ), 1062, (1062, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumNoOfSheetSegments' , 'pVal' , ), 1063, (1063, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumNoOfSheetSegments' , 'pVal' , ), 1063, (1063, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'MaximumNoOfSheetSegments' , 'pVal' , ), 1064, (1064, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'MaximumNoOfSheetSegments' , 'pVal' , ), 1064, (1064, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
]

IMTT2DContactProperty_vtables_dispatch_ = 1
IMTT2DContactProperty_vtables_ = [
	(( 'Stiffness' , 'ppVal' , ), 1001, (1001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 1002, (1002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MaximumDamping' , 'ppVal' , ), 1003, (1003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BoundaryPenetration' , 'ppVal' , ), 1004, (1004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 1005, (1005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 1006, (1006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ThresholdVelocity' , 'ppVal' , ), 1007, (1007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStiffness' , 'ppVal' , ), 1008, (1008, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStiffnessExponent' , 'ppVal' , ), 1009, (1009, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SpecialMaximumDamping' , 'ppVal' , ), 1010, (1010, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SpecialBoundaryPenetration' , 'ppVal' , ), 1011, (1011, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SpecialIndentationExponent' , 'ppVal' , ), 1012, (1012, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SpecialFrictionCoefficient' , 'ppVal' , ), 1013, (1013, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SpecialThresholdVelocity' , 'ppVal' , ), 1014, (1014, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 1015, (1015, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 1015, (1015, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffnessExponent' , 'pVal' , ), 1016, (1016, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffnessExponent' , 'pVal' , ), 1016, (1016, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialMaximumDamping' , 'pVal' , ), 1017, (1017, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialMaximumDamping' , 'pVal' , ), 1017, (1017, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialBoundaryPenetration' , 'pVal' , ), 1018, (1018, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialBoundaryPenetration' , 'pVal' , ), 1018, (1018, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialIndentationExponent' , 'pVal' , ), 1019, (1019, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialIndentationExponent' , 'pVal' , ), 1019, (1019, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialFrictionCoefficient' , 'pVal' , ), 1020, (1020, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialFrictionCoefficient' , 'pVal' , ), 1020, (1020, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialThresholdVelocity' , 'pVal' , ), 1021, (1021, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialThresholdVelocity' , 'pVal' , ), 1021, (1021, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameterType' , 'pVal' , ), 1022, (1022, (), [ (16387, 10, None, "IID('{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameterType' , 'pVal' , ), 1022, (1022, (), [ (3, 1, None, "IID('{2B940F51-FDCD-4C1D-876F-84F5AA3430D3}')") , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 1023, (1023, (), [ (16387, 10, None, "IID('{C2680614-B10F-47FA-8127-29C03A89BDA7}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 1023, (1023, (), [ (3, 1, None, "IID('{C2680614-B10F-47FA-8127-29C03A89BDA7}')") , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseRDF' , 'pVal' , ), 1024, (1024, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseRDF' , 'pVal' , ), 1024, (1024, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRDF' , 'pVal' , ), 1025, (1025, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRDF' , 'pVal' , ), 1025, (1025, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'SpecialRDF' , 'ppVal' , ), 1026, (1026, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RDF' , 'ppVal' , ), 1027, (1027, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
]

IMTT2DContactPropertyGuide_vtables_dispatch_ = 1
IMTT2DContactPropertyGuide_vtables_ = [
	(( 'UseGuideTolerance' , 'pVal' , ), 1101, (1101, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseGuideTolerance' , 'pVal' , ), 1101, (1101, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialGuideTolerance' , 'pVal' , ), 1102, (1102, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialGuideTolerance' , 'pVal' , ), 1102, (1102, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'GuideTolerance' , 'ppVal' , ), 1103, (1103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'SpecialGuideTolerance' , 'ppVal' , ), 1104, (1104, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
]

IMTT2DContactPropertyPGuide_vtables_dispatch_ = 1
IMTT2DContactPropertyPGuide_vtables_ = [
	(( 'GuideVelocity' , 'ppVal' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'GuideVelocityType' , 'pVal' , ), 1052, (1052, (), [ (16387, 10, None, "IID('{E92AC4EA-B94E-47DB-A4DD-39C954D07299}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'GuideVelocityType' , 'pVal' , ), 1052, (1052, (), [ (3, 1, None, "IID('{E92AC4EA-B94E-47DB-A4DD-39C954D07299}')") , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'GuideVelocityExpression' , 'ppVal' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'GuideVelocityExpression' , 'ppVal' , ), 1053, (1053, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
]

IMTT2DContactPropertyRoller_vtables_dispatch_ = 1
IMTT2DContactPropertyRoller_vtables_ = [
	(( 'UseMaxStictionDeformation' , 'pVal' , ), 1051, (1051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UseMaxStictionDeformation' , 'pVal' , ), 1051, (1051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'MaxStictionDeformation' , 'ppVal' , ), 1052, (1052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

IMTT2DContactPropertyRollerMovableToFixed_vtables_dispatch_ = 1
IMTT2DContactPropertyRollerMovableToFixed_vtables_ = [
	(( 'OffsetPenetration' , 'ppVal' , ), 1101, (1101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
]

IMTT2DContactPropertyRollerToSheet_vtables_dispatch_ = 1
IMTT2DContactPropertyRollerToSheet_vtables_ = [
]

IMTT2DContactSheetToSheet_vtables_dispatch_ = 1
IMTT2DContactSheetToSheet_vtables_ = [
	(( 'BaseSheetGroup' , 'ppVal' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BaseSheetGroup' , 'ppVal' , ), 1051, (1051, (), [ (9, 1, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActionSheetGroup' , 'ppVal' , ), 1052, (1052, (), [ (16393, 10, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ActionSheetGroup' , 'ppVal' , ), 1052, (1052, (), [ (9, 1, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertySheetToSheet' , 'ppVal' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{3641A1D2-6FCC-40AA-A4AA-8176CF6C755E}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 1054, (1054, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 1054, (1054, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoints' , 'ppVal' , ), 1055, (1055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPoints' , 'ppVal' , ), 1056, (1056, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 1057, (1057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 1057, (1057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IMTT2DContactSheetToSheetCollection_vtables_dispatch_ = 1
IMTT2DContactSheetToSheetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{AB78805A-064A-4015-812D-1332288F5789}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT2DFixedRollerGroupCollection_vtables_dispatch_ = 1
IMTT2DFixedRollerGroupCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{0E7F0C51-106B-446A-93A5-1912034EA1A7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT2DFlexibleRollerProperty_vtables_dispatch_ = 1
IMTT2DFlexibleRollerProperty_vtables_ = [
	(( 'Depth' , 'ppVal' , ), 1001, (1001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FDRRadius' , 'ppVal' , ), 1002, (1002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'NoOfNodesCircumference' , 'pVal' , ), 1003, (1003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NoOfNodesRadial' , 'pVal' , ), 1004, (1004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MassType' , 'type' , ), 1005, (1005, (), [ (3, 1, None, "IID('{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MassType' , 'type' , ), 1005, (1005, (), [ (16387, 10, None, "IID('{BCA74B1C-D06D-4C58-9338-8A2C2D6DE707}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'ppVal' , ), 1006, (1006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TotalMass' , 'ppVal' , ), 1007, (1007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingRatio' , 'ppVal' , ), 1008, (1008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus' , 'ppVal' , ), 1009, (1009, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'PoissonsRatio' , 'ppVal' , ), 1010, (1010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDensity' , 'ppVal' , ), 1011, (1011, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SpecialTotalMass' , 'ppVal' , ), 1012, (1012, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDampingRatio' , 'ppVal' , ), 1013, (1013, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SpecialYoungsModulus' , 'ppVal' , ), 1014, (1014, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SpecialPoissonsRatio' , 'ppVal' , ), 1015, (1015, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'AllDensity' , 'pVal' , ), 1016, (1016, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'AllDensity' , 'pVal' , ), 1016, (1016, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AllTotalMass' , 'pVal' , ), 1017, (1017, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AllTotalMass' , 'pVal' , ), 1017, (1017, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AllDampingRatio' , 'pVal' , ), 1018, (1018, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AllDampingRatio' , 'pVal' , ), 1018, (1018, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulus' , 'pVal' , ), 1019, (1019, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulus' , 'pVal' , ), 1019, (1019, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'AllPoissonsRatio' , 'pVal' , ), 1020, (1020, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'AllPoissonsRatio' , 'pVal' , ), 1020, (1020, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDensity' , 'pVal' , ), 1021, (1021, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDensity' , 'pVal' , ), 1021, (1021, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialTotalMass' , 'pVal' , ), 1022, (1022, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialTotalMass' , 'pVal' , ), 1022, (1022, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDampingRatio' , 'pVal' , ), 1023, (1023, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDampingRatio' , 'pVal' , ), 1023, (1023, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulus' , 'pVal' , ), 1024, (1024, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulus' , 'pVal' , ), 1024, (1024, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPoissonsRatio' , 'pVal' , ), 1025, (1025, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPoissonsRatio' , 'pVal' , ), 1025, (1025, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'DrillingStiffnessFactor' , 'ppVal' , ), 1026, (1026, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 1027, (1027, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 1027, (1027, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

IMTT2DForceNodal_vtables_dispatch_ = 1
IMTT2DForceNodal_vtables_ = [
	(( 'UserSubroutine' , 'ppVal' , ), 1051, (1051, (), [ (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'ppVal' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SetAppliedBody' , 'pVal' , 'vBool' , 'pResult' , ), 1052, (1052, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetAppliedBody' , 'pVal' , 'pResult' , ), 1053, (1053, (), [ (8, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 1054, (1054, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 1054, (1054, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IMTT2DForceNodalCollection_vtables_dispatch_ = 1
IMTT2DForceNodalCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{0F707193-3BDD-4899-8FD9-E9C21739ECCB}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT2DForceSpring_vtables_dispatch_ = 1
IMTT2DForceSpring_vtables_ = [
	(( 'BaseBody' , 'ppVal' , ), 1001, (1001, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 1001, (1001, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 1002, (1002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialStiffness' , 'pVal' , ), 1002, (1002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDamping' , 'pVal' , ), 1003, (1003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDamping' , 'pVal' , ), 1003, (1003, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPreload' , 'pVal' , ), 1004, (1004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialPreload' , 'pVal' , ), 1004, (1004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'SpecialStiffness' , 'ppVal' , ), 1008, (1008, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDamping' , 'ppVal' , ), 1009, (1009, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'SpecialPreload' , 'ppVal' , ), 1010, (1010, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
]

IMTT2DForceSpringNip_vtables_dispatch_ = 1
IMTT2DForceSpringNip_vtables_ = [
	(( 'BasePoint' , 'pVal' , ), 1051, (1051, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'BasePoint' , 'pVal' , ), 1051, (1051, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UseBasePoint' , 'pVal' , ), 1052, (1052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseBasePoint' , 'pVal' , ), 1052, (1052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
]

IMTT2DForceSpringTSD_vtables_dispatch_ = 1
IMTT2DForceSpringTSD_vtables_ = [
	(( 'ActionPoint' , 'pVal' , ), 1051, (1051, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ActionPoint' , 'pVal' , ), 1051, (1051, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UseStopperDistance' , 'pVal' , ), 1052, (1052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseStopperDistance' , 'pVal' , ), 1052, (1052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'StopperDistance' , 'ppVal' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'StopperFactor' , 'ppVal' , ), 1054, (1054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
]

IMTT2DGroupFixedRoller_vtables_dispatch_ = 1
IMTT2DGroupFixedRoller_vtables_ = [
	(( 'BaseBody' , 'pStr' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'pStr' , ), 1051, (1051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'pVal' , ), 1052, (1052, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'pVal' , ), 1052, (1052, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'ppVal' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 1054, (1054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Inertia' , 'ppVal' , ), 1055, (1055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 1056, (1056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 1056, (1056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Motion' , 'ppVal' , ), 1057, (1057, (), [ (16393, 10, None, "IID('{47F4E55C-4291-4251-866A-98A74112D266}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 1058, (1058, (), [ (16393, 10, None, "IID('{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1059, (1059, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1059, (1059, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'RollerBodyType' , 'pVal' , ), 1060, (1060, (), [ (16387, 10, None, "IID('{965EA0D7-3B24-4C39-87DD-0E6C1EA1CA47}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UpdateNonGeometricProperties' , ), 1063, (1063, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'RollerBody' , 'pVal' , ), 1064, (1064, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'RevJoint' , 'pVal' , ), 1065, (1065, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 1066, (1066, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 1066, (1066, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoints' , 'ppVal' , ), 1067, (1067, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPoints' , 'ppVal' , ), 1068, (1068, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 1069, (1069, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 1069, (1069, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
]

IMTT2DGroupFixedRollerShell_vtables_dispatch_ = 1
IMTT2DGroupFixedRollerShell_vtables_ = [
	(( 'BaseBody' , 'pStr' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'pStr' , ), 1051, (1051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'pVal' , ), 1052, (1052, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'pVal' , ), 1052, (1052, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'ppVal' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 1054, (1054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 1054, (1054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Motion' , 'ppVal' , ), 1055, (1055, (), [ (16393, 10, None, "IID('{47F4E55C-4291-4251-866A-98A74112D266}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 1056, (1056, (), [ (16393, 10, None, "IID('{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1057, (1057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1057, (1057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FlexibleRollerProperty' , 'ppVal' , ), 1058, (1058, (), [ (16393, 10, None, "IID('{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UpdateNonGeometricProperties' , ), 1059, (1059, (), [ ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseExtractWithoutPreStress' , ), 1060, (1060, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'FlexBody' , 'ppVal' , ), 1061, (1061, (), [ (16393, 10, None, "IID('{9257FD72-F3D0-4E57-A114-2045356D78CD}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 1062, (1062, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 1062, (1062, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoints' , 'ppVal' , ), 1063, (1063, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPoints' , 'ppVal' , ), 1064, (1064, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 1065, (1065, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 1065, (1065, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

IMTT2DGroupGuideBody_vtables_dispatch_ = 1
IMTT2DGroupGuideBody_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'StartPoint' , 'ppVal' , ), 1052, (1052, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SecondPoint' , 'ppVal' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 1054, (1054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'InertiaMoment' , 'ppVal' , ), 1055, (1055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseJointPoint' , 'pVal' , ), 1056, (1056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseJointPoint' , 'pVal' , ), 1056, (1056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'JointPoint' , 'pVal' , ), 1057, (1057, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'JointPoint' , 'pVal' , ), 1057, (1057, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseTSD' , 'pVal' , ), 1058, (1058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseTSD' , 'pVal' , ), 1058, (1058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'TSD' , 'ppVal' , ), 1059, (1059, (), [ (16393, 10, None, "IID('{66947C3A-68E2-406E-9491-42952BD66A96}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1060, (1060, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1060, (1060, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'SetStartPoint' , 'dX' , 'dY' , 'dZ' , ), 1061, (1061, (), [ 
			 (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'SetStartParametricPoint' , 'pVal' , ), 1062, (1062, (), [ (9, 1, None, "IID('{64B0B5B9-7662-40E8-B27C-9E42C3A158BF}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'SetSecondPoint' , 'dX' , 'dY' , 'dZ' , ), 1063, (1063, (), [ 
			 (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'SetSecondParametricPoint' , 'pVal' , ), 1064, (1064, (), [ (9, 1, None, "IID('{64B0B5B9-7662-40E8-B27C-9E42C3A158BF}')") , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
]

IMTT2DGroupMovableRoller_vtables_dispatch_ = 1
IMTT2DGroupMovableRoller_vtables_ = [
	(( 'BaseBody' , 'ppVal' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 1051, (1051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Direction' , 'pVal' , ), 1052, (1052, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Direction' , 'pVal' , ), 1052, (1052, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'ppVal' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 1054, (1054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Inertia' , 'ppVal' , ), 1055, (1055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialGap' , 'pVal' , ), 1056, (1056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialGap' , 'pVal' , ), 1056, (1056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'InitialGap' , 'value' , ), 1057, (1057, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'InitialGap' , 'value' , ), 1057, (1057, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 1058, (1058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 1058, (1058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Motion' , 'ppVal' , ), 1059, (1059, (), [ (16393, 10, None, "IID('{47F4E55C-4291-4251-866A-98A74112D266}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 1060, (1060, (), [ (16393, 10, None, "IID('{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToFixedRoller' , 'ppVal' , ), 1061, (1061, (), [ (16393, 10, None, "IID('{B006CA26-0F57-4100-9224-D3D62429E8F6}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseNipSpring' , 'pVal' , ), 1062, (1062, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseNipSpring' , 'pVal' , ), 1062, (1062, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'NipSpring' , 'ppVal' , ), 1063, (1063, (), [ (16393, 10, None, "IID('{4A4DE5B0-59EF-4CD2-B669-93768E326904}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UseSoftNip' , 'pVal' , ), 1064, (1064, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseSoftNip' , 'pVal' , ), 1064, (1064, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'SoftNip' , 'ppVal' , ), 1065, (1065, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'SoftNip' , 'ppVal' , ), 1065, (1065, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumGap' , 'pVal' , ), 1066, (1066, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumGap' , 'pVal' , ), 1066, (1066, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'MaximumGap' , 'ppVal' , ), 1067, (1067, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1068, (1068, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1068, (1068, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'RollerBodyType' , 'pVal' , ), 1070, (1070, (), [ (16387, 10, None, "IID('{965EA0D7-3B24-4C39-87DD-0E6C1EA1CA47}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UpdateNonGeometricProperties' , ), 1073, (1073, (), [ ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'DirectionEx' , 'ppVec' , ), 1074, (1074, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'value' , ), 1075, (1075, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'DirectionType' , 'pVal' , ), 1076, (1076, (), [ (16387, 10, None, "IID('{21BC4DDF-6454-4049-A7E7-797B0FD7A54F}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'DirectionType' , 'pVal' , ), 1076, (1076, (), [ (3, 1, None, "IID('{21BC4DDF-6454-4049-A7E7-797B0FD7A54F}')") , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoUpdateGeometry' , 'pVal' , ), 1077, (1077, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoUpdateGeometry' , 'pVal' , ), 1077, (1077, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'RollerBody' , 'pVal' , ), 1078, (1078, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'RARBody' , 'pVal' , ), 1079, (1079, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'RevJoint' , 'pVal' , ), 1080, (1080, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'TraJoint' , 'pVal' , ), 1081, (1081, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'SpringForce' , 'pVal' , ), 1082, (1082, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'GroupFixedRoller' , 'pVal' , ), 1083, (1083, (), [ (16393, 10, None, "IID('{979CB058-D7B2-4D8B-9EA5-26C16B8C5547}')") , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDirectionAngle' , 'ppVal' , ), 1084, (1084, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToSheet' , 'pVal' , ), 1085, (1085, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToSheet' , 'pVal' , ), 1085, (1085, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToRoller' , 'pVal' , ), 1086, (1086, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToRoller' , 'pVal' , ), 1086, (1086, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'ContactPointsToSheet' , 'ppVal' , ), 1087, (1087, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'ContactPointsToRoller' , 'ppVal' , ), 1088, (1088, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPointsToSheet' , 'ppVal' , ), 1089, (1089, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPointsToRoller' , 'ppVal' , ), 1090, (1090, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToSheet' , 'pVal' , ), 1091, (1091, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToSheet' , 'pVal' , ), 1091, (1091, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToRoller' , 'pVal' , ), 1092, (1092, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToRoller' , 'pVal' , ), 1092, (1092, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
]

IMTT2DGroupMovableRollerShell_vtables_dispatch_ = 1
IMTT2DGroupMovableRollerShell_vtables_ = [
	(( 'BaseBody' , 'ppVal' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 1051, (1051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'DirectionType' , 'pVal' , ), 1052, (1052, (), [ (16387, 10, None, "IID('{21BC4DDF-6454-4049-A7E7-797B0FD7A54F}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DirectionType' , 'pVal' , ), 1052, (1052, (), [ (3, 1, None, "IID('{21BC4DDF-6454-4049-A7E7-797B0FD7A54F}')") , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'ppVec' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DirectionAngle' , 'ppVal' , ), 1054, (1054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'ppVal' , ), 1055, (1055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialGap' , 'pVal' , ), 1056, (1056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialGap' , 'pVal' , ), 1056, (1056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'InitialGap' , 'value' , ), 1057, (1057, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'InitialGap' , 'value' , ), 1057, (1057, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 1058, (1058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseMotion' , 'pVal' , ), 1058, (1058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Motion' , 'ppVal' , ), 1059, (1059, (), [ (16393, 10, None, "IID('{47F4E55C-4291-4251-866A-98A74112D266}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 1060, (1060, (), [ (16393, 10, None, "IID('{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToFixedRoller' , 'ppVal' , ), 1061, (1061, (), [ (16393, 10, None, "IID('{B006CA26-0F57-4100-9224-D3D62429E8F6}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseNipSpring' , 'pVal' , ), 1062, (1062, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseNipSpring' , 'pVal' , ), 1062, (1062, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'NipSpring' , 'ppVal' , ), 1063, (1063, (), [ (16393, 10, None, "IID('{4A4DE5B0-59EF-4CD2-B669-93768E326904}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UseSoftNip' , 'pVal' , ), 1064, (1064, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseSoftNip' , 'pVal' , ), 1064, (1064, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'SoftNip' , 'ppVal' , ), 1065, (1065, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'SoftNip' , 'ppVal' , ), 1065, (1065, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumGap' , 'pVal' , ), 1066, (1066, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumGap' , 'pVal' , ), 1066, (1066, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'MaximumGap' , 'ppVal' , ), 1067, (1067, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1068, (1068, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoCenterMarker' , 'pVal' , ), 1068, (1068, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'FlexibleRollerProperty' , 'ppVal' , ), 1069, (1069, (), [ (16393, 10, None, "IID('{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UpdateNonGeometricProperties' , ), 1070, (1070, (), [ ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'GroupFixedRoller' , 'pVal' , ), 1071, (1071, (), [ (16393, 10, None, "IID('{979CB058-D7B2-4D8B-9EA5-26C16B8C5547}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'UseExtractWithoutPreStress' , ), 1072, (1072, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDirectionAngle' , 'ppVal' , ), 1073, (1073, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'FlexBody' , 'ppVal' , ), 1074, (1074, (), [ (16393, 10, None, "IID('{9257FD72-F3D0-4E57-A114-2045356D78CD}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToSheet' , 'pVal' , ), 1075, (1075, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToSheet' , 'pVal' , ), 1075, (1075, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToRoller' , 'pVal' , ), 1076, (1076, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplayToRoller' , 'pVal' , ), 1076, (1076, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'ContactPointsToSheet' , 'ppVal' , ), 1077, (1077, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'ContactPointsToRoller' , 'ppVal' , ), 1078, (1078, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPointsToSheet' , 'ppVal' , ), 1079, (1079, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPointsToRoller' , 'ppVal' , ), 1080, (1080, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToSheet' , 'pVal' , ), 1081, (1081, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToSheet' , 'pVal' , ), 1081, (1081, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToRoller' , 'pVal' , ), 1082, (1082, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPointsToRoller' , 'pVal' , ), 1082, (1082, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
]

IMTT2DGroupSheet_vtables_dispatch_ = 1
IMTT2DGroupSheet_vtables_ = [
	(( 'SegmentNumber' , 'pVal' , ), 1051, (1051, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'SegmentLength' , 'ppVal' , ), 1052, (1052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'HoldNoise' , 'pVal' , ), 1053, (1053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'HoldNoise' , 'pVal' , ), 1053, (1053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAllProperties' , ), 1054, (1054, (), [ ], 1 , 1 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'UpdateNonGeometricProperties' , ), 1055, (1055, (), [ ], 1 , 1 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'UseAirResistance' , 'pVal' , ), 1056, (1056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'UseAirResistance' , 'pVal' , ), 1056, (1056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceType' , 'pVal' , ), 1057, (1057, (), [ (16387, 10, None, "IID('{30770DB1-361B-40D9-895D-32D0523B640B}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceType' , 'pVal' , ), 1057, (1057, (), [ (3, 1, None, "IID('{30770DB1-361B-40D9-895D-32D0523B640B}')") , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceConstant' , 'ppVal' , ), 1058, (1058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceExpression' , 'ppVal' , ), 1059, (1059, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'AirResistanceExpression' , 'ppVal' , ), 1059, (1059, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'SheetBodyCollection' , 'ppVal' , ), 1060, (1060, (), [ (16393, 10, None, "IID('{767F4D3F-26B8-4F0A-B982-9A7FAC6CD1B2}')") , ], 1 , 2 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'RevoluteJointCollection' , 'ppVal' , ), 1061, (1061, (), [ (16393, 10, None, "IID('{AFC279E7-53CD-4DA1-96E2-3833740C410A}')") , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'PlanarJoint' , 'pVal' , ), 1062, (1062, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'RotationalSpringCollection' , 'ppVal' , ), 1063, (1063, (), [ (16393, 10, None, "IID('{F38F6090-E64E-4BA5-96B1-9865E77C4B31}')") , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAllProperties2' , ), 1064, (1064, (), [ ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'EachRenderMode' , 'pVal' , ), 1065, (1065, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}')") , ], 1 , 4 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'EachRenderMode' , 'pVal' , ), 1065, (1065, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}')") , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'GetOutputSheetList' , 'ppSafeArray' , ), 1066, (1066, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'AddOutputSheet' , 'strFileName' , ), 1067, (1067, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputSheet' , 'strFileName' , ), 1068, (1068, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'AddAllOutputSheet' , ), 1069, (1069, (), [ ], 1 , 1 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'RemoveAllOutputSheet' , ), 1070, (1070, (), [ ], 1 , 1 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'UpdateActiveFlagOfAllEntities' , 'val' , ), 1071, (1071, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
]

IMTT2DGroupSheetCollection_vtables_dispatch_ = 1
IMTT2DGroupSheetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT2DGuide_vtables_dispatch_ = 1
IMTT2DGuide_vtables_ = [
	(( 'MotherBody' , 'ppVal' , ), 1001, (1001, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MotherBody' , 'ppVal' , ), 1001, (1001, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAllProperties' , ), 1002, (1002, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 1003, (1003, (), [ (16393, 10, None, "IID('{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 1004, (1004, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 1004, (1004, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoints' , 'ppVal' , ), 1005, (1005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SpecialContactPoints' , 'ppVal' , ), 1006, (1006, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 1007, (1007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialContactPoints' , 'pVal' , ), 1007, (1007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IMTT2DGuideArc_vtables_dispatch_ = 1
IMTT2DGuideArc_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 1052, (1052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'ppVal' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 1054, (1054, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 1054, (1054, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ContactUpDirection' , 'pVal' , ), 1055, (1055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ContactUpDirection' , 'pVal' , ), 1055, (1055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 1056, (1056, (), [ (16393, 10, None, "IID('{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeStart' , 'pVal' , ), 1057, (1057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeStart' , 'pVal' , ), 1057, (1057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeEnd' , 'pVal' , ), 1058, (1058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeEnd' , 'pVal' , ), 1058, (1058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRadius' , 'pVal' , ), 1059, (1059, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRadius' , 'pVal' , ), 1059, (1059, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'SpecialRadius' , 'ppVal' , ), 1060, (1060, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeRadius' , 'ppVal' , ), 1061, (1061, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
]

IMTT2DGuideCircular_vtables_dispatch_ = 1
IMTT2DGuideCircular_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CenterPoint' , 'ppVal' , ), 1052, (1052, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 1053, (1053, (), [ (16393, 10, None, "IID('{B4F3A991-0483-415B-820F-A8B4116A3C9A}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

IMTT2DGuideCollection_vtables_dispatch_ = 1
IMTT2DGuideCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{333258BF-4C43-4C96-9079-6A4D54A4703C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT2DGuideLinear_vtables_dispatch_ = 1
IMTT2DGuideLinear_vtables_ = [
	(( 'StartPoint' , 'ppVal' , ), 1051, (1051, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'SecondPoint' , 'ppVal' , ), 1052, (1052, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ContactUpDirection' , 'pVal' , ), 1053, (1053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ContactUpDirection' , 'pVal' , ), 1053, (1053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ContactPropertyToSheet' , 'ppVal' , ), 1054, (1054, (), [ (16393, 10, None, "IID('{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeStart' , 'pVal' , ), 1055, (1055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeStart' , 'pVal' , ), 1055, (1055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeEnd' , 'pVal' , ), 1056, (1056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeEnd' , 'pVal' , ), 1056, (1056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRadius' , 'pVal' , ), 1057, (1057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialRadius' , 'pVal' , ), 1057, (1057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'SpecialRadius' , 'ppVal' , ), 1058, (1058, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ImaginaryPEdgeRadius' , 'ppVal' , ), 1059, (1059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
]

IMTT2DMovableRollerGroupCollection_vtables_dispatch_ = 1
IMTT2DMovableRollerGroupCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{D4F728AD-8867-4AA8-B319-88687F79C526}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT2DSheet_vtables_dispatch_ = 1
IMTT2DSheet_vtables_ = [
	(( 'StartPoint' , 'pVal' , ), 1001, (1001, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'StartPoint' , 'pVal' , ), 1001, (1001, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 1002, (1002, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DirectionPoint' , 'pVal' , ), 1002, (1002, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Fold' , 'pVal' , ), 1003, (1003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'PointList' , 'pVal' , ), 1004, (1004, (), [ (24588, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PointList' , 'pVal' , ), 1004, (1004, (), [ (8204, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'ppVal' , ), 1005, (1005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'pVal' , ), 1006, (1006, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'pVal' , ), 1006, (1006, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'InitialVelocity' , 'ppVal' , ), 1007, (1007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'AllDensity' , 'pVal' , ), 1008, (1008, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'AllDensity' , 'pVal' , ), 1008, (1008, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulus' , 'pVal' , ), 1009, (1009, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'AllYoungsModulus' , 'pVal' , ), 1009, (1009, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'AllDampingRatio' , 'pVal' , ), 1010, (1010, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'AllDampingRatio' , 'pVal' , ), 1010, (1010, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'AllCurlRadius' , 'pVal' , ), 1011, (1011, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'AllCurlRadius' , 'pVal' , ), 1011, (1011, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDensity' , 'pVal' , ), 1012, (1012, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDensity' , 'pVal' , ), 1012, (1012, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulus' , 'pVal' , ), 1013, (1013, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialYoungsModulus' , 'pVal' , ), 1013, (1013, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDampingRatio' , 'pVal' , ), 1014, (1014, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialDampingRatio' , 'pVal' , ), 1014, (1014, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialCurlRadius' , 'pVal' , ), 1015, (1015, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialCurlRadius' , 'pVal' , ), 1015, (1015, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'ppVal' , ), 1016, (1016, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus' , 'ppVal' , ), 1017, (1017, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'DampingRatio' , 'ppVal' , ), 1018, (1018, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'CurlRadius' , 'ppVal' , ), 1019, (1019, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDensity' , 'ppVal' , ), 1020, (1020, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SpecialYoungsModulus' , 'ppVal' , ), 1021, (1021, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'SpecialDampingRatio' , 'ppVal' , ), 1022, (1022, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'SpecialCurlRadius' , 'ppVal' , ), 1023, (1023, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialThickness' , 'pVal' , ), 1024, (1024, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'UseSpecialThickness' , 'pVal' , ), 1024, (1024, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'SetLayerNumber' , 'iVal' , ), 1025, (1025, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'SpecialThickness' , 'ppVal' , ), 1026, (1026, (), [ (16393, 10, None, "IID('{B58006F8-C5AC-4B97-8096-AF292F9DBE55}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryAutomatically' , 'pVal' , ), 1027, (1027, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryAutomatically' , 'pVal' , ), 1027, (1027, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
]

IMTT2DSheetBodyCollection_vtables_dispatch_ = 1
IMTT2DSheetBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT2DSheetRevJointCollection_vtables_dispatch_ = 1
IMTT2DSheetRevJointCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{B9173DAD-05DD-4037-9367-726DDDEE988E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT2DSheetRotSpringCollection_vtables_dispatch_ = 1
IMTT2DSheetRotSpringCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{EB73DE47-2BB8-46BD-A904-F61BCBC59D1F}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMTT2DSubSystem_vtables_dispatch_ = 1
IMTT2DSubSystem_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 1000, (1000, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupSheet' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'iNoOfSegments' , 
			 'dSegmentLength' , 'dSheetThickness' , 'ppResult' , ), 1001, (1001, (), [ (8, 1, None, None) , 
			 (8197, 1, None, None) , (8197, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , 
			 (16393, 10, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupSheetFolding' , 'strName' , 'pMultiPoints' , 'iNoOfSegments' , 'dSegmentLength' , 
			 'dSheetThickness' , 'ppResult' , ), 1002, (1002, (), [ (8, 1, None, None) , (8204, 1, None, None) , 
			 (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupFixedRoller' , 'strName' , 'pPoint' , 'dRadius' , 'ppResult' , 
			 ), 1003, (1003, (), [ (8, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{0E7F0C51-106B-446A-93A5-1912034EA1A7}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupMovableRoller' , 'strName' , 'pIFixedRoller' , 'pDirection' , 'dRadius' , 
			 'dDistance' , 'ppResult' , ), 1004, (1004, (), [ (8, 1, None, None) , (9, 1, None, "IID('{0E7F0C51-106B-446A-93A5-1912034EA1A7}')") , 
			 (8197, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{D4F728AD-8867-4AA8-B319-88687F79C526}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupRollerPair' , 'strFixedRollerName' , 'pPoint' , 'dFixedRollerRadius' , 'strMovableRollerName' , 
			 'pDirection' , 'dMovableRollerRadius' , 'dDistance' , 'ppResult' , ), 1005, (1005, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , 
			 (5, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{0E7F0C51-106B-446A-93A5-1912034EA1A7}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupGuideBody' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'dRadius' , 
			 'ppResult' , ), 1006, (1006, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{1AB7F0EE-74C9-4EF7-89BF-14AAF15EF35E}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideArc' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'dAngle' , 
			 'ppResult' , ), 1007, (1007, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{13439214-7EB0-439C-8C42-A2D55F1CC798}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideLinear' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'ppResult' , 
			 ), 1008, (1008, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{F4AE0FC8-97F2-4BA3-B061-799E91800B51}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideCircular' , 'strName' , 'pFirstPoint' , 'dRadius' , 'ppResult' , 
			 ), 1009, (1009, (), [ (8, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{2AEBA258-C4AC-4EAA-ADF1-BAF8730E6E99}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactSheetToSheet' , 'strName' , 'pBaseSheet' , 'pActionSheet' , 'ppResult' , 
			 ), 1010, (1010, (), [ (8, 1, None, None) , (9, 0, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , (9, 0, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , (16393, 10, None, "IID('{AB78805A-064A-4015-812D-1332288F5789}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceNodal' , 'strName' , 'pSheet' , 'ppResult' , ), 1011, (1011, (), [ 
			 (8, 1, None, None) , (9, 0, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , (16393, 10, None, "IID('{0F707193-3BDD-4899-8FD9-E9C21739ECCB}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'GuideConvert' , 'pMultiBodies' , 'pResult' , ), 1012, (1012, (), [ (8204, 1, None, None) , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'AlignSheetInRollers' , 'pSheet' , 'pMovableRoller' , 'pResult' , ), 1013, (1013, (), [ 
			 (9, 1, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , (9, 1, None, "IID('{D4F728AD-8867-4AA8-B319-88687F79C526}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupFlexibleFixedRoller' , 'name' , 'numNodesCircumference' , 'numNodesRadial' , 'roller' , 
			 ), 1014, (1014, (), [ (8, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{91034068-E6A9-4616-9D41-9B666E4018AB}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupFlexibleMovableRoller' , 'name' , 'numNodesCircumference' , 'numNodesRadial' , 'rollerFixed' , 
			 'roller' , ), 1015, (1015, (), [ (8, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , 
			 (9, 1, None, "IID('{979CB058-D7B2-4D8B-9EA5-26C16B8C5547}')") , (16393, 10, None, "IID('{2310F73F-2BE6-4338-93FF-609E572F4802}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'GuideConvertWithColor' , 'pMultiBodies' , 'oleColor' , 'pResult' , ), 1016, (1016, (), [ 
			 (8204, 1, None, None) , (19, 1, None, None) , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Assembly' , 'ppAssembly' , ), 1020, (1020, (), [ (16393, 10, None, "IID('{24C00315-36B5-498A-99A5-A3D3074E24DF}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorSpeed' , 'strName' , 'pPosition' , 'pDirection' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 1021, (1021, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{CCB7E742-F0DF-4F22-A377-04AA675FD281}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorDistance' , 'strName' , 'pPosition' , 'pDirection' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 1022, (1022, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{0CC3861B-CC2A-4402-9135-C8BC804EABBD}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorEvent' , 'strName' , 'pPosition' , 'pEntity' , 'dRange' , 
			 'ppVal' , ), 1023, (1023, (), [ (8, 1, None, None) , (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{FB0F1AE7-3A1E-4326-B1BF-8225DA2BF11E}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideArcWithEndPoint' , 'strName' , 'pCenterPoint' , 'pStartPoint' , 'pEndPoint' , 
			 'bDirection' , 'ppResult' , ), 1025, (1025, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (8197, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{13439214-7EB0-439C-8C42-A2D55F1CC798}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupMovableRollerWithAngle' , 'strName' , 'pIFixedRoller' , 'dAngle' , 'dRadius' , 
			 'dDistance' , 'ppResult' , ), 1026, (1026, (), [ (8, 1, None, None) , (9, 1, None, "IID('{0E7F0C51-106B-446A-93A5-1912034EA1A7}')") , 
			 (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{D4F728AD-8867-4AA8-B319-88687F79C526}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupSheet2' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'iNoOfSegments' , 
			 'dSegmentLength' , 'ppResult' , ), 1027, (1027, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupSheetFoldingWithPointList' , 'strName' , 'strFile' , 'iNoOfSegments' , 'dSegmentLength' , 
			 'dSheetThickness' , 'ppResult' , ), 1028, (1028, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (3, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorTension' , 'name' , 'ppVal' , ), 1029, (1029, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{55C49622-A503-4651-BF1E-2A84CD9E27AB}')") , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupSheetWithCurve' , 'strName' , 'pCurve' , 'iNoOfSegments' , 'dSheetThickness' , 
			 'ppResult' , ), 1030, (1030, (), [ (8, 1, None, None) , (9, 1, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , (3, 1, None, None) , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{59FE2E3A-2043-4651-8D6E-A58D8800205A}')") , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'FixedRollerGroupCollection' , 'ppVal' , ), 1031, (1031, (), [ (16393, 10, None, "IID('{8393C52E-FB87-4F44-AA3B-CF6BE4045DEA}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'MovableRollerGroupCollection' , 'ppVal' , ), 1032, (1032, (), [ (16393, 10, None, "IID('{1F97796F-D817-4F6D-BDD4-057FAB6AB0C1}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'GroupSheetCollection' , 'ppVal' , ), 1033, (1033, (), [ (16393, 10, None, "IID('{6DAA417B-BEE4-49CE-AD91-195F1AA003EF}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'ForceNodalCollection' , 'ppVal' , ), 1034, (1034, (), [ (16393, 10, None, "IID('{E3BB5B6C-23F0-4038-8466-36B8782CC65A}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'ContactSheetToSheetCollection' , 'ppVal' , ), 1035, (1035, (), [ (16393, 10, None, "IID('{9538383C-C3C2-463F-B9D5-9017468026D1}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'GuideCollection' , 'ppVal' , ), 1036, (1036, (), [ (16393, 10, None, "IID('{18DD760B-C7E8-4BCF-BAE7-EC87A7D22B42}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Contour' , 'ppVal' , ), 1037, (1037, (), [ (16393, 10, None, "IID('{BDF4F979-28B7-48D2-BF06-9C59B70D467B}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorTension2' , 'strName' , 'pPosition' , 'pEntity' , 'dRange' , 
			 'ppVal' , ), 1038, (1038, (), [ (8, 1, None, None) , (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{55C49622-A503-4651-BF1E-2A84CD9E27AB}')") , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'CreateGuideCircularWithGuide' , 'strName' , 'pGuide' , 'bStartPoint' , 'bupDirection' , 
			 'dRadius' , 'ppResult' , ), 1039, (1039, (), [ (8, 1, None, None) , (9, 1, None, "IID('{333258BF-4C43-4C96-9079-6A4D54A4703C}')") , 
			 (11, 1, None, None) , (11, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{2AEBA258-C4AC-4EAA-ADF1-BAF8730E6E99}')") , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{3641A1D2-6FCC-40AA-A4AA-8176CF6C755E}' : IMTT2DContactProperty,
	'{5FC1140C-915D-4378-A514-4E5D374B9D29}' : IMTT2DContactPropertyRoller,
	'{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}' : IMTT2DContactPropertyRollerToSheet,
	'{B006CA26-0F57-4100-9224-D3D62429E8F6}' : IMTT2DContactPropertyRollerMovableToFixed,
	'{B4F3A991-0483-415B-820F-A8B4116A3C9A}' : IMTT2DContactPropertyPGuide,
	'{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}' : IMTT2DContactPropertyGuide,
	'{5AB3349F-401D-4ED1-88E3-0A300C0C6B94}' : IMTT2DForceSpring,
	'{4A4DE5B0-59EF-4CD2-B669-93768E326904}' : IMTT2DForceSpringNip,
	'{66947C3A-68E2-406E-9491-42952BD66A96}' : IMTT2DForceSpringTSD,
	'{767F4D3F-26B8-4F0A-B982-9A7FAC6CD1B2}' : IMTT2DSheetBodyCollection,
	'{AFC279E7-53CD-4DA1-96E2-3833740C410A}' : IMTT2DSheetRevJointCollection,
	'{F38F6090-E64E-4BA5-96B1-9865E77C4B31}' : IMTT2DSheetRotSpringCollection,
	'{B6148C63-C63E-4B91-8051-EDCA38242816}' : IMTT2DSheet,
	'{59FE2E3A-2043-4651-8D6E-A58D8800205A}' : IMTT2DGroupSheet,
	'{0E7F0C51-106B-446A-93A5-1912034EA1A7}' : IMTT2DGroupFixedRoller,
	'{D4F728AD-8867-4AA8-B319-88687F79C526}' : IMTT2DGroupMovableRoller,
	'{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}' : IMTT2DFlexibleRollerProperty,
	'{91034068-E6A9-4616-9D41-9B666E4018AB}' : IMTT2DGroupFixedRollerShell,
	'{2310F73F-2BE6-4338-93FF-609E572F4802}' : IMTT2DGroupMovableRollerShell,
	'{1AB7F0EE-74C9-4EF7-89BF-14AAF15EF35E}' : IMTT2DGroupGuideBody,
	'{333258BF-4C43-4C96-9079-6A4D54A4703C}' : IMTT2DGuide,
	'{13439214-7EB0-439C-8C42-A2D55F1CC798}' : IMTT2DGuideArc,
	'{F4AE0FC8-97F2-4BA3-B061-799E91800B51}' : IMTT2DGuideLinear,
	'{2AEBA258-C4AC-4EAA-ADF1-BAF8730E6E99}' : IMTT2DGuideCircular,
	'{AB78805A-064A-4015-812D-1332288F5789}' : IMTT2DContactSheetToSheet,
	'{0F707193-3BDD-4899-8FD9-E9C21739ECCB}' : IMTT2DForceNodal,
	'{24C00315-36B5-498A-99A5-A3D3074E24DF}' : IMTT2DAssembly,
	'{8393C52E-FB87-4F44-AA3B-CF6BE4045DEA}' : IMTT2DFixedRollerGroupCollection,
	'{1F97796F-D817-4F6D-BDD4-057FAB6AB0C1}' : IMTT2DMovableRollerGroupCollection,
	'{6DAA417B-BEE4-49CE-AD91-195F1AA003EF}' : IMTT2DGroupSheetCollection,
	'{E3BB5B6C-23F0-4038-8466-36B8782CC65A}' : IMTT2DForceNodalCollection,
	'{9538383C-C3C2-463F-B9D5-9017468026D1}' : IMTT2DContactSheetToSheetCollection,
	'{18DD760B-C7E8-4BCF-BAE7-EC87A7D22B42}' : IMTT2DGuideCollection,
	'{4946A10D-6F44-45BC-B3F1-F1AA0CDA2C83}' : IMTT2DSubSystem,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{3641A1D2-6FCC-40AA-A4AA-8176CF6C755E}' : 'IMTT2DContactProperty',
	'{5FC1140C-915D-4378-A514-4E5D374B9D29}' : 'IMTT2DContactPropertyRoller',
	'{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}' : 'IMTT2DContactPropertyRollerToSheet',
	'{B006CA26-0F57-4100-9224-D3D62429E8F6}' : 'IMTT2DContactPropertyRollerMovableToFixed',
	'{B4F3A991-0483-415B-820F-A8B4116A3C9A}' : 'IMTT2DContactPropertyPGuide',
	'{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}' : 'IMTT2DContactPropertyGuide',
	'{5AB3349F-401D-4ED1-88E3-0A300C0C6B94}' : 'IMTT2DForceSpring',
	'{4A4DE5B0-59EF-4CD2-B669-93768E326904}' : 'IMTT2DForceSpringNip',
	'{66947C3A-68E2-406E-9491-42952BD66A96}' : 'IMTT2DForceSpringTSD',
	'{767F4D3F-26B8-4F0A-B982-9A7FAC6CD1B2}' : 'IMTT2DSheetBodyCollection',
	'{AFC279E7-53CD-4DA1-96E2-3833740C410A}' : 'IMTT2DSheetRevJointCollection',
	'{F38F6090-E64E-4BA5-96B1-9865E77C4B31}' : 'IMTT2DSheetRotSpringCollection',
	'{B6148C63-C63E-4B91-8051-EDCA38242816}' : 'IMTT2DSheet',
	'{59FE2E3A-2043-4651-8D6E-A58D8800205A}' : 'IMTT2DGroupSheet',
	'{0E7F0C51-106B-446A-93A5-1912034EA1A7}' : 'IMTT2DGroupFixedRoller',
	'{D4F728AD-8867-4AA8-B319-88687F79C526}' : 'IMTT2DGroupMovableRoller',
	'{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}' : 'IMTT2DFlexibleRollerProperty',
	'{91034068-E6A9-4616-9D41-9B666E4018AB}' : 'IMTT2DGroupFixedRollerShell',
	'{2310F73F-2BE6-4338-93FF-609E572F4802}' : 'IMTT2DGroupMovableRollerShell',
	'{1AB7F0EE-74C9-4EF7-89BF-14AAF15EF35E}' : 'IMTT2DGroupGuideBody',
	'{333258BF-4C43-4C96-9079-6A4D54A4703C}' : 'IMTT2DGuide',
	'{13439214-7EB0-439C-8C42-A2D55F1CC798}' : 'IMTT2DGuideArc',
	'{F4AE0FC8-97F2-4BA3-B061-799E91800B51}' : 'IMTT2DGuideLinear',
	'{2AEBA258-C4AC-4EAA-ADF1-BAF8730E6E99}' : 'IMTT2DGuideCircular',
	'{AB78805A-064A-4015-812D-1332288F5789}' : 'IMTT2DContactSheetToSheet',
	'{0F707193-3BDD-4899-8FD9-E9C21739ECCB}' : 'IMTT2DForceNodal',
	'{24C00315-36B5-498A-99A5-A3D3074E24DF}' : 'IMTT2DAssembly',
	'{8393C52E-FB87-4F44-AA3B-CF6BE4045DEA}' : 'IMTT2DFixedRollerGroupCollection',
	'{1F97796F-D817-4F6D-BDD4-057FAB6AB0C1}' : 'IMTT2DMovableRollerGroupCollection',
	'{6DAA417B-BEE4-49CE-AD91-195F1AA003EF}' : 'IMTT2DGroupSheetCollection',
	'{E3BB5B6C-23F0-4038-8466-36B8782CC65A}' : 'IMTT2DForceNodalCollection',
	'{9538383C-C3C2-463F-B9D5-9017468026D1}' : 'IMTT2DContactSheetToSheetCollection',
	'{18DD760B-C7E8-4BCF-BAE7-EC87A7D22B42}' : 'IMTT2DGuideCollection',
	'{4946A10D-6F44-45BC-B3F1-F1AA0CDA2C83}' : 'IMTT2DSubSystem',
}


NamesToIIDMap = {
	'IMTT2DContactProperty' : '{3641A1D2-6FCC-40AA-A4AA-8176CF6C755E}',
	'IMTT2DContactPropertyRoller' : '{5FC1140C-915D-4378-A514-4E5D374B9D29}',
	'IMTT2DContactPropertyRollerToSheet' : '{CC4BE154-2B21-4C7C-A67C-3F08942A20A0}',
	'IMTT2DContactPropertyRollerMovableToFixed' : '{B006CA26-0F57-4100-9224-D3D62429E8F6}',
	'IMTT2DContactPropertyPGuide' : '{B4F3A991-0483-415B-820F-A8B4116A3C9A}',
	'IMTT2DContactPropertyGuide' : '{B7C85E7D-D561-4C61-888E-29ACFFA48FF3}',
	'IMTT2DForceSpring' : '{5AB3349F-401D-4ED1-88E3-0A300C0C6B94}',
	'IMTT2DForceSpringNip' : '{4A4DE5B0-59EF-4CD2-B669-93768E326904}',
	'IMTT2DForceSpringTSD' : '{66947C3A-68E2-406E-9491-42952BD66A96}',
	'IMTT2DSheetBodyCollection' : '{767F4D3F-26B8-4F0A-B982-9A7FAC6CD1B2}',
	'IMTT2DSheetRevJointCollection' : '{AFC279E7-53CD-4DA1-96E2-3833740C410A}',
	'IMTT2DSheetRotSpringCollection' : '{F38F6090-E64E-4BA5-96B1-9865E77C4B31}',
	'IMTT2DSheet' : '{B6148C63-C63E-4B91-8051-EDCA38242816}',
	'IMTT2DGroupSheet' : '{59FE2E3A-2043-4651-8D6E-A58D8800205A}',
	'IMTT2DGroupFixedRoller' : '{0E7F0C51-106B-446A-93A5-1912034EA1A7}',
	'IMTT2DGroupMovableRoller' : '{D4F728AD-8867-4AA8-B319-88687F79C526}',
	'IMTT2DFlexibleRollerProperty' : '{4C5E08C2-A546-4EC0-BCED-5F725A2E6C6A}',
	'IMTT2DGroupFixedRollerShell' : '{91034068-E6A9-4616-9D41-9B666E4018AB}',
	'IMTT2DGroupMovableRollerShell' : '{2310F73F-2BE6-4338-93FF-609E572F4802}',
	'IMTT2DGroupGuideBody' : '{1AB7F0EE-74C9-4EF7-89BF-14AAF15EF35E}',
	'IMTT2DGuide' : '{333258BF-4C43-4C96-9079-6A4D54A4703C}',
	'IMTT2DGuideArc' : '{13439214-7EB0-439C-8C42-A2D55F1CC798}',
	'IMTT2DGuideLinear' : '{F4AE0FC8-97F2-4BA3-B061-799E91800B51}',
	'IMTT2DGuideCircular' : '{2AEBA258-C4AC-4EAA-ADF1-BAF8730E6E99}',
	'IMTT2DContactSheetToSheet' : '{AB78805A-064A-4015-812D-1332288F5789}',
	'IMTT2DForceNodal' : '{0F707193-3BDD-4899-8FD9-E9C21739ECCB}',
	'IMTT2DAssembly' : '{24C00315-36B5-498A-99A5-A3D3074E24DF}',
	'IMTT2DFixedRollerGroupCollection' : '{8393C52E-FB87-4F44-AA3B-CF6BE4045DEA}',
	'IMTT2DMovableRollerGroupCollection' : '{1F97796F-D817-4F6D-BDD4-057FAB6AB0C1}',
	'IMTT2DGroupSheetCollection' : '{6DAA417B-BEE4-49CE-AD91-195F1AA003EF}',
	'IMTT2DForceNodalCollection' : '{E3BB5B6C-23F0-4038-8466-36B8782CC65A}',
	'IMTT2DContactSheetToSheetCollection' : '{9538383C-C3C2-463F-B9D5-9017468026D1}',
	'IMTT2DGuideCollection' : '{18DD760B-C7E8-4BCF-BAE7-EC87A7D22B42}',
	'IMTT2DSubSystem' : '{4946A10D-6F44-45BC-B3F1-F1AA0CDA2C83}',
}


