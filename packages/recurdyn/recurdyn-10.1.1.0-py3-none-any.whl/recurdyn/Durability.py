# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMDurability.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMDurability Type Library'
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

CLSID = IID('{2A5B2E30-33D8-4FA2-AFE5-6AC2C6063A13}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class AngleType(IntEnum):
	'''
	AngleType enumeration.
	'''
	AngleType_MaxDamage           =0         
	'''Constant value is 0.'''
	AngleType_UserDefined         =1         
	'''Constant value is 1.'''
class AxialMode(IntEnum):
	'''
	AxialMode enumeration.
	'''
	BiAxial                       =1         
	'''Constant value is 1.'''
	UniAxial                      =0         
	'''Constant value is 0.'''
class BWIWeldType(IntEnum):
	'''
	BWIWeldType enumeration.
	'''
	BWI_CLASS_B                   =0         
	'''Constant value is 0.'''
	BWI_CLASS_C                   =1         
	'''Constant value is 1.'''
	BWI_CLASS_D                   =2         
	'''Constant value is 2.'''
	BWI_CLASS_E                   =3         
	'''Constant value is 3.'''
	BWI_CLASS_F                   =4         
	'''Constant value is 4.'''
	BWI_CLASS_F2                  =5         
	'''Constant value is 5.'''
	BWI_CLASS_G                   =6         
	'''Constant value is 6.'''
	BWI_CLASS_S                   =8         
	'''Constant value is 8.'''
	BWI_CLASS_T                   =9         
	'''Constant value is 9.'''
	BWI_CLASS_W                   =7         
	'''Constant value is 7.'''
class BandLegendLocationType(IntEnum):
	'''
	BandLegendLocationType enumeration.
	'''
	Band_Legned_Location_Bottom   =1         
	'''Constant value is 1.'''
	Band_Legned_Location_Left     =2         
	'''Constant value is 2.'''
	Band_Legned_Location_Right    =3         
	'''Constant value is 3.'''
	Band_Legned_Location_Top      =0         
	'''Constant value is 0.'''
class BandLegendType(IntEnum):
	'''
	BandLegendType enumeration.
	'''
	Band_Legned_Dialog            =1         
	'''Constant value is 1.'''
	Band_Legned_Disable           =0         
	'''Constant value is 0.'''
	Band_Legned_Display           =2         
	'''Constant value is 2.'''
class ColorStyle(IntEnum):
	'''
	ColorStyle enumeration.
	'''
	Color_Style_Smooth            =0         
	'''Constant value is 0.'''
	Color_Style_Stepped           =2         
	'''Constant value is 2.'''
	Color_Style_Wire              =1         
	'''Constant value is 1.'''
class ColorType(IntEnum):
	'''
	ColorType enumeration.
	'''
	Color_Gray_Scale              =1         
	'''Constant value is 1.'''
	Color_Spectrum                =0         
	'''Constant value is 0.'''
class ContourOptionType(IntEnum):
	'''
	ContourOptionType enumeration.
	'''
	Damage                        =0         
	'''Constant value is 0.'''
	Life                          =1         
	'''Constant value is 1.'''
class ContourViewType(IntEnum):
	'''
	ContourViewType enumeration.
	'''
	View_Both                     =2         
	'''Constant value is 2.'''
	View_Contour_Only             =0         
	'''Constant value is 0.'''
	View_Mean_Stress              =3         
	'''Constant value is 3.'''
	View_Stress_Amplitude         =4         
	'''Constant value is 4.'''
	View_Vector_Only              =1         
	'''Constant value is 1.'''
class FatigueMaterialUnitType(IntEnum):
	'''
	FatigueMaterialUnitType enumeration.
	'''
	inch_lb                       =2         
	'''Constant value is 2.'''
	m_N                           =0         
	'''Constant value is 0.'''
	mm_N                          =1         
	'''Constant value is 1.'''
class FatigueSurfaceFactorType(IntEnum):
	'''
	FatigueSurfaceFactorType enumeration.
	'''
	ForgedType                    =4         
	'''Constant value is 4.'''
	GroundType                    =1         
	'''Constant value is 1.'''
	MachinedType                  =2         
	'''Constant value is 2.'''
	PolishedType                  =0         
	'''Constant value is 0.'''
	RolledType                    =3         
	'''Constant value is 3.'''
	UserInputType                 =5         
	'''Constant value is 5.'''
class LifeCriteria(IntEnum):
	'''
	LifeCriteria enumeration.
	'''
	SafetyFactor                  =2         
	'''Constant value is 2.'''
	StrainBased                   =1         
	'''Constant value is 1.'''
	StressBased                   =0         
	'''Constant value is 0.'''
class MeanStressEffectType(IntEnum):
	'''
	MeanStressEffectType enumeration.
	'''
	Mean_Gerber                   =2         
	'''Constant value is 2.'''
	Mean_Goodman                  =1         
	'''Constant value is 1.'''
	Mean_Morrow                   =4         
	'''Constant value is 4.'''
	Mean_None                     =0         
	'''Constant value is 0.'''
	Mean_Sodeberg                 =3         
	'''Constant value is 3.'''
class MinMaxType(IntEnum):
	'''
	MinMaxType enumeration.
	'''
	Min_Max_Display               =0         
	'''Constant value is 0.'''
	Min_Max_UserDefined           =1         
	'''Constant value is 1.'''
class PatchLocationType(IntEnum):
	'''
	PatchLocationType enumeration.
	'''
	PatchLocationType_MaxDamage   =0         
	'''Constant value is 0.'''
	PatchLocationType_UserDefined =1         
	'''Constant value is 1.'''
class ProbeType(IntEnum):
	'''
	ProbeType enumeration.
	'''
	ProbeType_Node                =0         
	'''Constant value is 0.'''
	ProbeType_Patch               =1         
	'''Constant value is 1.'''
class RecoveryType(IntEnum):
	'''
	RecoveryType enumeration.
	'''
	Extrapolation                 =1         
	'''Constant value is 1.'''
	Face_Center                   =0         
	'''Constant value is 0.'''
class SafetyFactorLifeCriterion(IntEnum):
	'''
	SafetyFactorLifeCriterion enumeration.
	'''
	SafetyFactor_Gerber           =1         
	'''Constant value is 1.'''
	SafetyFactor_Goodman          =0         
	'''Constant value is 0.'''
	SafetyFactor_ModifiedGoodman  =2         
	'''Constant value is 2.'''
	SafetyFactor_UserDefined      =3         
	'''Constant value is 3.'''
class SearchingIncrement(IntEnum):
	'''
	SearchingIncrement enumeration.
	'''
	Increment_10Deg               =4         
	'''Constant value is 4.'''
	Increment_1Deg                =0         
	'''Constant value is 0.'''
	Increment_2Deg                =1         
	'''Constant value is 1.'''
	Increment_3Deg                =2         
	'''Constant value is 2.'''
	Increment_5Deg                =3         
	'''Constant value is 3.'''
class StrainLifeCriterion(IntEnum):
	'''
	StrainLifeCriterion enumeration.
	'''
	Strain_Brown_Miller           =0         
	'''Constant value is 0.'''
	Strain_Manson_Coffin          =1         
	'''Constant value is 1.'''
	Strain_Max_Shear              =4         
	'''Constant value is 4.'''
	Strain_Morrow                 =2         
	'''Constant value is 2.'''
	Strain_Smith_Watson_Topper    =3         
	'''Constant value is 3.'''
	Strain_UserDefined            =5         
	'''Constant value is 5.'''
class StressLifeCriterion(IntEnum):
	'''
	StressLifeCriterion enumeration.
	'''
	Stress_ASME                   =1         
	'''Constant value is 1.'''
	Stress_BWIWeld                =2         
	'''Constant value is 2.'''
	Stress_MansonCoffin           =0         
	'''Constant value is 0.'''
	Stress_UserDefined            =3         
	'''Constant value is 3.'''
class UserDefinedInterpolationType(IntEnum):
	'''
	UserDefinedInterpolationType enumeration.
	'''
	UserDefinedInterpolation_Exponential=1         
	'''Constant value is 1.'''
	UserDefinedInterpolation_Linear=0         
	'''Constant value is 0.'''

from win32com.client import DispatchBaseClass
class IDurabilityContour(DispatchBaseClass):
	'''Durability Contour'''
	CLSID = IID('{A7CCAFA8-34D0-4D9E-97F9-F92C15E19BAB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def ContourView(self):
		'''
		Contour View
		'''
		return self._oleobj_.InvokeTypes(8005, LCID, 1, (24, 0), (),)


	def ExportContourData(self, Val):
		'''
		Export Contour Data
		
		:param Val: str
		'''
		return self._oleobj_.InvokeTypes(8006, LCID, 1, (24, 0), ((8, 1),),Val
			)


	def ExportContourDataWithNodeSet(self, Val, pVal):
		'''
		Export Contour Data with Nodeset
		
		:param Val: str
		:param pVal: IGeneric
		'''
		return self._oleobj_.InvokeTypes(8010, LCID, 1, (24, 0), ((8, 1), (9, 1)),Val
			, pVal)


	def _get_BandOption(self):
		return self._ApplyTypes_(*(8002, 2, (9, 0), (), "BandOption", '{1877A27A-16EC-492A-B121-2158CA766380}'))
	def _get_MinMaxOption(self):
		return self._ApplyTypes_(*(8003, 2, (9, 0), (), "MinMaxOption", '{02902C9C-2767-4E11-A750-6AFDF9F1386B}'))
	def _get_OptionType(self):
		return self._ApplyTypes_(*(8001, 2, (3, 0), (), "OptionType", '{F2BAAF75-AFB8-4C6B-8CD5-6D51760DE479}'))
	def _get_ProbeOption(self):
		return self._ApplyTypes_(*(8009, 2, (9, 0), (), "ProbeOption", '{3707C188-79DF-4DC1-9F29-6DF34660C998}'))
	def _get_RecoveryType(self):
		return self._ApplyTypes_(*(8011, 2, (3, 0), (), "RecoveryType", '{B25FC8C8-6CB0-48D7-84B9-0233923E9B4A}'))
	def _get_StyleOption(self):
		return self._ApplyTypes_(*(8004, 2, (9, 0), (), "StyleOption", '{AD4A1D92-5D4B-47CA-BD19-CDBA4567BB11}'))
	def _get_ViewType(self):
		return self._ApplyTypes_(*(8008, 2, (3, 0), (), "ViewType", '{0DF9B5BF-ABCC-4F55-B059-ADF6739F936F}'))

	def _set_OptionType(self, value):
		if "OptionType" in self.__dict__: self.__dict__["OptionType"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_RecoveryType(self, value):
		if "RecoveryType" in self.__dict__: self.__dict__["RecoveryType"] = value; return
		self._oleobj_.Invoke(*((8011, LCID, 4, 0) + (value,) + ()))
	def _set_TimeHistoryIndex(self, value):
		if "TimeHistoryIndex" in self.__dict__: self.__dict__["TimeHistoryIndex"] = value; return
		self._oleobj_.Invoke(*((8007, LCID, 4, 0) + (value,) + ()))
	def _set_ViewType(self, value):
		if "ViewType" in self.__dict__: self.__dict__["ViewType"] = value; return
		self._oleobj_.Invoke(*((8008, LCID, 4, 0) + (value,) + ()))

	BandOption = property(_get_BandOption, None)
	'''
	Get Contour Band Option

	:type: recurdyn.Durability.IDurabilityContourBandOption
	'''
	MinMaxOption = property(_get_MinMaxOption, None)
	'''
	Get Contour MinMax Option

	:type: recurdyn.Durability.IDurabilityContourMinMaxOption
	'''
	OptionType = property(_get_OptionType, _set_OptionType)
	'''
	Contour Option Type

	:type: recurdyn.Durability.ContourOptionType
	'''
	ProbeOption = property(_get_ProbeOption, None)
	'''
	Get Contour Probe Option

	:type: recurdyn.Durability.IDurabilityContourProbeOption
	'''
	RecoveryType = property(_get_RecoveryType, _set_RecoveryType)
	'''
	Contour Recovery Type

	:type: recurdyn.Durability.RecoveryType
	'''
	StyleOption = property(_get_StyleOption, None)
	'''
	Get Contour Style Option

	:type: recurdyn.Durability.IDurabilityContourStyleOption
	'''
	ViewType = property(_get_ViewType, _set_ViewType)
	'''
	Contour View Type

	:type: recurdyn.Durability.ContourViewType
	'''
	TimeHistoryIndex = property(None, _set_TimeHistoryIndex)
	'''
	TimeHistory Index

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_OptionType": _set_OptionType,
		"_set_RecoveryType": _set_RecoveryType,
		"_set_TimeHistoryIndex": _set_TimeHistoryIndex,
		"_set_ViewType": _set_ViewType,
	}
	_prop_map_get_ = {
		"BandOption": (8002, 2, (9, 0), (), "BandOption", '{1877A27A-16EC-492A-B121-2158CA766380}'),
		"MinMaxOption": (8003, 2, (9, 0), (), "MinMaxOption", '{02902C9C-2767-4E11-A750-6AFDF9F1386B}'),
		"OptionType": (8001, 2, (3, 0), (), "OptionType", '{F2BAAF75-AFB8-4C6B-8CD5-6D51760DE479}'),
		"ProbeOption": (8009, 2, (9, 0), (), "ProbeOption", '{3707C188-79DF-4DC1-9F29-6DF34660C998}'),
		"RecoveryType": (8011, 2, (3, 0), (), "RecoveryType", '{B25FC8C8-6CB0-48D7-84B9-0233923E9B4A}'),
		"StyleOption": (8004, 2, (9, 0), (), "StyleOption", '{AD4A1D92-5D4B-47CA-BD19-CDBA4567BB11}'),
		"ViewType": (8008, 2, (3, 0), (), "ViewType", '{0DF9B5BF-ABCC-4F55-B059-ADF6739F936F}'),
	}
	_prop_map_put_ = {
		"OptionType": ((8001, LCID, 4, 0),()),
		"RecoveryType": ((8011, LCID, 4, 0),()),
		"TimeHistoryIndex": ((8007, LCID, 4, 0),()),
		"ViewType": ((8008, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityContourBandOption(DispatchBaseClass):
	'''Durability Contour Band Option'''
	CLSID = IID('{1877A27A-16EC-492A-B121-2158CA766380}')
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
		return self._ApplyTypes_(*(8054, 2, (19, 0), (), "BandLevel", None))
	def _get_LegendLocation(self):
		return self._ApplyTypes_(*(8052, 2, (3, 0), (), "LegendLocation", '{962D1C1A-1074-4306-BEAE-9EA10A4D2D6E}'))
	def _get_LegendType(self):
		return self._ApplyTypes_(*(8051, 2, (3, 0), (), "LegendType", '{98CEF211-B3D9-487F-AD57-B46FFDCE1E8E}'))
	def _get_ShowTextLegend(self):
		return self._ApplyTypes_(*(8053, 2, (11, 0), (), "ShowTextLegend", None))

	def _set_BandLevel(self, value):
		if "BandLevel" in self.__dict__: self.__dict__["BandLevel"] = value; return
		self._oleobj_.Invoke(*((8054, LCID, 4, 0) + (value,) + ()))
	def _set_LegendLocation(self, value):
		if "LegendLocation" in self.__dict__: self.__dict__["LegendLocation"] = value; return
		self._oleobj_.Invoke(*((8052, LCID, 4, 0) + (value,) + ()))
	def _set_LegendType(self, value):
		if "LegendType" in self.__dict__: self.__dict__["LegendType"] = value; return
		self._oleobj_.Invoke(*((8051, LCID, 4, 0) + (value,) + ()))
	def _set_ShowTextLegend(self, value):
		if "ShowTextLegend" in self.__dict__: self.__dict__["ShowTextLegend"] = value; return
		self._oleobj_.Invoke(*((8053, LCID, 4, 0) + (value,) + ()))

	BandLevel = property(_get_BandLevel, _set_BandLevel)
	'''
	Band Level

	:type: int
	'''
	LegendLocation = property(_get_LegendLocation, _set_LegendLocation)
	'''
	Contour Band Legend Location Type

	:type: recurdyn.Durability.BandLegendLocationType
	'''
	LegendType = property(_get_LegendType, _set_LegendType)
	'''
	Contour Band Legend Type

	:type: recurdyn.Durability.BandLegendType
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
		"BandLevel": (8054, 2, (19, 0), (), "BandLevel", None),
		"LegendLocation": (8052, 2, (3, 0), (), "LegendLocation", '{962D1C1A-1074-4306-BEAE-9EA10A4D2D6E}'),
		"LegendType": (8051, 2, (3, 0), (), "LegendType", '{98CEF211-B3D9-487F-AD57-B46FFDCE1E8E}'),
		"ShowTextLegend": (8053, 2, (11, 0), (), "ShowTextLegend", None),
	}
	_prop_map_put_ = {
		"BandLevel": ((8054, LCID, 4, 0),()),
		"LegendLocation": ((8052, LCID, 4, 0),()),
		"LegendType": ((8051, LCID, 4, 0),()),
		"ShowTextLegend": ((8053, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityContourMinMaxOption(DispatchBaseClass):
	'''Durability Contour MinMax Option'''
	CLSID = IID('{02902C9C-2767-4E11-A750-6AFDF9F1386B}')
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
		return self._oleobj_.InvokeTypes(8055, LCID, 1, (24, 0), (),)


	def _get_EnableLogScale(self):
		return self._ApplyTypes_(*(8053, 2, (11, 0), (), "EnableLogScale", None))
	def _get_Max(self):
		return self._ApplyTypes_(*(8057, 2, (5, 0), (), "Max", None))
	def _get_Min(self):
		return self._ApplyTypes_(*(8056, 2, (5, 0), (), "Min", None))
	def _get_MinMaxType(self):
		return self._ApplyTypes_(*(8051, 2, (3, 0), (), "MinMaxType", '{E2761D2D-999A-4CB7-BDFB-4868168F684D}'))
	def _get_ShowMinMax(self):
		return self._ApplyTypes_(*(8052, 2, (11, 0), (), "ShowMinMax", None))
	def _get_UserDefinedMax(self):
		return self._ApplyTypes_(*(8059, 2, (5, 0), (), "UserDefinedMax", None))
	def _get_UserDefinedMin(self):
		return self._ApplyTypes_(*(8058, 2, (5, 0), (), "UserDefinedMin", None))

	def _set_EnableLogScale(self, value):
		if "EnableLogScale" in self.__dict__: self.__dict__["EnableLogScale"] = value; return
		self._oleobj_.Invoke(*((8053, LCID, 4, 0) + (value,) + ()))
	def _set_MinMaxType(self, value):
		if "MinMaxType" in self.__dict__: self.__dict__["MinMaxType"] = value; return
		self._oleobj_.Invoke(*((8051, LCID, 4, 0) + (value,) + ()))
	def _set_ShowMinMax(self, value):
		if "ShowMinMax" in self.__dict__: self.__dict__["ShowMinMax"] = value; return
		self._oleobj_.Invoke(*((8052, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedMax(self, value):
		if "UserDefinedMax" in self.__dict__: self.__dict__["UserDefinedMax"] = value; return
		self._oleobj_.Invoke(*((8059, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedMin(self, value):
		if "UserDefinedMin" in self.__dict__: self.__dict__["UserDefinedMin"] = value; return
		self._oleobj_.Invoke(*((8058, LCID, 4, 0) + (value,) + ()))

	EnableLogScale = property(_get_EnableLogScale, _set_EnableLogScale)
	'''
	Enable Log Scale

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
	MinMaxType = property(_get_MinMaxType, _set_MinMaxType)
	'''
	Contour Min Max Type

	:type: recurdyn.Durability.MinMaxType
	'''
	ShowMinMax = property(_get_ShowMinMax, _set_ShowMinMax)
	'''
	Show Min Max

	:type: bool
	'''
	UserDefinedMax = property(_get_UserDefinedMax, _set_UserDefinedMax)
	'''
	User Defined Max Value

	:type: float
	'''
	UserDefinedMin = property(_get_UserDefinedMin, _set_UserDefinedMin)
	'''
	User Defined Min Value

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_EnableLogScale": _set_EnableLogScale,
		"_set_MinMaxType": _set_MinMaxType,
		"_set_ShowMinMax": _set_ShowMinMax,
		"_set_UserDefinedMax": _set_UserDefinedMax,
		"_set_UserDefinedMin": _set_UserDefinedMin,
	}
	_prop_map_get_ = {
		"EnableLogScale": (8053, 2, (11, 0), (), "EnableLogScale", None),
		"Max": (8057, 2, (5, 0), (), "Max", None),
		"Min": (8056, 2, (5, 0), (), "Min", None),
		"MinMaxType": (8051, 2, (3, 0), (), "MinMaxType", '{E2761D2D-999A-4CB7-BDFB-4868168F684D}'),
		"ShowMinMax": (8052, 2, (11, 0), (), "ShowMinMax", None),
		"UserDefinedMax": (8059, 2, (5, 0), (), "UserDefinedMax", None),
		"UserDefinedMin": (8058, 2, (5, 0), (), "UserDefinedMin", None),
	}
	_prop_map_put_ = {
		"EnableLogScale": ((8053, LCID, 4, 0),()),
		"MinMaxType": ((8051, LCID, 4, 0),()),
		"ShowMinMax": ((8052, LCID, 4, 0),()),
		"UserDefinedMax": ((8059, LCID, 4, 0),()),
		"UserDefinedMin": ((8058, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityContourProbeOption(DispatchBaseClass):
	'''Durability Contour Probe Option'''
	CLSID = IID('{3707C188-79DF-4DC1-9F29-6DF34660C998}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Clear(self):
		'''
		Clear Probe Data
		'''
		return self._oleobj_.InvokeTypes(8053, LCID, 1, (24, 0), (),)


	def Select(self, Val):
		'''
		Select Probe Data
		
		:param Val: ProbeType
		'''
		return self._oleobj_.InvokeTypes(8052, LCID, 1, (24, 0), ((3, 1),),Val
			)


	def _get_ShowProbeResult(self):
		return self._ApplyTypes_(*(8051, 2, (11, 0), (), "ShowProbeResult", None))

	def _set_ShowProbeResult(self, value):
		if "ShowProbeResult" in self.__dict__: self.__dict__["ShowProbeResult"] = value; return
		self._oleobj_.Invoke(*((8051, LCID, 4, 0) + (value,) + ()))

	ShowProbeResult = property(_get_ShowProbeResult, _set_ShowProbeResult)
	'''
	Show Probe Result

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ShowProbeResult": _set_ShowProbeResult,
	}
	_prop_map_get_ = {
		"ShowProbeResult": (8051, 2, (11, 0), (), "ShowProbeResult", None),
	}
	_prop_map_put_ = {
		"ShowProbeResult": ((8051, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityContourStyleOption(DispatchBaseClass):
	'''Durability Contour Style Option'''
	CLSID = IID('{AD4A1D92-5D4B-47CA-BD19-CDBA4567BB11}')
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
		return self._ApplyTypes_(*(8051, 2, (3, 0), (), "ColorType", '{9BA27F29-EA82-4029-ADFA-18351FD3A6E3}'))
	def _get_GrayScaleColor(self):
		return self._ApplyTypes_(*(8055, 2, (19, 0), (), "GrayScaleColor", None))
	def _get_MeshLinesColor(self):
		return self._ApplyTypes_(*(8058, 2, (19, 0), (), "MeshLinesColor", None))
	def _get_ShowMeshLines(self):
		return self._ApplyTypes_(*(8057, 2, (11, 0), (), "ShowMeshLines", None))
	def _get_SpectrumMaxColor(self):
		return self._ApplyTypes_(*(8054, 2, (19, 0), (), "SpectrumMaxColor", None))
	def _get_SpectrumMinColor(self):
		return self._ApplyTypes_(*(8053, 2, (19, 0), (), "SpectrumMinColor", None))
	def _get_Style(self):
		return self._ApplyTypes_(*(8052, 2, (3, 0), (), "Style", '{055C0C4E-D758-49A8-BC89-3262E1832894}'))
	def _get_TextColor(self):
		return self._ApplyTypes_(*(8056, 2, (19, 0), (), "TextColor", None))
	def _get_VectorColor(self):
		return self._ApplyTypes_(*(8059, 2, (19, 0), (), "VectorColor", None))
	def _get_VectorSize(self):
		return self._ApplyTypes_(*(8060, 2, (5, 0), (), "VectorSize", None))

	def _set_ColorType(self, value):
		if "ColorType" in self.__dict__: self.__dict__["ColorType"] = value; return
		self._oleobj_.Invoke(*((8051, LCID, 4, 0) + (value,) + ()))
	def _set_GrayScaleColor(self, value):
		if "GrayScaleColor" in self.__dict__: self.__dict__["GrayScaleColor"] = value; return
		self._oleobj_.Invoke(*((8055, LCID, 4, 0) + (value,) + ()))
	def _set_MeshLinesColor(self, value):
		if "MeshLinesColor" in self.__dict__: self.__dict__["MeshLinesColor"] = value; return
		self._oleobj_.Invoke(*((8058, LCID, 4, 0) + (value,) + ()))
	def _set_ShowMeshLines(self, value):
		if "ShowMeshLines" in self.__dict__: self.__dict__["ShowMeshLines"] = value; return
		self._oleobj_.Invoke(*((8057, LCID, 4, 0) + (value,) + ()))
	def _set_SpectrumMaxColor(self, value):
		if "SpectrumMaxColor" in self.__dict__: self.__dict__["SpectrumMaxColor"] = value; return
		self._oleobj_.Invoke(*((8054, LCID, 4, 0) + (value,) + ()))
	def _set_SpectrumMinColor(self, value):
		if "SpectrumMinColor" in self.__dict__: self.__dict__["SpectrumMinColor"] = value; return
		self._oleobj_.Invoke(*((8053, LCID, 4, 0) + (value,) + ()))
	def _set_Style(self, value):
		if "Style" in self.__dict__: self.__dict__["Style"] = value; return
		self._oleobj_.Invoke(*((8052, LCID, 4, 0) + (value,) + ()))
	def _set_TextColor(self, value):
		if "TextColor" in self.__dict__: self.__dict__["TextColor"] = value; return
		self._oleobj_.Invoke(*((8056, LCID, 4, 0) + (value,) + ()))
	def _set_VectorColor(self, value):
		if "VectorColor" in self.__dict__: self.__dict__["VectorColor"] = value; return
		self._oleobj_.Invoke(*((8059, LCID, 4, 0) + (value,) + ()))
	def _set_VectorSize(self, value):
		if "VectorSize" in self.__dict__: self.__dict__["VectorSize"] = value; return
		self._oleobj_.Invoke(*((8060, LCID, 4, 0) + (value,) + ()))

	ColorType = property(_get_ColorType, _set_ColorType)
	'''
	Color Type

	:type: recurdyn.Durability.ColorType
	'''
	GrayScaleColor = property(_get_GrayScaleColor, _set_GrayScaleColor)
	'''
	Gray Scale Color

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

	:type: recurdyn.Durability.ColorStyle
	'''
	TextColor = property(_get_TextColor, _set_TextColor)
	'''
	Text Color

	:type: int
	'''
	VectorColor = property(_get_VectorColor, _set_VectorColor)
	'''
	Vector Color

	:type: int
	'''
	VectorSize = property(_get_VectorSize, _set_VectorSize)
	'''
	Vector Size

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_ColorType": _set_ColorType,
		"_set_GrayScaleColor": _set_GrayScaleColor,
		"_set_MeshLinesColor": _set_MeshLinesColor,
		"_set_ShowMeshLines": _set_ShowMeshLines,
		"_set_SpectrumMaxColor": _set_SpectrumMaxColor,
		"_set_SpectrumMinColor": _set_SpectrumMinColor,
		"_set_Style": _set_Style,
		"_set_TextColor": _set_TextColor,
		"_set_VectorColor": _set_VectorColor,
		"_set_VectorSize": _set_VectorSize,
	}
	_prop_map_get_ = {
		"ColorType": (8051, 2, (3, 0), (), "ColorType", '{9BA27F29-EA82-4029-ADFA-18351FD3A6E3}'),
		"GrayScaleColor": (8055, 2, (19, 0), (), "GrayScaleColor", None),
		"MeshLinesColor": (8058, 2, (19, 0), (), "MeshLinesColor", None),
		"ShowMeshLines": (8057, 2, (11, 0), (), "ShowMeshLines", None),
		"SpectrumMaxColor": (8054, 2, (19, 0), (), "SpectrumMaxColor", None),
		"SpectrumMinColor": (8053, 2, (19, 0), (), "SpectrumMinColor", None),
		"Style": (8052, 2, (3, 0), (), "Style", '{055C0C4E-D758-49A8-BC89-3262E1832894}'),
		"TextColor": (8056, 2, (19, 0), (), "TextColor", None),
		"VectorColor": (8059, 2, (19, 0), (), "VectorColor", None),
		"VectorSize": (8060, 2, (5, 0), (), "VectorSize", None),
	}
	_prop_map_put_ = {
		"ColorType": ((8051, LCID, 4, 0),()),
		"GrayScaleColor": ((8055, LCID, 4, 0),()),
		"MeshLinesColor": ((8058, LCID, 4, 0),()),
		"ShowMeshLines": ((8057, LCID, 4, 0),()),
		"SpectrumMaxColor": ((8054, LCID, 4, 0),()),
		"SpectrumMinColor": ((8053, LCID, 4, 0),()),
		"Style": ((8052, LCID, 4, 0),()),
		"TextColor": ((8056, LCID, 4, 0),()),
		"VectorColor": ((8059, LCID, 4, 0),()),
		"VectorSize": ((8060, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityFatigueEvaluation(DispatchBaseClass):
	'''Durability Fatigue Evaluation'''
	CLSID = IID('{D65A4952-C3CE-42F4-A6F2-D7DEBEF72EC0}')
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
		Calculation Fatigue
		'''
		return self._oleobj_.InvokeTypes(8011, LCID, 1, (24, 0), (),)


	def ClearTimeHistory(self):
		'''
		Clear Time History List
		'''
		return self._oleobj_.InvokeTypes(8017, LCID, 1, (24, 0), (),)


	def CreateTimeHistory(self, use, Name, timeRange):
		'''
		Create Time History
		
		:param use: bool
		:param Name: str
		:param timeRange: str
		'''
		return self._oleobj_.InvokeTypes(8016, LCID, 1, (24, 0), ((11, 1), (8, 1), (8, 1)),use
			, Name, timeRange)


	def Import(self, strFileName):
		'''
		Import Previous Fatigue Results
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(8019, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def PlotHistory(self):
		'''
		Plot Original History in Fatigue Tool
		'''
		return self._oleobj_.InvokeTypes(8013, LCID, 1, (24, 0), (),)


	def RainFlowCounting(self):
		'''
		RainFlow Counting in Fatigue Tool
		'''
		return self._oleobj_.InvokeTypes(8012, LCID, 1, (24, 0), (),)


	def _get_AxialMode(self):
		return self._ApplyTypes_(*(8001, 2, (3, 0), (), "AxialMode", '{AA2BBDF8-4B1A-4EA2-8139-59D10C3CABC2}'))
	def _get_ElementPatchSet(self):
		return self._ApplyTypes_(*(8003, 2, (9, 0), (), "ElementPatchSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_LifeCriteria(self):
		return self._ApplyTypes_(*(8002, 2, (3, 0), (), "LifeCriteria", '{237F28A9-AF92-45CF-BA8A-0035B4D3E04D}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(8006, 2, (9, 0), (), "Material", '{6E70D029-92E7-453A-81C7-8BC9727DCB8D}'))
	def _get_Occurrence(self):
		return self._ApplyTypes_(*(8005, 2, (9, 0), (), "Occurrence", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlotOriginalHistory(self):
		return self._ApplyTypes_(*(8015, 2, (9, 0), (), "PlotOriginalHistory", '{1B06AC13-47EA-4070-A4FD-CE5E341F2650}'))
	def _get_PreStressFile(self):
		return self._ApplyTypes_(*(8021, 2, (8, 0), (), "PreStressFile", None))
	def _get_RainFlow(self):
		return self._ApplyTypes_(*(8014, 2, (9, 0), (), "RainFlow", '{5494C9D5-49B9-476D-A973-A5C524009AC9}'))
	def _get_Result(self):
		return self._ApplyTypes_(*(8010, 2, (9, 0), (), "Result", '{AA1358DD-7933-4CFE-B738-AFB37F0C0D0E}'))
	def _get_SafetyFactor(self):
		return self._ApplyTypes_(*(8009, 2, (9, 0), (), "SafetyFactor", '{CDBAEBAA-5287-4F55-A6A4-7AA213D3D045}'))
	def _get_SpecificAngleCalculationOption(self):
		return self._ApplyTypes_(*(8023, 2, (9, 0), (), "SpecificAngleCalculationOption", '{4D1AEBE0-9522-4D83-B1E9-784161452107}'))
	def _get_SpecificAngleCalculationResult(self):
		return self._ApplyTypes_(*(8024, 2, (9, 0), (), "SpecificAngleCalculationResult", '{20342F66-B448-4E67-8C28-3C74142E38C2}'))
	def _get_Strain(self):
		return self._ApplyTypes_(*(8008, 2, (9, 0), (), "Strain", '{EBA808F3-9FD8-4375-BD38-F71DFB281AC8}'))
	def _get_Stress(self):
		return self._ApplyTypes_(*(8007, 2, (9, 0), (), "Stress", '{40E8C43D-5AF9-44F9-80F5-F8FB9984879A}'))
	def _get_TimeHistoryCollection(self):
		return self._ApplyTypes_(*(8018, 2, (9, 0), (), "TimeHistoryCollection", '{0FC6C5F7-150B-4077-A5CA-D0DCF8B79777}'))
	def _get_TimeHistoryWithFrame(self):
		return self._ApplyTypes_(*(8004, 2, (8, 0), (), "TimeHistoryWithFrame", None))
	def _get_UsePreStress(self):
		return self._ApplyTypes_(*(8020, 2, (11, 0), (), "UsePreStress", None))
	def _get_UseRecalculateRecovery(self):
		return self._ApplyTypes_(*(8022, 2, (11, 0), (), "UseRecalculateRecovery", None))

	def _set_AxialMode(self, value):
		if "AxialMode" in self.__dict__: self.__dict__["AxialMode"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_ElementPatchSet(self, value):
		if "ElementPatchSet" in self.__dict__: self.__dict__["ElementPatchSet"] = value; return
		self._oleobj_.Invoke(*((8003, LCID, 4, 0) + (value,) + ()))
	def _set_LifeCriteria(self, value):
		if "LifeCriteria" in self.__dict__: self.__dict__["LifeCriteria"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))
	def _set_PreStressFile(self, value):
		if "PreStressFile" in self.__dict__: self.__dict__["PreStressFile"] = value; return
		self._oleobj_.Invoke(*((8021, LCID, 4, 0) + (value,) + ()))
	def _set_TimeHistoryWithFrame(self, value):
		if "TimeHistoryWithFrame" in self.__dict__: self.__dict__["TimeHistoryWithFrame"] = value; return
		self._oleobj_.Invoke(*((8004, LCID, 4, 0) + (value,) + ()))
	def _set_UsePreStress(self, value):
		if "UsePreStress" in self.__dict__: self.__dict__["UsePreStress"] = value; return
		self._oleobj_.Invoke(*((8020, LCID, 4, 0) + (value,) + ()))
	def _set_UseRecalculateRecovery(self, value):
		if "UseRecalculateRecovery" in self.__dict__: self.__dict__["UseRecalculateRecovery"] = value; return
		self._oleobj_.Invoke(*((8022, LCID, 4, 0) + (value,) + ()))

	AxialMode = property(_get_AxialMode, _set_AxialMode)
	'''
	Axial Mode

	:type: recurdyn.Durability.AxialMode
	'''
	ElementPatchSet = property(_get_ElementPatchSet, _set_ElementPatchSet)
	'''
	Element/ Patch Set

	:type: recurdyn.ProcessNet.IGeneric
	'''
	LifeCriteria = property(_get_LifeCriteria, _set_LifeCriteria)
	'''
	Life Criteria

	:type: recurdyn.Durability.LifeCriteria
	'''
	Material = property(_get_Material, None)
	'''
	Get fatigue Material

	:type: recurdyn.Durability.IDurabilityFatigueMaterial
	'''
	Occurrence = property(_get_Occurrence, None)
	'''
	Occurrence

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlotOriginalHistory = property(_get_PlotOriginalHistory, None)
	'''
	Get Plot Original History

	:type: recurdyn.Durability.IDurabilityPlotOriginalHistory
	'''
	PreStressFile = property(_get_PreStressFile, _set_PreStressFile)
	'''
	Pre-Stress file

	:type: str
	'''
	RainFlow = property(_get_RainFlow, None)
	'''
	Get Rainflow Counting

	:type: recurdyn.Durability.IDurabilityRainflowCounting
	'''
	Result = property(_get_Result, None)
	'''
	Get fatigue Evaluation Result

	:type: recurdyn.Durability.IDurabilityFatigueResult
	'''
	SafetyFactor = property(_get_SafetyFactor, None)
	'''
	Get fatigue Evaluation Safety Factor

	:type: recurdyn.Durability.IDurabilityFatigueEvaluationSafetyFactor
	'''
	SpecificAngleCalculationOption = property(_get_SpecificAngleCalculationOption, None)
	'''
	Get Specific Angle Calculation Option

	:type: recurdyn.Durability.IDurabilitySpecificAngleCalculationOption
	'''
	SpecificAngleCalculationResult = property(_get_SpecificAngleCalculationResult, None)
	'''
	Get Specific Angle Calculation Result

	:type: recurdyn.Durability.IDurabilitySpecificAngleCalculationResult
	'''
	Strain = property(_get_Strain, None)
	'''
	Get fatigue Evaluation Strain

	:type: recurdyn.Durability.IDurabilityFatigueEvaluationStrain
	'''
	Stress = property(_get_Stress, None)
	'''
	Get fatigue Evaluation Stress

	:type: recurdyn.Durability.IDurabilityFatigueEvaluationStress
	'''
	TimeHistoryCollection = property(_get_TimeHistoryCollection, None)
	'''
	Time History collection

	:type: recurdyn.Durability.IDurabilityTimeHistoryCollection
	'''
	TimeHistoryWithFrame = property(_get_TimeHistoryWithFrame, _set_TimeHistoryWithFrame)
	'''
	Time History With Frame : obsolete function

	:type: str
	'''
	UsePreStress = property(_get_UsePreStress, _set_UsePreStress)
	'''
	Use Pre-Stress file

	:type: bool
	'''
	UseRecalculateRecovery = property(_get_UseRecalculateRecovery, _set_UseRecalculateRecovery)
	'''
	Use RecalculateRecovery

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_AxialMode": _set_AxialMode,
		"_set_ElementPatchSet": _set_ElementPatchSet,
		"_set_LifeCriteria": _set_LifeCriteria,
		"_set_PreStressFile": _set_PreStressFile,
		"_set_TimeHistoryWithFrame": _set_TimeHistoryWithFrame,
		"_set_UsePreStress": _set_UsePreStress,
		"_set_UseRecalculateRecovery": _set_UseRecalculateRecovery,
	}
	_prop_map_get_ = {
		"AxialMode": (8001, 2, (3, 0), (), "AxialMode", '{AA2BBDF8-4B1A-4EA2-8139-59D10C3CABC2}'),
		"ElementPatchSet": (8003, 2, (9, 0), (), "ElementPatchSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"LifeCriteria": (8002, 2, (3, 0), (), "LifeCriteria", '{237F28A9-AF92-45CF-BA8A-0035B4D3E04D}'),
		"Material": (8006, 2, (9, 0), (), "Material", '{6E70D029-92E7-453A-81C7-8BC9727DCB8D}'),
		"Occurrence": (8005, 2, (9, 0), (), "Occurrence", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlotOriginalHistory": (8015, 2, (9, 0), (), "PlotOriginalHistory", '{1B06AC13-47EA-4070-A4FD-CE5E341F2650}'),
		"PreStressFile": (8021, 2, (8, 0), (), "PreStressFile", None),
		"RainFlow": (8014, 2, (9, 0), (), "RainFlow", '{5494C9D5-49B9-476D-A973-A5C524009AC9}'),
		"Result": (8010, 2, (9, 0), (), "Result", '{AA1358DD-7933-4CFE-B738-AFB37F0C0D0E}'),
		"SafetyFactor": (8009, 2, (9, 0), (), "SafetyFactor", '{CDBAEBAA-5287-4F55-A6A4-7AA213D3D045}'),
		"SpecificAngleCalculationOption": (8023, 2, (9, 0), (), "SpecificAngleCalculationOption", '{4D1AEBE0-9522-4D83-B1E9-784161452107}'),
		"SpecificAngleCalculationResult": (8024, 2, (9, 0), (), "SpecificAngleCalculationResult", '{20342F66-B448-4E67-8C28-3C74142E38C2}'),
		"Strain": (8008, 2, (9, 0), (), "Strain", '{EBA808F3-9FD8-4375-BD38-F71DFB281AC8}'),
		"Stress": (8007, 2, (9, 0), (), "Stress", '{40E8C43D-5AF9-44F9-80F5-F8FB9984879A}'),
		"TimeHistoryCollection": (8018, 2, (9, 0), (), "TimeHistoryCollection", '{0FC6C5F7-150B-4077-A5CA-D0DCF8B79777}'),
		"TimeHistoryWithFrame": (8004, 2, (8, 0), (), "TimeHistoryWithFrame", None),
		"UsePreStress": (8020, 2, (11, 0), (), "UsePreStress", None),
		"UseRecalculateRecovery": (8022, 2, (11, 0), (), "UseRecalculateRecovery", None),
	}
	_prop_map_put_ = {
		"AxialMode": ((8001, LCID, 4, 0),()),
		"ElementPatchSet": ((8003, LCID, 4, 0),()),
		"LifeCriteria": ((8002, LCID, 4, 0),()),
		"PreStressFile": ((8021, LCID, 4, 0),()),
		"TimeHistoryWithFrame": ((8004, LCID, 4, 0),()),
		"UsePreStress": ((8020, LCID, 4, 0),()),
		"UseRecalculateRecovery": ((8022, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityFatigueEvaluationSafetyFactor(DispatchBaseClass):
	'''Durability Fatigue Evaluation - Safety Factor'''
	CLSID = IID('{CDBAEBAA-5287-4F55-A6A4-7AA213D3D045}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_LifeCriterion(self):
		return self._ApplyTypes_(*(8001, 2, (3, 0), (), "LifeCriterion", '{BBA71A70-E454-4404-89B8-2D32905D5BA0}'))
	def _get_SearchingIncrement(self):
		return self._ApplyTypes_(*(8002, 2, (3, 0), (), "SearchingIncrement", '{F51B4542-080C-40A0-A728-866A4277B746}'))

	def _set_LifeCriterion(self, value):
		if "LifeCriterion" in self.__dict__: self.__dict__["LifeCriterion"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_SearchingIncrement(self, value):
		if "SearchingIncrement" in self.__dict__: self.__dict__["SearchingIncrement"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))

	LifeCriterion = property(_get_LifeCriterion, _set_LifeCriterion)
	'''
	Life Criterion

	:type: recurdyn.Durability.SafetyFactorLifeCriterion
	'''
	SearchingIncrement = property(_get_SearchingIncrement, _set_SearchingIncrement)
	'''
	Searching Increment

	:type: recurdyn.Durability.SearchingIncrement
	'''

	_prop_map_set_function_ = {
		"_set_LifeCriterion": _set_LifeCriterion,
		"_set_SearchingIncrement": _set_SearchingIncrement,
	}
	_prop_map_get_ = {
		"LifeCriterion": (8001, 2, (3, 0), (), "LifeCriterion", '{BBA71A70-E454-4404-89B8-2D32905D5BA0}'),
		"SearchingIncrement": (8002, 2, (3, 0), (), "SearchingIncrement", '{F51B4542-080C-40A0-A728-866A4277B746}'),
	}
	_prop_map_put_ = {
		"LifeCriterion": ((8001, LCID, 4, 0),()),
		"SearchingIncrement": ((8002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityFatigueEvaluationStrain(DispatchBaseClass):
	'''Durability Fatigue Evaluation - Strain'''
	CLSID = IID('{EBA808F3-9FD8-4375-BD38-F71DFB281AC8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_LifeCriterion(self):
		return self._ApplyTypes_(*(8001, 2, (3, 0), (), "LifeCriterion", '{1EE81CCA-D047-413E-A40C-5A3697D3BDA9}'))
	def _get_SearchingIncrement(self):
		return self._ApplyTypes_(*(8002, 2, (3, 0), (), "SearchingIncrement", '{F51B4542-080C-40A0-A728-866A4277B746}'))

	def _set_LifeCriterion(self, value):
		if "LifeCriterion" in self.__dict__: self.__dict__["LifeCriterion"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_SearchingIncrement(self, value):
		if "SearchingIncrement" in self.__dict__: self.__dict__["SearchingIncrement"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))

	LifeCriterion = property(_get_LifeCriterion, _set_LifeCriterion)
	'''
	Life Criterion

	:type: recurdyn.Durability.StrainLifeCriterion
	'''
	SearchingIncrement = property(_get_SearchingIncrement, _set_SearchingIncrement)
	'''
	Searching Increment

	:type: recurdyn.Durability.SearchingIncrement
	'''

	_prop_map_set_function_ = {
		"_set_LifeCriterion": _set_LifeCriterion,
		"_set_SearchingIncrement": _set_SearchingIncrement,
	}
	_prop_map_get_ = {
		"LifeCriterion": (8001, 2, (3, 0), (), "LifeCriterion", '{1EE81CCA-D047-413E-A40C-5A3697D3BDA9}'),
		"SearchingIncrement": (8002, 2, (3, 0), (), "SearchingIncrement", '{F51B4542-080C-40A0-A728-866A4277B746}'),
	}
	_prop_map_put_ = {
		"LifeCriterion": ((8001, LCID, 4, 0),()),
		"SearchingIncrement": ((8002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityFatigueEvaluationStress(DispatchBaseClass):
	'''Durability Fatigue Evaluation - Stress'''
	CLSID = IID('{40E8C43D-5AF9-44F9-80F5-F8FB9984879A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BWI_Weld(self):
		return self._ApplyTypes_(*(8004, 2, (3, 0), (), "BWI_Weld", '{2641C3C4-9436-4478-9EF6-FB0C91418A99}'))
	def _get_LifeCriterion(self):
		return self._ApplyTypes_(*(8001, 2, (3, 0), (), "LifeCriterion", '{BC43CC93-88BE-4D8E-8972-F22079EBF557}'))
	def _get_MeanStressEffect(self):
		return self._ApplyTypes_(*(8002, 2, (3, 0), (), "MeanStressEffect", '{F03AC2EC-9F4A-4F9F-B348-885C50164629}'))
	def _get_NumofStdDeviations(self):
		return self._ApplyTypes_(*(8005, 2, (9, 0), (), "NumofStdDeviations", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SearchingIncrement(self):
		return self._ApplyTypes_(*(8003, 2, (3, 0), (), "SearchingIncrement", '{F51B4542-080C-40A0-A728-866A4277B746}'))

	def _set_BWI_Weld(self, value):
		if "BWI_Weld" in self.__dict__: self.__dict__["BWI_Weld"] = value; return
		self._oleobj_.Invoke(*((8004, LCID, 4, 0) + (value,) + ()))
	def _set_LifeCriterion(self, value):
		if "LifeCriterion" in self.__dict__: self.__dict__["LifeCriterion"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_MeanStressEffect(self, value):
		if "MeanStressEffect" in self.__dict__: self.__dict__["MeanStressEffect"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))
	def _set_SearchingIncrement(self, value):
		if "SearchingIncrement" in self.__dict__: self.__dict__["SearchingIncrement"] = value; return
		self._oleobj_.Invoke(*((8003, LCID, 4, 0) + (value,) + ()))

	BWI_Weld = property(_get_BWI_Weld, _set_BWI_Weld)
	'''
	BWI Weld Type

	:type: recurdyn.Durability.BWIWeldType
	'''
	LifeCriterion = property(_get_LifeCriterion, _set_LifeCriterion)
	'''
	Life Criterion

	:type: recurdyn.Durability.StressLifeCriterion
	'''
	MeanStressEffect = property(_get_MeanStressEffect, _set_MeanStressEffect)
	'''
	Mean Stress Effect

	:type: recurdyn.Durability.MeanStressEffectType
	'''
	NumofStdDeviations = property(_get_NumofStdDeviations, None)
	'''
	Number of Std. Deviations

	:type: recurdyn.ProcessNet.IDouble
	'''
	SearchingIncrement = property(_get_SearchingIncrement, _set_SearchingIncrement)
	'''
	Searching Increment

	:type: recurdyn.Durability.SearchingIncrement
	'''

	_prop_map_set_function_ = {
		"_set_BWI_Weld": _set_BWI_Weld,
		"_set_LifeCriterion": _set_LifeCriterion,
		"_set_MeanStressEffect": _set_MeanStressEffect,
		"_set_SearchingIncrement": _set_SearchingIncrement,
	}
	_prop_map_get_ = {
		"BWI_Weld": (8004, 2, (3, 0), (), "BWI_Weld", '{2641C3C4-9436-4478-9EF6-FB0C91418A99}'),
		"LifeCriterion": (8001, 2, (3, 0), (), "LifeCriterion", '{BC43CC93-88BE-4D8E-8972-F22079EBF557}'),
		"MeanStressEffect": (8002, 2, (3, 0), (), "MeanStressEffect", '{F03AC2EC-9F4A-4F9F-B348-885C50164629}'),
		"NumofStdDeviations": (8005, 2, (9, 0), (), "NumofStdDeviations", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SearchingIncrement": (8003, 2, (3, 0), (), "SearchingIncrement", '{F51B4542-080C-40A0-A728-866A4277B746}'),
	}
	_prop_map_put_ = {
		"BWI_Weld": ((8004, LCID, 4, 0),()),
		"LifeCriterion": ((8001, LCID, 4, 0),()),
		"MeanStressEffect": ((8002, LCID, 4, 0),()),
		"SearchingIncrement": ((8003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityFatigueMaterial(DispatchBaseClass):
	'''Durability Fatigue Evaluation - Material'''
	CLSID = IID('{6E70D029-92E7-453A-81C7-8BC9727DCB8D}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ActiveMaterial(self):
		return self._ApplyTypes_(*(8002, 2, (8, 0), (), "ActiveMaterial", None))
	def _get_FileName(self):
		return self._ApplyTypes_(*(8001, 2, (8, 0), (), "FileName", None))
	def _get_Unit(self):
		return self._ApplyTypes_(*(8003, 2, (3, 0), (), "Unit", '{561AC3A1-F874-4089-8323-F64321CEA45D}'))
	def _get_UserDefined(self):
		return self._ApplyTypes_(*(8004, 2, (9, 0), (), "UserDefined", '{0006C001-A16E-4571-8402-A7589467302D}'))

	def _set_ActiveMaterial(self, value):
		if "ActiveMaterial" in self.__dict__: self.__dict__["ActiveMaterial"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))
	def _set_FileName(self, value):
		if "FileName" in self.__dict__: self.__dict__["FileName"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_Unit(self, value):
		if "Unit" in self.__dict__: self.__dict__["Unit"] = value; return
		self._oleobj_.Invoke(*((8003, LCID, 4, 0) + (value,) + ()))

	ActiveMaterial = property(_get_ActiveMaterial, _set_ActiveMaterial)
	'''
	Active Material Name

	:type: str
	'''
	FileName = property(_get_FileName, _set_FileName)
	'''
	Material XML File Name

	:type: str
	'''
	Unit = property(_get_Unit, _set_Unit)
	'''
	Material Unit Type

	:type: recurdyn.Durability.FatigueMaterialUnitType
	'''
	UserDefined = property(_get_UserDefined, None)
	'''
	Get User Defined Material

	:type: recurdyn.Durability.IDurabilityFatigueMaterialUserDefined
	'''

	_prop_map_set_function_ = {
		"_set_ActiveMaterial": _set_ActiveMaterial,
		"_set_FileName": _set_FileName,
		"_set_Unit": _set_Unit,
	}
	_prop_map_get_ = {
		"ActiveMaterial": (8002, 2, (8, 0), (), "ActiveMaterial", None),
		"FileName": (8001, 2, (8, 0), (), "FileName", None),
		"Unit": (8003, 2, (3, 0), (), "Unit", '{561AC3A1-F874-4089-8323-F64321CEA45D}'),
		"UserDefined": (8004, 2, (9, 0), (), "UserDefined", '{0006C001-A16E-4571-8402-A7589467302D}'),
	}
	_prop_map_put_ = {
		"ActiveMaterial": ((8002, LCID, 4, 0),()),
		"FileName": ((8001, LCID, 4, 0),()),
		"Unit": ((8003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityFatigueMaterialUserDefined(DispatchBaseClass):
	'''Durability Fatigue Evaluation - User Defined Material'''
	CLSID = IID('{0006C001-A16E-4571-8402-A7589467302D}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Export(self, path, OverWrite):
		'''
		Export method
		
		:param path: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(8004, LCID, 1, (24, 0), ((8, 1), (11, 1)),path
			, OverWrite)


	def Import(self, path):
		'''
		Import method
		
		:param path: str
		'''
		return self._oleobj_.InvokeTypes(8003, LCID, 1, (24, 0), ((8, 1),),path
			)


	def _get_Amplitude(self):
		return self._ApplyTypes_(*(8002, 2, (8197, 0), (), "Amplitude", None))
	def _get_CycleToFailure(self):
		return self._ApplyTypes_(*(8001, 2, (8197, 0), (), "CycleToFailure", None))
	def _get_InterpolationType(self):
		return self._ApplyTypes_(*(8008, 2, (3, 0), (), "InterpolationType", '{AC6533BB-7A3B-42EE-9141-3B2A7B8FB819}'))
	def _get_StrengthCoefficient(self):
		return self._ApplyTypes_(*(8007, 2, (9, 0), (), "StrengthCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UltimateStrength(self):
		return self._ApplyTypes_(*(8006, 2, (9, 0), (), "UltimateStrength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YieldStress(self):
		return self._ApplyTypes_(*(8005, 2, (9, 0), (), "YieldStress", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Amplitude(self, value):
		if "Amplitude" in self.__dict__: self.__dict__["Amplitude"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (variantValue,) + ()))
	def _set_CycleToFailure(self, value):
		if "CycleToFailure" in self.__dict__: self.__dict__["CycleToFailure"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (variantValue,) + ()))
	def _set_InterpolationType(self, value):
		if "InterpolationType" in self.__dict__: self.__dict__["InterpolationType"] = value; return
		self._oleobj_.Invoke(*((8008, LCID, 4, 0) + (value,) + ()))

	Amplitude = property(_get_Amplitude, _set_Amplitude)
	'''
	Amplitude

	:type: list[float]
	'''
	CycleToFailure = property(_get_CycleToFailure, _set_CycleToFailure)
	'''
	Cycle to Failure

	:type: list[float]
	'''
	InterpolationType = property(_get_InterpolationType, _set_InterpolationType)
	'''
	User Defined Interpolation Type

	:type: recurdyn.Durability.UserDefinedInterpolationType
	'''
	StrengthCoefficient = property(_get_StrengthCoefficient, None)
	'''
	Strength Coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	UltimateStrength = property(_get_UltimateStrength, None)
	'''
	Ultimate Strength

	:type: recurdyn.ProcessNet.IDouble
	'''
	YieldStress = property(_get_YieldStress, None)
	'''
	Yield Stress

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Amplitude": _set_Amplitude,
		"_set_CycleToFailure": _set_CycleToFailure,
		"_set_InterpolationType": _set_InterpolationType,
	}
	_prop_map_get_ = {
		"Amplitude": (8002, 2, (8197, 0), (), "Amplitude", None),
		"CycleToFailure": (8001, 2, (8197, 0), (), "CycleToFailure", None),
		"InterpolationType": (8008, 2, (3, 0), (), "InterpolationType", '{AC6533BB-7A3B-42EE-9141-3B2A7B8FB819}'),
		"StrengthCoefficient": (8007, 2, (9, 0), (), "StrengthCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UltimateStrength": (8006, 2, (9, 0), (), "UltimateStrength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YieldStress": (8005, 2, (9, 0), (), "YieldStress", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Amplitude": ((8002, LCID, 4, 0),()),
		"CycleToFailure": ((8001, LCID, 4, 0),()),
		"InterpolationType": ((8008, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityFatigueResult(DispatchBaseClass):
	'''Durability Fatigue Evaluation - Result'''
	CLSID = IID('{AA1358DD-7933-4CFE-B738-AFB37F0C0D0E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def MeanStressList(self, timeHist):
		'''
		Mean stress list
		
		:param timeHist: str
		:rtype: list[float]
		'''
		return self._ApplyTypes_(8010, 1, (8197, 0), ((8, 1),), 'MeanStressList', None,timeHist
			)


	def StressAmplitudeList(self, timeHist):
		'''
		Stress amplitude list
		
		:param timeHist: str
		:rtype: list[float]
		'''
		return self._ApplyTypes_(8011, 1, (8197, 0), ((8, 1),), 'StressAmplitudeList', None,timeHist
			)


	def _get_Damage(self):
		return self._ApplyTypes_(*(8002, 2, (5, 0), (), "Damage", None))
	def _get_DamageList(self):
		return self._ApplyTypes_(*(8006, 2, (8197, 0), (), "DamageList", None))
	def _get_FaceNodeIDs(self):
		return self._ApplyTypes_(*(8001, 2, (8, 0), (), "FaceNodeIDs", None))
	def _get_FaceNodeIDsList(self):
		return self._ApplyTypes_(*(8005, 2, (8200, 0), (), "FaceNodeIDsList", None))
	def _get_Life(self):
		return self._ApplyTypes_(*(8003, 2, (5, 0), (), "Life", None))
	def _get_LifeList(self):
		return self._ApplyTypes_(*(8007, 2, (8197, 0), (), "LifeList", None))
	def _get_SafetyFactor(self):
		return self._ApplyTypes_(*(8004, 2, (5, 0), (), "SafetyFactor", None))
	def _get_SafetyFactorList(self):
		return self._ApplyTypes_(*(8008, 2, (8197, 0), (), "SafetyFactorList", None))
	def _get_TimeHistoryNameList(self):
		return self._ApplyTypes_(*(8009, 2, (8200, 0), (), "TimeHistoryNameList", None))

	Damage = property(_get_Damage, None)
	'''
	Damage

	:type: float
	'''
	DamageList = property(_get_DamageList, None)
	'''
	Damage list

	:type: list[float]
	'''
	FaceNodeIDs = property(_get_FaceNodeIDs, None)
	'''
	Face Node IDs

	:type: str
	'''
	FaceNodeIDsList = property(_get_FaceNodeIDsList, None)
	'''
	Face Node IDs list

	:type: list[str]
	'''
	Life = property(_get_Life, None)
	'''
	Life

	:type: float
	'''
	LifeList = property(_get_LifeList, None)
	'''
	Life list

	:type: list[float]
	'''
	SafetyFactor = property(_get_SafetyFactor, None)
	'''
	Safety Factor

	:type: float
	'''
	SafetyFactorList = property(_get_SafetyFactorList, None)
	'''
	Safety Factor list

	:type: list[float]
	'''
	TimeHistoryNameList = property(_get_TimeHistoryNameList, None)
	'''
	TimeHistory Name list

	:type: list[str]
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Damage": (8002, 2, (5, 0), (), "Damage", None),
		"DamageList": (8006, 2, (8197, 0), (), "DamageList", None),
		"FaceNodeIDs": (8001, 2, (8, 0), (), "FaceNodeIDs", None),
		"FaceNodeIDsList": (8005, 2, (8200, 0), (), "FaceNodeIDsList", None),
		"Life": (8003, 2, (5, 0), (), "Life", None),
		"LifeList": (8007, 2, (8197, 0), (), "LifeList", None),
		"SafetyFactor": (8004, 2, (5, 0), (), "SafetyFactor", None),
		"SafetyFactorList": (8008, 2, (8197, 0), (), "SafetyFactorList", None),
		"TimeHistoryNameList": (8009, 2, (8200, 0), (), "TimeHistoryNameList", None),
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

class IDurabilityPlotOriginalHistory(DispatchBaseClass):
	'''Durability Fatigue Evaluation - Plot Original History'''
	CLSID = IID('{1B06AC13-47EA-4070-A4FD-CE5E341F2650}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AngleType(self):
		return self._ApplyTypes_(*(8004, 2, (3, 0), (), "AngleType", '{410F001D-4B12-4AAD-830C-9474DC21B470}'))
	def _get_LocationType(self):
		return self._ApplyTypes_(*(8001, 2, (3, 0), (), "LocationType", '{160F26E6-0856-48A7-A4EB-61C549192B1B}'))
	def _get_UserDefinedAngle(self):
		return self._ApplyTypes_(*(8005, 2, (5, 0), (), "UserDefinedAngle", None))
	def _get_UserDefinedPatchIndex(self):
		return self._ApplyTypes_(*(8002, 2, (3, 0), (), "UserDefinedPatchIndex", None))

	def _set_AngleType(self, value):
		if "AngleType" in self.__dict__: self.__dict__["AngleType"] = value; return
		self._oleobj_.Invoke(*((8004, LCID, 4, 0) + (value,) + ()))
	def _set_LocationType(self, value):
		if "LocationType" in self.__dict__: self.__dict__["LocationType"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_TimeHistoryName(self, value):
		if "TimeHistoryName" in self.__dict__: self.__dict__["TimeHistoryName"] = value; return
		self._oleobj_.Invoke(*((8003, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedAngle(self, value):
		if "UserDefinedAngle" in self.__dict__: self.__dict__["UserDefinedAngle"] = value; return
		self._oleobj_.Invoke(*((8005, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedPatchIndex(self, value):
		if "UserDefinedPatchIndex" in self.__dict__: self.__dict__["UserDefinedPatchIndex"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))

	AngleType = property(_get_AngleType, _set_AngleType)
	'''
	Angle Type

	:type: recurdyn.Durability.AngleType
	'''
	LocationType = property(_get_LocationType, _set_LocationType)
	'''
	LocationType

	:type: recurdyn.Durability.PatchLocationType
	'''
	UserDefinedAngle = property(_get_UserDefinedAngle, _set_UserDefinedAngle)
	'''
	User Defined Angle (Degree)

	:type: float
	'''
	UserDefinedPatchIndex = property(_get_UserDefinedPatchIndex, _set_UserDefinedPatchIndex)
	'''
	User Defined Patch Index

	:type: int
	'''
	TimeHistoryName = property(None, _set_TimeHistoryName)
	'''
	TimeHistory Name

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_AngleType": _set_AngleType,
		"_set_LocationType": _set_LocationType,
		"_set_TimeHistoryName": _set_TimeHistoryName,
		"_set_UserDefinedAngle": _set_UserDefinedAngle,
		"_set_UserDefinedPatchIndex": _set_UserDefinedPatchIndex,
	}
	_prop_map_get_ = {
		"AngleType": (8004, 2, (3, 0), (), "AngleType", '{410F001D-4B12-4AAD-830C-9474DC21B470}'),
		"LocationType": (8001, 2, (3, 0), (), "LocationType", '{160F26E6-0856-48A7-A4EB-61C549192B1B}'),
		"UserDefinedAngle": (8005, 2, (5, 0), (), "UserDefinedAngle", None),
		"UserDefinedPatchIndex": (8002, 2, (3, 0), (), "UserDefinedPatchIndex", None),
	}
	_prop_map_put_ = {
		"AngleType": ((8004, LCID, 4, 0),()),
		"LocationType": ((8001, LCID, 4, 0),()),
		"TimeHistoryName": ((8003, LCID, 4, 0),()),
		"UserDefinedAngle": ((8005, LCID, 4, 0),()),
		"UserDefinedPatchIndex": ((8002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityPreStress(DispatchBaseClass):
	'''Durability Pre-Stress'''
	CLSID = IID('{41015A8F-B86B-4D5A-9BAA-2D5CBE880191}')
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
		Execute method
		'''
		return self._oleobj_.InvokeTypes(8005, LCID, 1, (24, 0), (),)


	def _get_ElementPatchSet(self):
		return self._ApplyTypes_(*(8001, 2, (9, 0), (), "ElementPatchSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_InputFile(self):
		return self._ApplyTypes_(*(8003, 2, (8, 0), (), "InputFile", None))
	def _get_ReferenceMarker(self):
		return self._ApplyTypes_(*(8002, 2, (9, 0), (), "ReferenceMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_ResultFile(self):
		return self._ApplyTypes_(*(8004, 2, (8, 0), (), "ResultFile", None))

	def _set_ElementPatchSet(self, value):
		if "ElementPatchSet" in self.__dict__: self.__dict__["ElementPatchSet"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_InputFile(self, value):
		if "InputFile" in self.__dict__: self.__dict__["InputFile"] = value; return
		self._oleobj_.Invoke(*((8003, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceMarker(self, value):
		if "ReferenceMarker" in self.__dict__: self.__dict__["ReferenceMarker"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))
	def _set_ResultFile(self, value):
		if "ResultFile" in self.__dict__: self.__dict__["ResultFile"] = value; return
		self._oleobj_.Invoke(*((8004, LCID, 4, 0) + (value,) + ()))

	ElementPatchSet = property(_get_ElementPatchSet, _set_ElementPatchSet)
	'''
	Element/ Patch Set

	:type: recurdyn.ProcessNet.IGeneric
	'''
	InputFile = property(_get_InputFile, _set_InputFile)
	'''
	Input CSV file

	:type: str
	'''
	ReferenceMarker = property(_get_ReferenceMarker, _set_ReferenceMarker)
	'''
	Reference marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	ResultFile = property(_get_ResultFile, _set_ResultFile)
	'''
	Result DNSRD file

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ElementPatchSet": _set_ElementPatchSet,
		"_set_InputFile": _set_InputFile,
		"_set_ReferenceMarker": _set_ReferenceMarker,
		"_set_ResultFile": _set_ResultFile,
	}
	_prop_map_get_ = {
		"ElementPatchSet": (8001, 2, (9, 0), (), "ElementPatchSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"InputFile": (8003, 2, (8, 0), (), "InputFile", None),
		"ReferenceMarker": (8002, 2, (9, 0), (), "ReferenceMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"ResultFile": (8004, 2, (8, 0), (), "ResultFile", None),
	}
	_prop_map_put_ = {
		"ElementPatchSet": ((8001, LCID, 4, 0),()),
		"InputFile": ((8003, LCID, 4, 0),()),
		"ReferenceMarker": ((8002, LCID, 4, 0),()),
		"ResultFile": ((8004, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityPreference(DispatchBaseClass):
	'''Durability Preference'''
	CLSID = IID('{8D781640-3E0A-485F-920C-4338B86BEC54}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ConvergenceControl(self):
		return self._ApplyTypes_(*(8003, 2, (9, 0), (), "ConvergenceControl", '{60C11468-A82B-4AB4-9737-6946C4B5CA24}'))
	def _get_FatigueInfluencingFactors(self):
		return self._ApplyTypes_(*(8002, 2, (9, 0), (), "FatigueInfluencingFactors", '{AD378F84-F7A5-48B4-9A75-2C25A5D46125}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(8001, 2, (9, 0), (), "Material", '{B4393F58-156B-4530-87C6-7C1D325FBBEF}'))
	def _get_RainFlowCounting(self):
		return self._ApplyTypes_(*(8004, 2, (9, 0), (), "RainFlowCounting", '{190D59B5-5943-40C2-9890-AC8DF022BC7B}'))

	ConvergenceControl = property(_get_ConvergenceControl, None)
	'''
	Get Preference Convergence Control

	:type: recurdyn.Durability.IDurabilityPreferenceConvergenceControl
	'''
	FatigueInfluencingFactors = property(_get_FatigueInfluencingFactors, None)
	'''
	Get Preference Fatigue Influencing Factors

	:type: recurdyn.Durability.IDurabilityPreferenceFatigueInfluencingFactors
	'''
	Material = property(_get_Material, None)
	'''
	Get Preference Material

	:type: recurdyn.Durability.IDurabilityPreferenceMaterial
	'''
	RainFlowCounting = property(_get_RainFlowCounting, None)
	'''
	Get Preference Rainflow Counting

	:type: recurdyn.Durability.IDurabilityPreferenceRainflowCounting
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"ConvergenceControl": (8003, 2, (9, 0), (), "ConvergenceControl", '{60C11468-A82B-4AB4-9737-6946C4B5CA24}'),
		"FatigueInfluencingFactors": (8002, 2, (9, 0), (), "FatigueInfluencingFactors", '{AD378F84-F7A5-48B4-9A75-2C25A5D46125}'),
		"Material": (8001, 2, (9, 0), (), "Material", '{B4393F58-156B-4530-87C6-7C1D325FBBEF}'),
		"RainFlowCounting": (8004, 2, (9, 0), (), "RainFlowCounting", '{190D59B5-5943-40C2-9890-AC8DF022BC7B}'),
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

class IDurabilityPreferenceConvergenceControl(DispatchBaseClass):
	'''Durability Preference - Convergence Control'''
	CLSID = IID('{60C11468-A82B-4AB4-9737-6946C4B5CA24}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AbsoluteError(self):
		return self._ApplyTypes_(*(8053, 2, (9, 0), (), "AbsoluteError", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InitialValue(self):
		return self._ApplyTypes_(*(8052, 2, (9, 0), (), "InitialValue", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_MaxNumberIteration(self):
		return self._ApplyTypes_(*(8051, 2, (9, 0), (), "MaxNumberIteration", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	AbsoluteError = property(_get_AbsoluteError, None)
	'''
	Absolute Error

	:type: recurdyn.ProcessNet.IDouble
	'''
	InitialValue = property(_get_InitialValue, None)
	'''
	Inital Value

	:type: recurdyn.ProcessNet.IDouble
	'''
	MaxNumberIteration = property(_get_MaxNumberIteration, None)
	'''
	Max Number Iteration

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"AbsoluteError": (8053, 2, (9, 0), (), "AbsoluteError", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InitialValue": (8052, 2, (9, 0), (), "InitialValue", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"MaxNumberIteration": (8051, 2, (9, 0), (), "MaxNumberIteration", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IDurabilityPreferenceFatigueInfluencingFactors(DispatchBaseClass):
	'''Durability Preference - Fatigue Influencing Factors'''
	CLSID = IID('{AD378F84-F7A5-48B4-9A75-2C25A5D46125}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_LoadFactor(self):
		return self._ApplyTypes_(*(8053, 2, (9, 0), (), "LoadFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_NotchFactorAmp(self):
		return self._ApplyTypes_(*(8051, 2, (9, 0), (), "NotchFactorAmp", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_OtherFactor(self):
		return self._ApplyTypes_(*(8054, 2, (9, 0), (), "OtherFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ScaleFactor(self):
		return self._ApplyTypes_(*(8057, 2, (9, 0), (), "ScaleFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SizeFactor(self):
		return self._ApplyTypes_(*(8052, 2, (9, 0), (), "SizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SurfaceFactor(self):
		return self._ApplyTypes_(*(8055, 2, (9, 0), (), "SurfaceFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SurfaceFactorType(self):
		return self._ApplyTypes_(*(8056, 2, (3, 0), (), "SurfaceFactorType", '{C0A2D1B6-78D7-4011-A09C-B3ABFE9149CE}'))

	def _set_SurfaceFactorType(self, value):
		if "SurfaceFactorType" in self.__dict__: self.__dict__["SurfaceFactorType"] = value; return
		self._oleobj_.Invoke(*((8056, LCID, 4, 0) + (value,) + ()))

	LoadFactor = property(_get_LoadFactor, None)
	'''
	Load Factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	NotchFactorAmp = property(_get_NotchFactorAmp, None)
	'''
	Notch Factor Amp

	:type: recurdyn.ProcessNet.IDouble
	'''
	OtherFactor = property(_get_OtherFactor, None)
	'''
	Other Factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	ScaleFactor = property(_get_ScaleFactor, None)
	'''
	Scale Factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	SizeFactor = property(_get_SizeFactor, None)
	'''
	Size Factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	SurfaceFactor = property(_get_SurfaceFactor, None)
	'''
	Surface Factor

	:type: recurdyn.ProcessNet.IDouble
	'''
	SurfaceFactorType = property(_get_SurfaceFactorType, _set_SurfaceFactorType)
	'''
	Surface Factor type

	:type: recurdyn.Durability.FatigueSurfaceFactorType
	'''

	_prop_map_set_function_ = {
		"_set_SurfaceFactorType": _set_SurfaceFactorType,
	}
	_prop_map_get_ = {
		"LoadFactor": (8053, 2, (9, 0), (), "LoadFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"NotchFactorAmp": (8051, 2, (9, 0), (), "NotchFactorAmp", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"OtherFactor": (8054, 2, (9, 0), (), "OtherFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ScaleFactor": (8057, 2, (9, 0), (), "ScaleFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SizeFactor": (8052, 2, (9, 0), (), "SizeFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SurfaceFactor": (8055, 2, (9, 0), (), "SurfaceFactor", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SurfaceFactorType": (8056, 2, (3, 0), (), "SurfaceFactorType", '{C0A2D1B6-78D7-4011-A09C-B3ABFE9149CE}'),
	}
	_prop_map_put_ = {
		"SurfaceFactorType": ((8056, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityPreferenceMaterial(DispatchBaseClass):
	'''Durability Preference - Material'''
	CLSID = IID('{B4393F58-156B-4530-87C6-7C1D325FBBEF}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_LibraryPath(self):
		return self._ApplyTypes_(*(8051, 2, (8, 0), (), "LibraryPath", None))

	def _set_LibraryPath(self, value):
		if "LibraryPath" in self.__dict__: self.__dict__["LibraryPath"] = value; return
		self._oleobj_.Invoke(*((8051, LCID, 4, 0) + (value,) + ()))

	LibraryPath = property(_get_LibraryPath, _set_LibraryPath)
	'''
	Material Library Path

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_LibraryPath": _set_LibraryPath,
	}
	_prop_map_get_ = {
		"LibraryPath": (8051, 2, (8, 0), (), "LibraryPath", None),
	}
	_prop_map_put_ = {
		"LibraryPath": ((8051, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityPreferenceRainflowCounting(DispatchBaseClass):
	'''Durability Preference - RainFlow Counting'''
	CLSID = IID('{190D59B5-5943-40C2-9890-AC8DF022BC7B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_NumberRanges(self):
		return self._ApplyTypes_(*(8052, 2, (9, 0), (), "NumberRanges", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PeakValley(self):
		return self._ApplyTypes_(*(8051, 2, (9, 0), (), "PeakValley", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	NumberRanges = property(_get_NumberRanges, None)
	'''
	Number Ranges

	:type: recurdyn.ProcessNet.IDouble
	'''
	PeakValley = property(_get_PeakValley, None)
	'''
	Peak Valley

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"NumberRanges": (8052, 2, (9, 0), (), "NumberRanges", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PeakValley": (8051, 2, (9, 0), (), "PeakValley", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IDurabilityRainflowCounting(DispatchBaseClass):
	'''Durability Fatigue Evaluation - Rainflow Counting'''
	CLSID = IID('{5494C9D5-49B9-476D-A973-A5C524009AC9}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AngleType(self):
		return self._ApplyTypes_(*(8004, 2, (3, 0), (), "AngleType", '{410F001D-4B12-4AAD-830C-9474DC21B470}'))
	def _get_LocationType(self):
		return self._ApplyTypes_(*(8001, 2, (3, 0), (), "LocationType", '{160F26E6-0856-48A7-A4EB-61C549192B1B}'))
	def _get_UserDefinedAngle(self):
		return self._ApplyTypes_(*(8005, 2, (5, 0), (), "UserDefinedAngle", None))
	def _get_UserDefinedPatchIndex(self):
		return self._ApplyTypes_(*(8002, 2, (3, 0), (), "UserDefinedPatchIndex", None))

	def _set_AngleType(self, value):
		if "AngleType" in self.__dict__: self.__dict__["AngleType"] = value; return
		self._oleobj_.Invoke(*((8004, LCID, 4, 0) + (value,) + ()))
	def _set_LocationType(self, value):
		if "LocationType" in self.__dict__: self.__dict__["LocationType"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_TimeHistoryName(self, value):
		if "TimeHistoryName" in self.__dict__: self.__dict__["TimeHistoryName"] = value; return
		self._oleobj_.Invoke(*((8003, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedAngle(self, value):
		if "UserDefinedAngle" in self.__dict__: self.__dict__["UserDefinedAngle"] = value; return
		self._oleobj_.Invoke(*((8005, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedPatchIndex(self, value):
		if "UserDefinedPatchIndex" in self.__dict__: self.__dict__["UserDefinedPatchIndex"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))

	AngleType = property(_get_AngleType, _set_AngleType)
	'''
	Angle Type

	:type: recurdyn.Durability.AngleType
	'''
	LocationType = property(_get_LocationType, _set_LocationType)
	'''
	LocationType

	:type: recurdyn.Durability.PatchLocationType
	'''
	UserDefinedAngle = property(_get_UserDefinedAngle, _set_UserDefinedAngle)
	'''
	User Defined Angle (Degree)

	:type: float
	'''
	UserDefinedPatchIndex = property(_get_UserDefinedPatchIndex, _set_UserDefinedPatchIndex)
	'''
	User Defined Patch Index

	:type: int
	'''
	TimeHistoryName = property(None, _set_TimeHistoryName)
	'''
	TimeHistory Name

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_AngleType": _set_AngleType,
		"_set_LocationType": _set_LocationType,
		"_set_TimeHistoryName": _set_TimeHistoryName,
		"_set_UserDefinedAngle": _set_UserDefinedAngle,
		"_set_UserDefinedPatchIndex": _set_UserDefinedPatchIndex,
	}
	_prop_map_get_ = {
		"AngleType": (8004, 2, (3, 0), (), "AngleType", '{410F001D-4B12-4AAD-830C-9474DC21B470}'),
		"LocationType": (8001, 2, (3, 0), (), "LocationType", '{160F26E6-0856-48A7-A4EB-61C549192B1B}'),
		"UserDefinedAngle": (8005, 2, (5, 0), (), "UserDefinedAngle", None),
		"UserDefinedPatchIndex": (8002, 2, (3, 0), (), "UserDefinedPatchIndex", None),
	}
	_prop_map_put_ = {
		"AngleType": ((8004, LCID, 4, 0),()),
		"LocationType": ((8001, LCID, 4, 0),()),
		"TimeHistoryName": ((8003, LCID, 4, 0),()),
		"UserDefinedAngle": ((8005, LCID, 4, 0),()),
		"UserDefinedPatchIndex": ((8002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilitySpecificAngleCalculationOption(DispatchBaseClass):
	'''Durability Fatigue Evaluation - Specific Angle Calculation Option'''
	CLSID = IID('{4D1AEBE0-9522-4D83-B1E9-784161452107}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AngleType(self):
		return self._ApplyTypes_(*(8004, 2, (3, 0), (), "AngleType", '{410F001D-4B12-4AAD-830C-9474DC21B470}'))
	def _get_LocationType(self):
		return self._ApplyTypes_(*(8002, 2, (3, 0), (), "LocationType", '{160F26E6-0856-48A7-A4EB-61C549192B1B}'))
	def _get_UserDefinedAngle(self):
		return self._ApplyTypes_(*(8005, 2, (5, 0), (), "UserDefinedAngle", None))
	def _get_UserDefinedPatchIndex(self):
		return self._ApplyTypes_(*(8003, 2, (3, 0), (), "UserDefinedPatchIndex", None))

	def _set_AngleType(self, value):
		if "AngleType" in self.__dict__: self.__dict__["AngleType"] = value; return
		self._oleobj_.Invoke(*((8004, LCID, 4, 0) + (value,) + ()))
	def _set_LocationType(self, value):
		if "LocationType" in self.__dict__: self.__dict__["LocationType"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))
	def _set_TimeHistoryName(self, value):
		if "TimeHistoryName" in self.__dict__: self.__dict__["TimeHistoryName"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedAngle(self, value):
		if "UserDefinedAngle" in self.__dict__: self.__dict__["UserDefinedAngle"] = value; return
		self._oleobj_.Invoke(*((8005, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedPatchIndex(self, value):
		if "UserDefinedPatchIndex" in self.__dict__: self.__dict__["UserDefinedPatchIndex"] = value; return
		self._oleobj_.Invoke(*((8003, LCID, 4, 0) + (value,) + ()))

	AngleType = property(_get_AngleType, _set_AngleType)
	'''
	Angle Type

	:type: recurdyn.Durability.AngleType
	'''
	LocationType = property(_get_LocationType, _set_LocationType)
	'''
	Patch Location Type

	:type: recurdyn.Durability.PatchLocationType
	'''
	UserDefinedAngle = property(_get_UserDefinedAngle, _set_UserDefinedAngle)
	'''
	User Defined Angle (Degree)

	:type: float
	'''
	UserDefinedPatchIndex = property(_get_UserDefinedPatchIndex, _set_UserDefinedPatchIndex)
	'''
	User Defined Patch Index

	:type: int
	'''
	TimeHistoryName = property(None, _set_TimeHistoryName)
	'''
	TimeHistory Name

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_AngleType": _set_AngleType,
		"_set_LocationType": _set_LocationType,
		"_set_TimeHistoryName": _set_TimeHistoryName,
		"_set_UserDefinedAngle": _set_UserDefinedAngle,
		"_set_UserDefinedPatchIndex": _set_UserDefinedPatchIndex,
	}
	_prop_map_get_ = {
		"AngleType": (8004, 2, (3, 0), (), "AngleType", '{410F001D-4B12-4AAD-830C-9474DC21B470}'),
		"LocationType": (8002, 2, (3, 0), (), "LocationType", '{160F26E6-0856-48A7-A4EB-61C549192B1B}'),
		"UserDefinedAngle": (8005, 2, (5, 0), (), "UserDefinedAngle", None),
		"UserDefinedPatchIndex": (8003, 2, (3, 0), (), "UserDefinedPatchIndex", None),
	}
	_prop_map_put_ = {
		"AngleType": ((8004, LCID, 4, 0),()),
		"LocationType": ((8002, LCID, 4, 0),()),
		"TimeHistoryName": ((8001, LCID, 4, 0),()),
		"UserDefinedAngle": ((8005, LCID, 4, 0),()),
		"UserDefinedPatchIndex": ((8003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilitySpecificAngleCalculationResult(DispatchBaseClass):
	'''Durability Fatigue Evaluation - Specific Angle Calculation Result'''
	CLSID = IID('{20342F66-B448-4E67-8C28-3C74142E38C2}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Damage(self):
		return self._ApplyTypes_(*(8001, 2, (5, 0), (), "Damage", None))
	def _get_Life(self):
		return self._ApplyTypes_(*(8002, 2, (5, 0), (), "Life", None))
	def _get_SafetyFactor(self):
		return self._ApplyTypes_(*(8003, 2, (5, 0), (), "SafetyFactor", None))

	Damage = property(_get_Damage, None)
	'''
	Damage

	:type: float
	'''
	Life = property(_get_Life, None)
	'''
	Life

	:type: float
	'''
	SafetyFactor = property(_get_SafetyFactor, None)
	'''
	Safety Factor

	:type: float
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Damage": (8001, 2, (5, 0), (), "Damage", None),
		"Life": (8002, 2, (5, 0), (), "Life", None),
		"SafetyFactor": (8003, 2, (5, 0), (), "SafetyFactor", None),
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

class IDurabilityTimeHistory(DispatchBaseClass):
	'''IDurabilityTimeHistory'''
	CLSID = IID('{BA1DD446-7C44-42A8-B7D5-99667FC088F6}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_FrameRange(self):
		return self._ApplyTypes_(*(8003, 2, (8, 0), (), "FrameRange", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(8002, 2, (8, 0), (), "Name", None))
	def _get_UseTimeHistory(self):
		return self._ApplyTypes_(*(8001, 2, (11, 0), (), "UseTimeHistory", None))

	def _set_FrameRange(self, value):
		if "FrameRange" in self.__dict__: self.__dict__["FrameRange"] = value; return
		self._oleobj_.Invoke(*((8003, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((8002, LCID, 4, 0) + (value,) + ()))
	def _set_UseTimeHistory(self, value):
		if "UseTimeHistory" in self.__dict__: self.__dict__["UseTimeHistory"] = value; return
		self._oleobj_.Invoke(*((8001, LCID, 4, 0) + (value,) + ()))

	FrameRange = property(_get_FrameRange, _set_FrameRange)
	'''
	Time Range

	:type: str
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	UseTimeHistory = property(_get_UseTimeHistory, _set_UseTimeHistory)
	'''
	Use

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_FrameRange": _set_FrameRange,
		"_set_Name": _set_Name,
		"_set_UseTimeHistory": _set_UseTimeHistory,
	}
	_prop_map_get_ = {
		"FrameRange": (8003, 2, (8, 0), (), "FrameRange", None),
		"Name": (8002, 2, (8, 0), (), "Name", None),
		"UseTimeHistory": (8001, 2, (11, 0), (), "UseTimeHistory", None),
	}
	_prop_map_put_ = {
		"FrameRange": ((8003, LCID, 4, 0),()),
		"Name": ((8002, LCID, 4, 0),()),
		"UseTimeHistory": ((8001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDurabilityTimeHistoryCollection(DispatchBaseClass):
	'''IDurabilityTimeHistoryCollection'''
	CLSID = IID('{0FC6C5F7-150B-4077-A5CA-D0DCF8B79777}')
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
		:rtype: recurdyn.Durability.IDurabilityTimeHistory
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{BA1DD446-7C44-42A8-B7D5-99667FC088F6}')
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
		:rtype: recurdyn.Durability.IDurabilityTimeHistory
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{BA1DD446-7C44-42A8-B7D5-99667FC088F6}')
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
		return win32com.client.util.Iterator(ob, '{BA1DD446-7C44-42A8-B7D5-99667FC088F6}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{BA1DD446-7C44-42A8-B7D5-99667FC088F6}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IDurabilityToolkit(DispatchBaseClass):
	'''Durability Toolkit'''
	CLSID = IID('{8B1BCD31-C01E-4B81-8A52-E4533BEE9F10}')
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
	def _get_Contour(self):
		return self._ApplyTypes_(*(8003, 2, (9, 0), (), "Contour", '{A7CCAFA8-34D0-4D9E-97F9-F92C15E19BAB}'))
	def _get_FatigueEvaluation(self):
		return self._ApplyTypes_(*(8002, 2, (9, 0), (), "FatigueEvaluation", '{D65A4952-C3CE-42F4-A6F2-D7DEBEF72EC0}'))
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
	def _get_PreStress(self):
		return self._ApplyTypes_(*(8004, 2, (9, 0), (), "PreStress", '{41015A8F-B86B-4D5A-9BAA-2D5CBE880191}'))
	def _get_Preference(self):
		return self._ApplyTypes_(*(8001, 2, (9, 0), (), "Preference", '{8D781640-3E0A-485F-920C-4338B86BEC54}'))
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
	Contour = property(_get_Contour, None)
	'''
	Get Contour

	:type: recurdyn.Durability.IDurabilityContour
	'''
	FatigueEvaluation = property(_get_FatigueEvaluation, None)
	'''
	Get Fatigue Evaluation

	:type: recurdyn.Durability.IDurabilityFatigueEvaluation
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
	PreStress = property(_get_PreStress, None)
	'''
	Get Contour

	:type: recurdyn.Durability.IDurabilityPreStress
	'''
	Preference = property(_get_Preference, None)
	'''
	Get Preference

	:type: recurdyn.Durability.IDurabilityPreference
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
		"Contour": (8003, 2, (9, 0), (), "Contour", '{A7CCAFA8-34D0-4D9E-97F9-F92C15E19BAB}'),
		"FatigueEvaluation": (8002, 2, (9, 0), (), "FatigueEvaluation", '{D65A4952-C3CE-42F4-A6F2-D7DEBEF72EC0}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PreStress": (8004, 2, (9, 0), (), "PreStress", '{41015A8F-B86B-4D5A-9BAA-2D5CBE880191}'),
		"Preference": (8001, 2, (9, 0), (), "Preference", '{8D781640-3E0A-485F-920C-4338B86BEC54}'),
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

IDurabilityContour_vtables_dispatch_ = 1
IDurabilityContour_vtables_ = [
	(( 'OptionType' , 'pVal' , ), 8001, (8001, (), [ (3, 1, None, "IID('{F2BAAF75-AFB8-4C6B-8CD5-6D51760DE479}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'OptionType' , 'pVal' , ), 8001, (8001, (), [ (16387, 10, None, "IID('{F2BAAF75-AFB8-4C6B-8CD5-6D51760DE479}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BandOption' , 'ppVal' , ), 8002, (8002, (), [ (16393, 10, None, "IID('{1877A27A-16EC-492A-B121-2158CA766380}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MinMaxOption' , 'ppVal' , ), 8003, (8003, (), [ (16393, 10, None, "IID('{02902C9C-2767-4E11-A750-6AFDF9F1386B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StyleOption' , 'ppVal' , ), 8004, (8004, (), [ (16393, 10, None, "IID('{AD4A1D92-5D4B-47CA-BD19-CDBA4567BB11}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ContourView' , ), 8005, (8005, (), [ ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ExportContourData' , 'Val' , ), 8006, (8006, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TimeHistoryIndex' , ), 8007, (8007, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ViewType' , 'pVal' , ), 8008, (8008, (), [ (3, 1, None, "IID('{0DF9B5BF-ABCC-4F55-B059-ADF6739F936F}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ViewType' , 'pVal' , ), 8008, (8008, (), [ (16387, 10, None, "IID('{0DF9B5BF-ABCC-4F55-B059-ADF6739F936F}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ProbeOption' , 'ppVal' , ), 8009, (8009, (), [ (16393, 10, None, "IID('{3707C188-79DF-4DC1-9F29-6DF34660C998}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ExportContourDataWithNodeSet' , 'Val' , 'pVal' , ), 8010, (8010, (), [ (8, 1, None, None) , 
			 (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'RecoveryType' , 'enumType' , ), 8011, (8011, (), [ (3, 1, None, "IID('{B25FC8C8-6CB0-48D7-84B9-0233923E9B4A}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'RecoveryType' , 'enumType' , ), 8011, (8011, (), [ (16387, 10, None, "IID('{B25FC8C8-6CB0-48D7-84B9-0233923E9B4A}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IDurabilityContourBandOption_vtables_dispatch_ = 1
IDurabilityContourBandOption_vtables_ = [
	(( 'LegendType' , 'pVal' , ), 8051, (8051, (), [ (3, 1, None, "IID('{98CEF211-B3D9-487F-AD57-B46FFDCE1E8E}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LegendType' , 'pVal' , ), 8051, (8051, (), [ (16387, 10, None, "IID('{98CEF211-B3D9-487F-AD57-B46FFDCE1E8E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LegendLocation' , 'pVal' , ), 8052, (8052, (), [ (3, 1, None, "IID('{962D1C1A-1074-4306-BEAE-9EA10A4D2D6E}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LegendLocation' , 'pVal' , ), 8052, (8052, (), [ (16387, 10, None, "IID('{962D1C1A-1074-4306-BEAE-9EA10A4D2D6E}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ShowTextLegend' , 'pVal' , ), 8053, (8053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ShowTextLegend' , 'pVal' , ), 8053, (8053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'BandLevel' , 'pVal' , ), 8054, (8054, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'BandLevel' , 'pVal' , ), 8054, (8054, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IDurabilityContourMinMaxOption_vtables_dispatch_ = 1
IDurabilityContourMinMaxOption_vtables_ = [
	(( 'MinMaxType' , 'pVal' , ), 8051, (8051, (), [ (3, 1, None, "IID('{E2761D2D-999A-4CB7-BDFB-4868168F684D}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'MinMaxType' , 'pVal' , ), 8051, (8051, (), [ (16387, 10, None, "IID('{E2761D2D-999A-4CB7-BDFB-4868168F684D}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ShowMinMax' , 'pVal' , ), 8052, (8052, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ShowMinMax' , 'pVal' , ), 8052, (8052, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'EnableLogScale' , 'pVal' , ), 8053, (8053, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'EnableLogScale' , 'pVal' , ), 8053, (8053, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Calculation' , ), 8055, (8055, (), [ ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Min' , 'pVal' , ), 8056, (8056, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Max' , 'pVal' , ), 8057, (8057, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMin' , 'pVal' , ), 8058, (8058, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMin' , 'pVal' , ), 8058, (8058, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMax' , 'pVal' , ), 8059, (8059, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedMax' , 'pVal' , ), 8059, (8059, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IDurabilityContourProbeOption_vtables_dispatch_ = 1
IDurabilityContourProbeOption_vtables_ = [
	(( 'ShowProbeResult' , 'pVal' , ), 8051, (8051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ShowProbeResult' , 'pVal' , ), 8051, (8051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Select' , 'Val' , ), 8052, (8052, (), [ (3, 1, None, "IID('{2EE67FB6-013E-45B0-97D2-469D2915100A}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 8053, (8053, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IDurabilityContourStyleOption_vtables_dispatch_ = 1
IDurabilityContourStyleOption_vtables_ = [
	(( 'ColorType' , 'pVal' , ), 8051, (8051, (), [ (3, 1, None, "IID('{9BA27F29-EA82-4029-ADFA-18351FD3A6E3}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ColorType' , 'pVal' , ), 8051, (8051, (), [ (16387, 10, None, "IID('{9BA27F29-EA82-4029-ADFA-18351FD3A6E3}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'pVal' , ), 8052, (8052, (), [ (3, 1, None, "IID('{055C0C4E-D758-49A8-BC89-3262E1832894}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'pVal' , ), 8052, (8052, (), [ (16387, 10, None, "IID('{055C0C4E-D758-49A8-BC89-3262E1832894}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SpectrumMinColor' , 'pVal' , ), 8053, (8053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SpectrumMinColor' , 'pVal' , ), 8053, (8053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SpectrumMaxColor' , 'pVal' , ), 8054, (8054, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SpectrumMaxColor' , 'pVal' , ), 8054, (8054, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GrayScaleColor' , 'pVal' , ), 8055, (8055, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GrayScaleColor' , 'pVal' , ), 8055, (8055, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TextColor' , 'pVal' , ), 8056, (8056, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TextColor' , 'pVal' , ), 8056, (8056, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ShowMeshLines' , 'pVal' , ), 8057, (8057, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ShowMeshLines' , 'pVal' , ), 8057, (8057, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'MeshLinesColor' , 'pVal' , ), 8058, (8058, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'MeshLinesColor' , 'pVal' , ), 8058, (8058, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'VectorColor' , 'pVal' , ), 8059, (8059, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'VectorColor' , 'pVal' , ), 8059, (8059, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'VectorSize' , 'pVal' , ), 8060, (8060, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'VectorSize' , 'pVal' , ), 8060, (8060, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IDurabilityFatigueEvaluation_vtables_dispatch_ = 1
IDurabilityFatigueEvaluation_vtables_ = [
	(( 'AxialMode' , 'pVal' , ), 8001, (8001, (), [ (3, 1, None, "IID('{AA2BBDF8-4B1A-4EA2-8139-59D10C3CABC2}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AxialMode' , 'pVal' , ), 8001, (8001, (), [ (16387, 10, None, "IID('{AA2BBDF8-4B1A-4EA2-8139-59D10C3CABC2}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LifeCriteria' , 'pVal' , ), 8002, (8002, (), [ (3, 1, None, "IID('{237F28A9-AF92-45CF-BA8A-0035B4D3E04D}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LifeCriteria' , 'pVal' , ), 8002, (8002, (), [ (16387, 10, None, "IID('{237F28A9-AF92-45CF-BA8A-0035B4D3E04D}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ElementPatchSet' , 'ppVal' , ), 8003, (8003, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ElementPatchSet' , 'ppVal' , ), 8003, (8003, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TimeHistoryWithFrame' , 'pVal' , ), 8004, (8004, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TimeHistoryWithFrame' , 'pVal' , ), 8004, (8004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Occurrence' , 'ppVal' , ), 8005, (8005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'ppVal' , ), 8006, (8006, (), [ (16393, 10, None, "IID('{6E70D029-92E7-453A-81C7-8BC9727DCB8D}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Stress' , 'ppVal' , ), 8007, (8007, (), [ (16393, 10, None, "IID('{40E8C43D-5AF9-44F9-80F5-F8FB9984879A}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Strain' , 'ppVal' , ), 8008, (8008, (), [ (16393, 10, None, "IID('{EBA808F3-9FD8-4375-BD38-F71DFB281AC8}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SafetyFactor' , 'ppVal' , ), 8009, (8009, (), [ (16393, 10, None, "IID('{CDBAEBAA-5287-4F55-A6A4-7AA213D3D045}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Result' , 'ppVal' , ), 8010, (8010, (), [ (16393, 10, None, "IID('{AA1358DD-7933-4CFE-B738-AFB37F0C0D0E}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Calculation' , ), 8011, (8011, (), [ ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'RainFlowCounting' , ), 8012, (8012, (), [ ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'PlotHistory' , ), 8013, (8013, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'RainFlow' , 'ppVal' , ), 8014, (8014, (), [ (16393, 10, None, "IID('{5494C9D5-49B9-476D-A973-A5C524009AC9}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PlotOriginalHistory' , 'ppVal' , ), 8015, (8015, (), [ (16393, 10, None, "IID('{1B06AC13-47EA-4070-A4FD-CE5E341F2650}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CreateTimeHistory' , 'use' , 'Name' , 'timeRange' , ), 8016, (8016, (), [ 
			 (11, 1, None, None) , (8, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ClearTimeHistory' , ), 8017, (8017, (), [ ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'TimeHistoryCollection' , 'ppVal' , ), 8018, (8018, (), [ (16393, 10, None, "IID('{0FC6C5F7-150B-4077-A5CA-D0DCF8B79777}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strFileName' , ), 8019, (8019, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UsePreStress' , 'pVal' , ), 8020, (8020, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UsePreStress' , 'pVal' , ), 8020, (8020, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'PreStressFile' , 'pVal' , ), 8021, (8021, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'PreStressFile' , 'pVal' , ), 8021, (8021, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseRecalculateRecovery' , 'pVal' , ), 8022, (8022, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseRecalculateRecovery' , 'pVal' , ), 8022, (8022, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'SpecificAngleCalculationOption' , 'varOption' , ), 8023, (8023, (), [ (16393, 10, None, "IID('{4D1AEBE0-9522-4D83-B1E9-784161452107}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'SpecificAngleCalculationResult' , 'varResult' , ), 8024, (8024, (), [ (16393, 10, None, "IID('{20342F66-B448-4E67-8C28-3C74142E38C2}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
]

IDurabilityFatigueEvaluationSafetyFactor_vtables_dispatch_ = 1
IDurabilityFatigueEvaluationSafetyFactor_vtables_ = [
	(( 'LifeCriterion' , 'pVal' , ), 8001, (8001, (), [ (3, 1, None, "IID('{BBA71A70-E454-4404-89B8-2D32905D5BA0}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LifeCriterion' , 'pVal' , ), 8001, (8001, (), [ (16387, 10, None, "IID('{BBA71A70-E454-4404-89B8-2D32905D5BA0}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SearchingIncrement' , 'pVal' , ), 8002, (8002, (), [ (3, 1, None, "IID('{F51B4542-080C-40A0-A728-866A4277B746}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SearchingIncrement' , 'pVal' , ), 8002, (8002, (), [ (16387, 10, None, "IID('{F51B4542-080C-40A0-A728-866A4277B746}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IDurabilityFatigueEvaluationStrain_vtables_dispatch_ = 1
IDurabilityFatigueEvaluationStrain_vtables_ = [
	(( 'LifeCriterion' , 'pVal' , ), 8001, (8001, (), [ (3, 1, None, "IID('{1EE81CCA-D047-413E-A40C-5A3697D3BDA9}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LifeCriterion' , 'pVal' , ), 8001, (8001, (), [ (16387, 10, None, "IID('{1EE81CCA-D047-413E-A40C-5A3697D3BDA9}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SearchingIncrement' , 'pVal' , ), 8002, (8002, (), [ (3, 1, None, "IID('{F51B4542-080C-40A0-A728-866A4277B746}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SearchingIncrement' , 'pVal' , ), 8002, (8002, (), [ (16387, 10, None, "IID('{F51B4542-080C-40A0-A728-866A4277B746}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IDurabilityFatigueEvaluationStress_vtables_dispatch_ = 1
IDurabilityFatigueEvaluationStress_vtables_ = [
	(( 'LifeCriterion' , 'pVal' , ), 8001, (8001, (), [ (3, 1, None, "IID('{BC43CC93-88BE-4D8E-8972-F22079EBF557}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LifeCriterion' , 'pVal' , ), 8001, (8001, (), [ (16387, 10, None, "IID('{BC43CC93-88BE-4D8E-8972-F22079EBF557}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MeanStressEffect' , 'pVal' , ), 8002, (8002, (), [ (3, 1, None, "IID('{F03AC2EC-9F4A-4F9F-B348-885C50164629}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MeanStressEffect' , 'pVal' , ), 8002, (8002, (), [ (16387, 10, None, "IID('{F03AC2EC-9F4A-4F9F-B348-885C50164629}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SearchingIncrement' , 'pVal' , ), 8003, (8003, (), [ (3, 1, None, "IID('{F51B4542-080C-40A0-A728-866A4277B746}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SearchingIncrement' , 'pVal' , ), 8003, (8003, (), [ (16387, 10, None, "IID('{F51B4542-080C-40A0-A728-866A4277B746}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'BWI_Weld' , 'pVal' , ), 8004, (8004, (), [ (3, 1, None, "IID('{2641C3C4-9436-4478-9EF6-FB0C91418A99}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'BWI_Weld' , 'pVal' , ), 8004, (8004, (), [ (16387, 10, None, "IID('{2641C3C4-9436-4478-9EF6-FB0C91418A99}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'NumofStdDeviations' , 'ppVal' , ), 8005, (8005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IDurabilityFatigueMaterial_vtables_dispatch_ = 1
IDurabilityFatigueMaterial_vtables_ = [
	(( 'FileName' , 'pVal' , ), 8001, (8001, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FileName' , 'pVal' , ), 8001, (8001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ActiveMaterial' , 'pVal' , ), 8002, (8002, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ActiveMaterial' , 'pVal' , ), 8002, (8002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Unit' , 'pVal' , ), 8003, (8003, (), [ (3, 1, None, "IID('{561AC3A1-F874-4089-8323-F64321CEA45D}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Unit' , 'pVal' , ), 8003, (8003, (), [ (16387, 10, None, "IID('{561AC3A1-F874-4089-8323-F64321CEA45D}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UserDefined' , 'ppVal' , ), 8004, (8004, (), [ (16393, 10, None, "IID('{0006C001-A16E-4571-8402-A7589467302D}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IDurabilityFatigueMaterialUserDefined_vtables_dispatch_ = 1
IDurabilityFatigueMaterialUserDefined_vtables_ = [
	(( 'CycleToFailure' , 'pVal' , ), 8001, (8001, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'CycleToFailure' , 'pVal' , ), 8001, (8001, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Amplitude' , 'pVal' , ), 8002, (8002, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Amplitude' , 'pVal' , ), 8002, (8002, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'path' , ), 8003, (8003, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'path' , 'OverWrite' , ), 8004, (8004, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'YieldStress' , 'ppVal' , ), 8005, (8005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UltimateStrength' , 'ppVal' , ), 8006, (8006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StrengthCoefficient' , 'ppVal' , ), 8007, (8007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'InterpolationType' , 'pVal' , ), 8008, (8008, (), [ (3, 1, None, "IID('{AC6533BB-7A3B-42EE-9141-3B2A7B8FB819}')") , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'InterpolationType' , 'pVal' , ), 8008, (8008, (), [ (16387, 10, None, "IID('{AC6533BB-7A3B-42EE-9141-3B2A7B8FB819}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IDurabilityFatigueResult_vtables_dispatch_ = 1
IDurabilityFatigueResult_vtables_ = [
	(( 'FaceNodeIDs' , 'pVal' , ), 8001, (8001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Damage' , 'pVal' , ), 8002, (8002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Life' , 'pVal' , ), 8003, (8003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'SafetyFactor' , 'pVal' , ), 8004, (8004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FaceNodeIDsList' , 'ppVal' , ), 8005, (8005, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DamageList' , 'ppVal' , ), 8006, (8006, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LifeList' , 'ppVal' , ), 8007, (8007, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SafetyFactorList' , 'ppVal' , ), 8008, (8008, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TimeHistoryNameList' , 'ppVal' , ), 8009, (8009, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'MeanStressList' , 'timeHist' , 'ppVal' , ), 8010, (8010, (), [ (8, 1, None, None) , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'StressAmplitudeList' , 'timeHist' , 'ppVal' , ), 8011, (8011, (), [ (8, 1, None, None) , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IDurabilityPlotOriginalHistory_vtables_dispatch_ = 1
IDurabilityPlotOriginalHistory_vtables_ = [
	(( 'LocationType' , 'pVal' , ), 8001, (8001, (), [ (3, 1, None, "IID('{160F26E6-0856-48A7-A4EB-61C549192B1B}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LocationType' , 'pVal' , ), 8001, (8001, (), [ (16387, 10, None, "IID('{160F26E6-0856-48A7-A4EB-61C549192B1B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedPatchIndex' , 'pVal' , ), 8002, (8002, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedPatchIndex' , 'pVal' , ), 8002, (8002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TimeHistoryName' , ), 8003, (8003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AngleType' , 'enumType' , ), 8004, (8004, (), [ (3, 1, None, "IID('{410F001D-4B12-4AAD-830C-9474DC21B470}')") , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AngleType' , 'enumType' , ), 8004, (8004, (), [ (16387, 10, None, "IID('{410F001D-4B12-4AAD-830C-9474DC21B470}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedAngle' , 'dAngle' , ), 8005, (8005, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedAngle' , 'dAngle' , ), 8005, (8005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IDurabilityPreStress_vtables_dispatch_ = 1
IDurabilityPreStress_vtables_ = [
	(( 'ElementPatchSet' , 'ppVal' , ), 8001, (8001, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ElementPatchSet' , 'ppVal' , ), 8001, (8001, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceMarker' , 'ppVal' , ), 8002, (8002, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceMarker' , 'ppVal' , ), 8002, (8002, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'InputFile' , 'pVal' , ), 8003, (8003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'InputFile' , 'pVal' , ), 8003, (8003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ResultFile' , 'pVal' , ), 8004, (8004, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ResultFile' , 'pVal' , ), 8004, (8004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 8005, (8005, (), [ ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IDurabilityPreference_vtables_dispatch_ = 1
IDurabilityPreference_vtables_ = [
	(( 'Material' , 'ppVal' , ), 8001, (8001, (), [ (16393, 10, None, "IID('{B4393F58-156B-4530-87C6-7C1D325FBBEF}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FatigueInfluencingFactors' , 'ppVal' , ), 8002, (8002, (), [ (16393, 10, None, "IID('{AD378F84-F7A5-48B4-9A75-2C25A5D46125}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ConvergenceControl' , 'ppVal' , ), 8003, (8003, (), [ (16393, 10, None, "IID('{60C11468-A82B-4AB4-9737-6946C4B5CA24}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RainFlowCounting' , 'ppVal' , ), 8004, (8004, (), [ (16393, 10, None, "IID('{190D59B5-5943-40C2-9890-AC8DF022BC7B}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IDurabilityPreferenceConvergenceControl_vtables_dispatch_ = 1
IDurabilityPreferenceConvergenceControl_vtables_ = [
	(( 'MaxNumberIteration' , 'ppVal' , ), 8051, (8051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'InitialValue' , 'ppVal' , ), 8052, (8052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AbsoluteError' , 'ppVal' , ), 8053, (8053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IDurabilityPreferenceFatigueInfluencingFactors_vtables_dispatch_ = 1
IDurabilityPreferenceFatigueInfluencingFactors_vtables_ = [
	(( 'NotchFactorAmp' , 'ppVal' , ), 8051, (8051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SizeFactor' , 'ppVal' , ), 8052, (8052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LoadFactor' , 'ppVal' , ), 8053, (8053, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OtherFactor' , 'ppVal' , ), 8054, (8054, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SurfaceFactor' , 'ppVal' , ), 8055, (8055, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SurfaceFactorType' , 'pVal' , ), 8056, (8056, (), [ (3, 1, None, "IID('{C0A2D1B6-78D7-4011-A09C-B3ABFE9149CE}')") , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SurfaceFactorType' , 'pVal' , ), 8056, (8056, (), [ (16387, 10, None, "IID('{C0A2D1B6-78D7-4011-A09C-B3ABFE9149CE}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ScaleFactor' , 'ppVal' , ), 8057, (8057, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IDurabilityPreferenceMaterial_vtables_dispatch_ = 1
IDurabilityPreferenceMaterial_vtables_ = [
	(( 'LibraryPath' , 'pVal' , ), 8051, (8051, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LibraryPath' , 'pVal' , ), 8051, (8051, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IDurabilityPreferenceRainflowCounting_vtables_dispatch_ = 1
IDurabilityPreferenceRainflowCounting_vtables_ = [
	(( 'PeakValley' , 'ppVal' , ), 8051, (8051, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'NumberRanges' , 'ppVal' , ), 8052, (8052, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IDurabilityRainflowCounting_vtables_dispatch_ = 1
IDurabilityRainflowCounting_vtables_ = [
	(( 'LocationType' , 'pVal' , ), 8001, (8001, (), [ (3, 1, None, "IID('{160F26E6-0856-48A7-A4EB-61C549192B1B}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LocationType' , 'pVal' , ), 8001, (8001, (), [ (16387, 10, None, "IID('{160F26E6-0856-48A7-A4EB-61C549192B1B}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedPatchIndex' , 'pVal' , ), 8002, (8002, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedPatchIndex' , 'pVal' , ), 8002, (8002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TimeHistoryName' , ), 8003, (8003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AngleType' , 'enumType' , ), 8004, (8004, (), [ (3, 1, None, "IID('{410F001D-4B12-4AAD-830C-9474DC21B470}')") , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AngleType' , 'enumType' , ), 8004, (8004, (), [ (16387, 10, None, "IID('{410F001D-4B12-4AAD-830C-9474DC21B470}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedAngle' , 'dAngle' , ), 8005, (8005, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedAngle' , 'dAngle' , ), 8005, (8005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IDurabilitySpecificAngleCalculationOption_vtables_dispatch_ = 1
IDurabilitySpecificAngleCalculationOption_vtables_ = [
	(( 'TimeHistoryName' , ), 8001, (8001, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LocationType' , 'enumType' , ), 8002, (8002, (), [ (3, 1, None, "IID('{160F26E6-0856-48A7-A4EB-61C549192B1B}')") , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LocationType' , 'enumType' , ), 8002, (8002, (), [ (16387, 10, None, "IID('{160F26E6-0856-48A7-A4EB-61C549192B1B}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedPatchIndex' , 'lIndex' , ), 8003, (8003, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedPatchIndex' , 'lIndex' , ), 8003, (8003, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'AngleType' , 'enumType' , ), 8004, (8004, (), [ (3, 1, None, "IID('{410F001D-4B12-4AAD-830C-9474DC21B470}')") , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AngleType' , 'enumType' , ), 8004, (8004, (), [ (16387, 10, None, "IID('{410F001D-4B12-4AAD-830C-9474DC21B470}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedAngle' , 'dAngle' , ), 8005, (8005, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedAngle' , 'dAngle' , ), 8005, (8005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IDurabilitySpecificAngleCalculationResult_vtables_dispatch_ = 1
IDurabilitySpecificAngleCalculationResult_vtables_ = [
	(( 'Damage' , 'dDamage' , ), 8001, (8001, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Life' , 'dLife' , ), 8002, (8002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'SafetyFactor' , 'dSafetyFactor' , ), 8003, (8003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IDurabilityTimeHistory_vtables_dispatch_ = 1
IDurabilityTimeHistory_vtables_ = [
	(( 'UseTimeHistory' , 'pVal' , ), 8001, (8001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseTimeHistory' , 'pVal' , ), 8001, (8001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 8002, (8002, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 8002, (8002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FrameRange' , 'pVal' , ), 8003, (8003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FrameRange' , 'pVal' , ), 8003, (8003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IDurabilityTimeHistoryCollection_vtables_dispatch_ = 1
IDurabilityTimeHistoryCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{BA1DD446-7C44-42A8-B7D5-99667FC088F6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IDurabilityToolkit_vtables_dispatch_ = 1
IDurabilityToolkit_vtables_ = [
	(( 'Preference' , 'ppVal' , ), 8001, (8001, (), [ (16393, 10, None, "IID('{8D781640-3E0A-485F-920C-4338B86BEC54}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FatigueEvaluation' , 'ppVal' , ), 8002, (8002, (), [ (16393, 10, None, "IID('{D65A4952-C3CE-42F4-A6F2-D7DEBEF72EC0}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Contour' , 'ppVal' , ), 8003, (8003, (), [ (16393, 10, None, "IID('{A7CCAFA8-34D0-4D9E-97F9-F92C15E19BAB}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PreStress' , 'ppVal' , ), 8004, (8004, (), [ (16393, 10, None, "IID('{41015A8F-B86B-4D5A-9BAA-2D5CBE880191}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{B4393F58-156B-4530-87C6-7C1D325FBBEF}' : IDurabilityPreferenceMaterial,
	'{AD378F84-F7A5-48B4-9A75-2C25A5D46125}' : IDurabilityPreferenceFatigueInfluencingFactors,
	'{60C11468-A82B-4AB4-9737-6946C4B5CA24}' : IDurabilityPreferenceConvergenceControl,
	'{190D59B5-5943-40C2-9890-AC8DF022BC7B}' : IDurabilityPreferenceRainflowCounting,
	'{8D781640-3E0A-485F-920C-4338B86BEC54}' : IDurabilityPreference,
	'{AA1358DD-7933-4CFE-B738-AFB37F0C0D0E}' : IDurabilityFatigueResult,
	'{0006C001-A16E-4571-8402-A7589467302D}' : IDurabilityFatigueMaterialUserDefined,
	'{6E70D029-92E7-453A-81C7-8BC9727DCB8D}' : IDurabilityFatigueMaterial,
	'{40E8C43D-5AF9-44F9-80F5-F8FB9984879A}' : IDurabilityFatigueEvaluationStress,
	'{EBA808F3-9FD8-4375-BD38-F71DFB281AC8}' : IDurabilityFatigueEvaluationStrain,
	'{CDBAEBAA-5287-4F55-A6A4-7AA213D3D045}' : IDurabilityFatigueEvaluationSafetyFactor,
	'{5494C9D5-49B9-476D-A973-A5C524009AC9}' : IDurabilityRainflowCounting,
	'{1B06AC13-47EA-4070-A4FD-CE5E341F2650}' : IDurabilityPlotOriginalHistory,
	'{4D1AEBE0-9522-4D83-B1E9-784161452107}' : IDurabilitySpecificAngleCalculationOption,
	'{20342F66-B448-4E67-8C28-3C74142E38C2}' : IDurabilitySpecificAngleCalculationResult,
	'{BA1DD446-7C44-42A8-B7D5-99667FC088F6}' : IDurabilityTimeHistory,
	'{0FC6C5F7-150B-4077-A5CA-D0DCF8B79777}' : IDurabilityTimeHistoryCollection,
	'{D65A4952-C3CE-42F4-A6F2-D7DEBEF72EC0}' : IDurabilityFatigueEvaluation,
	'{1877A27A-16EC-492A-B121-2158CA766380}' : IDurabilityContourBandOption,
	'{02902C9C-2767-4E11-A750-6AFDF9F1386B}' : IDurabilityContourMinMaxOption,
	'{AD4A1D92-5D4B-47CA-BD19-CDBA4567BB11}' : IDurabilityContourStyleOption,
	'{3707C188-79DF-4DC1-9F29-6DF34660C998}' : IDurabilityContourProbeOption,
	'{A7CCAFA8-34D0-4D9E-97F9-F92C15E19BAB}' : IDurabilityContour,
	'{41015A8F-B86B-4D5A-9BAA-2D5CBE880191}' : IDurabilityPreStress,
	'{8B1BCD31-C01E-4B81-8A52-E4533BEE9F10}' : IDurabilityToolkit,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{B4393F58-156B-4530-87C6-7C1D325FBBEF}' : 'IDurabilityPreferenceMaterial',
	'{AD378F84-F7A5-48B4-9A75-2C25A5D46125}' : 'IDurabilityPreferenceFatigueInfluencingFactors',
	'{60C11468-A82B-4AB4-9737-6946C4B5CA24}' : 'IDurabilityPreferenceConvergenceControl',
	'{190D59B5-5943-40C2-9890-AC8DF022BC7B}' : 'IDurabilityPreferenceRainflowCounting',
	'{8D781640-3E0A-485F-920C-4338B86BEC54}' : 'IDurabilityPreference',
	'{AA1358DD-7933-4CFE-B738-AFB37F0C0D0E}' : 'IDurabilityFatigueResult',
	'{0006C001-A16E-4571-8402-A7589467302D}' : 'IDurabilityFatigueMaterialUserDefined',
	'{6E70D029-92E7-453A-81C7-8BC9727DCB8D}' : 'IDurabilityFatigueMaterial',
	'{40E8C43D-5AF9-44F9-80F5-F8FB9984879A}' : 'IDurabilityFatigueEvaluationStress',
	'{EBA808F3-9FD8-4375-BD38-F71DFB281AC8}' : 'IDurabilityFatigueEvaluationStrain',
	'{CDBAEBAA-5287-4F55-A6A4-7AA213D3D045}' : 'IDurabilityFatigueEvaluationSafetyFactor',
	'{5494C9D5-49B9-476D-A973-A5C524009AC9}' : 'IDurabilityRainflowCounting',
	'{1B06AC13-47EA-4070-A4FD-CE5E341F2650}' : 'IDurabilityPlotOriginalHistory',
	'{4D1AEBE0-9522-4D83-B1E9-784161452107}' : 'IDurabilitySpecificAngleCalculationOption',
	'{20342F66-B448-4E67-8C28-3C74142E38C2}' : 'IDurabilitySpecificAngleCalculationResult',
	'{BA1DD446-7C44-42A8-B7D5-99667FC088F6}' : 'IDurabilityTimeHistory',
	'{0FC6C5F7-150B-4077-A5CA-D0DCF8B79777}' : 'IDurabilityTimeHistoryCollection',
	'{D65A4952-C3CE-42F4-A6F2-D7DEBEF72EC0}' : 'IDurabilityFatigueEvaluation',
	'{1877A27A-16EC-492A-B121-2158CA766380}' : 'IDurabilityContourBandOption',
	'{02902C9C-2767-4E11-A750-6AFDF9F1386B}' : 'IDurabilityContourMinMaxOption',
	'{AD4A1D92-5D4B-47CA-BD19-CDBA4567BB11}' : 'IDurabilityContourStyleOption',
	'{3707C188-79DF-4DC1-9F29-6DF34660C998}' : 'IDurabilityContourProbeOption',
	'{A7CCAFA8-34D0-4D9E-97F9-F92C15E19BAB}' : 'IDurabilityContour',
	'{41015A8F-B86B-4D5A-9BAA-2D5CBE880191}' : 'IDurabilityPreStress',
	'{8B1BCD31-C01E-4B81-8A52-E4533BEE9F10}' : 'IDurabilityToolkit',
}


NamesToIIDMap = {
	'IDurabilityPreferenceMaterial' : '{B4393F58-156B-4530-87C6-7C1D325FBBEF}',
	'IDurabilityPreferenceFatigueInfluencingFactors' : '{AD378F84-F7A5-48B4-9A75-2C25A5D46125}',
	'IDurabilityPreferenceConvergenceControl' : '{60C11468-A82B-4AB4-9737-6946C4B5CA24}',
	'IDurabilityPreferenceRainflowCounting' : '{190D59B5-5943-40C2-9890-AC8DF022BC7B}',
	'IDurabilityPreference' : '{8D781640-3E0A-485F-920C-4338B86BEC54}',
	'IDurabilityFatigueResult' : '{AA1358DD-7933-4CFE-B738-AFB37F0C0D0E}',
	'IDurabilityFatigueMaterialUserDefined' : '{0006C001-A16E-4571-8402-A7589467302D}',
	'IDurabilityFatigueMaterial' : '{6E70D029-92E7-453A-81C7-8BC9727DCB8D}',
	'IDurabilityFatigueEvaluationStress' : '{40E8C43D-5AF9-44F9-80F5-F8FB9984879A}',
	'IDurabilityFatigueEvaluationStrain' : '{EBA808F3-9FD8-4375-BD38-F71DFB281AC8}',
	'IDurabilityFatigueEvaluationSafetyFactor' : '{CDBAEBAA-5287-4F55-A6A4-7AA213D3D045}',
	'IDurabilityRainflowCounting' : '{5494C9D5-49B9-476D-A973-A5C524009AC9}',
	'IDurabilityPlotOriginalHistory' : '{1B06AC13-47EA-4070-A4FD-CE5E341F2650}',
	'IDurabilitySpecificAngleCalculationOption' : '{4D1AEBE0-9522-4D83-B1E9-784161452107}',
	'IDurabilitySpecificAngleCalculationResult' : '{20342F66-B448-4E67-8C28-3C74142E38C2}',
	'IDurabilityTimeHistory' : '{BA1DD446-7C44-42A8-B7D5-99667FC088F6}',
	'IDurabilityTimeHistoryCollection' : '{0FC6C5F7-150B-4077-A5CA-D0DCF8B79777}',
	'IDurabilityFatigueEvaluation' : '{D65A4952-C3CE-42F4-A6F2-D7DEBEF72EC0}',
	'IDurabilityContourBandOption' : '{1877A27A-16EC-492A-B121-2158CA766380}',
	'IDurabilityContourMinMaxOption' : '{02902C9C-2767-4E11-A750-6AFDF9F1386B}',
	'IDurabilityContourStyleOption' : '{AD4A1D92-5D4B-47CA-BD19-CDBA4567BB11}',
	'IDurabilityContourProbeOption' : '{3707C188-79DF-4DC1-9F29-6DF34660C998}',
	'IDurabilityContour' : '{A7CCAFA8-34D0-4D9E-97F9-F92C15E19BAB}',
	'IDurabilityPreStress' : '{41015A8F-B86B-4D5A-9BAA-2D5CBE880191}',
	'IDurabilityToolkit' : '{8B1BCD31-C01E-4B81-8A52-E4533BEE9F10}',
}


