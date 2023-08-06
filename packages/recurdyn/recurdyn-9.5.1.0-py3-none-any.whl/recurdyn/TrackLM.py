# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMTrackLM.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5 RecurDynCOMTrackLM Type Library'
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

CLSID = IID('{1F0C0252-BCB0-47B5-9772-A0EE63319707}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class ContactParameterSoftGroundType(IntEnum):
	'''
	ContactParameterSoftGroundType enumeration.
	'''
	ContactParameterSoftGroundType_Clayey_Soil=4         
	'''Constant value is 4.'''
	ContactParameterSoftGroundType_Dry_Sand=0         
	'''Constant value is 0.'''
	ContactParameterSoftGroundType_Grenville_Loam=11        
	'''Constant value is 11.'''
	ContactParameterSoftGroundType_Heavy_Clay=5         
	'''Constant value is 5.'''
	ContactParameterSoftGroundType_LETE_Sand=7         
	'''Constant value is 7.'''
	ContactParameterSoftGroundType_Lean_Clay=6         
	'''Constant value is 6.'''
	ContactParameterSoftGroundType_North_Gower_Clayey_Loam=10        
	'''Constant value is 10.'''
	ContactParameterSoftGroundType_Rubicon_Sandy_Loam=9         
	'''Constant value is 9.'''
	ContactParameterSoftGroundType_Sandy_Loam_Hanamoto=3         
	'''Constant value is 3.'''
	ContactParameterSoftGroundType_Sandy_Loam_LLL=1         
	'''Constant value is 1.'''
	ContactParameterSoftGroundType_Sandy_Loam_Michigan=2         
	'''Constant value is 2.'''
	ContactParameterSoftGroundType_Snow_Sweden=13        
	'''Constant value is 13.'''
	ContactParameterSoftGroundType_Snow_US=12        
	'''Constant value is 12.'''
	ContactParameterSoftGroundType_Upland_Sandy_Loam=8         
	'''Constant value is 8.'''
class ContactSearchType(IntEnum):
	'''
	ContactSearchType enumeration.
	'''
	ContactSearchType_FullSearch  =0         
	'''Constant value is 0.'''
	ContactSearchType_PartialSearch=1         
	'''Constant value is 1.'''
class ContactSprocketType(IntEnum):
	'''
	ContactSprocketType enumeration.
	'''
	ContactSprocketType_LeftPin   =0         
	'''Constant value is 0.'''
	ContactSprocketType_RightPin  =1         
	'''Constant value is 1.'''
class InOutType(IntEnum):
	'''
	InOutType enumeration.
	'''
	InOutType_In                  =0         
	'''Constant value is 0.'''
	InOutType_None                =2         
	'''Constant value is 2.'''
	InOutType_Out                 =1         
	'''Constant value is 1.'''
class RollerGuardInactiveType(IntEnum):
	'''
	RollerGuardInactiveType enumeration.
	'''
	RollerGuardInactiveType_Left_Inactive=1         
	'''Constant value is 1.'''
	RollerGuardInactiveType_None  =0         
	'''Constant value is 0.'''
	RollerGuardInactiveType_Right_Inactive=2         
	'''Constant value is 2.'''
class TrackLMFrictionType(IntEnum):
	'''
	TrackLMFrictionType enumeration.
	'''
	TrackLMFrictionType_DynamicFrictionCoefficient=0         
	'''Constant value is 0.'''
	TrackLMFrictionType_FrictionCoefficientSpline=2         
	'''Constant value is 2.'''
	TrackLMFrictionType_FrictionForceSpline=1         
	'''Constant value is 1.'''

from win32com.client import DispatchBaseClass
class IPassingBodyCollection(DispatchBaseClass):
	'''TrackLM passing body collection of assembly'''
	CLSID = IID('{94F9A0BC-94F5-4474-B550-1240D060FD26}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
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

class ITrackLMAssembly(DispatchBaseClass):
	'''TrackLM Assembly'''
	CLSID = IID('{F3294DCE-CF25-4511-986C-DC2D245853B1}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddAllOutputLink(self):
		'''
		Add all the link body to output list
		'''
		return self._oleobj_.InvokeTypes(5513, LCID, 1, (24, 0), (),)


	def AddOutputLink(self, strFileName):
		'''
		Add a link body to output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(5511, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def AddPassingBody(self, pVal):
		'''
		Add a passing body
		
		:param pVal: IBody
		'''
		return self._oleobj_.InvokeTypes(5503, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def AddPassingBody2(self, pVal):
		'''
		Add a passing body with ITrackLMBody
		
		:param pVal: ITrackLMBody
		'''
		return self._oleobj_.InvokeTypes(5522, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def CreateGrouserContact(self):
		'''
		Create a grouser contact
		
		:rtype: recurdyn.TrackLM.ITrackLMAssemblyGrouserContact
		'''
		ret = self._oleobj_.InvokeTypes(5515, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'CreateGrouserContact', '{41C77E5C-5A0D-4060-9668-47AAEE4E7575}')
		return ret

	def DeleteGrouserContact(self, pVal):
		'''
		Delete a grouser contact
		
		:param pVal: ITrackLMAssemblyGrouserContact
		'''
		return self._oleobj_.InvokeTypes(5516, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody(self, pVal):
		'''
		Delete a passing body
		
		:param pVal: IBody
		'''
		return self._oleobj_.InvokeTypes(5504, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody2(self, pVal):
		'''
		Delete a passing body with ITrackLMBody
		
		:param pVal: ITrackLMBody
		'''
		return self._oleobj_.InvokeTypes(5523, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetOutputLinkList(self):
		'''
		TrackLM assembly output list
		
		:rtype: list[str]
		'''
		return self._ApplyTypes_(5510, 1, (8200, 0), (), 'GetOutputLinkList', None,)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def RemoveAllOutputLink(self):
		'''
		Remove all the link body from output list
		'''
		return self._oleobj_.InvokeTypes(5514, LCID, 1, (24, 0), (),)


	def RemoveOutputLink(self, strFileName):
		'''
		Remove a link body from output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(5512, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def UpdateLinkInitialVelocity(self):
		'''
		Update initial velocity of links
		'''
		return self._oleobj_.InvokeTypes(5521, LCID, 1, (24, 0), (),)


	def _get_BushingForceCollection(self):
		return self._ApplyTypes_(*(5520, 2, (9, 0), (), "BushingForceCollection", '{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}'))
	def _get_BushingForceParameter(self):
		return self._ApplyTypes_(*(5509, 2, (9, 0), (), "BushingForceParameter", '{08A3F46B-C852-46F4-BCE6-11A84CFD7C2B}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "ContactParameter", '{C37B595D-DE29-465E-88F7-288C5C63D7F7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GrouserContactCollection(self):
		return self._ApplyTypes_(*(5517, 2, (9, 0), (), "GrouserContactCollection", '{68152AA0-4470-4F17-AEF7-F45AA9ABE529}'))
	def _get_GrouserContactProperty(self):
		return self._ApplyTypes_(*(5519, 2, (9, 0), (), "GrouserContactProperty", '{860E76B0-9B85-4973-AE10-CA2BD4FEA254}'))
	def _get_GrouserToSphereContact(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "GrouserToSphereContact", '{71434E11-33AF-44E5-B36F-D0D92753A768}'))
	def _get_LinkInitialVelocityXAxis(self):
		return self._ApplyTypes_(*(5507, 2, (9, 0), (), "LinkInitialVelocityXAxis", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LinkNumbers(self):
		return self._ApplyTypes_(*(5506, 2, (19, 0), (), "LinkNumbers", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PassingBodyCollection(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'))
	def _get_TrackLMBodyLinkCollection(self):
		return self._ApplyTypes_(*(5508, 2, (9, 0), (), "TrackLMBodyLinkCollection", '{7E3C5275-F00D-4675-BAF6-9AE63689F8D2}'))
	def _get_UseInactiveGrouserContact(self):
		return self._ApplyTypes_(*(5518, 2, (11, 0), (), "UseInactiveGrouserContact", None))
	def _get_UsePressureSinkage(self):
		return self._ApplyTypes_(*(5500, 2, (11, 0), (), "UsePressureSinkage", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseInactiveGrouserContact(self, value):
		if "UseInactiveGrouserContact" in self.__dict__: self.__dict__["UseInactiveGrouserContact"] = value; return
		self._oleobj_.Invoke(*((5518, LCID, 4, 0) + (value,) + ()))
	def _set_UsePressureSinkage(self, value):
		if "UsePressureSinkage" in self.__dict__: self.__dict__["UsePressureSinkage"] = value; return
		self._oleobj_.Invoke(*((5500, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BushingForceCollection = property(_get_BushingForceCollection, None)
	'''
	Bushing force collection

	:type: recurdyn.ProcessNet.IForceCollection
	'''
	BushingForceParameter = property(_get_BushingForceParameter, None)
	'''
	Bushing force parameter

	:type: recurdyn.TrackLM.ITrackLMAssemblyBushingForceParameter
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact ground track link shoe

	:type: recurdyn.TrackLM.ITrackLMAssemblyContactGroundTrackLinkShoe
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GrouserContactCollection = property(_get_GrouserContactCollection, None)
	'''
	Grouser contact collection

	:type: recurdyn.TrackLM.ITrackLMAssemblyGrouserContactCollection
	'''
	GrouserContactProperty = property(_get_GrouserContactProperty, None)
	'''
	Grouser contact property

	:type: recurdyn.TrackLM.ITrackLMGrouserContactProperty
	'''
	GrouserToSphereContact = property(_get_GrouserToSphereContact, None)
	'''
	Grouser to sphere contact Property

	:type: recurdyn.TrackLM.ITrackLMAssemblyGrouserToSphereContact
	'''
	LinkInitialVelocityXAxis = property(_get_LinkInitialVelocityXAxis, None)
	'''
	Link initial velocity x-axis

	:type: recurdyn.ProcessNet.IDouble
	'''
	LinkNumbers = property(_get_LinkNumbers, None)
	'''
	Link numbers

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
	PassingBodyCollection = property(_get_PassingBodyCollection, None)
	'''
	Passing body collection

	:type: recurdyn.ProcessNet.IBodyCollection
	'''
	TrackLMBodyLinkCollection = property(_get_TrackLMBodyLinkCollection, None)
	'''
	TrackLM body link collection

	:type: recurdyn.TrackLM.ITrackLMBodyLinkCollection
	'''
	UseInactiveGrouserContact = property(_get_UseInactiveGrouserContact, _set_UseInactiveGrouserContact)
	'''
	Use inactive grouser contact

	:type: bool
	'''
	UsePressureSinkage = property(_get_UsePressureSinkage, _set_UsePressureSinkage)
	'''
	Use pressur sinkage

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
		"_set_UseInactiveGrouserContact": _set_UseInactiveGrouserContact,
		"_set_UsePressureSinkage": _set_UsePressureSinkage,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BushingForceCollection": (5520, 2, (9, 0), (), "BushingForceCollection", '{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}'),
		"BushingForceParameter": (5509, 2, (9, 0), (), "BushingForceParameter", '{08A3F46B-C852-46F4-BCE6-11A84CFD7C2B}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (5501, 2, (9, 0), (), "ContactParameter", '{C37B595D-DE29-465E-88F7-288C5C63D7F7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GrouserContactCollection": (5517, 2, (9, 0), (), "GrouserContactCollection", '{68152AA0-4470-4F17-AEF7-F45AA9ABE529}'),
		"GrouserContactProperty": (5519, 2, (9, 0), (), "GrouserContactProperty", '{860E76B0-9B85-4973-AE10-CA2BD4FEA254}'),
		"GrouserToSphereContact": (5505, 2, (9, 0), (), "GrouserToSphereContact", '{71434E11-33AF-44E5-B36F-D0D92753A768}'),
		"LinkInitialVelocityXAxis": (5507, 2, (9, 0), (), "LinkInitialVelocityXAxis", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LinkNumbers": (5506, 2, (19, 0), (), "LinkNumbers", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PassingBodyCollection": (5502, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'),
		"TrackLMBodyLinkCollection": (5508, 2, (9, 0), (), "TrackLMBodyLinkCollection", '{7E3C5275-F00D-4675-BAF6-9AE63689F8D2}'),
		"UseInactiveGrouserContact": (5518, 2, (11, 0), (), "UseInactiveGrouserContact", None),
		"UsePressureSinkage": (5500, 2, (11, 0), (), "UsePressureSinkage", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseInactiveGrouserContact": ((5518, LCID, 4, 0),()),
		"UsePressureSinkage": ((5500, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMAssemblyBushingForceParameter(DispatchBaseClass):
	'''TrackLM Assembly Bushing Force Parameter'''
	CLSID = IID('{08A3F46B-C852-46F4-BCE6-11A84CFD7C2B}')
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
		Export bushing force parameter
		
		:param strName: str
		:param val: bool
		'''
		return self._oleobj_.InvokeTypes(5548, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import bushing force parameter
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(5549, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_RotationDampingCoefficientX(self):
		return self._ApplyTypes_(*(5520, 2, (9, 0), (), "RotationDampingCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingCoefficientY(self):
		return self._ApplyTypes_(*(5521, 2, (9, 0), (), "RotationDampingCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingCoefficientZ(self):
		return self._ApplyTypes_(*(5522, 2, (9, 0), (), "RotationDampingCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponentX(self):
		return self._ApplyTypes_(*(5545, 2, (9, 0), (), "RotationDampingExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponentY(self):
		return self._ApplyTypes_(*(5546, 2, (9, 0), (), "RotationDampingExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponentZ(self):
		return self._ApplyTypes_(*(5547, 2, (9, 0), (), "RotationDampingExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingSplineX(self):
		return self._ApplyTypes_(*(5524, 2, (9, 0), (), "RotationDampingSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationDampingSplineY(self):
		return self._ApplyTypes_(*(5525, 2, (9, 0), (), "RotationDampingSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationDampingSplineZ(self):
		return self._ApplyTypes_(*(5526, 2, (9, 0), (), "RotationDampingSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationPreloadX(self):
		return self._ApplyTypes_(*(5527, 2, (9, 0), (), "RotationPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationPreloadY(self):
		return self._ApplyTypes_(*(5528, 2, (9, 0), (), "RotationPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationPreloadZ(self):
		return self._ApplyTypes_(*(5529, 2, (9, 0), (), "RotationPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationPresetAngle(self):
		return self._ApplyTypes_(*(5530, 2, (9, 0), (), "RotationPresetAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessCoefficientX(self):
		return self._ApplyTypes_(*(5513, 2, (9, 0), (), "RotationStiffnessCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessCoefficientY(self):
		return self._ApplyTypes_(*(5514, 2, (9, 0), (), "RotationStiffnessCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessCoefficientZ(self):
		return self._ApplyTypes_(*(5515, 2, (9, 0), (), "RotationStiffnessCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponentX(self):
		return self._ApplyTypes_(*(5541, 2, (9, 0), (), "RotationStiffnessExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponentY(self):
		return self._ApplyTypes_(*(5542, 2, (9, 0), (), "RotationStiffnessExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponentZ(self):
		return self._ApplyTypes_(*(5543, 2, (9, 0), (), "RotationStiffnessExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessSplineX(self):
		return self._ApplyTypes_(*(5517, 2, (9, 0), (), "RotationStiffnessSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationStiffnessSplineY(self):
		return self._ApplyTypes_(*(5518, 2, (9, 0), (), "RotationStiffnessSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationStiffnessSplineZ(self):
		return self._ApplyTypes_(*(5519, 2, (9, 0), (), "RotationStiffnessSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationStopAngle(self):
		return self._ApplyTypes_(*(5532, 2, (9, 0), (), "RotationStopAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStopStiffnessFactor(self):
		return self._ApplyTypes_(*(5533, 2, (9, 0), (), "RotationStopStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationClearance(self):
		return self._ApplyTypes_(*(5512, 2, (9, 0), (), "TranslationClearance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingCoefficientAxial(self):
		return self._ApplyTypes_(*(5506, 2, (9, 0), (), "TranslationDampingCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingCoefficientRadial(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "TranslationDampingCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingExponentAxial(self):
		return self._ApplyTypes_(*(5539, 2, (9, 0), (), "TranslationDampingExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingExponentRadial(self):
		return self._ApplyTypes_(*(5538, 2, (9, 0), (), "TranslationDampingExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingSplineAxial(self):
		return self._ApplyTypes_(*(5509, 2, (9, 0), (), "TranslationDampingSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationDampingSplineRadial(self):
		return self._ApplyTypes_(*(5508, 2, (9, 0), (), "TranslationDampingSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationPreloadAxial(self):
		return self._ApplyTypes_(*(5511, 2, (9, 0), (), "TranslationPreloadAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationPreloadRadial(self):
		return self._ApplyTypes_(*(5510, 2, (9, 0), (), "TranslationPreloadRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessCoefficientAxial(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "TranslationStiffnessCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessCoefficientRadial(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "TranslationStiffnessCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessExponentAxial(self):
		return self._ApplyTypes_(*(5536, 2, (9, 0), (), "TranslationStiffnessExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessExponentRadial(self):
		return self._ApplyTypes_(*(5535, 2, (9, 0), (), "TranslationStiffnessExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessSplineAxial(self):
		return self._ApplyTypes_(*(5504, 2, (9, 0), (), "TranslationStiffnessSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationStiffnessSplineRadial(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "TranslationStiffnessSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseRotationDampingExponent(self):
		return self._ApplyTypes_(*(5544, 2, (11, 0), (), "UseRotationDampingExponent", None))
	def _get_UseRotationDampingSpline(self):
		return self._ApplyTypes_(*(5523, 2, (11, 0), (), "UseRotationDampingSpline", None))
	def _get_UseRotationStiffnessExponent(self):
		return self._ApplyTypes_(*(5540, 2, (11, 0), (), "UseRotationStiffnessExponent", None))
	def _get_UseRotationStiffnessSpline(self):
		return self._ApplyTypes_(*(5516, 2, (11, 0), (), "UseRotationStiffnessSpline", None))
	def _get_UseRotationStopAngle(self):
		return self._ApplyTypes_(*(5531, 2, (11, 0), (), "UseRotationStopAngle", None))
	def _get_UseTranslationDampingExponent(self):
		return self._ApplyTypes_(*(5537, 2, (11, 0), (), "UseTranslationDampingExponent", None))
	def _get_UseTranslationDampingSpline(self):
		return self._ApplyTypes_(*(5507, 2, (11, 0), (), "UseTranslationDampingSpline", None))
	def _get_UseTranslationStiffnessExponent(self):
		return self._ApplyTypes_(*(5534, 2, (11, 0), (), "UseTranslationStiffnessExponent", None))
	def _get_UseTranslationStiffnessSpline(self):
		return self._ApplyTypes_(*(5502, 2, (11, 0), (), "UseTranslationStiffnessSpline", None))

	def _set_RotationDampingSplineX(self, value):
		if "RotationDampingSplineX" in self.__dict__: self.__dict__["RotationDampingSplineX"] = value; return
		self._oleobj_.Invoke(*((5524, LCID, 4, 0) + (value,) + ()))
	def _set_RotationDampingSplineY(self, value):
		if "RotationDampingSplineY" in self.__dict__: self.__dict__["RotationDampingSplineY"] = value; return
		self._oleobj_.Invoke(*((5525, LCID, 4, 0) + (value,) + ()))
	def _set_RotationDampingSplineZ(self, value):
		if "RotationDampingSplineZ" in self.__dict__: self.__dict__["RotationDampingSplineZ"] = value; return
		self._oleobj_.Invoke(*((5526, LCID, 4, 0) + (value,) + ()))
	def _set_RotationStiffnessSplineX(self, value):
		if "RotationStiffnessSplineX" in self.__dict__: self.__dict__["RotationStiffnessSplineX"] = value; return
		self._oleobj_.Invoke(*((5517, LCID, 4, 0) + (value,) + ()))
	def _set_RotationStiffnessSplineY(self, value):
		if "RotationStiffnessSplineY" in self.__dict__: self.__dict__["RotationStiffnessSplineY"] = value; return
		self._oleobj_.Invoke(*((5518, LCID, 4, 0) + (value,) + ()))
	def _set_RotationStiffnessSplineZ(self, value):
		if "RotationStiffnessSplineZ" in self.__dict__: self.__dict__["RotationStiffnessSplineZ"] = value; return
		self._oleobj_.Invoke(*((5519, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationDampingSplineAxial(self, value):
		if "TranslationDampingSplineAxial" in self.__dict__: self.__dict__["TranslationDampingSplineAxial"] = value; return
		self._oleobj_.Invoke(*((5509, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationDampingSplineRadial(self, value):
		if "TranslationDampingSplineRadial" in self.__dict__: self.__dict__["TranslationDampingSplineRadial"] = value; return
		self._oleobj_.Invoke(*((5508, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationStiffnessSplineAxial(self, value):
		if "TranslationStiffnessSplineAxial" in self.__dict__: self.__dict__["TranslationStiffnessSplineAxial"] = value; return
		self._oleobj_.Invoke(*((5504, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationStiffnessSplineRadial(self, value):
		if "TranslationStiffnessSplineRadial" in self.__dict__: self.__dict__["TranslationStiffnessSplineRadial"] = value; return
		self._oleobj_.Invoke(*((5503, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationDampingExponent(self, value):
		if "UseRotationDampingExponent" in self.__dict__: self.__dict__["UseRotationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((5544, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationDampingSpline(self, value):
		if "UseRotationDampingSpline" in self.__dict__: self.__dict__["UseRotationDampingSpline"] = value; return
		self._oleobj_.Invoke(*((5523, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStiffnessExponent(self, value):
		if "UseRotationStiffnessExponent" in self.__dict__: self.__dict__["UseRotationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5540, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStiffnessSpline(self, value):
		if "UseRotationStiffnessSpline" in self.__dict__: self.__dict__["UseRotationStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5516, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStopAngle(self, value):
		if "UseRotationStopAngle" in self.__dict__: self.__dict__["UseRotationStopAngle"] = value; return
		self._oleobj_.Invoke(*((5531, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationDampingExponent(self, value):
		if "UseTranslationDampingExponent" in self.__dict__: self.__dict__["UseTranslationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((5537, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationDampingSpline(self, value):
		if "UseTranslationDampingSpline" in self.__dict__: self.__dict__["UseTranslationDampingSpline"] = value; return
		self._oleobj_.Invoke(*((5507, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationStiffnessExponent(self, value):
		if "UseTranslationStiffnessExponent" in self.__dict__: self.__dict__["UseTranslationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5534, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationStiffnessSpline(self, value):
		if "UseTranslationStiffnessSpline" in self.__dict__: self.__dict__["UseTranslationStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5502, LCID, 4, 0) + (value,) + ()))

	RotationDampingCoefficientX = property(_get_RotationDampingCoefficientX, None)
	'''
	Rotation damping coefficient X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingCoefficientY = property(_get_RotationDampingCoefficientY, None)
	'''
	Rotation damping coefficient Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingCoefficientZ = property(_get_RotationDampingCoefficientZ, None)
	'''
	Rotation damping coefficient Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingExponentX = property(_get_RotationDampingExponentX, None)
	'''
	Rotation damping exponent X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingExponentY = property(_get_RotationDampingExponentY, None)
	'''
	Rotation damping exponent Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingExponentZ = property(_get_RotationDampingExponentZ, None)
	'''
	Rotation damping exponent Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingSplineX = property(_get_RotationDampingSplineX, _set_RotationDampingSplineX)
	'''
	Rotation damping spline X

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationDampingSplineY = property(_get_RotationDampingSplineY, _set_RotationDampingSplineY)
	'''
	Rotation damping spline Y

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationDampingSplineZ = property(_get_RotationDampingSplineZ, _set_RotationDampingSplineZ)
	'''
	Rotation damping spline Z

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationPreloadX = property(_get_RotationPreloadX, None)
	'''
	Rotation preload X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationPreloadY = property(_get_RotationPreloadY, None)
	'''
	Rotation preload Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationPreloadZ = property(_get_RotationPreloadZ, None)
	'''
	Rotation preload Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationPresetAngle = property(_get_RotationPresetAngle, None)
	'''
	Rotation preset angle

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessCoefficientX = property(_get_RotationStiffnessCoefficientX, None)
	'''
	Rotation stiffness coefficient X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessCoefficientY = property(_get_RotationStiffnessCoefficientY, None)
	'''
	Rotation stiffness coefficient Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessCoefficientZ = property(_get_RotationStiffnessCoefficientZ, None)
	'''
	Rotation stiffness coefficient Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessExponentX = property(_get_RotationStiffnessExponentX, None)
	'''
	Rotation stiffness exponent X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessExponentY = property(_get_RotationStiffnessExponentY, None)
	'''
	Rotation stiffness exponent Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessExponentZ = property(_get_RotationStiffnessExponentZ, None)
	'''
	Rotation stiffness exponent Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessSplineX = property(_get_RotationStiffnessSplineX, _set_RotationStiffnessSplineX)
	'''
	Rotation stiffness spline X

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationStiffnessSplineY = property(_get_RotationStiffnessSplineY, _set_RotationStiffnessSplineY)
	'''
	Rotation stiffness spline Y

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationStiffnessSplineZ = property(_get_RotationStiffnessSplineZ, _set_RotationStiffnessSplineZ)
	'''
	Rotation stiffness spline Z

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationStopAngle = property(_get_RotationStopAngle, None)
	'''
	RotationStopAngle

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStopStiffnessFactor = property(_get_RotationStopStiffnessFactor, None)
	'''
	Rotation Stop Stiffness Factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationClearance = property(_get_TranslationClearance, None)
	'''
	Translation clearance

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingCoefficientAxial = property(_get_TranslationDampingCoefficientAxial, None)
	'''
	Translation damping coefficient axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingCoefficientRadial = property(_get_TranslationDampingCoefficientRadial, None)
	'''
	Translation damping coefficient radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingExponentAxial = property(_get_TranslationDampingExponentAxial, None)
	'''
	Translation Damping exponent axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingExponentRadial = property(_get_TranslationDampingExponentRadial, None)
	'''
	Translation Damping exponent radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingSplineAxial = property(_get_TranslationDampingSplineAxial, _set_TranslationDampingSplineAxial)
	'''
	Translation damping spline axial

	:type: recurdyn.ProcessNet.ISpline
	'''
	TranslationDampingSplineRadial = property(_get_TranslationDampingSplineRadial, _set_TranslationDampingSplineRadial)
	'''
	Translation damping spline radial

	:type: recurdyn.ProcessNet.ISpline
	'''
	TranslationPreloadAxial = property(_get_TranslationPreloadAxial, None)
	'''
	Translation preload axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationPreloadRadial = property(_get_TranslationPreloadRadial, None)
	'''
	Translation preload radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessCoefficientAxial = property(_get_TranslationStiffnessCoefficientAxial, None)
	'''
	Translation stiffness coefficient axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessCoefficientRadial = property(_get_TranslationStiffnessCoefficientRadial, None)
	'''
	Translation stiffness coefficient radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessExponentAxial = property(_get_TranslationStiffnessExponentAxial, None)
	'''
	Translation stiffness exponent axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessExponentRadial = property(_get_TranslationStiffnessExponentRadial, None)
	'''
	Translation stiffness exponent radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessSplineAxial = property(_get_TranslationStiffnessSplineAxial, _set_TranslationStiffnessSplineAxial)
	'''
	Translation stiffness spline axial

	:type: recurdyn.ProcessNet.ISpline
	'''
	TranslationStiffnessSplineRadial = property(_get_TranslationStiffnessSplineRadial, _set_TranslationStiffnessSplineRadial)
	'''
	Translation stiffness spline radial

	:type: recurdyn.ProcessNet.ISpline
	'''
	UseRotationDampingExponent = property(_get_UseRotationDampingExponent, _set_UseRotationDampingExponent)
	'''
	Use rotation damping exponent

	:type: bool
	'''
	UseRotationDampingSpline = property(_get_UseRotationDampingSpline, _set_UseRotationDampingSpline)
	'''
	Use rotation damping spline

	:type: bool
	'''
	UseRotationStiffnessExponent = property(_get_UseRotationStiffnessExponent, _set_UseRotationStiffnessExponent)
	'''
	Use rotation stiffness exponent

	:type: bool
	'''
	UseRotationStiffnessSpline = property(_get_UseRotationStiffnessSpline, _set_UseRotationStiffnessSpline)
	'''
	Use rotation stiffness spline

	:type: bool
	'''
	UseRotationStopAngle = property(_get_UseRotationStopAngle, _set_UseRotationStopAngle)
	'''
	Use rotation stop angle

	:type: bool
	'''
	UseTranslationDampingExponent = property(_get_UseTranslationDampingExponent, _set_UseTranslationDampingExponent)
	'''
	Use translation Damping exponent

	:type: bool
	'''
	UseTranslationDampingSpline = property(_get_UseTranslationDampingSpline, _set_UseTranslationDampingSpline)
	'''
	Use translation damping spline

	:type: bool
	'''
	UseTranslationStiffnessExponent = property(_get_UseTranslationStiffnessExponent, _set_UseTranslationStiffnessExponent)
	'''
	Use translation stiffness exponent

	:type: bool
	'''
	UseTranslationStiffnessSpline = property(_get_UseTranslationStiffnessSpline, _set_UseTranslationStiffnessSpline)
	'''
	Use translation stiffness spline

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_RotationDampingSplineX": _set_RotationDampingSplineX,
		"_set_RotationDampingSplineY": _set_RotationDampingSplineY,
		"_set_RotationDampingSplineZ": _set_RotationDampingSplineZ,
		"_set_RotationStiffnessSplineX": _set_RotationStiffnessSplineX,
		"_set_RotationStiffnessSplineY": _set_RotationStiffnessSplineY,
		"_set_RotationStiffnessSplineZ": _set_RotationStiffnessSplineZ,
		"_set_TranslationDampingSplineAxial": _set_TranslationDampingSplineAxial,
		"_set_TranslationDampingSplineRadial": _set_TranslationDampingSplineRadial,
		"_set_TranslationStiffnessSplineAxial": _set_TranslationStiffnessSplineAxial,
		"_set_TranslationStiffnessSplineRadial": _set_TranslationStiffnessSplineRadial,
		"_set_UseRotationDampingExponent": _set_UseRotationDampingExponent,
		"_set_UseRotationDampingSpline": _set_UseRotationDampingSpline,
		"_set_UseRotationStiffnessExponent": _set_UseRotationStiffnessExponent,
		"_set_UseRotationStiffnessSpline": _set_UseRotationStiffnessSpline,
		"_set_UseRotationStopAngle": _set_UseRotationStopAngle,
		"_set_UseTranslationDampingExponent": _set_UseTranslationDampingExponent,
		"_set_UseTranslationDampingSpline": _set_UseTranslationDampingSpline,
		"_set_UseTranslationStiffnessExponent": _set_UseTranslationStiffnessExponent,
		"_set_UseTranslationStiffnessSpline": _set_UseTranslationStiffnessSpline,
	}
	_prop_map_get_ = {
		"RotationDampingCoefficientX": (5520, 2, (9, 0), (), "RotationDampingCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingCoefficientY": (5521, 2, (9, 0), (), "RotationDampingCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingCoefficientZ": (5522, 2, (9, 0), (), "RotationDampingCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponentX": (5545, 2, (9, 0), (), "RotationDampingExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponentY": (5546, 2, (9, 0), (), "RotationDampingExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponentZ": (5547, 2, (9, 0), (), "RotationDampingExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingSplineX": (5524, 2, (9, 0), (), "RotationDampingSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationDampingSplineY": (5525, 2, (9, 0), (), "RotationDampingSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationDampingSplineZ": (5526, 2, (9, 0), (), "RotationDampingSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationPreloadX": (5527, 2, (9, 0), (), "RotationPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationPreloadY": (5528, 2, (9, 0), (), "RotationPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationPreloadZ": (5529, 2, (9, 0), (), "RotationPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationPresetAngle": (5530, 2, (9, 0), (), "RotationPresetAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessCoefficientX": (5513, 2, (9, 0), (), "RotationStiffnessCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessCoefficientY": (5514, 2, (9, 0), (), "RotationStiffnessCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessCoefficientZ": (5515, 2, (9, 0), (), "RotationStiffnessCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponentX": (5541, 2, (9, 0), (), "RotationStiffnessExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponentY": (5542, 2, (9, 0), (), "RotationStiffnessExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponentZ": (5543, 2, (9, 0), (), "RotationStiffnessExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessSplineX": (5517, 2, (9, 0), (), "RotationStiffnessSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationStiffnessSplineY": (5518, 2, (9, 0), (), "RotationStiffnessSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationStiffnessSplineZ": (5519, 2, (9, 0), (), "RotationStiffnessSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationStopAngle": (5532, 2, (9, 0), (), "RotationStopAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStopStiffnessFactor": (5533, 2, (9, 0), (), "RotationStopStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationClearance": (5512, 2, (9, 0), (), "TranslationClearance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingCoefficientAxial": (5506, 2, (9, 0), (), "TranslationDampingCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingCoefficientRadial": (5505, 2, (9, 0), (), "TranslationDampingCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingExponentAxial": (5539, 2, (9, 0), (), "TranslationDampingExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingExponentRadial": (5538, 2, (9, 0), (), "TranslationDampingExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingSplineAxial": (5509, 2, (9, 0), (), "TranslationDampingSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationDampingSplineRadial": (5508, 2, (9, 0), (), "TranslationDampingSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationPreloadAxial": (5511, 2, (9, 0), (), "TranslationPreloadAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationPreloadRadial": (5510, 2, (9, 0), (), "TranslationPreloadRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessCoefficientAxial": (5501, 2, (9, 0), (), "TranslationStiffnessCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessCoefficientRadial": (5500, 2, (9, 0), (), "TranslationStiffnessCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessExponentAxial": (5536, 2, (9, 0), (), "TranslationStiffnessExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessExponentRadial": (5535, 2, (9, 0), (), "TranslationStiffnessExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessSplineAxial": (5504, 2, (9, 0), (), "TranslationStiffnessSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationStiffnessSplineRadial": (5503, 2, (9, 0), (), "TranslationStiffnessSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseRotationDampingExponent": (5544, 2, (11, 0), (), "UseRotationDampingExponent", None),
		"UseRotationDampingSpline": (5523, 2, (11, 0), (), "UseRotationDampingSpline", None),
		"UseRotationStiffnessExponent": (5540, 2, (11, 0), (), "UseRotationStiffnessExponent", None),
		"UseRotationStiffnessSpline": (5516, 2, (11, 0), (), "UseRotationStiffnessSpline", None),
		"UseRotationStopAngle": (5531, 2, (11, 0), (), "UseRotationStopAngle", None),
		"UseTranslationDampingExponent": (5537, 2, (11, 0), (), "UseTranslationDampingExponent", None),
		"UseTranslationDampingSpline": (5507, 2, (11, 0), (), "UseTranslationDampingSpline", None),
		"UseTranslationStiffnessExponent": (5534, 2, (11, 0), (), "UseTranslationStiffnessExponent", None),
		"UseTranslationStiffnessSpline": (5502, 2, (11, 0), (), "UseTranslationStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"RotationDampingSplineX": ((5524, LCID, 4, 0),()),
		"RotationDampingSplineY": ((5525, LCID, 4, 0),()),
		"RotationDampingSplineZ": ((5526, LCID, 4, 0),()),
		"RotationStiffnessSplineX": ((5517, LCID, 4, 0),()),
		"RotationStiffnessSplineY": ((5518, LCID, 4, 0),()),
		"RotationStiffnessSplineZ": ((5519, LCID, 4, 0),()),
		"TranslationDampingSplineAxial": ((5509, LCID, 4, 0),()),
		"TranslationDampingSplineRadial": ((5508, LCID, 4, 0),()),
		"TranslationStiffnessSplineAxial": ((5504, LCID, 4, 0),()),
		"TranslationStiffnessSplineRadial": ((5503, LCID, 4, 0),()),
		"UseRotationDampingExponent": ((5544, LCID, 4, 0),()),
		"UseRotationDampingSpline": ((5523, LCID, 4, 0),()),
		"UseRotationStiffnessExponent": ((5540, LCID, 4, 0),()),
		"UseRotationStiffnessSpline": ((5516, LCID, 4, 0),()),
		"UseRotationStopAngle": ((5531, LCID, 4, 0),()),
		"UseTranslationDampingExponent": ((5537, LCID, 4, 0),()),
		"UseTranslationDampingSpline": ((5507, LCID, 4, 0),()),
		"UseTranslationStiffnessExponent": ((5534, LCID, 4, 0),()),
		"UseTranslationStiffnessSpline": ((5502, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMAssemblyCollection(DispatchBaseClass):
	'''TrackLM Assembly Collection'''
	CLSID = IID('{22BE609F-1707-46CF-AA73-5BF5C0F577C4}')
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
		:rtype: recurdyn.TrackLM.ITrackLMAssembly
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F3294DCE-CF25-4511-986C-DC2D245853B1}')
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
		:rtype: recurdyn.TrackLM.ITrackLMAssembly
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F3294DCE-CF25-4511-986C-DC2D245853B1}')
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
		return win32com.client.util.Iterator(ob, '{F3294DCE-CF25-4511-986C-DC2D245853B1}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{F3294DCE-CF25-4511-986C-DC2D245853B1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITrackLMAssemblyContactGroundTrackLinkShoe(DispatchBaseClass):
	'''TrackLM Assembly Contact Ground TrackLink Shoe'''
	CLSID = IID('{C37B595D-DE29-465E-88F7-288C5C63D7F7}')
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
		Export ground parameter
		
		:param strName: str
		:param val: bool
		'''
		return self._oleobj_.InvokeTypes(5562, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import ground parameter
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(5563, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def SoftGroundType(self, val):
		'''
		Soft ground type
		
		:param val: ContactParameterSoftGroundType
		'''
		return self._oleobj_.InvokeTypes(5553, LCID, 1, (24, 0), ((3, 1),),val
			)


	def _get_Cohesion(self):
		return self._ApplyTypes_(*(5557, 2, (9, 0), (), "Cohesion", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(5512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_ExponentialNumber(self):
		return self._ApplyTypes_(*(5556, 2, (9, 0), (), "ExponentialNumber", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(5516, 2, (9, 0), (), "Friction", '{CB8726EC-DB26-4DBC-8C1F-E011ED239188}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(5506, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(5508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(5517, 2, (3, 0), (), "FrictionType", '{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(5514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LateralFrictionFactor(self):
		return self._ApplyTypes_(*(5551, 2, (9, 0), (), "LateralFrictionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearingDeformationModulus(self):
		return self._ApplyTypes_(*(5559, 2, (9, 0), (), "ShearingDeformationModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearingResistanceAngle(self):
		return self._ApplyTypes_(*(5558, 2, (9, 0), (), "ShearingResistanceAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SinkageRatio(self):
		return self._ApplyTypes_(*(5560, 2, (9, 0), (), "SinkageRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(5510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TerrainStiffnessKc(self):
		return self._ApplyTypes_(*(5554, 2, (9, 0), (), "TerrainStiffnessKc", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TerrainStiffnessKphi(self):
		return self._ApplyTypes_(*(5555, 2, (9, 0), (), "TerrainStiffnessKphi", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(5511, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(5504, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseFrictionSpline(self):
		return self._ApplyTypes_(*(5507, 2, (11, 0), (), "UseFrictionSpline", None))
	def _get_UseInactiveGroundParameter(self):
		return self._ApplyTypes_(*(5552, 2, (11, 0), (), "UseInactiveGroundParameter", None))
	def _get_UseInactiveSoftGroundParameter(self):
		return self._ApplyTypes_(*(5561, 2, (11, 0), (), "UseInactiveSoftGroundParameter", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(5513, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseLateralFrictionFactor(self):
		return self._ApplyTypes_(*(5550, 2, (11, 0), (), "UseLateralFrictionFactor", None))
	def _get_UseMoreFrictionData(self):
		return self._ApplyTypes_(*(5515, 2, (11, 0), (), "UseMoreFrictionData", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(5509, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(5501, 2, (11, 0), (), "UseStiffnessSpline", None))
	def _get_UseUserSubroutine(self):
		return self._ApplyTypes_(*(5564, 2, (11, 0), (), "UseUserSubroutine", None))
	def _get_UserSubroutine(self):
		return self._ApplyTypes_(*(5565, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((5505, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((5508, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((5517, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5502, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((5511, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((5504, LCID, 4, 0) + (value,) + ()))
	def _set_UseFrictionSpline(self, value):
		if "UseFrictionSpline" in self.__dict__: self.__dict__["UseFrictionSpline"] = value; return
		self._oleobj_.Invoke(*((5507, LCID, 4, 0) + (value,) + ()))
	def _set_UseInactiveGroundParameter(self, value):
		if "UseInactiveGroundParameter" in self.__dict__: self.__dict__["UseInactiveGroundParameter"] = value; return
		self._oleobj_.Invoke(*((5552, LCID, 4, 0) + (value,) + ()))
	def _set_UseInactiveSoftGroundParameter(self, value):
		if "UseInactiveSoftGroundParameter" in self.__dict__: self.__dict__["UseInactiveSoftGroundParameter"] = value; return
		self._oleobj_.Invoke(*((5561, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((5513, LCID, 4, 0) + (value,) + ()))
	def _set_UseLateralFrictionFactor(self, value):
		if "UseLateralFrictionFactor" in self.__dict__: self.__dict__["UseLateralFrictionFactor"] = value; return
		self._oleobj_.Invoke(*((5550, LCID, 4, 0) + (value,) + ()))
	def _set_UseMoreFrictionData(self, value):
		if "UseMoreFrictionData" in self.__dict__: self.__dict__["UseMoreFrictionData"] = value; return
		self._oleobj_.Invoke(*((5515, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5509, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5501, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserSubroutine(self, value):
		if "UseUserSubroutine" in self.__dict__: self.__dict__["UseUserSubroutine"] = value; return
		self._oleobj_.Invoke(*((5564, LCID, 4, 0) + (value,) + ()))
	def _set_UserSubroutine(self, value):
		if "UserSubroutine" in self.__dict__: self.__dict__["UserSubroutine"] = value; return
		self._oleobj_.Invoke(*((5565, LCID, 4, 0) + (value,) + ()))

	Cohesion = property(_get_Cohesion, None)
	'''
	Cohesion (c)

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
	ExponentialNumber = property(_get_ExponentialNumber, None)
	'''
	Exponential number (n)

	:type: recurdyn.ProcessNet.IDouble
	'''
	Friction = property(_get_Friction, None)
	'''
	Friction

	:type: recurdyn.TrackLM.ITrackLMContactFriction
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
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.TrackLM.TrackLMFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	The indentation exponent yields an indentation damping effect.

	:type: recurdyn.ProcessNet.IDouble
	'''
	LateralFrictionFactor = property(_get_LateralFrictionFactor, None)
	'''
	Lateral friction factor.

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearingDeformationModulus = property(_get_ShearingDeformationModulus, None)
	'''
	Shearing deformation modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearingResistanceAngle = property(_get_ShearingResistanceAngle, None)
	'''
	Shearing resistance angle

	:type: recurdyn.ProcessNet.IDouble
	'''
	SinkageRatio = property(_get_SinkageRatio, None)
	'''
	Sinkage ratio

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
	TerrainStiffnessKc = property(_get_TerrainStiffnessKc, None)
	'''
	Terrain stiffness (k_c)

	:type: recurdyn.ProcessNet.IDouble
	'''
	TerrainStiffnessKphi = property(_get_TerrainStiffnessKphi, None)
	'''
	Terrain stiffness (k_phi)

	:type: recurdyn.ProcessNet.IDouble
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
	Use friction spline

	:type: bool
	'''
	UseInactiveGroundParameter = property(_get_UseInactiveGroundParameter, _set_UseInactiveGroundParameter)
	'''
	Use inactive ground parameter

	:type: bool
	'''
	UseInactiveSoftGroundParameter = property(_get_UseInactiveSoftGroundParameter, _set_UseInactiveSoftGroundParameter)
	'''
	Use inactive soft ground parameter

	:type: bool
	'''
	UseIndentationExponent = property(_get_UseIndentationExponent, _set_UseIndentationExponent)
	'''
	Use indentation exponent

	:type: bool
	'''
	UseLateralFrictionFactor = property(_get_UseLateralFrictionFactor, _set_UseLateralFrictionFactor)
	'''
	Use lateral friction factor

	:type: bool
	'''
	UseMoreFrictionData = property(_get_UseMoreFrictionData, _set_UseMoreFrictionData)
	'''
	Contact friction type

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
	User Subroutine

	:type: recurdyn.ProcessNet.IUserSubroutine
	'''

	_prop_map_set_function_ = {
		"_set_DampingSpline": _set_DampingSpline,
		"_set_FrictionSpline": _set_FrictionSpline,
		"_set_FrictionType": _set_FrictionType,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseFrictionSpline": _set_UseFrictionSpline,
		"_set_UseInactiveGroundParameter": _set_UseInactiveGroundParameter,
		"_set_UseInactiveSoftGroundParameter": _set_UseInactiveSoftGroundParameter,
		"_set_UseIndentationExponent": _set_UseIndentationExponent,
		"_set_UseLateralFrictionFactor": _set_UseLateralFrictionFactor,
		"_set_UseMoreFrictionData": _set_UseMoreFrictionData,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
		"_set_UseUserSubroutine": _set_UseUserSubroutine,
		"_set_UserSubroutine": _set_UserSubroutine,
	}
	_prop_map_get_ = {
		"Cohesion": (5557, 2, (9, 0), (), "Cohesion", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingCoefficient": (5503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (5512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (5505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"ExponentialNumber": (5556, 2, (9, 0), (), "ExponentialNumber", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Friction": (5516, 2, (9, 0), (), "Friction", '{CB8726EC-DB26-4DBC-8C1F-E011ED239188}'),
		"FrictionCoefficient": (5506, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (5508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (5517, 2, (3, 0), (), "FrictionType", '{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}'),
		"IndentationExponent": (5514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LateralFrictionFactor": (5551, 2, (9, 0), (), "LateralFrictionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearingDeformationModulus": (5559, 2, (9, 0), (), "ShearingDeformationModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearingResistanceAngle": (5558, 2, (9, 0), (), "ShearingResistanceAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SinkageRatio": (5560, 2, (9, 0), (), "SinkageRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (5500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (5510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (5502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TerrainStiffnessKc": (5554, 2, (9, 0), (), "TerrainStiffnessKc", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TerrainStiffnessKphi": (5555, 2, (9, 0), (), "TerrainStiffnessKphi", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseDampingExponent": (5511, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (5504, 2, (11, 0), (), "UseDampingSpline", None),
		"UseFrictionSpline": (5507, 2, (11, 0), (), "UseFrictionSpline", None),
		"UseInactiveGroundParameter": (5552, 2, (11, 0), (), "UseInactiveGroundParameter", None),
		"UseInactiveSoftGroundParameter": (5561, 2, (11, 0), (), "UseInactiveSoftGroundParameter", None),
		"UseIndentationExponent": (5513, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseLateralFrictionFactor": (5550, 2, (11, 0), (), "UseLateralFrictionFactor", None),
		"UseMoreFrictionData": (5515, 2, (11, 0), (), "UseMoreFrictionData", None),
		"UseStiffnessExponent": (5509, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (5501, 2, (11, 0), (), "UseStiffnessSpline", None),
		"UseUserSubroutine": (5564, 2, (11, 0), (), "UseUserSubroutine", None),
		"UserSubroutine": (5565, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'),
	}
	_prop_map_put_ = {
		"DampingSpline": ((5505, LCID, 4, 0),()),
		"FrictionSpline": ((5508, LCID, 4, 0),()),
		"FrictionType": ((5517, LCID, 4, 0),()),
		"StiffnessSpline": ((5502, LCID, 4, 0),()),
		"UseDampingExponent": ((5511, LCID, 4, 0),()),
		"UseDampingSpline": ((5504, LCID, 4, 0),()),
		"UseFrictionSpline": ((5507, LCID, 4, 0),()),
		"UseInactiveGroundParameter": ((5552, LCID, 4, 0),()),
		"UseInactiveSoftGroundParameter": ((5561, LCID, 4, 0),()),
		"UseIndentationExponent": ((5513, LCID, 4, 0),()),
		"UseLateralFrictionFactor": ((5550, LCID, 4, 0),()),
		"UseMoreFrictionData": ((5515, LCID, 4, 0),()),
		"UseStiffnessExponent": ((5509, LCID, 4, 0),()),
		"UseStiffnessSpline": ((5501, LCID, 4, 0),()),
		"UseUserSubroutine": ((5564, LCID, 4, 0),()),
		"UserSubroutine": ((5565, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMAssemblyGrouserContact(DispatchBaseClass):
	'''TrackLM Assembly Grouser Contact'''
	CLSID = IID('{41C77E5C-5A0D-4060-9668-47AAEE4E7575}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ActionPosition(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "ActionPosition", '{5C8577DA-B2F5-4C78-AF81-251818CE7223}'))
	def _get_ActionRadius(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "ActionRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_BasePosition(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "BasePosition", '{5C8577DA-B2F5-4C78-AF81-251818CE7223}'))
	def _get_BaseRadius(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "BaseRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DistanceBetweenLinks(self):
		return self._ApplyTypes_(*(5504, 2, (5, 0), (), "DistanceBetweenLinks", None))

	def _set_DistanceBetweenLinks(self, value):
		if "DistanceBetweenLinks" in self.__dict__: self.__dict__["DistanceBetweenLinks"] = value; return
		self._oleobj_.Invoke(*((5504, LCID, 4, 0) + (value,) + ()))

	ActionPosition = property(_get_ActionPosition, None)
	'''
	Action position

	:type: recurdyn.ProcessNet.IPoint2D
	'''
	ActionRadius = property(_get_ActionRadius, None)
	'''
	Action radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	BasePosition = property(_get_BasePosition, None)
	'''
	Base position

	:type: recurdyn.ProcessNet.IPoint2D
	'''
	BaseRadius = property(_get_BaseRadius, None)
	'''
	Base radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	DistanceBetweenLinks = property(_get_DistanceBetweenLinks, _set_DistanceBetweenLinks)
	'''
	Distance between Links

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_DistanceBetweenLinks": _set_DistanceBetweenLinks,
	}
	_prop_map_get_ = {
		"ActionPosition": (5502, 2, (9, 0), (), "ActionPosition", '{5C8577DA-B2F5-4C78-AF81-251818CE7223}'),
		"ActionRadius": (5503, 2, (9, 0), (), "ActionRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"BasePosition": (5500, 2, (9, 0), (), "BasePosition", '{5C8577DA-B2F5-4C78-AF81-251818CE7223}'),
		"BaseRadius": (5501, 2, (9, 0), (), "BaseRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DistanceBetweenLinks": (5504, 2, (5, 0), (), "DistanceBetweenLinks", None),
	}
	_prop_map_put_ = {
		"DistanceBetweenLinks": ((5504, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMAssemblyGrouserContactCollection(DispatchBaseClass):
	'''TrackLM Assembly Grouser Contact Collection'''
	CLSID = IID('{68152AA0-4470-4F17-AEF7-F45AA9ABE529}')
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
		:rtype: recurdyn.TrackLM.ITrackLMAssemblyGrouserContact
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{41C77E5C-5A0D-4060-9668-47AAEE4E7575}')
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
		:rtype: recurdyn.TrackLM.ITrackLMAssemblyGrouserContact
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{41C77E5C-5A0D-4060-9668-47AAEE4E7575}')
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
		return win32com.client.util.Iterator(ob, '{41C77E5C-5A0D-4060-9668-47AAEE4E7575}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{41C77E5C-5A0D-4060-9668-47AAEE4E7575}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITrackLMAssemblyGrouserToSphereContact(DispatchBaseClass):
	'''TrackLM grouser to sphere contact property'''
	CLSID = IID('{71434E11-33AF-44E5-B36F-D0D92753A768}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddGrouserToSphereContact(self, pGeometrySphere):
		'''
		Add a grouser to sphere contact
		
		:param pGeometrySphere: IGeometrySphere
		'''
		return self._oleobj_.InvokeTypes(5502, LCID, 1, (24, 0), ((9, 1),),pGeometrySphere
			)


	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "ContactProperty", '{674DD026-A8F6-4A8B-91ED-0CF92C531AE3}'))
	def _get_GeometrySphereCollection(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "GeometrySphereCollection", '{0B006D28-70E2-4FBA-8A03-EC9EFC17C4E1}'))
	def _get_MaximumPenetration(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "MaximumPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	ContactProperty = property(_get_ContactProperty, None)
	'''
	Grouser to sphere contact property

	:type: recurdyn.TrackLM.ITrackLMGrouserToSphereContactProperty
	'''
	GeometrySphereCollection = property(_get_GeometrySphereCollection, None)
	'''
	Sphere geometry collection of grouser to sphere contact

	:type: recurdyn.ProcessNet.IGeometrySphereCollection
	'''
	MaximumPenetration = property(_get_MaximumPenetration, None)
	'''
	Maximum penetration.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"ContactProperty": (5501, 2, (9, 0), (), "ContactProperty", '{674DD026-A8F6-4A8B-91ED-0CF92C531AE3}'),
		"GeometrySphereCollection": (5503, 2, (9, 0), (), "GeometrySphereCollection", '{0B006D28-70E2-4FBA-8A03-EC9EFC17C4E1}'),
		"MaximumPenetration": (5500, 2, (9, 0), (), "MaximumPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackLMBody(DispatchBaseClass):
	'''TrackLM body'''
	CLSID = IID('{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}')
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
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
		"GeneralBody": (5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
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

class ITrackLMBodyCollection(DispatchBaseClass):
	'''TrackLM roller guard body collection'''
	CLSID = IID('{2E24F362-D8AA-41AD-8BD4-CD92CF24C188}')
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
		:rtype: recurdyn.TrackLM.ITrackLMBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}')
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
		:rtype: recurdyn.TrackLM.ITrackLMBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}')
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
		return win32com.client.util.Iterator(ob, '{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITrackLMBodyFlangeCenter(DispatchBaseClass):
	'''TrackLM flange center'''
	CLSID = IID('{B142F053-F79F-4E72-9252-26D82A373001}')
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
		return self._ApplyTypes_(*(5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(5551, 2, (9, 0), (), "Geometry", '{DF8894F1-EAE8-48C7-A734-F5EB5F50F9FE}'))
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
	Contact Property

	:type: recurdyn.TrackLM.ITrackLMContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.TrackLM.ITrackLMContactSearch
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

	:type: recurdyn.TrackLM.ITrackLMGeometryFlangeCenter
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
		"ContactProperty": (5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'),
		"ContactSearch": (5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (5551, 2, (9, 0), (), "Geometry", '{DF8894F1-EAE8-48C7-A734-F5EB5F50F9FE}'),
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

class ITrackLMBodyFlangeDouble(DispatchBaseClass):
	'''TrackLM flange double'''
	CLSID = IID('{7C581B15-F7A8-4FD4-B732-07DD8661FE01}')
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
		return self._ApplyTypes_(*(5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(5551, 2, (9, 0), (), "Geometry", '{8F09092F-1146-4BC0-A8BC-7A85F51F0054}'))
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
	Contact Property

	:type: recurdyn.TrackLM.ITrackLMContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.TrackLM.ITrackLMContactSearch
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

	:type: recurdyn.TrackLM.ITrackLMGeometryFlangeDouble
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
		"ContactProperty": (5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'),
		"ContactSearch": (5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (5551, 2, (9, 0), (), "Geometry", '{8F09092F-1146-4BC0-A8BC-7A85F51F0054}'),
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

class ITrackLMBodyFlangeFlat(DispatchBaseClass):
	'''TrackLM flange flat'''
	CLSID = IID('{1413E74E-9CDE-4E83-9BC2-14F6C0783FC0}')
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
		return self._ApplyTypes_(*(5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(5551, 2, (9, 0), (), "Geometry", '{3B1930FF-530C-4745-B19C-D335810BBDBD}'))
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
	Contact Property

	:type: recurdyn.TrackLM.ITrackLMContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.TrackLM.ITrackLMContactSearch
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

	:type: recurdyn.TrackLM.ITrackLMGeometryFlangeFlat
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
		"ContactProperty": (5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'),
		"ContactSearch": (5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (5551, 2, (9, 0), (), "Geometry", '{3B1930FF-530C-4745-B19C-D335810BBDBD}'),
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

class ITrackLMBodyFlangeSingle(DispatchBaseClass):
	'''TrackLM flange single'''
	CLSID = IID('{0FBAD430-C81A-4870-9D3E-9F6497D2C565}')
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
		return self._ApplyTypes_(*(5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(5551, 2, (9, 0), (), "Geometry", '{1552BF6E-3FFB-4111-A93D-A52A379E09CF}'))
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
	Contact Property

	:type: recurdyn.TrackLM.ITrackLMContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.TrackLM.ITrackLMContactSearch
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

	:type: recurdyn.TrackLM.ITrackLMGeometryFlangeSingle
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
		"ContactProperty": (5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'),
		"ContactSearch": (5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (5551, 2, (9, 0), (), "Geometry", '{1552BF6E-3FFB-4111-A93D-A52A379E09CF}'),
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

class ITrackLMBodyLink(DispatchBaseClass):
	'''TrackLM Body Link'''
	CLSID = IID('{D4D76CF3-BAAD-44E9-8D1E-18CB7B5F910D}')
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
		ret = self._oleobj_.InvokeTypes(5558, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
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
		return self._oleobj_.InvokeTypes(5555, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(5551, 2, (9, 0), (), "Geometry", '{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(5557, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_LinkGrouserProfile(self):
		return self._ApplyTypes_(*(5554, 2, (9, 0), (), "LinkGrouserProfile", '{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}'))
	def _get_LinkShapeProfile(self):
		return self._ApplyTypes_(*(5553, 2, (9, 0), (), "LinkShapeProfile", '{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(5556, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UseLinkShape(self):
		return self._ApplyTypes_(*(5552, 2, (11, 0), (), "UseLinkShape", None))
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
		self._oleobj_.Invoke(*((5556, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkShape(self, value):
		if "UseLinkShape" in self.__dict__: self.__dict__["UseLinkShape"] = value; return
		self._oleobj_.Invoke(*((5552, LCID, 4, 0) + (value,) + ()))
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

	:type: recurdyn.TrackLM.ITrackLMGeometryLink
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
	'''
	LinkGrouserProfile = property(_get_LinkGrouserProfile, None)
	'''
	Link grouser profile

	:type: recurdyn.TrackLM.ITrackLMProfileLinkGrouser
	'''
	LinkShapeProfile = property(_get_LinkShapeProfile, None)
	'''
	Link shape profile

	:type: recurdyn.TrackLM.ITrackLMProfileLinkShape
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
	UseLinkShape = property(_get_UseLinkShape, _set_UseLinkShape)
	'''
	Use link shape

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
		"_set_UseLinkShape": _set_UseLinkShape,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (5551, 2, (9, 0), (), "Geometry", '{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}'),
		"Graphic": (5557, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"LinkGrouserProfile": (5554, 2, (9, 0), (), "LinkGrouserProfile", '{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}'),
		"LinkShapeProfile": (5553, 2, (9, 0), (), "LinkShapeProfile", '{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (5556, 2, (11, 0), (), "UseBodyGraphic", None),
		"UseLinkShape": (5552, 2, (11, 0), (), "UseLinkShape", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((5556, LCID, 4, 0),()),
		"UseLinkShape": ((5552, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMBodyLinkCollection(DispatchBaseClass):
	'''TrackLM Body Link Collection'''
	CLSID = IID('{7E3C5275-F00D-4675-BAF6-9AE63689F8D2}')
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
		:rtype: recurdyn.TrackLM.ITrackLMBodyLink
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D4D76CF3-BAAD-44E9-8D1E-18CB7B5F910D}')
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
		:rtype: recurdyn.TrackLM.ITrackLMBodyLink
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D4D76CF3-BAAD-44E9-8D1E-18CB7B5F910D}')
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
		return win32com.client.util.Iterator(ob, '{D4D76CF3-BAAD-44E9-8D1E-18CB7B5F910D}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{D4D76CF3-BAAD-44E9-8D1E-18CB7B5F910D}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITrackLMBodyRollerGuard(DispatchBaseClass):
	'''TrackLM Body Roller Guard'''
	CLSID = IID('{E873D6AC-B791-48F4-B0AB-12560562B540}')
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
		return self._ApplyTypes_(*(5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(5551, 2, (9, 0), (), "Geometry", '{ABD47D59-1C65-4ACE-9DDA-0485A5EE880E}'))
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
	Contact Property

	:type: recurdyn.TrackLM.ITrackLMContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.TrackLM.ITrackLMContactSearch
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

	:type: recurdyn.TrackLM.ITrackLMGeometryRollerGuard
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
		"ContactProperty": (5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'),
		"ContactSearch": (5552, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (5551, 2, (9, 0), (), "Geometry", '{ABD47D59-1C65-4ACE-9DDA-0485A5EE880E}'),
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

class ITrackLMBodySprocket(DispatchBaseClass):
	'''TrackLMBodySprocket'''
	CLSID = IID('{C809FD1D-0B5D-4F2C-843C-BFBFCD795B11}')
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


	def UpdateProperties(self):
		'''
		Update Properties
		'''
		return self._oleobj_.InvokeTypes(5555, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(5553, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'))
	def _get_CreateContactOutputFile(self):
		return self._ApplyTypes_(*(5556, 2, (11, 0), (), "CreateContactOutputFile", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(5551, 2, (9, 0), (), "Geometry", '{FB048C8A-5E0F-414C-BB9A-16E7D2410E40}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ToothProfile(self):
		return self._ApplyTypes_(*(5552, 2, (9, 0), (), "ToothProfile", '{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_CreateContactOutputFile(self, value):
		if "CreateContactOutputFile" in self.__dict__: self.__dict__["CreateContactOutputFile"] = value; return
		self._oleobj_.Invoke(*((5556, LCID, 4, 0) + (value,) + ()))
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
	Contact Property

	:type: recurdyn.TrackLM.ITrackLMContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.TrackLM.ITrackLMContactSearch
	'''
	CreateContactOutputFile = property(_get_CreateContactOutputFile, _set_CreateContactOutputFile)
	'''
	Create contact output file

	:type: bool
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

	:type: recurdyn.TrackLM.ITrackLMGeometrySprocket
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
	ToothProfile = property(_get_ToothProfile, None)
	'''
	ToothProfile

	:type: recurdyn.TrackLM.ITrackLMToothProfileSprocket
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_CreateContactOutputFile": _set_CreateContactOutputFile,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactProperty": (5550, 2, (9, 0), (), "ContactProperty", '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}'),
		"ContactSearch": (5553, 2, (9, 0), (), "ContactSearch", '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}'),
		"CreateContactOutputFile": (5556, 2, (11, 0), (), "CreateContactOutputFile", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (5500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (5551, 2, (9, 0), (), "Geometry", '{FB048C8A-5E0F-414C-BB9A-16E7D2410E40}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ToothProfile": (5552, 2, (9, 0), (), "ToothProfile", '{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"CreateContactOutputFile": ((5556, LCID, 4, 0),()),
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

class ITrackLMContactFriction(DispatchBaseClass):
	'''TrackLM contact friction'''
	CLSID = IID('{CB8726EC-DB26-4DBC-8C1F-E011ED239188}')
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
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticFrictionCoefficient(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticThresholdVelocity(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	DynamicThresholdVelocity = property(_get_DynamicThresholdVelocity, None)
	'''
	Dynamic threshold velocity

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

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DynamicThresholdVelocity": (5502, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticFrictionCoefficient": (5503, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticThresholdVelocity": (5501, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackLMContactProperty(DispatchBaseClass):
	'''TrackLM contact property'''
	CLSID = IID('{492847E5-C7BF-4736-9BF3-70ED0D5DB576}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(5512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(5516, 2, (9, 0), (), "Friction", '{CB8726EC-DB26-4DBC-8C1F-E011ED239188}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(5506, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(5508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(5517, 2, (3, 0), (), "FrictionType", '{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(5514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(5510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(5511, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(5504, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseFrictionSpline(self):
		return self._ApplyTypes_(*(5507, 2, (11, 0), (), "UseFrictionSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(5513, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseMoreFrictionData(self):
		return self._ApplyTypes_(*(5515, 2, (11, 0), (), "UseMoreFrictionData", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(5509, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(5501, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((5505, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((5508, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((5517, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5502, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((5511, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((5504, LCID, 4, 0) + (value,) + ()))
	def _set_UseFrictionSpline(self, value):
		if "UseFrictionSpline" in self.__dict__: self.__dict__["UseFrictionSpline"] = value; return
		self._oleobj_.Invoke(*((5507, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((5513, LCID, 4, 0) + (value,) + ()))
	def _set_UseMoreFrictionData(self, value):
		if "UseMoreFrictionData" in self.__dict__: self.__dict__["UseMoreFrictionData"] = value; return
		self._oleobj_.Invoke(*((5515, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5509, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5501, LCID, 4, 0) + (value,) + ()))

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

	:type: recurdyn.TrackLM.ITrackLMContactFriction
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
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.TrackLM.TrackLMFrictionType
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
	Use friction spline

	:type: bool
	'''
	UseIndentationExponent = property(_get_UseIndentationExponent, _set_UseIndentationExponent)
	'''
	Use indentation exponent

	:type: bool
	'''
	UseMoreFrictionData = property(_get_UseMoreFrictionData, _set_UseMoreFrictionData)
	'''
	Contact friction type

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
		"_set_DampingSpline": _set_DampingSpline,
		"_set_FrictionSpline": _set_FrictionSpline,
		"_set_FrictionType": _set_FrictionType,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseFrictionSpline": _set_UseFrictionSpline,
		"_set_UseIndentationExponent": _set_UseIndentationExponent,
		"_set_UseMoreFrictionData": _set_UseMoreFrictionData,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
	}
	_prop_map_get_ = {
		"DampingCoefficient": (5503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (5512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (5505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"Friction": (5516, 2, (9, 0), (), "Friction", '{CB8726EC-DB26-4DBC-8C1F-E011ED239188}'),
		"FrictionCoefficient": (5506, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (5508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (5517, 2, (3, 0), (), "FrictionType", '{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}'),
		"IndentationExponent": (5514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (5500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (5510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (5502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (5511, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (5504, 2, (11, 0), (), "UseDampingSpline", None),
		"UseFrictionSpline": (5507, 2, (11, 0), (), "UseFrictionSpline", None),
		"UseIndentationExponent": (5513, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseMoreFrictionData": (5515, 2, (11, 0), (), "UseMoreFrictionData", None),
		"UseStiffnessExponent": (5509, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (5501, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"DampingSpline": ((5505, LCID, 4, 0),()),
		"FrictionSpline": ((5508, LCID, 4, 0),()),
		"FrictionType": ((5517, LCID, 4, 0),()),
		"StiffnessSpline": ((5502, LCID, 4, 0),()),
		"UseDampingExponent": ((5511, LCID, 4, 0),()),
		"UseDampingSpline": ((5504, LCID, 4, 0),()),
		"UseFrictionSpline": ((5507, LCID, 4, 0),()),
		"UseIndentationExponent": ((5513, LCID, 4, 0),()),
		"UseMoreFrictionData": ((5515, LCID, 4, 0),()),
		"UseStiffnessExponent": ((5509, LCID, 4, 0),()),
		"UseStiffnessSpline": ((5501, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMContactSearch(DispatchBaseClass):
	'''TrackLM flange contact search'''
	CLSID = IID('{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}')
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
		return self._ApplyTypes_(*(5500, 2, (3, 0), (), "Type", '{AB0354E4-81A0-4EF7-9579-3DBB2272CEE0}'))
	def _get_UseUserBoundaryForPartialSearch(self):
		return self._ApplyTypes_(*(5501, 2, (11, 0), (), "UseUserBoundaryForPartialSearch", None))
	def _get_UserBoundaryForPartialSearch(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "UserBoundaryForPartialSearch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((5500, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserBoundaryForPartialSearch(self, value):
		if "UseUserBoundaryForPartialSearch" in self.__dict__: self.__dict__["UseUserBoundaryForPartialSearch"] = value; return
		self._oleobj_.Invoke(*((5501, LCID, 4, 0) + (value,) + ()))

	Type = property(_get_Type, _set_Type)
	'''
	Search type of the flange.

	:type: recurdyn.TrackLM.ContactSearchType
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
		"Type": (5500, 2, (3, 0), (), "Type", '{AB0354E4-81A0-4EF7-9579-3DBB2272CEE0}'),
		"UseUserBoundaryForPartialSearch": (5501, 2, (11, 0), (), "UseUserBoundaryForPartialSearch", None),
		"UserBoundaryForPartialSearch": (5502, 2, (9, 0), (), "UserBoundaryForPartialSearch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Type": ((5500, LCID, 4, 0),()),
		"UseUserBoundaryForPartialSearch": ((5501, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMGeometryFlangeCenter(DispatchBaseClass):
	'''TrackLM flange center geometry'''
	CLSID = IID('{DF8894F1-EAE8-48C7-A734-F5EB5F50F9FE}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_InnerFlangeRadius(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "InnerFlangeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InnerFlangeWidth(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "InnerFlangeWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalWidth(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "TotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WheelRadius(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	InnerFlangeRadius = property(_get_InnerFlangeRadius, None)
	'''
	Inner flange radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	InnerFlangeWidth = property(_get_InnerFlangeWidth, None)
	'''
	Inner flange width.

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalWidth = property(_get_TotalWidth, None)
	'''
	Total width.

	:type: recurdyn.ProcessNet.IDouble
	'''
	WheelRadius = property(_get_WheelRadius, None)
	'''
	Wheel radius.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"InnerFlangeRadius": (5502, 2, (9, 0), (), "InnerFlangeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InnerFlangeWidth": (5500, 2, (9, 0), (), "InnerFlangeWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalWidth": (5501, 2, (9, 0), (), "TotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WheelRadius": (5503, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackLMGeometryFlangeDouble(DispatchBaseClass):
	'''TrackLM flange double geometry'''
	CLSID = IID('{8F09092F-1146-4BC0-A8BC-7A85F51F0054}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_HubAndInnerFlangeWidth(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "HubAndInnerFlangeWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_HubInnerFlangeAndWheelWidth(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "HubInnerFlangeAndWheelWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_HubRadius(self):
		return self._ApplyTypes_(*(5504, 2, (9, 0), (), "HubRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_HubWidth(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "HubWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InnerFlangeRadius(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "InnerFlangeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_OuterFlangeRadius(self):
		return self._ApplyTypes_(*(5507, 2, (9, 0), (), "OuterFlangeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalWidth(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "TotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WheelRadius(self):
		return self._ApplyTypes_(*(5506, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	HubAndInnerFlangeWidth = property(_get_HubAndInnerFlangeWidth, None)
	'''
	Hub and inner flange width.

	:type: recurdyn.ProcessNet.IDouble
	'''
	HubInnerFlangeAndWheelWidth = property(_get_HubInnerFlangeAndWheelWidth, None)
	'''
	Hub, inner flange and wheel width.

	:type: recurdyn.ProcessNet.IDouble
	'''
	HubRadius = property(_get_HubRadius, None)
	'''
	Hub radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	HubWidth = property(_get_HubWidth, None)
	'''
	Hub width.

	:type: recurdyn.ProcessNet.IDouble
	'''
	InnerFlangeRadius = property(_get_InnerFlangeRadius, None)
	'''
	Inner flange radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	OuterFlangeRadius = property(_get_OuterFlangeRadius, None)
	'''
	Outer flange radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalWidth = property(_get_TotalWidth, None)
	'''
	Total width.

	:type: recurdyn.ProcessNet.IDouble
	'''
	WheelRadius = property(_get_WheelRadius, None)
	'''
	Wheel radius.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"HubAndInnerFlangeWidth": (5501, 2, (9, 0), (), "HubAndInnerFlangeWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"HubInnerFlangeAndWheelWidth": (5502, 2, (9, 0), (), "HubInnerFlangeAndWheelWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"HubRadius": (5504, 2, (9, 0), (), "HubRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"HubWidth": (5500, 2, (9, 0), (), "HubWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InnerFlangeRadius": (5505, 2, (9, 0), (), "InnerFlangeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"OuterFlangeRadius": (5507, 2, (9, 0), (), "OuterFlangeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalWidth": (5503, 2, (9, 0), (), "TotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WheelRadius": (5506, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackLMGeometryFlangeFlat(DispatchBaseClass):
	'''TrackLM flange flat geometry'''
	CLSID = IID('{3B1930FF-530C-4745-B19C-D335810BBDBD}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_RollerRadius(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "RollerRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RollerWidth(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "RollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	RollerRadius = property(_get_RollerRadius, None)
	'''
	Roller radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	RollerWidth = property(_get_RollerWidth, None)
	'''
	Roller width.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"RollerRadius": (5501, 2, (9, 0), (), "RollerRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RollerWidth": (5500, 2, (9, 0), (), "RollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackLMGeometryFlangeSingle(DispatchBaseClass):
	'''TrackLM flange single geometry'''
	CLSID = IID('{1552BF6E-3FFB-4111-A93D-A52A379E09CF}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_FlangeRadius(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "FlangeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_HubRadius(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "HubRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_HubWidth(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "HubWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalWidth(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "TotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WheelAndHubWidth(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "WheelAndHubWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WheelRadius(self):
		return self._ApplyTypes_(*(5504, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	FlangeRadius = property(_get_FlangeRadius, None)
	'''
	Flange radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	HubRadius = property(_get_HubRadius, None)
	'''
	Hub radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	HubWidth = property(_get_HubWidth, None)
	'''
	Hub width.

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalWidth = property(_get_TotalWidth, None)
	'''
	Total width.

	:type: recurdyn.ProcessNet.IDouble
	'''
	WheelAndHubWidth = property(_get_WheelAndHubWidth, None)
	'''
	Wheel and hub width.

	:type: recurdyn.ProcessNet.IDouble
	'''
	WheelRadius = property(_get_WheelRadius, None)
	'''
	Wheel radius.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"FlangeRadius": (5505, 2, (9, 0), (), "FlangeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"HubRadius": (5503, 2, (9, 0), (), "HubRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"HubWidth": (5500, 2, (9, 0), (), "HubWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalWidth": (5502, 2, (9, 0), (), "TotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WheelAndHubWidth": (5501, 2, (9, 0), (), "WheelAndHubWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WheelRadius": (5504, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackLMGeometryLink(DispatchBaseClass):
	'''TrackLM link geometry'''
	CLSID = IID('{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BushingWidth(self):
		return self._ApplyTypes_(*(5514, 2, (5, 0), (), "BushingWidth", None))
	def _get_ContactWithSprocketType(self):
		return self._ApplyTypes_(*(5510, 2, (3, 0), (), "ContactWithSprocketType", '{9C0717B5-A01B-40C7-8311-05C9AB30925F}'))
	def _get_GrouserWidth(self):
		return self._ApplyTypes_(*(5509, 2, (9, 0), (), "GrouserWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Height(self):
		return self._ApplyTypes_(*(5506, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InnerWidth(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "InnerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftBushingPosition(self):
		return self._ApplyTypes_(*(5512, 2, (8197, 0), (), "LeftBushingPosition", None))
	def _get_LeftLength(self):
		return self._ApplyTypes_(*(5504, 2, (9, 0), (), "LeftLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftPinPosition(self):
		return self._ApplyTypes_(*(5507, 2, (8197, 0), (), "LeftPinPosition", None))
	def _get_OuterWidth(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "OuterWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinRadius(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RightBushingPosition(self):
		return self._ApplyTypes_(*(5513, 2, (8197, 0), (), "RightBushingPosition", None))
	def _get_RightLength(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "RightLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RightPinPosition(self):
		return self._ApplyTypes_(*(5508, 2, (8197, 0), (), "RightPinPosition", None))
	def _get_UseBushingPosition(self):
		return self._ApplyTypes_(*(5511, 2, (11, 0), (), "UseBushingPosition", None))

	def _set_BushingWidth(self, value):
		if "BushingWidth" in self.__dict__: self.__dict__["BushingWidth"] = value; return
		self._oleobj_.Invoke(*((5514, LCID, 4, 0) + (value,) + ()))
	def _set_ContactWithSprocketType(self, value):
		if "ContactWithSprocketType" in self.__dict__: self.__dict__["ContactWithSprocketType"] = value; return
		self._oleobj_.Invoke(*((5510, LCID, 4, 0) + (value,) + ()))
	def _set_LeftBushingPosition(self, value):
		if "LeftBushingPosition" in self.__dict__: self.__dict__["LeftBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5512, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LeftPinPosition(self, value):
		if "LeftPinPosition" in self.__dict__: self.__dict__["LeftPinPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5507, LCID, 4, 0) + (variantValue,) + ()))
	def _set_RightBushingPosition(self, value):
		if "RightBushingPosition" in self.__dict__: self.__dict__["RightBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5513, LCID, 4, 0) + (variantValue,) + ()))
	def _set_RightPinPosition(self, value):
		if "RightPinPosition" in self.__dict__: self.__dict__["RightPinPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((5508, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseBushingPosition(self, value):
		if "UseBushingPosition" in self.__dict__: self.__dict__["UseBushingPosition"] = value; return
		self._oleobj_.Invoke(*((5511, LCID, 4, 0) + (value,) + ()))

	BushingWidth = property(_get_BushingWidth, _set_BushingWidth)
	'''
	Bushing Width (Bw)

	:type: float
	'''
	ContactWithSprocketType = property(_get_ContactWithSprocketType, _set_ContactWithSprocketType)
	'''
	Contact with sprocket type.

	:type: recurdyn.TrackLM.ContactSprocketType
	'''
	GrouserWidth = property(_get_GrouserWidth, None)
	'''
	Grouser width

	:type: recurdyn.ProcessNet.IDouble
	'''
	Height = property(_get_Height, None)
	'''
	Height

	:type: recurdyn.ProcessNet.IDouble
	'''
	InnerWidth = property(_get_InnerWidth, None)
	'''
	Inner width

	:type: recurdyn.ProcessNet.IDouble
	'''
	LeftBushingPosition = property(_get_LeftBushingPosition, _set_LeftBushingPosition)
	'''
	Left Bushing Position

	:type: list[float]
	'''
	LeftLength = property(_get_LeftLength, None)
	'''
	Left length

	:type: recurdyn.ProcessNet.IDouble
	'''
	LeftPinPosition = property(_get_LeftPinPosition, _set_LeftPinPosition)
	'''
	Left pin position

	:type: list[float]
	'''
	OuterWidth = property(_get_OuterWidth, None)
	'''
	Outer width

	:type: recurdyn.ProcessNet.IDouble
	'''
	PinLength = property(_get_PinLength, None)
	'''
	Pin length

	:type: recurdyn.ProcessNet.IDouble
	'''
	PinRadius = property(_get_PinRadius, None)
	'''
	Pin radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	RightBushingPosition = property(_get_RightBushingPosition, _set_RightBushingPosition)
	'''
	Right Bushing Position

	:type: list[float]
	'''
	RightLength = property(_get_RightLength, None)
	'''
	Right length

	:type: recurdyn.ProcessNet.IDouble
	'''
	RightPinPosition = property(_get_RightPinPosition, _set_RightPinPosition)
	'''
	Right pin position

	:type: list[float]
	'''
	UseBushingPosition = property(_get_UseBushingPosition, _set_UseBushingPosition)
	'''
	Use Bushing Position

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_BushingWidth": _set_BushingWidth,
		"_set_ContactWithSprocketType": _set_ContactWithSprocketType,
		"_set_LeftBushingPosition": _set_LeftBushingPosition,
		"_set_LeftPinPosition": _set_LeftPinPosition,
		"_set_RightBushingPosition": _set_RightBushingPosition,
		"_set_RightPinPosition": _set_RightPinPosition,
		"_set_UseBushingPosition": _set_UseBushingPosition,
	}
	_prop_map_get_ = {
		"BushingWidth": (5514, 2, (5, 0), (), "BushingWidth", None),
		"ContactWithSprocketType": (5510, 2, (3, 0), (), "ContactWithSprocketType", '{9C0717B5-A01B-40C7-8311-05C9AB30925F}'),
		"GrouserWidth": (5509, 2, (9, 0), (), "GrouserWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Height": (5506, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InnerWidth": (5502, 2, (9, 0), (), "InnerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftBushingPosition": (5512, 2, (8197, 0), (), "LeftBushingPosition", None),
		"LeftLength": (5504, 2, (9, 0), (), "LeftLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftPinPosition": (5507, 2, (8197, 0), (), "LeftPinPosition", None),
		"OuterWidth": (5503, 2, (9, 0), (), "OuterWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinLength": (5501, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinRadius": (5500, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RightBushingPosition": (5513, 2, (8197, 0), (), "RightBushingPosition", None),
		"RightLength": (5505, 2, (9, 0), (), "RightLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RightPinPosition": (5508, 2, (8197, 0), (), "RightPinPosition", None),
		"UseBushingPosition": (5511, 2, (11, 0), (), "UseBushingPosition", None),
	}
	_prop_map_put_ = {
		"BushingWidth": ((5514, LCID, 4, 0),()),
		"ContactWithSprocketType": ((5510, LCID, 4, 0),()),
		"LeftBushingPosition": ((5512, LCID, 4, 0),()),
		"LeftPinPosition": ((5507, LCID, 4, 0),()),
		"RightBushingPosition": ((5513, LCID, 4, 0),()),
		"RightPinPosition": ((5508, LCID, 4, 0),()),
		"UseBushingPosition": ((5511, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMGeometryRollerGuard(DispatchBaseClass):
	'''TrackLM geometry of roller guard '''
	CLSID = IID('{ABD47D59-1C65-4ACE-9DDA-0485A5EE880E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Height(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InactiveType(self):
		return self._ApplyTypes_(*(5504, 2, (3, 0), (), "InactiveType", '{674BB7BB-6BE5-41B4-93AA-649213BBDA72}'))
	def _get_InnerWidth(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "InnerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Length(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "Length", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_InactiveType(self, value):
		if "InactiveType" in self.__dict__: self.__dict__["InactiveType"] = value; return
		self._oleobj_.Invoke(*((5504, LCID, 4, 0) + (value,) + ()))

	Height = property(_get_Height, None)
	'''
	Height of the roller guard.

	:type: recurdyn.ProcessNet.IDouble
	'''
	InactiveType = property(_get_InactiveType, _set_InactiveType)
	'''
	Inactive type.

	:type: recurdyn.TrackLM.RollerGuardInactiveType
	'''
	InnerWidth = property(_get_InnerWidth, None)
	'''
	Inner width of the roller guard.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Length = property(_get_Length, None)
	'''
	Length of the roller guard.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Thickness = property(_get_Thickness, None)
	'''
	Thickness of the roller guard.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_InactiveType": _set_InactiveType,
	}
	_prop_map_get_ = {
		"Height": (5501, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InactiveType": (5504, 2, (3, 0), (), "InactiveType", '{674BB7BB-6BE5-41B4-93AA-649213BBDA72}'),
		"InnerWidth": (5502, 2, (9, 0), (), "InnerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Length": (5500, 2, (9, 0), (), "Length", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Thickness": (5503, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"InactiveType": ((5504, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMGeometrySprocket(DispatchBaseClass):
	'''TrackLMBodySprocketGeometry'''
	CLSID = IID('{FB048C8A-5E0F-414C-BB9A-16E7D2410E40}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AddendumCircleRadius(self):
		return self._ApplyTypes_(*(5507, 2, (9, 0), (), "AddendumCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_BaseCircleRadius(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "BaseCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DedendumCircleRadius(self):
		return self._ApplyTypes_(*(5504, 2, (9, 0), (), "DedendumCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(5511, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None))
	def _get_LinkAssemblyRadialDistance(self):
		return self._ApplyTypes_(*(5512, 2, (5, 0), (), "LinkAssemblyRadialDistance", None))
	def _get_NumberOfTeeth(self):
		return self._ApplyTypes_(*(5503, 2, (19, 0), (), "NumberOfTeeth", None))
	def _get_PitchCircleRadius(self):
		return self._ApplyTypes_(*(5506, 2, (9, 0), (), "PitchCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SprocketWheelRadius(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "SprocketWheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TrackLinkLoopRadius(self):
		return self._ApplyTypes_(*(5509, 2, (5, 0), (), "TrackLinkLoopRadius", None))
	def _get_TrackLinkPinCircleRadius(self):
		return self._ApplyTypes_(*(5508, 2, (5, 0), (), "TrackLinkPinCircleRadius", None))
	def _get_UseLinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(5510, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None))
	def _get_WidthBetweenWheels(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "WidthBetweenWheels", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WidthOfTeeth(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "WidthOfTeeth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_LinkAssemblyAssembledRadius(self, value):
		if "LinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["LinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((5511, LCID, 4, 0) + (value,) + ()))
	def _set_LinkAssemblyRadialDistance(self, value):
		if "LinkAssemblyRadialDistance" in self.__dict__: self.__dict__["LinkAssemblyRadialDistance"] = value; return
		self._oleobj_.Invoke(*((5512, LCID, 4, 0) + (value,) + ()))
	def _set_NumberOfTeeth(self, value):
		if "NumberOfTeeth" in self.__dict__: self.__dict__["NumberOfTeeth"] = value; return
		self._oleobj_.Invoke(*((5503, LCID, 4, 0) + (value,) + ()))
	def _set_TrackLinkLoopRadius(self, value):
		if "TrackLinkLoopRadius" in self.__dict__: self.__dict__["TrackLinkLoopRadius"] = value; return
		self._oleobj_.Invoke(*((5509, LCID, 4, 0) + (value,) + ()))
	def _set_TrackLinkPinCircleRadius(self, value):
		if "TrackLinkPinCircleRadius" in self.__dict__: self.__dict__["TrackLinkPinCircleRadius"] = value; return
		self._oleobj_.Invoke(*((5508, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkAssemblyAssembledRadius(self, value):
		if "UseLinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["UseLinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((5510, LCID, 4, 0) + (value,) + ()))

	AddendumCircleRadius = property(_get_AddendumCircleRadius, None)
	'''
	Addendum circle radius of the sprocket.

	:type: recurdyn.ProcessNet.IDouble
	'''
	BaseCircleRadius = property(_get_BaseCircleRadius, None)
	'''
	Base circle radius of the sprocket.

	:type: recurdyn.ProcessNet.IDouble
	'''
	DedendumCircleRadius = property(_get_DedendumCircleRadius, None)
	'''
	Dedendum circle radius of the sprocket.

	:type: recurdyn.ProcessNet.IDouble
	'''
	LinkAssemblyAssembledRadius = property(_get_LinkAssemblyAssembledRadius, _set_LinkAssemblyAssembledRadius)
	'''
	Assembled radius of the link assembly.

	:type: float
	'''
	LinkAssemblyRadialDistance = property(_get_LinkAssemblyRadialDistance, _set_LinkAssemblyRadialDistance)
	'''
	Radial radius of the link assembly.

	:type: float
	'''
	NumberOfTeeth = property(_get_NumberOfTeeth, _set_NumberOfTeeth)
	'''
	Number of teeth of the sprocket.

	:type: int
	'''
	PitchCircleRadius = property(_get_PitchCircleRadius, None)
	'''
	Pitch circle radius of the sprocket.

	:type: recurdyn.ProcessNet.IDouble
	'''
	SprocketWheelRadius = property(_get_SprocketWheelRadius, None)
	'''
	Wheel radius of the sprocket.

	:type: recurdyn.ProcessNet.IDouble
	'''
	TrackLinkLoopRadius = property(_get_TrackLinkLoopRadius, _set_TrackLinkLoopRadius)
	'''
	Track link loop radius ot the sprocket.

	:type: float
	'''
	TrackLinkPinCircleRadius = property(_get_TrackLinkPinCircleRadius, _set_TrackLinkPinCircleRadius)
	'''
	Track link pin circle radius ot the sprocket.

	:type: float
	'''
	UseLinkAssemblyAssembledRadius = property(_get_UseLinkAssemblyAssembledRadius, _set_UseLinkAssemblyAssembledRadius)
	'''
	Use assembled radius.

	:type: bool
	'''
	WidthBetweenWheels = property(_get_WidthBetweenWheels, None)
	'''
	Width between wheels of the sprocket.

	:type: recurdyn.ProcessNet.IDouble
	'''
	WidthOfTeeth = property(_get_WidthOfTeeth, None)
	'''
	Width of teeth of the sprocket.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_LinkAssemblyAssembledRadius": _set_LinkAssemblyAssembledRadius,
		"_set_LinkAssemblyRadialDistance": _set_LinkAssemblyRadialDistance,
		"_set_NumberOfTeeth": _set_NumberOfTeeth,
		"_set_TrackLinkLoopRadius": _set_TrackLinkLoopRadius,
		"_set_TrackLinkPinCircleRadius": _set_TrackLinkPinCircleRadius,
		"_set_UseLinkAssemblyAssembledRadius": _set_UseLinkAssemblyAssembledRadius,
	}
	_prop_map_get_ = {
		"AddendumCircleRadius": (5507, 2, (9, 0), (), "AddendumCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"BaseCircleRadius": (5505, 2, (9, 0), (), "BaseCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DedendumCircleRadius": (5504, 2, (9, 0), (), "DedendumCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LinkAssemblyAssembledRadius": (5511, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None),
		"LinkAssemblyRadialDistance": (5512, 2, (5, 0), (), "LinkAssemblyRadialDistance", None),
		"NumberOfTeeth": (5503, 2, (19, 0), (), "NumberOfTeeth", None),
		"PitchCircleRadius": (5506, 2, (9, 0), (), "PitchCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SprocketWheelRadius": (5500, 2, (9, 0), (), "SprocketWheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TrackLinkLoopRadius": (5509, 2, (5, 0), (), "TrackLinkLoopRadius", None),
		"TrackLinkPinCircleRadius": (5508, 2, (5, 0), (), "TrackLinkPinCircleRadius", None),
		"UseLinkAssemblyAssembledRadius": (5510, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None),
		"WidthBetweenWheels": (5502, 2, (9, 0), (), "WidthBetweenWheels", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WidthOfTeeth": (5501, 2, (9, 0), (), "WidthOfTeeth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"LinkAssemblyAssembledRadius": ((5511, LCID, 4, 0),()),
		"LinkAssemblyRadialDistance": ((5512, LCID, 4, 0),()),
		"NumberOfTeeth": ((5503, LCID, 4, 0),()),
		"TrackLinkLoopRadius": ((5509, LCID, 4, 0),()),
		"TrackLinkPinCircleRadius": ((5508, LCID, 4, 0),()),
		"UseLinkAssemblyAssembledRadius": ((5510, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMGrouserContactProperty(DispatchBaseClass):
	'''TrackLM grouser contact property'''
	CLSID = IID('{860E76B0-9B85-4973-AE10-CA2BD4FEA254}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(5512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(5506, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(5508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(5510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(5502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(5511, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(5504, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseFrictionSpline(self):
		return self._ApplyTypes_(*(5507, 2, (11, 0), (), "UseFrictionSpline", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(5509, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(5501, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((5505, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((5508, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5502, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((5511, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((5504, LCID, 4, 0) + (value,) + ()))
	def _set_UseFrictionSpline(self, value):
		if "UseFrictionSpline" in self.__dict__: self.__dict__["UseFrictionSpline"] = value; return
		self._oleobj_.Invoke(*((5507, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5509, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5501, LCID, 4, 0) + (value,) + ()))

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
	Use friction spline

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
		"_set_DampingSpline": _set_DampingSpline,
		"_set_FrictionSpline": _set_FrictionSpline,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseFrictionSpline": _set_UseFrictionSpline,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
	}
	_prop_map_get_ = {
		"DampingCoefficient": (5503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (5512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (5505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionCoefficient": (5506, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (5508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"StiffnessCoefficient": (5500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (5510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (5502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (5511, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (5504, 2, (11, 0), (), "UseDampingSpline", None),
		"UseFrictionSpline": (5507, 2, (11, 0), (), "UseFrictionSpline", None),
		"UseStiffnessExponent": (5509, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (5501, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"DampingSpline": ((5505, LCID, 4, 0),()),
		"FrictionSpline": ((5508, LCID, 4, 0),()),
		"StiffnessSpline": ((5502, LCID, 4, 0),()),
		"UseDampingExponent": ((5511, LCID, 4, 0),()),
		"UseDampingSpline": ((5504, LCID, 4, 0),()),
		"UseFrictionSpline": ((5507, LCID, 4, 0),()),
		"UseStiffnessExponent": ((5509, LCID, 4, 0),()),
		"UseStiffnessSpline": ((5501, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMGrouserToSphereContactProperty(DispatchBaseClass):
	'''TrackLM grouser to sphere contact property'''
	CLSID = IID('{674DD026-A8F6-4A8B-91ED-0CF92C531AE3}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(5504, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(5513, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(5506, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(5507, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(5509, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(5516, 2, (3, 0), (), "FrictionType", '{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(5515, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(5511, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(5512, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(5505, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseFrictionSpline(self):
		return self._ApplyTypes_(*(5508, 2, (11, 0), (), "UseFrictionSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(5514, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(5510, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(5502, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((5506, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((5509, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((5516, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5503, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((5512, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((5505, LCID, 4, 0) + (value,) + ()))
	def _set_UseFrictionSpline(self, value):
		if "UseFrictionSpline" in self.__dict__: self.__dict__["UseFrictionSpline"] = value; return
		self._oleobj_.Invoke(*((5508, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((5514, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((5510, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((5502, LCID, 4, 0) + (value,) + ()))

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
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction type

	:type: recurdyn.TrackLM.TrackLMFrictionType
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
	Use friction spline

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
		"_set_DampingSpline": _set_DampingSpline,
		"_set_FrictionSpline": _set_FrictionSpline,
		"_set_FrictionType": _set_FrictionType,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseFrictionSpline": _set_UseFrictionSpline,
		"_set_UseIndentationExponent": _set_UseIndentationExponent,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
	}
	_prop_map_get_ = {
		"DampingCoefficient": (5504, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (5513, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (5506, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionCoefficient": (5507, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (5509, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (5516, 2, (3, 0), (), "FrictionType", '{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}'),
		"IndentationExponent": (5515, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (5501, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (5511, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (5503, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (5512, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (5505, 2, (11, 0), (), "UseDampingSpline", None),
		"UseFrictionSpline": (5508, 2, (11, 0), (), "UseFrictionSpline", None),
		"UseIndentationExponent": (5514, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseStiffnessExponent": (5510, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (5502, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"DampingSpline": ((5506, LCID, 4, 0),()),
		"FrictionSpline": ((5509, LCID, 4, 0),()),
		"FrictionType": ((5516, LCID, 4, 0),()),
		"StiffnessSpline": ((5503, LCID, 4, 0),()),
		"UseDampingExponent": ((5512, LCID, 4, 0),()),
		"UseDampingSpline": ((5505, LCID, 4, 0),()),
		"UseFrictionSpline": ((5508, LCID, 4, 0),()),
		"UseIndentationExponent": ((5514, LCID, 4, 0),()),
		"UseStiffnessExponent": ((5510, LCID, 4, 0),()),
		"UseStiffnessSpline": ((5502, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMLinkClone(DispatchBaseClass):
	'''TrackLM Link Clone'''
	CLSID = IID('{AD229002-EF52-48FC-9389-8A6A49EDAA72}')
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
		return self._oleobj_.InvokeTypes(5521, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(5520, LCID, 1, (24, 0), ((8, 1),),strFile
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
		return self._oleobj_.InvokeTypes(5519, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(5517, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(5522, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(5518, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(5515, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "Geometry", '{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(5507, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(5510, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(5508, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(5511, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(5512, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(5509, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LinkGrouserProfile(self):
		return self._ApplyTypes_(*(5504, 2, (9, 0), (), "LinkGrouserProfile", '{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}'))
	def _get_LinkShapeProfile(self):
		return self._ApplyTypes_(*(5503, 2, (9, 0), (), "LinkShapeProfile", '{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(5506, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(5514, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(5513, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(5516, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseLinkShape(self):
		return self._ApplyTypes_(*(5502, 2, (11, 0), (), "UseLinkShape", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((5522, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((5515, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((5514, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((5513, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((5516, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkShape(self, value):
		if "UseLinkShape" in self.__dict__: self.__dict__["UseLinkShape"] = value; return
		self._oleobj_.Invoke(*((5502, LCID, 4, 0) + (value,) + ()))
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

	:type: recurdyn.TrackLM.ITrackLMGeometryLink
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
	LinkGrouserProfile = property(_get_LinkGrouserProfile, None)
	'''
	Link grouser profile

	:type: recurdyn.TrackLM.ITrackLMProfileLinkGrouser
	'''
	LinkShapeProfile = property(_get_LinkShapeProfile, None)
	'''
	Link shape profile

	:type: recurdyn.TrackLM.ITrackLMProfileLinkShape
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
	UseLinkShape = property(_get_UseLinkShape, _set_UseLinkShape)
	'''
	Use link shape

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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UseLinkShape": _set_UseLinkShape,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (5522, 2, (11, 0), (), "Active", None),
		"CenterMarker": (5518, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (5515, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (5501, 2, (9, 0), (), "Geometry", '{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}'),
		"Graphic": (5505, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (5507, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (5510, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (5508, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (5511, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (5512, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (5509, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LinkGrouserProfile": (5504, 2, (9, 0), (), "LinkGrouserProfile", '{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}'),
		"LinkShapeProfile": (5503, 2, (9, 0), (), "LinkShapeProfile", '{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}'),
		"Mass": (5506, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (5514, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (5513, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (5516, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseLinkShape": (5502, 2, (11, 0), (), "UseLinkShape", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((5522, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((5515, LCID, 4, 0),()),
		"Material": ((5514, LCID, 4, 0),()),
		"MaterialInput": ((5513, LCID, 4, 0),()),
		"MaterialUser": ((5516, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseLinkShape": ((5502, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMLinkCloneCollection(DispatchBaseClass):
	'''TrackLM Clone Link Collection'''
	CLSID = IID('{6939141C-3175-47EB-A3B5-5267300EEA6F}')
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
		:rtype: recurdyn.TrackLM.ITrackLMLinkClone
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{AD229002-EF52-48FC-9389-8A6A49EDAA72}')
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
		:rtype: recurdyn.TrackLM.ITrackLMLinkClone
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{AD229002-EF52-48FC-9389-8A6A49EDAA72}')
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
		return win32com.client.util.Iterator(ob, '{AD229002-EF52-48FC-9389-8A6A49EDAA72}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{AD229002-EF52-48FC-9389-8A6A49EDAA72}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITrackLMProfileLinkGrouser(DispatchBaseClass):
	'''TrackLM link grouser profile'''
	CLSID = IID('{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Export(self, strFileName):
		'''
		Export point list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(5503, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def Import(self, strFileName):
		'''
		Import point list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(5502, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def ReverseProfilePoints(self):
		'''
		Reverse profile points
		'''
		return self._oleobj_.InvokeTypes(5516, LCID, 1, (24, 0), (),)


	def ShoePointExport(self, strFileName):
		'''
		Export shoe point
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(5507, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def ShoePointImport(self, strFileName):
		'''
		Import shoe point
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(5506, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def Update(self):
		'''
		Update method
		'''
		return self._oleobj_.InvokeTypes(5504, LCID, 1, (24, 0), (),)


	def _get_GrouserMeshDepthSegment(self):
		return self._ApplyTypes_(*(5515, 2, (19, 0), (), "GrouserMeshDepthSegment", None))
	def _get_GrouserMeshEndNode(self):
		return self._ApplyTypes_(*(5513, 2, (19, 0), (), "GrouserMeshEndNode", None))
	def _get_GrouserMeshLengthSegment(self):
		return self._ApplyTypes_(*(5514, 2, (19, 0), (), "GrouserMeshLengthSegment", None))
	def _get_GrouserMeshStartNode(self):
		return self._ApplyTypes_(*(5512, 2, (19, 0), (), "GrouserMeshStartNode", None))
	def _get_GrouserToSphereContactEndNode(self):
		return self._ApplyTypes_(*(5511, 2, (19, 0), (), "GrouserToSphereContactEndNode", None))
	def _get_GrouserToSphereContactStartNode(self):
		return self._ApplyTypes_(*(5510, 2, (19, 0), (), "GrouserToSphereContactStartNode", None))
	def _get_Point2DCollection(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "Point2DCollection", '{CDBA1369-C276-42F4-8C85-562A82C32E54}'))
	def _get_ShoePoint3DCollection(self):
		return self._ApplyTypes_(*(5505, 2, (9, 0), (), "ShoePoint3DCollection", '{7AAA986F-35DD-4DCF-843A-CEBA8E09D33A}'))

	def _set_GrouserMeshDepthSegment(self, value):
		if "GrouserMeshDepthSegment" in self.__dict__: self.__dict__["GrouserMeshDepthSegment"] = value; return
		self._oleobj_.Invoke(*((5515, LCID, 4, 0) + (value,) + ()))
	def _set_GrouserMeshEndNode(self, value):
		if "GrouserMeshEndNode" in self.__dict__: self.__dict__["GrouserMeshEndNode"] = value; return
		self._oleobj_.Invoke(*((5513, LCID, 4, 0) + (value,) + ()))
	def _set_GrouserMeshLengthSegment(self, value):
		if "GrouserMeshLengthSegment" in self.__dict__: self.__dict__["GrouserMeshLengthSegment"] = value; return
		self._oleobj_.Invoke(*((5514, LCID, 4, 0) + (value,) + ()))
	def _set_GrouserMeshStartNode(self, value):
		if "GrouserMeshStartNode" in self.__dict__: self.__dict__["GrouserMeshStartNode"] = value; return
		self._oleobj_.Invoke(*((5512, LCID, 4, 0) + (value,) + ()))
	def _set_GrouserToSphereContactEndNode(self, value):
		if "GrouserToSphereContactEndNode" in self.__dict__: self.__dict__["GrouserToSphereContactEndNode"] = value; return
		self._oleobj_.Invoke(*((5511, LCID, 4, 0) + (value,) + ()))
	def _set_GrouserToSphereContactStartNode(self, value):
		if "GrouserToSphereContactStartNode" in self.__dict__: self.__dict__["GrouserToSphereContactStartNode"] = value; return
		self._oleobj_.Invoke(*((5510, LCID, 4, 0) + (value,) + ()))

	GrouserMeshDepthSegment = property(_get_GrouserMeshDepthSegment, _set_GrouserMeshDepthSegment)
	'''
	Depth segment of grouser mesh

	:type: int
	'''
	GrouserMeshEndNode = property(_get_GrouserMeshEndNode, _set_GrouserMeshEndNode)
	'''
	End node of grouser mesh

	:type: int
	'''
	GrouserMeshLengthSegment = property(_get_GrouserMeshLengthSegment, _set_GrouserMeshLengthSegment)
	'''
	Length segment of grouser mesh

	:type: int
	'''
	GrouserMeshStartNode = property(_get_GrouserMeshStartNode, _set_GrouserMeshStartNode)
	'''
	Start node of grouser mesh

	:type: int
	'''
	GrouserToSphereContactEndNode = property(_get_GrouserToSphereContactEndNode, _set_GrouserToSphereContactEndNode)
	'''
	Contact end node of grouser to sphere

	:type: int
	'''
	GrouserToSphereContactStartNode = property(_get_GrouserToSphereContactStartNode, _set_GrouserToSphereContactStartNode)
	'''
	Contact start node of grouser to sphere

	:type: int
	'''
	Point2DCollection = property(_get_Point2DCollection, None)
	'''
	2D Point Collection

	:type: recurdyn.ProcessNet.IPoint2DCollection
	'''
	ShoePoint3DCollection = property(_get_ShoePoint3DCollection, None)
	'''
	3D Point Collection

	:type: recurdyn.ProcessNet.IPoint3DCollection
	'''

	_prop_map_set_function_ = {
		"_set_GrouserMeshDepthSegment": _set_GrouserMeshDepthSegment,
		"_set_GrouserMeshEndNode": _set_GrouserMeshEndNode,
		"_set_GrouserMeshLengthSegment": _set_GrouserMeshLengthSegment,
		"_set_GrouserMeshStartNode": _set_GrouserMeshStartNode,
		"_set_GrouserToSphereContactEndNode": _set_GrouserToSphereContactEndNode,
		"_set_GrouserToSphereContactStartNode": _set_GrouserToSphereContactStartNode,
	}
	_prop_map_get_ = {
		"GrouserMeshDepthSegment": (5515, 2, (19, 0), (), "GrouserMeshDepthSegment", None),
		"GrouserMeshEndNode": (5513, 2, (19, 0), (), "GrouserMeshEndNode", None),
		"GrouserMeshLengthSegment": (5514, 2, (19, 0), (), "GrouserMeshLengthSegment", None),
		"GrouserMeshStartNode": (5512, 2, (19, 0), (), "GrouserMeshStartNode", None),
		"GrouserToSphereContactEndNode": (5511, 2, (19, 0), (), "GrouserToSphereContactEndNode", None),
		"GrouserToSphereContactStartNode": (5510, 2, (19, 0), (), "GrouserToSphereContactStartNode", None),
		"Point2DCollection": (5501, 2, (9, 0), (), "Point2DCollection", '{CDBA1369-C276-42F4-8C85-562A82C32E54}'),
		"ShoePoint3DCollection": (5505, 2, (9, 0), (), "ShoePoint3DCollection", '{7AAA986F-35DD-4DCF-843A-CEBA8E09D33A}'),
	}
	_prop_map_put_ = {
		"GrouserMeshDepthSegment": ((5515, LCID, 4, 0),()),
		"GrouserMeshEndNode": ((5513, LCID, 4, 0),()),
		"GrouserMeshLengthSegment": ((5514, LCID, 4, 0),()),
		"GrouserMeshStartNode": ((5512, LCID, 4, 0),()),
		"GrouserToSphereContactEndNode": ((5511, LCID, 4, 0),()),
		"GrouserToSphereContactStartNode": ((5510, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackLMProfileLinkShape(DispatchBaseClass):
	'''TrackLM link shape profile'''
	CLSID = IID('{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Export(self, strFileName):
		'''
		Export point list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(5503, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def Import(self, strFileName):
		'''
		Import point list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(5502, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def _get_PointCollection(self):
		return self._ApplyTypes_(*(5501, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	PointCollection = property(_get_PointCollection, None)
	'''
	3D Point Collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PointCollection": (5501, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
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

class ITrackLMSubSystem(DispatchBaseClass):
	'''TrackLM subsystem'''
	CLSID = IID('{D0902FEE-86C9-4F2C-98CA-8113ED49E973}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def ConvertAssemblyLinksToBodies(self, assembly, numOfBushing):
		'''
		Convert all links of the assembly to general bodies
		
		:param assembly: ITrackLMAssembly
		:param numOfBushing: int
		:rtype: list[object]
		'''
		return self._ApplyTypes_(5521, 1, (24, 0), ((9, 1), (19, 1), (24588, 2)), 'ConvertAssemblyLinksToBodies', None,assembly
			, numOfBushing, pythoncom.Missing)


	def ConvertLinksToBodies(self, assembly, numOfBushing, links):
		'''
		Convert links to bodies
		
		:param assembly: ITrackLMAssembly
		:param numOfBushing: int
		:param links: list[object]
		:rtype: (list[object], list[object])
		'''
		_links_type = True if links and isinstance(links[0], win32com.client.VARIANT) else False
		if not _links_type:
			links = [win32com.client.VARIANT(12, _data) for _data in links]

		ret = self._ApplyTypes_(5512, 1, (24, 0), ((9, 1), (19, 1), (8204, 1), (24588, 2), (24588, 2)), 'ConvertLinksToBodies', None,assembly
			, numOfBushing, links, pythoncom.Missing, pythoncom.Missing)

		if not _links_type:
			links = [_data.value for _data in links]

		return ret


	def CreateBodyFlangeCenter(self, strName, pPoint):
		'''
		Create a single center
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackLM.ITrackLMBodyFlangeCenter
		'''
		ret = self._oleobj_.InvokeTypes(5504, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyFlangeCenter', '{B142F053-F79F-4E72-9252-26D82A373001}')
		return ret

	def CreateBodyFlangeDouble(self, strName, pPoint):
		'''
		Create a single double
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackLM.ITrackLMBodyFlangeDouble
		'''
		ret = self._oleobj_.InvokeTypes(5503, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyFlangeDouble', '{7C581B15-F7A8-4FD4-B732-07DD8661FE01}')
		return ret

	def CreateBodyFlangeFlat(self, strName, pPoint):
		'''
		Create a single flat
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackLM.ITrackLMBodyFlangeFlat
		'''
		ret = self._oleobj_.InvokeTypes(5505, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyFlangeFlat', '{1413E74E-9CDE-4E83-9BC2-14F6C0783FC0}')
		return ret

	def CreateBodyFlangeSingle(self, strName, pPoint):
		'''
		Create a single flange
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackLM.ITrackLMBodyFlangeSingle
		'''
		ret = self._oleobj_.InvokeTypes(5502, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyFlangeSingle', '{0FBAD430-C81A-4870-9D3E-9F6497D2C565}')
		return ret

	def CreateBodyRollerGuard(self, strName, pFirstPoint, pSecondPoint):
		'''
		Create a roller guard
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:rtype: recurdyn.TrackLM.ITrackLMBodyRollerGuard
		'''
		ret = self._oleobj_.InvokeTypes(5506, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1)),strName
			, pFirstPoint, pSecondPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyRollerGuard', '{E873D6AC-B791-48F4-B0AB-12560562B540}')
		return ret

	def CreateBodySprocket(self, strName, pPoint):
		'''
		Create a body sprocket
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackLM.ITrackLMBodySprocket
		'''
		ret = self._oleobj_.InvokeTypes(5501, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodySprocket', '{C809FD1D-0B5D-4F2C-843C-BFBFCD795B11}')
		return ret

	def CreateContactTrackToSurface(self, strName, pBaseBody, pActionBody):
		'''
		Create track assembly to surface contact
		
		:param strName: str
		:param pBaseBody: IGeneric
		:param pActionBody: IGeneric
		:rtype: recurdyn.ToolkitCommon.IContactTrackToSurface
		'''
		ret = self._oleobj_.InvokeTypes(5519, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody)
		if ret is not None:
			ret = Dispatch(ret, 'CreateContactTrackToSurface', '{1EAD15B7-3DFF-40FD-BD77-12CBB9F2CA6C}')
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
		ret = self._oleobj_.InvokeTypes(5518, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
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
		ret = self._oleobj_.InvokeTypes(5515, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
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
		ret = self._oleobj_.InvokeTypes(5516, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
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
		ret = self._oleobj_.InvokeTypes(5517, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pBaseRefFrame, pActionRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorSpring', '{93A5A572-A6DD-4F12-A3E5-64F95B78718F}')
		return ret

	def CreateLinkClone(self, strName, pPoint):
		'''
		Create a track link
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackLM.ITrackLMLinkClone
		'''
		ret = self._oleobj_.InvokeTypes(5507, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLinkClone', '{AD229002-EF52-48FC-9389-8A6A49EDAA72}')
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
		ret = self._oleobj_.InvokeTypes(5513, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (5, 1)),strName
			, pEntity, pSensorMarker, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorDisplacement', '{08F5AF0B-ADB1-4AB4-8FAB-54ADCB9B5F36}')
		return ret

	def CreateTrackAssembly(self, strName, pLinkClone, pBodyList, pInOutList, uiNumberOfLink):
		'''
		Create track assembly
		
		:param strName: str
		:param pLinkClone: ITrackLMLinkClone
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfLink: int
		:rtype: recurdyn.TrackLM.ITrackLMAssembly
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(5508, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (19, 1)),strName
			, pLinkClone, pBodyList, pInOutList, uiNumberOfLink)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateTrackAssembly', '{F3294DCE-CF25-4511-986C-DC2D245853B1}')
		return ret

	def CreateTrackAssemblyWithAutomaticSprocketAlignment(self, strName, pLinkClone, pBodyList, pInOutList, uiNumberOfLink):
		'''
		Create track assembly and fit sprockets to assembly
		
		:param strName: str
		:param pLinkClone: ITrackLMLinkClone
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfLink: int
		:rtype: recurdyn.TrackLM.ITrackLMAssembly
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(5520, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (19, 1)),strName
			, pLinkClone, pBodyList, pInOutList, uiNumberOfLink)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateTrackAssemblyWithAutomaticSprocketAlignment', '{F3294DCE-CF25-4511-986C-DC2D245853B1}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_AssemblyCollection(self):
		return self._ApplyTypes_(*(5510, 2, (9, 0), (), "AssemblyCollection", '{22BE609F-1707-46CF-AA73-5BF5C0F577C4}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_LinkCloneCollection(self):
		return self._ApplyTypes_(*(5509, 2, (9, 0), (), "LinkCloneCollection", '{6939141C-3175-47EB-A3B5-5267300EEA6F}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_TrackLMBodyCollection(self):
		return self._ApplyTypes_(*(5511, 2, (9, 0), (), "TrackLMBodyCollection", '{2E24F362-D8AA-41AD-8BD4-CD92CF24C188}'))
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

	AssemblyCollection = property(_get_AssemblyCollection, None)
	'''
	Get the collection of assembly

	:type: recurdyn.TrackLM.ITrackLMAssemblyCollection
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
	GeneralSubSystem = property(_get_GeneralSubSystem, None)
	'''
	General subsystem

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	LinkCloneCollection = property(_get_LinkCloneCollection, None)
	'''
	Get the collection of clones

	:type: recurdyn.TrackLM.ITrackLMLinkCloneCollection
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
	TrackLMBodyCollection = property(_get_TrackLMBodyCollection, None)
	'''
	Get the TrackLM body collection of assembly

	:type: recurdyn.TrackLM.ITrackLMBodyCollection
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
		"AssemblyCollection": (5510, 2, (9, 0), (), "AssemblyCollection", '{22BE609F-1707-46CF-AA73-5BF5C0F577C4}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralSubSystem": (5500, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"LinkCloneCollection": (5509, 2, (9, 0), (), "LinkCloneCollection", '{6939141C-3175-47EB-A3B5-5267300EEA6F}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"TrackLMBodyCollection": (5511, 2, (9, 0), (), "TrackLMBodyCollection", '{2E24F362-D8AA-41AD-8BD4-CD92CF24C188}'),
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

class ITrackLMToothProfileSprocket(DispatchBaseClass):
	'''TrackLMToothProfileSprocket'''
	CLSID = IID('{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}')
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
		return self._oleobj_.InvokeTypes(5501, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(5502, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_PointCollection(self):
		return self._ApplyTypes_(*(5500, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	PointCollection = property(_get_PointCollection, None)
	'''
	Point Collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PointCollection": (5500, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
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

IPassingBodyCollection_vtables_dispatch_ = 1
IPassingBodyCollection_vtables_ = [
]

ITrackLMAssembly_vtables_dispatch_ = 1
ITrackLMAssembly_vtables_ = [
	(( 'UsePressureSinkage' , 'pVal' , ), 5500, (5500, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UsePressureSinkage' , 'pVal' , ), 5500, (5500, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameter' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{C37B595D-DE29-465E-88F7-288C5C63D7F7}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PassingBodyCollection' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{E26794CD-5D37-4617-BB5A-1AD85F3ED410}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody' , 'pVal' , ), 5503, (5503, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody' , 'pVal' , ), 5504, (5504, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GrouserToSphereContact' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{71434E11-33AF-44E5-B36F-D0D92753A768}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LinkNumbers' , 'pVal' , ), 5506, (5506, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LinkInitialVelocityXAxis' , 'ppVal' , ), 5507, (5507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'TrackLMBodyLinkCollection' , 'ppVal' , ), 5508, (5508, (), [ (16393, 10, None, "IID('{7E3C5275-F00D-4675-BAF6-9AE63689F8D2}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BushingForceParameter' , 'ppVal' , ), 5509, (5509, (), [ (16393, 10, None, "IID('{08A3F46B-C852-46F4-BCE6-11A84CFD7C2B}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetOutputLinkList' , 'ppSafeArray' , ), 5510, (5510, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'AddOutputLink' , 'strFileName' , ), 5511, (5511, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputLink' , 'strFileName' , ), 5512, (5512, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'AddAllOutputLink' , ), 5513, (5513, (), [ ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RemoveAllOutputLink' , ), 5514, (5514, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CreateGrouserContact' , 'ppResult' , ), 5515, (5515, (), [ (16393, 10, None, "IID('{41C77E5C-5A0D-4060-9668-47AAEE4E7575}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DeleteGrouserContact' , 'pVal' , ), 5516, (5516, (), [ (9, 1, None, "IID('{41C77E5C-5A0D-4060-9668-47AAEE4E7575}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GrouserContactCollection' , 'ppVal' , ), 5517, (5517, (), [ (16393, 10, None, "IID('{68152AA0-4470-4F17-AEF7-F45AA9ABE529}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveGrouserContact' , 'pVal' , ), 5518, (5518, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveGrouserContact' , 'pVal' , ), 5518, (5518, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GrouserContactProperty' , 'ppVal' , ), 5519, (5519, (), [ (16393, 10, None, "IID('{860E76B0-9B85-4973-AE10-CA2BD4FEA254}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'BushingForceCollection' , 'ppVal' , ), 5520, (5520, (), [ (16393, 10, None, "IID('{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UpdateLinkInitialVelocity' , ), 5521, (5521, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody2' , 'pVal' , ), 5522, (5522, (), [ (9, 1, None, "IID('{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody2' , 'pVal' , ), 5523, (5523, (), [ (9, 1, None, "IID('{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}')") , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
]

ITrackLMAssemblyBushingForceParameter_vtables_dispatch_ = 1
ITrackLMAssemblyBushingForceParameter_vtables_ = [
	(( 'TranslationStiffnessCoefficientRadial' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessCoefficientAxial' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessSpline' , 'pVal' , ), 5502, (5502, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessSpline' , 'pVal' , ), 5502, (5502, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineRadial' , 'ppVal' , ), 5503, (5503, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineRadial' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineAxial' , 'ppVal' , ), 5504, (5504, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineAxial' , 'ppVal' , ), 5504, (5504, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingCoefficientRadial' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingCoefficientAxial' , 'ppVal' , ), 5506, (5506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingSpline' , 'pVal' , ), 5507, (5507, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingSpline' , 'pVal' , ), 5507, (5507, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineRadial' , 'ppVal' , ), 5508, (5508, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineRadial' , 'ppVal' , ), 5508, (5508, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineAxial' , 'ppVal' , ), 5509, (5509, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineAxial' , 'ppVal' , ), 5509, (5509, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TranslationPreloadRadial' , 'ppVal' , ), 5510, (5510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'TranslationPreloadAxial' , 'ppVal' , ), 5511, (5511, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TranslationClearance' , 'ppVal' , ), 5512, (5512, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessCoefficientX' , 'ppVal' , ), 5513, (5513, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessCoefficientY' , 'ppVal' , ), 5514, (5514, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessCoefficientZ' , 'ppVal' , ), 5515, (5515, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessSpline' , 'pVal' , ), 5516, (5516, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessSpline' , 'pVal' , ), 5516, (5516, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineX' , 'ppVal' , ), 5517, (5517, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineX' , 'ppVal' , ), 5517, (5517, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineY' , 'ppVal' , ), 5518, (5518, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineY' , 'ppVal' , ), 5518, (5518, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineZ' , 'ppVal' , ), 5519, (5519, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineZ' , 'ppVal' , ), 5519, (5519, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingCoefficientX' , 'ppVal' , ), 5520, (5520, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingCoefficientY' , 'ppVal' , ), 5521, (5521, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingCoefficientZ' , 'ppVal' , ), 5522, (5522, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingSpline' , 'pVal' , ), 5523, (5523, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingSpline' , 'pVal' , ), 5523, (5523, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineX' , 'ppVal' , ), 5524, (5524, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineX' , 'ppVal' , ), 5524, (5524, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineY' , 'ppVal' , ), 5525, (5525, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineY' , 'ppVal' , ), 5525, (5525, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineZ' , 'ppVal' , ), 5526, (5526, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineZ' , 'ppVal' , ), 5526, (5526, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RotationPreloadX' , 'ppVal' , ), 5527, (5527, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'RotationPreloadY' , 'ppVal' , ), 5528, (5528, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'RotationPreloadZ' , 'ppVal' , ), 5529, (5529, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'RotationPresetAngle' , 'ppVal' , ), 5530, (5530, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStopAngle' , 'pVal' , ), 5531, (5531, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStopAngle' , 'pVal' , ), 5531, (5531, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'RotationStopAngle' , 'ppVal' , ), 5532, (5532, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'RotationStopStiffnessFactor' , 'ppVal' , ), 5533, (5533, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 5534, (5534, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 5534, (5534, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessExponentRadial' , 'ppVal' , ), 5535, (5535, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessExponentAxial' , 'ppVal' , ), 5536, (5536, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 5537, (5537, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 5537, (5537, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingExponentRadial' , 'ppVal' , ), 5538, (5538, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingExponentAxial' , 'ppVal' , ), 5539, (5539, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 5540, (5540, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 5540, (5540, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponentX' , 'ppVal' , ), 5541, (5541, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponentY' , 'ppVal' , ), 5542, (5542, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponentZ' , 'ppVal' , ), 5543, (5543, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 5544, (5544, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 5544, (5544, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponentX' , 'ppVal' , ), 5545, (5545, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponentY' , 'ppVal' , ), 5546, (5546, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponentZ' , 'ppVal' , ), 5547, (5547, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 5548, (5548, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 5549, (5549, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
]

ITrackLMAssemblyCollection_vtables_dispatch_ = 1
ITrackLMAssemblyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{F3294DCE-CF25-4511-986C-DC2D245853B1}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITrackLMAssemblyContactGroundTrackLinkShoe_vtables_dispatch_ = 1
ITrackLMAssemblyContactGroundTrackLinkShoe_vtables_ = [
	(( 'UseLateralFrictionFactor' , 'pVal' , ), 5550, (5550, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseLateralFrictionFactor' , 'pVal' , ), 5550, (5550, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'LateralFrictionFactor' , 'ppVal' , ), 5551, (5551, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveGroundParameter' , 'pVal' , ), 5552, (5552, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveGroundParameter' , 'pVal' , ), 5552, (5552, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'SoftGroundType' , 'val' , ), 5553, (5553, (), [ (3, 1, None, "IID('{E8DFB797-7BAD-4B46-A1C3-FB757B06EF30}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'TerrainStiffnessKc' , 'ppVal' , ), 5554, (5554, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'TerrainStiffnessKphi' , 'ppVal' , ), 5555, (5555, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ExponentialNumber' , 'ppVal' , ), 5556, (5556, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Cohesion' , 'ppVal' , ), 5557, (5557, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ShearingResistanceAngle' , 'ppVal' , ), 5558, (5558, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ShearingDeformationModulus' , 'ppVal' , ), 5559, (5559, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'SinkageRatio' , 'ppVal' , ), 5560, (5560, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveSoftGroundParameter' , 'pVal' , ), 5561, (5561, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveSoftGroundParameter' , 'pVal' , ), 5561, (5561, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 5562, (5562, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 5563, (5563, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseUserSubroutine' , 'pVal' , ), 5564, (5564, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UseUserSubroutine' , 'pVal' , ), 5564, (5564, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'pVal' , ), 5565, (5565, (), [ (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'pVal' , ), 5565, (5565, (), [ (16393, 10, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
]

ITrackLMAssemblyGrouserContact_vtables_dispatch_ = 1
ITrackLMAssemblyGrouserContact_vtables_ = [
	(( 'BasePosition' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{5C8577DA-B2F5-4C78-AF81-251818CE7223}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BaseRadius' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ActionPosition' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{5C8577DA-B2F5-4C78-AF81-251818CE7223}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ActionRadius' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DistanceBetweenLinks' , 'pVal' , ), 5504, (5504, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DistanceBetweenLinks' , 'pVal' , ), 5504, (5504, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ITrackLMAssemblyGrouserContactCollection_vtables_dispatch_ = 1
ITrackLMAssemblyGrouserContactCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{41C77E5C-5A0D-4060-9668-47AAEE4E7575}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITrackLMAssemblyGrouserToSphereContact_vtables_dispatch_ = 1
ITrackLMAssemblyGrouserToSphereContact_vtables_ = [
	(( 'MaximumPenetration' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ContactProperty' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{674DD026-A8F6-4A8B-91ED-0CF92C531AE3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AddGrouserToSphereContact' , 'pGeometrySphere' , ), 5502, (5502, (), [ (9, 1, None, "IID('{2122DEE7-EE07-4A20-9B49-5A9AF4599906}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GeometrySphereCollection' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{0B006D28-70E2-4FBA-8A03-EC9EFC17C4E1}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ITrackLMBody_vtables_dispatch_ = 1
ITrackLMBody_vtables_ = [
	(( 'GeneralBody' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ITrackLMBodyCollection_vtables_dispatch_ = 1
ITrackLMBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITrackLMBodyFlangeCenter_vtables_dispatch_ = 1
ITrackLMBodyFlangeCenter_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 5550, (5550, (), [ (16393, 10, None, "IID('{492847E5-C7BF-4736-9BF3-70ED0D5DB576}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 5551, (5551, (), [ (16393, 10, None, "IID('{DF8894F1-EAE8-48C7-A734-F5EB5F50F9FE}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 5552, (5552, (), [ (16393, 10, None, "IID('{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

ITrackLMBodyFlangeDouble_vtables_dispatch_ = 1
ITrackLMBodyFlangeDouble_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 5550, (5550, (), [ (16393, 10, None, "IID('{492847E5-C7BF-4736-9BF3-70ED0D5DB576}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 5551, (5551, (), [ (16393, 10, None, "IID('{8F09092F-1146-4BC0-A8BC-7A85F51F0054}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 5552, (5552, (), [ (16393, 10, None, "IID('{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

ITrackLMBodyFlangeFlat_vtables_dispatch_ = 1
ITrackLMBodyFlangeFlat_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 5550, (5550, (), [ (16393, 10, None, "IID('{492847E5-C7BF-4736-9BF3-70ED0D5DB576}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 5551, (5551, (), [ (16393, 10, None, "IID('{3B1930FF-530C-4745-B19C-D335810BBDBD}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 5552, (5552, (), [ (16393, 10, None, "IID('{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

ITrackLMBodyFlangeSingle_vtables_dispatch_ = 1
ITrackLMBodyFlangeSingle_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 5550, (5550, (), [ (16393, 10, None, "IID('{492847E5-C7BF-4736-9BF3-70ED0D5DB576}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 5551, (5551, (), [ (16393, 10, None, "IID('{1552BF6E-3FFB-4111-A93D-A52A379E09CF}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 5552, (5552, (), [ (16393, 10, None, "IID('{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

ITrackLMBodyLink_vtables_dispatch_ = 1
ITrackLMBodyLink_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 5551, (5551, (), [ (16393, 10, None, "IID('{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkShape' , 'pVal' , ), 5552, (5552, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkShape' , 'pVal' , ), 5552, (5552, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'LinkShapeProfile' , 'ppLinkShapeProfile' , ), 5553, (5553, (), [ (16393, 10, None, "IID('{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'LinkGrouserProfile' , 'ppLinkGrouserProfile' , ), 5554, (5554, (), [ (16393, 10, None, "IID('{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 5555, (5555, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseBodyGraphic' , 'pVal' , ), 5556, (5556, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseBodyGraphic' , 'pVal' , ), 5556, (5556, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 5557, (5557, (), [ (16393, 10, None, "IID('{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CreateMarker' , 'strName' , 'pRefFrame' , 'ppVal' , ), 5558, (5558, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

ITrackLMBodyLinkCollection_vtables_dispatch_ = 1
ITrackLMBodyLinkCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{D4D76CF3-BAAD-44E9-8D1E-18CB7B5F910D}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITrackLMBodyRollerGuard_vtables_dispatch_ = 1
ITrackLMBodyRollerGuard_vtables_ = [
	(( 'ContactProperty' , 'ppContactProperty' , ), 5550, (5550, (), [ (16393, 10, None, "IID('{492847E5-C7BF-4736-9BF3-70ED0D5DB576}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppGeometry' , ), 5551, (5551, (), [ (16393, 10, None, "IID('{ABD47D59-1C65-4ACE-9DDA-0485A5EE880E}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 5552, (5552, (), [ (16393, 10, None, "IID('{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

ITrackLMBodySprocket_vtables_dispatch_ = 1
ITrackLMBodySprocket_vtables_ = [
	(( 'ContactProperty' , 'ppContactProperty' , ), 5550, (5550, (), [ (16393, 10, None, "IID('{492847E5-C7BF-4736-9BF3-70ED0D5DB576}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppGeometry' , ), 5551, (5551, (), [ (16393, 10, None, "IID('{FB048C8A-5E0F-414C-BB9A-16E7D2410E40}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ToothProfile' , 'ppToothProfile' , ), 5552, (5552, (), [ (16393, 10, None, "IID('{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 5553, (5553, (), [ (16393, 10, None, "IID('{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UpdateProperties' , ), 5555, (5555, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactOutputFile' , 'pVal' , ), 5556, (5556, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactOutputFile' , 'pVal' , ), 5556, (5556, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ITrackLMContactFriction_vtables_dispatch_ = 1
ITrackLMContactFriction_vtables_ = [
	(( 'StaticThresholdVelocity' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DynamicThresholdVelocity' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StaticFrictionCoefficient' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ITrackLMContactProperty_vtables_dispatch_ = 1
ITrackLMContactProperty_vtables_ = [
	(( 'StiffnessCoefficient' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 5501, (5501, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 5501, (5501, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 5502, (5502, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 5504, (5504, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 5504, (5504, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 5505, (5505, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 5506, (5506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 5507, (5507, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 5507, (5507, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 5508, (5508, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 5508, (5508, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 5509, (5509, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 5509, (5509, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 5510, (5510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 5511, (5511, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 5511, (5511, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 5512, (5512, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 5513, (5513, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 5513, (5513, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 5514, (5514, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseMoreFrictionData' , 'pVal' , ), 5515, (5515, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseMoreFrictionData' , 'pVal' , ), 5515, (5515, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Friction' , 'ppVal' , ), 5516, (5516, (), [ (16393, 10, None, "IID('{CB8726EC-DB26-4DBC-8C1F-E011ED239188}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 5517, (5517, (), [ (3, 1, None, "IID('{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}')") , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 5517, (5517, (), [ (16387, 10, None, "IID('{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

ITrackLMContactSearch_vtables_dispatch_ = 1
ITrackLMContactSearch_vtables_ = [
	(( 'Type' , 'pVal' , ), 5500, (5500, (), [ (3, 1, None, "IID('{AB0354E4-81A0-4EF7-9579-3DBB2272CEE0}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 5500, (5500, (), [ (16387, 10, None, "IID('{AB0354E4-81A0-4EF7-9579-3DBB2272CEE0}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseUserBoundaryForPartialSearch' , 'pVal' , ), 5501, (5501, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseUserBoundaryForPartialSearch' , 'pVal' , ), 5501, (5501, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UserBoundaryForPartialSearch' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ITrackLMGeometryFlangeCenter_vtables_dispatch_ = 1
ITrackLMGeometryFlangeCenter_vtables_ = [
	(( 'InnerFlangeWidth' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TotalWidth' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'InnerFlangeRadius' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'WheelRadius' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ITrackLMGeometryFlangeDouble_vtables_dispatch_ = 1
ITrackLMGeometryFlangeDouble_vtables_ = [
	(( 'HubWidth' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'HubAndInnerFlangeWidth' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'HubInnerFlangeAndWheelWidth' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TotalWidth' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'HubRadius' , 'ppVal' , ), 5504, (5504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'InnerFlangeRadius' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'WheelRadius' , 'ppVal' , ), 5506, (5506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'OuterFlangeRadius' , 'ppVal' , ), 5507, (5507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ITrackLMGeometryFlangeFlat_vtables_dispatch_ = 1
ITrackLMGeometryFlangeFlat_vtables_ = [
	(( 'RollerWidth' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RollerRadius' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ITrackLMGeometryFlangeSingle_vtables_dispatch_ = 1
ITrackLMGeometryFlangeSingle_vtables_ = [
	(( 'HubWidth' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'WheelAndHubWidth' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TotalWidth' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'HubRadius' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'WheelRadius' , 'ppVal' , ), 5504, (5504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FlangeRadius' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ITrackLMGeometryLink_vtables_dispatch_ = 1
ITrackLMGeometryLink_vtables_ = [
	(( 'PinRadius' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'InnerWidth' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OuterWidth' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LeftLength' , 'ppVal' , ), 5504, (5504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RightLength' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'ppVal' , ), 5506, (5506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LeftPinPosition' , 'pPoint' , ), 5507, (5507, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'LeftPinPosition' , 'pPoint' , ), 5507, (5507, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RightPinPosition' , 'pPoint' , ), 5508, (5508, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'RightPinPosition' , 'pPoint' , ), 5508, (5508, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GrouserWidth' , 'ppVal' , ), 5509, (5509, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ContactWithSprocketType' , 'pVal' , ), 5510, (5510, (), [ (3, 1, None, "IID('{9C0717B5-A01B-40C7-8311-05C9AB30925F}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ContactWithSprocketType' , 'pVal' , ), 5510, (5510, (), [ (16387, 10, None, "IID('{9C0717B5-A01B-40C7-8311-05C9AB30925F}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 5511, (5511, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 5511, (5511, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 5512, (5512, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 5512, (5512, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 5513, (5513, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 5513, (5513, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 5514, (5514, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 5514, (5514, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

ITrackLMGeometryRollerGuard_vtables_dispatch_ = 1
ITrackLMGeometryRollerGuard_vtables_ = [
	(( 'Length' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'InnerWidth' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'InactiveType' , 'pVal' , ), 5504, (5504, (), [ (3, 1, None, "IID('{674BB7BB-6BE5-41B4-93AA-649213BBDA72}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'InactiveType' , 'pVal' , ), 5504, (5504, (), [ (16387, 10, None, "IID('{674BB7BB-6BE5-41B4-93AA-649213BBDA72}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ITrackLMGeometrySprocket_vtables_dispatch_ = 1
ITrackLMGeometrySprocket_vtables_ = [
	(( 'SprocketWheelRadius' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'WidthOfTeeth' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'WidthBetweenWheels' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfTeeth' , 'pVal' , ), 5503, (5503, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfTeeth' , 'pVal' , ), 5503, (5503, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DedendumCircleRadius' , 'ppVal' , ), 5504, (5504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'BaseCircleRadius' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PitchCircleRadius' , 'ppVal' , ), 5506, (5506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AddendumCircleRadius' , 'ppVal' , ), 5507, (5507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TrackLinkPinCircleRadius' , 'pVal' , ), 5508, (5508, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TrackLinkPinCircleRadius' , 'pVal' , ), 5508, (5508, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TrackLinkLoopRadius' , 'pVal' , ), 5509, (5509, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TrackLinkLoopRadius' , 'pVal' , ), 5509, (5509, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkAssemblyAssembledRadius' , 'pVal' , ), 5510, (5510, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkAssemblyAssembledRadius' , 'pVal' , ), 5510, (5510, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyAssembledRadius' , 'pVal' , ), 5511, (5511, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyAssembledRadius' , 'pVal' , ), 5511, (5511, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyRadialDistance' , 'pVal' , ), 5512, (5512, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyRadialDistance' , 'pVal' , ), 5512, (5512, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ITrackLMGrouserContactProperty_vtables_dispatch_ = 1
ITrackLMGrouserContactProperty_vtables_ = [
	(( 'StiffnessCoefficient' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 5501, (5501, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 5501, (5501, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 5502, (5502, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 5502, (5502, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 5504, (5504, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 5504, (5504, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 5505, (5505, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 5506, (5506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 5507, (5507, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 5507, (5507, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 5508, (5508, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 5508, (5508, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 5509, (5509, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 5509, (5509, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 5510, (5510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 5511, (5511, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 5511, (5511, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 5512, (5512, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

ITrackLMGrouserToSphereContactProperty_vtables_dispatch_ = 1
ITrackLMGrouserToSphereContactProperty_vtables_ = [
	(( 'StiffnessCoefficient' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 5502, (5502, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 5502, (5502, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 5503, (5503, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 5504, (5504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 5505, (5505, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 5505, (5505, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 5506, (5506, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 5506, (5506, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 5507, (5507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 5508, (5508, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 5508, (5508, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 5509, (5509, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 5509, (5509, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 5510, (5510, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 5510, (5510, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 5511, (5511, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 5512, (5512, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 5512, (5512, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 5513, (5513, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 5514, (5514, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 5514, (5514, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 5515, (5515, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 5516, (5516, (), [ (3, 1, None, "IID('{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 5516, (5516, (), [ (16387, 10, None, "IID('{8CE78C6F-2320-4BDF-A3BC-EC26185FF79B}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

ITrackLMLinkClone_vtables_dispatch_ = 1
ITrackLMLinkClone_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkShape' , 'pVal' , ), 5502, (5502, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkShape' , 'pVal' , ), 5502, (5502, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'LinkShapeProfile' , 'ppLinkShapeProfile' , ), 5503, (5503, (), [ (16393, 10, None, "IID('{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'LinkGrouserProfile' , 'ppLinkGrouserProfile' , ), 5504, (5504, (), [ (16393, 10, None, "IID('{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{4C8B7C23-7D92-4D39-B530-5D93DC97F771}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 5506, (5506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'ppVal' , ), 5507, (5507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'ppVal' , ), 5508, (5508, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'ppVal' , ), 5509, (5509, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Ixy' , 'ppVal' , ), 5510, (5510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Iyz' , 'ppVal' , ), 5511, (5511, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Izx' , 'ppVal' , ), 5512, (5512, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'MaterialInput' , 'pVal' , ), 5513, (5513, (), [ (3, 1, None, "IID('{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'MaterialInput' , 'pVal' , ), 5513, (5513, (), [ (16387, 10, None, "IID('{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'pVal' , ), 5514, (5514, (), [ (3, 1, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'pVal' , ), 5514, (5514, (), [ (16387, 10, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 5515, (5515, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 5515, (5515, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'MaterialUser' , 'pVal' , ), 5516, (5516, (), [ (9, 1, None, "IID('{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}')") , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'MaterialUser' , 'pVal' , ), 5516, (5516, (), [ (16393, 10, None, "IID('{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 5517, (5517, (), [ ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CenterMarker' , 'pVal' , ), 5518, (5518, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'InitialBodyGraphicFlag' , ), 5519, (5519, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'FileImport' , 'strFile' , ), 5520, (5520, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'FileExport' , 'strFile' , 'OverWrite' , ), 5521, (5521, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 5522, (5522, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 5522, (5522, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

ITrackLMLinkCloneCollection_vtables_dispatch_ = 1
ITrackLMLinkCloneCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{AD229002-EF52-48FC-9389-8A6A49EDAA72}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITrackLMProfileLinkGrouser_vtables_dispatch_ = 1
ITrackLMProfileLinkGrouser_vtables_ = [
	(( 'Point2DCollection' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{CDBA1369-C276-42F4-8C85-562A82C32E54}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strFileName' , ), 5502, (5502, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strFileName' , ), 5503, (5503, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Update' , ), 5504, (5504, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ShoePoint3DCollection' , 'ppVal' , ), 5505, (5505, (), [ (16393, 10, None, "IID('{7AAA986F-35DD-4DCF-843A-CEBA8E09D33A}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ShoePointImport' , 'strFileName' , ), 5506, (5506, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShoePointExport' , 'strFileName' , ), 5507, (5507, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GrouserToSphereContactStartNode' , 'pVal' , ), 5510, (5510, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GrouserToSphereContactStartNode' , 'pVal' , ), 5510, (5510, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GrouserToSphereContactEndNode' , 'pVal' , ), 5511, (5511, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'GrouserToSphereContactEndNode' , 'pVal' , ), 5511, (5511, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'GrouserMeshStartNode' , 'pVal' , ), 5512, (5512, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GrouserMeshStartNode' , 'pVal' , ), 5512, (5512, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'GrouserMeshEndNode' , 'pVal' , ), 5513, (5513, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GrouserMeshEndNode' , 'pVal' , ), 5513, (5513, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'GrouserMeshLengthSegment' , 'pVal' , ), 5514, (5514, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GrouserMeshLengthSegment' , 'pVal' , ), 5514, (5514, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'GrouserMeshDepthSegment' , 'pVal' , ), 5515, (5515, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GrouserMeshDepthSegment' , 'pVal' , ), 5515, (5515, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ReverseProfilePoints' , ), 5516, (5516, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

ITrackLMProfileLinkShape_vtables_dispatch_ = 1
ITrackLMProfileLinkShape_vtables_ = [
	(( 'PointCollection' , 'ppVal' , ), 5501, (5501, (), [ (16393, 10, None, "IID('{2C0D70A3-D197-4781-940A-1672F3B420B9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strFileName' , ), 5502, (5502, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strFileName' , ), 5503, (5503, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ITrackLMSubSystem_vtables_dispatch_ = 1
ITrackLMSubSystem_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodySprocket' , 'strName' , 'pPoint' , 'ppResult' , ), 5501, (5501, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{C809FD1D-0B5D-4F2C-843C-BFBFCD795B11}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyFlangeSingle' , 'strName' , 'pPoint' , 'ppResult' , ), 5502, (5502, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{0FBAD430-C81A-4870-9D3E-9F6497D2C565}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyFlangeDouble' , 'strName' , 'pPoint' , 'ppResult' , ), 5503, (5503, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{7C581B15-F7A8-4FD4-B732-07DD8661FE01}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyFlangeCenter' , 'strName' , 'pPoint' , 'ppResult' , ), 5504, (5504, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{B142F053-F79F-4E72-9252-26D82A373001}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyFlangeFlat' , 'strName' , 'pPoint' , 'ppResult' , ), 5505, (5505, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{1413E74E-9CDE-4E83-9BC2-14F6C0783FC0}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyRollerGuard' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'ppResult' , 
			 ), 5506, (5506, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{E873D6AC-B791-48F4-B0AB-12560562B540}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateLinkClone' , 'strName' , 'pPoint' , 'ppResult' , ), 5507, (5507, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{AD229002-EF52-48FC-9389-8A6A49EDAA72}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CreateTrackAssembly' , 'strName' , 'pLinkClone' , 'pBodyList' , 'pInOutList' , 
			 'uiNumberOfLink' , 'ppResult' , ), 5508, (5508, (), [ (8, 1, None, None) , (9, 1, None, "IID('{AD229002-EF52-48FC-9389-8A6A49EDAA72}')") , 
			 (8204, 1, None, None) , (8204, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{F3294DCE-CF25-4511-986C-DC2D245853B1}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'LinkCloneCollection' , 'ppVal' , ), 5509, (5509, (), [ (16393, 10, None, "IID('{6939141C-3175-47EB-A3B5-5267300EEA6F}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'AssemblyCollection' , 'ppVal' , ), 5510, (5510, (), [ (16393, 10, None, "IID('{22BE609F-1707-46CF-AA73-5BF5C0F577C4}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'TrackLMBodyCollection' , 'ppVal' , ), 5511, (5511, (), [ (16393, 10, None, "IID('{2E24F362-D8AA-41AD-8BD4-CD92CF24C188}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ConvertLinksToBodies' , 'assembly' , 'numOfBushing' , 'links' , 'assemblies' , 
			 'bodies' , ), 5512, (5512, (), [ (9, 1, None, "IID('{F3294DCE-CF25-4511-986C-DC2D245853B1}')") , (19, 1, None, None) , (8204, 1, None, None) , 
			 (24588, 2, None, None) , (24588, 2, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorDisplacement' , 'strName' , 'pEntity' , 'pSensorMarker' , 'dRange' , 
			 'ppVal' , ), 5513, (5513, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{08F5AF0B-ADB1-4AB4-8FAB-54ADCB9B5F36}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorFixed' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 5515, (5515, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{39059D2F-DBEC-49DD-BFF2-AC0185541C99}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorRevolute' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 5516, (5516, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{D24BBA28-623F-4F1C-97D5-021413EB6736}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorSpring' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pBaseRefFrame' , 
			 'pActionRefFrame' , 'ppResult' , ), 5517, (5517, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{93A5A572-A6DD-4F12-A3E5-64F95B78718F}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorBushing' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 5518, (5518, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{F5A169B5-B529-4935-8B06-ACDD2A0BA456}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactTrackToSurface' , 'strName' , 'pBaseBody' , 'pActionBody' , 'ppResult' , 
			 ), 5519, (5519, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (16393, 10, None, "IID('{1EAD15B7-3DFF-40FD-BD77-12CBB9F2CA6C}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CreateTrackAssemblyWithAutomaticSprocketAlignment' , 'strName' , 'pLinkClone' , 'pBodyList' , 'pInOutList' , 
			 'uiNumberOfLink' , 'ppResult' , ), 5520, (5520, (), [ (8, 1, None, None) , (9, 1, None, "IID('{AD229002-EF52-48FC-9389-8A6A49EDAA72}')") , 
			 (8204, 1, None, None) , (8204, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{F3294DCE-CF25-4511-986C-DC2D245853B1}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ConvertAssemblyLinksToBodies' , 'assembly' , 'numOfBushing' , 'bodies' , ), 5521, (5521, (), [ 
			 (9, 1, None, "IID('{F3294DCE-CF25-4511-986C-DC2D245853B1}')") , (19, 1, None, None) , (24588, 2, None, None) , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
]

ITrackLMToothProfileSprocket_vtables_dispatch_ = 1
ITrackLMToothProfileSprocket_vtables_ = [
	(( 'PointCollection' , 'ppVal' , ), 5500, (5500, (), [ (16393, 10, None, "IID('{2C0D70A3-D197-4781-940A-1672F3B420B9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 5501, (5501, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 5502, (5502, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{CB8726EC-DB26-4DBC-8C1F-E011ED239188}' : ITrackLMContactFriction,
	'{492847E5-C7BF-4736-9BF3-70ED0D5DB576}' : ITrackLMContactProperty,
	'{860E76B0-9B85-4973-AE10-CA2BD4FEA254}' : ITrackLMGrouserContactProperty,
	'{1552BF6E-3FFB-4111-A93D-A52A379E09CF}' : ITrackLMGeometryFlangeSingle,
	'{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}' : ITrackLMContactSearch,
	'{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}' : ITrackLMBody,
	'{2E24F362-D8AA-41AD-8BD4-CD92CF24C188}' : ITrackLMBodyCollection,
	'{0FBAD430-C81A-4870-9D3E-9F6497D2C565}' : ITrackLMBodyFlangeSingle,
	'{8F09092F-1146-4BC0-A8BC-7A85F51F0054}' : ITrackLMGeometryFlangeDouble,
	'{7C581B15-F7A8-4FD4-B732-07DD8661FE01}' : ITrackLMBodyFlangeDouble,
	'{DF8894F1-EAE8-48C7-A734-F5EB5F50F9FE}' : ITrackLMGeometryFlangeCenter,
	'{B142F053-F79F-4E72-9252-26D82A373001}' : ITrackLMBodyFlangeCenter,
	'{3B1930FF-530C-4745-B19C-D335810BBDBD}' : ITrackLMGeometryFlangeFlat,
	'{1413E74E-9CDE-4E83-9BC2-14F6C0783FC0}' : ITrackLMBodyFlangeFlat,
	'{FB048C8A-5E0F-414C-BB9A-16E7D2410E40}' : ITrackLMGeometrySprocket,
	'{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}' : ITrackLMToothProfileSprocket,
	'{C809FD1D-0B5D-4F2C-843C-BFBFCD795B11}' : ITrackLMBodySprocket,
	'{ABD47D59-1C65-4ACE-9DDA-0485A5EE880E}' : ITrackLMGeometryRollerGuard,
	'{E873D6AC-B791-48F4-B0AB-12560562B540}' : ITrackLMBodyRollerGuard,
	'{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}' : ITrackLMGeometryLink,
	'{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}' : ITrackLMProfileLinkShape,
	'{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}' : ITrackLMProfileLinkGrouser,
	'{D4D76CF3-BAAD-44E9-8D1E-18CB7B5F910D}' : ITrackLMBodyLink,
	'{7E3C5275-F00D-4675-BAF6-9AE63689F8D2}' : ITrackLMBodyLinkCollection,
	'{AD229002-EF52-48FC-9389-8A6A49EDAA72}' : ITrackLMLinkClone,
	'{6939141C-3175-47EB-A3B5-5267300EEA6F}' : ITrackLMLinkCloneCollection,
	'{F3294DCE-CF25-4511-986C-DC2D245853B1}' : ITrackLMAssembly,
	'{C37B595D-DE29-465E-88F7-288C5C63D7F7}' : ITrackLMAssemblyContactGroundTrackLinkShoe,
	'{71434E11-33AF-44E5-B36F-D0D92753A768}' : ITrackLMAssemblyGrouserToSphereContact,
	'{674DD026-A8F6-4A8B-91ED-0CF92C531AE3}' : ITrackLMGrouserToSphereContactProperty,
	'{08A3F46B-C852-46F4-BCE6-11A84CFD7C2B}' : ITrackLMAssemblyBushingForceParameter,
	'{41C77E5C-5A0D-4060-9668-47AAEE4E7575}' : ITrackLMAssemblyGrouserContact,
	'{68152AA0-4470-4F17-AEF7-F45AA9ABE529}' : ITrackLMAssemblyGrouserContactCollection,
	'{22BE609F-1707-46CF-AA73-5BF5C0F577C4}' : ITrackLMAssemblyCollection,
	'{94F9A0BC-94F5-4474-B550-1240D060FD26}' : IPassingBodyCollection,
	'{D0902FEE-86C9-4F2C-98CA-8113ED49E973}' : ITrackLMSubSystem,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{CB8726EC-DB26-4DBC-8C1F-E011ED239188}' : 'ITrackLMContactFriction',
	'{492847E5-C7BF-4736-9BF3-70ED0D5DB576}' : 'ITrackLMContactProperty',
	'{860E76B0-9B85-4973-AE10-CA2BD4FEA254}' : 'ITrackLMGrouserContactProperty',
	'{1552BF6E-3FFB-4111-A93D-A52A379E09CF}' : 'ITrackLMGeometryFlangeSingle',
	'{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}' : 'ITrackLMContactSearch',
	'{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}' : 'ITrackLMBody',
	'{2E24F362-D8AA-41AD-8BD4-CD92CF24C188}' : 'ITrackLMBodyCollection',
	'{0FBAD430-C81A-4870-9D3E-9F6497D2C565}' : 'ITrackLMBodyFlangeSingle',
	'{8F09092F-1146-4BC0-A8BC-7A85F51F0054}' : 'ITrackLMGeometryFlangeDouble',
	'{7C581B15-F7A8-4FD4-B732-07DD8661FE01}' : 'ITrackLMBodyFlangeDouble',
	'{DF8894F1-EAE8-48C7-A734-F5EB5F50F9FE}' : 'ITrackLMGeometryFlangeCenter',
	'{B142F053-F79F-4E72-9252-26D82A373001}' : 'ITrackLMBodyFlangeCenter',
	'{3B1930FF-530C-4745-B19C-D335810BBDBD}' : 'ITrackLMGeometryFlangeFlat',
	'{1413E74E-9CDE-4E83-9BC2-14F6C0783FC0}' : 'ITrackLMBodyFlangeFlat',
	'{FB048C8A-5E0F-414C-BB9A-16E7D2410E40}' : 'ITrackLMGeometrySprocket',
	'{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}' : 'ITrackLMToothProfileSprocket',
	'{C809FD1D-0B5D-4F2C-843C-BFBFCD795B11}' : 'ITrackLMBodySprocket',
	'{ABD47D59-1C65-4ACE-9DDA-0485A5EE880E}' : 'ITrackLMGeometryRollerGuard',
	'{E873D6AC-B791-48F4-B0AB-12560562B540}' : 'ITrackLMBodyRollerGuard',
	'{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}' : 'ITrackLMGeometryLink',
	'{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}' : 'ITrackLMProfileLinkShape',
	'{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}' : 'ITrackLMProfileLinkGrouser',
	'{D4D76CF3-BAAD-44E9-8D1E-18CB7B5F910D}' : 'ITrackLMBodyLink',
	'{7E3C5275-F00D-4675-BAF6-9AE63689F8D2}' : 'ITrackLMBodyLinkCollection',
	'{AD229002-EF52-48FC-9389-8A6A49EDAA72}' : 'ITrackLMLinkClone',
	'{6939141C-3175-47EB-A3B5-5267300EEA6F}' : 'ITrackLMLinkCloneCollection',
	'{F3294DCE-CF25-4511-986C-DC2D245853B1}' : 'ITrackLMAssembly',
	'{C37B595D-DE29-465E-88F7-288C5C63D7F7}' : 'ITrackLMAssemblyContactGroundTrackLinkShoe',
	'{71434E11-33AF-44E5-B36F-D0D92753A768}' : 'ITrackLMAssemblyGrouserToSphereContact',
	'{674DD026-A8F6-4A8B-91ED-0CF92C531AE3}' : 'ITrackLMGrouserToSphereContactProperty',
	'{08A3F46B-C852-46F4-BCE6-11A84CFD7C2B}' : 'ITrackLMAssemblyBushingForceParameter',
	'{41C77E5C-5A0D-4060-9668-47AAEE4E7575}' : 'ITrackLMAssemblyGrouserContact',
	'{68152AA0-4470-4F17-AEF7-F45AA9ABE529}' : 'ITrackLMAssemblyGrouserContactCollection',
	'{22BE609F-1707-46CF-AA73-5BF5C0F577C4}' : 'ITrackLMAssemblyCollection',
	'{94F9A0BC-94F5-4474-B550-1240D060FD26}' : 'IPassingBodyCollection',
	'{D0902FEE-86C9-4F2C-98CA-8113ED49E973}' : 'ITrackLMSubSystem',
}


NamesToIIDMap = {
	'ITrackLMContactFriction' : '{CB8726EC-DB26-4DBC-8C1F-E011ED239188}',
	'ITrackLMContactProperty' : '{492847E5-C7BF-4736-9BF3-70ED0D5DB576}',
	'ITrackLMGrouserContactProperty' : '{860E76B0-9B85-4973-AE10-CA2BD4FEA254}',
	'ITrackLMGeometryFlangeSingle' : '{1552BF6E-3FFB-4111-A93D-A52A379E09CF}',
	'ITrackLMContactSearch' : '{C56DF74E-2091-43D8-BB23-1AAAD19F7A4E}',
	'ITrackLMBody' : '{5B2C7A2B-BE16-4711-93B2-3B37FEBC1068}',
	'ITrackLMBodyCollection' : '{2E24F362-D8AA-41AD-8BD4-CD92CF24C188}',
	'ITrackLMBodyFlangeSingle' : '{0FBAD430-C81A-4870-9D3E-9F6497D2C565}',
	'ITrackLMGeometryFlangeDouble' : '{8F09092F-1146-4BC0-A8BC-7A85F51F0054}',
	'ITrackLMBodyFlangeDouble' : '{7C581B15-F7A8-4FD4-B732-07DD8661FE01}',
	'ITrackLMGeometryFlangeCenter' : '{DF8894F1-EAE8-48C7-A734-F5EB5F50F9FE}',
	'ITrackLMBodyFlangeCenter' : '{B142F053-F79F-4E72-9252-26D82A373001}',
	'ITrackLMGeometryFlangeFlat' : '{3B1930FF-530C-4745-B19C-D335810BBDBD}',
	'ITrackLMBodyFlangeFlat' : '{1413E74E-9CDE-4E83-9BC2-14F6C0783FC0}',
	'ITrackLMGeometrySprocket' : '{FB048C8A-5E0F-414C-BB9A-16E7D2410E40}',
	'ITrackLMToothProfileSprocket' : '{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}',
	'ITrackLMBodySprocket' : '{C809FD1D-0B5D-4F2C-843C-BFBFCD795B11}',
	'ITrackLMGeometryRollerGuard' : '{ABD47D59-1C65-4ACE-9DDA-0485A5EE880E}',
	'ITrackLMBodyRollerGuard' : '{E873D6AC-B791-48F4-B0AB-12560562B540}',
	'ITrackLMGeometryLink' : '{1FE9D8E6-EFF5-4C75-97BF-92D1137180B4}',
	'ITrackLMProfileLinkShape' : '{AE6C8AA2-B926-44B4-9E9D-7103052A08BA}',
	'ITrackLMProfileLinkGrouser' : '{1DED937C-5D52-469F-81EF-1BE0FB2BE0D1}',
	'ITrackLMBodyLink' : '{D4D76CF3-BAAD-44E9-8D1E-18CB7B5F910D}',
	'ITrackLMBodyLinkCollection' : '{7E3C5275-F00D-4675-BAF6-9AE63689F8D2}',
	'ITrackLMLinkClone' : '{AD229002-EF52-48FC-9389-8A6A49EDAA72}',
	'ITrackLMLinkCloneCollection' : '{6939141C-3175-47EB-A3B5-5267300EEA6F}',
	'ITrackLMAssembly' : '{F3294DCE-CF25-4511-986C-DC2D245853B1}',
	'ITrackLMAssemblyContactGroundTrackLinkShoe' : '{C37B595D-DE29-465E-88F7-288C5C63D7F7}',
	'ITrackLMAssemblyGrouserToSphereContact' : '{71434E11-33AF-44E5-B36F-D0D92753A768}',
	'ITrackLMGrouserToSphereContactProperty' : '{674DD026-A8F6-4A8B-91ED-0CF92C531AE3}',
	'ITrackLMAssemblyBushingForceParameter' : '{08A3F46B-C852-46F4-BCE6-11A84CFD7C2B}',
	'ITrackLMAssemblyGrouserContact' : '{41C77E5C-5A0D-4060-9668-47AAEE4E7575}',
	'ITrackLMAssemblyGrouserContactCollection' : '{68152AA0-4470-4F17-AEF7-F45AA9ABE529}',
	'ITrackLMAssemblyCollection' : '{22BE609F-1707-46CF-AA73-5BF5C0F577C4}',
	'IPassingBodyCollection' : '{94F9A0BC-94F5-4474-B550-1240D060FD26}',
	'ITrackLMSubSystem' : '{D0902FEE-86C9-4F2C-98CA-8113ED49E973}',
}


