# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMTrackHM.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5 RecurDynCOMTrackHM Type Library'
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

CLSID = IID('{78BC7DAF-2BCD-4461-8B60-8F2D7FC6B2B4}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class TrackHMContactParameterSoftGroundType(IntEnum):
	'''
	TrackHMContactParameterSoftGroundType enumeration.
	'''
	TrackHMContactParameterSoftGroundType_Clayey_Soil=4         
	'''Constant value is 4.'''
	TrackHMContactParameterSoftGroundType_Dry_Sand=0         
	'''Constant value is 0.'''
	TrackHMContactParameterSoftGroundType_Grenville_Loam=11        
	'''Constant value is 11.'''
	TrackHMContactParameterSoftGroundType_Heavy_Clay=5         
	'''Constant value is 5.'''
	TrackHMContactParameterSoftGroundType_LETE_Sand=7         
	'''Constant value is 7.'''
	TrackHMContactParameterSoftGroundType_Lean_Clay=6         
	'''Constant value is 6.'''
	TrackHMContactParameterSoftGroundType_North_Gower_Clayey_Loam=10        
	'''Constant value is 10.'''
	TrackHMContactParameterSoftGroundType_Rubicon_Sandy_Loam=9         
	'''Constant value is 9.'''
	TrackHMContactParameterSoftGroundType_Sandy_Loam_Hanamoto=3         
	'''Constant value is 3.'''
	TrackHMContactParameterSoftGroundType_Sandy_Loam_LLL=1         
	'''Constant value is 1.'''
	TrackHMContactParameterSoftGroundType_Sandy_Loam_Michigan=2         
	'''Constant value is 2.'''
	TrackHMContactParameterSoftGroundType_Snow_Sweden=13        
	'''Constant value is 13.'''
	TrackHMContactParameterSoftGroundType_Snow_US=12        
	'''Constant value is 12.'''
	TrackHMContactParameterSoftGroundType_Upland_Sandy_Loam=8         
	'''Constant value is 8.'''
class TrackHMContactSearchType(IntEnum):
	'''
	TrackHMContactSearchType enumeration.
	'''
	TrackHMContactSearchType_FullSearch=0         
	'''Constant value is 0.'''
	TrackHMContactSearchType_PartialSearch=1         
	'''Constant value is 1.'''
class TrackHMFrictionType(IntEnum):
	'''
	TrackHMFrictionType enumeration.
	'''
	TrackHMFrictionType_DynamicFrictionCoefficient=0         
	'''Constant value is 0.'''
	TrackHMFrictionType_FrictionCoefficientSpline=2         
	'''Constant value is 2.'''
	TrackHMFrictionType_FrictionForceSpline=1         
	'''Constant value is 1.'''
class TrackHMInOutType(IntEnum):
	'''
	TrackHMInOutType enumeration.
	'''
	TrackHMInOutType_In           =0         
	'''Constant value is 0.'''
	TrackHMInOutType_None         =2         
	'''Constant value is 2.'''
	TrackHMInOutType_Out          =1         
	'''Constant value is 1.'''

from win32com.client import DispatchBaseClass
class ITrackHMAssembly(DispatchBaseClass):
	'''TrackHM Assembly'''
	CLSID = IID('{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')
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
		return self._oleobj_.InvokeTypes(6013, LCID, 1, (24, 0), (),)


	def AddOutputLink(self, strFileName):
		'''
		Add a link body to output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(6011, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def AddPassingBody(self, pVal):
		'''
		Add a passing body
		
		:param pVal: IBody
		'''
		return self._oleobj_.InvokeTypes(6003, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def AddPassingBody2(self, pVal):
		'''
		Add a passing body with ITrackHMBody
		
		:param pVal: ITrackHMBody
		'''
		return self._oleobj_.InvokeTypes(6025, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody(self, pVal):
		'''
		Delete a passing body
		
		:param pVal: IBody
		'''
		return self._oleobj_.InvokeTypes(6004, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody2(self, pVal):
		'''
		Delete a passing body with ITrackHMBody
		
		:param pVal: ITrackHMBody
		'''
		return self._oleobj_.InvokeTypes(6026, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetOutputLinkList(self):
		'''
		TrackHM assembly output list
		
		:rtype: list[str]
		'''
		return self._ApplyTypes_(6010, 1, (8200, 0), (), 'GetOutputLinkList', None,)


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
		return self._oleobj_.InvokeTypes(6014, LCID, 1, (24, 0), (),)


	def RemoveOutputLink(self, strFileName):
		'''
		Remove a link body from output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(6012, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def UpdateLinkInitialVelocity(self):
		'''
		Update initial velocity of links
		'''
		return self._oleobj_.InvokeTypes(6021, LCID, 1, (24, 0), (),)


	def _get_BushingForceCollection(self):
		return self._ApplyTypes_(*(6020, 2, (9, 0), (), "BushingForceCollection", '{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}'))
	def _get_BushingForceParameter(self):
		return self._ApplyTypes_(*(6009, 2, (9, 0), (), "BushingForceParameter", '{5D558264-0B36-4A12-8D70-8A2BA7315F32}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "ContactParameter", '{6E69D3B7-8017-427A-A4CE-B654E20AC0B6}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LinkInitialVelocityXAxis(self):
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "LinkInitialVelocityXAxis", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LinkNumbers(self):
		return self._ApplyTypes_(*(6006, 2, (19, 0), (), "LinkNumbers", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PassingBodyCollection(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'))
	def _get_SphereContact(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "SphereContact", '{6EBF0639-993D-437D-80AA-8372352B7281}'))
	def _get_TrackHMBodyLinkCollection(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "TrackHMBodyLinkCollection", '{F592F48A-ED83-4179-982F-13D4F1E9AA40}'))
	def _get_UseLinkInitialVelocityReferenceFrame(self):
		return self._ApplyTypes_(*(6023, 2, (11, 0), (), "UseLinkInitialVelocityReferenceFrame", None))
	def _get_UseLinkInitialVelocityXAxis(self):
		return self._ApplyTypes_(*(6022, 2, (11, 0), (), "UseLinkInitialVelocityXAxis", None))
	def _get_UsePressureSinkage(self):
		return self._ApplyTypes_(*(6000, 2, (11, 0), (), "UsePressureSinkage", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LinkInitialVelocityReferenceFrame(self, value):
		if "LinkInitialVelocityReferenceFrame" in self.__dict__: self.__dict__["LinkInitialVelocityReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((6024, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkInitialVelocityReferenceFrame(self, value):
		if "UseLinkInitialVelocityReferenceFrame" in self.__dict__: self.__dict__["UseLinkInitialVelocityReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((6023, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkInitialVelocityXAxis(self, value):
		if "UseLinkInitialVelocityXAxis" in self.__dict__: self.__dict__["UseLinkInitialVelocityXAxis"] = value; return
		self._oleobj_.Invoke(*((6022, LCID, 4, 0) + (value,) + ()))
	def _set_UsePressureSinkage(self, value):
		if "UsePressureSinkage" in self.__dict__: self.__dict__["UsePressureSinkage"] = value; return
		self._oleobj_.Invoke(*((6000, LCID, 4, 0) + (value,) + ()))
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

	:type: recurdyn.TrackHM.ITrackHMAssemblyBushingForceParameter
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact ground track link shoe

	:type: recurdyn.TrackHM.ITrackHMAssemblyContactGroundTrackLinkShoePad
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
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
	SphereContact = property(_get_SphereContact, None)
	'''
	Sphere contact Property

	:type: recurdyn.TrackHM.ITrackHMAssemblySphereContact
	'''
	TrackHMBodyLinkCollection = property(_get_TrackHMBodyLinkCollection, None)
	'''
	TrackHM body link collection

	:type: recurdyn.TrackHM.ITrackHMBodyLinkCollection
	'''
	UseLinkInitialVelocityReferenceFrame = property(_get_UseLinkInitialVelocityReferenceFrame, _set_UseLinkInitialVelocityReferenceFrame)
	'''
	Use link initialvelocity Reference Frame

	:type: bool
	'''
	UseLinkInitialVelocityXAxis = property(_get_UseLinkInitialVelocityXAxis, _set_UseLinkInitialVelocityXAxis)
	'''
	Use link initialvelocity x-axis

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
	LinkInitialVelocityReferenceFrame = property(None, _set_LinkInitialVelocityReferenceFrame)
	'''
	link initialvelocity Reference Frame

	:type: recurdyn.ProcessNet.IMarker
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_LinkInitialVelocityReferenceFrame": _set_LinkInitialVelocityReferenceFrame,
		"_set_Name": _set_Name,
		"_set_UseLinkInitialVelocityReferenceFrame": _set_UseLinkInitialVelocityReferenceFrame,
		"_set_UseLinkInitialVelocityXAxis": _set_UseLinkInitialVelocityXAxis,
		"_set_UsePressureSinkage": _set_UsePressureSinkage,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BushingForceCollection": (6020, 2, (9, 0), (), "BushingForceCollection", '{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}'),
		"BushingForceParameter": (6009, 2, (9, 0), (), "BushingForceParameter", '{5D558264-0B36-4A12-8D70-8A2BA7315F32}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (6001, 2, (9, 0), (), "ContactParameter", '{6E69D3B7-8017-427A-A4CE-B654E20AC0B6}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LinkInitialVelocityXAxis": (6007, 2, (9, 0), (), "LinkInitialVelocityXAxis", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LinkNumbers": (6006, 2, (19, 0), (), "LinkNumbers", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PassingBodyCollection": (6002, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'),
		"SphereContact": (6005, 2, (9, 0), (), "SphereContact", '{6EBF0639-993D-437D-80AA-8372352B7281}'),
		"TrackHMBodyLinkCollection": (6008, 2, (9, 0), (), "TrackHMBodyLinkCollection", '{F592F48A-ED83-4179-982F-13D4F1E9AA40}'),
		"UseLinkInitialVelocityReferenceFrame": (6023, 2, (11, 0), (), "UseLinkInitialVelocityReferenceFrame", None),
		"UseLinkInitialVelocityXAxis": (6022, 2, (11, 0), (), "UseLinkInitialVelocityXAxis", None),
		"UsePressureSinkage": (6000, 2, (11, 0), (), "UsePressureSinkage", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"LinkInitialVelocityReferenceFrame": ((6024, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseLinkInitialVelocityReferenceFrame": ((6023, LCID, 4, 0),()),
		"UseLinkInitialVelocityXAxis": ((6022, LCID, 4, 0),()),
		"UsePressureSinkage": ((6000, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMAssemblyBushingForceParameter(DispatchBaseClass):
	'''TrackHM Assembly Bushing Force Parameter'''
	CLSID = IID('{5D558264-0B36-4A12-8D70-8A2BA7315F32}')
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
		return self._oleobj_.InvokeTypes(6048, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import bushing force parameter
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(6049, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_RotationDampingCoefficientX(self):
		return self._ApplyTypes_(*(6020, 2, (9, 0), (), "RotationDampingCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingCoefficientY(self):
		return self._ApplyTypes_(*(6021, 2, (9, 0), (), "RotationDampingCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingCoefficientZ(self):
		return self._ApplyTypes_(*(6022, 2, (9, 0), (), "RotationDampingCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponentX(self):
		return self._ApplyTypes_(*(6045, 2, (9, 0), (), "RotationDampingExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponentY(self):
		return self._ApplyTypes_(*(6046, 2, (9, 0), (), "RotationDampingExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponentZ(self):
		return self._ApplyTypes_(*(6047, 2, (9, 0), (), "RotationDampingExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingSplineX(self):
		return self._ApplyTypes_(*(6024, 2, (9, 0), (), "RotationDampingSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationDampingSplineY(self):
		return self._ApplyTypes_(*(6025, 2, (9, 0), (), "RotationDampingSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationDampingSplineZ(self):
		return self._ApplyTypes_(*(6026, 2, (9, 0), (), "RotationDampingSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationPreloadX(self):
		return self._ApplyTypes_(*(6027, 2, (9, 0), (), "RotationPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationPreloadY(self):
		return self._ApplyTypes_(*(6028, 2, (9, 0), (), "RotationPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationPreloadZ(self):
		return self._ApplyTypes_(*(6029, 2, (9, 0), (), "RotationPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationPresetAngle(self):
		return self._ApplyTypes_(*(6030, 2, (9, 0), (), "RotationPresetAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessCoefficientX(self):
		return self._ApplyTypes_(*(6013, 2, (9, 0), (), "RotationStiffnessCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessCoefficientY(self):
		return self._ApplyTypes_(*(6014, 2, (9, 0), (), "RotationStiffnessCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessCoefficientZ(self):
		return self._ApplyTypes_(*(6015, 2, (9, 0), (), "RotationStiffnessCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponentX(self):
		return self._ApplyTypes_(*(6041, 2, (9, 0), (), "RotationStiffnessExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponentY(self):
		return self._ApplyTypes_(*(6042, 2, (9, 0), (), "RotationStiffnessExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponentZ(self):
		return self._ApplyTypes_(*(6043, 2, (9, 0), (), "RotationStiffnessExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessSplineX(self):
		return self._ApplyTypes_(*(6017, 2, (9, 0), (), "RotationStiffnessSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationStiffnessSplineY(self):
		return self._ApplyTypes_(*(6018, 2, (9, 0), (), "RotationStiffnessSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationStiffnessSplineZ(self):
		return self._ApplyTypes_(*(6019, 2, (9, 0), (), "RotationStiffnessSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationStopAngle(self):
		return self._ApplyTypes_(*(6032, 2, (9, 0), (), "RotationStopAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStopStiffnessFactor(self):
		return self._ApplyTypes_(*(6033, 2, (9, 0), (), "RotationStopStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationClearance(self):
		return self._ApplyTypes_(*(6012, 2, (9, 0), (), "TranslationClearance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingCoefficientAxial(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "TranslationDampingCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingCoefficientRadial(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "TranslationDampingCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingExponentAxial(self):
		return self._ApplyTypes_(*(6039, 2, (9, 0), (), "TranslationDampingExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingExponentRadial(self):
		return self._ApplyTypes_(*(6038, 2, (9, 0), (), "TranslationDampingExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingSplineAxial(self):
		return self._ApplyTypes_(*(6009, 2, (9, 0), (), "TranslationDampingSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationDampingSplineRadial(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "TranslationDampingSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationPreloadAxial(self):
		return self._ApplyTypes_(*(6011, 2, (9, 0), (), "TranslationPreloadAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationPreloadRadial(self):
		return self._ApplyTypes_(*(6010, 2, (9, 0), (), "TranslationPreloadRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessCoefficientAxial(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "TranslationStiffnessCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessCoefficientRadial(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "TranslationStiffnessCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessExponentAxial(self):
		return self._ApplyTypes_(*(6036, 2, (9, 0), (), "TranslationStiffnessExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessExponentRadial(self):
		return self._ApplyTypes_(*(6035, 2, (9, 0), (), "TranslationStiffnessExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessSplineAxial(self):
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "TranslationStiffnessSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationStiffnessSplineRadial(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "TranslationStiffnessSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseRotationDampingExponent(self):
		return self._ApplyTypes_(*(6044, 2, (11, 0), (), "UseRotationDampingExponent", None))
	def _get_UseRotationDampingSpline(self):
		return self._ApplyTypes_(*(6023, 2, (11, 0), (), "UseRotationDampingSpline", None))
	def _get_UseRotationStiffnessExponent(self):
		return self._ApplyTypes_(*(6040, 2, (11, 0), (), "UseRotationStiffnessExponent", None))
	def _get_UseRotationStiffnessSpline(self):
		return self._ApplyTypes_(*(6016, 2, (11, 0), (), "UseRotationStiffnessSpline", None))
	def _get_UseRotationStopAngle(self):
		return self._ApplyTypes_(*(6031, 2, (11, 0), (), "UseRotationStopAngle", None))
	def _get_UseTranslationDampingExponent(self):
		return self._ApplyTypes_(*(6037, 2, (11, 0), (), "UseTranslationDampingExponent", None))
	def _get_UseTranslationDampingSpline(self):
		return self._ApplyTypes_(*(6007, 2, (11, 0), (), "UseTranslationDampingSpline", None))
	def _get_UseTranslationStiffnessExponent(self):
		return self._ApplyTypes_(*(6034, 2, (11, 0), (), "UseTranslationStiffnessExponent", None))
	def _get_UseTranslationStiffnessSpline(self):
		return self._ApplyTypes_(*(6002, 2, (11, 0), (), "UseTranslationStiffnessSpline", None))

	def _set_RotationDampingSplineX(self, value):
		if "RotationDampingSplineX" in self.__dict__: self.__dict__["RotationDampingSplineX"] = value; return
		self._oleobj_.Invoke(*((6024, LCID, 4, 0) + (value,) + ()))
	def _set_RotationDampingSplineY(self, value):
		if "RotationDampingSplineY" in self.__dict__: self.__dict__["RotationDampingSplineY"] = value; return
		self._oleobj_.Invoke(*((6025, LCID, 4, 0) + (value,) + ()))
	def _set_RotationDampingSplineZ(self, value):
		if "RotationDampingSplineZ" in self.__dict__: self.__dict__["RotationDampingSplineZ"] = value; return
		self._oleobj_.Invoke(*((6026, LCID, 4, 0) + (value,) + ()))
	def _set_RotationStiffnessSplineX(self, value):
		if "RotationStiffnessSplineX" in self.__dict__: self.__dict__["RotationStiffnessSplineX"] = value; return
		self._oleobj_.Invoke(*((6017, LCID, 4, 0) + (value,) + ()))
	def _set_RotationStiffnessSplineY(self, value):
		if "RotationStiffnessSplineY" in self.__dict__: self.__dict__["RotationStiffnessSplineY"] = value; return
		self._oleobj_.Invoke(*((6018, LCID, 4, 0) + (value,) + ()))
	def _set_RotationStiffnessSplineZ(self, value):
		if "RotationStiffnessSplineZ" in self.__dict__: self.__dict__["RotationStiffnessSplineZ"] = value; return
		self._oleobj_.Invoke(*((6019, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationDampingSplineAxial(self, value):
		if "TranslationDampingSplineAxial" in self.__dict__: self.__dict__["TranslationDampingSplineAxial"] = value; return
		self._oleobj_.Invoke(*((6009, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationDampingSplineRadial(self, value):
		if "TranslationDampingSplineRadial" in self.__dict__: self.__dict__["TranslationDampingSplineRadial"] = value; return
		self._oleobj_.Invoke(*((6008, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationStiffnessSplineAxial(self, value):
		if "TranslationStiffnessSplineAxial" in self.__dict__: self.__dict__["TranslationStiffnessSplineAxial"] = value; return
		self._oleobj_.Invoke(*((6004, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationStiffnessSplineRadial(self, value):
		if "TranslationStiffnessSplineRadial" in self.__dict__: self.__dict__["TranslationStiffnessSplineRadial"] = value; return
		self._oleobj_.Invoke(*((6003, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationDampingExponent(self, value):
		if "UseRotationDampingExponent" in self.__dict__: self.__dict__["UseRotationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((6044, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationDampingSpline(self, value):
		if "UseRotationDampingSpline" in self.__dict__: self.__dict__["UseRotationDampingSpline"] = value; return
		self._oleobj_.Invoke(*((6023, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStiffnessExponent(self, value):
		if "UseRotationStiffnessExponent" in self.__dict__: self.__dict__["UseRotationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((6040, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStiffnessSpline(self, value):
		if "UseRotationStiffnessSpline" in self.__dict__: self.__dict__["UseRotationStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((6016, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStopAngle(self, value):
		if "UseRotationStopAngle" in self.__dict__: self.__dict__["UseRotationStopAngle"] = value; return
		self._oleobj_.Invoke(*((6031, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationDampingExponent(self, value):
		if "UseTranslationDampingExponent" in self.__dict__: self.__dict__["UseTranslationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((6037, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationDampingSpline(self, value):
		if "UseTranslationDampingSpline" in self.__dict__: self.__dict__["UseTranslationDampingSpline"] = value; return
		self._oleobj_.Invoke(*((6007, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationStiffnessExponent(self, value):
		if "UseTranslationStiffnessExponent" in self.__dict__: self.__dict__["UseTranslationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((6034, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationStiffnessSpline(self, value):
		if "UseTranslationStiffnessSpline" in self.__dict__: self.__dict__["UseTranslationStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((6002, LCID, 4, 0) + (value,) + ()))

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
		"RotationDampingCoefficientX": (6020, 2, (9, 0), (), "RotationDampingCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingCoefficientY": (6021, 2, (9, 0), (), "RotationDampingCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingCoefficientZ": (6022, 2, (9, 0), (), "RotationDampingCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponentX": (6045, 2, (9, 0), (), "RotationDampingExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponentY": (6046, 2, (9, 0), (), "RotationDampingExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponentZ": (6047, 2, (9, 0), (), "RotationDampingExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingSplineX": (6024, 2, (9, 0), (), "RotationDampingSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationDampingSplineY": (6025, 2, (9, 0), (), "RotationDampingSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationDampingSplineZ": (6026, 2, (9, 0), (), "RotationDampingSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationPreloadX": (6027, 2, (9, 0), (), "RotationPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationPreloadY": (6028, 2, (9, 0), (), "RotationPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationPreloadZ": (6029, 2, (9, 0), (), "RotationPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationPresetAngle": (6030, 2, (9, 0), (), "RotationPresetAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessCoefficientX": (6013, 2, (9, 0), (), "RotationStiffnessCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessCoefficientY": (6014, 2, (9, 0), (), "RotationStiffnessCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessCoefficientZ": (6015, 2, (9, 0), (), "RotationStiffnessCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponentX": (6041, 2, (9, 0), (), "RotationStiffnessExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponentY": (6042, 2, (9, 0), (), "RotationStiffnessExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponentZ": (6043, 2, (9, 0), (), "RotationStiffnessExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessSplineX": (6017, 2, (9, 0), (), "RotationStiffnessSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationStiffnessSplineY": (6018, 2, (9, 0), (), "RotationStiffnessSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationStiffnessSplineZ": (6019, 2, (9, 0), (), "RotationStiffnessSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationStopAngle": (6032, 2, (9, 0), (), "RotationStopAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStopStiffnessFactor": (6033, 2, (9, 0), (), "RotationStopStiffnessFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationClearance": (6012, 2, (9, 0), (), "TranslationClearance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingCoefficientAxial": (6006, 2, (9, 0), (), "TranslationDampingCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingCoefficientRadial": (6005, 2, (9, 0), (), "TranslationDampingCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingExponentAxial": (6039, 2, (9, 0), (), "TranslationDampingExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingExponentRadial": (6038, 2, (9, 0), (), "TranslationDampingExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingSplineAxial": (6009, 2, (9, 0), (), "TranslationDampingSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationDampingSplineRadial": (6008, 2, (9, 0), (), "TranslationDampingSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationPreloadAxial": (6011, 2, (9, 0), (), "TranslationPreloadAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationPreloadRadial": (6010, 2, (9, 0), (), "TranslationPreloadRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessCoefficientAxial": (6001, 2, (9, 0), (), "TranslationStiffnessCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessCoefficientRadial": (6000, 2, (9, 0), (), "TranslationStiffnessCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessExponentAxial": (6036, 2, (9, 0), (), "TranslationStiffnessExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessExponentRadial": (6035, 2, (9, 0), (), "TranslationStiffnessExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessSplineAxial": (6004, 2, (9, 0), (), "TranslationStiffnessSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationStiffnessSplineRadial": (6003, 2, (9, 0), (), "TranslationStiffnessSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseRotationDampingExponent": (6044, 2, (11, 0), (), "UseRotationDampingExponent", None),
		"UseRotationDampingSpline": (6023, 2, (11, 0), (), "UseRotationDampingSpline", None),
		"UseRotationStiffnessExponent": (6040, 2, (11, 0), (), "UseRotationStiffnessExponent", None),
		"UseRotationStiffnessSpline": (6016, 2, (11, 0), (), "UseRotationStiffnessSpline", None),
		"UseRotationStopAngle": (6031, 2, (11, 0), (), "UseRotationStopAngle", None),
		"UseTranslationDampingExponent": (6037, 2, (11, 0), (), "UseTranslationDampingExponent", None),
		"UseTranslationDampingSpline": (6007, 2, (11, 0), (), "UseTranslationDampingSpline", None),
		"UseTranslationStiffnessExponent": (6034, 2, (11, 0), (), "UseTranslationStiffnessExponent", None),
		"UseTranslationStiffnessSpline": (6002, 2, (11, 0), (), "UseTranslationStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"RotationDampingSplineX": ((6024, LCID, 4, 0),()),
		"RotationDampingSplineY": ((6025, LCID, 4, 0),()),
		"RotationDampingSplineZ": ((6026, LCID, 4, 0),()),
		"RotationStiffnessSplineX": ((6017, LCID, 4, 0),()),
		"RotationStiffnessSplineY": ((6018, LCID, 4, 0),()),
		"RotationStiffnessSplineZ": ((6019, LCID, 4, 0),()),
		"TranslationDampingSplineAxial": ((6009, LCID, 4, 0),()),
		"TranslationDampingSplineRadial": ((6008, LCID, 4, 0),()),
		"TranslationStiffnessSplineAxial": ((6004, LCID, 4, 0),()),
		"TranslationStiffnessSplineRadial": ((6003, LCID, 4, 0),()),
		"UseRotationDampingExponent": ((6044, LCID, 4, 0),()),
		"UseRotationDampingSpline": ((6023, LCID, 4, 0),()),
		"UseRotationStiffnessExponent": ((6040, LCID, 4, 0),()),
		"UseRotationStiffnessSpline": ((6016, LCID, 4, 0),()),
		"UseRotationStopAngle": ((6031, LCID, 4, 0),()),
		"UseTranslationDampingExponent": ((6037, LCID, 4, 0),()),
		"UseTranslationDampingSpline": ((6007, LCID, 4, 0),()),
		"UseTranslationStiffnessExponent": ((6034, LCID, 4, 0),()),
		"UseTranslationStiffnessSpline": ((6002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMAssemblyCollection(DispatchBaseClass):
	'''TrackHM Assembly Collection'''
	CLSID = IID('{12BBA5CC-DA01-4B3A-91DB-404C904569BD}')
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
		:rtype: recurdyn.TrackHM.ITrackHMAssembly
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')
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
		:rtype: recurdyn.TrackHM.ITrackHMAssembly
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')
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
		return win32com.client.util.Iterator(ob, '{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITrackHMAssemblyContactGroundTrackLinkShoePad(DispatchBaseClass):
	'''TrackHM Assembly Contact Ground TrackLink Shoe Pad'''
	CLSID = IID('{6E69D3B7-8017-427A-A4CE-B654E20AC0B6}')
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
		return self._oleobj_.InvokeTypes(6062, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import ground parameter
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(6063, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def SoftGroundType(self, val):
		'''
		Soft ground type
		
		:param val: TrackHMContactParameterSoftGroundType
		'''
		return self._oleobj_.InvokeTypes(6053, LCID, 1, (24, 0), ((3, 1),),val
			)


	def _get_Cohesion(self):
		return self._ApplyTypes_(*(6057, 2, (9, 0), (), "Cohesion", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(6012, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_ExponentialNumber(self):
		return self._ApplyTypes_(*(6056, 2, (9, 0), (), "ExponentialNumber", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(6016, 2, (9, 0), (), "Friction", '{839109C1-0AE4-4D08-BF2C-329740CBC436}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(6017, 2, (3, 0), (), "FrictionType", '{A9359E38-2F8C-46C9-9283-366B8FB02465}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(6014, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LateralFrictionFactor(self):
		return self._ApplyTypes_(*(6051, 2, (9, 0), (), "LateralFrictionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearingDeformationModulus(self):
		return self._ApplyTypes_(*(6059, 2, (9, 0), (), "ShearingDeformationModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearingResistanceAngle(self):
		return self._ApplyTypes_(*(6058, 2, (9, 0), (), "ShearingResistanceAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SinkageRatio(self):
		return self._ApplyTypes_(*(6060, 2, (9, 0), (), "SinkageRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(6010, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TerrainStiffnessKc(self):
		return self._ApplyTypes_(*(6054, 2, (9, 0), (), "TerrainStiffnessKc", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TerrainStiffnessKphi(self):
		return self._ApplyTypes_(*(6055, 2, (9, 0), (), "TerrainStiffnessKphi", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(6011, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(6004, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseFrictionSpline(self):
		return self._ApplyTypes_(*(6007, 2, (11, 0), (), "UseFrictionSpline", None))
	def _get_UseInactiveGroundParameter(self):
		return self._ApplyTypes_(*(6052, 2, (11, 0), (), "UseInactiveGroundParameter", None))
	def _get_UseInactiveSoftGroundParameter(self):
		return self._ApplyTypes_(*(6061, 2, (11, 0), (), "UseInactiveSoftGroundParameter", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(6013, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseLateralFrictionFactor(self):
		return self._ApplyTypes_(*(6050, 2, (11, 0), (), "UseLateralFrictionFactor", None))
	def _get_UseMoreFrictionData(self):
		return self._ApplyTypes_(*(6015, 2, (11, 0), (), "UseMoreFrictionData", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(6009, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(6001, 2, (11, 0), (), "UseStiffnessSpline", None))
	def _get_UseUserSubroutine(self):
		return self._ApplyTypes_(*(6064, 2, (11, 0), (), "UseUserSubroutine", None))
	def _get_UserSubroutine(self):
		return self._ApplyTypes_(*(6065, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((6005, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((6008, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((6017, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((6002, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((6011, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((6004, LCID, 4, 0) + (value,) + ()))
	def _set_UseFrictionSpline(self, value):
		if "UseFrictionSpline" in self.__dict__: self.__dict__["UseFrictionSpline"] = value; return
		self._oleobj_.Invoke(*((6007, LCID, 4, 0) + (value,) + ()))
	def _set_UseInactiveGroundParameter(self, value):
		if "UseInactiveGroundParameter" in self.__dict__: self.__dict__["UseInactiveGroundParameter"] = value; return
		self._oleobj_.Invoke(*((6052, LCID, 4, 0) + (value,) + ()))
	def _set_UseInactiveSoftGroundParameter(self, value):
		if "UseInactiveSoftGroundParameter" in self.__dict__: self.__dict__["UseInactiveSoftGroundParameter"] = value; return
		self._oleobj_.Invoke(*((6061, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((6013, LCID, 4, 0) + (value,) + ()))
	def _set_UseLateralFrictionFactor(self, value):
		if "UseLateralFrictionFactor" in self.__dict__: self.__dict__["UseLateralFrictionFactor"] = value; return
		self._oleobj_.Invoke(*((6050, LCID, 4, 0) + (value,) + ()))
	def _set_UseMoreFrictionData(self, value):
		if "UseMoreFrictionData" in self.__dict__: self.__dict__["UseMoreFrictionData"] = value; return
		self._oleobj_.Invoke(*((6015, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((6009, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((6001, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserSubroutine(self, value):
		if "UseUserSubroutine" in self.__dict__: self.__dict__["UseUserSubroutine"] = value; return
		self._oleobj_.Invoke(*((6064, LCID, 4, 0) + (value,) + ()))
	def _set_UserSubroutine(self, value):
		if "UserSubroutine" in self.__dict__: self.__dict__["UserSubroutine"] = value; return
		self._oleobj_.Invoke(*((6065, LCID, 4, 0) + (value,) + ()))

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

	:type: recurdyn.TrackHM.ITrackHMContactFriction
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

	:type: recurdyn.TrackHM.TrackHMFrictionType
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
		"Cohesion": (6057, 2, (9, 0), (), "Cohesion", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingCoefficient": (6003, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (6012, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (6005, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"ExponentialNumber": (6056, 2, (9, 0), (), "ExponentialNumber", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Friction": (6016, 2, (9, 0), (), "Friction", '{839109C1-0AE4-4D08-BF2C-329740CBC436}'),
		"FrictionCoefficient": (6006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (6008, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (6017, 2, (3, 0), (), "FrictionType", '{A9359E38-2F8C-46C9-9283-366B8FB02465}'),
		"IndentationExponent": (6014, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LateralFrictionFactor": (6051, 2, (9, 0), (), "LateralFrictionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearingDeformationModulus": (6059, 2, (9, 0), (), "ShearingDeformationModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearingResistanceAngle": (6058, 2, (9, 0), (), "ShearingResistanceAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SinkageRatio": (6060, 2, (9, 0), (), "SinkageRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (6000, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (6010, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (6002, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TerrainStiffnessKc": (6054, 2, (9, 0), (), "TerrainStiffnessKc", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TerrainStiffnessKphi": (6055, 2, (9, 0), (), "TerrainStiffnessKphi", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseDampingExponent": (6011, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (6004, 2, (11, 0), (), "UseDampingSpline", None),
		"UseFrictionSpline": (6007, 2, (11, 0), (), "UseFrictionSpline", None),
		"UseInactiveGroundParameter": (6052, 2, (11, 0), (), "UseInactiveGroundParameter", None),
		"UseInactiveSoftGroundParameter": (6061, 2, (11, 0), (), "UseInactiveSoftGroundParameter", None),
		"UseIndentationExponent": (6013, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseLateralFrictionFactor": (6050, 2, (11, 0), (), "UseLateralFrictionFactor", None),
		"UseMoreFrictionData": (6015, 2, (11, 0), (), "UseMoreFrictionData", None),
		"UseStiffnessExponent": (6009, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (6001, 2, (11, 0), (), "UseStiffnessSpline", None),
		"UseUserSubroutine": (6064, 2, (11, 0), (), "UseUserSubroutine", None),
		"UserSubroutine": (6065, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'),
	}
	_prop_map_put_ = {
		"DampingSpline": ((6005, LCID, 4, 0),()),
		"FrictionSpline": ((6008, LCID, 4, 0),()),
		"FrictionType": ((6017, LCID, 4, 0),()),
		"StiffnessSpline": ((6002, LCID, 4, 0),()),
		"UseDampingExponent": ((6011, LCID, 4, 0),()),
		"UseDampingSpline": ((6004, LCID, 4, 0),()),
		"UseFrictionSpline": ((6007, LCID, 4, 0),()),
		"UseInactiveGroundParameter": ((6052, LCID, 4, 0),()),
		"UseInactiveSoftGroundParameter": ((6061, LCID, 4, 0),()),
		"UseIndentationExponent": ((6013, LCID, 4, 0),()),
		"UseLateralFrictionFactor": ((6050, LCID, 4, 0),()),
		"UseMoreFrictionData": ((6015, LCID, 4, 0),()),
		"UseStiffnessExponent": ((6009, LCID, 4, 0),()),
		"UseStiffnessSpline": ((6001, LCID, 4, 0),()),
		"UseUserSubroutine": ((6064, LCID, 4, 0),()),
		"UserSubroutine": ((6065, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMAssemblySphereContact(DispatchBaseClass):
	'''TrackHM sphere contact property'''
	CLSID = IID('{6EBF0639-993D-437D-80AA-8372352B7281}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddSphereContact(self, pGeometrySphere):
		'''
		Add a sphere contact
		
		:param pGeometrySphere: IGeometrySphere
		'''
		return self._oleobj_.InvokeTypes(6002, LCID, 1, (24, 0), ((9, 1),),pGeometrySphere
			)


	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "ContactProperty", '{2248B1F9-1F1B-4D82-8B54-FAA47938AC38}'))
	def _get_GeometrySphereCollection(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "GeometrySphereCollection", '{0B006D28-70E2-4FBA-8A03-EC9EFC17C4E1}'))
	def _get_MaximumPenetration(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "MaximumPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	ContactProperty = property(_get_ContactProperty, None)
	'''
	Sphere contact property

	:type: recurdyn.TrackHM.ITrackHMSphereContactProperty
	'''
	GeometrySphereCollection = property(_get_GeometrySphereCollection, None)
	'''
	Sphere geometry collection of the sphere contact

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
		"ContactProperty": (6001, 2, (9, 0), (), "ContactProperty", '{2248B1F9-1F1B-4D82-8B54-FAA47938AC38}'),
		"GeometrySphereCollection": (6003, 2, (9, 0), (), "GeometrySphereCollection", '{0B006D28-70E2-4FBA-8A03-EC9EFC17C4E1}'),
		"MaximumPenetration": (6000, 2, (9, 0), (), "MaximumPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackHMBody(DispatchBaseClass):
	'''TrackHM body'''
	CLSID = IID('{4D568C44-E3AF-4517-B410-CA913214F421}')
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
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
		"GeneralBody": (6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
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

class ITrackHMBodyCollection(DispatchBaseClass):
	'''TrackHM wheel body collection'''
	CLSID = IID('{413B7957-9529-476C-932A-19CE19F9C013}')
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
		:rtype: recurdyn.TrackHM.ITrackHMBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4D568C44-E3AF-4517-B410-CA913214F421}')
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
		:rtype: recurdyn.TrackHM.ITrackHMBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4D568C44-E3AF-4517-B410-CA913214F421}')
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
		return win32com.client.util.Iterator(ob, '{4D568C44-E3AF-4517-B410-CA913214F421}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{4D568C44-E3AF-4517-B410-CA913214F421}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITrackHMBodyLink(DispatchBaseClass):
	'''TrackHM body link'''
	CLSID = IID('{710B4E1D-5E36-4439-ABFE-7D566EAAA31D}')
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
		ret = self._oleobj_.InvokeTypes(6062, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
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


	def UpdateAssembly(self):
		'''
		Update assembly
		'''
		return self._oleobj_.InvokeTypes(6059, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(6058, LCID, 1, (24, 0), (),)


	def _get_ActiveDoubleShoePad(self):
		return self._ApplyTypes_(*(6051, 2, (11, 0), (), "ActiveDoubleShoePad", None))
	def _get_ActiveShoePad(self):
		return self._ApplyTypes_(*(6050, 2, (11, 0), (), "ActiveShoePad", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DoubleShoePadFirst(self):
		return self._ApplyTypes_(*(6053, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_DoubleShoePadSecond(self):
		return self._ApplyTypes_(*(6054, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(6061, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_MeshSegment(self):
		return self._ApplyTypes_(*(6057, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ShoePadDepth(self):
		return self._ApplyTypes_(*(6056, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShoePointProfile(self):
		return self._ApplyTypes_(*(6055, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'))
	def _get_SingleShoePad(self):
		return self._ApplyTypes_(*(6052, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(6060, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActiveDoubleShoePad(self, value):
		if "ActiveDoubleShoePad" in self.__dict__: self.__dict__["ActiveDoubleShoePad"] = value; return
		self._oleobj_.Invoke(*((6051, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveShoePad(self, value):
		if "ActiveShoePad" in self.__dict__: self.__dict__["ActiveShoePad"] = value; return
		self._oleobj_.Invoke(*((6050, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((6060, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActiveDoubleShoePad = property(_get_ActiveDoubleShoePad, _set_ActiveDoubleShoePad)
	'''
	Double shoe pad

	:type: bool
	'''
	ActiveShoePad = property(_get_ActiveShoePad, _set_ActiveShoePad)
	'''
	Active shoe pad

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DoubleShoePadFirst = property(_get_DoubleShoePadFirst, None)
	'''
	Double shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	DoubleShoePadSecond = property(_get_DoubleShoePadSecond, None)
	'''
	Double shoe pad second profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
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
	MeshSegment = property(_get_MeshSegment, None)
	'''
	Mesh segment

	:type: recurdyn.TrackHM.ITrackHMMeshSegment
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
	ShoePadDepth = property(_get_ShoePadDepth, None)
	'''
	Shoe pad depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShoePointProfile = property(_get_ShoePointProfile, None)
	'''
	Shoe point profile

	:type: recurdyn.TrackHM.ITrackHMProfileShoePoint
	'''
	SingleShoePad = property(_get_SingleShoePad, None)
	'''
	Single shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
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
		"_set_ActiveDoubleShoePad": _set_ActiveDoubleShoePad,
		"_set_ActiveShoePad": _set_ActiveShoePad,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActiveDoubleShoePad": (6051, 2, (11, 0), (), "ActiveDoubleShoePad", None),
		"ActiveShoePad": (6050, 2, (11, 0), (), "ActiveShoePad", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DoubleShoePadFirst": (6053, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"DoubleShoePadSecond": (6054, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Graphic": (6061, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"MeshSegment": (6057, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ShoePadDepth": (6056, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShoePointProfile": (6055, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'),
		"SingleShoePad": (6052, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"UseBodyGraphic": (6060, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActiveDoubleShoePad": ((6051, LCID, 4, 0),()),
		"ActiveShoePad": ((6050, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((6060, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMBodyLinkCollection(DispatchBaseClass):
	'''TrackHM Body Link Collection'''
	CLSID = IID('{F592F48A-ED83-4179-982F-13D4F1E9AA40}')
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
		:rtype: recurdyn.TrackHM.ITrackHMBodyLink
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{710B4E1D-5E36-4439-ABFE-7D566EAAA31D}')
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
		:rtype: recurdyn.TrackHM.ITrackHMBodyLink
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{710B4E1D-5E36-4439-ABFE-7D566EAAA31D}')
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
		return win32com.client.util.Iterator(ob, '{710B4E1D-5E36-4439-ABFE-7D566EAAA31D}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{710B4E1D-5E36-4439-ABFE-7D566EAAA31D}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITrackHMBodyLinkDouble(DispatchBaseClass):
	'''TrackHM double link body'''
	CLSID = IID('{DEB4AA5A-2136-4E21-A20F-C00373893AD4}')
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
		ret = self._oleobj_.InvokeTypes(6062, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
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


	def UpdateAssembly(self):
		'''
		Update assembly
		'''
		return self._oleobj_.InvokeTypes(6059, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(6058, LCID, 1, (24, 0), (),)


	def _get_ActiveDoubleShoePad(self):
		return self._ApplyTypes_(*(6051, 2, (11, 0), (), "ActiveDoubleShoePad", None))
	def _get_ActiveShoePad(self):
		return self._ApplyTypes_(*(6050, 2, (11, 0), (), "ActiveShoePad", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DoubleShoePadFirst(self):
		return self._ApplyTypes_(*(6053, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_DoubleShoePadSecond(self):
		return self._ApplyTypes_(*(6054, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(6101, 2, (9, 0), (), "Geometry", '{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(6061, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_MeshSegment(self):
		return self._ApplyTypes_(*(6057, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ShoePadDepth(self):
		return self._ApplyTypes_(*(6056, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShoePointProfile(self):
		return self._ApplyTypes_(*(6055, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'))
	def _get_SingleShoePad(self):
		return self._ApplyTypes_(*(6052, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(6060, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActiveDoubleShoePad(self, value):
		if "ActiveDoubleShoePad" in self.__dict__: self.__dict__["ActiveDoubleShoePad"] = value; return
		self._oleobj_.Invoke(*((6051, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveShoePad(self, value):
		if "ActiveShoePad" in self.__dict__: self.__dict__["ActiveShoePad"] = value; return
		self._oleobj_.Invoke(*((6050, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((6060, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActiveDoubleShoePad = property(_get_ActiveDoubleShoePad, _set_ActiveDoubleShoePad)
	'''
	Double shoe pad

	:type: bool
	'''
	ActiveShoePad = property(_get_ActiveShoePad, _set_ActiveShoePad)
	'''
	Active shoe pad

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DoubleShoePadFirst = property(_get_DoubleShoePadFirst, None)
	'''
	Double shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	DoubleShoePadSecond = property(_get_DoubleShoePadSecond, None)
	'''
	Double shoe pad second profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
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

	:type: recurdyn.TrackHM.ITrackHMGeometryLinkDouble
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
	'''
	MeshSegment = property(_get_MeshSegment, None)
	'''
	Mesh segment

	:type: recurdyn.TrackHM.ITrackHMMeshSegment
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
	ShoePadDepth = property(_get_ShoePadDepth, None)
	'''
	Shoe pad depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShoePointProfile = property(_get_ShoePointProfile, None)
	'''
	Shoe point profile

	:type: recurdyn.TrackHM.ITrackHMProfileShoePoint
	'''
	SingleShoePad = property(_get_SingleShoePad, None)
	'''
	Single shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
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
		"_set_ActiveDoubleShoePad": _set_ActiveDoubleShoePad,
		"_set_ActiveShoePad": _set_ActiveShoePad,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActiveDoubleShoePad": (6051, 2, (11, 0), (), "ActiveDoubleShoePad", None),
		"ActiveShoePad": (6050, 2, (11, 0), (), "ActiveShoePad", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DoubleShoePadFirst": (6053, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"DoubleShoePadSecond": (6054, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (6101, 2, (9, 0), (), "Geometry", '{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}'),
		"Graphic": (6061, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"MeshSegment": (6057, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ShoePadDepth": (6056, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShoePointProfile": (6055, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'),
		"SingleShoePad": (6052, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"UseBodyGraphic": (6060, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActiveDoubleShoePad": ((6051, LCID, 4, 0),()),
		"ActiveShoePad": ((6050, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((6060, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMBodyLinkInner(DispatchBaseClass):
	'''TrackHM inner link body'''
	CLSID = IID('{F56F4B69-951E-4FD8-9770-3B45734FB048}')
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
		ret = self._oleobj_.InvokeTypes(6062, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
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


	def UpdateAssembly(self):
		'''
		Update assembly
		'''
		return self._oleobj_.InvokeTypes(6059, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(6058, LCID, 1, (24, 0), (),)


	def _get_ActiveDoubleShoePad(self):
		return self._ApplyTypes_(*(6051, 2, (11, 0), (), "ActiveDoubleShoePad", None))
	def _get_ActiveShoePad(self):
		return self._ApplyTypes_(*(6050, 2, (11, 0), (), "ActiveShoePad", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DoubleShoePadFirst(self):
		return self._ApplyTypes_(*(6053, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_DoubleShoePadSecond(self):
		return self._ApplyTypes_(*(6054, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(6101, 2, (9, 0), (), "Geometry", '{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(6061, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_MeshSegment(self):
		return self._ApplyTypes_(*(6057, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ShoePadDepth(self):
		return self._ApplyTypes_(*(6056, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShoePointProfile(self):
		return self._ApplyTypes_(*(6055, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'))
	def _get_SingleShoePad(self):
		return self._ApplyTypes_(*(6052, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(6060, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActiveDoubleShoePad(self, value):
		if "ActiveDoubleShoePad" in self.__dict__: self.__dict__["ActiveDoubleShoePad"] = value; return
		self._oleobj_.Invoke(*((6051, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveShoePad(self, value):
		if "ActiveShoePad" in self.__dict__: self.__dict__["ActiveShoePad"] = value; return
		self._oleobj_.Invoke(*((6050, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((6060, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActiveDoubleShoePad = property(_get_ActiveDoubleShoePad, _set_ActiveDoubleShoePad)
	'''
	Double shoe pad

	:type: bool
	'''
	ActiveShoePad = property(_get_ActiveShoePad, _set_ActiveShoePad)
	'''
	Active shoe pad

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DoubleShoePadFirst = property(_get_DoubleShoePadFirst, None)
	'''
	Double shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	DoubleShoePadSecond = property(_get_DoubleShoePadSecond, None)
	'''
	Double shoe pad second profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
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

	:type: recurdyn.TrackHM.ITrackHMGeometryLinkInner
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
	'''
	MeshSegment = property(_get_MeshSegment, None)
	'''
	Mesh segment

	:type: recurdyn.TrackHM.ITrackHMMeshSegment
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
	ShoePadDepth = property(_get_ShoePadDepth, None)
	'''
	Shoe pad depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShoePointProfile = property(_get_ShoePointProfile, None)
	'''
	Shoe point profile

	:type: recurdyn.TrackHM.ITrackHMProfileShoePoint
	'''
	SingleShoePad = property(_get_SingleShoePad, None)
	'''
	Single shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
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
		"_set_ActiveDoubleShoePad": _set_ActiveDoubleShoePad,
		"_set_ActiveShoePad": _set_ActiveShoePad,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActiveDoubleShoePad": (6051, 2, (11, 0), (), "ActiveDoubleShoePad", None),
		"ActiveShoePad": (6050, 2, (11, 0), (), "ActiveShoePad", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DoubleShoePadFirst": (6053, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"DoubleShoePadSecond": (6054, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (6101, 2, (9, 0), (), "Geometry", '{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}'),
		"Graphic": (6061, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"MeshSegment": (6057, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ShoePadDepth": (6056, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShoePointProfile": (6055, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'),
		"SingleShoePad": (6052, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"UseBodyGraphic": (6060, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActiveDoubleShoePad": ((6051, LCID, 4, 0),()),
		"ActiveShoePad": ((6050, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((6060, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMBodyLinkSingle(DispatchBaseClass):
	'''TrackHM single link body'''
	CLSID = IID('{A97F123D-9445-453A-A688-FD06CCEF9B94}')
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
		ret = self._oleobj_.InvokeTypes(6062, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
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


	def UpdateAssembly(self):
		'''
		Update assembly
		'''
		return self._oleobj_.InvokeTypes(6059, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(6058, LCID, 1, (24, 0), (),)


	def _get_ActiveDoubleShoePad(self):
		return self._ApplyTypes_(*(6051, 2, (11, 0), (), "ActiveDoubleShoePad", None))
	def _get_ActiveShoePad(self):
		return self._ApplyTypes_(*(6050, 2, (11, 0), (), "ActiveShoePad", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DoubleShoePadFirst(self):
		return self._ApplyTypes_(*(6053, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_DoubleShoePadSecond(self):
		return self._ApplyTypes_(*(6054, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(6101, 2, (9, 0), (), "Geometry", '{0CDCA31B-C017-4528-8B11-4CE8D5E60525}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(6061, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_MeshSegment(self):
		return self._ApplyTypes_(*(6057, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ShoePadDepth(self):
		return self._ApplyTypes_(*(6056, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShoePointProfile(self):
		return self._ApplyTypes_(*(6055, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'))
	def _get_SingleShoePad(self):
		return self._ApplyTypes_(*(6052, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(6060, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActiveDoubleShoePad(self, value):
		if "ActiveDoubleShoePad" in self.__dict__: self.__dict__["ActiveDoubleShoePad"] = value; return
		self._oleobj_.Invoke(*((6051, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveShoePad(self, value):
		if "ActiveShoePad" in self.__dict__: self.__dict__["ActiveShoePad"] = value; return
		self._oleobj_.Invoke(*((6050, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((6060, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActiveDoubleShoePad = property(_get_ActiveDoubleShoePad, _set_ActiveDoubleShoePad)
	'''
	Double shoe pad

	:type: bool
	'''
	ActiveShoePad = property(_get_ActiveShoePad, _set_ActiveShoePad)
	'''
	Active shoe pad

	:type: bool
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DoubleShoePadFirst = property(_get_DoubleShoePadFirst, None)
	'''
	Double shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	DoubleShoePadSecond = property(_get_DoubleShoePadSecond, None)
	'''
	Double shoe pad second profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
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

	:type: recurdyn.TrackHM.ITrackHMGeometryLinkSingle
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
	'''
	MeshSegment = property(_get_MeshSegment, None)
	'''
	Mesh segment

	:type: recurdyn.TrackHM.ITrackHMMeshSegment
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
	ShoePadDepth = property(_get_ShoePadDepth, None)
	'''
	Shoe pad depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShoePointProfile = property(_get_ShoePointProfile, None)
	'''
	Shoe point profile

	:type: recurdyn.TrackHM.ITrackHMProfileShoePoint
	'''
	SingleShoePad = property(_get_SingleShoePad, None)
	'''
	Single shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
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
		"_set_ActiveDoubleShoePad": _set_ActiveDoubleShoePad,
		"_set_ActiveShoePad": _set_ActiveShoePad,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActiveDoubleShoePad": (6051, 2, (11, 0), (), "ActiveDoubleShoePad", None),
		"ActiveShoePad": (6050, 2, (11, 0), (), "ActiveShoePad", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DoubleShoePadFirst": (6053, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"DoubleShoePadSecond": (6054, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (6101, 2, (9, 0), (), "Geometry", '{0CDCA31B-C017-4528-8B11-4CE8D5E60525}'),
		"Graphic": (6061, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"MeshSegment": (6057, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ShoePadDepth": (6056, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShoePointProfile": (6055, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'),
		"SingleShoePad": (6052, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"UseBodyGraphic": (6060, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActiveDoubleShoePad": ((6051, LCID, 4, 0),()),
		"ActiveShoePad": ((6050, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((6060, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMBodySprocket(DispatchBaseClass):
	'''TrackHMBodySprocket'''
	CLSID = IID('{4F847ED1-32A7-4A6F-9E0C-D0ECE3833FE2}')
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
		return self._oleobj_.InvokeTypes(6055, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(6050, 2, (9, 0), (), "ContactProperty", '{045DD783-342A-40C7-8743-C1EE4A708B7D}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(6053, 2, (9, 0), (), "ContactSearch", '{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}'))
	def _get_CreateContactOutputFile(self):
		return self._ApplyTypes_(*(6056, 2, (11, 0), (), "CreateContactOutputFile", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(6051, 2, (9, 0), (), "Geometry", '{9341322D-E9F4-41D4-B866-B97D1E1E773E}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ToothProfile(self):
		return self._ApplyTypes_(*(6052, 2, (9, 0), (), "ToothProfile", '{6049C1CF-A437-4579-BEA1-F7C3C016EF83}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_CreateContactOutputFile(self, value):
		if "CreateContactOutputFile" in self.__dict__: self.__dict__["CreateContactOutputFile"] = value; return
		self._oleobj_.Invoke(*((6056, LCID, 4, 0) + (value,) + ()))
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

	:type: recurdyn.TrackHM.ITrackHMContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.TrackHM.ITrackHMContactSearch
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

	:type: recurdyn.TrackHM.ITrackHMGeometrySprocket
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

	:type: recurdyn.TrackHM.ITrackHMToothProfileSprocket
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
		"ContactProperty": (6050, 2, (9, 0), (), "ContactProperty", '{045DD783-342A-40C7-8743-C1EE4A708B7D}'),
		"ContactSearch": (6053, 2, (9, 0), (), "ContactSearch", '{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}'),
		"CreateContactOutputFile": (6056, 2, (11, 0), (), "CreateContactOutputFile", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (6051, 2, (9, 0), (), "Geometry", '{9341322D-E9F4-41D4-B866-B97D1E1E773E}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ToothProfile": (6052, 2, (9, 0), (), "ToothProfile", '{6049C1CF-A437-4579-BEA1-F7C3C016EF83}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"CreateContactOutputFile": ((6056, LCID, 4, 0),()),
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

class ITrackHMBodyWheelDouble(DispatchBaseClass):
	'''TrackHM Wheel double'''
	CLSID = IID('{F271147D-2B1A-460F-841D-8743839E155D}')
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
	def _get_ContactCenterProperty(self):
		return self._ApplyTypes_(*(6051, 2, (9, 0), (), "ContactCenterProperty", '{045DD783-342A-40C7-8743-C1EE4A708B7D}'))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(6050, 2, (9, 0), (), "ContactProperty", '{045DD783-342A-40C7-8743-C1EE4A708B7D}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(6053, 2, (9, 0), (), "ContactSearch", '{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(6052, 2, (9, 0), (), "Geometry", '{4ED4187A-A396-4F74-95F7-8708C083E2B7}'))
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
	ContactCenterProperty = property(_get_ContactCenterProperty, None)
	'''
	Center Contact Property

	:type: recurdyn.TrackHM.ITrackHMContactProperty
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact Property

	:type: recurdyn.TrackHM.ITrackHMContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.TrackHM.ITrackHMContactSearch
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

	:type: recurdyn.TrackHM.ITrackHMGeometryWheelDouble
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
		"ContactCenterProperty": (6051, 2, (9, 0), (), "ContactCenterProperty", '{045DD783-342A-40C7-8743-C1EE4A708B7D}'),
		"ContactProperty": (6050, 2, (9, 0), (), "ContactProperty", '{045DD783-342A-40C7-8743-C1EE4A708B7D}'),
		"ContactSearch": (6053, 2, (9, 0), (), "ContactSearch", '{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (6052, 2, (9, 0), (), "Geometry", '{4ED4187A-A396-4F74-95F7-8708C083E2B7}'),
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

class ITrackHMBodyWheelSingle(DispatchBaseClass):
	'''TrackHM wheel single'''
	CLSID = IID('{93C13C52-83EC-4438-AEDD-D41A1EC42FF6}')
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
		return self._ApplyTypes_(*(6050, 2, (9, 0), (), "ContactProperty", '{045DD783-342A-40C7-8743-C1EE4A708B7D}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(6052, 2, (9, 0), (), "ContactSearch", '{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(6051, 2, (9, 0), (), "Geometry", '{CC11A196-ED40-4A90-BAD1-EAAFD94EC7B2}'))
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

	:type: recurdyn.TrackHM.ITrackHMContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.TrackHM.ITrackHMContactSearch
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

	:type: recurdyn.TrackHM.ITrackHMGeometryWheelSingle
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
		"ContactProperty": (6050, 2, (9, 0), (), "ContactProperty", '{045DD783-342A-40C7-8743-C1EE4A708B7D}'),
		"ContactSearch": (6052, 2, (9, 0), (), "ContactSearch", '{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (6000, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (6051, 2, (9, 0), (), "Geometry", '{CC11A196-ED40-4A90-BAD1-EAAFD94EC7B2}'),
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

class ITrackHMContactFriction(DispatchBaseClass):
	'''TrackHM contact friction'''
	CLSID = IID('{839109C1-0AE4-4D08-BF2C-329740CBC436}')
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
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticFrictionCoefficient(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticThresholdVelocity(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

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
		"DynamicThresholdVelocity": (6002, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticFrictionCoefficient": (6003, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticThresholdVelocity": (6001, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackHMContactProperty(DispatchBaseClass):
	'''TrackHM contact property'''
	CLSID = IID('{045DD783-342A-40C7-8743-C1EE4A708B7D}')
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
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(6012, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(6016, 2, (9, 0), (), "Friction", '{839109C1-0AE4-4D08-BF2C-329740CBC436}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(6017, 2, (3, 0), (), "FrictionType", '{A9359E38-2F8C-46C9-9283-366B8FB02465}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(6014, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(6010, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(6011, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(6004, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseFrictionSpline(self):
		return self._ApplyTypes_(*(6007, 2, (11, 0), (), "UseFrictionSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(6013, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseMoreFrictionData(self):
		return self._ApplyTypes_(*(6015, 2, (11, 0), (), "UseMoreFrictionData", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(6009, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(6001, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((6005, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((6008, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((6017, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((6002, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((6011, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((6004, LCID, 4, 0) + (value,) + ()))
	def _set_UseFrictionSpline(self, value):
		if "UseFrictionSpline" in self.__dict__: self.__dict__["UseFrictionSpline"] = value; return
		self._oleobj_.Invoke(*((6007, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((6013, LCID, 4, 0) + (value,) + ()))
	def _set_UseMoreFrictionData(self, value):
		if "UseMoreFrictionData" in self.__dict__: self.__dict__["UseMoreFrictionData"] = value; return
		self._oleobj_.Invoke(*((6015, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((6009, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((6001, LCID, 4, 0) + (value,) + ()))

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

	:type: recurdyn.TrackHM.ITrackHMContactFriction
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

	:type: recurdyn.TrackHM.TrackHMFrictionType
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
		"DampingCoefficient": (6003, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (6012, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (6005, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"Friction": (6016, 2, (9, 0), (), "Friction", '{839109C1-0AE4-4D08-BF2C-329740CBC436}'),
		"FrictionCoefficient": (6006, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (6008, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (6017, 2, (3, 0), (), "FrictionType", '{A9359E38-2F8C-46C9-9283-366B8FB02465}'),
		"IndentationExponent": (6014, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (6000, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (6010, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (6002, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (6011, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (6004, 2, (11, 0), (), "UseDampingSpline", None),
		"UseFrictionSpline": (6007, 2, (11, 0), (), "UseFrictionSpline", None),
		"UseIndentationExponent": (6013, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseMoreFrictionData": (6015, 2, (11, 0), (), "UseMoreFrictionData", None),
		"UseStiffnessExponent": (6009, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (6001, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"DampingSpline": ((6005, LCID, 4, 0),()),
		"FrictionSpline": ((6008, LCID, 4, 0),()),
		"FrictionType": ((6017, LCID, 4, 0),()),
		"StiffnessSpline": ((6002, LCID, 4, 0),()),
		"UseDampingExponent": ((6011, LCID, 4, 0),()),
		"UseDampingSpline": ((6004, LCID, 4, 0),()),
		"UseFrictionSpline": ((6007, LCID, 4, 0),()),
		"UseIndentationExponent": ((6013, LCID, 4, 0),()),
		"UseMoreFrictionData": ((6015, LCID, 4, 0),()),
		"UseStiffnessExponent": ((6009, LCID, 4, 0),()),
		"UseStiffnessSpline": ((6001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMContactSearch(DispatchBaseClass):
	'''TrackHM contact search'''
	CLSID = IID('{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}')
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
		return self._ApplyTypes_(*(6000, 2, (3, 0), (), "Type", '{7DADC137-519B-4F3E-B1FB-6AA19C0555B5}'))
	def _get_UseUserBoundaryForPartialSearch(self):
		return self._ApplyTypes_(*(6001, 2, (11, 0), (), "UseUserBoundaryForPartialSearch", None))
	def _get_UserBoundaryForPartialSearch(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "UserBoundaryForPartialSearch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((6000, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserBoundaryForPartialSearch(self, value):
		if "UseUserBoundaryForPartialSearch" in self.__dict__: self.__dict__["UseUserBoundaryForPartialSearch"] = value; return
		self._oleobj_.Invoke(*((6001, LCID, 4, 0) + (value,) + ()))

	Type = property(_get_Type, _set_Type)
	'''
	Search type

	:type: recurdyn.TrackHM.TrackHMContactSearchType
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
		"Type": (6000, 2, (3, 0), (), "Type", '{7DADC137-519B-4F3E-B1FB-6AA19C0555B5}'),
		"UseUserBoundaryForPartialSearch": (6001, 2, (11, 0), (), "UseUserBoundaryForPartialSearch", None),
		"UserBoundaryForPartialSearch": (6002, 2, (9, 0), (), "UserBoundaryForPartialSearch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Type": ((6000, LCID, 4, 0),()),
		"UseUserBoundaryForPartialSearch": ((6001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMGeometryLinkDouble(DispatchBaseClass):
	'''TrackHM double link geometry'''
	CLSID = IID('{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_CenterGuideLength(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "CenterGuideLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CenterGuidePosition(self):
		return self._ApplyTypes_(*(6012, 2, (8197, 0), (), "CenterGuidePosition", None))
	def _get_CenterGuideThickness(self):
		return self._ApplyTypes_(*(6009, 2, (9, 0), (), "CenterGuideThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_EndConnectorLength(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "EndConnectorLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftLength(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "LeftLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftPinPosition(self):
		return self._ApplyTypes_(*(6010, 2, (8197, 0), (), "LeftPinPosition", None))
	def _get_LowerHeight(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "LowerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinRadius(self):
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RightLength(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "RightLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RightPinPosition(self):
		return self._ApplyTypes_(*(6011, 2, (8197, 0), (), "RightPinPosition", None))
	def _get_UpperHeight(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "UpperHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_CenterGuidePosition(self, value):
		if "CenterGuidePosition" in self.__dict__: self.__dict__["CenterGuidePosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6012, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LeftPinPosition(self, value):
		if "LeftPinPosition" in self.__dict__: self.__dict__["LeftPinPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6010, LCID, 4, 0) + (variantValue,) + ()))
	def _set_RightPinPosition(self, value):
		if "RightPinPosition" in self.__dict__: self.__dict__["RightPinPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6011, LCID, 4, 0) + (variantValue,) + ()))

	CenterGuideLength = property(_get_CenterGuideLength, None)
	'''
	Center guide length

	:type: recurdyn.ProcessNet.IDouble
	'''
	CenterGuidePosition = property(_get_CenterGuidePosition, _set_CenterGuidePosition)
	'''
	Center guide position

	:type: list[float]
	'''
	CenterGuideThickness = property(_get_CenterGuideThickness, None)
	'''
	Center guide thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	EndConnectorLength = property(_get_EndConnectorLength, None)
	'''
	End connector Length

	:type: recurdyn.ProcessNet.IDouble
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
	LowerHeight = property(_get_LowerHeight, None)
	'''
	Lower height

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
	UpperHeight = property(_get_UpperHeight, None)
	'''
	Upper height

	:type: recurdyn.ProcessNet.IDouble
	'''
	Width = property(_get_Width, None)
	'''
	Width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_CenterGuidePosition": _set_CenterGuidePosition,
		"_set_LeftPinPosition": _set_LeftPinPosition,
		"_set_RightPinPosition": _set_RightPinPosition,
	}
	_prop_map_get_ = {
		"CenterGuideLength": (6008, 2, (9, 0), (), "CenterGuideLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CenterGuidePosition": (6012, 2, (8197, 0), (), "CenterGuidePosition", None),
		"CenterGuideThickness": (6009, 2, (9, 0), (), "CenterGuideThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"EndConnectorLength": (6005, 2, (9, 0), (), "EndConnectorLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftLength": (6000, 2, (9, 0), (), "LeftLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftPinPosition": (6010, 2, (8197, 0), (), "LeftPinPosition", None),
		"LowerHeight": (6003, 2, (9, 0), (), "LowerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinLength": (6006, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinRadius": (6007, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RightLength": (6001, 2, (9, 0), (), "RightLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RightPinPosition": (6011, 2, (8197, 0), (), "RightPinPosition", None),
		"UpperHeight": (6002, 2, (9, 0), (), "UpperHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Width": (6004, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"CenterGuidePosition": ((6012, LCID, 4, 0),()),
		"LeftPinPosition": ((6010, LCID, 4, 0),()),
		"RightPinPosition": ((6011, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMGeometryLinkInner(DispatchBaseClass):
	'''TrackHM inner link geometry'''
	CLSID = IID('{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_CenterGuideLength(self):
		return self._ApplyTypes_(*(6012, 2, (9, 0), (), "CenterGuideLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CenterGuidePosition(self):
		return self._ApplyTypes_(*(6011, 2, (8197, 0), (), "CenterGuidePosition", None))
	def _get_CenterGuideThickness(self):
		return self._ApplyTypes_(*(6013, 2, (9, 0), (), "CenterGuideThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ContactRadius(self):
		return self._ApplyTypes_(*(6016, 2, (9, 0), (), "ContactRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_EndConnectorLength(self):
		return self._ApplyTypes_(*(6018, 2, (9, 0), (), "EndConnectorLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InnerWidth(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "InnerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftContactCylinderPosition(self):
		return self._ApplyTypes_(*(6014, 2, (8197, 0), (), "LeftContactCylinderPosition", None))
	def _get_LeftLength(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "LeftLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftPinPosition(self):
		return self._ApplyTypes_(*(6008, 2, (8197, 0), (), "LeftPinPosition", None))
	def _get_LinkWidth(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "LinkWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LowerHeight(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "LowerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_OuterWidth(self):
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "OuterWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinRadius(self):
		return self._ApplyTypes_(*(6010, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RightContactCylinderPosition(self):
		return self._ApplyTypes_(*(6015, 2, (8197, 0), (), "RightContactCylinderPosition", None))
	def _get_RightLength(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "RightLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RightPinPosition(self):
		return self._ApplyTypes_(*(6009, 2, (8197, 0), (), "RightPinPosition", None))
	def _get_ShoeRadius(self):
		return self._ApplyTypes_(*(6017, 2, (9, 0), (), "ShoeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UpperHeight(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "UpperHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_CenterGuidePosition(self, value):
		if "CenterGuidePosition" in self.__dict__: self.__dict__["CenterGuidePosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6011, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LeftContactCylinderPosition(self, value):
		if "LeftContactCylinderPosition" in self.__dict__: self.__dict__["LeftContactCylinderPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6014, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LeftPinPosition(self, value):
		if "LeftPinPosition" in self.__dict__: self.__dict__["LeftPinPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6008, LCID, 4, 0) + (variantValue,) + ()))
	def _set_RightContactCylinderPosition(self, value):
		if "RightContactCylinderPosition" in self.__dict__: self.__dict__["RightContactCylinderPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6015, LCID, 4, 0) + (variantValue,) + ()))
	def _set_RightPinPosition(self, value):
		if "RightPinPosition" in self.__dict__: self.__dict__["RightPinPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6009, LCID, 4, 0) + (variantValue,) + ()))

	CenterGuideLength = property(_get_CenterGuideLength, None)
	'''
	Center guide length

	:type: recurdyn.ProcessNet.IDouble
	'''
	CenterGuidePosition = property(_get_CenterGuidePosition, _set_CenterGuidePosition)
	'''
	Center guide position

	:type: list[float]
	'''
	CenterGuideThickness = property(_get_CenterGuideThickness, None)
	'''
	Center guide thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	ContactRadius = property(_get_ContactRadius, None)
	'''
	Contact radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	EndConnectorLength = property(_get_EndConnectorLength, None)
	'''
	End connector length

	:type: recurdyn.ProcessNet.IDouble
	'''
	InnerWidth = property(_get_InnerWidth, None)
	'''
	Inner width

	:type: recurdyn.ProcessNet.IDouble
	'''
	LeftContactCylinderPosition = property(_get_LeftContactCylinderPosition, _set_LeftContactCylinderPosition)
	'''
	Left contact cylinder position

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
	LinkWidth = property(_get_LinkWidth, None)
	'''
	Link width

	:type: recurdyn.ProcessNet.IDouble
	'''
	LowerHeight = property(_get_LowerHeight, None)
	'''
	Lower height

	:type: recurdyn.ProcessNet.IDouble
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
	RightContactCylinderPosition = property(_get_RightContactCylinderPosition, _set_RightContactCylinderPosition)
	'''
	Right contact cylinder position

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
	ShoeRadius = property(_get_ShoeRadius, None)
	'''
	Shoe radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	UpperHeight = property(_get_UpperHeight, None)
	'''
	Upper height

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_CenterGuidePosition": _set_CenterGuidePosition,
		"_set_LeftContactCylinderPosition": _set_LeftContactCylinderPosition,
		"_set_LeftPinPosition": _set_LeftPinPosition,
		"_set_RightContactCylinderPosition": _set_RightContactCylinderPosition,
		"_set_RightPinPosition": _set_RightPinPosition,
	}
	_prop_map_get_ = {
		"CenterGuideLength": (6012, 2, (9, 0), (), "CenterGuideLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CenterGuidePosition": (6011, 2, (8197, 0), (), "CenterGuidePosition", None),
		"CenterGuideThickness": (6013, 2, (9, 0), (), "CenterGuideThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ContactRadius": (6016, 2, (9, 0), (), "ContactRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"EndConnectorLength": (6018, 2, (9, 0), (), "EndConnectorLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InnerWidth": (6006, 2, (9, 0), (), "InnerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftContactCylinderPosition": (6014, 2, (8197, 0), (), "LeftContactCylinderPosition", None),
		"LeftLength": (6000, 2, (9, 0), (), "LeftLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftPinPosition": (6008, 2, (8197, 0), (), "LeftPinPosition", None),
		"LinkWidth": (6005, 2, (9, 0), (), "LinkWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LowerHeight": (6003, 2, (9, 0), (), "LowerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"OuterWidth": (6007, 2, (9, 0), (), "OuterWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinLength": (6004, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinRadius": (6010, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RightContactCylinderPosition": (6015, 2, (8197, 0), (), "RightContactCylinderPosition", None),
		"RightLength": (6001, 2, (9, 0), (), "RightLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RightPinPosition": (6009, 2, (8197, 0), (), "RightPinPosition", None),
		"ShoeRadius": (6017, 2, (9, 0), (), "ShoeRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UpperHeight": (6002, 2, (9, 0), (), "UpperHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"CenterGuidePosition": ((6011, LCID, 4, 0),()),
		"LeftContactCylinderPosition": ((6014, LCID, 4, 0),()),
		"LeftPinPosition": ((6008, LCID, 4, 0),()),
		"RightContactCylinderPosition": ((6015, LCID, 4, 0),()),
		"RightPinPosition": ((6009, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMGeometryLinkSingle(DispatchBaseClass):
	'''TrackHM single link geometry'''
	CLSID = IID('{0CDCA31B-C017-4528-8B11-4CE8D5E60525}')
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
		return self._ApplyTypes_(*(6016, 2, (5, 0), (), "BushingWidth", None))
	def _get_CenterGuideLength(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "CenterGuideLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_CenterGuidePosition(self):
		return self._ApplyTypes_(*(6012, 2, (8197, 0), (), "CenterGuidePosition", None))
	def _get_CenterGuideThickness(self):
		return self._ApplyTypes_(*(6009, 2, (9, 0), (), "CenterGuideThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ConnectorLength(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "ConnectorLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftBushingPosition(self):
		return self._ApplyTypes_(*(6014, 2, (8197, 0), (), "LeftBushingPosition", None))
	def _get_LeftLength(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "LeftLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LeftPinPosition(self):
		return self._ApplyTypes_(*(6010, 2, (8197, 0), (), "LeftPinPosition", None))
	def _get_LowerHeight(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "LowerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinRadius(self):
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RightBushingPosition(self):
		return self._ApplyTypes_(*(6015, 2, (8197, 0), (), "RightBushingPosition", None))
	def _get_RightLength(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "RightLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RightPinPosition(self):
		return self._ApplyTypes_(*(6011, 2, (8197, 0), (), "RightPinPosition", None))
	def _get_UpperHeight(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "UpperHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseBushingPosition(self):
		return self._ApplyTypes_(*(6013, 2, (11, 0), (), "UseBushingPosition", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_BushingWidth(self, value):
		if "BushingWidth" in self.__dict__: self.__dict__["BushingWidth"] = value; return
		self._oleobj_.Invoke(*((6016, LCID, 4, 0) + (value,) + ()))
	def _set_CenterGuidePosition(self, value):
		if "CenterGuidePosition" in self.__dict__: self.__dict__["CenterGuidePosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6012, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LeftBushingPosition(self, value):
		if "LeftBushingPosition" in self.__dict__: self.__dict__["LeftBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6014, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LeftPinPosition(self, value):
		if "LeftPinPosition" in self.__dict__: self.__dict__["LeftPinPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6010, LCID, 4, 0) + (variantValue,) + ()))
	def _set_RightBushingPosition(self, value):
		if "RightBushingPosition" in self.__dict__: self.__dict__["RightBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6015, LCID, 4, 0) + (variantValue,) + ()))
	def _set_RightPinPosition(self, value):
		if "RightPinPosition" in self.__dict__: self.__dict__["RightPinPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((6011, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseBushingPosition(self, value):
		if "UseBushingPosition" in self.__dict__: self.__dict__["UseBushingPosition"] = value; return
		self._oleobj_.Invoke(*((6013, LCID, 4, 0) + (value,) + ()))

	BushingWidth = property(_get_BushingWidth, _set_BushingWidth)
	'''
	Bushing Width

	:type: float
	'''
	CenterGuideLength = property(_get_CenterGuideLength, None)
	'''
	Center guide length

	:type: recurdyn.ProcessNet.IDouble
	'''
	CenterGuidePosition = property(_get_CenterGuidePosition, _set_CenterGuidePosition)
	'''
	Center guide position

	:type: list[float]
	'''
	CenterGuideThickness = property(_get_CenterGuideThickness, None)
	'''
	Center guide thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	ConnectorLength = property(_get_ConnectorLength, None)
	'''
	Connector Length

	:type: recurdyn.ProcessNet.IDouble
	'''
	LeftBushingPosition = property(_get_LeftBushingPosition, _set_LeftBushingPosition)
	'''
	Left bushing position

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
	LowerHeight = property(_get_LowerHeight, None)
	'''
	Lower height

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
	Right bushing position

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
	UpperHeight = property(_get_UpperHeight, None)
	'''
	Upper height

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseBushingPosition = property(_get_UseBushingPosition, _set_UseBushingPosition)
	'''
	Use left bushing position

	:type: bool
	'''
	Width = property(_get_Width, None)
	'''
	Width

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_BushingWidth": _set_BushingWidth,
		"_set_CenterGuidePosition": _set_CenterGuidePosition,
		"_set_LeftBushingPosition": _set_LeftBushingPosition,
		"_set_LeftPinPosition": _set_LeftPinPosition,
		"_set_RightBushingPosition": _set_RightBushingPosition,
		"_set_RightPinPosition": _set_RightPinPosition,
		"_set_UseBushingPosition": _set_UseBushingPosition,
	}
	_prop_map_get_ = {
		"BushingWidth": (6016, 2, (5, 0), (), "BushingWidth", None),
		"CenterGuideLength": (6008, 2, (9, 0), (), "CenterGuideLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"CenterGuidePosition": (6012, 2, (8197, 0), (), "CenterGuidePosition", None),
		"CenterGuideThickness": (6009, 2, (9, 0), (), "CenterGuideThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ConnectorLength": (6005, 2, (9, 0), (), "ConnectorLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftBushingPosition": (6014, 2, (8197, 0), (), "LeftBushingPosition", None),
		"LeftLength": (6000, 2, (9, 0), (), "LeftLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LeftPinPosition": (6010, 2, (8197, 0), (), "LeftPinPosition", None),
		"LowerHeight": (6003, 2, (9, 0), (), "LowerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinLength": (6006, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinRadius": (6007, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RightBushingPosition": (6015, 2, (8197, 0), (), "RightBushingPosition", None),
		"RightLength": (6001, 2, (9, 0), (), "RightLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RightPinPosition": (6011, 2, (8197, 0), (), "RightPinPosition", None),
		"UpperHeight": (6002, 2, (9, 0), (), "UpperHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseBushingPosition": (6013, 2, (11, 0), (), "UseBushingPosition", None),
		"Width": (6004, 2, (9, 0), (), "Width", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"BushingWidth": ((6016, LCID, 4, 0),()),
		"CenterGuidePosition": ((6012, LCID, 4, 0),()),
		"LeftBushingPosition": ((6014, LCID, 4, 0),()),
		"LeftPinPosition": ((6010, LCID, 4, 0),()),
		"RightBushingPosition": ((6015, LCID, 4, 0),()),
		"RightPinPosition": ((6011, LCID, 4, 0),()),
		"UseBushingPosition": ((6013, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMGeometrySprocket(DispatchBaseClass):
	'''TrackHMBodySprocketGeometry'''
	CLSID = IID('{9341322D-E9F4-41D4-B866-B97D1E1E773E}')
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
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "AddendumCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_BaseCircleRadius(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "BaseCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DedendumCircleRadius(self):
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "DedendumCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(6011, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None))
	def _get_LinkAssemblyRadialDistance(self):
		return self._ApplyTypes_(*(6012, 2, (5, 0), (), "LinkAssemblyRadialDistance", None))
	def _get_NumberOfTeeth(self):
		return self._ApplyTypes_(*(6003, 2, (19, 0), (), "NumberOfTeeth", None))
	def _get_PitchCircleRadius(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "PitchCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SprocketCarrierRadius(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "SprocketCarrierRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SprocketCarrierWidth(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "SprocketCarrierWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SprocketTotalWidth(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "SprocketTotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TrackLinkLoopRadius(self):
		return self._ApplyTypes_(*(6009, 2, (5, 0), (), "TrackLinkLoopRadius", None))
	def _get_TrackLinkPinCircleRadius(self):
		return self._ApplyTypes_(*(6008, 2, (5, 0), (), "TrackLinkPinCircleRadius", None))
	def _get_UseLinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(6010, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None))

	def _set_LinkAssemblyAssembledRadius(self, value):
		if "LinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["LinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((6011, LCID, 4, 0) + (value,) + ()))
	def _set_LinkAssemblyRadialDistance(self, value):
		if "LinkAssemblyRadialDistance" in self.__dict__: self.__dict__["LinkAssemblyRadialDistance"] = value; return
		self._oleobj_.Invoke(*((6012, LCID, 4, 0) + (value,) + ()))
	def _set_NumberOfTeeth(self, value):
		if "NumberOfTeeth" in self.__dict__: self.__dict__["NumberOfTeeth"] = value; return
		self._oleobj_.Invoke(*((6003, LCID, 4, 0) + (value,) + ()))
	def _set_TrackLinkLoopRadius(self, value):
		if "TrackLinkLoopRadius" in self.__dict__: self.__dict__["TrackLinkLoopRadius"] = value; return
		self._oleobj_.Invoke(*((6009, LCID, 4, 0) + (value,) + ()))
	def _set_TrackLinkPinCircleRadius(self, value):
		if "TrackLinkPinCircleRadius" in self.__dict__: self.__dict__["TrackLinkPinCircleRadius"] = value; return
		self._oleobj_.Invoke(*((6008, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkAssemblyAssembledRadius(self, value):
		if "UseLinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["UseLinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((6010, LCID, 4, 0) + (value,) + ()))

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
	Assembled distance of the link assembly.

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
	SprocketCarrierRadius = property(_get_SprocketCarrierRadius, None)
	'''
	Carrier Radius of the sprocket.

	:type: recurdyn.ProcessNet.IDouble
	'''
	SprocketCarrierWidth = property(_get_SprocketCarrierWidth, None)
	'''
	Carrier Width of the sprocket.

	:type: recurdyn.ProcessNet.IDouble
	'''
	SprocketTotalWidth = property(_get_SprocketTotalWidth, None)
	'''
	Total Width of the sprocket.

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

	_prop_map_set_function_ = {
		"_set_LinkAssemblyAssembledRadius": _set_LinkAssemblyAssembledRadius,
		"_set_LinkAssemblyRadialDistance": _set_LinkAssemblyRadialDistance,
		"_set_NumberOfTeeth": _set_NumberOfTeeth,
		"_set_TrackLinkLoopRadius": _set_TrackLinkLoopRadius,
		"_set_TrackLinkPinCircleRadius": _set_TrackLinkPinCircleRadius,
		"_set_UseLinkAssemblyAssembledRadius": _set_UseLinkAssemblyAssembledRadius,
	}
	_prop_map_get_ = {
		"AddendumCircleRadius": (6007, 2, (9, 0), (), "AddendumCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"BaseCircleRadius": (6005, 2, (9, 0), (), "BaseCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DedendumCircleRadius": (6004, 2, (9, 0), (), "DedendumCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LinkAssemblyAssembledRadius": (6011, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None),
		"LinkAssemblyRadialDistance": (6012, 2, (5, 0), (), "LinkAssemblyRadialDistance", None),
		"NumberOfTeeth": (6003, 2, (19, 0), (), "NumberOfTeeth", None),
		"PitchCircleRadius": (6006, 2, (9, 0), (), "PitchCircleRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SprocketCarrierRadius": (6000, 2, (9, 0), (), "SprocketCarrierRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SprocketCarrierWidth": (6001, 2, (9, 0), (), "SprocketCarrierWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SprocketTotalWidth": (6002, 2, (9, 0), (), "SprocketTotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TrackLinkLoopRadius": (6009, 2, (5, 0), (), "TrackLinkLoopRadius", None),
		"TrackLinkPinCircleRadius": (6008, 2, (5, 0), (), "TrackLinkPinCircleRadius", None),
		"UseLinkAssemblyAssembledRadius": (6010, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None),
	}
	_prop_map_put_ = {
		"LinkAssemblyAssembledRadius": ((6011, LCID, 4, 0),()),
		"LinkAssemblyRadialDistance": ((6012, LCID, 4, 0),()),
		"NumberOfTeeth": ((6003, LCID, 4, 0),()),
		"TrackLinkLoopRadius": ((6009, LCID, 4, 0),()),
		"TrackLinkPinCircleRadius": ((6008, LCID, 4, 0),()),
		"UseLinkAssemblyAssembledRadius": ((6010, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMGeometryWheelDouble(DispatchBaseClass):
	'''TrackHM Wheel double geometry'''
	CLSID = IID('{4ED4187A-A396-4F74-95F7-8708C083E2B7}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_HubRadius(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "HubRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_HubWidth(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "HubWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalWidth(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "TotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WheelRadius(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	HubRadius = property(_get_HubRadius, None)
	'''
	Hub radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	HubWidth = property(_get_HubWidth, None)
	'''
	Hub width

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalWidth = property(_get_TotalWidth, None)
	'''
	Total width

	:type: recurdyn.ProcessNet.IDouble
	'''
	WheelRadius = property(_get_WheelRadius, None)
	'''
	Wheel radius

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"HubRadius": (6000, 2, (9, 0), (), "HubRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"HubWidth": (6002, 2, (9, 0), (), "HubWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalWidth": (6003, 2, (9, 0), (), "TotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WheelRadius": (6001, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackHMGeometryWheelSingle(DispatchBaseClass):
	'''TrackHM Wheel single geometry'''
	CLSID = IID('{CC11A196-ED40-4A90-BAD1-EAAFD94EC7B2}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_WheelRadius(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WheelWidth(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "WheelWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	WheelRadius = property(_get_WheelRadius, None)
	'''
	Wheel Radius.

	:type: recurdyn.ProcessNet.IDouble
	'''
	WheelWidth = property(_get_WheelWidth, None)
	'''
	Wheel Width.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"WheelRadius": (6001, 2, (9, 0), (), "WheelRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WheelWidth": (6000, 2, (9, 0), (), "WheelWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class ITrackHMLinkClone(DispatchBaseClass):
	'''TrackHM link clone'''
	CLSID = IID('{AF237B87-6456-4C4F-A326-252347D5FD5C}')
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
		return self._oleobj_.InvokeTypes(6025, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(6024, LCID, 1, (24, 0), ((8, 1),),strFile
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
		return self._oleobj_.InvokeTypes(6023, LCID, 1, (24, 0), (),)


	def UpdateAssembly(self):
		'''
		Update assembly
		'''
		return self._oleobj_.InvokeTypes(6022, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(6020, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(6026, 2, (11, 0), (), "Active", None))
	def _get_ActiveDoubleShoePad(self):
		return self._ApplyTypes_(*(6001, 2, (11, 0), (), "ActiveDoubleShoePad", None))
	def _get_ActiveShoePad(self):
		return self._ApplyTypes_(*(6000, 2, (11, 0), (), "ActiveShoePad", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(6021, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(6018, 2, (5, 0), (), "Density", None))
	def _get_DoubleShoePadFirst(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_DoubleShoePadSecond(self):
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(6010, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(6013, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(6011, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(6014, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(6015, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(6012, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(6009, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(6017, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(6016, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(6019, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
	def _get_MeshSegment(self):
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ShoePadDepth(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShoePointProfile(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'))
	def _get_SingleShoePad(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((6026, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveDoubleShoePad(self, value):
		if "ActiveDoubleShoePad" in self.__dict__: self.__dict__["ActiveDoubleShoePad"] = value; return
		self._oleobj_.Invoke(*((6001, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveShoePad(self, value):
		if "ActiveShoePad" in self.__dict__: self.__dict__["ActiveShoePad"] = value; return
		self._oleobj_.Invoke(*((6000, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((6018, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((6017, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((6016, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((6019, LCID, 4, 0) + (value,) + ()))
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
	ActiveDoubleShoePad = property(_get_ActiveDoubleShoePad, _set_ActiveDoubleShoePad)
	'''
	Double shoe pad

	:type: bool
	'''
	ActiveShoePad = property(_get_ActiveShoePad, _set_ActiveShoePad)
	'''
	Active shoe pad

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
	DoubleShoePadFirst = property(_get_DoubleShoePadFirst, None)
	'''
	Double shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	DoubleShoePadSecond = property(_get_DoubleShoePadSecond, None)
	'''
	Double shoe pad second profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
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
	MeshSegment = property(_get_MeshSegment, None)
	'''
	Mesh segment

	:type: recurdyn.TrackHM.ITrackHMMeshSegment
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
	ShoePadDepth = property(_get_ShoePadDepth, None)
	'''
	Shoe pad depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShoePointProfile = property(_get_ShoePointProfile, None)
	'''
	Shoe point profile

	:type: recurdyn.TrackHM.ITrackHMProfileShoePoint
	'''
	SingleShoePad = property(_get_SingleShoePad, None)
	'''
	Single shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_ActiveDoubleShoePad": _set_ActiveDoubleShoePad,
		"_set_ActiveShoePad": _set_ActiveShoePad,
		"_set_Comment": _set_Comment,
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (6026, 2, (11, 0), (), "Active", None),
		"ActiveDoubleShoePad": (6001, 2, (11, 0), (), "ActiveDoubleShoePad", None),
		"ActiveShoePad": (6000, 2, (11, 0), (), "ActiveShoePad", None),
		"CenterMarker": (6021, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (6018, 2, (5, 0), (), "Density", None),
		"DoubleShoePadFirst": (6003, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"DoubleShoePadSecond": (6004, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (6008, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (6010, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (6013, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (6011, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (6014, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (6015, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (6012, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (6009, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (6017, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (6016, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (6019, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"MeshSegment": (6007, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ShoePadDepth": (6006, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShoePointProfile": (6005, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'),
		"SingleShoePad": (6002, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((6026, LCID, 4, 0),()),
		"ActiveDoubleShoePad": ((6001, LCID, 4, 0),()),
		"ActiveShoePad": ((6000, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((6018, LCID, 4, 0),()),
		"Material": ((6017, LCID, 4, 0),()),
		"MaterialInput": ((6016, LCID, 4, 0),()),
		"MaterialUser": ((6019, LCID, 4, 0),()),
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

class ITrackHMLinkCloneCollection(DispatchBaseClass):
	'''TrackHM clone link collection'''
	CLSID = IID('{7D040B59-3161-4160-A334-E2306674DEEF}')
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
		:rtype: recurdyn.TrackHM.ITrackHMLinkClone
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{AF237B87-6456-4C4F-A326-252347D5FD5C}')
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
		:rtype: recurdyn.TrackHM.ITrackHMLinkClone
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{AF237B87-6456-4C4F-A326-252347D5FD5C}')
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
		return win32com.client.util.Iterator(ob, '{AF237B87-6456-4C4F-A326-252347D5FD5C}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{AF237B87-6456-4C4F-A326-252347D5FD5C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITrackHMLinkCloneDouble(DispatchBaseClass):
	'''TrackHM double link clone'''
	CLSID = IID('{A55A7812-3F75-4574-A3BE-8A1AEAFA44ED}')
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
		return self._oleobj_.InvokeTypes(6025, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(6024, LCID, 1, (24, 0), ((8, 1),),strFile
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
		return self._oleobj_.InvokeTypes(6023, LCID, 1, (24, 0), (),)


	def UpdateAssembly(self):
		'''
		Update assembly
		'''
		return self._oleobj_.InvokeTypes(6022, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(6020, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(6026, 2, (11, 0), (), "Active", None))
	def _get_ActiveDoubleShoePad(self):
		return self._ApplyTypes_(*(6001, 2, (11, 0), (), "ActiveDoubleShoePad", None))
	def _get_ActiveShoePad(self):
		return self._ApplyTypes_(*(6000, 2, (11, 0), (), "ActiveShoePad", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(6021, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(6018, 2, (5, 0), (), "Density", None))
	def _get_DoubleShoePadFirst(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_DoubleShoePadSecond(self):
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(6050, 2, (9, 0), (), "Geometry", '{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(6010, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(6013, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(6011, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(6014, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(6015, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(6012, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(6009, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(6017, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(6016, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(6019, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
	def _get_MeshSegment(self):
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ShoePadDepth(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShoePointProfile(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'))
	def _get_SingleShoePad(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((6026, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveDoubleShoePad(self, value):
		if "ActiveDoubleShoePad" in self.__dict__: self.__dict__["ActiveDoubleShoePad"] = value; return
		self._oleobj_.Invoke(*((6001, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveShoePad(self, value):
		if "ActiveShoePad" in self.__dict__: self.__dict__["ActiveShoePad"] = value; return
		self._oleobj_.Invoke(*((6000, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((6018, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((6017, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((6016, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((6019, LCID, 4, 0) + (value,) + ()))
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
	ActiveDoubleShoePad = property(_get_ActiveDoubleShoePad, _set_ActiveDoubleShoePad)
	'''
	Double shoe pad

	:type: bool
	'''
	ActiveShoePad = property(_get_ActiveShoePad, _set_ActiveShoePad)
	'''
	Active shoe pad

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
	DoubleShoePadFirst = property(_get_DoubleShoePadFirst, None)
	'''
	Double shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	DoubleShoePadSecond = property(_get_DoubleShoePadSecond, None)
	'''
	Double shoe pad second profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.TrackHM.ITrackHMGeometryLinkDouble
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
	MeshSegment = property(_get_MeshSegment, None)
	'''
	Mesh segment

	:type: recurdyn.TrackHM.ITrackHMMeshSegment
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
	ShoePadDepth = property(_get_ShoePadDepth, None)
	'''
	Shoe pad depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShoePointProfile = property(_get_ShoePointProfile, None)
	'''
	Shoe point profile

	:type: recurdyn.TrackHM.ITrackHMProfileShoePoint
	'''
	SingleShoePad = property(_get_SingleShoePad, None)
	'''
	Single shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_ActiveDoubleShoePad": _set_ActiveDoubleShoePad,
		"_set_ActiveShoePad": _set_ActiveShoePad,
		"_set_Comment": _set_Comment,
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (6026, 2, (11, 0), (), "Active", None),
		"ActiveDoubleShoePad": (6001, 2, (11, 0), (), "ActiveDoubleShoePad", None),
		"ActiveShoePad": (6000, 2, (11, 0), (), "ActiveShoePad", None),
		"CenterMarker": (6021, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (6018, 2, (5, 0), (), "Density", None),
		"DoubleShoePadFirst": (6003, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"DoubleShoePadSecond": (6004, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (6050, 2, (9, 0), (), "Geometry", '{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}'),
		"Graphic": (6008, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (6010, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (6013, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (6011, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (6014, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (6015, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (6012, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (6009, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (6017, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (6016, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (6019, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"MeshSegment": (6007, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ShoePadDepth": (6006, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShoePointProfile": (6005, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'),
		"SingleShoePad": (6002, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((6026, LCID, 4, 0),()),
		"ActiveDoubleShoePad": ((6001, LCID, 4, 0),()),
		"ActiveShoePad": ((6000, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((6018, LCID, 4, 0),()),
		"Material": ((6017, LCID, 4, 0),()),
		"MaterialInput": ((6016, LCID, 4, 0),()),
		"MaterialUser": ((6019, LCID, 4, 0),()),
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

class ITrackHMLinkCloneInner(DispatchBaseClass):
	'''TrackHM inner link clone'''
	CLSID = IID('{CB28018E-6D3A-42E5-B010-517C09143DF1}')
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
		return self._oleobj_.InvokeTypes(6025, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(6024, LCID, 1, (24, 0), ((8, 1),),strFile
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
		return self._oleobj_.InvokeTypes(6023, LCID, 1, (24, 0), (),)


	def UpdateAssembly(self):
		'''
		Update assembly
		'''
		return self._oleobj_.InvokeTypes(6022, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(6020, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(6026, 2, (11, 0), (), "Active", None))
	def _get_ActiveDoubleShoePad(self):
		return self._ApplyTypes_(*(6001, 2, (11, 0), (), "ActiveDoubleShoePad", None))
	def _get_ActiveShoePad(self):
		return self._ApplyTypes_(*(6000, 2, (11, 0), (), "ActiveShoePad", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(6021, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(6018, 2, (5, 0), (), "Density", None))
	def _get_DoubleShoePadFirst(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_DoubleShoePadSecond(self):
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(6051, 2, (9, 0), (), "Geometry", '{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(6010, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(6013, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(6011, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(6014, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(6015, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(6012, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(6009, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(6017, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(6016, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(6019, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
	def _get_MeshSegment(self):
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ShoePadDepth(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShoePointProfile(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'))
	def _get_SingleShoePad(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((6026, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveDoubleShoePad(self, value):
		if "ActiveDoubleShoePad" in self.__dict__: self.__dict__["ActiveDoubleShoePad"] = value; return
		self._oleobj_.Invoke(*((6001, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveShoePad(self, value):
		if "ActiveShoePad" in self.__dict__: self.__dict__["ActiveShoePad"] = value; return
		self._oleobj_.Invoke(*((6000, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((6018, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((6017, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((6016, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((6019, LCID, 4, 0) + (value,) + ()))
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
	ActiveDoubleShoePad = property(_get_ActiveDoubleShoePad, _set_ActiveDoubleShoePad)
	'''
	Double shoe pad

	:type: bool
	'''
	ActiveShoePad = property(_get_ActiveShoePad, _set_ActiveShoePad)
	'''
	Active shoe pad

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
	DoubleShoePadFirst = property(_get_DoubleShoePadFirst, None)
	'''
	Double shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	DoubleShoePadSecond = property(_get_DoubleShoePadSecond, None)
	'''
	Double shoe pad second profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.TrackHM.ITrackHMGeometryLinkInner
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
	MeshSegment = property(_get_MeshSegment, None)
	'''
	Mesh segment

	:type: recurdyn.TrackHM.ITrackHMMeshSegment
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
	ShoePadDepth = property(_get_ShoePadDepth, None)
	'''
	Shoe pad depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShoePointProfile = property(_get_ShoePointProfile, None)
	'''
	Shoe point profile

	:type: recurdyn.TrackHM.ITrackHMProfileShoePoint
	'''
	SingleShoePad = property(_get_SingleShoePad, None)
	'''
	Single shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_ActiveDoubleShoePad": _set_ActiveDoubleShoePad,
		"_set_ActiveShoePad": _set_ActiveShoePad,
		"_set_Comment": _set_Comment,
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (6026, 2, (11, 0), (), "Active", None),
		"ActiveDoubleShoePad": (6001, 2, (11, 0), (), "ActiveDoubleShoePad", None),
		"ActiveShoePad": (6000, 2, (11, 0), (), "ActiveShoePad", None),
		"CenterMarker": (6021, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (6018, 2, (5, 0), (), "Density", None),
		"DoubleShoePadFirst": (6003, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"DoubleShoePadSecond": (6004, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (6051, 2, (9, 0), (), "Geometry", '{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}'),
		"Graphic": (6008, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (6010, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (6013, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (6011, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (6014, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (6015, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (6012, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (6009, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (6017, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (6016, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (6019, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"MeshSegment": (6007, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ShoePadDepth": (6006, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShoePointProfile": (6005, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'),
		"SingleShoePad": (6002, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((6026, LCID, 4, 0),()),
		"ActiveDoubleShoePad": ((6001, LCID, 4, 0),()),
		"ActiveShoePad": ((6000, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((6018, LCID, 4, 0),()),
		"Material": ((6017, LCID, 4, 0),()),
		"MaterialInput": ((6016, LCID, 4, 0),()),
		"MaterialUser": ((6019, LCID, 4, 0),()),
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

class ITrackHMLinkCloneSingle(DispatchBaseClass):
	'''TrackHM single link clone'''
	CLSID = IID('{6C21457B-6BA1-48FE-AF34-8AB45CCC4E05}')
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
		return self._oleobj_.InvokeTypes(6025, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(6024, LCID, 1, (24, 0), ((8, 1),),strFile
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
		return self._oleobj_.InvokeTypes(6023, LCID, 1, (24, 0), (),)


	def UpdateAssembly(self):
		'''
		Update assembly
		'''
		return self._oleobj_.InvokeTypes(6022, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(6020, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(6026, 2, (11, 0), (), "Active", None))
	def _get_ActiveDoubleShoePad(self):
		return self._ApplyTypes_(*(6001, 2, (11, 0), (), "ActiveDoubleShoePad", None))
	def _get_ActiveShoePad(self):
		return self._ApplyTypes_(*(6000, 2, (11, 0), (), "ActiveShoePad", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(6021, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(6018, 2, (5, 0), (), "Density", None))
	def _get_DoubleShoePadFirst(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_DoubleShoePadSecond(self):
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(6051, 2, (9, 0), (), "Geometry", '{0CDCA31B-C017-4528-8B11-4CE8D5E60525}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(6008, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(6010, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(6013, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(6011, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(6014, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(6015, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(6012, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(6009, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(6017, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(6016, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(6019, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
	def _get_MeshSegment(self):
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ShoePadDepth(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShoePointProfile(self):
		return self._ApplyTypes_(*(6005, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'))
	def _get_SingleShoePad(self):
		return self._ApplyTypes_(*(6002, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((6026, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveDoubleShoePad(self, value):
		if "ActiveDoubleShoePad" in self.__dict__: self.__dict__["ActiveDoubleShoePad"] = value; return
		self._oleobj_.Invoke(*((6001, LCID, 4, 0) + (value,) + ()))
	def _set_ActiveShoePad(self, value):
		if "ActiveShoePad" in self.__dict__: self.__dict__["ActiveShoePad"] = value; return
		self._oleobj_.Invoke(*((6000, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((6018, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((6017, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((6016, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((6019, LCID, 4, 0) + (value,) + ()))
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
	ActiveDoubleShoePad = property(_get_ActiveDoubleShoePad, _set_ActiveDoubleShoePad)
	'''
	Double shoe pad

	:type: bool
	'''
	ActiveShoePad = property(_get_ActiveShoePad, _set_ActiveShoePad)
	'''
	Active shoe pad

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
	DoubleShoePadFirst = property(_get_DoubleShoePadFirst, None)
	'''
	Double shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	DoubleShoePadSecond = property(_get_DoubleShoePadSecond, None)
	'''
	Double shoe pad second profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.TrackHM.ITrackHMGeometryLinkSingle
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
	MeshSegment = property(_get_MeshSegment, None)
	'''
	Mesh segment

	:type: recurdyn.TrackHM.ITrackHMMeshSegment
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
	ShoePadDepth = property(_get_ShoePadDepth, None)
	'''
	Shoe pad depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShoePointProfile = property(_get_ShoePointProfile, None)
	'''
	Shoe point profile

	:type: recurdyn.TrackHM.ITrackHMProfileShoePoint
	'''
	SingleShoePad = property(_get_SingleShoePad, None)
	'''
	Single shoe pad first profile

	:type: recurdyn.TrackHM.ITrackHMShoePad
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_ActiveDoubleShoePad": _set_ActiveDoubleShoePad,
		"_set_ActiveShoePad": _set_ActiveShoePad,
		"_set_Comment": _set_Comment,
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (6026, 2, (11, 0), (), "Active", None),
		"ActiveDoubleShoePad": (6001, 2, (11, 0), (), "ActiveDoubleShoePad", None),
		"ActiveShoePad": (6000, 2, (11, 0), (), "ActiveShoePad", None),
		"CenterMarker": (6021, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (6018, 2, (5, 0), (), "Density", None),
		"DoubleShoePadFirst": (6003, 2, (9, 0), (), "DoubleShoePadFirst", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"DoubleShoePadSecond": (6004, 2, (9, 0), (), "DoubleShoePadSecond", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (6051, 2, (9, 0), (), "Geometry", '{0CDCA31B-C017-4528-8B11-4CE8D5E60525}'),
		"Graphic": (6008, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (6010, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (6013, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (6011, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (6014, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (6015, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (6012, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (6009, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (6017, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (6016, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (6019, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"MeshSegment": (6007, 2, (9, 0), (), "MeshSegment", '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ShoePadDepth": (6006, 2, (9, 0), (), "ShoePadDepth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShoePointProfile": (6005, 2, (9, 0), (), "ShoePointProfile", '{9BAE7474-F445-492C-8C6C-8959B10F51E3}'),
		"SingleShoePad": (6002, 2, (9, 0), (), "SingleShoePad", '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((6026, LCID, 4, 0),()),
		"ActiveDoubleShoePad": ((6001, LCID, 4, 0),()),
		"ActiveShoePad": ((6000, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((6018, LCID, 4, 0),()),
		"Material": ((6017, LCID, 4, 0),()),
		"MaterialInput": ((6016, LCID, 4, 0),()),
		"MaterialUser": ((6019, LCID, 4, 0),()),
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

class ITrackHMMeshSegment(DispatchBaseClass):
	'''TrackHM mesh segment'''
	CLSID = IID('{B06854C8-C58D-4BC2-9761-36B0D92DFA68}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ShoePadMeshHeightSegment(self):
		return self._ApplyTypes_(*(6002, 2, (19, 0), (), "ShoePadMeshHeightSegment", None))
	def _get_ShoePadMeshLengthSegment(self):
		return self._ApplyTypes_(*(6001, 2, (19, 0), (), "ShoePadMeshLengthSegment", None))
	def _get_ShoePadMeshWidthSegment(self):
		return self._ApplyTypes_(*(6000, 2, (19, 0), (), "ShoePadMeshWidthSegment", None))

	def _set_ShoePadMeshHeightSegment(self, value):
		if "ShoePadMeshHeightSegment" in self.__dict__: self.__dict__["ShoePadMeshHeightSegment"] = value; return
		self._oleobj_.Invoke(*((6002, LCID, 4, 0) + (value,) + ()))
	def _set_ShoePadMeshLengthSegment(self, value):
		if "ShoePadMeshLengthSegment" in self.__dict__: self.__dict__["ShoePadMeshLengthSegment"] = value; return
		self._oleobj_.Invoke(*((6001, LCID, 4, 0) + (value,) + ()))
	def _set_ShoePadMeshWidthSegment(self, value):
		if "ShoePadMeshWidthSegment" in self.__dict__: self.__dict__["ShoePadMeshWidthSegment"] = value; return
		self._oleobj_.Invoke(*((6000, LCID, 4, 0) + (value,) + ()))

	ShoePadMeshHeightSegment = property(_get_ShoePadMeshHeightSegment, _set_ShoePadMeshHeightSegment)
	'''
	Shoe pad height mesh segment

	:type: int
	'''
	ShoePadMeshLengthSegment = property(_get_ShoePadMeshLengthSegment, _set_ShoePadMeshLengthSegment)
	'''
	Shoe pad length mesh segment

	:type: int
	'''
	ShoePadMeshWidthSegment = property(_get_ShoePadMeshWidthSegment, _set_ShoePadMeshWidthSegment)
	'''
	Shoe pad width mesh segment

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_ShoePadMeshHeightSegment": _set_ShoePadMeshHeightSegment,
		"_set_ShoePadMeshLengthSegment": _set_ShoePadMeshLengthSegment,
		"_set_ShoePadMeshWidthSegment": _set_ShoePadMeshWidthSegment,
	}
	_prop_map_get_ = {
		"ShoePadMeshHeightSegment": (6002, 2, (19, 0), (), "ShoePadMeshHeightSegment", None),
		"ShoePadMeshLengthSegment": (6001, 2, (19, 0), (), "ShoePadMeshLengthSegment", None),
		"ShoePadMeshWidthSegment": (6000, 2, (19, 0), (), "ShoePadMeshWidthSegment", None),
	}
	_prop_map_put_ = {
		"ShoePadMeshHeightSegment": ((6002, LCID, 4, 0),()),
		"ShoePadMeshLengthSegment": ((6001, LCID, 4, 0),()),
		"ShoePadMeshWidthSegment": ((6000, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMProfileShoePoint(DispatchBaseClass):
	'''TrackHM link clone'''
	CLSID = IID('{9BAE7474-F445-492C-8C6C-8959B10F51E3}')
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
		Export shoe point
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(6002, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def Import(self, strFileName):
		'''
		Import shoe point
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(6001, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def _get_Point3DCollection(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "Point3DCollection", '{7AAA986F-35DD-4DCF-843A-CEBA8E09D33A}'))

	Point3DCollection = property(_get_Point3DCollection, None)
	'''
	3D Point Collection

	:type: recurdyn.ProcessNet.IPoint3DCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Point3DCollection": (6000, 2, (9, 0), (), "Point3DCollection", '{7AAA986F-35DD-4DCF-843A-CEBA8E09D33A}'),
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

class ITrackHMShoePad(DispatchBaseClass):
	'''TrackHM link clone'''
	CLSID = IID('{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_FirstPoint(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "FirstPoint", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'))
	def _get_SecondPoint(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "SecondPoint", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'))

	FirstPoint = property(_get_FirstPoint, None)
	'''
	First position

	:type: recurdyn.ProcessNet.IPoint3D
	'''
	SecondPoint = property(_get_SecondPoint, None)
	'''
	Second position

	:type: recurdyn.ProcessNet.IPoint3D
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"FirstPoint": (6000, 2, (9, 0), (), "FirstPoint", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'),
		"SecondPoint": (6001, 2, (9, 0), (), "SecondPoint", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'),
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

class ITrackHMSphereContactProperty(DispatchBaseClass):
	'''TrackHM sphere contact property'''
	CLSID = IID('{2248B1F9-1F1B-4D82-8B54-FAA47938AC38}')
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
		return self._ApplyTypes_(*(6004, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(6013, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(6006, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(6007, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(6009, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(6016, 2, (3, 0), (), "FrictionType", '{A9359E38-2F8C-46C9-9283-366B8FB02465}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(6015, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(6001, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(6011, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(6003, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(6012, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(6005, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseFrictionSpline(self):
		return self._ApplyTypes_(*(6008, 2, (11, 0), (), "UseFrictionSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(6014, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(6010, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(6002, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((6006, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((6009, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((6016, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((6003, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((6012, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((6005, LCID, 4, 0) + (value,) + ()))
	def _set_UseFrictionSpline(self, value):
		if "UseFrictionSpline" in self.__dict__: self.__dict__["UseFrictionSpline"] = value; return
		self._oleobj_.Invoke(*((6008, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((6014, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((6010, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((6002, LCID, 4, 0) + (value,) + ()))

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

	:type: recurdyn.TrackHM.TrackHMFrictionType
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
		"DampingCoefficient": (6004, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (6013, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (6006, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionCoefficient": (6007, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (6009, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (6016, 2, (3, 0), (), "FrictionType", '{A9359E38-2F8C-46C9-9283-366B8FB02465}'),
		"IndentationExponent": (6015, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (6001, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (6011, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (6003, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (6012, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (6005, 2, (11, 0), (), "UseDampingSpline", None),
		"UseFrictionSpline": (6008, 2, (11, 0), (), "UseFrictionSpline", None),
		"UseIndentationExponent": (6014, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseStiffnessExponent": (6010, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (6002, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"DampingSpline": ((6006, LCID, 4, 0),()),
		"FrictionSpline": ((6009, LCID, 4, 0),()),
		"FrictionType": ((6016, LCID, 4, 0),()),
		"StiffnessSpline": ((6003, LCID, 4, 0),()),
		"UseDampingExponent": ((6012, LCID, 4, 0),()),
		"UseDampingSpline": ((6005, LCID, 4, 0),()),
		"UseFrictionSpline": ((6008, LCID, 4, 0),()),
		"UseIndentationExponent": ((6014, LCID, 4, 0),()),
		"UseStiffnessExponent": ((6010, LCID, 4, 0),()),
		"UseStiffnessSpline": ((6002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITrackHMSubSystem(DispatchBaseClass):
	'''TrackHM subsystem'''
	CLSID = IID('{F42978E2-A470-4CC5-8BC1-06B2E4A54236}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateBodySprocket(self, strName, pPoint):
		'''
		Create a body sprocket
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackHM.ITrackHMBodySprocket
		'''
		ret = self._oleobj_.InvokeTypes(6001, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodySprocket', '{4F847ED1-32A7-4A6F-9E0C-D0ECE3833FE2}')
		return ret

	def CreateBodyWheelDouble(self, strName, pPoint):
		'''
		Create a single double
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackHM.ITrackHMBodyWheelDouble
		'''
		ret = self._oleobj_.InvokeTypes(6003, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyWheelDouble', '{F271147D-2B1A-460F-841D-8743839E155D}')
		return ret

	def CreateBodyWheelSingle(self, strName, pPoint):
		'''
		Create a single wheel
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackHM.ITrackHMBodyWheelSingle
		'''
		ret = self._oleobj_.InvokeTypes(6002, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyWheelSingle', '{93C13C52-83EC-4438-AEDD-D41A1EC42FF6}')
		return ret

	def CreateContactTrackToSurface(self, strName, pAssembly, pSurface):
		'''
		Create track assembly to surface contact
		
		:param strName: str
		:param pAssembly: IGeneric
		:param pSurface: IGeneric
		:rtype: recurdyn.ToolkitCommon.IContactTrackToSurface
		'''
		ret = self._oleobj_.InvokeTypes(6022, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pAssembly, pSurface)
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
		ret = self._oleobj_.InvokeTypes(6021, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
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
		ret = self._oleobj_.InvokeTypes(6018, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
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
		ret = self._oleobj_.InvokeTypes(6019, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
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
		ret = self._oleobj_.InvokeTypes(6020, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pBaseRefFrame, pActionRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorSpring', '{93A5A572-A6DD-4F12-A3E5-64F95B78718F}')
		return ret

	def CreateLinkCloneDouble(self, strName, pPoint):
		'''
		Create a track double link 
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackHM.ITrackHMLinkCloneDouble
		'''
		ret = self._oleobj_.InvokeTypes(6008, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLinkCloneDouble', '{A55A7812-3F75-4574-A3BE-8A1AEAFA44ED}')
		return ret

	def CreateLinkCloneInner(self, strName, pPoint):
		'''
		Create a track inner link 
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackHM.ITrackHMLinkCloneInner
		'''
		ret = self._oleobj_.InvokeTypes(6009, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLinkCloneInner', '{CB28018E-6D3A-42E5-B010-517C09143DF1}')
		return ret

	def CreateLinkCloneSingle(self, strName, pPoint):
		'''
		Create a track single link 
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.TrackHM.ITrackHMLinkCloneSingle
		'''
		ret = self._oleobj_.InvokeTypes(6007, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLinkCloneSingle', '{6C21457B-6BA1-48FE-AF34-8AB45CCC4E05}')
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
		ret = self._oleobj_.InvokeTypes(6016, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (5, 1)),strName
			, pEntity, pSensorMarker, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorDisplacement', '{08F5AF0B-ADB1-4AB4-8FAB-54ADCB9B5F36}')
		return ret

	def CreateTrackAssembly(self, strName, pLinkClone, pBodyList, pInOutList, uiNumberOfLink):
		'''
		Create track assembly
		
		:param strName: str
		:param pLinkClone: ITrackHMLinkClone
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfLink: int
		:rtype: recurdyn.TrackHM.ITrackHMAssembly
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(6010, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (19, 1)),strName
			, pLinkClone, pBodyList, pInOutList, uiNumberOfLink)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateTrackAssembly', '{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')
		return ret

	def CreateTrackAssemblyWithAutomaticSprocketAlignment(self, strName, pLinkClone, pBodyList, pInOutList, uiNumberOfLink):
		'''
		Create track assembly
		
		:param strName: str
		:param pLinkClone: ITrackHMLinkClone
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param uiNumberOfLink: int
		:rtype: recurdyn.TrackHM.ITrackHMAssembly
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(6023, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (19, 1)),strName
			, pLinkClone, pBodyList, pInOutList, uiNumberOfLink)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateTrackAssemblyWithAutomaticSprocketAlignment', '{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_AssemblyCollection(self):
		return self._ApplyTypes_(*(6014, 2, (9, 0), (), "AssemblyCollection", '{12BBA5CC-DA01-4B3A-91DB-404C904569BD}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_LinkCloneCollection(self):
		return self._ApplyTypes_(*(6011, 2, (9, 0), (), "LinkCloneCollection", '{7D040B59-3161-4160-A334-E2306674DEEF}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_TrackHMBodyCollection(self):
		return self._ApplyTypes_(*(6015, 2, (9, 0), (), "TrackHMBodyCollection", '{413B7957-9529-476C-932A-19CE19F9C013}'))
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

	:type: recurdyn.TrackHM.ITrackHMAssemblyCollection
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

	:type: recurdyn.TrackHM.ITrackHMLinkCloneCollection
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
	TrackHMBodyCollection = property(_get_TrackHMBodyCollection, None)
	'''
	Get the TrackHM body collection of assembly

	:type: recurdyn.TrackHM.ITrackHMBodyCollection
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
		"AssemblyCollection": (6014, 2, (9, 0), (), "AssemblyCollection", '{12BBA5CC-DA01-4B3A-91DB-404C904569BD}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralSubSystem": (6000, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"LinkCloneCollection": (6011, 2, (9, 0), (), "LinkCloneCollection", '{7D040B59-3161-4160-A334-E2306674DEEF}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"TrackHMBodyCollection": (6015, 2, (9, 0), (), "TrackHMBodyCollection", '{413B7957-9529-476C-932A-19CE19F9C013}'),
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

class ITrackHMToothProfileSprocket(DispatchBaseClass):
	'''TrackHMToothProfileSprocket'''
	CLSID = IID('{6049C1CF-A437-4579-BEA1-F7C3C016EF83}')
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
		return self._oleobj_.InvokeTypes(6001, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(6002, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_PointCollection(self):
		return self._ApplyTypes_(*(6000, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	PointCollection = property(_get_PointCollection, None)
	'''
	Point Collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PointCollection": (6000, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
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

ITrackHMAssembly_vtables_dispatch_ = 1
ITrackHMAssembly_vtables_ = [
	(( 'UsePressureSinkage' , 'pVal' , ), 6000, (6000, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UsePressureSinkage' , 'pVal' , ), 6000, (6000, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameter' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{6E69D3B7-8017-427A-A4CE-B654E20AC0B6}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PassingBodyCollection' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{E26794CD-5D37-4617-BB5A-1AD85F3ED410}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody' , 'pVal' , ), 6003, (6003, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody' , 'pVal' , ), 6004, (6004, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SphereContact' , 'ppVal' , ), 6005, (6005, (), [ (16393, 10, None, "IID('{6EBF0639-993D-437D-80AA-8372352B7281}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LinkNumbers' , 'pVal' , ), 6006, (6006, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LinkInitialVelocityXAxis' , 'ppVal' , ), 6007, (6007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'TrackHMBodyLinkCollection' , 'ppVal' , ), 6008, (6008, (), [ (16393, 10, None, "IID('{F592F48A-ED83-4179-982F-13D4F1E9AA40}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BushingForceParameter' , 'ppVal' , ), 6009, (6009, (), [ (16393, 10, None, "IID('{5D558264-0B36-4A12-8D70-8A2BA7315F32}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetOutputLinkList' , 'ppSafeArray' , ), 6010, (6010, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'AddOutputLink' , 'strFileName' , ), 6011, (6011, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputLink' , 'strFileName' , ), 6012, (6012, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'AddAllOutputLink' , ), 6013, (6013, (), [ ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RemoveAllOutputLink' , ), 6014, (6014, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'BushingForceCollection' , 'ppVal' , ), 6020, (6020, (), [ (16393, 10, None, "IID('{B1359BD3-DD1C-4A0C-A16D-466CC9B0B4F5}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UpdateLinkInitialVelocity' , ), 6021, (6021, (), [ ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkInitialVelocityXAxis' , 'pVal' , ), 6022, (6022, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkInitialVelocityXAxis' , 'pVal' , ), 6022, (6022, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkInitialVelocityReferenceFrame' , 'pVal' , ), 6023, (6023, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkInitialVelocityReferenceFrame' , 'pVal' , ), 6023, (6023, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'LinkInitialVelocityReferenceFrame' , ), 6024, (6024, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody2' , 'pVal' , ), 6025, (6025, (), [ (9, 1, None, "IID('{4D568C44-E3AF-4517-B410-CA913214F421}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody2' , 'pVal' , ), 6026, (6026, (), [ (9, 1, None, "IID('{4D568C44-E3AF-4517-B410-CA913214F421}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

ITrackHMAssemblyBushingForceParameter_vtables_dispatch_ = 1
ITrackHMAssemblyBushingForceParameter_vtables_ = [
	(( 'TranslationStiffnessCoefficientRadial' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessCoefficientAxial' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessSpline' , 'pVal' , ), 6002, (6002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessSpline' , 'pVal' , ), 6002, (6002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineRadial' , 'ppVal' , ), 6003, (6003, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineRadial' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineAxial' , 'ppVal' , ), 6004, (6004, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineAxial' , 'ppVal' , ), 6004, (6004, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingCoefficientRadial' , 'ppVal' , ), 6005, (6005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingCoefficientAxial' , 'ppVal' , ), 6006, (6006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingSpline' , 'pVal' , ), 6007, (6007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingSpline' , 'pVal' , ), 6007, (6007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineRadial' , 'ppVal' , ), 6008, (6008, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineRadial' , 'ppVal' , ), 6008, (6008, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineAxial' , 'ppVal' , ), 6009, (6009, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineAxial' , 'ppVal' , ), 6009, (6009, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TranslationPreloadRadial' , 'ppVal' , ), 6010, (6010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'TranslationPreloadAxial' , 'ppVal' , ), 6011, (6011, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TranslationClearance' , 'ppVal' , ), 6012, (6012, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessCoefficientX' , 'ppVal' , ), 6013, (6013, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessCoefficientY' , 'ppVal' , ), 6014, (6014, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessCoefficientZ' , 'ppVal' , ), 6015, (6015, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessSpline' , 'pVal' , ), 6016, (6016, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessSpline' , 'pVal' , ), 6016, (6016, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineX' , 'ppVal' , ), 6017, (6017, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineX' , 'ppVal' , ), 6017, (6017, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineY' , 'ppVal' , ), 6018, (6018, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineY' , 'ppVal' , ), 6018, (6018, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineZ' , 'ppVal' , ), 6019, (6019, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineZ' , 'ppVal' , ), 6019, (6019, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingCoefficientX' , 'ppVal' , ), 6020, (6020, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingCoefficientY' , 'ppVal' , ), 6021, (6021, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingCoefficientZ' , 'ppVal' , ), 6022, (6022, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingSpline' , 'pVal' , ), 6023, (6023, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingSpline' , 'pVal' , ), 6023, (6023, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineX' , 'ppVal' , ), 6024, (6024, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineX' , 'ppVal' , ), 6024, (6024, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineY' , 'ppVal' , ), 6025, (6025, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineY' , 'ppVal' , ), 6025, (6025, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineZ' , 'ppVal' , ), 6026, (6026, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineZ' , 'ppVal' , ), 6026, (6026, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RotationPreloadX' , 'ppVal' , ), 6027, (6027, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'RotationPreloadY' , 'ppVal' , ), 6028, (6028, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'RotationPreloadZ' , 'ppVal' , ), 6029, (6029, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'RotationPresetAngle' , 'ppVal' , ), 6030, (6030, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStopAngle' , 'pVal' , ), 6031, (6031, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStopAngle' , 'pVal' , ), 6031, (6031, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'RotationStopAngle' , 'ppVal' , ), 6032, (6032, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'RotationStopStiffnessFactor' , 'ppVal' , ), 6033, (6033, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 6034, (6034, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 6034, (6034, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessExponentRadial' , 'ppVal' , ), 6035, (6035, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessExponentAxial' , 'ppVal' , ), 6036, (6036, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 6037, (6037, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 6037, (6037, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingExponentRadial' , 'ppVal' , ), 6038, (6038, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingExponentAxial' , 'ppVal' , ), 6039, (6039, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 6040, (6040, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 6040, (6040, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponentX' , 'ppVal' , ), 6041, (6041, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponentY' , 'ppVal' , ), 6042, (6042, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponentZ' , 'ppVal' , ), 6043, (6043, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 6044, (6044, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 6044, (6044, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponentX' , 'ppVal' , ), 6045, (6045, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponentY' , 'ppVal' , ), 6046, (6046, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponentZ' , 'ppVal' , ), 6047, (6047, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 6048, (6048, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 6049, (6049, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
]

ITrackHMAssemblyCollection_vtables_dispatch_ = 1
ITrackHMAssemblyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITrackHMAssemblyContactGroundTrackLinkShoePad_vtables_dispatch_ = 1
ITrackHMAssemblyContactGroundTrackLinkShoePad_vtables_ = [
	(( 'UseLateralFrictionFactor' , 'pVal' , ), 6050, (6050, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseLateralFrictionFactor' , 'pVal' , ), 6050, (6050, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'LateralFrictionFactor' , 'ppVal' , ), 6051, (6051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveGroundParameter' , 'pVal' , ), 6052, (6052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveGroundParameter' , 'pVal' , ), 6052, (6052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'SoftGroundType' , 'val' , ), 6053, (6053, (), [ (3, 1, None, "IID('{9778678C-1CAF-4393-AC21-3FAF6B966328}')") , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'TerrainStiffnessKc' , 'ppVal' , ), 6054, (6054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'TerrainStiffnessKphi' , 'ppVal' , ), 6055, (6055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ExponentialNumber' , 'ppVal' , ), 6056, (6056, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Cohesion' , 'ppVal' , ), 6057, (6057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'ShearingResistanceAngle' , 'ppVal' , ), 6058, (6058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'ShearingDeformationModulus' , 'ppVal' , ), 6059, (6059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'SinkageRatio' , 'ppVal' , ), 6060, (6060, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveSoftGroundParameter' , 'pVal' , ), 6061, (6061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveSoftGroundParameter' , 'pVal' , ), 6061, (6061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 6062, (6062, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 6063, (6063, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseUserSubroutine' , 'pVal' , ), 6064, (6064, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UseUserSubroutine' , 'pVal' , ), 6064, (6064, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'pVal' , ), 6065, (6065, (), [ (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'pVal' , ), 6065, (6065, (), [ (16393, 10, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
]

ITrackHMAssemblySphereContact_vtables_dispatch_ = 1
ITrackHMAssemblySphereContact_vtables_ = [
	(( 'MaximumPenetration' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ContactProperty' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2248B1F9-1F1B-4D82-8B54-FAA47938AC38}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AddSphereContact' , 'pGeometrySphere' , ), 6002, (6002, (), [ (9, 1, None, "IID('{2122DEE7-EE07-4A20-9B49-5A9AF4599906}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GeometrySphereCollection' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{0B006D28-70E2-4FBA-8A03-EC9EFC17C4E1}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ITrackHMBody_vtables_dispatch_ = 1
ITrackHMBody_vtables_ = [
	(( 'GeneralBody' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

ITrackHMBodyCollection_vtables_dispatch_ = 1
ITrackHMBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{4D568C44-E3AF-4517-B410-CA913214F421}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITrackHMBodyLink_vtables_dispatch_ = 1
ITrackHMBodyLink_vtables_ = [
	(( 'ActiveShoePad' , 'pVal' , ), 6050, (6050, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ActiveShoePad' , 'pVal' , ), 6050, (6050, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ActiveDoubleShoePad' , 'pVal' , ), 6051, (6051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ActiveDoubleShoePad' , 'pVal' , ), 6051, (6051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SingleShoePad' , 'ppVal' , ), 6052, (6052, (), [ (16393, 10, None, "IID('{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DoubleShoePadFirst' , 'ppVal' , ), 6053, (6053, (), [ (16393, 10, None, "IID('{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DoubleShoePadSecond' , 'ppVal' , ), 6054, (6054, (), [ (16393, 10, None, "IID('{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ShoePointProfile' , 'pVal' , ), 6055, (6055, (), [ (16393, 10, None, "IID('{9BAE7474-F445-492C-8C6C-8959B10F51E3}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ShoePadDepth' , 'ppVal' , ), 6056, (6056, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'MeshSegment' , 'pVal' , ), 6057, (6057, (), [ (16393, 10, None, "IID('{B06854C8-C58D-4BC2-9761-36B0D92DFA68}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 6058, (6058, (), [ ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAssembly' , ), 6059, (6059, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseBodyGraphic' , 'pVal' , ), 6060, (6060, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseBodyGraphic' , 'pVal' , ), 6060, (6060, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 6061, (6061, (), [ (16393, 10, None, "IID('{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CreateMarker' , 'strName' , 'pRefFrame' , 'ppVal' , ), 6062, (6062, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

ITrackHMBodyLinkCollection_vtables_dispatch_ = 1
ITrackHMBodyLinkCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{710B4E1D-5E36-4439-ABFE-7D566EAAA31D}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITrackHMBodyLinkDouble_vtables_dispatch_ = 1
ITrackHMBodyLinkDouble_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 6101, (6101, (), [ (16393, 10, None, "IID('{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

ITrackHMBodyLinkInner_vtables_dispatch_ = 1
ITrackHMBodyLinkInner_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 6101, (6101, (), [ (16393, 10, None, "IID('{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

ITrackHMBodyLinkSingle_vtables_dispatch_ = 1
ITrackHMBodyLinkSingle_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 6101, (6101, (), [ (16393, 10, None, "IID('{0CDCA31B-C017-4528-8B11-4CE8D5E60525}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

ITrackHMBodySprocket_vtables_dispatch_ = 1
ITrackHMBodySprocket_vtables_ = [
	(( 'ContactProperty' , 'ppContactProperty' , ), 6050, (6050, (), [ (16393, 10, None, "IID('{045DD783-342A-40C7-8743-C1EE4A708B7D}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppGeometry' , ), 6051, (6051, (), [ (16393, 10, None, "IID('{9341322D-E9F4-41D4-B866-B97D1E1E773E}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ToothProfile' , 'ppToothProfile' , ), 6052, (6052, (), [ (16393, 10, None, "IID('{6049C1CF-A437-4579-BEA1-F7C3C016EF83}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 6053, (6053, (), [ (16393, 10, None, "IID('{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UpdateProperties' , ), 6055, (6055, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactOutputFile' , 'pVal' , ), 6056, (6056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactOutputFile' , 'pVal' , ), 6056, (6056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ITrackHMBodyWheelDouble_vtables_dispatch_ = 1
ITrackHMBodyWheelDouble_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 6050, (6050, (), [ (16393, 10, None, "IID('{045DD783-342A-40C7-8743-C1EE4A708B7D}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ContactCenterProperty' , 'ppVal' , ), 6051, (6051, (), [ (16393, 10, None, "IID('{045DD783-342A-40C7-8743-C1EE4A708B7D}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 6052, (6052, (), [ (16393, 10, None, "IID('{4ED4187A-A396-4F74-95F7-8708C083E2B7}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 6053, (6053, (), [ (16393, 10, None, "IID('{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

ITrackHMBodyWheelSingle_vtables_dispatch_ = 1
ITrackHMBodyWheelSingle_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 6050, (6050, (), [ (16393, 10, None, "IID('{045DD783-342A-40C7-8743-C1EE4A708B7D}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 6051, (6051, (), [ (16393, 10, None, "IID('{CC11A196-ED40-4A90-BAD1-EAAFD94EC7B2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 6052, (6052, (), [ (16393, 10, None, "IID('{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

ITrackHMContactFriction_vtables_dispatch_ = 1
ITrackHMContactFriction_vtables_ = [
	(( 'StaticThresholdVelocity' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DynamicThresholdVelocity' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StaticFrictionCoefficient' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ITrackHMContactProperty_vtables_dispatch_ = 1
ITrackHMContactProperty_vtables_ = [
	(( 'StiffnessCoefficient' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 6001, (6001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 6001, (6001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 6002, (6002, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 6004, (6004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 6004, (6004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 6005, (6005, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 6005, (6005, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 6006, (6006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 6007, (6007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 6007, (6007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 6008, (6008, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 6008, (6008, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 6009, (6009, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 6009, (6009, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 6010, (6010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 6011, (6011, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 6011, (6011, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 6012, (6012, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 6013, (6013, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 6013, (6013, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 6014, (6014, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseMoreFrictionData' , 'pVal' , ), 6015, (6015, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseMoreFrictionData' , 'pVal' , ), 6015, (6015, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Friction' , 'ppVal' , ), 6016, (6016, (), [ (16393, 10, None, "IID('{839109C1-0AE4-4D08-BF2C-329740CBC436}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 6017, (6017, (), [ (3, 1, None, "IID('{A9359E38-2F8C-46C9-9283-366B8FB02465}')") , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 6017, (6017, (), [ (16387, 10, None, "IID('{A9359E38-2F8C-46C9-9283-366B8FB02465}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

ITrackHMContactSearch_vtables_dispatch_ = 1
ITrackHMContactSearch_vtables_ = [
	(( 'Type' , 'pVal' , ), 6000, (6000, (), [ (3, 1, None, "IID('{7DADC137-519B-4F3E-B1FB-6AA19C0555B5}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 6000, (6000, (), [ (16387, 10, None, "IID('{7DADC137-519B-4F3E-B1FB-6AA19C0555B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseUserBoundaryForPartialSearch' , 'pVal' , ), 6001, (6001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseUserBoundaryForPartialSearch' , 'pVal' , ), 6001, (6001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UserBoundaryForPartialSearch' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

ITrackHMGeometryLinkDouble_vtables_dispatch_ = 1
ITrackHMGeometryLinkDouble_vtables_ = [
	(( 'LeftLength' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RightLength' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UpperHeight' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LowerHeight' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 6004, (6004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'EndConnectorLength' , 'ppVal' , ), 6005, (6005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 6006, (6006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PinRadius' , 'ppVal' , ), 6007, (6007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuideLength' , 'ppVal' , ), 6008, (6008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuideThickness' , 'ppVal' , ), 6009, (6009, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LeftPinPosition' , 'pPoint' , ), 6010, (6010, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LeftPinPosition' , 'pPoint' , ), 6010, (6010, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'RightPinPosition' , 'pPoint' , ), 6011, (6011, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'RightPinPosition' , 'pPoint' , ), 6011, (6011, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuidePosition' , 'pPoint' , ), 6012, (6012, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuidePosition' , 'pPoint' , ), 6012, (6012, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

ITrackHMGeometryLinkInner_vtables_dispatch_ = 1
ITrackHMGeometryLinkInner_vtables_ = [
	(( 'LeftLength' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RightLength' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UpperHeight' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LowerHeight' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 6004, (6004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'LinkWidth' , 'ppVal' , ), 6005, (6005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'InnerWidth' , 'ppVal' , ), 6006, (6006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'OuterWidth' , 'ppVal' , ), 6007, (6007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'LeftPinPosition' , 'pPoint' , ), 6008, (6008, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'LeftPinPosition' , 'pPoint' , ), 6008, (6008, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'RightPinPosition' , 'pPoint' , ), 6009, (6009, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'RightPinPosition' , 'pPoint' , ), 6009, (6009, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PinRadius' , 'ppVal' , ), 6010, (6010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuidePosition' , 'pPoint' , ), 6011, (6011, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuidePosition' , 'pPoint' , ), 6011, (6011, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuideLength' , 'ppVal' , ), 6012, (6012, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuideThickness' , 'ppVal' , ), 6013, (6013, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'LeftContactCylinderPosition' , 'pPoint' , ), 6014, (6014, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LeftContactCylinderPosition' , 'pPoint' , ), 6014, (6014, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RightContactCylinderPosition' , 'pPoint' , ), 6015, (6015, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RightContactCylinderPosition' , 'pPoint' , ), 6015, (6015, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ContactRadius' , 'ppVal' , ), 6016, (6016, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ShoeRadius' , 'ppVal' , ), 6017, (6017, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'EndConnectorLength' , 'ppVal' , ), 6018, (6018, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

ITrackHMGeometryLinkSingle_vtables_dispatch_ = 1
ITrackHMGeometryLinkSingle_vtables_ = [
	(( 'LeftLength' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RightLength' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UpperHeight' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LowerHeight' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'ppVal' , ), 6004, (6004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ConnectorLength' , 'ppVal' , ), 6005, (6005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 6006, (6006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PinRadius' , 'ppVal' , ), 6007, (6007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuideLength' , 'ppVal' , ), 6008, (6008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuideThickness' , 'ppVal' , ), 6009, (6009, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LeftPinPosition' , 'pPoint' , ), 6010, (6010, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LeftPinPosition' , 'pPoint' , ), 6010, (6010, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'RightPinPosition' , 'pPoint' , ), 6011, (6011, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'RightPinPosition' , 'pPoint' , ), 6011, (6011, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuidePosition' , 'pPoint' , ), 6012, (6012, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CenterGuidePosition' , 'pPoint' , ), 6012, (6012, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 6013, (6013, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 6013, (6013, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pPoint' , ), 6014, (6014, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pPoint' , ), 6014, (6014, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pPoint' , ), 6015, (6015, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pPoint' , ), 6015, (6015, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 6016, (6016, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 6016, (6016, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

ITrackHMGeometrySprocket_vtables_dispatch_ = 1
ITrackHMGeometrySprocket_vtables_ = [
	(( 'SprocketCarrierRadius' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SprocketCarrierWidth' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SprocketTotalWidth' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfTeeth' , 'pVal' , ), 6003, (6003, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfTeeth' , 'pVal' , ), 6003, (6003, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DedendumCircleRadius' , 'ppVal' , ), 6004, (6004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'BaseCircleRadius' , 'ppVal' , ), 6005, (6005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PitchCircleRadius' , 'ppVal' , ), 6006, (6006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AddendumCircleRadius' , 'ppVal' , ), 6007, (6007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TrackLinkPinCircleRadius' , 'pVal' , ), 6008, (6008, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TrackLinkPinCircleRadius' , 'pVal' , ), 6008, (6008, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TrackLinkLoopRadius' , 'pVal' , ), 6009, (6009, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TrackLinkLoopRadius' , 'pVal' , ), 6009, (6009, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkAssemblyAssembledRadius' , 'pVal' , ), 6010, (6010, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkAssemblyAssembledRadius' , 'pVal' , ), 6010, (6010, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyAssembledRadius' , 'pVal' , ), 6011, (6011, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyAssembledRadius' , 'pVal' , ), 6011, (6011, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyRadialDistance' , 'pVal' , ), 6012, (6012, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyRadialDistance' , 'pVal' , ), 6012, (6012, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

ITrackHMGeometryWheelDouble_vtables_dispatch_ = 1
ITrackHMGeometryWheelDouble_vtables_ = [
	(( 'HubRadius' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'WheelRadius' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'HubWidth' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TotalWidth' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ITrackHMGeometryWheelSingle_vtables_dispatch_ = 1
ITrackHMGeometryWheelSingle_vtables_ = [
	(( 'WheelWidth' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'WheelRadius' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ITrackHMLinkClone_vtables_dispatch_ = 1
ITrackHMLinkClone_vtables_ = [
	(( 'ActiveShoePad' , 'pVal' , ), 6000, (6000, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ActiveShoePad' , 'pVal' , ), 6000, (6000, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ActiveDoubleShoePad' , 'pVal' , ), 6001, (6001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ActiveDoubleShoePad' , 'pVal' , ), 6001, (6001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SingleShoePad' , 'ppVal' , ), 6002, (6002, (), [ (16393, 10, None, "IID('{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DoubleShoePadFirst' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'DoubleShoePadSecond' , 'ppVal' , ), 6004, (6004, (), [ (16393, 10, None, "IID('{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ShoePointProfile' , 'pVal' , ), 6005, (6005, (), [ (16393, 10, None, "IID('{9BAE7474-F445-492C-8C6C-8959B10F51E3}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ShoePadDepth' , 'ppVal' , ), 6006, (6006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'MeshSegment' , 'pVal' , ), 6007, (6007, (), [ (16393, 10, None, "IID('{B06854C8-C58D-4BC2-9761-36B0D92DFA68}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 6008, (6008, (), [ (16393, 10, None, "IID('{4C8B7C23-7D92-4D39-B530-5D93DC97F771}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 6009, (6009, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'ppVal' , ), 6010, (6010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'ppVal' , ), 6011, (6011, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'ppVal' , ), 6012, (6012, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Ixy' , 'ppVal' , ), 6013, (6013, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Iyz' , 'ppVal' , ), 6014, (6014, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Izx' , 'ppVal' , ), 6015, (6015, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'MaterialInput' , 'pVal' , ), 6016, (6016, (), [ (3, 1, None, "IID('{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}')") , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'MaterialInput' , 'pVal' , ), 6016, (6016, (), [ (16387, 10, None, "IID('{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'pVal' , ), 6017, (6017, (), [ (3, 1, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'pVal' , ), 6017, (6017, (), [ (16387, 10, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 6018, (6018, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 6018, (6018, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'MaterialUser' , 'pVal' , ), 6019, (6019, (), [ (9, 1, None, "IID('{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'MaterialUser' , 'pVal' , ), 6019, (6019, (), [ (16393, 10, None, "IID('{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 6020, (6020, (), [ ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'CenterMarker' , 'pVal' , ), 6021, (6021, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UpdateAssembly' , ), 6022, (6022, (), [ ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'InitialBodyGraphicFlag' , ), 6023, (6023, (), [ ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'FileImport' , 'strFile' , ), 6024, (6024, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'FileExport' , 'strFile' , 'OverWrite' , ), 6025, (6025, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 6026, (6026, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 6026, (6026, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
]

ITrackHMLinkCloneCollection_vtables_dispatch_ = 1
ITrackHMLinkCloneCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{AF237B87-6456-4C4F-A326-252347D5FD5C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITrackHMLinkCloneDouble_vtables_dispatch_ = 1
ITrackHMLinkCloneDouble_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 6050, (6050, (), [ (16393, 10, None, "IID('{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
]

ITrackHMLinkCloneInner_vtables_dispatch_ = 1
ITrackHMLinkCloneInner_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 6051, (6051, (), [ (16393, 10, None, "IID('{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
]

ITrackHMLinkCloneSingle_vtables_dispatch_ = 1
ITrackHMLinkCloneSingle_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 6051, (6051, (), [ (16393, 10, None, "IID('{0CDCA31B-C017-4528-8B11-4CE8D5E60525}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
]

ITrackHMMeshSegment_vtables_dispatch_ = 1
ITrackHMMeshSegment_vtables_ = [
	(( 'ShoePadMeshWidthSegment' , 'pVal' , ), 6000, (6000, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ShoePadMeshWidthSegment' , 'pVal' , ), 6000, (6000, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ShoePadMeshLengthSegment' , 'pVal' , ), 6001, (6001, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ShoePadMeshLengthSegment' , 'pVal' , ), 6001, (6001, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ShoePadMeshHeightSegment' , 'pVal' , ), 6002, (6002, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ShoePadMeshHeightSegment' , 'pVal' , ), 6002, (6002, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

ITrackHMProfileShoePoint_vtables_dispatch_ = 1
ITrackHMProfileShoePoint_vtables_ = [
	(( 'Point3DCollection' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{7AAA986F-35DD-4DCF-843A-CEBA8E09D33A}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strFileName' , ), 6001, (6001, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strFileName' , ), 6002, (6002, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

ITrackHMShoePad_vtables_dispatch_ = 1
ITrackHMShoePad_vtables_ = [
	(( 'FirstPoint' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SecondPoint' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

ITrackHMSphereContactProperty_vtables_dispatch_ = 1
ITrackHMSphereContactProperty_vtables_ = [
	(( 'StiffnessCoefficient' , 'ppVal' , ), 6001, (6001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 6002, (6002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 6002, (6002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 6003, (6003, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 6003, (6003, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 6004, (6004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 6005, (6005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 6005, (6005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 6006, (6006, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 6006, (6006, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 6007, (6007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 6008, (6008, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 6008, (6008, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 6009, (6009, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 6009, (6009, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 6010, (6010, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 6010, (6010, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 6011, (6011, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 6012, (6012, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 6012, (6012, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 6013, (6013, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 6014, (6014, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 6014, (6014, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 6015, (6015, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 6016, (6016, (), [ (3, 1, None, "IID('{A9359E38-2F8C-46C9-9283-366B8FB02465}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 6016, (6016, (), [ (16387, 10, None, "IID('{A9359E38-2F8C-46C9-9283-366B8FB02465}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

ITrackHMSubSystem_vtables_dispatch_ = 1
ITrackHMSubSystem_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodySprocket' , 'strName' , 'pPoint' , 'ppResult' , ), 6001, (6001, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{4F847ED1-32A7-4A6F-9E0C-D0ECE3833FE2}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyWheelSingle' , 'strName' , 'pPoint' , 'ppResult' , ), 6002, (6002, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{93C13C52-83EC-4438-AEDD-D41A1EC42FF6}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyWheelDouble' , 'strName' , 'pPoint' , 'ppResult' , ), 6003, (6003, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{F271147D-2B1A-460F-841D-8743839E155D}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateLinkCloneSingle' , 'strName' , 'pPoint' , 'ppResult' , ), 6007, (6007, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{6C21457B-6BA1-48FE-AF34-8AB45CCC4E05}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateLinkCloneDouble' , 'strName' , 'pPoint' , 'ppResult' , ), 6008, (6008, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{A55A7812-3F75-4574-A3BE-8A1AEAFA44ED}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateLinkCloneInner' , 'strName' , 'pPoint' , 'ppResult' , ), 6009, (6009, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{CB28018E-6D3A-42E5-B010-517C09143DF1}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateTrackAssembly' , 'strName' , 'pLinkClone' , 'pBodyList' , 'pInOutList' , 
			 'uiNumberOfLink' , 'ppResult' , ), 6010, (6010, (), [ (8, 1, None, None) , (9, 1, None, "IID('{AF237B87-6456-4C4F-A326-252347D5FD5C}')") , 
			 (8204, 1, None, None) , (8204, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LinkCloneCollection' , 'ppVal' , ), 6011, (6011, (), [ (16393, 10, None, "IID('{7D040B59-3161-4160-A334-E2306674DEEF}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'AssemblyCollection' , 'ppVal' , ), 6014, (6014, (), [ (16393, 10, None, "IID('{12BBA5CC-DA01-4B3A-91DB-404C904569BD}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'TrackHMBodyCollection' , 'ppVal' , ), 6015, (6015, (), [ (16393, 10, None, "IID('{413B7957-9529-476C-932A-19CE19F9C013}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorDisplacement' , 'strName' , 'pEntity' , 'pSensorMarker' , 'dRange' , 
			 'ppVal' , ), 6016, (6016, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{08F5AF0B-ADB1-4AB4-8FAB-54ADCB9B5F36}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorFixed' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 6018, (6018, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{39059D2F-DBEC-49DD-BFF2-AC0185541C99}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorRevolute' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 6019, (6019, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{D24BBA28-623F-4F1C-97D5-021413EB6736}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorSpring' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pBaseRefFrame' , 
			 'pActionRefFrame' , 'ppResult' , ), 6020, (6020, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{93A5A572-A6DD-4F12-A3E5-64F95B78718F}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorBushing' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 6021, (6021, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{F5A169B5-B529-4935-8B06-ACDD2A0BA456}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CreateContactTrackToSurface' , 'strName' , 'pAssembly' , 'pSurface' , 'ppResult' , 
			 ), 6022, (6022, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (16393, 10, None, "IID('{1EAD15B7-3DFF-40FD-BD77-12CBB9F2CA6C}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'CreateTrackAssemblyWithAutomaticSprocketAlignment' , 'strName' , 'pLinkClone' , 'pBodyList' , 'pInOutList' , 
			 'uiNumberOfLink' , 'ppResult' , ), 6023, (6023, (), [ (8, 1, None, None) , (9, 1, None, "IID('{AF237B87-6456-4C4F-A326-252347D5FD5C}')") , 
			 (8204, 1, None, None) , (8204, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{A8407D80-98E2-4F09-987F-8E8088FC7BE7}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

ITrackHMToothProfileSprocket_vtables_dispatch_ = 1
ITrackHMToothProfileSprocket_vtables_ = [
	(( 'PointCollection' , 'ppVal' , ), 6000, (6000, (), [ (16393, 10, None, "IID('{2C0D70A3-D197-4781-940A-1672F3B420B9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 6001, (6001, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 6002, (6002, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{839109C1-0AE4-4D08-BF2C-329740CBC436}' : ITrackHMContactFriction,
	'{045DD783-342A-40C7-8743-C1EE4A708B7D}' : ITrackHMContactProperty,
	'{CC11A196-ED40-4A90-BAD1-EAAFD94EC7B2}' : ITrackHMGeometryWheelSingle,
	'{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}' : ITrackHMContactSearch,
	'{4D568C44-E3AF-4517-B410-CA913214F421}' : ITrackHMBody,
	'{413B7957-9529-476C-932A-19CE19F9C013}' : ITrackHMBodyCollection,
	'{9BAE7474-F445-492C-8C6C-8959B10F51E3}' : ITrackHMProfileShoePoint,
	'{B06854C8-C58D-4BC2-9761-36B0D92DFA68}' : ITrackHMMeshSegment,
	'{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}' : ITrackHMShoePad,
	'{710B4E1D-5E36-4439-ABFE-7D566EAAA31D}' : ITrackHMBodyLink,
	'{93C13C52-83EC-4438-AEDD-D41A1EC42FF6}' : ITrackHMBodyWheelSingle,
	'{4ED4187A-A396-4F74-95F7-8708C083E2B7}' : ITrackHMGeometryWheelDouble,
	'{F271147D-2B1A-460F-841D-8743839E155D}' : ITrackHMBodyWheelDouble,
	'{9341322D-E9F4-41D4-B866-B97D1E1E773E}' : ITrackHMGeometrySprocket,
	'{6049C1CF-A437-4579-BEA1-F7C3C016EF83}' : ITrackHMToothProfileSprocket,
	'{4F847ED1-32A7-4A6F-9E0C-D0ECE3833FE2}' : ITrackHMBodySprocket,
	'{0CDCA31B-C017-4528-8B11-4CE8D5E60525}' : ITrackHMGeometryLinkSingle,
	'{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}' : ITrackHMGeometryLinkDouble,
	'{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}' : ITrackHMGeometryLinkInner,
	'{A97F123D-9445-453A-A688-FD06CCEF9B94}' : ITrackHMBodyLinkSingle,
	'{DEB4AA5A-2136-4E21-A20F-C00373893AD4}' : ITrackHMBodyLinkDouble,
	'{F56F4B69-951E-4FD8-9770-3B45734FB048}' : ITrackHMBodyLinkInner,
	'{F592F48A-ED83-4179-982F-13D4F1E9AA40}' : ITrackHMBodyLinkCollection,
	'{AF237B87-6456-4C4F-A326-252347D5FD5C}' : ITrackHMLinkClone,
	'{6C21457B-6BA1-48FE-AF34-8AB45CCC4E05}' : ITrackHMLinkCloneSingle,
	'{A55A7812-3F75-4574-A3BE-8A1AEAFA44ED}' : ITrackHMLinkCloneDouble,
	'{CB28018E-6D3A-42E5-B010-517C09143DF1}' : ITrackHMLinkCloneInner,
	'{7D040B59-3161-4160-A334-E2306674DEEF}' : ITrackHMLinkCloneCollection,
	'{A8407D80-98E2-4F09-987F-8E8088FC7BE7}' : ITrackHMAssembly,
	'{6E69D3B7-8017-427A-A4CE-B654E20AC0B6}' : ITrackHMAssemblyContactGroundTrackLinkShoePad,
	'{6EBF0639-993D-437D-80AA-8372352B7281}' : ITrackHMAssemblySphereContact,
	'{2248B1F9-1F1B-4D82-8B54-FAA47938AC38}' : ITrackHMSphereContactProperty,
	'{5D558264-0B36-4A12-8D70-8A2BA7315F32}' : ITrackHMAssemblyBushingForceParameter,
	'{12BBA5CC-DA01-4B3A-91DB-404C904569BD}' : ITrackHMAssemblyCollection,
	'{F42978E2-A470-4CC5-8BC1-06B2E4A54236}' : ITrackHMSubSystem,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{839109C1-0AE4-4D08-BF2C-329740CBC436}' : 'ITrackHMContactFriction',
	'{045DD783-342A-40C7-8743-C1EE4A708B7D}' : 'ITrackHMContactProperty',
	'{CC11A196-ED40-4A90-BAD1-EAAFD94EC7B2}' : 'ITrackHMGeometryWheelSingle',
	'{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}' : 'ITrackHMContactSearch',
	'{4D568C44-E3AF-4517-B410-CA913214F421}' : 'ITrackHMBody',
	'{413B7957-9529-476C-932A-19CE19F9C013}' : 'ITrackHMBodyCollection',
	'{9BAE7474-F445-492C-8C6C-8959B10F51E3}' : 'ITrackHMProfileShoePoint',
	'{B06854C8-C58D-4BC2-9761-36B0D92DFA68}' : 'ITrackHMMeshSegment',
	'{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}' : 'ITrackHMShoePad',
	'{710B4E1D-5E36-4439-ABFE-7D566EAAA31D}' : 'ITrackHMBodyLink',
	'{93C13C52-83EC-4438-AEDD-D41A1EC42FF6}' : 'ITrackHMBodyWheelSingle',
	'{4ED4187A-A396-4F74-95F7-8708C083E2B7}' : 'ITrackHMGeometryWheelDouble',
	'{F271147D-2B1A-460F-841D-8743839E155D}' : 'ITrackHMBodyWheelDouble',
	'{9341322D-E9F4-41D4-B866-B97D1E1E773E}' : 'ITrackHMGeometrySprocket',
	'{6049C1CF-A437-4579-BEA1-F7C3C016EF83}' : 'ITrackHMToothProfileSprocket',
	'{4F847ED1-32A7-4A6F-9E0C-D0ECE3833FE2}' : 'ITrackHMBodySprocket',
	'{0CDCA31B-C017-4528-8B11-4CE8D5E60525}' : 'ITrackHMGeometryLinkSingle',
	'{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}' : 'ITrackHMGeometryLinkDouble',
	'{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}' : 'ITrackHMGeometryLinkInner',
	'{A97F123D-9445-453A-A688-FD06CCEF9B94}' : 'ITrackHMBodyLinkSingle',
	'{DEB4AA5A-2136-4E21-A20F-C00373893AD4}' : 'ITrackHMBodyLinkDouble',
	'{F56F4B69-951E-4FD8-9770-3B45734FB048}' : 'ITrackHMBodyLinkInner',
	'{F592F48A-ED83-4179-982F-13D4F1E9AA40}' : 'ITrackHMBodyLinkCollection',
	'{AF237B87-6456-4C4F-A326-252347D5FD5C}' : 'ITrackHMLinkClone',
	'{6C21457B-6BA1-48FE-AF34-8AB45CCC4E05}' : 'ITrackHMLinkCloneSingle',
	'{A55A7812-3F75-4574-A3BE-8A1AEAFA44ED}' : 'ITrackHMLinkCloneDouble',
	'{CB28018E-6D3A-42E5-B010-517C09143DF1}' : 'ITrackHMLinkCloneInner',
	'{7D040B59-3161-4160-A334-E2306674DEEF}' : 'ITrackHMLinkCloneCollection',
	'{A8407D80-98E2-4F09-987F-8E8088FC7BE7}' : 'ITrackHMAssembly',
	'{6E69D3B7-8017-427A-A4CE-B654E20AC0B6}' : 'ITrackHMAssemblyContactGroundTrackLinkShoePad',
	'{6EBF0639-993D-437D-80AA-8372352B7281}' : 'ITrackHMAssemblySphereContact',
	'{2248B1F9-1F1B-4D82-8B54-FAA47938AC38}' : 'ITrackHMSphereContactProperty',
	'{5D558264-0B36-4A12-8D70-8A2BA7315F32}' : 'ITrackHMAssemblyBushingForceParameter',
	'{12BBA5CC-DA01-4B3A-91DB-404C904569BD}' : 'ITrackHMAssemblyCollection',
	'{F42978E2-A470-4CC5-8BC1-06B2E4A54236}' : 'ITrackHMSubSystem',
}


NamesToIIDMap = {
	'ITrackHMContactFriction' : '{839109C1-0AE4-4D08-BF2C-329740CBC436}',
	'ITrackHMContactProperty' : '{045DD783-342A-40C7-8743-C1EE4A708B7D}',
	'ITrackHMGeometryWheelSingle' : '{CC11A196-ED40-4A90-BAD1-EAAFD94EC7B2}',
	'ITrackHMContactSearch' : '{D9C49633-AC0E-4CC8-A20F-A547AA0DD849}',
	'ITrackHMBody' : '{4D568C44-E3AF-4517-B410-CA913214F421}',
	'ITrackHMBodyCollection' : '{413B7957-9529-476C-932A-19CE19F9C013}',
	'ITrackHMProfileShoePoint' : '{9BAE7474-F445-492C-8C6C-8959B10F51E3}',
	'ITrackHMMeshSegment' : '{B06854C8-C58D-4BC2-9761-36B0D92DFA68}',
	'ITrackHMShoePad' : '{8D48DBC4-F2C4-41DA-B0B0-4E3A6B5A4F56}',
	'ITrackHMBodyLink' : '{710B4E1D-5E36-4439-ABFE-7D566EAAA31D}',
	'ITrackHMBodyWheelSingle' : '{93C13C52-83EC-4438-AEDD-D41A1EC42FF6}',
	'ITrackHMGeometryWheelDouble' : '{4ED4187A-A396-4F74-95F7-8708C083E2B7}',
	'ITrackHMBodyWheelDouble' : '{F271147D-2B1A-460F-841D-8743839E155D}',
	'ITrackHMGeometrySprocket' : '{9341322D-E9F4-41D4-B866-B97D1E1E773E}',
	'ITrackHMToothProfileSprocket' : '{6049C1CF-A437-4579-BEA1-F7C3C016EF83}',
	'ITrackHMBodySprocket' : '{4F847ED1-32A7-4A6F-9E0C-D0ECE3833FE2}',
	'ITrackHMGeometryLinkSingle' : '{0CDCA31B-C017-4528-8B11-4CE8D5E60525}',
	'ITrackHMGeometryLinkDouble' : '{65D7A1BF-95C1-43E7-93FA-40AB03BF8C80}',
	'ITrackHMGeometryLinkInner' : '{CCD96F99-89A3-4F5E-8F20-E9BFDEEAC965}',
	'ITrackHMBodyLinkSingle' : '{A97F123D-9445-453A-A688-FD06CCEF9B94}',
	'ITrackHMBodyLinkDouble' : '{DEB4AA5A-2136-4E21-A20F-C00373893AD4}',
	'ITrackHMBodyLinkInner' : '{F56F4B69-951E-4FD8-9770-3B45734FB048}',
	'ITrackHMBodyLinkCollection' : '{F592F48A-ED83-4179-982F-13D4F1E9AA40}',
	'ITrackHMLinkClone' : '{AF237B87-6456-4C4F-A326-252347D5FD5C}',
	'ITrackHMLinkCloneSingle' : '{6C21457B-6BA1-48FE-AF34-8AB45CCC4E05}',
	'ITrackHMLinkCloneDouble' : '{A55A7812-3F75-4574-A3BE-8A1AEAFA44ED}',
	'ITrackHMLinkCloneInner' : '{CB28018E-6D3A-42E5-B010-517C09143DF1}',
	'ITrackHMLinkCloneCollection' : '{7D040B59-3161-4160-A334-E2306674DEEF}',
	'ITrackHMAssembly' : '{A8407D80-98E2-4F09-987F-8E8088FC7BE7}',
	'ITrackHMAssemblyContactGroundTrackLinkShoePad' : '{6E69D3B7-8017-427A-A4CE-B654E20AC0B6}',
	'ITrackHMAssemblySphereContact' : '{6EBF0639-993D-437D-80AA-8372352B7281}',
	'ITrackHMSphereContactProperty' : '{2248B1F9-1F1B-4D82-8B54-FAA47938AC38}',
	'ITrackHMAssemblyBushingForceParameter' : '{5D558264-0B36-4A12-8D70-8A2BA7315F32}',
	'ITrackHMAssemblyCollection' : '{12BBA5CC-DA01-4B3A-91DB-404C904569BD}',
	'ITrackHMSubSystem' : '{F42978E2-A470-4CC5-8BC1-06B2E4A54236}',
}


