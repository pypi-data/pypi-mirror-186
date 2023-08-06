# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMChart.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMChart Type Library'
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

CLSID = IID('{9273C2D5-ECD3-493B-A164-4392D2FE2A08}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class AxisAngleType(IntEnum):
	'''
	AxisAngleType enumeration.
	'''
	AxisAngleType_45Degrees       =2         
	'''Constant value is 2.'''
	AxisAngleType_Horizontal      =0         
	'''Constant value is 0.'''
	AxisAngleType_Vertical        =1         
	'''Constant value is 1.'''
class AxisPositionType(IntEnum):
	'''
	AxisPositionType enumeration.
	'''
	AxisPositionType_Far          =2         
	'''Constant value is 2.'''
	AxisPositionType_Near         =0         
	'''Constant value is 0.'''
class DockedPositionType(IntEnum):
	'''
	DockedPositionType enumeration.
	'''
	DockedPositionType_Bottom     =2         
	'''Constant value is 2.'''
	DockedPositionType_Left       =1         
	'''Constant value is 1.'''
	DockedPositionType_Right      =3         
	'''Constant value is 3.'''
	DockedPositionType_Top        =0         
	'''Constant value is 0.'''
class GalleryType(IntEnum):
	'''
	GalleryType enumeration.
	'''
	GalleryType_Area              =3         
	'''Constant value is 3.'''
	GalleryType_Bar               =2         
	'''Constant value is 2.'''
	GalleryType_Contour           =18        
	'''Constant value is 18.'''
	GalleryType_Curve             =6         
	'''Constant value is 6.'''
	GalleryType_CurveArea         =19        
	'''Constant value is 19.'''
	GalleryType_Line              =1         
	'''Constant value is 1.'''
	GalleryType_Reserved          =0         
	'''Constant value is 0.'''
	GalleryType_Scatter           =4         
	'''Constant value is 4.'''
	GalleryType_Step              =8         
	'''Constant value is 8.'''
	GalleryType_Surface           =10        
	'''Constant value is 10.'''
class LegendBoxAlignment(IntEnum):
	'''
	LegendBoxAlignment enumeration.
	'''
	LegendBoxAlignment_Center     =2         
	'''Constant value is 2.'''
	LegendBoxAlignment_Far        =3         
	'''Constant value is 3.'''
	LegendBoxAlignment_Near       =1         
	'''Constant value is 1.'''
	LegendBoxAlignment_Spread     =0         
	'''Constant value is 0.'''
class LineType(IntEnum):
	'''
	LineType enumeration.
	'''
	LineType_Dash                 =1         
	'''Constant value is 1.'''
	LineType_DashDot              =3         
	'''Constant value is 3.'''
	LineType_DashDotDot           =4         
	'''Constant value is 4.'''
	LineType_Dot                  =2         
	'''Constant value is 2.'''
	LineType_Solid                =0         
	'''Constant value is 0.'''
class MarkerType(IntEnum):
	'''
	MarkerType enumeration.
	'''
	MarkerType_Circle             =2         
	'''Constant value is 2.'''
	MarkerType_Cross              =8         
	'''Constant value is 8.'''
	MarkerType_Diamond            =4         
	'''Constant value is 4.'''
	MarkerType_HorzLine           =6         
	'''Constant value is 6.'''
	MarkerType_InvertedTriangle   =9         
	'''Constant value is 9.'''
	MarkerType_Marble             =5         
	'''Constant value is 5.'''
	MarkerType_None               =0         
	'''Constant value is 0.'''
	MarkerType_Rect               =1         
	'''Constant value is 1.'''
	MarkerType_Triangle           =3         
	'''Constant value is 3.'''
	MarkerType_VertLine           =7         
	'''Constant value is 7.'''
	MarkerType_X                  =10        
	'''Constant value is 10.'''
class TextAlignment(IntEnum):
	'''
	TextAlignment enumeration.
	'''
	TextAlignment_Center          =1         
	'''Constant value is 1.'''
	TextAlignment_Far             =2         
	'''Constant value is 2.'''
	TextAlignment_Near            =0         
	'''Constant value is 0.'''
class YAxisType(IntEnum):
	'''
	YAxisType enumeration.
	'''
	YAxisType_AxisX               =2         
	'''Constant value is 2.'''
	YAxisType_AxisY               =0         
	'''Constant value is 0.'''
	YAxisType_AxisY2              =1         
	'''Constant value is 1.'''

from win32com.client import DispatchBaseClass
class IAxis(DispatchBaseClass):
	'''IAxis'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28396}')
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
		return self._ApplyTypes_(*(1025, 2, (3, 0), (), "Angle", '{F8C24AB7-D222-4646-9F6D-BE4D01CA49FC}'))
	def _get_AutoScale(self):
		return self._ApplyTypes_(*(1012, 2, (11, 0), (), "AutoScale", None))
	def _get_Grid(self):
		return self._ApplyTypes_(*(1021, 2, (9, 0), (), "Grid", '{4DE0B045-C16A-46E4-A238-E70556CE1A4F}'))
	def _get_LabelsFormat(self):
		return self._ApplyTypes_(*(1022, 2, (9, 0), (), "LabelsFormat", '{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}'))
	def _get_Line(self):
		return self._ApplyTypes_(*(1023, 2, (9, 0), (), "Line", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}'))
	def _get_LogBase(self):
		return self._ApplyTypes_(*(1004, 2, (5, 0), (), "LogBase", None))
	def _get_MajorTickCount(self):
		return self._ApplyTypes_(*(1007, 2, (3, 0), (), "MajorTickCount", None))
	def _get_MajorTickStep(self):
		return self._ApplyTypes_(*(1006, 2, (5, 0), (), "MajorTickStep", None))
	def _get_Max(self):
		return self._ApplyTypes_(*(1002, 2, (5, 0), (), "Max", None))
	def _get_Min(self):
		return self._ApplyTypes_(*(1001, 2, (5, 0), (), "Min", None))
	def _get_MinorTickStep(self):
		return self._ApplyTypes_(*(1003, 2, (5, 0), (), "MinorTickStep", None))
	def _get_Position(self):
		return self._ApplyTypes_(*(1013, 2, (3, 0), (), "Position", '{E0E92E5B-7E01-4C8D-996B-349F51234E22}'))
	def _get_Staggered(self):
		return self._ApplyTypes_(*(1026, 2, (11, 0), (), "Staggered", None))
	def _get_StepFont(self):
		return self._ApplyTypes_(*(1024, 2, (9, 0), (), "StepFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'))
	def _get_Title(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'))
	def _get_UseMajorTickCount(self):
		return self._ApplyTypes_(*(1008, 2, (11, 0), (), "UseMajorTickCount", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(1005, 2, (11, 0), (), "Visible", None))

	def _set_Angle(self, value):
		if "Angle" in self.__dict__: self.__dict__["Angle"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_AutoScale(self, value):
		if "AutoScale" in self.__dict__: self.__dict__["AutoScale"] = value; return
		self._oleobj_.Invoke(*((1012, LCID, 4, 0) + (value,) + ()))
	def _set_LogBase(self, value):
		if "LogBase" in self.__dict__: self.__dict__["LogBase"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_MajorTickCount(self, value):
		if "MajorTickCount" in self.__dict__: self.__dict__["MajorTickCount"] = value; return
		self._oleobj_.Invoke(*((1007, LCID, 4, 0) + (value,) + ()))
	def _set_MajorTickStep(self, value):
		if "MajorTickStep" in self.__dict__: self.__dict__["MajorTickStep"] = value; return
		self._oleobj_.Invoke(*((1006, LCID, 4, 0) + (value,) + ()))
	def _set_Max(self, value):
		if "Max" in self.__dict__: self.__dict__["Max"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_Min(self, value):
		if "Min" in self.__dict__: self.__dict__["Min"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_MinorTickStep(self, value):
		if "MinorTickStep" in self.__dict__: self.__dict__["MinorTickStep"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		self._oleobj_.Invoke(*((1013, LCID, 4, 0) + (value,) + ()))
	def _set_Staggered(self, value):
		if "Staggered" in self.__dict__: self.__dict__["Staggered"] = value; return
		self._oleobj_.Invoke(*((1026, LCID, 4, 0) + (value,) + ()))
	def _set_UseMajorTickCount(self, value):
		if "UseMajorTickCount" in self.__dict__: self.__dict__["UseMajorTickCount"] = value; return
		self._oleobj_.Invoke(*((1008, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((1005, LCID, 4, 0) + (value,) + ()))

	Angle = property(_get_Angle, _set_Angle)
	'''
	Change the angle of the axis labels.

	:type: recurdyn.Chart.AxisAngleType
	'''
	AutoScale = property(_get_AutoScale, _set_AutoScale)
	'''
	always recalculate the specified Axis scale values (Min, Max) when new values are set to the chart.

	:type: bool
	'''
	Grid = property(_get_Grid, None)
	'''
	Allows customization of grid lines by providing access to the supported members of the Grids.

	:type: recurdyn.Chart.IGrid
	'''
	LabelsFormat = property(_get_LabelsFormat, None)
	'''
	Used to format the labels displayed on the selected axis.

	:type: recurdyn.Chart.IValueFormat
	'''
	Line = property(_get_Line, None)
	'''
	Allows you to apply supported Line class members to a selected axis line.

	:type: recurdyn.Chart.ILine
	'''
	LogBase = property(_get_LogBase, _set_LogBase)
	'''
	Used to set a logarithmic scale for a numerical axis and recalculate the values as powers equal to the setting of this property.

	:type: float
	'''
	MajorTickCount = property(_get_MajorTickCount, _set_MajorTickCount)
	'''
	Specifies the number of major tick marks and gridlines on the selected axis.

	:type: int
	'''
	MajorTickStep = property(_get_MajorTickStep, _set_MajorTickStep)
	'''
	Specifies the interval of major tick marks and gridlines on the selected axis, aka Step.

	:type: float
	'''
	Max = property(_get_Max, _set_Max)
	'''
	Defines the maximum value of a specific axis.

	:type: float
	'''
	Min = property(_get_Min, _set_Min)
	'''
	Defines the minimum value of a selected axis.

	:type: float
	'''
	MinorTickStep = property(_get_MinorTickStep, _set_MinorTickStep)
	'''
	Specifies the increment you want between minor tick marks and minor gridlines (if they are displayed) on the selected axis, aka MinorStep.

	:type: float
	'''
	Position = property(_get_Position, _set_Position)
	'''
	Specifies the placement of the axis labels and tick marks relative to the chart.

	:type: recurdyn.Chart.AxisPositionType
	'''
	Staggered = property(_get_Staggered, _set_Staggered)
	'''
	Use staggered labels.

	:type: bool
	'''
	StepFont = property(_get_StepFont, None)
	'''
	the font of the axis step number

	:type: recurdyn.Chart.IChartFont
	'''
	Title = property(_get_Title, None)
	'''
	the title for a specific axis.

	:type: recurdyn.Chart.ITitle
	'''
	UseMajorTickCount = property(_get_UseMajorTickCount, _set_UseMajorTickCount)
	'''
	Use MajorTickCount or MajorTickStep for the major tick marks and gridlines on the selected axis.

	:type: bool
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	Shows or hides the lines, labels, tick marks and grids for the selected axis.

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Angle": _set_Angle,
		"_set_AutoScale": _set_AutoScale,
		"_set_LogBase": _set_LogBase,
		"_set_MajorTickCount": _set_MajorTickCount,
		"_set_MajorTickStep": _set_MajorTickStep,
		"_set_Max": _set_Max,
		"_set_Min": _set_Min,
		"_set_MinorTickStep": _set_MinorTickStep,
		"_set_Position": _set_Position,
		"_set_Staggered": _set_Staggered,
		"_set_UseMajorTickCount": _set_UseMajorTickCount,
		"_set_Visible": _set_Visible,
	}
	_prop_map_get_ = {
		"Angle": (1025, 2, (3, 0), (), "Angle", '{F8C24AB7-D222-4646-9F6D-BE4D01CA49FC}'),
		"AutoScale": (1012, 2, (11, 0), (), "AutoScale", None),
		"Grid": (1021, 2, (9, 0), (), "Grid", '{4DE0B045-C16A-46E4-A238-E70556CE1A4F}'),
		"LabelsFormat": (1022, 2, (9, 0), (), "LabelsFormat", '{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}'),
		"Line": (1023, 2, (9, 0), (), "Line", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}'),
		"LogBase": (1004, 2, (5, 0), (), "LogBase", None),
		"MajorTickCount": (1007, 2, (3, 0), (), "MajorTickCount", None),
		"MajorTickStep": (1006, 2, (5, 0), (), "MajorTickStep", None),
		"Max": (1002, 2, (5, 0), (), "Max", None),
		"Min": (1001, 2, (5, 0), (), "Min", None),
		"MinorTickStep": (1003, 2, (5, 0), (), "MinorTickStep", None),
		"Position": (1013, 2, (3, 0), (), "Position", '{E0E92E5B-7E01-4C8D-996B-349F51234E22}'),
		"Staggered": (1026, 2, (11, 0), (), "Staggered", None),
		"StepFont": (1024, 2, (9, 0), (), "StepFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'),
		"Title": (1011, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'),
		"UseMajorTickCount": (1008, 2, (11, 0), (), "UseMajorTickCount", None),
		"Visible": (1005, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Angle": ((1025, LCID, 4, 0),()),
		"AutoScale": ((1012, LCID, 4, 0),()),
		"LogBase": ((1004, LCID, 4, 0),()),
		"MajorTickCount": ((1007, LCID, 4, 0),()),
		"MajorTickStep": ((1006, LCID, 4, 0),()),
		"Max": ((1002, LCID, 4, 0),()),
		"Min": ((1001, LCID, 4, 0),()),
		"MinorTickStep": ((1003, LCID, 4, 0),()),
		"Position": ((1013, LCID, 4, 0),()),
		"Staggered": ((1026, LCID, 4, 0),()),
		"UseMajorTickCount": ((1008, LCID, 4, 0),()),
		"Visible": ((1005, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IAxisX(DispatchBaseClass):
	'''IAxisX'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28397}')
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
		return self._ApplyTypes_(*(1025, 2, (3, 0), (), "Angle", '{F8C24AB7-D222-4646-9F6D-BE4D01CA49FC}'))
	def _get_AutoScale(self):
		return self._ApplyTypes_(*(1012, 2, (11, 0), (), "AutoScale", None))
	def _get_Grid(self):
		return self._ApplyTypes_(*(1021, 2, (9, 0), (), "Grid", '{4DE0B045-C16A-46E4-A238-E70556CE1A4F}'))
	def _get_LabelsFormat(self):
		return self._ApplyTypes_(*(1022, 2, (9, 0), (), "LabelsFormat", '{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}'))
	def _get_Line(self):
		return self._ApplyTypes_(*(1023, 2, (9, 0), (), "Line", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}'))
	def _get_LogBase(self):
		return self._ApplyTypes_(*(1004, 2, (5, 0), (), "LogBase", None))
	def _get_MajorTickCount(self):
		return self._ApplyTypes_(*(1007, 2, (3, 0), (), "MajorTickCount", None))
	def _get_MajorTickStep(self):
		return self._ApplyTypes_(*(1006, 2, (5, 0), (), "MajorTickStep", None))
	def _get_Max(self):
		return self._ApplyTypes_(*(1002, 2, (5, 0), (), "Max", None))
	def _get_Min(self):
		return self._ApplyTypes_(*(1001, 2, (5, 0), (), "Min", None))
	def _get_MinorTickStep(self):
		return self._ApplyTypes_(*(1003, 2, (5, 0), (), "MinorTickStep", None))
	def _get_Position(self):
		return self._ApplyTypes_(*(1013, 2, (3, 0), (), "Position", '{E0E92E5B-7E01-4C8D-996B-349F51234E22}'))
	def _get_Staggered(self):
		return self._ApplyTypes_(*(1026, 2, (11, 0), (), "Staggered", None))
	def _get_StepFont(self):
		return self._ApplyTypes_(*(1024, 2, (9, 0), (), "StepFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'))
	def _get_Title(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'))
	def _get_UseMajorTickCount(self):
		return self._ApplyTypes_(*(1008, 2, (11, 0), (), "UseMajorTickCount", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(1005, 2, (11, 0), (), "Visible", None))

	def _set_Angle(self, value):
		if "Angle" in self.__dict__: self.__dict__["Angle"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_AutoScale(self, value):
		if "AutoScale" in self.__dict__: self.__dict__["AutoScale"] = value; return
		self._oleobj_.Invoke(*((1012, LCID, 4, 0) + (value,) + ()))
	def _set_LogBase(self, value):
		if "LogBase" in self.__dict__: self.__dict__["LogBase"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_MajorTickCount(self, value):
		if "MajorTickCount" in self.__dict__: self.__dict__["MajorTickCount"] = value; return
		self._oleobj_.Invoke(*((1007, LCID, 4, 0) + (value,) + ()))
	def _set_MajorTickStep(self, value):
		if "MajorTickStep" in self.__dict__: self.__dict__["MajorTickStep"] = value; return
		self._oleobj_.Invoke(*((1006, LCID, 4, 0) + (value,) + ()))
	def _set_Max(self, value):
		if "Max" in self.__dict__: self.__dict__["Max"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_Min(self, value):
		if "Min" in self.__dict__: self.__dict__["Min"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_MinorTickStep(self, value):
		if "MinorTickStep" in self.__dict__: self.__dict__["MinorTickStep"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		self._oleobj_.Invoke(*((1013, LCID, 4, 0) + (value,) + ()))
	def _set_Staggered(self, value):
		if "Staggered" in self.__dict__: self.__dict__["Staggered"] = value; return
		self._oleobj_.Invoke(*((1026, LCID, 4, 0) + (value,) + ()))
	def _set_UseMajorTickCount(self, value):
		if "UseMajorTickCount" in self.__dict__: self.__dict__["UseMajorTickCount"] = value; return
		self._oleobj_.Invoke(*((1008, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((1005, LCID, 4, 0) + (value,) + ()))

	Angle = property(_get_Angle, _set_Angle)
	'''
	Change the angle of the axis labels.

	:type: recurdyn.Chart.AxisAngleType
	'''
	AutoScale = property(_get_AutoScale, _set_AutoScale)
	'''
	always recalculate the specified Axis scale values (Min, Max) when new values are set to the chart.

	:type: bool
	'''
	Grid = property(_get_Grid, None)
	'''
	Allows customization of grid lines by providing access to the supported members of the Grids.

	:type: recurdyn.Chart.IGrid
	'''
	LabelsFormat = property(_get_LabelsFormat, None)
	'''
	Used to format the labels displayed on the selected axis.

	:type: recurdyn.Chart.IValueFormat
	'''
	Line = property(_get_Line, None)
	'''
	Allows you to apply supported Line class members to a selected axis line.

	:type: recurdyn.Chart.ILine
	'''
	LogBase = property(_get_LogBase, _set_LogBase)
	'''
	Used to set a logarithmic scale for a numerical axis and recalculate the values as powers equal to the setting of this property.

	:type: float
	'''
	MajorTickCount = property(_get_MajorTickCount, _set_MajorTickCount)
	'''
	Specifies the number of major tick marks and gridlines on the selected axis.

	:type: int
	'''
	MajorTickStep = property(_get_MajorTickStep, _set_MajorTickStep)
	'''
	Specifies the interval of major tick marks and gridlines on the selected axis, aka Step.

	:type: float
	'''
	Max = property(_get_Max, _set_Max)
	'''
	Defines the maximum value of a specific axis.

	:type: float
	'''
	Min = property(_get_Min, _set_Min)
	'''
	Defines the minimum value of a selected axis.

	:type: float
	'''
	MinorTickStep = property(_get_MinorTickStep, _set_MinorTickStep)
	'''
	Specifies the increment you want between minor tick marks and minor gridlines (if they are displayed) on the selected axis, aka MinorStep.

	:type: float
	'''
	Position = property(_get_Position, _set_Position)
	'''
	Specifies the placement of the axis labels and tick marks relative to the chart.

	:type: recurdyn.Chart.AxisPositionType
	'''
	Staggered = property(_get_Staggered, _set_Staggered)
	'''
	Use staggered labels.

	:type: bool
	'''
	StepFont = property(_get_StepFont, None)
	'''
	the font of the axis step number

	:type: recurdyn.Chart.IChartFont
	'''
	Title = property(_get_Title, None)
	'''
	the title for a specific axis.

	:type: recurdyn.Chart.ITitle
	'''
	UseMajorTickCount = property(_get_UseMajorTickCount, _set_UseMajorTickCount)
	'''
	Use MajorTickCount or MajorTickStep for the major tick marks and gridlines on the selected axis.

	:type: bool
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	Shows or hides the lines, labels, tick marks and grids for the selected axis.

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Angle": _set_Angle,
		"_set_AutoScale": _set_AutoScale,
		"_set_LogBase": _set_LogBase,
		"_set_MajorTickCount": _set_MajorTickCount,
		"_set_MajorTickStep": _set_MajorTickStep,
		"_set_Max": _set_Max,
		"_set_Min": _set_Min,
		"_set_MinorTickStep": _set_MinorTickStep,
		"_set_Position": _set_Position,
		"_set_Staggered": _set_Staggered,
		"_set_UseMajorTickCount": _set_UseMajorTickCount,
		"_set_Visible": _set_Visible,
	}
	_prop_map_get_ = {
		"Angle": (1025, 2, (3, 0), (), "Angle", '{F8C24AB7-D222-4646-9F6D-BE4D01CA49FC}'),
		"AutoScale": (1012, 2, (11, 0), (), "AutoScale", None),
		"Grid": (1021, 2, (9, 0), (), "Grid", '{4DE0B045-C16A-46E4-A238-E70556CE1A4F}'),
		"LabelsFormat": (1022, 2, (9, 0), (), "LabelsFormat", '{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}'),
		"Line": (1023, 2, (9, 0), (), "Line", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}'),
		"LogBase": (1004, 2, (5, 0), (), "LogBase", None),
		"MajorTickCount": (1007, 2, (3, 0), (), "MajorTickCount", None),
		"MajorTickStep": (1006, 2, (5, 0), (), "MajorTickStep", None),
		"Max": (1002, 2, (5, 0), (), "Max", None),
		"Min": (1001, 2, (5, 0), (), "Min", None),
		"MinorTickStep": (1003, 2, (5, 0), (), "MinorTickStep", None),
		"Position": (1013, 2, (3, 0), (), "Position", '{E0E92E5B-7E01-4C8D-996B-349F51234E22}'),
		"Staggered": (1026, 2, (11, 0), (), "Staggered", None),
		"StepFont": (1024, 2, (9, 0), (), "StepFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'),
		"Title": (1011, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'),
		"UseMajorTickCount": (1008, 2, (11, 0), (), "UseMajorTickCount", None),
		"Visible": (1005, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Angle": ((1025, LCID, 4, 0),()),
		"AutoScale": ((1012, LCID, 4, 0),()),
		"LogBase": ((1004, LCID, 4, 0),()),
		"MajorTickCount": ((1007, LCID, 4, 0),()),
		"MajorTickStep": ((1006, LCID, 4, 0),()),
		"Max": ((1002, LCID, 4, 0),()),
		"Min": ((1001, LCID, 4, 0),()),
		"MinorTickStep": ((1003, LCID, 4, 0),()),
		"Position": ((1013, LCID, 4, 0),()),
		"Staggered": ((1026, LCID, 4, 0),()),
		"UseMajorTickCount": ((1008, LCID, 4, 0),()),
		"Visible": ((1005, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IAxisY(DispatchBaseClass):
	'''IAxisY'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28398}')
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
		return self._ApplyTypes_(*(1025, 2, (3, 0), (), "Angle", '{F8C24AB7-D222-4646-9F6D-BE4D01CA49FC}'))
	def _get_AutoScale(self):
		return self._ApplyTypes_(*(1012, 2, (11, 0), (), "AutoScale", None))
	def _get_Grid(self):
		return self._ApplyTypes_(*(1021, 2, (9, 0), (), "Grid", '{4DE0B045-C16A-46E4-A238-E70556CE1A4F}'))
	def _get_LabelsFormat(self):
		return self._ApplyTypes_(*(1022, 2, (9, 0), (), "LabelsFormat", '{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}'))
	def _get_Line(self):
		return self._ApplyTypes_(*(1023, 2, (9, 0), (), "Line", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}'))
	def _get_LogBase(self):
		return self._ApplyTypes_(*(1004, 2, (5, 0), (), "LogBase", None))
	def _get_MajorTickCount(self):
		return self._ApplyTypes_(*(1007, 2, (3, 0), (), "MajorTickCount", None))
	def _get_MajorTickStep(self):
		return self._ApplyTypes_(*(1006, 2, (5, 0), (), "MajorTickStep", None))
	def _get_Max(self):
		return self._ApplyTypes_(*(1002, 2, (5, 0), (), "Max", None))
	def _get_Min(self):
		return self._ApplyTypes_(*(1001, 2, (5, 0), (), "Min", None))
	def _get_MinorTickStep(self):
		return self._ApplyTypes_(*(1003, 2, (5, 0), (), "MinorTickStep", None))
	def _get_Pane(self):
		return self._ApplyTypes_(*(2001, 2, (3, 0), (), "Pane", None))
	def _get_Position(self):
		return self._ApplyTypes_(*(1013, 2, (3, 0), (), "Position", '{E0E92E5B-7E01-4C8D-996B-349F51234E22}'))
	def _get_Staggered(self):
		return self._ApplyTypes_(*(1026, 2, (11, 0), (), "Staggered", None))
	def _get_StepFont(self):
		return self._ApplyTypes_(*(1024, 2, (9, 0), (), "StepFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'))
	def _get_Title(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'))
	def _get_UseMajorTickCount(self):
		return self._ApplyTypes_(*(1008, 2, (11, 0), (), "UseMajorTickCount", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(1005, 2, (11, 0), (), "Visible", None))

	def _set_Angle(self, value):
		if "Angle" in self.__dict__: self.__dict__["Angle"] = value; return
		self._oleobj_.Invoke(*((1025, LCID, 4, 0) + (value,) + ()))
	def _set_AutoScale(self, value):
		if "AutoScale" in self.__dict__: self.__dict__["AutoScale"] = value; return
		self._oleobj_.Invoke(*((1012, LCID, 4, 0) + (value,) + ()))
	def _set_LogBase(self, value):
		if "LogBase" in self.__dict__: self.__dict__["LogBase"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_MajorTickCount(self, value):
		if "MajorTickCount" in self.__dict__: self.__dict__["MajorTickCount"] = value; return
		self._oleobj_.Invoke(*((1007, LCID, 4, 0) + (value,) + ()))
	def _set_MajorTickStep(self, value):
		if "MajorTickStep" in self.__dict__: self.__dict__["MajorTickStep"] = value; return
		self._oleobj_.Invoke(*((1006, LCID, 4, 0) + (value,) + ()))
	def _set_Max(self, value):
		if "Max" in self.__dict__: self.__dict__["Max"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_Min(self, value):
		if "Min" in self.__dict__: self.__dict__["Min"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_MinorTickStep(self, value):
		if "MinorTickStep" in self.__dict__: self.__dict__["MinorTickStep"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_Pane(self, value):
		if "Pane" in self.__dict__: self.__dict__["Pane"] = value; return
		self._oleobj_.Invoke(*((2001, LCID, 4, 0) + (value,) + ()))
	def _set_Position(self, value):
		if "Position" in self.__dict__: self.__dict__["Position"] = value; return
		self._oleobj_.Invoke(*((1013, LCID, 4, 0) + (value,) + ()))
	def _set_Staggered(self, value):
		if "Staggered" in self.__dict__: self.__dict__["Staggered"] = value; return
		self._oleobj_.Invoke(*((1026, LCID, 4, 0) + (value,) + ()))
	def _set_UseMajorTickCount(self, value):
		if "UseMajorTickCount" in self.__dict__: self.__dict__["UseMajorTickCount"] = value; return
		self._oleobj_.Invoke(*((1008, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((1005, LCID, 4, 0) + (value,) + ()))

	Angle = property(_get_Angle, _set_Angle)
	'''
	Change the angle of the axis labels.

	:type: recurdyn.Chart.AxisAngleType
	'''
	AutoScale = property(_get_AutoScale, _set_AutoScale)
	'''
	always recalculate the specified Axis scale values (Min, Max) when new values are set to the chart.

	:type: bool
	'''
	Grid = property(_get_Grid, None)
	'''
	Allows customization of grid lines by providing access to the supported members of the Grids.

	:type: recurdyn.Chart.IGrid
	'''
	LabelsFormat = property(_get_LabelsFormat, None)
	'''
	Used to format the labels displayed on the selected axis.

	:type: recurdyn.Chart.IValueFormat
	'''
	Line = property(_get_Line, None)
	'''
	Allows you to apply supported Line class members to a selected axis line.

	:type: recurdyn.Chart.ILine
	'''
	LogBase = property(_get_LogBase, _set_LogBase)
	'''
	Used to set a logarithmic scale for a numerical axis and recalculate the values as powers equal to the setting of this property.

	:type: float
	'''
	MajorTickCount = property(_get_MajorTickCount, _set_MajorTickCount)
	'''
	Specifies the number of major tick marks and gridlines on the selected axis.

	:type: int
	'''
	MajorTickStep = property(_get_MajorTickStep, _set_MajorTickStep)
	'''
	Specifies the interval of major tick marks and gridlines on the selected axis, aka Step.

	:type: float
	'''
	Max = property(_get_Max, _set_Max)
	'''
	Defines the maximum value of a specific axis.

	:type: float
	'''
	Min = property(_get_Min, _set_Min)
	'''
	Defines the minimum value of a selected axis.

	:type: float
	'''
	MinorTickStep = property(_get_MinorTickStep, _set_MinorTickStep)
	'''
	Specifies the increment you want between minor tick marks and minor gridlines (if they are displayed) on the selected axis, aka MinorStep.

	:type: float
	'''
	Pane = property(_get_Pane, _set_Pane)
	'''
	an integer value specifying the Pane for an Y Axis object.

	:type: int
	'''
	Position = property(_get_Position, _set_Position)
	'''
	Specifies the placement of the axis labels and tick marks relative to the chart.

	:type: recurdyn.Chart.AxisPositionType
	'''
	Staggered = property(_get_Staggered, _set_Staggered)
	'''
	Use staggered labels.

	:type: bool
	'''
	StepFont = property(_get_StepFont, None)
	'''
	the font of the axis step number

	:type: recurdyn.Chart.IChartFont
	'''
	Title = property(_get_Title, None)
	'''
	the title for a specific axis.

	:type: recurdyn.Chart.ITitle
	'''
	UseMajorTickCount = property(_get_UseMajorTickCount, _set_UseMajorTickCount)
	'''
	Use MajorTickCount or MajorTickStep for the major tick marks and gridlines on the selected axis.

	:type: bool
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	Shows or hides the lines, labels, tick marks and grids for the selected axis.

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Angle": _set_Angle,
		"_set_AutoScale": _set_AutoScale,
		"_set_LogBase": _set_LogBase,
		"_set_MajorTickCount": _set_MajorTickCount,
		"_set_MajorTickStep": _set_MajorTickStep,
		"_set_Max": _set_Max,
		"_set_Min": _set_Min,
		"_set_MinorTickStep": _set_MinorTickStep,
		"_set_Pane": _set_Pane,
		"_set_Position": _set_Position,
		"_set_Staggered": _set_Staggered,
		"_set_UseMajorTickCount": _set_UseMajorTickCount,
		"_set_Visible": _set_Visible,
	}
	_prop_map_get_ = {
		"Angle": (1025, 2, (3, 0), (), "Angle", '{F8C24AB7-D222-4646-9F6D-BE4D01CA49FC}'),
		"AutoScale": (1012, 2, (11, 0), (), "AutoScale", None),
		"Grid": (1021, 2, (9, 0), (), "Grid", '{4DE0B045-C16A-46E4-A238-E70556CE1A4F}'),
		"LabelsFormat": (1022, 2, (9, 0), (), "LabelsFormat", '{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}'),
		"Line": (1023, 2, (9, 0), (), "Line", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}'),
		"LogBase": (1004, 2, (5, 0), (), "LogBase", None),
		"MajorTickCount": (1007, 2, (3, 0), (), "MajorTickCount", None),
		"MajorTickStep": (1006, 2, (5, 0), (), "MajorTickStep", None),
		"Max": (1002, 2, (5, 0), (), "Max", None),
		"Min": (1001, 2, (5, 0), (), "Min", None),
		"MinorTickStep": (1003, 2, (5, 0), (), "MinorTickStep", None),
		"Pane": (2001, 2, (3, 0), (), "Pane", None),
		"Position": (1013, 2, (3, 0), (), "Position", '{E0E92E5B-7E01-4C8D-996B-349F51234E22}'),
		"Staggered": (1026, 2, (11, 0), (), "Staggered", None),
		"StepFont": (1024, 2, (9, 0), (), "StepFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'),
		"Title": (1011, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'),
		"UseMajorTickCount": (1008, 2, (11, 0), (), "UseMajorTickCount", None),
		"Visible": (1005, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Angle": ((1025, LCID, 4, 0),()),
		"AutoScale": ((1012, LCID, 4, 0),()),
		"LogBase": ((1004, LCID, 4, 0),()),
		"MajorTickCount": ((1007, LCID, 4, 0),()),
		"MajorTickStep": ((1006, LCID, 4, 0),()),
		"Max": ((1002, LCID, 4, 0),()),
		"Min": ((1001, LCID, 4, 0),()),
		"MinorTickStep": ((1003, LCID, 4, 0),()),
		"Pane": ((2001, LCID, 4, 0),()),
		"Position": ((1013, LCID, 4, 0),()),
		"Staggered": ((1026, LCID, 4, 0),()),
		"UseMajorTickCount": ((1008, LCID, 4, 0),()),
		"Visible": ((1005, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChart(DispatchBaseClass):
	'''IChart'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28395}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def DeleteSeries(self, uiSeriesIndex):
		'''
		Delete series with the index
		
		:param uiSeriesIndex: int
		'''
		return self._oleobj_.InvokeTypes(1053, LCID, 1, (24, 0), ((19, 1),),uiSeriesIndex
			)


	def Get3D(self):
		'''
		Return the 3D setting of the chart.
		
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(1034, LCID, 1, (11, 0), (),)


	def GetAddtionalYAxis(self):
		'''
		Returns a additional y axis.
		
		:rtype: recurdyn.Chart.IAxisY
		'''
		ret = self._oleobj_.InvokeTypes(1032, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'GetAddtionalYAxis', '{6EFBEC37-9BE6-43D4-8F59-36391BF28398}')
		return ret

	def GetAngleX(self):
		'''
		Return the degree of the view angle X
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(1040, LCID, 1, (3, 0), (),)


	def GetAngleY(self):
		'''
		Return the degree of the view angle Y
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(1042, LCID, 1, (3, 0), (),)


	def GetAxisY(self, index):
		'''
		Returns a indexed y axis.
		
		:param index: int
		:rtype: recurdyn.Chart.IAxisY
		'''
		ret = self._oleobj_.InvokeTypes(1018, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetAxisY', '{6EFBEC37-9BE6-43D4-8F59-36391BF28398}')
		return ret

	def GetCluster(self):
		'''
		Return cluster setting of the chart.
		
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(1038, LCID, 1, (11, 0), (),)


	def GetLineStyle(self):
		'''
		Get the Line Style of the Chart
		
		:rtype: recurdyn.Chart.LineType
		'''
		return self._oleobj_.InvokeTypes(1045, LCID, 1, (3, 0), (),)


	def GetLineWidth(self):
		'''
		Get the line width of chart
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(1051, LCID, 1, (3, 0), (),)


	def GetPane(self, index):
		'''
		Returns a indexed pane.
		
		:param index: int
		:rtype: recurdyn.Chart.IPane
		'''
		ret = self._oleobj_.InvokeTypes(1019, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetPane', '{6EFBEC37-9BE6-43D4-8F59-36391BF28399}')
		return ret

	def GetPlotDataWithSeriesIndex(self, uiSeriesIndex):
		'''
		Get plot data with sereis index
		
		:param uiSeriesIndex: int
		:rtype: list[float]
		'''
		return self._ApplyTypes_(1052, 1, (8197, 0), ((19, 1),), 'GetPlotDataWithSeriesIndex', None,uiSeriesIndex
			)


	def GetPlotDataXWithSeriesIndex(self, uiSeriesIndex):
		'''
		Get plot data X with sereis index
		
		:param uiSeriesIndex: int
		:rtype: list[float]
		'''
		return self._ApplyTypes_(1054, 1, (8197, 0), ((19, 1),), 'GetPlotDataXWithSeriesIndex', None,uiSeriesIndex
			)


	def GetSeries(self, index):
		'''
		Returns a indexed series attribute.
		
		:param index: int
		:rtype: recurdyn.Chart.ISeries
		'''
		ret = self._oleobj_.InvokeTypes(1021, LCID, 1, (9, 0), ((3, 1),),index
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetSeries', '{6EFBEC37-9BE6-43D4-8F59-36391BF2839B}')
		return ret

	def GetView3D(self):
		'''
		Return the 3D View setting of the chart.
		
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(1036, LCID, 1, (11, 0), (),)


	def GetView3DDepth(self):
		'''
		Get the depth of the series in 3D Chart
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(1047, LCID, 1, (3, 0), (),)


	def GetVolume(self):
		'''
		Get the gap between two series in 3D Chart
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(1049, LCID, 1, (2, 0), (),)


	def Invalidate(self):
		'''
		Invalidate method
		'''
		return self._oleobj_.InvokeTypes(1055, LCID, 1, (24, 0), (),)


	def RecalculateScale(self):
		'''
		calculate the Min, Max and Step for the axes. this method reads the entire data array, so abusing this method could affect the performance of your application
		'''
		return self._oleobj_.InvokeTypes(1031, LCID, 1, (24, 0), (),)


	def Set3D(self, Val):
		'''
		Set 3D setting of the chart.
		
		:param Val: bool
		'''
		return self._oleobj_.InvokeTypes(1033, LCID, 1, (24, 0), ((11, 1),),Val
			)


	def SetAngleX(self, Val):
		'''
		Set the view angle X in degree
		
		:param Val: int
		'''
		return self._oleobj_.InvokeTypes(1039, LCID, 1, (24, 0), ((3, 1),),Val
			)


	def SetAngleY(self, Val):
		'''
		Set the view angle Y in degree
		
		:param Val: int
		'''
		return self._oleobj_.InvokeTypes(1041, LCID, 1, (24, 0), ((3, 1),),Val
			)


	def SetCluster(self, Val):
		'''
		Set cluster of the chart.
		
		:param Val: bool
		'''
		return self._oleobj_.InvokeTypes(1037, LCID, 1, (24, 0), ((11, 1),),Val
			)


	def SetLineStyle(self, dashStyle):
		'''
		Set the Line Style of the Chart
		
		:param dashStyle: LineType
		'''
		return self._oleobj_.InvokeTypes(1044, LCID, 1, (24, 0), ((3, 1),),dashStyle
			)


	def SetLineWidth(self, lLineWidth):
		'''
		Set the line width of chart
		
		:param lLineWidth: int
		'''
		return self._oleobj_.InvokeTypes(1050, LCID, 1, (24, 0), ((3, 1),),lLineWidth
			)


	def SetVeiw3DDepth(self, uiDepth):
		'''
		Set the depth of the series in 3D Chart
		
		:param uiDepth: int
		'''
		return self._oleobj_.InvokeTypes(1046, LCID, 1, (24, 0), ((3, 1),),uiDepth
			)


	def SetView3D(self, Val):
		'''
		Set 3D View setting of the chart.
		
		:param Val: bool
		'''
		return self._oleobj_.InvokeTypes(1035, LCID, 1, (24, 0), ((11, 1),),Val
			)


	def SetVolume(self, uiVolume):
		'''
		Set the gap between two series in 3D Chart
		
		:param uiVolume: int
		'''
		return self._oleobj_.InvokeTypes(1048, LCID, 1, (24, 0), ((2, 1),),uiVolume
			)


	def _get_AxisX(self):
		return self._ApplyTypes_(*(1012, 2, (9, 0), (), "AxisX", '{6EFBEC37-9BE6-43D4-8F59-36391BF28397}'))
	def _get_AxisY(self):
		return self._ApplyTypes_(*(1013, 2, (9, 0), (), "AxisY", '{6EFBEC37-9BE6-43D4-8F59-36391BF28398}'))
	def _get_AxisY2(self):
		return self._ApplyTypes_(*(1014, 2, (9, 0), (), "AxisY2", '{6EFBEC37-9BE6-43D4-8F59-36391BF28398}'))
	def _get_BackColor(self):
		return self._ApplyTypes_(*(1002, 2, (19, 0), (), "BackColor", None))
	def _get_BackgroundImage(self):
		return self._ApplyTypes_(*(1005, 2, (8, 0), (), "BackgroundImage", None))
	def _get_GalleryType(self):
		return self._ApplyTypes_(*(1001, 2, (3, 0), (), "GalleryType", '{A3BCD2E7-2B76-49DC-BA19-D5D017A3E070}'))
	def _get_InsideColor(self):
		return self._ApplyTypes_(*(1003, 2, (19, 0), (), "InsideColor", None))
	def _get_LegendBox(self):
		return self._ApplyTypes_(*(1011, 2, (9, 0), (), "LegendBox", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839A}'))
	def _get_SeriesCount(self):
		return self._ApplyTypes_(*(1020, 2, (3, 0), (), "SeriesCount", None))
	def _get_Title(self):
		return self._ApplyTypes_(*(1015, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'))
	def _get_UseBackgroundImage(self):
		return self._ApplyTypes_(*(1004, 2, (11, 0), (), "UseBackgroundImage", None))

	def _set_BackColor(self, value):
		if "BackColor" in self.__dict__: self.__dict__["BackColor"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_BackgroundImage(self, value):
		if "BackgroundImage" in self.__dict__: self.__dict__["BackgroundImage"] = value; return
		self._oleobj_.Invoke(*((1005, LCID, 4, 0) + (value,) + ()))
	def _set_GalleryType(self, value):
		if "GalleryType" in self.__dict__: self.__dict__["GalleryType"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_InsideColor(self, value):
		if "InsideColor" in self.__dict__: self.__dict__["InsideColor"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_UseBackgroundImage(self, value):
		if "UseBackgroundImage" in self.__dict__: self.__dict__["UseBackgroundImage"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))

	AxisX = property(_get_AxisX, None)
	'''
	Assigns properties specifically to the primary X axis.

	:type: recurdyn.Chart.IAxisX
	'''
	AxisY = property(_get_AxisY, None)
	'''
	Assigns properties specifically to the primary Y axis of the chart.

	:type: recurdyn.Chart.IAxisY
	'''
	AxisY2 = property(_get_AxisY2, None)
	'''
	Assigns properties specifically to the secondary Y axis of the chart.

	:type: recurdyn.Chart.IAxisY
	'''
	BackColor = property(_get_BackColor, _set_BackColor)
	'''
	the background color of the chart.

	:type: int
	'''
	BackgroundImage = property(_get_BackgroundImage, _set_BackgroundImage)
	'''
	the fulll path of background image.

	:type: str
	'''
	GalleryType = property(_get_GalleryType, _set_GalleryType)
	'''
	the gallery type of the chart.

	:type: recurdyn.Chart.GalleryType
	'''
	InsideColor = property(_get_InsideColor, _set_InsideColor)
	'''
	the inside color of the chart.

	:type: int
	'''
	LegendBox = property(_get_LegendBox, None)
	'''
	Allows you to acces the legend box of the chart.

	:type: recurdyn.Chart.ILegendBox
	'''
	SeriesCount = property(_get_SeriesCount, None)
	'''
	the number of series allocated for the chart.

	:type: int
	'''
	Title = property(_get_Title, None)
	'''
	the title for a chart. same as GetTitleCollection(0).

	:type: recurdyn.Chart.ITitle
	'''
	UseBackgroundImage = property(_get_UseBackgroundImage, _set_UseBackgroundImage)
	'''
	Use background image flag.

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_BackColor": _set_BackColor,
		"_set_BackgroundImage": _set_BackgroundImage,
		"_set_GalleryType": _set_GalleryType,
		"_set_InsideColor": _set_InsideColor,
		"_set_UseBackgroundImage": _set_UseBackgroundImage,
	}
	_prop_map_get_ = {
		"AxisX": (1012, 2, (9, 0), (), "AxisX", '{6EFBEC37-9BE6-43D4-8F59-36391BF28397}'),
		"AxisY": (1013, 2, (9, 0), (), "AxisY", '{6EFBEC37-9BE6-43D4-8F59-36391BF28398}'),
		"AxisY2": (1014, 2, (9, 0), (), "AxisY2", '{6EFBEC37-9BE6-43D4-8F59-36391BF28398}'),
		"BackColor": (1002, 2, (19, 0), (), "BackColor", None),
		"BackgroundImage": (1005, 2, (8, 0), (), "BackgroundImage", None),
		"GalleryType": (1001, 2, (3, 0), (), "GalleryType", '{A3BCD2E7-2B76-49DC-BA19-D5D017A3E070}'),
		"InsideColor": (1003, 2, (19, 0), (), "InsideColor", None),
		"LegendBox": (1011, 2, (9, 0), (), "LegendBox", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839A}'),
		"SeriesCount": (1020, 2, (3, 0), (), "SeriesCount", None),
		"Title": (1015, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'),
		"UseBackgroundImage": (1004, 2, (11, 0), (), "UseBackgroundImage", None),
	}
	_prop_map_put_ = {
		"BackColor": ((1002, LCID, 4, 0),()),
		"BackgroundImage": ((1005, LCID, 4, 0),()),
		"GalleryType": ((1001, LCID, 4, 0),()),
		"InsideColor": ((1003, LCID, 4, 0),()),
		"UseBackgroundImage": ((1004, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChartFont(DispatchBaseClass):
	'''IFont'''
	CLSID = IID('{998544E2-D749-4094-B749-F9BEBB579DB1}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Bold(self):
		return self._ApplyTypes_(*(1003, 2, (11, 0), (), "Bold", None))
	def _get_Italic(self):
		return self._ApplyTypes_(*(1004, 2, (11, 0), (), "Italic", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(1001, 2, (8, 0), (), "Name", None))
	def _get_Size(self):
		return self._ApplyTypes_(*(1002, 2, (3, 0), (), "Size", None))
	def _get_Strikethrough(self):
		return self._ApplyTypes_(*(1006, 2, (11, 0), (), "Strikethrough", None))
	def _get_Underline(self):
		return self._ApplyTypes_(*(1005, 2, (11, 0), (), "Underline", None))

	def _set_Bold(self, value):
		if "Bold" in self.__dict__: self.__dict__["Bold"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_Italic(self, value):
		if "Italic" in self.__dict__: self.__dict__["Italic"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_Size(self, value):
		if "Size" in self.__dict__: self.__dict__["Size"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_Strikethrough(self, value):
		if "Strikethrough" in self.__dict__: self.__dict__["Strikethrough"] = value; return
		self._oleobj_.Invoke(*((1006, LCID, 4, 0) + (value,) + ()))
	def _set_Underline(self, value):
		if "Underline" in self.__dict__: self.__dict__["Underline"] = value; return
		self._oleobj_.Invoke(*((1005, LCID, 4, 0) + (value,) + ()))

	Bold = property(_get_Bold, _set_Bold)
	'''
	the flag of bold type

	:type: bool
	'''
	Italic = property(_get_Italic, _set_Italic)
	'''
	the flag of Italic type

	:type: bool
	'''
	Name = property(_get_Name, _set_Name)
	'''
	the name of the font

	:type: str
	'''
	Size = property(_get_Size, _set_Size)
	'''
	the size of the font

	:type: int
	'''
	Strikethrough = property(_get_Strikethrough, _set_Strikethrough)
	'''
	the flag of Italic type

	:type: bool
	'''
	Underline = property(_get_Underline, _set_Underline)
	'''
	the flag of Italic type

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Bold": _set_Bold,
		"_set_Italic": _set_Italic,
		"_set_Name": _set_Name,
		"_set_Size": _set_Size,
		"_set_Strikethrough": _set_Strikethrough,
		"_set_Underline": _set_Underline,
	}
	_prop_map_get_ = {
		"Bold": (1003, 2, (11, 0), (), "Bold", None),
		"Italic": (1004, 2, (11, 0), (), "Italic", None),
		"Name": (1001, 2, (8, 0), (), "Name", None),
		"Size": (1002, 2, (3, 0), (), "Size", None),
		"Strikethrough": (1006, 2, (11, 0), (), "Strikethrough", None),
		"Underline": (1005, 2, (11, 0), (), "Underline", None),
	}
	_prop_map_put_ = {
		"Bold": ((1003, LCID, 4, 0),()),
		"Italic": ((1004, LCID, 4, 0),()),
		"Name": ((1001, LCID, 4, 0),()),
		"Size": ((1002, LCID, 4, 0),()),
		"Strikethrough": ((1006, LCID, 4, 0),()),
		"Underline": ((1005, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IDataValue(DispatchBaseClass):
	'''IDataValue'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF283A1}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def SetX(self, ISeries, IPoint, arg2):
		'''
		Allows you to set X-Values for specific point of XY plots.
		
		:param ISeries: int
		:param IPoint: int
		'''
		return self._oleobj_.InvokeTypes(1003, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),ISeries
			, IPoint, arg2)


	def SetY(self, ISeries, IPoint, arg2):
		'''
		Allows you to access the Y coordinates of the data points
		
		:param ISeries: int
		:param IPoint: int
		'''
		return self._oleobj_.InvokeTypes(1004, LCID, 4, (24, 0), ((3, 1), (3, 1), (5, 1)),ISeries
			, IPoint, arg2)


	def X(self, ISeries, IPoint):
		'''
		Allows you to set X-Values for specific point of XY plots.
		
		:param ISeries: int
		:param IPoint: int
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(1003, LCID, 2, (5, 0), ((3, 1), (3, 1)),ISeries
			, IPoint)


	def Y(self, ISeries, IPoint):
		'''
		Allows you to access the Y coordinates of the data points
		
		:param ISeries: int
		:param IPoint: int
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(1004, LCID, 2, (5, 0), ((3, 1), (3, 1)),ISeries
			, IPoint)


	def _get_PointsCount(self):
		return self._ApplyTypes_(*(1002, 2, (3, 0), (), "PointsCount", None))
	def _get_SeriesCount(self):
		return self._ApplyTypes_(*(1001, 2, (3, 0), (), "SeriesCount", None))

	def _set_PointsCount(self, value):
		if "PointsCount" in self.__dict__: self.__dict__["PointsCount"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_SeriesCount(self, value):
		if "SeriesCount" in self.__dict__: self.__dict__["SeriesCount"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))

	PointsCount = property(_get_PointsCount, _set_PointsCount)
	'''
	the number of data points per series in a chart.

	:type: int
	'''
	SeriesCount = property(_get_SeriesCount, _set_SeriesCount)
	'''
	the number of series allocated for the chart.

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_PointsCount": _set_PointsCount,
		"_set_SeriesCount": _set_SeriesCount,
	}
	_prop_map_get_ = {
		"PointsCount": (1002, 2, (3, 0), (), "PointsCount", None),
		"SeriesCount": (1001, 2, (3, 0), (), "SeriesCount", None),
	}
	_prop_map_put_ = {
		"PointsCount": ((1002, LCID, 4, 0),()),
		"SeriesCount": ((1001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IGrid(DispatchBaseClass):
	'''IGrid'''
	CLSID = IID('{4DE0B045-C16A-46E4-A238-E70556CE1A4F}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Major(self):
		return self._ApplyTypes_(*(1001, 2, (9, 0), (), "Major", '{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}'))
	def _get_Minor(self):
		return self._ApplyTypes_(*(1002, 2, (9, 0), (), "Minor", '{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}'))

	Major = property(_get_Major, None)
	'''
	Provides access to the GridLine to customize the Mayor Grid.

	:type: recurdyn.Chart.IGridLine
	'''
	Minor = property(_get_Minor, None)
	'''
	Provides access to the GridLine to customize the Minor Grid.

	:type: recurdyn.Chart.IGridLine
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Major": (1001, 2, (9, 0), (), "Major", '{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}'),
		"Minor": (1002, 2, (9, 0), (), "Minor", '{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}'),
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

class IGridLine(DispatchBaseClass):
	'''IGridLine'''
	CLSID = IID('{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}')
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
		return self._ApplyTypes_(*(1002, 2, (19, 0), (), "Color", None))
	def _get_Style(self):
		return self._ApplyTypes_(*(1003, 2, (3, 0), (), "Style", '{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}'))
	def _get_Visible(self):
		return self._ApplyTypes_(*(2001, 2, (11, 0), (), "Visible", None))
	def _get_Width(self):
		return self._ApplyTypes_(*(1001, 2, (3, 0), (), "Width", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_Style(self, value):
		if "Style" in self.__dict__: self.__dict__["Style"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((2001, LCID, 4, 0) + (value,) + ()))
	def _set_Width(self, value):
		if "Width" in self.__dict__: self.__dict__["Width"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	the line color for a selected line.

	:type: int
	'''
	Style = property(_get_Style, _set_Style)
	'''
	the line style for a selected line.

	:type: recurdyn.Chart.LineType
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	a value indicating whether the grid line for the selected Gridline will be visible.

	:type: bool
	'''
	Width = property(_get_Width, _set_Width)
	'''
	the line width for a selected line.

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Style": _set_Style,
		"_set_Visible": _set_Visible,
		"_set_Width": _set_Width,
	}
	_prop_map_get_ = {
		"Color": (1002, 2, (19, 0), (), "Color", None),
		"Style": (1003, 2, (3, 0), (), "Style", '{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}'),
		"Visible": (2001, 2, (11, 0), (), "Visible", None),
		"Width": (1001, 2, (3, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((1002, LCID, 4, 0),()),
		"Style": ((1003, LCID, 4, 0),()),
		"Visible": ((2001, LCID, 4, 0),()),
		"Width": ((1001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ILegendBox(DispatchBaseClass):
	'''ILegendBox'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Alignment(self):
		return self._ApplyTypes_(*(1003, 2, (3, 0), (), "Alignment", '{F300F302-97EA-44B9-8DA4-82223B8FA9E1}'))
	def _get_BackColor(self):
		return self._ApplyTypes_(*(1002, 2, (19, 0), (), "BackColor", None))
	def _get_DockedPosition(self):
		return self._ApplyTypes_(*(1005, 2, (3, 0), (), "DockedPosition", '{D30AFB54-1718-42B0-BD22-0CAC3A225D3D}'))
	def _get_TextColor(self):
		return self._ApplyTypes_(*(1004, 2, (19, 0), (), "TextColor", None))
	def _get_TextFont(self):
		return self._ApplyTypes_(*(1006, 2, (9, 0), (), "TextFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'))
	def _get_Visible(self):
		return self._ApplyTypes_(*(1001, 2, (11, 0), (), "Visible", None))

	def _set_Alignment(self, value):
		if "Alignment" in self.__dict__: self.__dict__["Alignment"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_BackColor(self, value):
		if "BackColor" in self.__dict__: self.__dict__["BackColor"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_DockedPosition(self, value):
		if "DockedPosition" in self.__dict__: self.__dict__["DockedPosition"] = value; return
		self._oleobj_.Invoke(*((1005, LCID, 4, 0) + (value,) + ()))
	def _set_TextColor(self, value):
		if "TextColor" in self.__dict__: self.__dict__["TextColor"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))

	Alignment = property(_get_Alignment, _set_Alignment)
	'''
	Allows you to align the content for the legend box.

	:type: recurdyn.Chart.LegendBoxAlignment
	'''
	BackColor = property(_get_BackColor, _set_BackColor)
	'''
	Allows you to set the background color for the selected legend box.

	:type: int
	'''
	DockedPosition = property(_get_DockedPosition, _set_DockedPosition)
	'''
	Set the docked position of the legend box.

	:type: recurdyn.Chart.DockedPositionType
	'''
	TextColor = property(_get_TextColor, _set_TextColor)
	'''
	the color used for the text in the legend box

	:type: int
	'''
	TextFont = property(_get_TextFont, None)
	'''
	the font of the legend

	:type: recurdyn.Chart.IChartFont
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	a value indicating the legend box object should be shown or not.

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Alignment": _set_Alignment,
		"_set_BackColor": _set_BackColor,
		"_set_DockedPosition": _set_DockedPosition,
		"_set_TextColor": _set_TextColor,
		"_set_Visible": _set_Visible,
	}
	_prop_map_get_ = {
		"Alignment": (1003, 2, (3, 0), (), "Alignment", '{F300F302-97EA-44B9-8DA4-82223B8FA9E1}'),
		"BackColor": (1002, 2, (19, 0), (), "BackColor", None),
		"DockedPosition": (1005, 2, (3, 0), (), "DockedPosition", '{D30AFB54-1718-42B0-BD22-0CAC3A225D3D}'),
		"TextColor": (1004, 2, (19, 0), (), "TextColor", None),
		"TextFont": (1006, 2, (9, 0), (), "TextFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'),
		"Visible": (1001, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Alignment": ((1003, LCID, 4, 0),()),
		"BackColor": ((1002, LCID, 4, 0),()),
		"DockedPosition": ((1005, LCID, 4, 0),()),
		"TextColor": ((1004, LCID, 4, 0),()),
		"Visible": ((1001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ILine(DispatchBaseClass):
	'''ILine'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}')
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
		return self._ApplyTypes_(*(1002, 2, (19, 0), (), "Color", None))
	def _get_Style(self):
		return self._ApplyTypes_(*(1003, 2, (3, 0), (), "Style", '{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}'))
	def _get_Width(self):
		return self._ApplyTypes_(*(1001, 2, (3, 0), (), "Width", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_Style(self, value):
		if "Style" in self.__dict__: self.__dict__["Style"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_Width(self, value):
		if "Width" in self.__dict__: self.__dict__["Width"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	the line color for a selected line.

	:type: int
	'''
	Style = property(_get_Style, _set_Style)
	'''
	the line style for a selected line.

	:type: recurdyn.Chart.LineType
	'''
	Width = property(_get_Width, _set_Width)
	'''
	the line width for a selected line.

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_Style": _set_Style,
		"_set_Width": _set_Width,
	}
	_prop_map_get_ = {
		"Color": (1002, 2, (19, 0), (), "Color", None),
		"Style": (1003, 2, (3, 0), (), "Style", '{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}'),
		"Width": (1001, 2, (3, 0), (), "Width", None),
	}
	_prop_map_put_ = {
		"Color": ((1002, LCID, 4, 0),()),
		"Style": ((1003, LCID, 4, 0),()),
		"Width": ((1001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPane(DispatchBaseClass):
	'''IPane'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28399}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_BackColor(self):
		return self._ApplyTypes_(*(1001, 2, (19, 0), (), "BackColor", None))
	def _get_Title(self):
		return self._ApplyTypes_(*(1004, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'))

	def _set_BackColor(self, value):
		if "BackColor" in self.__dict__: self.__dict__["BackColor"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))

	BackColor = property(_get_BackColor, _set_BackColor)
	'''
	the inside color for the selected pane.

	:type: int
	'''
	Title = property(_get_Title, None)
	'''
	the Title object for a selected chart pane.

	:type: recurdyn.Chart.ITitle
	'''

	_prop_map_set_function_ = {
		"_set_BackColor": _set_BackColor,
	}
	_prop_map_get_ = {
		"BackColor": (1001, 2, (19, 0), (), "BackColor", None),
		"Title": (1004, 2, (9, 0), (), "Title", '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}'),
	}
	_prop_map_put_ = {
		"BackColor": ((1001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IPoint(DispatchBaseClass):
	'''IPoint'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839C}')
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

class IPointLabel(DispatchBaseClass):
	'''IPointLabel'''
	CLSID = IID('{85722F51-1CAE-442F-BB40-A969034C6FD0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Alignment(self):
		return self._ApplyTypes_(*(1002, 2, (3, 0), (), "Alignment", '{198D175B-A965-4988-B701-436DCD640111}'))
	def _get_Visible(self):
		return self._ApplyTypes_(*(1001, 2, (11, 0), (), "Visible", None))

	def _set_Alignment(self, value):
		if "Alignment" in self.__dict__: self.__dict__["Alignment"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))

	Alignment = property(_get_Alignment, _set_Alignment)
	'''
	the vertical alignment for the point label.

	:type: recurdyn.Chart.TextAlignment
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	a value indicating if point label should be displayed or not.

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Alignment": _set_Alignment,
		"_set_Visible": _set_Visible,
	}
	_prop_map_get_ = {
		"Alignment": (1002, 2, (3, 0), (), "Alignment", '{198D175B-A965-4988-B701-436DCD640111}'),
		"Visible": (1001, 2, (11, 0), (), "Visible", None),
	}
	_prop_map_put_ = {
		"Alignment": ((1002, LCID, 4, 0),()),
		"Visible": ((1001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ISeries(DispatchBaseClass):
	'''ISeries'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839B}')
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
		return self._ApplyTypes_(*(1003, 2, (19, 0), (), "Color", None))
	def _get_GalleryType(self):
		return self._ApplyTypes_(*(1002, 2, (3, 0), (), "GalleryType", '{A3BCD2E7-2B76-49DC-BA19-D5D017A3E070}'))
	def _get_LineStyle(self):
		return self._ApplyTypes_(*(1010, 2, (3, 0), (), "LineStyle", '{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}'))
	def _get_LineWidth(self):
		return self._ApplyTypes_(*(1011, 2, (3, 0), (), "LineWidth", None))
	def _get_MarkerShape(self):
		return self._ApplyTypes_(*(1005, 2, (3, 0), (), "MarkerShape", '{EA48A837-2A08-4817-9403-2C339113C3C0}'))
	def _get_MarkerSize(self):
		return self._ApplyTypes_(*(1006, 2, (3, 0), (), "MarkerSize", None))
	def _get_Text(self):
		return self._ApplyTypes_(*(1004, 2, (8, 0), (), "Text", None))
	def _get_Visible(self):
		return self._ApplyTypes_(*(1001, 2, (11, 0), (), "Visible", None))
	def _get_YAxis(self):
		return self._ApplyTypes_(*(1009, 2, (9, 0), (), "YAxis", '{6EFBEC37-9BE6-43D4-8F59-36391BF28398}'))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_GalleryType(self, value):
		if "GalleryType" in self.__dict__: self.__dict__["GalleryType"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_LineStyle(self, value):
		if "LineStyle" in self.__dict__: self.__dict__["LineStyle"] = value; return
		self._oleobj_.Invoke(*((1010, LCID, 4, 0) + (value,) + ()))
	def _set_LineWidth(self, value):
		if "LineWidth" in self.__dict__: self.__dict__["LineWidth"] = value; return
		self._oleobj_.Invoke(*((1011, LCID, 4, 0) + (value,) + ()))
	def _set_MarkerShape(self, value):
		if "MarkerShape" in self.__dict__: self.__dict__["MarkerShape"] = value; return
		self._oleobj_.Invoke(*((1005, LCID, 4, 0) + (value,) + ()))
	def _set_MarkerSize(self, value):
		if "MarkerSize" in self.__dict__: self.__dict__["MarkerSize"] = value; return
		self._oleobj_.Invoke(*((1006, LCID, 4, 0) + (value,) + ()))
	def _set_Text(self, value):
		if "Text" in self.__dict__: self.__dict__["Text"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))
	def _set_Visible(self, value):
		if "Visible" in self.__dict__: self.__dict__["Visible"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_YAxis(self, value):
		if "YAxis" in self.__dict__: self.__dict__["YAxis"] = value; return
		self._oleobj_.Invoke(*((1009, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	a Color for the selected series.

	:type: int
	'''
	GalleryType = property(_get_GalleryType, _set_GalleryType)
	'''
	a gallery type for a particular series. All chart types are available in both 2D and 3D modes.

	:type: recurdyn.Chart.GalleryType
	'''
	LineStyle = property(_get_LineStyle, _set_LineStyle)
	'''
	the line style of the series

	:type: recurdyn.Chart.LineType
	'''
	LineWidth = property(_get_LineWidth, _set_LineWidth)
	'''
	the line width of the series

	:type: int
	'''
	MarkerShape = property(_get_MarkerShape, _set_MarkerShape)
	'''
	the type used to paint markers for the selected item.

	:type: recurdyn.Chart.MarkerType
	'''
	MarkerSize = property(_get_MarkerSize, _set_MarkerSize)
	'''
	a value controlling the size of the markers for the selected item. 

	:type: int
	'''
	Text = property(_get_Text, _set_Text)
	'''
	a value for labeling the series.

	:type: str
	'''
	Visible = property(_get_Visible, _set_Visible)
	'''
	a value allowing you to show or hide the series.

	:type: bool
	'''
	YAxis = property(_get_YAxis, _set_YAxis)
	'''
	Gets or Sets AxisY the series is connected to.

	:type: recurdyn.Chart.IAxisY
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_GalleryType": _set_GalleryType,
		"_set_LineStyle": _set_LineStyle,
		"_set_LineWidth": _set_LineWidth,
		"_set_MarkerShape": _set_MarkerShape,
		"_set_MarkerSize": _set_MarkerSize,
		"_set_Text": _set_Text,
		"_set_Visible": _set_Visible,
		"_set_YAxis": _set_YAxis,
	}
	_prop_map_get_ = {
		"Color": (1003, 2, (19, 0), (), "Color", None),
		"GalleryType": (1002, 2, (3, 0), (), "GalleryType", '{A3BCD2E7-2B76-49DC-BA19-D5D017A3E070}'),
		"LineStyle": (1010, 2, (3, 0), (), "LineStyle", '{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}'),
		"LineWidth": (1011, 2, (3, 0), (), "LineWidth", None),
		"MarkerShape": (1005, 2, (3, 0), (), "MarkerShape", '{EA48A837-2A08-4817-9403-2C339113C3C0}'),
		"MarkerSize": (1006, 2, (3, 0), (), "MarkerSize", None),
		"Text": (1004, 2, (8, 0), (), "Text", None),
		"Visible": (1001, 2, (11, 0), (), "Visible", None),
		"YAxis": (1009, 2, (9, 0), (), "YAxis", '{6EFBEC37-9BE6-43D4-8F59-36391BF28398}'),
	}
	_prop_map_put_ = {
		"Color": ((1003, LCID, 4, 0),()),
		"GalleryType": ((1002, LCID, 4, 0),()),
		"LineStyle": ((1010, LCID, 4, 0),()),
		"LineWidth": ((1011, LCID, 4, 0),()),
		"MarkerShape": ((1005, LCID, 4, 0),()),
		"MarkerSize": ((1006, LCID, 4, 0),()),
		"Text": ((1004, LCID, 4, 0),()),
		"Visible": ((1001, LCID, 4, 0),()),
		"YAxis": ((1009, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITitle(DispatchBaseClass):
	'''ITitle'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Alignment(self):
		return self._ApplyTypes_(*(1001, 2, (3, 0), (), "Alignment", '{198D175B-A965-4988-B701-436DCD640111}'))
	def _get_BackColor(self):
		return self._ApplyTypes_(*(1003, 2, (19, 0), (), "BackColor", None))
	def _get_Text(self):
		return self._ApplyTypes_(*(1002, 2, (8, 0), (), "Text", None))
	def _get_TextColor(self):
		return self._ApplyTypes_(*(1004, 2, (19, 0), (), "TextColor", None))
	def _get_TextFont(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "TextFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'))

	def _set_Alignment(self, value):
		if "Alignment" in self.__dict__: self.__dict__["Alignment"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_BackColor(self, value):
		if "BackColor" in self.__dict__: self.__dict__["BackColor"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_Text(self, value):
		if "Text" in self.__dict__: self.__dict__["Text"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_TextColor(self, value):
		if "TextColor" in self.__dict__: self.__dict__["TextColor"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))

	Alignment = property(_get_Alignment, _set_Alignment)
	'''
	Allows you to set the alignment of the specified title.

	:type: recurdyn.Chart.TextAlignment
	'''
	BackColor = property(_get_BackColor, _set_BackColor)
	'''
	the color background of the specified title. 

	:type: int
	'''
	Text = property(_get_Text, _set_Text)
	'''
	the text for the selected title.

	:type: str
	'''
	TextColor = property(_get_TextColor, _set_TextColor)
	'''
	the color of text for the specified title.

	:type: int
	'''
	TextFont = property(_get_TextFont, None)
	'''
	the font of the title text

	:type: recurdyn.Chart.IChartFont
	'''

	_prop_map_set_function_ = {
		"_set_Alignment": _set_Alignment,
		"_set_BackColor": _set_BackColor,
		"_set_Text": _set_Text,
		"_set_TextColor": _set_TextColor,
	}
	_prop_map_get_ = {
		"Alignment": (1001, 2, (3, 0), (), "Alignment", '{198D175B-A965-4988-B701-436DCD640111}'),
		"BackColor": (1003, 2, (19, 0), (), "BackColor", None),
		"Text": (1002, 2, (8, 0), (), "Text", None),
		"TextColor": (1004, 2, (19, 0), (), "TextColor", None),
		"TextFont": (1005, 2, (9, 0), (), "TextFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'),
	}
	_prop_map_put_ = {
		"Alignment": ((1001, LCID, 4, 0),()),
		"BackColor": ((1003, LCID, 4, 0),()),
		"Text": ((1002, LCID, 4, 0),()),
		"TextColor": ((1004, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class ITitleEx(DispatchBaseClass):
	'''ITitleEx'''
	CLSID = IID('{48DE6C5D-FCF4-44FF-9673-9891ABC58E79}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Alignment(self):
		return self._ApplyTypes_(*(1001, 2, (3, 0), (), "Alignment", '{198D175B-A965-4988-B701-436DCD640111}'))
	def _get_BackColor(self):
		return self._ApplyTypes_(*(1003, 2, (19, 0), (), "BackColor", None))
	def _get_Text(self):
		return self._ApplyTypes_(*(1002, 2, (8, 0), (), "Text", None))
	def _get_TextColor(self):
		return self._ApplyTypes_(*(1004, 2, (19, 0), (), "TextColor", None))
	def _get_TextFont(self):
		return self._ApplyTypes_(*(1005, 2, (9, 0), (), "TextFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'))

	def _set_Alignment(self, value):
		if "Alignment" in self.__dict__: self.__dict__["Alignment"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))
	def _set_BackColor(self, value):
		if "BackColor" in self.__dict__: self.__dict__["BackColor"] = value; return
		self._oleobj_.Invoke(*((1003, LCID, 4, 0) + (value,) + ()))
	def _set_Text(self, value):
		if "Text" in self.__dict__: self.__dict__["Text"] = value; return
		self._oleobj_.Invoke(*((1002, LCID, 4, 0) + (value,) + ()))
	def _set_TextColor(self, value):
		if "TextColor" in self.__dict__: self.__dict__["TextColor"] = value; return
		self._oleobj_.Invoke(*((1004, LCID, 4, 0) + (value,) + ()))

	Alignment = property(_get_Alignment, _set_Alignment)
	'''
	Allows you to set the alignment of the specified title.

	:type: recurdyn.Chart.TextAlignment
	'''
	BackColor = property(_get_BackColor, _set_BackColor)
	'''
	the color background of the specified title. 

	:type: int
	'''
	Text = property(_get_Text, _set_Text)
	'''
	the text for the selected title.

	:type: str
	'''
	TextColor = property(_get_TextColor, _set_TextColor)
	'''
	the color of text for the specified title.

	:type: int
	'''
	TextFont = property(_get_TextFont, None)
	'''
	the font of the title text

	:type: recurdyn.Chart.IChartFont
	'''

	_prop_map_set_function_ = {
		"_set_Alignment": _set_Alignment,
		"_set_BackColor": _set_BackColor,
		"_set_Text": _set_Text,
		"_set_TextColor": _set_TextColor,
	}
	_prop_map_get_ = {
		"Alignment": (1001, 2, (3, 0), (), "Alignment", '{198D175B-A965-4988-B701-436DCD640111}'),
		"BackColor": (1003, 2, (19, 0), (), "BackColor", None),
		"Text": (1002, 2, (8, 0), (), "Text", None),
		"TextColor": (1004, 2, (19, 0), (), "TextColor", None),
		"TextFont": (1005, 2, (9, 0), (), "TextFont", '{998544E2-D749-4094-B749-F9BEBB579DB1}'),
	}
	_prop_map_put_ = {
		"Alignment": ((1001, LCID, 4, 0),()),
		"BackColor": ((1003, LCID, 4, 0),()),
		"Text": ((1002, LCID, 4, 0),()),
		"TextColor": ((1004, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IValueFormat(DispatchBaseClass):
	'''IValueFormat'''
	CLSID = IID('{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Decimals(self):
		return self._ApplyTypes_(*(1001, 2, (3, 0), (), "Decimals", None))

	def _set_Decimals(self, value):
		if "Decimals" in self.__dict__: self.__dict__["Decimals"] = value; return
		self._oleobj_.Invoke(*((1001, LCID, 4, 0) + (value,) + ()))

	Decimals = property(_get_Decimals, _set_Decimals)
	'''
	the number of decimals for the selected label, mouseover tip or value.

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_Decimals": _set_Decimals,
	}
	_prop_map_get_ = {
		"Decimals": (1001, 2, (3, 0), (), "Decimals", None),
	}
	_prop_map_put_ = {
		"Decimals": ((1001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

IAxis_vtables_dispatch_ = 1
IAxis_vtables_ = [
	(( 'Min' , 'pVal' , ), 1001, (1001, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Min' , 'pVal' , ), 1001, (1001, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Max' , 'pVal' , ), 1002, (1002, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Max' , 'pVal' , ), 1002, (1002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MinorTickStep' , 'pVal' , ), 1003, (1003, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MinorTickStep' , 'pVal' , ), 1003, (1003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'LogBase' , 'pVal' , ), 1004, (1004, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'LogBase' , 'pVal' , ), 1004, (1004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 1005, (1005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 1005, (1005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'MajorTickStep' , 'pVal' , ), 1006, (1006, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MajorTickStep' , 'pVal' , ), 1006, (1006, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'MajorTickCount' , 'pVal' , ), 1007, (1007, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'MajorTickCount' , 'pVal' , ), 1007, (1007, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseMajorTickCount' , 'pVal' , ), 1008, (1008, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseMajorTickCount' , 'pVal' , ), 1008, (1008, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pVal' , ), 1011, (1011, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'AutoScale' , 'pVal' , ), 1012, (1012, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'AutoScale' , 'pVal' , ), 1012, (1012, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 1013, (1013, (), [ (3, 1, None, "IID('{E0E92E5B-7E01-4C8D-996B-349F51234E22}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Position' , 'pVal' , ), 1013, (1013, (), [ (16387, 10, None, "IID('{E0E92E5B-7E01-4C8D-996B-349F51234E22}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Grid' , 'pVal' , ), 1021, (1021, (), [ (16393, 10, None, "IID('{4DE0B045-C16A-46E4-A238-E70556CE1A4F}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'LabelsFormat' , 'pVal' , ), 1022, (1022, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Line' , 'pVal' , ), 1023, (1023, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'StepFont' , 'font' , ), 1024, (1024, (), [ (16393, 10, None, "IID('{998544E2-D749-4094-B749-F9BEBB579DB1}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'pVal' , ), 1025, (1025, (), [ (3, 1, None, "IID('{F8C24AB7-D222-4646-9F6D-BE4D01CA49FC}')") , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Angle' , 'pVal' , ), 1025, (1025, (), [ (16387, 10, None, "IID('{F8C24AB7-D222-4646-9F6D-BE4D01CA49FC}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'Staggered' , 'pVal' , ), 1026, (1026, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'Staggered' , 'pVal' , ), 1026, (1026, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

IAxisX_vtables_dispatch_ = 1
IAxisX_vtables_ = [
]

IAxisY_vtables_dispatch_ = 1
IAxisY_vtables_ = [
	(( 'Pane' , 'pVal' , ), 2001, (2001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Pane' , 'pVal' , ), 2001, (2001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
]

IChart_vtables_dispatch_ = 1
IChart_vtables_ = [
	(( 'GalleryType' , 'pVal' , ), 1001, (1001, (), [ (3, 1, None, "IID('{A3BCD2E7-2B76-49DC-BA19-D5D017A3E070}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'GalleryType' , 'pVal' , ), 1001, (1001, (), [ (16387, 10, None, "IID('{A3BCD2E7-2B76-49DC-BA19-D5D017A3E070}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'pVal' , ), 1002, (1002, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'pVal' , ), 1002, (1002, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'InsideColor' , 'pVal' , ), 1003, (1003, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'InsideColor' , 'pVal' , ), 1003, (1003, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseBackgroundImage' , 'pVal' , ), 1004, (1004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseBackgroundImage' , 'pVal' , ), 1004, (1004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'BackgroundImage' , 'pVal' , ), 1005, (1005, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'BackgroundImage' , 'pVal' , ), 1005, (1005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'LegendBox' , 'pVal' , ), 1011, (1011, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839A}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'AxisX' , 'pVal' , ), 1012, (1012, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28397}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'AxisY' , 'pVal' , ), 1013, (1013, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28398}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AxisY2' , 'pVal' , ), 1014, (1014, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28398}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'pVal' , ), 1015, (1015, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'GetAxisY' , 'index' , 'ppVal' , ), 1018, (1018, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28398}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'GetPane' , 'index' , 'ppVal' , ), 1019, (1019, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28399}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SeriesCount' , 'pVal' , ), 1020, (1020, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'GetSeries' , 'index' , 'ppVal' , ), 1021, (1021, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839B}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RecalculateScale' , ), 1031, (1031, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'GetAddtionalYAxis' , 'ppVal' , ), 1032, (1032, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28398}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Set3D' , 'Val' , ), 1033, (1033, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Get3D' , 'pVal' , ), 1034, (1034, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'SetView3D' , 'Val' , ), 1035, (1035, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'GetView3D' , 'pVal' , ), 1036, (1036, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'SetCluster' , 'Val' , ), 1037, (1037, (), [ (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'GetCluster' , 'pVal' , ), 1038, (1038, (), [ (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'SetAngleX' , 'Val' , ), 1039, (1039, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'GetAngleX' , 'pVal' , ), 1040, (1040, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'SetAngleY' , 'Val' , ), 1041, (1041, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'GetAngleY' , 'pVal' , ), 1042, (1042, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'SetLineStyle' , 'dashStyle' , ), 1044, (1044, (), [ (3, 1, None, "IID('{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'GetLineStyle' , 'pDashStyle' , ), 1045, (1045, (), [ (16387, 10, None, "IID('{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'SetVeiw3DDepth' , 'uiDepth' , ), 1046, (1046, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'GetView3DDepth' , 'pVal' , ), 1047, (1047, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'SetVolume' , 'uiVolume' , ), 1048, (1048, (), [ (2, 1, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'GetVolume' , 'pVal' , ), 1049, (1049, (), [ (16386, 10, None, None) , ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'SetLineWidth' , 'lLineWidth' , ), 1050, (1050, (), [ (3, 1, None, None) , ], 1 , 1 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'GetLineWidth' , 'pVal' , ), 1051, (1051, (), [ (16387, 10, None, None) , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'GetPlotDataWithSeriesIndex' , 'uiSeriesIndex' , 'ppSafeArray' , ), 1052, (1052, (), [ (19, 1, None, None) , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'DeleteSeries' , 'uiSeriesIndex' , ), 1053, (1053, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'GetPlotDataXWithSeriesIndex' , 'uiSeriesIndex' , 'ppSafeArray' , ), 1054, (1054, (), [ (19, 1, None, None) , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'Invalidate' , ), 1055, (1055, (), [ ], 1 , 1 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
]

IChartFont_vtables_dispatch_ = 1
IChartFont_vtables_ = [
	(( 'Name' , 'Name' , ), 1001, (1001, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'Name' , ), 1001, (1001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 1002, (1002, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Size' , 'Size' , ), 1002, (1002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Bold' , 'fBold' , ), 1003, (1003, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Bold' , 'fBold' , ), 1003, (1003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Italic' , 'fItalic' , ), 1004, (1004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Italic' , 'fItalic' , ), 1004, (1004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Underline' , 'fUnderline' , ), 1005, (1005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Underline' , 'fUnderline' , ), 1005, (1005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Strikethrough' , 'fStrikethrough' , ), 1006, (1006, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Strikethrough' , 'fStrikethrough' , ), 1006, (1006, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IDataValue_vtables_dispatch_ = 1
IDataValue_vtables_ = [
	(( 'SeriesCount' , 'pVal' , ), 1001, (1001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SeriesCount' , 'pVal' , ), 1001, (1001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PointsCount' , 'pVal' , ), 1002, (1002, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PointsCount' , 'pVal' , ), 1002, (1002, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'X' , 'ISeries' , 'IPoint' , 'pVal' , ), 1003, (1003, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'X' , 'ISeries' , 'IPoint' , 'pVal' , ), 1003, (1003, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'ISeries' , 'IPoint' , 'pVal' , ), 1004, (1004, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Y' , 'ISeries' , 'IPoint' , 'pVal' , ), 1004, (1004, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IGrid_vtables_dispatch_ = 1
IGrid_vtables_ = [
	(( 'Major' , 'ppVal' , ), 1001, (1001, (), [ (16393, 10, None, "IID('{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Minor' , 'ppVal' , ), 1002, (1002, (), [ (16393, 10, None, "IID('{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IGridLine_vtables_dispatch_ = 1
IGridLine_vtables_ = [
	(( 'Visible' , 'pVal' , ), 2001, (2001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 2001, (2001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

ILegendBox_vtables_dispatch_ = 1
ILegendBox_vtables_ = [
	(( 'Visible' , 'pVal' , ), 1001, (1001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 1001, (1001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'pVal' , ), 1002, (1002, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'pVal' , ), 1002, (1002, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Alignment' , 'pVal' , ), 1003, (1003, (), [ (3, 1, None, "IID('{F300F302-97EA-44B9-8DA4-82223B8FA9E1}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Alignment' , 'pVal' , ), 1003, (1003, (), [ (16387, 10, None, "IID('{F300F302-97EA-44B9-8DA4-82223B8FA9E1}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TextColor' , 'pVal' , ), 1004, (1004, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TextColor' , 'pVal' , ), 1004, (1004, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DockedPosition' , 'pVal' , ), 1005, (1005, (), [ (3, 1, None, "IID('{D30AFB54-1718-42B0-BD22-0CAC3A225D3D}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DockedPosition' , 'pVal' , ), 1005, (1005, (), [ (16387, 10, None, "IID('{D30AFB54-1718-42B0-BD22-0CAC3A225D3D}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TextFont' , 'font' , ), 1006, (1006, (), [ (16393, 10, None, "IID('{998544E2-D749-4094-B749-F9BEBB579DB1}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

ILine_vtables_dispatch_ = 1
ILine_vtables_ = [
	(( 'Width' , 'pVal' , ), 1001, (1001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Width' , 'pVal' , ), 1001, (1001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 1002, (1002, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 1002, (1002, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'pVal' , ), 1003, (1003, (), [ (3, 1, None, "IID('{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Style' , 'pVal' , ), 1003, (1003, (), [ (16387, 10, None, "IID('{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IPane_vtables_dispatch_ = 1
IPane_vtables_ = [
	(( 'BackColor' , 'pVal' , ), 1001, (1001, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'pVal' , ), 1001, (1001, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Title' , 'ppVal' , ), 1004, (1004, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IPoint_vtables_dispatch_ = 1
IPoint_vtables_ = [
]

IPointLabel_vtables_dispatch_ = 1
IPointLabel_vtables_ = [
	(( 'Visible' , 'pVal' , ), 1001, (1001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 1001, (1001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Alignment' , 'pVal' , ), 1002, (1002, (), [ (3, 1, None, "IID('{198D175B-A965-4988-B701-436DCD640111}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Alignment' , 'pVal' , ), 1002, (1002, (), [ (16387, 10, None, "IID('{198D175B-A965-4988-B701-436DCD640111}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

ISeries_vtables_dispatch_ = 1
ISeries_vtables_ = [
	(( 'Visible' , 'pVal' , ), 1001, (1001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Visible' , 'pVal' , ), 1001, (1001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'GalleryType' , 'pVal' , ), 1002, (1002, (), [ (3, 1, None, "IID('{A3BCD2E7-2B76-49DC-BA19-D5D017A3E070}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'GalleryType' , 'pVal' , ), 1002, (1002, (), [ (16387, 10, None, "IID('{A3BCD2E7-2B76-49DC-BA19-D5D017A3E070}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 1003, (1003, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 1003, (1003, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'pVal' , ), 1004, (1004, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'pVal' , ), 1004, (1004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'MarkerShape' , 'pVal' , ), 1005, (1005, (), [ (3, 1, None, "IID('{EA48A837-2A08-4817-9403-2C339113C3C0}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'MarkerShape' , 'pVal' , ), 1005, (1005, (), [ (16387, 10, None, "IID('{EA48A837-2A08-4817-9403-2C339113C3C0}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'MarkerSize' , 'pVal' , ), 1006, (1006, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MarkerSize' , 'pVal' , ), 1006, (1006, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'YAxis' , 'ppVal' , ), 1009, (1009, (), [ (9, 1, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28398}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'YAxis' , 'ppVal' , ), 1009, (1009, (), [ (16393, 10, None, "IID('{6EFBEC37-9BE6-43D4-8F59-36391BF28398}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'LineType' , ), 1010, (1010, (), [ (3, 1, None, "IID('{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'LineStyle' , 'LineType' , ), 1010, (1010, (), [ (16387, 10, None, "IID('{E05CE3F8-74AF-4CF6-8225-68E5F58805D5}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'LineWidth' , 'Width' , ), 1011, (1011, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'LineWidth' , 'Width' , ), 1011, (1011, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

ITitle_vtables_dispatch_ = 1
ITitle_vtables_ = [
	(( 'Alignment' , 'pVal' , ), 1001, (1001, (), [ (3, 1, None, "IID('{198D175B-A965-4988-B701-436DCD640111}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Alignment' , 'pVal' , ), 1001, (1001, (), [ (16387, 10, None, "IID('{198D175B-A965-4988-B701-436DCD640111}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'pVal' , ), 1002, (1002, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Text' , 'pVal' , ), 1002, (1002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'pVal' , ), 1003, (1003, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'BackColor' , 'pVal' , ), 1003, (1003, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TextColor' , 'pVal' , ), 1004, (1004, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TextColor' , 'pVal' , ), 1004, (1004, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TextFont' , 'font' , ), 1005, (1005, (), [ (16393, 10, None, "IID('{998544E2-D749-4094-B749-F9BEBB579DB1}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

ITitleEx_vtables_dispatch_ = 1
ITitleEx_vtables_ = [
]

IValueFormat_vtables_dispatch_ = 1
IValueFormat_vtables_ = [
	(( 'Decimals' , 'pVal' , ), 1001, (1001, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Decimals' , 'pVal' , ), 1001, (1001, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}' : ITitle,
	'{998544E2-D749-4094-B749-F9BEBB579DB1}' : IChartFont,
	'{4DE0B045-C16A-46E4-A238-E70556CE1A4F}' : IGrid,
	'{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}' : IGridLine,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}' : ILine,
	'{85722F51-1CAE-442F-BB40-A969034C6FD0}' : IPointLabel,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}' : IValueFormat,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28396}' : IAxis,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28397}' : IAxisX,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28398}' : IAxisY,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28399}' : IPane,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839A}' : ILegendBox,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839B}' : ISeries,
	'{48DE6C5D-FCF4-44FF-9673-9891ABC58E79}' : ITitleEx,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839C}' : IPoint,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF283A1}' : IDataValue,
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28395}' : IChart,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}' : 'ITitle',
	'{998544E2-D749-4094-B749-F9BEBB579DB1}' : 'IChartFont',
	'{4DE0B045-C16A-46E4-A238-E70556CE1A4F}' : 'IGrid',
	'{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}' : 'IGridLine',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}' : 'ILine',
	'{85722F51-1CAE-442F-BB40-A969034C6FD0}' : 'IPointLabel',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}' : 'IValueFormat',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28396}' : 'IAxis',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28397}' : 'IAxisX',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28398}' : 'IAxisY',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28399}' : 'IPane',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839A}' : 'ILegendBox',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839B}' : 'ISeries',
	'{48DE6C5D-FCF4-44FF-9673-9891ABC58E79}' : 'ITitleEx',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF2839C}' : 'IPoint',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF283A1}' : 'IDataValue',
	'{6EFBEC37-9BE6-43D4-8F59-36391BF28395}' : 'IChart',
}


NamesToIIDMap = {
	'ITitle' : '{6EFBEC37-9BE6-43D4-8F59-36391BF2839E}',
	'IChartFont' : '{998544E2-D749-4094-B749-F9BEBB579DB1}',
	'IGrid' : '{4DE0B045-C16A-46E4-A238-E70556CE1A4F}',
	'IGridLine' : '{1080F746-559B-4F8E-8BBD-B4E9F2CBA4E0}',
	'ILine' : '{6EFBEC37-9BE6-43D4-8F59-36391BF2839D}',
	'IPointLabel' : '{85722F51-1CAE-442F-BB40-A969034C6FD0}',
	'IValueFormat' : '{6EFBEC37-9BE6-43D4-8F59-36391BF283A0}',
	'IAxis' : '{6EFBEC37-9BE6-43D4-8F59-36391BF28396}',
	'IAxisX' : '{6EFBEC37-9BE6-43D4-8F59-36391BF28397}',
	'IAxisY' : '{6EFBEC37-9BE6-43D4-8F59-36391BF28398}',
	'IPane' : '{6EFBEC37-9BE6-43D4-8F59-36391BF28399}',
	'ILegendBox' : '{6EFBEC37-9BE6-43D4-8F59-36391BF2839A}',
	'ISeries' : '{6EFBEC37-9BE6-43D4-8F59-36391BF2839B}',
	'ITitleEx' : '{48DE6C5D-FCF4-44FF-9673-9891ABC58E79}',
	'IPoint' : '{6EFBEC37-9BE6-43D4-8F59-36391BF2839C}',
	'IDataValue' : '{6EFBEC37-9BE6-43D4-8F59-36391BF283A1}',
	'IChart' : '{6EFBEC37-9BE6-43D4-8F59-36391BF28395}',
}


