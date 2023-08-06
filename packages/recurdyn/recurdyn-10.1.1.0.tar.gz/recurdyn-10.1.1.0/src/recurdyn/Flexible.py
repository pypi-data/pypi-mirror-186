# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMFlexible.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMFlexible Type Library'
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

CLSID = IID('{874B6C32-334A-4AFC-802D-E8ADE438CCB2}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class BodyType(IntEnum):
	'''
	BodyType enumeration.
	'''
	BodyType_FFLEX                =1         
	'''Constant value is 1.'''
	BodyType_RFLEX                =2         
	'''Constant value is 2.'''
	BodyType_RIGID                =0         
	'''Constant value is 0.'''
class ContourBandLegendType(IntEnum):
	'''
	ContourBandLegendType enumeration.
	'''
	CB_Legned_Dialog              =1         
	'''Constant value is 1.'''
	CB_Legned_Disable             =0         
	'''Constant value is 0.'''
	CB_Legned_Display             =2         
	'''Constant value is 2.'''
class ContourColorStyle(IntEnum):
	'''
	ContourColorStyle enumeration.
	'''
	C_Style_Smooth                =0         
	'''Constant value is 0.'''
	C_Style_Stepped               =2         
	'''Constant value is 2.'''
	C_Style_Wire                  =1         
	'''Constant value is 1.'''
class ContourComponent(IntEnum):
	'''
	ContourComponent enumeration.
	'''
	CC_CONTACT_MAGNITUDE          =33        
	'''Constant value is 33.'''
	CC_CONTACT_NORMAL             =31        
	'''Constant value is 31.'''
	CC_CONTACT_TANGENT            =32        
	'''Constant value is 32.'''
	CC_CP_CP                      =42        
	'''Constant value is 42.'''
	CC_CP_EL                      =41        
	'''Constant value is 41.'''
	CC_E1                         =15        
	'''Constant value is 15.'''
	CC_E2                         =16        
	'''Constant value is 16.'''
	CC_E3                         =17        
	'''Constant value is 17.'''
	CC_EINT                       =18        
	'''Constant value is 18.'''
	CC_EMISES                     =19        
	'''Constant value is 19.'''
	CC_ERP                        =51        
	'''Constant value is 51.'''
	CC_ERP_DENSITY                =52        
	'''Constant value is 52.'''
	CC_EX                         =9         
	'''Constant value is 9.'''
	CC_EXY                        =12        
	'''Constant value is 12.'''
	CC_EY                         =10        
	'''Constant value is 10.'''
	CC_EYZ                        =13        
	'''Constant value is 13.'''
	CC_EZ                         =11        
	'''Constant value is 11.'''
	CC_EZX                        =14        
	'''Constant value is 14.'''
	CC_RSUM                       =8         
	'''Constant value is 8.'''
	CC_RX                         =5         
	'''Constant value is 5.'''
	CC_RY                         =6         
	'''Constant value is 6.'''
	CC_RZ                         =7         
	'''Constant value is 7.'''
	CC_S1                         =26        
	'''Constant value is 26.'''
	CC_S2                         =27        
	'''Constant value is 27.'''
	CC_S3                         =28        
	'''Constant value is 28.'''
	CC_SINT                       =29        
	'''Constant value is 29.'''
	CC_SMISES                     =30        
	'''Constant value is 30.'''
	CC_SX                         =20        
	'''Constant value is 20.'''
	CC_SXY                        =23        
	'''Constant value is 23.'''
	CC_SY                         =21        
	'''Constant value is 21.'''
	CC_SYZ                        =24        
	'''Constant value is 24.'''
	CC_SZ                         =22        
	'''Constant value is 22.'''
	CC_SZX                        =25        
	'''Constant value is 25.'''
	CC_TSUM                       =4         
	'''Constant value is 4.'''
	CC_TX                         =1         
	'''Constant value is 1.'''
	CC_TY                         =2         
	'''Constant value is 2.'''
	CC_TZ                         =3         
	'''Constant value is 3.'''
class ContourContactSurfaceOnlyType(IntEnum):
	'''
	ContourContactSurfaceOnlyType enumeration.
	'''
	Contact_Patches_Only          =1         
	'''Constant value is 1.'''
	UserDefine_Contact_Surface    =0         
	'''Constant value is 0.'''
class ContourDataExportSelectType(IntEnum):
	'''
	ContourDataExportSelectType enumeration.
	'''
	Select_All                    =5         
	'''Constant value is 5.'''
	Select_ElementSet             =4         
	'''Constant value is 4.'''
	Select_LineSet                =3         
	'''Constant value is 3.'''
	Select_Node                   =0         
	'''Constant value is 0.'''
	Select_NodeSet                =1         
	'''Constant value is 1.'''
	Select_PatchSet               =2         
	'''Constant value is 2.'''
class ContourDataExportType(IntEnum):
	'''
	ContourDataExportType enumeration.
	'''
	Export_MinMax                 =2         
	'''Constant value is 2.'''
	Export_Node                   =0         
	'''Constant value is 0.'''
	Export_Time                   =1         
	'''Constant value is 1.'''
class ContourMinMaxType(IntEnum):
	'''
	ContourMinMaxType enumeration.
	'''
	MM_Display                    =0         
	'''Constant value is 0.'''
	MM_UserDefined                =1         
	'''Constant value is 1.'''
class ContourReferenceType(IntEnum):
	'''
	ContourReferenceType enumeration.
	'''
	ReferenceType_Marker          =1         
	'''Constant value is 1.'''
	ReferenceType_Node            =0         
	'''Constant value is 0.'''
class ContourType(IntEnum):
	'''
	ContourType enumeration.
	'''
	CT_CONTACT_FORCE              =3         
	'''Constant value is 3.'''
	CT_CONTACT_PRESSURE           =4         
	'''Constant value is 4.'''
	CT_DISPLACEMENT               =0         
	'''Constant value is 0.'''
	CT_ELASTIC_STRAIN             =5         
	'''Constant value is 5.'''
	CT_PLASTIC_STRAIN             =6         
	'''Constant value is 6.'''
	CT_SOUND                      =8         
	'''Constant value is 8.'''
	CT_STRAIN                     =1         
	'''Constant value is 1.'''
	CT_STRESS                     =2         
	'''Constant value is 2.'''
	CT_TEMPERATURE                =9         
	'''Constant value is 9.'''
	CT_THERMAL_STRAIN             =7         
	'''Constant value is 7.'''
class ConvertFFlexToRFlexType(IntEnum):
	'''
	ConvertFFlexToRFlexType enumeration.
	'''
	FFlexToRFlex_Swap_RFI         =1         
	'''Constant value is 1.'''
	FFlexToRFlex_Swap_RFlexGen    =0         
	'''Constant value is 0.'''
class ConvertFFlexToRigidType(IntEnum):
	'''
	ConvertFFlexToRigidType enumeration.
	'''
	FFlexToRigid_Convert          =1         
	'''Constant value is 1.'''
	FFlexToRigid_Convert_RigidShell=0         
	'''Constant value is 0.'''
	FFlexToRigid_Swap_CADData     =2         
	'''Constant value is 2.'''
class ConvertRFlexToFFlexType(IntEnum):
	'''
	ConvertRFlexToFFlexType enumeration.
	'''
	RFlexToFFlex_Convert          =0         
	'''Constant value is 0.'''
	RFlexToFFlex_Swap             =1         
	'''Constant value is 1.'''
class ConvertRFlexToRFlexType(IntEnum):
	'''
	ConvertRFlexToRFlexType enumeration.
	'''
	RFlexToRFlex_Swap_RFI         =1         
	'''Constant value is 1.'''
	RFlexToRFlex_Swap_RFlexGen    =0         
	'''Constant value is 0.'''
class ConvertRFlexToRigidType(IntEnum):
	'''
	ConvertRFlexToRigidType enumeration.
	'''
	RFlexToRigid_Convert_RigidShell=0         
	'''Constant value is 0.'''
	RFlexToRigid_Swap_CADData     =1         
	'''Constant value is 1.'''
class ConvertRigidToFFlexType(IntEnum):
	'''
	ConvertRigidToFFlexType enumeration.
	'''
	RigidToFFlex_Mesh             =0         
	'''Constant value is 0.'''
	RigidToFFlex_Swap             =1         
	'''Constant value is 1.'''
class CuttingPlaneFlexType(IntEnum):
	'''
	CuttingPlaneFlexType enumeration.
	'''
	CuttingPlaneFlexType_CrossSection=0         
	'''Constant value is 0.'''
	CuttingPlaneFlexType_ElementShape=1         
	'''Constant value is 1.'''
class RFlexGenerationSolverType(IntEnum):
	'''
	RFlexGenerationSolverType enumeration.
	'''
	SolverType_Dynamis            =1         
	'''Constant value is 1.'''
	SolverType_SunShine           =0         
	'''Constant value is 0.'''
class ShellDataExportType(IntEnum):
	'''
	ShellDataExportType enumeration.
	'''
	ShellDataExport_PatchSets     =1         
	'''Constant value is 1.'''
	ShellDataExport_VisibleComponent=0         
	'''Constant value is 0.'''
class ShowNodeIDType(IntEnum):
	'''
	ShowNodeIDType enumeration.
	'''
	ShowNodeID_AllNode            =4         
	'''Constant value is 4.'''
	ShowNodeID_BC                 =1         
	'''Constant value is 1.'''
	ShowNodeID_Marker             =3         
	'''Constant value is 3.'''
	ShowNodeID_NodeSet            =0         
	'''Constant value is 0.'''
	ShowNodeID_Output             =2         
	'''Constant value is 2.'''

from win32com.client import DispatchBaseClass
class IContour(DispatchBaseClass):
	'''Contour'''
	CLSID = IID('{BDF4F979-28B7-48D2-BF06-9C59B70D467B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddDataTrace(self, pVal, Val):
		'''
		Add DataTrace
		
		:param pVal: IGeneric
		:param Val: int
		'''
		return self._oleobj_.InvokeTypes(9010, LCID, 1, (24, 0), ((9, 1), (3, 1)),pVal
			, Val)


	def AddPartSelction(self, pBody, pSet):
		'''
		Add Part Selection
		
		:param pBody: IGeneric
		:param pSet: IGeneric
		'''
		return self._oleobj_.InvokeTypes(9013, LCID, 1, (24, 0), ((9, 1), (9, 1)),pBody
			, pSet)


	def CloseContourDialog(self):
		'''
		Close Contour Dialog
		'''
		return self._oleobj_.InvokeTypes(9018, LCID, 1, (24, 0), (),)


	def DeleteDataTrace(self, pVal):
		'''
		Delete DataTrace
		
		:param pVal: IContourDataTrace
		'''
		return self._oleobj_.InvokeTypes(9011, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeleteDataTracebyIndex(self, Val):
		'''
		Delete DataTrace
		
		:param Val: int
		'''
		return self._oleobj_.InvokeTypes(9012, LCID, 1, (24, 0), ((3, 1),),Val
			)


	def DeletePartSelction(self, pVal):
		'''
		Delete Part Selection
		
		:param pVal: IContourPartSelection
		'''
		return self._oleobj_.InvokeTypes(9014, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePartSelctionbyIndex(self, Val):
		'''
		Delete Part Selection
		
		:param Val: int
		'''
		return self._oleobj_.InvokeTypes(9015, LCID, 1, (24, 0), ((3, 1),),Val
			)


	def OpenContourDialog(self):
		'''
		Open Contour Dialog
		'''
		return self._oleobj_.InvokeTypes(9017, LCID, 1, (24, 0), (),)


	def UpdateLegend(self):
		'''
		Contour Setting Done
		'''
		return self._oleobj_.InvokeTypes(9016, LCID, 1, (24, 0), (),)


	def _get_BandOption(self):
		return self._ApplyTypes_(*(9004, 2, (9, 0), (), "BandOption", '{6A77B683-DB6D-47CC-A9A4-8A1236F68D9E}'))
	def _get_DataExport(self):
		return self._ApplyTypes_(*(9009, 2, (9, 0), (), "DataExport", '{139D3F54-8397-417D-8AA9-B8E92666E31A}'))
	def _get_DataTraceCollection(self):
		return self._ApplyTypes_(*(9007, 2, (9, 0), (), "DataTraceCollection", '{9F8AB0C2-9B88-4A3D-A279-5E653738A009}'))
	def _get_EnableView(self):
		return self._ApplyTypes_(*(9001, 2, (11, 0), (), "EnableView", None))
	def _get_MinMaxOption(self):
		return self._ApplyTypes_(*(9003, 2, (9, 0), (), "MinMaxOption", '{B88B9BB0-1991-486D-8248-3FD7CEE798DB}'))
	def _get_PartSelectionCollection(self):
		return self._ApplyTypes_(*(9008, 2, (9, 0), (), "PartSelectionCollection", '{4A8EAB35-DBC8-4E2E-8E70-2D5C34C7F6BA}'))
	def _get_ReferenceNodeCollection(self):
		return self._ApplyTypes_(*(9006, 2, (9, 0), (), "ReferenceNodeCollection", '{CC340394-39A2-489C-B59E-F62063FBE6D2}'))
	def _get_StyleOption(self):
		return self._ApplyTypes_(*(9005, 2, (9, 0), (), "StyleOption", '{FC113BCB-DE52-4C7B-BE93-029A709898B0}'))
	def _get_TypeOption(self):
		return self._ApplyTypes_(*(9002, 2, (9, 0), (), "TypeOption", '{49E653C4-054B-4496-B4FA-9EF8947B2C94}'))

	def _set_EnableView(self, value):
		if "EnableView" in self.__dict__: self.__dict__["EnableView"] = value; return
		self._oleobj_.Invoke(*((9001, LCID, 4, 0) + (value,) + ()))

	BandOption = property(_get_BandOption, None)
	'''
	Get Contour Band Option

	:type: recurdyn.Flexible.IContourBandOption
	'''
	DataExport = property(_get_DataExport, None)
	'''
	Get Contour Data Export

	:type: recurdyn.Flexible.IContourDataExport
	'''
	DataTraceCollection = property(_get_DataTraceCollection, None)
	'''
	Contains Contour Data Trace

	:type: recurdyn.Flexible.IContourDataTraceCollection
	'''
	EnableView = property(_get_EnableView, _set_EnableView)
	'''
	Enable View Flag

	:type: bool
	'''
	MinMaxOption = property(_get_MinMaxOption, None)
	'''
	Get Contour MinMax Option

	:type: recurdyn.Flexible.IContourMinMaxOption
	'''
	PartSelectionCollection = property(_get_PartSelectionCollection, None)
	'''
	Contains Contour Part Selection

	:type: recurdyn.Flexible.IContourPartSelectionCollection
	'''
	ReferenceNodeCollection = property(_get_ReferenceNodeCollection, None)
	'''
	Contains Contour Reference Node

	:type: recurdyn.Flexible.IContourReferenceNodeCollection
	'''
	StyleOption = property(_get_StyleOption, None)
	'''
	Get Contour Style Option

	:type: recurdyn.Flexible.IContourStyleOption
	'''
	TypeOption = property(_get_TypeOption, None)
	'''
	Get Contour Type Option

	:type: recurdyn.Flexible.IContourTypeOption
	'''

	_prop_map_set_function_ = {
		"_set_EnableView": _set_EnableView,
	}
	_prop_map_get_ = {
		"BandOption": (9004, 2, (9, 0), (), "BandOption", '{6A77B683-DB6D-47CC-A9A4-8A1236F68D9E}'),
		"DataExport": (9009, 2, (9, 0), (), "DataExport", '{139D3F54-8397-417D-8AA9-B8E92666E31A}'),
		"DataTraceCollection": (9007, 2, (9, 0), (), "DataTraceCollection", '{9F8AB0C2-9B88-4A3D-A279-5E653738A009}'),
		"EnableView": (9001, 2, (11, 0), (), "EnableView", None),
		"MinMaxOption": (9003, 2, (9, 0), (), "MinMaxOption", '{B88B9BB0-1991-486D-8248-3FD7CEE798DB}'),
		"PartSelectionCollection": (9008, 2, (9, 0), (), "PartSelectionCollection", '{4A8EAB35-DBC8-4E2E-8E70-2D5C34C7F6BA}'),
		"ReferenceNodeCollection": (9006, 2, (9, 0), (), "ReferenceNodeCollection", '{CC340394-39A2-489C-B59E-F62063FBE6D2}'),
		"StyleOption": (9005, 2, (9, 0), (), "StyleOption", '{FC113BCB-DE52-4C7B-BE93-029A709898B0}'),
		"TypeOption": (9002, 2, (9, 0), (), "TypeOption", '{49E653C4-054B-4496-B4FA-9EF8947B2C94}'),
	}
	_prop_map_put_ = {
		"EnableView": ((9001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IContourBandOption(DispatchBaseClass):
	'''Contour Band Option'''
	CLSID = IID('{6A77B683-DB6D-47CC-A9A4-8A1236F68D9E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BandLevel(self):
		return self._ApplyTypes_(*(9054, 2, (19, 0), (), "BandLevel", None))
	def _get_LegendLocation(self):
		return self._ApplyTypes_(*(9052, 2, (3, 0), (), "LegendLocation", '{40B0D145-E318-48E0-8114-B3400BA8B271}'))
	def _get_LegendType(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "LegendType", '{523C6F14-0660-455F-B6A6-136B5BFC19C4}'))
	def _get_ShowTextLegend(self):
		return self._ApplyTypes_(*(9053, 2, (11, 0), (), "ShowTextLegend", None))

	def _set_BandLevel(self, value):
		if "BandLevel" in self.__dict__: self.__dict__["BandLevel"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))
	def _set_LegendLocation(self, value):
		if "LegendLocation" in self.__dict__: self.__dict__["LegendLocation"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_LegendType(self, value):
		if "LegendType" in self.__dict__: self.__dict__["LegendType"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_ShowTextLegend(self, value):
		if "ShowTextLegend" in self.__dict__: self.__dict__["ShowTextLegend"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))

	BandLevel = property(_get_BandLevel, _set_BandLevel)
	'''
	Band Level

	:type: int
	'''
	LegendLocation = property(_get_LegendLocation, _set_LegendLocation)
	'''
	Contour Band Legend Location Type

	:type: recurdyn.ProcessNet.ContourBandLegendLocationType
	'''
	LegendType = property(_get_LegendType, _set_LegendType)
	'''
	Contour Band Legend Type

	:type: recurdyn.Flexible.ContourBandLegendType
	'''
	ShowTextLegend = property(_get_ShowTextLegend, _set_ShowTextLegend)
	'''
	Show Text Legend

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_BandLevel": _set_BandLevel,
		"_set_LegendLocation": _set_LegendLocation,
		"_set_LegendType": _set_LegendType,
		"_set_ShowTextLegend": _set_ShowTextLegend,
	}
	_prop_map_get_ = {
		"BandLevel": (9054, 2, (19, 0), (), "BandLevel", None),
		"LegendLocation": (9052, 2, (3, 0), (), "LegendLocation", '{40B0D145-E318-48E0-8114-B3400BA8B271}'),
		"LegendType": (9051, 2, (3, 0), (), "LegendType", '{523C6F14-0660-455F-B6A6-136B5BFC19C4}'),
		"ShowTextLegend": (9053, 2, (11, 0), (), "ShowTextLegend", None),
	}
	_prop_map_put_ = {
		"BandLevel": ((9054, LCID, 4, 0),()),
		"LegendLocation": ((9052, LCID, 4, 0),()),
		"LegendType": ((9051, LCID, 4, 0),()),
		"ShowTextLegend": ((9053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IContourDataExport(DispatchBaseClass):
	'''Contour Data Export'''
	CLSID = IID('{139D3F54-8397-417D-8AA9-B8E92666E31A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Export(self, Val):
		'''
		Export Contour Data
		
		:param Val: str
		'''
		return self._oleobj_.InvokeTypes(9057, LCID, 1, (24, 0), ((8, 1),),Val
			)


	def SelectFramesWithRange(self, start, end):
		'''
		Select Frames
		
		:param start: int
		:param end: int
		'''
		return self._oleobj_.InvokeTypes(9056, LCID, 1, (24, 0), ((19, 1), (19, 1)),start
			, end)


	def SelectNodesWithRange(self, start, end):
		'''
		Select Nodes
		
		:param start: int
		:param end: int
		'''
		return self._oleobj_.InvokeTypes(9054, LCID, 1, (24, 0), ((3, 1), (3, 1)),start
			, end)


	def _get_SignificantDigits(self):
		return self._ApplyTypes_(*(9059, 2, (19, 0), (), "SignificantDigits", None))
	def _get_UseScientificNotation(self):
		return self._ApplyTypes_(*(9058, 2, (11, 0), (), "UseScientificNotation", None))

	def _set_Body(self, value):
		if "Body" in self.__dict__: self.__dict__["Body"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_SelectFrames(self, value):
		if "SelectFrames" in self.__dict__: self.__dict__["SelectFrames"] = value; return
		self._oleobj_.Invoke(*((9055, LCID, 4, 0) + (value,) + ()))
	def _set_SelectNodes(self, value):
		if "SelectNodes" in self.__dict__: self.__dict__["SelectNodes"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_SelectType(self, value):
		if "SelectType" in self.__dict__: self.__dict__["SelectType"] = value; return
		self._oleobj_.Invoke(*((9060, LCID, 4, 0) + (value,) + ()))
	def _set_SignificantDigits(self, value):
		if "SignificantDigits" in self.__dict__: self.__dict__["SignificantDigits"] = value; return
		self._oleobj_.Invoke(*((9059, LCID, 4, 0) + (value,) + ()))
	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_UseScientificNotation(self, value):
		if "UseScientificNotation" in self.__dict__: self.__dict__["UseScientificNotation"] = value; return
		self._oleobj_.Invoke(*((9058, LCID, 4, 0) + (value,) + ()))

	SignificantDigits = property(_get_SignificantDigits, _set_SignificantDigits)
	'''
	Significant digits

	:type: int
	'''
	UseScientificNotation = property(_get_UseScientificNotation, _set_UseScientificNotation)
	'''
	Export data with scientific notation flag

	:type: bool
	'''
	Body = property(None, _set_Body)
	'''
	Export Body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	SelectFrames = property(None, _set_SelectFrames)
	'''
	Select Frames

	:type: str
	'''
	SelectNodes = property(None, _set_SelectNodes)
	'''
	Select Nodes

	:type: str
	'''
	SelectType = property(None, _set_SelectType)
	'''
	Select Type

	:type: recurdyn.Flexible.ContourDataExportSelectType
	'''
	Type = property(None, _set_Type)
	'''
	Type

	:type: recurdyn.Flexible.ContourDataExportType
	'''

	_prop_map_set_function_ = {
		"_set_Body": _set_Body,
		"_set_SelectFrames": _set_SelectFrames,
		"_set_SelectNodes": _set_SelectNodes,
		"_set_SelectType": _set_SelectType,
		"_set_SignificantDigits": _set_SignificantDigits,
		"_set_Type": _set_Type,
		"_set_UseScientificNotation": _set_UseScientificNotation,
	}
	_prop_map_get_ = {
		"SignificantDigits": (9059, 2, (19, 0), (), "SignificantDigits", None),
		"UseScientificNotation": (9058, 2, (11, 0), (), "UseScientificNotation", None),
	}
	_prop_map_put_ = {
		"Body": ((9052, LCID, 4, 0),()),
		"SelectFrames": ((9055, LCID, 4, 0),()),
		"SelectNodes": ((9053, LCID, 4, 0),()),
		"SelectType": ((9060, LCID, 4, 0),()),
		"SignificantDigits": ((9059, LCID, 4, 0),()),
		"Type": ((9051, LCID, 4, 0),()),
		"UseScientificNotation": ((9058, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IContourDataTrace(DispatchBaseClass):
	'''Contour Data Trace'''
	CLSID = IID('{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Body(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "Body", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_NodeID(self):
		return self._ApplyTypes_(*(9052, 2, (3, 0), (), "NodeID", None))
	def _get_Select(self):
		return self._ApplyTypes_(*(9051, 2, (11, 0), (), "Select", None))

	def _set_Body(self, value):
		if "Body" in self.__dict__: self.__dict__["Body"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_NodeID(self, value):
		if "NodeID" in self.__dict__: self.__dict__["NodeID"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_Select(self, value):
		if "Select" in self.__dict__: self.__dict__["Select"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))

	Body = property(_get_Body, _set_Body)
	'''
	Body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	NodeID = property(_get_NodeID, _set_NodeID)
	'''
	Reference Node ID

	:type: int
	'''
	Select = property(_get_Select, _set_Select)
	'''
	Selection

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Body": _set_Body,
		"_set_NodeID": _set_NodeID,
		"_set_Select": _set_Select,
	}
	_prop_map_get_ = {
		"Body": (9053, 2, (9, 0), (), "Body", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"NodeID": (9052, 2, (3, 0), (), "NodeID", None),
		"Select": (9051, 2, (11, 0), (), "Select", None),
	}
	_prop_map_put_ = {
		"Body": ((9053, LCID, 4, 0),()),
		"NodeID": ((9052, LCID, 4, 0),()),
		"Select": ((9051, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IContourDataTraceCollection(DispatchBaseClass):
	'''IContourDataTraceCollection'''
	CLSID = IID('{9F8AB0C2-9B88-4A3D-A279-5E653738A009}')
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
		:rtype: recurdyn.Flexible.IContourDataTrace
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}')
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
		:rtype: recurdyn.Flexible.IContourDataTrace
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}')
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
		return win32com.client.util.Iterator(ob, '{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IContourMinMaxOption(DispatchBaseClass):
	'''Contour MinMax Option'''
	CLSID = IID('{B88B9BB0-1991-486D-8248-3FD7CEE798DB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Calculation(self):
		'''
		Min Max Calculation
		'''
		return self._oleobj_.InvokeTypes(9052, LCID, 1, (24, 0), (),)


	def _get_EnableLogScale(self):
		return self._ApplyTypes_(*(9059, 2, (11, 0), (), "EnableLogScale", None))
	def _get_Max(self):
		return self._ApplyTypes_(*(9054, 2, (5, 0), (), "Max", None))
	def _get_Min(self):
		return self._ApplyTypes_(*(9053, 2, (5, 0), (), "Min", None))
	def _get_ShowMax(self):
		return self._ApplyTypes_(*(9062, 2, (11, 0), (), "ShowMax", None))
	def _get_ShowMin(self):
		return self._ApplyTypes_(*(9061, 2, (11, 0), (), "ShowMin", None))
	def _get_ShowMinMax(self):
		return self._ApplyTypes_(*(9057, 2, (11, 0), (), "ShowMinMax", None))
	def _get_Type(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "Type", '{7AD6FCD4-4167-4AA9-8A01-B8E3B31318B5}'))
	def _get_UserDefinedMax(self):
		return self._ApplyTypes_(*(9056, 2, (5, 0), (), "UserDefinedMax", None))
	def _get_UserDefinedMaxColor(self):
		return self._ApplyTypes_(*(9058, 2, (11, 0), (), "UserDefinedMaxColor", None))
	def _get_UserDefinedMin(self):
		return self._ApplyTypes_(*(9055, 2, (5, 0), (), "UserDefinedMin", None))
	def _get_UserDefinedMinColor(self):
		return self._ApplyTypes_(*(9060, 2, (11, 0), (), "UserDefinedMinColor", None))

	def _set_EnableLogScale(self, value):
		if "EnableLogScale" in self.__dict__: self.__dict__["EnableLogScale"] = value; return
		self._oleobj_.Invoke(*((9059, LCID, 4, 0) + (value,) + ()))
	def _set_ShowMax(self, value):
		if "ShowMax" in self.__dict__: self.__dict__["ShowMax"] = value; return
		self._oleobj_.Invoke(*((9062, LCID, 4, 0) + (value,) + ()))
	def _set_ShowMin(self, value):
		if "ShowMin" in self.__dict__: self.__dict__["ShowMin"] = value; return
		self._oleobj_.Invoke(*((9061, LCID, 4, 0) + (value,) + ()))
	def _set_ShowMinMax(self, value):
		if "ShowMinMax" in self.__dict__: self.__dict__["ShowMinMax"] = value; return
		self._oleobj_.Invoke(*((9057, LCID, 4, 0) + (value,) + ()))
	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedMax(self, value):
		if "UserDefinedMax" in self.__dict__: self.__dict__["UserDefinedMax"] = value; return
		self._oleobj_.Invoke(*((9056, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedMaxColor(self, value):
		if "UserDefinedMaxColor" in self.__dict__: self.__dict__["UserDefinedMaxColor"] = value; return
		self._oleobj_.Invoke(*((9058, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedMin(self, value):
		if "UserDefinedMin" in self.__dict__: self.__dict__["UserDefinedMin"] = value; return
		self._oleobj_.Invoke(*((9055, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedMinColor(self, value):
		if "UserDefinedMinColor" in self.__dict__: self.__dict__["UserDefinedMinColor"] = value; return
		self._oleobj_.Invoke(*((9060, LCID, 4, 0) + (value,) + ()))

	EnableLogScale = property(_get_EnableLogScale, _set_EnableLogScale)
	'''
	Log Scale

	:type: bool
	'''
	Max = property(_get_Max, None)
	'''
	Max Value

	:type: float
	'''
	Min = property(_get_Min, None)
	'''
	Min Value

	:type: float
	'''
	ShowMax = property(_get_ShowMax, _set_ShowMax)
	'''
	Show Min Max

	:type: bool
	'''
	ShowMin = property(_get_ShowMin, _set_ShowMin)
	'''
	Show Min Max

	:type: bool
	'''
	ShowMinMax = property(_get_ShowMinMax, _set_ShowMinMax)
	'''
	Show Min Max

	:type: bool
	'''
	Type = property(_get_Type, _set_Type)
	'''
	Min Max Type

	:type: recurdyn.Flexible.ContourMinMaxType
	'''
	UserDefinedMax = property(_get_UserDefinedMax, _set_UserDefinedMax)
	'''
	User Defined Max Value

	:type: float
	'''
	UserDefinedMaxColor = property(_get_UserDefinedMaxColor, _set_UserDefinedMaxColor)
	'''
	UserDefined Max Color

	:type: bool
	'''
	UserDefinedMin = property(_get_UserDefinedMin, _set_UserDefinedMin)
	'''
	User Defined Min Value

	:type: float
	'''
	UserDefinedMinColor = property(_get_UserDefinedMinColor, _set_UserDefinedMinColor)
	'''
	UserDefined Min Color

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_EnableLogScale": _set_EnableLogScale,
		"_set_ShowMax": _set_ShowMax,
		"_set_ShowMin": _set_ShowMin,
		"_set_ShowMinMax": _set_ShowMinMax,
		"_set_Type": _set_Type,
		"_set_UserDefinedMax": _set_UserDefinedMax,
		"_set_UserDefinedMaxColor": _set_UserDefinedMaxColor,
		"_set_UserDefinedMin": _set_UserDefinedMin,
		"_set_UserDefinedMinColor": _set_UserDefinedMinColor,
	}
	_prop_map_get_ = {
		"EnableLogScale": (9059, 2, (11, 0), (), "EnableLogScale", None),
		"Max": (9054, 2, (5, 0), (), "Max", None),
		"Min": (9053, 2, (5, 0), (), "Min", None),
		"ShowMax": (9062, 2, (11, 0), (), "ShowMax", None),
		"ShowMin": (9061, 2, (11, 0), (), "ShowMin", None),
		"ShowMinMax": (9057, 2, (11, 0), (), "ShowMinMax", None),
		"Type": (9051, 2, (3, 0), (), "Type", '{7AD6FCD4-4167-4AA9-8A01-B8E3B31318B5}'),
		"UserDefinedMax": (9056, 2, (5, 0), (), "UserDefinedMax", None),
		"UserDefinedMaxColor": (9058, 2, (11, 0), (), "UserDefinedMaxColor", None),
		"UserDefinedMin": (9055, 2, (5, 0), (), "UserDefinedMin", None),
		"UserDefinedMinColor": (9060, 2, (11, 0), (), "UserDefinedMinColor", None),
	}
	_prop_map_put_ = {
		"EnableLogScale": ((9059, LCID, 4, 0),()),
		"ShowMax": ((9062, LCID, 4, 0),()),
		"ShowMin": ((9061, LCID, 4, 0),()),
		"ShowMinMax": ((9057, LCID, 4, 0),()),
		"Type": ((9051, LCID, 4, 0),()),
		"UserDefinedMax": ((9056, LCID, 4, 0),()),
		"UserDefinedMaxColor": ((9058, LCID, 4, 0),()),
		"UserDefinedMin": ((9055, LCID, 4, 0),()),
		"UserDefinedMinColor": ((9060, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IContourPartSelection(DispatchBaseClass):
	'''Contour Part Selection'''
	CLSID = IID('{14C89575-CA21-4656-988A-87151B83C368}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Body(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "Body", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_ElementSet(self):
		return self._ApplyTypes_(*(9052, 2, (9, 0), (), "ElementSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Select(self):
		return self._ApplyTypes_(*(9051, 2, (11, 0), (), "Select", None))

	def _set_Body(self, value):
		if "Body" in self.__dict__: self.__dict__["Body"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_ElementSet(self, value):
		if "ElementSet" in self.__dict__: self.__dict__["ElementSet"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_Select(self, value):
		if "Select" in self.__dict__: self.__dict__["Select"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))

	Body = property(_get_Body, _set_Body)
	'''
	Body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	ElementSet = property(_get_ElementSet, _set_ElementSet)
	'''
	Element Set

	:type: recurdyn.ProcessNet.IGeneric
	'''
	Select = property(_get_Select, _set_Select)
	'''
	Selection

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Body": _set_Body,
		"_set_ElementSet": _set_ElementSet,
		"_set_Select": _set_Select,
	}
	_prop_map_get_ = {
		"Body": (9053, 2, (9, 0), (), "Body", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"ElementSet": (9052, 2, (9, 0), (), "ElementSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Select": (9051, 2, (11, 0), (), "Select", None),
	}
	_prop_map_put_ = {
		"Body": ((9053, LCID, 4, 0),()),
		"ElementSet": ((9052, LCID, 4, 0),()),
		"Select": ((9051, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IContourPartSelectionCollection(DispatchBaseClass):
	'''IContourPartSelectionCollection'''
	CLSID = IID('{4A8EAB35-DBC8-4E2E-8E70-2D5C34C7F6BA}')
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
		:rtype: recurdyn.Flexible.IContourPartSelection
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{14C89575-CA21-4656-988A-87151B83C368}')
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
		:rtype: recurdyn.Flexible.IContourPartSelection
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{14C89575-CA21-4656-988A-87151B83C368}')
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
		return win32com.client.util.Iterator(ob, '{14C89575-CA21-4656-988A-87151B83C368}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{14C89575-CA21-4656-988A-87151B83C368}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IContourReferenceNode(DispatchBaseClass):
	'''Contour Reference Node'''
	CLSID = IID('{FB58C4A7-6D67-465F-A7D3-ADB1B7E53425}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Body(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "Body", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Marker(self):
		return self._ApplyTypes_(*(9057, 2, (9, 0), (), "Marker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_NodeID(self):
		return self._ApplyTypes_(*(9052, 2, (3, 0), (), "NodeID", None))
	def _get_OrientationReferenceMarker(self):
		return self._ApplyTypes_(*(9055, 2, (9, 0), (), "OrientationReferenceMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_ReferenceType(self):
		return self._ApplyTypes_(*(9056, 2, (3, 0), (), "ReferenceType", '{D18FC6B4-5F7E-4DBD-BD41-407ECD00EFCE}'))
	def _get_Select(self):
		return self._ApplyTypes_(*(9051, 2, (11, 0), (), "Select", None))
	def _get_UseOrientationReferenceMarker(self):
		return self._ApplyTypes_(*(9054, 2, (11, 0), (), "UseOrientationReferenceMarker", None))

	def _set_Marker(self, value):
		if "Marker" in self.__dict__: self.__dict__["Marker"] = value; return
		self._oleobj_.Invoke(*((9057, LCID, 4, 0) + (value,) + ()))
	def _set_NodeID(self, value):
		if "NodeID" in self.__dict__: self.__dict__["NodeID"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_OrientationReferenceMarker(self, value):
		if "OrientationReferenceMarker" in self.__dict__: self.__dict__["OrientationReferenceMarker"] = value; return
		self._oleobj_.Invoke(*((9055, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceType(self, value):
		if "ReferenceType" in self.__dict__: self.__dict__["ReferenceType"] = value; return
		self._oleobj_.Invoke(*((9056, LCID, 4, 0) + (value,) + ()))
	def _set_Select(self, value):
		if "Select" in self.__dict__: self.__dict__["Select"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_UseOrientationReferenceMarker(self, value):
		if "UseOrientationReferenceMarker" in self.__dict__: self.__dict__["UseOrientationReferenceMarker"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))

	Body = property(_get_Body, None)
	'''
	Body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	Marker = property(_get_Marker, _set_Marker)
	'''
	reference marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	NodeID = property(_get_NodeID, _set_NodeID)
	'''
	Reference Node ID

	:type: int
	'''
	OrientationReferenceMarker = property(_get_OrientationReferenceMarker, _set_OrientationReferenceMarker)
	'''
	OrientationReferenceMarker is obsolete function

	:type: recurdyn.ProcessNet.IMarker
	'''
	ReferenceType = property(_get_ReferenceType, _set_ReferenceType)
	'''
	Reference Type

	:type: recurdyn.Flexible.ContourReferenceType
	'''
	Select = property(_get_Select, _set_Select)
	'''
	Selection

	:type: bool
	'''
	UseOrientationReferenceMarker = property(_get_UseOrientationReferenceMarker, _set_UseOrientationReferenceMarker)
	'''
	UseOrientationReferenceMarker is obsolete function

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Marker": _set_Marker,
		"_set_NodeID": _set_NodeID,
		"_set_OrientationReferenceMarker": _set_OrientationReferenceMarker,
		"_set_ReferenceType": _set_ReferenceType,
		"_set_Select": _set_Select,
		"_set_UseOrientationReferenceMarker": _set_UseOrientationReferenceMarker,
	}
	_prop_map_get_ = {
		"Body": (9053, 2, (9, 0), (), "Body", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Marker": (9057, 2, (9, 0), (), "Marker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"NodeID": (9052, 2, (3, 0), (), "NodeID", None),
		"OrientationReferenceMarker": (9055, 2, (9, 0), (), "OrientationReferenceMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"ReferenceType": (9056, 2, (3, 0), (), "ReferenceType", '{D18FC6B4-5F7E-4DBD-BD41-407ECD00EFCE}'),
		"Select": (9051, 2, (11, 0), (), "Select", None),
		"UseOrientationReferenceMarker": (9054, 2, (11, 0), (), "UseOrientationReferenceMarker", None),
	}
	_prop_map_put_ = {
		"Marker": ((9057, LCID, 4, 0),()),
		"NodeID": ((9052, LCID, 4, 0),()),
		"OrientationReferenceMarker": ((9055, LCID, 4, 0),()),
		"ReferenceType": ((9056, LCID, 4, 0),()),
		"Select": ((9051, LCID, 4, 0),()),
		"UseOrientationReferenceMarker": ((9054, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IContourReferenceNodeCollection(DispatchBaseClass):
	'''IConourReferenceNodeCollection'''
	CLSID = IID('{CC340394-39A2-489C-B59E-F62063FBE6D2}')
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
		:rtype: recurdyn.Flexible.IContourReferenceNode
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FB58C4A7-6D67-465F-A7D3-ADB1B7E53425}')
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
		:rtype: recurdyn.Flexible.IContourReferenceNode
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FB58C4A7-6D67-465F-A7D3-ADB1B7E53425}')
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
		return win32com.client.util.Iterator(ob, '{FB58C4A7-6D67-465F-A7D3-ADB1B7E53425}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{FB58C4A7-6D67-465F-A7D3-ADB1B7E53425}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IContourStyleOption(DispatchBaseClass):
	'''Contour Style Option'''
	CLSID = IID('{FC113BCB-DE52-4C7B-BE93-029A709898B0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ColorType(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "ColorType", '{2E75ED6F-ECC0-4EDD-90F6-E5A3EDB5B6F6}'))
	def _get_ExceedMaxColor(self):
		return self._ApplyTypes_(*(9059, 2, (19, 0), (), "ExceedMaxColor", None))
	def _get_GrayScaleColor(self):
		return self._ApplyTypes_(*(9055, 2, (19, 0), (), "GrayScaleColor", None))
	def _get_LessThanMinColor(self):
		return self._ApplyTypes_(*(9060, 2, (19, 0), (), "LessThanMinColor", None))
	def _get_MeshLinesColor(self):
		return self._ApplyTypes_(*(9058, 2, (19, 0), (), "MeshLinesColor", None))
	def _get_ShowMeshLines(self):
		return self._ApplyTypes_(*(9057, 2, (11, 0), (), "ShowMeshLines", None))
	def _get_SpectrumMaxColor(self):
		return self._ApplyTypes_(*(9054, 2, (19, 0), (), "SpectrumMaxColor", None))
	def _get_SpectrumMinColor(self):
		return self._ApplyTypes_(*(9053, 2, (19, 0), (), "SpectrumMinColor", None))
	def _get_Style(self):
		return self._ApplyTypes_(*(9052, 2, (3, 0), (), "Style", '{3FA68C9E-D1C2-49D0-B5F1-6603FFCFAB56}'))
	def _get_TextColor(self):
		return self._ApplyTypes_(*(9056, 2, (19, 0), (), "TextColor", None))

	def _set_ColorType(self, value):
		if "ColorType" in self.__dict__: self.__dict__["ColorType"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_ExceedMaxColor(self, value):
		if "ExceedMaxColor" in self.__dict__: self.__dict__["ExceedMaxColor"] = value; return
		self._oleobj_.Invoke(*((9059, LCID, 4, 0) + (value,) + ()))
	def _set_GrayScaleColor(self, value):
		if "GrayScaleColor" in self.__dict__: self.__dict__["GrayScaleColor"] = value; return
		self._oleobj_.Invoke(*((9055, LCID, 4, 0) + (value,) + ()))
	def _set_LessThanMinColor(self, value):
		if "LessThanMinColor" in self.__dict__: self.__dict__["LessThanMinColor"] = value; return
		self._oleobj_.Invoke(*((9060, LCID, 4, 0) + (value,) + ()))
	def _set_MeshLinesColor(self, value):
		if "MeshLinesColor" in self.__dict__: self.__dict__["MeshLinesColor"] = value; return
		self._oleobj_.Invoke(*((9058, LCID, 4, 0) + (value,) + ()))
	def _set_ShowMeshLines(self, value):
		if "ShowMeshLines" in self.__dict__: self.__dict__["ShowMeshLines"] = value; return
		self._oleobj_.Invoke(*((9057, LCID, 4, 0) + (value,) + ()))
	def _set_SpectrumMaxColor(self, value):
		if "SpectrumMaxColor" in self.__dict__: self.__dict__["SpectrumMaxColor"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))
	def _set_SpectrumMinColor(self, value):
		if "SpectrumMinColor" in self.__dict__: self.__dict__["SpectrumMinColor"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_Style(self, value):
		if "Style" in self.__dict__: self.__dict__["Style"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_TextColor(self, value):
		if "TextColor" in self.__dict__: self.__dict__["TextColor"] = value; return
		self._oleobj_.Invoke(*((9056, LCID, 4, 0) + (value,) + ()))

	ColorType = property(_get_ColorType, _set_ColorType)
	'''
	Color Type

	:type: recurdyn.ProcessNet.ContourColorType
	'''
	ExceedMaxColor = property(_get_ExceedMaxColor, _set_ExceedMaxColor)
	'''
	Exceed Max Color

	:type: int
	'''
	GrayScaleColor = property(_get_GrayScaleColor, _set_GrayScaleColor)
	'''
	Gray Scale Color

	:type: int
	'''
	LessThanMinColor = property(_get_LessThanMinColor, _set_LessThanMinColor)
	'''
	Less than Min Color

	:type: int
	'''
	MeshLinesColor = property(_get_MeshLinesColor, _set_MeshLinesColor)
	'''
	Mesh Lines Color

	:type: int
	'''
	ShowMeshLines = property(_get_ShowMeshLines, _set_ShowMeshLines)
	'''
	Show Mesh Lines

	:type: bool
	'''
	SpectrumMaxColor = property(_get_SpectrumMaxColor, _set_SpectrumMaxColor)
	'''
	Spectrum Max Color

	:type: int
	'''
	SpectrumMinColor = property(_get_SpectrumMinColor, _set_SpectrumMinColor)
	'''
	Spectrum Min Color

	:type: int
	'''
	Style = property(_get_Style, _set_Style)
	'''
	Color Style

	:type: recurdyn.Flexible.ContourColorStyle
	'''
	TextColor = property(_get_TextColor, _set_TextColor)
	'''
	Text Color

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_ColorType": _set_ColorType,
		"_set_ExceedMaxColor": _set_ExceedMaxColor,
		"_set_GrayScaleColor": _set_GrayScaleColor,
		"_set_LessThanMinColor": _set_LessThanMinColor,
		"_set_MeshLinesColor": _set_MeshLinesColor,
		"_set_ShowMeshLines": _set_ShowMeshLines,
		"_set_SpectrumMaxColor": _set_SpectrumMaxColor,
		"_set_SpectrumMinColor": _set_SpectrumMinColor,
		"_set_Style": _set_Style,
		"_set_TextColor": _set_TextColor,
	}
	_prop_map_get_ = {
		"ColorType": (9051, 2, (3, 0), (), "ColorType", '{2E75ED6F-ECC0-4EDD-90F6-E5A3EDB5B6F6}'),
		"ExceedMaxColor": (9059, 2, (19, 0), (), "ExceedMaxColor", None),
		"GrayScaleColor": (9055, 2, (19, 0), (), "GrayScaleColor", None),
		"LessThanMinColor": (9060, 2, (19, 0), (), "LessThanMinColor", None),
		"MeshLinesColor": (9058, 2, (19, 0), (), "MeshLinesColor", None),
		"ShowMeshLines": (9057, 2, (11, 0), (), "ShowMeshLines", None),
		"SpectrumMaxColor": (9054, 2, (19, 0), (), "SpectrumMaxColor", None),
		"SpectrumMinColor": (9053, 2, (19, 0), (), "SpectrumMinColor", None),
		"Style": (9052, 2, (3, 0), (), "Style", '{3FA68C9E-D1C2-49D0-B5F1-6603FFCFAB56}'),
		"TextColor": (9056, 2, (19, 0), (), "TextColor", None),
	}
	_prop_map_put_ = {
		"ColorType": ((9051, LCID, 4, 0),()),
		"ExceedMaxColor": ((9059, LCID, 4, 0),()),
		"GrayScaleColor": ((9055, LCID, 4, 0),()),
		"LessThanMinColor": ((9060, LCID, 4, 0),()),
		"MeshLinesColor": ((9058, LCID, 4, 0),()),
		"ShowMeshLines": ((9057, LCID, 4, 0),()),
		"SpectrumMaxColor": ((9054, LCID, 4, 0),()),
		"SpectrumMinColor": ((9053, LCID, 4, 0),()),
		"Style": ((9052, LCID, 4, 0),()),
		"TextColor": ((9056, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IContourTypeOption(DispatchBaseClass):
	'''Contour Type Option'''
	CLSID = IID('{49E653C4-054B-4496-B4FA-9EF8947B2C94}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Component(self):
		return self._ApplyTypes_(*(9052, 2, (3, 0), (), "Component", '{72EFA71D-BCE9-4369-9F66-CEB35906BB91}'))
	def _get_ContactSurfaceOnly(self):
		return self._ApplyTypes_(*(9053, 2, (11, 0), (), "ContactSurfaceOnly", None))
	def _get_ContactSurfaceOnlyType(self):
		return self._ApplyTypes_(*(9054, 2, (3, 0), (), "ContactSurfaceOnlyType", '{C95A86C1-418C-4819-805F-C3A8B0462E52}'))
	def _get_Type(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "Type", '{5F0554C6-5E01-4507-BC62-CABBE3020C2C}'))
	def _get_VectorDisplay(self):
		return self._ApplyTypes_(*(9055, 2, (11, 0), (), "VectorDisplay", None))
	def _get_VectorDisplayArrowSize(self):
		return self._ApplyTypes_(*(9056, 2, (5, 0), (), "VectorDisplayArrowSize", None))
	def _get_VectorDisplayArrowSizeUniformFlag(self):
		return self._ApplyTypes_(*(9057, 2, (11, 0), (), "VectorDisplayArrowSizeUniformFlag", None))

	def _set_Component(self, value):
		if "Component" in self.__dict__: self.__dict__["Component"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_ContactSurfaceOnly(self, value):
		if "ContactSurfaceOnly" in self.__dict__: self.__dict__["ContactSurfaceOnly"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_ContactSurfaceOnlyType(self, value):
		if "ContactSurfaceOnlyType" in self.__dict__: self.__dict__["ContactSurfaceOnlyType"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))
	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_VectorDisplay(self, value):
		if "VectorDisplay" in self.__dict__: self.__dict__["VectorDisplay"] = value; return
		self._oleobj_.Invoke(*((9055, LCID, 4, 0) + (value,) + ()))
	def _set_VectorDisplayArrowSize(self, value):
		if "VectorDisplayArrowSize" in self.__dict__: self.__dict__["VectorDisplayArrowSize"] = value; return
		self._oleobj_.Invoke(*((9056, LCID, 4, 0) + (value,) + ()))
	def _set_VectorDisplayArrowSizeUniformFlag(self, value):
		if "VectorDisplayArrowSizeUniformFlag" in self.__dict__: self.__dict__["VectorDisplayArrowSizeUniformFlag"] = value; return
		self._oleobj_.Invoke(*((9057, LCID, 4, 0) + (value,) + ()))

	Component = property(_get_Component, _set_Component)
	'''
	Component

	:type: recurdyn.Flexible.ContourComponent
	'''
	ContactSurfaceOnly = property(_get_ContactSurfaceOnly, _set_ContactSurfaceOnly)
	'''
	Contact Surface Only Flag

	:type: bool
	'''
	ContactSurfaceOnlyType = property(_get_ContactSurfaceOnlyType, _set_ContactSurfaceOnlyType)
	'''
	Contact Surface Only Type

	:type: recurdyn.Flexible.ContourContactSurfaceOnlyType
	'''
	Type = property(_get_Type, _set_Type)
	'''
	Type

	:type: recurdyn.Flexible.ContourType
	'''
	VectorDisplay = property(_get_VectorDisplay, _set_VectorDisplay)
	'''
	Vector Display Flag

	:type: bool
	'''
	VectorDisplayArrowSize = property(_get_VectorDisplayArrowSize, _set_VectorDisplayArrowSize)
	'''
	Vector Display Arrow Size

	:type: float
	'''
	VectorDisplayArrowSizeUniformFlag = property(_get_VectorDisplayArrowSizeUniformFlag, _set_VectorDisplayArrowSizeUniformFlag)
	'''
	Vector Display Uniform Arrow Size Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Component": _set_Component,
		"_set_ContactSurfaceOnly": _set_ContactSurfaceOnly,
		"_set_ContactSurfaceOnlyType": _set_ContactSurfaceOnlyType,
		"_set_Type": _set_Type,
		"_set_VectorDisplay": _set_VectorDisplay,
		"_set_VectorDisplayArrowSize": _set_VectorDisplayArrowSize,
		"_set_VectorDisplayArrowSizeUniformFlag": _set_VectorDisplayArrowSizeUniformFlag,
	}
	_prop_map_get_ = {
		"Component": (9052, 2, (3, 0), (), "Component", '{72EFA71D-BCE9-4369-9F66-CEB35906BB91}'),
		"ContactSurfaceOnly": (9053, 2, (11, 0), (), "ContactSurfaceOnly", None),
		"ContactSurfaceOnlyType": (9054, 2, (3, 0), (), "ContactSurfaceOnlyType", '{C95A86C1-418C-4819-805F-C3A8B0462E52}'),
		"Type": (9051, 2, (3, 0), (), "Type", '{5F0554C6-5E01-4507-BC62-CABBE3020C2C}'),
		"VectorDisplay": (9055, 2, (11, 0), (), "VectorDisplay", None),
		"VectorDisplayArrowSize": (9056, 2, (5, 0), (), "VectorDisplayArrowSize", None),
		"VectorDisplayArrowSizeUniformFlag": (9057, 2, (11, 0), (), "VectorDisplayArrowSizeUniformFlag", None),
	}
	_prop_map_put_ = {
		"Component": ((9052, LCID, 4, 0),()),
		"ContactSurfaceOnly": ((9053, LCID, 4, 0),()),
		"ContactSurfaceOnlyType": ((9054, LCID, 4, 0),()),
		"Type": ((9051, LCID, 4, 0),()),
		"VectorDisplay": ((9055, LCID, 4, 0),()),
		"VectorDisplayArrowSize": ((9056, LCID, 4, 0),()),
		"VectorDisplayArrowSizeUniformFlag": ((9057, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDisplaySetting(DispatchBaseClass):
	'''Flexible Body Display Setting'''
	CLSID = IID('{3FDF0768-0052-4B63-9D84-A644C3152051}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetNodeIDFlagWithType(self, valType):
		'''
		Get Show Node ID Flag With Type
		
		:param valType: ShowNodeIDType
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(9011, LCID, 1, (11, 0), ((3, 1),),valType
			)


	def SetNodeIDFlagWithType(self, valType, Val):
		'''
		Set Show Node ID Flag With Type
		
		:param valType: ShowNodeIDType
		:param Val: bool
		'''
		return self._oleobj_.InvokeTypes(9010, LCID, 1, (24, 0), ((3, 1), (11, 1)),valType
			, Val)


	def _get_CuttingPlane(self):
		return self._ApplyTypes_(*(9019, 2, (11, 0), (), "CuttingPlane", None))
	def _get_CuttingPlaneFlexType(self):
		return self._ApplyTypes_(*(9020, 2, (3, 0), (), "CuttingPlaneFlexType", '{06EC13C1-6CEB-4C01-826C-923D1D06B369}'))
	def _get_DisplaySettingElementComponentCollection(self):
		return self._ApplyTypes_(*(9002, 2, (9, 0), (), "DisplaySettingElementComponentCollection", '{52806F36-F171-48E0-8D94-7DD010A28932}'))
	def _get_DisplaySettingElementSetCollection(self):
		return self._ApplyTypes_(*(9004, 2, (9, 0), (), "DisplaySettingElementSetCollection", '{23196F83-DC3B-4007-8FA0-814AB1E6A121}'))
	def _get_DisplaySettingLineSetCollection(self):
		return self._ApplyTypes_(*(9021, 2, (9, 0), (), "DisplaySettingLineSetCollection", '{338BA605-D8D7-4E04-B937-8138288AFE4D}'))
	def _get_DisplaySettingNodeSetCollection(self):
		return self._ApplyTypes_(*(9003, 2, (9, 0), (), "DisplaySettingNodeSetCollection", '{B316708B-BF84-429A-8994-19A2A03A2F1E}'))
	def _get_DisplaySettingPatchSetCollection(self):
		return self._ApplyTypes_(*(9005, 2, (9, 0), (), "DisplaySettingPatchSetCollection", '{51C1F29C-9E5D-4CEA-B013-5623F0FCD1E8}'))
	def _get_DisplaySettingPropertyComponentCollection(self):
		return self._ApplyTypes_(*(9001, 2, (9, 0), (), "DisplaySettingPropertyComponentCollection", '{DFF377E2-7234-4010-96C0-8CA009DEBD56}'))
	def _get_DisplaySettingTopologyComponentCollection(self):
		return self._ApplyTypes_(*(9023, 2, (9, 0), (), "DisplaySettingTopologyComponentCollection", '{B7EAE1DC-7E8F-4008-84B8-801FBCECBB4C}'))
	def _get_FeatureLineColor(self):
		return self._ApplyTypes_(*(9015, 2, (19, 0), (), "FeatureLineColor", None))
	def _get_HighlightColor(self):
		return self._ApplyTypes_(*(9017, 2, (19, 0), (), "HighlightColor", None))
	def _get_MeshLineColor(self):
		return self._ApplyTypes_(*(9013, 2, (19, 0), (), "MeshLineColor", None))
	def _get_NodeColor(self):
		return self._ApplyTypes_(*(9018, 2, (19, 0), (), "NodeColor", None))
	def _get_ShowAllNodes(self):
		return self._ApplyTypes_(*(9007, 2, (11, 0), (), "ShowAllNodes", None))
	def _get_ShowBC(self):
		return self._ApplyTypes_(*(9006, 2, (11, 0), (), "ShowBC", None))
	def _get_ShowBeamCrossSection(self):
		return self._ApplyTypes_(*(9022, 2, (11, 0), (), "ShowBeamCrossSection", None))
	def _get_ShowFeatureLine(self):
		return self._ApplyTypes_(*(9014, 2, (11, 0), (), "ShowFeatureLine", None))
	def _get_ShowMeshLine(self):
		return self._ApplyTypes_(*(9012, 2, (11, 0), (), "ShowMeshLine", None))
	def _get_ShowNodeID(self):
		return self._ApplyTypes_(*(9009, 2, (11, 0), (), "ShowNodeID", None))
	def _get_ShowOutput(self):
		return self._ApplyTypes_(*(9008, 2, (11, 0), (), "ShowOutput", None))
	def _get_ShowRenderFeatureLineOnly(self):
		return self._ApplyTypes_(*(9016, 2, (11, 0), (), "ShowRenderFeatureLineOnly", None))
	def _get_ShowShellThickness(self):
		return self._ApplyTypes_(*(9024, 2, (11, 0), (), "ShowShellThickness", None))

	def _set_CuttingPlane(self, value):
		if "CuttingPlane" in self.__dict__: self.__dict__["CuttingPlane"] = value; return
		self._oleobj_.Invoke(*((9019, LCID, 4, 0) + (value,) + ()))
	def _set_CuttingPlaneFlexType(self, value):
		if "CuttingPlaneFlexType" in self.__dict__: self.__dict__["CuttingPlaneFlexType"] = value; return
		self._oleobj_.Invoke(*((9020, LCID, 4, 0) + (value,) + ()))
	def _set_FeatureLineColor(self, value):
		if "FeatureLineColor" in self.__dict__: self.__dict__["FeatureLineColor"] = value; return
		self._oleobj_.Invoke(*((9015, LCID, 4, 0) + (value,) + ()))
	def _set_HighlightColor(self, value):
		if "HighlightColor" in self.__dict__: self.__dict__["HighlightColor"] = value; return
		self._oleobj_.Invoke(*((9017, LCID, 4, 0) + (value,) + ()))
	def _set_MeshLineColor(self, value):
		if "MeshLineColor" in self.__dict__: self.__dict__["MeshLineColor"] = value; return
		self._oleobj_.Invoke(*((9013, LCID, 4, 0) + (value,) + ()))
	def _set_NodeColor(self, value):
		if "NodeColor" in self.__dict__: self.__dict__["NodeColor"] = value; return
		self._oleobj_.Invoke(*((9018, LCID, 4, 0) + (value,) + ()))
	def _set_ShowAllNodes(self, value):
		if "ShowAllNodes" in self.__dict__: self.__dict__["ShowAllNodes"] = value; return
		self._oleobj_.Invoke(*((9007, LCID, 4, 0) + (value,) + ()))
	def _set_ShowBC(self, value):
		if "ShowBC" in self.__dict__: self.__dict__["ShowBC"] = value; return
		self._oleobj_.Invoke(*((9006, LCID, 4, 0) + (value,) + ()))
	def _set_ShowBeamCrossSection(self, value):
		if "ShowBeamCrossSection" in self.__dict__: self.__dict__["ShowBeamCrossSection"] = value; return
		self._oleobj_.Invoke(*((9022, LCID, 4, 0) + (value,) + ()))
	def _set_ShowFeatureLine(self, value):
		if "ShowFeatureLine" in self.__dict__: self.__dict__["ShowFeatureLine"] = value; return
		self._oleobj_.Invoke(*((9014, LCID, 4, 0) + (value,) + ()))
	def _set_ShowMeshLine(self, value):
		if "ShowMeshLine" in self.__dict__: self.__dict__["ShowMeshLine"] = value; return
		self._oleobj_.Invoke(*((9012, LCID, 4, 0) + (value,) + ()))
	def _set_ShowNodeID(self, value):
		if "ShowNodeID" in self.__dict__: self.__dict__["ShowNodeID"] = value; return
		self._oleobj_.Invoke(*((9009, LCID, 4, 0) + (value,) + ()))
	def _set_ShowOutput(self, value):
		if "ShowOutput" in self.__dict__: self.__dict__["ShowOutput"] = value; return
		self._oleobj_.Invoke(*((9008, LCID, 4, 0) + (value,) + ()))
	def _set_ShowRenderFeatureLineOnly(self, value):
		if "ShowRenderFeatureLineOnly" in self.__dict__: self.__dict__["ShowRenderFeatureLineOnly"] = value; return
		self._oleobj_.Invoke(*((9016, LCID, 4, 0) + (value,) + ()))
	def _set_ShowShellThickness(self, value):
		if "ShowShellThickness" in self.__dict__: self.__dict__["ShowShellThickness"] = value; return
		self._oleobj_.Invoke(*((9024, LCID, 4, 0) + (value,) + ()))

	CuttingPlane = property(_get_CuttingPlane, _set_CuttingPlane)
	'''
	Apply cutting plane to a flex body. A flex body will show cross sections of elements.

	:type: bool
	'''
	CuttingPlaneFlexType = property(_get_CuttingPlaneFlexType, _set_CuttingPlaneFlexType)
	'''
	When appling cutting plane to a flex body, a flex body will show the cross section of the elements or whole elements' shape within a cutting plane.

	:type: recurdyn.Flexible.CuttingPlaneFlexType
	'''
	DisplaySettingElementComponentCollection = property(_get_DisplaySettingElementComponentCollection, None)
	'''
	Contains Element Component

	:type: recurdyn.Flexible.IDisplaySettingElementComponentCollection
	'''
	DisplaySettingElementSetCollection = property(_get_DisplaySettingElementSetCollection, None)
	'''
	Contains ElementSet Display Setting

	:type: recurdyn.Flexible.IDisplaySettingElementSetCollection
	'''
	DisplaySettingLineSetCollection = property(_get_DisplaySettingLineSetCollection, None)
	'''
	Contains LineSet Display Setting

	:type: recurdyn.Flexible.IDisplaySettingLineSetCollection
	'''
	DisplaySettingNodeSetCollection = property(_get_DisplaySettingNodeSetCollection, None)
	'''
	Contains NodeSet Display Setting

	:type: recurdyn.Flexible.IDisplaySettingNodeSetCollection
	'''
	DisplaySettingPatchSetCollection = property(_get_DisplaySettingPatchSetCollection, None)
	'''
	Contains PatchSet Display Setting

	:type: recurdyn.Flexible.IDisplaySettingPatchSetCollection
	'''
	DisplaySettingPropertyComponentCollection = property(_get_DisplaySettingPropertyComponentCollection, None)
	'''
	Contains Property Component

	:type: recurdyn.Flexible.IDisplaySettingPropertyComponentCollection
	'''
	DisplaySettingTopologyComponentCollection = property(_get_DisplaySettingTopologyComponentCollection, None)
	'''
	Contains Topology Component

	:type: recurdyn.Flexible.IDisplaySettingTopologyComponentCollection
	'''
	FeatureLineColor = property(_get_FeatureLineColor, _set_FeatureLineColor)
	'''
	Feature Line Color

	:type: int
	'''
	HighlightColor = property(_get_HighlightColor, _set_HighlightColor)
	'''
	Hightlight Color

	:type: int
	'''
	MeshLineColor = property(_get_MeshLineColor, _set_MeshLineColor)
	'''
	Mesh Line Color

	:type: int
	'''
	NodeColor = property(_get_NodeColor, _set_NodeColor)
	'''
	Stand Alone Node Color

	:type: int
	'''
	ShowAllNodes = property(_get_ShowAllNodes, _set_ShowAllNodes)
	'''
	Show Node Flag

	:type: bool
	'''
	ShowBC = property(_get_ShowBC, _set_ShowBC)
	'''
	Show BC Flag

	:type: bool
	'''
	ShowBeamCrossSection = property(_get_ShowBeamCrossSection, _set_ShowBeamCrossSection)
	'''
	Show Beam Cross Section Flag

	:type: bool
	'''
	ShowFeatureLine = property(_get_ShowFeatureLine, _set_ShowFeatureLine)
	'''
	Show Feature Line Flag

	:type: bool
	'''
	ShowMeshLine = property(_get_ShowMeshLine, _set_ShowMeshLine)
	'''
	Show Mesh Line Flag

	:type: bool
	'''
	ShowNodeID = property(_get_ShowNodeID, _set_ShowNodeID)
	'''
	Show Node ID Flag

	:type: bool
	'''
	ShowOutput = property(_get_ShowOutput, _set_ShowOutput)
	'''
	Show Output Flag

	:type: bool
	'''
	ShowRenderFeatureLineOnly = property(_get_ShowRenderFeatureLineOnly, _set_ShowRenderFeatureLineOnly)
	'''
	Show Render Feature Line Only Flag

	:type: bool
	'''
	ShowShellThickness = property(_get_ShowShellThickness, _set_ShowShellThickness)
	'''
	Show Shell Thickness Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_CuttingPlane": _set_CuttingPlane,
		"_set_CuttingPlaneFlexType": _set_CuttingPlaneFlexType,
		"_set_FeatureLineColor": _set_FeatureLineColor,
		"_set_HighlightColor": _set_HighlightColor,
		"_set_MeshLineColor": _set_MeshLineColor,
		"_set_NodeColor": _set_NodeColor,
		"_set_ShowAllNodes": _set_ShowAllNodes,
		"_set_ShowBC": _set_ShowBC,
		"_set_ShowBeamCrossSection": _set_ShowBeamCrossSection,
		"_set_ShowFeatureLine": _set_ShowFeatureLine,
		"_set_ShowMeshLine": _set_ShowMeshLine,
		"_set_ShowNodeID": _set_ShowNodeID,
		"_set_ShowOutput": _set_ShowOutput,
		"_set_ShowRenderFeatureLineOnly": _set_ShowRenderFeatureLineOnly,
		"_set_ShowShellThickness": _set_ShowShellThickness,
	}
	_prop_map_get_ = {
		"CuttingPlane": (9019, 2, (11, 0), (), "CuttingPlane", None),
		"CuttingPlaneFlexType": (9020, 2, (3, 0), (), "CuttingPlaneFlexType", '{06EC13C1-6CEB-4C01-826C-923D1D06B369}'),
		"DisplaySettingElementComponentCollection": (9002, 2, (9, 0), (), "DisplaySettingElementComponentCollection", '{52806F36-F171-48E0-8D94-7DD010A28932}'),
		"DisplaySettingElementSetCollection": (9004, 2, (9, 0), (), "DisplaySettingElementSetCollection", '{23196F83-DC3B-4007-8FA0-814AB1E6A121}'),
		"DisplaySettingLineSetCollection": (9021, 2, (9, 0), (), "DisplaySettingLineSetCollection", '{338BA605-D8D7-4E04-B937-8138288AFE4D}'),
		"DisplaySettingNodeSetCollection": (9003, 2, (9, 0), (), "DisplaySettingNodeSetCollection", '{B316708B-BF84-429A-8994-19A2A03A2F1E}'),
		"DisplaySettingPatchSetCollection": (9005, 2, (9, 0), (), "DisplaySettingPatchSetCollection", '{51C1F29C-9E5D-4CEA-B013-5623F0FCD1E8}'),
		"DisplaySettingPropertyComponentCollection": (9001, 2, (9, 0), (), "DisplaySettingPropertyComponentCollection", '{DFF377E2-7234-4010-96C0-8CA009DEBD56}'),
		"DisplaySettingTopologyComponentCollection": (9023, 2, (9, 0), (), "DisplaySettingTopologyComponentCollection", '{B7EAE1DC-7E8F-4008-84B8-801FBCECBB4C}'),
		"FeatureLineColor": (9015, 2, (19, 0), (), "FeatureLineColor", None),
		"HighlightColor": (9017, 2, (19, 0), (), "HighlightColor", None),
		"MeshLineColor": (9013, 2, (19, 0), (), "MeshLineColor", None),
		"NodeColor": (9018, 2, (19, 0), (), "NodeColor", None),
		"ShowAllNodes": (9007, 2, (11, 0), (), "ShowAllNodes", None),
		"ShowBC": (9006, 2, (11, 0), (), "ShowBC", None),
		"ShowBeamCrossSection": (9022, 2, (11, 0), (), "ShowBeamCrossSection", None),
		"ShowFeatureLine": (9014, 2, (11, 0), (), "ShowFeatureLine", None),
		"ShowMeshLine": (9012, 2, (11, 0), (), "ShowMeshLine", None),
		"ShowNodeID": (9009, 2, (11, 0), (), "ShowNodeID", None),
		"ShowOutput": (9008, 2, (11, 0), (), "ShowOutput", None),
		"ShowRenderFeatureLineOnly": (9016, 2, (11, 0), (), "ShowRenderFeatureLineOnly", None),
		"ShowShellThickness": (9024, 2, (11, 0), (), "ShowShellThickness", None),
	}
	_prop_map_put_ = {
		"CuttingPlane": ((9019, LCID, 4, 0),()),
		"CuttingPlaneFlexType": ((9020, LCID, 4, 0),()),
		"FeatureLineColor": ((9015, LCID, 4, 0),()),
		"HighlightColor": ((9017, LCID, 4, 0),()),
		"MeshLineColor": ((9013, LCID, 4, 0),()),
		"NodeColor": ((9018, LCID, 4, 0),()),
		"ShowAllNodes": ((9007, LCID, 4, 0),()),
		"ShowBC": ((9006, LCID, 4, 0),()),
		"ShowBeamCrossSection": ((9022, LCID, 4, 0),()),
		"ShowFeatureLine": ((9014, LCID, 4, 0),()),
		"ShowMeshLine": ((9012, LCID, 4, 0),()),
		"ShowNodeID": ((9009, LCID, 4, 0),()),
		"ShowOutput": ((9008, LCID, 4, 0),()),
		"ShowRenderFeatureLineOnly": ((9016, LCID, 4, 0),()),
		"ShowShellThickness": ((9024, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDisplaySettingElementComponent(DispatchBaseClass):
	'''Element Component'''
	CLSID = IID('{DE06422B-331F-496E-BCAD-FBBB082D57F2}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Color(self):
		return self._ApplyTypes_(*(9053, 2, (19, 0), (), "Color", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(9051, 2, (8, 0), (), "Name", None))
	def _get_Show(self):
		return self._ApplyTypes_(*(9052, 2, (11, 0), (), "Show", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_Show(self, value):
		if "Show" in self.__dict__: self.__dict__["Show"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Name = property(_get_Name, None)
	'''
	Name

	:type: str
	'''
	Show = property(_get_Show, _set_Show)
	'''
	Show Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Show": _set_Show,
	}
	_prop_map_get_ = {
		"Color": (9053, 2, (19, 0), (), "Color", None),
		"Name": (9051, 2, (8, 0), (), "Name", None),
		"Show": (9052, 2, (11, 0), (), "Show", None),
	}
	_prop_map_put_ = {
		"Color": ((9053, LCID, 4, 0),()),
		"Show": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDisplaySettingElementComponentCollection(DispatchBaseClass):
	'''IDisplaySettingElementComponentCollection'''
	CLSID = IID('{52806F36-F171-48E0-8D94-7DD010A28932}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingElementComponent
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DE06422B-331F-496E-BCAD-FBBB082D57F2}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingElementComponent
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DE06422B-331F-496E-BCAD-FBBB082D57F2}')
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
		return win32com.client.util.Iterator(ob, '{DE06422B-331F-496E-BCAD-FBBB082D57F2}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{DE06422B-331F-496E-BCAD-FBBB082D57F2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDisplaySettingElementSet(DispatchBaseClass):
	'''Display Setting ElementSet'''
	CLSID = IID('{C08D408A-9B9B-4F2D-A029-E4BA81008A6B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Color(self):
		return self._ApplyTypes_(*(9053, 2, (19, 0), (), "Color", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(9051, 2, (8, 0), (), "Name", None))
	def _get_Show(self):
		return self._ApplyTypes_(*(9052, 2, (11, 0), (), "Show", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_Show(self, value):
		if "Show" in self.__dict__: self.__dict__["Show"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Name = property(_get_Name, None)
	'''
	Name

	:type: str
	'''
	Show = property(_get_Show, _set_Show)
	'''
	Show Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Show": _set_Show,
	}
	_prop_map_get_ = {
		"Color": (9053, 2, (19, 0), (), "Color", None),
		"Name": (9051, 2, (8, 0), (), "Name", None),
		"Show": (9052, 2, (11, 0), (), "Show", None),
	}
	_prop_map_put_ = {
		"Color": ((9053, LCID, 4, 0),()),
		"Show": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDisplaySettingElementSetCollection(DispatchBaseClass):
	'''IDisplaySettingElementSetCollection'''
	CLSID = IID('{23196F83-DC3B-4007-8FA0-814AB1E6A121}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingElementSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{C08D408A-9B9B-4F2D-A029-E4BA81008A6B}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingElementSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{C08D408A-9B9B-4F2D-A029-E4BA81008A6B}')
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
		return win32com.client.util.Iterator(ob, '{C08D408A-9B9B-4F2D-A029-E4BA81008A6B}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{C08D408A-9B9B-4F2D-A029-E4BA81008A6B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDisplaySettingLineSet(DispatchBaseClass):
	'''Display Setting LineSet'''
	CLSID = IID('{BF489D0D-9A7B-4C64-8AA9-FA3330A12A33}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Color(self):
		return self._ApplyTypes_(*(9053, 2, (19, 0), (), "Color", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(9051, 2, (8, 0), (), "Name", None))
	def _get_Show(self):
		return self._ApplyTypes_(*(9052, 2, (11, 0), (), "Show", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_Show(self, value):
		if "Show" in self.__dict__: self.__dict__["Show"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Name = property(_get_Name, None)
	'''
	Name

	:type: str
	'''
	Show = property(_get_Show, _set_Show)
	'''
	Show Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Show": _set_Show,
	}
	_prop_map_get_ = {
		"Color": (9053, 2, (19, 0), (), "Color", None),
		"Name": (9051, 2, (8, 0), (), "Name", None),
		"Show": (9052, 2, (11, 0), (), "Show", None),
	}
	_prop_map_put_ = {
		"Color": ((9053, LCID, 4, 0),()),
		"Show": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDisplaySettingLineSetCollection(DispatchBaseClass):
	'''IDisplaySettingLineSetCollection'''
	CLSID = IID('{338BA605-D8D7-4E04-B937-8138288AFE4D}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingLineSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{BF489D0D-9A7B-4C64-8AA9-FA3330A12A33}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingLineSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{BF489D0D-9A7B-4C64-8AA9-FA3330A12A33}')
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
		return win32com.client.util.Iterator(ob, '{BF489D0D-9A7B-4C64-8AA9-FA3330A12A33}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{BF489D0D-9A7B-4C64-8AA9-FA3330A12A33}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDisplaySettingNodeSet(DispatchBaseClass):
	'''Display Setting NodeSet'''
	CLSID = IID('{ABB44B8A-B12A-452A-9F5F-C40C189D93C4}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Color(self):
		return self._ApplyTypes_(*(9053, 2, (19, 0), (), "Color", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(9051, 2, (8, 0), (), "Name", None))
	def _get_Show(self):
		return self._ApplyTypes_(*(9052, 2, (11, 0), (), "Show", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_Show(self, value):
		if "Show" in self.__dict__: self.__dict__["Show"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Name = property(_get_Name, None)
	'''
	Name

	:type: str
	'''
	Show = property(_get_Show, _set_Show)
	'''
	Show Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Show": _set_Show,
	}
	_prop_map_get_ = {
		"Color": (9053, 2, (19, 0), (), "Color", None),
		"Name": (9051, 2, (8, 0), (), "Name", None),
		"Show": (9052, 2, (11, 0), (), "Show", None),
	}
	_prop_map_put_ = {
		"Color": ((9053, LCID, 4, 0),()),
		"Show": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDisplaySettingNodeSetCollection(DispatchBaseClass):
	'''IDisplaySettingNodeSetCollection'''
	CLSID = IID('{B316708B-BF84-429A-8994-19A2A03A2F1E}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingNodeSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{ABB44B8A-B12A-452A-9F5F-C40C189D93C4}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingNodeSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{ABB44B8A-B12A-452A-9F5F-C40C189D93C4}')
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
		return win32com.client.util.Iterator(ob, '{ABB44B8A-B12A-452A-9F5F-C40C189D93C4}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{ABB44B8A-B12A-452A-9F5F-C40C189D93C4}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDisplaySettingPatchSet(DispatchBaseClass):
	'''Display Setting PatchSet'''
	CLSID = IID('{FD68A22C-A406-4D04-B1D7-1277926333BF}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Color(self):
		return self._ApplyTypes_(*(9053, 2, (19, 0), (), "Color", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(9051, 2, (8, 0), (), "Name", None))
	def _get_Show(self):
		return self._ApplyTypes_(*(9052, 2, (11, 0), (), "Show", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_Show(self, value):
		if "Show" in self.__dict__: self.__dict__["Show"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Name = property(_get_Name, None)
	'''
	Name

	:type: str
	'''
	Show = property(_get_Show, _set_Show)
	'''
	Show Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Show": _set_Show,
	}
	_prop_map_get_ = {
		"Color": (9053, 2, (19, 0), (), "Color", None),
		"Name": (9051, 2, (8, 0), (), "Name", None),
		"Show": (9052, 2, (11, 0), (), "Show", None),
	}
	_prop_map_put_ = {
		"Color": ((9053, LCID, 4, 0),()),
		"Show": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDisplaySettingPatchSetCollection(DispatchBaseClass):
	'''IDisplaySettingPatchSetCollection'''
	CLSID = IID('{51C1F29C-9E5D-4CEA-B013-5623F0FCD1E8}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FD68A22C-A406-4D04-B1D7-1277926333BF}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FD68A22C-A406-4D04-B1D7-1277926333BF}')
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
		return win32com.client.util.Iterator(ob, '{FD68A22C-A406-4D04-B1D7-1277926333BF}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{FD68A22C-A406-4D04-B1D7-1277926333BF}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDisplaySettingPropertyComponent(DispatchBaseClass):
	'''Property Component'''
	CLSID = IID('{3F3FB9FE-0E56-4FEA-A6A8-9912D45B7B10}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Color(self):
		return self._ApplyTypes_(*(9053, 2, (19, 0), (), "Color", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(9051, 2, (8, 0), (), "Name", None))
	def _get_Show(self):
		return self._ApplyTypes_(*(9052, 2, (11, 0), (), "Show", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_Show(self, value):
		if "Show" in self.__dict__: self.__dict__["Show"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Name = property(_get_Name, None)
	'''
	Name

	:type: str
	'''
	Show = property(_get_Show, _set_Show)
	'''
	Show Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Show": _set_Show,
	}
	_prop_map_get_ = {
		"Color": (9053, 2, (19, 0), (), "Color", None),
		"Name": (9051, 2, (8, 0), (), "Name", None),
		"Show": (9052, 2, (11, 0), (), "Show", None),
	}
	_prop_map_put_ = {
		"Color": ((9053, LCID, 4, 0),()),
		"Show": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDisplaySettingPropertyComponentCollection(DispatchBaseClass):
	'''IDisplaySettingPropertyComponentCollection'''
	CLSID = IID('{DFF377E2-7234-4010-96C0-8CA009DEBD56}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingPropertyComponent
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{3F3FB9FE-0E56-4FEA-A6A8-9912D45B7B10}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingPropertyComponent
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{3F3FB9FE-0E56-4FEA-A6A8-9912D45B7B10}')
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
		return win32com.client.util.Iterator(ob, '{3F3FB9FE-0E56-4FEA-A6A8-9912D45B7B10}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{3F3FB9FE-0E56-4FEA-A6A8-9912D45B7B10}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDisplaySettingTopologyComponent(DispatchBaseClass):
	'''Topology Component'''
	CLSID = IID('{F043499D-DB45-419E-AF1F-8F057CAAA006}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Color(self):
		return self._ApplyTypes_(*(9053, 2, (19, 0), (), "Color", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(9051, 2, (8, 0), (), "Name", None))
	def _get_Show(self):
		return self._ApplyTypes_(*(9052, 2, (11, 0), (), "Show", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_Show(self, value):
		if "Show" in self.__dict__: self.__dict__["Show"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Color

	:type: int
	'''
	Name = property(_get_Name, None)
	'''
	Name

	:type: str
	'''
	Show = property(_get_Show, _set_Show)
	'''
	Show Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Show": _set_Show,
	}
	_prop_map_get_ = {
		"Color": (9053, 2, (19, 0), (), "Color", None),
		"Name": (9051, 2, (8, 0), (), "Name", None),
		"Show": (9052, 2, (11, 0), (), "Show", None),
	}
	_prop_map_put_ = {
		"Color": ((9053, LCID, 4, 0),()),
		"Show": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDisplaySettingTopologyComponentCollection(DispatchBaseClass):
	'''IDisplaySettingTopologyComponentCollection'''
	CLSID = IID('{B7EAE1DC-7E8F-4008-84B8-801FBCECBB4C}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingTopologyComponent
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{F043499D-DB45-419E-AF1F-8F057CAAA006}')
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
		:rtype: recurdyn.Flexible.IDisplaySettingTopologyComponent
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{F043499D-DB45-419E-AF1F-8F057CAAA006}')
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
		return win32com.client.util.Iterator(ob, '{F043499D-DB45-419E-AF1F-8F057CAAA006}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{F043499D-DB45-419E-AF1F-8F057CAAA006}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IExportShellFormatData(DispatchBaseClass):
	'''Export Shell Format Data'''
	CLSID = IID('{2EE15E44-AD0C-4D9B-B53A-35BF7F1E1322}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddPatchSets(self, Val):
		'''
		Add PatchSets
		
		:param Val: list[object]
		'''
		_Val_type = True if Val and isinstance(Val[0], win32com.client.VARIANT) else False
		if not _Val_type:
			Val = [win32com.client.VARIANT(12, _data) for _data in Val]

		ret = self._oleobj_.InvokeTypes(9002, LCID, 1, (24, 0), ((8204, 1),),Val
			)

		if not _Val_type:
			Val = [_data.value for _data in Val]

		return ret


	def DeletePatchSets(self, Val):
		'''
		Delete PatchSets
		
		:param Val: list[object]
		'''
		_Val_type = True if Val and isinstance(Val[0], win32com.client.VARIANT) else False
		if not _Val_type:
			Val = [win32com.client.VARIANT(12, _data) for _data in Val]

		ret = self._oleobj_.InvokeTypes(9003, LCID, 1, (24, 0), ((8204, 1),),Val
			)

		if not _Val_type:
			Val = [_data.value for _data in Val]

		return ret


	def Export(self, Val):
		'''
		Export method
		
		:param Val: str
		'''
		return self._oleobj_.InvokeTypes(9004, LCID, 1, (24, 0), ((8, 1),),Val
			)


	def _get_Type(self):
		return self._ApplyTypes_(*(9001, 2, (3, 0), (), "Type", '{47CB4292-A8CC-4A9A-8FD5-A0876C024744}'))

	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((9001, LCID, 4, 0) + (value,) + ()))

	Type = property(_get_Type, _set_Type)
	'''
	Selection Type

	:type: recurdyn.Flexible.ShellDataExportType
	'''

	_prop_map_set_function_ = {
		"_set_Type": _set_Type,
	}
	_prop_map_get_ = {
		"Type": (9001, 2, (3, 0), (), "Type", '{47CB4292-A8CC-4A9A-8FD5-A0876C024744}'),
	}
	_prop_map_put_ = {
		"Type": ((9001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManager(DispatchBaseClass):
	'''GManager'''
	CLSID = IID('{04C740C7-BD7B-4DA9-A03A-CFAD5CBA0FFB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Execute(self):
		'''
		Excute
		'''
		return self._oleobj_.InvokeTypes(9007, LCID, 1, (24, 0), (),)


	def _get_FFlex(self):
		return self._ApplyTypes_(*(9006, 2, (9, 0), (), "FFlex", '{E131531A-921C-4AE5-A53D-F5C39A65AAFF}'))
	def _get_RFlex(self):
		return self._ApplyTypes_(*(9005, 2, (9, 0), (), "RFlex", '{B9638194-9BB8-44A9-B999-4E26073A84E6}'))
	def _get_Rigid(self):
		return self._ApplyTypes_(*(9004, 2, (9, 0), (), "Rigid", '{4FFEA591-BF79-4FF5-95A9-409860AC2D1E}'))
	def _get_SourceBody(self):
		return self._ApplyTypes_(*(9001, 2, (9, 0), (), "SourceBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_SourceBodyType(self):
		return self._ApplyTypes_(*(9002, 2, (3, 0), (), "SourceBodyType", '{169C1AA7-9A04-4768-AAB0-290810BEB2EC}'))
	def _get_TargetBodyType(self):
		return self._ApplyTypes_(*(9003, 2, (3, 0), (), "TargetBodyType", '{169C1AA7-9A04-4768-AAB0-290810BEB2EC}'))

	def _set_SourceBody(self, value):
		if "SourceBody" in self.__dict__: self.__dict__["SourceBody"] = value; return
		self._oleobj_.Invoke(*((9001, LCID, 4, 0) + (value,) + ()))
	def _set_TargetBodyType(self, value):
		if "TargetBodyType" in self.__dict__: self.__dict__["TargetBodyType"] = value; return
		self._oleobj_.Invoke(*((9003, LCID, 4, 0) + (value,) + ()))

	FFlex = property(_get_FFlex, None)
	'''
	Get GManager from FFlex

	:type: recurdyn.Flexible.IGManagerFFlex
	'''
	RFlex = property(_get_RFlex, None)
	'''
	Get GManager from RFlex

	:type: recurdyn.Flexible.IGManagerRFlex
	'''
	Rigid = property(_get_Rigid, None)
	'''
	Get GManager from Rigid

	:type: recurdyn.Flexible.IGManagerRigid
	'''
	SourceBody = property(_get_SourceBody, _set_SourceBody)
	'''
	Source body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	SourceBodyType = property(_get_SourceBodyType, None)
	'''
	Source body Type

	:type: recurdyn.Flexible.BodyType
	'''
	TargetBodyType = property(_get_TargetBodyType, _set_TargetBodyType)
	'''
	Target body Type

	:type: recurdyn.Flexible.BodyType
	'''

	_prop_map_set_function_ = {
		"_set_SourceBody": _set_SourceBody,
		"_set_TargetBodyType": _set_TargetBodyType,
	}
	_prop_map_get_ = {
		"FFlex": (9006, 2, (9, 0), (), "FFlex", '{E131531A-921C-4AE5-A53D-F5C39A65AAFF}'),
		"RFlex": (9005, 2, (9, 0), (), "RFlex", '{B9638194-9BB8-44A9-B999-4E26073A84E6}'),
		"Rigid": (9004, 2, (9, 0), (), "Rigid", '{4FFEA591-BF79-4FF5-95A9-409860AC2D1E}'),
		"SourceBody": (9001, 2, (9, 0), (), "SourceBody", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"SourceBodyType": (9002, 2, (3, 0), (), "SourceBodyType", '{169C1AA7-9A04-4768-AAB0-290810BEB2EC}'),
		"TargetBodyType": (9003, 2, (3, 0), (), "TargetBodyType", '{169C1AA7-9A04-4768-AAB0-290810BEB2EC}'),
	}
	_prop_map_put_ = {
		"SourceBody": ((9001, LCID, 4, 0),()),
		"TargetBodyType": ((9003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerAssistModelingOption(DispatchBaseClass):
	'''GManager Assist Modeling Option'''
	CLSID = IID('{16FD62CA-B60D-4326-9349-593F526D8399}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_TargetBodyName(self):
		return self._ApplyTypes_(*(9052, 2, (8, 0), (), "TargetBodyName", None))
	def _get_UseForce(self):
		return self._ApplyTypes_(*(9056, 2, (11, 0), (), "UseForce", None))
	def _get_UseGeoContact(self):
		return self._ApplyTypes_(*(9057, 2, (11, 0), (), "UseGeoContact", None))
	def _get_UseInitialVelocity(self):
		return self._ApplyTypes_(*(9053, 2, (11, 0), (), "UseInitialVelocity", None))
	def _get_UseJoint(self):
		return self._ApplyTypes_(*(9055, 2, (11, 0), (), "UseJoint", None))
	def _get_UseMassCMPosition(self):
		return self._ApplyTypes_(*(9054, 2, (11, 0), (), "UseMassCMPosition", None))
	def _get_UseName(self):
		return self._ApplyTypes_(*(9051, 2, (11, 0), (), "UseName", None))

	def _set_TargetBodyName(self, value):
		if "TargetBodyName" in self.__dict__: self.__dict__["TargetBodyName"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_UseForce(self, value):
		if "UseForce" in self.__dict__: self.__dict__["UseForce"] = value; return
		self._oleobj_.Invoke(*((9056, LCID, 4, 0) + (value,) + ()))
	def _set_UseGeoContact(self, value):
		if "UseGeoContact" in self.__dict__: self.__dict__["UseGeoContact"] = value; return
		self._oleobj_.Invoke(*((9057, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialVelocity(self, value):
		if "UseInitialVelocity" in self.__dict__: self.__dict__["UseInitialVelocity"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_UseJoint(self, value):
		if "UseJoint" in self.__dict__: self.__dict__["UseJoint"] = value; return
		self._oleobj_.Invoke(*((9055, LCID, 4, 0) + (value,) + ()))
	def _set_UseMassCMPosition(self, value):
		if "UseMassCMPosition" in self.__dict__: self.__dict__["UseMassCMPosition"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))
	def _set_UseName(self, value):
		if "UseName" in self.__dict__: self.__dict__["UseName"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))

	TargetBodyName = property(_get_TargetBodyName, _set_TargetBodyName)
	'''
	Body Name

	:type: str
	'''
	UseForce = property(_get_UseForce, _set_UseForce)
	'''
	Force

	:type: bool
	'''
	UseGeoContact = property(_get_UseGeoContact, _set_UseGeoContact)
	'''
	GeoContact

	:type: bool
	'''
	UseInitialVelocity = property(_get_UseInitialVelocity, _set_UseInitialVelocity)
	'''
	Initial Velocity

	:type: bool
	'''
	UseJoint = property(_get_UseJoint, _set_UseJoint)
	'''
	Joint

	:type: bool
	'''
	UseMassCMPosition = property(_get_UseMassCMPosition, _set_UseMassCMPosition)
	'''
	Mass and CM Position

	:type: bool
	'''
	UseName = property(_get_UseName, _set_UseName)
	'''
	Name

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_TargetBodyName": _set_TargetBodyName,
		"_set_UseForce": _set_UseForce,
		"_set_UseGeoContact": _set_UseGeoContact,
		"_set_UseInitialVelocity": _set_UseInitialVelocity,
		"_set_UseJoint": _set_UseJoint,
		"_set_UseMassCMPosition": _set_UseMassCMPosition,
		"_set_UseName": _set_UseName,
	}
	_prop_map_get_ = {
		"TargetBodyName": (9052, 2, (8, 0), (), "TargetBodyName", None),
		"UseForce": (9056, 2, (11, 0), (), "UseForce", None),
		"UseGeoContact": (9057, 2, (11, 0), (), "UseGeoContact", None),
		"UseInitialVelocity": (9053, 2, (11, 0), (), "UseInitialVelocity", None),
		"UseJoint": (9055, 2, (11, 0), (), "UseJoint", None),
		"UseMassCMPosition": (9054, 2, (11, 0), (), "UseMassCMPosition", None),
		"UseName": (9051, 2, (11, 0), (), "UseName", None),
	}
	_prop_map_put_ = {
		"TargetBodyName": ((9052, LCID, 4, 0),()),
		"UseForce": ((9056, LCID, 4, 0),()),
		"UseGeoContact": ((9057, LCID, 4, 0),()),
		"UseInitialVelocity": ((9053, LCID, 4, 0),()),
		"UseJoint": ((9055, LCID, 4, 0),()),
		"UseMassCMPosition": ((9054, LCID, 4, 0),()),
		"UseName": ((9051, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerFFlex(DispatchBaseClass):
	'''GManager From FFlex Interface '''
	CLSID = IID('{E131531A-921C-4AE5-A53D-F5C39A65AAFF}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_FFlex(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "FFlex", '{7446389E-9E2B-48BD-ACD2-158D332A3B70}'))
	def _get_MeshDataFileName(self):
		return self._ApplyTypes_(*(9055, 2, (8, 0), (), "MeshDataFileName", None))
	def _get_RFlex(self):
		return self._ApplyTypes_(*(9052, 2, (9, 0), (), "RFlex", '{AC2631CE-2984-4F21-B299-4808917E8F75}'))
	def _get_Rigid(self):
		return self._ApplyTypes_(*(9051, 2, (9, 0), (), "Rigid", '{2B8967E0-1892-46E4-A700-9E3384FE1AFF}'))
	def _get_UseCreateMeshDataFile(self):
		return self._ApplyTypes_(*(9054, 2, (11, 0), (), "UseCreateMeshDataFile", None))

	def _set_MeshDataFileName(self, value):
		if "MeshDataFileName" in self.__dict__: self.__dict__["MeshDataFileName"] = value; return
		self._oleobj_.Invoke(*((9055, LCID, 4, 0) + (value,) + ()))
	def _set_UseCreateMeshDataFile(self, value):
		if "UseCreateMeshDataFile" in self.__dict__: self.__dict__["UseCreateMeshDataFile"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))

	FFlex = property(_get_FFlex, None)
	'''
	Get GManager from FFlex to FFlex

	:type: recurdyn.Flexible.IGManagerFFlexToFFlex
	'''
	MeshDataFileName = property(_get_MeshDataFileName, _set_MeshDataFileName)
	'''
	Mesh Data File Name

	:type: str
	'''
	RFlex = property(_get_RFlex, None)
	'''
	Get GManager from FFlex to RFlex

	:type: recurdyn.Flexible.IGManagerFFlexToRFlex
	'''
	Rigid = property(_get_Rigid, None)
	'''
	Get GManager from FFlex to Rigid

	:type: recurdyn.Flexible.IGManagerFFlexToRigid
	'''
	UseCreateMeshDataFile = property(_get_UseCreateMeshDataFile, _set_UseCreateMeshDataFile)
	'''
	Create Mesh Data File Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_MeshDataFileName": _set_MeshDataFileName,
		"_set_UseCreateMeshDataFile": _set_UseCreateMeshDataFile,
	}
	_prop_map_get_ = {
		"FFlex": (9053, 2, (9, 0), (), "FFlex", '{7446389E-9E2B-48BD-ACD2-158D332A3B70}'),
		"MeshDataFileName": (9055, 2, (8, 0), (), "MeshDataFileName", None),
		"RFlex": (9052, 2, (9, 0), (), "RFlex", '{AC2631CE-2984-4F21-B299-4808917E8F75}'),
		"Rigid": (9051, 2, (9, 0), (), "Rigid", '{2B8967E0-1892-46E4-A700-9E3384FE1AFF}'),
		"UseCreateMeshDataFile": (9054, 2, (11, 0), (), "UseCreateMeshDataFile", None),
	}
	_prop_map_put_ = {
		"MeshDataFileName": ((9055, LCID, 4, 0),()),
		"UseCreateMeshDataFile": ((9054, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerFFlexBodySwapOption(DispatchBaseClass):
	'''GManager FFlexBody Swap Option'''
	CLSID = IID('{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_UnitOfSource(self):
		return self._ApplyTypes_(*(9052, 2, (9, 0), (), "UnitOfSource", '{09A65909-6FBB-488A-9726-D320F5666395}'))
	def _get_UseAllowNullProperty(self):
		return self._ApplyTypes_(*(9051, 2, (11, 0), (), "UseAllowNullProperty", None))
	def _get_UseCreateBeamElementWithPreStress(self):
		return self._ApplyTypes_(*(9055, 2, (11, 0), (), "UseCreateBeamElementWithPreStress", None))
	def _get_UseForceConnector(self):
		return self._ApplyTypes_(*(9054, 2, (11, 0), (), "UseForceConnector", None))
	def _get_UseGeneratePatchSetFromNodeElementSet(self):
		return self._ApplyTypes_(*(9056, 2, (11, 0), (), "UseGeneratePatchSetFromNodeElementSet", None))
	def _get_UseUnitForce(self):
		return self._ApplyTypes_(*(9053, 2, (11, 0), (), "UseUnitForce", None))

	def _set_UnitOfSource(self, value):
		if "UnitOfSource" in self.__dict__: self.__dict__["UnitOfSource"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_UseAllowNullProperty(self, value):
		if "UseAllowNullProperty" in self.__dict__: self.__dict__["UseAllowNullProperty"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_UseCreateBeamElementWithPreStress(self, value):
		if "UseCreateBeamElementWithPreStress" in self.__dict__: self.__dict__["UseCreateBeamElementWithPreStress"] = value; return
		self._oleobj_.Invoke(*((9055, LCID, 4, 0) + (value,) + ()))
	def _set_UseForceConnector(self, value):
		if "UseForceConnector" in self.__dict__: self.__dict__["UseForceConnector"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))
	def _set_UseGeneratePatchSetFromNodeElementSet(self, value):
		if "UseGeneratePatchSetFromNodeElementSet" in self.__dict__: self.__dict__["UseGeneratePatchSetFromNodeElementSet"] = value; return
		self._oleobj_.Invoke(*((9056, LCID, 4, 0) + (value,) + ()))
	def _set_UseUnitForce(self, value):
		if "UseUnitForce" in self.__dict__: self.__dict__["UseUnitForce"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))

	UnitOfSource = property(_get_UnitOfSource, _set_UnitOfSource)
	'''
	Unit of Source

	:type: recurdyn.ProcessNet.IUnit
	'''
	UseAllowNullProperty = property(_get_UseAllowNullProperty, _set_UseAllowNullProperty)
	'''
	If True, default materials and properties are generated.

	:type: bool
	'''
	UseCreateBeamElementWithPreStress = property(_get_UseCreateBeamElementWithPreStress, _set_UseCreateBeamElementWithPreStress)
	'''
	If True, create beam element with pre-stress.

	:type: bool
	'''
	UseForceConnector = property(_get_UseForceConnector, _set_UseForceConnector)
	'''
	Use Force Connector of Connecting Parameter

	:type: bool
	'''
	UseGeneratePatchSetFromNodeElementSet = property(_get_UseGeneratePatchSetFromNodeElementSet, _set_UseGeneratePatchSetFromNodeElementSet)
	'''
	If True, Patch set is generated from node or element set.

	:type: bool
	'''
	UseUnitForce = property(_get_UseUnitForce, _set_UseUnitForce)
	'''
	Force unit will be used for converting of Young's modulus of material

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_UnitOfSource": _set_UnitOfSource,
		"_set_UseAllowNullProperty": _set_UseAllowNullProperty,
		"_set_UseCreateBeamElementWithPreStress": _set_UseCreateBeamElementWithPreStress,
		"_set_UseForceConnector": _set_UseForceConnector,
		"_set_UseGeneratePatchSetFromNodeElementSet": _set_UseGeneratePatchSetFromNodeElementSet,
		"_set_UseUnitForce": _set_UseUnitForce,
	}
	_prop_map_get_ = {
		"UnitOfSource": (9052, 2, (9, 0), (), "UnitOfSource", '{09A65909-6FBB-488A-9726-D320F5666395}'),
		"UseAllowNullProperty": (9051, 2, (11, 0), (), "UseAllowNullProperty", None),
		"UseCreateBeamElementWithPreStress": (9055, 2, (11, 0), (), "UseCreateBeamElementWithPreStress", None),
		"UseForceConnector": (9054, 2, (11, 0), (), "UseForceConnector", None),
		"UseGeneratePatchSetFromNodeElementSet": (9056, 2, (11, 0), (), "UseGeneratePatchSetFromNodeElementSet", None),
		"UseUnitForce": (9053, 2, (11, 0), (), "UseUnitForce", None),
	}
	_prop_map_put_ = {
		"UnitOfSource": ((9052, LCID, 4, 0),()),
		"UseAllowNullProperty": ((9051, LCID, 4, 0),()),
		"UseCreateBeamElementWithPreStress": ((9055, LCID, 4, 0),()),
		"UseForceConnector": ((9054, LCID, 4, 0),()),
		"UseGeneratePatchSetFromNodeElementSet": ((9056, LCID, 4, 0),()),
		"UseUnitForce": ((9053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerFFlexToFFlex(DispatchBaseClass):
	'''GManager From FFlex To FFlex Interface'''
	CLSID = IID('{7446389E-9E2B-48BD-ACD2-158D332A3B70}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssistModelingOption(self):
		return self._ApplyTypes_(*(9054, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'))
	def _get_FileName(self):
		return self._ApplyTypes_(*(9051, 2, (8, 0), (), "FileName", None))
	def _get_ReferenceFrame(self):
		return self._ApplyTypes_(*(9052, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_SwapOption(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "SwapOption", '{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}'))

	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceFrame(self, value):
		if "ReferenceFrame" in self.__dict__: self.__dict__["ReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	AssistModelingOption = property(_get_AssistModelingOption, None)
	'''
	Get Assist Modeling Option

	:type: recurdyn.Flexible.IGManagerAssistModelingOption
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	Mesh Data File Name

	:type: str
	'''
	ReferenceFrame = property(_get_ReferenceFrame, _set_ReferenceFrame)
	'''
	Reference Frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	SwapOption = property(_get_SwapOption, None)
	'''
	Get FFlex Swap Option

	:type: recurdyn.Flexible.IGManagerFFlexBodySwapOption
	'''

	_prop_map_set_function_ = {
		"_set_FileName": _set_FileName,
		"_set_ReferenceFrame": _set_ReferenceFrame,
	}
	_prop_map_get_ = {
		"AssistModelingOption": (9054, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'),
		"FileName": (9051, 2, (8, 0), (), "FileName", None),
		"ReferenceFrame": (9052, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"SwapOption": (9053, 2, (9, 0), (), "SwapOption", '{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}'),
	}
	_prop_map_put_ = {
		"FileName": ((9051, LCID, 4, 0),()),
		"ReferenceFrame": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerFFlexToRFlex(DispatchBaseClass):
	'''GManager From FFlex To RFlex Interface'''
	CLSID = IID('{AC2631CE-2984-4F21-B299-4808917E8F75}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssistModelingOption(self):
		return self._ApplyTypes_(*(9056, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'))
	def _get_ConvertType(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "ConvertType", '{DBF72417-17F7-48D5-8A68-F05EF7815686}'))
	def _get_FileName(self):
		return self._ApplyTypes_(*(9052, 2, (8, 0), (), "FileName", None))
	def _get_RFlexGenerator(self):
		return self._ApplyTypes_(*(9054, 2, (9, 0), (), "RFlexGenerator", '{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}'))
	def _get_ReferenceFrame(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_SwapOption(self):
		return self._ApplyTypes_(*(9055, 2, (9, 0), (), "SwapOption", '{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}'))

	def _set_ConvertType(self, value):
		if "ConvertType" in self.__dict__: self.__dict__["ConvertType"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceFrame(self, value):
		if "ReferenceFrame" in self.__dict__: self.__dict__["ReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))

	AssistModelingOption = property(_get_AssistModelingOption, None)
	'''
	Get Assist Modeling Option

	:type: recurdyn.Flexible.IGManagerAssistModelingOption
	'''
	ConvertType = property(_get_ConvertType, _set_ConvertType)
	'''
	Convert Type

	:type: recurdyn.Flexible.ConvertFFlexToRFlexType
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	RFI File Name

	:type: str
	'''
	RFlexGenerator = property(_get_RFlexGenerator, None)
	'''
	Get RFlex Generator

	:type: recurdyn.Flexible.IGManagerRFlexGenerator
	'''
	ReferenceFrame = property(_get_ReferenceFrame, _set_ReferenceFrame)
	'''
	Reference Frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	SwapOption = property(_get_SwapOption, None)
	'''
	Get RFlex Swap Option

	:type: recurdyn.Flexible.IGManagerRFlexBodySwapOption
	'''

	_prop_map_set_function_ = {
		"_set_ConvertType": _set_ConvertType,
		"_set_FileName": _set_FileName,
		"_set_ReferenceFrame": _set_ReferenceFrame,
	}
	_prop_map_get_ = {
		"AssistModelingOption": (9056, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'),
		"ConvertType": (9051, 2, (3, 0), (), "ConvertType", '{DBF72417-17F7-48D5-8A68-F05EF7815686}'),
		"FileName": (9052, 2, (8, 0), (), "FileName", None),
		"RFlexGenerator": (9054, 2, (9, 0), (), "RFlexGenerator", '{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}'),
		"ReferenceFrame": (9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"SwapOption": (9055, 2, (9, 0), (), "SwapOption", '{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}'),
	}
	_prop_map_put_ = {
		"ConvertType": ((9051, LCID, 4, 0),()),
		"FileName": ((9052, LCID, 4, 0),()),
		"ReferenceFrame": ((9053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerFFlexToRigid(DispatchBaseClass):
	'''GManager From FFlex To Rigid Interface'''
	CLSID = IID('{2B8967E0-1892-46E4-A700-9E3384FE1AFF}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssistModelingOption(self):
		return self._ApplyTypes_(*(9054, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'))
	def _get_ConvertType(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "ConvertType", '{CAB41C0B-391A-4591-A8AB-D476023E8C54}'))
	def _get_FileName(self):
		return self._ApplyTypes_(*(9052, 2, (8, 0), (), "FileName", None))
	def _get_ReferenceFrame(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))

	def _set_ConvertType(self, value):
		if "ConvertType" in self.__dict__: self.__dict__["ConvertType"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceFrame(self, value):
		if "ReferenceFrame" in self.__dict__: self.__dict__["ReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))

	AssistModelingOption = property(_get_AssistModelingOption, None)
	'''
	Get Assist Modeling Option

	:type: recurdyn.Flexible.IGManagerAssistModelingOption
	'''
	ConvertType = property(_get_ConvertType, _set_ConvertType)
	'''
	Convert Type

	:type: recurdyn.Flexible.ConvertFFlexToRigidType
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	CAD File Name

	:type: str
	'''
	ReferenceFrame = property(_get_ReferenceFrame, _set_ReferenceFrame)
	'''
	Reference Frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''

	_prop_map_set_function_ = {
		"_set_ConvertType": _set_ConvertType,
		"_set_FileName": _set_FileName,
		"_set_ReferenceFrame": _set_ReferenceFrame,
	}
	_prop_map_get_ = {
		"AssistModelingOption": (9054, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'),
		"ConvertType": (9051, 2, (3, 0), (), "ConvertType", '{CAB41C0B-391A-4591-A8AB-D476023E8C54}'),
		"FileName": (9052, 2, (8, 0), (), "FileName", None),
		"ReferenceFrame": (9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
	}
	_prop_map_put_ = {
		"ConvertType": ((9051, LCID, 4, 0),()),
		"FileName": ((9052, LCID, 4, 0),()),
		"ReferenceFrame": ((9053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerMeshMode(DispatchBaseClass):
	'''GManager Mesh Mode'''
	CLSID = IID('{87FC24B2-6ADC-4804-A601-5B896632C326}')
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

class IGManagerRFlex(DispatchBaseClass):
	'''GManager From RFlex Interface'''
	CLSID = IID('{B9638194-9BB8-44A9-B999-4E26073A84E6}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_FFlex(self):
		return self._ApplyTypes_(*(9052, 2, (9, 0), (), "FFlex", '{4C4268D2-08E0-4D59-AF4F-E84E30762CE3}'))
	def _get_RFlex(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "RFlex", '{B1163AE3-2374-4B52-B76C-FA21254528E3}'))
	def _get_Rigid(self):
		return self._ApplyTypes_(*(9051, 2, (9, 0), (), "Rigid", '{91189C2F-929B-42E4-B61C-9823D5F5B6C6}'))

	FFlex = property(_get_FFlex, None)
	'''
	Get GManager from RFlex to FFlex

	:type: recurdyn.Flexible.IGManagerRFlexToFFlex
	'''
	RFlex = property(_get_RFlex, None)
	'''
	Get GManager from RFlex to RFlex

	:type: recurdyn.Flexible.IGManagerRFlexToRFlex
	'''
	Rigid = property(_get_Rigid, None)
	'''
	Get GManager from RFlex to Rigid

	:type: recurdyn.Flexible.IGManagerRFlexToRigid
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"FFlex": (9052, 2, (9, 0), (), "FFlex", '{4C4268D2-08E0-4D59-AF4F-E84E30762CE3}'),
		"RFlex": (9053, 2, (9, 0), (), "RFlex", '{B1163AE3-2374-4B52-B76C-FA21254528E3}'),
		"Rigid": (9051, 2, (9, 0), (), "Rigid", '{91189C2F-929B-42E4-B61C-9823D5F5B6C6}'),
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

class IGManagerRFlexBodySwapOption(DispatchBaseClass):
	'''GManager RFlexBody Swap Option'''
	CLSID = IID('{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_UseAnimationWithNoDeformation(self):
		return self._ApplyTypes_(*(9053, 2, (11, 0), (), "UseAnimationWithNoDeformation", None))
	def _get_UseUserDefinedRigidBodyFrequency(self):
		return self._ApplyTypes_(*(9051, 2, (11, 0), (), "UseUserDefinedRigidBodyFrequency", None))
	def _get_UserDefinedRigidBodyFrequency(self):
		return self._ApplyTypes_(*(9052, 2, (5, 0), (), "UserDefinedRigidBodyFrequency", None))

	def _set_UseAnimationWithNoDeformation(self, value):
		if "UseAnimationWithNoDeformation" in self.__dict__: self.__dict__["UseAnimationWithNoDeformation"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserDefinedRigidBodyFrequency(self, value):
		if "UseUserDefinedRigidBodyFrequency" in self.__dict__: self.__dict__["UseUserDefinedRigidBodyFrequency"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedRigidBodyFrequency(self, value):
		if "UserDefinedRigidBodyFrequency" in self.__dict__: self.__dict__["UserDefinedRigidBodyFrequency"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	UseAnimationWithNoDeformation = property(_get_UseAnimationWithNoDeformation, _set_UseAnimationWithNoDeformation)
	'''
	Animation with no deformation results

	:type: bool
	'''
	UseUserDefinedRigidBodyFrequency = property(_get_UseUserDefinedRigidBodyFrequency, _set_UseUserDefinedRigidBodyFrequency)
	'''
	Use user defined rigid body frequency

	:type: bool
	'''
	UserDefinedRigidBodyFrequency = property(_get_UserDefinedRigidBodyFrequency, _set_UserDefinedRigidBodyFrequency)
	'''
	User defined rigid body frequency

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_UseAnimationWithNoDeformation": _set_UseAnimationWithNoDeformation,
		"_set_UseUserDefinedRigidBodyFrequency": _set_UseUserDefinedRigidBodyFrequency,
		"_set_UserDefinedRigidBodyFrequency": _set_UserDefinedRigidBodyFrequency,
	}
	_prop_map_get_ = {
		"UseAnimationWithNoDeformation": (9053, 2, (11, 0), (), "UseAnimationWithNoDeformation", None),
		"UseUserDefinedRigidBodyFrequency": (9051, 2, (11, 0), (), "UseUserDefinedRigidBodyFrequency", None),
		"UserDefinedRigidBodyFrequency": (9052, 2, (5, 0), (), "UserDefinedRigidBodyFrequency", None),
	}
	_prop_map_put_ = {
		"UseAnimationWithNoDeformation": ((9053, LCID, 4, 0),()),
		"UseUserDefinedRigidBodyFrequency": ((9051, LCID, 4, 0),()),
		"UserDefinedRigidBodyFrequency": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerRFlexGenerationOption(DispatchBaseClass):
	''' GManager RFlex Generation Option '''
	CLSID = IID('{15EDB8CA-E02D-4905-AA0F-7A11B74C1885}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_InterfaceNodeIDs(self):
		return self._ApplyTypes_(*(9051, 2, (8195, 0), (), "InterfaceNodeIDs", None))
	def _get_InterfaceNodeNumber(self):
		return self._ApplyTypes_(*(9053, 2, (3, 0), (), "InterfaceNodeNumber", None))
	def _get_InterfaceNodeset(self):
		return self._ApplyTypes_(*(9052, 2, (9, 0), (), "InterfaceNodeset", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_LowerFrequency(self):
		return self._ApplyTypes_(*(9057, 2, (5, 0), (), "LowerFrequency", None))
	def _get_NormalModeNumber(self):
		return self._ApplyTypes_(*(9056, 2, (19, 0), (), "NormalModeNumber", None))
	def _get_ShellDrillingParameter(self):
		return self._ApplyTypes_(*(9064, 2, (5, 0), (), "ShellDrillingParameter", None))
	def _get_Solver(self):
		return self._ApplyTypes_(*(9067, 2, (3, 0), (), "Solver", '{751C1136-D0D2-41B4-98DF-2C88CE95D9C4}'))
	def _get_Unit(self):
		return self._ApplyTypes_(*(9059, 2, (9, 0), (), "Unit", '{09A65909-6FBB-488A-9726-D320F5666395}'))
	def _get_UpperFrequency(self):
		return self._ApplyTypes_(*(9058, 2, (5, 0), (), "UpperFrequency", None))
	def _get_UseDeleteDynamisDataBaseFiles(self):
		return self._ApplyTypes_(*(9062, 2, (11, 0), (), "UseDeleteDynamisDataBaseFiles", None))
	def _get_UseRFITranslator(self):
		return self._ApplyTypes_(*(9063, 2, (11, 0), (), "UseRFITranslator", None))
	def _get_UseRemoveMidNodeRelatedInformation(self):
		return self._ApplyTypes_(*(9060, 2, (11, 0), (), "UseRemoveMidNodeRelatedInformation", None))
	def _get_UseRemoveZeroValueForRotModeShape(self):
		return self._ApplyTypes_(*(9061, 2, (11, 0), (), "UseRemoveZeroValueForRotModeShape", None))
	def _get_UseStrainShape(self):
		return self._ApplyTypes_(*(9066, 2, (11, 0), (), "UseStrainShape", None))
	def _get_UseStressShape(self):
		return self._ApplyTypes_(*(9065, 2, (11, 0), (), "UseStressShape", None))
	def _get_UseUserDefinedDOFs(self):
		return self._ApplyTypes_(*(9054, 2, (11, 0), (), "UseUserDefinedDOFs", None))
	def _get_UserDefinedDOFs(self):
		return self._ApplyTypes_(*(9055, 2, (8200, 0), (), "UserDefinedDOFs", None))

	def _set_InterfaceNodeIDs(self, value):
		if "InterfaceNodeIDs" in self.__dict__: self.__dict__["InterfaceNodeIDs"] = value; return
		variantValue = win32com.client.VARIANT(8195, value)
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (variantValue,) + ()))
	def _set_InterfaceNodeset(self, value):
		if "InterfaceNodeset" in self.__dict__: self.__dict__["InterfaceNodeset"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_LowerFrequency(self, value):
		if "LowerFrequency" in self.__dict__: self.__dict__["LowerFrequency"] = value; return
		self._oleobj_.Invoke(*((9057, LCID, 4, 0) + (value,) + ()))
	def _set_NormalModeNumber(self, value):
		if "NormalModeNumber" in self.__dict__: self.__dict__["NormalModeNumber"] = value; return
		self._oleobj_.Invoke(*((9056, LCID, 4, 0) + (value,) + ()))
	def _set_ShellDrillingParameter(self, value):
		if "ShellDrillingParameter" in self.__dict__: self.__dict__["ShellDrillingParameter"] = value; return
		self._oleobj_.Invoke(*((9064, LCID, 4, 0) + (value,) + ()))
	def _set_Solver(self, value):
		if "Solver" in self.__dict__: self.__dict__["Solver"] = value; return
		self._oleobj_.Invoke(*((9067, LCID, 4, 0) + (value,) + ()))
	def _set_Unit(self, value):
		if "Unit" in self.__dict__: self.__dict__["Unit"] = value; return
		self._oleobj_.Invoke(*((9059, LCID, 4, 0) + (value,) + ()))
	def _set_UpperFrequency(self, value):
		if "UpperFrequency" in self.__dict__: self.__dict__["UpperFrequency"] = value; return
		self._oleobj_.Invoke(*((9058, LCID, 4, 0) + (value,) + ()))
	def _set_UseDeleteDynamisDataBaseFiles(self, value):
		if "UseDeleteDynamisDataBaseFiles" in self.__dict__: self.__dict__["UseDeleteDynamisDataBaseFiles"] = value; return
		self._oleobj_.Invoke(*((9062, LCID, 4, 0) + (value,) + ()))
	def _set_UseRFITranslator(self, value):
		if "UseRFITranslator" in self.__dict__: self.__dict__["UseRFITranslator"] = value; return
		self._oleobj_.Invoke(*((9063, LCID, 4, 0) + (value,) + ()))
	def _set_UseRemoveMidNodeRelatedInformation(self, value):
		if "UseRemoveMidNodeRelatedInformation" in self.__dict__: self.__dict__["UseRemoveMidNodeRelatedInformation"] = value; return
		self._oleobj_.Invoke(*((9060, LCID, 4, 0) + (value,) + ()))
	def _set_UseRemoveZeroValueForRotModeShape(self, value):
		if "UseRemoveZeroValueForRotModeShape" in self.__dict__: self.__dict__["UseRemoveZeroValueForRotModeShape"] = value; return
		self._oleobj_.Invoke(*((9061, LCID, 4, 0) + (value,) + ()))
	def _set_UseStrainShape(self, value):
		if "UseStrainShape" in self.__dict__: self.__dict__["UseStrainShape"] = value; return
		self._oleobj_.Invoke(*((9066, LCID, 4, 0) + (value,) + ()))
	def _set_UseStressShape(self, value):
		if "UseStressShape" in self.__dict__: self.__dict__["UseStressShape"] = value; return
		self._oleobj_.Invoke(*((9065, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserDefinedDOFs(self, value):
		if "UseUserDefinedDOFs" in self.__dict__: self.__dict__["UseUserDefinedDOFs"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedDOFs(self, value):
		if "UserDefinedDOFs" in self.__dict__: self.__dict__["UserDefinedDOFs"] = value; return
		variantValue = win32com.client.VARIANT(8200, value)
		self._oleobj_.Invoke(*((9055, LCID, 4, 0) + (variantValue,) + ()))

	InterfaceNodeIDs = property(_get_InterfaceNodeIDs, _set_InterfaceNodeIDs)
	'''
	Interface node IDs

	:type: list[int]
	'''
	InterfaceNodeNumber = property(_get_InterfaceNodeNumber, None)
	'''
	Interface node Number

	:type: int
	'''
	InterfaceNodeset = property(_get_InterfaceNodeset, _set_InterfaceNodeset)
	'''
	Interface node nodeset

	:type: recurdyn.ProcessNet.IGeneric
	'''
	LowerFrequency = property(_get_LowerFrequency, _set_LowerFrequency)
	'''
	Lower frequency

	:type: float
	'''
	NormalModeNumber = property(_get_NormalModeNumber, _set_NormalModeNumber)
	'''
	Number of fixed normal mode

	:type: int
	'''
	ShellDrillingParameter = property(_get_ShellDrillingParameter, _set_ShellDrillingParameter)
	'''
	Shell Drilling Parameter

	:type: float
	'''
	Solver = property(_get_Solver, _set_Solver)
	'''
	Solver is obsolete function

	:type: recurdyn.FlexInterface.RFISolverType
	'''
	Unit = property(_get_Unit, _set_Unit)
	'''
	Units

	:type: recurdyn.ProcessNet.IUnit
	'''
	UpperFrequency = property(_get_UpperFrequency, _set_UpperFrequency)
	'''
	Upper frequency

	:type: float
	'''
	UseDeleteDynamisDataBaseFiles = property(_get_UseDeleteDynamisDataBaseFiles, _set_UseDeleteDynamisDataBaseFiles)
	'''
	Flag to delete dynamis dataBase filess

	:type: bool
	'''
	UseRFITranslator = property(_get_UseRFITranslator, _set_UseRFITranslator)
	'''
	Flag to translate RFI file to text file

	:type: bool
	'''
	UseRemoveMidNodeRelatedInformation = property(_get_UseRemoveMidNodeRelatedInformation, _set_UseRemoveMidNodeRelatedInformation)
	'''
	Flag to remove mid node related information

	:type: bool
	'''
	UseRemoveZeroValueForRotModeShape = property(_get_UseRemoveZeroValueForRotModeShape, _set_UseRemoveZeroValueForRotModeShape)
	'''
	Flag to remove zero value for rot mode shape

	:type: bool
	'''
	UseStrainShape = property(_get_UseStrainShape, _set_UseStrainShape)
	'''
	Strain Shape Flag

	:type: bool
	'''
	UseStressShape = property(_get_UseStressShape, _set_UseStressShape)
	'''
	Stress Shape Flag

	:type: bool
	'''
	UseUserDefinedDOFs = property(_get_UseUserDefinedDOFs, _set_UseUserDefinedDOFs)
	'''
	User defined DOFs for computing constriant modes Flag

	:type: bool
	'''
	UserDefinedDOFs = property(_get_UserDefinedDOFs, _set_UserDefinedDOFs)
	'''
	User defined DOFs

	:type: list[str]
	'''

	_prop_map_set_function_ = {
		"_set_InterfaceNodeIDs": _set_InterfaceNodeIDs,
		"_set_InterfaceNodeset": _set_InterfaceNodeset,
		"_set_LowerFrequency": _set_LowerFrequency,
		"_set_NormalModeNumber": _set_NormalModeNumber,
		"_set_ShellDrillingParameter": _set_ShellDrillingParameter,
		"_set_Solver": _set_Solver,
		"_set_Unit": _set_Unit,
		"_set_UpperFrequency": _set_UpperFrequency,
		"_set_UseDeleteDynamisDataBaseFiles": _set_UseDeleteDynamisDataBaseFiles,
		"_set_UseRFITranslator": _set_UseRFITranslator,
		"_set_UseRemoveMidNodeRelatedInformation": _set_UseRemoveMidNodeRelatedInformation,
		"_set_UseRemoveZeroValueForRotModeShape": _set_UseRemoveZeroValueForRotModeShape,
		"_set_UseStrainShape": _set_UseStrainShape,
		"_set_UseStressShape": _set_UseStressShape,
		"_set_UseUserDefinedDOFs": _set_UseUserDefinedDOFs,
		"_set_UserDefinedDOFs": _set_UserDefinedDOFs,
	}
	_prop_map_get_ = {
		"InterfaceNodeIDs": (9051, 2, (8195, 0), (), "InterfaceNodeIDs", None),
		"InterfaceNodeNumber": (9053, 2, (3, 0), (), "InterfaceNodeNumber", None),
		"InterfaceNodeset": (9052, 2, (9, 0), (), "InterfaceNodeset", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"LowerFrequency": (9057, 2, (5, 0), (), "LowerFrequency", None),
		"NormalModeNumber": (9056, 2, (19, 0), (), "NormalModeNumber", None),
		"ShellDrillingParameter": (9064, 2, (5, 0), (), "ShellDrillingParameter", None),
		"Solver": (9067, 2, (3, 0), (), "Solver", '{751C1136-D0D2-41B4-98DF-2C88CE95D9C4}'),
		"Unit": (9059, 2, (9, 0), (), "Unit", '{09A65909-6FBB-488A-9726-D320F5666395}'),
		"UpperFrequency": (9058, 2, (5, 0), (), "UpperFrequency", None),
		"UseDeleteDynamisDataBaseFiles": (9062, 2, (11, 0), (), "UseDeleteDynamisDataBaseFiles", None),
		"UseRFITranslator": (9063, 2, (11, 0), (), "UseRFITranslator", None),
		"UseRemoveMidNodeRelatedInformation": (9060, 2, (11, 0), (), "UseRemoveMidNodeRelatedInformation", None),
		"UseRemoveZeroValueForRotModeShape": (9061, 2, (11, 0), (), "UseRemoveZeroValueForRotModeShape", None),
		"UseStrainShape": (9066, 2, (11, 0), (), "UseStrainShape", None),
		"UseStressShape": (9065, 2, (11, 0), (), "UseStressShape", None),
		"UseUserDefinedDOFs": (9054, 2, (11, 0), (), "UseUserDefinedDOFs", None),
		"UserDefinedDOFs": (9055, 2, (8200, 0), (), "UserDefinedDOFs", None),
	}
	_prop_map_put_ = {
		"InterfaceNodeIDs": ((9051, LCID, 4, 0),()),
		"InterfaceNodeset": ((9052, LCID, 4, 0),()),
		"LowerFrequency": ((9057, LCID, 4, 0),()),
		"NormalModeNumber": ((9056, LCID, 4, 0),()),
		"ShellDrillingParameter": ((9064, LCID, 4, 0),()),
		"Solver": ((9067, LCID, 4, 0),()),
		"Unit": ((9059, LCID, 4, 0),()),
		"UpperFrequency": ((9058, LCID, 4, 0),()),
		"UseDeleteDynamisDataBaseFiles": ((9062, LCID, 4, 0),()),
		"UseRFITranslator": ((9063, LCID, 4, 0),()),
		"UseRemoveMidNodeRelatedInformation": ((9060, LCID, 4, 0),()),
		"UseRemoveZeroValueForRotModeShape": ((9061, LCID, 4, 0),()),
		"UseStrainShape": ((9066, LCID, 4, 0),()),
		"UseStressShape": ((9065, LCID, 4, 0),()),
		"UseUserDefinedDOFs": ((9054, LCID, 4, 0),()),
		"UserDefinedDOFs": ((9055, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerRFlexGenerator(DispatchBaseClass):
	'''GManager RFlex Generator Interface'''
	CLSID = IID('{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Execute(self):
		'''
		Execute RFlex Generator
		'''
		return self._oleobj_.InvokeTypes(9052, LCID, 1, (24, 0), (),)


	def _get_Option(self):
		return self._ApplyTypes_(*(9051, 2, (9, 0), (), "Option", '{15EDB8CA-E02D-4905-AA0F-7A11B74C1885}'))

	Option = property(_get_Option, None)
	'''
	Get GManager RFlex Generator Option

	:type: recurdyn.Flexible.IGManagerRFlexGenerationOption
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Option": (9051, 2, (9, 0), (), "Option", '{15EDB8CA-E02D-4905-AA0F-7A11B74C1885}'),
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

class IGManagerRFlexToFFlex(DispatchBaseClass):
	'''GManager From RFlex To FFlex Interface'''
	CLSID = IID('{4C4268D2-08E0-4D59-AF4F-E84E30762CE3}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssistModelingOption(self):
		return self._ApplyTypes_(*(9055, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'))
	def _get_ConvertType(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "ConvertType", '{3A4759E5-0425-4ADD-A97D-73A552D9E92B}'))
	def _get_FileName(self):
		return self._ApplyTypes_(*(9052, 2, (8, 0), (), "FileName", None))
	def _get_ReferenceFrame(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_SwapOption(self):
		return self._ApplyTypes_(*(9054, 2, (9, 0), (), "SwapOption", '{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}'))

	def _set_ConvertType(self, value):
		if "ConvertType" in self.__dict__: self.__dict__["ConvertType"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceFrame(self, value):
		if "ReferenceFrame" in self.__dict__: self.__dict__["ReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))

	AssistModelingOption = property(_get_AssistModelingOption, None)
	'''
	Get Assist Modeling Option

	:type: recurdyn.Flexible.IGManagerAssistModelingOption
	'''
	ConvertType = property(_get_ConvertType, _set_ConvertType)
	'''
	Convert Type

	:type: recurdyn.Flexible.ConvertRFlexToFFlexType
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	Mesh Data File Name

	:type: str
	'''
	ReferenceFrame = property(_get_ReferenceFrame, _set_ReferenceFrame)
	'''
	Reference Frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	SwapOption = property(_get_SwapOption, None)
	'''
	Get FFlex Swap Option

	:type: recurdyn.Flexible.IGManagerFFlexBodySwapOption
	'''

	_prop_map_set_function_ = {
		"_set_ConvertType": _set_ConvertType,
		"_set_FileName": _set_FileName,
		"_set_ReferenceFrame": _set_ReferenceFrame,
	}
	_prop_map_get_ = {
		"AssistModelingOption": (9055, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'),
		"ConvertType": (9051, 2, (3, 0), (), "ConvertType", '{3A4759E5-0425-4ADD-A97D-73A552D9E92B}'),
		"FileName": (9052, 2, (8, 0), (), "FileName", None),
		"ReferenceFrame": (9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"SwapOption": (9054, 2, (9, 0), (), "SwapOption", '{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}'),
	}
	_prop_map_put_ = {
		"ConvertType": ((9051, LCID, 4, 0),()),
		"FileName": ((9052, LCID, 4, 0),()),
		"ReferenceFrame": ((9053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerRFlexToRFlex(DispatchBaseClass):
	'''GManager From RFlex To RFlex Interface'''
	CLSID = IID('{B1163AE3-2374-4B52-B76C-FA21254528E3}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssistModelingOption(self):
		return self._ApplyTypes_(*(9056, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'))
	def _get_ConvertType(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "ConvertType", '{E4BAB8EC-EBC5-4D4C-994E-33DA940FBA24}'))
	def _get_FileName(self):
		return self._ApplyTypes_(*(9052, 2, (8, 0), (), "FileName", None))
	def _get_RFlexGenerator(self):
		return self._ApplyTypes_(*(9054, 2, (9, 0), (), "RFlexGenerator", '{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}'))
	def _get_ReferenceFrame(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_SwapOption(self):
		return self._ApplyTypes_(*(9055, 2, (9, 0), (), "SwapOption", '{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}'))

	def _set_ConvertType(self, value):
		if "ConvertType" in self.__dict__: self.__dict__["ConvertType"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceFrame(self, value):
		if "ReferenceFrame" in self.__dict__: self.__dict__["ReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))

	AssistModelingOption = property(_get_AssistModelingOption, None)
	'''
	Get Assist Modeling Option

	:type: recurdyn.Flexible.IGManagerAssistModelingOption
	'''
	ConvertType = property(_get_ConvertType, _set_ConvertType)
	'''
	Convert Type

	:type: recurdyn.Flexible.ConvertRFlexToRFlexType
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	RFI File Name

	:type: str
	'''
	RFlexGenerator = property(_get_RFlexGenerator, None)
	'''
	Get RFlex Generator

	:type: recurdyn.Flexible.IGManagerRFlexGenerator
	'''
	ReferenceFrame = property(_get_ReferenceFrame, _set_ReferenceFrame)
	'''
	Reference Frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	SwapOption = property(_get_SwapOption, None)
	'''
	Get FFlex Swap Option

	:type: recurdyn.Flexible.IGManagerRFlexBodySwapOption
	'''

	_prop_map_set_function_ = {
		"_set_ConvertType": _set_ConvertType,
		"_set_FileName": _set_FileName,
		"_set_ReferenceFrame": _set_ReferenceFrame,
	}
	_prop_map_get_ = {
		"AssistModelingOption": (9056, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'),
		"ConvertType": (9051, 2, (3, 0), (), "ConvertType", '{E4BAB8EC-EBC5-4D4C-994E-33DA940FBA24}'),
		"FileName": (9052, 2, (8, 0), (), "FileName", None),
		"RFlexGenerator": (9054, 2, (9, 0), (), "RFlexGenerator", '{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}'),
		"ReferenceFrame": (9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"SwapOption": (9055, 2, (9, 0), (), "SwapOption", '{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}'),
	}
	_prop_map_put_ = {
		"ConvertType": ((9051, LCID, 4, 0),()),
		"FileName": ((9052, LCID, 4, 0),()),
		"ReferenceFrame": ((9053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerRFlexToRigid(DispatchBaseClass):
	'''GManager From RFlex To Rigid Interface'''
	CLSID = IID('{91189C2F-929B-42E4-B61C-9823D5F5B6C6}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssistModelingOption(self):
		return self._ApplyTypes_(*(9054, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'))
	def _get_ConvertType(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "ConvertType", '{5F3848CC-A1D6-49FE-B0CE-828636B19E9B}'))
	def _get_FileName(self):
		return self._ApplyTypes_(*(9052, 2, (8, 0), (), "FileName", None))
	def _get_ReferenceFrame(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))

	def _set_ConvertType(self, value):
		if "ConvertType" in self.__dict__: self.__dict__["ConvertType"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceFrame(self, value):
		if "ReferenceFrame" in self.__dict__: self.__dict__["ReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))

	AssistModelingOption = property(_get_AssistModelingOption, None)
	'''
	Get Assist Modeling Option

	:type: recurdyn.Flexible.IGManagerAssistModelingOption
	'''
	ConvertType = property(_get_ConvertType, _set_ConvertType)
	'''
	Convert Type

	:type: recurdyn.Flexible.ConvertRFlexToRigidType
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	CAD File Name

	:type: str
	'''
	ReferenceFrame = property(_get_ReferenceFrame, _set_ReferenceFrame)
	'''
	Reference Frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''

	_prop_map_set_function_ = {
		"_set_ConvertType": _set_ConvertType,
		"_set_FileName": _set_FileName,
		"_set_ReferenceFrame": _set_ReferenceFrame,
	}
	_prop_map_get_ = {
		"AssistModelingOption": (9054, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'),
		"ConvertType": (9051, 2, (3, 0), (), "ConvertType", '{5F3848CC-A1D6-49FE-B0CE-828636B19E9B}'),
		"FileName": (9052, 2, (8, 0), (), "FileName", None),
		"ReferenceFrame": (9053, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
	}
	_prop_map_put_ = {
		"ConvertType": ((9051, LCID, 4, 0),()),
		"FileName": ((9052, LCID, 4, 0),()),
		"ReferenceFrame": ((9053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerRigid(DispatchBaseClass):
	'''GManager From Rigid Interface'''
	CLSID = IID('{4FFEA591-BF79-4FF5-95A9-409860AC2D1E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_CADFileName(self):
		return self._ApplyTypes_(*(9054, 2, (8, 0), (), "CADFileName", None))
	def _get_FFlex(self):
		return self._ApplyTypes_(*(9051, 2, (9, 0), (), "FFlex", '{FC9A332A-067D-462E-8B85-57A5A41ECDF8}'))
	def _get_RFlex(self):
		return self._ApplyTypes_(*(9052, 2, (9, 0), (), "RFlex", '{80FB287D-32EF-4386-989A-4FD1DAC82798}'))
	def _get_UseCreateCADFile(self):
		return self._ApplyTypes_(*(9053, 2, (11, 0), (), "UseCreateCADFile", None))

	def _set_CADFileName(self, value):
		if "CADFileName" in self.__dict__: self.__dict__["CADFileName"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))
	def _set_UseCreateCADFile(self, value):
		if "UseCreateCADFile" in self.__dict__: self.__dict__["UseCreateCADFile"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))

	CADFileName = property(_get_CADFileName, _set_CADFileName)
	'''
	CAD File Name

	:type: str
	'''
	FFlex = property(_get_FFlex, None)
	'''
	Get GManager from Rigid to FFlex

	:type: recurdyn.Flexible.IGManagerRigidToFFlex
	'''
	RFlex = property(_get_RFlex, None)
	'''
	Get GManager from Rigid to RFlex

	:type: recurdyn.Flexible.IGManagerRigidToRFlex
	'''
	UseCreateCADFile = property(_get_UseCreateCADFile, _set_UseCreateCADFile)
	'''
	Create CAD File Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_CADFileName": _set_CADFileName,
		"_set_UseCreateCADFile": _set_UseCreateCADFile,
	}
	_prop_map_get_ = {
		"CADFileName": (9054, 2, (8, 0), (), "CADFileName", None),
		"FFlex": (9051, 2, (9, 0), (), "FFlex", '{FC9A332A-067D-462E-8B85-57A5A41ECDF8}'),
		"RFlex": (9052, 2, (9, 0), (), "RFlex", '{80FB287D-32EF-4386-989A-4FD1DAC82798}'),
		"UseCreateCADFile": (9053, 2, (11, 0), (), "UseCreateCADFile", None),
	}
	_prop_map_put_ = {
		"CADFileName": ((9054, LCID, 4, 0),()),
		"UseCreateCADFile": ((9053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerRigidToFFlex(DispatchBaseClass):
	'''GManager From Rigid To FFlex Interface'''
	CLSID = IID('{FC9A332A-067D-462E-8B85-57A5A41ECDF8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssistModelingOption(self):
		return self._ApplyTypes_(*(9056, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'))
	def _get_ConvertType(self):
		return self._ApplyTypes_(*(9051, 2, (3, 0), (), "ConvertType", '{0ACC9971-A2C9-49A0-94C7-41C4DA79A699}'))
	def _get_FileName(self):
		return self._ApplyTypes_(*(9053, 2, (8, 0), (), "FileName", None))
	def _get_MeshMode(self):
		return self._ApplyTypes_(*(9057, 2, (9, 0), (), "MeshMode", '{87FC24B2-6ADC-4804-A601-5B896632C326}'))
	def _get_ReferenceFrame(self):
		return self._ApplyTypes_(*(9054, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_SourceGeometry(self):
		return self._ApplyTypes_(*(9052, 2, (9, 0), (), "SourceGeometry", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'))
	def _get_SwapOption(self):
		return self._ApplyTypes_(*(9055, 2, (9, 0), (), "SwapOption", '{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}'))

	def _set_ConvertType(self, value):
		if "ConvertType" in self.__dict__: self.__dict__["ConvertType"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((9053, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceFrame(self, value):
		if "ReferenceFrame" in self.__dict__: self.__dict__["ReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((9054, LCID, 4, 0) + (value,) + ()))
	def _set_SourceGeometry(self, value):
		if "SourceGeometry" in self.__dict__: self.__dict__["SourceGeometry"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	AssistModelingOption = property(_get_AssistModelingOption, None)
	'''
	Get Assist Modeling Option

	:type: recurdyn.Flexible.IGManagerAssistModelingOption
	'''
	ConvertType = property(_get_ConvertType, _set_ConvertType)
	'''
	Convert Type

	:type: recurdyn.Flexible.ConvertRigidToFFlexType
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	Mesh Data File Name

	:type: str
	'''
	MeshMode = property(_get_MeshMode, None)
	'''
	Get Mesh Mode

	:type: recurdyn.Flexible.IGManagerMeshMode
	'''
	ReferenceFrame = property(_get_ReferenceFrame, _set_ReferenceFrame)
	'''
	Reference Frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	SourceGeometry = property(_get_SourceGeometry, _set_SourceGeometry)
	'''
	Source Geometry

	:type: recurdyn.ProcessNet.IGeometry
	'''
	SwapOption = property(_get_SwapOption, None)
	'''
	Get FFlex Swap Option

	:type: recurdyn.Flexible.IGManagerFFlexBodySwapOption
	'''

	_prop_map_set_function_ = {
		"_set_ConvertType": _set_ConvertType,
		"_set_FileName": _set_FileName,
		"_set_ReferenceFrame": _set_ReferenceFrame,
		"_set_SourceGeometry": _set_SourceGeometry,
	}
	_prop_map_get_ = {
		"AssistModelingOption": (9056, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'),
		"ConvertType": (9051, 2, (3, 0), (), "ConvertType", '{0ACC9971-A2C9-49A0-94C7-41C4DA79A699}'),
		"FileName": (9053, 2, (8, 0), (), "FileName", None),
		"MeshMode": (9057, 2, (9, 0), (), "MeshMode", '{87FC24B2-6ADC-4804-A601-5B896632C326}'),
		"ReferenceFrame": (9054, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"SourceGeometry": (9052, 2, (9, 0), (), "SourceGeometry", '{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}'),
		"SwapOption": (9055, 2, (9, 0), (), "SwapOption", '{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}'),
	}
	_prop_map_put_ = {
		"ConvertType": ((9051, LCID, 4, 0),()),
		"FileName": ((9053, LCID, 4, 0),()),
		"ReferenceFrame": ((9054, LCID, 4, 0),()),
		"SourceGeometry": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGManagerRigidToRFlex(DispatchBaseClass):
	'''GManager From Rigid To RFlex Interface'''
	CLSID = IID('{80FB287D-32EF-4386-989A-4FD1DAC82798}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AssistModelingOption(self):
		return self._ApplyTypes_(*(9054, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'))
	def _get_FileName(self):
		return self._ApplyTypes_(*(9051, 2, (8, 0), (), "FileName", None))
	def _get_ReferenceFrame(self):
		return self._ApplyTypes_(*(9052, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_SwapOption(self):
		return self._ApplyTypes_(*(9053, 2, (9, 0), (), "SwapOption", '{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}'))

	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((9051, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceFrame(self, value):
		if "ReferenceFrame" in self.__dict__: self.__dict__["ReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((9052, LCID, 4, 0) + (value,) + ()))

	AssistModelingOption = property(_get_AssistModelingOption, None)
	'''
	Get Assist Modeling Option

	:type: recurdyn.Flexible.IGManagerAssistModelingOption
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	RFI FIle Name

	:type: str
	'''
	ReferenceFrame = property(_get_ReferenceFrame, _set_ReferenceFrame)
	'''
	Reference Frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	SwapOption = property(_get_SwapOption, None)
	'''
	Get RFlex Swap Option

	:type: recurdyn.Flexible.IGManagerRFlexBodySwapOption
	'''

	_prop_map_set_function_ = {
		"_set_FileName": _set_FileName,
		"_set_ReferenceFrame": _set_ReferenceFrame,
	}
	_prop_map_get_ = {
		"AssistModelingOption": (9054, 2, (9, 0), (), "AssistModelingOption", '{16FD62CA-B60D-4326-9349-593F526D8399}'),
		"FileName": (9051, 2, (8, 0), (), "FileName", None),
		"ReferenceFrame": (9052, 2, (9, 0), (), "ReferenceFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"SwapOption": (9053, 2, (9, 0), (), "SwapOption", '{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}'),
	}
	_prop_map_put_ = {
		"FileName": ((9051, LCID, 4, 0),()),
		"ReferenceFrame": ((9052, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

IContour_vtables_dispatch_ = 1
IContour_vtables_ = [
	(( 'EnableView' , 'pVal' , ), 9001, (9001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'EnableView' , 'pVal' , ), 9001, (9001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TypeOption' , 'ppVal' , ), 9002, (9002, (), [ (16393, 10, None, "IID('{49E653C4-054B-4496-B4FA-9EF8947B2C94}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MinMaxOption' , 'ppVal' , ), 9003, (9003, (), [ (16393, 10, None, "IID('{B88B9BB0-1991-486D-8248-3FD7CEE798DB}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'BandOption' , 'ppVal' , ), 9004, (9004, (), [ (16393, 10, None, "IID('{6A77B683-DB6D-47CC-A9A4-8A1236F68D9E}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'StyleOption' , 'ppVal' , ), 9005, (9005, (), [ (16393, 10, None, "IID('{FC113BCB-DE52-4C7B-BE93-029A709898B0}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceNodeCollection' , 'ppVal' , ), 9006, (9006, (), [ (16393, 10, None, "IID('{CC340394-39A2-489C-B59E-F62063FBE6D2}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'DataTraceCollection' , 'ppVal' , ), 9007, (9007, (), [ (16393, 10, None, "IID('{9F8AB0C2-9B88-4A3D-A279-5E653738A009}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PartSelectionCollection' , 'ppVal' , ), 9008, (9008, (), [ (16393, 10, None, "IID('{4A8EAB35-DBC8-4E2E-8E70-2D5C34C7F6BA}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DataExport' , 'ppVal' , ), 9009, (9009, (), [ (16393, 10, None, "IID('{139D3F54-8397-417D-8AA9-B8E92666E31A}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'AddDataTrace' , 'pVal' , 'Val' , ), 9010, (9010, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DeleteDataTrace' , 'pVal' , ), 9011, (9011, (), [ (9, 1, None, "IID('{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DeleteDataTracebyIndex' , 'Val' , ), 9012, (9012, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AddPartSelction' , 'pBody' , 'pSet' , ), 9013, (9013, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DeletePartSelction' , 'pVal' , ), 9014, (9014, (), [ (9, 1, None, "IID('{14C89575-CA21-4656-988A-87151B83C368}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'DeletePartSelctionbyIndex' , 'Val' , ), 9015, (9015, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UpdateLegend' , ), 9016, (9016, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'OpenContourDialog' , ), 9017, (9017, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CloseContourDialog' , ), 9018, (9018, (), [ ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
]

IContourBandOption_vtables_dispatch_ = 1
IContourBandOption_vtables_ = [
	(( 'LegendType' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{523C6F14-0660-455F-B6A6-136B5BFC19C4}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LegendType' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{523C6F14-0660-455F-B6A6-136B5BFC19C4}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LegendLocation' , 'pVal' , ), 9052, (9052, (), [ (3, 1, None, "IID('{40B0D145-E318-48E0-8114-B3400BA8B271}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LegendLocation' , 'pVal' , ), 9052, (9052, (), [ (16387, 10, None, "IID('{40B0D145-E318-48E0-8114-B3400BA8B271}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ShowTextLegend' , 'pVal' , ), 9053, (9053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ShowTextLegend' , 'pVal' , ), 9053, (9053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'BandLevel' , 'pVal' , ), 9054, (9054, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'BandLevel' , 'pVal' , ), 9054, (9054, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IContourDataExport_vtables_dispatch_ = 1
IContourDataExport_vtables_ = [
	(( 'Type' , ), 9051, (9051, (), [ (3, 1, None, "IID('{D0E1232B-3D00-47CE-8DA8-F8319F586A3C}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Body' , ), 9052, (9052, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SelectNodes' , ), 9053, (9053, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SelectNodesWithRange' , 'start' , 'end' , ), 9054, (9054, (), [ (3, 1, None, None) , 
			 (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SelectFrames' , ), 9055, (9055, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SelectFramesWithRange' , 'start' , 'end' , ), 9056, (9056, (), [ (19, 1, None, None) , 
			 (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'Val' , ), 9057, (9057, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseScientificNotation' , 'pVal' , ), 9058, (9058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UseScientificNotation' , 'pVal' , ), 9058, (9058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SignificantDigits' , 'pVal' , ), 9059, (9059, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SignificantDigits' , 'pVal' , ), 9059, (9059, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SelectType' , ), 9060, (9060, (), [ (3, 1, None, "IID('{853012C4-A1D0-4BB7-B1B2-ABCB2E20C621}')") , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IContourDataTrace_vtables_dispatch_ = 1
IContourDataTrace_vtables_ = [
	(( 'Select' , 'pVal' , ), 9051, (9051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Select' , 'pVal' , ), 9051, (9051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'NodeID' , 'pVal' , ), 9052, (9052, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NodeID' , 'pVal' , ), 9052, (9052, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Body' , 'ppVal' , ), 9053, (9053, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Body' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IContourDataTraceCollection_vtables_dispatch_ = 1
IContourDataTraceCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IContourMinMaxOption_vtables_dispatch_ = 1
IContourMinMaxOption_vtables_ = [
	(( 'Type' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{7AD6FCD4-4167-4AA9-8A01-B8E3B31318B5}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{7AD6FCD4-4167-4AA9-8A01-B8E3B31318B5}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Calculation' , ), 9052, (9052, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Min' , 'pVal' , ), 9053, (9053, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Max' , 'pVal' , ), 9054, (9054, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMin' , 'pVal' , ), 9055, (9055, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMin' , 'pVal' , ), 9055, (9055, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMax' , 'pVal' , ), 9056, (9056, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMax' , 'pVal' , ), 9056, (9056, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ShowMinMax' , 'pVal' , ), 9057, (9057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ShowMinMax' , 'pVal' , ), 9057, (9057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMaxColor' , 'pVal' , ), 9058, (9058, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMaxColor' , 'pVal' , ), 9058, (9058, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'EnableLogScale' , 'pVal' , ), 9059, (9059, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'EnableLogScale' , 'pVal' , ), 9059, (9059, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMinColor' , 'pVal' , ), 9060, (9060, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMinColor' , 'pVal' , ), 9060, (9060, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ShowMin' , 'pVal' , ), 9061, (9061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ShowMin' , 'pVal' , ), 9061, (9061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ShowMax' , 'pVal' , ), 9062, (9062, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ShowMax' , 'pVal' , ), 9062, (9062, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IContourPartSelection_vtables_dispatch_ = 1
IContourPartSelection_vtables_ = [
	(( 'Select' , 'pVal' , ), 9051, (9051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Select' , 'pVal' , ), 9051, (9051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ElementSet' , 'ppVal' , ), 9052, (9052, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ElementSet' , 'ppVal' , ), 9052, (9052, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Body' , 'ppVal' , ), 9053, (9053, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Body' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IContourPartSelectionCollection_vtables_dispatch_ = 1
IContourPartSelectionCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{14C89575-CA21-4656-988A-87151B83C368}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IContourReferenceNode_vtables_dispatch_ = 1
IContourReferenceNode_vtables_ = [
	(( 'Select' , 'pVal' , ), 9051, (9051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Select' , 'pVal' , ), 9051, (9051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'NodeID' , 'pVal' , ), 9052, (9052, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'NodeID' , 'pVal' , ), 9052, (9052, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Body' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseOrientationReferenceMarker' , 'pVal' , ), 9054, (9054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseOrientationReferenceMarker' , 'pVal' , ), 9054, (9054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'OrientationReferenceMarker' , 'ppVal' , ), 9055, (9055, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'OrientationReferenceMarker' , 'ppVal' , ), 9055, (9055, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceType' , 'enumContourRefType' , ), 9056, (9056, (), [ (3, 1, None, "IID('{D18FC6B4-5F7E-4DBD-BD41-407ECD00EFCE}')") , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceType' , 'enumContourRefType' , ), 9056, (9056, (), [ (16387, 10, None, "IID('{D18FC6B4-5F7E-4DBD-BD41-407ECD00EFCE}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Marker' , 'varMarker' , ), 9057, (9057, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Marker' , 'varMarker' , ), 9057, (9057, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IContourReferenceNodeCollection_vtables_dispatch_ = 1
IContourReferenceNodeCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{FB58C4A7-6D67-465F-A7D3-ADB1B7E53425}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IContourStyleOption_vtables_dispatch_ = 1
IContourStyleOption_vtables_ = [
	(( 'ColorType' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{2E75ED6F-ECC0-4EDD-90F6-E5A3EDB5B6F6}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ColorType' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{2E75ED6F-ECC0-4EDD-90F6-E5A3EDB5B6F6}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'pVal' , ), 9052, (9052, (), [ (3, 1, None, "IID('{3FA68C9E-D1C2-49D0-B5F1-6603FFCFAB56}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'pVal' , ), 9052, (9052, (), [ (16387, 10, None, "IID('{3FA68C9E-D1C2-49D0-B5F1-6603FFCFAB56}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SpectrumMinColor' , 'pVal' , ), 9053, (9053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SpectrumMinColor' , 'pVal' , ), 9053, (9053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SpectrumMaxColor' , 'pVal' , ), 9054, (9054, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SpectrumMaxColor' , 'pVal' , ), 9054, (9054, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GrayScaleColor' , 'pVal' , ), 9055, (9055, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GrayScaleColor' , 'pVal' , ), 9055, (9055, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TextColor' , 'pVal' , ), 9056, (9056, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TextColor' , 'pVal' , ), 9056, (9056, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ShowMeshLines' , 'pVal' , ), 9057, (9057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ShowMeshLines' , 'pVal' , ), 9057, (9057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'MeshLinesColor' , 'pVal' , ), 9058, (9058, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'MeshLinesColor' , 'pVal' , ), 9058, (9058, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ExceedMaxColor' , 'pVal' , ), 9059, (9059, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ExceedMaxColor' , 'pVal' , ), 9059, (9059, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'LessThanMinColor' , 'pVal' , ), 9060, (9060, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'LessThanMinColor' , 'pVal' , ), 9060, (9060, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IContourTypeOption_vtables_dispatch_ = 1
IContourTypeOption_vtables_ = [
	(( 'Type' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{5F0554C6-5E01-4507-BC62-CABBE3020C2C}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{5F0554C6-5E01-4507-BC62-CABBE3020C2C}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Component' , 'pVal' , ), 9052, (9052, (), [ (3, 1, None, "IID('{72EFA71D-BCE9-4369-9F66-CEB35906BB91}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Component' , 'pVal' , ), 9052, (9052, (), [ (16387, 10, None, "IID('{72EFA71D-BCE9-4369-9F66-CEB35906BB91}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ContactSurfaceOnly' , 'pVal' , ), 9053, (9053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ContactSurfaceOnly' , 'pVal' , ), 9053, (9053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ContactSurfaceOnlyType' , 'pVal' , ), 9054, (9054, (), [ (3, 1, None, "IID('{C95A86C1-418C-4819-805F-C3A8B0462E52}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ContactSurfaceOnlyType' , 'pVal' , ), 9054, (9054, (), [ (16387, 10, None, "IID('{C95A86C1-418C-4819-805F-C3A8B0462E52}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'VectorDisplay' , 'flag' , ), 9055, (9055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'VectorDisplay' , 'flag' , ), 9055, (9055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'VectorDisplayArrowSize' , 'size' , ), 9056, (9056, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'VectorDisplayArrowSize' , 'size' , ), 9056, (9056, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'VectorDisplayArrowSizeUniformFlag' , 'flag' , ), 9057, (9057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'VectorDisplayArrowSizeUniformFlag' , 'flag' , ), 9057, (9057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IDisplaySetting_vtables_dispatch_ = 1
IDisplaySetting_vtables_ = [
	(( 'DisplaySettingPropertyComponentCollection' , 'ppVal' , ), 9001, (9001, (), [ (16393, 10, None, "IID('{DFF377E2-7234-4010-96C0-8CA009DEBD56}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySettingElementComponentCollection' , 'ppVal' , ), 9002, (9002, (), [ (16393, 10, None, "IID('{52806F36-F171-48E0-8D94-7DD010A28932}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySettingNodeSetCollection' , 'ppVal' , ), 9003, (9003, (), [ (16393, 10, None, "IID('{B316708B-BF84-429A-8994-19A2A03A2F1E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySettingElementSetCollection' , 'ppVal' , ), 9004, (9004, (), [ (16393, 10, None, "IID('{23196F83-DC3B-4007-8FA0-814AB1E6A121}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySettingPatchSetCollection' , 'ppVal' , ), 9005, (9005, (), [ (16393, 10, None, "IID('{51C1F29C-9E5D-4CEA-B013-5623F0FCD1E8}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ShowBC' , 'pVal' , ), 9006, (9006, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShowBC' , 'pVal' , ), 9006, (9006, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ShowAllNodes' , 'pVal' , ), 9007, (9007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ShowAllNodes' , 'pVal' , ), 9007, (9007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ShowOutput' , 'pVal' , ), 9008, (9008, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ShowOutput' , 'pVal' , ), 9008, (9008, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ShowNodeID' , 'pVal' , ), 9009, (9009, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ShowNodeID' , 'pVal' , ), 9009, (9009, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SetNodeIDFlagWithType' , 'valType' , 'Val' , ), 9010, (9010, (), [ (3, 1, None, "IID('{C53060A3-9F48-4893-BE0B-3C58109A7C94}')") , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'GetNodeIDFlagWithType' , 'valType' , 'ppVal' , ), 9011, (9011, (), [ (3, 1, None, "IID('{C53060A3-9F48-4893-BE0B-3C58109A7C94}')") , 
			 (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShowMeshLine' , 'pVal' , ), 9012, (9012, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ShowMeshLine' , 'pVal' , ), 9012, (9012, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'MeshLineColor' , 'pVal' , ), 9013, (9013, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'MeshLineColor' , 'pVal' , ), 9013, (9013, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ShowFeatureLine' , 'pVal' , ), 9014, (9014, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ShowFeatureLine' , 'pVal' , ), 9014, (9014, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'FeatureLineColor' , 'pVal' , ), 9015, (9015, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'FeatureLineColor' , 'pVal' , ), 9015, (9015, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ShowRenderFeatureLineOnly' , 'pVal' , ), 9016, (9016, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ShowRenderFeatureLineOnly' , 'pVal' , ), 9016, (9016, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'HighlightColor' , 'pVal' , ), 9017, (9017, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'HighlightColor' , 'pVal' , ), 9017, (9017, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'NodeColor' , 'pVal' , ), 9018, (9018, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'NodeColor' , 'pVal' , ), 9018, (9018, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CuttingPlane' , 'pVal' , ), 9019, (9019, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CuttingPlane' , 'pVal' , ), 9019, (9019, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CuttingPlaneFlexType' , 'pVal' , ), 9020, (9020, (), [ (3, 1, None, "IID('{06EC13C1-6CEB-4C01-826C-923D1D06B369}')") , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'CuttingPlaneFlexType' , 'pVal' , ), 9020, (9020, (), [ (16387, 10, None, "IID('{06EC13C1-6CEB-4C01-826C-923D1D06B369}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySettingLineSetCollection' , 'ppVal' , ), 9021, (9021, (), [ (16393, 10, None, "IID('{338BA605-D8D7-4E04-B937-8138288AFE4D}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ShowBeamCrossSection' , 'pVal' , ), 9022, (9022, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ShowBeamCrossSection' , 'pVal' , ), 9022, (9022, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySettingTopologyComponentCollection' , 'ppVal' , ), 9023, (9023, (), [ (16393, 10, None, "IID('{B7EAE1DC-7E8F-4008-84B8-801FBCECBB4C}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ShowShellThickness' , 'pVal' , ), 9024, (9024, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ShowShellThickness' , 'pVal' , ), 9024, (9024, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
]

IDisplaySettingElementComponent_vtables_dispatch_ = 1
IDisplaySettingElementComponent_vtables_ = [
	(( 'Name' , 'pVal' , ), 9051, (9051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDisplaySettingElementComponentCollection_vtables_dispatch_ = 1
IDisplaySettingElementComponentCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{DE06422B-331F-496E-BCAD-FBBB082D57F2}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IDisplaySettingElementSet_vtables_dispatch_ = 1
IDisplaySettingElementSet_vtables_ = [
	(( 'Name' , 'pVal' , ), 9051, (9051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDisplaySettingElementSetCollection_vtables_dispatch_ = 1
IDisplaySettingElementSetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{C08D408A-9B9B-4F2D-A029-E4BA81008A6B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IDisplaySettingLineSet_vtables_dispatch_ = 1
IDisplaySettingLineSet_vtables_ = [
	(( 'Name' , 'pVal' , ), 9051, (9051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDisplaySettingLineSetCollection_vtables_dispatch_ = 1
IDisplaySettingLineSetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{BF489D0D-9A7B-4C64-8AA9-FA3330A12A33}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IDisplaySettingNodeSet_vtables_dispatch_ = 1
IDisplaySettingNodeSet_vtables_ = [
	(( 'Name' , 'pVal' , ), 9051, (9051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDisplaySettingNodeSetCollection_vtables_dispatch_ = 1
IDisplaySettingNodeSetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{ABB44B8A-B12A-452A-9F5F-C40C189D93C4}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IDisplaySettingPatchSet_vtables_dispatch_ = 1
IDisplaySettingPatchSet_vtables_ = [
	(( 'Name' , 'pVal' , ), 9051, (9051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDisplaySettingPatchSetCollection_vtables_dispatch_ = 1
IDisplaySettingPatchSetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{FD68A22C-A406-4D04-B1D7-1277926333BF}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IDisplaySettingPropertyComponent_vtables_dispatch_ = 1
IDisplaySettingPropertyComponent_vtables_ = [
	(( 'Name' , 'pVal' , ), 9051, (9051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDisplaySettingPropertyComponentCollection_vtables_dispatch_ = 1
IDisplaySettingPropertyComponentCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{3F3FB9FE-0E56-4FEA-A6A8-9912D45B7B10}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IDisplaySettingTopologyComponent_vtables_dispatch_ = 1
IDisplaySettingTopologyComponent_vtables_ = [
	(( 'Name' , 'pVal' , ), 9051, (9051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Show' , 'pVal' , ), 9052, (9052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 9053, (9053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IDisplaySettingTopologyComponentCollection_vtables_dispatch_ = 1
IDisplaySettingTopologyComponentCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{F043499D-DB45-419E-AF1F-8F057CAAA006}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IExportShellFormatData_vtables_dispatch_ = 1
IExportShellFormatData_vtables_ = [
	(( 'Type' , 'pVal' , ), 9001, (9001, (), [ (3, 1, None, "IID('{47CB4292-A8CC-4A9A-8FD5-A0876C024744}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 9001, (9001, (), [ (16387, 10, None, "IID('{47CB4292-A8CC-4A9A-8FD5-A0876C024744}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AddPatchSets' , 'Val' , ), 9002, (9002, (), [ (8204, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DeletePatchSets' , 'Val' , ), 9003, (9003, (), [ (8204, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'Val' , ), 9004, (9004, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IGManager_vtables_dispatch_ = 1
IGManager_vtables_ = [
	(( 'SourceBody' , 'ppVal' , ), 9001, (9001, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SourceBody' , 'ppVal' , ), 9001, (9001, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SourceBodyType' , 'pVal' , ), 9002, (9002, (), [ (16387, 10, None, "IID('{169C1AA7-9A04-4768-AAB0-290810BEB2EC}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TargetBodyType' , 'pVal' , ), 9003, (9003, (), [ (3, 1, None, "IID('{169C1AA7-9A04-4768-AAB0-290810BEB2EC}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TargetBodyType' , 'pVal' , ), 9003, (9003, (), [ (16387, 10, None, "IID('{169C1AA7-9A04-4768-AAB0-290810BEB2EC}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Rigid' , 'ppVal' , ), 9004, (9004, (), [ (16393, 10, None, "IID('{4FFEA591-BF79-4FF5-95A9-409860AC2D1E}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RFlex' , 'ppVal' , ), 9005, (9005, (), [ (16393, 10, None, "IID('{B9638194-9BB8-44A9-B999-4E26073A84E6}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'FFlex' , 'ppVal' , ), 9006, (9006, (), [ (16393, 10, None, "IID('{E131531A-921C-4AE5-A53D-F5C39A65AAFF}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 9007, (9007, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IGManagerAssistModelingOption_vtables_dispatch_ = 1
IGManagerAssistModelingOption_vtables_ = [
	(( 'UseName' , 'pVal' , ), 9051, (9051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseName' , 'pVal' , ), 9051, (9051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'TargetBodyName' , 'pVal' , ), 9052, (9052, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'TargetBodyName' , 'pVal' , ), 9052, (9052, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'pVal' , ), 9053, (9053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialVelocity' , 'pVal' , ), 9053, (9053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseMassCMPosition' , 'pVal' , ), 9054, (9054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseMassCMPosition' , 'pVal' , ), 9054, (9054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UseJoint' , 'pVal' , ), 9055, (9055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'UseJoint' , 'pVal' , ), 9055, (9055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseForce' , 'pVal' , ), 9056, (9056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseForce' , 'pVal' , ), 9056, (9056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseGeoContact' , 'pVal' , ), 9057, (9057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseGeoContact' , 'pVal' , ), 9057, (9057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IGManagerFFlex_vtables_dispatch_ = 1
IGManagerFFlex_vtables_ = [
	(( 'Rigid' , 'ppVal' , ), 9051, (9051, (), [ (16393, 10, None, "IID('{2B8967E0-1892-46E4-A700-9E3384FE1AFF}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RFlex' , 'ppVal' , ), 9052, (9052, (), [ (16393, 10, None, "IID('{AC2631CE-2984-4F21-B299-4808917E8F75}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FFlex' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{7446389E-9E2B-48BD-ACD2-158D332A3B70}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseCreateMeshDataFile' , 'pVal' , ), 9054, (9054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseCreateMeshDataFile' , 'pVal' , ), 9054, (9054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MeshDataFileName' , 'pVal' , ), 9055, (9055, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'MeshDataFileName' , 'pVal' , ), 9055, (9055, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IGManagerFFlexBodySwapOption_vtables_dispatch_ = 1
IGManagerFFlexBodySwapOption_vtables_ = [
	(( 'UseAllowNullProperty' , 'pVal' , ), 9051, (9051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseAllowNullProperty' , 'pVal' , ), 9051, (9051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UnitOfSource' , 'ppVal' , ), 9052, (9052, (), [ (9, 1, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UnitOfSource' , 'ppVal' , ), 9052, (9052, (), [ (16393, 10, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseUnitForce' , 'pVal' , ), 9053, (9053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseUnitForce' , 'pVal' , ), 9053, (9053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseForceConnector' , 'pVal' , ), 9054, (9054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseForceConnector' , 'pVal' , ), 9054, (9054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UseCreateBeamElementWithPreStress' , 'pVal' , ), 9055, (9055, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'UseCreateBeamElementWithPreStress' , 'pVal' , ), 9055, (9055, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseGeneratePatchSetFromNodeElementSet' , 'pVal' , ), 9056, (9056, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseGeneratePatchSetFromNodeElementSet' , 'pVal' , ), 9056, (9056, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IGManagerFFlexToFFlex_vtables_dispatch_ = 1
IGManagerFFlexToFFlex_vtables_ = [
	(( 'FileName' , 'pVal' , ), 9051, (9051, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9051, (9051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9052, (9052, (), [ (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9052, (9052, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SwapOption' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AssistModelingOption' , 'ppVal' , ), 9054, (9054, (), [ (16393, 10, None, "IID('{16FD62CA-B60D-4326-9349-593F526D8399}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IGManagerFFlexToRFlex_vtables_dispatch_ = 1
IGManagerFFlexToRFlex_vtables_ = [
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{DBF72417-17F7-48D5-8A68-F05EF7815686}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{DBF72417-17F7-48D5-8A68-F05EF7815686}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RFlexGenerator' , 'ppResult' , ), 9054, (9054, (), [ (16393, 10, None, "IID('{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SwapOption' , 'ppVal' , ), 9055, (9055, (), [ (16393, 10, None, "IID('{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AssistModelingOption' , 'ppVal' , ), 9056, (9056, (), [ (16393, 10, None, "IID('{16FD62CA-B60D-4326-9349-593F526D8399}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IGManagerFFlexToRigid_vtables_dispatch_ = 1
IGManagerFFlexToRigid_vtables_ = [
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{CAB41C0B-391A-4591-A8AB-D476023E8C54}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{CAB41C0B-391A-4591-A8AB-D476023E8C54}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AssistModelingOption' , 'ppVal' , ), 9054, (9054, (), [ (16393, 10, None, "IID('{16FD62CA-B60D-4326-9349-593F526D8399}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IGManagerMeshMode_vtables_dispatch_ = 1
IGManagerMeshMode_vtables_ = [
]

IGManagerRFlex_vtables_dispatch_ = 1
IGManagerRFlex_vtables_ = [
	(( 'Rigid' , 'ppVal' , ), 9051, (9051, (), [ (16393, 10, None, "IID('{91189C2F-929B-42E4-B61C-9823D5F5B6C6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FFlex' , 'ppVal' , ), 9052, (9052, (), [ (16393, 10, None, "IID('{4C4268D2-08E0-4D59-AF4F-E84E30762CE3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RFlex' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{B1163AE3-2374-4B52-B76C-FA21254528E3}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IGManagerRFlexBodySwapOption_vtables_dispatch_ = 1
IGManagerRFlexBodySwapOption_vtables_ = [
	(( 'UseUserDefinedRigidBodyFrequency' , 'pVal' , ), 9051, (9051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedRigidBodyFrequency' , 'pVal' , ), 9051, (9051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedRigidBodyFrequency' , 'value' , ), 9052, (9052, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedRigidBodyFrequency' , 'value' , ), 9052, (9052, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseAnimationWithNoDeformation' , 'pVal' , ), 9053, (9053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseAnimationWithNoDeformation' , 'pVal' , ), 9053, (9053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IGManagerRFlexGenerationOption_vtables_dispatch_ = 1
IGManagerRFlexGenerationOption_vtables_ = [
	(( 'InterfaceNodeIDs' , 'arrNodeID' , ), 9051, (9051, (), [ (8195, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeIDs' , 'arrNodeID' , ), 9051, (9051, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeset' , 'ppVal' , ), 9052, (9052, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeset' , 'ppVal' , ), 9052, (9052, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeNumber' , 'pVal' , ), 9053, (9053, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedDOFs' , 'pVal' , ), 9054, (9054, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedDOFs' , 'pVal' , ), 9054, (9054, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedDOFs' , 'arrUserDefinedDOF' , ), 9055, (9055, (), [ (8200, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedDOFs' , 'arrUserDefinedDOF' , ), 9055, (9055, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'NormalModeNumber' , 'pVal' , ), 9056, (9056, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'NormalModeNumber' , 'pVal' , ), 9056, (9056, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LowerFrequency' , 'pVal' , ), 9057, (9057, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'LowerFrequency' , 'pVal' , ), 9057, (9057, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UpperFrequency' , 'pVal' , ), 9058, (9058, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UpperFrequency' , 'pVal' , ), 9058, (9058, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Unit' , 'ppVal' , ), 9059, (9059, (), [ (9, 1, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Unit' , 'ppVal' , ), 9059, (9059, (), [ (16393, 10, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UseRemoveMidNodeRelatedInformation' , 'pVal' , ), 9060, (9060, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseRemoveMidNodeRelatedInformation' , 'pVal' , ), 9060, (9060, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseRemoveZeroValueForRotModeShape' , 'pVal' , ), 9061, (9061, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UseRemoveZeroValueForRotModeShape' , 'pVal' , ), 9061, (9061, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseDeleteDynamisDataBaseFiles' , 'pVal' , ), 9062, (9062, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseDeleteDynamisDataBaseFiles' , 'pVal' , ), 9062, (9062, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseRFITranslator' , 'pVal' , ), 9063, (9063, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseRFITranslator' , 'pVal' , ), 9063, (9063, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ShellDrillingParameter' , 'pVal' , ), 9064, (9064, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ShellDrillingParameter' , 'pVal' , ), 9064, (9064, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseStressShape' , 'pVal' , ), 9065, (9065, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseStressShape' , 'pVal' , ), 9065, (9065, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseStrainShape' , 'pVal' , ), 9066, (9066, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseStrainShape' , 'pVal' , ), 9066, (9066, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Solver' , 'pVal' , ), 9067, (9067, (), [ (3, 1, None, "IID('{751C1136-D0D2-41B4-98DF-2C88CE95D9C4}')") , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Solver' , 'pVal' , ), 9067, (9067, (), [ (16387, 10, None, "IID('{751C1136-D0D2-41B4-98DF-2C88CE95D9C4}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IGManagerRFlexGenerator_vtables_dispatch_ = 1
IGManagerRFlexGenerator_vtables_ = [
	(( 'Option' , 'ppResult' , ), 9051, (9051, (), [ (16393, 10, None, "IID('{15EDB8CA-E02D-4905-AA0F-7A11B74C1885}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 9052, (9052, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IGManagerRFlexToFFlex_vtables_dispatch_ = 1
IGManagerRFlexToFFlex_vtables_ = [
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{3A4759E5-0425-4ADD-A97D-73A552D9E92B}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{3A4759E5-0425-4ADD-A97D-73A552D9E92B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SwapOption' , 'ppVal' , ), 9054, (9054, (), [ (16393, 10, None, "IID('{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AssistModelingOption' , 'ppVal' , ), 9055, (9055, (), [ (16393, 10, None, "IID('{16FD62CA-B60D-4326-9349-593F526D8399}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IGManagerRFlexToRFlex_vtables_dispatch_ = 1
IGManagerRFlexToRFlex_vtables_ = [
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{E4BAB8EC-EBC5-4D4C-994E-33DA940FBA24}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{E4BAB8EC-EBC5-4D4C-994E-33DA940FBA24}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RFlexGenerator' , 'ppResult' , ), 9054, (9054, (), [ (16393, 10, None, "IID('{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SwapOption' , 'ppVal' , ), 9055, (9055, (), [ (16393, 10, None, "IID('{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AssistModelingOption' , 'ppVal' , ), 9056, (9056, (), [ (16393, 10, None, "IID('{16FD62CA-B60D-4326-9349-593F526D8399}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IGManagerRFlexToRigid_vtables_dispatch_ = 1
IGManagerRFlexToRigid_vtables_ = [
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{5F3848CC-A1D6-49FE-B0CE-828636B19E9B}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{5F3848CC-A1D6-49FE-B0CE-828636B19E9B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9052, (9052, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AssistModelingOption' , 'ppVal' , ), 9054, (9054, (), [ (16393, 10, None, "IID('{16FD62CA-B60D-4326-9349-593F526D8399}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IGManagerRigid_vtables_dispatch_ = 1
IGManagerRigid_vtables_ = [
	(( 'FFlex' , 'ppVal' , ), 9051, (9051, (), [ (16393, 10, None, "IID('{FC9A332A-067D-462E-8B85-57A5A41ECDF8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'RFlex' , 'ppVal' , ), 9052, (9052, (), [ (16393, 10, None, "IID('{80FB287D-32EF-4386-989A-4FD1DAC82798}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseCreateCADFile' , 'pVal' , ), 9053, (9053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseCreateCADFile' , 'pVal' , ), 9053, (9053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CADFileName' , 'pVal' , ), 9054, (9054, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CADFileName' , 'pVal' , ), 9054, (9054, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IGManagerRigidToFFlex_vtables_dispatch_ = 1
IGManagerRigidToFFlex_vtables_ = [
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (3, 1, None, "IID('{0ACC9971-A2C9-49A0-94C7-41C4DA79A699}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ConvertType' , 'pVal' , ), 9051, (9051, (), [ (16387, 10, None, "IID('{0ACC9971-A2C9-49A0-94C7-41C4DA79A699}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SourceGeometry' , 'ppVal' , ), 9052, (9052, (), [ (9, 1, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SourceGeometry' , 'ppVal' , ), 9052, (9052, (), [ (16393, 10, None, "IID('{07DEC20D-9506-49E3-BF94-8CD7C78FA1EB}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9053, (9053, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9053, (9053, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9054, (9054, (), [ (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9054, (9054, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SwapOption' , 'ppVal' , ), 9055, (9055, (), [ (16393, 10, None, "IID('{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'AssistModelingOption' , 'ppVal' , ), 9056, (9056, (), [ (16393, 10, None, "IID('{16FD62CA-B60D-4326-9349-593F526D8399}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'MeshMode' , 'ppVal' , ), 9057, (9057, (), [ (16393, 10, None, "IID('{87FC24B2-6ADC-4804-A601-5B896632C326}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IGManagerRigidToRFlex_vtables_dispatch_ = 1
IGManagerRigidToRFlex_vtables_ = [
	(( 'FileName' , 'pVal' , ), 9051, (9051, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 9051, (9051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9052, (9052, (), [ (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceFrame' , 'ppVal' , ), 9052, (9052, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SwapOption' , 'ppVal' , ), 9053, (9053, (), [ (16393, 10, None, "IID('{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AssistModelingOption' , 'ppVal' , ), 9054, (9054, (), [ (16393, 10, None, "IID('{16FD62CA-B60D-4326-9349-593F526D8399}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{49E653C4-054B-4496-B4FA-9EF8947B2C94}' : IContourTypeOption,
	'{B88B9BB0-1991-486D-8248-3FD7CEE798DB}' : IContourMinMaxOption,
	'{6A77B683-DB6D-47CC-A9A4-8A1236F68D9E}' : IContourBandOption,
	'{FC113BCB-DE52-4C7B-BE93-029A709898B0}' : IContourStyleOption,
	'{FB58C4A7-6D67-465F-A7D3-ADB1B7E53425}' : IContourReferenceNode,
	'{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}' : IContourDataTrace,
	'{14C89575-CA21-4656-988A-87151B83C368}' : IContourPartSelection,
	'{139D3F54-8397-417D-8AA9-B8E92666E31A}' : IContourDataExport,
	'{CC340394-39A2-489C-B59E-F62063FBE6D2}' : IContourReferenceNodeCollection,
	'{9F8AB0C2-9B88-4A3D-A279-5E653738A009}' : IContourDataTraceCollection,
	'{4A8EAB35-DBC8-4E2E-8E70-2D5C34C7F6BA}' : IContourPartSelectionCollection,
	'{BDF4F979-28B7-48D2-BF06-9C59B70D467B}' : IContour,
	'{3F3FB9FE-0E56-4FEA-A6A8-9912D45B7B10}' : IDisplaySettingPropertyComponent,
	'{DE06422B-331F-496E-BCAD-FBBB082D57F2}' : IDisplaySettingElementComponent,
	'{F043499D-DB45-419E-AF1F-8F057CAAA006}' : IDisplaySettingTopologyComponent,
	'{ABB44B8A-B12A-452A-9F5F-C40C189D93C4}' : IDisplaySettingNodeSet,
	'{C08D408A-9B9B-4F2D-A029-E4BA81008A6B}' : IDisplaySettingElementSet,
	'{FD68A22C-A406-4D04-B1D7-1277926333BF}' : IDisplaySettingPatchSet,
	'{BF489D0D-9A7B-4C64-8AA9-FA3330A12A33}' : IDisplaySettingLineSet,
	'{DFF377E2-7234-4010-96C0-8CA009DEBD56}' : IDisplaySettingPropertyComponentCollection,
	'{52806F36-F171-48E0-8D94-7DD010A28932}' : IDisplaySettingElementComponentCollection,
	'{B7EAE1DC-7E8F-4008-84B8-801FBCECBB4C}' : IDisplaySettingTopologyComponentCollection,
	'{B316708B-BF84-429A-8994-19A2A03A2F1E}' : IDisplaySettingNodeSetCollection,
	'{23196F83-DC3B-4007-8FA0-814AB1E6A121}' : IDisplaySettingElementSetCollection,
	'{51C1F29C-9E5D-4CEA-B013-5623F0FCD1E8}' : IDisplaySettingPatchSetCollection,
	'{338BA605-D8D7-4E04-B937-8138288AFE4D}' : IDisplaySettingLineSetCollection,
	'{3FDF0768-0052-4B63-9D84-A644C3152051}' : IDisplaySetting,
	'{2EE15E44-AD0C-4D9B-B53A-35BF7F1E1322}' : IExportShellFormatData,
	'{87FC24B2-6ADC-4804-A601-5B896632C326}' : IGManagerMeshMode,
	'{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}' : IGManagerFFlexBodySwapOption,
	'{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}' : IGManagerRFlexBodySwapOption,
	'{16FD62CA-B60D-4326-9349-593F526D8399}' : IGManagerAssistModelingOption,
	'{15EDB8CA-E02D-4905-AA0F-7A11B74C1885}' : IGManagerRFlexGenerationOption,
	'{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}' : IGManagerRFlexGenerator,
	'{FC9A332A-067D-462E-8B85-57A5A41ECDF8}' : IGManagerRigidToFFlex,
	'{80FB287D-32EF-4386-989A-4FD1DAC82798}' : IGManagerRigidToRFlex,
	'{4FFEA591-BF79-4FF5-95A9-409860AC2D1E}' : IGManagerRigid,
	'{91189C2F-929B-42E4-B61C-9823D5F5B6C6}' : IGManagerRFlexToRigid,
	'{4C4268D2-08E0-4D59-AF4F-E84E30762CE3}' : IGManagerRFlexToFFlex,
	'{B1163AE3-2374-4B52-B76C-FA21254528E3}' : IGManagerRFlexToRFlex,
	'{B9638194-9BB8-44A9-B999-4E26073A84E6}' : IGManagerRFlex,
	'{2B8967E0-1892-46E4-A700-9E3384FE1AFF}' : IGManagerFFlexToRigid,
	'{AC2631CE-2984-4F21-B299-4808917E8F75}' : IGManagerFFlexToRFlex,
	'{7446389E-9E2B-48BD-ACD2-158D332A3B70}' : IGManagerFFlexToFFlex,
	'{E131531A-921C-4AE5-A53D-F5C39A65AAFF}' : IGManagerFFlex,
	'{04C740C7-BD7B-4DA9-A03A-CFAD5CBA0FFB}' : IGManager,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{49E653C4-054B-4496-B4FA-9EF8947B2C94}' : 'IContourTypeOption',
	'{B88B9BB0-1991-486D-8248-3FD7CEE798DB}' : 'IContourMinMaxOption',
	'{6A77B683-DB6D-47CC-A9A4-8A1236F68D9E}' : 'IContourBandOption',
	'{FC113BCB-DE52-4C7B-BE93-029A709898B0}' : 'IContourStyleOption',
	'{FB58C4A7-6D67-465F-A7D3-ADB1B7E53425}' : 'IContourReferenceNode',
	'{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}' : 'IContourDataTrace',
	'{14C89575-CA21-4656-988A-87151B83C368}' : 'IContourPartSelection',
	'{139D3F54-8397-417D-8AA9-B8E92666E31A}' : 'IContourDataExport',
	'{CC340394-39A2-489C-B59E-F62063FBE6D2}' : 'IContourReferenceNodeCollection',
	'{9F8AB0C2-9B88-4A3D-A279-5E653738A009}' : 'IContourDataTraceCollection',
	'{4A8EAB35-DBC8-4E2E-8E70-2D5C34C7F6BA}' : 'IContourPartSelectionCollection',
	'{BDF4F979-28B7-48D2-BF06-9C59B70D467B}' : 'IContour',
	'{3F3FB9FE-0E56-4FEA-A6A8-9912D45B7B10}' : 'IDisplaySettingPropertyComponent',
	'{DE06422B-331F-496E-BCAD-FBBB082D57F2}' : 'IDisplaySettingElementComponent',
	'{F043499D-DB45-419E-AF1F-8F057CAAA006}' : 'IDisplaySettingTopologyComponent',
	'{ABB44B8A-B12A-452A-9F5F-C40C189D93C4}' : 'IDisplaySettingNodeSet',
	'{C08D408A-9B9B-4F2D-A029-E4BA81008A6B}' : 'IDisplaySettingElementSet',
	'{FD68A22C-A406-4D04-B1D7-1277926333BF}' : 'IDisplaySettingPatchSet',
	'{BF489D0D-9A7B-4C64-8AA9-FA3330A12A33}' : 'IDisplaySettingLineSet',
	'{DFF377E2-7234-4010-96C0-8CA009DEBD56}' : 'IDisplaySettingPropertyComponentCollection',
	'{52806F36-F171-48E0-8D94-7DD010A28932}' : 'IDisplaySettingElementComponentCollection',
	'{B7EAE1DC-7E8F-4008-84B8-801FBCECBB4C}' : 'IDisplaySettingTopologyComponentCollection',
	'{B316708B-BF84-429A-8994-19A2A03A2F1E}' : 'IDisplaySettingNodeSetCollection',
	'{23196F83-DC3B-4007-8FA0-814AB1E6A121}' : 'IDisplaySettingElementSetCollection',
	'{51C1F29C-9E5D-4CEA-B013-5623F0FCD1E8}' : 'IDisplaySettingPatchSetCollection',
	'{338BA605-D8D7-4E04-B937-8138288AFE4D}' : 'IDisplaySettingLineSetCollection',
	'{3FDF0768-0052-4B63-9D84-A644C3152051}' : 'IDisplaySetting',
	'{2EE15E44-AD0C-4D9B-B53A-35BF7F1E1322}' : 'IExportShellFormatData',
	'{87FC24B2-6ADC-4804-A601-5B896632C326}' : 'IGManagerMeshMode',
	'{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}' : 'IGManagerFFlexBodySwapOption',
	'{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}' : 'IGManagerRFlexBodySwapOption',
	'{16FD62CA-B60D-4326-9349-593F526D8399}' : 'IGManagerAssistModelingOption',
	'{15EDB8CA-E02D-4905-AA0F-7A11B74C1885}' : 'IGManagerRFlexGenerationOption',
	'{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}' : 'IGManagerRFlexGenerator',
	'{FC9A332A-067D-462E-8B85-57A5A41ECDF8}' : 'IGManagerRigidToFFlex',
	'{80FB287D-32EF-4386-989A-4FD1DAC82798}' : 'IGManagerRigidToRFlex',
	'{4FFEA591-BF79-4FF5-95A9-409860AC2D1E}' : 'IGManagerRigid',
	'{91189C2F-929B-42E4-B61C-9823D5F5B6C6}' : 'IGManagerRFlexToRigid',
	'{4C4268D2-08E0-4D59-AF4F-E84E30762CE3}' : 'IGManagerRFlexToFFlex',
	'{B1163AE3-2374-4B52-B76C-FA21254528E3}' : 'IGManagerRFlexToRFlex',
	'{B9638194-9BB8-44A9-B999-4E26073A84E6}' : 'IGManagerRFlex',
	'{2B8967E0-1892-46E4-A700-9E3384FE1AFF}' : 'IGManagerFFlexToRigid',
	'{AC2631CE-2984-4F21-B299-4808917E8F75}' : 'IGManagerFFlexToRFlex',
	'{7446389E-9E2B-48BD-ACD2-158D332A3B70}' : 'IGManagerFFlexToFFlex',
	'{E131531A-921C-4AE5-A53D-F5C39A65AAFF}' : 'IGManagerFFlex',
	'{04C740C7-BD7B-4DA9-A03A-CFAD5CBA0FFB}' : 'IGManager',
}


NamesToIIDMap = {
	'IContourTypeOption' : '{49E653C4-054B-4496-B4FA-9EF8947B2C94}',
	'IContourMinMaxOption' : '{B88B9BB0-1991-486D-8248-3FD7CEE798DB}',
	'IContourBandOption' : '{6A77B683-DB6D-47CC-A9A4-8A1236F68D9E}',
	'IContourStyleOption' : '{FC113BCB-DE52-4C7B-BE93-029A709898B0}',
	'IContourReferenceNode' : '{FB58C4A7-6D67-465F-A7D3-ADB1B7E53425}',
	'IContourDataTrace' : '{7F27DD16-0BB9-42A0-8B9A-87110AAEBE50}',
	'IContourPartSelection' : '{14C89575-CA21-4656-988A-87151B83C368}',
	'IContourDataExport' : '{139D3F54-8397-417D-8AA9-B8E92666E31A}',
	'IContourReferenceNodeCollection' : '{CC340394-39A2-489C-B59E-F62063FBE6D2}',
	'IContourDataTraceCollection' : '{9F8AB0C2-9B88-4A3D-A279-5E653738A009}',
	'IContourPartSelectionCollection' : '{4A8EAB35-DBC8-4E2E-8E70-2D5C34C7F6BA}',
	'IContour' : '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}',
	'IDisplaySettingPropertyComponent' : '{3F3FB9FE-0E56-4FEA-A6A8-9912D45B7B10}',
	'IDisplaySettingElementComponent' : '{DE06422B-331F-496E-BCAD-FBBB082D57F2}',
	'IDisplaySettingTopologyComponent' : '{F043499D-DB45-419E-AF1F-8F057CAAA006}',
	'IDisplaySettingNodeSet' : '{ABB44B8A-B12A-452A-9F5F-C40C189D93C4}',
	'IDisplaySettingElementSet' : '{C08D408A-9B9B-4F2D-A029-E4BA81008A6B}',
	'IDisplaySettingPatchSet' : '{FD68A22C-A406-4D04-B1D7-1277926333BF}',
	'IDisplaySettingLineSet' : '{BF489D0D-9A7B-4C64-8AA9-FA3330A12A33}',
	'IDisplaySettingPropertyComponentCollection' : '{DFF377E2-7234-4010-96C0-8CA009DEBD56}',
	'IDisplaySettingElementComponentCollection' : '{52806F36-F171-48E0-8D94-7DD010A28932}',
	'IDisplaySettingTopologyComponentCollection' : '{B7EAE1DC-7E8F-4008-84B8-801FBCECBB4C}',
	'IDisplaySettingNodeSetCollection' : '{B316708B-BF84-429A-8994-19A2A03A2F1E}',
	'IDisplaySettingElementSetCollection' : '{23196F83-DC3B-4007-8FA0-814AB1E6A121}',
	'IDisplaySettingPatchSetCollection' : '{51C1F29C-9E5D-4CEA-B013-5623F0FCD1E8}',
	'IDisplaySettingLineSetCollection' : '{338BA605-D8D7-4E04-B937-8138288AFE4D}',
	'IDisplaySetting' : '{3FDF0768-0052-4B63-9D84-A644C3152051}',
	'IExportShellFormatData' : '{2EE15E44-AD0C-4D9B-B53A-35BF7F1E1322}',
	'IGManagerMeshMode' : '{87FC24B2-6ADC-4804-A601-5B896632C326}',
	'IGManagerFFlexBodySwapOption' : '{EA79E2EC-FC5C-4E01-8679-02B271AD65A0}',
	'IGManagerRFlexBodySwapOption' : '{95FDE7A7-8179-43B8-A60C-D3ABBD886E9B}',
	'IGManagerAssistModelingOption' : '{16FD62CA-B60D-4326-9349-593F526D8399}',
	'IGManagerRFlexGenerationOption' : '{15EDB8CA-E02D-4905-AA0F-7A11B74C1885}',
	'IGManagerRFlexGenerator' : '{B423FEFF-EC1A-4FA3-8D21-8E1A72D95937}',
	'IGManagerRigidToFFlex' : '{FC9A332A-067D-462E-8B85-57A5A41ECDF8}',
	'IGManagerRigidToRFlex' : '{80FB287D-32EF-4386-989A-4FD1DAC82798}',
	'IGManagerRigid' : '{4FFEA591-BF79-4FF5-95A9-409860AC2D1E}',
	'IGManagerRFlexToRigid' : '{91189C2F-929B-42E4-B61C-9823D5F5B6C6}',
	'IGManagerRFlexToFFlex' : '{4C4268D2-08E0-4D59-AF4F-E84E30762CE3}',
	'IGManagerRFlexToRFlex' : '{B1163AE3-2374-4B52-B76C-FA21254528E3}',
	'IGManagerRFlex' : '{B9638194-9BB8-44A9-B999-4E26073A84E6}',
	'IGManagerFFlexToRigid' : '{2B8967E0-1892-46E4-A700-9E3384FE1AFF}',
	'IGManagerFFlexToRFlex' : '{AC2631CE-2984-4F21-B299-4808917E8F75}',
	'IGManagerFFlexToFFlex' : '{7446389E-9E2B-48BD-ACD2-158D332A3B70}',
	'IGManagerFFlex' : '{E131531A-921C-4AE5-A53D-F5C39A65AAFF}',
	'IGManager' : '{04C740C7-BD7B-4DA9-A03A-CFAD5CBA0FFB}',
}


