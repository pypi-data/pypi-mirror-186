# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMRFlex.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMRFlex Type Library'
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

CLSID = IID('{972DB05A-F133-4D2C-8C89-4660D161C27D}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class AScalingType(IntEnum):
	'''
	AScalingType enumeration.
	'''
	Animation_Scaling_Mode        =1         
	'''Constant value is 1.'''
	Animation_Scaling_TraRot      =0         
	'''Constant value is 0.'''
class BeamGroupInertiaPropertyInput(IntEnum):
	'''
	BeamGroupInertiaPropertyInput enumeration.
	'''
	BeamGroup_Density             =1         
	'''Constant value is 1.'''
	BeamGroup_TotalMass           =0         
	'''Constant value is 0.'''
class BeamRecoveryType(IntEnum):
	'''
	BeamRecoveryType enumeration.
	'''
	Beam_Recovery_C               =1         
	'''Constant value is 1.'''
	Beam_Recovery_D               =2         
	'''Constant value is 2.'''
	Beam_Recovery_E               =3         
	'''Constant value is 3.'''
	Beam_Recovery_F               =4         
	'''Constant value is 4.'''
	Beam_Recovery_MAX_DISTANCE    =0         
	'''Constant value is 0.'''
	Beam_Recovery_MAX_VONMISES_STRESS=5         
	'''Constant value is 5.'''
class DataPrecisionofStressStrainShapeType(IntEnum):
	'''
	DataPrecisionofStressStrainShapeType enumeration.
	'''
	DataPrecisionDouble           =1         
	'''Constant value is 1.'''
	DataPrecisionSingle           =0         
	'''Constant value is 0.'''
class DisplacementDataPrecision(IntEnum):
	'''
	DisplacementDataPrecision enumeration.
	'''
	DisplacementDataPrecision_Double=1         
	'''Constant value is 1.'''
	DisplacementDataPrecision_Float=0         
	'''Constant value is 0.'''
class FEMFATVersionType(IntEnum):
	'''
	FEMFATVersionType enumeration.
	'''
	FEMFAT_48                     =0         
	'''Constant value is 0.'''
	FEMFAT_50                     =1         
	'''Constant value is 1.'''
	FEMFAT_53                     =2         
	'''Constant value is 2.'''
	FEMFAT_532                    =3         
	'''Constant value is 3.'''
class FESoftwareType(IntEnum):
	'''
	FESoftwareType enumeration.
	'''
	Ansys                         =0         
	'''Constant value is 0.'''
	MSC_Nastran                   =2         
	'''Constant value is 2.'''
	NX_Nastran                    =1         
	'''Constant value is 1.'''
class ModalLoadCaseType(IntEnum):
	'''
	ModalLoadCaseType enumeration.
	'''
	Modal_Load                    =1         
	'''Constant value is 1.'''
	Nodal_Load                    =0         
	'''Constant value is 0.'''
class OptimizerSourceType(IntEnum):
	'''
	OptimizerSourceType enumeration.
	'''
	Optimizer_Source_RFIFILE      =0         
	'''Constant value is 0.'''
	Optimizer_Source_RFLEXBODY    =1         
	'''Constant value is 1.'''
class OptimizerType(IntEnum):
	'''
	OptimizerType enumeration.
	'''
	Optimizer_NX                  =0         
	'''Constant value is 0.'''
	Optimizer_Update              =1         
	'''Constant value is 1.'''
class RFlexMassInvariantType(IntEnum):
	'''
	RFlexMassInvariantType enumeration.
	'''
	RFlexMassInvariantType_Full   =1         
	'''Constant value is 1.'''
	RFlexMassInvariantType_Partial=0         
	'''Constant value is 0.'''
class RFlexRequestBeamRecoveryType(IntEnum):
	'''
	RFlexRequestBeamRecoveryType enumeration.
	'''
	RFlexRequestBeamRecoveryType_C=1         
	'''Constant value is 1.'''
	RFlexRequestBeamRecoveryType_D=2         
	'''Constant value is 2.'''
	RFlexRequestBeamRecoveryType_E=3         
	'''Constant value is 3.'''
	RFlexRequestBeamRecoveryType_F=4         
	'''Constant value is 4.'''
	RFlexRequestBeamRecoveryType_MAX_DISTANCE=5         
	'''Constant value is 5.'''
	RFlexRequestBeamRecoveryType_MAX_VONMISES=6         
	'''Constant value is 6.'''
	RFlexRequestBeamRecoveryType_None=0         
	'''Constant value is 0.'''
class RFlexRequestShellRecoveryType(IntEnum):
	'''
	RFlexRequestShellRecoveryType enumeration.
	'''
	RFlexRequestShellRecoveryType_Bottom=2         
	'''Constant value is 2.'''
	RFlexRequestShellRecoveryType_None=0         
	'''Constant value is 0.'''
	RFlexRequestShellRecoveryType_Top=1         
	'''Constant value is 1.'''
class RFlexRequestType(IntEnum):
	'''
	RFlexRequestType enumeration.
	'''
	RFlexRequestType_Acceleration =2         
	'''Constant value is 2.'''
	RFlexRequestType_Deformation  =3         
	'''Constant value is 3.'''
	RFlexRequestType_Displacement =0         
	'''Constant value is 0.'''
	RFlexRequestType_Strain       =4         
	'''Constant value is 4.'''
	RFlexRequestType_Stress       =5         
	'''Constant value is 5.'''
	RFlexRequestType_Velocity     =1         
	'''Constant value is 1.'''
class ShellRecoveryType(IntEnum):
	'''
	ShellRecoveryType enumeration.
	'''
	Shell_Recovery_Bottom         =1         
	'''Constant value is 1.'''
	Shell_Recovery_Top            =0         
	'''Constant value is 0.'''
	Shell_Recovery_Top_Bottom     =3         
	'''Constant value is 3.'''

from win32com.client import DispatchBaseClass
class IRFlexAnimationDataScaling(DispatchBaseClass):
	'''RFlex Animation Scaling'''
	CLSID = IID('{E3D7FEE7-8867-4A03-B9EA-A1DD773026CC}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetAnimationScalingModeShapeFactor(self):
		'''
		GSetAnimationScalingModeShapeFactor is obsolete function.
		
		:rtype: float
		'''
		return self._ApplyTypes_(3003, 1, (24, 0), ((16389, 2),), 'GetAnimationScalingModeShapeFactor', None,pythoncom.Missing
			)


	def GetAnimationScalingRotationalFactor(self):
		'''
		GetAnimationScalingRotationalFactor is obsolete function.
		
		:rtype: (float, float, float)
		'''
		return self._ApplyTypes_(55, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetAnimationScalingRotationalFactor', None,pythoncom.Missing
			, pythoncom.Missing, pythoncom.Missing)


	def GetAnimationScalingTranslationalFactor(self):
		'''
		GetAnimationScalingTranslationalFactor is obsolete function.
		
		:rtype: (float, float, float)
		'''
		return self._ApplyTypes_(53, 1, (24, 0), ((16389, 2), (16389, 2), (16389, 2)), 'GetAnimationScalingTranslationalFactor', None,pythoncom.Missing
			, pythoncom.Missing, pythoncom.Missing)


	def SetAnimationScalingModeShapeFactor(self, dFactor):
		'''
		SetAnimationScalingModeShapeFactor is obsolete function.
		
		:param dFactor: float
		'''
		return self._oleobj_.InvokeTypes(3002, LCID, 1, (24, 0), ((5, 1),),dFactor
			)


	def SetAnimationScalingRotationalFactor(self, x, y, z):
		'''
		SetAnimationScalingRotationalFactor is obsolete function.
		
		:param x: float
		:param y: float
		:param z: float
		'''
		return self._oleobj_.InvokeTypes(54, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1)),x
			, y, z)


	def SetAnimationScalingTranslationalFactor(self, x, y, z):
		'''
		SetAnimationScalingTranslationalFactor is obsolete function.
		
		:param x: float
		:param y: float
		:param z: float
		'''
		return self._oleobj_.InvokeTypes(52, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1)),x
			, y, z)


	def _get_AnimationScalingRefMarker(self):
		return self._ApplyTypes_(*(3001, 2, (9, 0), (), "AnimationScalingRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_AnimationScalingType(self):
		return self._ApplyTypes_(*(3004, 2, (3, 0), (), "AnimationScalingType", '{2480C090-3421-4383-AE29-3915E4A37E7D}'))
	def _get_ReferenceNode(self):
		return self._ApplyTypes_(*(3005, 2, (9, 0), (), "ReferenceNode", '{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}'))
	def _get_UseAnimationScaling(self):
		return self._ApplyTypes_(*(51, 2, (11, 0), (), "UseAnimationScaling", None))

	def _set_AnimationScalingRefMarker(self, value):
		if "AnimationScalingRefMarker" in self.__dict__: self.__dict__["AnimationScalingRefMarker"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_AnimationScalingType(self, value):
		if "AnimationScalingType" in self.__dict__: self.__dict__["AnimationScalingType"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_ReferenceNode(self, value):
		if "ReferenceNode" in self.__dict__: self.__dict__["ReferenceNode"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))
	def _set_UseAnimationScaling(self, value):
		if "UseAnimationScaling" in self.__dict__: self.__dict__["UseAnimationScaling"] = value; return
		self._oleobj_.Invoke(*((51, LCID, 4, 0) + (value,) + ()))

	AnimationScalingRefMarker = property(_get_AnimationScalingRefMarker, _set_AnimationScalingRefMarker)
	'''
	AnimationScalingRefMarker is obsolete property.

	:type: recurdyn.ProcessNet.IMarker
	'''
	AnimationScalingType = property(_get_AnimationScalingType, _set_AnimationScalingType)
	'''
	AnimationScalingType is obsolete property.

	:type: recurdyn.RFlex.AScalingType
	'''
	ReferenceNode = property(_get_ReferenceNode, _set_ReferenceNode)
	'''
	ReferenceNode is obsolete property.

	:type: recurdyn.RFlex.IRFlexNode
	'''
	UseAnimationScaling = property(_get_UseAnimationScaling, _set_UseAnimationScaling)
	'''
	UseAnimationScaling is obsolete property.

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_AnimationScalingRefMarker": _set_AnimationScalingRefMarker,
		"_set_AnimationScalingType": _set_AnimationScalingType,
		"_set_ReferenceNode": _set_ReferenceNode,
		"_set_UseAnimationScaling": _set_UseAnimationScaling,
	}
	_prop_map_get_ = {
		"AnimationScalingRefMarker": (3001, 2, (9, 0), (), "AnimationScalingRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"AnimationScalingType": (3004, 2, (3, 0), (), "AnimationScalingType", '{2480C090-3421-4383-AE29-3915E4A37E7D}'),
		"ReferenceNode": (3005, 2, (9, 0), (), "ReferenceNode", '{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}'),
		"UseAnimationScaling": (51, 2, (11, 0), (), "UseAnimationScaling", None),
	}
	_prop_map_put_ = {
		"AnimationScalingRefMarker": ((3001, LCID, 4, 0),()),
		"AnimationScalingType": ((3004, LCID, 4, 0),()),
		"ReferenceNode": ((3005, LCID, 4, 0),()),
		"UseAnimationScaling": ((51, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexBody(DispatchBaseClass):
	'''FunctionBay Internal Use Only'''
	CLSID = IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateElementSet(self, strName, arrElementID):
		'''
		Create a element set
		
		:param strName: str
		:param arrElementID: list[int]
		:rtype: recurdyn.RFlex.IRFlexElementSet
		'''
		ret = self._oleobj_.InvokeTypes(3032, LCID, 1, (9, 0), ((8, 1), (8195, 1)),strName
			, arrElementID)
		if ret is not None:
			ret = Dispatch(ret, 'CreateElementSet', '{312FF880-5EB3-4AE9-A989-940D556064EE}')
		return ret

	def CreateLineSet(self, strName, arrNodeID):
		'''
		Create a line set
		
		:param strName: str
		:param arrNodeID: list[int]
		:rtype: recurdyn.RFlex.IRFlexLineSet
		'''
		ret = self._oleobj_.InvokeTypes(3045, LCID, 1, (9, 0), ((8, 1), (8195, 1)),strName
			, arrNodeID)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLineSet', '{7C9E9609-3A15-4847-8B60-6AE1460A7A58}')
		return ret

	def CreateMarker(self, strName, pRefFrame):
		'''
		Create a marker
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ProcessNet.IMarker
		'''
		ret = self._oleobj_.InvokeTypes(3055, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMarker', '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')
		return ret

	def CreateMarkerOnNode(self, strName, uiNodeID):
		'''
		Create a marker on target node
		
		:param strName: str
		:param uiNodeID: int
		:rtype: recurdyn.ProcessNet.IMarker
		'''
		ret = self._oleobj_.InvokeTypes(3031, LCID, 1, (9, 0), ((8, 1), (19, 1)),strName
			, uiNodeID)
		if ret is not None:
			ret = Dispatch(ret, 'CreateMarkerOnNode', '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')
		return ret

	def CreateNodeSet(self, strName, arrNodeID):
		'''
		Create a node set
		
		:param strName: str
		:param arrNodeID: list[int]
		:rtype: recurdyn.RFlex.IRFlexNodeSet
		'''
		ret = self._oleobj_.InvokeTypes(3040, LCID, 1, (9, 0), ((8, 1), (8195, 1)),strName
			, arrNodeID)
		if ret is not None:
			ret = Dispatch(ret, 'CreateNodeSet', '{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')
		return ret

	def CreateOutput(self, strName, arrNodeID):
		'''
		Create an output
		
		:param strName: str
		:param arrNodeID: list[int]
		:rtype: recurdyn.RFlex.IRFlexOutput
		'''
		ret = self._oleobj_.InvokeTypes(3037, LCID, 1, (9, 0), ((8, 1), (8195, 1)),strName
			, arrNodeID)
		if ret is not None:
			ret = Dispatch(ret, 'CreateOutput', '{5C616B86-29F2-486F-9E0C-D66502222E30}')
		return ret

	def CreateParametricPoint(self, strName, pPoint, pRefMarker):
		'''
		Creates a parametric point
		
		:param strName: str
		:param pPoint: list[float]
		:param pRefMarker: IMarker
		:rtype: recurdyn.ProcessNet.IParametricPoint
		'''
		ret = self._oleobj_.InvokeTypes(3067, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1)),strName
			, pPoint, pRefMarker)
		if ret is not None:
			ret = Dispatch(ret, 'CreateParametricPoint', '{64B0B5B9-7662-40E8-B27C-9E42C3A158BF}')
		return ret

	def CreateParametricPointWithText(self, strName, strText, pRefMarker):
		'''
		Creates a parametric point with text
		
		:param strName: str
		:param strText: str
		:param pRefMarker: IMarker
		:rtype: recurdyn.ProcessNet.IParametricPoint
		'''
		ret = self._oleobj_.InvokeTypes(3069, LCID, 1, (9, 0), ((8, 1), (8, 1), (9, 1)),strName
			, strText, pRefMarker)
		if ret is not None:
			ret = Dispatch(ret, 'CreateParametricPointWithText', '{64B0B5B9-7662-40E8-B27C-9E42C3A158BF}')
		return ret

	def CreateParametricValue(self, strName, dValue):
		'''
		Creates a parametric value
		
		:param strName: str
		:param dValue: float
		:rtype: recurdyn.ProcessNet.IParametricValue
		'''
		ret = self._oleobj_.InvokeTypes(3068, LCID, 1, (9, 0), ((8, 1), (5, 1)),strName
			, dValue)
		if ret is not None:
			ret = Dispatch(ret, 'CreateParametricValue', '{3EEED3CE-62E8-4882-AAE6-4812B49927B5}')
		return ret

	def CreateParametricValueWithText(self, strName, strText):
		'''
		Creates a parametric value with text
		
		:param strName: str
		:param strText: str
		:rtype: recurdyn.ProcessNet.IParametricValue
		'''
		ret = self._oleobj_.InvokeTypes(3070, LCID, 1, (9, 0), ((8, 1), (8, 1)),strName
			, strText)
		if ret is not None:
			ret = Dispatch(ret, 'CreateParametricValueWithText', '{3EEED3CE-62E8-4882-AAE6-4812B49927B5}')
		return ret

	def CreatePatchSet(self, strName, arrNodeID):
		'''
		Create a patch set
		
		:param strName: str
		:param arrNodeID: list[int]
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(3033, LCID, 1, (9, 0), ((8, 1), (8195, 1)),strName
			, arrNodeID)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePatchSet', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
		return ret

	def CreatePatchSetWithBox(self, strName, pRefFrame, dWidth, dHeight, dDepth):
		'''
		Create a patch set with a box
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:param dWidth: float
		:param dHeight: float
		:param dDepth: float
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(3049, LCID, 1, (9, 0), ((8, 1), (9, 1), (5, 1), (5, 1), (5, 1)),strName
			, pRefFrame, dWidth, dHeight, dDepth)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePatchSetWithBox', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
		return ret

	def CreatePatchSetWithCone(self, strName, pFirstPoint, pSecondPoint, dTopRadius, dBottomRadius, dTolerance):
		'''
		Create a patch set with a cone
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:param dTopRadius: float
		:param dBottomRadius: float
		:param dTolerance: float
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(3059, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (5, 1), (5, 1), (5, 1)),strName
			, pFirstPoint, pSecondPoint, dTopRadius, dBottomRadius, dTolerance
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePatchSetWithCone', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
		return ret

	def CreatePatchSetWithElementIDs(self, strName, arrElementID):
		'''
		Create a patch set with ElementIDs
		
		:param strName: str
		:param arrElementID: list[int]
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(3052, LCID, 1, (9, 0), ((8, 1), (8195, 1)),strName
			, arrElementID)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePatchSetWithElementIDs', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
		return ret

	def CreatePatchSetWithElementIDsContinuous(self, strName, arrElementID, dAngle, bCheckReverse):
		'''
		Create a patch set with ElementIDs, patches connected with the external patch of the element continuoulsy
		
		:param strName: str
		:param arrElementID: list[int]
		:param dAngle: float
		:param bCheckReverse: bool
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(3051, LCID, 1, (9, 0), ((8, 1), (8195, 1), (5, 1), (11, 1)),strName
			, arrElementID, dAngle, bCheckReverse)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePatchSetWithElementIDsContinuous', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
		return ret

	def CreatePatchSetWithNodeSet(self, strName, pNodeSet):
		'''
		Create a patch set with a nodeset
		
		:param strName: str
		:param pNodeSet: IRFlexNodeSet
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(3050, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pNodeSet)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePatchSetWithNodeSet', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
		return ret

	def CreatePatchSetWithPatchIndices(self, strName, arrPatchesIndices):
		'''
		Create a patch set with patches' indices
		
		:param strName: str
		:param arrPatchesIndices: list[int]
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(3053, LCID, 1, (9, 0), ((8, 1), (8195, 1)),strName
			, arrPatchesIndices)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePatchSetWithPatchIndices', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
		return ret

	def CreatePatchSetWithPatchIndicesContinuous(self, strName, arrPatchesIndices, dAngle, bCheckReverse):
		'''
		Create a patch set with patches' indices, patches connected continuously will be used for the patchset
		
		:param strName: str
		:param arrPatchesIndices: list[int]
		:param dAngle: float
		:param bCheckReverse: bool
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(3054, LCID, 1, (9, 0), ((8, 1), (8195, 1), (5, 1), (11, 1)),strName
			, arrPatchesIndices, dAngle, bCheckReverse)
		if ret is not None:
			ret = Dispatch(ret, 'CreatePatchSetWithPatchIndicesContinuous', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
		return ret

	def DeleteAnimationScaling(self):
		'''
		Delete Animation Scaling
		'''
		return self._oleobj_.InvokeTypes(3074, LCID, 1, (24, 0), (),)


	def ExportParametricPoint(self, strFileName):
		'''
		Export parametric point
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(3064, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def ExportParametricValue(self, strFileName):
		'''
		Export parametric value
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(3066, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def GetElementByID(self, nID):
		'''
		Get element by ID
		
		:param nID: int
		:rtype: recurdyn.RFlex.IRFlexElement
		'''
		ret = self._oleobj_.InvokeTypes(3058, LCID, 1, (9, 0), ((3, 1),),nID
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetElementByID', '{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}')
		return ret

	def GetEntity(self, strName):
		'''
		Get an entity
		
		:param strName: str
		:rtype: recurdyn.ProcessNet.IGeneric
		'''
		ret = self._oleobj_.InvokeTypes(3036, LCID, 1, (9, 0), ((8, 1),),strName
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetEntity', '{27A86788-8B85-40CF-BE7F-BA915103A7DB}')
		return ret

	def GetNodeByID(self, nID):
		'''
		Get node by ID
		
		:param nID: int
		:rtype: recurdyn.RFlex.IRFlexNode
		'''
		ret = self._oleobj_.InvokeTypes(3057, LCID, 1, (9, 0), ((3, 1),),nID
			)
		if ret is not None:
			ret = Dispatch(ret, 'GetNodeByID', '{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def ImportParametricPoint(self, strFileName):
		'''
		Import parametric point
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(3063, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def ImportParametricValue(self, strFileName):
		'''
		Import parametric value
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(3065, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def ModeInformation(self, pModeSequence):
		'''
		Get the Mode Information
		
		:param pModeSequence: int
		:rtype: recurdyn.RFlex.IRFlexModeInformation
		'''
		ret = self._oleobj_.InvokeTypes(3027, LCID, 1, (9, 0), ((19, 1),),pModeSequence
			)
		if ret is not None:
			ret = Dispatch(ret, 'ModeInformation', '{7ED2BDE4-77AC-4D41-8745-10EB8FC6812C}')
		return ret

	def _get_Active(self):
		return self._ApplyTypes_(*(3072, 2, (11, 0), (), "Active", None))
	def _get_AnimationDataScaling(self):
		return self._ApplyTypes_(*(3029, 2, (9, 0), (), "AnimationDataScaling", '{E3D7FEE7-8867-4A03-B9EA-A1DD773026CC}'))
	def _get_AnimationScaling(self):
		return self._ApplyTypes_(*(3073, 2, (9, 0), (), "AnimationScaling", '{13F0E996-9155-4427-BF61-8A8D60739288}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DisplaySetting(self):
		return self._ApplyTypes_(*(3042, 2, (9, 0), (), "DisplaySetting", '{3FDF0768-0052-4B63-9D84-A644C3152051}'))
	def _get_ExportShellFormatData(self):
		return self._ApplyTypes_(*(3043, 2, (9, 0), (), "ExportShellFormatData", '{2EE15E44-AD0C-4D9B-B53A-35BF7F1E1322}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(3030, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_InitialRotationalVelocityX(self):
		return self._ApplyTypes_(*(3015, 2, (9, 0), (), "InitialRotationalVelocityX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InitialRotationalVelocityY(self):
		return self._ApplyTypes_(*(3016, 2, (9, 0), (), "InitialRotationalVelocityY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InitialRotationalVelocityZ(self):
		return self._ApplyTypes_(*(3017, 2, (9, 0), (), "InitialRotationalVelocityZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InitialTranslationalVelocityX(self):
		return self._ApplyTypes_(*(3009, 2, (9, 0), (), "InitialTranslationalVelocityX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InitialTranslationalVelocityY(self):
		return self._ApplyTypes_(*(3010, 2, (9, 0), (), "InitialTranslationalVelocityY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InitialTranslationalVelocityZ(self):
		return self._ApplyTypes_(*(3011, 2, (9, 0), (), "InitialTranslationalVelocityZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(3003, 2, (5, 0), (), "Ixx", None))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(3006, 2, (5, 0), (), "Ixy", None))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(3004, 2, (5, 0), (), "Iyy", None))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(3007, 2, (5, 0), (), "Iyz", None))
	def _get_Izx(self):
		return self._ApplyTypes_(*(3008, 2, (5, 0), (), "Izx", None))
	def _get_Izz(self):
		return self._ApplyTypes_(*(3005, 2, (5, 0), (), "Izz", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(3060, 2, (19, 0), (), "LayerNumber", None))
	def _get_MarkerCollection(self):
		return self._ApplyTypes_(*(3047, 2, (9, 0), (), "MarkerCollection", '{6BEF9B6B-4708-445E-A3B5-0D65BA69F748}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(3002, 2, (5, 0), (), "Mass", None))
	def _get_MassInvariant(self):
		return self._ApplyTypes_(*(3048, 2, (3, 0), (), "MassInvariant", '{5BA4E584-3306-4C81-89A9-A452C0BE259D}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberOfMode(self):
		return self._ApplyTypes_(*(3025, 2, (19, 0), (), "NumberOfMode", None))
	def _get_OutputFileInfo(self):
		return self._ApplyTypes_(*(3041, 2, (9, 0), (), "OutputFileInfo", '{16BD870A-FA04-42F6-8B8D-7F484F5D421E}'))
	def _get_OutputFileInfoforRegenerator(self):
		return self._ApplyTypes_(*(3044, 2, (9, 0), (), "OutputFileInfoforRegenerator", '{1B06647C-BAD6-464A-8B5E-DD243D535970}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ParametricPointCollection(self):
		return self._ApplyTypes_(*(3061, 2, (9, 0), (), "ParametricPointCollection", '{65267578-7015-4BB5-BB65-F5F81CCEA244}'))
	def _get_ParametricValueCollection(self):
		return self._ApplyTypes_(*(3062, 2, (9, 0), (), "ParametricValueCollection", '{65267578-7015-4BB5-BB65-F5F81CCEA245}'))
	def _get_RFIFileName(self):
		return self._ApplyTypes_(*(3026, 2, (8, 0), (), "RFIFileName", None))
	def _get_RFlexElementCollection(self):
		return self._ApplyTypes_(*(3056, 2, (9, 0), (), "RFlexElementCollection", '{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}'))
	def _get_RFlexElementSetCollection(self):
		return self._ApplyTypes_(*(3034, 2, (9, 0), (), "RFlexElementSetCollection", '{B1A8C8FA-7869-4CB5-A285-91BCC4C2ADA3}'))
	def _get_RFlexLineSetCollection(self):
		return self._ApplyTypes_(*(3071, 2, (9, 0), (), "RFlexLineSetCollection", '{05938874-D404-42C9-9757-863978D57DE5}'))
	def _get_RFlexNodeCollection(self):
		return self._ApplyTypes_(*(3046, 2, (9, 0), (), "RFlexNodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'))
	def _get_RFlexNodeSetCollection(self):
		return self._ApplyTypes_(*(3039, 2, (9, 0), (), "RFlexNodeSetCollection", '{2AAD6766-1ED5-498D-96BA-F9363B2DF588}'))
	def _get_RFlexOutputCollection(self):
		return self._ApplyTypes_(*(3038, 2, (9, 0), (), "RFlexOutputCollection", '{D1E612A4-BFE5-4676-B55D-76C41FE47B42}'))
	def _get_RFlexPatchSetCollection(self):
		return self._ApplyTypes_(*(3035, 2, (9, 0), (), "RFlexPatchSetCollection", '{6A9E16A5-2CCC-4596-BDC0-07B767DB1A39}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(3001, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RotationalVelocityRefMarker(self):
		return self._ApplyTypes_(*(3022, 2, (9, 0), (), "RotationalVelocityRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_TranslationalVelocityRefMarker(self):
		return self._ApplyTypes_(*(3021, 2, (9, 0), (), "TranslationalVelocityRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_UseInitialRotationalVelocityX(self):
		return self._ApplyTypes_(*(3018, 2, (11, 0), (), "UseInitialRotationalVelocityX", None))
	def _get_UseInitialRotationalVelocityY(self):
		return self._ApplyTypes_(*(3019, 2, (11, 0), (), "UseInitialRotationalVelocityY", None))
	def _get_UseInitialRotationalVelocityZ(self):
		return self._ApplyTypes_(*(3020, 2, (11, 0), (), "UseInitialRotationalVelocityZ", None))
	def _get_UseInitialTranslationalVelocityX(self):
		return self._ApplyTypes_(*(3012, 2, (11, 0), (), "UseInitialTranslationalVelocityX", None))
	def _get_UseInitialTranslationalVelocityY(self):
		return self._ApplyTypes_(*(3013, 2, (11, 0), (), "UseInitialTranslationalVelocityY", None))
	def _get_UseInitialTranslationalVelocityZ(self):
		return self._ApplyTypes_(*(3014, 2, (11, 0), (), "UseInitialTranslationalVelocityZ", None))
	def _get_UseUserDefinedRigidBodyFrequency(self):
		return self._ApplyTypes_(*(3023, 2, (11, 0), (), "UseUserDefinedRigidBodyFrequency", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_UserDefinedRigidBodyFrequency(self):
		return self._ApplyTypes_(*(3024, 2, (9, 0), (), "UserDefinedRigidBodyFrequency", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((3072, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((3060, LCID, 4, 0) + (value,) + ()))
	def _set_MassInvariant(self, value):
		if "MassInvariant" in self.__dict__: self.__dict__["MassInvariant"] = value; return
		self._oleobj_.Invoke(*((3048, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_RFIFileName(self, value):
		if "RFIFileName" in self.__dict__: self.__dict__["RFIFileName"] = value; return
		self._oleobj_.Invoke(*((3026, LCID, 4, 0) + (value,) + ()))
	def _set_RotationalVelocityRefMarker(self, value):
		if "RotationalVelocityRefMarker" in self.__dict__: self.__dict__["RotationalVelocityRefMarker"] = value; return
		self._oleobj_.Invoke(*((3022, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationalVelocityRefMarker(self, value):
		if "TranslationalVelocityRefMarker" in self.__dict__: self.__dict__["TranslationalVelocityRefMarker"] = value; return
		self._oleobj_.Invoke(*((3021, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialRotationalVelocityX(self, value):
		if "UseInitialRotationalVelocityX" in self.__dict__: self.__dict__["UseInitialRotationalVelocityX"] = value; return
		self._oleobj_.Invoke(*((3018, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialRotationalVelocityY(self, value):
		if "UseInitialRotationalVelocityY" in self.__dict__: self.__dict__["UseInitialRotationalVelocityY"] = value; return
		self._oleobj_.Invoke(*((3019, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialRotationalVelocityZ(self, value):
		if "UseInitialRotationalVelocityZ" in self.__dict__: self.__dict__["UseInitialRotationalVelocityZ"] = value; return
		self._oleobj_.Invoke(*((3020, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialTranslationalVelocityX(self, value):
		if "UseInitialTranslationalVelocityX" in self.__dict__: self.__dict__["UseInitialTranslationalVelocityX"] = value; return
		self._oleobj_.Invoke(*((3012, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialTranslationalVelocityY(self, value):
		if "UseInitialTranslationalVelocityY" in self.__dict__: self.__dict__["UseInitialTranslationalVelocityY"] = value; return
		self._oleobj_.Invoke(*((3013, LCID, 4, 0) + (value,) + ()))
	def _set_UseInitialTranslationalVelocityZ(self, value):
		if "UseInitialTranslationalVelocityZ" in self.__dict__: self.__dict__["UseInitialTranslationalVelocityZ"] = value; return
		self._oleobj_.Invoke(*((3014, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserDefinedRigidBodyFrequency(self, value):
		if "UseUserDefinedRigidBodyFrequency" in self.__dict__: self.__dict__["UseUserDefinedRigidBodyFrequency"] = value; return
		self._oleobj_.Invoke(*((3023, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	AnimationDataScaling = property(_get_AnimationDataScaling, None)
	'''
	AnimationDataScaling is obsolete property.

	:type: recurdyn.RFlex.IRFlexAnimationDataScaling
	'''
	AnimationScaling = property(_get_AnimationScaling, None)
	'''
	AnimationScaling

	:type: recurdyn.ProcessNet.IAnimationScaling
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DisplaySetting = property(_get_DisplaySetting, None)
	'''
	Get Display Setting

	:type: recurdyn.Flexible.IDisplaySetting
	'''
	ExportShellFormatData = property(_get_ExportShellFormatData, None)
	'''
	Get Export Shell Format Data

	:type: recurdyn.Flexible.IExportShellFormatData
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
	InitialRotationalVelocityX = property(_get_InitialRotationalVelocityX, None)
	'''
	Initial rotational velocity X

	:type: recurdyn.ProcessNet.IDouble
	'''
	InitialRotationalVelocityY = property(_get_InitialRotationalVelocityY, None)
	'''
	Initial rotational velocity Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	InitialRotationalVelocityZ = property(_get_InitialRotationalVelocityZ, None)
	'''
	Initial rotational velocity Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	InitialTranslationalVelocityX = property(_get_InitialTranslationalVelocityX, None)
	'''
	Initial translational velocity X

	:type: recurdyn.ProcessNet.IDouble
	'''
	InitialTranslationalVelocityY = property(_get_InitialTranslationalVelocityY, None)
	'''
	Initial translational velocity Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	InitialTranslationalVelocityZ = property(_get_InitialTranslationalVelocityZ, None)
	'''
	Initial translational velocity Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: float
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: float
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: float
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: float
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: float
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: float
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	MarkerCollection = property(_get_MarkerCollection, None)
	'''
	Contains Marker

	:type: recurdyn.ProcessNet.IMarkerCollection
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: float
	'''
	MassInvariant = property(_get_MassInvariant, _set_MassInvariant)
	'''
	Mass Invariant Type

	:type: recurdyn.RFlex.RFlexMassInvariantType
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NumberOfMode = property(_get_NumberOfMode, None)
	'''
	Number of Mode

	:type: int
	'''
	OutputFileInfo = property(_get_OutputFileInfo, None)
	'''
	Get RFlex Output File Info

	:type: recurdyn.RFlex.IRFlexOutputFileInfo
	'''
	OutputFileInfoforRegenerator = property(_get_OutputFileInfoforRegenerator, None)
	'''
	Get RFlex Output File Info for regenerator

	:type: recurdyn.RFlex.IRFlexOutputFileInfoForRegenerator
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
	ParametricPointCollection = property(_get_ParametricPointCollection, None)
	ParametricValueCollection = property(_get_ParametricValueCollection, None)
	RFIFileName = property(_get_RFIFileName, _set_RFIFileName)
	'''
	RFI File Name

	:type: str
	'''
	RFlexElementCollection = property(_get_RFlexElementCollection, None)
	'''
	Contains Element

	:type: recurdyn.RFlex.IRFlexElementCollection
	'''
	RFlexElementSetCollection = property(_get_RFlexElementSetCollection, None)
	'''
	Contains ElementSet

	:type: recurdyn.RFlex.IRFlexElementSetCollection
	'''
	RFlexLineSetCollection = property(_get_RFlexLineSetCollection, None)
	'''
	Contains LineSet

	:type: recurdyn.RFlex.IRFlexLineSetCollection
	'''
	RFlexNodeCollection = property(_get_RFlexNodeCollection, None)
	'''
	Contains Node

	:type: recurdyn.RFlex.IRFlexNodeCollection
	'''
	RFlexNodeSetCollection = property(_get_RFlexNodeSetCollection, None)
	'''
	Contains NodeSet

	:type: recurdyn.RFlex.IRFlexNodeSetCollection
	'''
	RFlexOutputCollection = property(_get_RFlexOutputCollection, None)
	'''
	Contains Output

	:type: recurdyn.RFlex.IRFlexOutputCollection
	'''
	RFlexPatchSetCollection = property(_get_RFlexPatchSetCollection, None)
	'''
	Contains PatchSet

	:type: recurdyn.RFlex.IRFlexPatchSetCollection
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RotationalVelocityRefMarker = property(_get_RotationalVelocityRefMarker, _set_RotationalVelocityRefMarker)
	'''
	Rotational velocity reference marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	TranslationalVelocityRefMarker = property(_get_TranslationalVelocityRefMarker, _set_TranslationalVelocityRefMarker)
	'''
	Translational velocity reference marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	UseInitialRotationalVelocityX = property(_get_UseInitialRotationalVelocityX, _set_UseInitialRotationalVelocityX)
	'''
	Use Initial rotational velocity X

	:type: bool
	'''
	UseInitialRotationalVelocityY = property(_get_UseInitialRotationalVelocityY, _set_UseInitialRotationalVelocityY)
	'''
	Use Initial rotational velocity Y

	:type: bool
	'''
	UseInitialRotationalVelocityZ = property(_get_UseInitialRotationalVelocityZ, _set_UseInitialRotationalVelocityZ)
	'''
	Use Initial rotational velocity Z

	:type: bool
	'''
	UseInitialTranslationalVelocityX = property(_get_UseInitialTranslationalVelocityX, _set_UseInitialTranslationalVelocityX)
	'''
	Use initial translational velocity X

	:type: bool
	'''
	UseInitialTranslationalVelocityY = property(_get_UseInitialTranslationalVelocityY, _set_UseInitialTranslationalVelocityY)
	'''
	Use initial translational velocity Y

	:type: bool
	'''
	UseInitialTranslationalVelocityZ = property(_get_UseInitialTranslationalVelocityZ, _set_UseInitialTranslationalVelocityZ)
	'''
	Use initial translational velocity Z

	:type: bool
	'''
	UseUserDefinedRigidBodyFrequency = property(_get_UseUserDefinedRigidBodyFrequency, _set_UseUserDefinedRigidBodyFrequency)
	'''
	Use the user-defined rigid mode frequency

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	UserDefinedRigidBodyFrequency = property(_get_UserDefinedRigidBodyFrequency, None)
	'''
	User-defined rigid mode frequency

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_MassInvariant": _set_MassInvariant,
		"_set_Name": _set_Name,
		"_set_RFIFileName": _set_RFIFileName,
		"_set_RotationalVelocityRefMarker": _set_RotationalVelocityRefMarker,
		"_set_TranslationalVelocityRefMarker": _set_TranslationalVelocityRefMarker,
		"_set_UseInitialRotationalVelocityX": _set_UseInitialRotationalVelocityX,
		"_set_UseInitialRotationalVelocityY": _set_UseInitialRotationalVelocityY,
		"_set_UseInitialRotationalVelocityZ": _set_UseInitialRotationalVelocityZ,
		"_set_UseInitialTranslationalVelocityX": _set_UseInitialTranslationalVelocityX,
		"_set_UseInitialTranslationalVelocityY": _set_UseInitialTranslationalVelocityY,
		"_set_UseInitialTranslationalVelocityZ": _set_UseInitialTranslationalVelocityZ,
		"_set_UseUserDefinedRigidBodyFrequency": _set_UseUserDefinedRigidBodyFrequency,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (3072, 2, (11, 0), (), "Active", None),
		"AnimationDataScaling": (3029, 2, (9, 0), (), "AnimationDataScaling", '{E3D7FEE7-8867-4A03-B9EA-A1DD773026CC}'),
		"AnimationScaling": (3073, 2, (9, 0), (), "AnimationScaling", '{13F0E996-9155-4427-BF61-8A8D60739288}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DisplaySetting": (3042, 2, (9, 0), (), "DisplaySetting", '{3FDF0768-0052-4B63-9D84-A644C3152051}'),
		"ExportShellFormatData": (3043, 2, (9, 0), (), "ExportShellFormatData", '{2EE15E44-AD0C-4D9B-B53A-35BF7F1E1322}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (3030, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"InitialRotationalVelocityX": (3015, 2, (9, 0), (), "InitialRotationalVelocityX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InitialRotationalVelocityY": (3016, 2, (9, 0), (), "InitialRotationalVelocityY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InitialRotationalVelocityZ": (3017, 2, (9, 0), (), "InitialRotationalVelocityZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InitialTranslationalVelocityX": (3009, 2, (9, 0), (), "InitialTranslationalVelocityX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InitialTranslationalVelocityY": (3010, 2, (9, 0), (), "InitialTranslationalVelocityY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InitialTranslationalVelocityZ": (3011, 2, (9, 0), (), "InitialTranslationalVelocityZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixx": (3003, 2, (5, 0), (), "Ixx", None),
		"Ixy": (3006, 2, (5, 0), (), "Ixy", None),
		"Iyy": (3004, 2, (5, 0), (), "Iyy", None),
		"Iyz": (3007, 2, (5, 0), (), "Iyz", None),
		"Izx": (3008, 2, (5, 0), (), "Izx", None),
		"Izz": (3005, 2, (5, 0), (), "Izz", None),
		"LayerNumber": (3060, 2, (19, 0), (), "LayerNumber", None),
		"MarkerCollection": (3047, 2, (9, 0), (), "MarkerCollection", '{6BEF9B6B-4708-445E-A3B5-0D65BA69F748}'),
		"Mass": (3002, 2, (5, 0), (), "Mass", None),
		"MassInvariant": (3048, 2, (3, 0), (), "MassInvariant", '{5BA4E584-3306-4C81-89A9-A452C0BE259D}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberOfMode": (3025, 2, (19, 0), (), "NumberOfMode", None),
		"OutputFileInfo": (3041, 2, (9, 0), (), "OutputFileInfo", '{16BD870A-FA04-42F6-8B8D-7F484F5D421E}'),
		"OutputFileInfoforRegenerator": (3044, 2, (9, 0), (), "OutputFileInfoforRegenerator", '{1B06647C-BAD6-464A-8B5E-DD243D535970}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ParametricPointCollection": (3061, 2, (9, 0), (), "ParametricPointCollection", '{65267578-7015-4BB5-BB65-F5F81CCEA244}'),
		"ParametricValueCollection": (3062, 2, (9, 0), (), "ParametricValueCollection", '{65267578-7015-4BB5-BB65-F5F81CCEA245}'),
		"RFIFileName": (3026, 2, (8, 0), (), "RFIFileName", None),
		"RFlexElementCollection": (3056, 2, (9, 0), (), "RFlexElementCollection", '{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}'),
		"RFlexElementSetCollection": (3034, 2, (9, 0), (), "RFlexElementSetCollection", '{B1A8C8FA-7869-4CB5-A285-91BCC4C2ADA3}'),
		"RFlexLineSetCollection": (3071, 2, (9, 0), (), "RFlexLineSetCollection", '{05938874-D404-42C9-9757-863978D57DE5}'),
		"RFlexNodeCollection": (3046, 2, (9, 0), (), "RFlexNodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'),
		"RFlexNodeSetCollection": (3039, 2, (9, 0), (), "RFlexNodeSetCollection", '{2AAD6766-1ED5-498D-96BA-F9363B2DF588}'),
		"RFlexOutputCollection": (3038, 2, (9, 0), (), "RFlexOutputCollection", '{D1E612A4-BFE5-4676-B55D-76C41FE47B42}'),
		"RFlexPatchSetCollection": (3035, 2, (9, 0), (), "RFlexPatchSetCollection", '{6A9E16A5-2CCC-4596-BDC0-07B767DB1A39}'),
		"RefFrame": (3001, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RotationalVelocityRefMarker": (3022, 2, (9, 0), (), "RotationalVelocityRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"TranslationalVelocityRefMarker": (3021, 2, (9, 0), (), "TranslationalVelocityRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"UseInitialRotationalVelocityX": (3018, 2, (11, 0), (), "UseInitialRotationalVelocityX", None),
		"UseInitialRotationalVelocityY": (3019, 2, (11, 0), (), "UseInitialRotationalVelocityY", None),
		"UseInitialRotationalVelocityZ": (3020, 2, (11, 0), (), "UseInitialRotationalVelocityZ", None),
		"UseInitialTranslationalVelocityX": (3012, 2, (11, 0), (), "UseInitialTranslationalVelocityX", None),
		"UseInitialTranslationalVelocityY": (3013, 2, (11, 0), (), "UseInitialTranslationalVelocityY", None),
		"UseInitialTranslationalVelocityZ": (3014, 2, (11, 0), (), "UseInitialTranslationalVelocityZ", None),
		"UseUserDefinedRigidBodyFrequency": (3023, 2, (11, 0), (), "UseUserDefinedRigidBodyFrequency", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"UserDefinedRigidBodyFrequency": (3024, 2, (9, 0), (), "UserDefinedRigidBodyFrequency", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Active": ((3072, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((3060, LCID, 4, 0),()),
		"MassInvariant": ((3048, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"RFIFileName": ((3026, LCID, 4, 0),()),
		"RotationalVelocityRefMarker": ((3022, LCID, 4, 0),()),
		"TranslationalVelocityRefMarker": ((3021, LCID, 4, 0),()),
		"UseInitialRotationalVelocityX": ((3018, LCID, 4, 0),()),
		"UseInitialRotationalVelocityY": ((3019, LCID, 4, 0),()),
		"UseInitialRotationalVelocityZ": ((3020, LCID, 4, 0),()),
		"UseInitialTranslationalVelocityX": ((3012, LCID, 4, 0),()),
		"UseInitialTranslationalVelocityY": ((3013, LCID, 4, 0),()),
		"UseInitialTranslationalVelocityZ": ((3014, LCID, 4, 0),()),
		"UseUserDefinedRigidBodyFrequency": ((3023, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexBodyCollection(DispatchBaseClass):
	'''IRFlexBodyCollection'''
	CLSID = IID('{BF6E3DD3-F1E6-4FE4-B15F-4BAE1BFCBF48}')
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
		:rtype: recurdyn.RFlex.IRFlexBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5737600D-0E40-4578-9E18-8CBE68916DF8}')
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
		:rtype: recurdyn.RFlex.IRFlexBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5737600D-0E40-4578-9E18-8CBE68916DF8}')
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
		return win32com.client.util.Iterator(ob, '{5737600D-0E40-4578-9E18-8CBE68916DF8}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{5737600D-0E40-4578-9E18-8CBE68916DF8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexBodyImportOption(DispatchBaseClass):
	'''RFlexBody import option'''
	CLSID = IID('{8BE11A36-210D-41C5-AB9D-229134DCCA7E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_UseInternalNodes(self):
		return self._ApplyTypes_(*(3003, 2, (11, 0), (), "UseInternalNodes", None))
	def _get_UseNodalResidual(self):
		return self._ApplyTypes_(*(3000, 2, (11, 0), (), "UseNodalResidual", None))
	def _get_UseUserDefinedRigidBodyFrequency(self):
		return self._ApplyTypes_(*(3001, 2, (11, 0), (), "UseUserDefinedRigidBodyFrequency", None))
	def _get_UserDefinedRigidBodyFrequency(self):
		return self._ApplyTypes_(*(3002, 2, (5, 0), (), "UserDefinedRigidBodyFrequency", None))

	def _set_UseInternalNodes(self, value):
		if "UseInternalNodes" in self.__dict__: self.__dict__["UseInternalNodes"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_UseNodalResidual(self, value):
		if "UseNodalResidual" in self.__dict__: self.__dict__["UseNodalResidual"] = value; return
		self._oleobj_.Invoke(*((3000, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserDefinedRigidBodyFrequency(self, value):
		if "UseUserDefinedRigidBodyFrequency" in self.__dict__: self.__dict__["UseUserDefinedRigidBodyFrequency"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedRigidBodyFrequency(self, value):
		if "UserDefinedRigidBodyFrequency" in self.__dict__: self.__dict__["UserDefinedRigidBodyFrequency"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))

	UseInternalNodes = property(_get_UseInternalNodes, _set_UseInternalNodes)
	'''
	UseInternalNodes is obsolete function

	:type: bool
	'''
	UseNodalResidual = property(_get_UseNodalResidual, _set_UseNodalResidual)
	'''
	UseNodalResidual is obsolete function

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
		"_set_UseInternalNodes": _set_UseInternalNodes,
		"_set_UseNodalResidual": _set_UseNodalResidual,
		"_set_UseUserDefinedRigidBodyFrequency": _set_UseUserDefinedRigidBodyFrequency,
		"_set_UserDefinedRigidBodyFrequency": _set_UserDefinedRigidBodyFrequency,
	}
	_prop_map_get_ = {
		"UseInternalNodes": (3003, 2, (11, 0), (), "UseInternalNodes", None),
		"UseNodalResidual": (3000, 2, (11, 0), (), "UseNodalResidual", None),
		"UseUserDefinedRigidBodyFrequency": (3001, 2, (11, 0), (), "UseUserDefinedRigidBodyFrequency", None),
		"UserDefinedRigidBodyFrequency": (3002, 2, (5, 0), (), "UserDefinedRigidBodyFrequency", None),
	}
	_prop_map_put_ = {
		"UseInternalNodes": ((3003, LCID, 4, 0),()),
		"UseNodalResidual": ((3000, LCID, 4, 0),()),
		"UseUserDefinedRigidBodyFrequency": ((3001, LCID, 4, 0),()),
		"UserDefinedRigidBodyFrequency": ((3002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexElement(DispatchBaseClass):
	'''RFlex Element'''
	CLSID = IID('{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}')
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
	def _get_ElementType(self):
		return self._ApplyTypes_(*(152, 2, (3, 0), (), "ElementType", '{59250D4D-5C1C-4CEE-80A4-42A64F61F138}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_ID(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "ID", None))
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
	ElementType = property(_get_ElementType, None)
	'''
	Element type

	:type: recurdyn.ProcessNet.FlexibleElementType
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	ID = property(_get_ID, None)
	'''
	ID

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
		"ElementType": (152, 2, (3, 0), (), "ElementType", '{59250D4D-5C1C-4CEE-80A4-42A64F61F138}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"ID": (151, 2, (19, 0), (), "ID", None),
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

class IRFlexElementCollection(DispatchBaseClass):
	'''IRFlexElementCollection'''
	CLSID = IID('{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}')
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
		:rtype: recurdyn.RFlex.IRFlexElement
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}')
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
		:rtype: recurdyn.RFlex.IRFlexElement
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}')
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
		return win32com.client.util.Iterator(ob, '{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexElementSet(DispatchBaseClass):
	CLSID = IID('{312FF880-5EB3-4AE9-A989-940D556064EE}')
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
		return self._ApplyTypes_(*(3051, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ElementCollection(self):
		return self._ApplyTypes_(*(3052, 2, (9, 0), (), "ElementCollection", '{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeCollection(self):
		return self._ApplyTypes_(*(3053, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((3051, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Element set color

	:type: int
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ElementCollection = property(_get_ElementCollection, None)
	'''
	Element Collection

	:type: recurdyn.RFlex.IRFlexElementCollection
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
	NodeCollection = property(_get_NodeCollection, None)
	'''
	Node Collection of Element set

	:type: recurdyn.RFlex.IRFlexNodeCollection
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
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Color": (3051, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ElementCollection": (3052, 2, (9, 0), (), "ElementCollection", '{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeCollection": (3053, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Color": ((3051, LCID, 4, 0),()),
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

class IRFlexElementSetCollection(DispatchBaseClass):
	'''IRFlexElementSetCollection'''
	CLSID = IID('{B1A8C8FA-7869-4CB5-A285-91BCC4C2ADA3}')
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
		:rtype: recurdyn.RFlex.IRFlexElementSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{312FF880-5EB3-4AE9-A989-940D556064EE}')
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
		:rtype: recurdyn.RFlex.IRFlexElementSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{312FF880-5EB3-4AE9-A989-940D556064EE}')
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
		return win32com.client.util.Iterator(ob, '{312FF880-5EB3-4AE9-A989-940D556064EE}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{312FF880-5EB3-4AE9-A989-940D556064EE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexExportDurabilityInterfaceOption(DispatchBaseClass):
	'''option used in exporting durability interface'''
	CLSID = IID('{EB3A9E9B-54A9-440F-A594-294F547AA27A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_CreateFEMFATUnitStressScratchFileFlag(self):
		return self._ApplyTypes_(*(3002, 2, (11, 0), (), "CreateFEMFATUnitStressScratchFileFlag", None))
	def _get_LoadFactor(self):
		return self._ApplyTypes_(*(3000, 2, (5, 0), (), "LoadFactor", None))
	def _get_MaxFileName(self):
		return self._ApplyTypes_(*(3005, 2, (8, 0), (), "MaxFileName", None))
	def _get_RPCFileName(self):
		return self._ApplyTypes_(*(3003, 2, (8, 0), (), "RPCFileName", None))
	def _get_ScratchFileName(self):
		return self._ApplyTypes_(*(3004, 2, (8, 0), (), "ScratchFileName", None))
	def _get_ViewModalCoordinates(self):
		return self._ApplyTypes_(*(3001, 2, (8203, 0), (), "ViewModalCoordinates", None))

	def _set_CreateFEMFATUnitStressScratchFileFlag(self, value):
		if "CreateFEMFATUnitStressScratchFileFlag" in self.__dict__: self.__dict__["CreateFEMFATUnitStressScratchFileFlag"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_LoadFactor(self, value):
		if "LoadFactor" in self.__dict__: self.__dict__["LoadFactor"] = value; return
		self._oleobj_.Invoke(*((3000, LCID, 4, 0) + (value,) + ()))
	def _set_MaxFileName(self, value):
		if "MaxFileName" in self.__dict__: self.__dict__["MaxFileName"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))
	def _set_RPCFileName(self, value):
		if "RPCFileName" in self.__dict__: self.__dict__["RPCFileName"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_ScratchFileName(self, value):
		if "ScratchFileName" in self.__dict__: self.__dict__["ScratchFileName"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_ViewModalCoordinates(self, value):
		if "ViewModalCoordinates" in self.__dict__: self.__dict__["ViewModalCoordinates"] = value; return
		variantValue = win32com.client.VARIANT(8203, value)
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (variantValue,) + ()))

	CreateFEMFATUnitStressScratchFileFlag = property(_get_CreateFEMFATUnitStressScratchFileFlag, _set_CreateFEMFATUnitStressScratchFileFlag)
	'''
	Create FEMFAT Unit Stress Scratch File

	:type: bool
	'''
	LoadFactor = property(_get_LoadFactor, _set_LoadFactor)
	'''
	Load Factor

	:type: float
	'''
	MaxFileName = property(_get_MaxFileName, _set_MaxFileName)
	'''
	Max File Name

	:type: str
	'''
	RPCFileName = property(_get_RPCFileName, _set_RPCFileName)
	'''
	RPC File Name

	:type: str
	'''
	ScratchFileName = property(_get_ScratchFileName, _set_ScratchFileName)
	'''
	Scratch File Name

	:type: str
	'''
	ViewModalCoordinates = property(_get_ViewModalCoordinates, _set_ViewModalCoordinates)
	'''
	View Modal Coordinates

	:type: list[bool]
	'''

	_prop_map_set_function_ = {
		"_set_CreateFEMFATUnitStressScratchFileFlag": _set_CreateFEMFATUnitStressScratchFileFlag,
		"_set_LoadFactor": _set_LoadFactor,
		"_set_MaxFileName": _set_MaxFileName,
		"_set_RPCFileName": _set_RPCFileName,
		"_set_ScratchFileName": _set_ScratchFileName,
		"_set_ViewModalCoordinates": _set_ViewModalCoordinates,
	}
	_prop_map_get_ = {
		"CreateFEMFATUnitStressScratchFileFlag": (3002, 2, (11, 0), (), "CreateFEMFATUnitStressScratchFileFlag", None),
		"LoadFactor": (3000, 2, (5, 0), (), "LoadFactor", None),
		"MaxFileName": (3005, 2, (8, 0), (), "MaxFileName", None),
		"RPCFileName": (3003, 2, (8, 0), (), "RPCFileName", None),
		"ScratchFileName": (3004, 2, (8, 0), (), "ScratchFileName", None),
		"ViewModalCoordinates": (3001, 2, (8203, 0), (), "ViewModalCoordinates", None),
	}
	_prop_map_put_ = {
		"CreateFEMFATUnitStressScratchFileFlag": ((3002, LCID, 4, 0),()),
		"LoadFactor": ((3000, LCID, 4, 0),()),
		"MaxFileName": ((3005, LCID, 4, 0),()),
		"RPCFileName": ((3003, LCID, 4, 0),()),
		"ScratchFileName": ((3004, LCID, 4, 0),()),
		"ViewModalCoordinates": ((3001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexExportMDFFileOption(DispatchBaseClass):
	'''Export MDF File'''
	CLSID = IID('{C36C3EC0-A03A-40F1-A502-8EB259B56AFB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ExportMDFFileName(self):
		return self._ApplyTypes_(*(3001, 2, (8, 0), (), "ExportMDFFileName", None))
	def _get_SkippedTimeIndexListString(self):
		return self._ApplyTypes_(*(3000, 2, (8, 0), (), "SkippedTimeIndexListString", None))

	def _set_ExportMDFFileName(self, value):
		if "ExportMDFFileName" in self.__dict__: self.__dict__["ExportMDFFileName"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_SkippedTimeIndexListString(self, value):
		if "SkippedTimeIndexListString" in self.__dict__: self.__dict__["SkippedTimeIndexListString"] = value; return
		self._oleobj_.Invoke(*((3000, LCID, 4, 0) + (value,) + ()))

	ExportMDFFileName = property(_get_ExportMDFFileName, _set_ExportMDFFileName)
	'''
	Export MDF File Name

	:type: str
	'''
	SkippedTimeIndexListString = property(_get_SkippedTimeIndexListString, _set_SkippedTimeIndexListString)
	'''
	Skipped Time Index

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ExportMDFFileName": _set_ExportMDFFileName,
		"_set_SkippedTimeIndexListString": _set_SkippedTimeIndexListString,
	}
	_prop_map_get_ = {
		"ExportMDFFileName": (3001, 2, (8, 0), (), "ExportMDFFileName", None),
		"SkippedTimeIndexListString": (3000, 2, (8, 0), (), "SkippedTimeIndexListString", None),
	}
	_prop_map_put_ = {
		"ExportMDFFileName": ((3001, LCID, 4, 0),()),
		"SkippedTimeIndexListString": ((3000, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexForce(DispatchBaseClass):
	CLSID = IID('{7DA762BF-839E-49E6-AB67-2C28067114CE}')
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


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
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
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
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
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
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

class IRFlexForceCollection(DispatchBaseClass):
	'''IRFlexForceCollection'''
	CLSID = IID('{8C387B89-CD63-48E0-B37D-CCF014A3D879}')
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
		:rtype: recurdyn.RFlex.IRFlexForce
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7DA762BF-839E-49E6-AB67-2C28067114CE}')
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
		:rtype: recurdyn.RFlex.IRFlexForce
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7DA762BF-839E-49E6-AB67-2C28067114CE}')
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
		return win32com.client.util.Iterator(ob, '{7DA762BF-839E-49E6-AB67-2C28067114CE}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{7DA762BF-839E-49E6-AB67-2C28067114CE}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexForceModalForce(DispatchBaseClass):
	'''RFlex Modal Force'''
	CLSID = IID('{D4583F05-0EAC-434A-BC8E-C785137C783D}')
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


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(3005, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_ModalForceInfoCollection(self):
		return self._ApplyTypes_(*(3000, 2, (9, 0), (), "ModalForceInfoCollection", '{BED48F30-1BA6-40B0-80C6-ED2650A5E796}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeSet(self):
		return self._ApplyTypes_(*(3003, 2, (9, 0), (), "NodeSet", '{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RFlexBody(self):
		return self._ApplyTypes_(*(3002, 2, (9, 0), (), "RFlexBody", '{5737600D-0E40-4578-9E18-8CBE68916DF8}'))
	def _get_ReportNodeIDs(self):
		return self._ApplyTypes_(*(3007, 2, (8195, 0), (), "ReportNodeIDs", None))
	def _get_USUBType(self):
		return self._ApplyTypes_(*(3004, 2, (3, 0), (), "USUBType", None))
	def _get_UseReportNodes(self):
		return self._ApplyTypes_(*(3006, 2, (11, 0), (), "UseReportNodes", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_UserSubroutine(self):
		return self._ApplyTypes_(*(3001, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NodeSet(self, value):
		if "NodeSet" in self.__dict__: self.__dict__["NodeSet"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_ReportNodeIDs(self, value):
		if "ReportNodeIDs" in self.__dict__: self.__dict__["ReportNodeIDs"] = value; return
		variantValue = win32com.client.VARIANT(8195, value)
		self._oleobj_.Invoke(*((3007, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseReportNodes(self, value):
		if "UseReportNodes" in self.__dict__: self.__dict__["UseReportNodes"] = value; return
		self._oleobj_.Invoke(*((3006, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_UserSubroutine(self, value):
		if "UserSubroutine" in self.__dict__: self.__dict__["UserSubroutine"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseBody = property(_get_BaseBody, _set_BaseBody)
	'''
	BaseBody

	:type: recurdyn.ProcessNet.IBody
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
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	ModalForceInfoCollection = property(_get_ModalForceInfoCollection, None)
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NodeSet = property(_get_NodeSet, _set_NodeSet)
	'''
	Node Set

	:type: recurdyn.RFlex.IRFlexNodeSet
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
	RFlexBody = property(_get_RFlexBody, None)
	'''
	RFlexBody

	:type: recurdyn.RFlex.IRFlexBody
	'''
	ReportNodeIDs = property(_get_ReportNodeIDs, _set_ReportNodeIDs)
	'''
	Report node IDs

	:type: list[int]
	'''
	USUBType = property(_get_USUBType, None)
	'''
	USUBType

	:type: int
	'''
	UseReportNodes = property(_get_UseReportNodes, _set_UseReportNodes)
	'''
	Use report nNodes

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	UserSubroutine = property(_get_UserSubroutine, _set_UserSubroutine)
	'''
	User subroutine

	:type: recurdyn.ProcessNet.IUserSubroutine
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_BaseBody": _set_BaseBody,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_NodeSet": _set_NodeSet,
		"_set_ReportNodeIDs": _set_ReportNodeIDs,
		"_set_UseReportNodes": _set_UseReportNodes,
		"_set_UserData": _set_UserData,
		"_set_UserSubroutine": _set_UserSubroutine,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (3005, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"ModalForceInfoCollection": (3000, 2, (9, 0), (), "ModalForceInfoCollection", '{BED48F30-1BA6-40B0-80C6-ED2650A5E796}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeSet": (3003, 2, (9, 0), (), "NodeSet", '{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RFlexBody": (3002, 2, (9, 0), (), "RFlexBody", '{5737600D-0E40-4578-9E18-8CBE68916DF8}'),
		"ReportNodeIDs": (3007, 2, (8195, 0), (), "ReportNodeIDs", None),
		"USUBType": (3004, 2, (3, 0), (), "USUBType", None),
		"UseReportNodes": (3006, 2, (11, 0), (), "UseReportNodes", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"UserSubroutine": (3001, 2, (9, 0), (), "UserSubroutine", '{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((3005, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NodeSet": ((3003, LCID, 4, 0),()),
		"ReportNodeIDs": ((3007, LCID, 4, 0),()),
		"UseReportNodes": ((3006, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"UserSubroutine": ((3001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexForceModalForceInfo(DispatchBaseClass):
	'''Modal Force Infomation'''
	CLSID = IID('{5A81CC6A-C0E7-4B23-8E27-CD06F1E2CC13}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ModalLoadCase(self):
		return self._ApplyTypes_(*(3000, 2, (9, 0), (), "ModalLoadCase", '{6FB3F9CE-90B7-4111-8714-AA24F53632A6}'))
	def _get_Use(self):
		return self._ApplyTypes_(*(3001, 2, (11, 0), (), "Use", None))

	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))

	ModalLoadCase = property(_get_ModalLoadCase, None)
	'''
	Modal Load Case

	:type: recurdyn.RFlex.IRFlexModalLoadCase
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Use": _set_Use,
	}
	_prop_map_get_ = {
		"ModalLoadCase": (3000, 2, (9, 0), (), "ModalLoadCase", '{6FB3F9CE-90B7-4111-8714-AA24F53632A6}'),
		"Use": (3001, 2, (11, 0), (), "Use", None),
	}
	_prop_map_put_ = {
		"Use": ((3001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexForceModalForceInfoCollection(DispatchBaseClass):
	'''IRFlexForceModalForceInfoCollection'''
	CLSID = IID('{BED48F30-1BA6-40B0-80C6-ED2650A5E796}')
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
		:rtype: recurdyn.RFlex.IRFlexForceModalForceInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5A81CC6A-C0E7-4B23-8E27-CD06F1E2CC13}')
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
		:rtype: recurdyn.RFlex.IRFlexForceModalForceInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5A81CC6A-C0E7-4B23-8E27-CD06F1E2CC13}')
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
		return win32com.client.util.Iterator(ob, '{5A81CC6A-C0E7-4B23-8E27-CD06F1E2CC13}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{5A81CC6A-C0E7-4B23-8E27-CD06F1E2CC13}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexForceModalPreload(DispatchBaseClass):
	'''RFlex Modal Preload'''
	CLSID = IID('{46F35838-9402-4A28-8FE4-00FE959E31DF}')
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


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_ModalPreloadInfoCollection(self):
		return self._ApplyTypes_(*(3000, 2, (9, 0), (), "ModalPreloadInfoCollection", '{05ADCCED-A6D5-4E30-A946-DBA87CAC5F0B}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RFlexBody(self):
		return self._ApplyTypes_(*(3001, 2, (9, 0), (), "RFlexBody", '{5737600D-0E40-4578-9E18-8CBE68916DF8}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
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
	ModalPreloadInfoCollection = property(_get_ModalPreloadInfoCollection, None)
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
	RFlexBody = property(_get_RFlexBody, None)
	'''
	RFlexBody

	:type: recurdyn.RFlex.IRFlexBody
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"ModalPreloadInfoCollection": (3000, 2, (9, 0), (), "ModalPreloadInfoCollection", '{05ADCCED-A6D5-4E30-A946-DBA87CAC5F0B}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RFlexBody": (3001, 2, (9, 0), (), "RFlexBody", '{5737600D-0E40-4578-9E18-8CBE68916DF8}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
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

class IRFlexForceModalPreloadInfo(DispatchBaseClass):
	'''Modal Preload Infomation'''
	CLSID = IID('{EE8ABAE9-396E-46FB-B11F-AD1471097DAF}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ModalLoadCase(self):
		return self._ApplyTypes_(*(3000, 2, (9, 0), (), "ModalLoadCase", '{6FB3F9CE-90B7-4111-8714-AA24F53632A6}'))
	def _get_ScaleFactor(self):
		return self._ApplyTypes_(*(3002, 2, (5, 0), (), "ScaleFactor", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(3001, 2, (11, 0), (), "Use", None))

	def _set_ScaleFactor(self, value):
		if "ScaleFactor" in self.__dict__: self.__dict__["ScaleFactor"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))

	ModalLoadCase = property(_get_ModalLoadCase, None)
	'''
	Modal Load Case

	:type: recurdyn.RFlex.IRFlexModalLoadCase
	'''
	ScaleFactor = property(_get_ScaleFactor, _set_ScaleFactor)
	'''
	Modal Preload Scale Factor

	:type: float
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use Flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ScaleFactor": _set_ScaleFactor,
		"_set_Use": _set_Use,
	}
	_prop_map_get_ = {
		"ModalLoadCase": (3000, 2, (9, 0), (), "ModalLoadCase", '{6FB3F9CE-90B7-4111-8714-AA24F53632A6}'),
		"ScaleFactor": (3002, 2, (5, 0), (), "ScaleFactor", None),
		"Use": (3001, 2, (11, 0), (), "Use", None),
	}
	_prop_map_put_ = {
		"ScaleFactor": ((3002, LCID, 4, 0),()),
		"Use": ((3001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexForceModalPreloadInfoCollection(DispatchBaseClass):
	'''IRFlexForceModalPreloadInfoCollection'''
	CLSID = IID('{05ADCCED-A6D5-4E30-A946-DBA87CAC5F0B}')
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
		:rtype: recurdyn.RFlex.IRFlexForceModalPreloadInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{EE8ABAE9-396E-46FB-B11F-AD1471097DAF}')
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
		:rtype: recurdyn.RFlex.IRFlexForceModalPreloadInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{EE8ABAE9-396E-46FB-B11F-AD1471097DAF}')
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
		return win32com.client.util.Iterator(ob, '{EE8ABAE9-396E-46FB-B11F-AD1471097DAF}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{EE8ABAE9-396E-46FB-B11F-AD1471097DAF}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexGroupBeam(DispatchBaseClass):
	'''Beam force'''
	CLSID = IID('{3C055C79-373C-4034-A146-E1E5D485D36E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def DampingMatrix(self, i, j):
		'''
		Damping matrix
		
		:param i: int
		:param j: int
		:rtype: recurdyn.ProcessNet.IDouble
		'''
		ret = self._oleobj_.InvokeTypes(3002, LCID, 1, (9, 0), ((3, 1), (3, 1)),i
			, j)
		if ret is not None:
			ret = Dispatch(ret, 'DampingMatrix', '{2B5166E3-4B31-4607-B157-BE237A670336}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def UpdateBodyProperty(self):
		'''
		Update the Body properties of the beam group
		'''
		return self._oleobj_.InvokeTypes(3021, LCID, 1, (24, 0), (),)


	def UpdateCrossSectionProperty(self):
		'''
		Update mass, moment of inertia
		'''
		return self._oleobj_.InvokeTypes(3024, LCID, 1, (24, 0), (),)


	def UpdateForceProperty(self):
		'''
		Update the force properties of the beam group
		'''
		return self._oleobj_.InvokeTypes(3020, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BeamCrossSection(self):
		return self._ApplyTypes_(*(3023, 2, (9, 0), (), "BeamCrossSection", '{557175E7-72DD-447A-8DB1-319593C34BDC}'))
	def _get_BeamCrossSectionType(self):
		return self._ApplyTypes_(*(3022, 2, (3, 0), (), "BeamCrossSectionType", '{01406737-1007-468F-A0BC-A2F7C43239CF}'))
	def _get_Color(self):
		return self._ApplyTypes_(*(3014, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_CrossSectionArea(self):
		return self._ApplyTypes_(*(3001, 2, (9, 0), (), "CrossSectionArea", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Density(self):
		return self._ApplyTypes_(*(3016, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(3013, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_InertiaPropertyInput(self):
		return self._ApplyTypes_(*(3018, 2, (3, 0), (), "InertiaPropertyInput", '{F752AB94-C4F5-49AE-B368-095E39D47E86}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(3004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(3005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(3006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LayerNumber(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "LayerNumber", None))
	def _get_MeshSegmentNumber(self):
		return self._ApplyTypes_(*(3019, 2, (19, 0), (), "MeshSegmentNumber", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeThickness(self):
		return self._ApplyTypes_(*(3010, 2, (9, 0), (), "NodeThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ShearAreaRatioY(self):
		return self._ApplyTypes_(*(3025, 2, (9, 0), (), "ShearAreaRatioY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearAreaRatioZ(self):
		return self._ApplyTypes_(*(3026, 2, (9, 0), (), "ShearAreaRatioZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearAreaRationY(self):
		return self._ApplyTypes_(*(3007, 2, (9, 0), (), "ShearAreaRationY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearAreaRationZ(self):
		return self._ApplyTypes_(*(3008, 2, (9, 0), (), "ShearAreaRationZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_ShearModulus(self):
		return self._ApplyTypes_(*(3009, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(3015, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseDampingMatrix(self):
		return self._ApplyTypes_(*(3012, 2, (11, 0), (), "UseDampingMatrix", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_ViscousDampingRatio(self):
		return self._ApplyTypes_(*(3003, 2, (9, 0), (), "ViscousDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_YoungsModulus(self):
		return self._ApplyTypes_(*(3011, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BeamCrossSectionType(self, value):
		if "BeamCrossSectionType" in self.__dict__: self.__dict__["BeamCrossSectionType"] = value; return
		self._oleobj_.Invoke(*((3022, LCID, 4, 0) + (value,) + ()))
	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((3014, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_EachRenderMode(self, value):
		if "EachRenderMode" in self.__dict__: self.__dict__["EachRenderMode"] = value; return
		self._oleobj_.Invoke(*((3013, LCID, 4, 0) + (value,) + ()))
	def _set_InertiaPropertyInput(self, value):
		if "InertiaPropertyInput" in self.__dict__: self.__dict__["InertiaPropertyInput"] = value; return
		self._oleobj_.Invoke(*((3018, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_SolveLargeDOFBeam(self, value):
		if "SolveLargeDOFBeam" in self.__dict__: self.__dict__["SolveLargeDOFBeam"] = value; return
		self._oleobj_.Invoke(*((3017, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingMatrix(self, value):
		if "UseDampingMatrix" in self.__dict__: self.__dict__["UseDampingMatrix"] = value; return
		self._oleobj_.Invoke(*((3012, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BeamCrossSection = property(_get_BeamCrossSection, None)
	'''
	BeamForce cross section

	:type: recurdyn.ProcessNet.IBeamCrossSection
	'''
	BeamCrossSectionType = property(_get_BeamCrossSectionType, _set_BeamCrossSectionType)
	'''
	BeamForce cross section type

	:type: recurdyn.ProcessNet.BeamCrossSectionType
	'''
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
	CrossSectionArea = property(_get_CrossSectionArea, None)
	'''
	Beam library calculate automatically mass and area moment of inertia which is determined by cross section area.

	:type: recurdyn.ProcessNet.IDouble
	'''
	Density = property(_get_Density, None)
	'''
	Density

	:type: recurdyn.ProcessNet.IDouble
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
	InertiaPropertyInput = property(_get_InertiaPropertyInput, _set_InertiaPropertyInput)
	'''
	Material Input Type

	:type: recurdyn.RFlex.BeamGroupInertiaPropertyInput
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	LayerNumber = property(_get_LayerNumber, _set_LayerNumber)
	'''
	Layer number

	:type: int
	'''
	MeshSegmentNumber = property(_get_MeshSegmentNumber, None)
	'''
	The number of mesh segments

	:type: int
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NodeThickness = property(_get_NodeThickness, None)
	'''
	Node thickness

	:type: recurdyn.ProcessNet.IDouble
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
	ShearAreaRatioY = property(_get_ShearAreaRatioY, None)
	'''
	Shear area ratio Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearAreaRatioZ = property(_get_ShearAreaRatioZ, None)
	'''
	Shear area ratio Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearAreaRationY = property(_get_ShearAreaRationY, None)
	'''
	ShearAreaRationY is obsolete function

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearAreaRationZ = property(_get_ShearAreaRationZ, None)
	'''
	ShearAreaRationZ is obsolete function

	:type: recurdyn.ProcessNet.IDouble
	'''
	ShearModulus = property(_get_ShearModulus, None)
	'''
	Shear modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	TotalMass = property(_get_TotalMass, None)
	'''
	Total Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseDampingMatrix = property(_get_UseDampingMatrix, _set_UseDampingMatrix)
	'''
	Use damping matrix

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	ViscousDampingRatio = property(_get_ViscousDampingRatio, None)
	'''
	Viscous damping ratio

	:type: recurdyn.ProcessNet.IDouble
	'''
	YoungsModulus = property(_get_YoungsModulus, None)
	'''
	Young's modulus

	:type: recurdyn.ProcessNet.IDouble
	'''
	SolveLargeDOFBeam = property(None, _set_SolveLargeDOFBeam)
	'''
	Solve the large D.O.F beam

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_BeamCrossSectionType": _set_BeamCrossSectionType,
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_EachRenderMode": _set_EachRenderMode,
		"_set_InertiaPropertyInput": _set_InertiaPropertyInput,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_SolveLargeDOFBeam": _set_SolveLargeDOFBeam,
		"_set_UseDampingMatrix": _set_UseDampingMatrix,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BeamCrossSection": (3023, 2, (9, 0), (), "BeamCrossSection", '{557175E7-72DD-447A-8DB1-319593C34BDC}'),
		"BeamCrossSectionType": (3022, 2, (3, 0), (), "BeamCrossSectionType", '{01406737-1007-468F-A0BC-A2F7C43239CF}'),
		"Color": (3014, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"CrossSectionArea": (3001, 2, (9, 0), (), "CrossSectionArea", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Density": (3016, 2, (9, 0), (), "Density", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"EachRenderMode": (3013, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"InertiaPropertyInput": (3018, 2, (3, 0), (), "InertiaPropertyInput", '{F752AB94-C4F5-49AE-B368-095E39D47E86}'),
		"Ixx": (3004, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (3005, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (3006, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"MeshSegmentNumber": (3019, 2, (19, 0), (), "MeshSegmentNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeThickness": (3010, 2, (9, 0), (), "NodeThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ShearAreaRatioY": (3025, 2, (9, 0), (), "ShearAreaRatioY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearAreaRatioZ": (3026, 2, (9, 0), (), "ShearAreaRatioZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearAreaRationY": (3007, 2, (9, 0), (), "ShearAreaRationY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearAreaRationZ": (3008, 2, (9, 0), (), "ShearAreaRationZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"ShearModulus": (3009, 2, (9, 0), (), "ShearModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TotalMass": (3015, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseDampingMatrix": (3012, 2, (11, 0), (), "UseDampingMatrix", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"ViscousDampingRatio": (3003, 2, (9, 0), (), "ViscousDampingRatio", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"YoungsModulus": (3011, 2, (9, 0), (), "YoungsModulus", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BeamCrossSectionType": ((3022, LCID, 4, 0),()),
		"Color": ((3014, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((3013, LCID, 4, 0),()),
		"InertiaPropertyInput": ((3018, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"SolveLargeDOFBeam": ((3017, LCID, 4, 0),()),
		"UseDampingMatrix": ((3012, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexInterfaceANSYSOption(DispatchBaseClass):
	'''ANSYS specific option used in creating RFI file'''
	CLSID = IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C73}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_CMFileName(self):
		return self._ApplyTypes_(*(3003, 2, (8, 0), (), "CMFileName", None))
	def _get_DataPrecisionofStressStrainShape(self):
		return self._ApplyTypes_(*(3004, 2, (3, 0), (), "DataPrecisionofStressStrainShape", '{A353EE4A-BA4D-4F66-9D7C-355863AA890E}'))
	def _get_ElementMatricesFileName(self):
		return self._ApplyTypes_(*(3002, 2, (8, 0), (), "ElementMatricesFileName", None))
	def _get_MaterialFileName(self):
		return self._ApplyTypes_(*(3001, 2, (8, 0), (), "MaterialFileName", None))
	def _get_ResultFileName(self):
		return self._ApplyTypes_(*(3000, 2, (8, 0), (), "ResultFileName", None))
	def _get_ShellRecoveryType(self):
		return self._ApplyTypes_(*(3007, 2, (3, 0), (), "ShellRecoveryType", '{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}'))
	def _get_StrainShapeFlag(self):
		return self._ApplyTypes_(*(3006, 2, (11, 0), (), "StrainShapeFlag", None))
	def _get_StressShapeFlag(self):
		return self._ApplyTypes_(*(3005, 2, (11, 0), (), "StressShapeFlag", None))

	def _set_CMFileName(self, value):
		if "CMFileName" in self.__dict__: self.__dict__["CMFileName"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_DataPrecisionofStressStrainShape(self, value):
		if "DataPrecisionofStressStrainShape" in self.__dict__: self.__dict__["DataPrecisionofStressStrainShape"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_ElementMatricesFileName(self, value):
		if "ElementMatricesFileName" in self.__dict__: self.__dict__["ElementMatricesFileName"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialFileName(self, value):
		if "MaterialFileName" in self.__dict__: self.__dict__["MaterialFileName"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_ResultFileName(self, value):
		if "ResultFileName" in self.__dict__: self.__dict__["ResultFileName"] = value; return
		self._oleobj_.Invoke(*((3000, LCID, 4, 0) + (value,) + ()))
	def _set_ShellRecoveryType(self, value):
		if "ShellRecoveryType" in self.__dict__: self.__dict__["ShellRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3007, LCID, 4, 0) + (value,) + ()))
	def _set_StrainShapeFlag(self, value):
		if "StrainShapeFlag" in self.__dict__: self.__dict__["StrainShapeFlag"] = value; return
		self._oleobj_.Invoke(*((3006, LCID, 4, 0) + (value,) + ()))
	def _set_StressShapeFlag(self, value):
		if "StressShapeFlag" in self.__dict__: self.__dict__["StressShapeFlag"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))

	CMFileName = property(_get_CMFileName, _set_CMFileName)
	'''
	CM file (*.cm) contains interface node information

	:type: str
	'''
	DataPrecisionofStressStrainShape = property(_get_DataPrecisionofStressStrainShape, _set_DataPrecisionofStressStrainShape)
	'''
	Data Precision of Stress/Strain Shape

	:type: recurdyn.RFlex.DataPrecisionofStressStrainShapeType
	'''
	ElementMatricesFileName = property(_get_ElementMatricesFileName, _set_ElementMatricesFileName)
	'''
	Element matrices file (*.emat) contains element matrices information such as element stiffness and mass matrices.

	:type: str
	'''
	MaterialFileName = property(_get_MaterialFileName, _set_MaterialFileName)
	'''
	Material file (*.mp) contains material information such as Young's modulus, shear modulus and Poisson's ratio.

	:type: str
	'''
	ResultFileName = property(_get_ResultFileName, _set_ResultFileName)
	'''
	Result file (*.rst) contains model information such as node, element, property and the result of CMS or Modal analysis.

	:type: str
	'''
	ShellRecoveryType = property(_get_ShellRecoveryType, _set_ShellRecoveryType)
	'''
	Shell Recovery Type

	:type: recurdyn.RFlex.ShellRecoveryType
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

	_prop_map_set_function_ = {
		"_set_CMFileName": _set_CMFileName,
		"_set_DataPrecisionofStressStrainShape": _set_DataPrecisionofStressStrainShape,
		"_set_ElementMatricesFileName": _set_ElementMatricesFileName,
		"_set_MaterialFileName": _set_MaterialFileName,
		"_set_ResultFileName": _set_ResultFileName,
		"_set_ShellRecoveryType": _set_ShellRecoveryType,
		"_set_StrainShapeFlag": _set_StrainShapeFlag,
		"_set_StressShapeFlag": _set_StressShapeFlag,
	}
	_prop_map_get_ = {
		"CMFileName": (3003, 2, (8, 0), (), "CMFileName", None),
		"DataPrecisionofStressStrainShape": (3004, 2, (3, 0), (), "DataPrecisionofStressStrainShape", '{A353EE4A-BA4D-4F66-9D7C-355863AA890E}'),
		"ElementMatricesFileName": (3002, 2, (8, 0), (), "ElementMatricesFileName", None),
		"MaterialFileName": (3001, 2, (8, 0), (), "MaterialFileName", None),
		"ResultFileName": (3000, 2, (8, 0), (), "ResultFileName", None),
		"ShellRecoveryType": (3007, 2, (3, 0), (), "ShellRecoveryType", '{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}'),
		"StrainShapeFlag": (3006, 2, (11, 0), (), "StrainShapeFlag", None),
		"StressShapeFlag": (3005, 2, (11, 0), (), "StressShapeFlag", None),
	}
	_prop_map_put_ = {
		"CMFileName": ((3003, LCID, 4, 0),()),
		"DataPrecisionofStressStrainShape": ((3004, LCID, 4, 0),()),
		"ElementMatricesFileName": ((3002, LCID, 4, 0),()),
		"MaterialFileName": ((3001, LCID, 4, 0),()),
		"ResultFileName": ((3000, LCID, 4, 0),()),
		"ShellRecoveryType": ((3007, LCID, 4, 0),()),
		"StrainShapeFlag": ((3006, LCID, 4, 0),()),
		"StressShapeFlag": ((3005, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexInterfaceCommonOption(DispatchBaseClass):
	'''Common option used in creating RFI file'''
	CLSID = IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_LowerBoundFrequency(self):
		return self._ApplyTypes_(*(3004, 2, (5, 0), (), "LowerBoundFrequency", None))
	def _get_NumberOfMode(self):
		return self._ApplyTypes_(*(3003, 2, (5, 0), (), "NumberOfMode", None))
	def _get_RemoveMidNodeFlag(self):
		return self._ApplyTypes_(*(3008, 2, (11, 0), (), "RemoveMidNodeFlag", None))
	def _get_RemoveZeroValueFlag(self):
		return self._ApplyTypes_(*(3007, 2, (11, 0), (), "RemoveZeroValueFlag", None))
	def _get_UpperBoundFrequency(self):
		return self._ApplyTypes_(*(3005, 2, (5, 0), (), "UpperBoundFrequency", None))
	def _get_UseInternalNodes(self):
		return self._ApplyTypes_(*(3001, 2, (11, 0), (), "UseInternalNodes", None))
	def _get_UseNumberOfMode(self):
		return self._ApplyTypes_(*(3002, 2, (11, 0), (), "UseNumberOfMode", None))
	def _get_UseStiffnessMatrix(self):
		return self._ApplyTypes_(*(3000, 2, (11, 0), (), "UseStiffnessMatrix", None))
	def _get_UseUnitForce(self):
		return self._ApplyTypes_(*(3006, 2, (11, 0), (), "UseUnitForce", None))

	def _set_LowerBoundFrequency(self, value):
		if "LowerBoundFrequency" in self.__dict__: self.__dict__["LowerBoundFrequency"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_NumberOfMode(self, value):
		if "NumberOfMode" in self.__dict__: self.__dict__["NumberOfMode"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_RemoveMidNodeFlag(self, value):
		if "RemoveMidNodeFlag" in self.__dict__: self.__dict__["RemoveMidNodeFlag"] = value; return
		self._oleobj_.Invoke(*((3008, LCID, 4, 0) + (value,) + ()))
	def _set_RemoveZeroValueFlag(self, value):
		if "RemoveZeroValueFlag" in self.__dict__: self.__dict__["RemoveZeroValueFlag"] = value; return
		self._oleobj_.Invoke(*((3007, LCID, 4, 0) + (value,) + ()))
	def _set_UpperBoundFrequency(self, value):
		if "UpperBoundFrequency" in self.__dict__: self.__dict__["UpperBoundFrequency"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))
	def _set_UseInternalNodes(self, value):
		if "UseInternalNodes" in self.__dict__: self.__dict__["UseInternalNodes"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_UseNumberOfMode(self, value):
		if "UseNumberOfMode" in self.__dict__: self.__dict__["UseNumberOfMode"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessMatrix(self, value):
		if "UseStiffnessMatrix" in self.__dict__: self.__dict__["UseStiffnessMatrix"] = value; return
		self._oleobj_.Invoke(*((3000, LCID, 4, 0) + (value,) + ()))
	def _set_UseUnitForce(self, value):
		if "UseUnitForce" in self.__dict__: self.__dict__["UseUnitForce"] = value; return
		self._oleobj_.Invoke(*((3006, LCID, 4, 0) + (value,) + ()))

	LowerBoundFrequency = property(_get_LowerBoundFrequency, _set_LowerBoundFrequency)
	'''
	Lower bound frequency (default 0.0).

	:type: float
	'''
	NumberOfMode = property(_get_NumberOfMode, _set_NumberOfMode)
	'''
	Number of mode to be included in RFI file, set 0 for ALL mode.

	:type: float
	'''
	RemoveMidNodeFlag = property(_get_RemoveMidNodeFlag, _set_RemoveMidNodeFlag)
	'''
	Remove Mid-Node Related Information Flag (default TRUE)

	:type: bool
	'''
	RemoveZeroValueFlag = property(_get_RemoveZeroValueFlag, _set_RemoveZeroValueFlag)
	'''
	Remove Zero-Value for Rotational Mode Shape Flag (default TRUE)

	:type: bool
	'''
	UpperBoundFrequency = property(_get_UpperBoundFrequency, _set_UpperBoundFrequency)
	'''
	Upper bound frequency (default 1e+011).

	:type: float
	'''
	UseInternalNodes = property(_get_UseInternalNodes, _set_UseInternalNodes)
	'''
	UseInternalNodes is obsolete function

	:type: bool
	'''
	UseNumberOfMode = property(_get_UseNumberOfMode, _set_UseNumberOfMode)
	'''
	Use number of mode (default False).

	:type: bool
	'''
	UseStiffnessMatrix = property(_get_UseStiffnessMatrix, _set_UseStiffnessMatrix)
	'''
	Checking this option enables Static and Dynamic Correction Mode to be generated and User-defined Correction Mode to be attached. If these correction modes are not used, it is not necessary to include the stiffness matrix.

	:type: bool
	'''
	UseUnitForce = property(_get_UseUnitForce, _set_UseUnitForce)
	'''
	UseUnitForce is obsolete function

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_LowerBoundFrequency": _set_LowerBoundFrequency,
		"_set_NumberOfMode": _set_NumberOfMode,
		"_set_RemoveMidNodeFlag": _set_RemoveMidNodeFlag,
		"_set_RemoveZeroValueFlag": _set_RemoveZeroValueFlag,
		"_set_UpperBoundFrequency": _set_UpperBoundFrequency,
		"_set_UseInternalNodes": _set_UseInternalNodes,
		"_set_UseNumberOfMode": _set_UseNumberOfMode,
		"_set_UseStiffnessMatrix": _set_UseStiffnessMatrix,
		"_set_UseUnitForce": _set_UseUnitForce,
	}
	_prop_map_get_ = {
		"LowerBoundFrequency": (3004, 2, (5, 0), (), "LowerBoundFrequency", None),
		"NumberOfMode": (3003, 2, (5, 0), (), "NumberOfMode", None),
		"RemoveMidNodeFlag": (3008, 2, (11, 0), (), "RemoveMidNodeFlag", None),
		"RemoveZeroValueFlag": (3007, 2, (11, 0), (), "RemoveZeroValueFlag", None),
		"UpperBoundFrequency": (3005, 2, (5, 0), (), "UpperBoundFrequency", None),
		"UseInternalNodes": (3001, 2, (11, 0), (), "UseInternalNodes", None),
		"UseNumberOfMode": (3002, 2, (11, 0), (), "UseNumberOfMode", None),
		"UseStiffnessMatrix": (3000, 2, (11, 0), (), "UseStiffnessMatrix", None),
		"UseUnitForce": (3006, 2, (11, 0), (), "UseUnitForce", None),
	}
	_prop_map_put_ = {
		"LowerBoundFrequency": ((3004, LCID, 4, 0),()),
		"NumberOfMode": ((3003, LCID, 4, 0),()),
		"RemoveMidNodeFlag": ((3008, LCID, 4, 0),()),
		"RemoveZeroValueFlag": ((3007, LCID, 4, 0),()),
		"UpperBoundFrequency": ((3005, LCID, 4, 0),()),
		"UseInternalNodes": ((3001, LCID, 4, 0),()),
		"UseNumberOfMode": ((3002, LCID, 4, 0),()),
		"UseStiffnessMatrix": ((3000, LCID, 4, 0),()),
		"UseUnitForce": ((3006, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexInterfaceExtraModeOption(DispatchBaseClass):
	'''Extra mode option used in creating RFI file'''
	CLSID = IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C76}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ExtraModeInputFileList(self):
		return self._ApplyTypes_(*(3000, 2, (8200, 0), (), "ExtraModeInputFileList", None))
	def _get_LowerBoundFrequency(self):
		return self._ApplyTypes_(*(3001, 2, (5, 0), (), "LowerBoundFrequency", None))
	def _get_UpperBoundFrequency(self):
		return self._ApplyTypes_(*(3002, 2, (5, 0), (), "UpperBoundFrequency", None))

	def _set_ExtraModeInputFileList(self, value):
		if "ExtraModeInputFileList" in self.__dict__: self.__dict__["ExtraModeInputFileList"] = value; return
		variantValue = win32com.client.VARIANT(8200, value)
		self._oleobj_.Invoke(*((3000, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LowerBoundFrequency(self, value):
		if "LowerBoundFrequency" in self.__dict__: self.__dict__["LowerBoundFrequency"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_UpperBoundFrequency(self, value):
		if "UpperBoundFrequency" in self.__dict__: self.__dict__["UpperBoundFrequency"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))

	ExtraModeInputFileList = property(_get_ExtraModeInputFileList, _set_ExtraModeInputFileList)
	'''
	This file must contain static deformation modes resulted from FE software. RecurDyn/RFlex attaches these modes to RFI file through orthonomalization process.

	:type: list[str]
	'''
	LowerBoundFrequency = property(_get_LowerBoundFrequency, _set_LowerBoundFrequency)
	'''
	Lower bound frequency (default 0.0).

	:type: float
	'''
	UpperBoundFrequency = property(_get_UpperBoundFrequency, _set_UpperBoundFrequency)
	'''
	Upper bound frequency (default 1e+011).

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_ExtraModeInputFileList": _set_ExtraModeInputFileList,
		"_set_LowerBoundFrequency": _set_LowerBoundFrequency,
		"_set_UpperBoundFrequency": _set_UpperBoundFrequency,
	}
	_prop_map_get_ = {
		"ExtraModeInputFileList": (3000, 2, (8200, 0), (), "ExtraModeInputFileList", None),
		"LowerBoundFrequency": (3001, 2, (5, 0), (), "LowerBoundFrequency", None),
		"UpperBoundFrequency": (3002, 2, (5, 0), (), "UpperBoundFrequency", None),
	}
	_prop_map_put_ = {
		"ExtraModeInputFileList": ((3000, LCID, 4, 0),()),
		"LowerBoundFrequency": ((3001, LCID, 4, 0),()),
		"UpperBoundFrequency": ((3002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexInterfaceIdeasOption(DispatchBaseClass):
	'''Ideas specific option used in creating RFI file'''
	CLSID = IID('{6DB248B8-8ACE-49F0-9B06-5065FB9AE8B0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_UseElementSet(self):
		return self._ApplyTypes_(*(3000, 2, (11, 0), (), "UseElementSet", None))
	def _get_UseNodeSet(self):
		return self._ApplyTypes_(*(3001, 2, (11, 0), (), "UseNodeSet", None))

	def _set_UseElementSet(self, value):
		if "UseElementSet" in self.__dict__: self.__dict__["UseElementSet"] = value; return
		self._oleobj_.Invoke(*((3000, LCID, 4, 0) + (value,) + ()))
	def _set_UseNodeSet(self, value):
		if "UseNodeSet" in self.__dict__: self.__dict__["UseNodeSet"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))

	UseElementSet = property(_get_UseElementSet, _set_UseElementSet)
	'''
	Element Set

	:type: bool
	'''
	UseNodeSet = property(_get_UseNodeSet, _set_UseNodeSet)
	'''
	Node Set

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_UseElementSet": _set_UseElementSet,
		"_set_UseNodeSet": _set_UseNodeSet,
	}
	_prop_map_get_ = {
		"UseElementSet": (3000, 2, (11, 0), (), "UseElementSet", None),
		"UseNodeSet": (3001, 2, (11, 0), (), "UseNodeSet", None),
	}
	_prop_map_put_ = {
		"UseElementSet": ((3000, LCID, 4, 0),()),
		"UseNodeSet": ((3001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexInterfaceNastranOP2Option(DispatchBaseClass):
	'''Nastran OP2 specific option used in creating RFI file'''
	CLSID = IID('{3D4D50F5-2D1A-4618-B956-072A3EA9DD8A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DataPrecisionofStressStrainShape(self):
		return self._ApplyTypes_(*(3000, 2, (3, 0), (), "DataPrecisionofStressStrainShape", '{A353EE4A-BA4D-4F66-9D7C-355863AA890E}'))
	def _get_ShellRecoveryType(self):
		return self._ApplyTypes_(*(3003, 2, (3, 0), (), "ShellRecoveryType", '{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}'))
	def _get_StrainShapeFlag(self):
		return self._ApplyTypes_(*(3002, 2, (11, 0), (), "StrainShapeFlag", None))
	def _get_StressShapeFlag(self):
		return self._ApplyTypes_(*(3001, 2, (11, 0), (), "StressShapeFlag", None))

	def _set_DataPrecisionofStressStrainShape(self, value):
		if "DataPrecisionofStressStrainShape" in self.__dict__: self.__dict__["DataPrecisionofStressStrainShape"] = value; return
		self._oleobj_.Invoke(*((3000, LCID, 4, 0) + (value,) + ()))
	def _set_ShellRecoveryType(self, value):
		if "ShellRecoveryType" in self.__dict__: self.__dict__["ShellRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_StrainShapeFlag(self, value):
		if "StrainShapeFlag" in self.__dict__: self.__dict__["StrainShapeFlag"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_StressShapeFlag(self, value):
		if "StressShapeFlag" in self.__dict__: self.__dict__["StressShapeFlag"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))

	DataPrecisionofStressStrainShape = property(_get_DataPrecisionofStressStrainShape, _set_DataPrecisionofStressStrainShape)
	'''
	Data Precision of Stress/Strain Shape

	:type: recurdyn.RFlex.DataPrecisionofStressStrainShapeType
	'''
	ShellRecoveryType = property(_get_ShellRecoveryType, _set_ShellRecoveryType)
	'''
	Shell Recovery Type

	:type: recurdyn.RFlex.ShellRecoveryType
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

	_prop_map_set_function_ = {
		"_set_DataPrecisionofStressStrainShape": _set_DataPrecisionofStressStrainShape,
		"_set_ShellRecoveryType": _set_ShellRecoveryType,
		"_set_StrainShapeFlag": _set_StrainShapeFlag,
		"_set_StressShapeFlag": _set_StressShapeFlag,
	}
	_prop_map_get_ = {
		"DataPrecisionofStressStrainShape": (3000, 2, (3, 0), (), "DataPrecisionofStressStrainShape", '{A353EE4A-BA4D-4F66-9D7C-355863AA890E}'),
		"ShellRecoveryType": (3003, 2, (3, 0), (), "ShellRecoveryType", '{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}'),
		"StrainShapeFlag": (3002, 2, (11, 0), (), "StrainShapeFlag", None),
		"StressShapeFlag": (3001, 2, (11, 0), (), "StressShapeFlag", None),
	}
	_prop_map_put_ = {
		"DataPrecisionofStressStrainShape": ((3000, LCID, 4, 0),()),
		"ShellRecoveryType": ((3003, LCID, 4, 0),()),
		"StrainShapeFlag": ((3002, LCID, 4, 0),()),
		"StressShapeFlag": ((3001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexLineSet(DispatchBaseClass):
	CLSID = IID('{7C9E9609-3A15-4847-8B60-6AE1460A7A58}')
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
		return self._ApplyTypes_(*(3053, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeCollection(self):
		return self._ApplyTypes_(*(3052, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'))
	def _get_NodeIDs(self):
		return self._ApplyTypes_(*(3051, 2, (8195, 0), (), "NodeIDs", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((3053, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Line set color

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
	NodeCollection = property(_get_NodeCollection, None)
	'''
	Node Collection

	:type: recurdyn.RFlex.IRFlexNodeCollection
	'''
	NodeIDs = property(_get_NodeIDs, None)
	'''
	Contains Node

	:type: list[int]
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
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Color": (3053, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeCollection": (3052, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'),
		"NodeIDs": (3051, 2, (8195, 0), (), "NodeIDs", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Color": ((3053, LCID, 4, 0),()),
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

class IRFlexLineSetCollection(DispatchBaseClass):
	'''IRFlexLineSetCollection'''
	CLSID = IID('{05938874-D404-42C9-9757-863978D57DE5}')
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
		:rtype: recurdyn.RFlex.IRFlexLineSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7C9E9609-3A15-4847-8B60-6AE1460A7A58}')
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
		:rtype: recurdyn.RFlex.IRFlexLineSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7C9E9609-3A15-4847-8B60-6AE1460A7A58}')
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
		return win32com.client.util.Iterator(ob, '{7C9E9609-3A15-4847-8B60-6AE1460A7A58}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{7C9E9609-3A15-4847-8B60-6AE1460A7A58}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexLoad(DispatchBaseClass):
	CLSID = IID('{BA0F8202-4689-40C2-B583-9A907276C7D1}')
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


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
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
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
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
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
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

class IRFlexLoadPressureModal(DispatchBaseClass):
	CLSID = IID('{FB11F962-2D23-4DD7-A6DF-0C47507310E0}')
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


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseBody(self):
		return self._ApplyTypes_(*(3004, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
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
	def _get_PatchSet(self):
		return self._ApplyTypes_(*(3001, 2, (9, 0), (), "PatchSet", '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}'))
	def _get_Pressure(self):
		return self._ApplyTypes_(*(3003, 2, (9, 0), (), "Pressure", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_PressureUpDirction(self):
		return self._ApplyTypes_(*(3002, 2, (11, 0), (), "PressureUpDirction", None))
	def _get_ReportNodeIDs(self):
		return self._ApplyTypes_(*(3006, 2, (8195, 0), (), "ReportNodeIDs", None))
	def _get_StepSizeCriteria(self):
		return self._ApplyTypes_(*(3008, 2, (9, 0), (), "StepSizeCriteria", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseConvergedResult(self):
		return self._ApplyTypes_(*(3007, 2, (11, 0), (), "UseConvergedResult", None))
	def _get_UseReportNodes(self):
		return self._ApplyTypes_(*(3005, 2, (11, 0), (), "UseReportNodes", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseBody(self, value):
		if "BaseBody" in self.__dict__: self.__dict__["BaseBody"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_PatchSet(self, value):
		if "PatchSet" in self.__dict__: self.__dict__["PatchSet"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_Pressure(self, value):
		if "Pressure" in self.__dict__: self.__dict__["Pressure"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_PressureUpDirction(self, value):
		if "PressureUpDirction" in self.__dict__: self.__dict__["PressureUpDirction"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_ReportNodeIDs(self, value):
		if "ReportNodeIDs" in self.__dict__: self.__dict__["ReportNodeIDs"] = value; return
		variantValue = win32com.client.VARIANT(8195, value)
		self._oleobj_.Invoke(*((3006, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseConvergedResult(self, value):
		if "UseConvergedResult" in self.__dict__: self.__dict__["UseConvergedResult"] = value; return
		self._oleobj_.Invoke(*((3007, LCID, 4, 0) + (value,) + ()))
	def _set_UseReportNodes(self, value):
		if "UseReportNodes" in self.__dict__: self.__dict__["UseReportNodes"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Active = property(_get_Active, _set_Active)
	'''
	Active

	:type: bool
	'''
	BaseBody = property(_get_BaseBody, _set_BaseBody)
	'''
	Base Body

	:type: recurdyn.ProcessNet.IBody
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
	PatchSet = property(_get_PatchSet, _set_PatchSet)
	'''
	Patch set

	:type: recurdyn.RFlex.IRFlexPatchSet
	'''
	Pressure = property(_get_Pressure, _set_Pressure)
	'''
	Pressure

	:type: recurdyn.ProcessNet.IExpression
	'''
	PressureUpDirction = property(_get_PressureUpDirction, _set_PressureUpDirction)
	'''
	Pressure up dirction

	:type: bool
	'''
	ReportNodeIDs = property(_get_ReportNodeIDs, _set_ReportNodeIDs)
	'''
	Report node IDs

	:type: list[int]
	'''
	StepSizeCriteria = property(_get_StepSizeCriteria, None)
	'''
	Step size criteria

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseConvergedResult = property(_get_UseConvergedResult, _set_UseConvergedResult)
	'''
	Use converged result

	:type: bool
	'''
	UseReportNodes = property(_get_UseReportNodes, _set_UseReportNodes)
	'''
	Use report nNodes

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_BaseBody": _set_BaseBody,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_PatchSet": _set_PatchSet,
		"_set_Pressure": _set_Pressure,
		"_set_PressureUpDirction": _set_PressureUpDirction,
		"_set_ReportNodeIDs": _set_ReportNodeIDs,
		"_set_UseConvergedResult": _set_UseConvergedResult,
		"_set_UseReportNodes": _set_UseReportNodes,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseBody": (3004, 2, (9, 0), (), "BaseBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PatchSet": (3001, 2, (9, 0), (), "PatchSet", '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}'),
		"Pressure": (3003, 2, (9, 0), (), "Pressure", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"PressureUpDirction": (3002, 2, (11, 0), (), "PressureUpDirction", None),
		"ReportNodeIDs": (3006, 2, (8195, 0), (), "ReportNodeIDs", None),
		"StepSizeCriteria": (3008, 2, (9, 0), (), "StepSizeCriteria", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseConvergedResult": (3007, 2, (11, 0), (), "UseConvergedResult", None),
		"UseReportNodes": (3005, 2, (11, 0), (), "UseReportNodes", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"BaseBody": ((3004, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"PatchSet": ((3001, LCID, 4, 0),()),
		"Pressure": ((3003, LCID, 4, 0),()),
		"PressureUpDirction": ((3002, LCID, 4, 0),()),
		"ReportNodeIDs": ((3006, LCID, 4, 0),()),
		"UseConvergedResult": ((3007, LCID, 4, 0),()),
		"UseReportNodes": ((3005, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexModalLoadCase(DispatchBaseClass):
	'''Modal Load Case '''
	CLSID = IID('{6FB3F9CE-90B7-4111-8714-AA24F53632A6}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ID(self):
		return self._ApplyTypes_(*(3000, 2, (19, 0), (), "ID", None))
	def _get_ModalLoadValue(self):
		return self._ApplyTypes_(*(3005, 2, (9, 0), (), "ModalLoadValue", '{DC95F017-DABD-4F7B-8E19-D6DC880124BF}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(3001, 2, (8, 0), (), "Name", None))
	def _get_NodalLoadValueCollection(self):
		return self._ApplyTypes_(*(3004, 2, (9, 0), (), "NodalLoadValueCollection", '{8AEC2258-C39F-452F-BA67-11FC9D98B45A}'))
	def _get_RFlexBody(self):
		return self._ApplyTypes_(*(3002, 2, (9, 0), (), "RFlexBody", '{5737600D-0E40-4578-9E18-8CBE68916DF8}'))
	def _get_Type(self):
		return self._ApplyTypes_(*(3003, 2, (3, 0), (), "Type", '{BF28A376-C8E8-493C-B09F-BF5FCE1645E7}'))

	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))

	ID = property(_get_ID, None)
	'''
	Modal Load Case ID

	:type: int
	'''
	ModalLoadValue = property(_get_ModalLoadValue, None)
	'''
	Modal Load Value

	:type: recurdyn.RFlex.IRFlexModalLoadValue
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Modal Load Case Name

	:type: str
	'''
	NodalLoadValueCollection = property(_get_NodalLoadValueCollection, None)
	'''
	Nodal Load Value Collection

	:type: recurdyn.RFlex.IRFlexNodalLoadValueCollection
	'''
	RFlexBody = property(_get_RFlexBody, None)
	'''
	RFlex Body

	:type: recurdyn.RFlex.IRFlexBody
	'''
	Type = property(_get_Type, _set_Type)
	'''
	Modal Load Case Type

	:type: recurdyn.RFlex.ModalLoadCaseType
	'''

	_prop_map_set_function_ = {
		"_set_Name": _set_Name,
		"_set_Type": _set_Type,
	}
	_prop_map_get_ = {
		"ID": (3000, 2, (19, 0), (), "ID", None),
		"ModalLoadValue": (3005, 2, (9, 0), (), "ModalLoadValue", '{DC95F017-DABD-4F7B-8E19-D6DC880124BF}'),
		"Name": (3001, 2, (8, 0), (), "Name", None),
		"NodalLoadValueCollection": (3004, 2, (9, 0), (), "NodalLoadValueCollection", '{8AEC2258-C39F-452F-BA67-11FC9D98B45A}'),
		"RFlexBody": (3002, 2, (9, 0), (), "RFlexBody", '{5737600D-0E40-4578-9E18-8CBE68916DF8}'),
		"Type": (3003, 2, (3, 0), (), "Type", '{BF28A376-C8E8-493C-B09F-BF5FCE1645E7}'),
	}
	_prop_map_put_ = {
		"Name": ((3001, LCID, 4, 0),()),
		"Type": ((3003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexModalLoadCaseCollection(DispatchBaseClass):
	'''IRFlexModalLoadCaseCollection'''
	CLSID = IID('{B42BB386-EA95-4AE6-9A24-C74CB5027EB2}')
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
		:rtype: recurdyn.RFlex.IRFlexModalLoadCase
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{6FB3F9CE-90B7-4111-8714-AA24F53632A6}')
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
		:rtype: recurdyn.RFlex.IRFlexModalLoadCase
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{6FB3F9CE-90B7-4111-8714-AA24F53632A6}')
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
		return win32com.client.util.Iterator(ob, '{6FB3F9CE-90B7-4111-8714-AA24F53632A6}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{6FB3F9CE-90B7-4111-8714-AA24F53632A6}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexModalLoadValue(DispatchBaseClass):
	'''Modal Load Type Detail Value'''
	CLSID = IID('{DC95F017-DABD-4F7B-8E19-D6DC880124BF}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_FX(self):
		return self._ApplyTypes_(*(3001, 2, (5, 0), (), "FX", None))
	def _get_FY(self):
		return self._ApplyTypes_(*(3002, 2, (5, 0), (), "FY", None))
	def _get_FZ(self):
		return self._ApplyTypes_(*(3003, 2, (5, 0), (), "FZ", None))
	def _get_ModeValueCollection(self):
		return self._ApplyTypes_(*(3000, 2, (9, 0), (), "ModeValueCollection", '{FD818ABF-BF56-4B8B-896B-01F99E1ED037}'))
	def _get_TX(self):
		return self._ApplyTypes_(*(3004, 2, (5, 0), (), "TX", None))
	def _get_TY(self):
		return self._ApplyTypes_(*(3005, 2, (5, 0), (), "TY", None))
	def _get_TZ(self):
		return self._ApplyTypes_(*(3006, 2, (5, 0), (), "TZ", None))

	def _set_FX(self, value):
		if "FX" in self.__dict__: self.__dict__["FX"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_FY(self, value):
		if "FY" in self.__dict__: self.__dict__["FY"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_FZ(self, value):
		if "FZ" in self.__dict__: self.__dict__["FZ"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_TX(self, value):
		if "TX" in self.__dict__: self.__dict__["TX"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_TY(self, value):
		if "TY" in self.__dict__: self.__dict__["TY"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))
	def _set_TZ(self, value):
		if "TZ" in self.__dict__: self.__dict__["TZ"] = value; return
		self._oleobj_.Invoke(*((3006, LCID, 4, 0) + (value,) + ()))

	FX = property(_get_FX, _set_FX)
	'''
	FX Value

	:type: float
	'''
	FY = property(_get_FY, _set_FY)
	'''
	FY Value

	:type: float
	'''
	FZ = property(_get_FZ, _set_FZ)
	'''
	FZ Value

	:type: float
	'''
	ModeValueCollection = property(_get_ModeValueCollection, None)
	'''
	Mode Value Collection

	:type: recurdyn.RFlex.IRFlexModeValueCollection
	'''
	TX = property(_get_TX, _set_TX)
	'''
	TX Value

	:type: float
	'''
	TY = property(_get_TY, _set_TY)
	'''
	TY Value

	:type: float
	'''
	TZ = property(_get_TZ, _set_TZ)
	'''
	TZ Value

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_FX": _set_FX,
		"_set_FY": _set_FY,
		"_set_FZ": _set_FZ,
		"_set_TX": _set_TX,
		"_set_TY": _set_TY,
		"_set_TZ": _set_TZ,
	}
	_prop_map_get_ = {
		"FX": (3001, 2, (5, 0), (), "FX", None),
		"FY": (3002, 2, (5, 0), (), "FY", None),
		"FZ": (3003, 2, (5, 0), (), "FZ", None),
		"ModeValueCollection": (3000, 2, (9, 0), (), "ModeValueCollection", '{FD818ABF-BF56-4B8B-896B-01F99E1ED037}'),
		"TX": (3004, 2, (5, 0), (), "TX", None),
		"TY": (3005, 2, (5, 0), (), "TY", None),
		"TZ": (3006, 2, (5, 0), (), "TZ", None),
	}
	_prop_map_put_ = {
		"FX": ((3001, LCID, 4, 0),()),
		"FY": ((3002, LCID, 4, 0),()),
		"FZ": ((3003, LCID, 4, 0),()),
		"TX": ((3004, LCID, 4, 0),()),
		"TY": ((3005, LCID, 4, 0),()),
		"TZ": ((3006, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexModeInformation(DispatchBaseClass):
	'''Mode Information'''
	CLSID = IID('{7ED2BDE4-77AC-4D41-8745-10EB8FC6812C}')
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
		return self._ApplyTypes_(*(3003, 2, (5, 0), (), "DampingCoefficient", None))
	def _get_Frequency(self):
		return self._ApplyTypes_(*(3002, 2, (5, 0), (), "Frequency", None))
	def _get_UseMode(self):
		return self._ApplyTypes_(*(3001, 2, (11, 0), (), "UseMode", None))
	def _get_UseModeForAnimation(self):
		return self._ApplyTypes_(*(3004, 2, (11, 0), (), "UseModeForAnimation", None))

	def _set_DampingCoefficient(self, value):
		if "DampingCoefficient" in self.__dict__: self.__dict__["DampingCoefficient"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_UseMode(self, value):
		if "UseMode" in self.__dict__: self.__dict__["UseMode"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_UseModeForAnimation(self, value):
		if "UseModeForAnimation" in self.__dict__: self.__dict__["UseModeForAnimation"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))

	DampingCoefficient = property(_get_DampingCoefficient, _set_DampingCoefficient)
	'''
	Damping Coefficient

	:type: float
	'''
	Frequency = property(_get_Frequency, None)
	'''
	Frequency of the mode

	:type: float
	'''
	UseMode = property(_get_UseMode, _set_UseMode)
	'''
	Use this mode

	:type: bool
	'''
	UseModeForAnimation = property(_get_UseModeForAnimation, _set_UseModeForAnimation)
	'''
	Use this mode for animation

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_DampingCoefficient": _set_DampingCoefficient,
		"_set_UseMode": _set_UseMode,
		"_set_UseModeForAnimation": _set_UseModeForAnimation,
	}
	_prop_map_get_ = {
		"DampingCoefficient": (3003, 2, (5, 0), (), "DampingCoefficient", None),
		"Frequency": (3002, 2, (5, 0), (), "Frequency", None),
		"UseMode": (3001, 2, (11, 0), (), "UseMode", None),
		"UseModeForAnimation": (3004, 2, (11, 0), (), "UseModeForAnimation", None),
	}
	_prop_map_put_ = {
		"DampingCoefficient": ((3003, LCID, 4, 0),()),
		"UseMode": ((3001, LCID, 4, 0),()),
		"UseModeForAnimation": ((3004, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexModeValue(DispatchBaseClass):
	'''Mode Value Force Modal Load Value'''
	CLSID = IID('{EBF8DAD1-BFE3-4A50-BF0B-2ACC1B3FA3C6}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ModeValue(self):
		return self._ApplyTypes_(*(3001, 2, (5, 0), (), "ModeValue", None))
	def _get_Sequence(self):
		return self._ApplyTypes_(*(3000, 2, (19, 0), (), "Sequence", None))

	def _set_ModeValue(self, value):
		if "ModeValue" in self.__dict__: self.__dict__["ModeValue"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))

	ModeValue = property(_get_ModeValue, _set_ModeValue)
	'''
	Mode Value

	:type: float
	'''
	Sequence = property(_get_Sequence, None)
	'''
	Mode Sequence

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_ModeValue": _set_ModeValue,
	}
	_prop_map_get_ = {
		"ModeValue": (3001, 2, (5, 0), (), "ModeValue", None),
		"Sequence": (3000, 2, (19, 0), (), "Sequence", None),
	}
	_prop_map_put_ = {
		"ModeValue": ((3001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexModeValueCollection(DispatchBaseClass):
	'''IRFlexModeValue Collection'''
	CLSID = IID('{FD818ABF-BF56-4B8B-896B-01F99E1ED037}')
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
		:rtype: recurdyn.RFlex.IRFlexModeValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{EBF8DAD1-BFE3-4A50-BF0B-2ACC1B3FA3C6}')
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
		:rtype: recurdyn.RFlex.IRFlexModeValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{EBF8DAD1-BFE3-4A50-BF0B-2ACC1B3FA3C6}')
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
		return win32com.client.util.Iterator(ob, '{EBF8DAD1-BFE3-4A50-BF0B-2ACC1B3FA3C6}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{EBF8DAD1-BFE3-4A50-BF0B-2ACC1B3FA3C6}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexNodalLoadValue(DispatchBaseClass):
	'''Nodal Load Type Detail Value'''
	CLSID = IID('{5104436A-9AB2-4C96-8550-F085D5BE63F9}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_FX(self):
		return self._ApplyTypes_(*(3001, 2, (5, 0), (), "FX", None))
	def _get_FY(self):
		return self._ApplyTypes_(*(3002, 2, (5, 0), (), "FY", None))
	def _get_FZ(self):
		return self._ApplyTypes_(*(3003, 2, (5, 0), (), "FZ", None))
	def _get_NodeID(self):
		return self._ApplyTypes_(*(3000, 2, (19, 0), (), "NodeID", None))
	def _get_TX(self):
		return self._ApplyTypes_(*(3004, 2, (5, 0), (), "TX", None))
	def _get_TY(self):
		return self._ApplyTypes_(*(3005, 2, (5, 0), (), "TY", None))
	def _get_TZ(self):
		return self._ApplyTypes_(*(3006, 2, (5, 0), (), "TZ", None))

	def _set_FX(self, value):
		if "FX" in self.__dict__: self.__dict__["FX"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_FY(self, value):
		if "FY" in self.__dict__: self.__dict__["FY"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_FZ(self, value):
		if "FZ" in self.__dict__: self.__dict__["FZ"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_TX(self, value):
		if "TX" in self.__dict__: self.__dict__["TX"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_TY(self, value):
		if "TY" in self.__dict__: self.__dict__["TY"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))
	def _set_TZ(self, value):
		if "TZ" in self.__dict__: self.__dict__["TZ"] = value; return
		self._oleobj_.Invoke(*((3006, LCID, 4, 0) + (value,) + ()))

	FX = property(_get_FX, _set_FX)
	'''
	FX Value

	:type: float
	'''
	FY = property(_get_FY, _set_FY)
	'''
	FY Value

	:type: float
	'''
	FZ = property(_get_FZ, _set_FZ)
	'''
	FZ Value

	:type: float
	'''
	NodeID = property(_get_NodeID, None)
	'''
	Node ID

	:type: int
	'''
	TX = property(_get_TX, _set_TX)
	'''
	TX Value

	:type: float
	'''
	TY = property(_get_TY, _set_TY)
	'''
	TY Value

	:type: float
	'''
	TZ = property(_get_TZ, _set_TZ)
	'''
	TZ Value

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_FX": _set_FX,
		"_set_FY": _set_FY,
		"_set_FZ": _set_FZ,
		"_set_TX": _set_TX,
		"_set_TY": _set_TY,
		"_set_TZ": _set_TZ,
	}
	_prop_map_get_ = {
		"FX": (3001, 2, (5, 0), (), "FX", None),
		"FY": (3002, 2, (5, 0), (), "FY", None),
		"FZ": (3003, 2, (5, 0), (), "FZ", None),
		"NodeID": (3000, 2, (19, 0), (), "NodeID", None),
		"TX": (3004, 2, (5, 0), (), "TX", None),
		"TY": (3005, 2, (5, 0), (), "TY", None),
		"TZ": (3006, 2, (5, 0), (), "TZ", None),
	}
	_prop_map_put_ = {
		"FX": ((3001, LCID, 4, 0),()),
		"FY": ((3002, LCID, 4, 0),()),
		"FZ": ((3003, LCID, 4, 0),()),
		"TX": ((3004, LCID, 4, 0),()),
		"TY": ((3005, LCID, 4, 0),()),
		"TZ": ((3006, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexNodalLoadValueCollection(DispatchBaseClass):
	'''IRFlexNodalLoadValueCollection'''
	CLSID = IID('{8AEC2258-C39F-452F-BA67-11FC9D98B45A}')
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
		:rtype: recurdyn.RFlex.IRFlexNodalLoadValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5104436A-9AB2-4C96-8550-F085D5BE63F9}')
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
		:rtype: recurdyn.RFlex.IRFlexNodalLoadValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5104436A-9AB2-4C96-8550-F085D5BE63F9}')
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
		return win32com.client.util.Iterator(ob, '{5104436A-9AB2-4C96-8550-F085D5BE63F9}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{5104436A-9AB2-4C96-8550-F085D5BE63F9}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexNode(DispatchBaseClass):
	'''RFlex Node'''
	CLSID = IID('{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')
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
	def _get_ID(self):
		return self._ApplyTypes_(*(151, 2, (19, 0), (), "ID", None))
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
	def _get_x(self):
		return self._ApplyTypes_(*(152, 2, (5, 0), (), "x", None))
	def _get_y(self):
		return self._ApplyTypes_(*(153, 2, (5, 0), (), "y", None))
	def _get_z(self):
		return self._ApplyTypes_(*(154, 2, (5, 0), (), "z", None))

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
	ID = property(_get_ID, None)
	'''
	ID

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
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	x = property(_get_x, None)
	'''
	Position X

	:type: float
	'''
	y = property(_get_y, None)
	'''
	Position Y

	:type: float
	'''
	z = property(_get_z, None)
	'''
	Position Z

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"ID": (151, 2, (19, 0), (), "ID", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"x": (152, 2, (5, 0), (), "x", None),
		"y": (153, 2, (5, 0), (), "y", None),
		"z": (154, 2, (5, 0), (), "z", None),
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

class IRFlexNodeCollection(DispatchBaseClass):
	'''IRFlexNodeCollection'''
	CLSID = IID('{EEEA6051-9841-4895-BC92-93F52E98A389}')
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
		:rtype: recurdyn.RFlex.IRFlexNode
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')
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
		:rtype: recurdyn.RFlex.IRFlexNode
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')
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
		return win32com.client.util.Iterator(ob, '{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexNodeSet(DispatchBaseClass):
	CLSID = IID('{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddNodes(self, val):
		'''
		Add Nodes
		
		:param val: list[int]
		'''
		return self._oleobj_.InvokeTypes(3054, LCID, 1, (24, 0), ((8195, 1),),val
			)


	def DeleteNodes(self, val):
		'''
		Delete Nodes
		
		:param val: list[int]
		'''
		return self._oleobj_.InvokeTypes(3055, LCID, 1, (24, 0), ((8195, 1),),val
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Color(self):
		return self._ApplyTypes_(*(3053, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeCollection(self):
		return self._ApplyTypes_(*(3052, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'))
	def _get_NodeIDs(self):
		return self._ApplyTypes_(*(3051, 2, (8195, 0), (), "NodeIDs", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((3053, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Node set color

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
	NodeCollection = property(_get_NodeCollection, None)
	'''
	Node Collection

	:type: recurdyn.RFlex.IRFlexNodeCollection
	'''
	NodeIDs = property(_get_NodeIDs, None)
	'''
	Contains Node

	:type: list[int]
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
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Color": (3053, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeCollection": (3052, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'),
		"NodeIDs": (3051, 2, (8195, 0), (), "NodeIDs", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Color": ((3053, LCID, 4, 0),()),
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

class IRFlexNodeSetCollection(DispatchBaseClass):
	'''IRFlexNodeSetCollection'''
	CLSID = IID('{2AAD6766-1ED5-498D-96BA-F9363B2DF588}')
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
		:rtype: recurdyn.RFlex.IRFlexNodeSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')
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
		:rtype: recurdyn.RFlex.IRFlexNodeSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')
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
		return win32com.client.util.Iterator(ob, '{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexOutput(DispatchBaseClass):
	CLSID = IID('{5C616B86-29F2-486F-9E0C-D66502222E30}')
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
		return self._ApplyTypes_(*(3003, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeCollection(self):
		return self._ApplyTypes_(*(3002, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'))
	def _get_NodeIDs(self):
		return self._ApplyTypes_(*(3001, 2, (8195, 0), (), "NodeIDs", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Output color

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
	NodeCollection = property(_get_NodeCollection, None)
	'''
	Node Collection

	:type: recurdyn.RFlex.IRFlexNodeCollection
	'''
	NodeIDs = property(_get_NodeIDs, None)
	'''
	Contains Node

	:type: list[int]
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
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Color": (3003, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeCollection": (3002, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'),
		"NodeIDs": (3001, 2, (8195, 0), (), "NodeIDs", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Color": ((3003, LCID, 4, 0),()),
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

class IRFlexOutputCollection(DispatchBaseClass):
	'''IRFlexOutputCollection'''
	CLSID = IID('{D1E612A4-BFE5-4676-B55D-76C41FE47B42}')
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
		:rtype: recurdyn.RFlex.IRFlexOutput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{5C616B86-29F2-486F-9E0C-D66502222E30}')
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
		:rtype: recurdyn.RFlex.IRFlexOutput
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{5C616B86-29F2-486F-9E0C-D66502222E30}')
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
		return win32com.client.util.Iterator(ob, '{5C616B86-29F2-486F-9E0C-D66502222E30}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{5C616B86-29F2-486F-9E0C-D66502222E30}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexOutputFileGenerator(DispatchBaseClass):
	'''RFlex Output File Generator'''
	CLSID = IID('{6ED5F207-C518-4800-BA75-7990D637BAB5}')
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
		Generate
		'''
		return self._oleobj_.InvokeTypes(3002, LCID, 1, (24, 0), (),)


	def _get_OutputFileSetting(self):
		return self._ApplyTypes_(*(3001, 2, (9, 0), (), "OutputFileSetting", '{350C9018-D3B8-4D6B-B9EC-271CE461FDC0}'))

	OutputFileSetting = property(_get_OutputFileSetting, None)
	'''
	Get Output file Setting

	:type: recurdyn.ProcessNet.IStrainStressOutputFileSetting
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"OutputFileSetting": (3001, 2, (9, 0), (), "OutputFileSetting", '{350C9018-D3B8-4D6B-B9EC-271CE461FDC0}'),
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

class IRFlexOutputFileInfo(DispatchBaseClass):
	'''RFlex Output File Information'''
	CLSID = IID('{16BD870A-FA04-42F6-8B8D-7F484F5D421E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AnimationFileState(self):
		return self._ApplyTypes_(*(3003, 2, (8, 0), (), "AnimationFileState", None))
	def _get_BodyName(self):
		return self._ApplyTypes_(*(3001, 2, (8, 0), (), "BodyName", None))
	def _get_ShellRecoveryType(self):
		return self._ApplyTypes_(*(3006, 2, (3, 0), (), "ShellRecoveryType", '{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}'))
	def _get_StrainFileState(self):
		return self._ApplyTypes_(*(3004, 2, (8, 0), (), "StrainFileState", None))
	def _get_StressFileState(self):
		return self._ApplyTypes_(*(3005, 2, (8, 0), (), "StressFileState", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(3002, 2, (11, 0), (), "Use", None))

	def _set_ShellRecoveryType(self, value):
		if "ShellRecoveryType" in self.__dict__: self.__dict__["ShellRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3006, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))

	AnimationFileState = property(_get_AnimationFileState, None)
	'''
	Get rfa file state

	:type: str
	'''
	BodyName = property(_get_BodyName, None)
	'''
	Body name

	:type: str
	'''
	ShellRecoveryType = property(_get_ShellRecoveryType, _set_ShellRecoveryType)
	'''
	Shell recovery type

	:type: recurdyn.RFlex.ShellRecoveryType
	'''
	StrainFileState = property(_get_StrainFileState, None)
	'''
	Get erd file state

	:type: str
	'''
	StressFileState = property(_get_StressFileState, None)
	'''
	Get srd file state

	:type: str
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Generate flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_ShellRecoveryType": _set_ShellRecoveryType,
		"_set_Use": _set_Use,
	}
	_prop_map_get_ = {
		"AnimationFileState": (3003, 2, (8, 0), (), "AnimationFileState", None),
		"BodyName": (3001, 2, (8, 0), (), "BodyName", None),
		"ShellRecoveryType": (3006, 2, (3, 0), (), "ShellRecoveryType", '{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}'),
		"StrainFileState": (3004, 2, (8, 0), (), "StrainFileState", None),
		"StressFileState": (3005, 2, (8, 0), (), "StressFileState", None),
		"Use": (3002, 2, (11, 0), (), "Use", None),
	}
	_prop_map_put_ = {
		"ShellRecoveryType": ((3006, LCID, 4, 0),()),
		"Use": ((3002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexOutputFileInfoForRegenerator(DispatchBaseClass):
	'''RFlex Output File Information for Regenerator'''
	CLSID = IID('{1B06647C-BAD6-464A-8B5E-DD243D535970}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AnimationFileState(self):
		return self._ApplyTypes_(*(3009, 2, (8, 0), (), "AnimationFileState", None))
	def _get_BeamRecoveryType(self):
		return self._ApplyTypes_(*(3013, 2, (3, 0), (), "BeamRecoveryType", '{E6829DB6-AAEE-4CC3-9BC8-BF1F91851DF4}'))
	def _get_BodyName(self):
		return self._ApplyTypes_(*(3001, 2, (8, 0), (), "BodyName", None))
	def _get_DisplacementDataPrecision(self):
		return self._ApplyTypes_(*(3012, 2, (3, 0), (), "DisplacementDataPrecision", '{511C893E-A8F1-4026-80BE-F02530E47D72}'))
	def _get_StrainFileState(self):
		return self._ApplyTypes_(*(3010, 2, (8, 0), (), "StrainFileState", None))
	def _get_StrainShellRecoveryType(self):
		return self._ApplyTypes_(*(3007, 2, (8, 0), (), "StrainShellRecoveryType", None))
	def _get_StrainShellRecoveryTypeList(self):
		return self._ApplyTypes_(*(3005, 2, (8200, 0), (), "StrainShellRecoveryTypeList", None))
	def _get_StressFileState(self):
		return self._ApplyTypes_(*(3011, 2, (8, 0), (), "StressFileState", None))
	def _get_StressShellRecoveryType(self):
		return self._ApplyTypes_(*(3008, 2, (8, 0), (), "StressShellRecoveryType", None))
	def _get_StressShellRecoveryTypeList(self):
		return self._ApplyTypes_(*(3006, 2, (8200, 0), (), "StressShellRecoveryTypeList", None))
	def _get_UseDisplacementData(self):
		return self._ApplyTypes_(*(3002, 2, (11, 0), (), "UseDisplacementData", None))
	def _get_UseStrainStressData(self):
		return self._ApplyTypes_(*(3003, 2, (11, 0), (), "UseStrainStressData", None))

	def _set_BeamRecoveryType(self, value):
		if "BeamRecoveryType" in self.__dict__: self.__dict__["BeamRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3013, LCID, 4, 0) + (value,) + ()))
	def _set_DisplacementDataPrecision(self, value):
		if "DisplacementDataPrecision" in self.__dict__: self.__dict__["DisplacementDataPrecision"] = value; return
		self._oleobj_.Invoke(*((3012, LCID, 4, 0) + (value,) + ()))
	def _set_StrainShellRecoveryType(self, value):
		if "StrainShellRecoveryType" in self.__dict__: self.__dict__["StrainShellRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3007, LCID, 4, 0) + (value,) + ()))
	def _set_StressShellRecoveryType(self, value):
		if "StressShellRecoveryType" in self.__dict__: self.__dict__["StressShellRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3008, LCID, 4, 0) + (value,) + ()))
	def _set_UseDisplacementData(self, value):
		if "UseDisplacementData" in self.__dict__: self.__dict__["UseDisplacementData"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_UseStrainStressData(self, value):
		if "UseStrainStressData" in self.__dict__: self.__dict__["UseStrainStressData"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))

	AnimationFileState = property(_get_AnimationFileState, None)
	'''
	Get rfa file state

	:type: str
	'''
	BeamRecoveryType = property(_get_BeamRecoveryType, _set_BeamRecoveryType)
	'''
	Beam recovery type

	:type: recurdyn.RFlex.BeamRecoveryType
	'''
	BodyName = property(_get_BodyName, None)
	'''
	Body name

	:type: str
	'''
	DisplacementDataPrecision = property(_get_DisplacementDataPrecision, _set_DisplacementDataPrecision)
	'''
	Displacement(.rfa) Precision

	:type: recurdyn.RFlex.DisplacementDataPrecision
	'''
	StrainFileState = property(_get_StrainFileState, None)
	'''
	Get erd file state

	:type: str
	'''
	StrainShellRecoveryType = property(_get_StrainShellRecoveryType, _set_StrainShellRecoveryType)
	'''
	Strain Shell recovery type

	:type: str
	'''
	StrainShellRecoveryTypeList = property(_get_StrainShellRecoveryTypeList, None)
	'''
	Strain Shell recovery type

	:type: list[str]
	'''
	StressFileState = property(_get_StressFileState, None)
	'''
	Get srd file state

	:type: str
	'''
	StressShellRecoveryType = property(_get_StressShellRecoveryType, _set_StressShellRecoveryType)
	'''
	Stress Shell recovery type

	:type: str
	'''
	StressShellRecoveryTypeList = property(_get_StressShellRecoveryTypeList, None)
	'''
	Stress Shell recovery type

	:type: list[str]
	'''
	UseDisplacementData = property(_get_UseDisplacementData, _set_UseDisplacementData)
	'''
	Generate displacement data flag

	:type: bool
	'''
	UseStrainStressData = property(_get_UseStrainStressData, _set_UseStrainStressData)
	'''
	Generate strain stress data flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_BeamRecoveryType": _set_BeamRecoveryType,
		"_set_DisplacementDataPrecision": _set_DisplacementDataPrecision,
		"_set_StrainShellRecoveryType": _set_StrainShellRecoveryType,
		"_set_StressShellRecoveryType": _set_StressShellRecoveryType,
		"_set_UseDisplacementData": _set_UseDisplacementData,
		"_set_UseStrainStressData": _set_UseStrainStressData,
	}
	_prop_map_get_ = {
		"AnimationFileState": (3009, 2, (8, 0), (), "AnimationFileState", None),
		"BeamRecoveryType": (3013, 2, (3, 0), (), "BeamRecoveryType", '{E6829DB6-AAEE-4CC3-9BC8-BF1F91851DF4}'),
		"BodyName": (3001, 2, (8, 0), (), "BodyName", None),
		"DisplacementDataPrecision": (3012, 2, (3, 0), (), "DisplacementDataPrecision", '{511C893E-A8F1-4026-80BE-F02530E47D72}'),
		"StrainFileState": (3010, 2, (8, 0), (), "StrainFileState", None),
		"StrainShellRecoveryType": (3007, 2, (8, 0), (), "StrainShellRecoveryType", None),
		"StrainShellRecoveryTypeList": (3005, 2, (8200, 0), (), "StrainShellRecoveryTypeList", None),
		"StressFileState": (3011, 2, (8, 0), (), "StressFileState", None),
		"StressShellRecoveryType": (3008, 2, (8, 0), (), "StressShellRecoveryType", None),
		"StressShellRecoveryTypeList": (3006, 2, (8200, 0), (), "StressShellRecoveryTypeList", None),
		"UseDisplacementData": (3002, 2, (11, 0), (), "UseDisplacementData", None),
		"UseStrainStressData": (3003, 2, (11, 0), (), "UseStrainStressData", None),
	}
	_prop_map_put_ = {
		"BeamRecoveryType": ((3013, LCID, 4, 0),()),
		"DisplacementDataPrecision": ((3012, LCID, 4, 0),()),
		"StrainShellRecoveryType": ((3007, LCID, 4, 0),()),
		"StressShellRecoveryType": ((3008, LCID, 4, 0),()),
		"UseDisplacementData": ((3002, LCID, 4, 0),()),
		"UseStrainStressData": ((3003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexOutputFileRegenerator(DispatchBaseClass):
	'''RFlex Output File Regenerator'''
	CLSID = IID('{4E476724-E71A-4106-A906-531EBAC1F17A}')
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
		Generate
		'''
		return self._oleobj_.InvokeTypes(3006, LCID, 1, (24, 0), (),)


	def _get_BeamRecoveryType(self):
		return self._ApplyTypes_(*(3009, 2, (3, 0), (), "BeamRecoveryType", '{E6829DB6-AAEE-4CC3-9BC8-BF1F91851DF4}'))
	def _get_DisplacementDataPrecision(self):
		return self._ApplyTypes_(*(3008, 2, (3, 0), (), "DisplacementDataPrecision", '{511C893E-A8F1-4026-80BE-F02530E47D72}'))
	def _get_OutputFileSetting(self):
		return self._ApplyTypes_(*(3005, 2, (9, 0), (), "OutputFileSetting", '{350C9018-D3B8-4D6B-B9EC-271CE461FDC0}'))
	def _get_RecoverDisplacementData(self):
		return self._ApplyTypes_(*(3002, 2, (11, 0), (), "RecoverDisplacementData", None))
	def _get_RecoverStrainStressData(self):
		return self._ApplyTypes_(*(3003, 2, (11, 0), (), "RecoverStrainStressData", None))
	def _get_SameOptionsforAllRFlexBodies(self):
		return self._ApplyTypes_(*(3001, 2, (11, 0), (), "SameOptionsforAllRFlexBodies", None))
	def _get_ShellRecoveryType(self):
		return self._ApplyTypes_(*(3004, 2, (3, 0), (), "ShellRecoveryType", '{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}'))
	def _get_UserDefinedAnimation(self):
		return self._ApplyTypes_(*(3007, 2, (11, 0), (), "UserDefinedAnimation", None))

	def _set_BeamRecoveryType(self, value):
		if "BeamRecoveryType" in self.__dict__: self.__dict__["BeamRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3009, LCID, 4, 0) + (value,) + ()))
	def _set_DisplacementDataPrecision(self, value):
		if "DisplacementDataPrecision" in self.__dict__: self.__dict__["DisplacementDataPrecision"] = value; return
		self._oleobj_.Invoke(*((3008, LCID, 4, 0) + (value,) + ()))
	def _set_RecoverDisplacementData(self, value):
		if "RecoverDisplacementData" in self.__dict__: self.__dict__["RecoverDisplacementData"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_RecoverStrainStressData(self, value):
		if "RecoverStrainStressData" in self.__dict__: self.__dict__["RecoverStrainStressData"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_SameOptionsforAllRFlexBodies(self, value):
		if "SameOptionsforAllRFlexBodies" in self.__dict__: self.__dict__["SameOptionsforAllRFlexBodies"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_ShellRecoveryType(self, value):
		if "ShellRecoveryType" in self.__dict__: self.__dict__["ShellRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_UserDefinedAnimation(self, value):
		if "UserDefinedAnimation" in self.__dict__: self.__dict__["UserDefinedAnimation"] = value; return
		self._oleobj_.Invoke(*((3007, LCID, 4, 0) + (value,) + ()))

	BeamRecoveryType = property(_get_BeamRecoveryType, _set_BeamRecoveryType)
	'''
	Beam recovery type

	:type: recurdyn.RFlex.BeamRecoveryType
	'''
	DisplacementDataPrecision = property(_get_DisplacementDataPrecision, _set_DisplacementDataPrecision)
	'''
	Displacement(.rfa) Precision

	:type: recurdyn.RFlex.DisplacementDataPrecision
	'''
	OutputFileSetting = property(_get_OutputFileSetting, None)
	'''
	Output file Setting

	:type: recurdyn.ProcessNet.IStrainStressOutputFileSetting
	'''
	RecoverDisplacementData = property(_get_RecoverDisplacementData, _set_RecoverDisplacementData)
	'''
	Recover displacement data flag

	:type: bool
	'''
	RecoverStrainStressData = property(_get_RecoverStrainStressData, _set_RecoverStrainStressData)
	'''
	Recover strain stress data flag

	:type: bool
	'''
	SameOptionsforAllRFlexBodies = property(_get_SameOptionsforAllRFlexBodies, _set_SameOptionsforAllRFlexBodies)
	'''
	Same options for all bodies flag

	:type: bool
	'''
	ShellRecoveryType = property(_get_ShellRecoveryType, _set_ShellRecoveryType)
	'''
	Shell recovery type

	:type: recurdyn.RFlex.ShellRecoveryType
	'''
	UserDefinedAnimation = property(_get_UserDefinedAnimation, _set_UserDefinedAnimation)
	'''
	User Defined Animation flag

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_BeamRecoveryType": _set_BeamRecoveryType,
		"_set_DisplacementDataPrecision": _set_DisplacementDataPrecision,
		"_set_RecoverDisplacementData": _set_RecoverDisplacementData,
		"_set_RecoverStrainStressData": _set_RecoverStrainStressData,
		"_set_SameOptionsforAllRFlexBodies": _set_SameOptionsforAllRFlexBodies,
		"_set_ShellRecoveryType": _set_ShellRecoveryType,
		"_set_UserDefinedAnimation": _set_UserDefinedAnimation,
	}
	_prop_map_get_ = {
		"BeamRecoveryType": (3009, 2, (3, 0), (), "BeamRecoveryType", '{E6829DB6-AAEE-4CC3-9BC8-BF1F91851DF4}'),
		"DisplacementDataPrecision": (3008, 2, (3, 0), (), "DisplacementDataPrecision", '{511C893E-A8F1-4026-80BE-F02530E47D72}'),
		"OutputFileSetting": (3005, 2, (9, 0), (), "OutputFileSetting", '{350C9018-D3B8-4D6B-B9EC-271CE461FDC0}'),
		"RecoverDisplacementData": (3002, 2, (11, 0), (), "RecoverDisplacementData", None),
		"RecoverStrainStressData": (3003, 2, (11, 0), (), "RecoverStrainStressData", None),
		"SameOptionsforAllRFlexBodies": (3001, 2, (11, 0), (), "SameOptionsforAllRFlexBodies", None),
		"ShellRecoveryType": (3004, 2, (3, 0), (), "ShellRecoveryType", '{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}'),
		"UserDefinedAnimation": (3007, 2, (11, 0), (), "UserDefinedAnimation", None),
	}
	_prop_map_put_ = {
		"BeamRecoveryType": ((3009, LCID, 4, 0),()),
		"DisplacementDataPrecision": ((3008, LCID, 4, 0),()),
		"RecoverDisplacementData": ((3002, LCID, 4, 0),()),
		"RecoverStrainStressData": ((3003, LCID, 4, 0),()),
		"SameOptionsforAllRFlexBodies": ((3001, LCID, 4, 0),()),
		"ShellRecoveryType": ((3004, LCID, 4, 0),()),
		"UserDefinedAnimation": ((3007, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexPatchSet(DispatchBaseClass):
	CLSID = IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
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
		return self._ApplyTypes_(*(3053, 2, (19, 0), (), "Color", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeCollection(self):
		return self._ApplyTypes_(*(3052, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'))
	def _get_NodeIDs(self):
		return self._ApplyTypes_(*(3051, 2, (8195, 0), (), "NodeIDs", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((3053, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Color = property(_get_Color, _set_Color)
	'''
	Patch set color

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
	NodeCollection = property(_get_NodeCollection, None)
	'''
	Node Collection

	:type: recurdyn.RFlex.IRFlexNodeCollection
	'''
	NodeIDs = property(_get_NodeIDs, None)
	'''
	Contains Node

	:type: list[int]
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
		"_set_Color": _set_Color,
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Color": (3053, 2, (19, 0), (), "Color", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeCollection": (3052, 2, (9, 0), (), "NodeCollection", '{EEEA6051-9841-4895-BC92-93F52E98A389}'),
		"NodeIDs": (3051, 2, (8195, 0), (), "NodeIDs", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Color": ((3053, LCID, 4, 0),()),
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

class IRFlexPatchSetCollection(DispatchBaseClass):
	'''IRFlexPatchSetCollection'''
	CLSID = IID('{6A9E16A5-2CCC-4596-BDC0-07B767DB1A39}')
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
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
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
		:rtype: recurdyn.RFlex.IRFlexPatchSet
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
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
		return win32com.client.util.Iterator(ob, '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexRFIOptimizerOption(DispatchBaseClass):
	'''RFI Optimizer option'''
	CLSID = IID('{7CA7CF6E-47A2-417F-8E24-056FB7F2359E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ChangeToExternalPatchFlag(self):
		return self._ApplyTypes_(*(3005, 2, (11, 0), (), "ChangeToExternalPatchFlag", None))
	def _get_DATFileName(self):
		return self._ApplyTypes_(*(3012, 2, (8, 0), (), "DATFileName", None))
	def _get_OP2FileName(self):
		return self._ApplyTypes_(*(3001, 2, (8, 0), (), "OP2FileName", None))
	def _get_OriginalRFIFileName(self):
		return self._ApplyTypes_(*(3000, 2, (8, 0), (), "OriginalRFIFileName", None))
	def _get_RFlexBody(self):
		return self._ApplyTypes_(*(3011, 2, (9, 0), (), "RFlexBody", '{5737600D-0E40-4578-9E18-8CBE68916DF8}'))
	def _get_RemainExternalNodesFlag(self):
		return self._ApplyTypes_(*(3013, 2, (11, 0), (), "RemainExternalNodesFlag", None))
	def _get_RemainSelectedNodes(self):
		return self._ApplyTypes_(*(3016, 2, (8, 0), (), "RemainSelectedNodes", None))
	def _get_RemainSelectedNodesFlag(self):
		return self._ApplyTypes_(*(3015, 2, (11, 0), (), "RemainSelectedNodesFlag", None))
	def _get_RemainUsedNodesFlag(self):
		return self._ApplyTypes_(*(3014, 2, (11, 0), (), "RemainUsedNodesFlag", None))
	def _get_RemoveMidNodeFlag(self):
		return self._ApplyTypes_(*(3003, 2, (11, 0), (), "RemoveMidNodeFlag", None))
	def _get_RemoveModes(self):
		return self._ApplyTypes_(*(3009, 2, (8, 0), (), "RemoveModes", None))
	def _get_RemoveModesFlag(self):
		return self._ApplyTypes_(*(3008, 2, (11, 0), (), "RemoveModesFlag", None))
	def _get_RemoveZeroValueFlag(self):
		return self._ApplyTypes_(*(3004, 2, (11, 0), (), "RemoveZeroValueFlag", None))
	def _get_ResultRFIFileName(self):
		return self._ApplyTypes_(*(3002, 2, (8, 0), (), "ResultRFIFileName", None))
	def _get_SourceType(self):
		return self._ApplyTypes_(*(3010, 2, (3, 0), (), "SourceType", '{1FBBB3AE-164E-4A0C-B02D-45472F907F09}'))
	def _get_StrainStressShapePrecisionFlag(self):
		return self._ApplyTypes_(*(3007, 2, (11, 0), (), "StrainStressShapePrecisionFlag", None))
	def _get_Type(self):
		return self._ApplyTypes_(*(3006, 2, (3, 0), (), "Type", '{4A7E7C22-6E11-415A-A492-01782B6CCDB0}'))

	def _set_ChangeToExternalPatchFlag(self, value):
		if "ChangeToExternalPatchFlag" in self.__dict__: self.__dict__["ChangeToExternalPatchFlag"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))
	def _set_DATFileName(self, value):
		if "DATFileName" in self.__dict__: self.__dict__["DATFileName"] = value; return
		self._oleobj_.Invoke(*((3012, LCID, 4, 0) + (value,) + ()))
	def _set_OP2FileName(self, value):
		if "OP2FileName" in self.__dict__: self.__dict__["OP2FileName"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_OriginalRFIFileName(self, value):
		if "OriginalRFIFileName" in self.__dict__: self.__dict__["OriginalRFIFileName"] = value; return
		self._oleobj_.Invoke(*((3000, LCID, 4, 0) + (value,) + ()))
	def _set_RFlexBody(self, value):
		if "RFlexBody" in self.__dict__: self.__dict__["RFlexBody"] = value; return
		self._oleobj_.Invoke(*((3011, LCID, 4, 0) + (value,) + ()))
	def _set_RemainExternalNodesFlag(self, value):
		if "RemainExternalNodesFlag" in self.__dict__: self.__dict__["RemainExternalNodesFlag"] = value; return
		self._oleobj_.Invoke(*((3013, LCID, 4, 0) + (value,) + ()))
	def _set_RemainSelectedNodes(self, value):
		if "RemainSelectedNodes" in self.__dict__: self.__dict__["RemainSelectedNodes"] = value; return
		self._oleobj_.Invoke(*((3016, LCID, 4, 0) + (value,) + ()))
	def _set_RemainSelectedNodesFlag(self, value):
		if "RemainSelectedNodesFlag" in self.__dict__: self.__dict__["RemainSelectedNodesFlag"] = value; return
		self._oleobj_.Invoke(*((3015, LCID, 4, 0) + (value,) + ()))
	def _set_RemainUsedNodesFlag(self, value):
		if "RemainUsedNodesFlag" in self.__dict__: self.__dict__["RemainUsedNodesFlag"] = value; return
		self._oleobj_.Invoke(*((3014, LCID, 4, 0) + (value,) + ()))
	def _set_RemoveMidNodeFlag(self, value):
		if "RemoveMidNodeFlag" in self.__dict__: self.__dict__["RemoveMidNodeFlag"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_RemoveModes(self, value):
		if "RemoveModes" in self.__dict__: self.__dict__["RemoveModes"] = value; return
		self._oleobj_.Invoke(*((3009, LCID, 4, 0) + (value,) + ()))
	def _set_RemoveModesFlag(self, value):
		if "RemoveModesFlag" in self.__dict__: self.__dict__["RemoveModesFlag"] = value; return
		self._oleobj_.Invoke(*((3008, LCID, 4, 0) + (value,) + ()))
	def _set_RemoveZeroValueFlag(self, value):
		if "RemoveZeroValueFlag" in self.__dict__: self.__dict__["RemoveZeroValueFlag"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_ResultRFIFileName(self, value):
		if "ResultRFIFileName" in self.__dict__: self.__dict__["ResultRFIFileName"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_SourceType(self, value):
		if "SourceType" in self.__dict__: self.__dict__["SourceType"] = value; return
		self._oleobj_.Invoke(*((3010, LCID, 4, 0) + (value,) + ()))
	def _set_StrainStressShapePrecisionFlag(self, value):
		if "StrainStressShapePrecisionFlag" in self.__dict__: self.__dict__["StrainStressShapePrecisionFlag"] = value; return
		self._oleobj_.Invoke(*((3007, LCID, 4, 0) + (value,) + ()))
	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((3006, LCID, 4, 0) + (value,) + ()))

	ChangeToExternalPatchFlag = property(_get_ChangeToExternalPatchFlag, _set_ChangeToExternalPatchFlag)
	'''
	Change all Patch Info to External Patch Info Flag

	:type: bool
	'''
	DATFileName = property(_get_DATFileName, _set_DATFileName)
	'''
	DAT File Name

	:type: str
	'''
	OP2FileName = property(_get_OP2FileName, _set_OP2FileName)
	'''
	OP2 File Name

	:type: str
	'''
	OriginalRFIFileName = property(_get_OriginalRFIFileName, _set_OriginalRFIFileName)
	'''
	Original RFI File Name

	:type: str
	'''
	RFlexBody = property(_get_RFlexBody, _set_RFlexBody)
	'''
	RFlex Body

	:type: recurdyn.RFlex.IRFlexBody
	'''
	RemainExternalNodesFlag = property(_get_RemainExternalNodesFlag, _set_RemainExternalNodesFlag)
	'''
	Remain External Nodes Flag

	:type: bool
	'''
	RemainSelectedNodes = property(_get_RemainSelectedNodes, _set_RemainSelectedNodes)
	'''
	Remain Selected Nodes

	:type: str
	'''
	RemainSelectedNodesFlag = property(_get_RemainSelectedNodesFlag, _set_RemainSelectedNodesFlag)
	'''
	Remain Selected Nodes Flag

	:type: bool
	'''
	RemainUsedNodesFlag = property(_get_RemainUsedNodesFlag, _set_RemainUsedNodesFlag)
	'''
	Remain Used Nodes Flag

	:type: bool
	'''
	RemoveMidNodeFlag = property(_get_RemoveMidNodeFlag, _set_RemoveMidNodeFlag)
	'''
	Remove Mid-Node Related Information Flag

	:type: bool
	'''
	RemoveModes = property(_get_RemoveModes, _set_RemoveModes)
	'''
	Remove Modes

	:type: str
	'''
	RemoveModesFlag = property(_get_RemoveModesFlag, _set_RemoveModesFlag)
	'''
	Remove Modes Flag

	:type: bool
	'''
	RemoveZeroValueFlag = property(_get_RemoveZeroValueFlag, _set_RemoveZeroValueFlag)
	'''
	Remove Zero-Value for Rotational Mode Shape Flag

	:type: bool
	'''
	ResultRFIFileName = property(_get_ResultRFIFileName, _set_ResultRFIFileName)
	'''
	Optimized RFI File Name

	:type: str
	'''
	SourceType = property(_get_SourceType, _set_SourceType)
	'''
	Source Type

	:type: recurdyn.RFlex.OptimizerSourceType
	'''
	StrainStressShapePrecisionFlag = property(_get_StrainStressShapePrecisionFlag, _set_StrainStressShapePrecisionFlag)
	'''
	Change strain/stress shape precision

	:type: bool
	'''
	Type = property(_get_Type, _set_Type)
	'''
	Type

	:type: recurdyn.RFlex.OptimizerType
	'''

	_prop_map_set_function_ = {
		"_set_ChangeToExternalPatchFlag": _set_ChangeToExternalPatchFlag,
		"_set_DATFileName": _set_DATFileName,
		"_set_OP2FileName": _set_OP2FileName,
		"_set_OriginalRFIFileName": _set_OriginalRFIFileName,
		"_set_RFlexBody": _set_RFlexBody,
		"_set_RemainExternalNodesFlag": _set_RemainExternalNodesFlag,
		"_set_RemainSelectedNodes": _set_RemainSelectedNodes,
		"_set_RemainSelectedNodesFlag": _set_RemainSelectedNodesFlag,
		"_set_RemainUsedNodesFlag": _set_RemainUsedNodesFlag,
		"_set_RemoveMidNodeFlag": _set_RemoveMidNodeFlag,
		"_set_RemoveModes": _set_RemoveModes,
		"_set_RemoveModesFlag": _set_RemoveModesFlag,
		"_set_RemoveZeroValueFlag": _set_RemoveZeroValueFlag,
		"_set_ResultRFIFileName": _set_ResultRFIFileName,
		"_set_SourceType": _set_SourceType,
		"_set_StrainStressShapePrecisionFlag": _set_StrainStressShapePrecisionFlag,
		"_set_Type": _set_Type,
	}
	_prop_map_get_ = {
		"ChangeToExternalPatchFlag": (3005, 2, (11, 0), (), "ChangeToExternalPatchFlag", None),
		"DATFileName": (3012, 2, (8, 0), (), "DATFileName", None),
		"OP2FileName": (3001, 2, (8, 0), (), "OP2FileName", None),
		"OriginalRFIFileName": (3000, 2, (8, 0), (), "OriginalRFIFileName", None),
		"RFlexBody": (3011, 2, (9, 0), (), "RFlexBody", '{5737600D-0E40-4578-9E18-8CBE68916DF8}'),
		"RemainExternalNodesFlag": (3013, 2, (11, 0), (), "RemainExternalNodesFlag", None),
		"RemainSelectedNodes": (3016, 2, (8, 0), (), "RemainSelectedNodes", None),
		"RemainSelectedNodesFlag": (3015, 2, (11, 0), (), "RemainSelectedNodesFlag", None),
		"RemainUsedNodesFlag": (3014, 2, (11, 0), (), "RemainUsedNodesFlag", None),
		"RemoveMidNodeFlag": (3003, 2, (11, 0), (), "RemoveMidNodeFlag", None),
		"RemoveModes": (3009, 2, (8, 0), (), "RemoveModes", None),
		"RemoveModesFlag": (3008, 2, (11, 0), (), "RemoveModesFlag", None),
		"RemoveZeroValueFlag": (3004, 2, (11, 0), (), "RemoveZeroValueFlag", None),
		"ResultRFIFileName": (3002, 2, (8, 0), (), "ResultRFIFileName", None),
		"SourceType": (3010, 2, (3, 0), (), "SourceType", '{1FBBB3AE-164E-4A0C-B02D-45472F907F09}'),
		"StrainStressShapePrecisionFlag": (3007, 2, (11, 0), (), "StrainStressShapePrecisionFlag", None),
		"Type": (3006, 2, (3, 0), (), "Type", '{4A7E7C22-6E11-415A-A492-01782B6CCDB0}'),
	}
	_prop_map_put_ = {
		"ChangeToExternalPatchFlag": ((3005, LCID, 4, 0),()),
		"DATFileName": ((3012, LCID, 4, 0),()),
		"OP2FileName": ((3001, LCID, 4, 0),()),
		"OriginalRFIFileName": ((3000, LCID, 4, 0),()),
		"RFlexBody": ((3011, LCID, 4, 0),()),
		"RemainExternalNodesFlag": ((3013, LCID, 4, 0),()),
		"RemainSelectedNodes": ((3016, LCID, 4, 0),()),
		"RemainSelectedNodesFlag": ((3015, LCID, 4, 0),()),
		"RemainUsedNodesFlag": ((3014, LCID, 4, 0),()),
		"RemoveMidNodeFlag": ((3003, LCID, 4, 0),()),
		"RemoveModes": ((3009, LCID, 4, 0),()),
		"RemoveModesFlag": ((3008, LCID, 4, 0),()),
		"RemoveZeroValueFlag": ((3004, LCID, 4, 0),()),
		"ResultRFIFileName": ((3002, LCID, 4, 0),()),
		"SourceType": ((3010, LCID, 4, 0),()),
		"StrainStressShapePrecisionFlag": ((3007, LCID, 4, 0),()),
		"Type": ((3006, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexRequest(DispatchBaseClass):
	'''Request RFlex'''
	CLSID = IID('{E43E421D-2821-44FF-B7FA-7CDF332A240F}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetPlotNameList(self):
		'''
		Get Plottable Name List
		
		:rtype: list[str]
		'''
		return self._ApplyTypes_(3006, 1, (8200, 0), (), 'GetPlotNameList', None,)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_ActionNodeID(self):
		return self._ApplyTypes_(*(3002, 2, (19, 0), (), "ActionNodeID", None))
	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_BaseMarker(self):
		return self._ApplyTypes_(*(3003, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_BeamRecoveryType(self):
		return self._ApplyTypes_(*(3008, 2, (3, 0), (), "BeamRecoveryType", '{818B045A-34AC-4EEE-B440-3B8FEF411941}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
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
	def _get_RefMarker(self):
		return self._ApplyTypes_(*(3004, 2, (9, 0), (), "RefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_ShellRecoveryType(self):
		return self._ApplyTypes_(*(3007, 2, (3, 0), (), "ShellRecoveryType", '{A980771B-865C-4EC4-AFF5-142BBB99BCAE}'))
	def _get_Type(self):
		return self._ApplyTypes_(*(3001, 2, (3, 0), (), "Type", '{02D8BDB5-7A43-482E-AB97-2C3307E32EB1}'))
	def _get_Use4thMarkerFlag(self):
		return self._ApplyTypes_(*(3005, 2, (11, 0), (), "Use4thMarkerFlag", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ActionNodeID(self, value):
		if "ActionNodeID" in self.__dict__: self.__dict__["ActionNodeID"] = value; return
		self._oleobj_.Invoke(*((3002, LCID, 4, 0) + (value,) + ()))
	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((152, LCID, 4, 0) + (value,) + ()))
	def _set_BaseMarker(self, value):
		if "BaseMarker" in self.__dict__: self.__dict__["BaseMarker"] = value; return
		self._oleobj_.Invoke(*((3003, LCID, 4, 0) + (value,) + ()))
	def _set_BeamRecoveryType(self, value):
		if "BeamRecoveryType" in self.__dict__: self.__dict__["BeamRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3008, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_RefMarker(self, value):
		if "RefMarker" in self.__dict__: self.__dict__["RefMarker"] = value; return
		self._oleobj_.Invoke(*((3004, LCID, 4, 0) + (value,) + ()))
	def _set_ShellRecoveryType(self, value):
		if "ShellRecoveryType" in self.__dict__: self.__dict__["ShellRecoveryType"] = value; return
		self._oleobj_.Invoke(*((3007, LCID, 4, 0) + (value,) + ()))
	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((3001, LCID, 4, 0) + (value,) + ()))
	def _set_Use4thMarkerFlag(self, value):
		if "Use4thMarkerFlag" in self.__dict__: self.__dict__["Use4thMarkerFlag"] = value; return
		self._oleobj_.Invoke(*((3005, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ActionNodeID = property(_get_ActionNodeID, _set_ActionNodeID)
	'''
	Action node

	:type: int
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
	BeamRecoveryType = property(_get_BeamRecoveryType, _set_BeamRecoveryType)
	'''
	Beam Recovery type

	:type: recurdyn.RFlex.RFlexRequestBeamRecoveryType
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
	RefMarker = property(_get_RefMarker, _set_RefMarker)
	'''
	Reference marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	ShellRecoveryType = property(_get_ShellRecoveryType, _set_ShellRecoveryType)
	'''
	Shell Recovery type

	:type: recurdyn.RFlex.RFlexRequestShellRecoveryType
	'''
	Type = property(_get_Type, _set_Type)
	'''
	RFlex request type

	:type: recurdyn.RFlex.RFlexRequestType
	'''
	Use4thMarkerFlag = property(_get_Use4thMarkerFlag, _set_Use4thMarkerFlag)
	'''
	Use 4th Marker Flag

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ActionNodeID": _set_ActionNodeID,
		"_set_Active": _set_Active,
		"_set_BaseMarker": _set_BaseMarker,
		"_set_BeamRecoveryType": _set_BeamRecoveryType,
		"_set_Comment": _set_Comment,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_RefMarker": _set_RefMarker,
		"_set_ShellRecoveryType": _set_ShellRecoveryType,
		"_set_Type": _set_Type,
		"_set_Use4thMarkerFlag": _set_Use4thMarkerFlag,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ActionNodeID": (3002, 2, (19, 0), (), "ActionNodeID", None),
		"Active": (152, 2, (11, 0), (), "Active", None),
		"BaseMarker": (3003, 2, (9, 0), (), "BaseMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"BeamRecoveryType": (3008, 2, (3, 0), (), "BeamRecoveryType", '{818B045A-34AC-4EEE-B440-3B8FEF411941}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RefMarker": (3004, 2, (9, 0), (), "RefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"ShellRecoveryType": (3007, 2, (3, 0), (), "ShellRecoveryType", '{A980771B-865C-4EC4-AFF5-142BBB99BCAE}'),
		"Type": (3001, 2, (3, 0), (), "Type", '{02D8BDB5-7A43-482E-AB97-2C3307E32EB1}'),
		"Use4thMarkerFlag": (3005, 2, (11, 0), (), "Use4thMarkerFlag", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ActionNodeID": ((3002, LCID, 4, 0),()),
		"Active": ((152, LCID, 4, 0),()),
		"BaseMarker": ((3003, LCID, 4, 0),()),
		"BeamRecoveryType": ((3008, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"RefMarker": ((3004, LCID, 4, 0),()),
		"ShellRecoveryType": ((3007, LCID, 4, 0),()),
		"Type": ((3001, LCID, 4, 0),()),
		"Use4thMarkerFlag": ((3005, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IRFlexRequestCollection(DispatchBaseClass):
	'''IRFlexRequestCollection'''
	CLSID = IID('{A8F96B43-230B-49EB-B315-868F472669DF}')
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
		:rtype: recurdyn.RFlex.IRFlexRequest
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E43E421D-2821-44FF-B7FA-7CDF332A240F}')
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
		:rtype: recurdyn.RFlex.IRFlexRequest
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E43E421D-2821-44FF-B7FA-7CDF332A240F}')
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
		return win32com.client.util.Iterator(ob, '{E43E421D-2821-44FF-B7FA-7CDF332A240F}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{E43E421D-2821-44FF-B7FA-7CDF332A240F}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IRFlexToolFunction(DispatchBaseClass):
	'''RFlex Tool Function'''
	CLSID = IID('{D2DAC4E9-E5EC-4C27-94B2-0A0CFFB24767}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def GetNodeIDsFromMidNode(self, pVal, val):
		'''
		Get Node IDs From Mid-Node
		
		:param pVal: IRFlexBody
		:param val: int
		:rtype: list[int]
		'''
		return self._ApplyTypes_(3001, 1, (8195, 0), ((9, 1), (3, 1)), 'GetNodeIDsFromMidNode', None,pVal
			, val)


	def SelectMultiComponentsUsingGUI(self, varBody, Type):
		'''
		Select multi IDs by using GUI
		
		:param varBody: IRFlexBody
		:param Type: IDType
		:rtype: list[int]
		'''
		return self._ApplyTypes_(3002, 1, (8195, 0), ((9, 1), (3, 1)), 'SelectMultiComponentsUsingGUI', None,varBody
			, Type)


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

class IRFlexToolkit(DispatchBaseClass):
	'''RFlex Toolkit'''
	CLSID = IID('{7AAF53D9-9777-4B5D-827C-62A822442B49}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateGroupBeam(self, strName, pMultiPoints, dNodeThickness, uiMeshSegment):
		'''
		Use general CreateGroupBeam function : obsolete function
		
		:param strName: str
		:param pMultiPoints: list[object]
		:param dNodeThickness: float
		:param uiMeshSegment: int
		:rtype: recurdyn.RFlex.IRFlexGroupBeam
		'''
		_pMultiPoints_type = True if pMultiPoints and isinstance(pMultiPoints[0], win32com.client.VARIANT) else False
		if not _pMultiPoints_type:
			pMultiPoints = [win32com.client.VARIANT(12, _data) for _data in pMultiPoints]

		ret = self._oleobj_.InvokeTypes(3065, LCID, 1, (9, 0), ((8, 1), (8204, 1), (5, 1), (19, 1)),strName
			, pMultiPoints, dNodeThickness, uiMeshSegment)

		if not _pMultiPoints_type:
			pMultiPoints = [_data.value for _data in pMultiPoints]

		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupBeam', '{3C055C79-373C-4034-A146-E1E5D485D36E}')
		return ret

	def CreateModalForce(self, strName, pIRFlexBody, pVal):
		'''
		Create a modal force
		
		:param strName: str
		:param pIRFlexBody: IRFlexBody
		:param pVal: IUserSubroutine
		:rtype: recurdyn.RFlex.IRFlexForceModalForce
		'''
		ret = self._oleobj_.InvokeTypes(3078, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1)),strName
			, pIRFlexBody, pVal)
		if ret is not None:
			ret = Dispatch(ret, 'CreateModalForce', '{D4583F05-0EAC-434A-BC8E-C785137C783D}')
		return ret

	def CreateModalForceWithNodeSet(self, strName, pIRFlexBody, pINodeSet, pVal):
		'''
		Create a modal force With NodeSet
		
		:param strName: str
		:param pIRFlexBody: IRFlexBody
		:param pINodeSet: IRFlexNodeSet
		:param pVal: IUserSubroutine
		:rtype: recurdyn.RFlex.IRFlexForceModalForce
		'''
		ret = self._oleobj_.InvokeTypes(3084, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
			, pIRFlexBody, pINodeSet, pVal)
		if ret is not None:
			ret = Dispatch(ret, 'CreateModalForceWithNodeSet', '{D4583F05-0EAC-434A-BC8E-C785137C783D}')
		return ret

	def CreateModalPreload(self, strName, pVal):
		'''
		Create a modal preload
		
		:param strName: str
		:param pVal: IRFlexBody
		:rtype: recurdyn.RFlex.IRFlexForceModalPreload
		'''
		ret = self._oleobj_.InvokeTypes(3077, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pVal)
		if ret is not None:
			ret = Dispatch(ret, 'CreateModalPreload', '{46F35838-9402-4A28-8FE4-00FE959E31DF}')
		return ret

	def CreateModalPressureLoad(self, strName, pPatchSet):
		'''
		Create a Modal Pressure Load
		
		:param strName: str
		:param pPatchSet: IRFlexPatchSet
		:rtype: recurdyn.RFlex.IRFlexLoadPressureModal
		'''
		ret = self._oleobj_.InvokeTypes(3093, LCID, 1, (9, 0), ((8, 1), (9, 1)),strName
			, pPatchSet)
		if ret is not None:
			ret = Dispatch(ret, 'CreateModalPressureLoad', '{FB11F962-2D23-4DD7-A6DF-0C47507310E0}')
		return ret

	def CreateRFlexRequest(self, strName, enType, sActionNodeID, pBaseMarker, pRefMarker):
		'''
		Creates a request RFlex
		
		:param strName: str
		:param enType: RFlexRequestType
		:param sActionNodeID: str
		:param pBaseMarker: IMarker
		:param pRefMarker: IMarker
		:rtype: recurdyn.RFlex.IRFlexRequest
		'''
		ret = self._oleobj_.InvokeTypes(3071, LCID, 1, (9, 0), ((8, 1), (3, 1), (8, 1), (9, 1), (9, 1)),strName
			, enType, sActionNodeID, pBaseMarker, pRefMarker)
		if ret is not None:
			ret = Dispatch(ret, 'CreateRFlexRequest', '{E43E421D-2821-44FF-B7FA-7CDF332A240F}')
		return ret

	def CreateRfiFileFromANSYS(self, strRfiFileName, pANSYSOption, pCommonOption, UnitFactor):
		'''
		Create RFI (RecurDyn Flexible Input) file from ANSYS result
		
		:param strRfiFileName: str
		:param pANSYSOption: IRFlexInterfaceANSYSOption
		:param pCommonOption: IRFlexInterfaceCommonOption
		:param UnitFactor: IUnit
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(3054, LCID, 1, (11, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strRfiFileName
			, pANSYSOption, pCommonOption, UnitFactor)


	def CreateRfiFileFromIDEAS(self, strRfiFileName, strIDEASFileName, pCommonOption, UnitFactor):
		'''
		Create RFI (RecurDyn Flexible Input) file from IDEAS result
		
		:param strRfiFileName: str
		:param strIDEASFileName: str
		:param pCommonOption: IRFlexInterfaceCommonOption
		:param UnitFactor: IUnit
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(3055, LCID, 1, (11, 0), ((8, 1), (8, 1), (9, 1), (9, 1)),strRfiFileName
			, strIDEASFileName, pCommonOption, UnitFactor)


	def CreateRfiFileFromIDEASWithOption(self, strRfiFileName, strIDEASFileName, pIdeasOption, pCommonOption, UnitFactor):
		'''
		Create RFI file from IDEAS result
		
		:param strRfiFileName: str
		:param strIDEASFileName: str
		:param pIdeasOption: IRFlexInterfaceIdeasOption
		:param pCommonOption: IRFlexInterfaceCommonOption
		:param UnitFactor: IUnit
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(3089, LCID, 1, (11, 0), ((8, 1), (8, 1), (9, 1), (9, 1), (9, 1)),strRfiFileName
			, strIDEASFileName, pIdeasOption, pCommonOption, UnitFactor)


	def CreateRfiFileFromNASTRAN(self, strRfiFileName, strNASTRANFileName, pCommonOption, UnitFactor):
		'''
		Create RFI (RecurDyn Flexible Input) file from NASTRAN result
		
		:param strRfiFileName: str
		:param strNASTRANFileName: str
		:param pCommonOption: IRFlexInterfaceCommonOption
		:param UnitFactor: IUnit
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(3056, LCID, 1, (11, 0), ((8, 1), (8, 1), (9, 1), (9, 1)),strRfiFileName
			, strNASTRANFileName, pCommonOption, UnitFactor)


	def CreateRfiFileFromNASTRANOP2(self, strRfiFileName, strNASTRANFileName, pNastranOP2Option, pCommonOption, UnitFactor):
		'''
		Create RFI (RecurDyn Flexible Input) file from NASTRAN OP2 result
		
		:param strRfiFileName: str
		:param strNASTRANFileName: str
		:param pNastranOP2Option: IRFlexInterfaceNastranOP2Option
		:param pCommonOption: IRFlexInterfaceCommonOption
		:param UnitFactor: IUnit
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(3066, LCID, 1, (11, 0), ((8, 1), (8, 1), (9, 1), (9, 1), (9, 1)),strRfiFileName
			, strNASTRANFileName, pNastranOP2Option, pCommonOption, UnitFactor)


	def ExportDurabilityInterface(self, pRFlexBody, pExportDurabilityInterfaceOption):
		'''
		Export durability Interface
		
		:param pRFlexBody: IRFlexBody
		:param pExportDurabilityInterfaceOption: IRFlexExportDurabilityInterfaceOption
		'''
		return self._oleobj_.InvokeTypes(3068, LCID, 1, (24, 0), ((9, 1), (9, 1)),pRFlexBody
			, pExportDurabilityInterfaceOption)


	def ExportDurabilityInterfaceWithVersion(self, pRFlexBody, pExportDurabilityInterfaceOption, vertionType):
		'''
		Export durability Interface with Version
		
		:param pRFlexBody: IRFlexBody
		:param pExportDurabilityInterfaceOption: IRFlexExportDurabilityInterfaceOption
		:param vertionType: FEMFATVersionType
		'''
		return self._oleobj_.InvokeTypes(3095, LCID, 1, (24, 0), ((9, 1), (9, 1), (3, 1)),pRFlexBody
			, pExportDurabilityInterfaceOption, vertionType)


	def ExportMDFFile(self, pRFlexBody, pExportMDFFileOption):
		'''
		Export MDF File
		
		:param pRFlexBody: IRFlexBody
		:param pExportMDFFileOption: IRFlexExportMDFFileOption
		'''
		return self._oleobj_.InvokeTypes(3069, LCID, 1, (24, 0), ((9, 1), (9, 1)),pRFlexBody
			, pExportMDFFileOption)


	def ExportModalLoadCase(self, ModalLoadCaseExportFile):
		'''
		Export Modal Load Case
		
		:param ModalLoadCaseExportFile: str
		'''
		return self._oleobj_.InvokeTypes(3074, LCID, 1, (24, 0), ((8, 1),),ModalLoadCaseExportFile
			)


	def ExportModeShape(self, strRfiFileName, FESoftwareType, strExportFileName):
		'''
		Export Mode Shape
		
		:param strRfiFileName: str
		:param FESoftwareType: FESoftwareType
		:param strExportFileName: str
		'''
		return self._oleobj_.InvokeTypes(3062, LCID, 1, (24, 0), ((8, 1), (3, 1), (8, 1)),strRfiFileName
			, FESoftwareType, strExportFileName)


	def GenerateStrainStressShape(self, strRfiFileName, bGenerateStrainShape, bGenerateStressShape):
		'''
		Generate Strain Stress Shape
		
		:param strRfiFileName: str
		:param bGenerateStrainShape: bool
		:param bGenerateStressShape: bool
		'''
		return self._oleobj_.InvokeTypes(3064, LCID, 1, (24, 0), ((8, 1), (11, 1), (11, 1)),strRfiFileName
			, bGenerateStrainShape, bGenerateStressShape)


	def GenerateStrainStressShapeWithShellRecoveryType(self, strRfiFileName, bGenerateStrainShape, bGenerateStressShape, Type):
		'''
		Generate Strain Stress Shape with Shell Recovery Type
		
		:param strRfiFileName: str
		:param bGenerateStrainShape: bool
		:param bGenerateStressShape: bool
		:param Type: ShellRecoveryType
		'''
		return self._oleobj_.InvokeTypes(3085, LCID, 1, (24, 0), ((8, 1), (11, 1), (11, 1), (3, 1)),strRfiFileName
			, bGenerateStrainShape, bGenerateStressShape, Type)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def ImportBody(self, strName, pRefFrame, strRfiFileName, pImportOption):
		'''
		Import RFlexBody with predefined option
		
		:param strName: str
		:param pRefFrame: IReferenceFrame
		:param strRfiFileName: str
		:param pImportOption: IRFlexBodyImportOption
		:rtype: recurdyn.RFlex.IRFlexBody
		'''
		ret = self._oleobj_.InvokeTypes(3060, LCID, 1, (9, 0), ((8, 1), (9, 1), (8, 1), (9, 1)),strName
			, pRefFrame, strRfiFileName, pImportOption)
		if ret is not None:
			ret = Dispatch(ret, 'ImportBody', '{5737600D-0E40-4578-9E18-8CBE68916DF8}')
		return ret

	def ImportModalLoadCase(self, RFlexBody, ModalLoadCaseImportFile):
		'''
		Import Modal Load Case
		
		:param RFlexBody: IRFlexBody
		:param ModalLoadCaseImportFile: str
		'''
		return self._oleobj_.InvokeTypes(3073, LCID, 1, (24, 0), ((9, 1), (8, 1)),RFlexBody
			, ModalLoadCaseImportFile)


	def ImportStrainStressShape(self, strRfiFileName, FESoftwareType, strFEResultFileName):
		'''
		Import Strain Stress Shape
		
		:param strRfiFileName: str
		:param FESoftwareType: FESoftwareType
		:param strFEResultFileName: str
		'''
		return self._oleobj_.InvokeTypes(3063, LCID, 1, (24, 0), ((8, 1), (3, 1), (8, 1)),strRfiFileName
			, FESoftwareType, strFEResultFileName)


	def ModifyRfiFileFromANSYS(self, strRfiFileName, pExtraModeOption):
		'''
		Modify RFI (RecurDyn Flexible Input) file from ANSYS result
		
		:param strRfiFileName: str
		:param pExtraModeOption: IRFlexInterfaceExtraModeOption
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(3057, LCID, 1, (11, 0), ((8, 1), (9, 1)),strRfiFileName
			, pExtraModeOption)


	def ModifyRfiFileFromNASTRAN(self, strRfiFileName, pExtraModeOption):
		'''
		Modify RFI (RecurDyn Flexible Input) file from NASTRAN result
		
		:param strRfiFileName: str
		:param pExtraModeOption: IRFlexInterfaceExtraModeOption
		:rtype: bool
		'''
		return self._oleobj_.InvokeTypes(3058, LCID, 1, (11, 0), ((8, 1), (9, 1)),strRfiFileName
			, pExtraModeOption)


	def OptimizeRFIFile(self, pRFIOptimizerOption):
		'''
		Optimize RFI (RecurDyn Flexible Input) file
		
		:param pRFIOptimizerOption: IRFlexRFIOptimizerOption
		'''
		return self._oleobj_.InvokeTypes(3067, LCID, 1, (24, 0), ((9, 1),),pRFIOptimizerOption
			)


	def SwapBody(self, strName, TargetBody, strRfiFileName, pImportOption):
		'''
		Swap Existing Body for RFlexBody
		
		:param strName: str
		:param TargetBody: IBody
		:param strRfiFileName: str
		:param pImportOption: IRFlexBodyImportOption
		:rtype: recurdyn.RFlex.IRFlexBody
		'''
		ret = self._oleobj_.InvokeTypes(3061, LCID, 1, (9, 0), ((8, 1), (9, 1), (8, 1), (9, 1)),strName
			, TargetBody, strRfiFileName, pImportOption)
		if ret is not None:
			ret = Dispatch(ret, 'SwapBody', '{5737600D-0E40-4578-9E18-8CBE68916DF8}')
		return ret

	def SwapBodyGeneral(self, strName, TargetBody, strRfiFileName, pImportOption):
		'''
		Swap Existing Body for RFlexBody
		
		:param strName: str
		:param TargetBody: IGeneric
		:param strRfiFileName: str
		:param pImportOption: IRFlexBodyImportOption
		:rtype: recurdyn.RFlex.IRFlexBody
		'''
		ret = self._oleobj_.InvokeTypes(3092, LCID, 1, (9, 0), ((8, 1), (9, 1), (8, 1), (9, 1)),strName
			, TargetBody, strRfiFileName, pImportOption)
		if ret is not None:
			ret = Dispatch(ret, 'SwapBodyGeneral', '{5737600D-0E40-4578-9E18-8CBE68916DF8}')
		return ret

	def SwapBodyGeneralRefFrame(self, strName, TargetBody, pRefFrame, strRfiFileName, pImportOption):
		'''
		Swap Existing Body for RFlexBody with Reference Frame
		
		:param strName: str
		:param TargetBody: IGeneric
		:param pRefFrame: IReferenceFrame
		:param strRfiFileName: str
		:param pImportOption: IRFlexBodyImportOption
		:rtype: recurdyn.RFlex.IRFlexBody
		'''
		ret = self._oleobj_.InvokeTypes(3097, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (8, 1), (9, 1)),strName
			, TargetBody, pRefFrame, strRfiFileName, pImportOption)
		if ret is not None:
			ret = Dispatch(ret, 'SwapBodyGeneralRefFrame', '{5737600D-0E40-4578-9E18-8CBE68916DF8}')
		return ret

	def TranslateRFIFile(self, RFIFileName, OutputFileName):
		'''
		Translate RFI File
		
		:param RFIFileName: str
		:param OutputFileName: str
		'''
		return self._oleobj_.InvokeTypes(3098, LCID, 1, (24, 0), ((8, 1), (8, 1)),RFIFileName
			, OutputFileName)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Contour(self):
		return self._ApplyTypes_(*(3083, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'))
	def _get_DurabilityInterfaceOption(self):
		return self._ApplyTypes_(*(3081, 2, (9, 0), (), "DurabilityInterfaceOption", '{EB3A9E9B-54A9-440F-A594-294F547AA27A}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(3050, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ImportBodyOption(self):
		return self._ApplyTypes_(*(3059, 2, (9, 0), (), "ImportBodyOption", '{8BE11A36-210D-41C5-AB9D-229134DCCA7E}'))
	def _get_InterfaceANSYSOption(self):
		return self._ApplyTypes_(*(3051, 2, (9, 0), (), "InterfaceANSYSOption", '{F1C4FF92-BC23-4F5D-AA37-02D4085B2C73}'))
	def _get_InterfaceCommonOption(self):
		return self._ApplyTypes_(*(3052, 2, (9, 0), (), "InterfaceCommonOption", '{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}'))
	def _get_InterfaceExtraModeOption(self):
		return self._ApplyTypes_(*(3053, 2, (9, 0), (), "InterfaceExtraModeOption", '{F1C4FF92-BC23-4F5D-AA37-02D4085B2C76}'))
	def _get_InterfaceIdeasOption(self):
		return self._ApplyTypes_(*(3088, 2, (9, 0), (), "InterfaceIdeasOption", '{6DB248B8-8ACE-49F0-9B06-5065FB9AE8B0}'))
	def _get_InterfaceNastranOP2Option(self):
		return self._ApplyTypes_(*(3080, 2, (9, 0), (), "InterfaceNastranOP2Option", '{3D4D50F5-2D1A-4618-B956-072A3EA9DD8A}'))
	def _get_MDFOption(self):
		return self._ApplyTypes_(*(3082, 2, (9, 0), (), "MDFOption", '{C36C3EC0-A03A-40F1-A502-8EB259B56AFB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_OutputFileGenerator(self):
		return self._ApplyTypes_(*(3087, 2, (9, 0), (), "OutputFileGenerator", '{6ED5F207-C518-4800-BA75-7990D637BAB5}'))
	def _get_OutputFileRegenerator(self):
		return self._ApplyTypes_(*(3094, 2, (9, 0), (), "OutputFileRegenerator", '{4E476724-E71A-4106-A906-531EBAC1F17A}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RFIOptimizerOption(self):
		return self._ApplyTypes_(*(3079, 2, (9, 0), (), "RFIOptimizerOption", '{7CA7CF6E-47A2-417F-8E24-056FB7F2359E}'))
	def _get_RFlexBodyCollection(self):
		return self._ApplyTypes_(*(3070, 2, (9, 0), (), "RFlexBodyCollection", '{BF6E3DD3-F1E6-4FE4-B15F-4BAE1BFCBF48}'))
	def _get_RFlexForceCollection(self):
		return self._ApplyTypes_(*(3075, 2, (9, 0), (), "RFlexForceCollection", '{8C387B89-CD63-48E0-B37D-CCF014A3D879}'))
	def _get_RFlexModalLoadCaseCollection(self):
		return self._ApplyTypes_(*(3076, 2, (9, 0), (), "RFlexModalLoadCaseCollection", '{B42BB386-EA95-4AE6-9A24-C74CB5027EB2}'))
	def _get_RFlexRequestCollection(self):
		return self._ApplyTypes_(*(3072, 2, (9, 0), (), "RFlexRequestCollection", '{A8F96B43-230B-49EB-B315-868F472669DF}'))
	def _get_ToolFunction(self):
		return self._ApplyTypes_(*(3091, 2, (9, 0), (), "ToolFunction", '{D2DAC4E9-E5EC-4C27-94B2-0A0CFFB24767}'))
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

	:type: recurdyn.Flexible.IContour
	'''
	DurabilityInterfaceOption = property(_get_DurabilityInterfaceOption, None)
	'''
	Get Durability Intreface Option

	:type: recurdyn.RFlex.IRFlexExportDurabilityInterfaceOption
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
	ImportBodyOption = property(_get_ImportBodyOption, None)
	'''
	RFlexBody import option

	:type: recurdyn.RFlex.IRFlexBodyImportOption
	'''
	InterfaceANSYSOption = property(_get_InterfaceANSYSOption, None)
	'''
	Get InterfaceANSYSOption

	:type: recurdyn.RFlex.IRFlexInterfaceANSYSOption
	'''
	InterfaceCommonOption = property(_get_InterfaceCommonOption, None)
	'''
	Get InterfaceCommonOption

	:type: recurdyn.RFlex.IRFlexInterfaceCommonOption
	'''
	InterfaceExtraModeOption = property(_get_InterfaceExtraModeOption, None)
	'''
	Get InterfaceExtraModeOption

	:type: recurdyn.RFlex.IRFlexInterfaceExtraModeOption
	'''
	InterfaceIdeasOption = property(_get_InterfaceIdeasOption, None)
	'''
	Get Interface Ideas Option

	:type: recurdyn.RFlex.IRFlexInterfaceIdeasOption
	'''
	InterfaceNastranOP2Option = property(_get_InterfaceNastranOP2Option, None)
	'''
	Get Interface Nastran Option

	:type: recurdyn.RFlex.IRFlexInterfaceNastranOP2Option
	'''
	MDFOption = property(_get_MDFOption, None)
	'''
	Get Export MDF File Option

	:type: recurdyn.RFlex.IRFlexExportMDFFileOption
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	OutputFileGenerator = property(_get_OutputFileGenerator, None)
	'''
	Get output file generator

	:type: recurdyn.RFlex.IRFlexOutputFileGenerator
	'''
	OutputFileRegenerator = property(_get_OutputFileRegenerator, None)
	'''
	Get output file regenerator

	:type: recurdyn.RFlex.IRFlexOutputFileRegenerator
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
	RFIOptimizerOption = property(_get_RFIOptimizerOption, None)
	'''
	Get RFI Optimizer Option

	:type: recurdyn.RFlex.IRFlexRFIOptimizerOption
	'''
	RFlexBodyCollection = property(_get_RFlexBodyCollection, None)
	'''
	Contains RFlexBody

	:type: recurdyn.RFlex.IRFlexBodyCollection
	'''
	RFlexForceCollection = property(_get_RFlexForceCollection, None)
	'''
	Contains RFlex Force

	:type: recurdyn.RFlex.IRFlexForceCollection
	'''
	RFlexModalLoadCaseCollection = property(_get_RFlexModalLoadCaseCollection, None)
	'''
	Contains Modal Load Case

	:type: recurdyn.RFlex.IRFlexModalLoadCaseCollection
	'''
	RFlexRequestCollection = property(_get_RFlexRequestCollection, None)
	'''
	Contains RFlexRequest

	:type: recurdyn.RFlex.IRFlexRequestCollection
	'''
	ToolFunction = property(_get_ToolFunction, None)
	'''
	RFlexBody Tool Function

	:type: recurdyn.RFlex.IRFlexToolFunction
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
		"Contour": (3083, 2, (9, 0), (), "Contour", '{BDF4F979-28B7-48D2-BF06-9C59B70D467B}'),
		"DurabilityInterfaceOption": (3081, 2, (9, 0), (), "DurabilityInterfaceOption", '{EB3A9E9B-54A9-440F-A594-294F547AA27A}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralSubSystem": (3050, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ImportBodyOption": (3059, 2, (9, 0), (), "ImportBodyOption", '{8BE11A36-210D-41C5-AB9D-229134DCCA7E}'),
		"InterfaceANSYSOption": (3051, 2, (9, 0), (), "InterfaceANSYSOption", '{F1C4FF92-BC23-4F5D-AA37-02D4085B2C73}'),
		"InterfaceCommonOption": (3052, 2, (9, 0), (), "InterfaceCommonOption", '{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}'),
		"InterfaceExtraModeOption": (3053, 2, (9, 0), (), "InterfaceExtraModeOption", '{F1C4FF92-BC23-4F5D-AA37-02D4085B2C76}'),
		"InterfaceIdeasOption": (3088, 2, (9, 0), (), "InterfaceIdeasOption", '{6DB248B8-8ACE-49F0-9B06-5065FB9AE8B0}'),
		"InterfaceNastranOP2Option": (3080, 2, (9, 0), (), "InterfaceNastranOP2Option", '{3D4D50F5-2D1A-4618-B956-072A3EA9DD8A}'),
		"MDFOption": (3082, 2, (9, 0), (), "MDFOption", '{C36C3EC0-A03A-40F1-A502-8EB259B56AFB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"OutputFileGenerator": (3087, 2, (9, 0), (), "OutputFileGenerator", '{6ED5F207-C518-4800-BA75-7990D637BAB5}'),
		"OutputFileRegenerator": (3094, 2, (9, 0), (), "OutputFileRegenerator", '{4E476724-E71A-4106-A906-531EBAC1F17A}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RFIOptimizerOption": (3079, 2, (9, 0), (), "RFIOptimizerOption", '{7CA7CF6E-47A2-417F-8E24-056FB7F2359E}'),
		"RFlexBodyCollection": (3070, 2, (9, 0), (), "RFlexBodyCollection", '{BF6E3DD3-F1E6-4FE4-B15F-4BAE1BFCBF48}'),
		"RFlexForceCollection": (3075, 2, (9, 0), (), "RFlexForceCollection", '{8C387B89-CD63-48E0-B37D-CCF014A3D879}'),
		"RFlexModalLoadCaseCollection": (3076, 2, (9, 0), (), "RFlexModalLoadCaseCollection", '{B42BB386-EA95-4AE6-9A24-C74CB5027EB2}'),
		"RFlexRequestCollection": (3072, 2, (9, 0), (), "RFlexRequestCollection", '{A8F96B43-230B-49EB-B315-868F472669DF}'),
		"ToolFunction": (3091, 2, (9, 0), (), "ToolFunction", '{D2DAC4E9-E5EC-4C27-94B2-0A0CFFB24767}'),
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

IRFlexAnimationDataScaling_vtables_dispatch_ = 1
IRFlexAnimationDataScaling_vtables_ = [
	(( 'AnimationScalingRefMarker' , 'pMarker' , ), 3001, (3001, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AnimationScalingRefMarker' , 'pMarker' , ), 3001, (3001, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SetAnimationScalingModeShapeFactor' , 'dFactor' , ), 3002, (3002, (), [ (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GetAnimationScalingModeShapeFactor' , 'pFactor' , ), 3003, (3003, (), [ (16389, 2, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'AnimationScalingType' , 'pVal' , ), 3004, (3004, (), [ (3, 1, None, "IID('{2480C090-3421-4383-AE29-3915E4A37E7D}')") , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'AnimationScalingType' , 'pVal' , ), 3004, (3004, (), [ (16387, 10, None, "IID('{2480C090-3421-4383-AE29-3915E4A37E7D}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceNode' , 'ppVal' , ), 3005, (3005, (), [ (9, 1, None, "IID('{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ReferenceNode' , 'ppVal' , ), 3005, (3005, (), [ (16393, 10, None, "IID('{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IRFlexBody_vtables_dispatch_ = 1
IRFlexBody_vtables_ = [
	(( 'RefFrame' , 'pVal' , ), 3001, (3001, (), [ (16393, 10, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'pVal' , ), 3002, (3002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'pVal' , ), 3003, (3003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'pVal' , ), 3004, (3004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'pVal' , ), 3005, (3005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Ixy' , 'pVal' , ), 3006, (3006, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Iyz' , 'pVal' , ), 3007, (3007, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Izx' , 'pVal' , ), 3008, (3008, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'InitialTranslationalVelocityX' , 'pVal' , ), 3009, (3009, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'InitialTranslationalVelocityY' , 'pVal' , ), 3010, (3010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'InitialTranslationalVelocityZ' , 'pVal' , ), 3011, (3011, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialTranslationalVelocityX' , 'pVal' , ), 3012, (3012, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialTranslationalVelocityX' , 'pVal' , ), 3012, (3012, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialTranslationalVelocityY' , 'pVal' , ), 3013, (3013, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialTranslationalVelocityY' , 'pVal' , ), 3013, (3013, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialTranslationalVelocityZ' , 'pVal' , ), 3014, (3014, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialTranslationalVelocityZ' , 'pVal' , ), 3014, (3014, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'InitialRotationalVelocityX' , 'pVal' , ), 3015, (3015, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'InitialRotationalVelocityY' , 'pVal' , ), 3016, (3016, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'InitialRotationalVelocityZ' , 'pVal' , ), 3017, (3017, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialRotationalVelocityX' , 'pVal' , ), 3018, (3018, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialRotationalVelocityX' , 'pVal' , ), 3018, (3018, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialRotationalVelocityY' , 'pVal' , ), 3019, (3019, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialRotationalVelocityY' , 'pVal' , ), 3019, (3019, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialRotationalVelocityZ' , 'pVal' , ), 3020, (3020, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UseInitialRotationalVelocityZ' , 'pVal' , ), 3020, (3020, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalVelocityRefMarker' , 'strMarker' , ), 3021, (3021, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'TranslationalVelocityRefMarker' , 'strMarker' , ), 3021, (3021, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'RotationalVelocityRefMarker' , 'strMarker' , ), 3022, (3022, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'RotationalVelocityRefMarker' , 'strMarker' , ), 3022, (3022, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedRigidBodyFrequency' , 'pVal' , ), 3023, (3023, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedRigidBodyFrequency' , 'pVal' , ), 3023, (3023, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedRigidBodyFrequency' , 'pVal' , ), 3024, (3024, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfMode' , 'pVal' , ), 3025, (3025, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'RFIFileName' , 'pVal' , ), 3026, (3026, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'RFIFileName' , 'pVal' , ), 3026, (3026, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'ModeInformation' , 'pModeSequence' , 'pVal' , ), 3027, (3027, (), [ (19, 1, None, None) , 
			 (16393, 10, None, "IID('{7ED2BDE4-77AC-4D41-8745-10EB8FC6812C}')") , ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 3030, (3030, (), [ (16393, 10, None, "IID('{4C8B7C23-7D92-4D39-B530-5D93DC97F771}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'CreateMarkerOnNode' , 'strName' , 'uiNodeID' , 'ppVal' , ), 3031, (3031, (), [ 
			 (8, 1, None, None) , (19, 1, None, None) , (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'CreateElementSet' , 'strName' , 'arrElementID' , 'ppVal' , ), 3032, (3032, (), [ 
			 (8, 1, None, None) , (8195, 1, None, None) , (16393, 10, None, "IID('{312FF880-5EB3-4AE9-A989-940D556064EE}')") , ], 1 , 1 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'CreatePatchSet' , 'strName' , 'arrNodeID' , 'ppVal' , ), 3033, (3033, (), [ 
			 (8, 1, None, None) , (8195, 1, None, None) , (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'RFlexElementSetCollection' , 'pVal' , ), 3034, (3034, (), [ (16393, 10, None, "IID('{B1A8C8FA-7869-4CB5-A285-91BCC4C2ADA3}')") , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'RFlexPatchSetCollection' , 'pVal' , ), 3035, (3035, (), [ (16393, 10, None, "IID('{6A9E16A5-2CCC-4596-BDC0-07B767DB1A39}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'GetEntity' , 'strName' , 'ppVal' , ), 3036, (3036, (), [ (8, 1, None, None) , 
			 (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'CreateOutput' , 'strName' , 'arrNodeID' , 'ppVal' , ), 3037, (3037, (), [ 
			 (8, 1, None, None) , (8195, 1, None, None) , (16393, 10, None, "IID('{5C616B86-29F2-486F-9E0C-D66502222E30}')") , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'RFlexOutputCollection' , 'pVal' , ), 3038, (3038, (), [ (16393, 10, None, "IID('{D1E612A4-BFE5-4676-B55D-76C41FE47B42}')") , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'RFlexNodeSetCollection' , 'pVal' , ), 3039, (3039, (), [ (16393, 10, None, "IID('{2AAD6766-1ED5-498D-96BA-F9363B2DF588}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'CreateNodeSet' , 'strName' , 'arrNodeID' , 'ppVal' , ), 3040, (3040, (), [ 
			 (8, 1, None, None) , (8195, 1, None, None) , (16393, 10, None, "IID('{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')") , ], 1 , 1 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'OutputFileInfo' , 'ppVal' , ), 3041, (3041, (), [ (16393, 10, None, "IID('{16BD870A-FA04-42F6-8B8D-7F484F5D421E}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'DisplaySetting' , 'ppVal' , ), 3042, (3042, (), [ (16393, 10, None, "IID('{3FDF0768-0052-4B63-9D84-A644C3152051}')") , ], 1 , 2 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'ExportShellFormatData' , 'ppVal' , ), 3043, (3043, (), [ (16393, 10, None, "IID('{2EE15E44-AD0C-4D9B-B53A-35BF7F1E1322}')") , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'OutputFileInfoforRegenerator' , 'ppVal' , ), 3044, (3044, (), [ (16393, 10, None, "IID('{1B06647C-BAD6-464A-8B5E-DD243D535970}')") , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'CreateLineSet' , 'strName' , 'arrNodeID' , 'ppVal' , ), 3045, (3045, (), [ 
			 (8, 1, None, None) , (8195, 1, None, None) , (16393, 10, None, "IID('{7C9E9609-3A15-4847-8B60-6AE1460A7A58}')") , ], 1 , 1 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'RFlexNodeCollection' , 'pVal' , ), 3046, (3046, (), [ (16393, 10, None, "IID('{EEEA6051-9841-4895-BC92-93F52E98A389}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'MarkerCollection' , 'ppVal' , ), 3047, (3047, (), [ (16393, 10, None, "IID('{6BEF9B6B-4708-445E-A3B5-0D65BA69F748}')") , ], 1 , 2 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'MassInvariant' , 'pVal' , ), 3048, (3048, (), [ (3, 1, None, "IID('{5BA4E584-3306-4C81-89A9-A452C0BE259D}')") , ], 1 , 4 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
	(( 'MassInvariant' , 'pVal' , ), 3048, (3048, (), [ (16387, 10, None, "IID('{5BA4E584-3306-4C81-89A9-A452C0BE259D}')") , ], 1 , 2 , 4 , 0 , 592 , (3, 0, None, None) , 0 , )),
	(( 'CreatePatchSetWithBox' , 'strName' , 'pRefFrame' , 'dWidth' , 'dHeight' , 
			 'dDepth' , 'ppVal' , ), 3049, (3049, (), [ (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , 
			 (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 1 , 4 , 0 , 600 , (3, 0, None, None) , 0 , )),
	(( 'CreatePatchSetWithNodeSet' , 'strName' , 'pNodeSet' , 'ppVal' , ), 3050, (3050, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')") , (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 1 , 4 , 0 , 608 , (3, 0, None, None) , 0 , )),
	(( 'CreatePatchSetWithElementIDsContinuous' , 'strName' , 'arrElementID' , 'dAngle' , 'bCheckReverse' , 
			 'ppVal' , ), 3051, (3051, (), [ (8, 1, None, None) , (8195, 1, None, None) , (5, 1, None, None) , 
			 (11, 1, None, None) , (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 1 , 4 , 0 , 616 , (3, 0, None, None) , 0 , )),
	(( 'CreatePatchSetWithElementIDs' , 'strName' , 'arrElementID' , 'ppVal' , ), 3052, (3052, (), [ 
			 (8, 1, None, None) , (8195, 1, None, None) , (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 1 , 4 , 0 , 624 , (3, 0, None, None) , 0 , )),
	(( 'CreatePatchSetWithPatchIndices' , 'strName' , 'arrPatchesIndices' , 'ppVal' , ), 3053, (3053, (), [ 
			 (8, 1, None, None) , (8195, 1, None, None) , (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 1 , 4 , 0 , 632 , (3, 0, None, None) , 0 , )),
	(( 'CreatePatchSetWithPatchIndicesContinuous' , 'strName' , 'arrPatchesIndices' , 'dAngle' , 'bCheckReverse' , 
			 'ppVal' , ), 3054, (3054, (), [ (8, 1, None, None) , (8195, 1, None, None) , (5, 1, None, None) , 
			 (11, 1, None, None) , (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 1 , 4 , 0 , 640 , (3, 0, None, None) , 0 , )),
	(( 'CreateMarker' , 'strName' , 'pRefFrame' , 'ppVal' , ), 3055, (3055, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 1 , 4 , 0 , 648 , (3, 0, None, None) , 0 , )),
	(( 'RFlexElementCollection' , 'pVal' , ), 3056, (3056, (), [ (16393, 10, None, "IID('{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}')") , ], 1 , 2 , 4 , 0 , 656 , (3, 0, None, None) , 0 , )),
	(( 'GetNodeByID' , 'nID' , 'ppVal' , ), 3057, (3057, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')") , ], 1 , 1 , 4 , 0 , 664 , (3, 0, None, None) , 0 , )),
	(( 'GetElementByID' , 'nID' , 'ppVal' , ), 3058, (3058, (), [ (3, 1, None, None) , 
			 (16393, 10, None, "IID('{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}')") , ], 1 , 1 , 4 , 0 , 672 , (3, 0, None, None) , 0 , )),
	(( 'CreatePatchSetWithCone' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'dTopRadius' , 
			 'dBottomRadius' , 'dTolerance' , 'ppVal' , ), 3059, (3059, (), [ (8, 1, None, None) , 
			 (8197, 1, None, None) , (8197, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , 
			 (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 1 , 4 , 0 , 680 , (3, 0, None, None) , 0 , )),
	(( 'LayerNumber' , 'pVal' , ), 3060, (3060, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 688 , (3, 0, None, None) , 0 , )),
	(( 'LayerNumber' , 'pVal' , ), 3060, (3060, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 696 , (3, 0, None, None) , 0 , )),
	(( 'ParametricPointCollection' , 'ppVal' , ), 3061, (3061, (), [ (16393, 10, None, "IID('{65267578-7015-4BB5-BB65-F5F81CCEA244}')") , ], 1 , 2 , 4 , 0 , 704 , (3, 0, None, None) , 0 , )),
	(( 'ParametricValueCollection' , 'ppVal' , ), 3062, (3062, (), [ (16393, 10, None, "IID('{65267578-7015-4BB5-BB65-F5F81CCEA245}')") , ], 1 , 2 , 4 , 0 , 712 , (3, 0, None, None) , 0 , )),
	(( 'ImportParametricPoint' , 'strFileName' , ), 3063, (3063, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 720 , (3, 0, None, None) , 0 , )),
	(( 'ExportParametricPoint' , 'strFileName' , ), 3064, (3064, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 728 , (3, 0, None, None) , 0 , )),
	(( 'ImportParametricValue' , 'strFileName' , ), 3065, (3065, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 736 , (3, 0, None, None) , 0 , )),
	(( 'ExportParametricValue' , 'strFileName' , ), 3066, (3066, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 744 , (3, 0, None, None) , 0 , )),
	(( 'CreateParametricPoint' , 'strName' , 'pPoint' , 'pRefMarker' , 'ppVal' , 
			 ), 3067, (3067, (), [ (8, 1, None, None) , (8197, 1, None, None) , (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , (16393, 10, None, "IID('{64B0B5B9-7662-40E8-B27C-9E42C3A158BF}')") , ], 1 , 1 , 4 , 0 , 752 , (3, 0, None, None) , 0 , )),
	(( 'CreateParametricValue' , 'strName' , 'dValue' , 'ppVal' , ), 3068, (3068, (), [ 
			 (8, 1, None, None) , (5, 1, None, None) , (16393, 10, None, "IID('{3EEED3CE-62E8-4882-AAE6-4812B49927B5}')") , ], 1 , 1 , 4 , 0 , 760 , (3, 0, None, None) , 0 , )),
	(( 'CreateParametricPointWithText' , 'strName' , 'strText' , 'pRefMarker' , 'ppVal' , 
			 ), 3069, (3069, (), [ (8, 1, None, None) , (8, 1, None, None) , (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , (16393, 10, None, "IID('{64B0B5B9-7662-40E8-B27C-9E42C3A158BF}')") , ], 1 , 1 , 4 , 0 , 768 , (3, 0, None, None) , 0 , )),
	(( 'CreateParametricValueWithText' , 'strName' , 'strText' , 'ppVal' , ), 3070, (3070, (), [ 
			 (8, 1, None, None) , (8, 1, None, None) , (16393, 10, None, "IID('{3EEED3CE-62E8-4882-AAE6-4812B49927B5}')") , ], 1 , 1 , 4 , 0 , 776 , (3, 0, None, None) , 0 , )),
	(( 'RFlexLineSetCollection' , 'pVal' , ), 3071, (3071, (), [ (16393, 10, None, "IID('{05938874-D404-42C9-9757-863978D57DE5}')") , ], 1 , 2 , 4 , 0 , 784 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 3072, (3072, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 792 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 3072, (3072, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 800 , (3, 0, None, None) , 0 , )),
	(( 'AnimationScaling' , 'scaling' , ), 3073, (3073, (), [ (16393, 10, None, "IID('{13F0E996-9155-4427-BF61-8A8D60739288}')") , ], 1 , 2 , 4 , 0 , 808 , (3, 0, None, None) , 0 , )),
	(( 'DeleteAnimationScaling' , ), 3074, (3074, (), [ ], 1 , 1 , 4 , 0 , 816 , (3, 0, None, None) , 0 , )),
	(( 'AnimationDataScaling' , 'pVal' , ), 3029, (3029, (), [ (16393, 10, None, "IID('{E3D7FEE7-8867-4A03-B9EA-A1DD773026CC}')") , ], 1 , 2 , 4 , 0 , 824 , (3, 0, None, None) , 0 , )),
]

IRFlexBodyCollection_vtables_dispatch_ = 1
IRFlexBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexBodyImportOption_vtables_dispatch_ = 1
IRFlexBodyImportOption_vtables_ = [
	(( 'UseNodalResidual' , 'pVal' , ), 3000, (3000, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseNodalResidual' , 'pVal' , ), 3000, (3000, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedRigidBodyFrequency' , 'pVal' , ), 3001, (3001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseUserDefinedRigidBodyFrequency' , 'pVal' , ), 3001, (3001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedRigidBodyFrequency' , 'value' , ), 3002, (3002, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedRigidBodyFrequency' , 'value' , ), 3002, (3002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseInternalNodes' , 'pVal' , ), 3003, (3003, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseInternalNodes' , 'pVal' , ), 3003, (3003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IRFlexElement_vtables_dispatch_ = 1
IRFlexElement_vtables_ = [
]

IRFlexElementCollection_vtables_dispatch_ = 1
IRFlexElementCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexElementSet_vtables_dispatch_ = 1
IRFlexElementSet_vtables_ = [
	(( 'Color' , 'pVal' , ), 3051, (3051, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3051, (3051, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ElementCollection' , 'pVal' , ), 3052, (3052, (), [ (16393, 10, None, "IID('{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'NodeCollection' , 'pVal' , ), 3053, (3053, (), [ (16393, 10, None, "IID('{EEEA6051-9841-4895-BC92-93F52E98A389}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IRFlexElementSetCollection_vtables_dispatch_ = 1
IRFlexElementSetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{312FF880-5EB3-4AE9-A989-940D556064EE}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexExportDurabilityInterfaceOption_vtables_dispatch_ = 1
IRFlexExportDurabilityInterfaceOption_vtables_ = [
	(( 'LoadFactor' , 'pVal' , ), 3000, (3000, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'LoadFactor' , 'pVal' , ), 3000, (3000, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ViewModalCoordinates' , 'pVal' , ), 3001, (3001, (), [ (8203, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ViewModalCoordinates' , 'pVal' , ), 3001, (3001, (), [ (24587, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CreateFEMFATUnitStressScratchFileFlag' , 'pVal' , ), 3002, (3002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'CreateFEMFATUnitStressScratchFileFlag' , 'pVal' , ), 3002, (3002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RPCFileName' , 'pVal' , ), 3003, (3003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RPCFileName' , 'pVal' , ), 3003, (3003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ScratchFileName' , 'pVal' , ), 3004, (3004, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ScratchFileName' , 'pVal' , ), 3004, (3004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'MaxFileName' , 'pVal' , ), 3005, (3005, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MaxFileName' , 'pVal' , ), 3005, (3005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IRFlexExportMDFFileOption_vtables_dispatch_ = 1
IRFlexExportMDFFileOption_vtables_ = [
	(( 'SkippedTimeIndexListString' , 'pVal' , ), 3000, (3000, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SkippedTimeIndexListString' , 'pVal' , ), 3000, (3000, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ExportMDFFileName' , 'pVal' , ), 3001, (3001, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ExportMDFFileName' , 'pVal' , ), 3001, (3001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IRFlexForce_vtables_dispatch_ = 1
IRFlexForce_vtables_ = [
]

IRFlexForceCollection_vtables_dispatch_ = 1
IRFlexForceCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{7DA762BF-839E-49E6-AB67-2C28067114CE}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexForceModalForce_vtables_dispatch_ = 1
IRFlexForceModalForce_vtables_ = [
	(( 'ModalForceInfoCollection' , 'ppVal' , ), 3000, (3000, (), [ (16393, 10, None, "IID('{BED48F30-1BA6-40B0-80C6-ED2650A5E796}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'ppVal' , ), 3001, (3001, (), [ (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UserSubroutine' , 'ppVal' , ), 3001, (3001, (), [ (16393, 10, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RFlexBody' , 'ppVal' , ), 3002, (3002, (), [ (16393, 10, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'NodeSet' , 'ppVal' , ), 3003, (3003, (), [ (9, 1, None, "IID('{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NodeSet' , 'ppVal' , ), 3003, (3003, (), [ (16393, 10, None, "IID('{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'USUBType' , 'ppVal' , ), 3004, (3004, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 3005, (3005, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 3005, (3005, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseReportNodes' , 'pVal' , ), 3006, (3006, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseReportNodes' , 'pVal' , ), 3006, (3006, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ReportNodeIDs' , 'arrNodeIDs' , ), 3007, (3007, (), [ (8195, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ReportNodeIDs' , 'arrNodeIDs' , ), 3007, (3007, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

IRFlexForceModalForceInfo_vtables_dispatch_ = 1
IRFlexForceModalForceInfo_vtables_ = [
	(( 'ModalLoadCase' , 'ppVal' , ), 3000, (3000, (), [ (16393, 10, None, "IID('{6FB3F9CE-90B7-4111-8714-AA24F53632A6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 3001, (3001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 3001, (3001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IRFlexForceModalForceInfoCollection_vtables_dispatch_ = 1
IRFlexForceModalForceInfoCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{5A81CC6A-C0E7-4B23-8E27-CD06F1E2CC13}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexForceModalPreload_vtables_dispatch_ = 1
IRFlexForceModalPreload_vtables_ = [
	(( 'ModalPreloadInfoCollection' , 'ppVal' , ), 3000, (3000, (), [ (16393, 10, None, "IID('{05ADCCED-A6D5-4E30-A946-DBA87CAC5F0B}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'RFlexBody' , 'ppVal' , ), 3001, (3001, (), [ (16393, 10, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IRFlexForceModalPreloadInfo_vtables_dispatch_ = 1
IRFlexForceModalPreloadInfo_vtables_ = [
	(( 'ModalLoadCase' , 'ppVal' , ), 3000, (3000, (), [ (16393, 10, None, "IID('{6FB3F9CE-90B7-4111-8714-AA24F53632A6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 3001, (3001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 3001, (3001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ScaleFactor' , 'pVal' , ), 3002, (3002, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ScaleFactor' , 'pVal' , ), 3002, (3002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IRFlexForceModalPreloadInfoCollection_vtables_dispatch_ = 1
IRFlexForceModalPreloadInfoCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{EE8ABAE9-396E-46FB-B11F-AD1471097DAF}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexGroupBeam_vtables_dispatch_ = 1
IRFlexGroupBeam_vtables_ = [
	(( 'CrossSectionArea' , 'pVal' , ), 3001, (3001, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DampingMatrix' , 'i' , 'j' , 'pVal' , ), 3002, (3002, (), [ 
			 (3, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ViscousDampingRatio' , 'pVal' , ), 3003, (3003, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'pVal' , ), 3004, (3004, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'pVal' , ), 3005, (3005, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'pVal' , ), 3006, (3006, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ShearAreaRationY' , 'pVal' , ), 3007, (3007, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ShearAreaRationZ' , 'pVal' , ), 3008, (3008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ShearModulus' , 'pVal' , ), 3009, (3009, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'NodeThickness' , 'pVal' , ), 3010, (3010, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'YoungsModulus' , 'pVal' , ), 3011, (3011, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingMatrix' , 'pVal' , ), 3012, (3012, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingMatrix' , 'pVal' , ), 3012, (3012, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'EachRenderMode' , 'pVal' , ), 3013, (3013, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}')") , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'EachRenderMode' , 'pVal' , ), 3013, (3013, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3014, (3014, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3014, (3014, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'TotalMass' , 'pVal' , ), 3015, (3015, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 3016, (3016, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'SolveLargeDOFBeam' , ), 3017, (3017, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'InertiaPropertyInput' , 'pVal' , ), 3018, (3018, (), [ (3, 1, None, "IID('{F752AB94-C4F5-49AE-B368-095E39D47E86}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'InertiaPropertyInput' , 'pVal' , ), 3018, (3018, (), [ (16387, 10, None, "IID('{F752AB94-C4F5-49AE-B368-095E39D47E86}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'MeshSegmentNumber' , 'pVal' , ), 3019, (3019, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'UpdateForceProperty' , ), 3020, (3020, (), [ ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'UpdateBodyProperty' , ), 3021, (3021, (), [ ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'BeamCrossSectionType' , 'pVal' , ), 3022, (3022, (), [ (3, 1, None, "IID('{01406737-1007-468F-A0BC-A2F7C43239CF}')") , ], 1 , 4 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'BeamCrossSectionType' , 'pVal' , ), 3022, (3022, (), [ (16387, 10, None, "IID('{01406737-1007-468F-A0BC-A2F7C43239CF}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'BeamCrossSection' , 'ppVal' , ), 3023, (3023, (), [ (16393, 10, None, "IID('{557175E7-72DD-447A-8DB1-319593C34BDC}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'UpdateCrossSectionProperty' , ), 3024, (3024, (), [ ], 1 , 1 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'ShearAreaRatioY' , 'pVal' , ), 3025, (3025, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'ShearAreaRatioZ' , 'pVal' , ), 3026, (3026, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
]

IRFlexInterfaceANSYSOption_vtables_dispatch_ = 1
IRFlexInterfaceANSYSOption_vtables_ = [
	(( 'ResultFileName' , 'rstFileName' , ), 3000, (3000, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ResultFileName' , 'rstFileName' , ), 3000, (3000, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'MaterialFileName' , 'mpFileName' , ), 3001, (3001, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MaterialFileName' , 'mpFileName' , ), 3001, (3001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ElementMatricesFileName' , 'ematFileName' , ), 3002, (3002, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ElementMatricesFileName' , 'ematFileName' , ), 3002, (3002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'CMFileName' , 'CMFileName' , ), 3003, (3003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'CMFileName' , 'CMFileName' , ), 3003, (3003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DataPrecisionofStressStrainShape' , 'pVal' , ), 3004, (3004, (), [ (3, 1, None, "IID('{A353EE4A-BA4D-4F66-9D7C-355863AA890E}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DataPrecisionofStressStrainShape' , 'pVal' , ), 3004, (3004, (), [ (16387, 10, None, "IID('{A353EE4A-BA4D-4F66-9D7C-355863AA890E}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'StressShapeFlag' , 'pVal' , ), 3005, (3005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'StressShapeFlag' , 'pVal' , ), 3005, (3005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'StrainShapeFlag' , 'pVal' , ), 3006, (3006, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'StrainShapeFlag' , 'pVal' , ), 3006, (3006, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3007, (3007, (), [ (3, 1, None, "IID('{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3007, (3007, (), [ (16387, 10, None, "IID('{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IRFlexInterfaceCommonOption_vtables_dispatch_ = 1
IRFlexInterfaceCommonOption_vtables_ = [
	(( 'UseStiffnessMatrix' , 'pVal' , ), 3000, (3000, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessMatrix' , 'pVal' , ), 3000, (3000, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseInternalNodes' , 'pVal' , ), 3001, (3001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseInternalNodes' , 'pVal' , ), 3001, (3001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseNumberOfMode' , 'pVal' , ), 3002, (3002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseNumberOfMode' , 'pVal' , ), 3002, (3002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfMode' , 'value' , ), 3003, (3003, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfMode' , 'value' , ), 3003, (3003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'LowerBoundFrequency' , 'value' , ), 3004, (3004, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'LowerBoundFrequency' , 'value' , ), 3004, (3004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UpperBoundFrequency' , 'value' , ), 3005, (3005, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UpperBoundFrequency' , 'value' , ), 3005, (3005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'UseUnitForce' , 'pVal' , ), 3006, (3006, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseUnitForce' , 'pVal' , ), 3006, (3006, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'RemoveZeroValueFlag' , 'pVal' , ), 3007, (3007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'RemoveZeroValueFlag' , 'pVal' , ), 3007, (3007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'RemoveMidNodeFlag' , 'pVal' , ), 3008, (3008, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'RemoveMidNodeFlag' , 'pVal' , ), 3008, (3008, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IRFlexInterfaceExtraModeOption_vtables_dispatch_ = 1
IRFlexInterfaceExtraModeOption_vtables_ = [
	(( 'ExtraModeInputFileList' , 'outputFileList' , ), 3000, (3000, (), [ (8200, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ExtraModeInputFileList' , 'outputFileList' , ), 3000, (3000, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LowerBoundFrequency' , 'value' , ), 3001, (3001, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LowerBoundFrequency' , 'value' , ), 3001, (3001, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UpperBoundFrequency' , 'value' , ), 3002, (3002, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UpperBoundFrequency' , 'value' , ), 3002, (3002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IRFlexInterfaceIdeasOption_vtables_dispatch_ = 1
IRFlexInterfaceIdeasOption_vtables_ = [
	(( 'UseElementSet' , 'pVal' , ), 3000, (3000, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseElementSet' , 'pVal' , ), 3000, (3000, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseNodeSet' , 'pVal' , ), 3001, (3001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseNodeSet' , 'pVal' , ), 3001, (3001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IRFlexInterfaceNastranOP2Option_vtables_dispatch_ = 1
IRFlexInterfaceNastranOP2Option_vtables_ = [
	(( 'DataPrecisionofStressStrainShape' , 'pVal' , ), 3000, (3000, (), [ (3, 1, None, "IID('{A353EE4A-BA4D-4F66-9D7C-355863AA890E}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DataPrecisionofStressStrainShape' , 'pVal' , ), 3000, (3000, (), [ (16387, 10, None, "IID('{A353EE4A-BA4D-4F66-9D7C-355863AA890E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StressShapeFlag' , 'pVal' , ), 3001, (3001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StressShapeFlag' , 'pVal' , ), 3001, (3001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StrainShapeFlag' , 'pVal' , ), 3002, (3002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'StrainShapeFlag' , 'pVal' , ), 3002, (3002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3003, (3003, (), [ (3, 1, None, "IID('{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3003, (3003, (), [ (16387, 10, None, "IID('{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IRFlexLineSet_vtables_dispatch_ = 1
IRFlexLineSet_vtables_ = [
	(( 'NodeIDs' , 'arrNodeIDs' , ), 3051, (3051, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NodeCollection' , 'pVal' , ), 3052, (3052, (), [ (16393, 10, None, "IID('{EEEA6051-9841-4895-BC92-93F52E98A389}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3053, (3053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3053, (3053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IRFlexLineSetCollection_vtables_dispatch_ = 1
IRFlexLineSetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{7C9E9609-3A15-4847-8B60-6AE1460A7A58}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexLoad_vtables_dispatch_ = 1
IRFlexLoad_vtables_ = [
]

IRFlexLoadPressureModal_vtables_dispatch_ = 1
IRFlexLoadPressureModal_vtables_ = [
	(( 'PatchSet' , 'ppVal' , ), 3001, (3001, (), [ (9, 1, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'PatchSet' , 'ppVal' , ), 3001, (3001, (), [ (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PressureUpDirction' , 'pVal' , ), 3002, (3002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PressureUpDirction' , 'pVal' , ), 3002, (3002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Pressure' , 'ppVal' , ), 3003, (3003, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'Pressure' , 'ppVal' , ), 3003, (3003, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 3004, (3004, (), [ (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'BaseBody' , 'ppVal' , ), 3004, (3004, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseReportNodes' , 'pVal' , ), 3005, (3005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseReportNodes' , 'pVal' , ), 3005, (3005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ReportNodeIDs' , 'arrNodeIDs' , ), 3006, (3006, (), [ (8195, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ReportNodeIDs' , 'arrNodeIDs' , ), 3006, (3006, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseConvergedResult' , 'pVal' , ), 3007, (3007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseConvergedResult' , 'pVal' , ), 3007, (3007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'StepSizeCriteria' , 'ppVal' , ), 3008, (3008, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IRFlexModalLoadCase_vtables_dispatch_ = 1
IRFlexModalLoadCase_vtables_ = [
	(( 'ID' , 'pVal' , ), 3000, (3000, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 3001, (3001, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Name' , 'pVal' , ), 3001, (3001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RFlexBody' , 'ppVal' , ), 3002, (3002, (), [ (16393, 10, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 3003, (3003, (), [ (3, 1, None, "IID('{BF28A376-C8E8-493C-B09F-BF5FCE1645E7}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 3003, (3003, (), [ (16387, 10, None, "IID('{BF28A376-C8E8-493C-B09F-BF5FCE1645E7}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NodalLoadValueCollection' , 'ppVal' , ), 3004, (3004, (), [ (16393, 10, None, "IID('{8AEC2258-C39F-452F-BA67-11FC9D98B45A}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ModalLoadValue' , 'ppVal' , ), 3005, (3005, (), [ (16393, 10, None, "IID('{DC95F017-DABD-4F7B-8E19-D6DC880124BF}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IRFlexModalLoadCaseCollection_vtables_dispatch_ = 1
IRFlexModalLoadCaseCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{6FB3F9CE-90B7-4111-8714-AA24F53632A6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexModalLoadValue_vtables_dispatch_ = 1
IRFlexModalLoadValue_vtables_ = [
	(( 'ModeValueCollection' , 'pVal' , ), 3000, (3000, (), [ (16393, 10, None, "IID('{FD818ABF-BF56-4B8B-896B-01F99E1ED037}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FX' , 'pVal' , ), 3001, (3001, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FX' , 'pVal' , ), 3001, (3001, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FY' , 'pVal' , ), 3002, (3002, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FY' , 'pVal' , ), 3002, (3002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FZ' , 'pVal' , ), 3003, (3003, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'FZ' , 'pVal' , ), 3003, (3003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TX' , 'pVal' , ), 3004, (3004, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TX' , 'pVal' , ), 3004, (3004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TY' , 'pVal' , ), 3005, (3005, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TY' , 'pVal' , ), 3005, (3005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TZ' , 'pVal' , ), 3006, (3006, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TZ' , 'pVal' , ), 3006, (3006, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IRFlexModeInformation_vtables_dispatch_ = 1
IRFlexModeInformation_vtables_ = [
	(( 'UseMode' , 'pVal' , ), 3001, (3001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseMode' , 'pVal' , ), 3001, (3001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Frequency' , 'pVal' , ), 3002, (3002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'pVal' , ), 3003, (3003, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'pVal' , ), 3003, (3003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseModeForAnimation' , 'pVal' , ), 3004, (3004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseModeForAnimation' , 'pVal' , ), 3004, (3004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IRFlexModeValue_vtables_dispatch_ = 1
IRFlexModeValue_vtables_ = [
	(( 'Sequence' , 'pVal' , ), 3000, (3000, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ModeValue' , 'pVal' , ), 3001, (3001, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ModeValue' , 'pVal' , ), 3001, (3001, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IRFlexModeValueCollection_vtables_dispatch_ = 1
IRFlexModeValueCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{EBF8DAD1-BFE3-4A50-BF0B-2ACC1B3FA3C6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexNodalLoadValue_vtables_dispatch_ = 1
IRFlexNodalLoadValue_vtables_ = [
	(( 'NodeID' , 'pVal' , ), 3000, (3000, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'FX' , 'pVal' , ), 3001, (3001, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'FX' , 'pVal' , ), 3001, (3001, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'FY' , 'pVal' , ), 3002, (3002, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'FY' , 'pVal' , ), 3002, (3002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'FZ' , 'pVal' , ), 3003, (3003, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'FZ' , 'pVal' , ), 3003, (3003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TX' , 'pVal' , ), 3004, (3004, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TX' , 'pVal' , ), 3004, (3004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TY' , 'pVal' , ), 3005, (3005, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TY' , 'pVal' , ), 3005, (3005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'TZ' , 'pVal' , ), 3006, (3006, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TZ' , 'pVal' , ), 3006, (3006, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IRFlexNodalLoadValueCollection_vtables_dispatch_ = 1
IRFlexNodalLoadValueCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{5104436A-9AB2-4C96-8550-F085D5BE63F9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexNode_vtables_dispatch_ = 1
IRFlexNode_vtables_ = [
]

IRFlexNodeCollection_vtables_dispatch_ = 1
IRFlexNodeCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexNodeSet_vtables_dispatch_ = 1
IRFlexNodeSet_vtables_ = [
	(( 'NodeIDs' , 'arrNodeIDs' , ), 3051, (3051, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NodeCollection' , 'pVal' , ), 3052, (3052, (), [ (16393, 10, None, "IID('{EEEA6051-9841-4895-BC92-93F52E98A389}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3053, (3053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3053, (3053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AddNodes' , 'val' , ), 3054, (3054, (), [ (8195, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DeleteNodes' , 'val' , ), 3055, (3055, (), [ (8195, 1, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IRFlexNodeSetCollection_vtables_dispatch_ = 1
IRFlexNodeSetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexOutput_vtables_dispatch_ = 1
IRFlexOutput_vtables_ = [
	(( 'NodeIDs' , 'arrNodeIDs' , ), 3001, (3001, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NodeCollection' , 'ppVal' , ), 3002, (3002, (), [ (16393, 10, None, "IID('{EEEA6051-9841-4895-BC92-93F52E98A389}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3003, (3003, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3003, (3003, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IRFlexOutputCollection_vtables_dispatch_ = 1
IRFlexOutputCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{5C616B86-29F2-486F-9E0C-D66502222E30}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexOutputFileGenerator_vtables_dispatch_ = 1
IRFlexOutputFileGenerator_vtables_ = [
	(( 'OutputFileSetting' , 'ppVal' , ), 3001, (3001, (), [ (16393, 10, None, "IID('{350C9018-D3B8-4D6B-B9EC-271CE461FDC0}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 3002, (3002, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IRFlexOutputFileInfo_vtables_dispatch_ = 1
IRFlexOutputFileInfo_vtables_ = [
	(( 'BodyName' , 'pVal' , ), 3001, (3001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 3002, (3002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 3002, (3002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'AnimationFileState' , 'pVal' , ), 3003, (3003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StrainFileState' , 'pVal' , ), 3004, (3004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'StressFileState' , 'pVal' , ), 3005, (3005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3006, (3006, (), [ (3, 1, None, "IID('{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3006, (3006, (), [ (16387, 10, None, "IID('{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IRFlexOutputFileInfoForRegenerator_vtables_dispatch_ = 1
IRFlexOutputFileInfoForRegenerator_vtables_ = [
	(( 'BodyName' , 'pVal' , ), 3001, (3001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseDisplacementData' , 'pVal' , ), 3002, (3002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseDisplacementData' , 'pVal' , ), 3002, (3002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseStrainStressData' , 'pVal' , ), 3003, (3003, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseStrainStressData' , 'pVal' , ), 3003, (3003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'StrainShellRecoveryTypeList' , 'ppSafeArray' , ), 3005, (3005, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'StressShellRecoveryTypeList' , 'ppSafeArray' , ), 3006, (3006, (), [ (24584, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'StrainShellRecoveryType' , 'pVal' , ), 3007, (3007, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'StrainShellRecoveryType' , 'pVal' , ), 3007, (3007, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'StressShellRecoveryType' , 'pVal' , ), 3008, (3008, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'StressShellRecoveryType' , 'pVal' , ), 3008, (3008, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'AnimationFileState' , 'pVal' , ), 3009, (3009, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'StrainFileState' , 'pVal' , ), 3010, (3010, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'StressFileState' , 'pVal' , ), 3011, (3011, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DisplacementDataPrecision' , 'pVal' , ), 3012, (3012, (), [ (3, 1, None, "IID('{511C893E-A8F1-4026-80BE-F02530E47D72}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'DisplacementDataPrecision' , 'pVal' , ), 3012, (3012, (), [ (16387, 10, None, "IID('{511C893E-A8F1-4026-80BE-F02530E47D72}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'BeamRecoveryType' , 'pVal' , ), 3013, (3013, (), [ (3, 1, None, "IID('{E6829DB6-AAEE-4CC3-9BC8-BF1F91851DF4}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'BeamRecoveryType' , 'pVal' , ), 3013, (3013, (), [ (16387, 10, None, "IID('{E6829DB6-AAEE-4CC3-9BC8-BF1F91851DF4}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IRFlexOutputFileRegenerator_vtables_dispatch_ = 1
IRFlexOutputFileRegenerator_vtables_ = [
	(( 'SameOptionsforAllRFlexBodies' , 'pVal' , ), 3001, (3001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SameOptionsforAllRFlexBodies' , 'pVal' , ), 3001, (3001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'RecoverDisplacementData' , 'pVal' , ), 3002, (3002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RecoverDisplacementData' , 'pVal' , ), 3002, (3002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RecoverStrainStressData' , 'pVal' , ), 3003, (3003, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'RecoverStrainStressData' , 'pVal' , ), 3003, (3003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3004, (3004, (), [ (3, 1, None, "IID('{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3004, (3004, (), [ (16387, 10, None, "IID('{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'OutputFileSetting' , 'ppVal' , ), 3005, (3005, (), [ (16393, 10, None, "IID('{350C9018-D3B8-4D6B-B9EC-271CE461FDC0}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 3006, (3006, (), [ ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedAnimation' , 'pVal' , ), 3007, (3007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedAnimation' , 'pVal' , ), 3007, (3007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DisplacementDataPrecision' , 'pVal' , ), 3008, (3008, (), [ (3, 1, None, "IID('{511C893E-A8F1-4026-80BE-F02530E47D72}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DisplacementDataPrecision' , 'pVal' , ), 3008, (3008, (), [ (16387, 10, None, "IID('{511C893E-A8F1-4026-80BE-F02530E47D72}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'BeamRecoveryType' , 'pVal' , ), 3009, (3009, (), [ (3, 1, None, "IID('{E6829DB6-AAEE-4CC3-9BC8-BF1F91851DF4}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'BeamRecoveryType' , 'pVal' , ), 3009, (3009, (), [ (16387, 10, None, "IID('{E6829DB6-AAEE-4CC3-9BC8-BF1F91851DF4}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IRFlexPatchSet_vtables_dispatch_ = 1
IRFlexPatchSet_vtables_ = [
	(( 'NodeIDs' , 'arrNodeIDs' , ), 3051, (3051, (), [ (24579, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'NodeCollection' , 'pVal' , ), 3052, (3052, (), [ (16393, 10, None, "IID('{EEEA6051-9841-4895-BC92-93F52E98A389}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3053, (3053, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 3053, (3053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IRFlexPatchSetCollection_vtables_dispatch_ = 1
IRFlexPatchSetCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexRFIOptimizerOption_vtables_dispatch_ = 1
IRFlexRFIOptimizerOption_vtables_ = [
	(( 'OriginalRFIFileName' , 'pVal' , ), 3000, (3000, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'OriginalRFIFileName' , 'pVal' , ), 3000, (3000, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OP2FileName' , 'pVal' , ), 3001, (3001, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OP2FileName' , 'pVal' , ), 3001, (3001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'ResultRFIFileName' , 'pVal' , ), 3002, (3002, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ResultRFIFileName' , 'pVal' , ), 3002, (3002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RemoveMidNodeFlag' , 'pVal' , ), 3003, (3003, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'RemoveMidNodeFlag' , 'pVal' , ), 3003, (3003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'RemoveZeroValueFlag' , 'pVal' , ), 3004, (3004, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'RemoveZeroValueFlag' , 'pVal' , ), 3004, (3004, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ChangeToExternalPatchFlag' , 'pVal' , ), 3005, (3005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'ChangeToExternalPatchFlag' , 'pVal' , ), 3005, (3005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 3006, (3006, (), [ (3, 1, None, "IID('{4A7E7C22-6E11-415A-A492-01782B6CCDB0}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 3006, (3006, (), [ (16387, 10, None, "IID('{4A7E7C22-6E11-415A-A492-01782B6CCDB0}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'StrainStressShapePrecisionFlag' , 'pVal' , ), 3007, (3007, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'StrainStressShapePrecisionFlag' , 'pVal' , ), 3007, (3007, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'RemoveModesFlag' , 'pVal' , ), 3008, (3008, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'RemoveModesFlag' , 'pVal' , ), 3008, (3008, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RemoveModes' , 'pVal' , ), 3009, (3009, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RemoveModes' , 'pVal' , ), 3009, (3009, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'SourceType' , 'pVal' , ), 3010, (3010, (), [ (3, 1, None, "IID('{1FBBB3AE-164E-4A0C-B02D-45472F907F09}')") , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'SourceType' , 'pVal' , ), 3010, (3010, (), [ (16387, 10, None, "IID('{1FBBB3AE-164E-4A0C-B02D-45472F907F09}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'RFlexBody' , 'ppVal' , ), 3011, (3011, (), [ (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RFlexBody' , 'ppVal' , ), 3011, (3011, (), [ (16393, 10, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DATFileName' , 'pVal' , ), 3012, (3012, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DATFileName' , 'pVal' , ), 3012, (3012, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RemainExternalNodesFlag' , 'pVal' , ), 3013, (3013, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RemainExternalNodesFlag' , 'pVal' , ), 3013, (3013, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'RemainUsedNodesFlag' , 'pVal' , ), 3014, (3014, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'RemainUsedNodesFlag' , 'pVal' , ), 3014, (3014, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'RemainSelectedNodesFlag' , 'pVal' , ), 3015, (3015, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RemainSelectedNodesFlag' , 'pVal' , ), 3015, (3015, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'RemainSelectedNodes' , 'pVal' , ), 3016, (3016, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'RemainSelectedNodes' , 'pVal' , ), 3016, (3016, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IRFlexRequest_vtables_dispatch_ = 1
IRFlexRequest_vtables_ = [
	(( 'Type' , 'pVal' , ), 3001, (3001, (), [ (3, 1, None, "IID('{02D8BDB5-7A43-482E-AB97-2C3307E32EB1}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 3001, (3001, (), [ (16387, 10, None, "IID('{02D8BDB5-7A43-482E-AB97-2C3307E32EB1}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ActionNodeID' , 'pVal' , ), 3002, (3002, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ActionNodeID' , 'pVal' , ), 3002, (3002, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'BaseMarker' , 'ppVal' , ), 3003, (3003, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'BaseMarker' , 'ppVal' , ), 3003, (3003, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RefMarker' , 'ppVal' , ), 3004, (3004, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'RefMarker' , 'ppVal' , ), 3004, (3004, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Use4thMarkerFlag' , 'flag' , ), 3005, (3005, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Use4thMarkerFlag' , 'flag' , ), 3005, (3005, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GetPlotNameList' , 'ppSafeArray' , ), 3006, (3006, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3007, (3007, (), [ (3, 1, None, "IID('{A980771B-865C-4EC4-AFF5-142BBB99BCAE}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ShellRecoveryType' , 'pVal' , ), 3007, (3007, (), [ (16387, 10, None, "IID('{A980771B-865C-4EC4-AFF5-142BBB99BCAE}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'BeamRecoveryType' , 'pVal' , ), 3008, (3008, (), [ (3, 1, None, "IID('{818B045A-34AC-4EEE-B440-3B8FEF411941}')") , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'BeamRecoveryType' , 'pVal' , ), 3008, (3008, (), [ (16387, 10, None, "IID('{818B045A-34AC-4EEE-B440-3B8FEF411941}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IRFlexRequestCollection_vtables_dispatch_ = 1
IRFlexRequestCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E43E421D-2821-44FF-B7FA-7CDF332A240F}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IRFlexToolFunction_vtables_dispatch_ = 1
IRFlexToolFunction_vtables_ = [
	(( 'GetNodeIDsFromMidNode' , 'pVal' , 'val' , 'arrNodes' , ), 3001, (3001, (), [ 
			 (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , (3, 1, None, None) , (24579, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SelectMultiComponentsUsingGUI' , 'varBody' , 'Type' , 'arrID' , ), 3002, (3002, (), [ 
			 (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , (3, 1, None, "IID('{3C9EB2D7-4CCA-4543-B169-AE2CE6267D5B}')") , (24579, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IRFlexToolkit_vtables_dispatch_ = 1
IRFlexToolkit_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 3050, (3050, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceANSYSOption' , 'ppResult' , ), 3051, (3051, (), [ (16393, 10, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C73}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceCommonOption' , 'ppResult' , ), 3052, (3052, (), [ (16393, 10, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceExtraModeOption' , 'ppResult' , ), 3053, (3053, (), [ (16393, 10, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C76}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateRfiFileFromANSYS' , 'strRfiFileName' , 'pANSYSOption' , 'pCommonOption' , 'UnitFactor' , 
			 'bSuccess' , ), 3054, (3054, (), [ (8, 1, None, None) , (9, 1, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C73}')") , (9, 1, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}')") , 
			 (9, 1, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateRfiFileFromIDEAS' , 'strRfiFileName' , 'strIDEASFileName' , 'pCommonOption' , 'UnitFactor' , 
			 'bSuccess' , ), 3055, (3055, (), [ (8, 1, None, None) , (8, 1, None, None) , (9, 1, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}')") , 
			 (9, 1, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateRfiFileFromNASTRAN' , 'strRfiFileName' , 'strNASTRANFileName' , 'pCommonOption' , 'UnitFactor' , 
			 'bSuccess' , ), 3056, (3056, (), [ (8, 1, None, None) , (8, 1, None, None) , (9, 1, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}')") , 
			 (9, 1, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ModifyRfiFileFromANSYS' , 'strRfiFileName' , 'pExtraModeOption' , 'bSuccess' , ), 3057, (3057, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C76}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ModifyRfiFileFromNASTRAN' , 'strRfiFileName' , 'pExtraModeOption' , 'bSuccess' , ), 3058, (3058, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C76}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ImportBodyOption' , 'ppResult' , ), 3059, (3059, (), [ (16393, 10, None, "IID('{8BE11A36-210D-41C5-AB9D-229134DCCA7E}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ImportBody' , 'strName' , 'pRefFrame' , 'strRfiFileName' , 'pImportOption' , 
			 'ppResult' , ), 3060, (3060, (), [ (8, 1, None, None) , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (8, 1, None, None) , 
			 (9, 1, None, "IID('{8BE11A36-210D-41C5-AB9D-229134DCCA7E}')") , (16393, 10, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'SwapBody' , 'strName' , 'TargetBody' , 'strRfiFileName' , 'pImportOption' , 
			 'ppResult' , ), 3061, (3061, (), [ (8, 1, None, None) , (9, 1, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , (8, 1, None, None) , 
			 (9, 1, None, "IID('{8BE11A36-210D-41C5-AB9D-229134DCCA7E}')") , (16393, 10, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ExportModeShape' , 'strRfiFileName' , 'FESoftwareType' , 'strExportFileName' , ), 3062, (3062, (), [ 
			 (8, 1, None, None) , (3, 1, None, "IID('{01D35A35-9C5A-4DD4-B8DB-CC8A5D709936}')") , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ImportStrainStressShape' , 'strRfiFileName' , 'FESoftwareType' , 'strFEResultFileName' , ), 3063, (3063, (), [ 
			 (8, 1, None, None) , (3, 1, None, "IID('{01D35A35-9C5A-4DD4-B8DB-CC8A5D709936}')") , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'GenerateStrainStressShape' , 'strRfiFileName' , 'bGenerateStrainShape' , 'bGenerateStressShape' , ), 3064, (3064, (), [ 
			 (8, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupBeam' , 'strName' , 'pMultiPoints' , 'dNodeThickness' , 'uiMeshSegment' , 
			 'ppResult' , ), 3065, (3065, (), [ (8, 1, None, None) , (8204, 1, None, None) , (5, 1, None, None) , 
			 (19, 1, None, None) , (16393, 10, None, "IID('{3C055C79-373C-4034-A146-E1E5D485D36E}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CreateRfiFileFromNASTRANOP2' , 'strRfiFileName' , 'strNASTRANFileName' , 'pNastranOP2Option' , 'pCommonOption' , 
			 'UnitFactor' , 'bSuccess' , ), 3066, (3066, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (9, 1, None, "IID('{3D4D50F5-2D1A-4618-B956-072A3EA9DD8A}')") , (9, 1, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}')") , (9, 1, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'OptimizeRFIFile' , 'pRFIOptimizerOption' , ), 3067, (3067, (), [ (9, 1, None, "IID('{7CA7CF6E-47A2-417F-8E24-056FB7F2359E}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ExportDurabilityInterface' , 'pRFlexBody' , 'pExportDurabilityInterfaceOption' , ), 3068, (3068, (), [ (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , 
			 (9, 1, None, "IID('{EB3A9E9B-54A9-440F-A594-294F547AA27A}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'ExportMDFFile' , 'pRFlexBody' , 'pExportMDFFileOption' , ), 3069, (3069, (), [ (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , 
			 (9, 1, None, "IID('{C36C3EC0-A03A-40F1-A502-8EB259B56AFB}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RFlexBodyCollection' , 'pVal' , ), 3070, (3070, (), [ (16393, 10, None, "IID('{BF6E3DD3-F1E6-4FE4-B15F-4BAE1BFCBF48}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'CreateRFlexRequest' , 'strName' , 'enType' , 'sActionNodeID' , 'pBaseMarker' , 
			 'pRefMarker' , 'ppVal' , ), 3071, (3071, (), [ (8, 1, None, None) , (3, 1, None, "IID('{02D8BDB5-7A43-482E-AB97-2C3307E32EB1}')") , 
			 (8, 1, None, None) , (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , (16393, 10, None, "IID('{E43E421D-2821-44FF-B7FA-7CDF332A240F}')") , ], 1 , 1 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'RFlexRequestCollection' , 'ppVal' , ), 3072, (3072, (), [ (16393, 10, None, "IID('{A8F96B43-230B-49EB-B315-868F472669DF}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ImportModalLoadCase' , 'RFlexBody' , 'ModalLoadCaseImportFile' , ), 3073, (3073, (), [ (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ExportModalLoadCase' , 'ModalLoadCaseExportFile' , ), 3074, (3074, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'RFlexForceCollection' , 'ppVal' , ), 3075, (3075, (), [ (16393, 10, None, "IID('{8C387B89-CD63-48E0-B37D-CCF014A3D879}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RFlexModalLoadCaseCollection' , 'ppVal' , ), 3076, (3076, (), [ (16393, 10, None, "IID('{B42BB386-EA95-4AE6-9A24-C74CB5027EB2}')") , ], 1 , 2 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'CreateModalPreload' , 'strName' , 'pVal' , 'ppVal' , ), 3077, (3077, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , (16393, 10, None, "IID('{46F35838-9402-4A28-8FE4-00FE959E31DF}')") , ], 1 , 1 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'CreateModalForce' , 'strName' , 'pIRFlexBody' , 'pVal' , 'ppVal' , 
			 ), 3078, (3078, (), [ (8, 1, None, None) , (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , (16393, 10, None, "IID('{D4583F05-0EAC-434A-BC8E-C785137C783D}')") , ], 1 , 1 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'RFIOptimizerOption' , 'ppResult' , ), 3079, (3079, (), [ (16393, 10, None, "IID('{7CA7CF6E-47A2-417F-8E24-056FB7F2359E}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceNastranOP2Option' , 'ppResult' , ), 3080, (3080, (), [ (16393, 10, None, "IID('{3D4D50F5-2D1A-4618-B956-072A3EA9DD8A}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'DurabilityInterfaceOption' , 'ppResult' , ), 3081, (3081, (), [ (16393, 10, None, "IID('{EB3A9E9B-54A9-440F-A594-294F547AA27A}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'MDFOption' , 'ppResult' , ), 3082, (3082, (), [ (16393, 10, None, "IID('{C36C3EC0-A03A-40F1-A502-8EB259B56AFB}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'Contour' , 'ppVal' , ), 3083, (3083, (), [ (16393, 10, None, "IID('{BDF4F979-28B7-48D2-BF06-9C59B70D467B}')") , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'CreateModalForceWithNodeSet' , 'strName' , 'pIRFlexBody' , 'pINodeSet' , 'pVal' , 
			 'ppVal' , ), 3084, (3084, (), [ (8, 1, None, None) , (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , (9, 1, None, "IID('{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}')") , 
			 (9, 1, None, "IID('{9573C3F4-958E-4EC2-B9E6-C4660433CFA3}')") , (16393, 10, None, "IID('{D4583F05-0EAC-434A-BC8E-C785137C783D}')") , ], 1 , 1 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'GenerateStrainStressShapeWithShellRecoveryType' , 'strRfiFileName' , 'bGenerateStrainShape' , 'bGenerateStressShape' , 'Type' , 
			 ), 3085, (3085, (), [ (8, 1, None, None) , (11, 1, None, None) , (11, 1, None, None) , (3, 1, None, "IID('{938DAAE3-9FDD-4DC6-80E4-722BEAB9C0F6}')") , ], 1 , 1 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'OutputFileGenerator' , 'ppVal' , ), 3087, (3087, (), [ (16393, 10, None, "IID('{6ED5F207-C518-4800-BA75-7990D637BAB5}')") , ], 1 , 2 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'InterfaceIdeasOption' , 'ppResult' , ), 3088, (3088, (), [ (16393, 10, None, "IID('{6DB248B8-8ACE-49F0-9B06-5065FB9AE8B0}')") , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'CreateRfiFileFromIDEASWithOption' , 'strRfiFileName' , 'strIDEASFileName' , 'pIdeasOption' , 'pCommonOption' , 
			 'UnitFactor' , 'bSuccess' , ), 3089, (3089, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (9, 1, None, "IID('{6DB248B8-8ACE-49F0-9B06-5065FB9AE8B0}')") , (9, 1, None, "IID('{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}')") , (9, 1, None, "IID('{09A65909-6FBB-488A-9726-D320F5666395}')") , (16395, 10, None, None) , ], 1 , 1 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'ToolFunction' , 'ppResult' , ), 3091, (3091, (), [ (16393, 10, None, "IID('{D2DAC4E9-E5EC-4C27-94B2-0A0CFFB24767}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'SwapBodyGeneral' , 'strName' , 'TargetBody' , 'strRfiFileName' , 'pImportOption' , 
			 'ppResult' , ), 3092, (3092, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (8, 1, None, None) , 
			 (9, 1, None, "IID('{8BE11A36-210D-41C5-AB9D-229134DCCA7E}')") , (16393, 10, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 1 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'CreateModalPressureLoad' , 'strName' , 'pPatchSet' , 'ppVal' , ), 3093, (3093, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{D81E74E6-91E4-4473-8F75-3E25C1041FE6}')") , (16393, 10, None, "IID('{FB11F962-2D23-4DD7-A6DF-0C47507310E0}')") , ], 1 , 1 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'OutputFileRegenerator' , 'ppVal' , ), 3094, (3094, (), [ (16393, 10, None, "IID('{4E476724-E71A-4106-A906-531EBAC1F17A}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'ExportDurabilityInterfaceWithVersion' , 'pRFlexBody' , 'pExportDurabilityInterfaceOption' , 'vertionType' , ), 3095, (3095, (), [ 
			 (9, 1, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , (9, 1, None, "IID('{EB3A9E9B-54A9-440F-A594-294F547AA27A}')") , (3, 1, None, "IID('{47E33FCF-3221-4FE5-ADB5-4EECC0A689A7}')") , ], 1 , 1 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'SwapBodyGeneralRefFrame' , 'strName' , 'TargetBody' , 'pRefFrame' , 'strRfiFileName' , 
			 'pImportOption' , 'ppResult' , ), 3097, (3097, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (8, 1, None, None) , (9, 1, None, "IID('{8BE11A36-210D-41C5-AB9D-229134DCCA7E}')") , (16393, 10, None, "IID('{5737600D-0E40-4578-9E18-8CBE68916DF8}')") , ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'TranslateRFIFile' , 'RFIFileName' , 'OutputFileName' , ), 3098, (3098, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}' : IRFlexInterfaceCommonOption,
	'{F1C4FF92-BC23-4F5D-AA37-02D4085B2C73}' : IRFlexInterfaceANSYSOption,
	'{3D4D50F5-2D1A-4618-B956-072A3EA9DD8A}' : IRFlexInterfaceNastranOP2Option,
	'{6DB248B8-8ACE-49F0-9B06-5065FB9AE8B0}' : IRFlexInterfaceIdeasOption,
	'{EB3A9E9B-54A9-440F-A594-294F547AA27A}' : IRFlexExportDurabilityInterfaceOption,
	'{C36C3EC0-A03A-40F1-A502-8EB259B56AFB}' : IRFlexExportMDFFileOption,
	'{F1C4FF92-BC23-4F5D-AA37-02D4085B2C76}' : IRFlexInterfaceExtraModeOption,
	'{8BE11A36-210D-41C5-AB9D-229134DCCA7E}' : IRFlexBodyImportOption,
	'{7ED2BDE4-77AC-4D41-8745-10EB8FC6812C}' : IRFlexModeInformation,
	'{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}' : IRFlexNode,
	'{E3D7FEE7-8867-4A03-B9EA-A1DD773026CC}' : IRFlexAnimationDataScaling,
	'{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}' : IRFlexElement,
	'{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}' : IRFlexElementCollection,
	'{EEEA6051-9841-4895-BC92-93F52E98A389}' : IRFlexNodeCollection,
	'{312FF880-5EB3-4AE9-A989-940D556064EE}' : IRFlexElementSet,
	'{D81E74E6-91E4-4473-8F75-3E25C1041FE6}' : IRFlexPatchSet,
	'{7C9E9609-3A15-4847-8B60-6AE1460A7A58}' : IRFlexLineSet,
	'{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}' : IRFlexNodeSet,
	'{B1A8C8FA-7869-4CB5-A285-91BCC4C2ADA3}' : IRFlexElementSetCollection,
	'{6A9E16A5-2CCC-4596-BDC0-07B767DB1A39}' : IRFlexPatchSetCollection,
	'{05938874-D404-42C9-9757-863978D57DE5}' : IRFlexLineSetCollection,
	'{2AAD6766-1ED5-498D-96BA-F9363B2DF588}' : IRFlexNodeSetCollection,
	'{5C616B86-29F2-486F-9E0C-D66502222E30}' : IRFlexOutput,
	'{D1E612A4-BFE5-4676-B55D-76C41FE47B42}' : IRFlexOutputCollection,
	'{3C055C79-373C-4034-A146-E1E5D485D36E}' : IRFlexGroupBeam,
	'{E43E421D-2821-44FF-B7FA-7CDF332A240F}' : IRFlexRequest,
	'{A8F96B43-230B-49EB-B315-868F472669DF}' : IRFlexRequestCollection,
	'{EBF8DAD1-BFE3-4A50-BF0B-2ACC1B3FA3C6}' : IRFlexModeValue,
	'{FD818ABF-BF56-4B8B-896B-01F99E1ED037}' : IRFlexModeValueCollection,
	'{DC95F017-DABD-4F7B-8E19-D6DC880124BF}' : IRFlexModalLoadValue,
	'{5104436A-9AB2-4C96-8550-F085D5BE63F9}' : IRFlexNodalLoadValue,
	'{8AEC2258-C39F-452F-BA67-11FC9D98B45A}' : IRFlexNodalLoadValueCollection,
	'{7DA762BF-839E-49E6-AB67-2C28067114CE}' : IRFlexForce,
	'{BA0F8202-4689-40C2-B583-9A907276C7D1}' : IRFlexLoad,
	'{FB11F962-2D23-4DD7-A6DF-0C47507310E0}' : IRFlexLoadPressureModal,
	'{8C387B89-CD63-48E0-B37D-CCF014A3D879}' : IRFlexForceCollection,
	'{16BD870A-FA04-42F6-8B8D-7F484F5D421E}' : IRFlexOutputFileInfo,
	'{1B06647C-BAD6-464A-8B5E-DD243D535970}' : IRFlexOutputFileInfoForRegenerator,
	'{6ED5F207-C518-4800-BA75-7990D637BAB5}' : IRFlexOutputFileGenerator,
	'{4E476724-E71A-4106-A906-531EBAC1F17A}' : IRFlexOutputFileRegenerator,
	'{5737600D-0E40-4578-9E18-8CBE68916DF8}' : IRFlexBody,
	'{BF6E3DD3-F1E6-4FE4-B15F-4BAE1BFCBF48}' : IRFlexBodyCollection,
	'{6FB3F9CE-90B7-4111-8714-AA24F53632A6}' : IRFlexModalLoadCase,
	'{B42BB386-EA95-4AE6-9A24-C74CB5027EB2}' : IRFlexModalLoadCaseCollection,
	'{EE8ABAE9-396E-46FB-B11F-AD1471097DAF}' : IRFlexForceModalPreloadInfo,
	'{05ADCCED-A6D5-4E30-A946-DBA87CAC5F0B}' : IRFlexForceModalPreloadInfoCollection,
	'{5A81CC6A-C0E7-4B23-8E27-CD06F1E2CC13}' : IRFlexForceModalForceInfo,
	'{BED48F30-1BA6-40B0-80C6-ED2650A5E796}' : IRFlexForceModalForceInfoCollection,
	'{46F35838-9402-4A28-8FE4-00FE959E31DF}' : IRFlexForceModalPreload,
	'{D4583F05-0EAC-434A-BC8E-C785137C783D}' : IRFlexForceModalForce,
	'{7CA7CF6E-47A2-417F-8E24-056FB7F2359E}' : IRFlexRFIOptimizerOption,
	'{D2DAC4E9-E5EC-4C27-94B2-0A0CFFB24767}' : IRFlexToolFunction,
	'{7AAF53D9-9777-4B5D-827C-62A822442B49}' : IRFlexToolkit,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}' : 'IRFlexInterfaceCommonOption',
	'{F1C4FF92-BC23-4F5D-AA37-02D4085B2C73}' : 'IRFlexInterfaceANSYSOption',
	'{3D4D50F5-2D1A-4618-B956-072A3EA9DD8A}' : 'IRFlexInterfaceNastranOP2Option',
	'{6DB248B8-8ACE-49F0-9B06-5065FB9AE8B0}' : 'IRFlexInterfaceIdeasOption',
	'{EB3A9E9B-54A9-440F-A594-294F547AA27A}' : 'IRFlexExportDurabilityInterfaceOption',
	'{C36C3EC0-A03A-40F1-A502-8EB259B56AFB}' : 'IRFlexExportMDFFileOption',
	'{F1C4FF92-BC23-4F5D-AA37-02D4085B2C76}' : 'IRFlexInterfaceExtraModeOption',
	'{8BE11A36-210D-41C5-AB9D-229134DCCA7E}' : 'IRFlexBodyImportOption',
	'{7ED2BDE4-77AC-4D41-8745-10EB8FC6812C}' : 'IRFlexModeInformation',
	'{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}' : 'IRFlexNode',
	'{E3D7FEE7-8867-4A03-B9EA-A1DD773026CC}' : 'IRFlexAnimationDataScaling',
	'{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}' : 'IRFlexElement',
	'{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}' : 'IRFlexElementCollection',
	'{EEEA6051-9841-4895-BC92-93F52E98A389}' : 'IRFlexNodeCollection',
	'{312FF880-5EB3-4AE9-A989-940D556064EE}' : 'IRFlexElementSet',
	'{D81E74E6-91E4-4473-8F75-3E25C1041FE6}' : 'IRFlexPatchSet',
	'{7C9E9609-3A15-4847-8B60-6AE1460A7A58}' : 'IRFlexLineSet',
	'{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}' : 'IRFlexNodeSet',
	'{B1A8C8FA-7869-4CB5-A285-91BCC4C2ADA3}' : 'IRFlexElementSetCollection',
	'{6A9E16A5-2CCC-4596-BDC0-07B767DB1A39}' : 'IRFlexPatchSetCollection',
	'{05938874-D404-42C9-9757-863978D57DE5}' : 'IRFlexLineSetCollection',
	'{2AAD6766-1ED5-498D-96BA-F9363B2DF588}' : 'IRFlexNodeSetCollection',
	'{5C616B86-29F2-486F-9E0C-D66502222E30}' : 'IRFlexOutput',
	'{D1E612A4-BFE5-4676-B55D-76C41FE47B42}' : 'IRFlexOutputCollection',
	'{3C055C79-373C-4034-A146-E1E5D485D36E}' : 'IRFlexGroupBeam',
	'{E43E421D-2821-44FF-B7FA-7CDF332A240F}' : 'IRFlexRequest',
	'{A8F96B43-230B-49EB-B315-868F472669DF}' : 'IRFlexRequestCollection',
	'{EBF8DAD1-BFE3-4A50-BF0B-2ACC1B3FA3C6}' : 'IRFlexModeValue',
	'{FD818ABF-BF56-4B8B-896B-01F99E1ED037}' : 'IRFlexModeValueCollection',
	'{DC95F017-DABD-4F7B-8E19-D6DC880124BF}' : 'IRFlexModalLoadValue',
	'{5104436A-9AB2-4C96-8550-F085D5BE63F9}' : 'IRFlexNodalLoadValue',
	'{8AEC2258-C39F-452F-BA67-11FC9D98B45A}' : 'IRFlexNodalLoadValueCollection',
	'{7DA762BF-839E-49E6-AB67-2C28067114CE}' : 'IRFlexForce',
	'{BA0F8202-4689-40C2-B583-9A907276C7D1}' : 'IRFlexLoad',
	'{FB11F962-2D23-4DD7-A6DF-0C47507310E0}' : 'IRFlexLoadPressureModal',
	'{8C387B89-CD63-48E0-B37D-CCF014A3D879}' : 'IRFlexForceCollection',
	'{16BD870A-FA04-42F6-8B8D-7F484F5D421E}' : 'IRFlexOutputFileInfo',
	'{1B06647C-BAD6-464A-8B5E-DD243D535970}' : 'IRFlexOutputFileInfoForRegenerator',
	'{6ED5F207-C518-4800-BA75-7990D637BAB5}' : 'IRFlexOutputFileGenerator',
	'{4E476724-E71A-4106-A906-531EBAC1F17A}' : 'IRFlexOutputFileRegenerator',
	'{5737600D-0E40-4578-9E18-8CBE68916DF8}' : 'IRFlexBody',
	'{BF6E3DD3-F1E6-4FE4-B15F-4BAE1BFCBF48}' : 'IRFlexBodyCollection',
	'{6FB3F9CE-90B7-4111-8714-AA24F53632A6}' : 'IRFlexModalLoadCase',
	'{B42BB386-EA95-4AE6-9A24-C74CB5027EB2}' : 'IRFlexModalLoadCaseCollection',
	'{EE8ABAE9-396E-46FB-B11F-AD1471097DAF}' : 'IRFlexForceModalPreloadInfo',
	'{05ADCCED-A6D5-4E30-A946-DBA87CAC5F0B}' : 'IRFlexForceModalPreloadInfoCollection',
	'{5A81CC6A-C0E7-4B23-8E27-CD06F1E2CC13}' : 'IRFlexForceModalForceInfo',
	'{BED48F30-1BA6-40B0-80C6-ED2650A5E796}' : 'IRFlexForceModalForceInfoCollection',
	'{46F35838-9402-4A28-8FE4-00FE959E31DF}' : 'IRFlexForceModalPreload',
	'{D4583F05-0EAC-434A-BC8E-C785137C783D}' : 'IRFlexForceModalForce',
	'{7CA7CF6E-47A2-417F-8E24-056FB7F2359E}' : 'IRFlexRFIOptimizerOption',
	'{D2DAC4E9-E5EC-4C27-94B2-0A0CFFB24767}' : 'IRFlexToolFunction',
	'{7AAF53D9-9777-4B5D-827C-62A822442B49}' : 'IRFlexToolkit',
}


NamesToIIDMap = {
	'IRFlexInterfaceCommonOption' : '{F1C4FF92-BC23-4F5D-AA37-02D4085B2C72}',
	'IRFlexInterfaceANSYSOption' : '{F1C4FF92-BC23-4F5D-AA37-02D4085B2C73}',
	'IRFlexInterfaceNastranOP2Option' : '{3D4D50F5-2D1A-4618-B956-072A3EA9DD8A}',
	'IRFlexInterfaceIdeasOption' : '{6DB248B8-8ACE-49F0-9B06-5065FB9AE8B0}',
	'IRFlexExportDurabilityInterfaceOption' : '{EB3A9E9B-54A9-440F-A594-294F547AA27A}',
	'IRFlexExportMDFFileOption' : '{C36C3EC0-A03A-40F1-A502-8EB259B56AFB}',
	'IRFlexInterfaceExtraModeOption' : '{F1C4FF92-BC23-4F5D-AA37-02D4085B2C76}',
	'IRFlexBodyImportOption' : '{8BE11A36-210D-41C5-AB9D-229134DCCA7E}',
	'IRFlexModeInformation' : '{7ED2BDE4-77AC-4D41-8745-10EB8FC6812C}',
	'IRFlexNode' : '{676058EF-4A4E-4E4E-BBBF-2150FFBE932C}',
	'IRFlexAnimationDataScaling' : '{E3D7FEE7-8867-4A03-B9EA-A1DD773026CC}',
	'IRFlexElement' : '{D4391208-4F5B-4A0C-80B0-8CBF5F198DBB}',
	'IRFlexElementCollection' : '{0D1751C5-008C-4B1A-9B5D-41CD0E76D87A}',
	'IRFlexNodeCollection' : '{EEEA6051-9841-4895-BC92-93F52E98A389}',
	'IRFlexElementSet' : '{312FF880-5EB3-4AE9-A989-940D556064EE}',
	'IRFlexPatchSet' : '{D81E74E6-91E4-4473-8F75-3E25C1041FE6}',
	'IRFlexLineSet' : '{7C9E9609-3A15-4847-8B60-6AE1460A7A58}',
	'IRFlexNodeSet' : '{26BFA995-9AE3-41D6-9F5B-B3699DC551A8}',
	'IRFlexElementSetCollection' : '{B1A8C8FA-7869-4CB5-A285-91BCC4C2ADA3}',
	'IRFlexPatchSetCollection' : '{6A9E16A5-2CCC-4596-BDC0-07B767DB1A39}',
	'IRFlexLineSetCollection' : '{05938874-D404-42C9-9757-863978D57DE5}',
	'IRFlexNodeSetCollection' : '{2AAD6766-1ED5-498D-96BA-F9363B2DF588}',
	'IRFlexOutput' : '{5C616B86-29F2-486F-9E0C-D66502222E30}',
	'IRFlexOutputCollection' : '{D1E612A4-BFE5-4676-B55D-76C41FE47B42}',
	'IRFlexGroupBeam' : '{3C055C79-373C-4034-A146-E1E5D485D36E}',
	'IRFlexRequest' : '{E43E421D-2821-44FF-B7FA-7CDF332A240F}',
	'IRFlexRequestCollection' : '{A8F96B43-230B-49EB-B315-868F472669DF}',
	'IRFlexModeValue' : '{EBF8DAD1-BFE3-4A50-BF0B-2ACC1B3FA3C6}',
	'IRFlexModeValueCollection' : '{FD818ABF-BF56-4B8B-896B-01F99E1ED037}',
	'IRFlexModalLoadValue' : '{DC95F017-DABD-4F7B-8E19-D6DC880124BF}',
	'IRFlexNodalLoadValue' : '{5104436A-9AB2-4C96-8550-F085D5BE63F9}',
	'IRFlexNodalLoadValueCollection' : '{8AEC2258-C39F-452F-BA67-11FC9D98B45A}',
	'IRFlexForce' : '{7DA762BF-839E-49E6-AB67-2C28067114CE}',
	'IRFlexLoad' : '{BA0F8202-4689-40C2-B583-9A907276C7D1}',
	'IRFlexLoadPressureModal' : '{FB11F962-2D23-4DD7-A6DF-0C47507310E0}',
	'IRFlexForceCollection' : '{8C387B89-CD63-48E0-B37D-CCF014A3D879}',
	'IRFlexOutputFileInfo' : '{16BD870A-FA04-42F6-8B8D-7F484F5D421E}',
	'IRFlexOutputFileInfoForRegenerator' : '{1B06647C-BAD6-464A-8B5E-DD243D535970}',
	'IRFlexOutputFileGenerator' : '{6ED5F207-C518-4800-BA75-7990D637BAB5}',
	'IRFlexOutputFileRegenerator' : '{4E476724-E71A-4106-A906-531EBAC1F17A}',
	'IRFlexBody' : '{5737600D-0E40-4578-9E18-8CBE68916DF8}',
	'IRFlexBodyCollection' : '{BF6E3DD3-F1E6-4FE4-B15F-4BAE1BFCBF48}',
	'IRFlexModalLoadCase' : '{6FB3F9CE-90B7-4111-8714-AA24F53632A6}',
	'IRFlexModalLoadCaseCollection' : '{B42BB386-EA95-4AE6-9A24-C74CB5027EB2}',
	'IRFlexForceModalPreloadInfo' : '{EE8ABAE9-396E-46FB-B11F-AD1471097DAF}',
	'IRFlexForceModalPreloadInfoCollection' : '{05ADCCED-A6D5-4E30-A946-DBA87CAC5F0B}',
	'IRFlexForceModalForceInfo' : '{5A81CC6A-C0E7-4B23-8E27-CD06F1E2CC13}',
	'IRFlexForceModalForceInfoCollection' : '{BED48F30-1BA6-40B0-80C6-ED2650A5E796}',
	'IRFlexForceModalPreload' : '{46F35838-9402-4A28-8FE4-00FE959E31DF}',
	'IRFlexForceModalForce' : '{D4583F05-0EAC-434A-BC8E-C785137C783D}',
	'IRFlexRFIOptimizerOption' : '{7CA7CF6E-47A2-417F-8E24-056FB7F2359E}',
	'IRFlexToolFunction' : '{D2DAC4E9-E5EC-4C27-94B2-0A0CFFB24767}',
	'IRFlexToolkit' : '{7AAF53D9-9777-4B5D-827C-62A822442B49}',
}


