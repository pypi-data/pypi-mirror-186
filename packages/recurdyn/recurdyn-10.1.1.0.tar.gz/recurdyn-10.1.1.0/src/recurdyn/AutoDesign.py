# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMAutoDesign.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMAutoDesign Type Library'
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

CLSID = IID('{35B0CF77-CB1A-4C8B-BCAD-A4D0E544EB71}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class ADProcessNetType(IntEnum):
	'''
	ADProcessNetType enumeration.
	'''
	ADProcessNet_General          =1         
	'''Constant value is 1.'''
	ADProcessNet_Python           =2         
	'''Constant value is 2.'''
	ADProcessNet_VSTA             =0         
	'''Constant value is 0.'''
class ADSimulationType(IntEnum):
	'''
	ADSimulationType enumeration.
	'''
	ADSimulation_DynKinematic     =0         
	'''Constant value is 0.'''
	ADSimulation_Static           =1         
	'''Constant value is 1.'''
class AnalysisResponseType(IntEnum):
	'''
	AnalysisResponseType enumeration.
	'''
	AnalysisResponse_Basic        =0         
	'''Constant value is 0.'''
	AnalysisResponse_FEResult     =1         
	'''Constant value is 1.'''
	AnalysisResponse_ProcessNet   =3         
	'''Constant value is 3.'''
	AnalysisResponse_Scope        =2         
	'''Constant value is 2.'''
class CheckFlagType(IntEnum):
	'''
	CheckFlagType enumeration.
	'''
	CheckFlag_Export              =1         
	'''Constant value is 1.'''
	CheckFlag_Get                 =0         
	'''Constant value is 0.'''
class CombinationType(IntEnum):
	'''
	CombinationType enumeration.
	'''
	Combination_MAX               =1         
	'''Constant value is 1.'''
	Combination_MIN               =0         
	'''Constant value is 0.'''
class ConfigurationDesignType(IntEnum):
	'''
	ConfigurationDesignType enumeration.
	'''
	ConfigurationDesign_OFF       =1         
	'''Constant value is 1.'''
	ConfigurationDesign_ON        =0         
	'''Constant value is 0.'''
class ConstraintGoalType(IntEnum):
	'''
	ConstraintGoalType enumeration.
	'''
	ConstraintGoal_EQ             =0         
	'''Constant value is 0.'''
	ConstraintGoal_GE             =2         
	'''Constant value is 2.'''
	ConstraintGoal_LE             =1         
	'''Constant value is 1.'''
class ConvergenceRelaxationControlType(IntEnum):
	'''
	ConvergenceRelaxationControlType enumeration.
	'''
	ConvergenceRelaxationControl_OFF=0         
	'''Constant value is 0.'''
	ConvergenceRelaxationControl_ON=1         
	'''Constant value is 1.'''
class DOEMethodType(IntEnum):
	'''
	DOEMethodType enumeration.
	'''
	DOEMethod_BoseOrthogonalArray =5         
	'''Constant value is 5.'''
	DOEMethod_ExtendedPlackettBurman=0         
	'''Constant value is 0.'''
	DOEMethod_FullFactorialDesign =1         
	'''Constant value is 1.'''
	DOEMethod_LevelBalancedDescriptiveDesign=3         
	'''Constant value is 3.'''
	DOEMethod_ThreelevelOrthogonalArray=2         
	'''Constant value is 2.'''
	DOEMethod_TwoLevelOrthogonalArray=4         
	'''Constant value is 4.'''
class DPFormType(IntEnum):
	'''
	DPFormType enumeration.
	'''
	DPForm_Scale                  =1         
	'''Constant value is 1.'''
	DPForm_Value                  =0         
	'''Constant value is 0.'''
class DefinitionType(IntEnum):
	'''
	DefinitionType enumeration.
	'''
	Definition_Constraint         =1         
	'''Constant value is 1.'''
	Definition_Objective          =0         
	'''Constant value is 0.'''
class DesignParameterType(IntEnum):
	'''
	DesignParameterType enumeration.
	'''
	DesignParameter_Angular       =4         
	'''Constant value is 4.'''
	DesignParameter_Cylindrical   =2         
	'''Constant value is 2.'''
	DesignParameter_Direct        =0         
	'''Constant value is 0.'''
	DesignParameter_Spherical     =3         
	'''Constant value is 3.'''
	DesignParameter_Translational =1         
	'''Constant value is 1.'''
class DesignVariableType(IntEnum):
	'''
	DesignVariableType enumeration.
	'''
	DesignVariable_Constant       =1         
	'''Constant value is 1.'''
	DesignVariable_Variable       =0         
	'''Constant value is 0.'''
class DeviationType(IntEnum):
	'''
	DeviationType enumeration.
	'''
	Deviation_COV                 =1         
	'''Constant value is 1.'''
	Deviation_SD                  =0         
	'''Constant value is 0.'''
class ExportDataType(IntEnum):
	'''
	ExportDataType enumeration.
	'''
	ExportData_AR                 =4         
	'''Constant value is 4.'''
	ExportData_All                =6         
	'''Constant value is 6.'''
	ExportData_DV                 =5         
	'''Constant value is 5.'''
	ExportData_DesignCost         =0         
	'''Constant value is 0.'''
	ExportData_SimulationDescription=1         
	'''Constant value is 1.'''
	ExportData_SimulationStatus   =2         
	'''Constant value is 2.'''
	ExportData_Violation          =3         
	'''Constant value is 3.'''
class ExtendedPlackettBurmanLevelType(IntEnum):
	'''
	ExtendedPlackettBurmanLevelType enumeration.
	'''
	ExtendedPlackettBurmanLevel_Level2=0         
	'''Constant value is 0.'''
	ExtendedPlackettBurmanLevel_Level3=1         
	'''Constant value is 1.'''
	ExtendedPlackettBurmanLevel_Level4=2         
	'''Constant value is 2.'''
class FEResultType(IntEnum):
	'''
	FEResultType enumeration.
	'''
	FEResult_Mass_ElementSet      =2         
	'''Constant value is 2.'''
	FEResult_Stress_ElementSet    =1         
	'''Constant value is 1.'''
	FEResult_Stress_NodeSet       =0         
	'''Constant value is 0.'''
class FETreatmentType(IntEnum):
	'''
	FETreatmentType enumeration.
	'''
	FETreatment_AverageValue      =3         
	'''Constant value is 3.'''
	FETreatment_EndValue          =2         
	'''Constant value is 2.'''
	FETreatment_InitialValue      =1         
	'''Constant value is 1.'''
	FETreatment_MaxValue          =5         
	'''Constant value is 5.'''
	FETreatment_MinValue          =4         
	'''Constant value is 4.'''
class FullFactorialDesignLevelType(IntEnum):
	'''
	FullFactorialDesignLevelType enumeration.
	'''
	FullFactorialDesignLevel_Level2=0         
	'''Constant value is 0.'''
	FullFactorialDesignLevel_Level3=1         
	'''Constant value is 1.'''
	FullFactorialDesignLevel_Level4=2         
	'''Constant value is 2.'''
	FullFactorialDesignLevel_Level5=3         
	'''Constant value is 3.'''
class HybridSamplingOptionType(IntEnum):
	'''
	HybridSamplingOptionType enumeration.
	'''
	HybridSamplingOption_GetFromSimulationHistory=2         
	'''Constant value is 2.'''
	HybridSamplingOption_KoshalMethod=0         
	'''Constant value is 0.'''
	HybridSamplingOption_LatinHypercubeSample=1         
	'''Constant value is 1.'''
class MetaModelDOEMethodType(IntEnum):
	'''
	MetaModelDOEMethodType enumeration.
	'''
	MetaModelDOEMethod_BoxAndBehnkenDesign=2         
	'''Constant value is 2.'''
	MetaModelDOEMethod_CentralCompositeDesign=1         
	'''Constant value is 1.'''
	MetaModelDOEMethod_DiscreteLatinHypercubeDesign=3         
	'''Constant value is 3.'''
	MetaModelDOEMethod_GeneralizedSmallCompositeDesign=0         
	'''Constant value is 0.'''
	MetaModelDOEMethod_IncompleteSmallCompositeDesign1=4         
	'''Constant value is 4.'''
	MetaModelDOEMethod_IncompleteSmallCompositeDesign2=5         
	'''Constant value is 5.'''
class MetaModelingMethodType(IntEnum):
	'''
	MetaModelingMethodType enumeration.
	'''
	MetaModelingMethod_Gaussian   =1         
	'''Constant value is 1.'''
	MetaModelingMethod_KrigingDACEModel=0         
	'''Constant value is 0.'''
	MetaModelingMethod_MultiQuadratic=2         
	'''Constant value is 2.'''
	MetaModelingMethod_ResponseSurfaceModel=3         
	'''Constant value is 3.'''
class ObjectiveGoalType(IntEnum):
	'''
	ObjectiveGoalType enumeration.
	'''
	ObjectiveGoal_MAX             =1         
	'''Constant value is 1.'''
	ObjectiveGoal_MIN             =0         
	'''Constant value is 0.'''
class PolynomialFunctionType(IntEnum):
	'''
	PolynomialFunctionType enumeration.
	'''
	PolynomialFunction_Auto       =0         
	'''Constant value is 0.'''
	PolynomialFunction_CompleteQuadraticModel=3         
	'''Constant value is 3.'''
	PolynomialFunction_ConstantModel=1         
	'''Constant value is 1.'''
	PolynomialFunction_HybridLinear=6         
	'''Constant value is 6.'''
	PolynomialFunction_LinearModel=2         
	'''Constant value is 2.'''
	PolynomialFunction_PureCubicModel=5         
	'''Constant value is 5.'''
	PolynomialFunction_PureQuadraticModel=4         
	'''Constant value is 4.'''
class ProbabilityDistributionType(IntEnum):
	'''
	ProbabilityDistributionType enumeration.
	'''
	ProbabilityDistribution_Beta  =11        
	'''Constant value is 11.'''
	ProbabilityDistribution_LogNormal=2         
	'''Constant value is 2.'''
	ProbabilityDistribution_Normal=1         
	'''Constant value is 1.'''
	ProbabilityDistribution_OneEVD_Max=3         
	'''Constant value is 3.'''
	ProbabilityDistribution_OneEVD_Min=4         
	'''Constant value is 4.'''
	ProbabilityDistribution_ThreeEVD_Max=7         
	'''Constant value is 7.'''
	ProbabilityDistribution_ThreeEVD_Min=8         
	'''Constant value is 8.'''
	ProbabilityDistribution_TwoEVD_Max=5         
	'''Constant value is 5.'''
	ProbabilityDistribution_TwoEVD_Min=6         
	'''Constant value is 6.'''
	ProbabilityDistribution_Uniform=10        
	'''Constant value is 10.'''
	ProbabilityDistribution_Weibull_Gnedenko=9         
	'''Constant value is 9.'''
class ReliabilityConstraintGoalType(IntEnum):
	'''
	ReliabilityConstraintGoalType enumeration.
	'''
	ReliabilityConstraintGoal_GE  =0         
	'''Constant value is 0.'''
	ReliabilityConstraintGoal_LE  =1         
	'''Constant value is 1.'''
class ReliablitySolverType(IntEnum):
	'''
	ReliablitySolverType enumeration.
	'''
	ReliablitySolver_AFORM        =0         
	'''Constant value is 0.'''
	ReliablitySolver_AFORM_DRM1   =1         
	'''Constant value is 1.'''
	ReliablitySolver_AFORM_DRM2   =2         
	'''Constant value is 2.'''
class SamplingMethodType(IntEnum):
	'''
	SamplingMethodType enumeration.
	'''
	SamplingMethod_LatinHypercubeDesign=0         
	'''Constant value is 0.'''
	SamplingMethod_RandomSampling =1         
	'''Constant value is 1.'''
class SimulationStatusType(IntEnum):
	'''
	SimulationStatusType enumeration.
	'''
	SimulationStatus_Duplication  =3         
	'''Constant value is 3.'''
	SimulationStatus_Failure      =2         
	'''Constant value is 2.'''
	SimulationStatus_None         =0         
	'''Constant value is 0.'''
	SimulationStatus_Success      =1         
	'''Constant value is 1.'''
class StatisticalInfoType(IntEnum):
	'''
	StatisticalInfoType enumeration.
	'''
	StatisticalInfo_Deterministic =1         
	'''Constant value is 1.'''
	StatisticalInfo_Random        =0         
	'''Constant value is 0.'''
class TreatmentType(IntEnum):
	'''
	TreatmentType enumeration.
	'''
	Treatment_AverageValue        =3         
	'''Constant value is 3.'''
	Treatment_EndValue            =2         
	'''Constant value is 2.'''
	Treatment_InitialValue        =1         
	'''Constant value is 1.'''
	Treatment_MaxABSValue         =7         
	'''Constant value is 7.'''
	Treatment_MaxDevValue         =9         
	'''Constant value is 9.'''
	Treatment_MaxValue            =5         
	'''Constant value is 5.'''
	Treatment_MinABSValue         =6         
	'''Constant value is 6.'''
	Treatment_MinValue            =4         
	'''Constant value is 4.'''
	Treatment_None                =0         
	'''Constant value is 0.'''
	Treatment_RMSValue            =8         
	'''Constant value is 8.'''
	Treatment_SDValue             =10        
	'''Constant value is 10.'''
class ValidationType(IntEnum):
	'''
	ValidationType enumeration.
	'''
	Validation_None               =0         
	'''Constant value is 0.'''
	Validation_Validation         =1         
	'''Constant value is 1.'''
	Validation_Validation_ReOptimization=2         
	'''Constant value is 2.'''
class VarianceEstimationMethodType(IntEnum):
	'''
	VarianceEstimationMethodType enumeration.
	'''
	VarianceEstimationMethod_RandomSampling=2         
	'''Constant value is 2.'''
	VarianceEstimationMethod_TaylorSeries=1         
	'''Constant value is 1.'''

from win32com.client import DispatchBaseClass
class IADAnalysisControlMonteCarloReliability(DispatchBaseClass):
	'''Analysis Control - MonteCarlo Reliability'''
	CLSID = IID('{D8BE75E5-32E7-42DF-A930-8A591F57583B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_SamplingMethodType(self):
		return self._ApplyTypes_(*(12053, 2, (3, 0), (), "SamplingMethodType", '{53ECF8FC-F2B6-4C59-8C1D-F43035C81E6E}'))
	def _get_SamplingPoints(self):
		return self._ApplyTypes_(*(12052, 2, (19, 0), (), "SamplingPoints", None))
	def _get_SaveResult(self):
		return self._ApplyTypes_(*(12003, 2, (8, 0), (), "SaveResult", None))
	def _get_SimulationType(self):
		return self._ApplyTypes_(*(12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'))
	def _get_UseNewSampling(self):
		return self._ApplyTypes_(*(12051, 2, (11, 0), (), "UseNewSampling", None))
	def _get_UseSaveResult(self):
		return self._ApplyTypes_(*(12002, 2, (11, 0), (), "UseSaveResult", None))

	def _set_SamplingMethodType(self, value):
		if "SamplingMethodType" in self.__dict__: self.__dict__["SamplingMethodType"] = value; return
		self._oleobj_.Invoke(*((12053, LCID, 4, 0) + (value,) + ()))
	def _set_SamplingPoints(self, value):
		if "SamplingPoints" in self.__dict__: self.__dict__["SamplingPoints"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_SaveResult(self, value):
		if "SaveResult" in self.__dict__: self.__dict__["SaveResult"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_SimulationType(self, value):
		if "SimulationType" in self.__dict__: self.__dict__["SimulationType"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UseNewSampling(self, value):
		if "UseNewSampling" in self.__dict__: self.__dict__["UseNewSampling"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_UseSaveResult(self, value):
		if "UseSaveResult" in self.__dict__: self.__dict__["UseSaveResult"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))

	SamplingMethodType = property(_get_SamplingMethodType, _set_SamplingMethodType)
	'''
	Sampling Method Type

	:type: recurdyn.AutoDesign.SamplingMethodType
	'''
	SamplingPoints = property(_get_SamplingPoints, _set_SamplingPoints)
	'''
	Number of Sampling Points

	:type: int
	'''
	SaveResult = property(_get_SaveResult, _set_SaveResult)
	'''
	Save results

	:type: str
	'''
	SimulationType = property(_get_SimulationType, _set_SimulationType)
	'''
	Simulation Type

	:type: recurdyn.AutoDesign.ADSimulationType
	'''
	UseNewSampling = property(_get_UseNewSampling, _set_UseNewSampling)
	'''
	Use New Sampling

	:type: bool
	'''
	UseSaveResult = property(_get_UseSaveResult, _set_UseSaveResult)
	'''
	Use save results

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_SamplingMethodType": _set_SamplingMethodType,
		"_set_SamplingPoints": _set_SamplingPoints,
		"_set_SaveResult": _set_SaveResult,
		"_set_SimulationType": _set_SimulationType,
		"_set_UseNewSampling": _set_UseNewSampling,
		"_set_UseSaveResult": _set_UseSaveResult,
	}
	_prop_map_get_ = {
		"SamplingMethodType": (12053, 2, (3, 0), (), "SamplingMethodType", '{53ECF8FC-F2B6-4C59-8C1D-F43035C81E6E}'),
		"SamplingPoints": (12052, 2, (19, 0), (), "SamplingPoints", None),
		"SaveResult": (12003, 2, (8, 0), (), "SaveResult", None),
		"SimulationType": (12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'),
		"UseNewSampling": (12051, 2, (11, 0), (), "UseNewSampling", None),
		"UseSaveResult": (12002, 2, (11, 0), (), "UseSaveResult", None),
	}
	_prop_map_put_ = {
		"SamplingMethodType": ((12053, LCID, 4, 0),()),
		"SamplingPoints": ((12052, LCID, 4, 0),()),
		"SaveResult": ((12003, LCID, 4, 0),()),
		"SimulationType": ((12001, LCID, 4, 0),()),
		"UseNewSampling": ((12051, LCID, 4, 0),()),
		"UseSaveResult": ((12002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADAnalysisControlSAOReliability(DispatchBaseClass):
	'''Analysis Control - SAOReliability'''
	CLSID = IID('{9CF67D49-AFD5-46EA-B69E-50E384C63F41}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ConvergenceTolerance(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "ConvergenceTolerance", '{97D04758-E009-46C2-BE5F-AD4A1CB49AB5}'))
	def _get_HybridSamplingOptionType(self):
		return self._ApplyTypes_(*(12052, 2, (3, 0), (), "HybridSamplingOptionType", '{257F16C6-873D-4022-9DD6-D4D93F476387}'))
	def _get_LatinHybercubeSample(self):
		return self._ApplyTypes_(*(12054, 2, (5, 0), (), "LatinHybercubeSample", None))
	def _get_ReliablitySolverType(self):
		return self._ApplyTypes_(*(12053, 2, (3, 0), (), "ReliablitySolverType", '{3C183DD5-59F1-4593-8DF6-3F9AF6540039}'))
	def _get_SaveResult(self):
		return self._ApplyTypes_(*(12003, 2, (8, 0), (), "SaveResult", None))
	def _get_SimulationType(self):
		return self._ApplyTypes_(*(12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'))
	def _get_UseSaveResult(self):
		return self._ApplyTypes_(*(12002, 2, (11, 0), (), "UseSaveResult", None))

	def _set_HybridSamplingOptionType(self, value):
		if "HybridSamplingOptionType" in self.__dict__: self.__dict__["HybridSamplingOptionType"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_LatinHybercubeSample(self, value):
		if "LatinHybercubeSample" in self.__dict__: self.__dict__["LatinHybercubeSample"] = value; return
		self._oleobj_.Invoke(*((12054, LCID, 4, 0) + (value,) + ()))
	def _set_ReliablitySolverType(self, value):
		if "ReliablitySolverType" in self.__dict__: self.__dict__["ReliablitySolverType"] = value; return
		self._oleobj_.Invoke(*((12053, LCID, 4, 0) + (value,) + ()))
	def _set_SaveResult(self, value):
		if "SaveResult" in self.__dict__: self.__dict__["SaveResult"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_SimulationType(self, value):
		if "SimulationType" in self.__dict__: self.__dict__["SimulationType"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UseSaveResult(self, value):
		if "UseSaveResult" in self.__dict__: self.__dict__["UseSaveResult"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))

	ConvergenceTolerance = property(_get_ConvergenceTolerance, None)
	'''
	Convergence Tolerance

	:type: recurdyn.AutoDesign.IADConvergenceTolerance
	'''
	HybridSamplingOptionType = property(_get_HybridSamplingOptionType, _set_HybridSamplingOptionType)
	'''
	Sampling Option Type for Hybrid Method

	:type: recurdyn.AutoDesign.HybridSamplingOptionType
	'''
	LatinHybercubeSample = property(_get_LatinHybercubeSample, _set_LatinHybercubeSample)
	'''
	LatinHybercube Sample

	:type: float
	'''
	ReliablitySolverType = property(_get_ReliablitySolverType, _set_ReliablitySolverType)
	'''
	Reliablity Solver Type

	:type: recurdyn.AutoDesign.ReliablitySolverType
	'''
	SaveResult = property(_get_SaveResult, _set_SaveResult)
	'''
	Save results

	:type: str
	'''
	SimulationType = property(_get_SimulationType, _set_SimulationType)
	'''
	Simulation Type

	:type: recurdyn.AutoDesign.ADSimulationType
	'''
	UseSaveResult = property(_get_UseSaveResult, _set_UseSaveResult)
	'''
	Use save results

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_HybridSamplingOptionType": _set_HybridSamplingOptionType,
		"_set_LatinHybercubeSample": _set_LatinHybercubeSample,
		"_set_ReliablitySolverType": _set_ReliablitySolverType,
		"_set_SaveResult": _set_SaveResult,
		"_set_SimulationType": _set_SimulationType,
		"_set_UseSaveResult": _set_UseSaveResult,
	}
	_prop_map_get_ = {
		"ConvergenceTolerance": (12051, 2, (9, 0), (), "ConvergenceTolerance", '{97D04758-E009-46C2-BE5F-AD4A1CB49AB5}'),
		"HybridSamplingOptionType": (12052, 2, (3, 0), (), "HybridSamplingOptionType", '{257F16C6-873D-4022-9DD6-D4D93F476387}'),
		"LatinHybercubeSample": (12054, 2, (5, 0), (), "LatinHybercubeSample", None),
		"ReliablitySolverType": (12053, 2, (3, 0), (), "ReliablitySolverType", '{3C183DD5-59F1-4593-8DF6-3F9AF6540039}'),
		"SaveResult": (12003, 2, (8, 0), (), "SaveResult", None),
		"SimulationType": (12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'),
		"UseSaveResult": (12002, 2, (11, 0), (), "UseSaveResult", None),
	}
	_prop_map_put_ = {
		"HybridSamplingOptionType": ((12052, LCID, 4, 0),()),
		"LatinHybercubeSample": ((12054, LCID, 4, 0),()),
		"ReliablitySolverType": ((12053, LCID, 4, 0),()),
		"SaveResult": ((12003, LCID, 4, 0),()),
		"SimulationType": ((12001, LCID, 4, 0),()),
		"UseSaveResult": ((12002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADAnalysisResponse(DispatchBaseClass):
	'''AnalysisResponse'''
	CLSID = IID('{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')
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


	def _get_AnalysisResponseType(self):
		return self._ApplyTypes_(*(12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))
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
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	AnalysisResponseType = property(_get_AnalysisResponseType, None)
	'''
	Analysis Response Type

	:type: recurdyn.AutoDesign.AnalysisResponseType
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

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
	Use = property(_get_Use, _set_Use)
	'''
	Use PI

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Description": _set_Description,
		"_set_Name": _set_Name,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"AnalysisResponseType": (12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Description": ((12002, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADAnalysisResponseBasic(DispatchBaseClass):
	'''AnalysisResponse - Basic'''
	CLSID = IID('{1F6675E9-0D4F-48E3-8957-D50DD217490D}')
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


	def _get_AnalysisResponseType(self):
		return self._ApplyTypes_(*(12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))
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
	def _get_ResultOutput(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "ResultOutput", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'))
	def _get_TreatmentType(self):
		return self._ApplyTypes_(*(12052, 2, (3, 0), (), "TreatmentType", '{90F45D5E-BEB4-47B0-9296-7DC9AA0ECDAC}'))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ResultOutput(self, value):
		if "ResultOutput" in self.__dict__: self.__dict__["ResultOutput"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_TreatmentType(self, value):
		if "TreatmentType" in self.__dict__: self.__dict__["TreatmentType"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	AnalysisResponseType = property(_get_AnalysisResponseType, None)
	'''
	Analysis Response Type

	:type: recurdyn.AutoDesign.AnalysisResponseType
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

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
	ResultOutput = property(_get_ResultOutput, _set_ResultOutput)
	'''
	Result Output

	:type: recurdyn.ProcessNet.IExpression
	'''
	TreatmentType = property(_get_TreatmentType, _set_TreatmentType)
	'''
	Treatment Type

	:type: recurdyn.AutoDesign.TreatmentType
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use PI

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Description": _set_Description,
		"_set_Name": _set_Name,
		"_set_ResultOutput": _set_ResultOutput,
		"_set_TreatmentType": _set_TreatmentType,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"AnalysisResponseType": (12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ResultOutput": (12051, 2, (9, 0), (), "ResultOutput", '{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}'),
		"TreatmentType": (12052, 2, (3, 0), (), "TreatmentType", '{90F45D5E-BEB4-47B0-9296-7DC9AA0ECDAC}'),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Description": ((12002, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ResultOutput": ((12051, LCID, 4, 0),()),
		"TreatmentType": ((12052, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADAnalysisResponseCollection(DispatchBaseClass):
	'''AnalysisResponse Collection'''
	CLSID = IID('{A0BF51C0-1CAE-4EF2-AD18-A604B83B3990}')
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
		:rtype: recurdyn.AutoDesign.IADAnalysisResponse
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')
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
		:rtype: recurdyn.AutoDesign.IADAnalysisResponse
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')
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
		return win32com.client.util.Iterator(ob, '{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADAnalysisResponseFEResult(DispatchBaseClass):
	'''AnalysisResponse - FEResult'''
	CLSID = IID('{8D621F9F-850A-464E-A0BC-9326FA9131AA}')
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


	def _get_AnalysisResponseType(self):
		return self._ApplyTypes_(*(12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeElementSet(self):
		return self._ApplyTypes_(*(12053, 2, (9, 0), (), "NodeElementSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ResultType(self):
		return self._ApplyTypes_(*(12051, 2, (3, 0), (), "ResultType", '{6C353CFD-C07B-4EBB-9F32-B0F8263445A8}'))
	def _get_TreatmentType(self):
		return self._ApplyTypes_(*(12052, 2, (3, 0), (), "TreatmentType", '{5A785C7D-7AAD-454E-BC98-5E5FF448174C}'))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NodeElementSet(self, value):
		if "NodeElementSet" in self.__dict__: self.__dict__["NodeElementSet"] = value; return
		self._oleobj_.Invoke(*((12053, LCID, 4, 0) + (value,) + ()))
	def _set_ResultType(self, value):
		if "ResultType" in self.__dict__: self.__dict__["ResultType"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_TreatmentType(self, value):
		if "TreatmentType" in self.__dict__: self.__dict__["TreatmentType"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	AnalysisResponseType = property(_get_AnalysisResponseType, None)
	'''
	Analysis Response Type

	:type: recurdyn.AutoDesign.AnalysisResponseType
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

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
	NodeElementSet = property(_get_NodeElementSet, _set_NodeElementSet)
	'''
	NodeSet or ElementSet

	:type: recurdyn.ProcessNet.IGeneric
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
	ResultType = property(_get_ResultType, _set_ResultType)
	'''
	FEResult Type

	:type: recurdyn.AutoDesign.FEResultType
	'''
	TreatmentType = property(_get_TreatmentType, _set_TreatmentType)
	'''
	Treatment Type

	:type: recurdyn.AutoDesign.FETreatmentType
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use PI

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Description": _set_Description,
		"_set_Name": _set_Name,
		"_set_NodeElementSet": _set_NodeElementSet,
		"_set_ResultType": _set_ResultType,
		"_set_TreatmentType": _set_TreatmentType,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"AnalysisResponseType": (12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeElementSet": (12053, 2, (9, 0), (), "NodeElementSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ResultType": (12051, 2, (3, 0), (), "ResultType", '{6C353CFD-C07B-4EBB-9F32-B0F8263445A8}'),
		"TreatmentType": (12052, 2, (3, 0), (), "TreatmentType", '{5A785C7D-7AAD-454E-BC98-5E5FF448174C}'),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Description": ((12002, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NodeElementSet": ((12053, LCID, 4, 0),()),
		"ResultType": ((12051, LCID, 4, 0),()),
		"TreatmentType": ((12052, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADAnalysisResponseProcessNet(DispatchBaseClass):
	'''AnalysisResponse - ProcessNet'''
	CLSID = IID('{FD187EC7-42C4-4101-B682-B8B0A40FDDCD}')
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


	def _get_ADProcessNetType(self):
		return self._ApplyTypes_(*(12051, 2, (3, 0), (), "ADProcessNetType", '{F79FD2CD-0BDC-4C34-B93C-8AC579120A20}'))
	def _get_AnalysisResponseType(self):
		return self._ApplyTypes_(*(12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))
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
	def _get_ProcessNetDllProjectPath(self):
		return self._ApplyTypes_(*(12052, 2, (8, 0), (), "ProcessNetDllProjectPath", None))
	def _get_ProcessNetFunctionName(self):
		return self._ApplyTypes_(*(12053, 2, (8, 0), (), "ProcessNetFunctionName", None))
	def _get_ProcessNetScriptPath(self):
		return self._ApplyTypes_(*(12054, 2, (8, 0), (), "ProcessNetScriptPath", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_ADProcessNetType(self, value):
		if "ADProcessNetType" in self.__dict__: self.__dict__["ADProcessNetType"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ProcessNetDllProjectPath(self, value):
		if "ProcessNetDllProjectPath" in self.__dict__: self.__dict__["ProcessNetDllProjectPath"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_ProcessNetFunctionName(self, value):
		if "ProcessNetFunctionName" in self.__dict__: self.__dict__["ProcessNetFunctionName"] = value; return
		self._oleobj_.Invoke(*((12053, LCID, 4, 0) + (value,) + ()))
	def _set_ProcessNetScriptPath(self, value):
		if "ProcessNetScriptPath" in self.__dict__: self.__dict__["ProcessNetScriptPath"] = value; return
		self._oleobj_.Invoke(*((12054, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ADProcessNetType = property(_get_ADProcessNetType, _set_ADProcessNetType)
	'''
	ProcessNet Type

	:type: recurdyn.AutoDesign.ADProcessNetType
	'''
	AnalysisResponseType = property(_get_AnalysisResponseType, None)
	'''
	Analysis Response Type

	:type: recurdyn.AutoDesign.AnalysisResponseType
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

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
	ProcessNetDllProjectPath = property(_get_ProcessNetDllProjectPath, _set_ProcessNetDllProjectPath)
	'''
	Full path of ProcessNet Dll or Project

	:type: str
	'''
	ProcessNetFunctionName = property(_get_ProcessNetFunctionName, _set_ProcessNetFunctionName)
	'''
	Function name of ProcessNet

	:type: str
	'''
	ProcessNetScriptPath = property(_get_ProcessNetScriptPath, _set_ProcessNetScriptPath)
	'''
	Function name of ProcessNet Script

	:type: str
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use PI

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_ADProcessNetType": _set_ADProcessNetType,
		"_set_Comment": _set_Comment,
		"_set_Description": _set_Description,
		"_set_Name": _set_Name,
		"_set_ProcessNetDllProjectPath": _set_ProcessNetDllProjectPath,
		"_set_ProcessNetFunctionName": _set_ProcessNetFunctionName,
		"_set_ProcessNetScriptPath": _set_ProcessNetScriptPath,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ADProcessNetType": (12051, 2, (3, 0), (), "ADProcessNetType", '{F79FD2CD-0BDC-4C34-B93C-8AC579120A20}'),
		"AnalysisResponseType": (12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ProcessNetDllProjectPath": (12052, 2, (8, 0), (), "ProcessNetDllProjectPath", None),
		"ProcessNetFunctionName": (12053, 2, (8, 0), (), "ProcessNetFunctionName", None),
		"ProcessNetScriptPath": (12054, 2, (8, 0), (), "ProcessNetScriptPath", None),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"ADProcessNetType": ((12051, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Description": ((12002, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ProcessNetDllProjectPath": ((12052, LCID, 4, 0),()),
		"ProcessNetFunctionName": ((12053, LCID, 4, 0),()),
		"ProcessNetScriptPath": ((12054, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADAnalysisResponseScope(DispatchBaseClass):
	'''AnalysisResponse - Scope'''
	CLSID = IID('{BA363739-67DF-4E8B-80B2-35DA843EC406}')
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


	def _get_AnalysisResponseType(self):
		return self._ApplyTypes_(*(12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))
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
	def _get_Scope(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "Scope", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_TreatmentType(self):
		return self._ApplyTypes_(*(12052, 2, (3, 0), (), "TreatmentType", '{90F45D5E-BEB4-47B0-9296-7DC9AA0ECDAC}'))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_Scope(self, value):
		if "Scope" in self.__dict__: self.__dict__["Scope"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_TreatmentType(self, value):
		if "TreatmentType" in self.__dict__: self.__dict__["TreatmentType"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	AnalysisResponseType = property(_get_AnalysisResponseType, None)
	'''
	Analysis Response Type

	:type: recurdyn.AutoDesign.AnalysisResponseType
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

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
	Scope = property(_get_Scope, _set_Scope)
	'''
	Scope

	:type: recurdyn.ProcessNet.IGeneric
	'''
	TreatmentType = property(_get_TreatmentType, _set_TreatmentType)
	'''
	Treatment Type

	:type: recurdyn.AutoDesign.TreatmentType
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use PI

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Description": _set_Description,
		"_set_Name": _set_Name,
		"_set_Scope": _set_Scope,
		"_set_TreatmentType": _set_TreatmentType,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"AnalysisResponseType": (12003, 2, (3, 0), (), "AnalysisResponseType", '{2D2927C1-DFED-4562-BA6F-A310F6C417CF}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Scope": (12051, 2, (9, 0), (), "Scope", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"TreatmentType": (12052, 2, (3, 0), (), "TreatmentType", '{90F45D5E-BEB4-47B0-9296-7DC9AA0ECDAC}'),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Description": ((12002, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"Scope": ((12051, LCID, 4, 0),()),
		"TreatmentType": ((12052, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADConvergenceTolerance(DispatchBaseClass):
	'''Convergence Tolerance'''
	CLSID = IID('{97D04758-E009-46C2-BE5F-AD4A1CB49AB5}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_LimitStateValue(self):
		return self._ApplyTypes_(*(12002, 2, (5, 0), (), "LimitStateValue", None))
	def _get_MaximumIteration(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "MaximumIteration", None))
	def _get_ObjectiveChangeRate(self):
		return self._ApplyTypes_(*(12001, 2, (5, 0), (), "ObjectiveChangeRate", None))

	def _set_LimitStateValue(self, value):
		if "LimitStateValue" in self.__dict__: self.__dict__["LimitStateValue"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_MaximumIteration(self, value):
		if "MaximumIteration" in self.__dict__: self.__dict__["MaximumIteration"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_ObjectiveChangeRate(self, value):
		if "ObjectiveChangeRate" in self.__dict__: self.__dict__["ObjectiveChangeRate"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))

	LimitStateValue = property(_get_LimitStateValue, _set_LimitStateValue)
	'''
	Limit State Value

	:type: float
	'''
	MaximumIteration = property(_get_MaximumIteration, _set_MaximumIteration)
	'''
	Maximum Iteration

	:type: float
	'''
	ObjectiveChangeRate = property(_get_ObjectiveChangeRate, _set_ObjectiveChangeRate)
	'''
	Objective Change Rate in Consecutive Interations

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_LimitStateValue": _set_LimitStateValue,
		"_set_MaximumIteration": _set_MaximumIteration,
		"_set_ObjectiveChangeRate": _set_ObjectiveChangeRate,
	}
	_prop_map_get_ = {
		"LimitStateValue": (12002, 2, (5, 0), (), "LimitStateValue", None),
		"MaximumIteration": (12004, 2, (5, 0), (), "MaximumIteration", None),
		"ObjectiveChangeRate": (12001, 2, (5, 0), (), "ObjectiveChangeRate", None),
	}
	_prop_map_put_ = {
		"LimitStateValue": ((12002, LCID, 4, 0),()),
		"MaximumIteration": ((12004, LCID, 4, 0),()),
		"ObjectiveChangeRate": ((12001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADConvergenceToleranceOptimization(DispatchBaseClass):
	'''Convergence Tolerance - Optimization'''
	CLSID = IID('{3C2D3CAD-1681-493B-A387-87E60A34606F}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ConvergenceRelaxationControlType(self):
		return self._ApplyTypes_(*(12005, 2, (3, 0), (), "ConvergenceRelaxationControlType", '{BEC0AB59-2285-4EF1-989D-DD586FBAA4C1}'))
	def _get_EqualityConstraints(self):
		return self._ApplyTypes_(*(12002, 2, (5, 0), (), "EqualityConstraints", None))
	def _get_InequalityConstraints(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "InequalityConstraints", None))
	def _get_MaximumIteration(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "MaximumIteration", None))
	def _get_ObjectiveChangeRate(self):
		return self._ApplyTypes_(*(12001, 2, (5, 0), (), "ObjectiveChangeRate", None))

	def _set_ConvergenceRelaxationControlType(self, value):
		if "ConvergenceRelaxationControlType" in self.__dict__: self.__dict__["ConvergenceRelaxationControlType"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_EqualityConstraints(self, value):
		if "EqualityConstraints" in self.__dict__: self.__dict__["EqualityConstraints"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_InequalityConstraints(self, value):
		if "InequalityConstraints" in self.__dict__: self.__dict__["InequalityConstraints"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_MaximumIteration(self, value):
		if "MaximumIteration" in self.__dict__: self.__dict__["MaximumIteration"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_ObjectiveChangeRate(self, value):
		if "ObjectiveChangeRate" in self.__dict__: self.__dict__["ObjectiveChangeRate"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))

	ConvergenceRelaxationControlType = property(_get_ConvergenceRelaxationControlType, _set_ConvergenceRelaxationControlType)
	'''
	Convergence Relaxation Control Type

	:type: recurdyn.AutoDesign.ConvergenceRelaxationControlType
	'''
	EqualityConstraints = property(_get_EqualityConstraints, _set_EqualityConstraints)
	'''
	Equality Constraints

	:type: float
	'''
	InequalityConstraints = property(_get_InequalityConstraints, _set_InequalityConstraints)
	'''
	Inequality Constraints

	:type: float
	'''
	MaximumIteration = property(_get_MaximumIteration, _set_MaximumIteration)
	'''
	Maximum Iteration of SAO

	:type: float
	'''
	ObjectiveChangeRate = property(_get_ObjectiveChangeRate, _set_ObjectiveChangeRate)
	'''
	Objective Change Rate in Consecutive Interations

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_ConvergenceRelaxationControlType": _set_ConvergenceRelaxationControlType,
		"_set_EqualityConstraints": _set_EqualityConstraints,
		"_set_InequalityConstraints": _set_InequalityConstraints,
		"_set_MaximumIteration": _set_MaximumIteration,
		"_set_ObjectiveChangeRate": _set_ObjectiveChangeRate,
	}
	_prop_map_get_ = {
		"ConvergenceRelaxationControlType": (12005, 2, (3, 0), (), "ConvergenceRelaxationControlType", '{BEC0AB59-2285-4EF1-989D-DD586FBAA4C1}'),
		"EqualityConstraints": (12002, 2, (5, 0), (), "EqualityConstraints", None),
		"InequalityConstraints": (12003, 2, (5, 0), (), "InequalityConstraints", None),
		"MaximumIteration": (12004, 2, (5, 0), (), "MaximumIteration", None),
		"ObjectiveChangeRate": (12001, 2, (5, 0), (), "ObjectiveChangeRate", None),
	}
	_prop_map_put_ = {
		"ConvergenceRelaxationControlType": ((12005, LCID, 4, 0),()),
		"EqualityConstraints": ((12002, LCID, 4, 0),()),
		"InequalityConstraints": ((12003, LCID, 4, 0),()),
		"MaximumIteration": ((12004, LCID, 4, 0),()),
		"ObjectiveChangeRate": ((12001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADCorrelationAnalysis(DispatchBaseClass):
	'''Correlation Analysis'''
	CLSID = IID('{23CD2F5A-F2CB-499B-907E-F52B2BEDCC86}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AnalysisResponseResult(self, AR):
		'''
		Result of Analysis Response
		
		:param AR: IADAnalysisResponse
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12001, 1, (8197, 0), ((9, 1),), 'AnalysisResponseResult', None,AR
			)


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

class IADDesignMonteCarloReliability(DispatchBaseClass):
	'''MonteCarlo Reliability'''
	CLSID = IID('{EFD6644C-E331-4E80-B99A-DBFD663B4F9C}')
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
		Execution
		'''
		return self._oleobj_.InvokeTypes(12006, LCID, 1, (24, 0), (),)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_AnalysisControl(self):
		return self._ApplyTypes_(*(12003, 2, (9, 0), (), "AnalysisControl", '{D8BE75E5-32E7-42DF-A930-8A591F57583B}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DesignVariable(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "DesignVariable", '{F661EC5C-4647-4033-92BA-46E38C97192F}'))
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
	def _get_PerformanceIndex(self):
		return self._ApplyTypes_(*(12002, 2, (9, 0), (), "PerformanceIndex", '{7CFDA97B-0D26-4330-A9A7-33E67162C207}'))
	def _get_ResultSheet(self):
		return self._ApplyTypes_(*(12004, 2, (9, 0), (), "ResultSheet", '{AE3EFE31-E75A-43FB-9923-BCB2F2B4CB3B}'))
	def _get_SummarySheet(self):
		return self._ApplyTypes_(*(12005, 2, (9, 0), (), "SummarySheet", '{AB84ECBA-52ED-470B-BD07-9E4F851BFDC0}'))
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

	AnalysisControl = property(_get_AnalysisControl, None)
	'''
	Analysis Control

	:type: recurdyn.AutoDesign.IADAnalysisControlMonteCarloReliability
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DesignVariable = property(_get_DesignVariable, None)
	'''
	Design Variable

	:type: recurdyn.AutoDesign.IADDesignVariableReliability
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
	PerformanceIndex = property(_get_PerformanceIndex, None)
	'''
	Performance Index

	:type: recurdyn.AutoDesign.IADPerformanceIndexReliability
	'''
	ResultSheet = property(_get_ResultSheet, None)
	'''
	Result Sheet

	:type: recurdyn.AutoDesign.IADResultSheetMonteCarloReliability
	'''
	SummarySheet = property(_get_SummarySheet, None)
	'''
	Summary Sheet

	:type: recurdyn.AutoDesign.IADSummarySheetMonteCarloReliability
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
		"AnalysisControl": (12003, 2, (9, 0), (), "AnalysisControl", '{D8BE75E5-32E7-42DF-A930-8A591F57583B}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DesignVariable": (12001, 2, (9, 0), (), "DesignVariable", '{F661EC5C-4647-4033-92BA-46E38C97192F}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PerformanceIndex": (12002, 2, (9, 0), (), "PerformanceIndex", '{7CFDA97B-0D26-4330-A9A7-33E67162C207}'),
		"ResultSheet": (12004, 2, (9, 0), (), "ResultSheet", '{AE3EFE31-E75A-43FB-9923-BCB2F2B4CB3B}'),
		"SummarySheet": (12005, 2, (9, 0), (), "SummarySheet", '{AB84ECBA-52ED-470B-BD07-9E4F851BFDC0}'),
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

class IADDesignOptimization(DispatchBaseClass):
	'''Optimization'''
	CLSID = IID('{21F86233-F1EC-444F-BFAD-5480C4DBA5B1}')
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
		Execution
		'''
		return self._oleobj_.InvokeTypes(12006, LCID, 1, (24, 0), (),)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DesignVariable(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "DesignVariable", '{5BB9E831-64AE-4AD1-88DB-FE8D333C7934}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_OptimizationControl(self):
		return self._ApplyTypes_(*(12003, 2, (9, 0), (), "OptimizationControl", '{FA5F5341-8EAE-4F15-92A0-4FA3B7425525}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PerformanceIndex(self):
		return self._ApplyTypes_(*(12002, 2, (9, 0), (), "PerformanceIndex", '{BBEBBABF-49D9-4B0B-A64F-007BD3B048EC}'))
	def _get_ResultSheet(self):
		return self._ApplyTypes_(*(12004, 2, (9, 0), (), "ResultSheet", '{8B6F84EB-837F-4794-A9DB-D0C118F54305}'))
	def _get_SummarySheet(self):
		return self._ApplyTypes_(*(12005, 2, (9, 0), (), "SummarySheet", '{1CFAE095-09EA-43A3-ABE0-9412CC096017}'))
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
	DesignVariable = property(_get_DesignVariable, None)
	'''
	Design Variable

	:type: recurdyn.AutoDesign.IADDesignVariableOptimization
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
	OptimizationControl = property(_get_OptimizationControl, None)
	'''
	Optimization Control

	:type: recurdyn.AutoDesign.IADOptimizationControl
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
	PerformanceIndex = property(_get_PerformanceIndex, None)
	'''
	Performance Index

	:type: recurdyn.AutoDesign.IADPerformanceIndexOptimization
	'''
	ResultSheet = property(_get_ResultSheet, None)
	'''
	Result Sheet

	:type: recurdyn.AutoDesign.IADResultSheetOptimization
	'''
	SummarySheet = property(_get_SummarySheet, None)
	'''
	Summary Sheet

	:type: recurdyn.AutoDesign.IADSummarySheetOptimization
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
		"DesignVariable": (12001, 2, (9, 0), (), "DesignVariable", '{5BB9E831-64AE-4AD1-88DB-FE8D333C7934}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"OptimizationControl": (12003, 2, (9, 0), (), "OptimizationControl", '{FA5F5341-8EAE-4F15-92A0-4FA3B7425525}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PerformanceIndex": (12002, 2, (9, 0), (), "PerformanceIndex", '{BBEBBABF-49D9-4B0B-A64F-007BD3B048EC}'),
		"ResultSheet": (12004, 2, (9, 0), (), "ResultSheet", '{8B6F84EB-837F-4794-A9DB-D0C118F54305}'),
		"SummarySheet": (12005, 2, (9, 0), (), "SummarySheet", '{1CFAE095-09EA-43A3-ABE0-9412CC096017}'),
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

class IADDesignParameter(DispatchBaseClass):
	'''DesignParameter'''
	CLSID = IID('{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')
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
	def _get_Current(self):
		return self._ApplyTypes_(*(12002, 2, (5, 0), (), "Current", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12005, 2, (8, 0), (), "Description", None))
	def _get_DesignParameterType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LB(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "LB", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UB(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "UB", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_LB(self, value):
		if "LB" in self.__dict__: self.__dict__["LB"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UB(self, value):
		if "UB" in self.__dict__: self.__dict__["UB"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Current = property(_get_Current, None)
	'''
	Current

	:type: float
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

	:type: str
	'''
	DesignParameterType = property(_get_DesignParameterType, None)
	'''
	Design Parameter Type

	:type: recurdyn.AutoDesign.DesignParameterType
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	LB = property(_get_LB, _set_LB)
	'''
	Lower bound

	:type: float
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
	UB = property(_get_UB, _set_UB)
	'''
	Upper bound

	:type: float
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use DV

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Description": _set_Description,
		"_set_LB": _set_LB,
		"_set_Name": _set_Name,
		"_set_UB": _set_UB,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Current": (12002, 2, (5, 0), (), "Current", None),
		"Description": (12005, 2, (8, 0), (), "Description", None),
		"DesignParameterType": (12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LB": (12003, 2, (5, 0), (), "LB", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UB": (12004, 2, (5, 0), (), "UB", None),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Description": ((12005, LCID, 4, 0),()),
		"LB": ((12003, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UB": ((12004, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignParameterAngular(DispatchBaseClass):
	'''FEShape4 : Angular Relation'''
	CLSID = IID('{B34F3E57-7FD8-4176-AA85-F0B882CAD4B3}')
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
	def _get_ConfigurationDesignType(self):
		return self._ApplyTypes_(*(12052, 2, (3, 0), (), "ConfigurationDesignType", '{91B00663-8DB7-4C49-A8E4-CCEF2445220B}'))
	def _get_Current(self):
		return self._ApplyTypes_(*(12002, 2, (5, 0), (), "Current", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12005, 2, (8, 0), (), "Description", None))
	def _get_DesignParameterType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LB(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "LB", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeSet(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RefMarker(self):
		return self._ApplyTypes_(*(12053, 2, (9, 0), (), "RefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_ReferencePoint(self):
		return self._ApplyTypes_(*(12055, 2, (9, 0), (), "ReferencePoint", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'))
	def _get_RotationAxisUnitVector(self):
		return self._ApplyTypes_(*(12054, 2, (9, 0), (), "RotationAxisUnitVector", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'))
	def _get_UB(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "UB", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ConfigurationDesignType(self, value):
		if "ConfigurationDesignType" in self.__dict__: self.__dict__["ConfigurationDesignType"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_LB(self, value):
		if "LB" in self.__dict__: self.__dict__["LB"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NodeSet(self, value):
		if "NodeSet" in self.__dict__: self.__dict__["NodeSet"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_RefMarker(self, value):
		if "RefMarker" in self.__dict__: self.__dict__["RefMarker"] = value; return
		self._oleobj_.Invoke(*((12053, LCID, 4, 0) + (value,) + ()))
	def _set_UB(self, value):
		if "UB" in self.__dict__: self.__dict__["UB"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ConfigurationDesignType = property(_get_ConfigurationDesignType, _set_ConfigurationDesignType)
	'''
	Cartesian motion type

	:type: recurdyn.AutoDesign.ConfigurationDesignType
	'''
	Current = property(_get_Current, None)
	'''
	Current

	:type: float
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

	:type: str
	'''
	DesignParameterType = property(_get_DesignParameterType, None)
	'''
	Design Parameter Type

	:type: recurdyn.AutoDesign.DesignParameterType
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	LB = property(_get_LB, _set_LB)
	'''
	Lower bound

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NodeSet = property(_get_NodeSet, _set_NodeSet)
	'''
	NodeSet

	:type: recurdyn.ProcessNet.IGeneric
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
	ReferencePoint = property(_get_ReferencePoint, None)
	'''
	Rotation Point

	:type: recurdyn.ProcessNet.IPoint3D
	'''
	RotationAxisUnitVector = property(_get_RotationAxisUnitVector, None)
	'''
	Rotation Axis Unit Vector

	:type: recurdyn.ProcessNet.IPoint3D
	'''
	UB = property(_get_UB, _set_UB)
	'''
	Upper bound

	:type: float
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use DV

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_ConfigurationDesignType": _set_ConfigurationDesignType,
		"_set_Description": _set_Description,
		"_set_LB": _set_LB,
		"_set_Name": _set_Name,
		"_set_NodeSet": _set_NodeSet,
		"_set_RefMarker": _set_RefMarker,
		"_set_UB": _set_UB,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConfigurationDesignType": (12052, 2, (3, 0), (), "ConfigurationDesignType", '{91B00663-8DB7-4C49-A8E4-CCEF2445220B}'),
		"Current": (12002, 2, (5, 0), (), "Current", None),
		"Description": (12005, 2, (8, 0), (), "Description", None),
		"DesignParameterType": (12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LB": (12003, 2, (5, 0), (), "LB", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeSet": (12051, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RefMarker": (12053, 2, (9, 0), (), "RefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"ReferencePoint": (12055, 2, (9, 0), (), "ReferencePoint", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'),
		"RotationAxisUnitVector": (12054, 2, (9, 0), (), "RotationAxisUnitVector", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'),
		"UB": (12004, 2, (5, 0), (), "UB", None),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ConfigurationDesignType": ((12052, LCID, 4, 0),()),
		"Description": ((12005, LCID, 4, 0),()),
		"LB": ((12003, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NodeSet": ((12051, LCID, 4, 0),()),
		"RefMarker": ((12053, LCID, 4, 0),()),
		"UB": ((12004, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignParameterCollection(DispatchBaseClass):
	'''DesignParameter Collection'''
	CLSID = IID('{39B651B4-D8F5-4B36-BA9B-5A5EB8F32D1B}')
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
		:rtype: recurdyn.AutoDesign.IADDesignParameter
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')
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
		:rtype: recurdyn.AutoDesign.IADDesignParameter
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')
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
		return win32com.client.util.Iterator(ob, '{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADDesignParameterCylindrical(DispatchBaseClass):
	'''FEShape2 : Cylindrical Distance'''
	CLSID = IID('{661B8B3F-0219-4D76-B7EE-90B3C54F6FF9}')
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


	def _get_CenterAxisUnitVector(self):
		return self._ApplyTypes_(*(12054, 2, (9, 0), (), "CenterAxisUnitVector", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'))
	def _get_CenterRefMarker(self):
		return self._ApplyTypes_(*(12053, 2, (9, 0), (), "CenterRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ConfigurationDesignType(self):
		return self._ApplyTypes_(*(12052, 2, (3, 0), (), "ConfigurationDesignType", '{91B00663-8DB7-4C49-A8E4-CCEF2445220B}'))
	def _get_Current(self):
		return self._ApplyTypes_(*(12002, 2, (5, 0), (), "Current", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12005, 2, (8, 0), (), "Description", None))
	def _get_DesignParameterType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LB(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "LB", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeSet(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UB(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "UB", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_CenterRefMarker(self, value):
		if "CenterRefMarker" in self.__dict__: self.__dict__["CenterRefMarker"] = value; return
		self._oleobj_.Invoke(*((12053, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ConfigurationDesignType(self, value):
		if "ConfigurationDesignType" in self.__dict__: self.__dict__["ConfigurationDesignType"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_LB(self, value):
		if "LB" in self.__dict__: self.__dict__["LB"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NodeSet(self, value):
		if "NodeSet" in self.__dict__: self.__dict__["NodeSet"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_UB(self, value):
		if "UB" in self.__dict__: self.__dict__["UB"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	CenterAxisUnitVector = property(_get_CenterAxisUnitVector, None)
	'''
	Center Axis Unit Vector

	:type: recurdyn.ProcessNet.IPoint3D
	'''
	CenterRefMarker = property(_get_CenterRefMarker, _set_CenterRefMarker)
	'''
	Center Reference marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ConfigurationDesignType = property(_get_ConfigurationDesignType, _set_ConfigurationDesignType)
	'''
	Cartesian motion type

	:type: recurdyn.AutoDesign.ConfigurationDesignType
	'''
	Current = property(_get_Current, None)
	'''
	Current

	:type: float
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

	:type: str
	'''
	DesignParameterType = property(_get_DesignParameterType, None)
	'''
	Design Parameter Type

	:type: recurdyn.AutoDesign.DesignParameterType
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	LB = property(_get_LB, _set_LB)
	'''
	Lower bound

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NodeSet = property(_get_NodeSet, _set_NodeSet)
	'''
	NodeSet

	:type: recurdyn.ProcessNet.IGeneric
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
	UB = property(_get_UB, _set_UB)
	'''
	Upper bound

	:type: float
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use DV

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_CenterRefMarker": _set_CenterRefMarker,
		"_set_Comment": _set_Comment,
		"_set_ConfigurationDesignType": _set_ConfigurationDesignType,
		"_set_Description": _set_Description,
		"_set_LB": _set_LB,
		"_set_Name": _set_Name,
		"_set_NodeSet": _set_NodeSet,
		"_set_UB": _set_UB,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"CenterAxisUnitVector": (12054, 2, (9, 0), (), "CenterAxisUnitVector", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'),
		"CenterRefMarker": (12053, 2, (9, 0), (), "CenterRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConfigurationDesignType": (12052, 2, (3, 0), (), "ConfigurationDesignType", '{91B00663-8DB7-4C49-A8E4-CCEF2445220B}'),
		"Current": (12002, 2, (5, 0), (), "Current", None),
		"Description": (12005, 2, (8, 0), (), "Description", None),
		"DesignParameterType": (12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LB": (12003, 2, (5, 0), (), "LB", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeSet": (12051, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UB": (12004, 2, (5, 0), (), "UB", None),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"CenterRefMarker": ((12053, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ConfigurationDesignType": ((12052, LCID, 4, 0),()),
		"Description": ((12005, LCID, 4, 0),()),
		"LB": ((12003, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NodeSet": ((12051, LCID, 4, 0),()),
		"UB": ((12004, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignParameterDirect(DispatchBaseClass):
	'''Direct Relation'''
	CLSID = IID('{274D959F-B501-4C61-804B-A5458E8B73C3}')
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
	def _get_Current(self):
		return self._ApplyTypes_(*(12002, 2, (5, 0), (), "Current", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12005, 2, (8, 0), (), "Description", None))
	def _get_DesignParameterType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LB(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "LB", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_ParametricValue(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "ParametricValue", '{3EEED3CE-62E8-4882-AAE6-4812B49927B5}'))
	def _get_UB(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "UB", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_LB(self, value):
		if "LB" in self.__dict__: self.__dict__["LB"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_ParametricValue(self, value):
		if "ParametricValue" in self.__dict__: self.__dict__["ParametricValue"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_UB(self, value):
		if "UB" in self.__dict__: self.__dict__["UB"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Current = property(_get_Current, None)
	'''
	Current

	:type: float
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

	:type: str
	'''
	DesignParameterType = property(_get_DesignParameterType, None)
	'''
	Design Parameter Type

	:type: recurdyn.AutoDesign.DesignParameterType
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	LB = property(_get_LB, _set_LB)
	'''
	Lower bound

	:type: float
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
	ParametricValue = property(_get_ParametricValue, _set_ParametricValue)
	'''
	Parametric value

	:type: recurdyn.ProcessNet.IParametricValue
	'''
	UB = property(_get_UB, _set_UB)
	'''
	Upper bound

	:type: float
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use DV

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Description": _set_Description,
		"_set_LB": _set_LB,
		"_set_Name": _set_Name,
		"_set_ParametricValue": _set_ParametricValue,
		"_set_UB": _set_UB,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Current": (12002, 2, (5, 0), (), "Current", None),
		"Description": (12005, 2, (8, 0), (), "Description", None),
		"DesignParameterType": (12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LB": (12003, 2, (5, 0), (), "LB", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"ParametricValue": (12051, 2, (9, 0), (), "ParametricValue", '{3EEED3CE-62E8-4882-AAE6-4812B49927B5}'),
		"UB": (12004, 2, (5, 0), (), "UB", None),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Description": ((12005, LCID, 4, 0),()),
		"LB": ((12003, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"ParametricValue": ((12051, LCID, 4, 0),()),
		"UB": ((12004, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignParameterSpherical(DispatchBaseClass):
	'''FEShape3 : Spherical Distance'''
	CLSID = IID('{0AE6489F-7BB8-4D8A-8121-FDDBB4363359}')
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


	def _get_CenterRefMarker(self):
		return self._ApplyTypes_(*(12053, 2, (9, 0), (), "CenterRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ConfigurationDesignType(self):
		return self._ApplyTypes_(*(12052, 2, (3, 0), (), "ConfigurationDesignType", '{91B00663-8DB7-4C49-A8E4-CCEF2445220B}'))
	def _get_Current(self):
		return self._ApplyTypes_(*(12002, 2, (5, 0), (), "Current", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12005, 2, (8, 0), (), "Description", None))
	def _get_DesignParameterType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LB(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "LB", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeSet(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UB(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "UB", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_CenterRefMarker(self, value):
		if "CenterRefMarker" in self.__dict__: self.__dict__["CenterRefMarker"] = value; return
		self._oleobj_.Invoke(*((12053, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ConfigurationDesignType(self, value):
		if "ConfigurationDesignType" in self.__dict__: self.__dict__["ConfigurationDesignType"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_LB(self, value):
		if "LB" in self.__dict__: self.__dict__["LB"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NodeSet(self, value):
		if "NodeSet" in self.__dict__: self.__dict__["NodeSet"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_UB(self, value):
		if "UB" in self.__dict__: self.__dict__["UB"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	CenterRefMarker = property(_get_CenterRefMarker, _set_CenterRefMarker)
	'''
	Center Reference marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ConfigurationDesignType = property(_get_ConfigurationDesignType, _set_ConfigurationDesignType)
	'''
	Cartesian motion type

	:type: recurdyn.AutoDesign.ConfigurationDesignType
	'''
	Current = property(_get_Current, None)
	'''
	Current

	:type: float
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

	:type: str
	'''
	DesignParameterType = property(_get_DesignParameterType, None)
	'''
	Design Parameter Type

	:type: recurdyn.AutoDesign.DesignParameterType
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	LB = property(_get_LB, _set_LB)
	'''
	Lower bound

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NodeSet = property(_get_NodeSet, _set_NodeSet)
	'''
	NodeSet

	:type: recurdyn.ProcessNet.IGeneric
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
	UB = property(_get_UB, _set_UB)
	'''
	Upper bound

	:type: float
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use DV

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_CenterRefMarker": _set_CenterRefMarker,
		"_set_Comment": _set_Comment,
		"_set_ConfigurationDesignType": _set_ConfigurationDesignType,
		"_set_Description": _set_Description,
		"_set_LB": _set_LB,
		"_set_Name": _set_Name,
		"_set_NodeSet": _set_NodeSet,
		"_set_UB": _set_UB,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"CenterRefMarker": (12053, 2, (9, 0), (), "CenterRefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConfigurationDesignType": (12052, 2, (3, 0), (), "ConfigurationDesignType", '{91B00663-8DB7-4C49-A8E4-CCEF2445220B}'),
		"Current": (12002, 2, (5, 0), (), "Current", None),
		"Description": (12005, 2, (8, 0), (), "Description", None),
		"DesignParameterType": (12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LB": (12003, 2, (5, 0), (), "LB", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeSet": (12051, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UB": (12004, 2, (5, 0), (), "UB", None),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"CenterRefMarker": ((12053, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"ConfigurationDesignType": ((12052, LCID, 4, 0),()),
		"Description": ((12005, LCID, 4, 0),()),
		"LB": ((12003, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NodeSet": ((12051, LCID, 4, 0),()),
		"UB": ((12004, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignParameterTranslational(DispatchBaseClass):
	'''FEShape1 : Translational Relation'''
	CLSID = IID('{F171C34B-E486-48C8-8030-769C8ABD2D55}')
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
	def _get_ConfigurationDesignType(self):
		return self._ApplyTypes_(*(12052, 2, (3, 0), (), "ConfigurationDesignType", '{91B00663-8DB7-4C49-A8E4-CCEF2445220B}'))
	def _get_Current(self):
		return self._ApplyTypes_(*(12002, 2, (5, 0), (), "Current", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12005, 2, (8, 0), (), "Description", None))
	def _get_DesignParameterType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'))
	def _get_DirectionalUnitVector(self):
		return self._ApplyTypes_(*(12054, 2, (9, 0), (), "DirectionalUnitVector", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LB(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "LB", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NodeSet(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RefMarker(self):
		return self._ApplyTypes_(*(12053, 2, (9, 0), (), "RefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_UB(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "UB", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ConfigurationDesignType(self, value):
		if "ConfigurationDesignType" in self.__dict__: self.__dict__["ConfigurationDesignType"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_Description(self, value):
		if "Description" in self.__dict__: self.__dict__["Description"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_LB(self, value):
		if "LB" in self.__dict__: self.__dict__["LB"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NodeSet(self, value):
		if "NodeSet" in self.__dict__: self.__dict__["NodeSet"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_RefMarker(self, value):
		if "RefMarker" in self.__dict__: self.__dict__["RefMarker"] = value; return
		self._oleobj_.Invoke(*((12053, LCID, 4, 0) + (value,) + ()))
	def _set_UB(self, value):
		if "UB" in self.__dict__: self.__dict__["UB"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ConfigurationDesignType = property(_get_ConfigurationDesignType, _set_ConfigurationDesignType)
	'''
	Cartesian motion type

	:type: recurdyn.AutoDesign.ConfigurationDesignType
	'''
	Current = property(_get_Current, None)
	'''
	Current

	:type: float
	'''
	Description = property(_get_Description, _set_Description)
	'''
	Description

	:type: str
	'''
	DesignParameterType = property(_get_DesignParameterType, None)
	'''
	Design Parameter Type

	:type: recurdyn.AutoDesign.DesignParameterType
	'''
	DirectionalUnitVector = property(_get_DirectionalUnitVector, None)
	'''
	Directional Unit Vector

	:type: recurdyn.ProcessNet.IPoint3D
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	LB = property(_get_LB, _set_LB)
	'''
	Lower bound

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NodeSet = property(_get_NodeSet, _set_NodeSet)
	'''
	NodeSet

	:type: recurdyn.ProcessNet.IGeneric
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
	UB = property(_get_UB, _set_UB)
	'''
	Upper bound

	:type: float
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use DV

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_ConfigurationDesignType": _set_ConfigurationDesignType,
		"_set_Description": _set_Description,
		"_set_LB": _set_LB,
		"_set_Name": _set_Name,
		"_set_NodeSet": _set_NodeSet,
		"_set_RefMarker": _set_RefMarker,
		"_set_UB": _set_UB,
		"_set_Use": _set_Use,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ConfigurationDesignType": (12052, 2, (3, 0), (), "ConfigurationDesignType", '{91B00663-8DB7-4C49-A8E4-CCEF2445220B}'),
		"Current": (12002, 2, (5, 0), (), "Current", None),
		"Description": (12005, 2, (8, 0), (), "Description", None),
		"DesignParameterType": (12006, 2, (3, 0), (), "DesignParameterType", '{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}'),
		"DirectionalUnitVector": (12054, 2, (9, 0), (), "DirectionalUnitVector", '{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LB": (12003, 2, (5, 0), (), "LB", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NodeSet": (12051, 2, (9, 0), (), "NodeSet", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RefMarker": (12053, 2, (9, 0), (), "RefMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"UB": (12004, 2, (5, 0), (), "UB", None),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ConfigurationDesignType": ((12052, LCID, 4, 0),()),
		"Description": ((12005, LCID, 4, 0),()),
		"LB": ((12003, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NodeSet": ((12051, LCID, 4, 0),()),
		"RefMarker": ((12053, LCID, 4, 0),()),
		"UB": ((12004, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignRobustOptimization(DispatchBaseClass):
	'''Robust Optimization'''
	CLSID = IID('{94B1BEFB-5C73-4A2A-92F2-997AF6CBAD62}')
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
		Execution
		'''
		return self._oleobj_.InvokeTypes(12006, LCID, 1, (24, 0), (),)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DesignVariable(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "DesignVariable", '{21581656-E8B6-4C52-A435-6C6F7BC30720}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_OptimizationControl(self):
		return self._ApplyTypes_(*(12003, 2, (9, 0), (), "OptimizationControl", '{EA42004C-FAA2-4507-B161-FCC1E8CFD5B8}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PerformanceIndex(self):
		return self._ApplyTypes_(*(12002, 2, (9, 0), (), "PerformanceIndex", '{4C5071E8-AFE7-4056-B4B2-DD3CFD7A534B}'))
	def _get_ResultSheet(self):
		return self._ApplyTypes_(*(12004, 2, (9, 0), (), "ResultSheet", '{A0AE4D34-C41F-4AF7-83F6-310D52FADC4E}'))
	def _get_SummarySheet(self):
		return self._ApplyTypes_(*(12005, 2, (9, 0), (), "SummarySheet", '{0EAE4DF9-530B-4C01-8E01-05B444BA70FB}'))
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
	DesignVariable = property(_get_DesignVariable, None)
	'''
	Design Variable

	:type: recurdyn.AutoDesign.IADDesignVariableRobustOptimization
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
	OptimizationControl = property(_get_OptimizationControl, None)
	'''
	Optimization Control

	:type: recurdyn.AutoDesign.IADRobustOptimizationControl
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
	PerformanceIndex = property(_get_PerformanceIndex, None)
	'''
	Performance Index

	:type: recurdyn.AutoDesign.IADPerformanceIndexRobustOptimization
	'''
	ResultSheet = property(_get_ResultSheet, None)
	'''
	Result Sheet

	:type: recurdyn.AutoDesign.IADResultSheetRobustOptimization
	'''
	SummarySheet = property(_get_SummarySheet, None)
	'''
	Summary Sheet

	:type: recurdyn.AutoDesign.IADSummarySheetRobustOptimization
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
		"DesignVariable": (12001, 2, (9, 0), (), "DesignVariable", '{21581656-E8B6-4C52-A435-6C6F7BC30720}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"OptimizationControl": (12003, 2, (9, 0), (), "OptimizationControl", '{EA42004C-FAA2-4507-B161-FCC1E8CFD5B8}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PerformanceIndex": (12002, 2, (9, 0), (), "PerformanceIndex", '{4C5071E8-AFE7-4056-B4B2-DD3CFD7A534B}'),
		"ResultSheet": (12004, 2, (9, 0), (), "ResultSheet", '{A0AE4D34-C41F-4AF7-83F6-310D52FADC4E}'),
		"SummarySheet": (12005, 2, (9, 0), (), "SummarySheet", '{0EAE4DF9-530B-4C01-8E01-05B444BA70FB}'),
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

class IADDesignSAOReliability(DispatchBaseClass):
	'''SAO Reliability'''
	CLSID = IID('{A481E1C1-5497-468B-B072-CDB83437D5D3}')
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
		Execution
		'''
		return self._oleobj_.InvokeTypes(12006, LCID, 1, (24, 0), (),)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_AnalysisControl(self):
		return self._ApplyTypes_(*(12003, 2, (9, 0), (), "AnalysisControl", '{9CF67D49-AFD5-46EA-B69E-50E384C63F41}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DesignVariable(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "DesignVariable", '{F661EC5C-4647-4033-92BA-46E38C97192F}'))
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
	def _get_PerformanceIndex(self):
		return self._ApplyTypes_(*(12002, 2, (9, 0), (), "PerformanceIndex", '{7CFDA97B-0D26-4330-A9A7-33E67162C207}'))
	def _get_ResultSheet(self):
		return self._ApplyTypes_(*(12004, 2, (9, 0), (), "ResultSheet", '{090D60A3-B9C2-4E96-8B46-9224257A6C8B}'))
	def _get_SummarySheet(self):
		return self._ApplyTypes_(*(12005, 2, (9, 0), (), "SummarySheet", '{34968513-D22A-4A7C-876F-D97623DC5BB8}'))
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

	AnalysisControl = property(_get_AnalysisControl, None)
	'''
	Analysis Control

	:type: recurdyn.AutoDesign.IADAnalysisControlSAOReliability
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DesignVariable = property(_get_DesignVariable, None)
	'''
	Design Variable

	:type: recurdyn.AutoDesign.IADDesignVariableReliability
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
	PerformanceIndex = property(_get_PerformanceIndex, None)
	'''
	Performance Index

	:type: recurdyn.AutoDesign.IADPerformanceIndexReliability
	'''
	ResultSheet = property(_get_ResultSheet, None)
	'''
	Result Sheet

	:type: recurdyn.AutoDesign.IADResultSheetSAOReliability
	'''
	SummarySheet = property(_get_SummarySheet, None)
	'''
	Summary Sheet

	:type: recurdyn.AutoDesign.IADSummarySheetSAOReliability
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
		"AnalysisControl": (12003, 2, (9, 0), (), "AnalysisControl", '{9CF67D49-AFD5-46EA-B69E-50E384C63F41}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DesignVariable": (12001, 2, (9, 0), (), "DesignVariable", '{F661EC5C-4647-4033-92BA-46E38C97192F}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PerformanceIndex": (12002, 2, (9, 0), (), "PerformanceIndex", '{7CFDA97B-0D26-4330-A9A7-33E67162C207}'),
		"ResultSheet": (12004, 2, (9, 0), (), "ResultSheet", '{090D60A3-B9C2-4E96-8B46-9224257A6C8B}'),
		"SummarySheet": (12005, 2, (9, 0), (), "SummarySheet", '{34968513-D22A-4A7C-876F-D97623DC5BB8}'),
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

class IADDesignSimulationHistory(DispatchBaseClass):
	'''Simulation History'''
	CLSID = IID('{A17668CB-A526-42D3-B8CC-21A35B441EAB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Check(self, type, flag, startIndex, endIndex):
		'''
		Check Get or Export flag
		
		:param type: CheckFlagType
		:param flag: bool
		:param startIndex: int
		:param endIndex: int
		'''
		return self._oleobj_.InvokeTypes(12007, LCID, 1, (24, 0), ((3, 1), (11, 1), (19, 1), (19, 1)),type
			, flag, startIndex, endIndex)


	def CheckAll(self, type, flag):
		'''
		Check all Get or Export flag
		
		:param type: CheckFlagType
		:param flag: bool
		'''
		return self._oleobj_.InvokeTypes(12008, LCID, 1, (24, 0), ((3, 1), (11, 1)),type
			, flag)


	def Delete(self, startIndex, endIndex):
		'''
		Delete simualtion history values
		
		:param startIndex: int
		:param endIndex: int
		'''
		return self._oleobj_.InvokeTypes(12005, LCID, 1, (24, 0), ((19, 1), (19, 1)),startIndex
			, endIndex)


	def DeleteAll(self):
		'''
		Delete all simualtion history values
		'''
		return self._oleobj_.InvokeTypes(12006, LCID, 1, (24, 0), (),)


	def Export(self, name, val, startIndex, endIndex, bOverWrite):
		'''
		Export the simulation history value collection to the file
		
		:param name: str
		:param val: ExportDataType
		:param startIndex: int
		:param endIndex: int
		:param bOverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(12004, LCID, 1, (24, 0), ((8, 1), (8195, 1), (19, 1), (19, 1), (11, 1)),name
			, val, startIndex, endIndex, bOverWrite)


	def ExportAll(self, name, val, bOverWrite):
		'''
		Export the simulation history value collection to the file
		
		:param name: str
		:param val: ExportDataType
		:param bOverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(12003, LCID, 1, (24, 0), ((8, 1), (8195, 1), (11, 1)),name
			, val, bOverWrite)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def Import(self, name):
		'''
		Import the simualtion history value collection file
		
		:param name: str
		'''
		return self._oleobj_.InvokeTypes(12002, LCID, 1, (24, 0), ((8, 1),),name
			)


	def UpdateCurrentModel(self, val):
		'''
		Update Current Model
		
		:param val: IADSimulationHistoryValue
		'''
		return self._oleobj_.InvokeTypes(12010, LCID, 1, (24, 0), ((9, 1),),val
			)


	def UpdateNewModel(self, val, name, bOverWrite):
		'''
		Update New Model
		
		:param val: IADSimulationHistoryValue
		:param name: str
		:param bOverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(12009, LCID, 1, (24, 0), ((9, 1), (8, 1), (11, 1)),val
			, name, bOverWrite)


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
	def _get_SimulationHistoryValueCollection(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "SimulationHistoryValueCollection", '{848C36F6-B86F-404E-A809-D8687EC91DEB}'))
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
	SimulationHistoryValueCollection = property(_get_SimulationHistoryValueCollection, None)
	'''
	Get the collection of Simulation History Value

	:type: recurdyn.AutoDesign.IADSimulationHistoryValueCollection
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
		"SimulationHistoryValueCollection": (12001, 2, (9, 0), (), "SimulationHistoryValueCollection", '{848C36F6-B86F-404E-A809-D8687EC91DEB}'),
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

class IADDesignStudy(DispatchBaseClass):
	'''DesignStudy'''
	CLSID = IID('{6BCFA125-3F0C-42DA-AA88-8949B4625E32}')
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
		Execution
		'''
		return self._oleobj_.InvokeTypes(12007, LCID, 1, (24, 0), (),)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_CorrelationAnalysis(self):
		return self._ApplyTypes_(*(12006, 2, (9, 0), (), "CorrelationAnalysis", '{23CD2F5A-F2CB-499B-907E-F52B2BEDCC86}'))
	def _get_DesignVariable(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "DesignVariable", '{EA349BD0-8E34-435E-BDC8-22434008169E}'))
	def _get_EffectAnalysis(self):
		return self._ApplyTypes_(*(12004, 2, (9, 0), (), "EffectAnalysis", '{E6D34A7F-E67B-43F6-AD41-4E3526234647}'))
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
	def _get_PerformanceIndex(self):
		return self._ApplyTypes_(*(12002, 2, (9, 0), (), "PerformanceIndex", '{B29F78DD-B76C-407A-921F-E2305173B26D}'))
	def _get_ScreeningVariable(self):
		return self._ApplyTypes_(*(12005, 2, (9, 0), (), "ScreeningVariable", '{23B3FD64-1889-4D1E-9CF2-5A39543F8806}'))
	def _get_SimulationControl(self):
		return self._ApplyTypes_(*(12003, 2, (9, 0), (), "SimulationControl", '{0838C8AB-285F-4456-8E62-2C7BC633DB4C}'))
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
	CorrelationAnalysis = property(_get_CorrelationAnalysis, None)
	'''
	Correlation Analysis

	:type: recurdyn.AutoDesign.IADCorrelationAnalysis
	'''
	DesignVariable = property(_get_DesignVariable, None)
	'''
	Design Variable

	:type: recurdyn.AutoDesign.IADDesignVariable
	'''
	EffectAnalysis = property(_get_EffectAnalysis, None)
	'''
	Effect Analysis

	:type: recurdyn.AutoDesign.IADEffectAnalysis
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
	PerformanceIndex = property(_get_PerformanceIndex, None)
	'''
	Performance Index

	:type: recurdyn.AutoDesign.IADPerformanceIndex
	'''
	ScreeningVariable = property(_get_ScreeningVariable, None)
	'''
	Screening Variable

	:type: recurdyn.AutoDesign.IADScreeningVariable
	'''
	SimulationControl = property(_get_SimulationControl, None)
	'''
	Simulation Control

	:type: recurdyn.AutoDesign.IADSimulationControl
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
		"CorrelationAnalysis": (12006, 2, (9, 0), (), "CorrelationAnalysis", '{23CD2F5A-F2CB-499B-907E-F52B2BEDCC86}'),
		"DesignVariable": (12001, 2, (9, 0), (), "DesignVariable", '{EA349BD0-8E34-435E-BDC8-22434008169E}'),
		"EffectAnalysis": (12004, 2, (9, 0), (), "EffectAnalysis", '{E6D34A7F-E67B-43F6-AD41-4E3526234647}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PerformanceIndex": (12002, 2, (9, 0), (), "PerformanceIndex", '{B29F78DD-B76C-407A-921F-E2305173B26D}'),
		"ScreeningVariable": (12005, 2, (9, 0), (), "ScreeningVariable", '{23B3FD64-1889-4D1E-9CF2-5A39543F8806}'),
		"SimulationControl": (12003, 2, (9, 0), (), "SimulationControl", '{0838C8AB-285F-4456-8E62-2C7BC633DB4C}'),
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

class IADDesignVariable(DispatchBaseClass):
	'''DesignVariable'''
	CLSID = IID('{EA349BD0-8E34-435E-BDC8-22434008169E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AllLevelSetBoseOrthogonalArray(self, val):
		'''
		Update All Level for Bose`s Orthogonal Array
		
		:param val: int
		'''
		return self._oleobj_.InvokeTypes(12009, LCID, 1, (24, 0), ((19, 1),),val
			)


	def AllLevelSetExtendedPlackettBurman(self, val):
		'''
		Update All Level for Extended Plackett Burman
		
		:param val: ExtendedPlackettBurmanLevelType
		'''
		return self._oleobj_.InvokeTypes(12007, LCID, 1, (24, 0), ((3, 1),),val
			)


	def AllLevelSetFullFactorialDesign(self, val):
		'''
		Update All Level for Full Factorial Design
		
		:param val: FullFactorialDesignLevelType
		'''
		return self._oleobj_.InvokeTypes(12008, LCID, 1, (24, 0), ((3, 1),),val
			)


	def AllLevelSetLevelBalancedDescriptiveDesign(self, val):
		'''
		Update All Level for Level Balanced Descriptive Design
		
		:param val: int
		'''
		return self._oleobj_.InvokeTypes(12010, LCID, 1, (24, 0), ((19, 1),),val
			)


	def CalculateAvailableLevelsOfBoseOrthogonalArray(self, nDV):
		'''
		Calculate available levels of Bose`s Orthogonal Array
		
		:param nDV: int
		:rtype: list[int]
		'''
		return self._ApplyTypes_(12011, 1, (8195, 0), ((19, 1),), 'CalculateAvailableLevelsOfBoseOrthogonalArray', None,nDV
			)


	def SetDefault(self):
		'''
		Calculate default values with current level
		'''
		return self._oleobj_.InvokeTypes(12006, LCID, 1, (24, 0), (),)


	def _get_AllLevelSet(self):
		return self._ApplyTypes_(*(12002, 2, (19, 0), (), "AllLevelSet", None))
	def _get_DOEMethod(self):
		return self._ApplyTypes_(*(12001, 2, (3, 0), (), "DOEMethod", '{3EAB6469-0B54-43D6-A51C-F29A31057AE2}'))
	def _get_DesignVariableValueCollection(self):
		return self._ApplyTypes_(*(12005, 2, (9, 0), (), "DesignVariableValueCollection", '{4041B853-0350-4DC4-A516-53EB9B0EF3E6}'))
	def _get_NumberOfTrials(self):
		return self._ApplyTypes_(*(12004, 2, (19, 0), (), "NumberOfTrials", None))
	def _get_RequiredRuns(self):
		return self._ApplyTypes_(*(12003, 2, (19, 0), (), "RequiredRuns", None))

	def _set_DOEMethod(self, value):
		if "DOEMethod" in self.__dict__: self.__dict__["DOEMethod"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_RequiredRuns(self, value):
		if "RequiredRuns" in self.__dict__: self.__dict__["RequiredRuns"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))

	AllLevelSet = property(_get_AllLevelSet, None)
	'''
	All level set

	:type: int
	'''
	DOEMethod = property(_get_DOEMethod, _set_DOEMethod)
	'''
	DOEMethod type

	:type: recurdyn.AutoDesign.DOEMethodType
	'''
	DesignVariableValueCollection = property(_get_DesignVariableValueCollection, None)
	'''
	Get the collection of Design VariableValue

	:type: recurdyn.AutoDesign.IADDesignVariableValueCollection
	'''
	NumberOfTrials = property(_get_NumberOfTrials, None)
	'''
	Number of trials

	:type: int
	'''
	RequiredRuns = property(_get_RequiredRuns, _set_RequiredRuns)
	'''
	Required runs

	:type: int
	'''

	_prop_map_set_function_ = {
		"_set_DOEMethod": _set_DOEMethod,
		"_set_RequiredRuns": _set_RequiredRuns,
	}
	_prop_map_get_ = {
		"AllLevelSet": (12002, 2, (19, 0), (), "AllLevelSet", None),
		"DOEMethod": (12001, 2, (3, 0), (), "DOEMethod", '{3EAB6469-0B54-43D6-A51C-F29A31057AE2}'),
		"DesignVariableValueCollection": (12005, 2, (9, 0), (), "DesignVariableValueCollection", '{4041B853-0350-4DC4-A516-53EB9B0EF3E6}'),
		"NumberOfTrials": (12004, 2, (19, 0), (), "NumberOfTrials", None),
		"RequiredRuns": (12003, 2, (19, 0), (), "RequiredRuns", None),
	}
	_prop_map_put_ = {
		"DOEMethod": ((12001, LCID, 4, 0),()),
		"RequiredRuns": ((12003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignVariableOptimization(DispatchBaseClass):
	'''DesignVariable - Optimization'''
	CLSID = IID('{5BB9E831-64AE-4AD1-88DB-FE8D333C7934}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DesignVariableValueCollection(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "DesignVariableValueCollection", '{4AE4ADC1-5D80-48D8-9DED-60AFF06B076F}'))

	DesignVariableValueCollection = property(_get_DesignVariableValueCollection, None)
	'''
	Get the collection of Design Variable

	:type: recurdyn.AutoDesign.IADDesignVariableValueOptimizationCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DesignVariableValueCollection": (12001, 2, (9, 0), (), "DesignVariableValueCollection", '{4AE4ADC1-5D80-48D8-9DED-60AFF06B076F}'),
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

class IADDesignVariableReliability(DispatchBaseClass):
	'''DesignVariable - Reliability'''
	CLSID = IID('{F661EC5C-4647-4033-92BA-46E38C97192F}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DesignVariableValueCollection(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "DesignVariableValueCollection", '{26B20F68-D1FA-4DD6-B690-2C4AA0BC6B6F}'))

	DesignVariableValueCollection = property(_get_DesignVariableValueCollection, None)
	'''
	Get the collection of Design Variable

	:type: recurdyn.AutoDesign.IADDesignVariableValueReliabilityCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DesignVariableValueCollection": (12001, 2, (9, 0), (), "DesignVariableValueCollection", '{26B20F68-D1FA-4DD6-B690-2C4AA0BC6B6F}'),
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

class IADDesignVariableRobustOptimization(DispatchBaseClass):
	'''DesignVariable - RobustOptimization'''
	CLSID = IID('{21581656-E8B6-4C52-A435-6C6F7BC30720}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DesignVariableValueCollection(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "DesignVariableValueCollection", '{FBDB8850-EF61-47B2-A7C8-EE7A36DEBAE1}'))

	DesignVariableValueCollection = property(_get_DesignVariableValueCollection, None)
	'''
	Get the collection of Design Variable

	:type: recurdyn.AutoDesign.IADDesignVariableValueRobustOptimizationCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DesignVariableValueCollection": (12001, 2, (9, 0), (), "DesignVariableValueCollection", '{FBDB8850-EF61-47B2-A7C8-EE7A36DEBAE1}'),
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

class IADDesignVariableValue(DispatchBaseClass):
	'''DesignVariable Value'''
	CLSID = IID('{3EDECE37-7EBE-4189-8F11-78C4FFC54E0C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DPName(self):
		return self._ApplyTypes_(*(12001, 2, (8, 0), (), "DPName", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))
	def _get_LB(self):
		return self._ApplyTypes_(*(12005, 2, (5, 0), (), "LB", None))
	def _get_Level(self):
		return self._ApplyTypes_(*(12003, 2, (19, 0), (), "Level", None))
	def _get_Mid(self):
		return self._ApplyTypes_(*(12007, 2, (8197, 0), (), "Mid", None))
	def _get_UB(self):
		return self._ApplyTypes_(*(12006, 2, (5, 0), (), "UB", None))

	def _set_ExtendedPlackettBurmanLevelType(self, value):
		if "ExtendedPlackettBurmanLevelType" in self.__dict__: self.__dict__["ExtendedPlackettBurmanLevelType"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_Mid(self, value):
		if "Mid" in self.__dict__: self.__dict__["Mid"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((12007, LCID, 4, 0) + (variantValue,) + ()))

	DPName = property(_get_DPName, None)
	'''
	DP Name

	:type: str
	'''
	Description = property(_get_Description, None)
	'''
	Description

	:type: str
	'''
	LB = property(_get_LB, None)
	'''
	Lower bound

	:type: float
	'''
	Level = property(_get_Level, None)
	'''
	Level

	:type: int
	'''
	Mid = property(_get_Mid, _set_Mid)
	'''
	Mid-Values

	:type: list[float]
	'''
	UB = property(_get_UB, None)
	'''
	Upper bound

	:type: float
	'''
	ExtendedPlackettBurmanLevelType = property(None, _set_ExtendedPlackettBurmanLevelType)
	'''
	It can be set in case of Extended Placket

	:type: recurdyn.AutoDesign.ExtendedPlackettBurmanLevelType
	'''

	_prop_map_set_function_ = {
		"_set_ExtendedPlackettBurmanLevelType": _set_ExtendedPlackettBurmanLevelType,
		"_set_Mid": _set_Mid,
	}
	_prop_map_get_ = {
		"DPName": (12001, 2, (8, 0), (), "DPName", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
		"LB": (12005, 2, (5, 0), (), "LB", None),
		"Level": (12003, 2, (19, 0), (), "Level", None),
		"Mid": (12007, 2, (8197, 0), (), "Mid", None),
		"UB": (12006, 2, (5, 0), (), "UB", None),
	}
	_prop_map_put_ = {
		"ExtendedPlackettBurmanLevelType": ((12004, LCID, 4, 0),()),
		"Mid": ((12007, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignVariableValueCollection(DispatchBaseClass):
	'''DesignVariableValue Collection'''
	CLSID = IID('{4041B853-0350-4DC4-A516-53EB9B0EF3E6}')
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
		:rtype: recurdyn.AutoDesign.IADDesignVariableValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{3EDECE37-7EBE-4189-8F11-78C4FFC54E0C}')
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
		:rtype: recurdyn.AutoDesign.IADDesignVariableValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{3EDECE37-7EBE-4189-8F11-78C4FFC54E0C}')
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
		return win32com.client.util.Iterator(ob, '{3EDECE37-7EBE-4189-8F11-78C4FFC54E0C}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{3EDECE37-7EBE-4189-8F11-78C4FFC54E0C}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADDesignVariableValueOptimization(DispatchBaseClass):
	'''DesignVariable Value - Optimization'''
	CLSID = IID('{FAD5D54F-8696-4C06-A2AE-6958AE3C15E3}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Current(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "Current", None))
	def _get_DPName(self):
		return self._ApplyTypes_(*(12001, 2, (8, 0), (), "DPName", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))
	def _get_DesignVariableType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "DesignVariableType", '{87FFE66D-548A-420F-96FB-8ECBAD2762FD}'))
	def _get_LB(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "LB", None))
	def _get_UB(self):
		return self._ApplyTypes_(*(12005, 2, (5, 0), (), "UB", None))
	def _get_Value(self):
		return self._ApplyTypes_(*(12007, 2, (5, 0), (), "Value", None))

	def _set_DesignVariableType(self, value):
		if "DesignVariableType" in self.__dict__: self.__dict__["DesignVariableType"] = value; return
		self._oleobj_.Invoke(*((12006, LCID, 4, 0) + (value,) + ()))
	def _set_Value(self, value):
		if "Value" in self.__dict__: self.__dict__["Value"] = value; return
		self._oleobj_.Invoke(*((12007, LCID, 4, 0) + (value,) + ()))

	Current = property(_get_Current, None)
	'''
	Current

	:type: float
	'''
	DPName = property(_get_DPName, None)
	'''
	DP Name

	:type: str
	'''
	Description = property(_get_Description, None)
	'''
	Description

	:type: str
	'''
	DesignVariableType = property(_get_DesignVariableType, _set_DesignVariableType)
	'''
	Design Variable Type

	:type: recurdyn.AutoDesign.DesignVariableType
	'''
	LB = property(_get_LB, None)
	'''
	Lower bound

	:type: float
	'''
	UB = property(_get_UB, None)
	'''
	Upper bound

	:type: float
	'''
	Value = property(_get_Value, _set_Value)
	'''
	Value

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_DesignVariableType": _set_DesignVariableType,
		"_set_Value": _set_Value,
	}
	_prop_map_get_ = {
		"Current": (12003, 2, (5, 0), (), "Current", None),
		"DPName": (12001, 2, (8, 0), (), "DPName", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
		"DesignVariableType": (12006, 2, (3, 0), (), "DesignVariableType", '{87FFE66D-548A-420F-96FB-8ECBAD2762FD}'),
		"LB": (12004, 2, (5, 0), (), "LB", None),
		"UB": (12005, 2, (5, 0), (), "UB", None),
		"Value": (12007, 2, (5, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"DesignVariableType": ((12006, LCID, 4, 0),()),
		"Value": ((12007, LCID, 4, 0),()),
	}
	def __call__(self):
		return self._ApplyTypes_(*(12007, 2, (5, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignVariableValueOptimizationCollection(DispatchBaseClass):
	'''DesignVariableValue Collection - Optimization'''
	CLSID = IID('{4AE4ADC1-5D80-48D8-9DED-60AFF06B076F}')
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
		:rtype: recurdyn.AutoDesign.IADDesignVariableValueOptimization
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{FAD5D54F-8696-4C06-A2AE-6958AE3C15E3}')
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
		:rtype: recurdyn.AutoDesign.IADDesignVariableValueOptimization
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{FAD5D54F-8696-4C06-A2AE-6958AE3C15E3}')
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
		return win32com.client.util.Iterator(ob, '{FAD5D54F-8696-4C06-A2AE-6958AE3C15E3}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{FAD5D54F-8696-4C06-A2AE-6958AE3C15E3}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADDesignVariableValueReliability(DispatchBaseClass):
	'''DesignVariable Value - Reliability'''
	CLSID = IID('{BA8157EE-5975-42E0-833D-A5ADE8CD107B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Current(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "Current", None))
	def _get_DPName(self):
		return self._ApplyTypes_(*(12001, 2, (8, 0), (), "DPName", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))
	def _get_DesignVariableType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "DesignVariableType", '{87FFE66D-548A-420F-96FB-8ECBAD2762FD}'))
	def _get_DeviationType(self):
		return self._ApplyTypes_(*(12009, 2, (3, 0), (), "DeviationType", '{3A831DE1-C118-44B2-8774-238F0E9DB5BE}'))
	def _get_DeviationValue(self):
		return self._ApplyTypes_(*(12010, 2, (5, 0), (), "DeviationValue", None))
	def _get_LB(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "LB", None))
	def _get_MeanValue(self):
		return self._ApplyTypes_(*(12007, 2, (5, 0), (), "MeanValue", None))
	def _get_ProbabilityDistributionType(self):
		return self._ApplyTypes_(*(12008, 2, (3, 0), (), "ProbabilityDistributionType", '{067A69BB-310D-4900-910B-520F40F6D5EF}'))
	def _get_UB(self):
		return self._ApplyTypes_(*(12005, 2, (5, 0), (), "UB", None))

	def _set_DeviationType(self, value):
		if "DeviationType" in self.__dict__: self.__dict__["DeviationType"] = value; return
		self._oleobj_.Invoke(*((12009, LCID, 4, 0) + (value,) + ()))
	def _set_DeviationValue(self, value):
		if "DeviationValue" in self.__dict__: self.__dict__["DeviationValue"] = value; return
		self._oleobj_.Invoke(*((12010, LCID, 4, 0) + (value,) + ()))
	def _set_MeanValue(self, value):
		if "MeanValue" in self.__dict__: self.__dict__["MeanValue"] = value; return
		self._oleobj_.Invoke(*((12007, LCID, 4, 0) + (value,) + ()))
	def _set_ProbabilityDistributionType(self, value):
		if "ProbabilityDistributionType" in self.__dict__: self.__dict__["ProbabilityDistributionType"] = value; return
		self._oleobj_.Invoke(*((12008, LCID, 4, 0) + (value,) + ()))

	Current = property(_get_Current, None)
	'''
	Current

	:type: float
	'''
	DPName = property(_get_DPName, None)
	'''
	DP Name

	:type: str
	'''
	Description = property(_get_Description, None)
	'''
	Description

	:type: str
	'''
	DesignVariableType = property(_get_DesignVariableType, None)
	'''
	Design Variable Type

	:type: recurdyn.AutoDesign.DesignVariableType
	'''
	DeviationType = property(_get_DeviationType, _set_DeviationType)
	'''
	Deviation Type

	:type: recurdyn.AutoDesign.DeviationType
	'''
	DeviationValue = property(_get_DeviationValue, _set_DeviationValue)
	'''
	Deviation Value

	:type: float
	'''
	LB = property(_get_LB, None)
	'''
	Lower bound

	:type: float
	'''
	MeanValue = property(_get_MeanValue, _set_MeanValue)
	'''
	Mean Value

	:type: float
	'''
	ProbabilityDistributionType = property(_get_ProbabilityDistributionType, _set_ProbabilityDistributionType)
	'''
	Probability Distribution Type

	:type: recurdyn.AutoDesign.ProbabilityDistributionType
	'''
	UB = property(_get_UB, None)
	'''
	Upper bound

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_DeviationType": _set_DeviationType,
		"_set_DeviationValue": _set_DeviationValue,
		"_set_MeanValue": _set_MeanValue,
		"_set_ProbabilityDistributionType": _set_ProbabilityDistributionType,
	}
	_prop_map_get_ = {
		"Current": (12003, 2, (5, 0), (), "Current", None),
		"DPName": (12001, 2, (8, 0), (), "DPName", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
		"DesignVariableType": (12006, 2, (3, 0), (), "DesignVariableType", '{87FFE66D-548A-420F-96FB-8ECBAD2762FD}'),
		"DeviationType": (12009, 2, (3, 0), (), "DeviationType", '{3A831DE1-C118-44B2-8774-238F0E9DB5BE}'),
		"DeviationValue": (12010, 2, (5, 0), (), "DeviationValue", None),
		"LB": (12004, 2, (5, 0), (), "LB", None),
		"MeanValue": (12007, 2, (5, 0), (), "MeanValue", None),
		"ProbabilityDistributionType": (12008, 2, (3, 0), (), "ProbabilityDistributionType", '{067A69BB-310D-4900-910B-520F40F6D5EF}'),
		"UB": (12005, 2, (5, 0), (), "UB", None),
	}
	_prop_map_put_ = {
		"DeviationType": ((12009, LCID, 4, 0),()),
		"DeviationValue": ((12010, LCID, 4, 0),()),
		"MeanValue": ((12007, LCID, 4, 0),()),
		"ProbabilityDistributionType": ((12008, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignVariableValueReliabilityCollection(DispatchBaseClass):
	'''DesignVariableValue Collection - Reliability'''
	CLSID = IID('{26B20F68-D1FA-4DD6-B690-2C4AA0BC6B6F}')
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
		:rtype: recurdyn.AutoDesign.IADDesignVariableValueReliability
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{BA8157EE-5975-42E0-833D-A5ADE8CD107B}')
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
		:rtype: recurdyn.AutoDesign.IADDesignVariableValueReliability
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{BA8157EE-5975-42E0-833D-A5ADE8CD107B}')
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
		return win32com.client.util.Iterator(ob, '{BA8157EE-5975-42E0-833D-A5ADE8CD107B}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{BA8157EE-5975-42E0-833D-A5ADE8CD107B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADDesignVariableValueRobustOptimization(DispatchBaseClass):
	'''DesignVariable Value - RobustOptimization'''
	CLSID = IID('{44C71273-E70C-4AC7-B285-7741F8DF8F49}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Current(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "Current", None))
	def _get_DPName(self):
		return self._ApplyTypes_(*(12001, 2, (8, 0), (), "DPName", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))
	def _get_DesignVariableType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "DesignVariableType", '{87FFE66D-548A-420F-96FB-8ECBAD2762FD}'))
	def _get_DeviationType(self):
		return self._ApplyTypes_(*(12052, 2, (3, 0), (), "DeviationType", '{3A831DE1-C118-44B2-8774-238F0E9DB5BE}'))
	def _get_DeviationValue(self):
		return self._ApplyTypes_(*(12053, 2, (5, 0), (), "DeviationValue", None))
	def _get_LB(self):
		return self._ApplyTypes_(*(12004, 2, (5, 0), (), "LB", None))
	def _get_StatisticalInfoType(self):
		return self._ApplyTypes_(*(12051, 2, (3, 0), (), "StatisticalInfoType", '{AC42F832-BB21-4945-859C-2BFDC16F09C7}'))
	def _get_UB(self):
		return self._ApplyTypes_(*(12005, 2, (5, 0), (), "UB", None))
	def _get_Value(self):
		return self._ApplyTypes_(*(12007, 2, (5, 0), (), "Value", None))

	def _set_DesignVariableType(self, value):
		if "DesignVariableType" in self.__dict__: self.__dict__["DesignVariableType"] = value; return
		self._oleobj_.Invoke(*((12006, LCID, 4, 0) + (value,) + ()))
	def _set_DeviationType(self, value):
		if "DeviationType" in self.__dict__: self.__dict__["DeviationType"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_DeviationValue(self, value):
		if "DeviationValue" in self.__dict__: self.__dict__["DeviationValue"] = value; return
		self._oleobj_.Invoke(*((12053, LCID, 4, 0) + (value,) + ()))
	def _set_StatisticalInfoType(self, value):
		if "StatisticalInfoType" in self.__dict__: self.__dict__["StatisticalInfoType"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_Value(self, value):
		if "Value" in self.__dict__: self.__dict__["Value"] = value; return
		self._oleobj_.Invoke(*((12007, LCID, 4, 0) + (value,) + ()))

	Current = property(_get_Current, None)
	'''
	Current

	:type: float
	'''
	DPName = property(_get_DPName, None)
	'''
	DP Name

	:type: str
	'''
	Description = property(_get_Description, None)
	'''
	Description

	:type: str
	'''
	DesignVariableType = property(_get_DesignVariableType, _set_DesignVariableType)
	'''
	Design Variable Type

	:type: recurdyn.AutoDesign.DesignVariableType
	'''
	DeviationType = property(_get_DeviationType, _set_DeviationType)
	'''
	Deviation Type

	:type: recurdyn.AutoDesign.DeviationType
	'''
	DeviationValue = property(_get_DeviationValue, _set_DeviationValue)
	'''
	Deviation Value

	:type: float
	'''
	LB = property(_get_LB, None)
	'''
	Lower bound

	:type: float
	'''
	StatisticalInfoType = property(_get_StatisticalInfoType, _set_StatisticalInfoType)
	'''
	Statistical Info Type

	:type: recurdyn.AutoDesign.StatisticalInfoType
	'''
	UB = property(_get_UB, None)
	'''
	Upper bound

	:type: float
	'''
	Value = property(_get_Value, _set_Value)
	'''
	Value

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_DesignVariableType": _set_DesignVariableType,
		"_set_DeviationType": _set_DeviationType,
		"_set_DeviationValue": _set_DeviationValue,
		"_set_StatisticalInfoType": _set_StatisticalInfoType,
		"_set_Value": _set_Value,
	}
	_prop_map_get_ = {
		"Current": (12003, 2, (5, 0), (), "Current", None),
		"DPName": (12001, 2, (8, 0), (), "DPName", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
		"DesignVariableType": (12006, 2, (3, 0), (), "DesignVariableType", '{87FFE66D-548A-420F-96FB-8ECBAD2762FD}'),
		"DeviationType": (12052, 2, (3, 0), (), "DeviationType", '{3A831DE1-C118-44B2-8774-238F0E9DB5BE}'),
		"DeviationValue": (12053, 2, (5, 0), (), "DeviationValue", None),
		"LB": (12004, 2, (5, 0), (), "LB", None),
		"StatisticalInfoType": (12051, 2, (3, 0), (), "StatisticalInfoType", '{AC42F832-BB21-4945-859C-2BFDC16F09C7}'),
		"UB": (12005, 2, (5, 0), (), "UB", None),
		"Value": (12007, 2, (5, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"DesignVariableType": ((12006, LCID, 4, 0),()),
		"DeviationType": ((12052, LCID, 4, 0),()),
		"DeviationValue": ((12053, LCID, 4, 0),()),
		"StatisticalInfoType": ((12051, LCID, 4, 0),()),
		"Value": ((12007, LCID, 4, 0),()),
	}
	def __call__(self):
		return self._ApplyTypes_(*(12007, 2, (5, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADDesignVariableValueRobustOptimizationCollection(DispatchBaseClass):
	'''DesignVariableValue Collection - Robust Optimization'''
	CLSID = IID('{FBDB8850-EF61-47B2-A7C8-EE7A36DEBAE1}')
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
		:rtype: recurdyn.AutoDesign.IADDesignVariableValueRobustOptimization
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{44C71273-E70C-4AC7-B285-7741F8DF8F49}')
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
		:rtype: recurdyn.AutoDesign.IADDesignVariableValueRobustOptimization
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{44C71273-E70C-4AC7-B285-7741F8DF8F49}')
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
		return win32com.client.util.Iterator(ob, '{44C71273-E70C-4AC7-B285-7741F8DF8F49}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{44C71273-E70C-4AC7-B285-7741F8DF8F49}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADEffectAnalysis(DispatchBaseClass):
	'''Effect Analysis'''
	CLSID = IID('{E6D34A7F-E67B-43F6-AD41-4E3526234647}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def EffectValues(self, DV):
		'''
		Effect Values
		
		:param DV: IADDesignParameter
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12004, 1, (8197, 0), ((9, 1),), 'EffectValues', None,DV
			)


	def MaximizationCombination(self):
		'''
		Maximization Combination
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12006, 1, (8197, 0), (), 'MaximizationCombination', None,)


	def MinimizationCombination(self):
		'''
		Minimization Combination
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12005, 1, (8197, 0), (), 'MinimizationCombination', None,)


	def Simulation(self, type):
		'''
		Simuation
		
		:param type: CombinationType
		'''
		return self._oleobj_.InvokeTypes(12007, LCID, 1, (24, 0), ((3, 1),),type
			)


	def Variation(self, DV):
		'''
		Variation method
		
		:param DV: IADDesignParameter
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12003, 1, (8197, 0), ((9, 1),), 'Variation', None,DV
			)


	def _get_ARName(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "ARName", None))

	def _set_SelectAnalysisResponse(self, value):
		if "SelectAnalysisResponse" in self.__dict__: self.__dict__["SelectAnalysisResponse"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))

	ARName = property(_get_ARName, None)
	'''
	Selected  Analysis Response Name

	:type: str
	'''
	SelectAnalysisResponse = property(None, _set_SelectAnalysisResponse)
	'''
	Select Analysis Response

	:type: recurdyn.AutoDesign.IADAnalysisResponse
	'''

	_prop_map_set_function_ = {
		"_set_SelectAnalysisResponse": _set_SelectAnalysisResponse,
	}
	_prop_map_get_ = {
		"ARName": (12002, 2, (8, 0), (), "ARName", None),
	}
	_prop_map_put_ = {
		"SelectAnalysisResponse": ((12001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADMetaModel(DispatchBaseClass):
	'''Meta Model'''
	CLSID = IID('{F7310378-6376-4E72-8590-21B13F775AB4}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DOEMethodType(self):
		return self._ApplyTypes_(*(12004, 2, (3, 0), (), "DOEMethodType", '{22E7B466-BB8D-47A0-A967-442E38BCA533}'))
	def _get_DiscreteLatinHypercubeDesignNumber(self):
		return self._ApplyTypes_(*(12005, 2, (19, 0), (), "DiscreteLatinHypercubeDesignNumber", None))
	def _get_MetaModelingMethodType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "MetaModelingMethodType", '{CDD675EF-2B10-454D-874A-79C9EA607FD7}'))
	def _get_PolynomialFunctionType(self):
		return self._ApplyTypes_(*(12007, 2, (3, 0), (), "PolynomialFunctionType", '{4FCC8FE8-CFFA-4794-BC1F-0C095D91C142}'))
	def _get_UseAutoSelection(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "UseAutoSelection", None))
	def _get_UseDOEMethod(self):
		return self._ApplyTypes_(*(12002, 2, (11, 0), (), "UseDOEMethod", None))
	def _get_UseGetFromSimulationHistory(self):
		return self._ApplyTypes_(*(12003, 2, (11, 0), (), "UseGetFromSimulationHistory", None))

	def _set_DOEMethodType(self, value):
		if "DOEMethodType" in self.__dict__: self.__dict__["DOEMethodType"] = value; return
		self._oleobj_.Invoke(*((12004, LCID, 4, 0) + (value,) + ()))
	def _set_DiscreteLatinHypercubeDesignNumber(self, value):
		if "DiscreteLatinHypercubeDesignNumber" in self.__dict__: self.__dict__["DiscreteLatinHypercubeDesignNumber"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_MetaModelingMethodType(self, value):
		if "MetaModelingMethodType" in self.__dict__: self.__dict__["MetaModelingMethodType"] = value; return
		self._oleobj_.Invoke(*((12006, LCID, 4, 0) + (value,) + ()))
	def _set_PolynomialFunctionType(self, value):
		if "PolynomialFunctionType" in self.__dict__: self.__dict__["PolynomialFunctionType"] = value; return
		self._oleobj_.Invoke(*((12007, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoSelection(self, value):
		if "UseAutoSelection" in self.__dict__: self.__dict__["UseAutoSelection"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UseDOEMethod(self, value):
		if "UseDOEMethod" in self.__dict__: self.__dict__["UseDOEMethod"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_UseGetFromSimulationHistory(self, value):
		if "UseGetFromSimulationHistory" in self.__dict__: self.__dict__["UseGetFromSimulationHistory"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))

	DOEMethodType = property(_get_DOEMethodType, _set_DOEMethodType)
	'''
	DOEMethod Type

	:type: recurdyn.AutoDesign.MetaModelDOEMethodType
	'''
	DiscreteLatinHypercubeDesignNumber = property(_get_DiscreteLatinHypercubeDesignNumber, _set_DiscreteLatinHypercubeDesignNumber)
	'''
	The Number of Discrete Latin Hypercube Design

	:type: int
	'''
	MetaModelingMethodType = property(_get_MetaModelingMethodType, _set_MetaModelingMethodType)
	'''
	Meta Modeling Method Type

	:type: recurdyn.AutoDesign.MetaModelingMethodType
	'''
	PolynomialFunctionType = property(_get_PolynomialFunctionType, _set_PolynomialFunctionType)
	'''
	Polynomial Function Type

	:type: recurdyn.AutoDesign.PolynomialFunctionType
	'''
	UseAutoSelection = property(_get_UseAutoSelection, _set_UseAutoSelection)
	'''
	Use Auto Selection

	:type: bool
	'''
	UseDOEMethod = property(_get_UseDOEMethod, _set_UseDOEMethod)
	'''
	Use DOE Method

	:type: bool
	'''
	UseGetFromSimulationHistory = property(_get_UseGetFromSimulationHistory, _set_UseGetFromSimulationHistory)
	'''
	Use GetFromSimulationHistory

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_DOEMethodType": _set_DOEMethodType,
		"_set_DiscreteLatinHypercubeDesignNumber": _set_DiscreteLatinHypercubeDesignNumber,
		"_set_MetaModelingMethodType": _set_MetaModelingMethodType,
		"_set_PolynomialFunctionType": _set_PolynomialFunctionType,
		"_set_UseAutoSelection": _set_UseAutoSelection,
		"_set_UseDOEMethod": _set_UseDOEMethod,
		"_set_UseGetFromSimulationHistory": _set_UseGetFromSimulationHistory,
	}
	_prop_map_get_ = {
		"DOEMethodType": (12004, 2, (3, 0), (), "DOEMethodType", '{22E7B466-BB8D-47A0-A967-442E38BCA533}'),
		"DiscreteLatinHypercubeDesignNumber": (12005, 2, (19, 0), (), "DiscreteLatinHypercubeDesignNumber", None),
		"MetaModelingMethodType": (12006, 2, (3, 0), (), "MetaModelingMethodType", '{CDD675EF-2B10-454D-874A-79C9EA607FD7}'),
		"PolynomialFunctionType": (12007, 2, (3, 0), (), "PolynomialFunctionType", '{4FCC8FE8-CFFA-4794-BC1F-0C095D91C142}'),
		"UseAutoSelection": (12001, 2, (11, 0), (), "UseAutoSelection", None),
		"UseDOEMethod": (12002, 2, (11, 0), (), "UseDOEMethod", None),
		"UseGetFromSimulationHistory": (12003, 2, (11, 0), (), "UseGetFromSimulationHistory", None),
	}
	_prop_map_put_ = {
		"DOEMethodType": ((12004, LCID, 4, 0),()),
		"DiscreteLatinHypercubeDesignNumber": ((12005, LCID, 4, 0),()),
		"MetaModelingMethodType": ((12006, LCID, 4, 0),()),
		"PolynomialFunctionType": ((12007, LCID, 4, 0),()),
		"UseAutoSelection": ((12001, LCID, 4, 0),()),
		"UseDOEMethod": ((12002, LCID, 4, 0),()),
		"UseGetFromSimulationHistory": ((12003, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADOptimizationControl(DispatchBaseClass):
	'''Optimization Control'''
	CLSID = IID('{FA5F5341-8EAE-4F15-92A0-4FA3B7425525}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ConvergenceTolerance(self):
		return self._ApplyTypes_(*(12052, 2, (9, 0), (), "ConvergenceTolerance", '{3C2D3CAD-1681-493B-A387-87E60A34606F}'))
	def _get_MetaModel(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "MetaModel", '{F7310378-6376-4E72-8590-21B13F775AB4}'))
	def _get_NumberOfTrials(self):
		return self._ApplyTypes_(*(12053, 2, (19, 0), (), "NumberOfTrials", None))
	def _get_SaveResult(self):
		return self._ApplyTypes_(*(12003, 2, (8, 0), (), "SaveResult", None))
	def _get_SimulationType(self):
		return self._ApplyTypes_(*(12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'))
	def _get_UseSaveResult(self):
		return self._ApplyTypes_(*(12002, 2, (11, 0), (), "UseSaveResult", None))

	def _set_SaveResult(self, value):
		if "SaveResult" in self.__dict__: self.__dict__["SaveResult"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_SimulationType(self, value):
		if "SimulationType" in self.__dict__: self.__dict__["SimulationType"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UseSaveResult(self, value):
		if "UseSaveResult" in self.__dict__: self.__dict__["UseSaveResult"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))

	ConvergenceTolerance = property(_get_ConvergenceTolerance, None)
	'''
	Convergence Tolerance

	:type: recurdyn.AutoDesign.IADConvergenceToleranceOptimization
	'''
	MetaModel = property(_get_MetaModel, None)
	'''
	Meta Model

	:type: recurdyn.AutoDesign.IADMetaModel
	'''
	NumberOfTrials = property(_get_NumberOfTrials, None)
	'''
	Number of trials

	:type: int
	'''
	SaveResult = property(_get_SaveResult, _set_SaveResult)
	'''
	Save results

	:type: str
	'''
	SimulationType = property(_get_SimulationType, _set_SimulationType)
	'''
	Simulation Type

	:type: recurdyn.AutoDesign.ADSimulationType
	'''
	UseSaveResult = property(_get_UseSaveResult, _set_UseSaveResult)
	'''
	Use save results

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_SaveResult": _set_SaveResult,
		"_set_SimulationType": _set_SimulationType,
		"_set_UseSaveResult": _set_UseSaveResult,
	}
	_prop_map_get_ = {
		"ConvergenceTolerance": (12052, 2, (9, 0), (), "ConvergenceTolerance", '{3C2D3CAD-1681-493B-A387-87E60A34606F}'),
		"MetaModel": (12051, 2, (9, 0), (), "MetaModel", '{F7310378-6376-4E72-8590-21B13F775AB4}'),
		"NumberOfTrials": (12053, 2, (19, 0), (), "NumberOfTrials", None),
		"SaveResult": (12003, 2, (8, 0), (), "SaveResult", None),
		"SimulationType": (12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'),
		"UseSaveResult": (12002, 2, (11, 0), (), "UseSaveResult", None),
	}
	_prop_map_put_ = {
		"SaveResult": ((12003, LCID, 4, 0),()),
		"SimulationType": ((12001, LCID, 4, 0),()),
		"UseSaveResult": ((12002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADPerformanceIndex(DispatchBaseClass):
	'''PerformanceIndex'''
	CLSID = IID('{B29F78DD-B76C-407A-921F-E2305173B26D}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_PerformanceIndexValueCollection(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "PerformanceIndexValueCollection", '{0D17420F-646F-40BC-BA44-3ED8D71659DB}'))

	PerformanceIndexValueCollection = property(_get_PerformanceIndexValueCollection, None)
	'''
	Get the collection of PerformanceIndex Value

	:type: recurdyn.AutoDesign.IADPerformanceIndexValueCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PerformanceIndexValueCollection": (12001, 2, (9, 0), (), "PerformanceIndexValueCollection", '{0D17420F-646F-40BC-BA44-3ED8D71659DB}'),
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

class IADPerformanceIndexOptimization(DispatchBaseClass):
	'''PerformanceIndex - Optimization'''
	CLSID = IID('{BBEBBABF-49D9-4B0B-A64F-007BD3B048EC}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddPerformanceIndexValue(self):
		'''
		Add PerformanceIndex Value
		
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValueOptimization
		'''
		ret = self._oleobj_.InvokeTypes(12002, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddPerformanceIndexValue', '{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}')
		return ret

	def DeletePerformanceIndexValue(self, pVal):
		'''
		Delete PerformanceIndex Value
		
		:param pVal: IADPerformanceIndexValueOptimization
		'''
		return self._oleobj_.InvokeTypes(12003, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def _get_PerformanceIndexValueCollection(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "PerformanceIndexValueCollection", '{E1417D0E-3016-43ED-BB4C-525D39CEDD02}'))

	PerformanceIndexValueCollection = property(_get_PerformanceIndexValueCollection, None)
	'''
	Get the collection of PerformanceIndex Value

	:type: recurdyn.AutoDesign.IADPerformanceIndexValueOptimizationCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PerformanceIndexValueCollection": (12001, 2, (9, 0), (), "PerformanceIndexValueCollection", '{E1417D0E-3016-43ED-BB4C-525D39CEDD02}'),
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

class IADPerformanceIndexReliability(DispatchBaseClass):
	'''PerformanceIndex - Reliability'''
	CLSID = IID('{7CFDA97B-0D26-4330-A9A7-33E67162C207}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddPerformanceIndexValue(self):
		'''
		Add PerformanceIndex Value
		
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValueReliability
		'''
		ret = self._oleobj_.InvokeTypes(12002, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddPerformanceIndexValue', '{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')
		return ret

	def DeletePerformanceIndexValue(self, pVal):
		'''
		Delete PerformanceIndex Value
		
		:param pVal: IADPerformanceIndexValueReliability
		'''
		return self._oleobj_.InvokeTypes(12003, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def _get_PerformanceIndexValueCollection(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "PerformanceIndexValueCollection", '{921490EB-AF1C-4DC8-9901-2394EA388ED1}'))

	PerformanceIndexValueCollection = property(_get_PerformanceIndexValueCollection, None)
	'''
	Get the collection of PerformanceIndex Value

	:type: recurdyn.AutoDesign.IADPerformanceIndexValueReliabilityCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PerformanceIndexValueCollection": (12001, 2, (9, 0), (), "PerformanceIndexValueCollection", '{921490EB-AF1C-4DC8-9901-2394EA388ED1}'),
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

class IADPerformanceIndexRobustOptimization(DispatchBaseClass):
	'''PerformanceIndex - RobustOptimization'''
	CLSID = IID('{4C5071E8-AFE7-4056-B4B2-DD3CFD7A534B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddPerformanceIndexValue(self):
		'''
		Add PerformanceIndex Value
		
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValueRobustOptimization
		'''
		ret = self._oleobj_.InvokeTypes(12002, LCID, 1, (9, 0), (),)
		if ret is not None:
			ret = Dispatch(ret, 'AddPerformanceIndexValue', '{E6741EBF-DDF9-4A34-8AFA-DF0796377699}')
		return ret

	def DeletePerformanceIndexValue(self, pVal):
		'''
		Delete PerformanceIndex Value
		
		:param pVal: IADPerformanceIndexValueRobustOptimization
		'''
		return self._oleobj_.InvokeTypes(12003, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def _get_PerformanceIndexValueCollection(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "PerformanceIndexValueCollection", '{ABE15F3A-BE3E-4A4A-9A9B-50EFFBB1089A}'))

	PerformanceIndexValueCollection = property(_get_PerformanceIndexValueCollection, None)
	'''
	Get the collection of PerformanceIndex Value

	:type: recurdyn.AutoDesign.IADPerformanceIndexValueRobustOptimizationCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PerformanceIndexValueCollection": (12001, 2, (9, 0), (), "PerformanceIndexValueCollection", '{ABE15F3A-BE3E-4A4A-9A9B-50EFFBB1089A}'),
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

class IADPerformanceIndexValue(DispatchBaseClass):
	'''PerformanceIndex Value'''
	CLSID = IID('{24A6DAE3-98C0-4137-8870-63C4A04F253A}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ARName(self):
		return self._ApplyTypes_(*(12001, 2, (8, 0), (), "ARName", None))
	def _get_Description(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "Description", None))

	ARName = property(_get_ARName, None)
	'''
	AR Name

	:type: str
	'''
	Description = property(_get_Description, None)
	'''
	Description

	:type: str
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"ARName": (12001, 2, (8, 0), (), "ARName", None),
		"Description": (12002, 2, (8, 0), (), "Description", None),
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

class IADPerformanceIndexValueCollection(DispatchBaseClass):
	'''PerformanceIndexValue Collection'''
	CLSID = IID('{0D17420F-646F-40BC-BA44-3ED8D71659DB}')
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
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{24A6DAE3-98C0-4137-8870-63C4A04F253A}')
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
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{24A6DAE3-98C0-4137-8870-63C4A04F253A}')
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
		return win32com.client.util.Iterator(ob, '{24A6DAE3-98C0-4137-8870-63C4A04F253A}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{24A6DAE3-98C0-4137-8870-63C4A04F253A}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADPerformanceIndexValueOptimization(DispatchBaseClass):
	'''PerformanceIndex Value - Optimization'''
	CLSID = IID('{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ARName(self):
		return self._ApplyTypes_(*(12003, 2, (8, 0), (), "ARName", None))
	def _get_ConstraintGoalType(self):
		return self._ApplyTypes_(*(12007, 2, (3, 0), (), "ConstraintGoalType", '{537DBB5B-F92C-4933-95B8-6A049DB2D403}'))
	def _get_DefinitionType(self):
		return self._ApplyTypes_(*(12005, 2, (3, 0), (), "DefinitionType", '{25B34E7A-D5B7-4908-9E7A-B367DD9E7C0F}'))
	def _get_Description(self):
		return self._ApplyTypes_(*(12004, 2, (8, 0), (), "Description", None))
	def _get_ObjectiveGoalType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "ObjectiveGoalType", '{4FD8CFA2-CE43-4501-830B-9971CE55E521}'))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_Value(self):
		return self._ApplyTypes_(*(12008, 2, (5, 0), (), "Value", None))

	def _set_AnalysisResponse(self, value):
		if "AnalysisResponse" in self.__dict__: self.__dict__["AnalysisResponse"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_ConstraintGoalType(self, value):
		if "ConstraintGoalType" in self.__dict__: self.__dict__["ConstraintGoalType"] = value; return
		self._oleobj_.Invoke(*((12007, LCID, 4, 0) + (value,) + ()))
	def _set_DefinitionType(self, value):
		if "DefinitionType" in self.__dict__: self.__dict__["DefinitionType"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_ObjectiveGoalType(self, value):
		if "ObjectiveGoalType" in self.__dict__: self.__dict__["ObjectiveGoalType"] = value; return
		self._oleobj_.Invoke(*((12006, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_Value(self, value):
		if "Value" in self.__dict__: self.__dict__["Value"] = value; return
		self._oleobj_.Invoke(*((12008, LCID, 4, 0) + (value,) + ()))

	ARName = property(_get_ARName, None)
	'''
	AR Name

	:type: str
	'''
	ConstraintGoalType = property(_get_ConstraintGoalType, _set_ConstraintGoalType)
	'''
	Constraint Goal Type

	:type: recurdyn.AutoDesign.ConstraintGoalType
	'''
	DefinitionType = property(_get_DefinitionType, _set_DefinitionType)
	'''
	Definiton Type

	:type: recurdyn.AutoDesign.DefinitionType
	'''
	Description = property(_get_Description, None)
	'''
	Description

	:type: str
	'''
	ObjectiveGoalType = property(_get_ObjectiveGoalType, _set_ObjectiveGoalType)
	'''
	Objective Goal Type

	:type: recurdyn.AutoDesign.ObjectiveGoalType
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use PI

	:type: bool
	'''
	Value = property(_get_Value, _set_Value)
	'''
	Value

	:type: float
	'''
	AnalysisResponse = property(None, _set_AnalysisResponse)
	'''
	Analysis Response

	:type: recurdyn.AutoDesign.IADAnalysisResponse
	'''

	_prop_map_set_function_ = {
		"_set_AnalysisResponse": _set_AnalysisResponse,
		"_set_ConstraintGoalType": _set_ConstraintGoalType,
		"_set_DefinitionType": _set_DefinitionType,
		"_set_ObjectiveGoalType": _set_ObjectiveGoalType,
		"_set_Use": _set_Use,
		"_set_Value": _set_Value,
	}
	_prop_map_get_ = {
		"ARName": (12003, 2, (8, 0), (), "ARName", None),
		"ConstraintGoalType": (12007, 2, (3, 0), (), "ConstraintGoalType", '{537DBB5B-F92C-4933-95B8-6A049DB2D403}'),
		"DefinitionType": (12005, 2, (3, 0), (), "DefinitionType", '{25B34E7A-D5B7-4908-9E7A-B367DD9E7C0F}'),
		"Description": (12004, 2, (8, 0), (), "Description", None),
		"ObjectiveGoalType": (12006, 2, (3, 0), (), "ObjectiveGoalType", '{4FD8CFA2-CE43-4501-830B-9971CE55E521}'),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"Value": (12008, 2, (5, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"AnalysisResponse": ((12002, LCID, 4, 0),()),
		"ConstraintGoalType": ((12007, LCID, 4, 0),()),
		"DefinitionType": ((12005, LCID, 4, 0),()),
		"ObjectiveGoalType": ((12006, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"Value": ((12008, LCID, 4, 0),()),
	}
	def __call__(self):
		return self._ApplyTypes_(*(12008, 2, (5, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADPerformanceIndexValueOptimizationCollection(DispatchBaseClass):
	'''PerformanceIndexValue Collection - Optimization'''
	CLSID = IID('{E1417D0E-3016-43ED-BB4C-525D39CEDD02}')
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
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValueOptimization
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}')
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
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValueOptimization
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}')
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
		return win32com.client.util.Iterator(ob, '{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADPerformanceIndexValueReliability(DispatchBaseClass):
	'''PerformanceIndex Value - Reliability'''
	CLSID = IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ARName(self):
		return self._ApplyTypes_(*(12003, 2, (8, 0), (), "ARName", None))
	def _get_DefinitionType(self):
		return self._ApplyTypes_(*(12005, 2, (3, 0), (), "DefinitionType", '{25B34E7A-D5B7-4908-9E7A-B367DD9E7C0F}'))
	def _get_Description(self):
		return self._ApplyTypes_(*(12004, 2, (8, 0), (), "Description", None))
	def _get_GoalType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "GoalType", '{AC26D1B4-B440-4CD4-B9E2-5E4AF9BC9E2D}'))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_Value(self):
		return self._ApplyTypes_(*(12007, 2, (5, 0), (), "Value", None))

	def _set_AnalysisResponse(self, value):
		if "AnalysisResponse" in self.__dict__: self.__dict__["AnalysisResponse"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_GoalType(self, value):
		if "GoalType" in self.__dict__: self.__dict__["GoalType"] = value; return
		self._oleobj_.Invoke(*((12006, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_Value(self, value):
		if "Value" in self.__dict__: self.__dict__["Value"] = value; return
		self._oleobj_.Invoke(*((12007, LCID, 4, 0) + (value,) + ()))

	ARName = property(_get_ARName, None)
	'''
	AR Name

	:type: str
	'''
	DefinitionType = property(_get_DefinitionType, None)
	'''
	Definiton Type

	:type: recurdyn.AutoDesign.DefinitionType
	'''
	Description = property(_get_Description, None)
	'''
	Description

	:type: str
	'''
	GoalType = property(_get_GoalType, _set_GoalType)
	'''
	Constraint Goal Type

	:type: recurdyn.AutoDesign.ReliabilityConstraintGoalType
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use PI

	:type: bool
	'''
	Value = property(_get_Value, _set_Value)
	'''
	Limit Value

	:type: float
	'''
	AnalysisResponse = property(None, _set_AnalysisResponse)
	'''
	Analysis Response

	:type: recurdyn.AutoDesign.IADAnalysisResponse
	'''

	_prop_map_set_function_ = {
		"_set_AnalysisResponse": _set_AnalysisResponse,
		"_set_GoalType": _set_GoalType,
		"_set_Use": _set_Use,
		"_set_Value": _set_Value,
	}
	_prop_map_get_ = {
		"ARName": (12003, 2, (8, 0), (), "ARName", None),
		"DefinitionType": (12005, 2, (3, 0), (), "DefinitionType", '{25B34E7A-D5B7-4908-9E7A-B367DD9E7C0F}'),
		"Description": (12004, 2, (8, 0), (), "Description", None),
		"GoalType": (12006, 2, (3, 0), (), "GoalType", '{AC26D1B4-B440-4CD4-B9E2-5E4AF9BC9E2D}'),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"Value": (12007, 2, (5, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"AnalysisResponse": ((12002, LCID, 4, 0),()),
		"GoalType": ((12006, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"Value": ((12007, LCID, 4, 0),()),
	}
	def __call__(self):
		return self._ApplyTypes_(*(12007, 2, (5, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADPerformanceIndexValueReliabilityCollection(DispatchBaseClass):
	'''PerformanceIndexValue Collection - Reliability'''
	CLSID = IID('{921490EB-AF1C-4DC8-9901-2394EA388ED1}')
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
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValueReliability
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')
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
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValueReliability
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')
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
		return win32com.client.util.Iterator(ob, '{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADPerformanceIndexValueRobustOptimization(DispatchBaseClass):
	'''PerformanceIndex Value - RobustOptimization'''
	CLSID = IID('{E6741EBF-DDF9-4A34-8AFA-DF0796377699}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ARName(self):
		return self._ApplyTypes_(*(12003, 2, (8, 0), (), "ARName", None))
	def _get_AlphaWeight(self):
		return self._ApplyTypes_(*(12052, 2, (5, 0), (), "AlphaWeight", None))
	def _get_ConstraintGoalType(self):
		return self._ApplyTypes_(*(12007, 2, (3, 0), (), "ConstraintGoalType", '{537DBB5B-F92C-4933-95B8-6A049DB2D403}'))
	def _get_DefinitionType(self):
		return self._ApplyTypes_(*(12005, 2, (3, 0), (), "DefinitionType", '{25B34E7A-D5B7-4908-9E7A-B367DD9E7C0F}'))
	def _get_Description(self):
		return self._ApplyTypes_(*(12004, 2, (8, 0), (), "Description", None))
	def _get_ObjectiveGoalType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "ObjectiveGoalType", '{4FD8CFA2-CE43-4501-830B-9971CE55E521}'))
	def _get_RobustIndex(self):
		return self._ApplyTypes_(*(12051, 2, (5, 0), (), "RobustIndex", None))
	def _get_Use(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "Use", None))
	def _get_Value(self):
		return self._ApplyTypes_(*(12008, 2, (5, 0), (), "Value", None))

	def _set_AlphaWeight(self, value):
		if "AlphaWeight" in self.__dict__: self.__dict__["AlphaWeight"] = value; return
		self._oleobj_.Invoke(*((12052, LCID, 4, 0) + (value,) + ()))
	def _set_AnalysisResponse(self, value):
		if "AnalysisResponse" in self.__dict__: self.__dict__["AnalysisResponse"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_ConstraintGoalType(self, value):
		if "ConstraintGoalType" in self.__dict__: self.__dict__["ConstraintGoalType"] = value; return
		self._oleobj_.Invoke(*((12007, LCID, 4, 0) + (value,) + ()))
	def _set_DefinitionType(self, value):
		if "DefinitionType" in self.__dict__: self.__dict__["DefinitionType"] = value; return
		self._oleobj_.Invoke(*((12005, LCID, 4, 0) + (value,) + ()))
	def _set_ObjectiveGoalType(self, value):
		if "ObjectiveGoalType" in self.__dict__: self.__dict__["ObjectiveGoalType"] = value; return
		self._oleobj_.Invoke(*((12006, LCID, 4, 0) + (value,) + ()))
	def _set_RobustIndex(self, value):
		if "RobustIndex" in self.__dict__: self.__dict__["RobustIndex"] = value; return
		self._oleobj_.Invoke(*((12051, LCID, 4, 0) + (value,) + ()))
	def _set_Use(self, value):
		if "Use" in self.__dict__: self.__dict__["Use"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_Value(self, value):
		if "Value" in self.__dict__: self.__dict__["Value"] = value; return
		self._oleobj_.Invoke(*((12008, LCID, 4, 0) + (value,) + ()))

	ARName = property(_get_ARName, None)
	'''
	AR Name

	:type: str
	'''
	AlphaWeight = property(_get_AlphaWeight, _set_AlphaWeight)
	'''
	Alpha Weight

	:type: float
	'''
	ConstraintGoalType = property(_get_ConstraintGoalType, _set_ConstraintGoalType)
	'''
	Constraint Goal Type

	:type: recurdyn.AutoDesign.ConstraintGoalType
	'''
	DefinitionType = property(_get_DefinitionType, _set_DefinitionType)
	'''
	Definiton Type

	:type: recurdyn.AutoDesign.DefinitionType
	'''
	Description = property(_get_Description, None)
	'''
	Description

	:type: str
	'''
	ObjectiveGoalType = property(_get_ObjectiveGoalType, _set_ObjectiveGoalType)
	'''
	Objective Goal Type

	:type: recurdyn.AutoDesign.ObjectiveGoalType
	'''
	RobustIndex = property(_get_RobustIndex, _set_RobustIndex)
	'''
	Robust Index

	:type: float
	'''
	Use = property(_get_Use, _set_Use)
	'''
	Use PI

	:type: bool
	'''
	Value = property(_get_Value, _set_Value)
	'''
	Value

	:type: float
	'''
	AnalysisResponse = property(None, _set_AnalysisResponse)
	'''
	Analysis Response

	:type: recurdyn.AutoDesign.IADAnalysisResponse
	'''

	_prop_map_set_function_ = {
		"_set_AlphaWeight": _set_AlphaWeight,
		"_set_AnalysisResponse": _set_AnalysisResponse,
		"_set_ConstraintGoalType": _set_ConstraintGoalType,
		"_set_DefinitionType": _set_DefinitionType,
		"_set_ObjectiveGoalType": _set_ObjectiveGoalType,
		"_set_RobustIndex": _set_RobustIndex,
		"_set_Use": _set_Use,
		"_set_Value": _set_Value,
	}
	_prop_map_get_ = {
		"ARName": (12003, 2, (8, 0), (), "ARName", None),
		"AlphaWeight": (12052, 2, (5, 0), (), "AlphaWeight", None),
		"ConstraintGoalType": (12007, 2, (3, 0), (), "ConstraintGoalType", '{537DBB5B-F92C-4933-95B8-6A049DB2D403}'),
		"DefinitionType": (12005, 2, (3, 0), (), "DefinitionType", '{25B34E7A-D5B7-4908-9E7A-B367DD9E7C0F}'),
		"Description": (12004, 2, (8, 0), (), "Description", None),
		"ObjectiveGoalType": (12006, 2, (3, 0), (), "ObjectiveGoalType", '{4FD8CFA2-CE43-4501-830B-9971CE55E521}'),
		"RobustIndex": (12051, 2, (5, 0), (), "RobustIndex", None),
		"Use": (12001, 2, (11, 0), (), "Use", None),
		"Value": (12008, 2, (5, 0), (), "Value", None),
	}
	_prop_map_put_ = {
		"AlphaWeight": ((12052, LCID, 4, 0),()),
		"AnalysisResponse": ((12002, LCID, 4, 0),()),
		"ConstraintGoalType": ((12007, LCID, 4, 0),()),
		"DefinitionType": ((12005, LCID, 4, 0),()),
		"ObjectiveGoalType": ((12006, LCID, 4, 0),()),
		"RobustIndex": ((12051, LCID, 4, 0),()),
		"Use": ((12001, LCID, 4, 0),()),
		"Value": ((12008, LCID, 4, 0),()),
	}
	def __call__(self):
		return self._ApplyTypes_(*(12008, 2, (5, 0), (), "Value", None))
	def __str__(self, *args):
		return str(self.__call__(*args))
	def __int__(self, *args):
		return int(self.__call__(*args))
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADPerformanceIndexValueRobustOptimizationCollection(DispatchBaseClass):
	'''PerformanceIndexValue Collection - Robust Optimization'''
	CLSID = IID('{ABE15F3A-BE3E-4A4A-9A9B-50EFFBB1089A}')
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
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValueRobustOptimization
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{E6741EBF-DDF9-4A34-8AFA-DF0796377699}')
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
		:rtype: recurdyn.AutoDesign.IADPerformanceIndexValueRobustOptimization
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{E6741EBF-DDF9-4A34-8AFA-DF0796377699}')
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
		return win32com.client.util.Iterator(ob, '{E6741EBF-DDF9-4A34-8AFA-DF0796377699}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{E6741EBF-DDF9-4A34-8AFA-DF0796377699}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADResultSheetMonteCarloReliability(DispatchBaseClass):
	'''ResultSheet - MonteCarlo Reliability'''
	CLSID = IID('{AE3EFE31-E75A-43FB-9923-BCB2F2B4CB3B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def DistributionOfSamplingPoints(self, DV):
		'''
		Distribution Of Sampling Points
		
		:param DV: IADDesignVariableValueReliability
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12001, 1, (8197, 0), ((9, 1),), 'DistributionOfSamplingPoints', None,DV
			)


	def PerformanceIndexAverage(self, performance):
		'''
		Statistical Distribution of Performance Index - Average
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(12006, LCID, 1, (5, 0), ((9, 1),),performance
			)


	def PerformanceIndexKurtosis(self, performance):
		'''
		Statistical Distribution of Performance Index - Kurtosis
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(12011, LCID, 1, (5, 0), ((9, 1),),performance
			)


	def PerformanceIndexMedian(self, performance):
		'''
		Statistical Distribution of Performance Index - Median
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(12007, LCID, 1, (5, 0), ((9, 1),),performance
			)


	def PerformanceIndexMode(self, performance):
		'''
		Statistical Distribution of Performance Index - Mode
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(12008, LCID, 1, (5, 0), ((9, 1),),performance
			)


	def PerformanceIndexProbability(self, performance):
		'''
		Probability Distribution of Performance Index
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12005, 1, (8197, 0), ((9, 1),), 'PerformanceIndexProbability', None,performance
			)


	def PerformanceIndexResult(self, performance):
		'''
		Result of Performance Index
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12004, 1, (8197, 0), ((9, 1),), 'PerformanceIndexResult', None,performance
			)


	def PerformanceIndexSkewness(self, performance):
		'''
		Statistical Distribution of Performance Index - Skewness
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(12010, LCID, 1, (5, 0), ((9, 1),),performance
			)


	def PerformanceIndexStandardDeviation(self, performance):
		'''
		Statistical Distribution of Performance Index - Standard Deviation
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(12009, LCID, 1, (5, 0), ((9, 1),),performance
			)


	def StatisticalFrequency(self, performance):
		'''
		Statistical Distribution of Performance Index
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: list[int]
		'''
		return self._ApplyTypes_(12003, 1, (8195, 0), ((9, 1),), 'StatisticalFrequency', None,performance
			)


	def StatisticalMidPoint(self, performance):
		'''
		Statistical Distribution of Performance Index
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12002, 1, (8197, 0), ((9, 1),), 'StatisticalMidPoint', None,performance
			)


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

class IADResultSheetOptimization(DispatchBaseClass):
	'''ResultSheet - Optimization'''
	CLSID = IID('{8B6F84EB-837F-4794-A9DB-D0C118F54305}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AnalysisResponseResult(self, AR):
		'''
		Result of Analysis Response
		
		:param AR: IADAnalysisResponse
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12001, 1, (8197, 0), ((9, 1),), 'AnalysisResponseResult', None,AR
			)


	def NormalizedObject(self):
		'''
		Normalized Object
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12003, 1, (8197, 0), (), 'NormalizedObject', None,)


	def Violation(self):
		'''
		Violation method
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12002, 1, (8197, 0), (), 'Violation', None,)


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

class IADResultSheetRobustOptimization(DispatchBaseClass):
	'''ResultSheet - Robust Optimization'''
	CLSID = IID('{A0AE4D34-C41F-4AF7-83F6-310D52FADC4E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AnalysisResponseResult(self, AR):
		'''
		Result of Analysis Response
		
		:param AR: IADAnalysisResponse
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12001, 1, (8197, 0), ((9, 1),), 'AnalysisResponseResult', None,AR
			)


	def EstimatedStandardDeviation(self):
		'''
		Estimated Standard Deviation
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12051, 1, (8197, 0), (), 'EstimatedStandardDeviation', None,)


	def NormalizedObject(self):
		'''
		Normalized Object
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12003, 1, (8197, 0), (), 'NormalizedObject', None,)


	def RelaxedRobustIndex(self):
		'''
		Relaxed Robust Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12054, 1, (8197, 0), (), 'RelaxedRobustIndex', None,)


	def SampledStandardDeviation(self):
		'''
		Sampled Standard Deviation
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12052, 1, (8197, 0), (), 'SampledStandardDeviation', None,)


	def UserDefinedRobustIndex(self):
		'''
		User Defined Robust Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12053, 1, (8197, 0), (), 'UserDefinedRobustIndex', None,)


	def Violation(self):
		'''
		Violation method
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12002, 1, (8197, 0), (), 'Violation', None,)


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

class IADResultSheetSAOReliability(DispatchBaseClass):
	'''ResultSheet - SAO Reliability'''
	CLSID = IID('{090D60A3-B9C2-4E96-8B46-9224257A6C8B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CriticalLimitFunctionError(self):
		'''
		Critical Limit Function Error
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12002, 1, (8197, 0), (), 'CriticalLimitFunctionError', None,)


	def PerformanceIndexResult(self, performance):
		'''
		Result of Performance Index
		
		:param performance: IADPerformanceIndexValueReliability
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12001, 1, (8197, 0), ((9, 1),), 'PerformanceIndexResult', None,performance
			)


	def Probability(self):
		'''
		Probability method
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12004, 1, (8197, 0), (), 'Probability', None,)


	def ReliabilityIndexError(self):
		'''
		Reliability Index Error
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12003, 1, (8197, 0), (), 'ReliabilityIndexError', None,)


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

class IADRobustOptimizationControl(DispatchBaseClass):
	'''RobustOptimization Control'''
	CLSID = IID('{EA42004C-FAA2-4507-B161-FCC1E8CFD5B8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_ConvergenceTolerance(self):
		return self._ApplyTypes_(*(12052, 2, (9, 0), (), "ConvergenceTolerance", '{3C2D3CAD-1681-493B-A387-87E60A34606F}'))
	def _get_MetaModel(self):
		return self._ApplyTypes_(*(12051, 2, (9, 0), (), "MetaModel", '{F7310378-6376-4E72-8590-21B13F775AB4}'))
	def _get_NumberOfTrials(self):
		return self._ApplyTypes_(*(12053, 2, (19, 0), (), "NumberOfTrials", None))
	def _get_SamplePoints(self):
		return self._ApplyTypes_(*(12103, 2, (19, 0), (), "SamplePoints", None))
	def _get_SaveResult(self):
		return self._ApplyTypes_(*(12003, 2, (8, 0), (), "SaveResult", None))
	def _get_SimulationType(self):
		return self._ApplyTypes_(*(12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'))
	def _get_UseSaveResult(self):
		return self._ApplyTypes_(*(12002, 2, (11, 0), (), "UseSaveResult", None))
	def _get_ValidationType(self):
		return self._ApplyTypes_(*(12101, 2, (3, 0), (), "ValidationType", '{43AAFFED-0880-44F4-A863-408879D3ED8C}'))
	def _get_VarianceEstimationMethodType(self):
		return self._ApplyTypes_(*(12102, 2, (3, 0), (), "VarianceEstimationMethodType", '{57E9204D-3EE2-4788-9AC9-F6BAFDA506BD}'))

	def _set_SamplePoints(self, value):
		if "SamplePoints" in self.__dict__: self.__dict__["SamplePoints"] = value; return
		self._oleobj_.Invoke(*((12103, LCID, 4, 0) + (value,) + ()))
	def _set_SaveResult(self, value):
		if "SaveResult" in self.__dict__: self.__dict__["SaveResult"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_SimulationType(self, value):
		if "SimulationType" in self.__dict__: self.__dict__["SimulationType"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UseSaveResult(self, value):
		if "UseSaveResult" in self.__dict__: self.__dict__["UseSaveResult"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_ValidationType(self, value):
		if "ValidationType" in self.__dict__: self.__dict__["ValidationType"] = value; return
		self._oleobj_.Invoke(*((12101, LCID, 4, 0) + (value,) + ()))
	def _set_VarianceEstimationMethodType(self, value):
		if "VarianceEstimationMethodType" in self.__dict__: self.__dict__["VarianceEstimationMethodType"] = value; return
		self._oleobj_.Invoke(*((12102, LCID, 4, 0) + (value,) + ()))

	ConvergenceTolerance = property(_get_ConvergenceTolerance, None)
	'''
	Convergence Tolerance

	:type: recurdyn.AutoDesign.IADConvergenceToleranceOptimization
	'''
	MetaModel = property(_get_MetaModel, None)
	'''
	Meta Model

	:type: recurdyn.AutoDesign.IADMetaModel
	'''
	NumberOfTrials = property(_get_NumberOfTrials, None)
	'''
	Number of trials

	:type: int
	'''
	SamplePoints = property(_get_SamplePoints, _set_SamplePoints)
	'''
	SamplePoints for Validation

	:type: int
	'''
	SaveResult = property(_get_SaveResult, _set_SaveResult)
	'''
	Save results

	:type: str
	'''
	SimulationType = property(_get_SimulationType, _set_SimulationType)
	'''
	Simulation Type

	:type: recurdyn.AutoDesign.ADSimulationType
	'''
	UseSaveResult = property(_get_UseSaveResult, _set_UseSaveResult)
	'''
	Use save results

	:type: bool
	'''
	ValidationType = property(_get_ValidationType, _set_ValidationType)
	'''
	Validation Type

	:type: recurdyn.AutoDesign.ValidationType
	'''
	VarianceEstimationMethodType = property(_get_VarianceEstimationMethodType, _set_VarianceEstimationMethodType)
	'''
	Variance Estimation Method Type

	:type: recurdyn.AutoDesign.VarianceEstimationMethodType
	'''

	_prop_map_set_function_ = {
		"_set_SamplePoints": _set_SamplePoints,
		"_set_SaveResult": _set_SaveResult,
		"_set_SimulationType": _set_SimulationType,
		"_set_UseSaveResult": _set_UseSaveResult,
		"_set_ValidationType": _set_ValidationType,
		"_set_VarianceEstimationMethodType": _set_VarianceEstimationMethodType,
	}
	_prop_map_get_ = {
		"ConvergenceTolerance": (12052, 2, (9, 0), (), "ConvergenceTolerance", '{3C2D3CAD-1681-493B-A387-87E60A34606F}'),
		"MetaModel": (12051, 2, (9, 0), (), "MetaModel", '{F7310378-6376-4E72-8590-21B13F775AB4}'),
		"NumberOfTrials": (12053, 2, (19, 0), (), "NumberOfTrials", None),
		"SamplePoints": (12103, 2, (19, 0), (), "SamplePoints", None),
		"SaveResult": (12003, 2, (8, 0), (), "SaveResult", None),
		"SimulationType": (12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'),
		"UseSaveResult": (12002, 2, (11, 0), (), "UseSaveResult", None),
		"ValidationType": (12101, 2, (3, 0), (), "ValidationType", '{43AAFFED-0880-44F4-A863-408879D3ED8C}'),
		"VarianceEstimationMethodType": (12102, 2, (3, 0), (), "VarianceEstimationMethodType", '{57E9204D-3EE2-4788-9AC9-F6BAFDA506BD}'),
	}
	_prop_map_put_ = {
		"SamplePoints": ((12103, LCID, 4, 0),()),
		"SaveResult": ((12003, LCID, 4, 0),()),
		"SimulationType": ((12001, LCID, 4, 0),()),
		"UseSaveResult": ((12002, LCID, 4, 0),()),
		"ValidationType": ((12101, LCID, 4, 0),()),
		"VarianceEstimationMethodType": ((12102, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADScreeningVariable(DispatchBaseClass):
	'''Screening Variable'''
	CLSID = IID('{23B3FD64-1889-4D1E-9CF2-5A39543F8806}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def ClearScreenedDV(self):
		'''
		Clear Screened DV
		'''
		return self._oleobj_.InvokeTypes(12010, LCID, 1, (24, 0), (),)


	def ProbabilityDensity(self):
		'''
		Probability Density
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12007, 1, (8197, 0), (), 'ProbabilityDensity', None,)


	def ProbabilityDensityAllDataWithDP(self, DP):
		'''
		Probability Density
		
		:param DP: IADDesignParameter
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12009, 1, (8197, 0), ((9, 1),), 'ProbabilityDensityAllDataWithDP', None,DP
			)


	def ProbabilityDensityWithDP(self, DP):
		'''
		Probability Density
		
		:param DP: IADDesignParameter
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(12008, LCID, 1, (5, 0), ((9, 1),),DP
			)


	def SaveCurrentModel(self):
		'''
		Save a Model with Screened DV
		'''
		return self._oleobj_.InvokeTypes(12011, LCID, 1, (24, 0), (),)


	def SaveNewModel(self, name, bOverWrite):
		'''
		Save a Model with Screened DV
		
		:param name: str
		:param bOverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(12012, LCID, 1, (24, 0), ((8, 1), (11, 1)),name
			, bOverWrite)


	def SensitivityMagnitude(self):
		'''
		Magnitude of Sensitivity
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12004, 1, (8197, 0), (), 'SensitivityMagnitude', None,)


	def SensitivityMagnitudeAllDataWithDP(self, DP):
		'''
		Magnitude of Sensitivity
		
		:param DP: IADDesignParameter
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12006, 1, (8197, 0), ((9, 1),), 'SensitivityMagnitudeAllDataWithDP', None,DP
			)


	def SensitivityMagnitudeWithDP(self, DP):
		'''
		Magnitude of Sensitivity
		
		:param DP: IADDesignParameter
		:rtype: float
		'''
		return self._oleobj_.InvokeTypes(12005, LCID, 1, (5, 0), ((9, 1),),DP
			)


	def _get_ARName(self):
		return self._ApplyTypes_(*(12002, 2, (8, 0), (), "ARName", None))
	def _get_ScreenedDV(self):
		return self._ApplyTypes_(*(12003, 2, (8203, 0), (), "ScreenedDV", None))

	def _set_ScreenedDV(self, value):
		if "ScreenedDV" in self.__dict__: self.__dict__["ScreenedDV"] = value; return
		variantValue = win32com.client.VARIANT(8203, value)
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (variantValue,) + ()))
	def _set_SelectAnalysisResponse(self, value):
		if "SelectAnalysisResponse" in self.__dict__: self.__dict__["SelectAnalysisResponse"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))

	ARName = property(_get_ARName, None)
	'''
	Selected  Analysis Response Name

	:type: str
	'''
	ScreenedDV = property(_get_ScreenedDV, _set_ScreenedDV)
	'''
	Screened DV

	:type: list[bool]
	'''
	SelectAnalysisResponse = property(None, _set_SelectAnalysisResponse)
	'''
	Select Analysis Response

	:type: recurdyn.AutoDesign.IADAnalysisResponse
	'''

	_prop_map_set_function_ = {
		"_set_ScreenedDV": _set_ScreenedDV,
		"_set_SelectAnalysisResponse": _set_SelectAnalysisResponse,
	}
	_prop_map_get_ = {
		"ARName": (12002, 2, (8, 0), (), "ARName", None),
		"ScreenedDV": (12003, 2, (8203, 0), (), "ScreenedDV", None),
	}
	_prop_map_put_ = {
		"ScreenedDV": ((12003, LCID, 4, 0),()),
		"SelectAnalysisResponse": ((12001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADSimulationControl(DispatchBaseClass):
	'''SimulationControl'''
	CLSID = IID('{0838C8AB-285F-4456-8E62-2C7BC633DB4C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_SaveResult(self):
		return self._ApplyTypes_(*(12003, 2, (8, 0), (), "SaveResult", None))
	def _get_SimulationType(self):
		return self._ApplyTypes_(*(12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'))
	def _get_UseSaveResult(self):
		return self._ApplyTypes_(*(12002, 2, (11, 0), (), "UseSaveResult", None))

	def _set_SaveResult(self, value):
		if "SaveResult" in self.__dict__: self.__dict__["SaveResult"] = value; return
		self._oleobj_.Invoke(*((12003, LCID, 4, 0) + (value,) + ()))
	def _set_SimulationType(self, value):
		if "SimulationType" in self.__dict__: self.__dict__["SimulationType"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))
	def _set_UseSaveResult(self, value):
		if "UseSaveResult" in self.__dict__: self.__dict__["UseSaveResult"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))

	SaveResult = property(_get_SaveResult, _set_SaveResult)
	'''
	Save results

	:type: str
	'''
	SimulationType = property(_get_SimulationType, _set_SimulationType)
	'''
	Simulation Type

	:type: recurdyn.AutoDesign.ADSimulationType
	'''
	UseSaveResult = property(_get_UseSaveResult, _set_UseSaveResult)
	'''
	Use save results

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_SaveResult": _set_SaveResult,
		"_set_SimulationType": _set_SimulationType,
		"_set_UseSaveResult": _set_UseSaveResult,
	}
	_prop_map_get_ = {
		"SaveResult": (12003, 2, (8, 0), (), "SaveResult", None),
		"SimulationType": (12001, 2, (3, 0), (), "SimulationType", '{7BB6E64D-2FCE-4303-BECE-2F03205CA387}'),
		"UseSaveResult": (12002, 2, (11, 0), (), "UseSaveResult", None),
	}
	_prop_map_put_ = {
		"SaveResult": ((12003, LCID, 4, 0),()),
		"SimulationType": ((12001, LCID, 4, 0),()),
		"UseSaveResult": ((12002, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADSimulationHistoryValue(DispatchBaseClass):
	'''Simulation History Value'''
	CLSID = IID('{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AR(self):
		'''
		Analysis Response
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12007, 1, (8197, 0), (), 'AR', None,)


	def DV(self):
		'''
		Design Variable
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12008, 1, (8197, 0), (), 'DV', None,)


	def _get_DesignCost(self):
		return self._ApplyTypes_(*(12003, 2, (5, 0), (), "DesignCost", None))
	def _get_SimulationDescription(self):
		return self._ApplyTypes_(*(12004, 2, (8, 0), (), "SimulationDescription", None))
	def _get_SimulationStatus(self):
		return self._ApplyTypes_(*(12005, 2, (3, 0), (), "SimulationStatus", '{8EABF107-E2FA-4E81-AD75-C4F166884A0A}'))
	def _get_UseExport(self):
		return self._ApplyTypes_(*(12002, 2, (11, 0), (), "UseExport", None))
	def _get_UseUpdate(self):
		return self._ApplyTypes_(*(12001, 2, (11, 0), (), "UseUpdate", None))
	def _get_Violation(self):
		return self._ApplyTypes_(*(12006, 2, (5, 0), (), "Violation", None))

	def _set_UseExport(self, value):
		if "UseExport" in self.__dict__: self.__dict__["UseExport"] = value; return
		self._oleobj_.Invoke(*((12002, LCID, 4, 0) + (value,) + ()))
	def _set_UseUpdate(self, value):
		if "UseUpdate" in self.__dict__: self.__dict__["UseUpdate"] = value; return
		self._oleobj_.Invoke(*((12001, LCID, 4, 0) + (value,) + ()))

	DesignCost = property(_get_DesignCost, None)
	'''
	DesignCost

	:type: float
	'''
	SimulationDescription = property(_get_SimulationDescription, None)
	'''
	Simulation Description

	:type: str
	'''
	SimulationStatus = property(_get_SimulationStatus, None)
	'''
	Simulation Status

	:type: recurdyn.AutoDesign.SimulationStatusType
	'''
	UseExport = property(_get_UseExport, _set_UseExport)
	'''
	Use Export flag

	:type: bool
	'''
	UseUpdate = property(_get_UseUpdate, _set_UseUpdate)
	'''
	Use Update flag

	:type: bool
	'''
	Violation = property(_get_Violation, None)
	'''
	Violation

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_UseExport": _set_UseExport,
		"_set_UseUpdate": _set_UseUpdate,
	}
	_prop_map_get_ = {
		"DesignCost": (12003, 2, (5, 0), (), "DesignCost", None),
		"SimulationDescription": (12004, 2, (8, 0), (), "SimulationDescription", None),
		"SimulationStatus": (12005, 2, (3, 0), (), "SimulationStatus", '{8EABF107-E2FA-4E81-AD75-C4F166884A0A}'),
		"UseExport": (12002, 2, (11, 0), (), "UseExport", None),
		"UseUpdate": (12001, 2, (11, 0), (), "UseUpdate", None),
		"Violation": (12006, 2, (5, 0), (), "Violation", None),
	}
	_prop_map_put_ = {
		"UseExport": ((12002, LCID, 4, 0),()),
		"UseUpdate": ((12001, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IADSimulationHistoryValueCollection(DispatchBaseClass):
	'''Simulation History Collection'''
	CLSID = IID('{848C36F6-B86F-404E-A809-D8687EC91DEB}')
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
		:rtype: recurdyn.AutoDesign.IADSimulationHistoryValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}')
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
		:rtype: recurdyn.AutoDesign.IADSimulationHistoryValue
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}')
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
		return win32com.client.util.Iterator(ob, '{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IADSummarySheetMonteCarloReliability(DispatchBaseClass):
	'''SummarySheet - MonteCarlo Reliability'''
	CLSID = IID('{AB84ECBA-52ED-470B-BD07-9E4F851BFDC0}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def COVProability(self):
		'''
		Coefficient of Variance¡¯ of Peformance Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12004, 1, (8197, 0), (), 'COVProability', None,)


	def Mean(self):
		'''
		Mean of Peformance Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12002, 1, (8197, 0), (), 'Mean', None,)


	def Param1(self):
		'''
		Param 1
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12006, 1, (8197, 0), (), 'Param1', None,)


	def Param2(self):
		'''
		Param 2
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12007, 1, (8197, 0), (), 'Param2', None,)


	def Param3(self):
		'''
		Param 3
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12008, 1, (8197, 0), (), 'Param3', None,)


	def ProbabilityFailure(self):
		'''
		Probability Failure of Peformance Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12001, 1, (8197, 0), (), 'ProbabilityFailure', None,)


	def RelativeNorm(self):
		'''
		Relative Norm of Peformance Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12005, 1, (8197, 0), (), 'RelativeNorm', None,)


	def StandardDeviation(self):
		'''
		Standard Deviation of Peformance Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12003, 1, (8197, 0), (), 'StandardDeviation', None,)


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

class IADSummarySheetOptimization(DispatchBaseClass):
	'''SummarySheet - Optimization'''
	CLSID = IID('{1CFAE095-09EA-43A3-ABE0-9412CC096017}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def ApplyToCurrentModel(self):
		'''
		Apply To Current Model
		'''
		return self._oleobj_.InvokeTypes(12004, LCID, 1, (24, 0), (),)


	def CreateNewOptimumModel(self, name, bOverWrite):
		'''
		Create New Optimum Model
		
		:param name: str
		:param bOverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(12003, LCID, 1, (24, 0), ((8, 1), (11, 1)),name
			, bOverWrite)


	def OptimumAR(self):
		'''
		Optimum Value of Analysis Responses
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12002, 1, (8197, 0), (), 'OptimumAR', None,)


	def OptimumDV(self):
		'''
		Optimum Value of Design Variables
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12001, 1, (8197, 0), (), 'OptimumDV', None,)


	def _get_DOEMethodType(self):
		return self._ApplyTypes_(*(12005, 2, (3, 0), (), "DOEMethodType", '{22E7B466-BB8D-47A0-A967-442E38BCA533}'))
	def _get_InitialSampleRuns(self):
		return self._ApplyTypes_(*(12008, 2, (19, 0), (), "InitialSampleRuns", None))
	def _get_MetaModelingMethodType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "MetaModelingMethodType", '{CDD675EF-2B10-454D-874A-79C9EA607FD7}'))
	def _get_OptimalDesignReulst(self):
		return self._ApplyTypes_(*(12012, 2, (8, 0), (), "OptimalDesignReulst", None))
	def _get_PolynomialFunctionType(self):
		return self._ApplyTypes_(*(12007, 2, (3, 0), (), "PolynomialFunctionType", '{4FCC8FE8-CFFA-4794-BC1F-0C095D91C142}'))
	def _get_SAORuns(self):
		return self._ApplyTypes_(*(12009, 2, (19, 0), (), "SAORuns", None))
	def _get_SAORunsDuplication(self):
		return self._ApplyTypes_(*(12010, 2, (19, 0), (), "SAORunsDuplication", None))
	def _get_TotalEvaluations(self):
		return self._ApplyTypes_(*(12011, 2, (19, 0), (), "TotalEvaluations", None))

	DOEMethodType = property(_get_DOEMethodType, None)
	'''
	DOEMethod Type

	:type: recurdyn.AutoDesign.MetaModelDOEMethodType
	'''
	InitialSampleRuns = property(_get_InitialSampleRuns, None)
	'''
	Initial Sample Runs

	:type: int
	'''
	MetaModelingMethodType = property(_get_MetaModelingMethodType, None)
	'''
	Meta Modeling Method Type

	:type: recurdyn.AutoDesign.MetaModelingMethodType
	'''
	OptimalDesignReulst = property(_get_OptimalDesignReulst, None)
	'''
	Optimal Design Reulst

	:type: str
	'''
	PolynomialFunctionType = property(_get_PolynomialFunctionType, None)
	'''
	Polynomial Function Type

	:type: recurdyn.AutoDesign.PolynomialFunctionType
	'''
	SAORuns = property(_get_SAORuns, None)
	'''
	SAO Runs

	:type: int
	'''
	SAORunsDuplication = property(_get_SAORunsDuplication, None)
	'''
	SAO Duplication Runs

	:type: int
	'''
	TotalEvaluations = property(_get_TotalEvaluations, None)
	'''
	Total Evaluations

	:type: int
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DOEMethodType": (12005, 2, (3, 0), (), "DOEMethodType", '{22E7B466-BB8D-47A0-A967-442E38BCA533}'),
		"InitialSampleRuns": (12008, 2, (19, 0), (), "InitialSampleRuns", None),
		"MetaModelingMethodType": (12006, 2, (3, 0), (), "MetaModelingMethodType", '{CDD675EF-2B10-454D-874A-79C9EA607FD7}'),
		"OptimalDesignReulst": (12012, 2, (8, 0), (), "OptimalDesignReulst", None),
		"PolynomialFunctionType": (12007, 2, (3, 0), (), "PolynomialFunctionType", '{4FCC8FE8-CFFA-4794-BC1F-0C095D91C142}'),
		"SAORuns": (12009, 2, (19, 0), (), "SAORuns", None),
		"SAORunsDuplication": (12010, 2, (19, 0), (), "SAORunsDuplication", None),
		"TotalEvaluations": (12011, 2, (19, 0), (), "TotalEvaluations", None),
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

class IADSummarySheetRobustOptimization(DispatchBaseClass):
	'''SummarySheet - Robust Optimization'''
	CLSID = IID('{0EAE4DF9-530B-4C01-8E01-05B444BA70FB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def ApplyToCurrentModel(self):
		'''
		Apply To Current Model
		'''
		return self._oleobj_.InvokeTypes(12004, LCID, 1, (24, 0), (),)


	def CreateNewOptimumModel(self, name, bOverWrite):
		'''
		Create New Optimum Model
		
		:param name: str
		:param bOverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(12003, LCID, 1, (24, 0), ((8, 1), (11, 1)),name
			, bOverWrite)


	def OptimumAR(self):
		'''
		Optimum Value of Analysis Responses
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12002, 1, (8197, 0), (), 'OptimumAR', None,)


	def OptimumDV(self):
		'''
		Optimum Value of Design Variables
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12001, 1, (8197, 0), (), 'OptimumDV', None,)


	def RelaxedRobustIndex(self):
		'''
		Relaxed Robust Index of Analysis Responses
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12052, 1, (8197, 0), (), 'RelaxedRobustIndex', None,)


	def SampledStandardDeviation(self):
		'''
		Sampled Standard Deviation of Analysis Responses
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12051, 1, (8197, 0), (), 'SampledStandardDeviation', None,)


	def _get_DOEMethodType(self):
		return self._ApplyTypes_(*(12005, 2, (3, 0), (), "DOEMethodType", '{22E7B466-BB8D-47A0-A967-442E38BCA533}'))
	def _get_InitialSampleRuns(self):
		return self._ApplyTypes_(*(12008, 2, (19, 0), (), "InitialSampleRuns", None))
	def _get_MetaModelingMethodType(self):
		return self._ApplyTypes_(*(12006, 2, (3, 0), (), "MetaModelingMethodType", '{CDD675EF-2B10-454D-874A-79C9EA607FD7}'))
	def _get_OptimalDesignReulst(self):
		return self._ApplyTypes_(*(12012, 2, (8, 0), (), "OptimalDesignReulst", None))
	def _get_PolynomialFunctionType(self):
		return self._ApplyTypes_(*(12007, 2, (3, 0), (), "PolynomialFunctionType", '{4FCC8FE8-CFFA-4794-BC1F-0C095D91C142}'))
	def _get_SAORuns(self):
		return self._ApplyTypes_(*(12009, 2, (19, 0), (), "SAORuns", None))
	def _get_SAORunsDuplication(self):
		return self._ApplyTypes_(*(12010, 2, (19, 0), (), "SAORunsDuplication", None))
	def _get_TotalEvaluations(self):
		return self._ApplyTypes_(*(12011, 2, (19, 0), (), "TotalEvaluations", None))
	def _get_Validation(self):
		return self._ApplyTypes_(*(12053, 2, (19, 0), (), "Validation", None))

	DOEMethodType = property(_get_DOEMethodType, None)
	'''
	DOEMethod Type

	:type: recurdyn.AutoDesign.MetaModelDOEMethodType
	'''
	InitialSampleRuns = property(_get_InitialSampleRuns, None)
	'''
	Initial Sample Runs

	:type: int
	'''
	MetaModelingMethodType = property(_get_MetaModelingMethodType, None)
	'''
	Meta Modeling Method Type

	:type: recurdyn.AutoDesign.MetaModelingMethodType
	'''
	OptimalDesignReulst = property(_get_OptimalDesignReulst, None)
	'''
	Optimal Design Reulst

	:type: str
	'''
	PolynomialFunctionType = property(_get_PolynomialFunctionType, None)
	'''
	Polynomial Function Type

	:type: recurdyn.AutoDesign.PolynomialFunctionType
	'''
	SAORuns = property(_get_SAORuns, None)
	'''
	SAO Runs

	:type: int
	'''
	SAORunsDuplication = property(_get_SAORunsDuplication, None)
	'''
	SAO Duplication Runs

	:type: int
	'''
	TotalEvaluations = property(_get_TotalEvaluations, None)
	'''
	Total Evaluations

	:type: int
	'''
	Validation = property(_get_Validation, None)
	'''
	Validation

	:type: int
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DOEMethodType": (12005, 2, (3, 0), (), "DOEMethodType", '{22E7B466-BB8D-47A0-A967-442E38BCA533}'),
		"InitialSampleRuns": (12008, 2, (19, 0), (), "InitialSampleRuns", None),
		"MetaModelingMethodType": (12006, 2, (3, 0), (), "MetaModelingMethodType", '{CDD675EF-2B10-454D-874A-79C9EA607FD7}'),
		"OptimalDesignReulst": (12012, 2, (8, 0), (), "OptimalDesignReulst", None),
		"PolynomialFunctionType": (12007, 2, (3, 0), (), "PolynomialFunctionType", '{4FCC8FE8-CFFA-4794-BC1F-0C095D91C142}'),
		"SAORuns": (12009, 2, (19, 0), (), "SAORuns", None),
		"SAORunsDuplication": (12010, 2, (19, 0), (), "SAORunsDuplication", None),
		"TotalEvaluations": (12011, 2, (19, 0), (), "TotalEvaluations", None),
		"Validation": (12053, 2, (19, 0), (), "Validation", None),
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

class IADSummarySheetSAOReliability(DispatchBaseClass):
	'''SummarySheet - SAO Reliability'''
	CLSID = IID('{34968513-D22A-4A7C-876F-D97623DC5BB8}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def MPP_BETA_MEAN(self):
		'''
		Most Probable Failure Point Information, Reliability(BETA) / MEAN
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12005, 1, (8197, 0), (), 'MPP_BETA_MEAN', None,)


	def MPP_BETA_STDV(self):
		'''
		Most Probable Failure Point Information, Reliability(BETA) / Standard Deviation(STDV)
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12006, 1, (8197, 0), (), 'MPP_BETA_STDV', None,)


	def MPP_DV(self):
		'''
		Most Probable Failure Point Information, MPP_DV
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12004, 1, (8197, 0), (), 'MPP_DV', None,)


	def MPP_PROB_MEAN(self):
		'''
		Most Probable Failure Point Information, Probability(PROB) / MEAN
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12007, 1, (8197, 0), (), 'MPP_PROB_MEAN', None,)


	def MPP_PROB_STDV(self):
		'''
		Most Probable Failure Point Information, Probability(PROB) / Standard Deviation(STDV)
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12008, 1, (8197, 0), (), 'MPP_PROB_STDV', None,)


	def Param1(self):
		'''
		Param 1
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12009, 1, (8197, 0), (), 'Param1', None,)


	def Param2(self):
		'''
		Param 2
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12010, 1, (8197, 0), (), 'Param2', None,)


	def Param3(self):
		'''
		Param 3
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12011, 1, (8197, 0), (), 'Param3', None,)


	def ProbabilityFailure(self):
		'''
		Probability Failure of Peformance Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12003, 1, (8197, 0), (), 'ProbabilityFailure', None,)


	def ReliabilityIndex(self):
		'''
		Reliability Index of Peformance Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12002, 1, (8197, 0), (), 'ReliabilityIndex', None,)


	def ValueAtMPP(self):
		'''
		Most Probable Failure Point of Peformance Index
		
		:rtype: list[float]
		'''
		return self._ApplyTypes_(12001, 1, (8197, 0), (), 'ValueAtMPP', None,)


	def _get_DRMRuns(self):
		return self._ApplyTypes_(*(12014, 2, (19, 0), (), "DRMRuns", None))
	def _get_InitialDOERuns(self):
		return self._ApplyTypes_(*(12012, 2, (19, 0), (), "InitialDOERuns", None))
	def _get_SAORuns(self):
		return self._ApplyTypes_(*(12013, 2, (19, 0), (), "SAORuns", None))

	DRMRuns = property(_get_DRMRuns, None)
	'''
	DRM Runs

	:type: int
	'''
	InitialDOERuns = property(_get_InitialDOERuns, None)
	'''
	Initial DOE Runs

	:type: int
	'''
	SAORuns = property(_get_SAORuns, None)
	'''
	SAO Runs

	:type: int
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DRMRuns": (12014, 2, (19, 0), (), "DRMRuns", None),
		"InitialDOERuns": (12012, 2, (19, 0), (), "InitialDOERuns", None),
		"SAORuns": (12013, 2, (19, 0), (), "SAORuns", None),
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

class IAutoDesignToolkit(DispatchBaseClass):
	'''AutoDesign Toolkit'''
	CLSID = IID('{4CD4C1F4-2733-4B7D-88AC-5CA98D412E5F}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateAnalysisResponse(self, name, type):
		'''
		Creates Analysis Response
		
		:param name: str
		:param type: AnalysisResponseType
		:rtype: recurdyn.AutoDesign.IADAnalysisResponse
		'''
		ret = self._oleobj_.InvokeTypes(12011, LCID, 1, (9, 0), ((8, 1), (3, 1)),name
			, type)
		if ret is not None:
			ret = Dispatch(ret, 'CreateAnalysisResponse', '{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')
		return ret

	def CreateDesignParamter(self, name, type):
		'''
		Creates Design Parameter
		
		:param name: str
		:param type: DesignParameterType
		:rtype: recurdyn.AutoDesign.IADDesignParameter
		'''
		ret = self._oleobj_.InvokeTypes(12010, LCID, 1, (9, 0), ((8, 1), (3, 1)),name
			, type)
		if ret is not None:
			ret = Dispatch(ret, 'CreateDesignParamter', '{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_AnalysisResponseCollection(self):
		return self._ApplyTypes_(*(12009, 2, (9, 0), (), "AnalysisResponseCollection", '{A0BF51C0-1CAE-4EF2-AD18-A604B83B3990}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DesignParameterCollection(self):
		return self._ApplyTypes_(*(12008, 2, (9, 0), (), "DesignParameterCollection", '{39B651B4-D8F5-4B36-BA9B-5A5EB8F32D1B}'))
	def _get_DesignStudy(self):
		return self._ApplyTypes_(*(12002, 2, (9, 0), (), "DesignStudy", '{6BCFA125-3F0C-42DA-AA88-8949B4625E32}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(12001, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_MonteCarloReliability(self):
		return self._ApplyTypes_(*(12006, 2, (9, 0), (), "MonteCarloReliability", '{EFD6644C-E331-4E80-B99A-DBFD663B4F9C}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Optimization(self):
		return self._ApplyTypes_(*(12003, 2, (9, 0), (), "Optimization", '{21F86233-F1EC-444F-BFAD-5480C4DBA5B1}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_RobustOptimization(self):
		return self._ApplyTypes_(*(12004, 2, (9, 0), (), "RobustOptimization", '{94B1BEFB-5C73-4A2A-92F2-997AF6CBAD62}'))
	def _get_SAOReliability(self):
		return self._ApplyTypes_(*(12005, 2, (9, 0), (), "SAOReliability", '{A481E1C1-5497-468B-B072-CDB83437D5D3}'))
	def _get_SimulationHistory(self):
		return self._ApplyTypes_(*(12007, 2, (9, 0), (), "SimulationHistory", '{A17668CB-A526-42D3-B8CC-21A35B441EAB}'))
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

	AnalysisResponseCollection = property(_get_AnalysisResponseCollection, None)
	'''
	Get the collection of Analysis Response

	:type: recurdyn.AutoDesign.IADAnalysisResponseCollection
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DesignParameterCollection = property(_get_DesignParameterCollection, None)
	'''
	Get the collection of Design Parameter

	:type: recurdyn.AutoDesign.IADDesignParameterCollection
	'''
	DesignStudy = property(_get_DesignStudy, None)
	'''
	DesignStudy

	:type: recurdyn.AutoDesign.IADDesignStudy
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
	MonteCarloReliability = property(_get_MonteCarloReliability, None)
	'''
	MonteCarlo Reliability

	:type: recurdyn.AutoDesign.IADDesignMonteCarloReliability
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	Optimization = property(_get_Optimization, None)
	'''
	Optimization

	:type: recurdyn.AutoDesign.IADDesignOptimization
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
	RobustOptimization = property(_get_RobustOptimization, None)
	'''
	Robust Optimization

	:type: recurdyn.AutoDesign.IADDesignRobustOptimization
	'''
	SAOReliability = property(_get_SAOReliability, None)
	'''
	SAO Reliability

	:type: recurdyn.AutoDesign.IADDesignSAOReliability
	'''
	SimulationHistory = property(_get_SimulationHistory, None)
	'''
	Simulation History

	:type: recurdyn.AutoDesign.IADDesignSimulationHistory
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
		"AnalysisResponseCollection": (12009, 2, (9, 0), (), "AnalysisResponseCollection", '{A0BF51C0-1CAE-4EF2-AD18-A604B83B3990}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DesignParameterCollection": (12008, 2, (9, 0), (), "DesignParameterCollection", '{39B651B4-D8F5-4B36-BA9B-5A5EB8F32D1B}'),
		"DesignStudy": (12002, 2, (9, 0), (), "DesignStudy", '{6BCFA125-3F0C-42DA-AA88-8949B4625E32}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralSubSystem": (12001, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"MonteCarloReliability": (12006, 2, (9, 0), (), "MonteCarloReliability", '{EFD6644C-E331-4E80-B99A-DBFD663B4F9C}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Optimization": (12003, 2, (9, 0), (), "Optimization", '{21F86233-F1EC-444F-BFAD-5480C4DBA5B1}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RobustOptimization": (12004, 2, (9, 0), (), "RobustOptimization", '{94B1BEFB-5C73-4A2A-92F2-997AF6CBAD62}'),
		"SAOReliability": (12005, 2, (9, 0), (), "SAOReliability", '{A481E1C1-5497-468B-B072-CDB83437D5D3}'),
		"SimulationHistory": (12007, 2, (9, 0), (), "SimulationHistory", '{A17668CB-A526-42D3-B8CC-21A35B441EAB}'),
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

IADAnalysisControlMonteCarloReliability_vtables_dispatch_ = 1
IADAnalysisControlMonteCarloReliability_vtables_ = [
	(( 'UseNewSampling' , 'pVal' , ), 12051, (12051, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseNewSampling' , 'pVal' , ), 12051, (12051, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SamplingPoints' , 'pVal' , ), 12052, (12052, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SamplingPoints' , 'pVal' , ), 12052, (12052, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'SamplingMethodType' , 'pVal' , ), 12053, (12053, (), [ (3, 1, None, "IID('{53ECF8FC-F2B6-4C59-8C1D-F43035C81E6E}')") , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SamplingMethodType' , 'pVal' , ), 12053, (12053, (), [ (16387, 10, None, "IID('{53ECF8FC-F2B6-4C59-8C1D-F43035C81E6E}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IADAnalysisControlSAOReliability_vtables_dispatch_ = 1
IADAnalysisControlSAOReliability_vtables_ = [
	(( 'ConvergenceTolerance' , 'ppVal' , ), 12051, (12051, (), [ (16393, 10, None, "IID('{97D04758-E009-46C2-BE5F-AD4A1CB49AB5}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'HybridSamplingOptionType' , 'pVal' , ), 12052, (12052, (), [ (3, 1, None, "IID('{257F16C6-873D-4022-9DD6-D4D93F476387}')") , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'HybridSamplingOptionType' , 'pVal' , ), 12052, (12052, (), [ (16387, 10, None, "IID('{257F16C6-873D-4022-9DD6-D4D93F476387}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ReliablitySolverType' , 'pVal' , ), 12053, (12053, (), [ (3, 1, None, "IID('{3C183DD5-59F1-4593-8DF6-3F9AF6540039}')") , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ReliablitySolverType' , 'pVal' , ), 12053, (12053, (), [ (16387, 10, None, "IID('{3C183DD5-59F1-4593-8DF6-3F9AF6540039}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'LatinHybercubeSample' , 'pVal' , ), 12054, (12054, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'LatinHybercubeSample' , 'pVal' , ), 12054, (12054, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IADAnalysisResponse_vtables_dispatch_ = 1
IADAnalysisResponse_vtables_ = [
	(( 'Use' , 'pVal' , ), 12001, (12001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 12001, (12001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12002, (12002, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12002, (12002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AnalysisResponseType' , 'pVal' , ), 12003, (12003, (), [ (16387, 10, None, "IID('{2D2927C1-DFED-4562-BA6F-A310F6C417CF}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IADAnalysisResponseBasic_vtables_dispatch_ = 1
IADAnalysisResponseBasic_vtables_ = [
	(( 'ResultOutput' , 'ppVal' , ), 12051, (12051, (), [ (9, 1, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ResultOutput' , 'ppVal' , ), 12051, (12051, (), [ (16393, 10, None, "IID('{81E4B241-3167-4FAE-B0FE-3ED5AB7F4040}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TreatmentType' , 'pVal' , ), 12052, (12052, (), [ (3, 1, None, "IID('{90F45D5E-BEB4-47B0-9296-7DC9AA0ECDAC}')") , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'TreatmentType' , 'pVal' , ), 12052, (12052, (), [ (16387, 10, None, "IID('{90F45D5E-BEB4-47B0-9296-7DC9AA0ECDAC}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IADAnalysisResponseCollection_vtables_dispatch_ = 1
IADAnalysisResponseCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADAnalysisResponseFEResult_vtables_dispatch_ = 1
IADAnalysisResponseFEResult_vtables_ = [
	(( 'ResultType' , 'pVal' , ), 12051, (12051, (), [ (3, 1, None, "IID('{6C353CFD-C07B-4EBB-9F32-B0F8263445A8}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ResultType' , 'pVal' , ), 12051, (12051, (), [ (16387, 10, None, "IID('{6C353CFD-C07B-4EBB-9F32-B0F8263445A8}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TreatmentType' , 'pVal' , ), 12052, (12052, (), [ (3, 1, None, "IID('{5A785C7D-7AAD-454E-BC98-5E5FF448174C}')") , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'TreatmentType' , 'pVal' , ), 12052, (12052, (), [ (16387, 10, None, "IID('{5A785C7D-7AAD-454E-BC98-5E5FF448174C}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NodeElementSet' , 'ppVal' , ), 12053, (12053, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'NodeElementSet' , 'ppVal' , ), 12053, (12053, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IADAnalysisResponseProcessNet_vtables_dispatch_ = 1
IADAnalysisResponseProcessNet_vtables_ = [
	(( 'ADProcessNetType' , 'pVal' , ), 12051, (12051, (), [ (3, 1, None, "IID('{F79FD2CD-0BDC-4C34-B93C-8AC579120A20}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ADProcessNetType' , 'pVal' , ), 12051, (12051, (), [ (16387, 10, None, "IID('{F79FD2CD-0BDC-4C34-B93C-8AC579120A20}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ProcessNetDllProjectPath' , 'name' , ), 12052, (12052, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'ProcessNetDllProjectPath' , 'name' , ), 12052, (12052, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'ProcessNetFunctionName' , 'name' , ), 12053, (12053, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'ProcessNetFunctionName' , 'name' , ), 12053, (12053, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ProcessNetScriptPath' , 'name' , ), 12054, (12054, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ProcessNetScriptPath' , 'name' , ), 12054, (12054, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
]

IADAnalysisResponseScope_vtables_dispatch_ = 1
IADAnalysisResponseScope_vtables_ = [
	(( 'Scope' , 'ppVal' , ), 12051, (12051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Scope' , 'ppVal' , ), 12051, (12051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TreatmentType' , 'pVal' , ), 12052, (12052, (), [ (3, 1, None, "IID('{90F45D5E-BEB4-47B0-9296-7DC9AA0ECDAC}')") , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'TreatmentType' , 'pVal' , ), 12052, (12052, (), [ (16387, 10, None, "IID('{90F45D5E-BEB4-47B0-9296-7DC9AA0ECDAC}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IADConvergenceTolerance_vtables_dispatch_ = 1
IADConvergenceTolerance_vtables_ = [
	(( 'ObjectiveChangeRate' , 'pVal' , ), 12001, (12001, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveChangeRate' , 'pVal' , ), 12001, (12001, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LimitStateValue' , 'pVal' , ), 12002, (12002, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LimitStateValue' , 'pVal' , ), 12002, (12002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MaximumIteration' , 'pVal' , ), 12004, (12004, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MaximumIteration' , 'pVal' , ), 12004, (12004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IADConvergenceToleranceOptimization_vtables_dispatch_ = 1
IADConvergenceToleranceOptimization_vtables_ = [
	(( 'ObjectiveChangeRate' , 'pVal' , ), 12001, (12001, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveChangeRate' , 'pVal' , ), 12001, (12001, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'EqualityConstraints' , 'pVal' , ), 12002, (12002, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'EqualityConstraints' , 'pVal' , ), 12002, (12002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'InequalityConstraints' , 'pVal' , ), 12003, (12003, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'InequalityConstraints' , 'pVal' , ), 12003, (12003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'MaximumIteration' , 'pVal' , ), 12004, (12004, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'MaximumIteration' , 'pVal' , ), 12004, (12004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ConvergenceRelaxationControlType' , 'pVal' , ), 12005, (12005, (), [ (3, 1, None, "IID('{BEC0AB59-2285-4EF1-989D-DD586FBAA4C1}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ConvergenceRelaxationControlType' , 'pVal' , ), 12005, (12005, (), [ (16387, 10, None, "IID('{BEC0AB59-2285-4EF1-989D-DD586FBAA4C1}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IADCorrelationAnalysis_vtables_dispatch_ = 1
IADCorrelationAnalysis_vtables_ = [
	(( 'AnalysisResponseResult' , 'AR' , 'pVal' , ), 12001, (12001, (), [ (9, 1, None, "IID('{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IADDesignMonteCarloReliability_vtables_dispatch_ = 1
IADDesignMonteCarloReliability_vtables_ = [
	(( 'DesignVariable' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{F661EC5C-4647-4033-92BA-46E38C97192F}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndex' , 'ppVal' , ), 12002, (12002, (), [ (16393, 10, None, "IID('{7CFDA97B-0D26-4330-A9A7-33E67162C207}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AnalysisControl' , 'ppVal' , ), 12003, (12003, (), [ (16393, 10, None, "IID('{D8BE75E5-32E7-42DF-A930-8A591F57583B}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ResultSheet' , 'ppVal' , ), 12004, (12004, (), [ (16393, 10, None, "IID('{AE3EFE31-E75A-43FB-9923-BCB2F2B4CB3B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SummarySheet' , 'ppVal' , ), 12005, (12005, (), [ (16393, 10, None, "IID('{AB84ECBA-52ED-470B-BD07-9E4F851BFDC0}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 12006, (12006, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IADDesignOptimization_vtables_dispatch_ = 1
IADDesignOptimization_vtables_ = [
	(( 'DesignVariable' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{5BB9E831-64AE-4AD1-88DB-FE8D333C7934}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndex' , 'ppVal' , ), 12002, (12002, (), [ (16393, 10, None, "IID('{BBEBBABF-49D9-4B0B-A64F-007BD3B048EC}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'OptimizationControl' , 'ppVal' , ), 12003, (12003, (), [ (16393, 10, None, "IID('{FA5F5341-8EAE-4F15-92A0-4FA3B7425525}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ResultSheet' , 'ppVal' , ), 12004, (12004, (), [ (16393, 10, None, "IID('{8B6F84EB-837F-4794-A9DB-D0C118F54305}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SummarySheet' , 'ppVal' , ), 12005, (12005, (), [ (16393, 10, None, "IID('{1CFAE095-09EA-43A3-ABE0-9412CC096017}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 12006, (12006, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IADDesignParameter_vtables_dispatch_ = 1
IADDesignParameter_vtables_ = [
	(( 'Use' , 'pVal' , ), 12001, (12001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 12001, (12001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Current' , 'pVal' , ), 12002, (12002, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'LB' , 'pVal' , ), 12003, (12003, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'LB' , 'pVal' , ), 12003, (12003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UB' , 'pVal' , ), 12004, (12004, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UB' , 'pVal' , ), 12004, (12004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12005, (12005, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12005, (12005, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DesignParameterType' , 'pVal' , ), 12006, (12006, (), [ (16387, 10, None, "IID('{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IADDesignParameterAngular_vtables_dispatch_ = 1
IADDesignParameterAngular_vtables_ = [
	(( 'NodeSet' , 'ppVal' , ), 12051, (12051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NodeSet' , 'ppVal' , ), 12051, (12051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ConfigurationDesignType' , 'pVal' , ), 12052, (12052, (), [ (3, 1, None, "IID('{91B00663-8DB7-4C49-A8E4-CCEF2445220B}')") , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ConfigurationDesignType' , 'pVal' , ), 12052, (12052, (), [ (16387, 10, None, "IID('{91B00663-8DB7-4C49-A8E4-CCEF2445220B}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'RefMarker' , 'ppVal' , ), 12053, (12053, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RefMarker' , 'ppVal' , ), 12053, (12053, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RotationAxisUnitVector' , 'ppVal' , ), 12054, (12054, (), [ (16393, 10, None, "IID('{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ReferencePoint' , 'ppVal' , ), 12055, (12055, (), [ (16393, 10, None, "IID('{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

IADDesignParameterCollection_vtables_dispatch_ = 1
IADDesignParameterCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADDesignParameterCylindrical_vtables_dispatch_ = 1
IADDesignParameterCylindrical_vtables_ = [
	(( 'NodeSet' , 'ppVal' , ), 12051, (12051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NodeSet' , 'ppVal' , ), 12051, (12051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ConfigurationDesignType' , 'pVal' , ), 12052, (12052, (), [ (3, 1, None, "IID('{91B00663-8DB7-4C49-A8E4-CCEF2445220B}')") , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ConfigurationDesignType' , 'pVal' , ), 12052, (12052, (), [ (16387, 10, None, "IID('{91B00663-8DB7-4C49-A8E4-CCEF2445220B}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CenterRefMarker' , 'ppVal' , ), 12053, (12053, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CenterRefMarker' , 'ppVal' , ), 12053, (12053, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CenterAxisUnitVector' , 'ppVal' , ), 12054, (12054, (), [ (16393, 10, None, "IID('{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

IADDesignParameterDirect_vtables_dispatch_ = 1
IADDesignParameterDirect_vtables_ = [
	(( 'ParametricValue' , 'ppVal' , ), 12051, (12051, (), [ (9, 1, None, "IID('{3EEED3CE-62E8-4882-AAE6-4812B49927B5}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ParametricValue' , 'ppVal' , ), 12051, (12051, (), [ (16393, 10, None, "IID('{3EEED3CE-62E8-4882-AAE6-4812B49927B5}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
]

IADDesignParameterSpherical_vtables_dispatch_ = 1
IADDesignParameterSpherical_vtables_ = [
	(( 'NodeSet' , 'ppVal' , ), 12051, (12051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NodeSet' , 'ppVal' , ), 12051, (12051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ConfigurationDesignType' , 'pVal' , ), 12052, (12052, (), [ (3, 1, None, "IID('{91B00663-8DB7-4C49-A8E4-CCEF2445220B}')") , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ConfigurationDesignType' , 'pVal' , ), 12052, (12052, (), [ (16387, 10, None, "IID('{91B00663-8DB7-4C49-A8E4-CCEF2445220B}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CenterRefMarker' , 'ppVal' , ), 12053, (12053, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CenterRefMarker' , 'ppVal' , ), 12053, (12053, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IADDesignParameterTranslational_vtables_dispatch_ = 1
IADDesignParameterTranslational_vtables_ = [
	(( 'NodeSet' , 'ppVal' , ), 12051, (12051, (), [ (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NodeSet' , 'ppVal' , ), 12051, (12051, (), [ (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ConfigurationDesignType' , 'pVal' , ), 12052, (12052, (), [ (3, 1, None, "IID('{91B00663-8DB7-4C49-A8E4-CCEF2445220B}')") , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'ConfigurationDesignType' , 'pVal' , ), 12052, (12052, (), [ (16387, 10, None, "IID('{91B00663-8DB7-4C49-A8E4-CCEF2445220B}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'RefMarker' , 'ppVal' , ), 12053, (12053, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RefMarker' , 'ppVal' , ), 12053, (12053, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DirectionalUnitVector' , 'ppVal' , ), 12054, (12054, (), [ (16393, 10, None, "IID('{F67F5E56-F3F7-4249-BCBE-02B8D43716B0}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
]

IADDesignRobustOptimization_vtables_dispatch_ = 1
IADDesignRobustOptimization_vtables_ = [
	(( 'DesignVariable' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{21581656-E8B6-4C52-A435-6C6F7BC30720}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndex' , 'ppVal' , ), 12002, (12002, (), [ (16393, 10, None, "IID('{4C5071E8-AFE7-4056-B4B2-DD3CFD7A534B}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'OptimizationControl' , 'ppVal' , ), 12003, (12003, (), [ (16393, 10, None, "IID('{EA42004C-FAA2-4507-B161-FCC1E8CFD5B8}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ResultSheet' , 'ppVal' , ), 12004, (12004, (), [ (16393, 10, None, "IID('{A0AE4D34-C41F-4AF7-83F6-310D52FADC4E}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SummarySheet' , 'ppVal' , ), 12005, (12005, (), [ (16393, 10, None, "IID('{0EAE4DF9-530B-4C01-8E01-05B444BA70FB}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 12006, (12006, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IADDesignSAOReliability_vtables_dispatch_ = 1
IADDesignSAOReliability_vtables_ = [
	(( 'DesignVariable' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{F661EC5C-4647-4033-92BA-46E38C97192F}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndex' , 'ppVal' , ), 12002, (12002, (), [ (16393, 10, None, "IID('{7CFDA97B-0D26-4330-A9A7-33E67162C207}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'AnalysisControl' , 'ppVal' , ), 12003, (12003, (), [ (16393, 10, None, "IID('{9CF67D49-AFD5-46EA-B69E-50E384C63F41}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ResultSheet' , 'ppVal' , ), 12004, (12004, (), [ (16393, 10, None, "IID('{090D60A3-B9C2-4E96-8B46-9224257A6C8B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SummarySheet' , 'ppVal' , ), 12005, (12005, (), [ (16393, 10, None, "IID('{34968513-D22A-4A7C-876F-D97623DC5BB8}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 12006, (12006, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IADDesignSimulationHistory_vtables_dispatch_ = 1
IADDesignSimulationHistory_vtables_ = [
	(( 'SimulationHistoryValueCollection' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{848C36F6-B86F-404E-A809-D8687EC91DEB}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'name' , ), 12002, (12002, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'ExportAll' , 'name' , 'val' , 'bOverWrite' , ), 12003, (12003, (), [ 
			 (8, 1, None, None) , (8195, 1, None, "IID('{5C5BE52A-1289-44A9-8BFD-0C9AF2E44791}')") , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'name' , 'val' , 'startIndex' , 'endIndex' , 
			 'bOverWrite' , ), 12004, (12004, (), [ (8, 1, None, None) , (8195, 1, None, "IID('{5C5BE52A-1289-44A9-8BFD-0C9AF2E44791}')") , (19, 1, None, None) , 
			 (19, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Delete' , 'startIndex' , 'endIndex' , ), 12005, (12005, (), [ (19, 1, None, None) , 
			 (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DeleteAll' , ), 12006, (12006, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Check' , 'type' , 'flag' , 'startIndex' , 'endIndex' , 
			 ), 12007, (12007, (), [ (3, 1, None, "IID('{BC598FA0-D90D-497B-A7B0-F5A33DB19C80}')") , (11, 1, None, None) , (19, 1, None, None) , (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CheckAll' , 'type' , 'flag' , ), 12008, (12008, (), [ (3, 1, None, "IID('{BC598FA0-D90D-497B-A7B0-F5A33DB19C80}')") , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UpdateNewModel' , 'val' , 'name' , 'bOverWrite' , ), 12009, (12009, (), [ 
			 (9, 1, None, "IID('{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}')") , (8, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UpdateCurrentModel' , 'val' , ), 12010, (12010, (), [ (9, 1, None, "IID('{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
]

IADDesignStudy_vtables_dispatch_ = 1
IADDesignStudy_vtables_ = [
	(( 'DesignVariable' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{EA349BD0-8E34-435E-BDC8-22434008169E}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndex' , 'ppVal' , ), 12002, (12002, (), [ (16393, 10, None, "IID('{B29F78DD-B76C-407A-921F-E2305173B26D}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SimulationControl' , 'ppVal' , ), 12003, (12003, (), [ (16393, 10, None, "IID('{0838C8AB-285F-4456-8E62-2C7BC633DB4C}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'EffectAnalysis' , 'ppVal' , ), 12004, (12004, (), [ (16393, 10, None, "IID('{E6D34A7F-E67B-43F6-AD41-4E3526234647}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ScreeningVariable' , 'ppVal' , ), 12005, (12005, (), [ (16393, 10, None, "IID('{23B3FD64-1889-4D1E-9CF2-5A39543F8806}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CorrelationAnalysis' , 'ppVal' , ), 12006, (12006, (), [ (16393, 10, None, "IID('{23CD2F5A-F2CB-499B-907E-F52B2BEDCC86}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Execute' , ), 12007, (12007, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IADDesignVariable_vtables_dispatch_ = 1
IADDesignVariable_vtables_ = [
	(( 'DOEMethod' , 'pVal' , ), 12001, (12001, (), [ (3, 1, None, "IID('{3EAB6469-0B54-43D6-A51C-F29A31057AE2}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DOEMethod' , 'pVal' , ), 12001, (12001, (), [ (16387, 10, None, "IID('{3EAB6469-0B54-43D6-A51C-F29A31057AE2}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AllLevelSet' , 'pVal' , ), 12002, (12002, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'RequiredRuns' , 'pVal' , ), 12003, (12003, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RequiredRuns' , 'pVal' , ), 12003, (12003, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfTrials' , 'pVal' , ), 12004, (12004, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DesignVariableValueCollection' , 'ppVal' , ), 12005, (12005, (), [ (16393, 10, None, "IID('{4041B853-0350-4DC4-A516-53EB9B0EF3E6}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'SetDefault' , ), 12006, (12006, (), [ ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AllLevelSetExtendedPlackettBurman' , 'val' , ), 12007, (12007, (), [ (3, 1, None, "IID('{ACADFFA2-1946-46B6-A63E-9C26159BE237}')") , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'AllLevelSetFullFactorialDesign' , 'val' , ), 12008, (12008, (), [ (3, 1, None, "IID('{0FAC978E-C189-4B79-9702-1EC49F3303E0}')") , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'AllLevelSetBoseOrthogonalArray' , 'val' , ), 12009, (12009, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'AllLevelSetLevelBalancedDescriptiveDesign' , 'val' , ), 12010, (12010, (), [ (19, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CalculateAvailableLevelsOfBoseOrthogonalArray' , 'nDV' , 'pVal' , ), 12011, (12011, (), [ (19, 1, None, None) , 
			 (24579, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IADDesignVariableOptimization_vtables_dispatch_ = 1
IADDesignVariableOptimization_vtables_ = [
	(( 'DesignVariableValueCollection' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{4AE4ADC1-5D80-48D8-9DED-60AFF06B076F}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IADDesignVariableReliability_vtables_dispatch_ = 1
IADDesignVariableReliability_vtables_ = [
	(( 'DesignVariableValueCollection' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{26B20F68-D1FA-4DD6-B690-2C4AA0BC6B6F}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IADDesignVariableRobustOptimization_vtables_dispatch_ = 1
IADDesignVariableRobustOptimization_vtables_ = [
	(( 'DesignVariableValueCollection' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{FBDB8850-EF61-47B2-A7C8-EE7A36DEBAE1}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IADDesignVariableValue_vtables_dispatch_ = 1
IADDesignVariableValue_vtables_ = [
	(( 'DPName' , 'name' , ), 12001, (12001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12002, (12002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Level' , 'pVal' , ), 12003, (12003, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ExtendedPlackettBurmanLevelType' , ), 12004, (12004, (), [ (3, 1, None, "IID('{ACADFFA2-1946-46B6-A63E-9C26159BE237}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'LB' , 'pVal' , ), 12005, (12005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UB' , 'pVal' , ), 12006, (12006, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Mid' , 'pVal' , ), 12007, (12007, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Mid' , 'pVal' , ), 12007, (12007, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IADDesignVariableValueCollection_vtables_dispatch_ = 1
IADDesignVariableValueCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{3EDECE37-7EBE-4189-8F11-78C4FFC54E0C}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADDesignVariableValueOptimization_vtables_dispatch_ = 1
IADDesignVariableValueOptimization_vtables_ = [
	(( 'DPName' , 'name' , ), 12001, (12001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12002, (12002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Current' , 'pVal' , ), 12003, (12003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LB' , 'pVal' , ), 12004, (12004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UB' , 'pVal' , ), 12005, (12005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DesignVariableType' , 'pVal' , ), 12006, (12006, (), [ (3, 1, None, "IID('{87FFE66D-548A-420F-96FB-8ECBAD2762FD}')") , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DesignVariableType' , 'pVal' , ), 12006, (12006, (), [ (16387, 10, None, "IID('{87FFE66D-548A-420F-96FB-8ECBAD2762FD}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pVal' , ), 12007, (12007, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pVal' , ), 12007, (12007, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IADDesignVariableValueOptimizationCollection_vtables_dispatch_ = 1
IADDesignVariableValueOptimizationCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{FAD5D54F-8696-4C06-A2AE-6958AE3C15E3}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADDesignVariableValueReliability_vtables_dispatch_ = 1
IADDesignVariableValueReliability_vtables_ = [
	(( 'DPName' , 'name' , ), 12001, (12001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12002, (12002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Current' , 'pVal' , ), 12003, (12003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LB' , 'pVal' , ), 12004, (12004, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UB' , 'pVal' , ), 12005, (12005, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DesignVariableType' , 'pVal' , ), 12006, (12006, (), [ (16387, 10, None, "IID('{87FFE66D-548A-420F-96FB-8ECBAD2762FD}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'MeanValue' , 'pVal' , ), 12007, (12007, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'MeanValue' , 'pVal' , ), 12007, (12007, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ProbabilityDistributionType' , 'pVal' , ), 12008, (12008, (), [ (3, 1, None, "IID('{067A69BB-310D-4900-910B-520F40F6D5EF}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ProbabilityDistributionType' , 'pVal' , ), 12008, (12008, (), [ (16387, 10, None, "IID('{067A69BB-310D-4900-910B-520F40F6D5EF}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'DeviationType' , 'pVal' , ), 12009, (12009, (), [ (3, 1, None, "IID('{3A831DE1-C118-44B2-8774-238F0E9DB5BE}')") , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DeviationType' , 'pVal' , ), 12009, (12009, (), [ (16387, 10, None, "IID('{3A831DE1-C118-44B2-8774-238F0E9DB5BE}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DeviationValue' , 'pVal' , ), 12010, (12010, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DeviationValue' , 'pVal' , ), 12010, (12010, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IADDesignVariableValueReliabilityCollection_vtables_dispatch_ = 1
IADDesignVariableValueReliabilityCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{BA8157EE-5975-42E0-833D-A5ADE8CD107B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADDesignVariableValueRobustOptimization_vtables_dispatch_ = 1
IADDesignVariableValueRobustOptimization_vtables_ = [
	(( 'StatisticalInfoType' , 'pVal' , ), 12051, (12051, (), [ (3, 1, None, "IID('{AC42F832-BB21-4945-859C-2BFDC16F09C7}')") , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'StatisticalInfoType' , 'pVal' , ), 12051, (12051, (), [ (16387, 10, None, "IID('{AC42F832-BB21-4945-859C-2BFDC16F09C7}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DeviationType' , 'pVal' , ), 12052, (12052, (), [ (3, 1, None, "IID('{3A831DE1-C118-44B2-8774-238F0E9DB5BE}')") , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DeviationType' , 'pVal' , ), 12052, (12052, (), [ (16387, 10, None, "IID('{3A831DE1-C118-44B2-8774-238F0E9DB5BE}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DeviationValue' , 'pVal' , ), 12053, (12053, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'DeviationValue' , 'pVal' , ), 12053, (12053, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IADDesignVariableValueRobustOptimizationCollection_vtables_dispatch_ = 1
IADDesignVariableValueRobustOptimizationCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{44C71273-E70C-4AC7-B285-7741F8DF8F49}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADEffectAnalysis_vtables_dispatch_ = 1
IADEffectAnalysis_vtables_ = [
	(( 'SelectAnalysisResponse' , ), 12001, (12001, (), [ (9, 1, None, "IID('{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ARName' , 'name' , ), 12002, (12002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Variation' , 'DV' , 'pVal' , ), 12003, (12003, (), [ (9, 1, None, "IID('{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'EffectValues' , 'DV' , 'pVal' , ), 12004, (12004, (), [ (9, 1, None, "IID('{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MinimizationCombination' , 'pVal' , ), 12005, (12005, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MaximizationCombination' , 'pVal' , ), 12006, (12006, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Simulation' , 'type' , ), 12007, (12007, (), [ (3, 1, None, "IID('{A1DF4D20-76DE-4FBF-A406-2347D2D7A266}')") , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IADMetaModel_vtables_dispatch_ = 1
IADMetaModel_vtables_ = [
	(( 'UseAutoSelection' , 'pVal' , ), 12001, (12001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoSelection' , 'pVal' , ), 12001, (12001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseDOEMethod' , 'pVal' , ), 12002, (12002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseDOEMethod' , 'pVal' , ), 12002, (12002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UseGetFromSimulationHistory' , 'pVal' , ), 12003, (12003, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UseGetFromSimulationHistory' , 'pVal' , ), 12003, (12003, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DOEMethodType' , 'pVal' , ), 12004, (12004, (), [ (3, 1, None, "IID('{22E7B466-BB8D-47A0-A967-442E38BCA533}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'DOEMethodType' , 'pVal' , ), 12004, (12004, (), [ (16387, 10, None, "IID('{22E7B466-BB8D-47A0-A967-442E38BCA533}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DiscreteLatinHypercubeDesignNumber' , 'pVal' , ), 12005, (12005, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DiscreteLatinHypercubeDesignNumber' , 'pVal' , ), 12005, (12005, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'MetaModelingMethodType' , 'pVal' , ), 12006, (12006, (), [ (3, 1, None, "IID('{CDD675EF-2B10-454D-874A-79C9EA607FD7}')") , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'MetaModelingMethodType' , 'pVal' , ), 12006, (12006, (), [ (16387, 10, None, "IID('{CDD675EF-2B10-454D-874A-79C9EA607FD7}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'PolynomialFunctionType' , 'pVal' , ), 12007, (12007, (), [ (3, 1, None, "IID('{4FCC8FE8-CFFA-4794-BC1F-0C095D91C142}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'PolynomialFunctionType' , 'pVal' , ), 12007, (12007, (), [ (16387, 10, None, "IID('{4FCC8FE8-CFFA-4794-BC1F-0C095D91C142}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IADOptimizationControl_vtables_dispatch_ = 1
IADOptimizationControl_vtables_ = [
	(( 'MetaModel' , 'ppVal' , ), 12051, (12051, (), [ (16393, 10, None, "IID('{F7310378-6376-4E72-8590-21B13F775AB4}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ConvergenceTolerance' , 'ppVal' , ), 12052, (12052, (), [ (16393, 10, None, "IID('{3C2D3CAD-1681-493B-A387-87E60A34606F}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfTrials' , 'pVal' , ), 12053, (12053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
]

IADPerformanceIndex_vtables_dispatch_ = 1
IADPerformanceIndex_vtables_ = [
	(( 'PerformanceIndexValueCollection' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{0D17420F-646F-40BC-BA44-3ED8D71659DB}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IADPerformanceIndexOptimization_vtables_dispatch_ = 1
IADPerformanceIndexOptimization_vtables_ = [
	(( 'PerformanceIndexValueCollection' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{E1417D0E-3016-43ED-BB4C-525D39CEDD02}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AddPerformanceIndexValue' , 'ppVal' , ), 12002, (12002, (), [ (16393, 10, None, "IID('{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DeletePerformanceIndexValue' , 'pVal' , ), 12003, (12003, (), [ (9, 1, None, "IID('{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IADPerformanceIndexReliability_vtables_dispatch_ = 1
IADPerformanceIndexReliability_vtables_ = [
	(( 'PerformanceIndexValueCollection' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{921490EB-AF1C-4DC8-9901-2394EA388ED1}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AddPerformanceIndexValue' , 'ppVal' , ), 12002, (12002, (), [ (16393, 10, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DeletePerformanceIndexValue' , 'pVal' , ), 12003, (12003, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IADPerformanceIndexRobustOptimization_vtables_dispatch_ = 1
IADPerformanceIndexRobustOptimization_vtables_ = [
	(( 'PerformanceIndexValueCollection' , 'ppVal' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{ABE15F3A-BE3E-4A4A-9A9B-50EFFBB1089A}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'AddPerformanceIndexValue' , 'ppVal' , ), 12002, (12002, (), [ (16393, 10, None, "IID('{E6741EBF-DDF9-4A34-8AFA-DF0796377699}')") , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'DeletePerformanceIndexValue' , 'pVal' , ), 12003, (12003, (), [ (9, 1, None, "IID('{E6741EBF-DDF9-4A34-8AFA-DF0796377699}')") , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IADPerformanceIndexValue_vtables_dispatch_ = 1
IADPerformanceIndexValue_vtables_ = [
	(( 'ARName' , 'name' , ), 12001, (12001, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12002, (12002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
]

IADPerformanceIndexValueCollection_vtables_dispatch_ = 1
IADPerformanceIndexValueCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{24A6DAE3-98C0-4137-8870-63C4A04F253A}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADPerformanceIndexValueOptimization_vtables_dispatch_ = 1
IADPerformanceIndexValueOptimization_vtables_ = [
	(( 'Use' , 'pVal' , ), 12001, (12001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 12001, (12001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AnalysisResponse' , ), 12002, (12002, (), [ (9, 1, None, "IID('{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ARName' , 'name' , ), 12003, (12003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12004, (12004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DefinitionType' , 'pVal' , ), 12005, (12005, (), [ (3, 1, None, "IID('{25B34E7A-D5B7-4908-9E7A-B367DD9E7C0F}')") , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'DefinitionType' , 'pVal' , ), 12005, (12005, (), [ (16387, 10, None, "IID('{25B34E7A-D5B7-4908-9E7A-B367DD9E7C0F}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveGoalType' , 'pVal' , ), 12006, (12006, (), [ (3, 1, None, "IID('{4FD8CFA2-CE43-4501-830B-9971CE55E521}')") , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ObjectiveGoalType' , 'pVal' , ), 12006, (12006, (), [ (16387, 10, None, "IID('{4FD8CFA2-CE43-4501-830B-9971CE55E521}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintGoalType' , 'pVal' , ), 12007, (12007, (), [ (3, 1, None, "IID('{537DBB5B-F92C-4933-95B8-6A049DB2D403}')") , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ConstraintGoalType' , 'pVal' , ), 12007, (12007, (), [ (16387, 10, None, "IID('{537DBB5B-F92C-4933-95B8-6A049DB2D403}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pVal' , ), 12008, (12008, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pVal' , ), 12008, (12008, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IADPerformanceIndexValueOptimizationCollection_vtables_dispatch_ = 1
IADPerformanceIndexValueOptimizationCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADPerformanceIndexValueReliability_vtables_dispatch_ = 1
IADPerformanceIndexValueReliability_vtables_ = [
	(( 'Use' , 'pVal' , ), 12001, (12001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Use' , 'pVal' , ), 12001, (12001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'AnalysisResponse' , ), 12002, (12002, (), [ (9, 1, None, "IID('{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')") , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ARName' , 'name' , ), 12003, (12003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Description' , 'name' , ), 12004, (12004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DefinitionType' , 'pVal' , ), 12005, (12005, (), [ (16387, 10, None, "IID('{25B34E7A-D5B7-4908-9E7A-B367DD9E7C0F}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GoalType' , 'pVal' , ), 12006, (12006, (), [ (3, 1, None, "IID('{AC26D1B4-B440-4CD4-B9E2-5E4AF9BC9E2D}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GoalType' , 'pVal' , ), 12006, (12006, (), [ (16387, 10, None, "IID('{AC26D1B4-B440-4CD4-B9E2-5E4AF9BC9E2D}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pVal' , ), 12007, (12007, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Value' , 'pVal' , ), 12007, (12007, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IADPerformanceIndexValueReliabilityCollection_vtables_dispatch_ = 1
IADPerformanceIndexValueReliabilityCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADPerformanceIndexValueRobustOptimization_vtables_dispatch_ = 1
IADPerformanceIndexValueRobustOptimization_vtables_ = [
	(( 'RobustIndex' , 'pVal' , ), 12051, (12051, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'RobustIndex' , 'pVal' , ), 12051, (12051, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AlphaWeight' , 'pVal' , ), 12052, (12052, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'AlphaWeight' , 'pVal' , ), 12052, (12052, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IADPerformanceIndexValueRobustOptimizationCollection_vtables_dispatch_ = 1
IADPerformanceIndexValueRobustOptimizationCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{E6741EBF-DDF9-4A34-8AFA-DF0796377699}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADResultSheetMonteCarloReliability_vtables_dispatch_ = 1
IADResultSheetMonteCarloReliability_vtables_ = [
	(( 'DistributionOfSamplingPoints' , 'DV' , 'pVal' , ), 12001, (12001, (), [ (9, 1, None, "IID('{BA8157EE-5975-42E0-833D-A5ADE8CD107B}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'StatisticalMidPoint' , 'performance' , 'pVal' , ), 12002, (12002, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StatisticalFrequency' , 'performance' , 'pVal' , ), 12003, (12003, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (24579, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndexResult' , 'performance' , 'pVal' , ), 12004, (12004, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndexProbability' , 'performance' , 'pVal' , ), 12005, (12005, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndexAverage' , 'performance' , 'pVal' , ), 12006, (12006, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndexMedian' , 'performance' , 'pVal' , ), 12007, (12007, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndexMode' , 'performance' , 'pVal' , ), 12008, (12008, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndexStandardDeviation' , 'performance' , 'pVal' , ), 12009, (12009, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndexSkewness' , 'performance' , 'pVal' , ), 12010, (12010, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'PerformanceIndexKurtosis' , 'performance' , 'pVal' , ), 12011, (12011, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
]

IADResultSheetOptimization_vtables_dispatch_ = 1
IADResultSheetOptimization_vtables_ = [
	(( 'AnalysisResponseResult' , 'AR' , 'pVal' , ), 12001, (12001, (), [ (9, 1, None, "IID('{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Violation' , 'pVal' , ), 12002, (12002, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'NormalizedObject' , 'pVal' , ), 12003, (12003, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IADResultSheetRobustOptimization_vtables_dispatch_ = 1
IADResultSheetRobustOptimization_vtables_ = [
	(( 'EstimatedStandardDeviation' , 'pVal' , ), 12051, (12051, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SampledStandardDeviation' , 'pVal' , ), 12052, (12052, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'UserDefinedRobustIndex' , 'pVal' , ), 12053, (12053, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'RelaxedRobustIndex' , 'pVal' , ), 12054, (12054, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
]

IADResultSheetSAOReliability_vtables_dispatch_ = 1
IADResultSheetSAOReliability_vtables_ = [
	(( 'PerformanceIndexResult' , 'performance' , 'pVal' , ), 12001, (12001, (), [ (9, 1, None, "IID('{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'CriticalLimitFunctionError' , 'pVal' , ), 12002, (12002, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ReliabilityIndexError' , 'pVal' , ), 12003, (12003, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Probability' , 'pVal' , ), 12004, (12004, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IADRobustOptimizationControl_vtables_dispatch_ = 1
IADRobustOptimizationControl_vtables_ = [
	(( 'ValidationType' , 'pVal' , ), 12101, (12101, (), [ (3, 1, None, "IID('{43AAFFED-0880-44F4-A863-408879D3ED8C}')") , ], 1 , 4 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ValidationType' , 'pVal' , ), 12101, (12101, (), [ (16387, 10, None, "IID('{43AAFFED-0880-44F4-A863-408879D3ED8C}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'VarianceEstimationMethodType' , 'pVal' , ), 12102, (12102, (), [ (3, 1, None, "IID('{57E9204D-3EE2-4788-9AC9-F6BAFDA506BD}')") , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'VarianceEstimationMethodType' , 'pVal' , ), 12102, (12102, (), [ (16387, 10, None, "IID('{57E9204D-3EE2-4788-9AC9-F6BAFDA506BD}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SamplePoints' , 'pVal' , ), 12103, (12103, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'SamplePoints' , 'pVal' , ), 12103, (12103, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IADScreeningVariable_vtables_dispatch_ = 1
IADScreeningVariable_vtables_ = [
	(( 'SelectAnalysisResponse' , ), 12001, (12001, (), [ (9, 1, None, "IID('{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ARName' , 'name' , ), 12002, (12002, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ScreenedDV' , 'pVal' , ), 12003, (12003, (), [ (8203, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ScreenedDV' , 'pVal' , ), 12003, (12003, (), [ (24587, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SensitivityMagnitude' , 'pVal' , ), 12004, (12004, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SensitivityMagnitudeWithDP' , 'DP' , 'pVal' , ), 12005, (12005, (), [ (9, 1, None, "IID('{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')") , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SensitivityMagnitudeAllDataWithDP' , 'DP' , 'pVal' , ), 12006, (12006, (), [ (9, 1, None, "IID('{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ProbabilityDensity' , 'pVal' , ), 12007, (12007, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'ProbabilityDensityWithDP' , 'DP' , 'pVal' , ), 12008, (12008, (), [ (9, 1, None, "IID('{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')") , 
			 (16389, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'ProbabilityDensityAllDataWithDP' , 'DP' , 'pVal' , ), 12009, (12009, (), [ (9, 1, None, "IID('{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')") , 
			 (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'ClearScreenedDV' , ), 12010, (12010, (), [ ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'SaveCurrentModel' , ), 12011, (12011, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SaveNewModel' , 'name' , 'bOverWrite' , ), 12012, (12012, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IADSimulationControl_vtables_dispatch_ = 1
IADSimulationControl_vtables_ = [
	(( 'SimulationType' , 'pVal' , ), 12001, (12001, (), [ (3, 1, None, "IID('{7BB6E64D-2FCE-4303-BECE-2F03205CA387}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'SimulationType' , 'pVal' , ), 12001, (12001, (), [ (16387, 10, None, "IID('{7BB6E64D-2FCE-4303-BECE-2F03205CA387}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseSaveResult' , 'pVal' , ), 12002, (12002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseSaveResult' , 'pVal' , ), 12002, (12002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'SaveResult' , 'name' , ), 12003, (12003, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SaveResult' , 'name' , ), 12003, (12003, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
]

IADSimulationHistoryValue_vtables_dispatch_ = 1
IADSimulationHistoryValue_vtables_ = [
	(( 'UseUpdate' , 'pVal' , ), 12001, (12001, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseUpdate' , 'pVal' , ), 12001, (12001, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseExport' , 'pVal' , ), 12002, (12002, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseExport' , 'pVal' , ), 12002, (12002, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DesignCost' , 'pVal' , ), 12003, (12003, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'SimulationDescription' , 'pVal' , ), 12004, (12004, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'SimulationStatus' , 'pVal' , ), 12005, (12005, (), [ (16387, 10, None, "IID('{8EABF107-E2FA-4E81-AD75-C4F166884A0A}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Violation' , 'pVal' , ), 12006, (12006, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'AR' , 'pVal' , ), 12007, (12007, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DV' , 'pVal' , ), 12008, (12008, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
]

IADSimulationHistoryValueCollection_vtables_dispatch_ = 1
IADSimulationHistoryValueCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IADSummarySheetMonteCarloReliability_vtables_dispatch_ = 1
IADSummarySheetMonteCarloReliability_vtables_ = [
	(( 'ProbabilityFailure' , 'pVal' , ), 12001, (12001, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Mean' , 'pVal' , ), 12002, (12002, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StandardDeviation' , 'pVal' , ), 12003, (12003, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'COVProability' , 'pVal' , ), 12004, (12004, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'RelativeNorm' , 'pVal' , ), 12005, (12005, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'Param1' , 'pVal' , ), 12006, (12006, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'Param2' , 'pVal' , ), 12007, (12007, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Param3' , 'pVal' , ), 12008, (12008, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IADSummarySheetOptimization_vtables_dispatch_ = 1
IADSummarySheetOptimization_vtables_ = [
	(( 'OptimumDV' , 'pVal' , ), 12001, (12001, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'OptimumAR' , 'pVal' , ), 12002, (12002, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'CreateNewOptimumModel' , 'name' , 'bOverWrite' , ), 12003, (12003, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'ApplyToCurrentModel' , ), 12004, (12004, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DOEMethodType' , 'pVal' , ), 12005, (12005, (), [ (16387, 10, None, "IID('{22E7B466-BB8D-47A0-A967-442E38BCA533}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MetaModelingMethodType' , 'pVal' , ), 12006, (12006, (), [ (16387, 10, None, "IID('{CDD675EF-2B10-454D-874A-79C9EA607FD7}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'PolynomialFunctionType' , 'pVal' , ), 12007, (12007, (), [ (16387, 10, None, "IID('{4FCC8FE8-CFFA-4794-BC1F-0C095D91C142}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'InitialSampleRuns' , 'pVal' , ), 12008, (12008, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'SAORuns' , 'pVal' , ), 12009, (12009, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'SAORunsDuplication' , 'pVal' , ), 12010, (12010, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'TotalEvaluations' , 'pVal' , ), 12011, (12011, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'OptimalDesignReulst' , 'pVal' , ), 12012, (12012, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IADSummarySheetRobustOptimization_vtables_dispatch_ = 1
IADSummarySheetRobustOptimization_vtables_ = [
	(( 'SampledStandardDeviation' , 'pVal' , ), 12051, (12051, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'RelaxedRobustIndex' , 'pVal' , ), 12052, (12052, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Validation' , 'pVal' , ), 12053, (12053, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IADSummarySheetSAOReliability_vtables_dispatch_ = 1
IADSummarySheetSAOReliability_vtables_ = [
	(( 'ValueAtMPP' , 'pVal' , ), 12001, (12001, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ReliabilityIndex' , 'pVal' , ), 12002, (12002, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'ProbabilityFailure' , 'pVal' , ), 12003, (12003, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'MPP_DV' , 'pVal' , ), 12004, (12004, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'MPP_BETA_MEAN' , 'pVal' , ), 12005, (12005, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'MPP_BETA_STDV' , 'pVal' , ), 12006, (12006, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'MPP_PROB_MEAN' , 'pVal' , ), 12007, (12007, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'MPP_PROB_STDV' , 'pVal' , ), 12008, (12008, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Param1' , 'pVal' , ), 12009, (12009, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Param2' , 'pVal' , ), 12010, (12010, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Param3' , 'pVal' , ), 12011, (12011, (), [ (24581, 10, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'InitialDOERuns' , 'pVal' , ), 12012, (12012, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'SAORuns' , 'pVal' , ), 12013, (12013, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'DRMRuns' , 'pVal' , ), 12014, (12014, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
]

IAutoDesignToolkit_vtables_dispatch_ = 1
IAutoDesignToolkit_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 12001, (12001, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DesignStudy' , 'ppVal' , ), 12002, (12002, (), [ (16393, 10, None, "IID('{6BCFA125-3F0C-42DA-AA88-8949B4625E32}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Optimization' , 'ppVal' , ), 12003, (12003, (), [ (16393, 10, None, "IID('{21F86233-F1EC-444F-BFAD-5480C4DBA5B1}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'RobustOptimization' , 'ppVal' , ), 12004, (12004, (), [ (16393, 10, None, "IID('{94B1BEFB-5C73-4A2A-92F2-997AF6CBAD62}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'SAOReliability' , 'ppVal' , ), 12005, (12005, (), [ (16393, 10, None, "IID('{A481E1C1-5497-468B-B072-CDB83437D5D3}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'MonteCarloReliability' , 'ppVal' , ), 12006, (12006, (), [ (16393, 10, None, "IID('{EFD6644C-E331-4E80-B99A-DBFD663B4F9C}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SimulationHistory' , 'ppVal' , ), 12007, (12007, (), [ (16393, 10, None, "IID('{A17668CB-A526-42D3-B8CC-21A35B441EAB}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'DesignParameterCollection' , 'ppVal' , ), 12008, (12008, (), [ (16393, 10, None, "IID('{39B651B4-D8F5-4B36-BA9B-5A5EB8F32D1B}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'AnalysisResponseCollection' , 'ppVal' , ), 12009, (12009, (), [ (16393, 10, None, "IID('{A0BF51C0-1CAE-4EF2-AD18-A604B83B3990}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CreateDesignParamter' , 'name' , 'type' , 'ppVal' , ), 12010, (12010, (), [ 
			 (8, 1, None, None) , (3, 1, None, "IID('{23EBCA44-1AD7-42AB-9E1D-F6BC1640ECA7}')") , (16393, 10, None, "IID('{1B1A9E20-C349-4415-AC09-E9CD38F531A1}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CreateAnalysisResponse' , 'name' , 'type' , 'ppVal' , ), 12011, (12011, (), [ 
			 (8, 1, None, None) , (3, 1, None, "IID('{2D2927C1-DFED-4562-BA6F-A310F6C417CF}')") , (16393, 10, None, "IID('{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{4041B853-0350-4DC4-A516-53EB9B0EF3E6}' : IADDesignVariableValueCollection,
	'{3EDECE37-7EBE-4189-8F11-78C4FFC54E0C}' : IADDesignVariableValue,
	'{4AE4ADC1-5D80-48D8-9DED-60AFF06B076F}' : IADDesignVariableValueOptimizationCollection,
	'{FAD5D54F-8696-4C06-A2AE-6958AE3C15E3}' : IADDesignVariableValueOptimization,
	'{FBDB8850-EF61-47B2-A7C8-EE7A36DEBAE1}' : IADDesignVariableValueRobustOptimizationCollection,
	'{44C71273-E70C-4AC7-B285-7741F8DF8F49}' : IADDesignVariableValueRobustOptimization,
	'{26B20F68-D1FA-4DD6-B690-2C4AA0BC6B6F}' : IADDesignVariableValueReliabilityCollection,
	'{BA8157EE-5975-42E0-833D-A5ADE8CD107B}' : IADDesignVariableValueReliability,
	'{0D17420F-646F-40BC-BA44-3ED8D71659DB}' : IADPerformanceIndexValueCollection,
	'{24A6DAE3-98C0-4137-8870-63C4A04F253A}' : IADPerformanceIndexValue,
	'{E1417D0E-3016-43ED-BB4C-525D39CEDD02}' : IADPerformanceIndexValueOptimizationCollection,
	'{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}' : IADPerformanceIndexValueOptimization,
	'{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}' : IADAnalysisResponse,
	'{ABE15F3A-BE3E-4A4A-9A9B-50EFFBB1089A}' : IADPerformanceIndexValueRobustOptimizationCollection,
	'{E6741EBF-DDF9-4A34-8AFA-DF0796377699}' : IADPerformanceIndexValueRobustOptimization,
	'{921490EB-AF1C-4DC8-9901-2394EA388ED1}' : IADPerformanceIndexValueReliabilityCollection,
	'{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}' : IADPerformanceIndexValueReliability,
	'{848C36F6-B86F-404E-A809-D8687EC91DEB}' : IADSimulationHistoryValueCollection,
	'{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}' : IADSimulationHistoryValue,
	'{1B1A9E20-C349-4415-AC09-E9CD38F531A1}' : IADDesignParameter,
	'{274D959F-B501-4C61-804B-A5458E8B73C3}' : IADDesignParameterDirect,
	'{F171C34B-E486-48C8-8030-769C8ABD2D55}' : IADDesignParameterTranslational,
	'{661B8B3F-0219-4D76-B7EE-90B3C54F6FF9}' : IADDesignParameterCylindrical,
	'{0AE6489F-7BB8-4D8A-8121-FDDBB4363359}' : IADDesignParameterSpherical,
	'{B34F3E57-7FD8-4176-AA85-F0B882CAD4B3}' : IADDesignParameterAngular,
	'{1F6675E9-0D4F-48E3-8957-D50DD217490D}' : IADAnalysisResponseBasic,
	'{8D621F9F-850A-464E-A0BC-9326FA9131AA}' : IADAnalysisResponseFEResult,
	'{BA363739-67DF-4E8B-80B2-35DA843EC406}' : IADAnalysisResponseScope,
	'{FD187EC7-42C4-4101-B682-B8B0A40FDDCD}' : IADAnalysisResponseProcessNet,
	'{EA349BD0-8E34-435E-BDC8-22434008169E}' : IADDesignVariable,
	'{5BB9E831-64AE-4AD1-88DB-FE8D333C7934}' : IADDesignVariableOptimization,
	'{21581656-E8B6-4C52-A435-6C6F7BC30720}' : IADDesignVariableRobustOptimization,
	'{F661EC5C-4647-4033-92BA-46E38C97192F}' : IADDesignVariableReliability,
	'{B29F78DD-B76C-407A-921F-E2305173B26D}' : IADPerformanceIndex,
	'{BBEBBABF-49D9-4B0B-A64F-007BD3B048EC}' : IADPerformanceIndexOptimization,
	'{4C5071E8-AFE7-4056-B4B2-DD3CFD7A534B}' : IADPerformanceIndexRobustOptimization,
	'{7CFDA97B-0D26-4330-A9A7-33E67162C207}' : IADPerformanceIndexReliability,
	'{F7310378-6376-4E72-8590-21B13F775AB4}' : IADMetaModel,
	'{97D04758-E009-46C2-BE5F-AD4A1CB49AB5}' : IADConvergenceTolerance,
	'{3C2D3CAD-1681-493B-A387-87E60A34606F}' : IADConvergenceToleranceOptimization,
	'{0838C8AB-285F-4456-8E62-2C7BC633DB4C}' : IADSimulationControl,
	'{FA5F5341-8EAE-4F15-92A0-4FA3B7425525}' : IADOptimizationControl,
	'{EA42004C-FAA2-4507-B161-FCC1E8CFD5B8}' : IADRobustOptimizationControl,
	'{9CF67D49-AFD5-46EA-B69E-50E384C63F41}' : IADAnalysisControlSAOReliability,
	'{D8BE75E5-32E7-42DF-A930-8A591F57583B}' : IADAnalysisControlMonteCarloReliability,
	'{E6D34A7F-E67B-43F6-AD41-4E3526234647}' : IADEffectAnalysis,
	'{23B3FD64-1889-4D1E-9CF2-5A39543F8806}' : IADScreeningVariable,
	'{23CD2F5A-F2CB-499B-907E-F52B2BEDCC86}' : IADCorrelationAnalysis,
	'{8B6F84EB-837F-4794-A9DB-D0C118F54305}' : IADResultSheetOptimization,
	'{A0AE4D34-C41F-4AF7-83F6-310D52FADC4E}' : IADResultSheetRobustOptimization,
	'{090D60A3-B9C2-4E96-8B46-9224257A6C8B}' : IADResultSheetSAOReliability,
	'{AE3EFE31-E75A-43FB-9923-BCB2F2B4CB3B}' : IADResultSheetMonteCarloReliability,
	'{1CFAE095-09EA-43A3-ABE0-9412CC096017}' : IADSummarySheetOptimization,
	'{0EAE4DF9-530B-4C01-8E01-05B444BA70FB}' : IADSummarySheetRobustOptimization,
	'{34968513-D22A-4A7C-876F-D97623DC5BB8}' : IADSummarySheetSAOReliability,
	'{AB84ECBA-52ED-470B-BD07-9E4F851BFDC0}' : IADSummarySheetMonteCarloReliability,
	'{39B651B4-D8F5-4B36-BA9B-5A5EB8F32D1B}' : IADDesignParameterCollection,
	'{A0BF51C0-1CAE-4EF2-AD18-A604B83B3990}' : IADAnalysisResponseCollection,
	'{6BCFA125-3F0C-42DA-AA88-8949B4625E32}' : IADDesignStudy,
	'{21F86233-F1EC-444F-BFAD-5480C4DBA5B1}' : IADDesignOptimization,
	'{94B1BEFB-5C73-4A2A-92F2-997AF6CBAD62}' : IADDesignRobustOptimization,
	'{A481E1C1-5497-468B-B072-CDB83437D5D3}' : IADDesignSAOReliability,
	'{EFD6644C-E331-4E80-B99A-DBFD663B4F9C}' : IADDesignMonteCarloReliability,
	'{A17668CB-A526-42D3-B8CC-21A35B441EAB}' : IADDesignSimulationHistory,
	'{4CD4C1F4-2733-4B7D-88AC-5CA98D412E5F}' : IAutoDesignToolkit,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{4041B853-0350-4DC4-A516-53EB9B0EF3E6}' : 'IADDesignVariableValueCollection',
	'{3EDECE37-7EBE-4189-8F11-78C4FFC54E0C}' : 'IADDesignVariableValue',
	'{4AE4ADC1-5D80-48D8-9DED-60AFF06B076F}' : 'IADDesignVariableValueOptimizationCollection',
	'{FAD5D54F-8696-4C06-A2AE-6958AE3C15E3}' : 'IADDesignVariableValueOptimization',
	'{FBDB8850-EF61-47B2-A7C8-EE7A36DEBAE1}' : 'IADDesignVariableValueRobustOptimizationCollection',
	'{44C71273-E70C-4AC7-B285-7741F8DF8F49}' : 'IADDesignVariableValueRobustOptimization',
	'{26B20F68-D1FA-4DD6-B690-2C4AA0BC6B6F}' : 'IADDesignVariableValueReliabilityCollection',
	'{BA8157EE-5975-42E0-833D-A5ADE8CD107B}' : 'IADDesignVariableValueReliability',
	'{0D17420F-646F-40BC-BA44-3ED8D71659DB}' : 'IADPerformanceIndexValueCollection',
	'{24A6DAE3-98C0-4137-8870-63C4A04F253A}' : 'IADPerformanceIndexValue',
	'{E1417D0E-3016-43ED-BB4C-525D39CEDD02}' : 'IADPerformanceIndexValueOptimizationCollection',
	'{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}' : 'IADPerformanceIndexValueOptimization',
	'{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}' : 'IADAnalysisResponse',
	'{ABE15F3A-BE3E-4A4A-9A9B-50EFFBB1089A}' : 'IADPerformanceIndexValueRobustOptimizationCollection',
	'{E6741EBF-DDF9-4A34-8AFA-DF0796377699}' : 'IADPerformanceIndexValueRobustOptimization',
	'{921490EB-AF1C-4DC8-9901-2394EA388ED1}' : 'IADPerformanceIndexValueReliabilityCollection',
	'{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}' : 'IADPerformanceIndexValueReliability',
	'{848C36F6-B86F-404E-A809-D8687EC91DEB}' : 'IADSimulationHistoryValueCollection',
	'{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}' : 'IADSimulationHistoryValue',
	'{1B1A9E20-C349-4415-AC09-E9CD38F531A1}' : 'IADDesignParameter',
	'{274D959F-B501-4C61-804B-A5458E8B73C3}' : 'IADDesignParameterDirect',
	'{F171C34B-E486-48C8-8030-769C8ABD2D55}' : 'IADDesignParameterTranslational',
	'{661B8B3F-0219-4D76-B7EE-90B3C54F6FF9}' : 'IADDesignParameterCylindrical',
	'{0AE6489F-7BB8-4D8A-8121-FDDBB4363359}' : 'IADDesignParameterSpherical',
	'{B34F3E57-7FD8-4176-AA85-F0B882CAD4B3}' : 'IADDesignParameterAngular',
	'{1F6675E9-0D4F-48E3-8957-D50DD217490D}' : 'IADAnalysisResponseBasic',
	'{8D621F9F-850A-464E-A0BC-9326FA9131AA}' : 'IADAnalysisResponseFEResult',
	'{BA363739-67DF-4E8B-80B2-35DA843EC406}' : 'IADAnalysisResponseScope',
	'{FD187EC7-42C4-4101-B682-B8B0A40FDDCD}' : 'IADAnalysisResponseProcessNet',
	'{EA349BD0-8E34-435E-BDC8-22434008169E}' : 'IADDesignVariable',
	'{5BB9E831-64AE-4AD1-88DB-FE8D333C7934}' : 'IADDesignVariableOptimization',
	'{21581656-E8B6-4C52-A435-6C6F7BC30720}' : 'IADDesignVariableRobustOptimization',
	'{F661EC5C-4647-4033-92BA-46E38C97192F}' : 'IADDesignVariableReliability',
	'{B29F78DD-B76C-407A-921F-E2305173B26D}' : 'IADPerformanceIndex',
	'{BBEBBABF-49D9-4B0B-A64F-007BD3B048EC}' : 'IADPerformanceIndexOptimization',
	'{4C5071E8-AFE7-4056-B4B2-DD3CFD7A534B}' : 'IADPerformanceIndexRobustOptimization',
	'{7CFDA97B-0D26-4330-A9A7-33E67162C207}' : 'IADPerformanceIndexReliability',
	'{F7310378-6376-4E72-8590-21B13F775AB4}' : 'IADMetaModel',
	'{97D04758-E009-46C2-BE5F-AD4A1CB49AB5}' : 'IADConvergenceTolerance',
	'{3C2D3CAD-1681-493B-A387-87E60A34606F}' : 'IADConvergenceToleranceOptimization',
	'{0838C8AB-285F-4456-8E62-2C7BC633DB4C}' : 'IADSimulationControl',
	'{FA5F5341-8EAE-4F15-92A0-4FA3B7425525}' : 'IADOptimizationControl',
	'{EA42004C-FAA2-4507-B161-FCC1E8CFD5B8}' : 'IADRobustOptimizationControl',
	'{9CF67D49-AFD5-46EA-B69E-50E384C63F41}' : 'IADAnalysisControlSAOReliability',
	'{D8BE75E5-32E7-42DF-A930-8A591F57583B}' : 'IADAnalysisControlMonteCarloReliability',
	'{E6D34A7F-E67B-43F6-AD41-4E3526234647}' : 'IADEffectAnalysis',
	'{23B3FD64-1889-4D1E-9CF2-5A39543F8806}' : 'IADScreeningVariable',
	'{23CD2F5A-F2CB-499B-907E-F52B2BEDCC86}' : 'IADCorrelationAnalysis',
	'{8B6F84EB-837F-4794-A9DB-D0C118F54305}' : 'IADResultSheetOptimization',
	'{A0AE4D34-C41F-4AF7-83F6-310D52FADC4E}' : 'IADResultSheetRobustOptimization',
	'{090D60A3-B9C2-4E96-8B46-9224257A6C8B}' : 'IADResultSheetSAOReliability',
	'{AE3EFE31-E75A-43FB-9923-BCB2F2B4CB3B}' : 'IADResultSheetMonteCarloReliability',
	'{1CFAE095-09EA-43A3-ABE0-9412CC096017}' : 'IADSummarySheetOptimization',
	'{0EAE4DF9-530B-4C01-8E01-05B444BA70FB}' : 'IADSummarySheetRobustOptimization',
	'{34968513-D22A-4A7C-876F-D97623DC5BB8}' : 'IADSummarySheetSAOReliability',
	'{AB84ECBA-52ED-470B-BD07-9E4F851BFDC0}' : 'IADSummarySheetMonteCarloReliability',
	'{39B651B4-D8F5-4B36-BA9B-5A5EB8F32D1B}' : 'IADDesignParameterCollection',
	'{A0BF51C0-1CAE-4EF2-AD18-A604B83B3990}' : 'IADAnalysisResponseCollection',
	'{6BCFA125-3F0C-42DA-AA88-8949B4625E32}' : 'IADDesignStudy',
	'{21F86233-F1EC-444F-BFAD-5480C4DBA5B1}' : 'IADDesignOptimization',
	'{94B1BEFB-5C73-4A2A-92F2-997AF6CBAD62}' : 'IADDesignRobustOptimization',
	'{A481E1C1-5497-468B-B072-CDB83437D5D3}' : 'IADDesignSAOReliability',
	'{EFD6644C-E331-4E80-B99A-DBFD663B4F9C}' : 'IADDesignMonteCarloReliability',
	'{A17668CB-A526-42D3-B8CC-21A35B441EAB}' : 'IADDesignSimulationHistory',
	'{4CD4C1F4-2733-4B7D-88AC-5CA98D412E5F}' : 'IAutoDesignToolkit',
}


NamesToIIDMap = {
	'IADDesignVariableValueCollection' : '{4041B853-0350-4DC4-A516-53EB9B0EF3E6}',
	'IADDesignVariableValue' : '{3EDECE37-7EBE-4189-8F11-78C4FFC54E0C}',
	'IADDesignVariableValueOptimizationCollection' : '{4AE4ADC1-5D80-48D8-9DED-60AFF06B076F}',
	'IADDesignVariableValueOptimization' : '{FAD5D54F-8696-4C06-A2AE-6958AE3C15E3}',
	'IADDesignVariableValueRobustOptimizationCollection' : '{FBDB8850-EF61-47B2-A7C8-EE7A36DEBAE1}',
	'IADDesignVariableValueRobustOptimization' : '{44C71273-E70C-4AC7-B285-7741F8DF8F49}',
	'IADDesignVariableValueReliabilityCollection' : '{26B20F68-D1FA-4DD6-B690-2C4AA0BC6B6F}',
	'IADDesignVariableValueReliability' : '{BA8157EE-5975-42E0-833D-A5ADE8CD107B}',
	'IADPerformanceIndexValueCollection' : '{0D17420F-646F-40BC-BA44-3ED8D71659DB}',
	'IADPerformanceIndexValue' : '{24A6DAE3-98C0-4137-8870-63C4A04F253A}',
	'IADPerformanceIndexValueOptimizationCollection' : '{E1417D0E-3016-43ED-BB4C-525D39CEDD02}',
	'IADPerformanceIndexValueOptimization' : '{A0DFAC0B-9F6F-48E6-B4B0-F882A8A7F8E7}',
	'IADAnalysisResponse' : '{E2B5DB56-5890-4B4E-8CB6-0EA6B1B25B91}',
	'IADPerformanceIndexValueRobustOptimizationCollection' : '{ABE15F3A-BE3E-4A4A-9A9B-50EFFBB1089A}',
	'IADPerformanceIndexValueRobustOptimization' : '{E6741EBF-DDF9-4A34-8AFA-DF0796377699}',
	'IADPerformanceIndexValueReliabilityCollection' : '{921490EB-AF1C-4DC8-9901-2394EA388ED1}',
	'IADPerformanceIndexValueReliability' : '{EBA951F9-B4EB-44E1-9A74-3CFC40AE054B}',
	'IADSimulationHistoryValueCollection' : '{848C36F6-B86F-404E-A809-D8687EC91DEB}',
	'IADSimulationHistoryValue' : '{7EAE7DD2-60C1-442E-814A-CF4BBA43E523}',
	'IADDesignParameter' : '{1B1A9E20-C349-4415-AC09-E9CD38F531A1}',
	'IADDesignParameterDirect' : '{274D959F-B501-4C61-804B-A5458E8B73C3}',
	'IADDesignParameterTranslational' : '{F171C34B-E486-48C8-8030-769C8ABD2D55}',
	'IADDesignParameterCylindrical' : '{661B8B3F-0219-4D76-B7EE-90B3C54F6FF9}',
	'IADDesignParameterSpherical' : '{0AE6489F-7BB8-4D8A-8121-FDDBB4363359}',
	'IADDesignParameterAngular' : '{B34F3E57-7FD8-4176-AA85-F0B882CAD4B3}',
	'IADAnalysisResponseBasic' : '{1F6675E9-0D4F-48E3-8957-D50DD217490D}',
	'IADAnalysisResponseFEResult' : '{8D621F9F-850A-464E-A0BC-9326FA9131AA}',
	'IADAnalysisResponseScope' : '{BA363739-67DF-4E8B-80B2-35DA843EC406}',
	'IADAnalysisResponseProcessNet' : '{FD187EC7-42C4-4101-B682-B8B0A40FDDCD}',
	'IADDesignVariable' : '{EA349BD0-8E34-435E-BDC8-22434008169E}',
	'IADDesignVariableOptimization' : '{5BB9E831-64AE-4AD1-88DB-FE8D333C7934}',
	'IADDesignVariableRobustOptimization' : '{21581656-E8B6-4C52-A435-6C6F7BC30720}',
	'IADDesignVariableReliability' : '{F661EC5C-4647-4033-92BA-46E38C97192F}',
	'IADPerformanceIndex' : '{B29F78DD-B76C-407A-921F-E2305173B26D}',
	'IADPerformanceIndexOptimization' : '{BBEBBABF-49D9-4B0B-A64F-007BD3B048EC}',
	'IADPerformanceIndexRobustOptimization' : '{4C5071E8-AFE7-4056-B4B2-DD3CFD7A534B}',
	'IADPerformanceIndexReliability' : '{7CFDA97B-0D26-4330-A9A7-33E67162C207}',
	'IADMetaModel' : '{F7310378-6376-4E72-8590-21B13F775AB4}',
	'IADConvergenceTolerance' : '{97D04758-E009-46C2-BE5F-AD4A1CB49AB5}',
	'IADConvergenceToleranceOptimization' : '{3C2D3CAD-1681-493B-A387-87E60A34606F}',
	'IADSimulationControl' : '{0838C8AB-285F-4456-8E62-2C7BC633DB4C}',
	'IADOptimizationControl' : '{FA5F5341-8EAE-4F15-92A0-4FA3B7425525}',
	'IADRobustOptimizationControl' : '{EA42004C-FAA2-4507-B161-FCC1E8CFD5B8}',
	'IADAnalysisControlSAOReliability' : '{9CF67D49-AFD5-46EA-B69E-50E384C63F41}',
	'IADAnalysisControlMonteCarloReliability' : '{D8BE75E5-32E7-42DF-A930-8A591F57583B}',
	'IADEffectAnalysis' : '{E6D34A7F-E67B-43F6-AD41-4E3526234647}',
	'IADScreeningVariable' : '{23B3FD64-1889-4D1E-9CF2-5A39543F8806}',
	'IADCorrelationAnalysis' : '{23CD2F5A-F2CB-499B-907E-F52B2BEDCC86}',
	'IADResultSheetOptimization' : '{8B6F84EB-837F-4794-A9DB-D0C118F54305}',
	'IADResultSheetRobustOptimization' : '{A0AE4D34-C41F-4AF7-83F6-310D52FADC4E}',
	'IADResultSheetSAOReliability' : '{090D60A3-B9C2-4E96-8B46-9224257A6C8B}',
	'IADResultSheetMonteCarloReliability' : '{AE3EFE31-E75A-43FB-9923-BCB2F2B4CB3B}',
	'IADSummarySheetOptimization' : '{1CFAE095-09EA-43A3-ABE0-9412CC096017}',
	'IADSummarySheetRobustOptimization' : '{0EAE4DF9-530B-4C01-8E01-05B444BA70FB}',
	'IADSummarySheetSAOReliability' : '{34968513-D22A-4A7C-876F-D97623DC5BB8}',
	'IADSummarySheetMonteCarloReliability' : '{AB84ECBA-52ED-470B-BD07-9E4F851BFDC0}',
	'IADDesignParameterCollection' : '{39B651B4-D8F5-4B36-BA9B-5A5EB8F32D1B}',
	'IADAnalysisResponseCollection' : '{A0BF51C0-1CAE-4EF2-AD18-A604B83B3990}',
	'IADDesignStudy' : '{6BCFA125-3F0C-42DA-AA88-8949B4625E32}',
	'IADDesignOptimization' : '{21F86233-F1EC-444F-BFAD-5480C4DBA5B1}',
	'IADDesignRobustOptimization' : '{94B1BEFB-5C73-4A2A-92F2-997AF6CBAD62}',
	'IADDesignSAOReliability' : '{A481E1C1-5497-468B-B072-CDB83437D5D3}',
	'IADDesignMonteCarloReliability' : '{EFD6644C-E331-4E80-B99A-DBFD663B4F9C}',
	'IADDesignSimulationHistory' : '{A17668CB-A526-42D3-B8CC-21A35B441EAB}',
	'IAutoDesignToolkit' : '{4CD4C1F4-2733-4B7D-88AC-5CA98D412E5F}',
}


