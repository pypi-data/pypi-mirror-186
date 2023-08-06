# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMExternalSPI.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5 RecurDynCOMExternalSPI Type Library'
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

CLSID = IID('{481074A4-9011-468F-82A3-404626869494}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IExternalSPIToolkit(DispatchBaseClass):
	'''ExternalSPI Toolkit'''
	CLSID = IID('{5493C868-80A1-408B-8B91-722738B17635}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateMassCenter(self, Name):
		'''
		Creates a MassCenter
		
		:param Name: str
		:rtype: recurdyn.ExternalSPI.IMassCenterExternal
		'''
		ret = self._oleobj_.InvokeTypes(13066, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMassCenter', '{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}')
		return ret

	def CreateParticleSensorBox(self, Name, referenceBody):
		'''
		Creates a box ParticleSensor
		
		:param Name: str
		:param referenceBody: IBody
		:rtype: recurdyn.ExternalSPI.IParticleSensorExternalBox
		'''
		ret = self._oleobj_.InvokeTypes(13069, LCID, 1, (9, 0), ((8, 1), (9, 1)),Name
			, referenceBody)
		if ret is not None:
			ret = Dispatch(ret, 'CreateParticleSensorBox', '{25F31E37-59B8-4666-A55A-FC5872D4EAA9}')
		return ret

	def CreateParticleSensorSphere(self, Name, referenceBody):
		'''
		Creates a sphere ParticleSensor
		
		:param Name: str
		:param referenceBody: IBody
		:rtype: recurdyn.ExternalSPI.IParticleSensorExternalSphere
		'''
		ret = self._oleobj_.InvokeTypes(13068, LCID, 1, (9, 0), ((8, 1), (9, 1)),Name
			, referenceBody)
		if ret is not None:
			ret = Dispatch(ret, 'CreateParticleSensorSphere', '{E076254E-15EB-4468-B567-F8D0C0AAACB1}')
		return ret

	def CreateProfile2D(self, Name, referenceBody):
		'''
		Creates a 2D profile
		
		:param Name: str
		:param referenceBody: IBody
		:rtype: recurdyn.ExternalSPI.IProfile2DExternal
		'''
		ret = self._oleobj_.InvokeTypes(13071, LCID, 1, (9, 0), ((8, 1), (9, 1)),Name
			, referenceBody)
		if ret is not None:
			ret = Dispatch(ret, 'CreateProfile2D', '{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}')
		return ret

	def CreateTrace(self, Name):
		'''
		Creates a Trace
		
		:param Name: str
		:rtype: recurdyn.ExternalSPI.ITraceExternal
		'''
		ret = self._oleobj_.InvokeTypes(13064, LCID, 1, (9, 0), ((8, 1),),Name
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateTrace', '{F3349896-A8B5-4D86-99D5-FD78580AA1A8}')
		return ret

	def CreateWall(self, Name, entity):
		'''
		Creates a wall
		
		:param Name: str
		:param entity: IGeneric
		:rtype: recurdyn.ParticleBase.IWall
		'''
		ret = self._oleobj_.InvokeTypes(13061, LCID, 1, (9, 0), ((8, 1), (9, 1)),Name
			, entity)
		if ret is not None:
			ret = Dispatch(ret, 'CreateWall', '{9E1686A2-8CE5-4D33-993A-8583147C5EEA}')
		return ret

	def ExportParticlePostData(self, path, titles, groupSequences):
		'''
		Export Particle Post Data
		
		:param path: str
		:param titles: list[str]
		:param groupSequences: list[int]
		'''
		return self._oleobj_.InvokeTypes(13078, LCID, 1, (24, 0), ((8, 1), (8200, 1), (8195, 1)),path
			, titles, groupSequences)


	def ExportWallFile(self, folderName):
		'''
		Export wall file with target folder
		
		:param folderName: str
		'''
		return self._oleobj_.InvokeTypes(13062, LCID, 1, (24, 0), ((8, 1),),folderName
			)


	def ExportWallPostData(self, path, titles, wallSequences):
		'''
		Export Wall Post Data
		
		:param path: str
		:param titles: list[str]
		:param wallSequences: list[int]
		'''
		return self._oleobj_.InvokeTypes(13079, LCID, 1, (24, 0), ((8, 1), (8200, 1), (8195, 1)),path
			, titles, wallSequences)


	def FluidDisplay(self, GroupSequence):
		'''
		Fluid Display
		
		:param GroupSequence: int
		:rtype: recurdyn.ExternalSPI.IParticleFluidDisplay
		'''
		ret = self._oleobj_.InvokeTypes(13081, LCID, 1, (9, 0), ((3, 1),),GroupSequence
			)
		if ret is not None:
			ret = Dispatch(ret, 'FluidDisplay', '{F474A409-5990-45C4-BE20-FC1B85C0D977}')
		return ret

	def GetClipMinMaxValue(self, GroupSequence, particleDataTitle):
		'''
		Get Clip Min Max Value of target Data name
		
		:param GroupSequence: int
		:param particleDataTitle: str
		:rtype: (float, float, bool)
		'''
		return self._ApplyTypes_(13075, 1, (24, 0), ((3, 1), (8, 1), (16389, 2), (16389, 2), (16395, 2)), 'GetClipMinMaxValue', None,GroupSequence
			, particleDataTitle, pythoncom.Missing, pythoncom.Missing, pythoncom.Missing)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def SetClipMinMaxValue(self, GroupSequence, particleDataTitle, minValue, maxValue, fUse):
		'''
		Set Clip Min Max Value of target Data name
		
		:param GroupSequence: int
		:param particleDataTitle: str
		:param minValue: float
		:param maxValue: float
		:param fUse: bool
		'''
		return self._oleobj_.InvokeTypes(13074, LCID, 1, (24, 0), ((3, 1), (8, 1), (5, 1), (5, 1), (11, 1)),GroupSequence
			, particleDataTitle, minValue, maxValue, fUse)


	def UpdatePostData(self):
		'''
		Update post data
		'''
		return self._oleobj_.InvokeTypes(13080, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Connect(self):
		return self._ApplyTypes_(*(13082, 2, (11, 0), (), "Connect", None))
	def _get_ContourParticle(self):
		return self._ApplyTypes_(*(13076, 2, (9, 0), (), "ContourParticle", '{9B435673-BCFA-4FDF-A34F-0A6758DC9AE4}'))
	def _get_ContourWall(self):
		return self._ApplyTypes_(*(13077, 2, (9, 0), (), "ContourWall", '{9B5F3020-811C-495A-80A2-21CE0C1D585B}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_HideParticleSets(self):
		return self._ApplyTypes_(*(13083, 2, (11, 0), (), "HideParticleSets", None))
	def _get_MassCenterCollection(self):
		return self._ApplyTypes_(*(13065, 2, (9, 0), (), "MassCenterCollection", '{6D30D962-900A-4303-9DAA-181B862E36B7}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ParticlePostDataTitleCollection(self):
		return self._ApplyTypes_(*(13072, 2, (8200, 0), (), "ParticlePostDataTitleCollection", None))
	def _get_ParticleSensorCollection(self):
		return self._ApplyTypes_(*(13067, 2, (9, 0), (), "ParticleSensorCollection", '{8F3D2213-D9EF-47CD-93C7-8E3E91F4706C}'))
	def _get_ParticleSetExternalCollection(self):
		return self._ApplyTypes_(*(13053, 2, (9, 0), (), "ParticleSetExternalCollection", '{2410BF87-ECBC-4C94-AD7B-2772AEB1705A}'))
	def _get_Profile2DCollection(self):
		return self._ApplyTypes_(*(13070, 2, (9, 0), (), "Profile2DCollection", '{73DD3F05-6291-40A0-AB1A-DB6F2431F2B9}'))
	def _get_Program(self):
		return self._ApplyTypes_(*(13051, 2, (8, 0), (), "Program", None))
	def _get_TraceCollection(self):
		return self._ApplyTypes_(*(13063, 2, (9, 0), (), "TraceCollection", '{19CE10D3-0B31-4762-8AAC-71D8E22E62DF}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_WallCollection(self):
		return self._ApplyTypes_(*(13052, 2, (9, 0), (), "WallCollection", '{66991464-4D29-4DC9-8D9D-D0A77DD811FF}'))
	def _get_WallPostDataTitleCollection(self):
		return self._ApplyTypes_(*(13073, 2, (8200, 0), (), "WallPostDataTitleCollection", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Connect(self, value):
		if "Connect" in self.__dict__: self.__dict__["Connect"] = value; return
		self._oleobj_.Invoke(*((13082, LCID, 4, 0) + (value,) + ()))
	def _set_HideParticleSets(self, value):
		if "HideParticleSets" in self.__dict__: self.__dict__["HideParticleSets"] = value; return
		self._oleobj_.Invoke(*((13083, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Program(self, value):
		if "Program" in self.__dict__: self.__dict__["Program"] = value; return
		self._oleobj_.Invoke(*((13051, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Connect = property(_get_Connect, _set_Connect)
	'''
	Current program's Switch of Co-Simulation

	:type: bool
	'''
	ContourParticle = property(_get_ContourParticle, None)
	ContourWall = property(_get_ContourWall, None)
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	HideParticleSets = property(_get_HideParticleSets, _set_HideParticleSets)
	'''
	If true, RecurDyn hide all particle sets.

	:type: bool
	'''
	MassCenterCollection = property(_get_MassCenterCollection, None)
	'''
	MassCenter Collection

	:type: recurdyn.ExternalSPI.IMassCenterCollection
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
	ParticlePostDataTitleCollection = property(_get_ParticlePostDataTitleCollection, None)
	'''
	Particle Post Data Name Collection

	:type: list[str]
	'''
	ParticleSensorCollection = property(_get_ParticleSensorCollection, None)
	'''
	ParticleSensor Collection

	:type: recurdyn.ExternalSPI.IParticleSensorCollection
	'''
	ParticleSetExternalCollection = property(_get_ParticleSetExternalCollection, None)
	'''
	ParticleSetExternal Collection

	:type: recurdyn.ExternalSPI.IParticleSetExternalCollection
	'''
	Profile2DCollection = property(_get_Profile2DCollection, None)
	'''
	2D Profile Collection

	:type: recurdyn.ExternalSPI.IProfile2DCollection
	'''
	Program = property(_get_Program, _set_Program)
	'''
	Current Program

	:type: str
	'''
	TraceCollection = property(_get_TraceCollection, None)
	'''
	Trace Collection

	:type: recurdyn.ExternalSPI.ITraceCollection
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	WallCollection = property(_get_WallCollection, None)
	'''
	Wall Collection

	:type: recurdyn.ExternalSPI.IWallCollection
	'''
	WallPostDataTitleCollection = property(_get_WallPostDataTitleCollection, None)
	'''
	Wall Post Data Name Collection

	:type: list[str]
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Connect": _set_Connect,
		"_set_HideParticleSets": _set_HideParticleSets,
		"_set_Name": _set_Name,
		"_set_Program": _set_Program,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Connect": (13082, 2, (11, 0), (), "Connect", None),
		"ContourParticle": (13076, 2, (9, 0), (), "ContourParticle", '{9B435673-BCFA-4FDF-A34F-0A6758DC9AE4}'),
		"ContourWall": (13077, 2, (9, 0), (), "ContourWall", '{9B5F3020-811C-495A-80A2-21CE0C1D585B}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"HideParticleSets": (13083, 2, (11, 0), (), "HideParticleSets", None),
		"MassCenterCollection": (13065, 2, (9, 0), (), "MassCenterCollection", '{6D30D962-900A-4303-9DAA-181B862E36B7}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ParticlePostDataTitleCollection": (13072, 2, (8200, 0), (), "ParticlePostDataTitleCollection", None),
		"ParticleSensorCollection": (13067, 2, (9, 0), (), "ParticleSensorCollection", '{8F3D2213-D9EF-47CD-93C7-8E3E91F4706C}'),
		"ParticleSetExternalCollection": (13053, 2, (9, 0), (), "ParticleSetExternalCollection", '{2410BF87-ECBC-4C94-AD7B-2772AEB1705A}'),
		"Profile2DCollection": (13070, 2, (9, 0), (), "Profile2DCollection", '{73DD3F05-6291-40A0-AB1A-DB6F2431F2B9}'),
		"Program": (13051, 2, (8, 0), (), "Program", None),
		"TraceCollection": (13063, 2, (9, 0), (), "TraceCollection", '{19CE10D3-0B31-4762-8AAC-71D8E22E62DF}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"WallCollection": (13052, 2, (9, 0), (), "WallCollection", '{66991464-4D29-4DC9-8D9D-D0A77DD811FF}'),
		"WallPostDataTitleCollection": (13073, 2, (8200, 0), (), "WallPostDataTitleCollection", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Connect": ((13082, LCID, 4, 0),()),
		"HideParticleSets": ((13083, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Program": ((13051, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IMassCenterCollection(DispatchBaseClass):
	'''Mass Center Collection'''
	CLSID = IID('{6D30D962-900A-4303-9DAA-181B862E36B7}')
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
		:rtype: recurdyn.ExternalSPI.IMassCenterExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}')
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
		:rtype: recurdyn.ExternalSPI.IMassCenterExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}')
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
		return win32com.client.util.Iterator(ob, '{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IMassCenterExternal(DispatchBaseClass):
	'''Mass Center'''
	CLSID = IID('{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddParticleSet(self, GroupSequence, density):
		'''
		Add a particle set and define its density
		
		:param GroupSequence: int
		:param density: float
		'''
		return self._oleobj_.InvokeTypes(13001, LCID, 1, (24, 0), ((3, 1), (4, 1)),GroupSequence
			, density)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(12502, 2, (19, 0), (), "Color", None))
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
		return self._ApplyTypes_(*(12503, 2, (11, 0), (), "Visible", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(12501, 2, (4, 0), (), "Width", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((12502, LCID, 4, 0) + (value,) + ()))
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
		self._oleobj_.Invoke(*((12503, LCID, 4, 0) + (value,) + ()))
	def _set_Width(self, value):
		if "Width" in self.__dict__: self.__dict__["Width"] = value; return
		self._oleobj_.Invoke(*((12501, LCID, 4, 0) + (value,) + ()))

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
		"Color": (12502, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (12503, 2, (11, 0), (), "Visible", None),
		"Width": (12501, 2, (4, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((12502, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((12503, LCID, 4, 0),()),
		"Width": ((12501, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleFluidDisplay(DispatchBaseClass):
	'''Fluid Display'''
	CLSID = IID('{F474A409-5990-45C4-BE20-FC1B85C0D977}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Create(self):
		'''
		Create Fluid Data
		'''
		return self._oleobj_.InvokeTypes(13009, LCID, 1, (24, 0), (),)


	def Import(self):
		'''
		Import Fluid Data
		'''
		return self._oleobj_.InvokeTypes(13010, LCID, 1, (24, 0), (),)


	def _get_Alpha(self):
		return self._ApplyTypes_(*(13001, 2, (5, 0), (), "Alpha", None))
	def _get_CellSize(self):
		return self._ApplyTypes_(*(13003, 2, (5, 0), (), "CellSize", None))
	def _get_Directory(self):
		return self._ApplyTypes_(*(13008, 2, (8, 0), (), "Directory", None))
	def _get_DrawLine(self):
		return self._ApplyTypes_(*(13011, 2, (11, 0), (), "DrawLine", None))
	def _get_EndFrame(self):
		return self._ApplyTypes_(*(13006, 2, (3, 0), (), "EndFrame", None))
	def _get_Show(self):
		return self._ApplyTypes_(*(13004, 2, (11, 0), (), "Show", None))
	def _get_SmoothRendering(self):
		return self._ApplyTypes_(*(13012, 2, (11, 0), (), "SmoothRendering", None))
	def _get_StartFrame(self):
		return self._ApplyTypes_(*(13005, 2, (3, 0), (), "StartFrame", None))
	def _get_Threshold(self):
		return self._ApplyTypes_(*(13002, 2, (5, 0), (), "Threshold", None))
	def _get_UseDirectory(self):
		return self._ApplyTypes_(*(13007, 2, (11, 0), (), "UseDirectory", None))

	def _set_Alpha(self, value):
		if "Alpha" in self.__dict__: self.__dict__["Alpha"] = value; return
		self._oleobj_.Invoke(*((13001, LCID, 4, 0) + (value,) + ()))
	def _set_CellSize(self, value):
		if "CellSize" in self.__dict__: self.__dict__["CellSize"] = value; return
		self._oleobj_.Invoke(*((13003, LCID, 4, 0) + (value,) + ()))
	def _set_Directory(self, value):
		if "Directory" in self.__dict__: self.__dict__["Directory"] = value; return
		self._oleobj_.Invoke(*((13008, LCID, 4, 0) + (value,) + ()))
	def _set_DrawLine(self, value):
		if "DrawLine" in self.__dict__: self.__dict__["DrawLine"] = value; return
		self._oleobj_.Invoke(*((13011, LCID, 4, 0) + (value,) + ()))
	def _set_EndFrame(self, value):
		if "EndFrame" in self.__dict__: self.__dict__["EndFrame"] = value; return
		self._oleobj_.Invoke(*((13006, LCID, 4, 0) + (value,) + ()))
	def _set_Show(self, value):
		if "Show" in self.__dict__: self.__dict__["Show"] = value; return
		self._oleobj_.Invoke(*((13004, LCID, 4, 0) + (value,) + ()))
	def _set_SmoothRendering(self, value):
		if "SmoothRendering" in self.__dict__: self.__dict__["SmoothRendering"] = value; return
		self._oleobj_.Invoke(*((13012, LCID, 4, 0) + (value,) + ()))
	def _set_StartFrame(self, value):
		if "StartFrame" in self.__dict__: self.__dict__["StartFrame"] = value; return
		self._oleobj_.Invoke(*((13005, LCID, 4, 0) + (value,) + ()))
	def _set_Threshold(self, value):
		if "Threshold" in self.__dict__: self.__dict__["Threshold"] = value; return
		self._oleobj_.Invoke(*((13002, LCID, 4, 0) + (value,) + ()))
	def _set_UseDirectory(self, value):
		if "UseDirectory" in self.__dict__: self.__dict__["UseDirectory"] = value; return
		self._oleobj_.Invoke(*((13007, LCID, 4, 0) + (value,) + ()))

	Alpha = property(_get_Alpha, _set_Alpha)
	'''
	Alpah Parameter

	:type: float
	'''
	CellSize = property(_get_CellSize, _set_CellSize)
	'''
	Cell size

	:type: float
	'''
	Directory = property(_get_Directory, _set_Directory)
	'''
	Directory

	:type: str
	'''
	DrawLine = property(_get_DrawLine, _set_DrawLine)
	'''
	Draw Line

	:type: bool
	'''
	EndFrame = property(_get_EndFrame, _set_EndFrame)
	'''
	End Frame

	:type: int
	'''
	Show = property(_get_Show, _set_Show)
	'''
	Show Fulid Disply

	:type: bool
	'''
	SmoothRendering = property(_get_SmoothRendering, _set_SmoothRendering)
	'''
	Vertex Normal

	:type: bool
	'''
	StartFrame = property(_get_StartFrame, _set_StartFrame)
	'''
	Start Frame

	:type: int
	'''
	Threshold = property(_get_Threshold, _set_Threshold)
	'''
	Threshold Value

	:type: float
	'''
	UseDirectory = property(_get_UseDirectory, _set_UseDirectory)
	'''
	Use Directory

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Alpha": _set_Alpha,
		"_set_CellSize": _set_CellSize,
		"_set_Directory": _set_Directory,
		"_set_DrawLine": _set_DrawLine,
		"_set_EndFrame": _set_EndFrame,
		"_set_Show": _set_Show,
		"_set_SmoothRendering": _set_SmoothRendering,
		"_set_StartFrame": _set_StartFrame,
		"_set_Threshold": _set_Threshold,
		"_set_UseDirectory": _set_UseDirectory,
	}
	_prop_map_get_ = {
		"Alpha": (13001, 2, (5, 0), (), "Alpha", None),
		"CellSize": (13003, 2, (5, 0), (), "CellSize", None),
		"Directory": (13008, 2, (8, 0), (), "Directory", None),
		"DrawLine": (13011, 2, (11, 0), (), "DrawLine", None),
		"EndFrame": (13006, 2, (3, 0), (), "EndFrame", None),
		"Show": (13004, 2, (11, 0), (), "Show", None),
		"SmoothRendering": (13012, 2, (11, 0), (), "SmoothRendering", None),
		"StartFrame": (13005, 2, (3, 0), (), "StartFrame", None),
		"Threshold": (13002, 2, (5, 0), (), "Threshold", None),
		"UseDirectory": (13007, 2, (11, 0), (), "UseDirectory", None),
	}
	_prop_map_put_ = {
		"Alpha": ((13001, LCID, 4, 0),()),
		"CellSize": ((13003, LCID, 4, 0),()),
		"Directory": ((13008, LCID, 4, 0),()),
		"DrawLine": ((13011, LCID, 4, 0),()),
		"EndFrame": ((13006, LCID, 4, 0),()),
		"Show": ((13004, LCID, 4, 0),()),
		"SmoothRendering": ((13012, LCID, 4, 0),()),
		"StartFrame": ((13005, LCID, 4, 0),()),
		"Threshold": ((13002, LCID, 4, 0),()),
		"UseDirectory": ((13007, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleSensorCollection(DispatchBaseClass):
	'''Particle Sensor Collection'''
	CLSID = IID('{8F3D2213-D9EF-47CD-93C7-8E3E91F4706C}')
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
		:rtype: recurdyn.ExternalSPI.IParticleSensorExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E1FD328A-243E-4924-AA28-F1F71CD925FD}')
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
		:rtype: recurdyn.ExternalSPI.IParticleSensorExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E1FD328A-243E-4924-AA28-F1F71CD925FD}')
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
		return win32com.client.util.Iterator(ob, '{E1FD328A-243E-4924-AA28-F1F71CD925FD}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{E1FD328A-243E-4924-AA28-F1F71CD925FD}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IParticleSensorExternal(DispatchBaseClass):
	'''Particle Sensor'''
	CLSID = IID('{E1FD328A-243E-4924-AA28-F1F71CD925FD}')
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
		return self._oleobj_.InvokeTypes(12512, LCID, 1, (24, 0), (),)


	def ShowPlotDialog(self):
		'''
		Show the plot dialog
		'''
		return self._oleobj_.InvokeTypes(12511, LCID, 1, (24, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(12503, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(13001, 2, (3, 0), (), "GroupSequence", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Position(self):
		return self._ApplyTypes_(*(12501, 2, (8197, 0), (), "Position", None))
	def _get_ReferenceBody(self):
		return self._ApplyTypes_(*(12502, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(12504, 2, (11, 0), (), "Visible", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((12503, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((13001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((12501, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ReferenceBody(self, value):
		if "ReferenceBody" in self.__dict__: self.__dict__["ReferenceBody"] = value; return
		self._oleobj_.Invoke(*((12502, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((12504, LCID, 4, 0) + (value,) + ()))

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
		"Color": (12503, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (13001, 2, (3, 0), (), "GroupSequence", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Position": (12501, 2, (8197, 0), (), "Position", None),
		"ReferenceBody": (12502, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (12504, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Color": ((12503, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"GroupSequence": ((13001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Position": ((12501, LCID, 4, 0),()),
		"ReferenceBody": ((12502, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((12504, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleSensorExternalBox(DispatchBaseClass):
	'''Particle Sensor'''
	CLSID = IID('{25F31E37-59B8-4666-A55A-FC5872D4EAA9}')
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
		return self._oleobj_.InvokeTypes(12512, LCID, 1, (24, 0), (),)


	def ShowPlotDialog(self):
		'''
		Show the plot dialog
		'''
		return self._oleobj_.InvokeTypes(12511, LCID, 1, (24, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(12503, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Depth(self):
		return self._ApplyTypes_(*(13055, 2, (5, 0), (), "Depth", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(13001, 2, (3, 0), (), "GroupSequence", None))
	def _get_Height(self):
		return self._ApplyTypes_(*(13054, 2, (5, 0), (), "Height", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NormalDirection(self):
		return self._ApplyTypes_(*(13051, 2, (8197, 0), (), "NormalDirection", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Position(self):
		return self._ApplyTypes_(*(12501, 2, (8197, 0), (), "Position", None))
	def _get_ReferenceBody(self):
		return self._ApplyTypes_(*(12502, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_ReferenceDirection(self):
		return self._ApplyTypes_(*(13052, 2, (8197, 0), (), "ReferenceDirection", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(12504, 2, (11, 0), (), "Visible", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(13053, 2, (5, 0), (), "Width", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((12503, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Depth(self, value):
		if "Depth" in self.__dict__: self.__dict__["Depth"] = value; return
		self._oleobj_.Invoke(*((13055, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((13001, LCID, 4, 0) + (value,) + ()))
	def _set_Height(self, value):
		if "Height" in self.__dict__: self.__dict__["Height"] = value; return
		self._oleobj_.Invoke(*((13054, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NormalDirection(self, value):
		if "NormalDirection" in self.__dict__: self.__dict__["NormalDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((13051, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((12501, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ReferenceBody(self, value):
		if "ReferenceBody" in self.__dict__: self.__dict__["ReferenceBody"] = value; return
		self._oleobj_.Invoke(*((12502, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceDirection(self, value):
		if "ReferenceDirection" in self.__dict__: self.__dict__["ReferenceDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((13052, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((12504, LCID, 4, 0) + (value,) + ()))
	def _set_Width(self, value):
		if "Width" in self.__dict__: self.__dict__["Width"] = value; return
		self._oleobj_.Invoke(*((13053, LCID, 4, 0) + (value,) + ()))

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
		"Color": (12503, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Depth": (13055, 2, (5, 0), (), "Depth", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (13001, 2, (3, 0), (), "GroupSequence", None),
		"Height": (13054, 2, (5, 0), (), "Height", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NormalDirection": (13051, 2, (8197, 0), (), "NormalDirection", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Position": (12501, 2, (8197, 0), (), "Position", None),
		"ReferenceBody": (12502, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"ReferenceDirection": (13052, 2, (8197, 0), (), "ReferenceDirection", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (12504, 2, (11, 0), (), "Visible", None),
		"Width": (13053, 2, (5, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((12503, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Depth": ((13055, LCID, 4, 0),()),
		"GroupSequence": ((13001, LCID, 4, 0),()),
		"Height": ((13054, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NormalDirection": ((13051, LCID, 4, 0),()),
		"Position": ((12501, LCID, 4, 0),()),
		"ReferenceBody": ((12502, LCID, 4, 0),()),
		"ReferenceDirection": ((13052, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((12504, LCID, 4, 0),()),
		"Width": ((13053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleSensorExternalSphere(DispatchBaseClass):
	'''Particle Sensor'''
	CLSID = IID('{E076254E-15EB-4468-B567-F8D0C0AAACB1}')
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
		return self._oleobj_.InvokeTypes(12512, LCID, 1, (24, 0), (),)


	def ShowPlotDialog(self):
		'''
		Show the plot dialog
		'''
		return self._oleobj_.InvokeTypes(12511, LCID, 1, (24, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(12503, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(13001, 2, (3, 0), (), "GroupSequence", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Position(self):
		return self._ApplyTypes_(*(12501, 2, (8197, 0), (), "Position", None))
	def _get_Radius(self):
		return self._ApplyTypes_(*(13051, 2, (5, 0), (), "Radius", None))
	def _get_ReferenceBody(self):
		return self._ApplyTypes_(*(12502, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(12504, 2, (11, 0), (), "Visible", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((12503, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((13001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((12501, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Radius(self, value):
		if "Radius" in self.__dict__: self.__dict__["Radius"] = value; return
		self._oleobj_.Invoke(*((13051, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceBody(self, value):
		if "ReferenceBody" in self.__dict__: self.__dict__["ReferenceBody"] = value; return
		self._oleobj_.Invoke(*((12502, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((12504, LCID, 4, 0) + (value,) + ()))

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
		"Color": (12503, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (13001, 2, (3, 0), (), "GroupSequence", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Position": (12501, 2, (8197, 0), (), "Position", None),
		"Radius": (13051, 2, (5, 0), (), "Radius", None),
		"ReferenceBody": (12502, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (12504, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Color": ((12503, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"GroupSequence": ((13001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Position": ((12501, LCID, 4, 0),()),
		"Radius": ((13051, LCID, 4, 0),()),
		"ReferenceBody": ((12502, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((12504, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IParticleSetExternal(DispatchBaseClass):
	'''ParticleSetExternal'''
	CLSID = IID('{83B0ECE1-A2B0-4F93-9DC6-861FCD42335E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_GraphicMaterial(self):
		return self._ApplyTypes_(*(13002, 2, (9, 0), (), "GraphicMaterial", '{50D4EBE3-721F-4673-BEDE-56BC2583A64F}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(13001, 2, (8, 0), (), "Name", None))

	GraphicMaterial = property(_get_GraphicMaterial, None)
	'''
	Graphic Material

	:type: recurdyn.ProcessNet.IGraphicMaterial
	'''
	Name = property(_get_Name, None)
	'''
	Name

	:type: str
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"GraphicMaterial": (13002, 2, (9, 0), (), "GraphicMaterial", '{50D4EBE3-721F-4673-BEDE-56BC2583A64F}'),
		"Name": (13001, 2, (8, 0), (), "Name", None),
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

class IParticleSetExternalCollection(DispatchBaseClass):
	'''ParticleSetExternal Collection'''
	CLSID = IID('{2410BF87-ECBC-4C94-AD7B-2772AEB1705A}')
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
		:rtype: recurdyn.ExternalSPI.IParticleSetExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{83B0ECE1-A2B0-4F93-9DC6-861FCD42335E}')
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
		:rtype: recurdyn.ExternalSPI.IParticleSetExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{83B0ECE1-A2B0-4F93-9DC6-861FCD42335E}')
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
		return win32com.client.util.Iterator(ob, '{83B0ECE1-A2B0-4F93-9DC6-861FCD42335E}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{83B0ECE1-A2B0-4F93-9DC6-861FCD42335E}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IProfile2DCollection(DispatchBaseClass):
	'''2D Profile Collection'''
	CLSID = IID('{73DD3F05-6291-40A0-AB1A-DB6F2431F2B9}')
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
		:rtype: recurdyn.ExternalSPI.IProfile2DExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}')
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
		:rtype: recurdyn.ExternalSPI.IProfile2DExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}')
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
		return win32com.client.util.Iterator(ob, '{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IProfile2DExternal(DispatchBaseClass):
	'''2D Profile'''
	CLSID = IID('{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}')
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
		return self._oleobj_.InvokeTypes(12512, LCID, 1, (24, 0), (),)


	def ShowPlotDialog(self):
		'''
		Show the plot dialog
		'''
		return self._oleobj_.InvokeTypes(12511, LCID, 1, (24, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(12509, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Division(self):
		return self._ApplyTypes_(*(12506, 2, (3, 0), (), "Division", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(13001, 2, (3, 0), (), "GroupSequence", None))
	def _get_Halfdepth(self):
		return self._ApplyTypes_(*(12504, 2, (5, 0), (), "Halfdepth", None))
	def _get_Length(self):
		return self._ApplyTypes_(*(12505, 2, (5, 0), (), "Length", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NormalDirection(self):
		return self._ApplyTypes_(*(12502, 2, (8197, 0), (), "NormalDirection", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Position(self):
		return self._ApplyTypes_(*(12501, 2, (8197, 0), (), "Position", None))
	def _get_ReferenceBody(self):
		return self._ApplyTypes_(*(12508, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_ReferenceDirection(self):
		return self._ApplyTypes_(*(12503, 2, (8197, 0), (), "ReferenceDirection", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(12510, 2, (11, 0), (), "Visible", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((12509, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Division(self, value):
		if "Division" in self.__dict__: self.__dict__["Division"] = value; return
		self._oleobj_.Invoke(*((12506, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((13001, LCID, 4, 0) + (value,) + ()))
	def _set_Halfdepth(self, value):
		if "Halfdepth" in self.__dict__: self.__dict__["Halfdepth"] = value; return
		self._oleobj_.Invoke(*((12504, LCID, 4, 0) + (value,) + ()))
	def _set_Length(self, value):
		if "Length" in self.__dict__: self.__dict__["Length"] = value; return
		self._oleobj_.Invoke(*((12505, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NormalDirection(self, value):
		if "NormalDirection" in self.__dict__: self.__dict__["NormalDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((12502, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((12501, LCID, 4, 0) + (variantValue,) + ()))
	def _set_ReferenceBody(self, value):
		if "ReferenceBody" in self.__dict__: self.__dict__["ReferenceBody"] = value; return
		self._oleobj_.Invoke(*((12508, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceDirection(self, value):
		if "ReferenceDirection" in self.__dict__: self.__dict__["ReferenceDirection"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((12503, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((12510, LCID, 4, 0) + (value,) + ()))

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
		"Color": (12509, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Division": (12506, 2, (3, 0), (), "Division", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (13001, 2, (3, 0), (), "GroupSequence", None),
		"Halfdepth": (12504, 2, (5, 0), (), "Halfdepth", None),
		"Length": (12505, 2, (5, 0), (), "Length", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NormalDirection": (12502, 2, (8197, 0), (), "NormalDirection", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Position": (12501, 2, (8197, 0), (), "Position", None),
		"ReferenceBody": (12508, 2, (9, 0), (), "ReferenceBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"ReferenceDirection": (12503, 2, (8197, 0), (), "ReferenceDirection", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (12510, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Color": ((12509, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Division": ((12506, LCID, 4, 0),()),
		"GroupSequence": ((13001, LCID, 4, 0),()),
		"Halfdepth": ((12504, LCID, 4, 0),()),
		"Length": ((12505, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NormalDirection": ((12502, LCID, 4, 0),()),
		"Position": ((12501, LCID, 4, 0),()),
		"ReferenceBody": ((12508, LCID, 4, 0),()),
		"ReferenceDirection": ((12503, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((12510, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITraceCollection(DispatchBaseClass):
	'''Trace Collection'''
	CLSID = IID('{19CE10D3-0B31-4762-8AAC-71D8E22E62DF}')
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
		:rtype: recurdyn.ExternalSPI.ITraceExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F3349896-A8B5-4D86-99D5-FD78580AA1A8}')
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
		:rtype: recurdyn.ExternalSPI.ITraceExternal
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F3349896-A8B5-4D86-99D5-FD78580AA1A8}')
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
		return win32com.client.util.Iterator(ob, '{F3349896-A8B5-4D86-99D5-FD78580AA1A8}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{F3349896-A8B5-4D86-99D5-FD78580AA1A8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class ITraceExternal(DispatchBaseClass):
	'''Trace'''
	CLSID = IID('{F3349896-A8B5-4D86-99D5-FD78580AA1A8}')
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
		return self._ApplyTypes_(*(12503, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GroupSequence(self):
		return self._ApplyTypes_(*(13001, 2, (3, 0), (), "GroupSequence", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ParticleID(self):
		return self._ApplyTypes_(*(12501, 2, (3, 0), (), "ParticleID", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(12504, 2, (11, 0), (), "Visible", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(12502, 2, (4, 0), (), "Width", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((12503, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_GroupSequence(self, value):
		if "GroupSequence" in self.__dict__: self.__dict__["GroupSequence"] = value; return
		self._oleobj_.Invoke(*((13001, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ParticleID(self, value):
		if "ParticleID" in self.__dict__: self.__dict__["ParticleID"] = value; return
		self._oleobj_.Invoke(*((12501, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((12504, LCID, 4, 0) + (value,) + ()))
	def _set_Width(self, value):
		if "Width" in self.__dict__: self.__dict__["Width"] = value; return
		self._oleobj_.Invoke(*((12502, LCID, 4, 0) + (value,) + ()))

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
	Sequence of the Particle Set

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
	ParticleID = property(_get_ParticleID, _set_ParticleID)
	'''
	ID of the Particle

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
		"_set_ParticleID": _set_ParticleID,
		"_set_UserData": _set_UserData,
		"_set_Visible": _set_Visible,
		"_set_Width": _set_Width,
	}
	_prop_map_get_ = {
		"Color": (12503, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GroupSequence": (13001, 2, (3, 0), (), "GroupSequence", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ParticleID": (12501, 2, (3, 0), (), "ParticleID", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"Visible": (12504, 2, (11, 0), (), "Visible", None),
		"Width": (12502, 2, (4, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((12503, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"GroupSequence": ((13001, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ParticleID": ((12501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"Visible": ((12504, LCID, 4, 0),()),
		"Width": ((12502, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IWallCollection(DispatchBaseClass):
	'''Wall Collection'''
	CLSID = IID('{66991464-4D29-4DC9-8D9D-D0A77DD811FF}')
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
		:rtype: recurdyn.ParticleBase.IWall
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{9E1686A2-8CE5-4D33-993A-8583147C5EEA}')
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
		:rtype: recurdyn.ParticleBase.IWall
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{9E1686A2-8CE5-4D33-993A-8583147C5EEA}')
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
		return win32com.client.util.Iterator(ob, '{9E1686A2-8CE5-4D33-993A-8583147C5EEA}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{9E1686A2-8CE5-4D33-993A-8583147C5EEA}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

IExternalSPIToolkit_vtables_dispatch_ = 1
IExternalSPIToolkit_vtables_ = [
	(( 'Program' , 'Program' , ), 13051, (13051, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Program' , 'Program' , ), 13051, (13051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'WallCollection' , 'WallCollection' , ), 13052, (13052, (), [ (16393, 10, None, "IID('{66991464-4D29-4DC9-8D9D-D0A77DD811FF}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ParticleSetExternalCollection' , 'ParticleSetExternalCollection' , ), 13053, (13053, (), [ (16393, 10, None, "IID('{2410BF87-ECBC-4C94-AD7B-2772AEB1705A}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateWall' , 'Name' , 'entity' , 'wall' , ), 13061, (13061, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (16393, 10, None, "IID('{9E1686A2-8CE5-4D33-993A-8583147C5EEA}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ExportWallFile' , 'folderName' , ), 13062, (13062, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'TraceCollection' , 'TraceCollection' , ), 13063, (13063, (), [ (16393, 10, None, "IID('{19CE10D3-0B31-4762-8AAC-71D8E22E62DF}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateTrace' , 'Name' , 'trace' , ), 13064, (13064, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{F3349896-A8B5-4D86-99D5-FD78580AA1A8}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'MassCenterCollection' , 'MassCenterCollection' , ), 13065, (13065, (), [ (16393, 10, None, "IID('{6D30D962-900A-4303-9DAA-181B862E36B7}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CreateMassCenter' , 'Name' , 'massCenter' , ), 13066, (13066, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ParticleSensorCollection' , 'sensorCollection' , ), 13067, (13067, (), [ (16393, 10, None, "IID('{8F3D2213-D9EF-47CD-93C7-8E3E91F4706C}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CreateParticleSensorSphere' , 'Name' , 'referenceBody' , 'sensor' , ), 13068, (13068, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , (16393, 10, None, "IID('{E076254E-15EB-4468-B567-F8D0C0AAACB1}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CreateParticleSensorBox' , 'Name' , 'referenceBody' , 'sensor' , ), 13069, (13069, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , (16393, 10, None, "IID('{25F31E37-59B8-4666-A55A-FC5872D4EAA9}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Profile2DCollection' , 'Profile2DCollection' , ), 13070, (13070, (), [ (16393, 10, None, "IID('{73DD3F05-6291-40A0-AB1A-DB6F2431F2B9}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CreateProfile2D' , 'Name' , 'referenceBody' , 'profile2D' , ), 13071, (13071, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , (16393, 10, None, "IID('{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ParticlePostDataTitleCollection' , 'titles' , ), 13072, (13072, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'WallPostDataTitleCollection' , 'titles' , ), 13073, (13073, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'SetClipMinMaxValue' , 'GroupSequence' , 'particleDataTitle' , 'minValue' , 'maxValue' , 
			 'fUse' , ), 13074, (13074, (), [ (3, 1, None, None) , (8, 1, None, None) , (5, 1, None, None) , 
			 (5, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'GetClipMinMaxValue' , 'GroupSequence' , 'particleDataTitle' , 'minValue' , 'maxValue' , 
			 'fUse' , ), 13075, (13075, (), [ (3, 1, None, None) , (8, 1, None, None) , (16389, 2, None, None) , 
			 (16389, 2, None, None) , (16395, 2, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ContourParticle' , 'ppVal' , ), 13076, (13076, (), [ (16393, 10, None, "IID('{9B435673-BCFA-4FDF-A34F-0A6758DC9AE4}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'ContourWall' , 'ppVal' , ), 13077, (13077, (), [ (16393, 10, None, "IID('{9B5F3020-811C-495A-80A2-21CE0C1D585B}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'ExportParticlePostData' , 'path' , 'titles' , 'groupSequences' , ), 13078, (13078, (), [ 
			 (8, 1, None, None) , (8200, 1, None, None) , (8195, 1, None, None) , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'ExportWallPostData' , 'path' , 'titles' , 'wallSequences' , ), 13079, (13079, (), [ 
			 (8, 1, None, None) , (8200, 1, None, None) , (8195, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UpdatePostData' , ), 13080, (13080, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'FluidDisplay' , 'GroupSequence' , 'FluidDisplay' , ), 13081, (13081, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{F474A409-5990-45C4-BE20-FC1B85C0D977}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'flag' , ), 13082, (13082, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'Connect' , 'flag' , ), 13082, (13082, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'HideParticleSets' , 'flag' , ), 13083, (13083, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'HideParticleSets' , 'flag' , ), 13083, (13083, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
]

IMassCenterCollection_vtables_dispatch_ = 1
IMassCenterCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IMassCenterExternal_vtables_dispatch_ = 1
IMassCenterExternal_vtables_ = [
	(( 'AddParticleSet' , 'GroupSequence' , 'density' , ), 13001, (13001, (), [ (3, 1, None, None) , 
			 (4, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IParticleFluidDisplay_vtables_dispatch_ = 1
IParticleFluidDisplay_vtables_ = [
	(( 'Alpha' , 'param' , ), 13001, (13001, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Alpha' , 'param' , ), 13001, (13001, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Threshold' , 'length' , ), 13002, (13002, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Threshold' , 'length' , ), 13002, (13002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CellSize' , 'param' , ), 13003, (13003, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CellSize' , 'param' , ), 13003, (13003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'flag' , ), 13004, (13004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'flag' , ), 13004, (13004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StartFrame' , 'frame' , ), 13005, (13005, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'StartFrame' , 'frame' , ), 13005, (13005, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'EndFrame' , 'frame' , ), 13006, (13006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'EndFrame' , 'frame' , ), 13006, (13006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseDirectory' , 'flag' , ), 13007, (13007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseDirectory' , 'flag' , ), 13007, (13007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Directory' , 'Directory' , ), 13008, (13008, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Directory' , 'Directory' , ), 13008, (13008, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Create' , ), 13009, (13009, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Import' , ), 13010, (13010, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DrawLine' , 'flag' , ), 13011, (13011, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'DrawLine' , 'flag' , ), 13011, (13011, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SmoothRendering' , 'flag' , ), 13012, (13012, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'SmoothRendering' , 'flag' , ), 13012, (13012, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IParticleSensorCollection_vtables_dispatch_ = 1
IParticleSensorCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E1FD328A-243E-4924-AA28-F1F71CD925FD}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IParticleSensorExternal_vtables_dispatch_ = 1
IParticleSensorExternal_vtables_ = [
	(( 'GroupSequence' , 'GroupSequence' , ), 13001, (13001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GroupSequence' , 'GroupSequence' , ), 13001, (13001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
]

IParticleSensorExternalBox_vtables_dispatch_ = 1
IParticleSensorExternalBox_vtables_ = [
	(( 'NormalDirection' , 'normal' , ), 13051, (13051, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'normal' , ), 13051, (13051, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'direction' , ), 13052, (13052, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceDirection' , 'direction' , ), 13052, (13052, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 13053, (13053, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'Width' , ), 13053, (13053, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 13054, (13054, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'Height' , ), 13054, (13054, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'Depth' , ), 13055, (13055, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'Depth' , ), 13055, (13055, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IParticleSensorExternalSphere_vtables_dispatch_ = 1
IParticleSensorExternalSphere_vtables_ = [
	(( 'Radius' , 'Radius' , ), 13051, (13051, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Radius' , 'Radius' , ), 13051, (13051, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IParticleSetExternal_vtables_dispatch_ = 1
IParticleSetExternal_vtables_ = [
	(( 'Name' , 'Name' , ), 13001, (13001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GraphicMaterial' , 'material' , ), 13002, (13002, (), [ (16393, 10, None, "IID('{50D4EBE3-721F-4673-BEDE-56BC2583A64F}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IParticleSetExternalCollection_vtables_dispatch_ = 1
IParticleSetExternalCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{83B0ECE1-A2B0-4F93-9DC6-861FCD42335E}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IProfile2DCollection_vtables_dispatch_ = 1
IProfile2DCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IProfile2DExternal_vtables_dispatch_ = 1
IProfile2DExternal_vtables_ = [
	(( 'GroupSequence' , 'GroupSequence' , ), 13001, (13001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GroupSequence' , 'GroupSequence' , ), 13001, (13001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

ITraceCollection_vtables_dispatch_ = 1
ITraceCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{F3349896-A8B5-4D86-99D5-FD78580AA1A8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

ITraceExternal_vtables_dispatch_ = 1
ITraceExternal_vtables_ = [
	(( 'GroupSequence' , 'GroupSequence' , ), 13001, (13001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'GroupSequence' , 'GroupSequence' , ), 13001, (13001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IWallCollection_vtables_dispatch_ = 1
IWallCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{9E1686A2-8CE5-4D33-993A-8583147C5EEA}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{83B0ECE1-A2B0-4F93-9DC6-861FCD42335E}' : IParticleSetExternal,
	'{2410BF87-ECBC-4C94-AD7B-2772AEB1705A}' : IParticleSetExternalCollection,
	'{66991464-4D29-4DC9-8D9D-D0A77DD811FF}' : IWallCollection,
	'{F3349896-A8B5-4D86-99D5-FD78580AA1A8}' : ITraceExternal,
	'{19CE10D3-0B31-4762-8AAC-71D8E22E62DF}' : ITraceCollection,
	'{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}' : IMassCenterExternal,
	'{6D30D962-900A-4303-9DAA-181B862E36B7}' : IMassCenterCollection,
	'{E1FD328A-243E-4924-AA28-F1F71CD925FD}' : IParticleSensorExternal,
	'{E076254E-15EB-4468-B567-F8D0C0AAACB1}' : IParticleSensorExternalSphere,
	'{25F31E37-59B8-4666-A55A-FC5872D4EAA9}' : IParticleSensorExternalBox,
	'{8F3D2213-D9EF-47CD-93C7-8E3E91F4706C}' : IParticleSensorCollection,
	'{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}' : IProfile2DExternal,
	'{73DD3F05-6291-40A0-AB1A-DB6F2431F2B9}' : IProfile2DCollection,
	'{F474A409-5990-45C4-BE20-FC1B85C0D977}' : IParticleFluidDisplay,
	'{5493C868-80A1-408B-8B91-722738B17635}' : IExternalSPIToolkit,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{83B0ECE1-A2B0-4F93-9DC6-861FCD42335E}' : 'IParticleSetExternal',
	'{2410BF87-ECBC-4C94-AD7B-2772AEB1705A}' : 'IParticleSetExternalCollection',
	'{66991464-4D29-4DC9-8D9D-D0A77DD811FF}' : 'IWallCollection',
	'{F3349896-A8B5-4D86-99D5-FD78580AA1A8}' : 'ITraceExternal',
	'{19CE10D3-0B31-4762-8AAC-71D8E22E62DF}' : 'ITraceCollection',
	'{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}' : 'IMassCenterExternal',
	'{6D30D962-900A-4303-9DAA-181B862E36B7}' : 'IMassCenterCollection',
	'{E1FD328A-243E-4924-AA28-F1F71CD925FD}' : 'IParticleSensorExternal',
	'{E076254E-15EB-4468-B567-F8D0C0AAACB1}' : 'IParticleSensorExternalSphere',
	'{25F31E37-59B8-4666-A55A-FC5872D4EAA9}' : 'IParticleSensorExternalBox',
	'{8F3D2213-D9EF-47CD-93C7-8E3E91F4706C}' : 'IParticleSensorCollection',
	'{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}' : 'IProfile2DExternal',
	'{73DD3F05-6291-40A0-AB1A-DB6F2431F2B9}' : 'IProfile2DCollection',
	'{F474A409-5990-45C4-BE20-FC1B85C0D977}' : 'IParticleFluidDisplay',
	'{5493C868-80A1-408B-8B91-722738B17635}' : 'IExternalSPIToolkit',
}


NamesToIIDMap = {
	'IParticleSetExternal' : '{83B0ECE1-A2B0-4F93-9DC6-861FCD42335E}',
	'IParticleSetExternalCollection' : '{2410BF87-ECBC-4C94-AD7B-2772AEB1705A}',
	'IWallCollection' : '{66991464-4D29-4DC9-8D9D-D0A77DD811FF}',
	'ITraceExternal' : '{F3349896-A8B5-4D86-99D5-FD78580AA1A8}',
	'ITraceCollection' : '{19CE10D3-0B31-4762-8AAC-71D8E22E62DF}',
	'IMassCenterExternal' : '{DA0C15FA-2CE4-47B0-902F-5457DCDD7B78}',
	'IMassCenterCollection' : '{6D30D962-900A-4303-9DAA-181B862E36B7}',
	'IParticleSensorExternal' : '{E1FD328A-243E-4924-AA28-F1F71CD925FD}',
	'IParticleSensorExternalSphere' : '{E076254E-15EB-4468-B567-F8D0C0AAACB1}',
	'IParticleSensorExternalBox' : '{25F31E37-59B8-4666-A55A-FC5872D4EAA9}',
	'IParticleSensorCollection' : '{8F3D2213-D9EF-47CD-93C7-8E3E91F4706C}',
	'IProfile2DExternal' : '{C2E474A7-8D4E-4EB0-939A-3720A0DED9A8}',
	'IProfile2DCollection' : '{73DD3F05-6291-40A0-AB1A-DB6F2431F2B9}',
	'IParticleFluidDisplay' : '{F474A409-5990-45C4-BE20-FC1B85C0D977}',
	'IExternalSPIToolkit' : '{5493C868-80A1-408B-8B91-722738B17635}',
}


