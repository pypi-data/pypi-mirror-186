# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMToolkitCommon.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5 RecurDynCOMToolkitCommon Type Library'
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

CLSID = IID('{8A430389-1D81-4189-8AA7-55DEC914FAD1}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class ToolkitSoftGroundType(IntEnum):
	'''
	ToolkitSoftGroundType enumeration.
	'''
	ToolkitSoftGroundType_Clayey_Soil=4         
	'''Constant value is 4.'''
	ToolkitSoftGroundType_Dry_Sand=0         
	'''Constant value is 0.'''
	ToolkitSoftGroundType_Grenville_Loam=11        
	'''Constant value is 11.'''
	ToolkitSoftGroundType_Heavy_Clay=5         
	'''Constant value is 5.'''
	ToolkitSoftGroundType_LETE_Sand=7         
	'''Constant value is 7.'''
	ToolkitSoftGroundType_Lean_Clay=6         
	'''Constant value is 6.'''
	ToolkitSoftGroundType_North_Gower_Clayey_Loam=10        
	'''Constant value is 10.'''
	ToolkitSoftGroundType_Rubicon_Sandy_Loam=9         
	'''Constant value is 9.'''
	ToolkitSoftGroundType_Sandy_Loam_Hanamoto=3         
	'''Constant value is 3.'''
	ToolkitSoftGroundType_Sandy_Loam_LLL=1         
	'''Constant value is 1.'''
	ToolkitSoftGroundType_Sandy_Loam_Michigan=2         
	'''Constant value is 2.'''
	ToolkitSoftGroundType_Snow_Sweden=13        
	'''Constant value is 13.'''
	ToolkitSoftGroundType_Snow_US =12        
	'''Constant value is 12.'''
	ToolkitSoftGroundType_Upland_Sandy_Loam=8         
	'''Constant value is 8.'''
class TrackFrictionType(IntEnum):
	'''
	TrackFrictionType enumeration.
	'''
	TrackFrictionType_DynamicFrictionCoefficient=0         
	'''Constant value is 0.'''
	TrackFrictionType_FrictionCoefficientSpline=2         
	'''Constant value is 2.'''
	TrackFrictionType_FrictionForceSpline=1         
	'''Constant value is 1.'''

from win32com.client import DispatchBaseClass
class IContactTrackToSurface(DispatchBaseClass):
	'''Track to surface contact'''
	CLSID = IID('{1EAD15B7-3DFF-40FD-BD77-12CBB9F2CA6C}')
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
		return self._ApplyTypes_(*(7006, 2, (9, 0), (), "ActionEntity", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'))
	def _get_ActionPatchOption(self):
		return self._ApplyTypes_(*(7004, 2, (9, 0), (), "ActionPatchOption", '{D479C190-172F-42AC-A4B9-5B3AFE1EB81B}'))
	def _get_ActionUpDirection(self):
		return self._ApplyTypes_(*(7003, 2, (11, 0), (), "ActionUpDirection", None))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseEntity(self):
		return self._ApplyTypes_(*(7005, 2, (9, 0), (), "BaseEntity", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactParameter(self):
		return self._ApplyTypes_(*(7002, 2, (9, 0), (), "ContactParameter", '{EBF27DFC-CCEC-401F-A201-00E6B5758270}'))
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
	def _get_UseActionNodeContact(self):
		return self._ApplyTypes_(*(7007, 2, (11, 0), (), "UseActionNodeContact", None))
	def _get_UsePressureSinkage(self):
		return self._ApplyTypes_(*(7001, 2, (11, 0), (), "UsePressureSinkage", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionEntity(self, value):
		if "ActionEntity" in self.__dict__: self.__dict__["ActionEntity"] = value; return
		self._oleobj_.Invoke(*((7006, LCID, 4, 0) + (value,) + ()))
	def _set_ActionUpDirection(self, value):
		if "ActionUpDirection" in self.__dict__: self.__dict__["ActionUpDirection"] = value; return
		self._oleobj_.Invoke(*((7003, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseEntity(self, value):
		if "BaseEntity" in self.__dict__: self.__dict__["BaseEntity"] = value; return
		self._oleobj_.Invoke(*((7005, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseActionNodeContact(self, value):
		if "UseActionNodeContact" in self.__dict__: self.__dict__["UseActionNodeContact"] = value; return
		self._oleobj_.Invoke(*((7007, LCID, 4, 0) + (value,) + ()))
	def _set_UsePressureSinkage(self, value):
		if "UsePressureSinkage" in self.__dict__: self.__dict__["UsePressureSinkage"] = value; return
		self._oleobj_.Invoke(*((7001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionEntity = property(_get_ActionEntity, _set_ActionEntity)
	'''
	Action entity

	:type: recurdyn.ProcessNet.IGeometry
	'''
	ActionPatchOption = property(_get_ActionPatchOption, None)
	'''
	Solid contact action patch option

	:type: recurdyn.ProcessNet.IContactSolidPatchOption
	'''
	ActionUpDirection = property(_get_ActionUpDirection, _set_ActionUpDirection)
	'''
	Action up direction

	:type: bool
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
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactParameter = property(_get_ContactParameter, None)
	'''
	Contact parameter

	:type: recurdyn.ToolkitCommon.IContactTrackToSurfaceProperty
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
	UseActionNodeContact = property(_get_UseActionNodeContact, _set_UseActionNodeContact)
	'''
	Use Action Node Contact

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
		"_set_ActionEntity": _set_ActionEntity,
		"_set_ActionUpDirection": _set_ActionUpDirection,
		"_set_Active": _set_Active,
		"_set_BaseEntity": _set_BaseEntity,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseActionNodeContact": _set_UseActionNodeContact,
		"_set_UsePressureSinkage": _set_UsePressureSinkage,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionEntity": (7006, 2, (9, 0), (), "ActionEntity", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'),
		"ActionPatchOption": (7004, 2, (9, 0), (), "ActionPatchOption", '{D479C190-172F-42AC-A4B9-5B3AFE1EB81B}'),
		"ActionUpDirection": (7003, 2, (11, 0), (), "ActionUpDirection", None),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseEntity": (7005, 2, (9, 0), (), "BaseEntity", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactParameter": (7002, 2, (9, 0), (), "ContactParameter", '{EBF27DFC-CCEC-401F-A201-00E6B5758270}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseActionNodeContact": (7007, 2, (11, 0), (), "UseActionNodeContact", None),
		"UsePressureSinkage": (7001, 2, (11, 0), (), "UsePressureSinkage", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionEntity": ((7006, LCID, 4, 0),()),
		"ActionUpDirection": ((7003, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseEntity": ((7005, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseActionNodeContact": ((7007, LCID, 4, 0),()),
		"UsePressureSinkage": ((7001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IContactTrackToSurfaceProperty(DispatchBaseClass):
	'''Track assembly to surface contact property'''
	CLSID = IID('{EBF27DFC-CCEC-401F-A201-00E6B5758270}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Export(self, strName, Val):
		'''
		Export is obsolete function
		
		:param strName: str
		:param Val: bool
		'''
		return self._oleobj_.InvokeTypes(7012, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, Val)


	def Import(self, strName):
		'''
		Import is obsolete function
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(7013, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def SoftGroundType(self, Val):
		'''
		Soft ground type
		
		:param Val: TrackHMContactParameterSoftGroundType
		'''
		return self._oleobj_.InvokeTypes(7003, LCID, 1, (24, 0), ((3, 1),),Val
			)


	def _get_Cohesion(self):
		return self._ApplyTypes_(*(7007, 2, (9, 0), (), "Cohesion", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(7019, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(7028, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(7021, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_ExponentialNumber(self):
		return self._ApplyTypes_(*(7006, 2, (9, 0), (), "ExponentialNumber", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(7032, 2, (9, 0), (), "Friction", '{28A3BBB4-DF34-4A57-9527-048B76671247}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(7022, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(7024, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(7033, 2, (3, 0), (), "FrictionType", '{66A716E9-F39F-4CB2-94E9-034EDE35D487}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(7030, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LateralFrictionFactor(self):
		return self._ApplyTypes_(*(7001, 2, (9, 0), (), "LateralFrictionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaxPenetration(self):
		return self._ApplyTypes_(*(7035, 2, (9, 0), (), "MaxPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearingDeformationModulus(self):
		return self._ApplyTypes_(*(7009, 2, (9, 0), (), "ShearingDeformationModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearingResistanceAngle(self):
		return self._ApplyTypes_(*(7008, 2, (9, 0), (), "ShearingResistanceAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SinkageRatio(self):
		return self._ApplyTypes_(*(7010, 2, (9, 0), (), "SinkageRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(7016, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(7026, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(7018, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TerrainStiffnessKc(self):
		return self._ApplyTypes_(*(7004, 2, (9, 0), (), "TerrainStiffnessKc", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TerrainStiffnessKphi(self):
		return self._ApplyTypes_(*(7005, 2, (9, 0), (), "TerrainStiffnessKphi", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(7027, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(7020, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseFrictionSpline(self):
		return self._ApplyTypes_(*(7023, 2, (11, 0), (), "UseFrictionSpline", None))
	def _get_UseInactiveGroundParameter(self):
		return self._ApplyTypes_(*(7002, 2, (11, 0), (), "UseInactiveGroundParameter", None))
	def _get_UseInactiveSoftGroundParameter(self):
		return self._ApplyTypes_(*(7011, 2, (11, 0), (), "UseInactiveSoftGroundParameter", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(7029, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseLateralFrictionFactor(self):
		return self._ApplyTypes_(*(7000, 2, (11, 0), (), "UseLateralFrictionFactor", None))
	def _get_UseMaxPenetration(self):
		return self._ApplyTypes_(*(7034, 2, (11, 0), (), "UseMaxPenetration", None))
	def _get_UseMoreFrictionData(self):
		return self._ApplyTypes_(*(7031, 2, (11, 0), (), "UseMoreFrictionData", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(7025, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(7017, 2, (11, 0), (), "UseStiffnessSpline", None))
	def _get_UseUserSubroutine(self):
		return self._ApplyTypes_(*(7014, 2, (11, 0), (), "UseUserSubroutine", None))
	def _get_UserSubroutine(self):
		return self._ApplyTypes_(*(7015, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((7021, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((7024, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((7033, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((7018, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((7027, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((7020, LCID, 4, 0) + (value,) + ()))
	def _set_UseFrictionSpline(self, value):
		if "UseFrictionSpline" in self.__dict__: self.__dict__["UseFrictionSpline"] = value; return
		self._oleobj_.Invoke(*((7023, LCID, 4, 0) + (value,) + ()))
	def _set_UseInactiveGroundParameter(self, value):
		if "UseInactiveGroundParameter" in self.__dict__: self.__dict__["UseInactiveGroundParameter"] = value; return
		self._oleobj_.Invoke(*((7002, LCID, 4, 0) + (value,) + ()))
	def _set_UseInactiveSoftGroundParameter(self, value):
		if "UseInactiveSoftGroundParameter" in self.__dict__: self.__dict__["UseInactiveSoftGroundParameter"] = value; return
		self._oleobj_.Invoke(*((7011, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((7029, LCID, 4, 0) + (value,) + ()))
	def _set_UseLateralFrictionFactor(self, value):
		if "UseLateralFrictionFactor" in self.__dict__: self.__dict__["UseLateralFrictionFactor"] = value; return
		self._oleobj_.Invoke(*((7000, LCID, 4, 0) + (value,) + ()))
	def _set_UseMaxPenetration(self, value):
		if "UseMaxPenetration" in self.__dict__: self.__dict__["UseMaxPenetration"] = value; return
		self._oleobj_.Invoke(*((7034, LCID, 4, 0) + (value,) + ()))
	def _set_UseMoreFrictionData(self, value):
		if "UseMoreFrictionData" in self.__dict__: self.__dict__["UseMoreFrictionData"] = value; return
		self._oleobj_.Invoke(*((7031, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((7025, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((7017, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserSubroutine(self, value):
		if "UseUserSubroutine" in self.__dict__: self.__dict__["UseUserSubroutine"] = value; return
		self._oleobj_.Invoke(*((7014, LCID, 4, 0) + (value,) + ()))
	def _set_UserSubroutine(self, value):
		if "UserSubroutine" in self.__dict__: self.__dict__["UserSubroutine"] = value; return
		self._oleobj_.Invoke(*((7015, LCID, 4, 0) + (value,) + ()))

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

	:type: recurdyn.ToolkitCommon.IToolkitContactFriction
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

	:type: recurdyn.ToolkitCommon.TrackFrictionType
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
	MaxPenetration = property(_get_MaxPenetration, None)
	'''
	Max penetration

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
	UseInactiveGroundParameter is obsolete function

	:type: bool
	'''
	UseInactiveSoftGroundParameter = property(_get_UseInactiveSoftGroundParameter, _set_UseInactiveSoftGroundParameter)
	'''
	UseInactiveSoftGroundParameter is obsolete function

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
	UseMaxPenetration = property(_get_UseMaxPenetration, _set_UseMaxPenetration)
	'''
	Use max penetration

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
		"_set_UseMaxPenetration": _set_UseMaxPenetration,
		"_set_UseMoreFrictionData": _set_UseMoreFrictionData,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
		"_set_UseUserSubroutine": _set_UseUserSubroutine,
		"_set_UserSubroutine": _set_UserSubroutine,
	}
	_prop_map_get_ = {
		"Cohesion": (7007, 2, (9, 0), (), "Cohesion", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingCoefficient": (7019, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (7028, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (7021, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"ExponentialNumber": (7006, 2, (9, 0), (), "ExponentialNumber", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Friction": (7032, 2, (9, 0), (), "Friction", '{28A3BBB4-DF34-4A57-9527-048B76671247}'),
		"FrictionCoefficient": (7022, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (7024, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (7033, 2, (3, 0), (), "FrictionType", '{66A716E9-F39F-4CB2-94E9-034EDE35D487}'),
		"IndentationExponent": (7030, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LateralFrictionFactor": (7001, 2, (9, 0), (), "LateralFrictionFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaxPenetration": (7035, 2, (9, 0), (), "MaxPenetration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearingDeformationModulus": (7009, 2, (9, 0), (), "ShearingDeformationModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearingResistanceAngle": (7008, 2, (9, 0), (), "ShearingResistanceAngle", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SinkageRatio": (7010, 2, (9, 0), (), "SinkageRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (7016, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (7026, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (7018, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TerrainStiffnessKc": (7004, 2, (9, 0), (), "TerrainStiffnessKc", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TerrainStiffnessKphi": (7005, 2, (9, 0), (), "TerrainStiffnessKphi", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseDampingExponent": (7027, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (7020, 2, (11, 0), (), "UseDampingSpline", None),
		"UseFrictionSpline": (7023, 2, (11, 0), (), "UseFrictionSpline", None),
		"UseInactiveGroundParameter": (7002, 2, (11, 0), (), "UseInactiveGroundParameter", None),
		"UseInactiveSoftGroundParameter": (7011, 2, (11, 0), (), "UseInactiveSoftGroundParameter", None),
		"UseIndentationExponent": (7029, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseLateralFrictionFactor": (7000, 2, (11, 0), (), "UseLateralFrictionFactor", None),
		"UseMaxPenetration": (7034, 2, (11, 0), (), "UseMaxPenetration", None),
		"UseMoreFrictionData": (7031, 2, (11, 0), (), "UseMoreFrictionData", None),
		"UseStiffnessExponent": (7025, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (7017, 2, (11, 0), (), "UseStiffnessSpline", None),
		"UseUserSubroutine": (7014, 2, (11, 0), (), "UseUserSubroutine", None),
		"UserSubroutine": (7015, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'),
	}
	_prop_map_put_ = {
		"DampingSpline": ((7021, LCID, 4, 0),()),
		"FrictionSpline": ((7024, LCID, 4, 0),()),
		"FrictionType": ((7033, LCID, 4, 0),()),
		"StiffnessSpline": ((7018, LCID, 4, 0),()),
		"UseDampingExponent": ((7027, LCID, 4, 0),()),
		"UseDampingSpline": ((7020, LCID, 4, 0),()),
		"UseFrictionSpline": ((7023, LCID, 4, 0),()),
		"UseInactiveGroundParameter": ((7002, LCID, 4, 0),()),
		"UseInactiveSoftGroundParameter": ((7011, LCID, 4, 0),()),
		"UseIndentationExponent": ((7029, LCID, 4, 0),()),
		"UseLateralFrictionFactor": ((7000, LCID, 4, 0),()),
		"UseMaxPenetration": ((7034, LCID, 4, 0),()),
		"UseMoreFrictionData": ((7031, LCID, 4, 0),()),
		"UseStiffnessExponent": ((7025, LCID, 4, 0),()),
		"UseStiffnessSpline": ((7017, LCID, 4, 0),()),
		"UseUserSubroutine": ((7014, LCID, 4, 0),()),
		"UserSubroutine": ((7015, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IForceConnectorBushing(DispatchBaseClass):
	'''Bushing force'''
	CLSID = IID('{F5A169B5-B529-4935-8B06-ACDD2A0BA456}')
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
	def _get_BaseMarker(self):
		return self._ApplyTypes_(*(202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayColor(self):
		return self._ApplyTypes_(*(207, 2, (19, 0), (), "ForceDisplayColor", None))
	def _get_ForceDisplayUse(self):
		return self._ApplyTypes_(*(209, 2, (11, 0), (), "ForceDisplayUse", None))
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
	def _get_RotationalDampingX(self):
		return self._ApplyTypes_(*(7051, 2, (9, 0), (), "RotationalDampingX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_RotationalDampingY(self):
		return self._ApplyTypes_(*(7052, 2, (9, 0), (), "RotationalDampingY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_RotationalDampingZ(self):
		return self._ApplyTypes_(*(7053, 2, (9, 0), (), "RotationalDampingZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_RotationalPreloadX(self):
		return self._ApplyTypes_(*(7057, 2, (9, 0), (), "RotationalPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationalPreloadY(self):
		return self._ApplyTypes_(*(7058, 2, (9, 0), (), "RotationalPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationalPreloadZ(self):
		return self._ApplyTypes_(*(7059, 2, (9, 0), (), "RotationalPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationalStiffnessX(self):
		return self._ApplyTypes_(*(7054, 2, (9, 0), (), "RotationalStiffnessX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_RotationalStiffnessY(self):
		return self._ApplyTypes_(*(7055, 2, (9, 0), (), "RotationalStiffnessY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_RotationalStiffnessZ(self):
		return self._ApplyTypes_(*(7056, 2, (9, 0), (), "RotationalStiffnessZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_TranslationalDampingX(self):
		return self._ApplyTypes_(*(7060, 2, (9, 0), (), "TranslationalDampingX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TranslationalDampingY(self):
		return self._ApplyTypes_(*(7061, 2, (9, 0), (), "TranslationalDampingY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TranslationalDampingZ(self):
		return self._ApplyTypes_(*(7062, 2, (9, 0), (), "TranslationalDampingZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TranslationalPreloadX(self):
		return self._ApplyTypes_(*(7066, 2, (9, 0), (), "TranslationalPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationalPreloadY(self):
		return self._ApplyTypes_(*(7067, 2, (9, 0), (), "TranslationalPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationalPreloadZ(self):
		return self._ApplyTypes_(*(7068, 2, (9, 0), (), "TranslationalPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationalStiffnessX(self):
		return self._ApplyTypes_(*(7063, 2, (9, 0), (), "TranslationalStiffnessX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TranslationalStiffnessY(self):
		return self._ApplyTypes_(*(7064, 2, (9, 0), (), "TranslationalStiffnessY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TranslationalStiffnessZ(self):
		return self._ApplyTypes_(*(7065, 2, (9, 0), (), "TranslationalStiffnessZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_UseRadial(self):
		return self._ApplyTypes_(*(7069, 2, (11, 0), (), "UseRadial", None))
	def _get_UseStaticBushing(self):
		return self._ApplyTypes_(*(7070, 2, (11, 0), (), "UseStaticBushing", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionMarker(self, value):
		if "ActionMarker" in self.__dict__: self.__dict__["ActionMarker"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
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
	def _set_UseRadial(self, value):
		if "UseRadial" in self.__dict__: self.__dict__["UseRadial"] = value; return
		self._oleobj_.Invoke(*((7069, LCID, 4, 0) + (value,) + ()))
	def _set_UseStaticBushing(self, value):
		if "UseStaticBushing" in self.__dict__: self.__dict__["UseStaticBushing"] = value; return
		self._oleobj_.Invoke(*((7070, LCID, 4, 0) + (value,) + ()))
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
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
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
	RotationalDampingX = property(_get_RotationalDampingX, None)
	'''
	Rotational damping X

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	RotationalDampingY = property(_get_RotationalDampingY, None)
	'''
	Rotational damping Y

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	RotationalDampingZ = property(_get_RotationalDampingZ, None)
	'''
	Rotational damping Z

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	RotationalPreloadX = property(_get_RotationalPreloadX, None)
	'''
	Rotational preload X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationalPreloadY = property(_get_RotationalPreloadY, None)
	'''
	Rotational preload Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationalPreloadZ = property(_get_RotationalPreloadZ, None)
	'''
	Rotational preload Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationalStiffnessX = property(_get_RotationalStiffnessX, None)
	'''
	Rotational stiffness X

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	RotationalStiffnessY = property(_get_RotationalStiffnessY, None)
	'''
	Rotational stiffness Y

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	RotationalStiffnessZ = property(_get_RotationalStiffnessZ, None)
	'''
	Rotational stiffness Z

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	TorqueDisplayColor = property(_get_TorqueDisplayColor, _set_TorqueDisplayColor)
	'''
	Torque display color

	:type: int
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
	TranslationalDampingZ = property(_get_TranslationalDampingZ, None)
	'''
	Translational damping Z

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
	TranslationalPreloadZ = property(_get_TranslationalPreloadZ, None)
	'''
	Translational preload Z

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
	TranslationalStiffnessZ = property(_get_TranslationalStiffnessZ, None)
	'''
	Translational stiffness Z

	:type: recurdyn.ProcessNet.ICoefficient
	'''
	UseRadial = property(_get_UseRadial, _set_UseRadial)
	'''
	If you use radial type, translational x direction of bushing force and translational y direction of bushing force are combined.

	:type: bool
	'''
	UseStaticBushing = property(_get_UseStaticBushing, _set_UseStaticBushing)
	'''
	If you use static bushing, a bushing force is used only executing the static analysis.

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
		"_set_BaseMarker": _set_BaseMarker,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_ForceDisplayColor": _set_ForceDisplayColor,
		"_set_ForceDisplayUse": _set_ForceDisplayUse,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_TorqueDisplayColor": _set_TorqueDisplayColor,
		"_set_UseRadial": _set_UseRadial,
		"_set_UseStaticBushing": _set_UseStaticBushing,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionMarker": (203, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseMarker": (202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ForceDisplay": (201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayColor": (207, 2, (19, 0), (), "ForceDisplayColor", None),
		"ForceDisplayUse": (209, 2, (11, 0), (), "ForceDisplayUse", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerName": (204, 2, (8, 0), (), "LayerName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RotationalDampingX": (7051, 2, (9, 0), (), "RotationalDampingX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"RotationalDampingY": (7052, 2, (9, 0), (), "RotationalDampingY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"RotationalDampingZ": (7053, 2, (9, 0), (), "RotationalDampingZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"RotationalPreloadX": (7057, 2, (9, 0), (), "RotationalPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationalPreloadY": (7058, 2, (9, 0), (), "RotationalPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationalPreloadZ": (7059, 2, (9, 0), (), "RotationalPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationalStiffnessX": (7054, 2, (9, 0), (), "RotationalStiffnessX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"RotationalStiffnessY": (7055, 2, (9, 0), (), "RotationalStiffnessY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"RotationalStiffnessZ": (7056, 2, (9, 0), (), "RotationalStiffnessZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TorqueDisplayColor": (208, 2, (19, 0), (), "TorqueDisplayColor", None),
		"TranslationalDampingX": (7060, 2, (9, 0), (), "TranslationalDampingX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TranslationalDampingY": (7061, 2, (9, 0), (), "TranslationalDampingY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TranslationalDampingZ": (7062, 2, (9, 0), (), "TranslationalDampingZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TranslationalPreloadX": (7066, 2, (9, 0), (), "TranslationalPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationalPreloadY": (7067, 2, (9, 0), (), "TranslationalPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationalPreloadZ": (7068, 2, (9, 0), (), "TranslationalPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationalStiffnessX": (7063, 2, (9, 0), (), "TranslationalStiffnessX", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TranslationalStiffnessY": (7064, 2, (9, 0), (), "TranslationalStiffnessY", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TranslationalStiffnessZ": (7065, 2, (9, 0), (), "TranslationalStiffnessZ", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"UseRadial": (7069, 2, (11, 0), (), "UseRadial", None),
		"UseStaticBushing": (7070, 2, (11, 0), (), "UseStaticBushing", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionMarker": ((203, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseMarker": ((202, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((207, LCID, 4, 0),()),
		"ForceDisplayUse": ((209, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((208, LCID, 4, 0),()),
		"UseRadial": ((7069, LCID, 4, 0),()),
		"UseStaticBushing": ((7070, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IForceConnectorFixed(DispatchBaseClass):
	'''Connector fixed force'''
	CLSID = IID('{39059D2F-DBEC-49DD-BFF2-AC0185541C99}')
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
	def _get_BaseMarker(self):
		return self._ApplyTypes_(*(202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayColor(self):
		return self._ApplyTypes_(*(207, 2, (19, 0), (), "ForceDisplayColor", None))
	def _get_ForceDisplayUse(self):
		return self._ApplyTypes_(*(209, 2, (11, 0), (), "ForceDisplayUse", None))
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
	def _get_RotationDamping(self):
		return self._ApplyTypes_(*(7058, 2, (9, 0), (), "RotationDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponent(self):
		return self._ApplyTypes_(*(7062, 2, (9, 0), (), "RotationDampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffness(self):
		return self._ApplyTypes_(*(7057, 2, (9, 0), (), "RotationStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponent(self):
		return self._ApplyTypes_(*(7060, 2, (9, 0), (), "RotationStiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_TranslationDamping(self):
		return self._ApplyTypes_(*(7052, 2, (9, 0), (), "TranslationDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingExponent(self):
		return self._ApplyTypes_(*(7056, 2, (9, 0), (), "TranslationDampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffness(self):
		return self._ApplyTypes_(*(7051, 2, (9, 0), (), "TranslationStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessExponent(self):
		return self._ApplyTypes_(*(7054, 2, (9, 0), (), "TranslationStiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseRotationDampingExponent(self):
		return self._ApplyTypes_(*(7061, 2, (11, 0), (), "UseRotationDampingExponent", None))
	def _get_UseRotationStiffnessExponent(self):
		return self._ApplyTypes_(*(7059, 2, (11, 0), (), "UseRotationStiffnessExponent", None))
	def _get_UseTranslationDampingExponent(self):
		return self._ApplyTypes_(*(7055, 2, (11, 0), (), "UseTranslationDampingExponent", None))
	def _get_UseTranslationStiffnessExponent(self):
		return self._ApplyTypes_(*(7053, 2, (11, 0), (), "UseTranslationStiffnessExponent", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionMarker(self, value):
		if "ActionMarker" in self.__dict__: self.__dict__["ActionMarker"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
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
	def _set_UseRotationDampingExponent(self, value):
		if "UseRotationDampingExponent" in self.__dict__: self.__dict__["UseRotationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((7061, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStiffnessExponent(self, value):
		if "UseRotationStiffnessExponent" in self.__dict__: self.__dict__["UseRotationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((7059, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationDampingExponent(self, value):
		if "UseTranslationDampingExponent" in self.__dict__: self.__dict__["UseTranslationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((7055, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationStiffnessExponent(self, value):
		if "UseTranslationStiffnessExponent" in self.__dict__: self.__dict__["UseTranslationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((7053, LCID, 4, 0) + (value,) + ()))
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
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
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
	RotationDamping = property(_get_RotationDamping, None)
	'''
	Damping of rotation

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingExponent = property(_get_RotationDampingExponent, None)
	'''
	Damping exponent of rotation

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffness = property(_get_RotationStiffness, None)
	'''
	Stiffness of rotation

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessExponent = property(_get_RotationStiffnessExponent, None)
	'''
	Stiffness exponent of rotation

	:type: recurdyn.ProcessNet.IDouble
	'''
	TorqueDisplayColor = property(_get_TorqueDisplayColor, _set_TorqueDisplayColor)
	'''
	Torque display color

	:type: int
	'''
	TranslationDamping = property(_get_TranslationDamping, None)
	'''
	Damping of translation

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingExponent = property(_get_TranslationDampingExponent, None)
	'''
	Damping exponent of translation

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffness = property(_get_TranslationStiffness, None)
	'''
	Stiffness of translation

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessExponent = property(_get_TranslationStiffnessExponent, None)
	'''
	Stiffness exponent of translation

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseRotationDampingExponent = property(_get_UseRotationDampingExponent, _set_UseRotationDampingExponent)
	'''
	Use stiffness exponent of rotation

	:type: bool
	'''
	UseRotationStiffnessExponent = property(_get_UseRotationStiffnessExponent, _set_UseRotationStiffnessExponent)
	'''
	Use stiffness exponent of rotation

	:type: bool
	'''
	UseTranslationDampingExponent = property(_get_UseTranslationDampingExponent, _set_UseTranslationDampingExponent)
	'''
	Use stiffness exponent of translation

	:type: bool
	'''
	UseTranslationStiffnessExponent = property(_get_UseTranslationStiffnessExponent, _set_UseTranslationStiffnessExponent)
	'''
	Use stiffness exponent of translation

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
		"_set_BaseMarker": _set_BaseMarker,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_ForceDisplayColor": _set_ForceDisplayColor,
		"_set_ForceDisplayUse": _set_ForceDisplayUse,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_TorqueDisplayColor": _set_TorqueDisplayColor,
		"_set_UseRotationDampingExponent": _set_UseRotationDampingExponent,
		"_set_UseRotationStiffnessExponent": _set_UseRotationStiffnessExponent,
		"_set_UseTranslationDampingExponent": _set_UseTranslationDampingExponent,
		"_set_UseTranslationStiffnessExponent": _set_UseTranslationStiffnessExponent,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionMarker": (203, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseMarker": (202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ForceDisplay": (201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayColor": (207, 2, (19, 0), (), "ForceDisplayColor", None),
		"ForceDisplayUse": (209, 2, (11, 0), (), "ForceDisplayUse", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerName": (204, 2, (8, 0), (), "LayerName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RotationDamping": (7058, 2, (9, 0), (), "RotationDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponent": (7062, 2, (9, 0), (), "RotationDampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffness": (7057, 2, (9, 0), (), "RotationStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponent": (7060, 2, (9, 0), (), "RotationStiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TorqueDisplayColor": (208, 2, (19, 0), (), "TorqueDisplayColor", None),
		"TranslationDamping": (7052, 2, (9, 0), (), "TranslationDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingExponent": (7056, 2, (9, 0), (), "TranslationDampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffness": (7051, 2, (9, 0), (), "TranslationStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessExponent": (7054, 2, (9, 0), (), "TranslationStiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseRotationDampingExponent": (7061, 2, (11, 0), (), "UseRotationDampingExponent", None),
		"UseRotationStiffnessExponent": (7059, 2, (11, 0), (), "UseRotationStiffnessExponent", None),
		"UseTranslationDampingExponent": (7055, 2, (11, 0), (), "UseTranslationDampingExponent", None),
		"UseTranslationStiffnessExponent": (7053, 2, (11, 0), (), "UseTranslationStiffnessExponent", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionMarker": ((203, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseMarker": ((202, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((207, LCID, 4, 0),()),
		"ForceDisplayUse": ((209, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((208, LCID, 4, 0),()),
		"UseRotationDampingExponent": ((7061, LCID, 4, 0),()),
		"UseRotationStiffnessExponent": ((7059, LCID, 4, 0),()),
		"UseTranslationDampingExponent": ((7055, LCID, 4, 0),()),
		"UseTranslationStiffnessExponent": ((7053, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IForceConnectorRevolute(DispatchBaseClass):
	'''Connector revolute force'''
	CLSID = IID('{D24BBA28-623F-4F1C-97D5-021413EB6736}')
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
	def _get_BaseMarker(self):
		return self._ApplyTypes_(*(202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayColor(self):
		return self._ApplyTypes_(*(207, 2, (19, 0), (), "ForceDisplayColor", None))
	def _get_ForceDisplayUse(self):
		return self._ApplyTypes_(*(209, 2, (11, 0), (), "ForceDisplayUse", None))
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
	def _get_RotationDamping(self):
		return self._ApplyTypes_(*(7058, 2, (9, 0), (), "RotationDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponent(self):
		return self._ApplyTypes_(*(7062, 2, (9, 0), (), "RotationDampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffness(self):
		return self._ApplyTypes_(*(7057, 2, (9, 0), (), "RotationStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponent(self):
		return self._ApplyTypes_(*(7060, 2, (9, 0), (), "RotationStiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_TranslationDamping(self):
		return self._ApplyTypes_(*(7052, 2, (9, 0), (), "TranslationDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingExponent(self):
		return self._ApplyTypes_(*(7056, 2, (9, 0), (), "TranslationDampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffness(self):
		return self._ApplyTypes_(*(7051, 2, (9, 0), (), "TranslationStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessExponent(self):
		return self._ApplyTypes_(*(7054, 2, (9, 0), (), "TranslationStiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseRotationDampingExponent(self):
		return self._ApplyTypes_(*(7061, 2, (11, 0), (), "UseRotationDampingExponent", None))
	def _get_UseRotationStiffnessExponent(self):
		return self._ApplyTypes_(*(7059, 2, (11, 0), (), "UseRotationStiffnessExponent", None))
	def _get_UseTranslationDampingExponent(self):
		return self._ApplyTypes_(*(7055, 2, (11, 0), (), "UseTranslationDampingExponent", None))
	def _get_UseTranslationStiffnessExponent(self):
		return self._ApplyTypes_(*(7053, 2, (11, 0), (), "UseTranslationStiffnessExponent", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionMarker(self, value):
		if "ActionMarker" in self.__dict__: self.__dict__["ActionMarker"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
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
	def _set_UseRotationDampingExponent(self, value):
		if "UseRotationDampingExponent" in self.__dict__: self.__dict__["UseRotationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((7061, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStiffnessExponent(self, value):
		if "UseRotationStiffnessExponent" in self.__dict__: self.__dict__["UseRotationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((7059, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationDampingExponent(self, value):
		if "UseTranslationDampingExponent" in self.__dict__: self.__dict__["UseTranslationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((7055, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationStiffnessExponent(self, value):
		if "UseTranslationStiffnessExponent" in self.__dict__: self.__dict__["UseTranslationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((7053, LCID, 4, 0) + (value,) + ()))
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
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
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
	RotationDamping = property(_get_RotationDamping, None)
	'''
	Damping of rotation

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingExponent = property(_get_RotationDampingExponent, None)
	'''
	Damping exponent of rotation

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffness = property(_get_RotationStiffness, None)
	'''
	Stiffness of rotation

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessExponent = property(_get_RotationStiffnessExponent, None)
	'''
	Stiffness exponent of rotation

	:type: recurdyn.ProcessNet.IDouble
	'''
	TorqueDisplayColor = property(_get_TorqueDisplayColor, _set_TorqueDisplayColor)
	'''
	Torque display color

	:type: int
	'''
	TranslationDamping = property(_get_TranslationDamping, None)
	'''
	Damping of translation

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingExponent = property(_get_TranslationDampingExponent, None)
	'''
	Damping exponent of translation

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffness = property(_get_TranslationStiffness, None)
	'''
	Stiffness of translation

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessExponent = property(_get_TranslationStiffnessExponent, None)
	'''
	Stiffness exponent of translation

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseRotationDampingExponent = property(_get_UseRotationDampingExponent, _set_UseRotationDampingExponent)
	'''
	Use stiffness exponent of rotation

	:type: bool
	'''
	UseRotationStiffnessExponent = property(_get_UseRotationStiffnessExponent, _set_UseRotationStiffnessExponent)
	'''
	Use stiffness exponent of rotation

	:type: bool
	'''
	UseTranslationDampingExponent = property(_get_UseTranslationDampingExponent, _set_UseTranslationDampingExponent)
	'''
	Use stiffness exponent of translation

	:type: bool
	'''
	UseTranslationStiffnessExponent = property(_get_UseTranslationStiffnessExponent, _set_UseTranslationStiffnessExponent)
	'''
	Use stiffness exponent of translation

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
		"_set_BaseMarker": _set_BaseMarker,
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_ForceDisplayColor": _set_ForceDisplayColor,
		"_set_ForceDisplayUse": _set_ForceDisplayUse,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_TorqueDisplayColor": _set_TorqueDisplayColor,
		"_set_UseRotationDampingExponent": _set_UseRotationDampingExponent,
		"_set_UseRotationStiffnessExponent": _set_UseRotationStiffnessExponent,
		"_set_UseTranslationDampingExponent": _set_UseTranslationDampingExponent,
		"_set_UseTranslationStiffnessExponent": _set_UseTranslationStiffnessExponent,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionMarker": (203, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseMarker": (202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ForceDisplay": (201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayColor": (207, 2, (19, 0), (), "ForceDisplayColor", None),
		"ForceDisplayUse": (209, 2, (11, 0), (), "ForceDisplayUse", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerName": (204, 2, (8, 0), (), "LayerName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RotationDamping": (7058, 2, (9, 0), (), "RotationDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponent": (7062, 2, (9, 0), (), "RotationDampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffness": (7057, 2, (9, 0), (), "RotationStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponent": (7060, 2, (9, 0), (), "RotationStiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TorqueDisplayColor": (208, 2, (19, 0), (), "TorqueDisplayColor", None),
		"TranslationDamping": (7052, 2, (9, 0), (), "TranslationDamping", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingExponent": (7056, 2, (9, 0), (), "TranslationDampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffness": (7051, 2, (9, 0), (), "TranslationStiffness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessExponent": (7054, 2, (9, 0), (), "TranslationStiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseRotationDampingExponent": (7061, 2, (11, 0), (), "UseRotationDampingExponent", None),
		"UseRotationStiffnessExponent": (7059, 2, (11, 0), (), "UseRotationStiffnessExponent", None),
		"UseTranslationDampingExponent": (7055, 2, (11, 0), (), "UseTranslationDampingExponent", None),
		"UseTranslationStiffnessExponent": (7053, 2, (11, 0), (), "UseTranslationStiffnessExponent", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionMarker": ((203, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseMarker": ((202, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((207, LCID, 4, 0),()),
		"ForceDisplayUse": ((209, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((208, LCID, 4, 0),()),
		"UseRotationDampingExponent": ((7061, LCID, 4, 0),()),
		"UseRotationStiffnessExponent": ((7059, LCID, 4, 0),()),
		"UseTranslationDampingExponent": ((7055, LCID, 4, 0),()),
		"UseTranslationStiffnessExponent": ((7053, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IForceConnectorSpring(DispatchBaseClass):
	'''Connector Spring force'''
	CLSID = IID('{93A5A572-A6DD-4F12-A3E5-64F95B78718F}')
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
	def _get_BaseMarker(self):
		return self._ApplyTypes_(*(202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Damping(self):
		return self._ApplyTypes_(*(7055, 2, (9, 0), (), "Damping", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_ForceDisplayColor(self):
		return self._ApplyTypes_(*(207, 2, (19, 0), (), "ForceDisplayColor", None))
	def _get_ForceDisplayUse(self):
		return self._ApplyTypes_(*(209, 2, (11, 0), (), "ForceDisplayUse", None))
	def _get_FreeLength(self):
		return self._ApplyTypes_(*(7052, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
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
		return self._ApplyTypes_(*(7053, 2, (9, 0), (), "Preload", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SpringGraphic(self):
		return self._ApplyTypes_(*(7051, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'))
	def _get_Stiffness(self):
		return self._ApplyTypes_(*(7054, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'))
	def _get_TorqueDisplayColor(self):
		return self._ApplyTypes_(*(208, 2, (19, 0), (), "TorqueDisplayColor", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionMarker(self, value):
		if "ActionMarker" in self.__dict__: self.__dict__["ActionMarker"] = value; return
		self._oleobj_.Invoke(*((203, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
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
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ActionMarker": _set_ActionMarker,
		"_set_Active": _set_Active,
		"_set_BaseMarker": _set_BaseMarker,
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
		"ActionMarker": (203, 2, (9, 0), (), "ActionMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseMarker": (202, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Damping": (7055, 2, (9, 0), (), "Damping", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"ForceDisplay": (201, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"ForceDisplayColor": (207, 2, (19, 0), (), "ForceDisplayColor", None),
		"ForceDisplayUse": (209, 2, (11, 0), (), "ForceDisplayUse", None),
		"FreeLength": (7052, 2, (9, 0), (), "FreeLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerName": (204, 2, (8, 0), (), "LayerName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Preload": (7053, 2, (9, 0), (), "Preload", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SpringGraphic": (7051, 2, (9, 0), (), "SpringGraphic", '{61C55C33-4716-4D26-8030-F9D29ED8B413}'),
		"Stiffness": (7054, 2, (9, 0), (), "Stiffness", '{07D4A7FC-5B11-4E7D-B805-4B32646009AC}'),
		"TorqueDisplayColor": (208, 2, (19, 0), (), "TorqueDisplayColor", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionMarker": ((203, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseMarker": ((202, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((201, LCID, 4, 0),()),
		"ForceDisplayColor": ((207, LCID, 4, 0),()),
		"ForceDisplayUse": ((209, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"TorqueDisplayColor": ((208, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IToolkitContactFriction(DispatchBaseClass):
	'''Toolkit contact friction'''
	CLSID = IID('{28A3BBB4-DF34-4A57-9527-048B76671247}')
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
		return self._ApplyTypes_(*(7002, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaxStictionDeformaton(self):
		return self._ApplyTypes_(*(7005, 2, (9, 0), (), "MaxStictionDeformaton", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticFrictionCoefficient(self):
		return self._ApplyTypes_(*(7003, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticThresholdVelocity(self):
		return self._ApplyTypes_(*(7001, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseMaxStictionDeformaton(self):
		return self._ApplyTypes_(*(7004, 2, (11, 0), (), "UseMaxStictionDeformaton", None))

	def _set_UseMaxStictionDeformaton(self, value):
		if "UseMaxStictionDeformaton" in self.__dict__: self.__dict__["UseMaxStictionDeformaton"] = value; return
		self._oleobj_.Invoke(*((7004, LCID, 4, 0) + (value,) + ()))

	DynamicThresholdVelocity = property(_get_DynamicThresholdVelocity, None)
	'''
	Dynamic threshold velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaxStictionDeformaton = property(_get_MaxStictionDeformaton, None)
	'''
	Max friction force

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
	UseMaxStictionDeformaton = property(_get_UseMaxStictionDeformaton, _set_UseMaxStictionDeformaton)
	'''
	Use max friction force

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_UseMaxStictionDeformaton": _set_UseMaxStictionDeformaton,
	}
	_prop_map_get_ = {
		"DynamicThresholdVelocity": (7002, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaxStictionDeformaton": (7005, 2, (9, 0), (), "MaxStictionDeformaton", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticFrictionCoefficient": (7003, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticThresholdVelocity": (7001, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseMaxStictionDeformaton": (7004, 2, (11, 0), (), "UseMaxStictionDeformaton", None),
	}
	_prop_map_put_ = {
		"UseMaxStictionDeformaton": ((7004, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

IContactTrackToSurface_vtables_dispatch_ = 1
IContactTrackToSurface_vtables_ = [
	(( 'UsePressureSinkage' , 'pVal' , ), 7001, (7001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UsePressureSinkage' , 'pVal' , ), 7001, (7001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ContactParameter' , 'ppVal' , ), 7002, (7002, (), [ (16393, 10, None, "IID('{EBF27DFC-CCEC-401F-A201-00E6B5758270}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ActionUpDirection' , 'pVal' , ), 7003, (7003, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ActionUpDirection' , 'pVal' , ), 7003, (7003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ActionPatchOption' , 'ppVal' , ), 7004, (7004, (), [ (16393, 10, None, "IID('{D479C190-172F-42AC-A4B9-5B3AFE1EB81B}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BaseEntity' , 'ppVal' , ), 7005, (7005, (), [ (9, 1, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BaseEntity' , 'ppVal' , ), 7005, (7005, (), [ (16393, 10, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ActionEntity' , 'ppVal' , ), 7006, (7006, (), [ (9, 1, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ActionEntity' , 'ppVal' , ), 7006, (7006, (), [ (16393, 10, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseActionNodeContact' , 'pVal' , ), 7007, (7007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseActionNodeContact' , 'pVal' , ), 7007, (7007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IContactTrackToSurfaceProperty_vtables_dispatch_ = 1
IContactTrackToSurfaceProperty_vtables_ = [
	(( 'UseLateralFrictionFactor' , 'pVal' , ), 7000, (7000, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseLateralFrictionFactor' , 'pVal' , ), 7000, (7000, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LateralFrictionFactor' , 'ppVal' , ), 7001, (7001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveGroundParameter' , 'pVal' , ), 7002, (7002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveGroundParameter' , 'pVal' , ), 7002, (7002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SoftGroundType' , 'Val' , ), 7003, (7003, (), [ (3, 1, None, "IID('{9778678C-1CAF-4393-AC21-3FAF6B966328}')") , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TerrainStiffnessKc' , 'ppVal' , ), 7004, (7004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TerrainStiffnessKphi' , 'ppVal' , ), 7005, (7005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ExponentialNumber' , 'ppVal' , ), 7006, (7006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Cohesion' , 'ppVal' , ), 7007, (7007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ShearingResistanceAngle' , 'ppVal' , ), 7008, (7008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ShearingDeformationModulus' , 'ppVal' , ), 7009, (7009, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SinkageRatio' , 'ppVal' , ), 7010, (7010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveSoftGroundParameter' , 'pVal' , ), 7011, (7011, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseInactiveSoftGroundParameter' , 'pVal' , ), 7011, (7011, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'Val' , ), 7012, (7012, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 7013, (7013, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UseUserSubroutine' , 'pVal' , ), 7014, (7014, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseUserSubroutine' , 'pVal' , ), 7014, (7014, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'pVal' , ), 7015, (7015, (), [ (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'pVal' , ), 7015, (7015, (), [ (16393, 10, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessCoefficient' , 'ppVal' , ), 7016, (7016, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 7017, (7017, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 7017, (7017, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 7018, (7018, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 7018, (7018, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 7019, (7019, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 7020, (7020, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 7020, (7020, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 7021, (7021, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 7021, (7021, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 7022, (7022, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 7023, (7023, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseFrictionSpline' , 'pVal' , ), 7023, (7023, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 7024, (7024, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 7024, (7024, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 7025, (7025, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 7025, (7025, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 7026, (7026, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 7027, (7027, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 7027, (7027, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 7028, (7028, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 7029, (7029, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 7029, (7029, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 7030, (7030, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UseMoreFrictionData' , 'pVal' , ), 7031, (7031, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'UseMoreFrictionData' , 'pVal' , ), 7031, (7031, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'Friction' , 'ppVal' , ), 7032, (7032, (), [ (16393, 10, None, "IID('{28A3BBB4-DF34-4A57-9527-048B76671247}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 7033, (7033, (), [ (3, 1, None, "IID('{66A716E9-F39F-4CB2-94E9-034EDE35D487}')") , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 7033, (7033, (), [ (16387, 10, None, "IID('{66A716E9-F39F-4CB2-94E9-034EDE35D487}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'UseMaxPenetration' , 'pVal' , ), 7034, (7034, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'UseMaxPenetration' , 'pVal' , ), 7034, (7034, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'MaxPenetration' , 'ppVal' , ), 7035, (7035, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
]

IForceConnectorBushing_vtables_dispatch_ = 1
IForceConnectorBushing_vtables_ = [
	(( 'RotationalDampingX' , 'ppVal' , ), 7051, (7051, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RotationalDampingY' , 'ppVal' , ), 7052, (7052, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'RotationalDampingZ' , 'ppVal' , ), 7053, (7053, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'RotationalStiffnessX' , 'ppVal' , ), 7054, (7054, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'RotationalStiffnessY' , 'ppVal' , ), 7055, (7055, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'RotationalStiffnessZ' , 'ppVal' , ), 7056, (7056, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'RotationalPreloadX' , 'ppVal' , ), 7057, (7057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RotationalPreloadY' , 'ppVal' , ), 7058, (7058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'RotationalPreloadZ' , 'ppVal' , ), 7059, (7059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDampingX' , 'ppVal' , ), 7060, (7060, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDampingY' , 'ppVal' , ), 7061, (7061, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalDampingZ' , 'ppVal' , ), 7062, (7062, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalStiffnessX' , 'ppVal' , ), 7063, (7063, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalStiffnessY' , 'ppVal' , ), 7064, (7064, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalStiffnessZ' , 'ppVal' , ), 7065, (7065, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalPreloadX' , 'ppVal' , ), 7066, (7066, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalPreloadY' , 'ppVal' , ), 7067, (7067, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalPreloadZ' , 'ppVal' , ), 7068, (7068, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UseRadial' , 'pVal' , ), 7069, (7069, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseRadial' , 'pVal' , ), 7069, (7069, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'UseStaticBushing' , 'pVal' , ), 7070, (7070, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'UseStaticBushing' , 'pVal' , ), 7070, (7070, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
]

IForceConnectorFixed_vtables_dispatch_ = 1
IForceConnectorFixed_vtables_ = [
	(( 'TranslationStiffness' , 'ppVal' , ), 7051, (7051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDamping' , 'ppVal' , ), 7052, (7052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 7053, (7053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 7053, (7053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessExponent' , 'ppVal' , ), 7054, (7054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 7055, (7055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 7055, (7055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingExponent' , 'ppVal' , ), 7056, (7056, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffness' , 'ppVal' , ), 7057, (7057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'RotationDamping' , 'ppVal' , ), 7058, (7058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 7059, (7059, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 7059, (7059, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponent' , 'ppVal' , ), 7060, (7060, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 7061, (7061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 7061, (7061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponent' , 'ppVal' , ), 7062, (7062, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
]

IForceConnectorRevolute_vtables_dispatch_ = 1
IForceConnectorRevolute_vtables_ = [
	(( 'TranslationStiffness' , 'ppVal' , ), 7051, (7051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDamping' , 'ppVal' , ), 7052, (7052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 7053, (7053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 7053, (7053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessExponent' , 'ppVal' , ), 7054, (7054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 7055, (7055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 7055, (7055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingExponent' , 'ppVal' , ), 7056, (7056, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffness' , 'ppVal' , ), 7057, (7057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'RotationDamping' , 'ppVal' , ), 7058, (7058, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 7059, (7059, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 7059, (7059, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponent' , 'ppVal' , ), 7060, (7060, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 7061, (7061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 7061, (7061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponent' , 'ppVal' , ), 7062, (7062, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
]

IForceConnectorSpring_vtables_dispatch_ = 1
IForceConnectorSpring_vtables_ = [
	(( 'SpringGraphic' , 'ppVal' , ), 7051, (7051, (), [ (16393, 10, None, "IID('{61C55C33-4716-4D26-8030-F9D29ED8B413}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'FreeLength' , 'ppVal' , ), 7052, (7052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Preload' , 'ppVal' , ), 7053, (7053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Stiffness' , 'ppVal' , ), 7054, (7054, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Damping' , 'ppVal' , ), 7055, (7055, (), [ (16393, 10, None, "IID('{07D4A7FC-5B11-4E7D-B805-4B32646009AC}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

IToolkitContactFriction_vtables_dispatch_ = 1
IToolkitContactFriction_vtables_ = [
	(( 'StaticThresholdVelocity' , 'ppVal' , ), 7001, (7001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DynamicThresholdVelocity' , 'ppVal' , ), 7002, (7002, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StaticFrictionCoefficient' , 'ppVal' , ), 7003, (7003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseMaxStictionDeformaton' , 'pVal' , ), 7004, (7004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseMaxStictionDeformaton' , 'pVal' , ), 7004, (7004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MaxStictionDeformaton' , 'ppVal' , ), 7005, (7005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{39059D2F-DBEC-49DD-BFF2-AC0185541C99}' : IForceConnectorFixed,
	'{D24BBA28-623F-4F1C-97D5-021413EB6736}' : IForceConnectorRevolute,
	'{93A5A572-A6DD-4F12-A3E5-64F95B78718F}' : IForceConnectorSpring,
	'{F5A169B5-B529-4935-8B06-ACDD2A0BA456}' : IForceConnectorBushing,
	'{28A3BBB4-DF34-4A57-9527-048B76671247}' : IToolkitContactFriction,
	'{EBF27DFC-CCEC-401F-A201-00E6B5758270}' : IContactTrackToSurfaceProperty,
	'{1EAD15B7-3DFF-40FD-BD77-12CBB9F2CA6C}' : IContactTrackToSurface,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{39059D2F-DBEC-49DD-BFF2-AC0185541C99}' : 'IForceConnectorFixed',
	'{D24BBA28-623F-4F1C-97D5-021413EB6736}' : 'IForceConnectorRevolute',
	'{93A5A572-A6DD-4F12-A3E5-64F95B78718F}' : 'IForceConnectorSpring',
	'{F5A169B5-B529-4935-8B06-ACDD2A0BA456}' : 'IForceConnectorBushing',
	'{28A3BBB4-DF34-4A57-9527-048B76671247}' : 'IToolkitContactFriction',
	'{EBF27DFC-CCEC-401F-A201-00E6B5758270}' : 'IContactTrackToSurfaceProperty',
	'{1EAD15B7-3DFF-40FD-BD77-12CBB9F2CA6C}' : 'IContactTrackToSurface',
}


NamesToIIDMap = {
	'IForceConnectorFixed' : '{39059D2F-DBEC-49DD-BFF2-AC0185541C99}',
	'IForceConnectorRevolute' : '{D24BBA28-623F-4F1C-97D5-021413EB6736}',
	'IForceConnectorSpring' : '{93A5A572-A6DD-4F12-A3E5-64F95B78718F}',
	'IForceConnectorBushing' : '{F5A169B5-B529-4935-8B06-ACDD2A0BA456}',
	'IToolkitContactFriction' : '{28A3BBB4-DF34-4A57-9527-048B76671247}',
	'IContactTrackToSurfaceProperty' : '{EBF27DFC-CCEC-401F-A201-00E6B5758270}',
	'IContactTrackToSurface' : '{1EAD15B7-3DFF-40FD-BD77-12CBB9F2CA6C}',
}


