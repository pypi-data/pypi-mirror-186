# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMFlexInterface.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMFlexInterface Type Library'
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

CLSID = IID('{E67422E0-9B06-4621-B474-8444BD15F4F2}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class InterfaceNodeType(IntEnum):
	'''
	InterfaceNodeType enumeration.
	'''
	InterfaceNodeType_DirectInput =3         
	'''Constant value is 3.'''
	InterfaceNodeType_MultiFDRElement=2         
	'''Constant value is 2.'''
	InterfaceNodeType_MultiNodeSet=1         
	'''Constant value is 1.'''
	InterfaceNodeType_SingleNodeSet=0         
	'''Constant value is 0.'''
class RFIShellRecoveryType(IntEnum):
	'''
	RFIShellRecoveryType enumeration.
	'''
	RFIShellRecoveryType_BOTTOM   =1         
	'''Constant value is 1.'''
	RFIShellRecoveryType_TOP      =0         
	'''Constant value is 0.'''
class RFISolverType(IntEnum):
	'''
	RFISolverType enumeration.
	'''
	RFISolverType_Dynamis         =1         
	'''Constant value is 1.'''
	RFISolverType_SunShine        =0         
	'''Constant value is 0.'''
class RFITargetBodyType(IntEnum):
	'''
	RFITargetBodyType enumeration.
	'''
	RFITargetBodyType_BDFFile     =1         
	'''Constant value is 1.'''
	RFITargetBodyType_Body        =0         
	'''Constant value is 0.'''
	RFITargetBodyType_DYNAMISInputFile=2         
	'''Constant value is 2.'''

from win32com.client import DispatchBaseClass
class IFlexInterface(DispatchBaseClass):
	'''Flex Interface Toolkit'''
	CLSID = IID('{E2DFC1B4-01F7-438E-AEEB-3285174A7BDB}')
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
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RFlexGenerator(self):
		return self._ApplyTypes_(*(9551, 2, (9, 0), (), "RFlexGenerator", '{99AE2E87-8BEC-4292-9AA1-4F2DB831E7C8}'))
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
	RFlexGenerator = property(_get_RFlexGenerator, None)
	'''
	Get RFlex Generator

	:type: recurdyn.FlexInterface.IRFlexGenerator
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
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RFlexGenerator": (9551, 2, (9, 0), (), "RFlexGenerator", '{99AE2E87-8BEC-4292-9AA1-4F2DB831E7C8}'),
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

class IRFlexGenerationOption(DispatchBaseClass):
	'''Option for Generating RFlex Body '''
	CLSID = IID('{7C31022B-7395-4475-99F0-ACF0A75A3698}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AutoMPCFlag(self):
		return self._ApplyTypes_(*(9528, 2, (11, 0), (), "AutoMPCFlag", None))
	def _get_BDFFilePath(self):
		return self._ApplyTypes_(*(9504, 2, (8, 0), (), "BDFFilePath", None))
	def _get_Body(self):
		return self._ApplyTypes_(*(9503, 2, (9, 0), (), "Body", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_DeleteDynamisDataBaseFilesFlag(self):
		return self._ApplyTypes_(*(9518, 2, (11, 0), (), "DeleteDynamisDataBaseFilesFlag", None))
	def _get_DynamisInputFilePath(self):
		return self._ApplyTypes_(*(9524, 2, (8, 0), (), "DynamisInputFilePath", None))
	def _get_FixedInterfaceNormalModeLowerFrequency(self):
		return self._ApplyTypes_(*(9526, 2, (5, 0), (), "FixedInterfaceNormalModeLowerFrequency", None))
	def _get_FixedInterfaceNormalModeUpperFrequency(self):
		return self._ApplyTypes_(*(9527, 2, (5, 0), (), "FixedInterfaceNormalModeUpperFrequency", None))
	def _get_IncludeBCFlag(self):
		return self._ApplyTypes_(*(9529, 2, (11, 0), (), "IncludeBCFlag", None))
	def _get_InterfaceNodeFDRElementMulti(self):
		return self._ApplyTypes_(*(9531, 2, (8195, 0), (), "InterfaceNodeFDRElementMulti", None))
	def _get_InterfaceNodeIDs(self):
		return self._ApplyTypes_(*(9506, 2, (8195, 0), (), "InterfaceNodeIDs", None))
	def _get_InterfaceNodeNumber(self):
		return self._ApplyTypes_(*(9508, 2, (3, 0), (), "InterfaceNodeNumber", None))
	def _get_InterfaceNodeSelectionType(self):
		return self._ApplyTypes_(*(9533, 2, (3, 0), (), "InterfaceNodeSelectionType", '{5BFEC982-5971-4CD8-B118-FBF85AD5CC57}'))
	def _get_InterfaceNodeSetMulti(self):
		return self._ApplyTypes_(*(9530, 2, (8204, 0), (), "InterfaceNodeSetMulti", None))
	def _get_InterfaceNodeset(self):
		return self._ApplyTypes_(*(9507, 2, (9, 0), (), "InterfaceNodeset", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_LanczosBlockSize(self):
		return self._ApplyTypes_(*(9534, 2, (19, 0), (), "LanczosBlockSize", None))
	def _get_LanczosBlockSizeFlag(self):
		return self._ApplyTypes_(*(9535, 2, (11, 0), (), "LanczosBlockSizeFlag", None))
	def _get_LowerFrequency(self):
		return self._ApplyTypes_(*(9512, 2, (5, 0), (), "LowerFrequency", None))
	def _get_MeshDataType(self):
		return self._ApplyTypes_(*(9502, 2, (3, 0), (), "MeshDataType", '{AA0FDD6C-F5DA-41C6-9B47-35C90BC3B3FC}'))
	def _get_NormalModeNumber(self):
		return self._ApplyTypes_(*(9511, 2, (19, 0), (), "NormalModeNumber", None))
	def _get_RFIFilePath(self):
		return self._ApplyTypes_(*(9517, 2, (8, 0), (), "RFIFilePath", None))
	def _get_RFITranslatorFlag(self):
		return self._ApplyTypes_(*(9519, 2, (11, 0), (), "RFITranslatorFlag", None))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(9505, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RemoveMidNodeRelatedInformationFlag(self):
		return self._ApplyTypes_(*(9515, 2, (11, 0), (), "RemoveMidNodeRelatedInformationFlag", None))
	def _get_RemoveZeroValueForRotModeShapeFlag(self):
		return self._ApplyTypes_(*(9516, 2, (11, 0), (), "RemoveZeroValueForRotModeShapeFlag", None))
	def _get_SMPComputingNoThread(self):
		return self._ApplyTypes_(*(9539, 2, (19, 0), (), "SMPComputingNoThread", None))
	def _get_SavedModeNumber(self):
		return self._ApplyTypes_(*(9525, 2, (19, 0), (), "SavedModeNumber", None))
	def _get_ShellDrillingParameter(self):
		return self._ApplyTypes_(*(9520, 2, (5, 0), (), "ShellDrillingParameter", None))
	def _get_ShellRecoveryType(self):
		return self._ApplyTypes_(*(9523, 2, (3, 0), (), "ShellRecoveryType", '{D21798C7-4AF1-416C-8CAC-FB9483D6C2CC}'))
	def _get_SingularCheckMaxRatio(self):
		return self._ApplyTypes_(*(9536, 2, (5, 0), (), "SingularCheckMaxRatio", None))
	def _get_SingularCheckMaxRatioFlag(self):
		return self._ApplyTypes_(*(9537, 2, (11, 0), (), "SingularCheckMaxRatioFlag", None))
	def _get_Solver(self):
		return self._ApplyTypes_(*(9501, 2, (3, 0), (), "Solver", '{751C1136-D0D2-41B4-98DF-2C88CE95D9C4}'))
	def _get_StopSimulationWhenLowMeshQualityFlag(self):
		return self._ApplyTypes_(*(9538, 2, (11, 0), (), "StopSimulationWhenLowMeshQualityFlag", None))
	def _get_StrainShapeFlag(self):
		return self._ApplyTypes_(*(9522, 2, (11, 0), (), "StrainShapeFlag", None))
	def _get_StressShapeFlag(self):
		return self._ApplyTypes_(*(9521, 2, (11, 0), (), "StressShapeFlag", None))
	def _get_Unit(self):
		return self._ApplyTypes_(*(9514, 2, (9, 0), (), "Unit", '{09A65909-6FBB-488A-9726-D320F5666395}'))
	def _get_UpperFrequency(self):
		return self._ApplyTypes_(*(9513, 2, (5, 0), (), "UpperFrequency", None))
	def _get_UserDefinedDOFs(self):
		return self._ApplyTypes_(*(9510, 2, (8200, 0), (), "UserDefinedDOFs", None))
	def _get_UserDefinedDOFsFlag(self):
		return self._ApplyTypes_(*(9509, 2, (11, 0), (), "UserDefinedDOFsFlag", None))
	def _get_UserDefinedDOFsforEachNodeinNodeSetFlag(self):
		return self._ApplyTypes_(*(9532, 2, (11, 0), (), "UserDefinedDOFsforEachNodeinNodeSetFlag", None))

	def _set_AutoMPCFlag(self, value):
		if "AutoMPCFlag" in self.__dict__: self.__dict__["AutoMPCFlag"] = value; return
		self._oleobj_.Invoke(*((9528, LCID, 4, 0) + (value,) + ()))
	def _set_BDFFilePath(self, value):
		if "BDFFilePath" in self.__dict__: self.__dict__["BDFFilePath"] = value; return
		self._oleobj_.Invoke(*((9504, LCID, 4, 0) + (value,) + ()))
	def _set_Body(self, value):
		if "Body" in self.__dict__: self.__dict__["Body"] = value; return
		self._oleobj_.Invoke(*((9503, LCID, 4, 0) + (value,) + ()))
	def _set_DeleteDynamisDataBaseFilesFlag(self, value):
		if "DeleteDynamisDataBaseFilesFlag" in self.__dict__: self.__dict__["DeleteDynamisDataBaseFilesFlag"] = value; return
		self._oleobj_.Invoke(*((9518, LCID, 4, 0) + (value,) + ()))
	def _set_DynamisInputFilePath(self, value):
		if "DynamisInputFilePath" in self.__dict__: self.__dict__["DynamisInputFilePath"] = value; return
		self._oleobj_.Invoke(*((9524, LCID, 4, 0) + (value,) + ()))
	def _set_FixedInterfaceNormalModeLowerFrequency(self, value):
		if "FixedInterfaceNormalModeLowerFrequency" in self.__dict__: self.__dict__["FixedInterfaceNormalModeLowerFrequency"] = value; return
		self._oleobj_.Invoke(*((9526, LCID, 4, 0) + (value,) + ()))
	def _set_FixedInterfaceNormalModeUpperFrequency(self, value):
		if "FixedInterfaceNormalModeUpperFrequency" in self.__dict__: self.__dict__["FixedInterfaceNormalModeUpperFrequency"] = value; return
		self._oleobj_.Invoke(*((9527, LCID, 4, 0) + (value,) + ()))
	def _set_IncludeBCFlag(self, value):
		if "IncludeBCFlag" in self.__dict__: self.__dict__["IncludeBCFlag"] = value; return
		self._oleobj_.Invoke(*((9529, LCID, 4, 0) + (value,) + ()))
	def _set_InterfaceNodeFDRElementMulti(self, value):
		if "InterfaceNodeFDRElementMulti" in self.__dict__: self.__dict__["InterfaceNodeFDRElementMulti"] = value; return
		variantValue = win32com.client.VARIANT(8195, value)
		self._oleobj_.Invoke(*((9531, LCID, 4, 0) + (variantValue,) + ()))
	def _set_InterfaceNodeIDs(self, value):
		if "InterfaceNodeIDs" in self.__dict__: self.__dict__["InterfaceNodeIDs"] = value; return
		variantValue = win32com.client.VARIANT(8195, value)
		self._oleobj_.Invoke(*((9506, LCID, 4, 0) + (variantValue,) + ()))
	def _set_InterfaceNodeSelectionType(self, value):
		if "InterfaceNodeSelectionType" in self.__dict__: self.__dict__["InterfaceNodeSelectionType"] = value; return
		self._oleobj_.Invoke(*((9533, LCID, 4, 0) + (value,) + ()))
	def _set_InterfaceNodeSetMulti(self, value):
		if "InterfaceNodeSetMulti" in self.__dict__: self.__dict__["InterfaceNodeSetMulti"] = value; return
		_value_type = True if value and isinstance(value[0], win32com.client.VARIANT) else False
		if not _value_type:
			value = [win32com.client.VARIANT(12, _data) for _data in value]
		variantValue = win32com.client.VARIANT(8204, value)
		self._oleobj_.Invoke(*((9530, LCID, 4, 0) + (variantValue,) + ()))
		if not _value_type:
			value = [_data.value for _data in value]
	def _set_InterfaceNodeset(self, value):
		if "InterfaceNodeset" in self.__dict__: self.__dict__["InterfaceNodeset"] = value; return
		self._oleobj_.Invoke(*((9507, LCID, 4, 0) + (value,) + ()))
	def _set_LanczosBlockSize(self, value):
		if "LanczosBlockSize" in self.__dict__: self.__dict__["LanczosBlockSize"] = value; return
		self._oleobj_.Invoke(*((9534, LCID, 4, 0) + (value,) + ()))
	def _set_LanczosBlockSizeFlag(self, value):
		if "LanczosBlockSizeFlag" in self.__dict__: self.__dict__["LanczosBlockSizeFlag"] = value; return
		self._oleobj_.Invoke(*((9535, LCID, 4, 0) + (value,) + ()))
	def _set_LowerFrequency(self, value):
		if "LowerFrequency" in self.__dict__: self.__dict__["LowerFrequency"] = value; return
		self._oleobj_.Invoke(*((9512, LCID, 4, 0) + (value,) + ()))
	def _set_MeshDataType(self, value):
		if "MeshDataType" in self.__dict__: self.__dict__["MeshDataType"] = value; return
		self._oleobj_.Invoke(*((9502, LCID, 4, 0) + (value,) + ()))
	def _set_NormalModeNumber(self, value):
		if "NormalModeNumber" in self.__dict__: self.__dict__["NormalModeNumber"] = value; return
		self._oleobj_.Invoke(*((9511, LCID, 4, 0) + (value,) + ()))
	def _set_RFIFilePath(self, value):
		if "RFIFilePath" in self.__dict__: self.__dict__["RFIFilePath"] = value; return
		self._oleobj_.Invoke(*((9517, LCID, 4, 0) + (value,) + ()))
	def _set_RFITranslatorFlag(self, value):
		if "RFITranslatorFlag" in self.__dict__: self.__dict__["RFITranslatorFlag"] = value; return
		self._oleobj_.Invoke(*((9519, LCID, 4, 0) + (value,) + ()))
	def _set_RefFrame(self, value):
		if "RefFrame" in self.__dict__: self.__dict__["RefFrame"] = value; return
		self._oleobj_.Invoke(*((9505, LCID, 4, 0) + (value,) + ()))
	def _set_RemoveMidNodeRelatedInformationFlag(self, value):
		if "RemoveMidNodeRelatedInformationFlag" in self.__dict__: self.__dict__["RemoveMidNodeRelatedInformationFlag"] = value; return
		self._oleobj_.Invoke(*((9515, LCID, 4, 0) + (value,) + ()))
	def _set_RemoveZeroValueForRotModeShapeFlag(self, value):
		if "RemoveZeroValueForRotModeShapeFlag" in self.__dict__: self.__dict__["RemoveZeroValueForRotModeShapeFlag"] = value; return
		self._oleobj_.Invoke(*((9516, LCID, 4, 0) + (value,) + ()))
	def _set_SMPComputingNoThread(self, value):
		if "SMPComputingNoThread" in self.__dict__: self.__dict__["SMPComputingNoThread"] = value; return
		self._oleobj_.Invoke(*((9539, LCID, 4, 0) + (value,) + ()))
	def _set_SavedModeNumber(self, value):
		if "SavedModeNumber" in self.__dict__: self.__dict__["SavedModeNumber"] = value; return
		self._oleobj_.Invoke(*((9525, LCID, 4, 0) + (value,) + ()))
	def _set_ShellDrillingParameter(self, value):
		if "ShellDrillingParameter" in self.__dict__: self.__dict__["ShellDrillingParameter"] = value; return
		self._oleobj_.Invoke(*((9520, LCID, 4, 0) + (value,) + ()))
	def _set_ShellRecoveryType(self, value):
		if "ShellRecoveryType" in self.__dict__: self.__dict__["ShellRecoveryType"] = value; return
		self._oleobj_.Invoke(*((9523, LCID, 4, 0) + (value,) + ()))
	def _set_SingularCheckMaxRatio(self, value):
		if "SingularCheckMaxRatio" in self.__dict__: self.__dict__["SingularCheckMaxRatio"] = value; return
		self._oleobj_.Invoke(*((9536, LCID, 4, 0) + (value,) + ()))
	def _set_SingularCheckMaxRatioFlag(self, value):
		if "SingularCheckMaxRatioFlag" in self.__dict__: self.__dict__["SingularCheckMaxRatioFlag"] = value; return
		self._oleobj_.Invoke(*((9537, LCID, 4, 0) + (value,) + ()))
	def _set_Solver(self, value):
		if "Solver" in self.__dict__: self.__dict__["Solver"] = value; return
		self._oleobj_.Invoke(*((9501, LCID, 4, 0) + (value,) + ()))
	def _set_StopSimulationWhenLowMeshQualityFlag(self, value):
		if "StopSimulationWhenLowMeshQualityFlag" in self.__dict__: self.__dict__["StopSimulationWhenLowMeshQualityFlag"] = value; return
		self._oleobj_.Invoke(*((9538, LCID, 4, 0) + (value,) + ()))
	def _set_StrainShapeFlag(self, value):
		if "StrainShapeFlag" in self.__dict__: self.__dict__["StrainShapeFlag"] = value; return
		self._oleobj_.Invoke(*((9522, LCID, 4, 0) + (value,) + ()))
	def _set_StressShapeFlag(self, value):
		if "StressShapeFlag" in self.__dict__: self.__dict__["StressShapeFlag"] = value; return
		self._oleobj_.Invoke(*((9521, LCID, 4, 0) + (value,) + ()))
	def _set_Unit(self, value):
		if "Unit" in self.__dict__: self.__dict__["Unit"] = value; return
		self._oleobj_.Invoke(*((9514, LCID, 4, 0) + (value,) + ()))
	def _set_UpperFrequency(self, value):
		if "UpperFrequency" in self.__dict__: self.__dict__["UpperFrequency"] = value; return
		self._oleobj_.Invoke(*((9513, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedDOFs(self, value):
		if "UserDefinedDOFs" in self.__dict__: self.__dict__["UserDefinedDOFs"] = value; return
		variantValue = win32com.client.VARIANT(8200, value)
		self._oleobj_.Invoke(*((9510, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UserDefinedDOFsFlag(self, value):
		if "UserDefinedDOFsFlag" in self.__dict__: self.__dict__["UserDefinedDOFsFlag"] = value; return
		self._oleobj_.Invoke(*((9509, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedDOFsforEachNodeinNodeSetFlag(self, value):
		if "UserDefinedDOFsforEachNodeinNodeSetFlag" in self.__dict__: self.__dict__["UserDefinedDOFsforEachNodeinNodeSetFlag"] = value; return
		self._oleobj_.Invoke(*((9532, LCID, 4, 0) + (value,) + ()))

	AutoMPCFlag = property(_get_AutoMPCFlag, _set_AutoMPCFlag)
	'''
	AutoMPC Flag

	:type: bool
	'''
	BDFFilePath = property(_get_BDFFilePath, _set_BDFFilePath)
	'''
	BDF file path

	:type: str
	'''
	Body = property(_get_Body, _set_Body)
	'''
	Target Body

	:type: recurdyn.ProcessNet.IGeneric
	'''
	DeleteDynamisDataBaseFilesFlag = property(_get_DeleteDynamisDataBaseFilesFlag, _set_DeleteDynamisDataBaseFilesFlag)
	'''
	Flag to delete dynamis dataBase filess

	:type: bool
	'''
	DynamisInputFilePath = property(_get_DynamisInputFilePath, _set_DynamisInputFilePath)
	'''
	DYNAMIS input file path

	:type: str
	'''
	FixedInterfaceNormalModeLowerFrequency = property(_get_FixedInterfaceNormalModeLowerFrequency, _set_FixedInterfaceNormalModeLowerFrequency)
	'''
	Fixed Interface Normal Mode Lower frequency

	:type: float
	'''
	FixedInterfaceNormalModeUpperFrequency = property(_get_FixedInterfaceNormalModeUpperFrequency, _set_FixedInterfaceNormalModeUpperFrequency)
	'''
	Fixed Interface Normal Mode Upper frequency

	:type: float
	'''
	IncludeBCFlag = property(_get_IncludeBCFlag, _set_IncludeBCFlag)
	'''
	Inlcude BC from fixed joint and FFlex BC Flag

	:type: bool
	'''
	InterfaceNodeFDRElementMulti = property(_get_InterfaceNodeFDRElementMulti, _set_InterfaceNodeFDRElementMulti)
	'''
	Interface node Multi FDR

	:type: list[int]
	'''
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
	InterfaceNodeSelectionType = property(_get_InterfaceNodeSelectionType, _set_InterfaceNodeSelectionType)
	'''
	Interface Node Selection Type

	:type: recurdyn.FlexInterface.InterfaceNodeType
	'''
	InterfaceNodeSetMulti = property(_get_InterfaceNodeSetMulti, _set_InterfaceNodeSetMulti)
	'''
	Interface node Multi Nodeset

	:type: list[object]
	'''
	InterfaceNodeset = property(_get_InterfaceNodeset, _set_InterfaceNodeset)
	'''
	Interface node nodeset

	:type: recurdyn.ProcessNet.IGeneric
	'''
	LanczosBlockSize = property(_get_LanczosBlockSize, _set_LanczosBlockSize)
	'''
	Lanczos Block Size

	:type: int
	'''
	LanczosBlockSizeFlag = property(_get_LanczosBlockSizeFlag, _set_LanczosBlockSizeFlag)
	'''
	Lanczos Block Size Flag

	:type: bool
	'''
	LowerFrequency = property(_get_LowerFrequency, _set_LowerFrequency)
	'''
	Lower frequency

	:type: float
	'''
	MeshDataType = property(_get_MeshDataType, _set_MeshDataType)
	'''
	Mesh Data Information Type

	:type: recurdyn.FlexInterface.RFITargetBodyType
	'''
	NormalModeNumber = property(_get_NormalModeNumber, _set_NormalModeNumber)
	'''
	Number of fixed normal mode

	:type: int
	'''
	RFIFilePath = property(_get_RFIFilePath, _set_RFIFilePath)
	'''
	RFI file path

	:type: str
	'''
	RFITranslatorFlag = property(_get_RFITranslatorFlag, _set_RFITranslatorFlag)
	'''
	Flag to translate RFI file to text file

	:type: bool
	'''
	RefFrame = property(_get_RefFrame, _set_RefFrame)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RemoveMidNodeRelatedInformationFlag = property(_get_RemoveMidNodeRelatedInformationFlag, _set_RemoveMidNodeRelatedInformationFlag)
	'''
	Flag to remove mid node related information

	:type: bool
	'''
	RemoveZeroValueForRotModeShapeFlag = property(_get_RemoveZeroValueForRotModeShapeFlag, _set_RemoveZeroValueForRotModeShapeFlag)
	'''
	Flag to remove zero value for rot mode shape

	:type: bool
	'''
	SMPComputingNoThread = property(_get_SMPComputingNoThread, _set_SMPComputingNoThread)
	'''
	SMP Computing No. Thread

	:type: int
	'''
	SavedModeNumber = property(_get_SavedModeNumber, _set_SavedModeNumber)
	'''
	Number of Saved modes

	:type: int
	'''
	ShellDrillingParameter = property(_get_ShellDrillingParameter, _set_ShellDrillingParameter)
	'''
	Shell Drilling Parameter

	:type: float
	'''
	ShellRecoveryType = property(_get_ShellRecoveryType, _set_ShellRecoveryType)
	'''
	Shell Recovery Type

	:type: recurdyn.FlexInterface.RFIShellRecoveryType
	'''
	SingularCheckMaxRatio = property(_get_SingularCheckMaxRatio, _set_SingularCheckMaxRatio)
	'''
	Stiffness Matrix Singular Check Max. Ratio

	:type: float
	'''
	SingularCheckMaxRatioFlag = property(_get_SingularCheckMaxRatioFlag, _set_SingularCheckMaxRatioFlag)
	'''
	Stiffness Matrix Singular Check Max. Ratio Flag

	:type: bool
	'''
	Solver = property(_get_Solver, _set_Solver)
	'''
	Solver is obsolete function

	:type: recurdyn.FlexInterface.RFISolverType
	'''
	StopSimulationWhenLowMeshQualityFlag = property(_get_StopSimulationWhenLowMeshQualityFlag, _set_StopSimulationWhenLowMeshQualityFlag)
	'''
	Stop Simulation When Low Mesh Quality Flag

	:type: bool
	'''
	StrainShapeFlag = property(_get_StrainShapeFlag, _set_StrainShapeFlag)
	'''
	Strain Shape Flag

	:type: bool
	'''
	StressShapeFlag = property(_get_StressShapeFlag, _set_StressShapeFlag)
	'''
	Stress Shape Flag

	:type: bool
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
	UserDefinedDOFs = property(_get_UserDefinedDOFs, _set_UserDefinedDOFs)
	'''
	User defined DOFs

	:type: list[str]
	'''
	UserDefinedDOFsFlag = property(_get_UserDefinedDOFsFlag, _set_UserDefinedDOFsFlag)
	'''
	User defined DOFs for computing constriant modes Flag

	:type: bool
	'''
	UserDefinedDOFsforEachNodeinNodeSetFlag = property(_get_UserDefinedDOFsforEachNodeinNodeSetFlag, _set_UserDefinedDOFsforEachNodeinNodeSetFlag)
	'''
	User defined DOFs for Each Node in NodeSet

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_AutoMPCFlag": _set_AutoMPCFlag,
		"_set_BDFFilePath": _set_BDFFilePath,
		"_set_Body": _set_Body,
		"_set_DeleteDynamisDataBaseFilesFlag": _set_DeleteDynamisDataBaseFilesFlag,
		"_set_DynamisInputFilePath": _set_DynamisInputFilePath,
		"_set_FixedInterfaceNormalModeLowerFrequency": _set_FixedInterfaceNormalModeLowerFrequency,
		"_set_FixedInterfaceNormalModeUpperFrequency": _set_FixedInterfaceNormalModeUpperFrequency,
		"_set_IncludeBCFlag": _set_IncludeBCFlag,
		"_set_InterfaceNodeFDRElementMulti": _set_InterfaceNodeFDRElementMulti,
		"_set_InterfaceNodeIDs": _set_InterfaceNodeIDs,
		"_set_InterfaceNodeSelectionType": _set_InterfaceNodeSelectionType,
		"_set_InterfaceNodeSetMulti": _set_InterfaceNodeSetMulti,
		"_set_InterfaceNodeset": _set_InterfaceNodeset,
		"_set_LanczosBlockSize": _set_LanczosBlockSize,
		"_set_LanczosBlockSizeFlag": _set_LanczosBlockSizeFlag,
		"_set_LowerFrequency": _set_LowerFrequency,
		"_set_MeshDataType": _set_MeshDataType,
		"_set_NormalModeNumber": _set_NormalModeNumber,
		"_set_RFIFilePath": _set_RFIFilePath,
		"_set_RFITranslatorFlag": _set_RFITranslatorFlag,
		"_set_RefFrame": _set_RefFrame,
		"_set_RemoveMidNodeRelatedInformationFlag": _set_RemoveMidNodeRelatedInformationFlag,
		"_set_RemoveZeroValueForRotModeShapeFlag": _set_RemoveZeroValueForRotModeShapeFlag,
		"_set_SMPComputingNoThread": _set_SMPComputingNoThread,
		"_set_SavedModeNumber": _set_SavedModeNumber,
		"_set_ShellDrillingParameter": _set_ShellDrillingParameter,
		"_set_ShellRecoveryType": _set_ShellRecoveryType,
		"_set_SingularCheckMaxRatio": _set_SingularCheckMaxRatio,
		"_set_SingularCheckMaxRatioFlag": _set_SingularCheckMaxRatioFlag,
		"_set_Solver": _set_Solver,
		"_set_StopSimulationWhenLowMeshQualityFlag": _set_StopSimulationWhenLowMeshQualityFlag,
		"_set_StrainShapeFlag": _set_StrainShapeFlag,
		"_set_StressShapeFlag": _set_StressShapeFlag,
		"_set_Unit": _set_Unit,
		"_set_UpperFrequency": _set_UpperFrequency,
		"_set_UserDefinedDOFs": _set_UserDefinedDOFs,
		"_set_UserDefinedDOFsFlag": _set_UserDefinedDOFsFlag,
		"_set_UserDefinedDOFsforEachNodeinNodeSetFlag": _set_UserDefinedDOFsforEachNodeinNodeSetFlag,
	}
	_prop_map_get_ = {
		"AutoMPCFlag": (9528, 2, (11, 0), (), "AutoMPCFlag", None),
		"BDFFilePath": (9504, 2, (8, 0), (), "BDFFilePath", None),
		"Body": (9503, 2, (9, 0), (), "Body", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"DeleteDynamisDataBaseFilesFlag": (9518, 2, (11, 0), (), "DeleteDynamisDataBaseFilesFlag", None),
		"DynamisInputFilePath": (9524, 2, (8, 0), (), "DynamisInputFilePath", None),
		"FixedInterfaceNormalModeLowerFrequency": (9526, 2, (5, 0), (), "FixedInterfaceNormalModeLowerFrequency", None),
		"FixedInterfaceNormalModeUpperFrequency": (9527, 2, (5, 0), (), "FixedInterfaceNormalModeUpperFrequency", None),
		"IncludeBCFlag": (9529, 2, (11, 0), (), "IncludeBCFlag", None),
		"InterfaceNodeFDRElementMulti": (9531, 2, (8195, 0), (), "InterfaceNodeFDRElementMulti", None),
		"InterfaceNodeIDs": (9506, 2, (8195, 0), (), "InterfaceNodeIDs", None),
		"InterfaceNodeNumber": (9508, 2, (3, 0), (), "InterfaceNodeNumber", None),
		"InterfaceNodeSelectionType": (9533, 2, (3, 0), (), "InterfaceNodeSelectionType", '{5BFEC982-5971-4CD8-B118-FBF85AD5CC57}'),
		"InterfaceNodeSetMulti": (9530, 2, (8204, 0), (), "InterfaceNodeSetMulti", None),
		"InterfaceNodeset": (9507, 2, (9, 0), (), "InterfaceNodeset", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"LanczosBlockSize": (9534, 2, (19, 0), (), "LanczosBlockSize", None),
		"LanczosBlockSizeFlag": (9535, 2, (11, 0), (), "LanczosBlockSizeFlag", None),
		"LowerFrequency": (9512, 2, (5, 0), (), "LowerFrequency", None),
		"MeshDataType": (9502, 2, (3, 0), (), "MeshDataType", '{AA0FDD6C-F5DA-41C6-9B47-35C90BC3B3FC}'),
		"NormalModeNumber": (9511, 2, (19, 0), (), "NormalModeNumber", None),
		"RFIFilePath": (9517, 2, (8, 0), (), "RFIFilePath", None),
		"RFITranslatorFlag": (9519, 2, (11, 0), (), "RFITranslatorFlag", None),
		"RefFrame": (9505, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RemoveMidNodeRelatedInformationFlag": (9515, 2, (11, 0), (), "RemoveMidNodeRelatedInformationFlag", None),
		"RemoveZeroValueForRotModeShapeFlag": (9516, 2, (11, 0), (), "RemoveZeroValueForRotModeShapeFlag", None),
		"SMPComputingNoThread": (9539, 2, (19, 0), (), "SMPComputingNoThread", None),
		"SavedModeNumber": (9525, 2, (19, 0), (), "SavedModeNumber", None),
		"ShellDrillingParameter": (9520, 2, (5, 0), (), "ShellDrillingParameter", None),
		"ShellRecoveryType": (9523, 2, (3, 0), (), "ShellRecoveryType", '{D21798C7-4AF1-416C-8CAC-FB9483D6C2CC}'),
		"SingularCheckMaxRatio": (9536, 2, (5, 0), (), "SingularCheckMaxRatio", None),
		"SingularCheckMaxRatioFlag": (9537, 2, (11, 0), (), "SingularCheckMaxRatioFlag", None),
		"Solver": (9501, 2, (3, 0), (), "Solver", '{751C1136-D0D2-41B4-98DF-2C88CE95D9C4}'),
		"StopSimulationWhenLowMeshQualityFlag": (9538, 2, (11, 0), (), "StopSimulationWhenLowMeshQualityFlag", None),
		"StrainShapeFlag": (9522, 2, (11, 0), (), "StrainShapeFlag", None),
		"StressShapeFlag": (9521, 2, (11, 0), (), "StressShapeFlag", None),
		"Unit": (9514, 2, (9, 0), (), "Unit", '{09A65909-6FBB-488A-9726-D320F5666395}'),
		"UpperFrequency": (9513, 2, (5, 0), (), "UpperFrequency", None),
		"UserDefinedDOFs": (9510, 2, (8200, 0), (), "UserDefinedDOFs", None),
		"UserDefinedDOFsFlag": (9509, 2, (11, 0), (), "UserDefinedDOFsFlag", None),
		"UserDefinedDOFsforEachNodeinNodeSetFlag": (9532, 2, (11, 0), (), "UserDefinedDOFsforEachNodeinNodeSetFlag", None),
	}
	_prop_map_put_ = {
		"AutoMPCFlag": ((9528, LCID, 4, 0),()),
		"BDFFilePath": ((9504, LCID, 4, 0),()),
		"Body": ((9503, LCID, 4, 0),()),
		"DeleteDynamisDataBaseFilesFlag": ((9518, LCID, 4, 0),()),
		"DynamisInputFilePath": ((9524, LCID, 4, 0),()),
		"FixedInterfaceNormalModeLowerFrequency": ((9526, LCID, 4, 0),()),
		"FixedInterfaceNormalModeUpperFrequency": ((9527, LCID, 4, 0),()),
		"IncludeBCFlag": ((9529, LCID, 4, 0),()),
		"InterfaceNodeFDRElementMulti": ((9531, LCID, 4, 0),()),
		"InterfaceNodeIDs": ((9506, LCID, 4, 0),()),
		"InterfaceNodeSelectionType": ((9533, LCID, 4, 0),()),
		"InterfaceNodeSetMulti": ((9530, LCID, 4, 0),()),
		"InterfaceNodeset": ((9507, LCID, 4, 0),()),
		"LanczosBlockSize": ((9534, LCID, 4, 0),()),
		"LanczosBlockSizeFlag": ((9535, LCID, 4, 0),()),
		"LowerFrequency": ((9512, LCID, 4, 0),()),
		"MeshDataType": ((9502, LCID, 4, 0),()),
		"NormalModeNumber": ((9511, LCID, 4, 0),()),
		"RFIFilePath": ((9517, LCID, 4, 0),()),
		"RFITranslatorFlag": ((9519, LCID, 4, 0),()),
		"RefFrame": ((9505, LCID, 4, 0),()),
		"RemoveMidNodeRelatedInformationFlag": ((9515, LCID, 4, 0),()),
		"RemoveZeroValueForRotModeShapeFlag": ((9516, LCID, 4, 0),()),
		"SMPComputingNoThread": ((9539, LCID, 4, 0),()),
		"SavedModeNumber": ((9525, LCID, 4, 0),()),
		"ShellDrillingParameter": ((9520, LCID, 4, 0),()),
		"ShellRecoveryType": ((9523, LCID, 4, 0),()),
		"SingularCheckMaxRatio": ((9536, LCID, 4, 0),()),
		"SingularCheckMaxRatioFlag": ((9537, LCID, 4, 0),()),
		"Solver": ((9501, LCID, 4, 0),()),
		"StopSimulationWhenLowMeshQualityFlag": ((9538, LCID, 4, 0),()),
		"StrainShapeFlag": ((9522, LCID, 4, 0),()),
		"StressShapeFlag": ((9521, LCID, 4, 0),()),
		"Unit": ((9514, LCID, 4, 0),()),
		"UpperFrequency": ((9513, LCID, 4, 0),()),
		"UserDefinedDOFs": ((9510, LCID, 4, 0),()),
		"UserDefinedDOFsFlag": ((9509, LCID, 4, 0),()),
		"UserDefinedDOFsforEachNodeinNodeSetFlag": ((9532, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexGenerator(DispatchBaseClass):
	'''RFlex Generator'''
	CLSID = IID('{99AE2E87-8BEC-4292-9AA1-4F2DB831E7C8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def execute(self):
		'''
		Generate RFlex Body
		'''
		return self._oleobj_.InvokeTypes(9552, LCID, 1, (24, 0), (),)


	def _get_Option(self):
		return self._ApplyTypes_(*(9551, 2, (9, 0), (), "Option", '{7C31022B-7395-4475-99F0-ACF0A75A3698}'))

	Option = property(_get_Option, None)
	'''
	Option to generate RFlex Body

	:type: recurdyn.FlexInterface.IRFlexGenerationOption
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Option": (9551, 2, (9, 0), (), "Option", '{7C31022B-7395-4475-99F0-ACF0A75A3698}'),
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

IFlexInterface_vtables_dispatch_ = 1
IFlexInterface_vtables_ = [
	(( 'RFlexGenerator' , 'ppResult' , ), 9551, (9551, (), [ (16393, 10, None, "IID('{99AE2E87-8BEC-4292-9AA1-4F2DB831E7C8}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IRFlexGenerationOption_vtables_dispatch_ = 1
IRFlexGenerationOption_vtables_ = [
	(( 'Solver' , 'pVal' , ), 9501, (9501, (), [ (3, 1, None, "IID('{751C1136-D0D2-41B4-98DF-2C88CE95D9C4}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Solver' , 'pVal' , ), 9501, (9501, (), [ (16387, 10, None, "IID('{751C1136-D0D2-41B4-98DF-2C88CE95D9C4}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MeshDataType' , 'pVal' , ), 9502, (9502, (), [ (3, 1, None, "IID('{AA0FDD6C-F5DA-41C6-9B47-35C90BC3B3FC}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MeshDataType' , 'pVal' , ), 9502, (9502, (), [ (16387, 10, None, "IID('{AA0FDD6C-F5DA-41C6-9B47-35C90BC3B3FC}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Body' , 'ppVal' , ), 9503, (9503, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Body' , 'ppVal' , ), 9503, (9503, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'BDFFilePath' , 'pVal' , ), 9504, (9504, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'BDFFilePath' , 'pVal' , ), 9504, (9504, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RefFrame' , 'ppVal' , ), 9505, (9505, (), [ (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RefFrame' , 'ppVal' , ), 9505, (9505, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeIDs' , 'arrNodeID' , ), 9506, (9506, (), [ (8195, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeIDs' , 'arrNodeID' , ), 9506, (9506, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeset' , 'ppVal' , ), 9507, (9507, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeset' , 'ppVal' , ), 9507, (9507, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeNumber' , 'pVal' , ), 9508, (9508, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedDOFsFlag' , 'pVal' , ), 9509, (9509, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedDOFsFlag' , 'pVal' , ), 9509, (9509, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedDOFs' , 'arrUserDefinedDOF' , ), 9510, (9510, (), [ (8200, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedDOFs' , 'arrUserDefinedDOF' , ), 9510, (9510, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'NormalModeNumber' , 'pVal' , ), 9511, (9511, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NormalModeNumber' , 'pVal' , ), 9511, (9511, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'LowerFrequency' , 'pVal' , ), 9512, (9512, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'LowerFrequency' , 'pVal' , ), 9512, (9512, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UpperFrequency' , 'pVal' , ), 9513, (9513, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UpperFrequency' , 'pVal' , ), 9513, (9513, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'Unit' , 'ppVal' , ), 9514, (9514, (), [ (9, 1, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Unit' , 'ppVal' , ), 9514, (9514, (), [ (16393, 10, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RemoveMidNodeRelatedInformationFlag' , 'pVal' , ), 9515, (9515, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'RemoveMidNodeRelatedInformationFlag' , 'pVal' , ), 9515, (9515, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'RemoveZeroValueForRotModeShapeFlag' , 'pVal' , ), 9516, (9516, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'RemoveZeroValueForRotModeShapeFlag' , 'pVal' , ), 9516, (9516, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RFIFilePath' , 'pVal' , ), 9517, (9517, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'RFIFilePath' , 'pVal' , ), 9517, (9517, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'DeleteDynamisDataBaseFilesFlag' , 'pVal' , ), 9518, (9518, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'DeleteDynamisDataBaseFilesFlag' , 'pVal' , ), 9518, (9518, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'RFITranslatorFlag' , 'pVal' , ), 9519, (9519, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'RFITranslatorFlag' , 'pVal' , ), 9519, (9519, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ShellDrillingParameter' , 'pVal' , ), 9520, (9520, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ShellDrillingParameter' , 'pVal' , ), 9520, (9520, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'StressShapeFlag' , 'pVal' , ), 9521, (9521, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'StressShapeFlag' , 'pVal' , ), 9521, (9521, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'StrainShapeFlag' , 'pVal' , ), 9522, (9522, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'StrainShapeFlag' , 'pVal' , ), 9522, (9522, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 9523, (9523, (), [ (3, 1, None, "IID('{D21798C7-4AF1-416C-8CAC-FB9483D6C2CC}')") , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 9523, (9523, (), [ (16387, 10, None, "IID('{D21798C7-4AF1-416C-8CAC-FB9483D6C2CC}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'DynamisInputFilePath' , 'pVal' , ), 9524, (9524, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'DynamisInputFilePath' , 'pVal' , ), 9524, (9524, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'SavedModeNumber' , 'pVal' , ), 9525, (9525, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'SavedModeNumber' , 'pVal' , ), 9525, (9525, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'FixedInterfaceNormalModeLowerFrequency' , 'pVal' , ), 9526, (9526, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'FixedInterfaceNormalModeLowerFrequency' , 'pVal' , ), 9526, (9526, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'FixedInterfaceNormalModeUpperFrequency' , 'pVal' , ), 9527, (9527, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'FixedInterfaceNormalModeUpperFrequency' , 'pVal' , ), 9527, (9527, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'AutoMPCFlag' , 'pVal' , ), 9528, (9528, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'AutoMPCFlag' , 'pVal' , ), 9528, (9528, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'IncludeBCFlag' , 'pVal' , ), 9529, (9529, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'IncludeBCFlag' , 'pVal' , ), 9529, (9529, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeSetMulti' , 'arrNodeSet' , ), 9530, (9530, (), [ (8204, 1, None, None) , ], 1 , 4 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeSetMulti' , 'arrNodeSet' , ), 9530, (9530, (), [ (24588, 10, None, None) , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeFDRElementMulti' , 'arrFDRElementID' , ), 9531, (9531, (), [ (8195, 1, None, None) , ], 1 , 4 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeFDRElementMulti' , 'arrFDRElementID' , ), 9531, (9531, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedDOFsforEachNodeinNodeSetFlag' , 'pVal' , ), 9532, (9532, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedDOFsforEachNodeinNodeSetFlag' , 'pVal' , ), 9532, (9532, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeSelectionType' , 'pVal' , ), 9533, (9533, (), [ (3, 1, None, "IID('{5BFEC982-5971-4CD8-B118-FBF85AD5CC57}')") , ], 1 , 4 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNodeSelectionType' , 'pVal' , ), 9533, (9533, (), [ (16387, 10, None, "IID('{5BFEC982-5971-4CD8-B118-FBF85AD5CC57}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'LanczosBlockSize' , 'pVal' , ), 9534, (9534, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'LanczosBlockSize' , 'pVal' , ), 9534, (9534, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'LanczosBlockSizeFlag' , 'pVal' , ), 9535, (9535, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'LanczosBlockSizeFlag' , 'pVal' , ), 9535, (9535, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'SingularCheckMaxRatio' , 'pVal' , ), 9536, (9536, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'SingularCheckMaxRatio' , 'pVal' , ), 9536, (9536, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'SingularCheckMaxRatioFlag' , 'pVal' , ), 9537, (9537, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'SingularCheckMaxRatioFlag' , 'pVal' , ), 9537, (9537, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'StopSimulationWhenLowMeshQualityFlag' , 'bValue' , ), 9538, (9538, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'StopSimulationWhenLowMeshQualityFlag' , 'bValue' , ), 9538, (9538, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'SMPComputingNoThread' , 'uiValue' , ), 9539, (9539, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'SMPComputingNoThread' , 'uiValue' , ), 9539, (9539, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
]

IRFlexGenerator_vtables_dispatch_ = 1
IRFlexGenerator_vtables_ = [
	(( 'Option' , 'ppResult' , ), 9551, (9551, (), [ (16393, 10, None, "IID('{7C31022B-7395-4475-99F0-ACF0A75A3698}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'execute' , ), 9552, (9552, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{7C31022B-7395-4475-99F0-ACF0A75A3698}' : IRFlexGenerationOption,
	'{99AE2E87-8BEC-4292-9AA1-4F2DB831E7C8}' : IRFlexGenerator,
	'{E2DFC1B4-01F7-438E-AEEB-3285174A7BDB}' : IFlexInterface,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{7C31022B-7395-4475-99F0-ACF0A75A3698}' : 'IRFlexGenerationOption',
	'{99AE2E87-8BEC-4292-9AA1-4F2DB831E7C8}' : 'IRFlexGenerator',
	'{E2DFC1B4-01F7-438E-AEEB-3285174A7BDB}' : 'IFlexInterface',
}


NamesToIIDMap = {
	'IRFlexGenerationOption' : '{7C31022B-7395-4475-99F0-ACF0A75A3698}',
	'IRFlexGenerator' : '{99AE2E87-8BEC-4292-9AA1-4F2DB831E7C8}',
	'IFlexInterface' : '{E2DFC1B4-01F7-438E-AEEB-3285174A7BDB}',
}


