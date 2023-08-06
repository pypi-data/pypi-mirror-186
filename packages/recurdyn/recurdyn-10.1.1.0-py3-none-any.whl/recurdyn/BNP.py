# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMBNP.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMBNP Type Library'
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

CLSID = IID('{D3A402B7-7D23-4F0C-A7AB-D7A034901627}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class BNPAssemblyInformationType(IntEnum):
	'''
	BNPAssemblyInformationType enumeration.
	'''
	Assembed_Radius               =0         
	'''Constant value is 0.'''
	Radial_Distance               =1         
	'''Constant value is 1.'''
class BNPBCOrienationType(IntEnum):
	'''
	BNPBCOrienationType enumeration.
	'''
	BNPBCOrienationType_Inertia   =1         
	'''Constant value is 1.'''
	BNPBCOrienationType_Node      =0         
	'''Constant value is 0.'''
class BNPBeltElementDampingForceType(IntEnum):
	'''
	BNPBeltElementDampingForceType enumeration.
	'''
	BNPBeltElementDampingForceType_10=0         
	'''Constant value is 0.'''
	BNPBeltElementDampingForceType_100=1         
	'''Constant value is 1.'''
class BNPBeltGroupModelType(IntEnum):
	'''
	BNPBeltGroupModelType enumeration.
	'''
	BNPBeltGroupModelType_BeamModel=0         
	'''Constant value is 0.'''
	BNPBeltGroupModelType_UserMatrix=1         
	'''Constant value is 1.'''
class BNPBeltMassType(IntEnum):
	'''
	BNPBeltMassType enumeration.
	'''
	BNPBeltMassType_Density       =0         
	'''Constant value is 0.'''
	BNPBeltMassType_TotalMass     =1         
	'''Constant value is 1.'''
class BNPBeltSpecialMaterialPropertyType(IntEnum):
	'''
	BNPBeltSpecialMaterialPropertyType enumeration.
	'''
	BNPBeltSpecialMaterialPropertyType_Anisotropic=2         
	'''Constant value is 2.'''
	BNPBeltSpecialMaterialPropertyType_Isotropic=0         
	'''Constant value is 0.'''
	BNPBeltSpecialMaterialPropertyType_Orthotropic=1         
	'''Constant value is 1.'''
class BNPBeltType(IntEnum):
	'''
	BNPBeltType enumeration.
	'''
	BNPBeltType_Flat              =0         
	'''Constant value is 0.'''
	BNPBeltType_Round             =2         
	'''Constant value is 2.'''
	BNPBeltType_Timing            =3         
	'''Constant value is 3.'''
	BNPBeltType_V                 =1         
	'''Constant value is 1.'''
class BNPContactDirectionType(IntEnum):
	'''
	BNPContactDirectionType enumeration.
	'''
	BNPContactDirectionType_Lower =1         
	'''Constant value is 1.'''
	BNPContactDirectionType_Upper =0         
	'''Constant value is 0.'''
class BNPContactSearchType(IntEnum):
	'''
	BNPContactSearchType enumeration.
	'''
	BNPContactSearchType_FullSearch=0         
	'''Constant value is 0.'''
	BNPContactSearchType_PartialSearch=1         
	'''Constant value is 1.'''
class BNPGuideNormalDirectionType(IntEnum):
	'''
	BNPGuideNormalDirectionType enumeration.
	'''
	BNPGuideNormalDirectionType_DOWN=1         
	'''Constant value is 1.'''
	BNPGuideNormalDirectionType_UP=0         
	'''Constant value is 0.'''
class BNPInOutType(IntEnum):
	'''
	BNPInOutType enumeration.
	'''
	BNPInOutType_In               =0         
	'''Constant value is 0.'''
	BNPInOutType_None             =2         
	'''Constant value is 2.'''
	BNPInOutType_Out              =1         
	'''Constant value is 1.'''
class BNPPulleyType(IntEnum):
	'''
	BNPPulleyType enumeration.
	'''
	BNPPulleyType_General         =1         
	'''Constant value is 1.'''
	BNPPulleyType_Parameters      =0         
	'''Constant value is 0.'''
class BNPToothProfileType(IntEnum):
	'''
	BNPToothProfileType enumeration.
	'''
	BNPToothProfileType_General   =0         
	'''Constant value is 0.'''
	BNPToothProfileType_Parameters=1         
	'''Constant value is 1.'''

from win32com.client import DispatchBaseClass
class IBNPAssembly(DispatchBaseClass):
	'''BNP Assembly'''
	CLSID = IID('{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddAllOutputBelt(self):
		'''
		Add all the belt body to output list
		'''
		return self._oleobj_.InvokeTypes(11013, LCID, 1, (24, 0), (),)


	def AddOutputBelt(self, strFileName):
		'''
		Add a belt body to output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11011, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def AddPassingBody(self, pVal):
		'''
		Add a passing body
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11003, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody(self, pVal):
		'''
		Delete a passing body
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11004, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetOutputBeltList(self):
		'''
		BNP assembly output list
		
		:rtype: list[str]
		'''
		return self._ApplyTypes_(11010, 1, (8200, 0), (), 'GetOutputBeltList', None,)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def RemoveAllOutputBelt(self):
		'''
		Remove all the belt body from output list
		'''
		return self._oleobj_.InvokeTypes(11014, LCID, 1, (24, 0), (),)


	def RemoveOutputBelt(self, strFileName):
		'''
		Remove a belt body from output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11012, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def UpdateBeltInitialVelocity(self):
		'''
		Update initial velocity of belts
		'''
		return self._oleobj_.InvokeTypes(11021, LCID, 1, (24, 0), (),)


	def _get_BNPBodyBeltCollection(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "BNPBodyBeltCollection", '{B49E6018-2162-41C9-9AC4-AF610E2E2356}'))
	def _get_BushingForceCollection(self):
		return self._ApplyTypes_(*(11020, 2, (9, 0), (), "BushingForceCollection", '{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ConnectingForceParameter(self):
		return self._ApplyTypes_(*(11009, 2, (9, 0), (), "ConnectingForceParameter", '{E789A6A6-79B6-49EE-B0C4-EC84A24499B1}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberOfSegment(self):
		return self._ApplyTypes_(*(11006, 2, (19, 0), (), "NumberOfSegment", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PassingBodyCollection(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'))
	def _get_UseInitialVelocity(self):
		return self._ApplyTypes_(*(11022, 2, (11, 0), (), "UseInitialVelocity", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialVelocity(self, value):
		if "UseInitialVelocity" in self.__dict__: self.__dict__["UseInitialVelocity"] = value; return
		self._oleobj_.Invoke(*((11022, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BNPBodyBeltCollection = property(_get_BNPBodyBeltCollection, None)
	'''
	Belt body collection

	:type: recurdyn.BNP.IBNPBodyBeltCollection
	'''
	BushingForceCollection = property(_get_BushingForceCollection, None)
	'''
	Bushing force collection

	:type: recurdyn.ProcessNet.IForceCollection
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ConnectingForceParameter = property(_get_ConnectingForceParameter, None)
	'''
	Connecting force parameter

	:type: recurdyn.BNP.IBNPAssemblyConnectingForceParameter
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	InitialLongitudinalVelocity = property(_get_InitialLongitudinalVelocity, None)
	'''
	Initial longitudinal velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NumberOfSegment = property(_get_NumberOfSegment, None)
	'''
	NUmber of segment

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
	PassingBodyCollection = property(_get_PassingBodyCollection, None)
	'''
	Passing body collection

	:type: recurdyn.ProcessNet.IBodyCollection
	'''
	UseInitialVelocity = property(_get_UseInitialVelocity, _set_UseInitialVelocity)
	'''
	Use initial velocity

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
		"_set_UseInitialVelocity": _set_UseInitialVelocity,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BNPBodyBeltCollection": (11008, 2, (9, 0), (), "BNPBodyBeltCollection", '{B49E6018-2162-41C9-9AC4-AF610E2E2356}'),
		"BushingForceCollection": (11020, 2, (9, 0), (), "BushingForceCollection", '{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConnectingForceParameter": (11009, 2, (9, 0), (), "ConnectingForceParameter", '{E789A6A6-79B6-49EE-B0C4-EC84A24499B1}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InitialLongitudinalVelocity": (11007, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberOfSegment": (11006, 2, (19, 0), (), "NumberOfSegment", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PassingBodyCollection": (11002, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'),
		"UseInitialVelocity": (11022, 2, (11, 0), (), "UseInitialVelocity", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseInitialVelocity": ((11022, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPAssembly2D(DispatchBaseClass):
	'''BNP 2D Assembly'''
	CLSID = IID('{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddAllOutputBelt(self):
		'''
		Add all the belt body to output list
		'''
		return self._oleobj_.InvokeTypes(11065, LCID, 1, (24, 0), (),)


	def AddOutputBelt(self, strFileName):
		'''
		Add a belt body to output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11063, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def AddPassingBody(self, pVal):
		'''
		Add a passing body
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11060, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody(self, pVal):
		'''
		Delete a passing body
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11061, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetOutputBeltList(self):
		'''
		BNP assembly output list
		
		:rtype: list[str]
		'''
		return self._ApplyTypes_(11062, 1, (8200, 0), (), 'GetOutputBeltList', None,)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def RemoveAllOutputBelt(self):
		'''
		Remove all the belt body from output list
		'''
		return self._oleobj_.InvokeTypes(11066, LCID, 1, (24, 0), (),)


	def RemoveOutputBelt(self, strFileName):
		'''
		Remove a belt body from output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11064, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def UpdateBeltInitialVelocity(self):
		'''
		Update initial velocity of belts
		'''
		return self._oleobj_.InvokeTypes(11067, LCID, 1, (24, 0), (),)


	def _get_BNPBodyBeltCollection(self):
		return self._ApplyTypes_(*(11054, 2, (9, 0), (), "BNPBodyBeltCollection", '{B49E6018-2162-41C9-9AC4-AF610E2E2356}'))
	def _get_BushingForceCollection(self):
		return self._ApplyTypes_(*(11056, 2, (9, 0), (), "BushingForceCollection", '{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}'))
	def _get_BusingForceParameter(self):
		return self._ApplyTypes_(*(11055, 2, (9, 0), (), "BusingForceParameter", '{4C336B22-AB0D-4922-B913-91F61EB5C6CB}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(11053, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NormalDirection(self):
		return self._ApplyTypes_(*(11051, 2, (8197, 0), (), "NormalDirection", None))
	def _get_NumberOfSegment(self):
		return self._ApplyTypes_(*(11052, 2, (19, 0), (), "NumberOfSegment", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PassingBodyCollection(self):
		return self._ApplyTypes_(*(11058, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'))
	def _get_UseInitialVelocity(self):
		return self._ApplyTypes_(*(11057, 2, (11, 0), (), "UseInitialVelocity", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NormalDirection(self, value):
		if "NormalDirection" in self.__dict__: self.__dict__["NormalDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((11051, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseInitialVelocity(self, value):
		if "UseInitialVelocity" in self.__dict__: self.__dict__["UseInitialVelocity"] = value; return
		self._oleobj_.Invoke(*((11057, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BNPBodyBeltCollection = property(_get_BNPBodyBeltCollection, None)
	'''
	Belt body collection

	:type: recurdyn.BNP.IBNPBodyBeltCollection
	'''
	BushingForceCollection = property(_get_BushingForceCollection, None)
	'''
	Bushing force collection

	:type: recurdyn.ProcessNet.IForceCollection
	'''
	BusingForceParameter = property(_get_BusingForceParameter, None)
	'''
	2D busing force parameter

	:type: recurdyn.BNP.IBNPAssembly2DBushingForceParameter
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
	InitialLongitudinalVelocity = property(_get_InitialLongitudinalVelocity, None)
	'''
	Initial longitudinal velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NormalDirection = property(_get_NormalDirection, _set_NormalDirection)
	'''
	Global Normal Direction

	:type: list[float]
	'''
	NumberOfSegment = property(_get_NumberOfSegment, None)
	'''
	NUmber of segment

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
	PassingBodyCollection = property(_get_PassingBodyCollection, None)
	'''
	Passing body collection

	:type: recurdyn.ProcessNet.IBodyCollection
	'''
	UseInitialVelocity = property(_get_UseInitialVelocity, _set_UseInitialVelocity)
	'''
	Use initial velocity

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
		"_set_NormalDirection": _set_NormalDirection,
		"_set_UseInitialVelocity": _set_UseInitialVelocity,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BNPBodyBeltCollection": (11054, 2, (9, 0), (), "BNPBodyBeltCollection", '{B49E6018-2162-41C9-9AC4-AF610E2E2356}'),
		"BushingForceCollection": (11056, 2, (9, 0), (), "BushingForceCollection", '{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}'),
		"BusingForceParameter": (11055, 2, (9, 0), (), "BusingForceParameter", '{4C336B22-AB0D-4922-B913-91F61EB5C6CB}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InitialLongitudinalVelocity": (11053, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NormalDirection": (11051, 2, (8197, 0), (), "NormalDirection", None),
		"NumberOfSegment": (11052, 2, (19, 0), (), "NumberOfSegment", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PassingBodyCollection": (11058, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'),
		"UseInitialVelocity": (11057, 2, (11, 0), (), "UseInitialVelocity", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NormalDirection": ((11051, LCID, 4, 0),()),
		"UseInitialVelocity": ((11057, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPAssembly2DBushingForceParameter(DispatchBaseClass):
	'''BNP assembly 2D bushing force parameter'''
	CLSID = IID('{4C336B22-AB0D-4922-B913-91F61EB5C6CB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_RotationalDampingZ(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "RotationalDampingZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_RotationalPreloadZ(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "RotationalPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationalStiffnessZ(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "RotationalStiffnessZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TranslationalDampingX(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "TranslationalDampingX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TranslationalDampingY(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "TranslationalDampingY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TranslationalPreloadX(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "TranslationalPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationalPreloadY(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "TranslationalPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationalStiffnessX(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "TranslationalStiffnessX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TranslationalStiffnessY(self):
		return self._ApplyTypes_(*(11001, 2, (9, 0), (), "TranslationalStiffnessY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))

	RotationalDampingZ = property(_get_RotationalDampingZ, None)
	'''
	Rotational damping Z

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	RotationalPreloadZ = property(_get_RotationalPreloadZ, None)
	'''
	Rotational preload Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationalStiffnessZ = property(_get_RotationalStiffnessZ, None)
	'''
	Rotational stiffness Z

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	TranslationalDampingX = property(_get_TranslationalDampingX, None)
	'''
	Translational damping X

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	TranslationalDampingY = property(_get_TranslationalDampingY, None)
	'''
	Translational damping Y

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	TranslationalPreloadX = property(_get_TranslationalPreloadX, None)
	'''
	Translational preload X

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationalPreloadY = property(_get_TranslationalPreloadY, None)
	'''
	Translational preload Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationalStiffnessX = property(_get_TranslationalStiffnessX, None)
	'''
	Translational stiffness X

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	TranslationalStiffnessY = property(_get_TranslationalStiffnessY, None)
	'''
	Translational stiffness Y

	:type: recurdyn.ProcessNet.ICoefficient
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"RotationalDampingZ": (11007, 2, (9, 0), (), "RotationalDampingZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"RotationalPreloadZ": (11008, 2, (9, 0), (), "RotationalPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationalStiffnessZ": (11006, 2, (9, 0), (), "RotationalStiffnessZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TranslationalDampingX": (11002, 2, (9, 0), (), "TranslationalDampingX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TranslationalDampingY": (11003, 2, (9, 0), (), "TranslationalDampingY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TranslationalPreloadX": (11004, 2, (9, 0), (), "TranslationalPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationalPreloadY": (11005, 2, (9, 0), (), "TranslationalPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationalStiffnessX": (11000, 2, (9, 0), (), "TranslationalStiffnessX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TranslationalStiffnessY": (11001, 2, (9, 0), (), "TranslationalStiffnessY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
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

class IBNPAssembly2DCollection(DispatchBaseClass):
	'''2D Belt assembly collection'''
	CLSID = IID('{D857EC59-8A2A-4228-99C9-07F5E95B84B0}')
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
		:rtype: recurdyn.BNP.IBNPAssembly2D
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}')
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
		:rtype: recurdyn.BNP.IBNPAssembly2D
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}')
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
		return win32com.client.util.Iterator(ob, '{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IBNPAssemblyCollection(DispatchBaseClass):
	'''Belt and pulley assembly collection'''
	CLSID = IID('{9CE8D58D-66F0-42F7-991B-2BDE5CB7E940}')
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
		:rtype: recurdyn.BNP.IBNPAssembly
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')
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
		:rtype: recurdyn.BNP.IBNPAssembly
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')
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
		return win32com.client.util.Iterator(ob, '{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IBNPAssemblyConnectingForceParameter(DispatchBaseClass):
	'''BNP assembly connecting force parameter'''
	CLSID = IID('{E789A6A6-79B6-49EE-B0C4-EC84A24499B1}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Preload(self, Index):
		'''
		Preload force and torque
		
		:param Index: int
		:rtype: recurdyn.ProcessNet.IDouble
		'''
		ret = self._oleobj_.InvokeTypes(11003, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'Preload', '{2B5166E3-4B31-4607-B157-BE237A670336}')
		return ret

	def ReferenceLength(self, Index):
		'''
		Six reference length
		
		:param Index: int
		:rtype: recurdyn.ProcessNet.IDouble
		'''
		ret = self._oleobj_.InvokeTypes(11004, LCID, 1, (9, 0), ((3, 1),),Index
			)
		if ret is not None:
			ret = Dispatch(ret, 'ReferenceLength', '{2B5166E3-4B31-4607-B157-BE237A670336}')
		return ret

	def StiffnessMatrix(self, i, j):
		'''
		Matrix of stiffness coefficients
		
		:param i: int
		:param j: int
		:rtype: recurdyn.ProcessNet.IDouble
		'''
		ret = self._oleobj_.InvokeTypes(11000, LCID, 1, (9, 0), ((3, 1), (3, 1)),i
			, j)
		if ret is not None:
			ret = Dispatch(ret, 'StiffnessMatrix', '{2B5166E3-4B31-4607-B157-BE237A670336}')
		return ret

	def ViscousDampingMatrix(self, i, j):
		'''
		Viscous damping matrix
		
		:param i: int
		:param j: int
		:rtype: recurdyn.ProcessNet.IDouble
		'''
		ret = self._oleobj_.InvokeTypes(11006, LCID, 1, (9, 0), ((3, 1), (3, 1)),i
			, j)
		if ret is not None:
			ret = Dispatch(ret, 'ViscousDampingMatrix', '{2B5166E3-4B31-4607-B157-BE237A670336}')
		return ret

	def _get_UseDampingMatrix(self):
		return self._ApplyTypes_(*(11002, 2, (11, 0), (), "UseDampingMatrix", None))
	def _get_ViscousDampingRatio(self):
		return self._ApplyTypes_(*(11001, 2, (9, 0), (), "ViscousDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_UseDampingMatrix(self, value):
		if "UseDampingMatrix" in self.__dict__: self.__dict__["UseDampingMatrix"] = value; return
		self._oleobj_.Invoke(*((11002, LCID, 4, 0) + (value,) + ()))

	UseDampingMatrix = property(_get_UseDampingMatrix, _set_UseDampingMatrix)
	'''
	Use viscous damping matrix

	:type: bool
	'''
	ViscousDampingRatio = property(_get_ViscousDampingRatio, None)
	'''
	Viscous damping coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_UseDampingMatrix": _set_UseDampingMatrix,
	}
	_prop_map_get_ = {
		"UseDampingMatrix": (11002, 2, (11, 0), (), "UseDampingMatrix", None),
		"ViscousDampingRatio": (11001, 2, (9, 0), (), "ViscousDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"UseDampingMatrix": ((11002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBeltBeamMaterialProperty(DispatchBaseClass):
	'''Beam belt material property'''
	CLSID = IID('{D9C23616-C0D3-422D-8A74-02654AB2E863}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def UpdateAreaProperties(self):
		'''
		Update Area Properties
		'''
		return self._oleobj_.InvokeTypes(11222, LCID, 1, (24, 0), (),)


	def _get_Asy(self):
		return self._ApplyTypes_(*(11211, 2, (9, 0), (), "Asy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Asz(self):
		return self._ApplyTypes_(*(11212, 2, (9, 0), (), "Asz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CY(self):
		return self._ApplyTypes_(*(11213, 2, (5, 0), (), "CY", None))
	def _get_CZ(self):
		return self._ApplyTypes_(*(11214, 2, (5, 0), (), "CZ", None))
	def _get_CrossSectionArea(self):
		return self._ApplyTypes_(*(11210, 2, (9, 0), (), "CrossSectionArea", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DY(self):
		return self._ApplyTypes_(*(11215, 2, (5, 0), (), "DY", None))
	def _get_DZ(self):
		return self._ApplyTypes_(*(11216, 2, (5, 0), (), "DZ", None))
	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(11203, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(11201, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_EY(self):
		return self._ApplyTypes_(*(11217, 2, (5, 0), (), "EY", None))
	def _get_EZ(self):
		return self._ApplyTypes_(*(11218, 2, (5, 0), (), "EZ", None))
	def _get_FY(self):
		return self._ApplyTypes_(*(11219, 2, (5, 0), (), "FY", None))
	def _get_FZ(self):
		return self._ApplyTypes_(*(11220, 2, (5, 0), (), "FZ", None))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(11207, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(11208, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(11209, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MassType(self):
		return self._ApplyTypes_(*(11200, 2, (3, 0), (), "MassType", '{723CDBB9-022E-4BE4-91BC-A182933DB430}'))
	def _get_PoissonsRatio(self):
		return self._ApplyTypes_(*(11206, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearModulus(self):
		return self._ApplyTypes_(*(11205, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(11202, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UpdateCrossSectionPropertyAutomaticallyFlag(self):
		return self._ApplyTypes_(*(11221, 2, (11, 0), (), "UpdateCrossSectionPropertyAutomaticallyFlag", None))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(11204, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_CY(self, value):
		if "CY" in self.__dict__: self.__dict__["CY"] = value; return
		self._oleobj_.Invoke(*((11213, LCID, 4, 0) + (value,) + ()))
	def _set_CZ(self, value):
		if "CZ" in self.__dict__: self.__dict__["CZ"] = value; return
		self._oleobj_.Invoke(*((11214, LCID, 4, 0) + (value,) + ()))
	def _set_DY(self, value):
		if "DY" in self.__dict__: self.__dict__["DY"] = value; return
		self._oleobj_.Invoke(*((11215, LCID, 4, 0) + (value,) + ()))
	def _set_DZ(self, value):
		if "DZ" in self.__dict__: self.__dict__["DZ"] = value; return
		self._oleobj_.Invoke(*((11216, LCID, 4, 0) + (value,) + ()))
	def _set_EY(self, value):
		if "EY" in self.__dict__: self.__dict__["EY"] = value; return
		self._oleobj_.Invoke(*((11217, LCID, 4, 0) + (value,) + ()))
	def _set_EZ(self, value):
		if "EZ" in self.__dict__: self.__dict__["EZ"] = value; return
		self._oleobj_.Invoke(*((11218, LCID, 4, 0) + (value,) + ()))
	def _set_FY(self, value):
		if "FY" in self.__dict__: self.__dict__["FY"] = value; return
		self._oleobj_.Invoke(*((11219, LCID, 4, 0) + (value,) + ()))
	def _set_FZ(self, value):
		if "FZ" in self.__dict__: self.__dict__["FZ"] = value; return
		self._oleobj_.Invoke(*((11220, LCID, 4, 0) + (value,) + ()))
	def _set_MassType(self, value):
		if "MassType" in self.__dict__: self.__dict__["MassType"] = value; return
		self._oleobj_.Invoke(*((11200, LCID, 4, 0) + (value,) + ()))
	def _set_UpdateCrossSectionPropertyAutomaticallyFlag(self, value):
		if "UpdateCrossSectionPropertyAutomaticallyFlag" in self.__dict__: self.__dict__["UpdateCrossSectionPropertyAutomaticallyFlag"] = value; return
		self._oleobj_.Invoke(*((11221, LCID, 4, 0) + (value,) + ()))

	Asy = property(_get_Asy, None)
	'''
	Asy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Asz = property(_get_Asz, None)
	'''
	Asz

	:type: recurdyn.ProcessNet.IDouble
	'''
	CY = property(_get_CY, _set_CY)
	'''
	Stress Recovery Points CY

	:type: float
	'''
	CZ = property(_get_CZ, _set_CZ)
	'''
	Stress Recovery Points CZ

	:type: float
	'''
	CrossSectionArea = property(_get_CrossSectionArea, None)
	'''
	Cross section area

	:type: recurdyn.ProcessNet.IDouble
	'''
	DY = property(_get_DY, _set_DY)
	'''
	Stress Recovery Points DY

	:type: float
	'''
	DZ = property(_get_DZ, _set_DZ)
	'''
	Stress Recovery Points DZ

	:type: float
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
	EY = property(_get_EY, _set_EY)
	'''
	Stress Recovery Points EY

	:type: float
	'''
	EZ = property(_get_EZ, _set_EZ)
	'''
	Stress Recovery Points EZ

	:type: float
	'''
	FY = property(_get_FY, _set_FY)
	'''
	Stress Recovery Points FY

	:type: float
	'''
	FZ = property(_get_FZ, _set_FZ)
	'''
	Stress Recovery Points FZ

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

	:type: recurdyn.BNP.BNPBeltMassType
	'''
	PoissonsRatio = property(_get_PoissonsRatio, None)
	'''
	Poisson's ratio

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearModulus = property(_get_ShearModulus, None)
	'''
	Shere Modulus

	:type: recurdyn.ProcessNet.IDouble
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
		"_set_CY": _set_CY,
		"_set_CZ": _set_CZ,
		"_set_DY": _set_DY,
		"_set_DZ": _set_DZ,
		"_set_EY": _set_EY,
		"_set_EZ": _set_EZ,
		"_set_FY": _set_FY,
		"_set_FZ": _set_FZ,
		"_set_MassType": _set_MassType,
		"_set_UpdateCrossSectionPropertyAutomaticallyFlag": _set_UpdateCrossSectionPropertyAutomaticallyFlag,
	}
	_prop_map_get_ = {
		"Asy": (11211, 2, (9, 0), (), "Asy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Asz": (11212, 2, (9, 0), (), "Asz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CY": (11213, 2, (5, 0), (), "CY", None),
		"CZ": (11214, 2, (5, 0), (), "CZ", None),
		"CrossSectionArea": (11210, 2, (9, 0), (), "CrossSectionArea", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DY": (11215, 2, (5, 0), (), "DY", None),
		"DZ": (11216, 2, (5, 0), (), "DZ", None),
		"DampingRatio": (11203, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (11201, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"EY": (11217, 2, (5, 0), (), "EY", None),
		"EZ": (11218, 2, (5, 0), (), "EZ", None),
		"FY": (11219, 2, (5, 0), (), "FY", None),
		"FZ": (11220, 2, (5, 0), (), "FZ", None),
		"Ixx": (11207, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (11208, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (11209, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MassType": (11200, 2, (3, 0), (), "MassType", '{723CDBB9-022E-4BE4-91BC-A182933DB430}'),
		"PoissonsRatio": (11206, 2, (9, 0), (), "PoissonsRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearModulus": (11205, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalMass": (11202, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UpdateCrossSectionPropertyAutomaticallyFlag": (11221, 2, (11, 0), (), "UpdateCrossSectionPropertyAutomaticallyFlag", None),
		"YoungsModulus": (11204, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"CY": ((11213, LCID, 4, 0),()),
		"CZ": ((11214, LCID, 4, 0),()),
		"DY": ((11215, LCID, 4, 0),()),
		"DZ": ((11216, LCID, 4, 0),()),
		"EY": ((11217, LCID, 4, 0),()),
		"EZ": ((11218, LCID, 4, 0),()),
		"FY": ((11219, LCID, 4, 0),()),
		"FZ": ((11220, LCID, 4, 0),()),
		"MassType": ((11200, LCID, 4, 0),()),
		"UpdateCrossSectionPropertyAutomaticallyFlag": ((11221, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBeltClone(DispatchBaseClass):
	'''Belt clone'''
	CLSID = IID('{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(11017, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(11016, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(11015, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11001, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(11018, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(11012, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((11018, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((11012, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((11011, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((11010, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((11013, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (11018, 2, (11, 0), (), "Active", None),
		"CenterMarker": (11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (11012, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((11018, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((11012, LCID, 4, 0),()),
		"Material": ((11011, LCID, 4, 0),()),
		"MaterialInput": ((11010, LCID, 4, 0),()),
		"MaterialUser": ((11013, LCID, 4, 0),()),
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

class IBNPBeltCloneCollection(DispatchBaseClass):
	'''BNP belt clone collection'''
	CLSID = IID('{7309E615-192D-406B-9F7A-AFF15939E207}')
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
		:rtype: recurdyn.BNP.IBNPBeltClone
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}')
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
		:rtype: recurdyn.BNP.IBNPBeltClone
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}')
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
		return win32com.client.util.Iterator(ob, '{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IBNPBeltCloneFlat(DispatchBaseClass):
	'''Flat belt clone'''
	CLSID = IID('{F60BB117-D220-4FD8-B603-74573A033D40}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(11017, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(11016, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(11015, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11001, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(11018, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactNode(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactNode", '{0711C396-7AF8-4A58-A98E-EDC99123FB42}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(11012, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "Geometry", '{9033BB6E-5115-49FA-83A2-E39301FBFD6C}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((11018, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((11012, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((11011, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((11010, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((11013, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactNode = property(_get_ContactNode, None)
	'''
	Contact node

	:type: recurdyn.BNP.IBNPContactNodePropertyBeltFlat
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryBeltFlat
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (11018, 2, (11, 0), (), "Active", None),
		"CenterMarker": (11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactNode": (11051, 2, (9, 0), (), "ContactNode", '{0711C396-7AF8-4A58-A98E-EDC99123FB42}'),
		"Density": (11012, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (11050, 2, (9, 0), (), "Geometry", '{9033BB6E-5115-49FA-83A2-E39301FBFD6C}'),
		"Graphic": (11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((11018, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((11012, LCID, 4, 0),()),
		"Material": ((11011, LCID, 4, 0),()),
		"MaterialInput": ((11010, LCID, 4, 0),()),
		"MaterialUser": ((11013, LCID, 4, 0),()),
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

class IBNPBeltCloneRibbedV(DispatchBaseClass):
	'''Ribbed belt clone'''
	CLSID = IID('{1DD37F48-A065-4B60-BA2D-5A2BFB10AB67}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(11017, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(11016, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(11015, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11001, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(11018, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactNode(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactNode", '{ABC5653E-52A2-4028-AE40-3738D348CF0D}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(11012, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "Geometry", '{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((11018, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((11012, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((11011, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((11010, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((11013, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactNode = property(_get_ContactNode, None)
	'''
	Contact node

	:type: recurdyn.BNP.IBNPContactNodePropertyBeltRibbedV
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryBeltRibbedV
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (11018, 2, (11, 0), (), "Active", None),
		"CenterMarker": (11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactNode": (11051, 2, (9, 0), (), "ContactNode", '{ABC5653E-52A2-4028-AE40-3738D348CF0D}'),
		"Density": (11012, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (11050, 2, (9, 0), (), "Geometry", '{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}'),
		"Graphic": (11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((11018, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((11012, LCID, 4, 0),()),
		"Material": ((11011, LCID, 4, 0),()),
		"MaterialInput": ((11010, LCID, 4, 0),()),
		"MaterialUser": ((11013, LCID, 4, 0),()),
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

class IBNPBeltCloneTiming(DispatchBaseClass):
	'''timing belt clone'''
	CLSID = IID('{7D32C453-E2E6-413F-8F69-C66F17CE38C6}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(11017, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(11016, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(11015, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11001, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(11018, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(11012, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "Geometry", '{28B9F577-7066-4B2E-80A2-AF7D140593AC}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((11018, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((11012, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((11011, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((11010, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((11013, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryBeltTiming
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (11018, 2, (11, 0), (), "Active", None),
		"CenterMarker": (11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (11012, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (11050, 2, (9, 0), (), "Geometry", '{28B9F577-7066-4B2E-80A2-AF7D140593AC}'),
		"Graphic": (11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((11018, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((11012, LCID, 4, 0),()),
		"Material": ((11011, LCID, 4, 0),()),
		"MaterialInput": ((11010, LCID, 4, 0),()),
		"MaterialUser": ((11013, LCID, 4, 0),()),
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

class IBNPBeltCloneV(DispatchBaseClass):
	'''V belt clone'''
	CLSID = IID('{8FC53768-BC25-4B05-BE34-6E537955559C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(11017, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(11016, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(11015, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11001, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(11018, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactNode(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactNode", '{7AE525B3-FE13-4117-809E-476C72E2847C}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(11012, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "Geometry", '{185F6935-19D9-4664-91A4-C564A61DF014}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((11018, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((11012, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((11011, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((11010, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((11013, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactNode = property(_get_ContactNode, None)
	'''
	Contact node

	:type: recurdyn.BNP.IBNPContactNodePropertyBeltV
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryBeltV
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (11018, 2, (11, 0), (), "Active", None),
		"CenterMarker": (11014, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactNode": (11051, 2, (9, 0), (), "ContactNode", '{7AE525B3-FE13-4117-809E-476C72E2847C}'),
		"Density": (11012, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (11050, 2, (9, 0), (), "Geometry", '{185F6935-19D9-4664-91A4-C564A61DF014}'),
		"Graphic": (11002, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (11004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (11007, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (11005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (11008, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (11009, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (11006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (11003, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (11011, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (11010, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (11013, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((11018, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((11012, LCID, 4, 0),()),
		"Material": ((11011, LCID, 4, 0),()),
		"MaterialInput": ((11010, LCID, 4, 0),()),
		"MaterialUser": ((11013, LCID, 4, 0),()),
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

class IBNPBeltGroup(DispatchBaseClass):
	'''BNP belt group'''
	CLSID = IID('{80511C7B-B89C-4FA4-B21C-A9A7182B0E61}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddAllOutputBelt(self):
		'''
		Add all the belt body to output list
		'''
		return self._oleobj_.InvokeTypes(11024, LCID, 1, (24, 0), (),)


	def AddOutputBelt(self, strFileName):
		'''
		Add a belt body to output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11022, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def AddPassingBody(self, pVal):
		'''
		Add a passing body
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11016, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody(self, pVal):
		'''
		Delete a passing body
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11017, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetOutputBeltList(self):
		'''
		Belt group output list
		
		:rtype: list[str]
		'''
		return self._ApplyTypes_(11021, 1, (8200, 0), (), 'GetOutputBeltList', None,)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def RemoveAllOutputBelt(self):
		'''
		Remove all the belt body from output list
		'''
		return self._oleobj_.InvokeTypes(11025, LCID, 1, (24, 0), (),)


	def RemoveOutputBelt(self, strFileName):
		'''
		Remove a belt body from output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(11023, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


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
	def _get_BeltType(self):
		return self._ApplyTypes_(*(11003, 2, (3, 0), (), "BeltType", '{0BB88860-1CA3-4F91-973F-ACA0600D489B}'))
	def _get_Color(self):
		return self._ApplyTypes_(*(11000, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactPoint(self):
		return self._ApplyTypes_(*(11012, 2, (9, 0), (), "ContactPoint", '{C687377E-15AA-4340-A9F5-DB9CB8F4C9DA}'))
	def _get_DisplayNode(self):
		return self._ApplyTypes_(*(11001, 2, (11, 0), (), "DisplayNode", None))
	def _get_DisplayNodeID(self):
		return self._ApplyTypes_(*(11002, 2, (11, 0), (), "DisplayNodeID", None))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_ElementLength(self):
		return self._ApplyTypes_(*(11008, 2, (5, 0), (), "ElementLength", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(11019, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_LowerThickness(self):
		return self._ApplyTypes_(*(11004, 2, (9, 0), (), "LowerThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaterialProperty(self):
		return self._ApplyTypes_(*(11011, 2, (9, 0), (), "MaterialProperty", '{4FD6E858-87DC-4106-858F-F8CF4C6E60D5}'))
	def _get_ModelType(self):
		return self._ApplyTypes_(*(11009, 2, (3, 0), (), "ModelType", '{90F9A508-6441-4D9C-9ECC-CE148ACE6008}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberOfElements(self):
		return self._ApplyTypes_(*(11007, 2, (19, 0), (), "NumberOfElements", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PassingBodyCollection(self):
		return self._ApplyTypes_(*(11015, 2, (9, 0), (), "PassingBodyCollection", '{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}'))
	def _get_StretchedLength(self):
		return self._ApplyTypes_(*(11010, 2, (9, 0), (), "StretchedLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UpperThickness(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "UpperThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseInitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(11018, 2, (11, 0), (), "UseInitialLongitudinalVelocity", None))
	def _get_UseUpdateGeometryInformationAutomatically(self):
		return self._ApplyTypes_(*(11020, 2, (11, 0), (), "UseUpdateGeometryInformationAutomatically", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BeltType(self, value):
		if "BeltType" in self.__dict__: self.__dict__["BeltType"] = value; return
		self._oleobj_.Invoke(*((11003, LCID, 4, 0) + (value,) + ()))
	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((11000, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_DisplayNode(self, value):
		if "DisplayNode" in self.__dict__: self.__dict__["DisplayNode"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))
	def _set_DisplayNodeID(self, value):
		if "DisplayNodeID" in self.__dict__: self.__dict__["DisplayNodeID"] = value; return
		self._oleobj_.Invoke(*((11002, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_ModelType(self, value):
		if "ModelType" in self.__dict__: self.__dict__["ModelType"] = value; return
		self._oleobj_.Invoke(*((11009, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialLongitudinalVelocity(self, value):
		if "UseInitialLongitudinalVelocity" in self.__dict__: self.__dict__["UseInitialLongitudinalVelocity"] = value; return
		self._oleobj_.Invoke(*((11018, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdateGeometryInformationAutomatically(self, value):
		if "UseUpdateGeometryInformationAutomatically" in self.__dict__: self.__dict__["UseUpdateGeometryInformationAutomatically"] = value; return
		self._oleobj_.Invoke(*((11020, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BeltType = property(_get_BeltType, _set_BeltType)
	'''
	Belt type

	:type: recurdyn.BNP.BNPBeltType
	'''
	Color = property(_get_Color, _set_Color)
	'''
	Belt color

	:type: int
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactPoint = property(_get_ContactPoint, None)
	'''
	Contact node

	:type: recurdyn.BNP.IBNPBeltGroupContactPoint
	'''
	DisplayNode = property(_get_DisplayNode, _set_DisplayNode)
	'''
	Display node

	:type: bool
	'''
	DisplayNodeID = property(_get_DisplayNodeID, _set_DisplayNodeID)
	'''
	Display node ID

	:type: bool
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	ElementLength = property(_get_ElementLength, None)
	'''
	Element length

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
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
	LowerThickness = property(_get_LowerThickness, None)
	'''
	Lower thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaterialProperty = property(_get_MaterialProperty, None)
	'''
	Material property

	:type: recurdyn.BNP.IBNPBeltGroupMaterialProperty
	'''
	ModelType = property(_get_ModelType, _set_ModelType)
	'''
	Model type

	:type: recurdyn.BNP.BNPBeltGroupModelType
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NumberOfElements = property(_get_NumberOfElements, None)
	'''
	Number of elements

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
	PassingBodyCollection = property(_get_PassingBodyCollection, None)
	'''
	Passing body collection

	:type: recurdyn.BNP.IBNPPassingBodyCollection
	'''
	StretchedLength = property(_get_StretchedLength, None)
	'''
	Stretched length

	:type: recurdyn.ProcessNet.IDouble
	'''
	UpperThickness = property(_get_UpperThickness, None)
	'''
	Upper thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseInitialLongitudinalVelocity = property(_get_UseInitialLongitudinalVelocity, _set_UseInitialLongitudinalVelocity)
	'''
	Use initial longitudinal velocity

	:type: bool
	'''
	UseUpdateGeometryInformationAutomatically = property(_get_UseUpdateGeometryInformationAutomatically, _set_UseUpdateGeometryInformationAutomatically)
	'''
	Update geometry information automatically

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	Width = property(_get_Width, None)
	'''
	Width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_BeltType": _set_BeltType,
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_DisplayNode": _set_DisplayNode,
		"_set_DisplayNodeID": _set_DisplayNodeID,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_ModelType": _set_ModelType,
		"_set_Name": _set_Name,
		"_set_UseInitialLongitudinalVelocity": _set_UseInitialLongitudinalVelocity,
		"_set_UseUpdateGeometryInformationAutomatically": _set_UseUpdateGeometryInformationAutomatically,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BeltType": (11003, 2, (3, 0), (), "BeltType", '{0BB88860-1CA3-4F91-973F-ACA0600D489B}'),
		"Color": (11000, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactPoint": (11012, 2, (9, 0), (), "ContactPoint", '{C687377E-15AA-4340-A9F5-DB9CB8F4C9DA}'),
		"DisplayNode": (11001, 2, (11, 0), (), "DisplayNode", None),
		"DisplayNodeID": (11002, 2, (11, 0), (), "DisplayNodeID", None),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"ElementLength": (11008, 2, (5, 0), (), "ElementLength", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InitialLongitudinalVelocity": (11019, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"LowerThickness": (11004, 2, (9, 0), (), "LowerThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaterialProperty": (11011, 2, (9, 0), (), "MaterialProperty", '{4FD6E858-87DC-4106-858F-F8CF4C6E60D5}'),
		"ModelType": (11009, 2, (3, 0), (), "ModelType", '{90F9A508-6441-4D9C-9ECC-CE148ACE6008}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberOfElements": (11007, 2, (19, 0), (), "NumberOfElements", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PassingBodyCollection": (11015, 2, (9, 0), (), "PassingBodyCollection", '{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}'),
		"StretchedLength": (11010, 2, (9, 0), (), "StretchedLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UpperThickness": (11005, 2, (9, 0), (), "UpperThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseInitialLongitudinalVelocity": (11018, 2, (11, 0), (), "UseInitialLongitudinalVelocity", None),
		"UseUpdateGeometryInformationAutomatically": (11020, 2, (11, 0), (), "UseUpdateGeometryInformationAutomatically", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Width": (11006, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BeltType": ((11003, LCID, 4, 0),()),
		"Color": ((11000, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"DisplayNode": ((11001, LCID, 4, 0),()),
		"DisplayNodeID": ((11002, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"ModelType": ((11009, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseInitialLongitudinalVelocity": ((11018, LCID, 4, 0),()),
		"UseUpdateGeometryInformationAutomatically": ((11020, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBeltGroupContactPoint(DispatchBaseClass):
	'''Belt group contact node property'''
	CLSID = IID('{C687377E-15AA-4340-A9F5-DB9CB8F4C9DA}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ContactNodeBottom(self):
		return self._ApplyTypes_(*(11050, 2, (19, 0), (), "ContactNodeBottom", None))
	def _get_ContactNodeSide(self):
		return self._ApplyTypes_(*(11051, 2, (19, 0), (), "ContactNodeSide", None))
	def _get_ContactNodeTop(self):
		return self._ApplyTypes_(*(11052, 2, (19, 0), (), "ContactNodeTop", None))

	def _set_ContactNodeBottom(self, value):
		if "ContactNodeBottom" in self.__dict__: self.__dict__["ContactNodeBottom"] = value; return
		self._oleobj_.Invoke(*((11050, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeSide(self, value):
		if "ContactNodeSide" in self.__dict__: self.__dict__["ContactNodeSide"] = value; return
		self._oleobj_.Invoke(*((11051, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeTop(self, value):
		if "ContactNodeTop" in self.__dict__: self.__dict__["ContactNodeTop"] = value; return
		self._oleobj_.Invoke(*((11052, LCID, 4, 0) + (value,) + ()))

	ContactNodeBottom = property(_get_ContactNodeBottom, _set_ContactNodeBottom)
	'''
	Belt group bottom contact node

	:type: int
	'''
	ContactNodeSide = property(_get_ContactNodeSide, _set_ContactNodeSide)
	'''
	Belt group side contact node

	:type: int
	'''
	ContactNodeTop = property(_get_ContactNodeTop, _set_ContactNodeTop)
	'''
	Belt group top contact node

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_ContactNodeBottom": _set_ContactNodeBottom,
		"_set_ContactNodeSide": _set_ContactNodeSide,
		"_set_ContactNodeTop": _set_ContactNodeTop,
	}
	_prop_map_get_ = {
		"ContactNodeBottom": (11050, 2, (19, 0), (), "ContactNodeBottom", None),
		"ContactNodeSide": (11051, 2, (19, 0), (), "ContactNodeSide", None),
		"ContactNodeTop": (11052, 2, (19, 0), (), "ContactNodeTop", None),
	}
	_prop_map_put_ = {
		"ContactNodeBottom": ((11050, LCID, 4, 0),()),
		"ContactNodeSide": ((11051, LCID, 4, 0),()),
		"ContactNodeTop": ((11052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBeltGroupMaterialProperty(DispatchBaseClass):
	'''Belt Group material property'''
	CLSID = IID('{4FD6E858-87DC-4106-858F-F8CF4C6E60D5}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_CrossSectionArea(self):
		return self._ApplyTypes_(*(11059, 2, (9, 0), (), "CrossSectionArea", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingRatio(self):
		return self._ApplyTypes_(*(11053, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(11056, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(11057, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(11058, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MassType(self):
		return self._ApplyTypes_(*(11050, 2, (3, 0), (), "MassType", '{723CDBB9-022E-4BE4-91BC-A182933DB430}'))
	def _get_ShearModulus(self):
		return self._ApplyTypes_(*(11055, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(11054, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_MassType(self, value):
		if "MassType" in self.__dict__: self.__dict__["MassType"] = value; return
		self._oleobj_.Invoke(*((11050, LCID, 4, 0) + (value,) + ()))

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
	Material property type

	:type: recurdyn.BNP.BNPBeltMassType
	'''
	ShearModulus = property(_get_ShearModulus, None)
	'''
	Shere Modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalMass = property(_get_TotalMass, None)
	'''
	Totoal mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	Young's Modulus

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_MassType": _set_MassType,
	}
	_prop_map_get_ = {
		"CrossSectionArea": (11059, 2, (9, 0), (), "CrossSectionArea", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingRatio": (11053, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (11051, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixx": (11056, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (11057, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (11058, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MassType": (11050, 2, (3, 0), (), "MassType", '{723CDBB9-022E-4BE4-91BC-A182933DB430}'),
		"ShearModulus": (11055, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalMass": (11052, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YoungsModulus": (11054, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"MassType": ((11050, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBeltShellMaterialProperty(DispatchBaseClass):
	'''Shell belt material property'''
	CLSID = IID('{9BC7A528-18AE-43FF-B8FF-81EBDAF0F812}')
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
		return self._ApplyTypes_(*(11204, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(11202, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DrillingStiffnessFactor(self):
		return self._ApplyTypes_(*(11211, 2, (9, 0), (), "DrillingStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ElementDampingForceType(self):
		return self._ApplyTypes_(*(11212, 2, (3, 0), (), "ElementDampingForceType", '{9757FC8B-6458-44FB-A16E-850F76CE5608}'))
	def _get_G11(self):
		return self._ApplyTypes_(*(11216, 2, (9, 0), (), "G11", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G12(self):
		return self._ApplyTypes_(*(11217, 2, (9, 0), (), "G12", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G13(self):
		return self._ApplyTypes_(*(11218, 2, (9, 0), (), "G13", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G22(self):
		return self._ApplyTypes_(*(11219, 2, (9, 0), (), "G22", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G23(self):
		return self._ApplyTypes_(*(11220, 2, (9, 0), (), "G23", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_G33(self):
		return self._ApplyTypes_(*(11221, 2, (9, 0), (), "G33", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MassType(self):
		return self._ApplyTypes_(*(11201, 2, (3, 0), (), "MassType", '{723CDBB9-022E-4BE4-91BC-A182933DB430}'))
	def _get_MaterialPropertyType(self):
		return self._ApplyTypes_(*(11200, 2, (3, 0), (), "MaterialPropertyType", '{CEA0FB7A-8C16-4D2F-B859-C3A84BC76392}'))
	def _get_PoissonsModulus(self):
		return self._ApplyTypes_(*(11206, 2, (9, 0), (), "PoissonsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PoissonsRatio1(self):
		return self._ApplyTypes_(*(11210, 2, (9, 0), (), "PoissonsRatio1", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearModulus(self):
		return self._ApplyTypes_(*(11209, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(11203, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TransverseShearModulus1(self):
		return self._ApplyTypes_(*(11214, 2, (9, 0), (), "TransverseShearModulus1", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TransverseShearModulus2(self):
		return self._ApplyTypes_(*(11215, 2, (9, 0), (), "TransverseShearModulus2", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseUserDefinedTransverseShearModulus(self):
		return self._ApplyTypes_(*(11213, 2, (11, 0), (), "UseUserDefinedTransverseShearModulus", None))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(11205, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YoungsModulus1(self):
		return self._ApplyTypes_(*(11207, 2, (9, 0), (), "YoungsModulus1", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YoungsModulus2(self):
		return self._ApplyTypes_(*(11208, 2, (9, 0), (), "YoungsModulus2", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_ElementDampingForceType(self, value):
		if "ElementDampingForceType" in self.__dict__: self.__dict__["ElementDampingForceType"] = value; return
		self._oleobj_.Invoke(*((11212, LCID, 4, 0) + (value,) + ()))
	def _set_MassType(self, value):
		if "MassType" in self.__dict__: self.__dict__["MassType"] = value; return
		self._oleobj_.Invoke(*((11201, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialPropertyType(self, value):
		if "MaterialPropertyType" in self.__dict__: self.__dict__["MaterialPropertyType"] = value; return
		self._oleobj_.Invoke(*((11200, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserDefinedTransverseShearModulus(self, value):
		if "UseUserDefinedTransverseShearModulus" in self.__dict__: self.__dict__["UseUserDefinedTransverseShearModulus"] = value; return
		self._oleobj_.Invoke(*((11213, LCID, 4, 0) + (value,) + ()))

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
	DrillingStiffnessFactor = property(_get_DrillingStiffnessFactor, None)
	'''
	Drilling Stiffness Factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	ElementDampingForceType = property(_get_ElementDampingForceType, _set_ElementDampingForceType)
	'''
	Element damping force type : obsolete function

	:type: recurdyn.BNP.BNPBeltElementDampingForceType
	'''
	G11 = property(_get_G11, None)
	'''
	The G11 of the shell

	:type: recurdyn.ProcessNet.IDouble
	'''
	G12 = property(_get_G12, None)
	'''
	The G12 of the shell

	:type: recurdyn.ProcessNet.IDouble
	'''
	G13 = property(_get_G13, None)
	'''
	The G13 of the shell

	:type: recurdyn.ProcessNet.IDouble
	'''
	G22 = property(_get_G22, None)
	'''
	The G22 of the shell

	:type: recurdyn.ProcessNet.IDouble
	'''
	G23 = property(_get_G23, None)
	'''
	The G23 of the shell

	:type: recurdyn.ProcessNet.IDouble
	'''
	G33 = property(_get_G33, None)
	'''
	The G33 of the shell

	:type: recurdyn.ProcessNet.IDouble
	'''
	MassType = property(_get_MassType, _set_MassType)
	'''
	Mass type

	:type: recurdyn.BNP.BNPBeltMassType
	'''
	MaterialPropertyType = property(_get_MaterialPropertyType, _set_MaterialPropertyType)
	'''
	Material property type

	:type: recurdyn.BNP.BNPBeltSpecialMaterialPropertyType
	'''
	PoissonsModulus = property(_get_PoissonsModulus, None)
	'''
	Poisson's Modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	PoissonsRatio1 = property(_get_PoissonsRatio1, None)
	'''
	Poisson's Ratio1

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearModulus = property(_get_ShearModulus, None)
	'''
	Shear Modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalMass = property(_get_TotalMass, None)
	'''
	Totoal mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	TransverseShearModulus1 = property(_get_TransverseShearModulus1, None)
	'''
	The shear modulus of XY direction of the shell

	:type: recurdyn.ProcessNet.IDouble
	'''
	TransverseShearModulus2 = property(_get_TransverseShearModulus2, None)
	'''
	The shear modulus of YZ direction of the shell

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseUserDefinedTransverseShearModulus = property(_get_UseUserDefinedTransverseShearModulus, _set_UseUserDefinedTransverseShearModulus)
	'''
	Use user-defined transverse shear modulus

	:type: bool
	'''
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	Young's Modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	YoungsModulus1 = property(_get_YoungsModulus1, None)
	'''
	Young's Modulus1

	:type: recurdyn.ProcessNet.IDouble
	'''
	YoungsModulus2 = property(_get_YoungsModulus2, None)
	'''
	Young's Modulus2

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_ElementDampingForceType": _set_ElementDampingForceType,
		"_set_MassType": _set_MassType,
		"_set_MaterialPropertyType": _set_MaterialPropertyType,
		"_set_UseUserDefinedTransverseShearModulus": _set_UseUserDefinedTransverseShearModulus,
	}
	_prop_map_get_ = {
		"DampingRatio": (11204, 2, (9, 0), (), "DampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (11202, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DrillingStiffnessFactor": (11211, 2, (9, 0), (), "DrillingStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ElementDampingForceType": (11212, 2, (3, 0), (), "ElementDampingForceType", '{9757FC8B-6458-44FB-A16E-850F76CE5608}'),
		"G11": (11216, 2, (9, 0), (), "G11", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G12": (11217, 2, (9, 0), (), "G12", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G13": (11218, 2, (9, 0), (), "G13", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G22": (11219, 2, (9, 0), (), "G22", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G23": (11220, 2, (9, 0), (), "G23", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"G33": (11221, 2, (9, 0), (), "G33", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MassType": (11201, 2, (3, 0), (), "MassType", '{723CDBB9-022E-4BE4-91BC-A182933DB430}'),
		"MaterialPropertyType": (11200, 2, (3, 0), (), "MaterialPropertyType", '{CEA0FB7A-8C16-4D2F-B859-C3A84BC76392}'),
		"PoissonsModulus": (11206, 2, (9, 0), (), "PoissonsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PoissonsRatio1": (11210, 2, (9, 0), (), "PoissonsRatio1", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearModulus": (11209, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalMass": (11203, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TransverseShearModulus1": (11214, 2, (9, 0), (), "TransverseShearModulus1", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TransverseShearModulus2": (11215, 2, (9, 0), (), "TransverseShearModulus2", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseUserDefinedTransverseShearModulus": (11213, 2, (11, 0), (), "UseUserDefinedTransverseShearModulus", None),
		"YoungsModulus": (11205, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YoungsModulus1": (11207, 2, (9, 0), (), "YoungsModulus1", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YoungsModulus2": (11208, 2, (9, 0), (), "YoungsModulus2", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"ElementDampingForceType": ((11212, LCID, 4, 0),()),
		"MassType": ((11201, LCID, 4, 0),()),
		"MaterialPropertyType": ((11200, LCID, 4, 0),()),
		"UseUserDefinedTransverseShearModulus": ((11213, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBody(DispatchBaseClass):
	'''Belt body'''
	CLSID = IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')
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
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
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

class IBNPBody2DGuide(DispatchBaseClass):
	'''2D Guide body'''
	CLSID = IID('{3285D284-E32D-4EA9-B44D-1490297A25BF}')
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
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
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
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
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

class IBNPBody2DGuideArc(DispatchBaseClass):
	'''2D Arc Guide body'''
	CLSID = IID('{3CD85FDD-669E-47E0-A0BC-165B3BACBAC5}')
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
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11100, 2, (9, 0), (), "Geometry", '{28DFE5F6-D718-4CD5-AA3B-4CC4538DEB62}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NormalDirection(self):
		return self._ApplyTypes_(*(11101, 2, (3, 0), (), "NormalDirection", '{CFBA2C41-79A2-4AD3-913D-41E55C6DF27F}'))
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
	def _set_NormalDirection(self, value):
		if "NormalDirection" in self.__dict__: self.__dict__["NormalDirection"] = value; return
		self._oleobj_.Invoke(*((11101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
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

	:type: recurdyn.BNP.IBNPGeometry2DGuideArc
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NormalDirection = property(_get_NormalDirection, _set_NormalDirection)
	'''
	Obsolete Function

	:type: recurdyn.BNP.BNPGuideNormalDirectionType
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
		"_set_NormalDirection": _set_NormalDirection,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11100, 2, (9, 0), (), "Geometry", '{28DFE5F6-D718-4CD5-AA3B-4CC4538DEB62}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NormalDirection": (11101, 2, (3, 0), (), "NormalDirection", '{CFBA2C41-79A2-4AD3-913D-41E55C6DF27F}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NormalDirection": ((11101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBody2DGuideLinear(DispatchBaseClass):
	'''2D Linear Guide body'''
	CLSID = IID('{6496CE67-5383-4DDF-9FA1-CC2614D1B96C}')
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
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11100, 2, (9, 0), (), "Geometry", '{6E62C6CA-9D43-4D53-A2B1-4BEFD6DE5D22}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NormalDirection(self):
		return self._ApplyTypes_(*(11101, 2, (3, 0), (), "NormalDirection", '{CFBA2C41-79A2-4AD3-913D-41E55C6DF27F}'))
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
	def _set_NormalDirection(self, value):
		if "NormalDirection" in self.__dict__: self.__dict__["NormalDirection"] = value; return
		self._oleobj_.Invoke(*((11101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
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

	:type: recurdyn.BNP.IBNPGeometry2DGuideLinear
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NormalDirection = property(_get_NormalDirection, _set_NormalDirection)
	'''
	Normal Direction

	:type: recurdyn.BNP.BNPGuideNormalDirectionType
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
		"_set_NormalDirection": _set_NormalDirection,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11100, 2, (9, 0), (), "Geometry", '{6E62C6CA-9D43-4D53-A2B1-4BEFD6DE5D22}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NormalDirection": (11101, 2, (3, 0), (), "NormalDirection", '{CFBA2C41-79A2-4AD3-913D-41E55C6DF27F}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NormalDirection": ((11101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBodyBelt(DispatchBaseClass):
	'''Belt body'''
	CLSID = IID('{8ED56403-6EF8-4451-9CA4-7DBE298F4FE5}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateMarker(self, strName, pRefFrame):
		'''
		Creates a marker
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ProcessNet.IMarker
		'''
		ret = self._oleobj_.InvokeTypes(11054, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMarker', '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11051, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(11052, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((11052, LCID, 4, 0) + (value,) + ()))
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
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

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
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Graphic": (11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (11052, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((11052, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBodyBeltBeam(DispatchBaseClass):
	'''Beam belt body'''
	CLSID = IID('{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}')
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
		return self._oleobj_.InvokeTypes(11106, LCID, 1, (24, 0), (),)


	def _get_BCCollection(self):
		return self._ApplyTypes_(*(11102, 2, (9, 0), (), "BCCollection", '{7F035946-EE7C-4557-BAFC-000BDD366EDF}'))
	def _get_BCOrienation(self):
		return self._ApplyTypes_(*(11104, 2, (3, 0), (), "BCOrienation", '{14B4CA05-EA66-4C59-BED0-04E27062CE88}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ConnectingParameters(self):
		return self._ApplyTypes_(*(11100, 2, (9, 0), (), "ConnectingParameters", '{A111AE4E-7116-496C-BA07-1B125F33ECEA}'))
	def _get_FlexBody(self):
		return self._ApplyTypes_(*(11105, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "Geometry", '{64E4D842-5C51-484B-B3F8-C54D097BBDA1}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_OutputCollection(self):
		return self._ApplyTypes_(*(11103, 2, (9, 0), (), "OutputCollection", '{4549131A-72B6-45B1-9ABE-C2A32F250FED}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_BCOrienation(self, value):
		if "BCOrienation" in self.__dict__: self.__dict__["BCOrienation"] = value; return
		self._oleobj_.Invoke(*((11104, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BCCollection = property(_get_BCCollection, None)
	'''
	Node boundary condition collection

	:type: recurdyn.ProcessNet.INodeBCCollection
	'''
	BCOrienation = property(_get_BCOrienation, _set_BCOrienation)
	'''
	BC Orienation

	:type: recurdyn.BNP.BNPBCOrienationType
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ConnectingParameters = property(_get_ConnectingParameters, None)
	'''
	Connecting parameters

	:type: recurdyn.BNP.IBNPConnectingParameters
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

	:type: recurdyn.BNP.IBNPGeometryBeltBeam
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
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_BCOrienation": _set_BCOrienation,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BCCollection": (11102, 2, (9, 0), (), "BCCollection", '{7F035946-EE7C-4557-BAFC-000BDD366EDF}'),
		"BCOrienation": (11104, 2, (3, 0), (), "BCOrienation", '{14B4CA05-EA66-4C59-BED0-04E27062CE88}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConnectingParameters": (11100, 2, (9, 0), (), "ConnectingParameters", '{A111AE4E-7116-496C-BA07-1B125F33ECEA}'),
		"FlexBody": (11105, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (11101, 2, (9, 0), (), "Geometry", '{64E4D842-5C51-484B-B3F8-C54D097BBDA1}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"OutputCollection": (11103, 2, (9, 0), (), "OutputCollection", '{4549131A-72B6-45B1-9ABE-C2A32F250FED}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"BCOrienation": ((11104, LCID, 4, 0),()),
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

class IBNPBodyBeltCollection(DispatchBaseClass):
	'''BNP Body belt Collection'''
	CLSID = IID('{B49E6018-2162-41C9-9AC4-AF610E2E2356}')
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
		:rtype: recurdyn.BNP.IBNPBodyBelt
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{8ED56403-6EF8-4451-9CA4-7DBE298F4FE5}')
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
		:rtype: recurdyn.BNP.IBNPBodyBelt
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{8ED56403-6EF8-4451-9CA4-7DBE298F4FE5}')
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
		return win32com.client.util.Iterator(ob, '{8ED56403-6EF8-4451-9CA4-7DBE298F4FE5}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{8ED56403-6EF8-4451-9CA4-7DBE298F4FE5}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IBNPBodyBeltFlat(DispatchBaseClass):
	'''Flat belt body'''
	CLSID = IID('{EFB4D776-2786-4A6D-BF68-A50DE0B265E2}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateMarker(self, strName, pRefFrame):
		'''
		Creates a marker
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ProcessNet.IMarker
		'''
		ret = self._oleobj_.InvokeTypes(11054, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMarker', '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11051, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactNode(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "ContactNode", '{0711C396-7AF8-4A58-A98E-EDC99123FB42}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11100, 2, (9, 0), (), "Geometry", '{9033BB6E-5115-49FA-83A2-E39301FBFD6C}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(11052, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((11052, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactNode = property(_get_ContactNode, None)
	'''
	Contact node

	:type: recurdyn.BNP.IBNPContactNodePropertyBeltFlat
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

	:type: recurdyn.BNP.IBNPGeometryBeltFlat
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

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
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactNode": (11101, 2, (9, 0), (), "ContactNode", '{0711C396-7AF8-4A58-A98E-EDC99123FB42}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11100, 2, (9, 0), (), "Geometry", '{9033BB6E-5115-49FA-83A2-E39301FBFD6C}'),
		"Graphic": (11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (11052, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((11052, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBodyBeltRibbedV(DispatchBaseClass):
	'''Ribbed_V belt body'''
	CLSID = IID('{ADEA5DA8-03AA-4840-B783-E04A9840F972}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateMarker(self, strName, pRefFrame):
		'''
		Creates a marker
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ProcessNet.IMarker
		'''
		ret = self._oleobj_.InvokeTypes(11054, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMarker', '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11051, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactNode(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "ContactNode", '{ABC5653E-52A2-4028-AE40-3738D348CF0D}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11100, 2, (9, 0), (), "Geometry", '{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(11052, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((11052, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactNode = property(_get_ContactNode, None)
	'''
	Contact node

	:type: recurdyn.BNP.IBNPContactNodePropertyBeltRibbedV
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

	:type: recurdyn.BNP.IBNPGeometryBeltRibbedV
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

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
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactNode": (11101, 2, (9, 0), (), "ContactNode", '{ABC5653E-52A2-4028-AE40-3738D348CF0D}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11100, 2, (9, 0), (), "Geometry", '{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}'),
		"Graphic": (11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (11052, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((11052, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBodyBeltShell(DispatchBaseClass):
	'''Shell belt body'''
	CLSID = IID('{AE6E5127-052C-43DC-B39E-9C19E632FC4A}')
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


	def _get_BCCollection(self):
		return self._ApplyTypes_(*(11102, 2, (9, 0), (), "BCCollection", '{7F035946-EE7C-4557-BAFC-000BDD366EDF}'))
	def _get_BCOrienation(self):
		return self._ApplyTypes_(*(11104, 2, (3, 0), (), "BCOrienation", '{14B4CA05-EA66-4C59-BED0-04E27062CE88}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ConnectingParameters(self):
		return self._ApplyTypes_(*(11100, 2, (9, 0), (), "ConnectingParameters", '{A111AE4E-7116-496C-BA07-1B125F33ECEA}'))
	def _get_FlexBody(self):
		return self._ApplyTypes_(*(11105, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "Geometry", '{FD1CA7C1-21FE-488D-88DC-87AF6CC66D8E}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_OutputCollection(self):
		return self._ApplyTypes_(*(11103, 2, (9, 0), (), "OutputCollection", '{4549131A-72B6-45B1-9ABE-C2A32F250FED}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_BCOrienation(self, value):
		if "BCOrienation" in self.__dict__: self.__dict__["BCOrienation"] = value; return
		self._oleobj_.Invoke(*((11104, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BCCollection = property(_get_BCCollection, None)
	'''
	Node boundary condition collection

	:type: recurdyn.ProcessNet.INodeBCCollection
	'''
	BCOrienation = property(_get_BCOrienation, _set_BCOrienation)
	'''
	BC Orienation

	:type: recurdyn.BNP.BNPBCOrienationType
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ConnectingParameters = property(_get_ConnectingParameters, None)
	'''
	Connecting parameters

	:type: recurdyn.BNP.IBNPConnectingParameters
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

	:type: recurdyn.BNP.IBNPGeometryBeltShell
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
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_BCOrienation": _set_BCOrienation,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BCCollection": (11102, 2, (9, 0), (), "BCCollection", '{7F035946-EE7C-4557-BAFC-000BDD366EDF}'),
		"BCOrienation": (11104, 2, (3, 0), (), "BCOrienation", '{14B4CA05-EA66-4C59-BED0-04E27062CE88}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConnectingParameters": (11100, 2, (9, 0), (), "ConnectingParameters", '{A111AE4E-7116-496C-BA07-1B125F33ECEA}'),
		"FlexBody": (11105, 2, (9, 0), (), "FlexBody", '{9257FD72-F3D0-4E57-A114-2045356D78CD}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (11101, 2, (9, 0), (), "Geometry", '{FD1CA7C1-21FE-488D-88DC-87AF6CC66D8E}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"OutputCollection": (11103, 2, (9, 0), (), "OutputCollection", '{4549131A-72B6-45B1-9ABE-C2A32F250FED}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"BCOrienation": ((11104, LCID, 4, 0),()),
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

class IBNPBodyBeltTiming(DispatchBaseClass):
	'''Timing belt body'''
	CLSID = IID('{776A8BE0-9FC0-4A70-983E-7015F0EC7EF0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateMarker(self, strName, pRefFrame):
		'''
		Creates a marker
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ProcessNet.IMarker
		'''
		ret = self._oleobj_.InvokeTypes(11054, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMarker', '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11051, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11100, 2, (9, 0), (), "Geometry", '{28B9F577-7066-4B2E-80A2-AF7D140593AC}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(11052, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((11052, LCID, 4, 0) + (value,) + ()))
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
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryBeltTiming
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

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
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11100, 2, (9, 0), (), "Geometry", '{28B9F577-7066-4B2E-80A2-AF7D140593AC}'),
		"Graphic": (11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (11052, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((11052, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBodyBeltV(DispatchBaseClass):
	'''V belt body'''
	CLSID = IID('{147D3D43-46A0-4F8F-8BC8-F8554A9EC105}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateMarker(self, strName, pRefFrame):
		'''
		Creates a marker
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ProcessNet.IMarker
		'''
		ret = self._oleobj_.InvokeTypes(11054, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMarker', '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(11051, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactNode(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "ContactNode", '{7AE525B3-FE13-4117-809E-476C72E2847C}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11100, 2, (9, 0), (), "Geometry", '{185F6935-19D9-4664-91A4-C564A61DF014}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(11052, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((11052, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactNode = property(_get_ContactNode, None)
	'''
	Contact node

	:type: recurdyn.BNP.IBNPContactNodePropertyBeltV
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

	:type: recurdyn.BNP.IBNPGeometryBeltV
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

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
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactNode": (11101, 2, (9, 0), (), "ContactNode", '{7AE525B3-FE13-4117-809E-476C72E2847C}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11100, 2, (9, 0), (), "Geometry", '{185F6935-19D9-4664-91A4-C564A61DF014}'),
		"Graphic": (11053, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (11052, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((11052, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPBodyCollection(DispatchBaseClass):
	'''BNP body collection'''
	CLSID = IID('{DE7BC821-F8B2-493F-A604-08BC45622B02}')
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
		:rtype: recurdyn.BNP.IBNPBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')
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
		:rtype: recurdyn.BNP.IBNPBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')
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
		return win32com.client.util.Iterator(ob, '{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IBNPBodyPulley(DispatchBaseClass):
	'''Belt body pulley'''
	CLSID = IID('{0AF5EA96-DFB9-43D4-925C-CEC2CB1EB928}')
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
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(11054, 2, (19, 0), (), "ContactPoints", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
	def _set_ContactPoints(self, value):
		if "ContactPoints" in self.__dict__: self.__dict__["ContactPoints"] = value; return
		self._oleobj_.Invoke(*((11054, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (value,) + ()))
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
	ContactDirection = property(_get_ContactDirection, None)
	'''
	Contact direction type

	:type: recurdyn.BNP.IBNPContactDirection
	'''
	ContactPoints = property(_get_ContactPoints, _set_ContactPoints)
	'''
	The number of max contact points

	:type: int
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	Contact search type

	:type: recurdyn.BNP.IBNPContactSearch
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
		"_set_ContactPoints": _set_ContactPoints,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'),
		"ContactPoints": (11054, 2, (19, 0), (), "ContactPoints", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"ContactSearch": (11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'),
		"ForceDisplay": (11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ContactPoints": ((11054, LCID, 4, 0),()),
		"ForceDisplay": ((11053, LCID, 4, 0),()),
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

class IBNPBodyPulleyCrown(DispatchBaseClass):
	'''Belt crown pulley body'''
	CLSID = IID('{1640FE01-608A-4380-B9EF-6C40A8DC5B57}')
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
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(11054, 2, (19, 0), (), "ContactPoints", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "Geometry", '{7ACC0B53-41A1-45D3-A170-8C7FD07C4E66}'))
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
	def _set_ContactPoints(self, value):
		if "ContactPoints" in self.__dict__: self.__dict__["ContactPoints"] = value; return
		self._oleobj_.Invoke(*((11054, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (value,) + ()))
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
	ContactDirection = property(_get_ContactDirection, None)
	'''
	Contact direction type

	:type: recurdyn.BNP.IBNPContactDirection
	'''
	ContactPoints = property(_get_ContactPoints, _set_ContactPoints)
	'''
	The number of max contact points

	:type: int
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	Contact search type

	:type: recurdyn.BNP.IBNPContactSearch
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryPulleyCrown
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
		"_set_ContactPoints": _set_ContactPoints,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'),
		"ContactPoints": (11054, 2, (19, 0), (), "ContactPoints", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"ContactSearch": (11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'),
		"ForceDisplay": (11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11101, 2, (9, 0), (), "Geometry", '{7ACC0B53-41A1-45D3-A170-8C7FD07C4E66}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ContactPoints": ((11054, LCID, 4, 0),()),
		"ForceDisplay": ((11053, LCID, 4, 0),()),
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

class IBNPBodyPulleyFlange(DispatchBaseClass):
	'''Belt flange pulley body'''
	CLSID = IID('{FFD05BAA-458B-4C65-AF21-DF21C3C5FA4D}')
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
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(11054, 2, (19, 0), (), "ContactPoints", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "Geometry", '{D15BA410-27CD-4BBF-8B63-7157B683989A}'))
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
	def _set_ContactPoints(self, value):
		if "ContactPoints" in self.__dict__: self.__dict__["ContactPoints"] = value; return
		self._oleobj_.Invoke(*((11054, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (value,) + ()))
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
	ContactDirection = property(_get_ContactDirection, None)
	'''
	Contact direction type

	:type: recurdyn.BNP.IBNPContactDirection
	'''
	ContactPoints = property(_get_ContactPoints, _set_ContactPoints)
	'''
	The number of max contact points

	:type: int
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	Contact search type

	:type: recurdyn.BNP.IBNPContactSearch
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryPulleyFlange
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
		"_set_ContactPoints": _set_ContactPoints,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'),
		"ContactPoints": (11054, 2, (19, 0), (), "ContactPoints", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"ContactSearch": (11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'),
		"ForceDisplay": (11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11101, 2, (9, 0), (), "Geometry", '{D15BA410-27CD-4BBF-8B63-7157B683989A}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ContactPoints": ((11054, LCID, 4, 0),()),
		"ForceDisplay": ((11053, LCID, 4, 0),()),
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

class IBNPBodyPulleyPrism(DispatchBaseClass):
	'''Belt prism pulley body'''
	CLSID = IID('{915B275A-9C28-4898-93D2-C28DB53018E2}')
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
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(11054, 2, (19, 0), (), "ContactPoints", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "Geometry", '{CAFDBC3C-C51A-412A-80E1-7F58BB60F820}'))
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
	def _set_ContactPoints(self, value):
		if "ContactPoints" in self.__dict__: self.__dict__["ContactPoints"] = value; return
		self._oleobj_.Invoke(*((11054, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (value,) + ()))
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
	ContactDirection = property(_get_ContactDirection, None)
	'''
	Contact direction type

	:type: recurdyn.BNP.IBNPContactDirection
	'''
	ContactPoints = property(_get_ContactPoints, _set_ContactPoints)
	'''
	The number of max contact points

	:type: int
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	Contact search type

	:type: recurdyn.BNP.IBNPContactSearch
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryPulleyPrism
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
		"_set_ContactPoints": _set_ContactPoints,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'),
		"ContactPoints": (11054, 2, (19, 0), (), "ContactPoints", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"ContactSearch": (11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'),
		"ForceDisplay": (11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11101, 2, (9, 0), (), "Geometry", '{CAFDBC3C-C51A-412A-80E1-7F58BB60F820}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ContactPoints": ((11054, LCID, 4, 0),()),
		"ForceDisplay": ((11053, LCID, 4, 0),()),
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

class IBNPBodyPulleyRibbedV(DispatchBaseClass):
	'''Belt ribbed_v pulley body'''
	CLSID = IID('{57849CE0-405E-474C-B4C1-65523C6DEE04}')
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
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(11054, 2, (19, 0), (), "ContactPoints", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "Geometry", '{32EA063C-BD96-48EA-93C6-C3DAA3961197}'))
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
	def _set_ContactPoints(self, value):
		if "ContactPoints" in self.__dict__: self.__dict__["ContactPoints"] = value; return
		self._oleobj_.Invoke(*((11054, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (value,) + ()))
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
	ContactDirection = property(_get_ContactDirection, None)
	'''
	Contact direction type

	:type: recurdyn.BNP.IBNPContactDirection
	'''
	ContactPoints = property(_get_ContactPoints, _set_ContactPoints)
	'''
	The number of max contact points

	:type: int
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	Contact search type

	:type: recurdyn.BNP.IBNPContactSearch
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryPulleyRibbedV
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
		"_set_ContactPoints": _set_ContactPoints,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'),
		"ContactPoints": (11054, 2, (19, 0), (), "ContactPoints", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"ContactSearch": (11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'),
		"ForceDisplay": (11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11101, 2, (9, 0), (), "Geometry", '{32EA063C-BD96-48EA-93C6-C3DAA3961197}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ContactPoints": ((11054, LCID, 4, 0),()),
		"ForceDisplay": ((11053, LCID, 4, 0),()),
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

class IBNPBodyPulleyRoller(DispatchBaseClass):
	'''Belt roller pulley body'''
	CLSID = IID('{FB9C36C7-777E-4F21-92B5-662D9B696B9F}')
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
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(11054, 2, (19, 0), (), "ContactPoints", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "Geometry", '{530E037B-C319-4E08-A507-77020D1582D4}'))
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
	def _set_ContactPoints(self, value):
		if "ContactPoints" in self.__dict__: self.__dict__["ContactPoints"] = value; return
		self._oleobj_.Invoke(*((11054, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (value,) + ()))
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
	ContactDirection = property(_get_ContactDirection, None)
	'''
	Contact direction type

	:type: recurdyn.BNP.IBNPContactDirection
	'''
	ContactPoints = property(_get_ContactPoints, _set_ContactPoints)
	'''
	The number of max contact points

	:type: int
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	Contact search type

	:type: recurdyn.BNP.IBNPContactSearch
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryPulleyRoller
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
		"_set_ContactPoints": _set_ContactPoints,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'),
		"ContactPoints": (11054, 2, (19, 0), (), "ContactPoints", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"ContactSearch": (11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'),
		"ForceDisplay": (11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11101, 2, (9, 0), (), "Geometry", '{530E037B-C319-4E08-A507-77020D1582D4}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ContactPoints": ((11054, LCID, 4, 0),()),
		"ForceDisplay": ((11053, LCID, 4, 0),()),
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

class IBNPBodyPulleyTiming(DispatchBaseClass):
	'''Belt timing pulley body'''
	CLSID = IID('{6CAB2527-B23C-46F2-9E3F-9D793E4950EA}')
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
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(11054, 2, (19, 0), (), "ContactPoints", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "Geometry", '{73E882E6-E6A2-41EB-B965-F386ADD519E8}'))
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
	def _set_ContactPoints(self, value):
		if "ContactPoints" in self.__dict__: self.__dict__["ContactPoints"] = value; return
		self._oleobj_.Invoke(*((11054, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (value,) + ()))
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
	ContactDirection = property(_get_ContactDirection, None)
	'''
	Contact direction type

	:type: recurdyn.BNP.IBNPContactDirection
	'''
	ContactPoints = property(_get_ContactPoints, _set_ContactPoints)
	'''
	The number of max contact points

	:type: int
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	Contact search type

	:type: recurdyn.BNP.IBNPContactSearch
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryPulleyTiming
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
		"_set_ContactPoints": _set_ContactPoints,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'),
		"ContactPoints": (11054, 2, (19, 0), (), "ContactPoints", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"ContactSearch": (11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'),
		"ForceDisplay": (11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11101, 2, (9, 0), (), "Geometry", '{73E882E6-E6A2-41EB-B965-F386ADD519E8}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ContactPoints": ((11054, LCID, 4, 0),()),
		"ForceDisplay": ((11053, LCID, 4, 0),()),
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

class IBNPBodyPulleyV(DispatchBaseClass):
	'''Belt V pulley body'''
	CLSID = IID('{DF52F1D2-21BC-4B10-989F-1C434899404A}')
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
	def _get_ContactDirection(self):
		return self._ApplyTypes_(*(11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'))
	def _get_ContactPoints(self):
		return self._ApplyTypes_(*(11054, 2, (19, 0), (), "ContactPoints", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(11101, 2, (9, 0), (), "Geometry", '{CB8A9B5A-33D9-4AE8-8EB6-AE1CD753C5AF}'))
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
	def _set_ContactPoints(self, value):
		if "ContactPoints" in self.__dict__: self.__dict__["ContactPoints"] = value; return
		self._oleobj_.Invoke(*((11054, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((11053, LCID, 4, 0) + (value,) + ()))
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
	ContactDirection = property(_get_ContactDirection, None)
	'''
	Contact direction type

	:type: recurdyn.BNP.IBNPContactDirection
	'''
	ContactPoints = property(_get_ContactPoints, _set_ContactPoints)
	'''
	The number of max contact points

	:type: int
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact property

	:type: recurdyn.BNP.IBNPContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	Contact search type

	:type: recurdyn.BNP.IBNPContactSearch
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.BNP.IBNPGeometryPulleyV
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
		"_set_ContactPoints": _set_ContactPoints,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactDirection": (11052, 2, (9, 0), (), "ContactDirection", '{2391593F-3C53-4F17-8285-F2857B2229C7}'),
		"ContactPoints": (11054, 2, (19, 0), (), "ContactPoints", None),
		"ContactProperty": (11050, 2, (9, 0), (), "ContactProperty", '{06D06385-6578-48E1-AACC-2BB6BD56B20A}'),
		"ContactSearch": (11051, 2, (9, 0), (), "ContactSearch", '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}'),
		"ForceDisplay": (11053, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (11000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (11101, 2, (9, 0), (), "Geometry", '{CB8A9B5A-33D9-4AE8-8EB6-AE1CD753C5AF}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ContactPoints": ((11054, LCID, 4, 0),()),
		"ForceDisplay": ((11053, LCID, 4, 0),()),
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

class IBNPConnectingParameters(DispatchBaseClass):
	'''BNP connecting parameters'''
	CLSID = IID('{A111AE4E-7116-496C-BA07-1B125F33ECEA}')
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
		return self._ApplyTypes_(*(11152, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MomentOfInertia(self):
		return self._ApplyTypes_(*(11153, 2, (9, 0), (), "MomentOfInertia", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationnalDampingRatio(self):
		return self._ApplyTypes_(*(11157, 2, (9, 0), (), "RotationnalDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationnalStiffness(self):
		return self._ApplyTypes_(*(11156, 2, (9, 0), (), "RotationnalStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationalDampingRatio(self):
		return self._ApplyTypes_(*(11155, 2, (9, 0), (), "TranslationalDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationalStiffness(self):
		return self._ApplyTypes_(*(11154, 2, (9, 0), (), "TranslationalStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseForceConnector(self):
		return self._ApplyTypes_(*(11150, 2, (11, 0), (), "UseForceConnector", None))
	def _get_UseSyncFDR(self):
		return self._ApplyTypes_(*(11151, 2, (11, 0), (), "UseSyncFDR", None))

	def _set_UseForceConnector(self, value):
		if "UseForceConnector" in self.__dict__: self.__dict__["UseForceConnector"] = value; return
		self._oleobj_.Invoke(*((11150, LCID, 4, 0) + (value,) + ()))
	def _set_UseSyncFDR(self, value):
		if "UseSyncFDR" in self.__dict__: self.__dict__["UseSyncFDR"] = value; return
		self._oleobj_.Invoke(*((11151, LCID, 4, 0) + (value,) + ()))

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
		"Mass": (11152, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MomentOfInertia": (11153, 2, (9, 0), (), "MomentOfInertia", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationnalDampingRatio": (11157, 2, (9, 0), (), "RotationnalDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationnalStiffness": (11156, 2, (9, 0), (), "RotationnalStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationalDampingRatio": (11155, 2, (9, 0), (), "TranslationalDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationalStiffness": (11154, 2, (9, 0), (), "TranslationalStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseForceConnector": (11150, 2, (11, 0), (), "UseForceConnector", None),
		"UseSyncFDR": (11151, 2, (11, 0), (), "UseSyncFDR", None),
	}
	_prop_map_put_ = {
		"UseForceConnector": ((11150, LCID, 4, 0),()),
		"UseSyncFDR": ((11151, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPContactDirection(DispatchBaseClass):
	'''BNP contact direction'''
	CLSID = IID('{2391593F-3C53-4F17-8285-F2857B2229C7}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Type(self):
		return self._ApplyTypes_(*(11000, 2, (3, 0), (), "Type", '{22B08D86-DCCB-468A-A747-466E1F7ACAFD}'))

	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((11000, LCID, 4, 0) + (value,) + ()))

	Type = property(_get_Type, _set_Type)
	'''
	Direction type

	:type: recurdyn.BNP.BNPContactDirectionType
	'''

	_prop_map_set_function_ = {
		"_set_Type": _set_Type,
	}
	_prop_map_get_ = {
		"Type": (11000, 2, (3, 0), (), "Type", '{22B08D86-DCCB-468A-A747-466E1F7ACAFD}'),
	}
	_prop_map_put_ = {
		"Type": ((11000, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPContactFriction(DispatchBaseClass):
	'''BNP contact friction'''
	CLSID = IID('{E2EB7072-FAB5-4AAE-8E30-4DABC6A590BA}')
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
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumFrictionForce(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "MaximumFrictionForce", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaximumstictionDeformation(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "MaximumstictionDeformation", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticFrictionCoefficient(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticThresholdVelocity(self):
		return self._ApplyTypes_(*(11001, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseMaximumFrictionForce(self):
		return self._ApplyTypes_(*(11004, 2, (11, 0), (), "UseMaximumFrictionForce", None))

	def _set_UseMaximumFrictionForce(self, value):
		if "UseMaximumFrictionForce" in self.__dict__: self.__dict__["UseMaximumFrictionForce"] = value; return
		self._oleobj_.Invoke(*((11004, LCID, 4, 0) + (value,) + ()))

	DynamicThresholdVelocity = property(_get_DynamicThresholdVelocity, None)
	'''
	Dynamic threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumFrictionForce = property(_get_MaximumFrictionForce, None)
	'''
	Static friction coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaximumstictionDeformation = property(_get_MaximumstictionDeformation, None)
	'''
	Static friction coefficient

	:type: recurdyn.ProcessNet.IDouble
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

	_prop_map_set_function_ = {
		"_set_UseMaximumFrictionForce": _set_UseMaximumFrictionForce,
	}
	_prop_map_get_ = {
		"DynamicThresholdVelocity": (11002, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumFrictionForce": (11005, 2, (9, 0), (), "MaximumFrictionForce", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaximumstictionDeformation": (11006, 2, (9, 0), (), "MaximumstictionDeformation", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticFrictionCoefficient": (11003, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticThresholdVelocity": (11001, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseMaximumFrictionForce": (11004, 2, (11, 0), (), "UseMaximumFrictionForce", None),
	}
	_prop_map_put_ = {
		"UseMaximumFrictionForce": ((11004, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPContactNodePropertyBeltFlat(DispatchBaseClass):
	'''Flat belt contact node property'''
	CLSID = IID('{0711C396-7AF8-4A58-A98E-EDC99123FB42}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ContactNodeBottom(self):
		return self._ApplyTypes_(*(22050, 2, (19, 0), (), "ContactNodeBottom", None))
	def _get_ContactNodeSide(self):
		return self._ApplyTypes_(*(22051, 2, (19, 0), (), "ContactNodeSide", None))
	def _get_ContactNodeTop(self):
		return self._ApplyTypes_(*(22052, 2, (19, 0), (), "ContactNodeTop", None))
	def _get_EstimationContactNodes(self):
		return self._ApplyTypes_(*(22053, 2, (11, 0), (), "EstimationContactNodes", None))

	def _set_ContactNodeBottom(self, value):
		if "ContactNodeBottom" in self.__dict__: self.__dict__["ContactNodeBottom"] = value; return
		self._oleobj_.Invoke(*((22050, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeSide(self, value):
		if "ContactNodeSide" in self.__dict__: self.__dict__["ContactNodeSide"] = value; return
		self._oleobj_.Invoke(*((22051, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeTop(self, value):
		if "ContactNodeTop" in self.__dict__: self.__dict__["ContactNodeTop"] = value; return
		self._oleobj_.Invoke(*((22052, LCID, 4, 0) + (value,) + ()))
	def _set_EstimationContactNodes(self, value):
		if "EstimationContactNodes" in self.__dict__: self.__dict__["EstimationContactNodes"] = value; return
		self._oleobj_.Invoke(*((22053, LCID, 4, 0) + (value,) + ()))

	ContactNodeBottom = property(_get_ContactNodeBottom, _set_ContactNodeBottom)
	'''
	Flat belt bottom contact node

	:type: int
	'''
	ContactNodeSide = property(_get_ContactNodeSide, _set_ContactNodeSide)
	'''
	Flat belt side contact node

	:type: int
	'''
	ContactNodeTop = property(_get_ContactNodeTop, _set_ContactNodeTop)
	'''
	Flat belt top contact node

	:type: int
	'''
	EstimationContactNodes = property(_get_EstimationContactNodes, _set_EstimationContactNodes)
	'''
	Estimation contact nodes

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactNodeBottom": _set_ContactNodeBottom,
		"_set_ContactNodeSide": _set_ContactNodeSide,
		"_set_ContactNodeTop": _set_ContactNodeTop,
		"_set_EstimationContactNodes": _set_EstimationContactNodes,
	}
	_prop_map_get_ = {
		"ContactNodeBottom": (22050, 2, (19, 0), (), "ContactNodeBottom", None),
		"ContactNodeSide": (22051, 2, (19, 0), (), "ContactNodeSide", None),
		"ContactNodeTop": (22052, 2, (19, 0), (), "ContactNodeTop", None),
		"EstimationContactNodes": (22053, 2, (11, 0), (), "EstimationContactNodes", None),
	}
	_prop_map_put_ = {
		"ContactNodeBottom": ((22050, LCID, 4, 0),()),
		"ContactNodeSide": ((22051, LCID, 4, 0),()),
		"ContactNodeTop": ((22052, LCID, 4, 0),()),
		"EstimationContactNodes": ((22053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPContactNodePropertyBeltRibbedV(DispatchBaseClass):
	'''Ribbed_V belt contact node property'''
	CLSID = IID('{ABC5653E-52A2-4028-AE40-3738D348CF0D}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ContactNodeBottom(self):
		return self._ApplyTypes_(*(22050, 2, (19, 0), (), "ContactNodeBottom", None))
	def _get_ContactNodeGroove(self):
		return self._ApplyTypes_(*(22054, 2, (19, 0), (), "ContactNodeGroove", None))
	def _get_ContactNodeLowerSide(self):
		return self._ApplyTypes_(*(22051, 2, (19, 0), (), "ContactNodeLowerSide", None))
	def _get_ContactNodeTop(self):
		return self._ApplyTypes_(*(22053, 2, (19, 0), (), "ContactNodeTop", None))
	def _get_ContactNodeUpperSide(self):
		return self._ApplyTypes_(*(22052, 2, (19, 0), (), "ContactNodeUpperSide", None))
	def _get_EstimationContactNodes(self):
		return self._ApplyTypes_(*(22055, 2, (11, 0), (), "EstimationContactNodes", None))

	def _set_ContactNodeBottom(self, value):
		if "ContactNodeBottom" in self.__dict__: self.__dict__["ContactNodeBottom"] = value; return
		self._oleobj_.Invoke(*((22050, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeGroove(self, value):
		if "ContactNodeGroove" in self.__dict__: self.__dict__["ContactNodeGroove"] = value; return
		self._oleobj_.Invoke(*((22054, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeLowerSide(self, value):
		if "ContactNodeLowerSide" in self.__dict__: self.__dict__["ContactNodeLowerSide"] = value; return
		self._oleobj_.Invoke(*((22051, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeTop(self, value):
		if "ContactNodeTop" in self.__dict__: self.__dict__["ContactNodeTop"] = value; return
		self._oleobj_.Invoke(*((22053, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeUpperSide(self, value):
		if "ContactNodeUpperSide" in self.__dict__: self.__dict__["ContactNodeUpperSide"] = value; return
		self._oleobj_.Invoke(*((22052, LCID, 4, 0) + (value,) + ()))
	def _set_EstimationContactNodes(self, value):
		if "EstimationContactNodes" in self.__dict__: self.__dict__["EstimationContactNodes"] = value; return
		self._oleobj_.Invoke(*((22055, LCID, 4, 0) + (value,) + ()))

	ContactNodeBottom = property(_get_ContactNodeBottom, _set_ContactNodeBottom)
	'''
	Ribbed_V belt bottom contact node

	:type: int
	'''
	ContactNodeGroove = property(_get_ContactNodeGroove, _set_ContactNodeGroove)
	'''
	Ribbed_V belt top contact node

	:type: int
	'''
	ContactNodeLowerSide = property(_get_ContactNodeLowerSide, _set_ContactNodeLowerSide)
	'''
	Ribbed_V belt lower side contact node

	:type: int
	'''
	ContactNodeTop = property(_get_ContactNodeTop, _set_ContactNodeTop)
	'''
	Ribbed_V belt top contact node

	:type: int
	'''
	ContactNodeUpperSide = property(_get_ContactNodeUpperSide, _set_ContactNodeUpperSide)
	'''
	Ribbed_V belt upper side contact node

	:type: int
	'''
	EstimationContactNodes = property(_get_EstimationContactNodes, _set_EstimationContactNodes)
	'''
	Estimation contact nodes

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactNodeBottom": _set_ContactNodeBottom,
		"_set_ContactNodeGroove": _set_ContactNodeGroove,
		"_set_ContactNodeLowerSide": _set_ContactNodeLowerSide,
		"_set_ContactNodeTop": _set_ContactNodeTop,
		"_set_ContactNodeUpperSide": _set_ContactNodeUpperSide,
		"_set_EstimationContactNodes": _set_EstimationContactNodes,
	}
	_prop_map_get_ = {
		"ContactNodeBottom": (22050, 2, (19, 0), (), "ContactNodeBottom", None),
		"ContactNodeGroove": (22054, 2, (19, 0), (), "ContactNodeGroove", None),
		"ContactNodeLowerSide": (22051, 2, (19, 0), (), "ContactNodeLowerSide", None),
		"ContactNodeTop": (22053, 2, (19, 0), (), "ContactNodeTop", None),
		"ContactNodeUpperSide": (22052, 2, (19, 0), (), "ContactNodeUpperSide", None),
		"EstimationContactNodes": (22055, 2, (11, 0), (), "EstimationContactNodes", None),
	}
	_prop_map_put_ = {
		"ContactNodeBottom": ((22050, LCID, 4, 0),()),
		"ContactNodeGroove": ((22054, LCID, 4, 0),()),
		"ContactNodeLowerSide": ((22051, LCID, 4, 0),()),
		"ContactNodeTop": ((22053, LCID, 4, 0),()),
		"ContactNodeUpperSide": ((22052, LCID, 4, 0),()),
		"EstimationContactNodes": ((22055, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPContactNodePropertyBeltV(DispatchBaseClass):
	'''V belt contact node property'''
	CLSID = IID('{7AE525B3-FE13-4117-809E-476C72E2847C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ContactNodeBottom(self):
		return self._ApplyTypes_(*(22050, 2, (19, 0), (), "ContactNodeBottom", None))
	def _get_ContactNodeLowerSide(self):
		return self._ApplyTypes_(*(22051, 2, (19, 0), (), "ContactNodeLowerSide", None))
	def _get_ContactNodeTop(self):
		return self._ApplyTypes_(*(22053, 2, (19, 0), (), "ContactNodeTop", None))
	def _get_ContactNodeUpperSide(self):
		return self._ApplyTypes_(*(22052, 2, (19, 0), (), "ContactNodeUpperSide", None))
	def _get_EstimationContactNodes(self):
		return self._ApplyTypes_(*(22054, 2, (11, 0), (), "EstimationContactNodes", None))

	def _set_ContactNodeBottom(self, value):
		if "ContactNodeBottom" in self.__dict__: self.__dict__["ContactNodeBottom"] = value; return
		self._oleobj_.Invoke(*((22050, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeLowerSide(self, value):
		if "ContactNodeLowerSide" in self.__dict__: self.__dict__["ContactNodeLowerSide"] = value; return
		self._oleobj_.Invoke(*((22051, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeTop(self, value):
		if "ContactNodeTop" in self.__dict__: self.__dict__["ContactNodeTop"] = value; return
		self._oleobj_.Invoke(*((22053, LCID, 4, 0) + (value,) + ()))
	def _set_ContactNodeUpperSide(self, value):
		if "ContactNodeUpperSide" in self.__dict__: self.__dict__["ContactNodeUpperSide"] = value; return
		self._oleobj_.Invoke(*((22052, LCID, 4, 0) + (value,) + ()))
	def _set_EstimationContactNodes(self, value):
		if "EstimationContactNodes" in self.__dict__: self.__dict__["EstimationContactNodes"] = value; return
		self._oleobj_.Invoke(*((22054, LCID, 4, 0) + (value,) + ()))

	ContactNodeBottom = property(_get_ContactNodeBottom, _set_ContactNodeBottom)
	'''
	V belt bottom contact node

	:type: int
	'''
	ContactNodeLowerSide = property(_get_ContactNodeLowerSide, _set_ContactNodeLowerSide)
	'''
	V belt lower side contact node

	:type: int
	'''
	ContactNodeTop = property(_get_ContactNodeTop, _set_ContactNodeTop)
	'''
	V belt top contact node

	:type: int
	'''
	ContactNodeUpperSide = property(_get_ContactNodeUpperSide, _set_ContactNodeUpperSide)
	'''
	V belt upper side contact node

	:type: int
	'''
	EstimationContactNodes = property(_get_EstimationContactNodes, _set_EstimationContactNodes)
	'''
	Estimation contact nodes

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ContactNodeBottom": _set_ContactNodeBottom,
		"_set_ContactNodeLowerSide": _set_ContactNodeLowerSide,
		"_set_ContactNodeTop": _set_ContactNodeTop,
		"_set_ContactNodeUpperSide": _set_ContactNodeUpperSide,
		"_set_EstimationContactNodes": _set_EstimationContactNodes,
	}
	_prop_map_get_ = {
		"ContactNodeBottom": (22050, 2, (19, 0), (), "ContactNodeBottom", None),
		"ContactNodeLowerSide": (22051, 2, (19, 0), (), "ContactNodeLowerSide", None),
		"ContactNodeTop": (22053, 2, (19, 0), (), "ContactNodeTop", None),
		"ContactNodeUpperSide": (22052, 2, (19, 0), (), "ContactNodeUpperSide", None),
		"EstimationContactNodes": (22054, 2, (11, 0), (), "EstimationContactNodes", None),
	}
	_prop_map_put_ = {
		"ContactNodeBottom": ((22050, LCID, 4, 0),()),
		"ContactNodeLowerSide": ((22051, LCID, 4, 0),()),
		"ContactNodeTop": ((22053, LCID, 4, 0),()),
		"ContactNodeUpperSide": ((22052, LCID, 4, 0),()),
		"EstimationContactNodes": ((22054, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPContactProperty(DispatchBaseClass):
	'''BNP contact property'''
	CLSID = IID('{06D06385-6578-48E1-AACC-2BB6BD56B20A}')
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
		return self._ApplyTypes_(*(11016, 2, (3, 0), (), "ContactFrictionType", '{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}'))
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(11003, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(11012, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(11005, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(11015, 2, (9, 0), (), "Friction", '{E2EB7072-FAB5-4AAE-8E30-4DABC6A590BA}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(11006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(11008, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(11014, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(11010, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(11011, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(11004, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseFrictionSpline(self):
		return self._ApplyTypes_(*(11007, 2, (11, 0), (), "UseFrictionSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(11013, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(11009, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(11001, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_ContactFrictionType(self, value):
		if "ContactFrictionType" in self.__dict__: self.__dict__["ContactFrictionType"] = value; return
		self._oleobj_.Invoke(*((11016, LCID, 4, 0) + (value,) + ()))
	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((11005, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((11008, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((11002, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((11011, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((11004, LCID, 4, 0) + (value,) + ()))
	def _set_UseFrictionSpline(self, value):
		if "UseFrictionSpline" in self.__dict__: self.__dict__["UseFrictionSpline"] = value; return
		self._oleobj_.Invoke(*((11007, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((11013, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((11009, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))

	ContactFrictionType = property(_get_ContactFrictionType, _set_ContactFrictionType)
	'''
	Contact friction type

	:type: recurdyn.ProcessNet.ContactFrictionType
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
	Friction = property(_get_Friction, None)
	'''
	Friction

	:type: recurdyn.BNP.IBNPContactFriction
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
	UseFrictionSpline = property(_get_UseFrictionSpline, _set_UseFrictionSpline)
	'''
	Use friction spline : obsolete function

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

	_prop_map_set_function_ = {
		"_set_ContactFrictionType": _set_ContactFrictionType,
		"_set_DampingSpline": _set_DampingSpline,
		"_set_FrictionSpline": _set_FrictionSpline,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseFrictionSpline": _set_UseFrictionSpline,
		"_set_UseIndentationExponent": _set_UseIndentationExponent,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
	}
	_prop_map_get_ = {
		"ContactFrictionType": (11016, 2, (3, 0), (), "ContactFrictionType", '{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}'),
		"DampingCoefficient": (11003, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (11012, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (11005, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"Friction": (11015, 2, (9, 0), (), "Friction", '{E2EB7072-FAB5-4AAE-8E30-4DABC6A590BA}'),
		"FrictionCoefficient": (11006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (11008, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"IndentationExponent": (11014, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (11000, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (11010, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (11002, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (11011, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (11004, 2, (11, 0), (), "UseDampingSpline", None),
		"UseFrictionSpline": (11007, 2, (11, 0), (), "UseFrictionSpline", None),
		"UseIndentationExponent": (11013, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseStiffnessExponent": (11009, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (11001, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"ContactFrictionType": ((11016, LCID, 4, 0),()),
		"DampingSpline": ((11005, LCID, 4, 0),()),
		"FrictionSpline": ((11008, LCID, 4, 0),()),
		"StiffnessSpline": ((11002, LCID, 4, 0),()),
		"UseDampingExponent": ((11011, LCID, 4, 0),()),
		"UseDampingSpline": ((11004, LCID, 4, 0),()),
		"UseFrictionSpline": ((11007, LCID, 4, 0),()),
		"UseIndentationExponent": ((11013, LCID, 4, 0),()),
		"UseStiffnessExponent": ((11009, LCID, 4, 0),()),
		"UseStiffnessSpline": ((11001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPContactSearch(DispatchBaseClass):
	'''BNP contact search'''
	CLSID = IID('{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Type(self):
		return self._ApplyTypes_(*(11000, 2, (3, 0), (), "Type", '{FA51F4CB-1D66-4B58-A5C0-185D24EFBC01}'))
	def _get_UseUserBoundaryForPartialSearch(self):
		return self._ApplyTypes_(*(11001, 2, (11, 0), (), "UseUserBoundaryForPartialSearch", None))
	def _get_UserBoundaryForPartialSearch(self):
		return self._ApplyTypes_(*(11002, 2, (9, 0), (), "UserBoundaryForPartialSearch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((11000, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserBoundaryForPartialSearch(self, value):
		if "UseUserBoundaryForPartialSearch" in self.__dict__: self.__dict__["UseUserBoundaryForPartialSearch"] = value; return
		self._oleobj_.Invoke(*((11001, LCID, 4, 0) + (value,) + ()))

	Type = property(_get_Type, _set_Type)
	'''
	Search type

	:type: recurdyn.BNP.BNPContactSearchType
	'''
	UseUserBoundaryForPartialSearch = property(_get_UseUserBoundaryForPartialSearch, _set_UseUserBoundaryForPartialSearch)
	'''
	Use the user boundary of the partial search.

	:type: bool
	'''
	UserBoundaryForPartialSearch = property(_get_UserBoundaryForPartialSearch, None)
	'''
	User boundary of the partial search.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Type": _set_Type,
		"_set_UseUserBoundaryForPartialSearch": _set_UseUserBoundaryForPartialSearch,
	}
	_prop_map_get_ = {
		"Type": (11000, 2, (3, 0), (), "Type", '{FA51F4CB-1D66-4B58-A5C0-185D24EFBC01}'),
		"UseUserBoundaryForPartialSearch": (11001, 2, (11, 0), (), "UseUserBoundaryForPartialSearch", None),
		"UserBoundaryForPartialSearch": (11002, 2, (9, 0), (), "UserBoundaryForPartialSearch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Type": ((11000, LCID, 4, 0),()),
		"UseUserBoundaryForPartialSearch": ((11001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometry2DGuide(DispatchBaseClass):
	'''2D Guide geometry'''
	CLSID = IID('{97BC1771-06D1-4B98-B91C-3B78C3E47C95}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def UpdateGeometry(self):
		'''
		Update Geometry
		'''
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), (),)


	def _get_Depth(self):
		return self._ApplyTypes_(*(50, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ViewRefFrame(self):
		return self._ApplyTypes_(*(51, 2, (9, 0), (), "ViewRefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))

	Depth = property(_get_Depth, None)
	'''
	Depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	ViewRefFrame = property(_get_ViewRefFrame, None)
	'''
	View reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Depth": (50, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ViewRefFrame": (51, 2, (9, 0), (), "ViewRefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
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

class IBNPGeometry2DGuideArc(DispatchBaseClass):
	'''2D Arc Guide geometry'''
	CLSID = IID('{28DFE5F6-D718-4CD5-AA3B-4CC4538DEB62}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def UpdateGeometry(self):
		'''
		Update Geometry
		'''
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), (),)


	def _get_Depth(self):
		return self._ApplyTypes_(*(50, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Point3DWithRadiusCollection(self):
		return self._ApplyTypes_(*(100, 2, (9, 0), (), "Point3DWithRadiusCollection", '{0476BFAD-0FF1-4CA4-8B59-AE9E00842CCB}'))
	def _get_ViewRefFrame(self):
		return self._ApplyTypes_(*(51, 2, (9, 0), (), "ViewRefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))

	Depth = property(_get_Depth, None)
	'''
	Depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	Point3DWithRadiusCollection = property(_get_Point3DWithRadiusCollection, None)
	'''
	Point3D with Radius collection

	:type: recurdyn.ProcessNet.IPoint3DWithRadiusCollection
	'''
	ViewRefFrame = property(_get_ViewRefFrame, None)
	'''
	View reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Depth": (50, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Point3DWithRadiusCollection": (100, 2, (9, 0), (), "Point3DWithRadiusCollection", '{0476BFAD-0FF1-4CA4-8B59-AE9E00842CCB}'),
		"ViewRefFrame": (51, 2, (9, 0), (), "ViewRefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
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

class IBNPGeometry2DGuideLinear(DispatchBaseClass):
	'''2D Linear Guide geometry'''
	CLSID = IID('{6E62C6CA-9D43-4D53-A2B1-4BEFD6DE5D22}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def UpdateGeometry(self):
		'''
		Update Geometry
		'''
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), (),)


	def _get_Depth(self):
		return self._ApplyTypes_(*(50, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Point3DCollection(self):
		return self._ApplyTypes_(*(100, 2, (9, 0), (), "Point3DCollection", '{7AAA986F-35DD-4DCF-843A-CEBA8E09D33A}'))
	def _get_ViewRefFrame(self):
		return self._ApplyTypes_(*(51, 2, (9, 0), (), "ViewRefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))

	Depth = property(_get_Depth, None)
	'''
	Depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	Point3DCollection = property(_get_Point3DCollection, None)
	'''
	Point3D collection

	:type: recurdyn.ProcessNet.IPoint3DCollection
	'''
	ViewRefFrame = property(_get_ViewRefFrame, None)
	'''
	View reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Depth": (50, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Point3DCollection": (100, 2, (9, 0), (), "Point3DCollection", '{7AAA986F-35DD-4DCF-843A-CEBA8E09D33A}'),
		"ViewRefFrame": (51, 2, (9, 0), (), "ViewRefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
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

class IBNPGeometryBeltBeam(DispatchBaseClass):
	'''Beam belt geometry'''
	CLSID = IID('{64E4D842-5C51-484B-B3F8-C54D097BBDA1}')
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
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11166, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody(self, pVal):
		'''
		Delete a passing body
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11167, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def _get_Angle(self):
		return self._ApplyTypes_(*(11156, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_AssembledThickness(self):
		return self._ApplyTypes_(*(11158, 2, (9, 0), (), "AssembledThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_BeltType(self):
		return self._ApplyTypes_(*(11152, 2, (3, 0), (), "BeltType", '{0BB88860-1CA3-4F91-973F-ACA0600D489B}'))
	def _get_Color(self):
		return self._ApplyTypes_(*(11150, 2, (19, 0), (), "Color", None))
	def _get_DisplayNodeID(self):
		return self._ApplyTypes_(*(11151, 2, (11, 0), (), "DisplayNodeID", None))
	def _get_ElementLength(self):
		return self._ApplyTypes_(*(11162, 2, (5, 0), (), "ElementLength", None))
	def _get_InitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(11169, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Interval(self):
		return self._ApplyTypes_(*(11159, 2, (3, 0), (), "Interval", None))
	def _get_LowerThickness(self):
		return self._ApplyTypes_(*(11153, 2, (9, 0), (), "LowerThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaterialProperty(self):
		return self._ApplyTypes_(*(11164, 2, (9, 0), (), "MaterialProperty", '{D9C23616-C0D3-422D-8A74-02654AB2E863}'))
	def _get_NumberOfElements(self):
		return self._ApplyTypes_(*(11161, 2, (19, 0), (), "NumberOfElements", None))
	def _get_PassingBodyCollection(self):
		return self._ApplyTypes_(*(11165, 2, (9, 0), (), "PassingBodyCollection", '{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(11160, 2, (9, 0), (), "Profile", '{3218112D-CC7E-4DC3-A6A4-36A6B33C12B6}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(11157, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StretchedLength(self):
		return self._ApplyTypes_(*(11163, 2, (9, 0), (), "StretchedLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UpperThickness(self):
		return self._ApplyTypes_(*(11154, 2, (9, 0), (), "UpperThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseInitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(11168, 2, (11, 0), (), "UseInitialLongitudinalVelocity", None))
	def _get_UseUpdateGeometryInformationAutomatically(self):
		return self._ApplyTypes_(*(11170, 2, (11, 0), (), "UseUpdateGeometryInformationAutomatically", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(11155, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_BeltType(self, value):
		if "BeltType" in self.__dict__: self.__dict__["BeltType"] = value; return
		self._oleobj_.Invoke(*((11152, LCID, 4, 0) + (value,) + ()))
	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((11150, LCID, 4, 0) + (value,) + ()))
	def _set_DisplayNodeID(self, value):
		if "DisplayNodeID" in self.__dict__: self.__dict__["DisplayNodeID"] = value; return
		self._oleobj_.Invoke(*((11151, LCID, 4, 0) + (value,) + ()))
	def _set_Interval(self, value):
		if "Interval" in self.__dict__: self.__dict__["Interval"] = value; return
		self._oleobj_.Invoke(*((11159, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialLongitudinalVelocity(self, value):
		if "UseInitialLongitudinalVelocity" in self.__dict__: self.__dict__["UseInitialLongitudinalVelocity"] = value; return
		self._oleobj_.Invoke(*((11168, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdateGeometryInformationAutomatically(self, value):
		if "UseUpdateGeometryInformationAutomatically" in self.__dict__: self.__dict__["UseUpdateGeometryInformationAutomatically"] = value; return
		self._oleobj_.Invoke(*((11170, LCID, 4, 0) + (value,) + ()))

	Angle = property(_get_Angle, None)
	'''
	Angle

	:type: recurdyn.ProcessNet.IDouble
	'''
	AssembledThickness = property(_get_AssembledThickness, None)
	'''
	Assembled thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	BeltType = property(_get_BeltType, _set_BeltType)
	'''
	Belt type

	:type: recurdyn.BNP.BNPBeltType
	'''
	Color = property(_get_Color, _set_Color)
	'''
	Belt color

	:type: int
	'''
	DisplayNodeID = property(_get_DisplayNodeID, _set_DisplayNodeID)
	'''
	Display node ID

	:type: bool
	'''
	ElementLength = property(_get_ElementLength, None)
	'''
	Element length

	:type: float
	'''
	InitialLongitudinalVelocity = property(_get_InitialLongitudinalVelocity, None)
	'''
	Initial longitudinal velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	Interval = property(_get_Interval, _set_Interval)
	'''
	Interval

	:type: int
	'''
	LowerThickness = property(_get_LowerThickness, None)
	'''
	Lower thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaterialProperty = property(_get_MaterialProperty, None)
	'''
	Material property

	:type: recurdyn.BNP.IBNPBeltBeamMaterialProperty
	'''
	NumberOfElements = property(_get_NumberOfElements, None)
	'''
	Number of elements

	:type: int
	'''
	PassingBodyCollection = property(_get_PassingBodyCollection, None)
	'''
	Passing body collection

	:type: recurdyn.BNP.IBNPPassingBodyCollection
	'''
	Profile = property(_get_Profile, None)
	'''
	Timing belt profile

	:type: recurdyn.BNP.IBNPProfileBeamTiming
	'''
	Radius = property(_get_Radius, None)
	'''
	Radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	StretchedLength = property(_get_StretchedLength, None)
	'''
	Stretched length

	:type: recurdyn.ProcessNet.IDouble
	'''
	UpperThickness = property(_get_UpperThickness, None)
	'''
	Upper thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseInitialLongitudinalVelocity = property(_get_UseInitialLongitudinalVelocity, _set_UseInitialLongitudinalVelocity)
	'''
	Use initial longitudinal velocity

	:type: bool
	'''
	UseUpdateGeometryInformationAutomatically = property(_get_UseUpdateGeometryInformationAutomatically, _set_UseUpdateGeometryInformationAutomatically)
	'''
	Update geometry information automatically

	:type: bool
	'''
	Width = property(_get_Width, None)
	'''
	Width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_BeltType": _set_BeltType,
		"_set_Color": _set_Color,
		"_set_DisplayNodeID": _set_DisplayNodeID,
		"_set_Interval": _set_Interval,
		"_set_UseInitialLongitudinalVelocity": _set_UseInitialLongitudinalVelocity,
		"_set_UseUpdateGeometryInformationAutomatically": _set_UseUpdateGeometryInformationAutomatically,
	}
	_prop_map_get_ = {
		"Angle": (11156, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"AssembledThickness": (11158, 2, (9, 0), (), "AssembledThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"BeltType": (11152, 2, (3, 0), (), "BeltType", '{0BB88860-1CA3-4F91-973F-ACA0600D489B}'),
		"Color": (11150, 2, (19, 0), (), "Color", None),
		"DisplayNodeID": (11151, 2, (11, 0), (), "DisplayNodeID", None),
		"ElementLength": (11162, 2, (5, 0), (), "ElementLength", None),
		"InitialLongitudinalVelocity": (11169, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Interval": (11159, 2, (3, 0), (), "Interval", None),
		"LowerThickness": (11153, 2, (9, 0), (), "LowerThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaterialProperty": (11164, 2, (9, 0), (), "MaterialProperty", '{D9C23616-C0D3-422D-8A74-02654AB2E863}'),
		"NumberOfElements": (11161, 2, (19, 0), (), "NumberOfElements", None),
		"PassingBodyCollection": (11165, 2, (9, 0), (), "PassingBodyCollection", '{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}'),
		"Profile": (11160, 2, (9, 0), (), "Profile", '{3218112D-CC7E-4DC3-A6A4-36A6B33C12B6}'),
		"Radius": (11157, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StretchedLength": (11163, 2, (9, 0), (), "StretchedLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UpperThickness": (11154, 2, (9, 0), (), "UpperThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseInitialLongitudinalVelocity": (11168, 2, (11, 0), (), "UseInitialLongitudinalVelocity", None),
		"UseUpdateGeometryInformationAutomatically": (11170, 2, (11, 0), (), "UseUpdateGeometryInformationAutomatically", None),
		"Width": (11155, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"BeltType": ((11152, LCID, 4, 0),()),
		"Color": ((11150, LCID, 4, 0),()),
		"DisplayNodeID": ((11151, LCID, 4, 0),()),
		"Interval": ((11159, LCID, 4, 0),()),
		"UseInitialLongitudinalVelocity": ((11168, LCID, 4, 0),()),
		"UseUpdateGeometryInformationAutomatically": ((11170, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometryBeltFlat(DispatchBaseClass):
	'''Flat belt geometry'''
	CLSID = IID('{9033BB6E-5115-49FA-83A2-E39301FBFD6C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_CordDistance(self):
		return self._ApplyTypes_(*(22053, 2, (9, 0), (), "CordDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Height(self):
		return self._ApplyTypes_(*(22050, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftConnectionPosition(self):
		return self._ApplyTypes_(*(22054, 2, (5, 0), (), "LeftConnectionPosition", None))
	def _get_RightConnectionPosition(self):
		return self._ApplyTypes_(*(22055, 2, (5, 0), (), "RightConnectionPosition", None))
	def _get_SegmentLength(self):
		return self._ApplyTypes_(*(22052, 2, (9, 0), (), "SegmentLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(22051, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_LeftConnectionPosition(self, value):
		if "LeftConnectionPosition" in self.__dict__: self.__dict__["LeftConnectionPosition"] = value; return
		self._oleobj_.Invoke(*((22054, LCID, 4, 0) + (value,) + ()))
	def _set_RightConnectionPosition(self, value):
		if "RightConnectionPosition" in self.__dict__: self.__dict__["RightConnectionPosition"] = value; return
		self._oleobj_.Invoke(*((22055, LCID, 4, 0) + (value,) + ()))

	CordDistance = property(_get_CordDistance, None)
	'''
	Flat belt cord distance

	:type: recurdyn.ProcessNet.IDouble
	'''
	Height = property(_get_Height, None)
	'''
	Flat belt height

	:type: recurdyn.ProcessNet.IDouble
	'''
	LeftConnectionPosition = property(_get_LeftConnectionPosition, _set_LeftConnectionPosition)
	'''
	Flat belt left connection position

	:type: float
	'''
	RightConnectionPosition = property(_get_RightConnectionPosition, _set_RightConnectionPosition)
	'''
	Flat belt right connection position

	:type: float
	'''
	SegmentLength = property(_get_SegmentLength, None)
	'''
	Flat belt segment length

	:type: recurdyn.ProcessNet.IDouble
	'''
	Width = property(_get_Width, None)
	'''
	Flat belt width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_LeftConnectionPosition": _set_LeftConnectionPosition,
		"_set_RightConnectionPosition": _set_RightConnectionPosition,
	}
	_prop_map_get_ = {
		"CordDistance": (22053, 2, (9, 0), (), "CordDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Height": (22050, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftConnectionPosition": (22054, 2, (5, 0), (), "LeftConnectionPosition", None),
		"RightConnectionPosition": (22055, 2, (5, 0), (), "RightConnectionPosition", None),
		"SegmentLength": (22052, 2, (9, 0), (), "SegmentLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Width": (22051, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"LeftConnectionPosition": ((22054, LCID, 4, 0),()),
		"RightConnectionPosition": ((22055, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometryBeltRibbedV(DispatchBaseClass):
	'''Ribbed_V belt geometry'''
	CLSID = IID('{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Angle(self):
		return self._ApplyTypes_(*(22054, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CordDistance(self):
		return self._ApplyTypes_(*(22059, 2, (9, 0), (), "CordDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Height(self):
		return self._ApplyTypes_(*(22050, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftConnectionPosition(self):
		return self._ApplyTypes_(*(22060, 2, (5, 0), (), "LeftConnectionPosition", None))
	def _get_NumberOfPeak(self):
		return self._ApplyTypes_(*(22056, 2, (19, 0), (), "NumberOfPeak", None))
	def _get_Pitch(self):
		return self._ApplyTypes_(*(22055, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RibHeight(self):
		return self._ApplyTypes_(*(22052, 2, (9, 0), (), "RibHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RibWidth(self):
		return self._ApplyTypes_(*(22057, 2, (5, 0), (), "RibWidth", None))
	def _get_RightConnectionPosition(self):
		return self._ApplyTypes_(*(22061, 2, (5, 0), (), "RightConnectionPosition", None))
	def _get_SegmentLength(self):
		return self._ApplyTypes_(*(22058, 2, (9, 0), (), "SegmentLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(22051, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(22053, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_LeftConnectionPosition(self, value):
		if "LeftConnectionPosition" in self.__dict__: self.__dict__["LeftConnectionPosition"] = value; return
		self._oleobj_.Invoke(*((22060, LCID, 4, 0) + (value,) + ()))
	def _set_NumberOfPeak(self, value):
		if "NumberOfPeak" in self.__dict__: self.__dict__["NumberOfPeak"] = value; return
		self._oleobj_.Invoke(*((22056, LCID, 4, 0) + (value,) + ()))
	def _set_RightConnectionPosition(self, value):
		if "RightConnectionPosition" in self.__dict__: self.__dict__["RightConnectionPosition"] = value; return
		self._oleobj_.Invoke(*((22061, LCID, 4, 0) + (value,) + ()))

	Angle = property(_get_Angle, None)
	'''
	Ribbed_V belt angle

	:type: recurdyn.ProcessNet.IDouble
	'''
	CordDistance = property(_get_CordDistance, None)
	'''
	Ribbed_V belt cord distance

	:type: recurdyn.ProcessNet.IDouble
	'''
	Height = property(_get_Height, None)
	'''
	Ribbed_V belt height

	:type: recurdyn.ProcessNet.IDouble
	'''
	LeftConnectionPosition = property(_get_LeftConnectionPosition, _set_LeftConnectionPosition)
	'''
	Ribbed_V belt left connection position

	:type: float
	'''
	NumberOfPeak = property(_get_NumberOfPeak, _set_NumberOfPeak)
	'''
	Ribbed_V number of peak

	:type: int
	'''
	Pitch = property(_get_Pitch, None)
	'''
	Ribbed_V belt pitch

	:type: recurdyn.ProcessNet.IDouble
	'''
	RibHeight = property(_get_RibHeight, None)
	'''
	Ribbed_V belt rib height

	:type: recurdyn.ProcessNet.IDouble
	'''
	RibWidth = property(_get_RibWidth, None)
	'''
	Ribbed_V belt rib width

	:type: float
	'''
	RightConnectionPosition = property(_get_RightConnectionPosition, _set_RightConnectionPosition)
	'''
	Ribbed_V belt right connection position

	:type: float
	'''
	SegmentLength = property(_get_SegmentLength, None)
	'''
	Ribbed_V belt segment length

	:type: recurdyn.ProcessNet.IDouble
	'''
	Thickness = property(_get_Thickness, None)
	'''
	Ribbed_V belt thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	Width = property(_get_Width, None)
	'''
	Ribbed_V belt width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_LeftConnectionPosition": _set_LeftConnectionPosition,
		"_set_NumberOfPeak": _set_NumberOfPeak,
		"_set_RightConnectionPosition": _set_RightConnectionPosition,
	}
	_prop_map_get_ = {
		"Angle": (22054, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CordDistance": (22059, 2, (9, 0), (), "CordDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Height": (22050, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftConnectionPosition": (22060, 2, (5, 0), (), "LeftConnectionPosition", None),
		"NumberOfPeak": (22056, 2, (19, 0), (), "NumberOfPeak", None),
		"Pitch": (22055, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RibHeight": (22052, 2, (9, 0), (), "RibHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RibWidth": (22057, 2, (5, 0), (), "RibWidth", None),
		"RightConnectionPosition": (22061, 2, (5, 0), (), "RightConnectionPosition", None),
		"SegmentLength": (22058, 2, (9, 0), (), "SegmentLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Thickness": (22051, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Width": (22053, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"LeftConnectionPosition": ((22060, LCID, 4, 0),()),
		"NumberOfPeak": ((22056, LCID, 4, 0),()),
		"RightConnectionPosition": ((22061, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometryBeltShell(DispatchBaseClass):
	'''Shell belt geometry'''
	CLSID = IID('{FD1CA7C1-21FE-488D-88DC-87AF6CC66D8E}')
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
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11163, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody(self, pVal):
		'''
		Delete a passing body
		
		:param pVal: IBNPBody
		'''
		return self._oleobj_.InvokeTypes(11164, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def _get_Color(self):
		return self._ApplyTypes_(*(11150, 2, (19, 0), (), "Color", None))
	def _get_CurlRadiusLateral(self):
		return self._ApplyTypes_(*(11159, 2, (9, 0), (), "CurlRadiusLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CurlRadiusLongitudinal(self):
		return self._ApplyTypes_(*(11158, 2, (9, 0), (), "CurlRadiusLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DisplayNodeID(self):
		return self._ApplyTypes_(*(11151, 2, (11, 0), (), "DisplayNodeID", None))
	def _get_ElementLengthLateral(self):
		return self._ApplyTypes_(*(11157, 2, (5, 0), (), "ElementLengthLateral", None))
	def _get_ElementLengthLongitudinal(self):
		return self._ApplyTypes_(*(11156, 2, (5, 0), (), "ElementLengthLongitudinal", None))
	def _get_InitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(11166, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftThickness(self):
		return self._ApplyTypes_(*(11168, 2, (9, 0), (), "LeftThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaterialProperty(self):
		return self._ApplyTypes_(*(11161, 2, (9, 0), (), "MaterialProperty", '{9BC7A528-18AE-43FF-B8FF-81EBDAF0F812}'))
	def _get_NumberOfElementsLateral(self):
		return self._ApplyTypes_(*(11155, 2, (19, 0), (), "NumberOfElementsLateral", None))
	def _get_NumberOfElementsLongitudinal(self):
		return self._ApplyTypes_(*(11154, 2, (19, 0), (), "NumberOfElementsLongitudinal", None))
	def _get_PassingBodyCollection(self):
		return self._ApplyTypes_(*(11162, 2, (9, 0), (), "PassingBodyCollection", '{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}'))
	def _get_RightThickness(self):
		return self._ApplyTypes_(*(11169, 2, (9, 0), (), "RightThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StretchedLength(self):
		return self._ApplyTypes_(*(11160, 2, (9, 0), (), "StretchedLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(11152, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseInitialLongitudinalVelocity(self):
		return self._ApplyTypes_(*(11165, 2, (11, 0), (), "UseInitialLongitudinalVelocity", None))
	def _get_UseUpdateGeometryInformationAutomatically(self):
		return self._ApplyTypes_(*(11167, 2, (11, 0), (), "UseUpdateGeometryInformationAutomatically", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(11153, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((11150, LCID, 4, 0) + (value,) + ()))
	def _set_DisplayNodeID(self, value):
		if "DisplayNodeID" in self.__dict__: self.__dict__["DisplayNodeID"] = value; return
		self._oleobj_.Invoke(*((11151, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialLongitudinalVelocity(self, value):
		if "UseInitialLongitudinalVelocity" in self.__dict__: self.__dict__["UseInitialLongitudinalVelocity"] = value; return
		self._oleobj_.Invoke(*((11165, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdateGeometryInformationAutomatically(self, value):
		if "UseUpdateGeometryInformationAutomatically" in self.__dict__: self.__dict__["UseUpdateGeometryInformationAutomatically"] = value; return
		self._oleobj_.Invoke(*((11167, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Belt color

	:type: int
	'''
	CurlRadiusLateral = property(_get_CurlRadiusLateral, None)
	'''
	Lateral curl radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	CurlRadiusLongitudinal = property(_get_CurlRadiusLongitudinal, None)
	'''
	Longitudinal curl radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	DisplayNodeID = property(_get_DisplayNodeID, _set_DisplayNodeID)
	'''
	Display node ID

	:type: bool
	'''
	ElementLengthLateral = property(_get_ElementLengthLateral, None)
	'''
	Lateral element length

	:type: float
	'''
	ElementLengthLongitudinal = property(_get_ElementLengthLongitudinal, None)
	'''
	Longitudinal element length

	:type: float
	'''
	InitialLongitudinalVelocity = property(_get_InitialLongitudinalVelocity, None)
	'''
	Initial longitudinal velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	LeftThickness = property(_get_LeftThickness, None)
	'''
	Left Thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaterialProperty = property(_get_MaterialProperty, None)
	'''
	Material property

	:type: recurdyn.BNP.IBNPBeltShellMaterialProperty
	'''
	NumberOfElementsLateral = property(_get_NumberOfElementsLateral, None)
	'''
	Lateral number of elements

	:type: int
	'''
	NumberOfElementsLongitudinal = property(_get_NumberOfElementsLongitudinal, None)
	'''
	Longitudinal number of elements

	:type: int
	'''
	PassingBodyCollection = property(_get_PassingBodyCollection, None)
	'''
	Passing body collection

	:type: recurdyn.BNP.IBNPPassingBodyCollection
	'''
	RightThickness = property(_get_RightThickness, None)
	'''
	Right Thickness

	:type: recurdyn.ProcessNet.IDouble
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
	UseInitialLongitudinalVelocity = property(_get_UseInitialLongitudinalVelocity, _set_UseInitialLongitudinalVelocity)
	'''
	Use initial longitudinal velocity

	:type: bool
	'''
	UseUpdateGeometryInformationAutomatically = property(_get_UseUpdateGeometryInformationAutomatically, _set_UseUpdateGeometryInformationAutomatically)
	'''
	Update geometry information automatically

	:type: bool
	'''
	Width = property(_get_Width, None)
	'''
	Width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_DisplayNodeID": _set_DisplayNodeID,
		"_set_UseInitialLongitudinalVelocity": _set_UseInitialLongitudinalVelocity,
		"_set_UseUpdateGeometryInformationAutomatically": _set_UseUpdateGeometryInformationAutomatically,
	}
	_prop_map_get_ = {
		"Color": (11150, 2, (19, 0), (), "Color", None),
		"CurlRadiusLateral": (11159, 2, (9, 0), (), "CurlRadiusLateral", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CurlRadiusLongitudinal": (11158, 2, (9, 0), (), "CurlRadiusLongitudinal", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DisplayNodeID": (11151, 2, (11, 0), (), "DisplayNodeID", None),
		"ElementLengthLateral": (11157, 2, (5, 0), (), "ElementLengthLateral", None),
		"ElementLengthLongitudinal": (11156, 2, (5, 0), (), "ElementLengthLongitudinal", None),
		"InitialLongitudinalVelocity": (11166, 2, (9, 0), (), "InitialLongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftThickness": (11168, 2, (9, 0), (), "LeftThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaterialProperty": (11161, 2, (9, 0), (), "MaterialProperty", '{9BC7A528-18AE-43FF-B8FF-81EBDAF0F812}'),
		"NumberOfElementsLateral": (11155, 2, (19, 0), (), "NumberOfElementsLateral", None),
		"NumberOfElementsLongitudinal": (11154, 2, (19, 0), (), "NumberOfElementsLongitudinal", None),
		"PassingBodyCollection": (11162, 2, (9, 0), (), "PassingBodyCollection", '{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}'),
		"RightThickness": (11169, 2, (9, 0), (), "RightThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StretchedLength": (11160, 2, (9, 0), (), "StretchedLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Thickness": (11152, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseInitialLongitudinalVelocity": (11165, 2, (11, 0), (), "UseInitialLongitudinalVelocity", None),
		"UseUpdateGeometryInformationAutomatically": (11167, 2, (11, 0), (), "UseUpdateGeometryInformationAutomatically", None),
		"Width": (11153, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Color": ((11150, LCID, 4, 0),()),
		"DisplayNodeID": ((11151, LCID, 4, 0),()),
		"UseInitialLongitudinalVelocity": ((11165, LCID, 4, 0),()),
		"UseUpdateGeometryInformationAutomatically": ((11167, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometryBeltTiming(DispatchBaseClass):
	'''Timing belt geometry'''
	CLSID = IID('{28B9F577-7066-4B2E-80A2-AF7D140593AC}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Angle(self):
		return self._ApplyTypes_(*(22052, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CordDistance(self):
		return self._ApplyTypes_(*(22054, 2, (9, 0), (), "CordDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftConnectionPosition(self):
		return self._ApplyTypes_(*(22055, 2, (5, 0), (), "LeftConnectionPosition", None))
	def _get_NominalHeight(self):
		return self._ApplyTypes_(*(22059, 2, (9, 0), (), "NominalHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Pitch(self):
		return self._ApplyTypes_(*(22051, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(22062, 2, (9, 0), (), "Profile", '{94B262DF-F40E-41A3-AEBF-98580C067EE0}'))
	def _get_RightConnectionPosition(self):
		return self._ApplyTypes_(*(22056, 2, (5, 0), (), "RightConnectionPosition", None))
	def _get_ToothHeight(self):
		return self._ApplyTypes_(*(22058, 2, (9, 0), (), "ToothHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ToothLength(self):
		return self._ApplyTypes_(*(22057, 2, (9, 0), (), "ToothLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ToothProfileType(self):
		return self._ApplyTypes_(*(22050, 2, (3, 0), (), "ToothProfileType", '{E0737D18-B0FC-4DEF-8DC2-AC308C6A21A8}'))
	def _get_ToothRootRadius(self):
		return self._ApplyTypes_(*(22060, 2, (9, 0), (), "ToothRootRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ToothTipRadius(self):
		return self._ApplyTypes_(*(22061, 2, (9, 0), (), "ToothTipRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(22053, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_LeftConnectionPosition(self, value):
		if "LeftConnectionPosition" in self.__dict__: self.__dict__["LeftConnectionPosition"] = value; return
		self._oleobj_.Invoke(*((22055, LCID, 4, 0) + (value,) + ()))
	def _set_RightConnectionPosition(self, value):
		if "RightConnectionPosition" in self.__dict__: self.__dict__["RightConnectionPosition"] = value; return
		self._oleobj_.Invoke(*((22056, LCID, 4, 0) + (value,) + ()))
	def _set_ToothProfileType(self, value):
		if "ToothProfileType" in self.__dict__: self.__dict__["ToothProfileType"] = value; return
		self._oleobj_.Invoke(*((22050, LCID, 4, 0) + (value,) + ()))

	Angle = property(_get_Angle, None)
	'''
	Timing belt angle

	:type: recurdyn.ProcessNet.IDouble
	'''
	CordDistance = property(_get_CordDistance, None)
	'''
	Timing belt cord distance

	:type: recurdyn.ProcessNet.IDouble
	'''
	LeftConnectionPosition = property(_get_LeftConnectionPosition, _set_LeftConnectionPosition)
	'''
	Timing belt left connection position

	:type: float
	'''
	NominalHeight = property(_get_NominalHeight, None)
	'''
	Timing belt nominal height

	:type: recurdyn.ProcessNet.IDouble
	'''
	Pitch = property(_get_Pitch, None)
	'''
	Timing belt pitch

	:type: recurdyn.ProcessNet.IDouble
	'''
	Profile = property(_get_Profile, None)
	'''
	Timing belt profile

	:type: recurdyn.BNP.IBNPProfileBeltTiming
	'''
	RightConnectionPosition = property(_get_RightConnectionPosition, _set_RightConnectionPosition)
	'''
	Timing belt right connection position

	:type: float
	'''
	ToothHeight = property(_get_ToothHeight, None)
	'''
	Timing belt tooth height

	:type: recurdyn.ProcessNet.IDouble
	'''
	ToothLength = property(_get_ToothLength, None)
	'''
	Timing belt tooth length

	:type: recurdyn.ProcessNet.IDouble
	'''
	ToothProfileType = property(_get_ToothProfileType, _set_ToothProfileType)
	'''
	Timing belt tooth profile type

	:type: recurdyn.BNP.BNPToothProfileType
	'''
	ToothRootRadius = property(_get_ToothRootRadius, None)
	'''
	Timing belt tooth root radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	ToothTipRadius = property(_get_ToothTipRadius, None)
	'''
	Timing belt tooth tip radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	Width = property(_get_Width, None)
	'''
	Timing belt width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_LeftConnectionPosition": _set_LeftConnectionPosition,
		"_set_RightConnectionPosition": _set_RightConnectionPosition,
		"_set_ToothProfileType": _set_ToothProfileType,
	}
	_prop_map_get_ = {
		"Angle": (22052, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CordDistance": (22054, 2, (9, 0), (), "CordDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftConnectionPosition": (22055, 2, (5, 0), (), "LeftConnectionPosition", None),
		"NominalHeight": (22059, 2, (9, 0), (), "NominalHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Pitch": (22051, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Profile": (22062, 2, (9, 0), (), "Profile", '{94B262DF-F40E-41A3-AEBF-98580C067EE0}'),
		"RightConnectionPosition": (22056, 2, (5, 0), (), "RightConnectionPosition", None),
		"ToothHeight": (22058, 2, (9, 0), (), "ToothHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ToothLength": (22057, 2, (9, 0), (), "ToothLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ToothProfileType": (22050, 2, (3, 0), (), "ToothProfileType", '{E0737D18-B0FC-4DEF-8DC2-AC308C6A21A8}'),
		"ToothRootRadius": (22060, 2, (9, 0), (), "ToothRootRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ToothTipRadius": (22061, 2, (9, 0), (), "ToothTipRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Width": (22053, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"LeftConnectionPosition": ((22055, LCID, 4, 0),()),
		"RightConnectionPosition": ((22056, LCID, 4, 0),()),
		"ToothProfileType": ((22050, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometryBeltV(DispatchBaseClass):
	'''V belt geometry'''
	CLSID = IID('{185F6935-19D9-4664-91A4-C564A61DF014}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Angle(self):
		return self._ApplyTypes_(*(22053, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CordDistance(self):
		return self._ApplyTypes_(*(22055, 2, (9, 0), (), "CordDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Height(self):
		return self._ApplyTypes_(*(22050, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftConnectionPosition(self):
		return self._ApplyTypes_(*(22056, 2, (5, 0), (), "LeftConnectionPosition", None))
	def _get_RightConnectionPosition(self):
		return self._ApplyTypes_(*(22057, 2, (5, 0), (), "RightConnectionPosition", None))
	def _get_SegmentLength(self):
		return self._ApplyTypes_(*(22054, 2, (9, 0), (), "SegmentLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(22051, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(22052, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_LeftConnectionPosition(self, value):
		if "LeftConnectionPosition" in self.__dict__: self.__dict__["LeftConnectionPosition"] = value; return
		self._oleobj_.Invoke(*((22056, LCID, 4, 0) + (value,) + ()))
	def _set_RightConnectionPosition(self, value):
		if "RightConnectionPosition" in self.__dict__: self.__dict__["RightConnectionPosition"] = value; return
		self._oleobj_.Invoke(*((22057, LCID, 4, 0) + (value,) + ()))

	Angle = property(_get_Angle, None)
	'''
	V belt angle

	:type: recurdyn.ProcessNet.IDouble
	'''
	CordDistance = property(_get_CordDistance, None)
	'''
	V belt cord distance

	:type: recurdyn.ProcessNet.IDouble
	'''
	Height = property(_get_Height, None)
	'''
	V belt height

	:type: recurdyn.ProcessNet.IDouble
	'''
	LeftConnectionPosition = property(_get_LeftConnectionPosition, _set_LeftConnectionPosition)
	'''
	V belt left connection position

	:type: float
	'''
	RightConnectionPosition = property(_get_RightConnectionPosition, _set_RightConnectionPosition)
	'''
	V belt right connection position

	:type: float
	'''
	SegmentLength = property(_get_SegmentLength, None)
	'''
	V belt segment length

	:type: recurdyn.ProcessNet.IDouble
	'''
	Thickness = property(_get_Thickness, None)
	'''
	V belt thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	Width = property(_get_Width, None)
	'''
	V belt width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_LeftConnectionPosition": _set_LeftConnectionPosition,
		"_set_RightConnectionPosition": _set_RightConnectionPosition,
	}
	_prop_map_get_ = {
		"Angle": (22053, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CordDistance": (22055, 2, (9, 0), (), "CordDistance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Height": (22050, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftConnectionPosition": (22056, 2, (5, 0), (), "LeftConnectionPosition", None),
		"RightConnectionPosition": (22057, 2, (5, 0), (), "RightConnectionPosition", None),
		"SegmentLength": (22054, 2, (9, 0), (), "SegmentLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Thickness": (22051, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Width": (22052, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"LeftConnectionPosition": ((22056, LCID, 4, 0),()),
		"RightConnectionPosition": ((22057, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometryPulleyCrown(DispatchBaseClass):
	'''BNP crown pulley body geometry'''
	CLSID = IID('{7ACC0B53-41A1-45D3-A170-8C7FD07C4E66}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssembledRadius(self):
		return self._ApplyTypes_(*(22103, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(22104, 2, (9, 0), (), "Profile", '{D5E4799C-AD42-492B-BF4F-C9B2AEAD3917}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(22100, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseAssembledRadius(self):
		return self._ApplyTypes_(*(22102, 2, (11, 0), (), "UseAssembledRadius", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(22101, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_UseAssembledRadius(self, value):
		if "UseAssembledRadius" in self.__dict__: self.__dict__["UseAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((22102, LCID, 4, 0) + (value,) + ()))

	AssembledRadius = property(_get_AssembledRadius, None)
	'''
	Assembled radius of the crown pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Profile = property(_get_Profile, None)
	'''
	Profile

	:type: recurdyn.BNP.IBNPProfilePulleyCrown
	'''
	Radius = property(_get_Radius, None)
	'''
	Radius of the crown pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseAssembledRadius = property(_get_UseAssembledRadius, _set_UseAssembledRadius)
	'''
	Assembled radius of the crown pulley.

	:type: bool
	'''
	Width = property(_get_Width, None)
	'''
	Width of the crown pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_UseAssembledRadius": _set_UseAssembledRadius,
	}
	_prop_map_get_ = {
		"AssembledRadius": (22103, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Profile": (22104, 2, (9, 0), (), "Profile", '{D5E4799C-AD42-492B-BF4F-C9B2AEAD3917}'),
		"Radius": (22100, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseAssembledRadius": (22102, 2, (11, 0), (), "UseAssembledRadius", None),
		"Width": (22101, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"UseAssembledRadius": ((22102, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometryPulleyFlange(DispatchBaseClass):
	'''BNP flange pulley body geometry'''
	CLSID = IID('{D15BA410-27CD-4BBF-8B63-7157B683989A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Angle(self):
		return self._ApplyTypes_(*(22102, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(22100, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(22101, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	Angle = property(_get_Angle, None)
	'''
	Angle of the flange pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Radius = property(_get_Radius, None)
	'''
	Radius of the flange pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Width = property(_get_Width, None)
	'''
	Width of the flange pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Angle": (22102, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Radius": (22100, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Width": (22101, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IBNPGeometryPulleyPrism(DispatchBaseClass):
	'''BNP prism pulley body geometry'''
	CLSID = IID('{CAFDBC3C-C51A-412A-80E1-7F58BB60F820}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssembledRadius(self):
		return self._ApplyTypes_(*(22101, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(22102, 2, (9, 0), (), "Profile", '{1FA326B0-7EA6-4D8C-A58B-7E69947E8B6D}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(22100, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	AssembledRadius = property(_get_AssembledRadius, None)
	'''
	Assembled radius of the prism pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Profile = property(_get_Profile, None)
	'''
	Profile

	:type: recurdyn.BNP.IBNPProfilePulleyPrism
	'''
	Width = property(_get_Width, None)
	'''
	Width of the prism pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"AssembledRadius": (22101, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Profile": (22102, 2, (9, 0), (), "Profile", '{1FA326B0-7EA6-4D8C-A58B-7E69947E8B6D}'),
		"Width": (22100, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IBNPGeometryPulleyRibbedV(DispatchBaseClass):
	'''BNP ribbed_v pulley body geometry'''
	CLSID = IID('{32EA063C-BD96-48EA-93C6-C3DAA3961197}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Angle(self):
		return self._ApplyTypes_(*(22104, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_AssembledRadius(self):
		return self._ApplyTypes_(*(22108, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InnerRadius(self):
		return self._ApplyTypes_(*(22100, 2, (9, 0), (), "InnerRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_NumberOfGroove(self):
		return self._ApplyTypes_(*(22106, 2, (19, 0), (), "NumberOfGroove", None))
	def _get_OuterRadius(self):
		return self._ApplyTypes_(*(22102, 2, (9, 0), (), "OuterRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Pitch(self):
		return self._ApplyTypes_(*(22105, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PulleyWidth(self):
		return self._ApplyTypes_(*(22107, 2, (5, 0), (), "PulleyWidth", None))
	def _get_Radius(self):
		return self._ApplyTypes_(*(22101, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(22103, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_NumberOfGroove(self, value):
		if "NumberOfGroove" in self.__dict__: self.__dict__["NumberOfGroove"] = value; return
		self._oleobj_.Invoke(*((22106, LCID, 4, 0) + (value,) + ()))

	Angle = property(_get_Angle, None)
	'''
	Angle of the ribbed_v pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	AssembledRadius = property(_get_AssembledRadius, None)
	'''
	Assembled radius of the ribbed_v pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	InnerRadius = property(_get_InnerRadius, None)
	'''
	Inner radius of the ribbed_v pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	NumberOfGroove = property(_get_NumberOfGroove, _set_NumberOfGroove)
	'''
	Number of groove

	:type: int
	'''
	OuterRadius = property(_get_OuterRadius, None)
	'''
	Outer radius of the ribbed_v pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Pitch = property(_get_Pitch, None)
	'''
	Pitch of the ribbed_v pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	PulleyWidth = property(_get_PulleyWidth, None)
	'''
	Pulley width of the ribbed_v pulley.

	:type: float
	'''
	Radius = property(_get_Radius, None)
	'''
	Radius of the ribbed_v pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Width = property(_get_Width, None)
	'''
	Width of the ribbed_v pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_NumberOfGroove": _set_NumberOfGroove,
	}
	_prop_map_get_ = {
		"Angle": (22104, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"AssembledRadius": (22108, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InnerRadius": (22100, 2, (9, 0), (), "InnerRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"NumberOfGroove": (22106, 2, (19, 0), (), "NumberOfGroove", None),
		"OuterRadius": (22102, 2, (9, 0), (), "OuterRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Pitch": (22105, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PulleyWidth": (22107, 2, (5, 0), (), "PulleyWidth", None),
		"Radius": (22101, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Width": (22103, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"NumberOfGroove": ((22106, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometryPulleyRoller(DispatchBaseClass):
	'''BNP roller pulley body geometry'''
	CLSID = IID('{530E037B-C319-4E08-A507-77020D1582D4}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssembledRadius(self):
		return self._ApplyTypes_(*(22102, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(22100, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(22101, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	AssembledRadius = property(_get_AssembledRadius, None)
	'''
	Assembled radius of the pulley roller.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Radius = property(_get_Radius, None)
	'''
	Radius of the pulley roller.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Width = property(_get_Width, None)
	'''
	Width of the pulley roller.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"AssembledRadius": (22102, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Radius": (22100, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Width": (22101, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IBNPGeometryPulleyTiming(DispatchBaseClass):
	'''BNP timing pulley body geometry'''
	CLSID = IID('{73E882E6-E6A2-41EB-B965-F386ADD519E8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AddenRadius(self):
		return self._ApplyTypes_(*(22112, 2, (9, 0), (), "AddenRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Angle(self):
		return self._ApplyTypes_(*(22102, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_AssembledRadius(self):
		return self._ApplyTypes_(*(22117, 2, (5, 0), (), "AssembledRadius", None))
	def _get_AssemblyInformationType(self):
		return self._ApplyTypes_(*(22116, 2, (3, 0), (), "AssemblyInformationType", '{2237E8C8-FFDD-40BE-A9F2-6D06738D0389}'))
	def _get_BaseRadius(self):
		return self._ApplyTypes_(*(22110, 2, (9, 0), (), "BaseRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DedenRadius(self):
		return self._ApplyTypes_(*(22109, 2, (9, 0), (), "DedenRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FlangeHeight(self):
		return self._ApplyTypes_(*(22113, 2, (9, 0), (), "FlangeHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FlangeWidth(self):
		return self._ApplyTypes_(*(22115, 2, (9, 0), (), "FlangeWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_NumberOfTeeth(self):
		return self._ApplyTypes_(*(22101, 2, (19, 0), (), "NumberOfTeeth", None))
	def _get_OutsideDiameter(self):
		return self._ApplyTypes_(*(22107, 2, (9, 0), (), "OutsideDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PitchRadius(self):
		return self._ApplyTypes_(*(22111, 2, (9, 0), (), "PitchRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PulleyRadius(self):
		return self._ApplyTypes_(*(22108, 2, (9, 0), (), "PulleyRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PulleyType(self):
		return self._ApplyTypes_(*(22100, 2, (3, 0), (), "PulleyType", '{45F846EF-57B0-4496-A5F4-774D896B5038}'))
	def _get_PulleyWidth(self):
		return self._ApplyTypes_(*(22114, 2, (9, 0), (), "PulleyWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadialDistance(self):
		return self._ApplyTypes_(*(22118, 2, (5, 0), (), "RadialDistance", None))
	def _get_ToothHeight(self):
		return self._ApplyTypes_(*(22103, 2, (9, 0), (), "ToothHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ToothLength(self):
		return self._ApplyTypes_(*(22104, 2, (9, 0), (), "ToothLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ToothRootRadius(self):
		return self._ApplyTypes_(*(22105, 2, (9, 0), (), "ToothRootRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ToothTipRadius(self):
		return self._ApplyTypes_(*(22106, 2, (9, 0), (), "ToothTipRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_AssembledRadius(self, value):
		if "AssembledRadius" in self.__dict__: self.__dict__["AssembledRadius"] = value; return
		self._oleobj_.Invoke(*((22117, LCID, 4, 0) + (value,) + ()))
	def _set_AssemblyInformationType(self, value):
		if "AssemblyInformationType" in self.__dict__: self.__dict__["AssemblyInformationType"] = value; return
		self._oleobj_.Invoke(*((22116, LCID, 4, 0) + (value,) + ()))
	def _set_NumberOfTeeth(self, value):
		if "NumberOfTeeth" in self.__dict__: self.__dict__["NumberOfTeeth"] = value; return
		self._oleobj_.Invoke(*((22101, LCID, 4, 0) + (value,) + ()))
	def _set_PulleyType(self, value):
		if "PulleyType" in self.__dict__: self.__dict__["PulleyType"] = value; return
		self._oleobj_.Invoke(*((22100, LCID, 4, 0) + (value,) + ()))
	def _set_RadialDistance(self, value):
		if "RadialDistance" in self.__dict__: self.__dict__["RadialDistance"] = value; return
		self._oleobj_.Invoke(*((22118, LCID, 4, 0) + (value,) + ()))

	AddenRadius = property(_get_AddenRadius, None)
	'''
	Adden radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	Angle = property(_get_Angle, None)
	'''
	Angle

	:type: recurdyn.ProcessNet.IDouble
	'''
	AssembledRadius = property(_get_AssembledRadius, _set_AssembledRadius)
	'''
	Assembled radius.

	:type: float
	'''
	AssemblyInformationType = property(_get_AssemblyInformationType, _set_AssemblyInformationType)
	'''
	Assembly information

	:type: recurdyn.BNP.BNPAssemblyInformationType
	'''
	BaseRadius = property(_get_BaseRadius, None)
	'''
	Base radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	DedenRadius = property(_get_DedenRadius, None)
	'''
	Deden radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	FlangeHeight = property(_get_FlangeHeight, None)
	'''
	Flange height

	:type: recurdyn.ProcessNet.IDouble
	'''
	FlangeWidth = property(_get_FlangeWidth, None)
	'''
	Flange width

	:type: recurdyn.ProcessNet.IDouble
	'''
	NumberOfTeeth = property(_get_NumberOfTeeth, _set_NumberOfTeeth)
	'''
	Number of teeth

	:type: int
	'''
	OutsideDiameter = property(_get_OutsideDiameter, None)
	'''
	Outside diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	PitchRadius = property(_get_PitchRadius, None)
	'''
	Pitch radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	PulleyRadius = property(_get_PulleyRadius, None)
	'''
	Pulley radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	PulleyType = property(_get_PulleyType, _set_PulleyType)
	'''
	Timing pulley type

	:type: recurdyn.BNP.BNPPulleyType
	'''
	PulleyWidth = property(_get_PulleyWidth, None)
	'''
	Pulley width

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadialDistance = property(_get_RadialDistance, _set_RadialDistance)
	'''
	Radial radius

	:type: float
	'''
	ToothHeight = property(_get_ToothHeight, None)
	'''
	Tooth height

	:type: recurdyn.ProcessNet.IDouble
	'''
	ToothLength = property(_get_ToothLength, None)
	'''
	Tooth length

	:type: recurdyn.ProcessNet.IDouble
	'''
	ToothRootRadius = property(_get_ToothRootRadius, None)
	'''
	Tooth root radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	ToothTipRadius = property(_get_ToothTipRadius, None)
	'''
	Tooth tip radius

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_AssembledRadius": _set_AssembledRadius,
		"_set_AssemblyInformationType": _set_AssemblyInformationType,
		"_set_NumberOfTeeth": _set_NumberOfTeeth,
		"_set_PulleyType": _set_PulleyType,
		"_set_RadialDistance": _set_RadialDistance,
	}
	_prop_map_get_ = {
		"AddenRadius": (22112, 2, (9, 0), (), "AddenRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Angle": (22102, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"AssembledRadius": (22117, 2, (5, 0), (), "AssembledRadius", None),
		"AssemblyInformationType": (22116, 2, (3, 0), (), "AssemblyInformationType", '{2237E8C8-FFDD-40BE-A9F2-6D06738D0389}'),
		"BaseRadius": (22110, 2, (9, 0), (), "BaseRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DedenRadius": (22109, 2, (9, 0), (), "DedenRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FlangeHeight": (22113, 2, (9, 0), (), "FlangeHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FlangeWidth": (22115, 2, (9, 0), (), "FlangeWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"NumberOfTeeth": (22101, 2, (19, 0), (), "NumberOfTeeth", None),
		"OutsideDiameter": (22107, 2, (9, 0), (), "OutsideDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PitchRadius": (22111, 2, (9, 0), (), "PitchRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PulleyRadius": (22108, 2, (9, 0), (), "PulleyRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PulleyType": (22100, 2, (3, 0), (), "PulleyType", '{45F846EF-57B0-4496-A5F4-774D896B5038}'),
		"PulleyWidth": (22114, 2, (9, 0), (), "PulleyWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadialDistance": (22118, 2, (5, 0), (), "RadialDistance", None),
		"ToothHeight": (22103, 2, (9, 0), (), "ToothHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ToothLength": (22104, 2, (9, 0), (), "ToothLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ToothRootRadius": (22105, 2, (9, 0), (), "ToothRootRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ToothTipRadius": (22106, 2, (9, 0), (), "ToothTipRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"AssembledRadius": ((22117, LCID, 4, 0),()),
		"AssemblyInformationType": ((22116, LCID, 4, 0),()),
		"NumberOfTeeth": ((22101, LCID, 4, 0),()),
		"PulleyType": ((22100, LCID, 4, 0),()),
		"RadialDistance": ((22118, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IBNPGeometryPulleyV(DispatchBaseClass):
	'''BNP V pulley body geometry'''
	CLSID = IID('{CB8A9B5A-33D9-4AE8-8EB6-AE1CD753C5AF}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Angle(self):
		return self._ApplyTypes_(*(22105, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_AssembledRadius(self):
		return self._ApplyTypes_(*(22106, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InnerRadius(self):
		return self._ApplyTypes_(*(22100, 2, (9, 0), (), "InnerRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_OuterRadius(self):
		return self._ApplyTypes_(*(22102, 2, (9, 0), (), "OuterRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PulleyWidth(self):
		return self._ApplyTypes_(*(22104, 2, (9, 0), (), "PulleyWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Radius(self):
		return self._ApplyTypes_(*(22101, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(22103, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	Angle = property(_get_Angle, None)
	'''
	Angle of the V pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	AssembledRadius = property(_get_AssembledRadius, None)
	'''
	Assembled radius of the V pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	InnerRadius = property(_get_InnerRadius, None)
	'''
	Inner radius of the V pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	OuterRadius = property(_get_OuterRadius, None)
	'''
	Outer radius of the V pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	PulleyWidth = property(_get_PulleyWidth, None)
	'''
	Pulley width of the V pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Radius = property(_get_Radius, None)
	'''
	Radius of the V pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Width = property(_get_Width, None)
	'''
	Width of the V pulley.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Angle": (22105, 2, (9, 0), (), "Angle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"AssembledRadius": (22106, 2, (9, 0), (), "AssembledRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InnerRadius": (22100, 2, (9, 0), (), "InnerRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"OuterRadius": (22102, 2, (9, 0), (), "OuterRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PulleyWidth": (22104, 2, (9, 0), (), "PulleyWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Radius": (22101, 2, (9, 0), (), "Radius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Width": (22103, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IBNPPassingBodyCollection(DispatchBaseClass):
	'''IBNPPassingBodyCollection'''
	CLSID = IID('{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}')
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

class IBNPProfile(DispatchBaseClass):
	'''BNP profile'''
	CLSID = IID('{DFFBFB64-8139-4586-A092-98FFE8D298DA}')
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
		return self._oleobj_.InvokeTypes(33101, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(33102, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_PointCollection(self):
		return self._ApplyTypes_(*(33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	PointCollection = property(_get_PointCollection, None)
	'''
	Point with radius collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PointCollection": (33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
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

class IBNPProfileBeamTiming(DispatchBaseClass):
	'''Belt timing beam profile'''
	CLSID = IID('{3218112D-CC7E-4DC3-A6A4-36A6B33C12B6}')
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
		return self._oleobj_.InvokeTypes(33101, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(33102, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_PointCollection(self):
		return self._ApplyTypes_(*(33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	PointCollection = property(_get_PointCollection, None)
	'''
	Point with radius collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PointCollection": (33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
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

class IBNPProfileBeltTiming(DispatchBaseClass):
	'''Timing Belt profile'''
	CLSID = IID('{94B262DF-F40E-41A3-AEBF-98580C067EE0}')
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
		return self._oleobj_.InvokeTypes(33101, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(33102, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_PointCollection(self):
		return self._ApplyTypes_(*(33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	PointCollection = property(_get_PointCollection, None)
	'''
	Point with radius collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PointCollection": (33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
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

class IBNPProfilePulleyCrown(DispatchBaseClass):
	'''Pulley Crown profile'''
	CLSID = IID('{D5E4799C-AD42-492B-BF4F-C9B2AEAD3917}')
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
		return self._oleobj_.InvokeTypes(33101, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(33102, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_PointCollection(self):
		return self._ApplyTypes_(*(33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	PointCollection = property(_get_PointCollection, None)
	'''
	Point with radius collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PointCollection": (33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
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

class IBNPProfilePulleyPrism(DispatchBaseClass):
	'''Pulley Prism profile'''
	CLSID = IID('{1FA326B0-7EA6-4D8C-A58B-7E69947E8B6D}')
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
		return self._oleobj_.InvokeTypes(33101, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(33102, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_PointCollection(self):
		return self._ApplyTypes_(*(33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	PointCollection = property(_get_PointCollection, None)
	'''
	Point with radius collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PointCollection": (33100, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
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

class IBNPSubSystem(DispatchBaseClass):
	'''Belt subsystem'''
	CLSID = IID('{9E5B67A9-F6AF-4BDE-B7F5-FD7926E2B2CC}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateBNPAssembly(self, strName, pBeltClone, pBodyList, pInOutList, uiNumberOfBelt):
		'''
		Create BNP assembly
		
		:param strName: str
		:param pBeltClone: IBNPBeltClone
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfBelt: int
		:rtype: recurdyn.BNP.IBNPAssembly
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(11012, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (19, 1)),strName
			, pBeltClone, pBodyList, pInOutList, uiNumberOfBelt)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBNPAssembly', '{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')
		return ret

	def CreateBNPAssembly2D(self, strName, pBeltClone, pBodyList, pInOutList, pDirection, uiNumberOfBelt):
		'''
		Create 2D Belt  assembly
		
		:param strName: str
		:param pBeltClone: IBNPBeltClone
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param pDirection: list[float]
		:param uiNumberOfBelt: int
		:rtype: recurdyn.BNP.IBNPAssembly2D
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(11026, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (8197, 1), (19, 1)),strName
			, pBeltClone, pBodyList, pInOutList, pDirection, uiNumberOfBelt
			)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBNPAssembly2D', '{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}')
		return ret

	def CreateBNPAssemblyWithAutomaticTimingPulleyAlignment(self, strName, pBeltClone, pBodyList, pInOutList, uiNumberOfBelt):
		'''
		Create BNP assembly and fit timing pulley to assembly
		
		:param strName: str
		:param pBeltClone: IBNPBeltClone
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfBelt: int
		:rtype: recurdyn.BNP.IBNPAssembly
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(11037, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (19, 1)),strName
			, pBeltClone, pBodyList, pInOutList, uiNumberOfBelt)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBNPAssemblyWithAutomaticTimingPulleyAlignment', '{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')
		return ret

	def CreateBNPBeltGroup(self, strName, pBodyList, pInOutList):
		'''
		obsolete
		
		:param strName: str
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:rtype: recurdyn.BNP.IBNPBeltGroup
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(11030, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1)),strName
			, pBodyList, pInOutList)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBNPBeltGroup', '{80511C7B-B89C-4FA4-B21C-A9A7182B0E61}')
		return ret

	def CreateBeltCloneFlat(self, strName, pPoint):
		'''
		Create a flat belt
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBeltCloneFlat
		'''
		ret = self._oleobj_.InvokeTypes(11001, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBeltCloneFlat', '{F60BB117-D220-4FD8-B603-74573A033D40}')
		return ret

	def CreateBeltCloneRibbedV(self, strName, pPoint):
		'''
		Create a ribbed v belt
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBeltCloneRibbedV
		'''
		ret = self._oleobj_.InvokeTypes(11003, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBeltCloneRibbedV', '{1DD37F48-A065-4B60-BA2D-5A2BFB10AB67}')
		return ret

	def CreateBeltCloneTiming(self, strName, pPoint):
		'''
		Create a timing belt
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBeltCloneTiming
		'''
		ret = self._oleobj_.InvokeTypes(11004, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBeltCloneTiming', '{7D32C453-E2E6-413F-8F69-C66F17CE38C6}')
		return ret

	def CreateBeltCloneV(self, strName, pPoint):
		'''
		Create a v belt
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBeltCloneV
		'''
		ret = self._oleobj_.InvokeTypes(11002, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBeltCloneV', '{8FC53768-BC25-4B05-BE34-6E537955559C}')
		return ret

	def CreateBody2DArcGuide(self, strName, pPoint):
		'''
		Create a 2D arc guide body
		
		:param strName: str
		:param pPoint: list[object]
		:rtype: recurdyn.BNP.IBNPBody2DGuideArc
		'''
		_pPoint_type = True if pPoint and isinstance(pPoint[0], win32com.client.VARIANT) else False
		if not _pPoint_type:
			pPoint = [win32com.client.VARIANT(12, _data) for _data in pPoint]

		ret = self._oleobj_.InvokeTypes(11032, LCID, 1, (9, 0), ((8, 1), (8204, 1)),strName
			, pPoint)

		if not _pPoint_type:
			pPoint = [_data.value for _data in pPoint]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBody2DArcGuide', '{3CD85FDD-669E-47E0-A0BC-165B3BACBAC5}')
		return ret

	def CreateBody2DLinearGuide(self, strName, pPoint):
		'''
		Create a 2D linear guide body
		
		:param strName: str
		:param pPoint: list[object]
		:rtype: recurdyn.BNP.IBNPBody2DGuideLinear
		'''
		_pPoint_type = True if pPoint and isinstance(pPoint[0], win32com.client.VARIANT) else False
		if not _pPoint_type:
			pPoint = [win32com.client.VARIANT(12, _data) for _data in pPoint]

		ret = self._oleobj_.InvokeTypes(11031, LCID, 1, (9, 0), ((8, 1), (8204, 1)),strName
			, pPoint)

		if not _pPoint_type:
			pPoint = [_data.value for _data in pPoint]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBody2DLinearGuide', '{6496CE67-5383-4DDF-9FA1-CC2614D1B96C}')
		return ret

	def CreateBodyBeltBeam(self, strName, pMultiPoint):
		'''
		Create a beam belt
		
		:param strName: str
		:param pMultiPoint: list[object]
		:rtype: recurdyn.BNP.IBNPBodyBeltBeam
		'''
		_pMultiPoint_type = True if pMultiPoint and isinstance(pMultiPoint[0], win32com.client.VARIANT) else False
		if not _pMultiPoint_type:
			pMultiPoint = [win32com.client.VARIANT(12, _data) for _data in pMultiPoint]

		ret = self._oleobj_.InvokeTypes(11028, LCID, 1, (9, 0), ((8, 1), (8204, 1)),strName
			, pMultiPoint)

		if not _pMultiPoint_type:
			pMultiPoint = [_data.value for _data in pMultiPoint]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeltBeam', '{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}')
		return ret

	def CreateBodyBeltBeam2(self, strName, pMultiBodyPoint, pInOutList):
		'''
		Create a beam belt with multi body and point
		
		:param strName: str
		:param pMultiBodyPoint: list[object]
		:param pInOutList: list[object]
		:rtype: recurdyn.BNP.IBNPBodyBeltBeam
		'''
		_pMultiBodyPoint_type = True if pMultiBodyPoint and isinstance(pMultiBodyPoint[0], win32com.client.VARIANT) else False
		if not _pMultiBodyPoint_type:
			pMultiBodyPoint = [win32com.client.VARIANT(12, _data) for _data in pMultiBodyPoint]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(11033, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1)),strName
			, pMultiBodyPoint, pInOutList)

		if not _pMultiBodyPoint_type:
			pMultiBodyPoint = [_data.value for _data in pMultiBodyPoint]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeltBeam2', '{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}')
		return ret

	def CreateBodyBeltBeam3(self, strName, pMultiBodyPoint, pInOutList, uiNumberOfElements, dLowerThickness, dUpperThickness):
		'''
		Create a beam belt with multi bodies and points
		
		:param strName: str
		:param pMultiBodyPoint: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfElements: int
		:param dLowerThickness: float
		:param dUpperThickness: float
		:rtype: recurdyn.BNP.IBNPBodyBeltBeam
		'''
		_pMultiBodyPoint_type = True if pMultiBodyPoint and isinstance(pMultiBodyPoint[0], win32com.client.VARIANT) else False
		if not _pMultiBodyPoint_type:
			pMultiBodyPoint = [win32com.client.VARIANT(12, _data) for _data in pMultiBodyPoint]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(11035, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (19, 1), (5, 1), (5, 1)),strName
			, pMultiBodyPoint, pInOutList, uiNumberOfElements, dLowerThickness, dUpperThickness
			)

		if not _pMultiBodyPoint_type:
			pMultiBodyPoint = [_data.value for _data in pMultiBodyPoint]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeltBeam3', '{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}')
		return ret

	def CreateBodyBeltShell(self, strName, pMultiPoint):
		'''
		Create a shell belt
		
		:param strName: str
		:param pMultiPoint: list[object]
		:rtype: recurdyn.BNP.IBNPBodyBeltShell
		'''
		_pMultiPoint_type = True if pMultiPoint and isinstance(pMultiPoint[0], win32com.client.VARIANT) else False
		if not _pMultiPoint_type:
			pMultiPoint = [win32com.client.VARIANT(12, _data) for _data in pMultiPoint]

		ret = self._oleobj_.InvokeTypes(11029, LCID, 1, (9, 0), ((8, 1), (8204, 1)),strName
			, pMultiPoint)

		if not _pMultiPoint_type:
			pMultiPoint = [_data.value for _data in pMultiPoint]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeltShell', '{AE6E5127-052C-43DC-B39E-9C19E632FC4A}')
		return ret

	def CreateBodyBeltShell2(self, strName, pMultiBodyPoint, pInOutList):
		'''
		Create a shell belt with multi body and point
		
		:param strName: str
		:param pMultiBodyPoint: list[object]
		:param pInOutList: list[object]
		:rtype: recurdyn.BNP.IBNPBodyBeltShell
		'''
		_pMultiBodyPoint_type = True if pMultiBodyPoint and isinstance(pMultiBodyPoint[0], win32com.client.VARIANT) else False
		if not _pMultiBodyPoint_type:
			pMultiBodyPoint = [win32com.client.VARIANT(12, _data) for _data in pMultiBodyPoint]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(11034, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1)),strName
			, pMultiBodyPoint, pInOutList)

		if not _pMultiBodyPoint_type:
			pMultiBodyPoint = [_data.value for _data in pMultiBodyPoint]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeltShell2', '{AE6E5127-052C-43DC-B39E-9C19E632FC4A}')
		return ret

	def CreateBodyBeltShell3(self, strName, pMultiBodyPoint, pInOutList, uiNumberOfElementsLongitudinal, uiNumberOfElementsLateral, dThickness, dWidth):
		'''
		Create a shell belt with multi bodies, points, nubmer of elements, width, and thickness
		
		:param strName: str
		:param pMultiBodyPoint: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfElementsLongitudinal: int
		:param uiNumberOfElementsLateral: int
		:param dThickness: float
		:param dWidth: float
		:rtype: recurdyn.BNP.IBNPBodyBeltShell
		'''
		_pMultiBodyPoint_type = True if pMultiBodyPoint and isinstance(pMultiBodyPoint[0], win32com.client.VARIANT) else False
		if not _pMultiBodyPoint_type:
			pMultiBodyPoint = [win32com.client.VARIANT(12, _data) for _data in pMultiBodyPoint]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(11036, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8204, 1), (19, 1), (19, 1), (5, 1), (5, 1)),strName
			, pMultiBodyPoint, pInOutList, uiNumberOfElementsLongitudinal, uiNumberOfElementsLateral, dThickness
			, dWidth)

		if not _pMultiBodyPoint_type:
			pMultiBodyPoint = [_data.value for _data in pMultiBodyPoint]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyBeltShell3', '{AE6E5127-052C-43DC-B39E-9C19E632FC4A}')
		return ret

	def CreateBodyPulleyCrown(self, strName, pPoint):
		'''
		Create a crown pulley body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBodyPulleyCrown
		'''
		ret = self._oleobj_.InvokeTypes(11006, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyPulleyCrown', '{1640FE01-608A-4380-B9EF-6C40A8DC5B57}')
		return ret

	def CreateBodyPulleyFlange(self, strName, pBNPBodySurface):
		'''
		Create a flange pulley body
		
		:param strName: str
		:param pBNPBodySurface: IGeneric
		:rtype: recurdyn.BNP.IBNPBodyPulleyFlange
		'''
		ret = self._oleobj_.InvokeTypes(11008, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pBNPBodySurface)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyPulleyFlange', '{FFD05BAA-458B-4C65-AF21-DF21C3C5FA4D}')
		return ret

	def CreateBodyPulleyPrism(self, strName, pPoint):
		'''
		Create a crown pulley body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBodyPulleyPrism
		'''
		ret = self._oleobj_.InvokeTypes(11007, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyPulleyPrism', '{915B275A-9C28-4898-93D2-C28DB53018E2}')
		return ret

	def CreateBodyPulleyRibbedV(self, strName, pPoint):
		'''
		Create a ribbed v pulley body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBodyPulleyRibbedV
		'''
		ret = self._oleobj_.InvokeTypes(11010, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyPulleyRibbedV', '{57849CE0-405E-474C-B4C1-65523C6DEE04}')
		return ret

	def CreateBodyPulleyRoller(self, strName, pPoint):
		'''
		Create a roller pulley body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBodyPulleyRoller
		'''
		ret = self._oleobj_.InvokeTypes(11005, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyPulleyRoller', '{FB9C36C7-777E-4F21-92B5-662D9B696B9F}')
		return ret

	def CreateBodyPulleyTiming(self, strName, pPoint):
		'''
		Create a timing pulley body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBodyPulleyTiming
		'''
		ret = self._oleobj_.InvokeTypes(11011, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyPulleyTiming', '{6CAB2527-B23C-46F2-9E3F-9D793E4950EA}')
		return ret

	def CreateBodyPulleyV(self, strName, pPoint):
		'''
		Create a v pulley body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.BNP.IBNPBodyPulleyV
		'''
		ret = self._oleobj_.InvokeTypes(11009, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyPulleyV', '{DF52F1D2-21BC-4B10-989F-1C434899404A}')
		return ret

	def CreateForceConnectorBushing(self, strName, pBaseBody, pActionBody, pRefFrame):
		'''
		Create bushing connector
		
		:param strName: str
		:param pBaseBody: IGeneric
		:param pActionBody: IGeneric
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ToolkitCommon.IForceConnectorBushing
		'''
		ret = self._oleobj_.InvokeTypes(11024, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorBushing', '{F5A169B5-B529-4935-8B06-ACDD2A0BA456}')
		return ret

	def CreateForceConnectorFixed(self, strName, pBaseBody, pActionBody, pRefFrame):
		'''
		Create fixed connector
		
		:param strName: str
		:param pBaseBody: IGeneric
		:param pActionBody: IGeneric
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ToolkitCommon.IForceConnectorFixed
		'''
		ret = self._oleobj_.InvokeTypes(11021, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorFixed', '{39059D2F-DBEC-49DD-BFF2-AC0185541C99}')
		return ret

	def CreateForceConnectorRevolute(self, strName, pBaseBody, pActionBody, pRefFrame):
		'''
		Create revolute connector
		
		:param strName: str
		:param pBaseBody: IGeneric
		:param pActionBody: IGeneric
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ToolkitCommon.IForceConnectorRevolute
		'''
		ret = self._oleobj_.InvokeTypes(11022, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorRevolute', '{D24BBA28-623F-4F1C-97D5-021413EB6736}')
		return ret

	def CreateForceConnectorSpring(self, strName, pBaseBody, pActionBody, pBaseRefFrame, pActionRefFrame):
		'''
		Create spring connector
		
		:param strName: str
		:param pBaseBody: IGeneric
		:param pActionBody: IGeneric
		:param pBaseRefFrame: IReferenceFrame
		:param pActionRefFrame: IReferenceFrame
		:rtype: recurdyn.ToolkitCommon.IForceConnectorSpring
		'''
		ret = self._oleobj_.InvokeTypes(11023, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pBaseRefFrame, pActionRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorSpring', '{93A5A572-A6DD-4F12-A3E5-64F95B78718F}')
		return ret

	def CreateSensorDisplacement(self, strName, pEntity, pSensorMarker, dRange):
		'''
		Create a displacement sensor
		
		:param strName: str
		:param pEntity: IGeneric
		:param pSensorMarker: IMarker
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorDisplacement
		'''
		ret = self._oleobj_.InvokeTypes(11020, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (5, 1)),strName
			, pEntity, pSensorMarker, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorDisplacement', '{08F5AF0B-ADB1-4AB4-8FAB-54ADCB9B5F36}')
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
		ret = self._oleobj_.InvokeTypes(11017, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (9, 1), (5, 1)),strName
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
		ret = self._oleobj_.InvokeTypes(11018, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1), (9, 1), (5, 1)),strName
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
		ret = self._oleobj_.InvokeTypes(11016, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (9, 1), (5, 1)),strName
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
		ret = self._oleobj_.InvokeTypes(11019, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1), (5, 1)),strName
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


	def _get_Assembly2DCollection(self):
		return self._ApplyTypes_(*(11027, 2, (9, 0), (), "Assembly2DCollection", '{D857EC59-8A2A-4228-99C9-07F5E95B84B0}'))
	def _get_AssemblyCollection(self):
		return self._ApplyTypes_(*(11014, 2, (9, 0), (), "AssemblyCollection", '{9CE8D58D-66F0-42F7-991B-2BDE5CB7E940}'))
	def _get_BNPBodyCollection(self):
		return self._ApplyTypes_(*(11015, 2, (9, 0), (), "BNPBodyCollection", '{DE7BC821-F8B2-493F-A604-08BC45622B02}'))
	def _get_BeltCloneCollection(self):
		return self._ApplyTypes_(*(11013, 2, (9, 0), (), "BeltCloneCollection", '{7309E615-192D-406B-9F7A-AFF15939E207}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Contour(self):
		return self._ApplyTypes_(*(11025, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(11000, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
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

	Assembly2DCollection = property(_get_Assembly2DCollection, None)
	'''
	Get the collection of 2D assembly

	:type: recurdyn.BNP.IBNPAssembly2DCollection
	'''
	AssemblyCollection = property(_get_AssemblyCollection, None)
	'''
	Get the collection of assembly

	:type: recurdyn.BNP.IBNPAssemblyCollection
	'''
	BNPBodyCollection = property(_get_BNPBodyCollection, None)
	'''
	Get the BNP body collection of the assembly

	:type: recurdyn.BNP.IBNPBodyCollection
	'''
	BeltCloneCollection = property(_get_BeltCloneCollection, None)
	'''
	Get the belt collection of clones

	:type: recurdyn.BNP.IBNPBeltCloneCollection
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Contour = property(_get_Contour, None)
	'''
	Get Contour

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
		"Assembly2DCollection": (11027, 2, (9, 0), (), "Assembly2DCollection", '{D857EC59-8A2A-4228-99C9-07F5E95B84B0}'),
		"AssemblyCollection": (11014, 2, (9, 0), (), "AssemblyCollection", '{9CE8D58D-66F0-42F7-991B-2BDE5CB7E940}'),
		"BNPBodyCollection": (11015, 2, (9, 0), (), "BNPBodyCollection", '{DE7BC821-F8B2-493F-A604-08BC45622B02}'),
		"BeltCloneCollection": (11013, 2, (9, 0), (), "BeltCloneCollection", '{7309E615-192D-406B-9F7A-AFF15939E207}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Contour": (11025, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralSubSystem": (11000, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
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

IBNPAssembly_vtables_dispatch_ = 1
IBNPAssembly_vtables_ = [
	(( 'PassingBodyCollection' , 'ppVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{E26794CD-5D37-4617-BB5A-1AD85F3ED410}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody' , 'pVal' , ), 11003, (11003, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody' , 'pVal' , ), 11004, (11004, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfSegment' , 'pVal' , ), 11006, (11006, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'InitialLongitudinalVelocity' , 'ppVal' , ), 11007, (11007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BNPBodyBeltCollection' , 'ppVal' , ), 11008, (11008, (), [ (16393, 10, None, "IID('{B49E6018-2162-41C9-9AC4-AF610E2E2356}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ConnectingForceParameter' , 'ppVal' , ), 11009, (11009, (), [ (16393, 10, None, "IID('{E789A6A6-79B6-49EE-B0C4-EC84A24499B1}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetOutputBeltList' , 'ppSafeArray' , ), 11010, (11010, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AddOutputBelt' , 'strFileName' , ), 11011, (11011, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputBelt' , 'strFileName' , ), 11012, (11012, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AddAllOutputBelt' , ), 11013, (11013, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'RemoveAllOutputBelt' , ), 11014, (11014, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'BushingForceCollection' , 'ppVal' , ), 11020, (11020, (), [ (16393, 10, None, "IID('{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UpdateBeltInitialVelocity' , ), 11021, (11021, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'pVal' , ), 11022, (11022, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'pVal' , ), 11022, (11022, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IBNPAssembly2D_vtables_dispatch_ = 1
IBNPAssembly2D_vtables_ = [
	(( 'NormalDirection' , 'pVal' , ), 11051, (11051, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'pVal' , ), 11051, (11051, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfSegment' , 'pVal' , ), 11052, (11052, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'InitialLongitudinalVelocity' , 'ppVal' , ), 11053, (11053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'BNPBodyBeltCollection' , 'ppVal' , ), 11054, (11054, (), [ (16393, 10, None, "IID('{B49E6018-2162-41C9-9AC4-AF610E2E2356}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BusingForceParameter' , 'ppVal' , ), 11055, (11055, (), [ (16393, 10, None, "IID('{4C336B22-AB0D-4922-B913-91F61EB5C6CB}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BushingForceCollection' , 'ppVal' , ), 11056, (11056, (), [ (16393, 10, None, "IID('{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'pVal' , ), 11057, (11057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'pVal' , ), 11057, (11057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'PassingBodyCollection' , 'ppVal' , ), 11058, (11058, (), [ (16393, 10, None, "IID('{E26794CD-5D37-4617-BB5A-1AD85F3ED410}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody' , 'pVal' , ), 11060, (11060, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody' , 'pVal' , ), 11061, (11061, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'GetOutputBeltList' , 'ppSafeArray' , ), 11062, (11062, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'AddOutputBelt' , 'strFileName' , ), 11063, (11063, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputBelt' , 'strFileName' , ), 11064, (11064, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'AddAllOutputBelt' , ), 11065, (11065, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RemoveAllOutputBelt' , ), 11066, (11066, (), [ ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UpdateBeltInitialVelocity' , ), 11067, (11067, (), [ ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

IBNPAssembly2DBushingForceParameter_vtables_dispatch_ = 1
IBNPAssembly2DBushingForceParameter_vtables_ = [
	(( 'TranslationalStiffnessX' , 'ppVal' , ), 11000, (11000, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalStiffnessY' , 'ppVal' , ), 11001, (11001, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDampingX' , 'ppVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDampingY' , 'ppVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalPreloadX' , 'ppVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalPreloadY' , 'ppVal' , ), 11005, (11005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RotationalStiffnessZ' , 'ppVal' , ), 11006, (11006, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RotationalDampingZ' , 'ppVal' , ), 11007, (11007, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RotationalPreloadZ' , 'ppVal' , ), 11008, (11008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IBNPAssembly2DCollection_vtables_dispatch_ = 1
IBNPAssembly2DCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IBNPAssemblyCollection_vtables_dispatch_ = 1
IBNPAssemblyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IBNPAssemblyConnectingForceParameter_vtables_dispatch_ = 1
IBNPAssemblyConnectingForceParameter_vtables_ = [
	(( 'StiffnessMatrix' , 'i' , 'j' , 'ppVal' , ), 11000, (11000, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ViscousDampingRatio' , 'ppVal' , ), 11001, (11001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingMatrix' , 'pVal' , ), 11002, (11002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingMatrix' , 'pVal' , ), 11002, (11002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ViscousDampingMatrix' , 'i' , 'j' , 'ppVal' , ), 11006, (11006, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Preload' , 'Index' , 'ppVal' , ), 11003, (11003, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceLength' , 'Index' , 'ppVal' , ), 11004, (11004, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IBNPBeltBeamMaterialProperty_vtables_dispatch_ = 1
IBNPBeltBeamMaterialProperty_vtables_ = [
	(( 'MassType' , 'pVal' , ), 11200, (11200, (), [ (3, 1, None, "IID('{723CDBB9-022E-4BE4-91BC-A182933DB430}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MassType' , 'pVal' , ), 11200, (11200, (), [ (16387, 10, None, "IID('{723CDBB9-022E-4BE4-91BC-A182933DB430}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'ppVal' , ), 11201, (11201, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TotalMass' , 'ppVal' , ), 11202, (11202, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DampingRatio' , 'ppVal' , ), 11203, (11203, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus' , 'ppVal' , ), 11204, (11204, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulus' , 'ppVal' , ), 11205, (11205, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PoissonsRatio' , 'ppVal' , ), 11206, (11206, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'ppVal' , ), 11207, (11207, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'ppVal' , ), 11208, (11208, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'ppVal' , ), 11209, (11209, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'CrossSectionArea' , 'ppVal' , ), 11210, (11210, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Asy' , 'ppVal' , ), 11211, (11211, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Asz' , 'ppVal' , ), 11212, (11212, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CY' , 'pVal' , ), 11213, (11213, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CY' , 'pVal' , ), 11213, (11213, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CZ' , 'pVal' , ), 11214, (11214, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CZ' , 'pVal' , ), 11214, (11214, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DY' , 'pVal' , ), 11215, (11215, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DY' , 'pVal' , ), 11215, (11215, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DZ' , 'pVal' , ), 11216, (11216, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'DZ' , 'pVal' , ), 11216, (11216, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'EY' , 'pVal' , ), 11217, (11217, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'EY' , 'pVal' , ), 11217, (11217, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'EZ' , 'pVal' , ), 11218, (11218, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'EZ' , 'pVal' , ), 11218, (11218, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'FY' , 'pVal' , ), 11219, (11219, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'FY' , 'pVal' , ), 11219, (11219, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'FZ' , 'pVal' , ), 11220, (11220, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'FZ' , 'pVal' , ), 11220, (11220, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UpdateCrossSectionPropertyAutomaticallyFlag' , 'updateFlag' , ), 11221, (11221, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UpdateCrossSectionPropertyAutomaticallyFlag' , 'updateFlag' , ), 11221, (11221, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAreaProperties' , ), 11222, (11222, (), [ ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IBNPBeltClone_vtables_dispatch_ = 1
IBNPBeltClone_vtables_ = [
	(( 'UpdateGeometry' , ), 11001, (11001, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{4C8B7C23-7D92-4D39-B530-5D93DC97F771}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'ppVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'ppVal' , ), 11005, (11005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'ppVal' , ), 11006, (11006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Ixy' , 'ppVal' , ), 11007, (11007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Iyz' , 'ppVal' , ), 11008, (11008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Izx' , 'ppVal' , ), 11009, (11009, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'MaterialInput' , 'pVal' , ), 11010, (11010, (), [ (3, 1, None, "IID('{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}')") , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'MaterialInput' , 'pVal' , ), 11010, (11010, (), [ (16387, 10, None, "IID('{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'pVal' , ), 11011, (11011, (), [ (3, 1, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'pVal' , ), 11011, (11011, (), [ (16387, 10, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 11012, (11012, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 11012, (11012, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'MaterialUser' , 'pVal' , ), 11013, (11013, (), [ (9, 1, None, "IID('{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'MaterialUser' , 'pVal' , ), 11013, (11013, (), [ (16393, 10, None, "IID('{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'CenterMarker' , 'pVal' , ), 11014, (11014, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'InitialBodyGraphicFlag' , ), 11015, (11015, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'FileImport' , 'strFile' , ), 11016, (11016, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FileExport' , 'strFile' , 'OverWrite' , ), 11017, (11017, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 11018, (11018, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 11018, (11018, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IBNPBeltCloneCollection_vtables_dispatch_ = 1
IBNPBeltCloneCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IBNPBeltCloneFlat_vtables_dispatch_ = 1
IBNPBeltCloneFlat_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11050, (11050, (), [ (16393, 10, None, "IID('{9033BB6E-5115-49FA-83A2-E39301FBFD6C}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ContactNode' , 'ppProperty' , ), 11051, (11051, (), [ (16393, 10, None, "IID('{0711C396-7AF8-4A58-A98E-EDC99123FB42}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IBNPBeltCloneRibbedV_vtables_dispatch_ = 1
IBNPBeltCloneRibbedV_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11050, (11050, (), [ (16393, 10, None, "IID('{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ContactNode' , 'ppProperty' , ), 11051, (11051, (), [ (16393, 10, None, "IID('{ABC5653E-52A2-4028-AE40-3738D348CF0D}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IBNPBeltCloneTiming_vtables_dispatch_ = 1
IBNPBeltCloneTiming_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11050, (11050, (), [ (16393, 10, None, "IID('{28B9F577-7066-4B2E-80A2-AF7D140593AC}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

IBNPBeltCloneV_vtables_dispatch_ = 1
IBNPBeltCloneV_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11050, (11050, (), [ (16393, 10, None, "IID('{185F6935-19D9-4664-91A4-C564A61DF014}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ContactNode' , 'ppProperty' , ), 11051, (11051, (), [ (16393, 10, None, "IID('{7AE525B3-FE13-4117-809E-476C72E2847C}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IBNPBeltGroup_vtables_dispatch_ = 1
IBNPBeltGroup_vtables_ = [
	(( 'Color' , 'pVal' , ), 11000, (11000, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 11000, (11000, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNode' , 'pVal' , ), 11001, (11001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNode' , 'pVal' , ), 11001, (11001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeID' , 'pVal' , ), 11002, (11002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeID' , 'pVal' , ), 11002, (11002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'BeltType' , 'pVal' , ), 11003, (11003, (), [ (3, 1, None, "IID('{0BB88860-1CA3-4F91-973F-ACA0600D489B}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'BeltType' , 'pVal' , ), 11003, (11003, (), [ (16387, 10, None, "IID('{0BB88860-1CA3-4F91-973F-ACA0600D489B}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'LowerThickness' , 'ppVal' , ), 11004, (11004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UpperThickness' , 'ppVal' , ), 11005, (11005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 11006, (11006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfElements' , 'pVal' , ), 11007, (11007, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ElementLength' , 'pVal' , ), 11008, (11008, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ModelType' , 'pVal' , ), 11009, (11009, (), [ (3, 1, None, "IID('{90F9A508-6441-4D9C-9ECC-CE148ACE6008}')") , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ModelType' , 'pVal' , ), 11009, (11009, (), [ (16387, 10, None, "IID('{90F9A508-6441-4D9C-9ECC-CE148ACE6008}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'StretchedLength' , 'ppVal' , ), 11010, (11010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'MaterialProperty' , 'ppVal' , ), 11011, (11011, (), [ (16393, 10, None, "IID('{4FD6E858-87DC-4106-858F-F8CF4C6E60D5}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoint' , 'ppProperty' , ), 11012, (11012, (), [ (16393, 10, None, "IID('{C687377E-15AA-4340-A9F5-DB9CB8F4C9DA}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'PassingBodyCollection' , 'ppVal' , ), 11015, (11015, (), [ (16393, 10, None, "IID('{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody' , 'pVal' , ), 11016, (11016, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody' , 'pVal' , ), 11017, (11017, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialLongitudinalVelocity' , 'pVal' , ), 11018, (11018, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialLongitudinalVelocity' , 'pVal' , ), 11018, (11018, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'InitialLongitudinalVelocity' , 'ppVal' , ), 11019, (11019, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryInformationAutomatically' , 'pVal' , ), 11020, (11020, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryInformationAutomatically' , 'pVal' , ), 11020, (11020, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'GetOutputBeltList' , 'ppSafeArray' , ), 11021, (11021, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'AddOutputBelt' , 'strFileName' , ), 11022, (11022, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputBelt' , 'strFileName' , ), 11023, (11023, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'AddAllOutputBelt' , ), 11024, (11024, (), [ ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'RemoveAllOutputBelt' , ), 11025, (11025, (), [ ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
]

IBNPBeltGroupContactPoint_vtables_dispatch_ = 1
IBNPBeltGroupContactPoint_vtables_ = [
	(( 'ContactNodeBottom' , 'pVal' , ), 11050, (11050, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeBottom' , 'pVal' , ), 11050, (11050, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeSide' , 'pVal' , ), 11051, (11051, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeSide' , 'pVal' , ), 11051, (11051, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeTop' , 'pVal' , ), 11052, (11052, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeTop' , 'pVal' , ), 11052, (11052, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IBNPBeltGroupMaterialProperty_vtables_dispatch_ = 1
IBNPBeltGroupMaterialProperty_vtables_ = [
	(( 'MassType' , 'pVal' , ), 11050, (11050, (), [ (3, 1, None, "IID('{723CDBB9-022E-4BE4-91BC-A182933DB430}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MassType' , 'pVal' , ), 11050, (11050, (), [ (16387, 10, None, "IID('{723CDBB9-022E-4BE4-91BC-A182933DB430}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'ppVal' , ), 11051, (11051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TotalMass' , 'ppVal' , ), 11052, (11052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DampingRatio' , 'ppVal' , ), 11053, (11053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus' , 'ppVal' , ), 11054, (11054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulus' , 'ppVal' , ), 11055, (11055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'ppVal' , ), 11056, (11056, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'ppVal' , ), 11057, (11057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'ppVal' , ), 11058, (11058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CrossSectionArea' , 'ppVal' , ), 11059, (11059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IBNPBeltShellMaterialProperty_vtables_dispatch_ = 1
IBNPBeltShellMaterialProperty_vtables_ = [
	(( 'MaterialPropertyType' , 'pVal' , ), 11200, (11200, (), [ (3, 1, None, "IID('{CEA0FB7A-8C16-4D2F-B859-C3A84BC76392}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MaterialPropertyType' , 'pVal' , ), 11200, (11200, (), [ (16387, 10, None, "IID('{CEA0FB7A-8C16-4D2F-B859-C3A84BC76392}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MassType' , 'pVal' , ), 11201, (11201, (), [ (3, 1, None, "IID('{723CDBB9-022E-4BE4-91BC-A182933DB430}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MassType' , 'pVal' , ), 11201, (11201, (), [ (16387, 10, None, "IID('{723CDBB9-022E-4BE4-91BC-A182933DB430}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'ppVal' , ), 11202, (11202, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TotalMass' , 'ppVal' , ), 11203, (11203, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DampingRatio' , 'ppVal' , ), 11204, (11204, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus' , 'ppVal' , ), 11205, (11205, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PoissonsModulus' , 'ppVal' , ), 11206, (11206, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus1' , 'ppVal' , ), 11207, (11207, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus2' , 'ppVal' , ), 11208, (11208, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulus' , 'ppVal' , ), 11209, (11209, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PoissonsRatio1' , 'ppVal' , ), 11210, (11210, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DrillingStiffnessFactor' , 'ppVal' , ), 11211, (11211, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ElementDampingForceType' , 'pVal' , ), 11212, (11212, (), [ (3, 1, None, "IID('{9757FC8B-6458-44FB-A16E-850F76CE5608}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ElementDampingForceType' , 'pVal' , ), 11212, (11212, (), [ (16387, 10, None, "IID('{9757FC8B-6458-44FB-A16E-850F76CE5608}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedTransverseShearModulus' , 'flag' , ), 11213, (11213, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedTransverseShearModulus' , 'flag' , ), 11213, (11213, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TransverseShearModulus1' , 'value' , ), 11214, (11214, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'TransverseShearModulus2' , 'value' , ), 11215, (11215, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'G11' , 'value' , ), 11216, (11216, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'G12' , 'value' , ), 11217, (11217, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'G13' , 'value' , ), 11218, (11218, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'G22' , 'value' , ), 11219, (11219, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'G23' , 'value' , ), 11220, (11220, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'G33' , 'value' , ), 11221, (11221, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IBNPBody_vtables_dispatch_ = 1
IBNPBody_vtables_ = [
	(( 'GeneralBody' , 'ppVal' , ), 11000, (11000, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IBNPBody2DGuide_vtables_dispatch_ = 1
IBNPBody2DGuide_vtables_ = [
	(( 'ContactProperty' , 'ppContactProperty' , ), 11050, (11050, (), [ (16393, 10, None, "IID('{06D06385-6578-48E1-AACC-2BB6BD56B20A}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IBNPBody2DGuideArc_vtables_dispatch_ = 1
IBNPBody2DGuideArc_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11100, (11100, (), [ (16393, 10, None, "IID('{28DFE5F6-D718-4CD5-AA3B-4CC4538DEB62}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'pVal' , ), 11101, (11101, (), [ (3, 1, None, "IID('{CFBA2C41-79A2-4AD3-913D-41E55C6DF27F}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'pVal' , ), 11101, (11101, (), [ (16387, 10, None, "IID('{CFBA2C41-79A2-4AD3-913D-41E55C6DF27F}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IBNPBody2DGuideLinear_vtables_dispatch_ = 1
IBNPBody2DGuideLinear_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11100, (11100, (), [ (16393, 10, None, "IID('{6E62C6CA-9D43-4D53-A2B1-4BEFD6DE5D22}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'pVal' , ), 11101, (11101, (), [ (3, 1, None, "IID('{CFBA2C41-79A2-4AD3-913D-41E55C6DF27F}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'pVal' , ), 11101, (11101, (), [ (16387, 10, None, "IID('{CFBA2C41-79A2-4AD3-913D-41E55C6DF27F}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IBNPBodyBelt_vtables_dispatch_ = 1
IBNPBodyBelt_vtables_ = [
	(( 'UpdateGeometry' , ), 11051, (11051, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseBodyGraphic' , 'pVal' , ), 11052, (11052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseBodyGraphic' , 'pVal' , ), 11052, (11052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 11053, (11053, (), [ (16393, 10, None, "IID('{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateMarker' , 'strName' , 'pRefFrame' , 'ppVal' , ), 11054, (11054, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IBNPBodyBeltBeam_vtables_dispatch_ = 1
IBNPBodyBeltBeam_vtables_ = [
	(( 'ConnectingParameters' , 'ppConnectingParameters' , ), 11100, (11100, (), [ (16393, 10, None, "IID('{A111AE4E-7116-496C-BA07-1B125F33ECEA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppGeometry' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{64E4D842-5C51-484B-B3F8-C54D097BBDA1}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'BCCollection' , 'ppCollection' , ), 11102, (11102, (), [ (16393, 10, None, "IID('{7F035946-EE7C-4557-BAFC-000BDD366EDF}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'OutputCollection' , 'ppCollection' , ), 11103, (11103, (), [ (16393, 10, None, "IID('{4549131A-72B6-45B1-9ABE-C2A32F250FED}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'BCOrienation' , 'pVal' , ), 11104, (11104, (), [ (3, 1, None, "IID('{14B4CA05-EA66-4C59-BED0-04E27062CE88}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BCOrienation' , 'pVal' , ), 11104, (11104, (), [ (16387, 10, None, "IID('{14B4CA05-EA66-4C59-BED0-04E27062CE88}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'FlexBody' , 'ppVal' , ), 11105, (11105, (), [ (16393, 10, None, "IID('{9257FD72-F3D0-4E57-A114-2045356D78CD}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAllProperties' , ), 11106, (11106, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IBNPBodyBeltCollection_vtables_dispatch_ = 1
IBNPBodyBeltCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{8ED56403-6EF8-4451-9CA4-7DBE298F4FE5}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IBNPBodyBeltFlat_vtables_dispatch_ = 1
IBNPBodyBeltFlat_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11100, (11100, (), [ (16393, 10, None, "IID('{9033BB6E-5115-49FA-83A2-E39301FBFD6C}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ContactNode' , 'ppProperty' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{0711C396-7AF8-4A58-A98E-EDC99123FB42}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IBNPBodyBeltRibbedV_vtables_dispatch_ = 1
IBNPBodyBeltRibbedV_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11100, (11100, (), [ (16393, 10, None, "IID('{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ContactNode' , 'ppProperty' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{ABC5653E-52A2-4028-AE40-3738D348CF0D}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IBNPBodyBeltShell_vtables_dispatch_ = 1
IBNPBodyBeltShell_vtables_ = [
	(( 'ConnectingParameters' , 'ppConnectingParameters' , ), 11100, (11100, (), [ (16393, 10, None, "IID('{A111AE4E-7116-496C-BA07-1B125F33ECEA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppGeometry' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{FD1CA7C1-21FE-488D-88DC-87AF6CC66D8E}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'BCCollection' , 'ppCollection' , ), 11102, (11102, (), [ (16393, 10, None, "IID('{7F035946-EE7C-4557-BAFC-000BDD366EDF}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'OutputCollection' , 'ppCollection' , ), 11103, (11103, (), [ (16393, 10, None, "IID('{4549131A-72B6-45B1-9ABE-C2A32F250FED}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'BCOrienation' , 'pVal' , ), 11104, (11104, (), [ (3, 1, None, "IID('{14B4CA05-EA66-4C59-BED0-04E27062CE88}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BCOrienation' , 'pVal' , ), 11104, (11104, (), [ (16387, 10, None, "IID('{14B4CA05-EA66-4C59-BED0-04E27062CE88}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'FlexBody' , 'ppVal' , ), 11105, (11105, (), [ (16393, 10, None, "IID('{9257FD72-F3D0-4E57-A114-2045356D78CD}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IBNPBodyBeltTiming_vtables_dispatch_ = 1
IBNPBodyBeltTiming_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11100, (11100, (), [ (16393, 10, None, "IID('{28B9F577-7066-4B2E-80A2-AF7D140593AC}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IBNPBodyBeltV_vtables_dispatch_ = 1
IBNPBodyBeltV_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11100, (11100, (), [ (16393, 10, None, "IID('{185F6935-19D9-4664-91A4-C564A61DF014}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ContactNode' , 'ppProperty' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{7AE525B3-FE13-4117-809E-476C72E2847C}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IBNPBodyCollection_vtables_dispatch_ = 1
IBNPBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IBNPBodyPulley_vtables_dispatch_ = 1
IBNPBodyPulley_vtables_ = [
	(( 'ContactProperty' , 'ppContactProperty' , ), 11050, (11050, (), [ (16393, 10, None, "IID('{06D06385-6578-48E1-AACC-2BB6BD56B20A}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 11051, (11051, (), [ (16393, 10, None, "IID('{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactDirection' , 'ppVal' , ), 11052, (11052, (), [ (16393, 10, None, "IID('{2391593F-3C53-4F17-8285-F2857B2229C7}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 11053, (11053, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 11053, (11053, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoints' , 'pVal' , ), 11054, (11054, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ContactPoints' , 'pVal' , ), 11054, (11054, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IBNPBodyPulleyCrown_vtables_dispatch_ = 1
IBNPBodyPulleyCrown_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{7ACC0B53-41A1-45D3-A170-8C7FD07C4E66}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IBNPBodyPulleyFlange_vtables_dispatch_ = 1
IBNPBodyPulleyFlange_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{D15BA410-27CD-4BBF-8B63-7157B683989A}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IBNPBodyPulleyPrism_vtables_dispatch_ = 1
IBNPBodyPulleyPrism_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{CAFDBC3C-C51A-412A-80E1-7F58BB60F820}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IBNPBodyPulleyRibbedV_vtables_dispatch_ = 1
IBNPBodyPulleyRibbedV_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{32EA063C-BD96-48EA-93C6-C3DAA3961197}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IBNPBodyPulleyRoller_vtables_dispatch_ = 1
IBNPBodyPulleyRoller_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{530E037B-C319-4E08-A507-77020D1582D4}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IBNPBodyPulleyTiming_vtables_dispatch_ = 1
IBNPBodyPulleyTiming_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{73E882E6-E6A2-41EB-B965-F386ADD519E8}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IBNPBodyPulleyV_vtables_dispatch_ = 1
IBNPBodyPulleyV_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 11101, (11101, (), [ (16393, 10, None, "IID('{CB8A9B5A-33D9-4AE8-8EB6-AE1CD753C5AF}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IBNPConnectingParameters_vtables_dispatch_ = 1
IBNPConnectingParameters_vtables_ = [
	(( 'UseForceConnector' , 'pVal' , ), 11150, (11150, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseForceConnector' , 'pVal' , ), 11150, (11150, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseSyncFDR' , 'pVal' , ), 11151, (11151, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseSyncFDR' , 'pVal' , ), 11151, (11151, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 11152, (11152, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MomentOfInertia' , 'ppVal' , ), 11153, (11153, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalStiffness' , 'ppVal' , ), 11154, (11154, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDampingRatio' , 'ppVal' , ), 11155, (11155, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RotationnalStiffness' , 'ppVal' , ), 11156, (11156, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RotationnalDampingRatio' , 'ppVal' , ), 11157, (11157, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IBNPContactDirection_vtables_dispatch_ = 1
IBNPContactDirection_vtables_ = [
	(( 'Type' , 'pVal' , ), 11000, (11000, (), [ (3, 1, None, "IID('{22B08D86-DCCB-468A-A747-466E1F7ACAFD}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 11000, (11000, (), [ (16387, 10, None, "IID('{22B08D86-DCCB-468A-A747-466E1F7ACAFD}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IBNPContactFriction_vtables_dispatch_ = 1
IBNPContactFriction_vtables_ = [
	(( 'StaticThresholdVelocity' , 'ppVal' , ), 11001, (11001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DynamicThresholdVelocity' , 'ppVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StaticFrictionCoefficient' , 'ppVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumFrictionForce' , 'pVal' , ), 11004, (11004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseMaximumFrictionForce' , 'pVal' , ), 11004, (11004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MaximumFrictionForce' , 'ppVal' , ), 11005, (11005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'MaximumstictionDeformation' , 'ppVal' , ), 11006, (11006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IBNPContactNodePropertyBeltFlat_vtables_dispatch_ = 1
IBNPContactNodePropertyBeltFlat_vtables_ = [
	(( 'ContactNodeBottom' , 'pVal' , ), 22050, (22050, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeBottom' , 'pVal' , ), 22050, (22050, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeSide' , 'pVal' , ), 22051, (22051, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeSide' , 'pVal' , ), 22051, (22051, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeTop' , 'pVal' , ), 22052, (22052, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeTop' , 'pVal' , ), 22052, (22052, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'EstimationContactNodes' , 'pVal' , ), 22053, (22053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'EstimationContactNodes' , 'pVal' , ), 22053, (22053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IBNPContactNodePropertyBeltRibbedV_vtables_dispatch_ = 1
IBNPContactNodePropertyBeltRibbedV_vtables_ = [
	(( 'ContactNodeBottom' , 'pVal' , ), 22050, (22050, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeBottom' , 'pVal' , ), 22050, (22050, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeLowerSide' , 'pVal' , ), 22051, (22051, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeLowerSide' , 'pVal' , ), 22051, (22051, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeUpperSide' , 'pVal' , ), 22052, (22052, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeUpperSide' , 'pVal' , ), 22052, (22052, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeTop' , 'pVal' , ), 22053, (22053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeTop' , 'pVal' , ), 22053, (22053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeGroove' , 'pVal' , ), 22054, (22054, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeGroove' , 'pVal' , ), 22054, (22054, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'EstimationContactNodes' , 'pVal' , ), 22055, (22055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'EstimationContactNodes' , 'pVal' , ), 22055, (22055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IBNPContactNodePropertyBeltV_vtables_dispatch_ = 1
IBNPContactNodePropertyBeltV_vtables_ = [
	(( 'ContactNodeBottom' , 'pVal' , ), 22050, (22050, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeBottom' , 'pVal' , ), 22050, (22050, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeLowerSide' , 'pVal' , ), 22051, (22051, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeLowerSide' , 'pVal' , ), 22051, (22051, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeUpperSide' , 'pVal' , ), 22052, (22052, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeUpperSide' , 'pVal' , ), 22052, (22052, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeTop' , 'pVal' , ), 22053, (22053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ContactNodeTop' , 'pVal' , ), 22053, (22053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'EstimationContactNodes' , 'pVal' , ), 22054, (22054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'EstimationContactNodes' , 'pVal' , ), 22054, (22054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IBNPContactProperty_vtables_dispatch_ = 1
IBNPContactProperty_vtables_ = [
	(( 'StiffnessCoefficient' , 'ppVal' , ), 11000, (11000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 11001, (11001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 11001, (11001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 11002, (11002, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 11003, (11003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 11004, (11004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 11004, (11004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 11005, (11005, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 11005, (11005, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 11006, (11006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 11007, (11007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 11007, (11007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 11008, (11008, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 11008, (11008, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 11009, (11009, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 11009, (11009, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 11010, (11010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 11011, (11011, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 11011, (11011, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 11012, (11012, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 11013, (11013, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 11013, (11013, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 11014, (11014, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Friction' , 'ppVal' , ), 11015, (11015, (), [ (16393, 10, None, "IID('{E2EB7072-FAB5-4AAE-8E30-4DABC6A590BA}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ContactFrictionType' , 'ContactFrictionType' , ), 11016, (11016, (), [ (16387, 10, None, "IID('{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ContactFrictionType' , 'ContactFrictionType' , ), 11016, (11016, (), [ (3, 1, None, "IID('{D0BC9C52-6D99-4CC5-9124-E1520C347D7A}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IBNPContactSearch_vtables_dispatch_ = 1
IBNPContactSearch_vtables_ = [
	(( 'Type' , 'pVal' , ), 11000, (11000, (), [ (3, 1, None, "IID('{FA51F4CB-1D66-4B58-A5C0-185D24EFBC01}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 11000, (11000, (), [ (16387, 10, None, "IID('{FA51F4CB-1D66-4B58-A5C0-185D24EFBC01}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseUserBoundaryForPartialSearch' , 'pVal' , ), 11001, (11001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseUserBoundaryForPartialSearch' , 'pVal' , ), 11001, (11001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UserBoundaryForPartialSearch' , 'ppVal' , ), 11002, (11002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IBNPGeometry2DGuide_vtables_dispatch_ = 1
IBNPGeometry2DGuide_vtables_ = [
	(( 'Depth' , 'ppVal' , ), 50, (50, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ViewRefFrame' , 'ppVal' , ), 51, (51, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 52, (52, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IBNPGeometry2DGuideArc_vtables_dispatch_ = 1
IBNPGeometry2DGuideArc_vtables_ = [
	(( 'Point3DWithRadiusCollection' , 'ppVal' , ), 100, (100, (), [ (16393, 10, None, "IID('{0476BFAD-0FF1-4CA4-8B59-AE9E00842CCB}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IBNPGeometry2DGuideLinear_vtables_dispatch_ = 1
IBNPGeometry2DGuideLinear_vtables_ = [
	(( 'Point3DCollection' , 'ppVal' , ), 100, (100, (), [ (16393, 10, None, "IID('{7AAA986F-35DD-4DCF-843A-CEBA8E09D33A}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryBeltBeam_vtables_dispatch_ = 1
IBNPGeometryBeltBeam_vtables_ = [
	(( 'Color' , 'pVal' , ), 11150, (11150, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 11150, (11150, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeID' , 'pVal' , ), 11151, (11151, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeID' , 'pVal' , ), 11151, (11151, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'BeltType' , 'pVal' , ), 11152, (11152, (), [ (3, 1, None, "IID('{0BB88860-1CA3-4F91-973F-ACA0600D489B}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'BeltType' , 'pVal' , ), 11152, (11152, (), [ (16387, 10, None, "IID('{0BB88860-1CA3-4F91-973F-ACA0600D489B}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LowerThickness' , 'ppVal' , ), 11153, (11153, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UpperThickness' , 'ppVal' , ), 11154, (11154, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 11155, (11155, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 11156, (11156, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'ppVal' , ), 11157, (11157, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'AssembledThickness' , 'ppVal' , ), 11158, (11158, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Interval' , 'pVal' , ), 11159, (11159, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Interval' , 'pVal' , ), 11159, (11159, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppVal' , ), 11160, (11160, (), [ (16393, 10, None, "IID('{3218112D-CC7E-4DC3-A6A4-36A6B33C12B6}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfElements' , 'pVal' , ), 11161, (11161, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ElementLength' , 'pVal' , ), 11162, (11162, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StretchedLength' , 'ppVal' , ), 11163, (11163, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'MaterialProperty' , 'ppVal' , ), 11164, (11164, (), [ (16393, 10, None, "IID('{D9C23616-C0D3-422D-8A74-02654AB2E863}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PassingBodyCollection' , 'ppVal' , ), 11165, (11165, (), [ (16393, 10, None, "IID('{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody' , 'pVal' , ), 11166, (11166, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody' , 'pVal' , ), 11167, (11167, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialLongitudinalVelocity' , 'pVal' , ), 11168, (11168, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialLongitudinalVelocity' , 'pVal' , ), 11168, (11168, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'InitialLongitudinalVelocity' , 'ppVal' , ), 11169, (11169, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryInformationAutomatically' , 'pVal' , ), 11170, (11170, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryInformationAutomatically' , 'pVal' , ), 11170, (11170, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryBeltFlat_vtables_dispatch_ = 1
IBNPGeometryBeltFlat_vtables_ = [
	(( 'Height' , 'ppVal' , ), 22050, (22050, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 22051, (22051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SegmentLength' , 'ppVal' , ), 22052, (22052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CordDistance' , 'ppVal' , ), 22053, (22053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LeftConnectionPosition' , 'pVal' , ), 22054, (22054, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LeftConnectionPosition' , 'pVal' , ), 22054, (22054, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RightConnectionPosition' , 'pVal' , ), 22055, (22055, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RightConnectionPosition' , 'pVal' , ), 22055, (22055, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryBeltRibbedV_vtables_dispatch_ = 1
IBNPGeometryBeltRibbedV_vtables_ = [
	(( 'Height' , 'ppVal' , ), 22050, (22050, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'ppVal' , ), 22051, (22051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RibHeight' , 'ppVal' , ), 22052, (22052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 22053, (22053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 22054, (22054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Pitch' , 'ppVal' , ), 22055, (22055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPeak' , 'pVal' , ), 22056, (22056, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPeak' , 'pVal' , ), 22056, (22056, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RibWidth' , 'pVal' , ), 22057, (22057, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SegmentLength' , 'ppVal' , ), 22058, (22058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CordDistance' , 'ppVal' , ), 22059, (22059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LeftConnectionPosition' , 'pVal' , ), 22060, (22060, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'LeftConnectionPosition' , 'pVal' , ), 22060, (22060, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'RightConnectionPosition' , 'pVal' , ), 22061, (22061, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'RightConnectionPosition' , 'pVal' , ), 22061, (22061, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryBeltShell_vtables_dispatch_ = 1
IBNPGeometryBeltShell_vtables_ = [
	(( 'Color' , 'pVal' , ), 11150, (11150, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 11150, (11150, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeID' , 'pVal' , ), 11151, (11151, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DisplayNodeID' , 'pVal' , ), 11151, (11151, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'ppVal' , ), 11152, (11152, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 11153, (11153, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfElementsLongitudinal' , 'pVal' , ), 11154, (11154, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfElementsLateral' , 'pVal' , ), 11155, (11155, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ElementLengthLongitudinal' , 'pVal' , ), 11156, (11156, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ElementLengthLateral' , 'pVal' , ), 11157, (11157, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'CurlRadiusLongitudinal' , 'ppVal' , ), 11158, (11158, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'CurlRadiusLateral' , 'ppVal' , ), 11159, (11159, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'StretchedLength' , 'ppVal' , ), 11160, (11160, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'MaterialProperty' , 'ppVal' , ), 11161, (11161, (), [ (16393, 10, None, "IID('{9BC7A528-18AE-43FF-B8FF-81EBDAF0F812}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PassingBodyCollection' , 'ppVal' , ), 11162, (11162, (), [ (16393, 10, None, "IID('{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody' , 'pVal' , ), 11163, (11163, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody' , 'pVal' , ), 11164, (11164, (), [ (9, 1, None, "IID('{7E83926D-1A31-4FC1-B317-411A03FF7DF8}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialLongitudinalVelocity' , 'pVal' , ), 11165, (11165, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialLongitudinalVelocity' , 'pVal' , ), 11165, (11165, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'InitialLongitudinalVelocity' , 'ppVal' , ), 11166, (11166, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryInformationAutomatically' , 'pVal' , ), 11167, (11167, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdateGeometryInformationAutomatically' , 'pVal' , ), 11167, (11167, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'LeftThickness' , 'ppVal' , ), 11168, (11168, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RightThickness' , 'ppVal' , ), 11169, (11169, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryBeltTiming_vtables_dispatch_ = 1
IBNPGeometryBeltTiming_vtables_ = [
	(( 'ToothProfileType' , 'pVal' , ), 22050, (22050, (), [ (3, 1, None, "IID('{E0737D18-B0FC-4DEF-8DC2-AC308C6A21A8}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ToothProfileType' , 'pVal' , ), 22050, (22050, (), [ (16387, 10, None, "IID('{E0737D18-B0FC-4DEF-8DC2-AC308C6A21A8}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Pitch' , 'ppVal' , ), 22051, (22051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 22052, (22052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 22053, (22053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CordDistance' , 'ppVal' , ), 22054, (22054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LeftConnectionPosition' , 'pVal' , ), 22055, (22055, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LeftConnectionPosition' , 'pVal' , ), 22055, (22055, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RightConnectionPosition' , 'pVal' , ), 22056, (22056, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RightConnectionPosition' , 'pVal' , ), 22056, (22056, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ToothLength' , 'ppVal' , ), 22057, (22057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ToothHeight' , 'ppVal' , ), 22058, (22058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NominalHeight' , 'ppVal' , ), 22059, (22059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ToothRootRadius' , 'ppVal' , ), 22060, (22060, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ToothTipRadius' , 'ppVal' , ), 22061, (22061, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppVal' , ), 22062, (22062, (), [ (16393, 10, None, "IID('{94B262DF-F40E-41A3-AEBF-98580C067EE0}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryBeltV_vtables_dispatch_ = 1
IBNPGeometryBeltV_vtables_ = [
	(( 'Height' , 'ppVal' , ), 22050, (22050, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'ppVal' , ), 22051, (22051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 22052, (22052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 22053, (22053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SegmentLength' , 'ppVal' , ), 22054, (22054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CordDistance' , 'ppVal' , ), 22055, (22055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LeftConnectionPosition' , 'pVal' , ), 22056, (22056, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LeftConnectionPosition' , 'pVal' , ), 22056, (22056, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RightConnectionPosition' , 'pVal' , ), 22057, (22057, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RightConnectionPosition' , 'pVal' , ), 22057, (22057, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryPulleyCrown_vtables_dispatch_ = 1
IBNPGeometryPulleyCrown_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 22100, (22100, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 22101, (22101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseAssembledRadius' , 'pVal' , ), 22102, (22102, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseAssembledRadius' , 'pVal' , ), 22102, (22102, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'AssembledRadius' , 'ppVal' , ), 22103, (22103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppProfile' , ), 22104, (22104, (), [ (16393, 10, None, "IID('{D5E4799C-AD42-492B-BF4F-C9B2AEAD3917}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryPulleyFlange_vtables_dispatch_ = 1
IBNPGeometryPulleyFlange_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 22100, (22100, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 22101, (22101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 22102, (22102, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryPulleyPrism_vtables_dispatch_ = 1
IBNPGeometryPulleyPrism_vtables_ = [
	(( 'Width' , 'ppVal' , ), 22100, (22100, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AssembledRadius' , 'ppVal' , ), 22101, (22101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppProfile' , ), 22102, (22102, (), [ (16393, 10, None, "IID('{1FA326B0-7EA6-4D8C-A58B-7E69947E8B6D}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryPulleyRibbedV_vtables_dispatch_ = 1
IBNPGeometryPulleyRibbedV_vtables_ = [
	(( 'InnerRadius' , 'ppVal' , ), 22100, (22100, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'ppVal' , ), 22101, (22101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OuterRadius' , 'ppVal' , ), 22102, (22102, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 22103, (22103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 22104, (22104, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Pitch' , 'ppVal' , ), 22105, (22105, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfGroove' , 'pVal' , ), 22106, (22106, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfGroove' , 'pVal' , ), 22106, (22106, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PulleyWidth' , 'pVal' , ), 22107, (22107, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'AssembledRadius' , 'ppVal' , ), 22108, (22108, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryPulleyRoller_vtables_dispatch_ = 1
IBNPGeometryPulleyRoller_vtables_ = [
	(( 'Radius' , 'ppVal' , ), 22100, (22100, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 22101, (22101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AssembledRadius' , 'ppVal' , ), 22102, (22102, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryPulleyTiming_vtables_dispatch_ = 1
IBNPGeometryPulleyTiming_vtables_ = [
	(( 'PulleyType' , 'pVal' , ), 22100, (22100, (), [ (3, 1, None, "IID('{45F846EF-57B0-4496-A5F4-774D896B5038}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PulleyType' , 'pVal' , ), 22100, (22100, (), [ (16387, 10, None, "IID('{45F846EF-57B0-4496-A5F4-774D896B5038}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfTeeth' , 'pVal' , ), 22101, (22101, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfTeeth' , 'pVal' , ), 22101, (22101, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 22102, (22102, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ToothHeight' , 'ppVal' , ), 22103, (22103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ToothLength' , 'ppVal' , ), 22104, (22104, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ToothRootRadius' , 'ppVal' , ), 22105, (22105, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ToothTipRadius' , 'ppVal' , ), 22106, (22106, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'OutsideDiameter' , 'ppVal' , ), 22107, (22107, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'PulleyRadius' , 'ppVal' , ), 22108, (22108, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DedenRadius' , 'ppVal' , ), 22109, (22109, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'BaseRadius' , 'ppVal' , ), 22110, (22110, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PitchRadius' , 'ppVal' , ), 22111, (22111, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'AddenRadius' , 'ppVal' , ), 22112, (22112, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'FlangeHeight' , 'ppVal' , ), 22113, (22113, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'PulleyWidth' , 'ppVal' , ), 22114, (22114, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'FlangeWidth' , 'ppVal' , ), 22115, (22115, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AssemblyInformationType' , 'pVal' , ), 22116, (22116, (), [ (3, 1, None, "IID('{2237E8C8-FFDD-40BE-A9F2-6D06738D0389}')") , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AssemblyInformationType' , 'pVal' , ), 22116, (22116, (), [ (16387, 10, None, "IID('{2237E8C8-FFDD-40BE-A9F2-6D06738D0389}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AssembledRadius' , 'pVal' , ), 22117, (22117, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AssembledRadius' , 'pVal' , ), 22117, (22117, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'RadialDistance' , 'pVal' , ), 22118, (22118, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RadialDistance' , 'pVal' , ), 22118, (22118, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IBNPGeometryPulleyV_vtables_dispatch_ = 1
IBNPGeometryPulleyV_vtables_ = [
	(( 'InnerRadius' , 'ppVal' , ), 22100, (22100, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'ppVal' , ), 22101, (22101, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OuterRadius' , 'ppVal' , ), 22102, (22102, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 22103, (22103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PulleyWidth' , 'ppVal' , ), 22104, (22104, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'ppVal' , ), 22105, (22105, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AssembledRadius' , 'ppVal' , ), 22106, (22106, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IBNPPassingBodyCollection_vtables_dispatch_ = 1
IBNPPassingBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IBNPProfile_vtables_dispatch_ = 1
IBNPProfile_vtables_ = [
	(( 'PointCollection' , 'ppVal' , ), 33100, (33100, (), [ (16393, 10, None, "IID('{2C0D70A3-D197-4781-940A-1672F3B420B9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 33101, (33101, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 33102, (33102, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IBNPProfileBeamTiming_vtables_dispatch_ = 1
IBNPProfileBeamTiming_vtables_ = [
]

IBNPProfileBeltTiming_vtables_dispatch_ = 1
IBNPProfileBeltTiming_vtables_ = [
]

IBNPProfilePulleyCrown_vtables_dispatch_ = 1
IBNPProfilePulleyCrown_vtables_ = [
]

IBNPProfilePulleyPrism_vtables_dispatch_ = 1
IBNPProfilePulleyPrism_vtables_ = [
]

IBNPSubSystem_vtables_dispatch_ = 1
IBNPSubSystem_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 11000, (11000, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreateBeltCloneFlat' , 'strName' , 'pPoint' , 'ppResult' , ), 11001, (11001, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{F60BB117-D220-4FD8-B603-74573A033D40}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CreateBeltCloneV' , 'strName' , 'pPoint' , 'ppResult' , ), 11002, (11002, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{8FC53768-BC25-4B05-BE34-6E537955559C}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CreateBeltCloneRibbedV' , 'strName' , 'pPoint' , 'ppResult' , ), 11003, (11003, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{1DD37F48-A065-4B60-BA2D-5A2BFB10AB67}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateBeltCloneTiming' , 'strName' , 'pPoint' , 'ppResult' , ), 11004, (11004, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{7D32C453-E2E6-413F-8F69-C66F17CE38C6}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyPulleyRoller' , 'strName' , 'pPoint' , 'ppResult' , ), 11005, (11005, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{FB9C36C7-777E-4F21-92B5-662D9B696B9F}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyPulleyCrown' , 'strName' , 'pPoint' , 'ppResult' , ), 11006, (11006, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{1640FE01-608A-4380-B9EF-6C40A8DC5B57}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyPulleyPrism' , 'strName' , 'pPoint' , 'ppResult' , ), 11007, (11007, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{915B275A-9C28-4898-93D2-C28DB53018E2}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyPulleyFlange' , 'strName' , 'pBNPBodySurface' , 'ppResult' , ), 11008, (11008, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (16393, 10, None, "IID('{FFD05BAA-458B-4C65-AF21-DF21C3C5FA4D}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyPulleyV' , 'strName' , 'pPoint' , 'ppResult' , ), 11009, (11009, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{DF52F1D2-21BC-4B10-989F-1C434899404A}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyPulleyRibbedV' , 'strName' , 'pPoint' , 'ppResult' , ), 11010, (11010, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{57849CE0-405E-474C-B4C1-65523C6DEE04}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyPulleyTiming' , 'strName' , 'pPoint' , 'ppResult' , ), 11011, (11011, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{6CAB2527-B23C-46F2-9E3F-9D793E4950EA}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CreateBNPAssembly' , 'strName' , 'pBeltClone' , 'pBodyList' , 'pInOutList' , 
			 'uiNumberOfBelt' , 'ppResult' , ), 11012, (11012, (), [ (8, 1, None, None) , (9, 1, None, "IID('{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}')") , 
			 (8204, 1, None, None) , (8204, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'BeltCloneCollection' , 'ppVal' , ), 11013, (11013, (), [ (16393, 10, None, "IID('{7309E615-192D-406B-9F7A-AFF15939E207}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'AssemblyCollection' , 'ppVal' , ), 11014, (11014, (), [ (16393, 10, None, "IID('{9CE8D58D-66F0-42F7-991B-2BDE5CB7E940}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'BNPBodyCollection' , 'ppVal' , ), 11015, (11015, (), [ (16393, 10, None, "IID('{DE7BC821-F8B2-493F-A604-08BC45622B02}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorSpeed' , 'strName' , 'pPosition' , 'pDirection' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 11016, (11016, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{CCB7E742-F0DF-4F22-A377-04AA675FD281}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorDistance' , 'strName' , 'pPosition' , 'pDirection' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 11017, (11017, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{0CC3861B-CC2A-4402-9135-C8BC804EABBD}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorSlip' , 'strName' , 'pPosition' , 'pSlipEntity' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 11018, (11018, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{08675B12-6A90-4082-BAED-E54382FDF107}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorTension' , 'strName' , 'pPosition' , 'pEntity' , 'dRange' , 
			 'ppVal' , ), 11019, (11019, (), [ (8, 1, None, None) , (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{55C49622-A503-4651-BF1E-2A84CD9E27AB}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorDisplacement' , 'strName' , 'pEntity' , 'pSensorMarker' , 'dRange' , 
			 'ppVal' , ), 11020, (11020, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{08F5AF0B-ADB1-4AB4-8FAB-54ADCB9B5F36}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorFixed' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 11021, (11021, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{39059D2F-DBEC-49DD-BFF2-AC0185541C99}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorRevolute' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 11022, (11022, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{D24BBA28-623F-4F1C-97D5-021413EB6736}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorSpring' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pBaseRefFrame' , 
			 'pActionRefFrame' , 'ppResult' , ), 11023, (11023, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{93A5A572-A6DD-4F12-A3E5-64F95B78718F}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorBushing' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 11024, (11024, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{F5A169B5-B529-4935-8B06-ACDD2A0BA456}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Contour' , 'ppVal' , ), 11025, (11025, (), [ (16393, 10, None, "IID('{BDF4F979-28B7-48D2-BF06-9C59B70D467B}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'CreateBNPAssembly2D' , 'strName' , 'pBeltClone' , 'pBodyList' , 'pInOutList' , 
			 'pDirection' , 'uiNumberOfBelt' , 'ppResult' , ), 11026, (11026, (), [ (8, 1, None, None) , 
			 (9, 1, None, "IID('{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}')") , (8204, 1, None, None) , (8204, 1, None, None) , (8197, 1, None, None) , (19, 1, None, None) , 
			 (16393, 10, None, "IID('{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}')") , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Assembly2DCollection' , 'ppVal' , ), 11027, (11027, (), [ (16393, 10, None, "IID('{D857EC59-8A2A-4228-99C9-07F5E95B84B0}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeltBeam' , 'strName' , 'pMultiPoint' , 'ppResult' , ), 11028, (11028, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}')") , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeltShell' , 'strName' , 'pMultiPoint' , 'ppResult' , ), 11029, (11029, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{AE6E5127-052C-43DC-B39E-9C19E632FC4A}')") , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'CreateBNPBeltGroup' , 'strName' , 'pBodyList' , 'pInOutList' , 'ppResult' , 
			 ), 11030, (11030, (), [ (8, 1, None, None) , (8204, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{80511C7B-B89C-4FA4-B21C-A9A7182B0E61}')") , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'CreateBody2DLinearGuide' , 'strName' , 'pPoint' , 'ppResult' , ), 11031, (11031, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{6496CE67-5383-4DDF-9FA1-CC2614D1B96C}')") , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'CreateBody2DArcGuide' , 'strName' , 'pPoint' , 'ppResult' , ), 11032, (11032, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{3CD85FDD-669E-47E0-A0BC-165B3BACBAC5}')") , ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeltBeam2' , 'strName' , 'pMultiBodyPoint' , 'pInOutList' , 'ppResult' , 
			 ), 11033, (11033, (), [ (8, 1, None, None) , (8204, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}')") , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeltShell2' , 'strName' , 'pMultiBodyPoint' , 'pInOutList' , 'ppResult' , 
			 ), 11034, (11034, (), [ (8, 1, None, None) , (8204, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{AE6E5127-052C-43DC-B39E-9C19E632FC4A}')") , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeltBeam3' , 'strName' , 'pMultiBodyPoint' , 'pInOutList' , 'uiNumberOfElements' , 
			 'dLowerThickness' , 'dUpperThickness' , 'ppResult' , ), 11035, (11035, (), [ (8, 1, None, None) , 
			 (8204, 1, None, None) , (8204, 1, None, None) , (19, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , 
			 (16393, 10, None, "IID('{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}')") , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyBeltShell3' , 'strName' , 'pMultiBodyPoint' , 'pInOutList' , 'uiNumberOfElementsLongitudinal' , 
			 'uiNumberOfElementsLateral' , 'dThickness' , 'dWidth' , 'ppResult' , ), 11036, (11036, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (8204, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , 
			 (5, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{AE6E5127-052C-43DC-B39E-9C19E632FC4A}')") , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'CreateBNPAssemblyWithAutomaticTimingPulleyAlignment' , 'strName' , 'pBeltClone' , 'pBodyList' , 'pInOutList' , 
			 'uiNumberOfBelt' , 'ppResult' , ), 11037, (11037, (), [ (8, 1, None, None) , (9, 1, None, "IID('{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}')") , 
			 (8204, 1, None, None) , (8204, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}')") , ], 1 , 1 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{E2EB7072-FAB5-4AAE-8E30-4DABC6A590BA}' : IBNPContactFriction,
	'{06D06385-6578-48E1-AACC-2BB6BD56B20A}' : IBNPContactProperty,
	'{2391593F-3C53-4F17-8285-F2857B2229C7}' : IBNPContactDirection,
	'{A111AE4E-7116-496C-BA07-1B125F33ECEA}' : IBNPConnectingParameters,
	'{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}' : IBNPContactSearch,
	'{7E83926D-1A31-4FC1-B317-411A03FF7DF8}' : IBNPBody,
	'{8ED56403-6EF8-4451-9CA4-7DBE298F4FE5}' : IBNPBodyBelt,
	'{DE7BC821-F8B2-493F-A604-08BC45622B02}' : IBNPBodyCollection,
	'{530E037B-C319-4E08-A507-77020D1582D4}' : IBNPGeometryPulleyRoller,
	'{DFFBFB64-8139-4586-A092-98FFE8D298DA}' : IBNPProfile,
	'{94B262DF-F40E-41A3-AEBF-98580C067EE0}' : IBNPProfileBeltTiming,
	'{D5E4799C-AD42-492B-BF4F-C9B2AEAD3917}' : IBNPProfilePulleyCrown,
	'{1FA326B0-7EA6-4D8C-A58B-7E69947E8B6D}' : IBNPProfilePulleyPrism,
	'{3218112D-CC7E-4DC3-A6A4-36A6B33C12B6}' : IBNPProfileBeamTiming,
	'{D9C23616-C0D3-422D-8A74-02654AB2E863}' : IBNPBeltBeamMaterialProperty,
	'{4FD6E858-87DC-4106-858F-F8CF4C6E60D5}' : IBNPBeltGroupMaterialProperty,
	'{9BC7A528-18AE-43FF-B8FF-81EBDAF0F812}' : IBNPBeltShellMaterialProperty,
	'{7ACC0B53-41A1-45D3-A170-8C7FD07C4E66}' : IBNPGeometryPulleyCrown,
	'{CAFDBC3C-C51A-412A-80E1-7F58BB60F820}' : IBNPGeometryPulleyPrism,
	'{D15BA410-27CD-4BBF-8B63-7157B683989A}' : IBNPGeometryPulleyFlange,
	'{CB8A9B5A-33D9-4AE8-8EB6-AE1CD753C5AF}' : IBNPGeometryPulleyV,
	'{32EA063C-BD96-48EA-93C6-C3DAA3961197}' : IBNPGeometryPulleyRibbedV,
	'{73E882E6-E6A2-41EB-B965-F386ADD519E8}' : IBNPGeometryPulleyTiming,
	'{0AF5EA96-DFB9-43D4-925C-CEC2CB1EB928}' : IBNPBodyPulley,
	'{FB9C36C7-777E-4F21-92B5-662D9B696B9F}' : IBNPBodyPulleyRoller,
	'{1640FE01-608A-4380-B9EF-6C40A8DC5B57}' : IBNPBodyPulleyCrown,
	'{915B275A-9C28-4898-93D2-C28DB53018E2}' : IBNPBodyPulleyPrism,
	'{FFD05BAA-458B-4C65-AF21-DF21C3C5FA4D}' : IBNPBodyPulleyFlange,
	'{DF52F1D2-21BC-4B10-989F-1C434899404A}' : IBNPBodyPulleyV,
	'{57849CE0-405E-474C-B4C1-65523C6DEE04}' : IBNPBodyPulleyRibbedV,
	'{6CAB2527-B23C-46F2-9E3F-9D793E4950EA}' : IBNPBodyPulleyTiming,
	'{97BC1771-06D1-4B98-B91C-3B78C3E47C95}' : IBNPGeometry2DGuide,
	'{28DFE5F6-D718-4CD5-AA3B-4CC4538DEB62}' : IBNPGeometry2DGuideArc,
	'{6E62C6CA-9D43-4D53-A2B1-4BEFD6DE5D22}' : IBNPGeometry2DGuideLinear,
	'{9033BB6E-5115-49FA-83A2-E39301FBFD6C}' : IBNPGeometryBeltFlat,
	'{185F6935-19D9-4664-91A4-C564A61DF014}' : IBNPGeometryBeltV,
	'{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}' : IBNPGeometryBeltRibbedV,
	'{28B9F577-7066-4B2E-80A2-AF7D140593AC}' : IBNPGeometryBeltTiming,
	'{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}' : IBNPPassingBodyCollection,
	'{64E4D842-5C51-484B-B3F8-C54D097BBDA1}' : IBNPGeometryBeltBeam,
	'{FD1CA7C1-21FE-488D-88DC-87AF6CC66D8E}' : IBNPGeometryBeltShell,
	'{0711C396-7AF8-4A58-A98E-EDC99123FB42}' : IBNPContactNodePropertyBeltFlat,
	'{7AE525B3-FE13-4117-809E-476C72E2847C}' : IBNPContactNodePropertyBeltV,
	'{ABC5653E-52A2-4028-AE40-3738D348CF0D}' : IBNPContactNodePropertyBeltRibbedV,
	'{C687377E-15AA-4340-A9F5-DB9CB8F4C9DA}' : IBNPBeltGroupContactPoint,
	'{EFB4D776-2786-4A6D-BF68-A50DE0B265E2}' : IBNPBodyBeltFlat,
	'{147D3D43-46A0-4F8F-8BC8-F8554A9EC105}' : IBNPBodyBeltV,
	'{ADEA5DA8-03AA-4840-B783-E04A9840F972}' : IBNPBodyBeltRibbedV,
	'{776A8BE0-9FC0-4A70-983E-7015F0EC7EF0}' : IBNPBodyBeltTiming,
	'{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}' : IBNPBodyBeltBeam,
	'{AE6E5127-052C-43DC-B39E-9C19E632FC4A}' : IBNPBodyBeltShell,
	'{3285D284-E32D-4EA9-B44D-1490297A25BF}' : IBNPBody2DGuide,
	'{3CD85FDD-669E-47E0-A0BC-165B3BACBAC5}' : IBNPBody2DGuideArc,
	'{6496CE67-5383-4DDF-9FA1-CC2614D1B96C}' : IBNPBody2DGuideLinear,
	'{B49E6018-2162-41C9-9AC4-AF610E2E2356}' : IBNPBodyBeltCollection,
	'{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}' : IBNPBeltClone,
	'{F60BB117-D220-4FD8-B603-74573A033D40}' : IBNPBeltCloneFlat,
	'{8FC53768-BC25-4B05-BE34-6E537955559C}' : IBNPBeltCloneV,
	'{1DD37F48-A065-4B60-BA2D-5A2BFB10AB67}' : IBNPBeltCloneRibbedV,
	'{7D32C453-E2E6-413F-8F69-C66F17CE38C6}' : IBNPBeltCloneTiming,
	'{7309E615-192D-406B-9F7A-AFF15939E207}' : IBNPBeltCloneCollection,
	'{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}' : IBNPAssembly,
	'{E789A6A6-79B6-49EE-B0C4-EC84A24499B1}' : IBNPAssemblyConnectingForceParameter,
	'{9CE8D58D-66F0-42F7-991B-2BDE5CB7E940}' : IBNPAssemblyCollection,
	'{4C336B22-AB0D-4922-B913-91F61EB5C6CB}' : IBNPAssembly2DBushingForceParameter,
	'{80511C7B-B89C-4FA4-B21C-A9A7182B0E61}' : IBNPBeltGroup,
	'{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}' : IBNPAssembly2D,
	'{D857EC59-8A2A-4228-99C9-07F5E95B84B0}' : IBNPAssembly2DCollection,
	'{9E5B67A9-F6AF-4BDE-B7F5-FD7926E2B2CC}' : IBNPSubSystem,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{E2EB7072-FAB5-4AAE-8E30-4DABC6A590BA}' : 'IBNPContactFriction',
	'{06D06385-6578-48E1-AACC-2BB6BD56B20A}' : 'IBNPContactProperty',
	'{2391593F-3C53-4F17-8285-F2857B2229C7}' : 'IBNPContactDirection',
	'{A111AE4E-7116-496C-BA07-1B125F33ECEA}' : 'IBNPConnectingParameters',
	'{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}' : 'IBNPContactSearch',
	'{7E83926D-1A31-4FC1-B317-411A03FF7DF8}' : 'IBNPBody',
	'{8ED56403-6EF8-4451-9CA4-7DBE298F4FE5}' : 'IBNPBodyBelt',
	'{DE7BC821-F8B2-493F-A604-08BC45622B02}' : 'IBNPBodyCollection',
	'{530E037B-C319-4E08-A507-77020D1582D4}' : 'IBNPGeometryPulleyRoller',
	'{DFFBFB64-8139-4586-A092-98FFE8D298DA}' : 'IBNPProfile',
	'{94B262DF-F40E-41A3-AEBF-98580C067EE0}' : 'IBNPProfileBeltTiming',
	'{D5E4799C-AD42-492B-BF4F-C9B2AEAD3917}' : 'IBNPProfilePulleyCrown',
	'{1FA326B0-7EA6-4D8C-A58B-7E69947E8B6D}' : 'IBNPProfilePulleyPrism',
	'{3218112D-CC7E-4DC3-A6A4-36A6B33C12B6}' : 'IBNPProfileBeamTiming',
	'{D9C23616-C0D3-422D-8A74-02654AB2E863}' : 'IBNPBeltBeamMaterialProperty',
	'{4FD6E858-87DC-4106-858F-F8CF4C6E60D5}' : 'IBNPBeltGroupMaterialProperty',
	'{9BC7A528-18AE-43FF-B8FF-81EBDAF0F812}' : 'IBNPBeltShellMaterialProperty',
	'{7ACC0B53-41A1-45D3-A170-8C7FD07C4E66}' : 'IBNPGeometryPulleyCrown',
	'{CAFDBC3C-C51A-412A-80E1-7F58BB60F820}' : 'IBNPGeometryPulleyPrism',
	'{D15BA410-27CD-4BBF-8B63-7157B683989A}' : 'IBNPGeometryPulleyFlange',
	'{CB8A9B5A-33D9-4AE8-8EB6-AE1CD753C5AF}' : 'IBNPGeometryPulleyV',
	'{32EA063C-BD96-48EA-93C6-C3DAA3961197}' : 'IBNPGeometryPulleyRibbedV',
	'{73E882E6-E6A2-41EB-B965-F386ADD519E8}' : 'IBNPGeometryPulleyTiming',
	'{0AF5EA96-DFB9-43D4-925C-CEC2CB1EB928}' : 'IBNPBodyPulley',
	'{FB9C36C7-777E-4F21-92B5-662D9B696B9F}' : 'IBNPBodyPulleyRoller',
	'{1640FE01-608A-4380-B9EF-6C40A8DC5B57}' : 'IBNPBodyPulleyCrown',
	'{915B275A-9C28-4898-93D2-C28DB53018E2}' : 'IBNPBodyPulleyPrism',
	'{FFD05BAA-458B-4C65-AF21-DF21C3C5FA4D}' : 'IBNPBodyPulleyFlange',
	'{DF52F1D2-21BC-4B10-989F-1C434899404A}' : 'IBNPBodyPulleyV',
	'{57849CE0-405E-474C-B4C1-65523C6DEE04}' : 'IBNPBodyPulleyRibbedV',
	'{6CAB2527-B23C-46F2-9E3F-9D793E4950EA}' : 'IBNPBodyPulleyTiming',
	'{97BC1771-06D1-4B98-B91C-3B78C3E47C95}' : 'IBNPGeometry2DGuide',
	'{28DFE5F6-D718-4CD5-AA3B-4CC4538DEB62}' : 'IBNPGeometry2DGuideArc',
	'{6E62C6CA-9D43-4D53-A2B1-4BEFD6DE5D22}' : 'IBNPGeometry2DGuideLinear',
	'{9033BB6E-5115-49FA-83A2-E39301FBFD6C}' : 'IBNPGeometryBeltFlat',
	'{185F6935-19D9-4664-91A4-C564A61DF014}' : 'IBNPGeometryBeltV',
	'{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}' : 'IBNPGeometryBeltRibbedV',
	'{28B9F577-7066-4B2E-80A2-AF7D140593AC}' : 'IBNPGeometryBeltTiming',
	'{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}' : 'IBNPPassingBodyCollection',
	'{64E4D842-5C51-484B-B3F8-C54D097BBDA1}' : 'IBNPGeometryBeltBeam',
	'{FD1CA7C1-21FE-488D-88DC-87AF6CC66D8E}' : 'IBNPGeometryBeltShell',
	'{0711C396-7AF8-4A58-A98E-EDC99123FB42}' : 'IBNPContactNodePropertyBeltFlat',
	'{7AE525B3-FE13-4117-809E-476C72E2847C}' : 'IBNPContactNodePropertyBeltV',
	'{ABC5653E-52A2-4028-AE40-3738D348CF0D}' : 'IBNPContactNodePropertyBeltRibbedV',
	'{C687377E-15AA-4340-A9F5-DB9CB8F4C9DA}' : 'IBNPBeltGroupContactPoint',
	'{EFB4D776-2786-4A6D-BF68-A50DE0B265E2}' : 'IBNPBodyBeltFlat',
	'{147D3D43-46A0-4F8F-8BC8-F8554A9EC105}' : 'IBNPBodyBeltV',
	'{ADEA5DA8-03AA-4840-B783-E04A9840F972}' : 'IBNPBodyBeltRibbedV',
	'{776A8BE0-9FC0-4A70-983E-7015F0EC7EF0}' : 'IBNPBodyBeltTiming',
	'{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}' : 'IBNPBodyBeltBeam',
	'{AE6E5127-052C-43DC-B39E-9C19E632FC4A}' : 'IBNPBodyBeltShell',
	'{3285D284-E32D-4EA9-B44D-1490297A25BF}' : 'IBNPBody2DGuide',
	'{3CD85FDD-669E-47E0-A0BC-165B3BACBAC5}' : 'IBNPBody2DGuideArc',
	'{6496CE67-5383-4DDF-9FA1-CC2614D1B96C}' : 'IBNPBody2DGuideLinear',
	'{B49E6018-2162-41C9-9AC4-AF610E2E2356}' : 'IBNPBodyBeltCollection',
	'{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}' : 'IBNPBeltClone',
	'{F60BB117-D220-4FD8-B603-74573A033D40}' : 'IBNPBeltCloneFlat',
	'{8FC53768-BC25-4B05-BE34-6E537955559C}' : 'IBNPBeltCloneV',
	'{1DD37F48-A065-4B60-BA2D-5A2BFB10AB67}' : 'IBNPBeltCloneRibbedV',
	'{7D32C453-E2E6-413F-8F69-C66F17CE38C6}' : 'IBNPBeltCloneTiming',
	'{7309E615-192D-406B-9F7A-AFF15939E207}' : 'IBNPBeltCloneCollection',
	'{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}' : 'IBNPAssembly',
	'{E789A6A6-79B6-49EE-B0C4-EC84A24499B1}' : 'IBNPAssemblyConnectingForceParameter',
	'{9CE8D58D-66F0-42F7-991B-2BDE5CB7E940}' : 'IBNPAssemblyCollection',
	'{4C336B22-AB0D-4922-B913-91F61EB5C6CB}' : 'IBNPAssembly2DBushingForceParameter',
	'{80511C7B-B89C-4FA4-B21C-A9A7182B0E61}' : 'IBNPBeltGroup',
	'{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}' : 'IBNPAssembly2D',
	'{D857EC59-8A2A-4228-99C9-07F5E95B84B0}' : 'IBNPAssembly2DCollection',
	'{9E5B67A9-F6AF-4BDE-B7F5-FD7926E2B2CC}' : 'IBNPSubSystem',
}


NamesToIIDMap = {
	'IBNPContactFriction' : '{E2EB7072-FAB5-4AAE-8E30-4DABC6A590BA}',
	'IBNPContactProperty' : '{06D06385-6578-48E1-AACC-2BB6BD56B20A}',
	'IBNPContactDirection' : '{2391593F-3C53-4F17-8285-F2857B2229C7}',
	'IBNPConnectingParameters' : '{A111AE4E-7116-496C-BA07-1B125F33ECEA}',
	'IBNPContactSearch' : '{8AF5B5D5-1462-4B8F-9B94-C8647AE1C058}',
	'IBNPBody' : '{7E83926D-1A31-4FC1-B317-411A03FF7DF8}',
	'IBNPBodyBelt' : '{8ED56403-6EF8-4451-9CA4-7DBE298F4FE5}',
	'IBNPBodyCollection' : '{DE7BC821-F8B2-493F-A604-08BC45622B02}',
	'IBNPGeometryPulleyRoller' : '{530E037B-C319-4E08-A507-77020D1582D4}',
	'IBNPProfile' : '{DFFBFB64-8139-4586-A092-98FFE8D298DA}',
	'IBNPProfileBeltTiming' : '{94B262DF-F40E-41A3-AEBF-98580C067EE0}',
	'IBNPProfilePulleyCrown' : '{D5E4799C-AD42-492B-BF4F-C9B2AEAD3917}',
	'IBNPProfilePulleyPrism' : '{1FA326B0-7EA6-4D8C-A58B-7E69947E8B6D}',
	'IBNPProfileBeamTiming' : '{3218112D-CC7E-4DC3-A6A4-36A6B33C12B6}',
	'IBNPBeltBeamMaterialProperty' : '{D9C23616-C0D3-422D-8A74-02654AB2E863}',
	'IBNPBeltGroupMaterialProperty' : '{4FD6E858-87DC-4106-858F-F8CF4C6E60D5}',
	'IBNPBeltShellMaterialProperty' : '{9BC7A528-18AE-43FF-B8FF-81EBDAF0F812}',
	'IBNPGeometryPulleyCrown' : '{7ACC0B53-41A1-45D3-A170-8C7FD07C4E66}',
	'IBNPGeometryPulleyPrism' : '{CAFDBC3C-C51A-412A-80E1-7F58BB60F820}',
	'IBNPGeometryPulleyFlange' : '{D15BA410-27CD-4BBF-8B63-7157B683989A}',
	'IBNPGeometryPulleyV' : '{CB8A9B5A-33D9-4AE8-8EB6-AE1CD753C5AF}',
	'IBNPGeometryPulleyRibbedV' : '{32EA063C-BD96-48EA-93C6-C3DAA3961197}',
	'IBNPGeometryPulleyTiming' : '{73E882E6-E6A2-41EB-B965-F386ADD519E8}',
	'IBNPBodyPulley' : '{0AF5EA96-DFB9-43D4-925C-CEC2CB1EB928}',
	'IBNPBodyPulleyRoller' : '{FB9C36C7-777E-4F21-92B5-662D9B696B9F}',
	'IBNPBodyPulleyCrown' : '{1640FE01-608A-4380-B9EF-6C40A8DC5B57}',
	'IBNPBodyPulleyPrism' : '{915B275A-9C28-4898-93D2-C28DB53018E2}',
	'IBNPBodyPulleyFlange' : '{FFD05BAA-458B-4C65-AF21-DF21C3C5FA4D}',
	'IBNPBodyPulleyV' : '{DF52F1D2-21BC-4B10-989F-1C434899404A}',
	'IBNPBodyPulleyRibbedV' : '{57849CE0-405E-474C-B4C1-65523C6DEE04}',
	'IBNPBodyPulleyTiming' : '{6CAB2527-B23C-46F2-9E3F-9D793E4950EA}',
	'IBNPGeometry2DGuide' : '{97BC1771-06D1-4B98-B91C-3B78C3E47C95}',
	'IBNPGeometry2DGuideArc' : '{28DFE5F6-D718-4CD5-AA3B-4CC4538DEB62}',
	'IBNPGeometry2DGuideLinear' : '{6E62C6CA-9D43-4D53-A2B1-4BEFD6DE5D22}',
	'IBNPGeometryBeltFlat' : '{9033BB6E-5115-49FA-83A2-E39301FBFD6C}',
	'IBNPGeometryBeltV' : '{185F6935-19D9-4664-91A4-C564A61DF014}',
	'IBNPGeometryBeltRibbedV' : '{087D45C5-BCA8-4FB8-90B7-90EEA414EDB2}',
	'IBNPGeometryBeltTiming' : '{28B9F577-7066-4B2E-80A2-AF7D140593AC}',
	'IBNPPassingBodyCollection' : '{6DB95EEE-D599-4BD5-B8DE-D2E19FC5CDF0}',
	'IBNPGeometryBeltBeam' : '{64E4D842-5C51-484B-B3F8-C54D097BBDA1}',
	'IBNPGeometryBeltShell' : '{FD1CA7C1-21FE-488D-88DC-87AF6CC66D8E}',
	'IBNPContactNodePropertyBeltFlat' : '{0711C396-7AF8-4A58-A98E-EDC99123FB42}',
	'IBNPContactNodePropertyBeltV' : '{7AE525B3-FE13-4117-809E-476C72E2847C}',
	'IBNPContactNodePropertyBeltRibbedV' : '{ABC5653E-52A2-4028-AE40-3738D348CF0D}',
	'IBNPBeltGroupContactPoint' : '{C687377E-15AA-4340-A9F5-DB9CB8F4C9DA}',
	'IBNPBodyBeltFlat' : '{EFB4D776-2786-4A6D-BF68-A50DE0B265E2}',
	'IBNPBodyBeltV' : '{147D3D43-46A0-4F8F-8BC8-F8554A9EC105}',
	'IBNPBodyBeltRibbedV' : '{ADEA5DA8-03AA-4840-B783-E04A9840F972}',
	'IBNPBodyBeltTiming' : '{776A8BE0-9FC0-4A70-983E-7015F0EC7EF0}',
	'IBNPBodyBeltBeam' : '{F5B0F0BC-1BA8-45C7-8DBD-0853264FF94A}',
	'IBNPBodyBeltShell' : '{AE6E5127-052C-43DC-B39E-9C19E632FC4A}',
	'IBNPBody2DGuide' : '{3285D284-E32D-4EA9-B44D-1490297A25BF}',
	'IBNPBody2DGuideArc' : '{3CD85FDD-669E-47E0-A0BC-165B3BACBAC5}',
	'IBNPBody2DGuideLinear' : '{6496CE67-5383-4DDF-9FA1-CC2614D1B96C}',
	'IBNPBodyBeltCollection' : '{B49E6018-2162-41C9-9AC4-AF610E2E2356}',
	'IBNPBeltClone' : '{CF75FB5E-F7B8-4C82-AF46-C6B7B0B74892}',
	'IBNPBeltCloneFlat' : '{F60BB117-D220-4FD8-B603-74573A033D40}',
	'IBNPBeltCloneV' : '{8FC53768-BC25-4B05-BE34-6E537955559C}',
	'IBNPBeltCloneRibbedV' : '{1DD37F48-A065-4B60-BA2D-5A2BFB10AB67}',
	'IBNPBeltCloneTiming' : '{7D32C453-E2E6-413F-8F69-C66F17CE38C6}',
	'IBNPBeltCloneCollection' : '{7309E615-192D-406B-9F7A-AFF15939E207}',
	'IBNPAssembly' : '{E7B4F8B6-2EC5-4157-9F0E-B8B9F9F46E66}',
	'IBNPAssemblyConnectingForceParameter' : '{E789A6A6-79B6-49EE-B0C4-EC84A24499B1}',
	'IBNPAssemblyCollection' : '{9CE8D58D-66F0-42F7-991B-2BDE5CB7E940}',
	'IBNPAssembly2DBushingForceParameter' : '{4C336B22-AB0D-4922-B913-91F61EB5C6CB}',
	'IBNPBeltGroup' : '{80511C7B-B89C-4FA4-B21C-A9A7182B0E61}',
	'IBNPAssembly2D' : '{8FE4279C-158C-4D8A-B726-1A3689B0DAA0}',
	'IBNPAssembly2DCollection' : '{D857EC59-8A2A-4228-99C9-07F5E95B84B0}',
	'IBNPSubSystem' : '{9E5B67A9-F6AF-4BDE-B7F5-FD7926E2B2CC}',
}


