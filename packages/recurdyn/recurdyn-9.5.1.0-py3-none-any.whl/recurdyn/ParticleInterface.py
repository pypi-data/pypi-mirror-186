# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMParticleInterface.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5 RecurDynCOMParticleInterface Type Library'
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

CLSID = IID('{F9CA71A8-A705-4F56-B8F7-9FFF22622493}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IParticleInterface2DProfile(DispatchBaseClass):
	'''2D Profile'''
	CLSID = IID('{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}')
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


	def HidePlotDialog(self):
		'''
		Hide the plot dialog
		'''
		return self._oleobj_.InvokeTypes(7512, LCID, 1, (24, 0), (),)


	def ShowPlotDialog(self):
		'''
		Show the plot dialog
		'''
		return self._oleobj_.InvokeTypes(7511, LCID, 1, (24, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(7509, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Division(self):
		return self._ApplyTypes_(*(7506, 2, (3, 0), (), "Division", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(7513, 2, (3, 0), (), "GroupSequence", None))
	def _get_Halfdepth(self):
		return self._ApplyTypes_(*(7504, 2, (5, 0), (), "Halfdepth", None))
	def _get_Length(self):
		return self._ApplyTypes_(*(7505, 2, (5, 0), (), "Length", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NormalDirection(self):
		return self._ApplyTypes_(*(7502, 2, (8197, 0), (), "NormalDirection", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Position(self):
		return self._ApplyTypes_(*(7501, 2, (8197, 0), (), "Position", None))
	def _get_ReferenceBody(self):
		return self._ApplyTypes_(*(7508, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_ReferenceDirection(self):
		return self._ApplyTypes_(*(7503, 2, (8197, 0), (), "ReferenceDirection", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(7510, 2, (11, 0), (), "Visible", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((7509, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Division(self, value):
		if "Division" in self.__dict__: self.__dict__["Division"] = value; return
		self._oleobj_.Invoke(*((7506, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((7513, LCID, 4, 0) + (value,) + ()))
	def _set_Halfdepth(self, value):
		if "Halfdepth" in self.__dict__: self.__dict__["Halfdepth"] = value; return
		self._oleobj_.Invoke(*((7504, LCID, 4, 0) + (value,) + ()))
	def _set_Length(self, value):
		if "Length" in self.__dict__: self.__dict__["Length"] = value; return
		self._oleobj_.Invoke(*((7505, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NormalDirection(self, value):
		if "NormalDirection" in self.__dict__: self.__dict__["NormalDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((7502, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((7501, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ReferenceBody(self, value):
		if "ReferenceBody" in self.__dict__: self.__dict__["ReferenceBody"] = value; return
		self._oleobj_.Invoke(*((7508, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceDirection(self, value):
		if "ReferenceDirection" in self.__dict__: self.__dict__["ReferenceDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((7503, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((7510, LCID, 4, 0) + (value,) + ()))

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
	Division = property(_get_Division, _set_Division)
	'''
	Division of the 2D Profile

	:type: int
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GroupSequence = property(_get_GroupSequence, _set_GroupSequence)
	'''
	Sequence of the Particle Group

	:type: int
	'''
	Halfdepth = property(_get_Halfdepth, _set_Halfdepth)
	'''
	Halfdepth of the 2D Profile

	:type: float
	'''
	Length = property(_get_Length, _set_Length)
	'''
	Reference length of the 2D Profile

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NormalDirection = property(_get_NormalDirection, _set_NormalDirection)
	'''
	Normal direction of the 2D profile

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
	Position = property(_get_Position, _set_Position)
	'''
	Position of the 2D profile

	:type: list[float]
	'''
	ReferenceBody = property(_get_ReferenceBody, _set_ReferenceBody)
	'''
	Reference Body

	:type: recurdyn.ProcessNet.IBody
	'''
	ReferenceDirection = property(_get_ReferenceDirection, _set_ReferenceDirection)
	'''
	Reference direction of the 2D profile

	:type: list[float]
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	Visible Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_Division": _set_Division,
		"_set_GroupSequence": _set_GroupSequence,
		"_set_Halfdepth": _set_Halfdepth,
		"_set_Length": _set_Length,
		"_set_Name": _set_Name,
		"_set_NormalDirection": _set_NormalDirection,
		"_set_Position": _set_Position,
		"_set_ReferenceBody": _set_ReferenceBody,
		"_set_ReferenceDirection": _set_ReferenceDirection,
		"_set_UserData": _set_UserData,
		"_set_Visible": _set_Visible,
	}
	_prop_map_get_ = {
		"Color": (7509, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Division": (7506, 2, (3, 0), (), "Division", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (7513, 2, (3, 0), (), "GroupSequence", None),
		"Halfdepth": (7504, 2, (5, 0), (), "Halfdepth", None),
		"Length": (7505, 2, (5, 0), (), "Length", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NormalDirection": (7502, 2, (8197, 0), (), "NormalDirection", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Position": (7501, 2, (8197, 0), (), "Position", None),
		"ReferenceBody": (7508, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"ReferenceDirection": (7503, 2, (8197, 0), (), "ReferenceDirection", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (7510, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Color": ((7509, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Division": ((7506, LCID, 4, 0),()),
		"GroupSequence": ((7513, LCID, 4, 0),()),
		"Halfdepth": ((7504, LCID, 4, 0),()),
		"Length": ((7505, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NormalDirection": ((7502, LCID, 4, 0),()),
		"Position": ((7501, LCID, 4, 0),()),
		"ReferenceBody": ((7508, LCID, 4, 0),()),
		"ReferenceDirection": ((7503, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((7510, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleInterface2DProfileCollection(DispatchBaseClass):
	'''2D Profile Collection'''
	CLSID = IID('{F889ED2E-42FD-462C-8E19-9006064D7DDF}')
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
		:rtype: recurdyn.ParticleInterface.IParticleInterface2DProfile
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}')
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
		:rtype: recurdyn.ParticleInterface.IParticleInterface2DProfile
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}')
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
		return win32com.client.util.Iterator(ob, '{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IParticleInterfaceMassCenter(DispatchBaseClass):
	'''Mass Center'''
	CLSID = IID('{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddGroup(self, sequence, density):
		'''
		Add a particle group and define its density
		
		:param sequence: int
		:param density: float
		'''
		return self._oleobj_.InvokeTypes(7501, LCID, 1, (24, 0), ((3, 1), (4, 1)),sequence
			, density)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(7503, 2, (19, 0), (), "Color", None))
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
	def _get_Visible(self):
		return self._ApplyTypes_(*(7504, 2, (11, 0), (), "Visible", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(7502, 2, (4, 0), (), "Width", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((7503, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((7504, LCID, 4, 0) + (value,) + ()))
	def _set_Width(self, value):
		if "Width" in self.__dict__: self.__dict__["Width"] = value; return
		self._oleobj_.Invoke(*((7502, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Color of the Mass Center

	:type: int
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
	Visible = property(_get_Visible, _set_Visible)
	'''
	Visible Flag of the Mass Center

	:type: bool
	'''
	Width = property(_get_Width, _set_Width)
	'''
	Width of the Mass Center

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
		"_set_Visible": _set_Visible,
		"_set_Width": _set_Width,
	}
	_prop_map_get_ = {
		"Color": (7503, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (7504, 2, (11, 0), (), "Visible", None),
		"Width": (7502, 2, (4, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((7503, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((7504, LCID, 4, 0),()),
		"Width": ((7502, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleInterfaceMassCenterCollection(DispatchBaseClass):
	'''Mass Center Collection'''
	CLSID = IID('{D4B0D8AB-5C95-4E16-8B1F-A907B1C9C6D8}')
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
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceMassCenter
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}')
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
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceMassCenter
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}')
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
		return win32com.client.util.Iterator(ob, '{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IParticleInterfaceSensor(DispatchBaseClass):
	'''Particle Sensor'''
	CLSID = IID('{B15BC09F-3F76-4F2B-8F0E-D7A407B0009C}')
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


	def HidePlotDialog(self):
		'''
		Hide the plot dialog
		'''
		return self._oleobj_.InvokeTypes(7507, LCID, 1, (24, 0), (),)


	def ShowPlotDialog(self):
		'''
		Show the plot dialog
		'''
		return self._oleobj_.InvokeTypes(7506, LCID, 1, (24, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(7504, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(7508, 2, (3, 0), (), "GroupSequence", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Position(self):
		return self._ApplyTypes_(*(7501, 2, (8197, 0), (), "Position", None))
	def _get_ReferenceBody(self):
		return self._ApplyTypes_(*(7503, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(7505, 2, (11, 0), (), "Visible", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((7504, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((7508, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((7501, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ReferenceBody(self, value):
		if "ReferenceBody" in self.__dict__: self.__dict__["ReferenceBody"] = value; return
		self._oleobj_.Invoke(*((7503, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((7505, LCID, 4, 0) + (value,) + ()))

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
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GroupSequence = property(_get_GroupSequence, _set_GroupSequence)
	'''
	Sequence of the Particle Group

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
	Position = property(_get_Position, _set_Position)
	'''
	Sensor Position

	:type: list[float]
	'''
	ReferenceBody = property(_get_ReferenceBody, _set_ReferenceBody)
	'''
	Reference Body

	:type: recurdyn.ProcessNet.IBody
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	Visible Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_GroupSequence": _set_GroupSequence,
		"_set_Name": _set_Name,
		"_set_Position": _set_Position,
		"_set_ReferenceBody": _set_ReferenceBody,
		"_set_UserData": _set_UserData,
		"_set_Visible": _set_Visible,
	}
	_prop_map_get_ = {
		"Color": (7504, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (7508, 2, (3, 0), (), "GroupSequence", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Position": (7501, 2, (8197, 0), (), "Position", None),
		"ReferenceBody": (7503, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (7505, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Color": ((7504, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"GroupSequence": ((7508, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Position": ((7501, LCID, 4, 0),()),
		"ReferenceBody": ((7503, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((7505, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleInterfaceSensorBox(DispatchBaseClass):
	'''Particle Box Sensor'''
	CLSID = IID('{39AB1B83-6261-4FF8-B908-D6554BE92FC1}')
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


	def HidePlotDialog(self):
		'''
		Hide the plot dialog
		'''
		return self._oleobj_.InvokeTypes(7507, LCID, 1, (24, 0), (),)


	def ShowPlotDialog(self):
		'''
		Show the plot dialog
		'''
		return self._oleobj_.InvokeTypes(7506, LCID, 1, (24, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(7504, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Depth(self):
		return self._ApplyTypes_(*(7555, 2, (5, 0), (), "Depth", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(7508, 2, (3, 0), (), "GroupSequence", None))
	def _get_Height(self):
		return self._ApplyTypes_(*(7554, 2, (5, 0), (), "Height", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NormalDirection(self):
		return self._ApplyTypes_(*(7551, 2, (8197, 0), (), "NormalDirection", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Position(self):
		return self._ApplyTypes_(*(7501, 2, (8197, 0), (), "Position", None))
	def _get_ReferenceBody(self):
		return self._ApplyTypes_(*(7503, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_ReferenceDirection(self):
		return self._ApplyTypes_(*(7552, 2, (8197, 0), (), "ReferenceDirection", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(7505, 2, (11, 0), (), "Visible", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(7553, 2, (5, 0), (), "Width", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((7504, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Depth(self, value):
		if "Depth" in self.__dict__: self.__dict__["Depth"] = value; return
		self._oleobj_.Invoke(*((7555, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((7508, LCID, 4, 0) + (value,) + ()))
	def _set_Height(self, value):
		if "Height" in self.__dict__: self.__dict__["Height"] = value; return
		self._oleobj_.Invoke(*((7554, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NormalDirection(self, value):
		if "NormalDirection" in self.__dict__: self.__dict__["NormalDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((7551, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((7501, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ReferenceBody(self, value):
		if "ReferenceBody" in self.__dict__: self.__dict__["ReferenceBody"] = value; return
		self._oleobj_.Invoke(*((7503, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceDirection(self, value):
		if "ReferenceDirection" in self.__dict__: self.__dict__["ReferenceDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((7552, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((7505, LCID, 4, 0) + (value,) + ()))
	def _set_Width(self, value):
		if "Width" in self.__dict__: self.__dict__["Width"] = value; return
		self._oleobj_.Invoke(*((7553, LCID, 4, 0) + (value,) + ()))

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
	Depth = property(_get_Depth, _set_Depth)
	'''
	Depth of box sensor

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GroupSequence = property(_get_GroupSequence, _set_GroupSequence)
	'''
	Sequence of the Particle Group

	:type: int
	'''
	Height = property(_get_Height, _set_Height)
	'''
	Height of box sensor

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NormalDirection = property(_get_NormalDirection, _set_NormalDirection)
	'''
	Sensor Normal Direction

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
	Position = property(_get_Position, _set_Position)
	'''
	Sensor Position

	:type: list[float]
	'''
	ReferenceBody = property(_get_ReferenceBody, _set_ReferenceBody)
	'''
	Reference Body

	:type: recurdyn.ProcessNet.IBody
	'''
	ReferenceDirection = property(_get_ReferenceDirection, _set_ReferenceDirection)
	'''
	Sensor Reference Direction

	:type: list[float]
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	Visible Flag

	:type: bool
	'''
	Width = property(_get_Width, _set_Width)
	'''
	Width of box sensor

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_Depth": _set_Depth,
		"_set_GroupSequence": _set_GroupSequence,
		"_set_Height": _set_Height,
		"_set_Name": _set_Name,
		"_set_NormalDirection": _set_NormalDirection,
		"_set_Position": _set_Position,
		"_set_ReferenceBody": _set_ReferenceBody,
		"_set_ReferenceDirection": _set_ReferenceDirection,
		"_set_UserData": _set_UserData,
		"_set_Visible": _set_Visible,
		"_set_Width": _set_Width,
	}
	_prop_map_get_ = {
		"Color": (7504, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Depth": (7555, 2, (5, 0), (), "Depth", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (7508, 2, (3, 0), (), "GroupSequence", None),
		"Height": (7554, 2, (5, 0), (), "Height", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NormalDirection": (7551, 2, (8197, 0), (), "NormalDirection", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Position": (7501, 2, (8197, 0), (), "Position", None),
		"ReferenceBody": (7503, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"ReferenceDirection": (7552, 2, (8197, 0), (), "ReferenceDirection", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (7505, 2, (11, 0), (), "Visible", None),
		"Width": (7553, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((7504, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Depth": ((7555, LCID, 4, 0),()),
		"GroupSequence": ((7508, LCID, 4, 0),()),
		"Height": ((7554, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NormalDirection": ((7551, LCID, 4, 0),()),
		"Position": ((7501, LCID, 4, 0),()),
		"ReferenceBody": ((7503, LCID, 4, 0),()),
		"ReferenceDirection": ((7552, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((7505, LCID, 4, 0),()),
		"Width": ((7553, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleInterfaceSensorCollection(DispatchBaseClass):
	'''Particle Sensor Collection'''
	CLSID = IID('{6F1AA193-3FF9-4A68-9FA4-AD8ED98B65A6}')
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
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceSensor
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B15BC09F-3F76-4F2B-8F0E-D7A407B0009C}')
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
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceSensor
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B15BC09F-3F76-4F2B-8F0E-D7A407B0009C}')
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
		return win32com.client.util.Iterator(ob, '{B15BC09F-3F76-4F2B-8F0E-D7A407B0009C}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{B15BC09F-3F76-4F2B-8F0E-D7A407B0009C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IParticleInterfaceSensorSphere(DispatchBaseClass):
	'''Particle Sphere Sensor'''
	CLSID = IID('{BDA0F283-E603-4616-B415-ABAB8C89AFFE}')
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


	def HidePlotDialog(self):
		'''
		Hide the plot dialog
		'''
		return self._oleobj_.InvokeTypes(7507, LCID, 1, (24, 0), (),)


	def ShowPlotDialog(self):
		'''
		Show the plot dialog
		'''
		return self._oleobj_.InvokeTypes(7506, LCID, 1, (24, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(7504, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(7508, 2, (3, 0), (), "GroupSequence", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Position(self):
		return self._ApplyTypes_(*(7501, 2, (8197, 0), (), "Position", None))
	def _get_Radius(self):
		return self._ApplyTypes_(*(7551, 2, (5, 0), (), "Radius", None))
	def _get_ReferenceBody(self):
		return self._ApplyTypes_(*(7503, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(7505, 2, (11, 0), (), "Visible", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((7504, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((7508, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((7501, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Radius(self, value):
		if "Radius" in self.__dict__: self.__dict__["Radius"] = value; return
		self._oleobj_.Invoke(*((7551, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceBody(self, value):
		if "ReferenceBody" in self.__dict__: self.__dict__["ReferenceBody"] = value; return
		self._oleobj_.Invoke(*((7503, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((7505, LCID, 4, 0) + (value,) + ()))

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
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GroupSequence = property(_get_GroupSequence, _set_GroupSequence)
	'''
	Sequence of the Particle Group

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
	Position = property(_get_Position, _set_Position)
	'''
	Sensor Position

	:type: list[float]
	'''
	Radius = property(_get_Radius, _set_Radius)
	'''
	Radius of sphere sensor

	:type: float
	'''
	ReferenceBody = property(_get_ReferenceBody, _set_ReferenceBody)
	'''
	Reference Body

	:type: recurdyn.ProcessNet.IBody
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	Visible Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_GroupSequence": _set_GroupSequence,
		"_set_Name": _set_Name,
		"_set_Position": _set_Position,
		"_set_Radius": _set_Radius,
		"_set_ReferenceBody": _set_ReferenceBody,
		"_set_UserData": _set_UserData,
		"_set_Visible": _set_Visible,
	}
	_prop_map_get_ = {
		"Color": (7504, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (7508, 2, (3, 0), (), "GroupSequence", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Position": (7501, 2, (8197, 0), (), "Position", None),
		"Radius": (7551, 2, (5, 0), (), "Radius", None),
		"ReferenceBody": (7503, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (7505, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Color": ((7504, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"GroupSequence": ((7508, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Position": ((7501, LCID, 4, 0),()),
		"Radius": ((7551, LCID, 4, 0),()),
		"ReferenceBody": ((7503, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((7505, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleInterfaceToolkit(DispatchBaseClass):
	'''ParticleInterface Toolkit'''
	CLSID = IID('{82CE3033-5263-4F9F-98F6-D54AAFCAE6F7}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateBoxSensor(self, name, ReferenceBody):
		'''
		Creates a box sensor
		
		:param name: str
		:param ReferenceBody: IBody
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceSensorBox
		'''
		ret = self._oleobj_.InvokeTypes(7568, LCID, 1, (9, 0), ((8, 1), (9, 1)),name
			, ReferenceBody)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBoxSensor', '{39AB1B83-6261-4FF8-B908-D6554BE92FC1}')
		return ret

	def CreateMassCenter(self, name):
		'''
		Creates a MassCenter
		
		:param name: str
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceMassCenter
		'''
		ret = self._oleobj_.InvokeTypes(7572, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMassCenter', '{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}')
		return ret

	def CreateProfile(self, name, ReferenceBody):
		'''
		Creates a 2D profile
		
		:param name: str
		:param ReferenceBody: IBody
		:rtype: recurdyn.ParticleInterface.IParticleInterface2DProfile
		'''
		ret = self._oleobj_.InvokeTypes(7565, LCID, 1, (9, 0), ((8, 1), (9, 1)),name
			, ReferenceBody)
		if ret is not None:
			ret = Dispatch(ret, 'CreateProfile', '{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}')
		return ret

	def CreateSphereSensor(self, name, ReferenceBody):
		'''
		Creates a sphere sensor
		
		:param name: str
		:param ReferenceBody: IBody
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceSensorSphere
		'''
		ret = self._oleobj_.InvokeTypes(7567, LCID, 1, (9, 0), ((8, 1), (9, 1)),name
			, ReferenceBody)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSphereSensor', '{BDA0F283-E603-4616-B415-ABAB8C89AFFE}')
		return ret

	def CreateTrace(self, name):
		'''
		Creates a Trace
		
		:param name: str
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceTrace
		'''
		ret = self._oleobj_.InvokeTypes(7570, LCID, 1, (9, 0), ((8, 1),),name
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateTrace', '{296B8986-4D37-409A-BB6F-73B7F815E662}')
		return ret

	def CreateVessel(self, name, Entity):
		'''
		Creates a vessel
		
		:param name: str
		:param Entity: IGeneric
		:rtype: recurdyn.ParticleInterface.IVessel
		'''
		ret = self._oleobj_.InvokeTypes(7561, LCID, 1, (9, 0), ((8, 1), (9, 1)),name
			, Entity)
		if ret is not None:
			ret = Dispatch(ret, 'CreateVessel', '{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}')
		return ret

	def ExportVesselFiles(self, folderName):
		'''
		Export vessel OBJ files with target folder
		
		:param folderName: str
		'''
		return self._oleobj_.InvokeTypes(7562, LCID, 1, (24, 0), ((8, 1),),folderName
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def UpdatePostData(self):
		'''
		Update post data
		'''
		return self._oleobj_.InvokeTypes(7563, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ConnectParticleworks(self):
		return self._ApplyTypes_(*(7553, 2, (11, 0), (), "ConnectParticleworks", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_HideParticles(self):
		return self._ApplyTypes_(*(7552, 2, (11, 0), (), "HideParticles", None))
	def _get_InitialParticleFile(self):
		return self._ApplyTypes_(*(7556, 2, (8, 0), (), "InitialParticleFile", None))
	def _get_MassCenterCollection(self):
		return self._ApplyTypes_(*(7571, 2, (9, 0), (), "MassCenterCollection", '{D4B0D8AB-5C95-4E16-8B1F-A907B1C9C6D8}'))
	def _get_MatchStepSize(self):
		return self._ApplyTypes_(*(7554, 2, (11, 0), (), "MatchStepSize", None))
	def _get_ModifyContainerFile(self):
		return self._ApplyTypes_(*(7555, 2, (11, 0), (), "ModifyContainerFile", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ProfileCollection(self):
		return self._ApplyTypes_(*(7564, 2, (9, 0), (), "ProfileCollection", '{F889ED2E-42FD-462C-8E19-9006064D7DDF}'))
	def _get_SensorCollection(self):
		return self._ApplyTypes_(*(7566, 2, (9, 0), (), "SensorCollection", '{6F1AA193-3FF9-4A68-9FA4-AD8ED98B65A6}'))
	def _get_TraceCollection(self):
		return self._ApplyTypes_(*(7569, 2, (9, 0), (), "TraceCollection", '{9B9E9C52-CA24-4D4B-BDCD-133407D8CE63}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VesselCollection(self):
		return self._ApplyTypes_(*(7551, 2, (9, 0), (), "VesselCollection", '{C50813B7-8819-46F5-A9F7-78322BFEFEA3}'))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ConnectParticleworks(self, value):
		if "ConnectParticleworks" in self.__dict__: self.__dict__["ConnectParticleworks"] = value; return
		self._oleobj_.Invoke(*((7553, LCID, 4, 0) + (value,) + ()))
	def _set_HideParticles(self, value):
		if "HideParticles" in self.__dict__: self.__dict__["HideParticles"] = value; return
		self._oleobj_.Invoke(*((7552, LCID, 4, 0) + (value,) + ()))
	def _set_InitialParticleFile(self, value):
		if "InitialParticleFile" in self.__dict__: self.__dict__["InitialParticleFile"] = value; return
		self._oleobj_.Invoke(*((7556, LCID, 4, 0) + (value,) + ()))
	def _set_MatchStepSize(self, value):
		if "MatchStepSize" in self.__dict__: self.__dict__["MatchStepSize"] = value; return
		self._oleobj_.Invoke(*((7554, LCID, 4, 0) + (value,) + ()))
	def _set_ModifyContainerFile(self, value):
		if "ModifyContainerFile" in self.__dict__: self.__dict__["ModifyContainerFile"] = value; return
		self._oleobj_.Invoke(*((7555, LCID, 4, 0) + (value,) + ()))
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
	ConnectParticleworks = property(_get_ConnectParticleworks, _set_ConnectParticleworks)
	'''
	Co-simulate with Particleworks

	:type: bool
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	HideParticles = property(_get_HideParticles, _set_HideParticles)
	'''
	Hide particles during animation

	:type: bool
	'''
	InitialParticleFile = property(_get_InitialParticleFile, _set_InitialParticleFile)
	'''
	Initial particle file

	:type: str
	'''
	MassCenterCollection = property(_get_MassCenterCollection, None)
	'''
	MassCenter Collection

	:type: recurdyn.ParticleInterface.IParticleInterfaceMassCenterCollection
	'''
	MatchStepSize = property(_get_MatchStepSize, _set_MatchStepSize)
	'''
	Synchronize the solving step size during co-simulation

	:type: bool
	'''
	ModifyContainerFile = property(_get_ModifyContainerFile, _set_ModifyContainerFile)
	'''
	Modify the Particleworks pw.container file automatically

	:type: bool
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
	ProfileCollection = property(_get_ProfileCollection, None)
	'''
	2D Profile Collection

	:type: recurdyn.ParticleInterface.IParticleInterface2DProfileCollection
	'''
	SensorCollection = property(_get_SensorCollection, None)
	'''
	Sensor Collection

	:type: recurdyn.ParticleInterface.IParticleInterfaceSensorCollection
	'''
	TraceCollection = property(_get_TraceCollection, None)
	'''
	Trace Collection

	:type: recurdyn.ParticleInterface.IParticleInterfaceTraceCollection
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VesselCollection = property(_get_VesselCollection, None)
	'''
	Vessel Collection

	:type: recurdyn.ParticleInterface.IVesselCollection
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_ConnectParticleworks": _set_ConnectParticleworks,
		"_set_HideParticles": _set_HideParticles,
		"_set_InitialParticleFile": _set_InitialParticleFile,
		"_set_MatchStepSize": _set_MatchStepSize,
		"_set_ModifyContainerFile": _set_ModifyContainerFile,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConnectParticleworks": (7553, 2, (11, 0), (), "ConnectParticleworks", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"HideParticles": (7552, 2, (11, 0), (), "HideParticles", None),
		"InitialParticleFile": (7556, 2, (8, 0), (), "InitialParticleFile", None),
		"MassCenterCollection": (7571, 2, (9, 0), (), "MassCenterCollection", '{D4B0D8AB-5C95-4E16-8B1F-A907B1C9C6D8}'),
		"MatchStepSize": (7554, 2, (11, 0), (), "MatchStepSize", None),
		"ModifyContainerFile": (7555, 2, (11, 0), (), "ModifyContainerFile", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ProfileCollection": (7564, 2, (9, 0), (), "ProfileCollection", '{F889ED2E-42FD-462C-8E19-9006064D7DDF}'),
		"SensorCollection": (7566, 2, (9, 0), (), "SensorCollection", '{6F1AA193-3FF9-4A68-9FA4-AD8ED98B65A6}'),
		"TraceCollection": (7569, 2, (9, 0), (), "TraceCollection", '{9B9E9C52-CA24-4D4B-BDCD-133407D8CE63}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VesselCollection": (7551, 2, (9, 0), (), "VesselCollection", '{C50813B7-8819-46F5-A9F7-78322BFEFEA3}'),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ConnectParticleworks": ((7553, LCID, 4, 0),()),
		"HideParticles": ((7552, LCID, 4, 0),()),
		"InitialParticleFile": ((7556, LCID, 4, 0),()),
		"MatchStepSize": ((7554, LCID, 4, 0),()),
		"ModifyContainerFile": ((7555, LCID, 4, 0),()),
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

class IParticleInterfaceTrace(DispatchBaseClass):
	'''Trace'''
	CLSID = IID('{296B8986-4D37-409A-BB6F-73B7F815E662}')
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


	def _get_Color(self):
		return self._ApplyTypes_(*(7504, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(7501, 2, (3, 0), (), "GroupSequence", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ParticleIndex(self):
		return self._ApplyTypes_(*(7502, 2, (3, 0), (), "ParticleIndex", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(7505, 2, (11, 0), (), "Visible", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(7503, 2, (4, 0), (), "Width", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((7504, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((7501, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ParticleIndex(self, value):
		if "ParticleIndex" in self.__dict__: self.__dict__["ParticleIndex"] = value; return
		self._oleobj_.Invoke(*((7502, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((7505, LCID, 4, 0) + (value,) + ()))
	def _set_Width(self, value):
		if "Width" in self.__dict__: self.__dict__["Width"] = value; return
		self._oleobj_.Invoke(*((7503, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Color of the Trace Line

	:type: int
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
	GroupSequence = property(_get_GroupSequence, _set_GroupSequence)
	'''
	Sequence of the Particle Group

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
	ParticleIndex = property(_get_ParticleIndex, _set_ParticleIndex)
	'''
	Index of the Particle

	:type: int
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	Visible Flag of the Trace Line

	:type: bool
	'''
	Width = property(_get_Width, _set_Width)
	'''
	Width of the Trace Line

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_GroupSequence": _set_GroupSequence,
		"_set_Name": _set_Name,
		"_set_ParticleIndex": _set_ParticleIndex,
		"_set_UserData": _set_UserData,
		"_set_Visible": _set_Visible,
		"_set_Width": _set_Width,
	}
	_prop_map_get_ = {
		"Color": (7504, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (7501, 2, (3, 0), (), "GroupSequence", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ParticleIndex": (7502, 2, (3, 0), (), "ParticleIndex", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (7505, 2, (11, 0), (), "Visible", None),
		"Width": (7503, 2, (4, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((7504, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"GroupSequence": ((7501, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ParticleIndex": ((7502, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((7505, LCID, 4, 0),()),
		"Width": ((7503, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleInterfaceTraceCollection(DispatchBaseClass):
	'''Trace Collection'''
	CLSID = IID('{9B9E9C52-CA24-4D4B-BDCD-133407D8CE63}')
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
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceTrace
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{296B8986-4D37-409A-BB6F-73B7F815E662}')
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
		:rtype: recurdyn.ParticleInterface.IParticleInterfaceTrace
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{296B8986-4D37-409A-BB6F-73B7F815E662}')
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
		return win32com.client.util.Iterator(ob, '{296B8986-4D37-409A-BB6F-73B7F815E662}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{296B8986-4D37-409A-BB6F-73B7F815E662}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IVessel(DispatchBaseClass):
	'''Vessel'''
	CLSID = IID('{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}')
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
	def _get_Entity(self):
		return self._ApplyTypes_(*(7501, 2, (9, 0), (), "Entity", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_FileName(self):
		return self._ApplyTypes_(*(7503, 2, (8, 0), (), "FileName", None))
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
	def _get_PatchOption(self):
		return self._ApplyTypes_(*(7502, 2, (9, 0), (), "PatchOption", '{A581D2E2-BA02-4246-A22E-5B07167097F0}'))
	def _get_SynchName(self):
		return self._ApplyTypes_(*(7504, 2, (11, 0), (), "SynchName", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Entity(self, value):
		if "Entity" in self.__dict__: self.__dict__["Entity"] = value; return
		self._oleobj_.Invoke(*((7501, LCID, 4, 0) + (value,) + ()))
	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((7503, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_SynchName(self, value):
		if "SynchName" in self.__dict__: self.__dict__["SynchName"] = value; return
		self._oleobj_.Invoke(*((7504, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Entity = property(_get_Entity, _set_Entity)
	'''
	Target entity of vessel

	:type: recurdyn.ProcessNet.IGeneric
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	OBJ file name for export

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
	PatchOption = property(_get_PatchOption, None)
	'''
	Vessel patch option

	:type: recurdyn.ParticleInterface.IVesselPatchOption
	'''
	SynchName = property(_get_SynchName, _set_SynchName)
	'''
	Flag to synchronize file name

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Entity": _set_Entity,
		"_set_FileName": _set_FileName,
		"_set_Name": _set_Name,
		"_set_SynchName": _set_SynchName,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Entity": (7501, 2, (9, 0), (), "Entity", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"FileName": (7503, 2, (8, 0), (), "FileName", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PatchOption": (7502, 2, (9, 0), (), "PatchOption", '{A581D2E2-BA02-4246-A22E-5B07167097F0}'),
		"SynchName": (7504, 2, (11, 0), (), "SynchName", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Entity": ((7501, LCID, 4, 0),()),
		"FileName": ((7503, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"SynchName": ((7504, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IVesselCollection(DispatchBaseClass):
	'''IVesselCollection'''
	CLSID = IID('{C50813B7-8819-46F5-A9F7-78322BFEFEA3}')
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
		:rtype: recurdyn.ParticleInterface.IVessel
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}')
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
		:rtype: recurdyn.ParticleInterface.IVessel
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}')
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
		return win32com.client.util.Iterator(ob, '{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IVesselPatchOption(DispatchBaseClass):
	'''Vessel patch option'''
	CLSID = IID('{A581D2E2-BA02-4246-A22E-5B07167097F0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_MaxFacetSizeFactor(self):
		return self._ApplyTypes_(*(7504, 2, (9, 0), (), "MaxFacetSizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlaneToleranceFactor(self):
		return self._ApplyTypes_(*(7502, 2, (9, 0), (), "PlaneToleranceFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseMaxFacetSizeFactor(self):
		return self._ApplyTypes_(*(7503, 2, (11, 0), (), "UseMaxFacetSizeFactor", None))
	def _get_UsePlaneToleranceFactor(self):
		return self._ApplyTypes_(*(7501, 2, (11, 0), (), "UsePlaneToleranceFactor", None))

	def _set_UseMaxFacetSizeFactor(self, value):
		if "UseMaxFacetSizeFactor" in self.__dict__: self.__dict__["UseMaxFacetSizeFactor"] = value; return
		self._oleobj_.Invoke(*((7503, LCID, 4, 0) + (value,) + ()))
	def _set_UsePlaneToleranceFactor(self, value):
		if "UsePlaneToleranceFactor" in self.__dict__: self.__dict__["UsePlaneToleranceFactor"] = value; return
		self._oleobj_.Invoke(*((7501, LCID, 4, 0) + (value,) + ()))

	MaxFacetSizeFactor = property(_get_MaxFacetSizeFactor, None)
	'''
	You can specify the maximum facet size factor as a value from 0 to 10. This value controls the maximum size of triangular patch length.

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlaneToleranceFactor = property(_get_PlaneToleranceFactor, None)
	'''
	You can specify the plane tolerance factor as a value from 0 to 10. A smaller value produces a more refined patch.

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseMaxFacetSizeFactor = property(_get_UseMaxFacetSizeFactor, _set_UseMaxFacetSizeFactor)
	'''
	Use maximum facet size factor

	:type: bool
	'''
	UsePlaneToleranceFactor = property(_get_UsePlaneToleranceFactor, _set_UsePlaneToleranceFactor)
	'''
	Use plane tolerance factor

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_UseMaxFacetSizeFactor": _set_UseMaxFacetSizeFactor,
		"_set_UsePlaneToleranceFactor": _set_UsePlaneToleranceFactor,
	}
	_prop_map_get_ = {
		"MaxFacetSizeFactor": (7504, 2, (9, 0), (), "MaxFacetSizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlaneToleranceFactor": (7502, 2, (9, 0), (), "PlaneToleranceFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseMaxFacetSizeFactor": (7503, 2, (11, 0), (), "UseMaxFacetSizeFactor", None),
		"UsePlaneToleranceFactor": (7501, 2, (11, 0), (), "UsePlaneToleranceFactor", None),
	}
	_prop_map_put_ = {
		"UseMaxFacetSizeFactor": ((7503, LCID, 4, 0),()),
		"UsePlaneToleranceFactor": ((7501, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

IParticleInterface2DProfile_vtables_dispatch_ = 1
IParticleInterface2DProfile_vtables_ = [
	(( 'Position' , 'Position' , ), 7501, (7501, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'Position' , ), 7501, (7501, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'normal' , ), 7502, (7502, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'normal' , ), 7502, (7502, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'direction' , ), 7503, (7503, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'direction' , ), 7503, (7503, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Halfdepth' , 'Halfdepth' , ), 7504, (7504, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Halfdepth' , 'Halfdepth' , ), 7504, (7504, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'Length' , ), 7505, (7505, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Length' , 'Length' , ), 7505, (7505, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Division' , 'Division' , ), 7506, (7506, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Division' , 'Division' , ), 7506, (7506, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceBody' , 'body' , ), 7508, (7508, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceBody' , 'body' , ), 7508, (7508, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 7509, (7509, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 7509, (7509, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'flag' , ), 7510, (7510, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'flag' , ), 7510, (7510, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ShowPlotDialog' , ), 7511, (7511, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'HidePlotDialog' , ), 7512, (7512, (), [ ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'GroupSequence' , 'sequence' , ), 7513, (7513, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GroupSequence' , 'sequence' , ), 7513, (7513, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IParticleInterface2DProfileCollection_vtables_dispatch_ = 1
IParticleInterface2DProfileCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IParticleInterfaceMassCenter_vtables_dispatch_ = 1
IParticleInterfaceMassCenter_vtables_ = [
	(( 'AddGroup' , 'sequence' , 'density' , ), 7501, (7501, (), [ (3, 1, None, None) , 
			 (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 7502, (7502, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 7502, (7502, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 7503, (7503, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 7503, (7503, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'flag' , ), 7504, (7504, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'flag' , ), 7504, (7504, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IParticleInterfaceMassCenterCollection_vtables_dispatch_ = 1
IParticleInterfaceMassCenterCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IParticleInterfaceSensor_vtables_dispatch_ = 1
IParticleInterfaceSensor_vtables_ = [
	(( 'Position' , 'Position' , ), 7501, (7501, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'Position' , ), 7501, (7501, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceBody' , 'body' , ), 7503, (7503, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceBody' , 'body' , ), 7503, (7503, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 7504, (7504, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 7504, (7504, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'flag' , ), 7505, (7505, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'flag' , ), 7505, (7505, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ShowPlotDialog' , ), 7506, (7506, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'HidePlotDialog' , ), 7507, (7507, (), [ ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'GroupSequence' , 'sequence' , ), 7508, (7508, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GroupSequence' , 'sequence' , ), 7508, (7508, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
]

IParticleInterfaceSensorBox_vtables_dispatch_ = 1
IParticleInterfaceSensorBox_vtables_ = [
	(( 'NormalDirection' , 'normal' , ), 7551, (7551, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'normal' , ), 7551, (7551, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'direction' , ), 7552, (7552, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'direction' , ), 7552, (7552, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 7553, (7553, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 7553, (7553, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 7554, (7554, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 7554, (7554, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'Depth' , ), 7555, (7555, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'Depth' , ), 7555, (7555, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IParticleInterfaceSensorCollection_vtables_dispatch_ = 1
IParticleInterfaceSensorCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{B15BC09F-3F76-4F2B-8F0E-D7A407B0009C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IParticleInterfaceSensorSphere_vtables_dispatch_ = 1
IParticleInterfaceSensorSphere_vtables_ = [
	(( 'Radius' , 'Radius' , ), 7551, (7551, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'Radius' , ), 7551, (7551, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IParticleInterfaceToolkit_vtables_dispatch_ = 1
IParticleInterfaceToolkit_vtables_ = [
	(( 'VesselCollection' , 'vessels' , ), 7551, (7551, (), [ (16393, 10, None, "IID('{C50813B7-8819-46F5-A9F7-78322BFEFEA3}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'HideParticles' , 'flag' , ), 7552, (7552, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'HideParticles' , 'flag' , ), 7552, (7552, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ConnectParticleworks' , 'flag' , ), 7553, (7553, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ConnectParticleworks' , 'flag' , ), 7553, (7553, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MatchStepSize' , 'flag' , ), 7554, (7554, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'MatchStepSize' , 'flag' , ), 7554, (7554, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ModifyContainerFile' , 'flag' , ), 7555, (7555, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ModifyContainerFile' , 'flag' , ), 7555, (7555, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'InitialParticleFile' , 'FileName' , ), 7556, (7556, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'InitialParticleFile' , 'FileName' , ), 7556, (7556, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CreateVessel' , 'name' , 'Entity' , 'vessel' , ), 7561, (7561, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (16393, 10, None, "IID('{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ExportVesselFiles' , 'folderName' , ), 7562, (7562, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UpdatePostData' , ), 7563, (7563, (), [ ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ProfileCollection' , 'profiles' , ), 7564, (7564, (), [ (16393, 10, None, "IID('{F889ED2E-42FD-462C-8E19-9006064D7DDF}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CreateProfile' , 'name' , 'ReferenceBody' , 'profile' , ), 7565, (7565, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , (16393, 10, None, "IID('{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'SensorCollection' , 'sensors' , ), 7566, (7566, (), [ (16393, 10, None, "IID('{6F1AA193-3FF9-4A68-9FA4-AD8ED98B65A6}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'CreateSphereSensor' , 'name' , 'ReferenceBody' , 'sensor' , ), 7567, (7567, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , (16393, 10, None, "IID('{BDA0F283-E603-4616-B415-ABAB8C89AFFE}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CreateBoxSensor' , 'name' , 'ReferenceBody' , 'sensor' , ), 7568, (7568, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , (16393, 10, None, "IID('{39AB1B83-6261-4FF8-B908-D6554BE92FC1}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'TraceCollection' , 'traces' , ), 7569, (7569, (), [ (16393, 10, None, "IID('{9B9E9C52-CA24-4D4B-BDCD-133407D8CE63}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CreateTrace' , 'name' , 'trace' , ), 7570, (7570, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{296B8986-4D37-409A-BB6F-73B7F815E662}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'MassCenterCollection' , 'massCenters' , ), 7571, (7571, (), [ (16393, 10, None, "IID('{D4B0D8AB-5C95-4E16-8B1F-A907B1C9C6D8}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'CreateMassCenter' , 'name' , 'MassCenter' , ), 7572, (7572, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}')") , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IParticleInterfaceTrace_vtables_dispatch_ = 1
IParticleInterfaceTrace_vtables_ = [
	(( 'GroupSequence' , 'sequence' , ), 7501, (7501, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'GroupSequence' , 'sequence' , ), 7501, (7501, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ParticleIndex' , 'ParticleIndex' , ), 7502, (7502, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ParticleIndex' , 'ParticleIndex' , ), 7502, (7502, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 7503, (7503, (), [ (4, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 7503, (7503, (), [ (16388, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 7504, (7504, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'Color' , ), 7504, (7504, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'flag' , ), 7505, (7505, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'flag' , ), 7505, (7505, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IParticleInterfaceTraceCollection_vtables_dispatch_ = 1
IParticleInterfaceTraceCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{296B8986-4D37-409A-BB6F-73B7F815E662}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IVessel_vtables_dispatch_ = 1
IVessel_vtables_ = [
	(( 'Entity' , 'Entity' , ), 7501, (7501, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Entity' , 'Entity' , ), 7501, (7501, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PatchOption' , 'option' , ), 7502, (7502, (), [ (16393, 10, None, "IID('{A581D2E2-BA02-4246-A22E-5B07167097F0}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'FileName' , ), 7503, (7503, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'FileName' , ), 7503, (7503, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'SynchName' , 'fSynchName' , ), 7504, (7504, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SynchName' , 'fSynchName' , ), 7504, (7504, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IVesselCollection_vtables_dispatch_ = 1
IVesselCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IVesselPatchOption_vtables_dispatch_ = 1
IVesselPatchOption_vtables_ = [
	(( 'UsePlaneToleranceFactor' , 'flag' , ), 7501, (7501, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UsePlaneToleranceFactor' , 'flag' , ), 7501, (7501, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PlaneToleranceFactor' , 'value' , ), 7502, (7502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseMaxFacetSizeFactor' , 'flag' , ), 7503, (7503, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseMaxFacetSizeFactor' , 'flag' , ), 7503, (7503, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MaxFacetSizeFactor' , 'value' , ), 7504, (7504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{A581D2E2-BA02-4246-A22E-5B07167097F0}' : IVesselPatchOption,
	'{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}' : IVessel,
	'{C50813B7-8819-46F5-A9F7-78322BFEFEA3}' : IVesselCollection,
	'{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}' : IParticleInterfaceMassCenter,
	'{D4B0D8AB-5C95-4E16-8B1F-A907B1C9C6D8}' : IParticleInterfaceMassCenterCollection,
	'{296B8986-4D37-409A-BB6F-73B7F815E662}' : IParticleInterfaceTrace,
	'{9B9E9C52-CA24-4D4B-BDCD-133407D8CE63}' : IParticleInterfaceTraceCollection,
	'{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}' : IParticleInterface2DProfile,
	'{F889ED2E-42FD-462C-8E19-9006064D7DDF}' : IParticleInterface2DProfileCollection,
	'{B15BC09F-3F76-4F2B-8F0E-D7A407B0009C}' : IParticleInterfaceSensor,
	'{BDA0F283-E603-4616-B415-ABAB8C89AFFE}' : IParticleInterfaceSensorSphere,
	'{39AB1B83-6261-4FF8-B908-D6554BE92FC1}' : IParticleInterfaceSensorBox,
	'{6F1AA193-3FF9-4A68-9FA4-AD8ED98B65A6}' : IParticleInterfaceSensorCollection,
	'{82CE3033-5263-4F9F-98F6-D54AAFCAE6F7}' : IParticleInterfaceToolkit,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{A581D2E2-BA02-4246-A22E-5B07167097F0}' : 'IVesselPatchOption',
	'{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}' : 'IVessel',
	'{C50813B7-8819-46F5-A9F7-78322BFEFEA3}' : 'IVesselCollection',
	'{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}' : 'IParticleInterfaceMassCenter',
	'{D4B0D8AB-5C95-4E16-8B1F-A907B1C9C6D8}' : 'IParticleInterfaceMassCenterCollection',
	'{296B8986-4D37-409A-BB6F-73B7F815E662}' : 'IParticleInterfaceTrace',
	'{9B9E9C52-CA24-4D4B-BDCD-133407D8CE63}' : 'IParticleInterfaceTraceCollection',
	'{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}' : 'IParticleInterface2DProfile',
	'{F889ED2E-42FD-462C-8E19-9006064D7DDF}' : 'IParticleInterface2DProfileCollection',
	'{B15BC09F-3F76-4F2B-8F0E-D7A407B0009C}' : 'IParticleInterfaceSensor',
	'{BDA0F283-E603-4616-B415-ABAB8C89AFFE}' : 'IParticleInterfaceSensorSphere',
	'{39AB1B83-6261-4FF8-B908-D6554BE92FC1}' : 'IParticleInterfaceSensorBox',
	'{6F1AA193-3FF9-4A68-9FA4-AD8ED98B65A6}' : 'IParticleInterfaceSensorCollection',
	'{82CE3033-5263-4F9F-98F6-D54AAFCAE6F7}' : 'IParticleInterfaceToolkit',
}


NamesToIIDMap = {
	'IVesselPatchOption' : '{A581D2E2-BA02-4246-A22E-5B07167097F0}',
	'IVessel' : '{3DCC7BAF-C0EB-4BD2-9412-CE718C6E8E2E}',
	'IVesselCollection' : '{C50813B7-8819-46F5-A9F7-78322BFEFEA3}',
	'IParticleInterfaceMassCenter' : '{B0D86EF7-51AF-4ABA-B3E0-1D47FBE3E21C}',
	'IParticleInterfaceMassCenterCollection' : '{D4B0D8AB-5C95-4E16-8B1F-A907B1C9C6D8}',
	'IParticleInterfaceTrace' : '{296B8986-4D37-409A-BB6F-73B7F815E662}',
	'IParticleInterfaceTraceCollection' : '{9B9E9C52-CA24-4D4B-BDCD-133407D8CE63}',
	'IParticleInterface2DProfile' : '{6D43D4B7-BB44-43D7-9E83-D91F37FA0148}',
	'IParticleInterface2DProfileCollection' : '{F889ED2E-42FD-462C-8E19-9006064D7DDF}',
	'IParticleInterfaceSensor' : '{B15BC09F-3F76-4F2B-8F0E-D7A407B0009C}',
	'IParticleInterfaceSensorSphere' : '{BDA0F283-E603-4616-B415-ABAB8C89AFFE}',
	'IParticleInterfaceSensorBox' : '{39AB1B83-6261-4FF8-B908-D6554BE92FC1}',
	'IParticleInterfaceSensorCollection' : '{6F1AA193-3FF9-4A68-9FA4-AD8ED98B65A6}',
	'IParticleInterfaceToolkit' : '{82CE3033-5263-4F9F-98F6-D54AAFCAE6F7}',
}


