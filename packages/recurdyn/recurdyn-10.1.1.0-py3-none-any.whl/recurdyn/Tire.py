# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMTire.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMTire Type Library'
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

CLSID = IID('{1F294933-82D9-405C-84D4-F01A70FD82FA}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class ITire(DispatchBaseClass):
	'''Tire'''
	CLSID = IID('{C4B87451-54E2-430D-84F3-E9A9087B2476}')
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
	def _get_TireBody(self):
		return self._ApplyTypes_(*(4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
	TireBody = property(_get_TireBody, None)
	'''
	Get Tire Body

	:type: recurdyn.ProcessNet.IBody
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
		"TireBody": (4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
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

class ITireGeometryRim(DispatchBaseClass):
	'''Tire RIM Geometry'''
	CLSID = IID('{917E1C84-02D0-4205-B70F-E0C55BC77209}')
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
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RimDiameter(self):
		return self._ApplyTypes_(*(4052, 2, (9, 0), (), "RimDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RimDiameterUnitInch(self):
		return self._ApplyTypes_(*(4054, 2, (5, 0), (), "RimDiameterUnitInch", None))
	def _get_RimWidth(self):
		return self._ApplyTypes_(*(4051, 2, (9, 0), (), "RimWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RimWidthUnitMM(self):
		return self._ApplyTypes_(*(4053, 2, (5, 0), (), "RimWidthUnitMM", None))
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
	def _set_RimDiameterUnitInch(self, value):
		if "RimDiameterUnitInch" in self.__dict__: self.__dict__["RimDiameterUnitInch"] = value; return
		self._oleobj_.Invoke(*((4054, LCID, 4, 0) + (value,) + ()))
	def _set_RimWidthUnitMM(self, value):
		if "RimWidthUnitMM" in self.__dict__: self.__dict__["RimWidthUnitMM"] = value; return
		self._oleobj_.Invoke(*((4053, LCID, 4, 0) + (value,) + ()))
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
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RimDiameter = property(_get_RimDiameter, None)
	'''
	Rim Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	RimDiameterUnitInch = property(_get_RimDiameterUnitInch, _set_RimDiameterUnitInch)
	'''
	Rim Diameter

	:type: float
	'''
	RimWidth = property(_get_RimWidth, None)
	'''
	Rim Width

	:type: recurdyn.ProcessNet.IDouble
	'''
	RimWidthUnitMM = property(_get_RimWidthUnitMM, _set_RimWidthUnitMM)
	'''
	Rim Width

	:type: float
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
		"_set_RimDiameterUnitInch": _set_RimDiameterUnitInch,
		"_set_RimWidthUnitMM": _set_RimWidthUnitMM,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RimDiameter": (4052, 2, (9, 0), (), "RimDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RimDiameterUnitInch": (4054, 2, (5, 0), (), "RimDiameterUnitInch", None),
		"RimWidth": (4051, 2, (9, 0), (), "RimWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RimWidthUnitMM": (4053, 2, (5, 0), (), "RimWidthUnitMM", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"RimDiameterUnitInch": ((4054, LCID, 4, 0),()),
		"RimWidthUnitMM": ((4053, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITireGeometryRimGeneric(DispatchBaseClass):
	'''Tire RIM Geometry for generic'''
	CLSID = IID('{8F7EAE62-8E94-4E0B-AEC2-0BCE70CE5C62}')
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


	def _get_AngleOfRimHole(self):
		return self._ApplyTypes_(*(4102, 2, (9, 0), (), "AngleOfRimHole", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberOfLeads(self):
		return self._ApplyTypes_(*(4101, 2, (3, 0), (), "NumberOfLeads", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RimDiameter(self):
		return self._ApplyTypes_(*(4052, 2, (9, 0), (), "RimDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RimDiameterUnitInch(self):
		return self._ApplyTypes_(*(4054, 2, (5, 0), (), "RimDiameterUnitInch", None))
	def _get_RimInnerDiameter(self):
		return self._ApplyTypes_(*(4103, 2, (9, 0), (), "RimInnerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RimInnerDiameterUnitInch(self):
		return self._ApplyTypes_(*(4104, 2, (5, 0), (), "RimInnerDiameterUnitInch", None))
	def _get_RimWidth(self):
		return self._ApplyTypes_(*(4051, 2, (9, 0), (), "RimWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RimWidthUnitMM(self):
		return self._ApplyTypes_(*(4053, 2, (5, 0), (), "RimWidthUnitMM", None))
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
	def _set_NumberOfLeads(self, value):
		if "NumberOfLeads" in self.__dict__: self.__dict__["NumberOfLeads"] = value; return
		self._oleobj_.Invoke(*((4101, LCID, 4, 0) + (value,) + ()))
	def _set_RimDiameterUnitInch(self, value):
		if "RimDiameterUnitInch" in self.__dict__: self.__dict__["RimDiameterUnitInch"] = value; return
		self._oleobj_.Invoke(*((4054, LCID, 4, 0) + (value,) + ()))
	def _set_RimInnerDiameterUnitInch(self, value):
		if "RimInnerDiameterUnitInch" in self.__dict__: self.__dict__["RimInnerDiameterUnitInch"] = value; return
		self._oleobj_.Invoke(*((4104, LCID, 4, 0) + (value,) + ()))
	def _set_RimWidthUnitMM(self, value):
		if "RimWidthUnitMM" in self.__dict__: self.__dict__["RimWidthUnitMM"] = value; return
		self._oleobj_.Invoke(*((4053, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	AngleOfRimHole = property(_get_AngleOfRimHole, None)
	'''
	Angle of RimHole

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
	NumberOfLeads = property(_get_NumberOfLeads, _set_NumberOfLeads)
	'''
	Number of Leads

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
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RimDiameter = property(_get_RimDiameter, None)
	'''
	Rim Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	RimDiameterUnitInch = property(_get_RimDiameterUnitInch, _set_RimDiameterUnitInch)
	'''
	Rim Diameter

	:type: float
	'''
	RimInnerDiameter = property(_get_RimInnerDiameter, None)
	'''
	Rim Inner Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	RimInnerDiameterUnitInch = property(_get_RimInnerDiameterUnitInch, _set_RimInnerDiameterUnitInch)
	'''
	Rim Inner Diameter(Inch)

	:type: float
	'''
	RimWidth = property(_get_RimWidth, None)
	'''
	Rim Width

	:type: recurdyn.ProcessNet.IDouble
	'''
	RimWidthUnitMM = property(_get_RimWidthUnitMM, _set_RimWidthUnitMM)
	'''
	Rim Width

	:type: float
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
		"_set_NumberOfLeads": _set_NumberOfLeads,
		"_set_RimDiameterUnitInch": _set_RimDiameterUnitInch,
		"_set_RimInnerDiameterUnitInch": _set_RimInnerDiameterUnitInch,
		"_set_RimWidthUnitMM": _set_RimWidthUnitMM,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"AngleOfRimHole": (4102, 2, (9, 0), (), "AngleOfRimHole", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberOfLeads": (4101, 2, (3, 0), (), "NumberOfLeads", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RimDiameter": (4052, 2, (9, 0), (), "RimDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RimDiameterUnitInch": (4054, 2, (5, 0), (), "RimDiameterUnitInch", None),
		"RimInnerDiameter": (4103, 2, (9, 0), (), "RimInnerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RimInnerDiameterUnitInch": (4104, 2, (5, 0), (), "RimInnerDiameterUnitInch", None),
		"RimWidth": (4051, 2, (9, 0), (), "RimWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RimWidthUnitMM": (4053, 2, (5, 0), (), "RimWidthUnitMM", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NumberOfLeads": ((4101, LCID, 4, 0),()),
		"RimDiameterUnitInch": ((4054, LCID, 4, 0),()),
		"RimInnerDiameterUnitInch": ((4104, LCID, 4, 0),()),
		"RimWidthUnitMM": ((4053, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITireGeometryTire(DispatchBaseClass):
	'''Tire Geometry'''
	CLSID = IID('{C00BB7B9-649E-4377-8A92-AF637D601E38}')
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


	def UpdateTireRadius(self):
		'''
		Update Tire Radius
		'''
		return self._oleobj_.InvokeTypes(4056, LCID, 1, (24, 0), (),)


	def _get_AspectRatio(self):
		return self._ApplyTypes_(*(4052, 2, (9, 0), (), "AspectRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
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
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RimDiameter(self):
		return self._ApplyTypes_(*(4053, 2, (9, 0), (), "RimDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RimDiameterUnitInch(self):
		return self._ApplyTypes_(*(4055, 2, (5, 0), (), "RimDiameterUnitInch", None))
	def _get_SectionWidth(self):
		return self._ApplyTypes_(*(4051, 2, (9, 0), (), "SectionWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SectionWidthUnitMM(self):
		return self._ApplyTypes_(*(4054, 2, (5, 0), (), "SectionWidthUnitMM", None))
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
	def _set_RimDiameterUnitInch(self, value):
		if "RimDiameterUnitInch" in self.__dict__: self.__dict__["RimDiameterUnitInch"] = value; return
		self._oleobj_.Invoke(*((4055, LCID, 4, 0) + (value,) + ()))
	def _set_SectionWidthUnitMM(self, value):
		if "SectionWidthUnitMM" in self.__dict__: self.__dict__["SectionWidthUnitMM"] = value; return
		self._oleobj_.Invoke(*((4054, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	AspectRatio = property(_get_AspectRatio, None)
	'''
	Aspect Ratio

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
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RimDiameter = property(_get_RimDiameter, None)
	'''
	Rim Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	RimDiameterUnitInch = property(_get_RimDiameterUnitInch, _set_RimDiameterUnitInch)
	'''
	Rim Diameter

	:type: float
	'''
	SectionWidth = property(_get_SectionWidth, None)
	'''
	Section Width

	:type: recurdyn.ProcessNet.IDouble
	'''
	SectionWidthUnitMM = property(_get_SectionWidthUnitMM, _set_SectionWidthUnitMM)
	'''
	Section Width

	:type: float
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
		"_set_RimDiameterUnitInch": _set_RimDiameterUnitInch,
		"_set_SectionWidthUnitMM": _set_SectionWidthUnitMM,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"AspectRatio": (4052, 2, (9, 0), (), "AspectRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RimDiameter": (4053, 2, (9, 0), (), "RimDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RimDiameterUnitInch": (4055, 2, (5, 0), (), "RimDiameterUnitInch", None),
		"SectionWidth": (4051, 2, (9, 0), (), "SectionWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SectionWidthUnitMM": (4054, 2, (5, 0), (), "SectionWidthUnitMM", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"RimDiameterUnitInch": ((4055, LCID, 4, 0),()),
		"SectionWidthUnitMM": ((4054, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITireGroup(DispatchBaseClass):
	'''Tire Group'''
	CLSID = IID('{4DE9BFB3-300F-48DC-9DC2-82FE6DC39C84}')
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
	def _get_TireBody(self):
		return self._ApplyTypes_(*(4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_TireForce(self):
		return self._ApplyTypes_(*(4051, 2, (9, 0), (), "TireForce", '{57CC4E39-380C-40B8-AE7F-0908ADC0DB18}'))
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
	TireBody = property(_get_TireBody, None)
	'''
	Get Tire Body

	:type: recurdyn.ProcessNet.IBody
	'''
	TireForce = property(_get_TireForce, None)
	'''
	Get Tire Force

	:type: recurdyn.ProcessNet.IForceTire
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
		"TireBody": (4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"TireForce": (4051, 2, (9, 0), (), "TireForce", '{57CC4E39-380C-40B8-AE7F-0908ADC0DB18}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
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

class ITireGroupGeneric(DispatchBaseClass):
	'''Generic Tire Group'''
	CLSID = IID('{4078C2ED-0A08-4307-B854-1E7E24AF481B}')
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
	def _get_AspectRatio(self):
		return self._ApplyTypes_(*(4054, 2, (5, 0), (), "AspectRatio", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_LongitudinalVelocity(self):
		return self._ApplyTypes_(*(4057, 2, (9, 0), (), "LongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_OrientationX(self):
		return self._ApplyTypes_(*(4063, 2, (9, 0), (), "OrientationX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_OrientationY(self):
		return self._ApplyTypes_(*(4062, 2, (9, 0), (), "OrientationY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_OrientationZ(self):
		return self._ApplyTypes_(*(4061, 2, (9, 0), (), "OrientationZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Origin(self):
		return self._ApplyTypes_(*(4060, 2, (9, 0), (), "Origin", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RimRadius(self):
		return self._ApplyTypes_(*(4055, 2, (5, 0), (), "RimRadius", None))
	def _get_Road(self):
		return self._ApplyTypes_(*(4064, 2, (8, 0), (), "Road", None))
	def _get_SpinAxisAngularVelocity(self):
		return self._ApplyTypes_(*(4059, 2, (9, 0), (), "SpinAxisAngularVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TireBody(self):
		return self._ApplyTypes_(*(4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_TireFile(self):
		return self._ApplyTypes_(*(4051, 2, (8, 0), (), "TireFile", None))
	def _get_TireRadius(self):
		return self._ApplyTypes_(*(4052, 2, (5, 0), (), "TireRadius", None))
	def _get_TireSide(self):
		return self._ApplyTypes_(*(4065, 2, (3, 0), (), "TireSide", '{F0B47155-E2C8-499D-B8A2-2B9BBC744C7C}'))
	def _get_TireWidth(self):
		return self._ApplyTypes_(*(4053, 2, (5, 0), (), "TireWidth", None))
	def _get_UseLongitudinalVelocity(self):
		return self._ApplyTypes_(*(4056, 2, (11, 0), (), "UseLongitudinalVelocity", None))
	def _get_UseSpinAxisAngularVelocity(self):
		return self._ApplyTypes_(*(4058, 2, (11, 0), (), "UseSpinAxisAngularVelocity", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_UserInputParameter(self):
		return self._ApplyTypes_(*(4066, 2, (9, 0), (), "UserInputParameter", '{5810F409-F289-4DB7-819A-CE79BE9370D2}'))

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
	def _set_Road(self, value):
		if "Road" in self.__dict__: self.__dict__["Road"] = value; return
		self._oleobj_.Invoke(*((4064, LCID, 4, 0) + (value,) + ()))
	def _set_TireFile(self, value):
		if "TireFile" in self.__dict__: self.__dict__["TireFile"] = value; return
		self._oleobj_.Invoke(*((4051, LCID, 4, 0) + (value,) + ()))
	def _set_TireSide(self, value):
		if "TireSide" in self.__dict__: self.__dict__["TireSide"] = value; return
		self._oleobj_.Invoke(*((4065, LCID, 4, 0) + (value,) + ()))
	def _set_UseLongitudinalVelocity(self, value):
		if "UseLongitudinalVelocity" in self.__dict__: self.__dict__["UseLongitudinalVelocity"] = value; return
		self._oleobj_.Invoke(*((4056, LCID, 4, 0) + (value,) + ()))
	def _set_UseSpinAxisAngularVelocity(self, value):
		if "UseSpinAxisAngularVelocity" in self.__dict__: self.__dict__["UseSpinAxisAngularVelocity"] = value; return
		self._oleobj_.Invoke(*((4058, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	AspectRatio = property(_get_AspectRatio, None)
	'''
	Aspect Ratio

	:type: float
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
	LongitudinalVelocity = property(_get_LongitudinalVelocity, None)
	'''
	LongitudinalVelocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	OrientationX = property(_get_OrientationX, None)
	'''
	Orientation X

	:type: recurdyn.ProcessNet.IDouble
	'''
	OrientationY = property(_get_OrientationY, None)
	'''
	Orientation Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	OrientationZ = property(_get_OrientationZ, None)
	'''
	Orientation Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	Origin = property(_get_Origin, None)
	'''
	Origin

	:type: recurdyn.ProcessNet.IVector
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
	RimRadius = property(_get_RimRadius, None)
	'''
	Rim Radius

	:type: float
	'''
	Road = property(_get_Road, _set_Road)
	'''
	Road

	:type: str
	'''
	SpinAxisAngularVelocity = property(_get_SpinAxisAngularVelocity, None)
	'''
	Spin Axis Angular Velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	TireBody = property(_get_TireBody, None)
	'''
	Get Tire Body

	:type: recurdyn.ProcessNet.IBody
	'''
	TireFile = property(_get_TireFile, _set_TireFile)
	'''
	Relative Path of Tire File

	:type: str
	'''
	TireRadius = property(_get_TireRadius, None)
	'''
	Tire Radius

	:type: float
	'''
	TireSide = property(_get_TireSide, _set_TireSide)
	'''
	Tire Side

	:type: recurdyn.ProcessNet.TireSideType
	'''
	TireWidth = property(_get_TireWidth, None)
	'''
	Tire Width

	:type: float
	'''
	UseLongitudinalVelocity = property(_get_UseLongitudinalVelocity, _set_UseLongitudinalVelocity)
	'''
	Use Longitudinal Velocity

	:type: bool
	'''
	UseSpinAxisAngularVelocity = property(_get_UseSpinAxisAngularVelocity, _set_UseSpinAxisAngularVelocity)
	'''
	Use Spin Axis Angular Velocity

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	UserInputParameter = property(_get_UserInputParameter, None)
	'''
	User Input Parameter

	:type: recurdyn.Tire.IUserInputParameter
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_Road": _set_Road,
		"_set_TireFile": _set_TireFile,
		"_set_TireSide": _set_TireSide,
		"_set_UseLongitudinalVelocity": _set_UseLongitudinalVelocity,
		"_set_UseSpinAxisAngularVelocity": _set_UseSpinAxisAngularVelocity,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"AspectRatio": (4054, 2, (5, 0), (), "AspectRatio", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"LongitudinalVelocity": (4057, 2, (9, 0), (), "LongitudinalVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"OrientationX": (4063, 2, (9, 0), (), "OrientationX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"OrientationY": (4062, 2, (9, 0), (), "OrientationY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"OrientationZ": (4061, 2, (9, 0), (), "OrientationZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Origin": (4060, 2, (9, 0), (), "Origin", '{918CAF9A-7A62-4EC4-B45D-C259C997B661}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RimRadius": (4055, 2, (5, 0), (), "RimRadius", None),
		"Road": (4064, 2, (8, 0), (), "Road", None),
		"SpinAxisAngularVelocity": (4059, 2, (9, 0), (), "SpinAxisAngularVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TireBody": (4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"TireFile": (4051, 2, (8, 0), (), "TireFile", None),
		"TireRadius": (4052, 2, (5, 0), (), "TireRadius", None),
		"TireSide": (4065, 2, (3, 0), (), "TireSide", '{F0B47155-E2C8-499D-B8A2-2B9BBC744C7C}'),
		"TireWidth": (4053, 2, (5, 0), (), "TireWidth", None),
		"UseLongitudinalVelocity": (4056, 2, (11, 0), (), "UseLongitudinalVelocity", None),
		"UseSpinAxisAngularVelocity": (4058, 2, (11, 0), (), "UseSpinAxisAngularVelocity", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"UserInputParameter": (4066, 2, (9, 0), (), "UserInputParameter", '{5810F409-F289-4DB7-819A-CE79BE9370D2}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Road": ((4064, LCID, 4, 0),()),
		"TireFile": ((4051, LCID, 4, 0),()),
		"TireSide": ((4065, LCID, 4, 0),()),
		"UseLongitudinalVelocity": ((4056, LCID, 4, 0),()),
		"UseSpinAxisAngularVelocity": ((4058, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITireGroupMF(DispatchBaseClass):
	'''MF Tire Group'''
	CLSID = IID('{00C1AB1B-C9C5-4DC3-942D-496D904A038F}')
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
	def _get_TireBody(self):
		return self._ApplyTypes_(*(4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_TireForce(self):
		return self._ApplyTypes_(*(4051, 2, (9, 0), (), "TireForce", '{F99074AA-1B0D-4BBB-BFDD-8C490375373F}'))
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
	TireBody = property(_get_TireBody, None)
	'''
	Get Tire Body

	:type: recurdyn.ProcessNet.IBody
	'''
	TireForce = property(_get_TireForce, None)
	'''
	Get MF Tire Force

	:type: recurdyn.ProcessNet.IForceTireMF
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
		"TireBody": (4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"TireForce": (4051, 2, (9, 0), (), "TireForce", '{F99074AA-1B0D-4BBB-BFDD-8C490375373F}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
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

class ITireGroupSoil(DispatchBaseClass):
	'''Soil Tire Group'''
	CLSID = IID('{1AF10A49-7812-4489-A02A-63F06B9565B6}')
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
	def _get_TireBody(self):
		return self._ApplyTypes_(*(4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_TireForce(self):
		return self._ApplyTypes_(*(4051, 2, (9, 0), (), "TireForce", '{023C2BF6-0000-41CA-8E0E-C3C047C16C73}'))
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
	TireBody = property(_get_TireBody, None)
	'''
	Get Tire Body

	:type: recurdyn.ProcessNet.IBody
	'''
	TireForce = property(_get_TireForce, None)
	'''
	Get Soil Tire Force

	:type: recurdyn.ProcessNet.IForceTireSoil
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
		"TireBody": (4001, 2, (9, 0), (), "TireBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"TireForce": (4051, 2, (9, 0), (), "TireForce", '{023C2BF6-0000-41CA-8E0E-C3C047C16C73}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
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

class ITireToolkit(DispatchBaseClass):
	'''Tire Toolkit'''
	CLSID = IID('{1EA508EB-91CB-4278-A58E-94EC244D6DF2}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateTireGroupGenericGround(self, strName, pRefFrame):
		'''
		Creates a Generic Tire Group Ground
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.Tire.ITireGroupGeneric
		'''
		ret = self._oleobj_.InvokeTypes(4057, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateTireGroupGenericGround', '{4078C2ED-0A08-4307-B854-1E7E24AF481B}')
		return ret

	def CreateTireGroupGround(self, strName, pRefFrame):
		'''
		Creates a Tire Group Ground
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.Tire.ITireGroup
		'''
		ret = self._oleobj_.InvokeTypes(4052, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateTireGroupGround', '{4DE9BFB3-300F-48DC-9DC2-82FE6DC39C84}')
		return ret

	def CreateTireGroupMFGround(self, strName, pRefFrame):
		'''
		Creates a MF Tire Group Ground
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.Tire.ITireGroupMF
		'''
		ret = self._oleobj_.InvokeTypes(4054, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateTireGroupMFGround', '{00C1AB1B-C9C5-4DC3-942D-496D904A038F}')
		return ret

	def CreateTireGroupSoilGround(self, strName, pRefFrame):
		'''
		CreateTireGroupSoilGround is obsolete function
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.Tire.ITireGroupSoil
		'''
		ret = self._oleobj_.InvokeTypes(4056, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateTireGroupSoilGround', '{1AF10A49-7812-4489-A02A-63F06B9565B6}')
		return ret

	def CreateTireGroupSolidContact(self, strName, pRefFrame, pBaseEntity):
		'''
		Creates a Tire Group SolidContact
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:param pBaseEntity: IGeneric
		:rtype: recurdyn.Tire.ITireGroup
		'''
		ret = self._oleobj_.InvokeTypes(4053, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pRefFrame, pBaseEntity)
		if ret is not None:
			ret = Dispatch(ret, 'CreateTireGroupSolidContact', '{4DE9BFB3-300F-48DC-9DC2-82FE6DC39C84}')
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
		return self._ApplyTypes_(*(4051, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
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
		"GeneralSubSystem": (4051, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
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

class IUserInputParameter(DispatchBaseClass):
	'''user Input Parameter'''
	CLSID = IID('{5810F409-F289-4DB7-819A-CE79BE9370D2}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Arguments(self):
		return self._ApplyTypes_(*(4052, 2, (8200, 0), (), "Arguments", None))
	def _get_UserParameter(self):
		return self._ApplyTypes_(*(4051, 2, (8, 0), (), "UserParameter", None))

	def _set_Arguments(self, value):
		if "Arguments" in self.__dict__: self.__dict__["Arguments"] = value; return
		variantValue = win32com.client.VARIANT(8200, value)
		self._oleobj_.Invoke(*((4052, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UserParameter(self, value):
		if "UserParameter" in self.__dict__: self.__dict__["UserParameter"] = value; return
		self._oleobj_.Invoke(*((4051, LCID, 4, 0) + (value,) + ()))

	Arguments = property(_get_Arguments, _set_Arguments)
	'''
	Arguments list

	:type: list[str]
	'''
	UserParameter = property(_get_UserParameter, _set_UserParameter)
	'''
	User defined parameters needed for the user written subroutine

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Arguments": _set_Arguments,
		"_set_UserParameter": _set_UserParameter,
	}
	_prop_map_get_ = {
		"Arguments": (4052, 2, (8200, 0), (), "Arguments", None),
		"UserParameter": (4051, 2, (8, 0), (), "UserParameter", None),
	}
	_prop_map_put_ = {
		"Arguments": ((4052, LCID, 4, 0),()),
		"UserParameter": ((4051, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

ITire_vtables_dispatch_ = 1
ITire_vtables_ = [
	(( 'TireBody' , 'ppResult' , ), 4001, (4001, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

ITireGeometryRim_vtables_dispatch_ = 1
ITireGeometryRim_vtables_ = [
	(( 'RimWidth' , 'ppVal' , ), 4051, (4051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'RimDiameter' , 'ppVal' , ), 4052, (4052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RimWidthUnitMM' , 'pVal' , ), 4053, (4053, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RimWidthUnitMM' , 'pVal' , ), 4053, (4053, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RimDiameterUnitInch' , 'pVal' , ), 4054, (4054, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RimDiameterUnitInch' , 'pVal' , ), 4054, (4054, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

ITireGeometryRimGeneric_vtables_dispatch_ = 1
ITireGeometryRimGeneric_vtables_ = [
	(( 'NumberOfLeads' , 'pVal' , ), 4101, (4101, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfLeads' , 'pVal' , ), 4101, (4101, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'AngleOfRimHole' , 'ppVal' , ), 4102, (4102, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'RimInnerDiameter' , 'ppVal' , ), 4103, (4103, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RimInnerDiameterUnitInch' , 'pVal' , ), 4104, (4104, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RimInnerDiameterUnitInch' , 'pVal' , ), 4104, (4104, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

ITireGeometryTire_vtables_dispatch_ = 1
ITireGeometryTire_vtables_ = [
	(( 'SectionWidth' , 'ppVal' , ), 4051, (4051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'AspectRatio' , 'ppVal' , ), 4052, (4052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RimDiameter' , 'ppVal' , ), 4053, (4053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'SectionWidthUnitMM' , 'pVal' , ), 4054, (4054, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SectionWidthUnitMM' , 'pVal' , ), 4054, (4054, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RimDiameterUnitInch' , 'pVal' , ), 4055, (4055, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'RimDiameterUnitInch' , 'pVal' , ), 4055, (4055, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UpdateTireRadius' , ), 4056, (4056, (), [ ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

ITireGroup_vtables_dispatch_ = 1
ITireGroup_vtables_ = [
	(( 'TireForce' , 'ppResult' , ), 4051, (4051, (), [ (16393, 10, None, "IID('{57CC4E39-380C-40B8-AE7F-0908ADC0DB18}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

ITireGroupGeneric_vtables_dispatch_ = 1
ITireGroupGeneric_vtables_ = [
	(( 'TireFile' , 'TireFile' , ), 4051, (4051, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'TireFile' , 'TireFile' , ), 4051, (4051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'TireRadius' , 'pVal' , ), 4052, (4052, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'TireWidth' , 'pVal' , ), 4053, (4053, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'AspectRatio' , 'pVal' , ), 4054, (4054, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RimRadius' , 'pVal' , ), 4055, (4055, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseLongitudinalVelocity' , 'pVal' , ), 4056, (4056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseLongitudinalVelocity' , 'pVal' , ), 4056, (4056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'LongitudinalVelocity' , 'ppVal' , ), 4057, (4057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseSpinAxisAngularVelocity' , 'pVal' , ), 4058, (4058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseSpinAxisAngularVelocity' , 'pVal' , ), 4058, (4058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'SpinAxisAngularVelocity' , 'ppVal' , ), 4059, (4059, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Origin' , 'ppVal' , ), 4060, (4060, (), [ (16393, 10, None, "IID('{918CAF9A-7A62-4EC4-B45D-C259C997B661}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'OrientationZ' , 'ppVal' , ), 4061, (4061, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'OrientationY' , 'ppVal' , ), 4062, (4062, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'OrientationX' , 'ppVal' , ), 4063, (4063, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Road' , 'roadname' , ), 4064, (4064, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'Road' , 'roadname' , ), 4064, (4064, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'TireSide' , 'TireSide' , ), 4065, (4065, (), [ (3, 1, None, "IID('{F0B47155-E2C8-499D-B8A2-2B9BBC744C7C}')") , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'TireSide' , 'TireSide' , ), 4065, (4065, (), [ (16387, 10, None, "IID('{F0B47155-E2C8-499D-B8A2-2B9BBC744C7C}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UserInputParameter' , 'ppVal' , ), 4066, (4066, (), [ (16393, 10, None, "IID('{5810F409-F289-4DB7-819A-CE79BE9370D2}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
]

ITireGroupMF_vtables_dispatch_ = 1
ITireGroupMF_vtables_ = [
	(( 'TireForce' , 'ppResult' , ), 4051, (4051, (), [ (16393, 10, None, "IID('{F99074AA-1B0D-4BBB-BFDD-8C490375373F}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

ITireGroupSoil_vtables_dispatch_ = 1
ITireGroupSoil_vtables_ = [
	(( 'TireForce' , 'ppResult' , ), 4051, (4051, (), [ (16393, 10, None, "IID('{023C2BF6-0000-41CA-8E0E-C3C047C16C73}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

ITireToolkit_vtables_dispatch_ = 1
ITireToolkit_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 4051, (4051, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreateTireGroupGround' , 'strName' , 'pRefFrame' , 'ppResult' , ), 4052, (4052, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{4DE9BFB3-300F-48DC-9DC2-82FE6DC39C84}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CreateTireGroupSolidContact' , 'strName' , 'pRefFrame' , 'pBaseEntity' , 'ppResult' , 
			 ), 4053, (4053, (), [ (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (16393, 10, None, "IID('{4DE9BFB3-300F-48DC-9DC2-82FE6DC39C84}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CreateTireGroupMFGround' , 'strName' , 'pRefFrame' , 'ppResult' , ), 4054, (4054, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{00C1AB1B-C9C5-4DC3-942D-496D904A038F}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateTireGroupSoilGround' , 'strName' , 'pRefFrame' , 'ppResult' , ), 4056, (4056, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{1AF10A49-7812-4489-A02A-63F06B9565B6}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateTireGroupGenericGround' , 'strName' , 'pRefFrame' , 'ppResult' , ), 4057, (4057, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{4078C2ED-0A08-4307-B854-1E7E24AF481B}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IUserInputParameter_vtables_dispatch_ = 1
IUserInputParameter_vtables_ = [
	(( 'UserParameter' , 'pVal' , ), 4051, (4051, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UserParameter' , 'pVal' , ), 4051, (4051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Arguments' , 'ppSafeArray' , ), 4052, (4052, (), [ (8200, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Arguments' , 'ppSafeArray' , ), 4052, (4052, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{917E1C84-02D0-4205-B70F-E0C55BC77209}' : ITireGeometryRim,
	'{8F7EAE62-8E94-4E0B-AEC2-0BCE70CE5C62}' : ITireGeometryRimGeneric,
	'{C00BB7B9-649E-4377-8A92-AF637D601E38}' : ITireGeometryTire,
	'{5810F409-F289-4DB7-819A-CE79BE9370D2}' : IUserInputParameter,
	'{C4B87451-54E2-430D-84F3-E9A9087B2476}' : ITire,
	'{00C1AB1B-C9C5-4DC3-942D-496D904A038F}' : ITireGroupMF,
	'{4DE9BFB3-300F-48DC-9DC2-82FE6DC39C84}' : ITireGroup,
	'{1AF10A49-7812-4489-A02A-63F06B9565B6}' : ITireGroupSoil,
	'{4078C2ED-0A08-4307-B854-1E7E24AF481B}' : ITireGroupGeneric,
	'{1EA508EB-91CB-4278-A58E-94EC244D6DF2}' : ITireToolkit,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{917E1C84-02D0-4205-B70F-E0C55BC77209}' : 'ITireGeometryRim',
	'{8F7EAE62-8E94-4E0B-AEC2-0BCE70CE5C62}' : 'ITireGeometryRimGeneric',
	'{C00BB7B9-649E-4377-8A92-AF637D601E38}' : 'ITireGeometryTire',
	'{5810F409-F289-4DB7-819A-CE79BE9370D2}' : 'IUserInputParameter',
	'{C4B87451-54E2-430D-84F3-E9A9087B2476}' : 'ITire',
	'{00C1AB1B-C9C5-4DC3-942D-496D904A038F}' : 'ITireGroupMF',
	'{4DE9BFB3-300F-48DC-9DC2-82FE6DC39C84}' : 'ITireGroup',
	'{1AF10A49-7812-4489-A02A-63F06B9565B6}' : 'ITireGroupSoil',
	'{4078C2ED-0A08-4307-B854-1E7E24AF481B}' : 'ITireGroupGeneric',
	'{1EA508EB-91CB-4278-A58E-94EC244D6DF2}' : 'ITireToolkit',
}


NamesToIIDMap = {
	'ITireGeometryRim' : '{917E1C84-02D0-4205-B70F-E0C55BC77209}',
	'ITireGeometryRimGeneric' : '{8F7EAE62-8E94-4E0B-AEC2-0BCE70CE5C62}',
	'ITireGeometryTire' : '{C00BB7B9-649E-4377-8A92-AF637D601E38}',
	'IUserInputParameter' : '{5810F409-F289-4DB7-819A-CE79BE9370D2}',
	'ITire' : '{C4B87451-54E2-430D-84F3-E9A9087B2476}',
	'ITireGroupMF' : '{00C1AB1B-C9C5-4DC3-942D-496D904A038F}',
	'ITireGroup' : '{4DE9BFB3-300F-48DC-9DC2-82FE6DC39C84}',
	'ITireGroupSoil' : '{1AF10A49-7812-4489-A02A-63F06B9565B6}',
	'ITireGroupGeneric' : '{4078C2ED-0A08-4307-B854-1E7E24AF481B}',
	'ITireToolkit' : '{1EA508EB-91CB-4278-A58E-94EC244D6DF2}',
}


