# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMChain.tlb'
# On Mon Jan 16 02:20:01 2023
'RecurDyn V10R1 RecurDynCOMCHAIN Type Library'
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

CLSID = IID('{5C07BAAC-4232-4A0D-9032-AB095DF61F1C}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

class ChainAssemblyBushingType(IntEnum):
	'''
	ChainAssemblyBushingType enumeration.
	'''
	ChainAssemblyBushingType_Double=1         
	'''Constant value is 1.'''
	ChainAssemblyBushingType_Single=0         
	'''Constant value is 0.'''
class ChainContactSearchType(IntEnum):
	'''
	ChainContactSearchType enumeration.
	'''
	ChainContactSearchType_FullSearch=0         
	'''Constant value is 0.'''
	ChainContactSearchType_PartialSearch=1         
	'''Constant value is 1.'''
class ChainFrictionType(IntEnum):
	'''
	ChainFrictionType enumeration.
	'''
	ChainFrictionType_DynamicFrictionCoefficient=0         
	'''Constant value is 0.'''
	ChainFrictionType_FrictionCoefficientSpline=2         
	'''Constant value is 2.'''
	ChainFrictionType_FrictionForceSpline=1         
	'''Constant value is 1.'''
class ChainGuardInactiveType(IntEnum):
	'''
	ChainGuardInactiveType enumeration.
	'''
	ChainGuardInactiveType_Left_Inactive=1         
	'''Constant value is 1.'''
	ChainGuardInactiveType_None   =0         
	'''Constant value is 0.'''
	ChainGuardInactiveType_Right_Inactive=2         
	'''Constant value is 2.'''
class ChainGuidePointsType(IntEnum):
	'''
	ChainGuidePointsType enumeration.
	'''
	ChainGuidePointsType_CenterPointsAndArcAngle=2         
	'''Constant value is 2.'''
	ChainGuidePointsType_CenterPointsAndRadius=1         
	'''Constant value is 1.'''
	ChainGuidePointsType_PassingPoints=0         
	'''Constant value is 0.'''
class ChainInOutType(IntEnum):
	'''
	ChainInOutType enumeration.
	'''
	ChainInOutType_In             =0         
	'''Constant value is 0.'''
	ChainInOutType_None           =2         
	'''Constant value is 2.'''
	ChainInOutType_Out            =1         
	'''Constant value is 1.'''
class ChainLinkPlateShapeType(IntEnum):
	'''
	ChainLinkPlateShapeType enumeration.
	'''
	ChainLinkPlateShapeType_Box   =1         
	'''Constant value is 1.'''
	ChainLinkPlateShapeType_Circle=0         
	'''Constant value is 0.'''
class ChainLinkType(IntEnum):
	'''
	ChainLinkType enumeration.
	'''
	ChainLinkType_GeneralRollerLink=0         
	'''Constant value is 0.'''
	ChainLinkType_ISO606_05B      =1         
	'''Constant value is 1.'''
	ChainLinkType_ISO606_06B      =2         
	'''Constant value is 2.'''
	ChainLinkType_ISO606_081      =5         
	'''Constant value is 5.'''
	ChainLinkType_ISO606_083      =6         
	'''Constant value is 6.'''
	ChainLinkType_ISO606_084      =7         
	'''Constant value is 7.'''
	ChainLinkType_ISO606_085      =8         
	'''Constant value is 8.'''
	ChainLinkType_ISO606_08A      =3         
	'''Constant value is 3.'''
	ChainLinkType_ISO606_08B      =4         
	'''Constant value is 4.'''
	ChainLinkType_ISO606_10A      =9         
	'''Constant value is 9.'''
	ChainLinkType_ISO606_10B      =10        
	'''Constant value is 10.'''
	ChainLinkType_ISO606_12A      =11        
	'''Constant value is 11.'''
	ChainLinkType_ISO606_12B      =12        
	'''Constant value is 12.'''
	ChainLinkType_ISO606_16A      =13        
	'''Constant value is 13.'''
	ChainLinkType_ISO606_16B      =14        
	'''Constant value is 14.'''
	ChainLinkType_ISO606_20A      =15        
	'''Constant value is 15.'''
	ChainLinkType_ISO606_20B      =16        
	'''Constant value is 16.'''
	ChainLinkType_ISO606_24A      =17        
	'''Constant value is 17.'''
	ChainLinkType_ISO606_24B      =18        
	'''Constant value is 18.'''
	ChainLinkType_ISO606_28A      =19        
	'''Constant value is 19.'''
	ChainLinkType_ISO606_28B      =20        
	'''Constant value is 20.'''
	ChainLinkType_ISO606_32A      =21        
	'''Constant value is 21.'''
	ChainLinkType_ISO606_32B      =22        
	'''Constant value is 22.'''
	ChainLinkType_ISO606_36A      =23        
	'''Constant value is 23.'''
	ChainLinkType_ISO606_40A      =24        
	'''Constant value is 24.'''
	ChainLinkType_ISO606_40B      =25        
	'''Constant value is 25.'''
	ChainLinkType_ISO606_48A      =26        
	'''Constant value is 26.'''
	ChainLinkType_ISO606_48B      =27        
	'''Constant value is 27.'''
	ChainLinkType_ISO606_56B      =28        
	'''Constant value is 28.'''
	ChainLinkType_ISO606_64B      =29        
	'''Constant value is 29.'''
	ChainLinkType_ISO606_72B      =30        
	'''Constant value is 30.'''
class ChainNormalDirectionType(IntEnum):
	'''
	ChainNormalDirectionType enumeration.
	'''
	ChainNormalDirectionType_Down =1         
	'''Constant value is 1.'''
	ChainNormalDirectionType_Up   =0         
	'''Constant value is 0.'''
class ChainSprocketType(IntEnum):
	'''
	ChainSprocketType enumeration.
	'''
	ChainSprocketType_General     =0         
	'''Constant value is 0.'''
	ChainSprocketType_ISO606Library=1         
	'''Constant value is 1.'''
	ChainSprocketType_Parameters  =2         
	'''Constant value is 2.'''

from win32com.client import DispatchBaseClass
class IChainAssembly(DispatchBaseClass):
	'''Chain Assembly'''
	CLSID = IID('{0963256F-0F65-4E93-8FFA-B58651838BC6}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def AddAllOutputLink(self):
		'''
		Add all the link body to output list
		'''
		return self._oleobj_.InvokeTypes(10513, LCID, 1, (24, 0), (),)


	def AddOutputLink(self, strFileName):
		'''
		Add a link body to output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(10511, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def AddPassingBody(self, pVal):
		'''
		Add a Passing Body
		
		:param pVal: IChainBody
		'''
		return self._oleobj_.InvokeTypes(10504, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def DeletePassingBody(self, pVal):
		'''
		Delete a Passing Body
		
		:param pVal: IChainBody
		'''
		return self._oleobj_.InvokeTypes(10505, LCID, 1, (24, 0), ((9, 1),),pVal
			)


	def GetOutputLinkList(self):
		'''
		Chain assembly output list
		
		:rtype: list[str]
		'''
		return self._ApplyTypes_(10510, 1, (8200, 0), (), 'GetOutputLinkList', None,)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def RemoveAllOutputLink(self):
		'''
		Remove all the link body from output list
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def RemoveOutputLink(self, strFileName):
		'''
		Remove a link body from output list
		
		:param strFileName: str
		'''
		return self._oleobj_.InvokeTypes(10512, LCID, 1, (24, 0), ((8, 1),),strFileName
			)


	def UpdateLinkInitialVelocityXAxis(self):
		'''
		Update Link Initial Velocity X-Axis Value
		'''
		return self._oleobj_.InvokeTypes(10509, LCID, 1, (24, 0), (),)


	def _get_BushingForceParameter(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "BushingForceParameter", '{15D9554A-5BA8-4892-8AC3-1A026ED0FBCA}'))
	def _get_ChainBodyLinkCollection(self):
		return self._ApplyTypes_(*(10516, 2, (9, 0), (), "ChainBodyLinkCollection", '{7DCEE901-515D-4780-AB01-89ECA089D8BE}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(10515, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_LinkInitialVelocityXAxis(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "LinkInitialVelocityXAxis", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LinkNumbers(self):
		return self._ApplyTypes_(*(10506, 2, (19, 0), (), "LinkNumbers", None))
	def _get_LinkPlateShapeType(self):
		return self._ApplyTypes_(*(10502, 2, (3, 0), (), "LinkPlateShapeType", '{70767D30-A128-49F0-BFC5-1CEE78841C28}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PassingBodyCollection(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'))
	def _get_UseLinkInitialVelocityXAxis(self):
		return self._ApplyTypes_(*(10507, 2, (11, 0), (), "UseLinkInitialVelocityXAxis", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((10515, LCID, 4, 0) + (value,) + ()))
	def _set_LinkPlateShapeType(self, value):
		if "LinkPlateShapeType" in self.__dict__: self.__dict__["LinkPlateShapeType"] = value; return
		self._oleobj_.Invoke(*((10502, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkInitialVelocityXAxis(self, value):
		if "UseLinkInitialVelocityXAxis" in self.__dict__: self.__dict__["UseLinkInitialVelocityXAxis"] = value; return
		self._oleobj_.Invoke(*((10507, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BushingForceParameter = property(_get_BushingForceParameter, None)
	'''
	Bushing Force Parameter

	:type: recurdyn.Chain.IChainAssemblyBushingForceParameter
	'''
	ChainBodyLinkCollection = property(_get_ChainBodyLinkCollection, None)
	'''
	Get the Chain Body Link Collection

	:type: recurdyn.Chain.IChainBodyLinkCollection
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
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	LinkInitialVelocityXAxis = property(_get_LinkInitialVelocityXAxis, None)
	'''
	Link Initial Velocity X-Axis

	:type: recurdyn.ProcessNet.IDouble
	'''
	LinkNumbers = property(_get_LinkNumbers, None)
	'''
	Link Numbers

	:type: int
	'''
	LinkPlateShapeType = property(_get_LinkPlateShapeType, _set_LinkPlateShapeType)
	'''
	Link Plate Shape Type

	:type: recurdyn.Chain.ChainLinkPlateShapeType
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
	PassingBodyCollection = property(_get_PassingBodyCollection, None)
	'''
	Passing Body Collection

	:type: recurdyn.ProcessNet.IBodyCollection
	'''
	UseLinkInitialVelocityXAxis = property(_get_UseLinkInitialVelocityXAxis, _set_UseLinkInitialVelocityXAxis)
	'''
	Use Link Initial Velocity X-Axis

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LinkPlateShapeType": _set_LinkPlateShapeType,
		"_set_Name": _set_Name,
		"_set_UseLinkInitialVelocityXAxis": _set_UseLinkInitialVelocityXAxis,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BushingForceParameter": (10501, 2, (9, 0), (), "BushingForceParameter", '{15D9554A-5BA8-4892-8AC3-1A026ED0FBCA}'),
		"ChainBodyLinkCollection": (10516, 2, (9, 0), (), "ChainBodyLinkCollection", '{7DCEE901-515D-4780-AB01-89ECA089D8BE}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ForceDisplay": (10515, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"LinkInitialVelocityXAxis": (10508, 2, (9, 0), (), "LinkInitialVelocityXAxis", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LinkNumbers": (10506, 2, (19, 0), (), "LinkNumbers", None),
		"LinkPlateShapeType": (10502, 2, (3, 0), (), "LinkPlateShapeType", '{70767D30-A128-49F0-BFC5-1CEE78841C28}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PassingBodyCollection": (10503, 2, (9, 0), (), "PassingBodyCollection", '{E26794CD-5D37-4617-BB5A-1AD85F3ED410}'),
		"UseLinkInitialVelocityXAxis": (10507, 2, (11, 0), (), "UseLinkInitialVelocityXAxis", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((10515, LCID, 4, 0),()),
		"LinkPlateShapeType": ((10502, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseLinkInitialVelocityXAxis": ((10507, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainAssemblyBushingForceParameter(DispatchBaseClass):
	'''Chain Assembly'''
	CLSID = IID('{15D9554A-5BA8-4892-8AC3-1A026ED0FBCA}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Export(self, strName, val):
		'''
		Export bushing force parameter
		
		:param strName: str
		:param val: bool
		'''
		return self._oleobj_.InvokeTypes(10546, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import bushing force parameter
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(10547, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_Friction(self):
		return self._ApplyTypes_(*(10531, 2, (9, 0), (), "Friction", '{6F6A35D3-97FF-494A-8E1A-DF4E8101EBDB}'))
	def _get_RotationDampingCoefficientX(self):
		return self._ApplyTypes_(*(10520, 2, (9, 0), (), "RotationDampingCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingCoefficientY(self):
		return self._ApplyTypes_(*(10521, 2, (9, 0), (), "RotationDampingCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingCoefficientZ(self):
		return self._ApplyTypes_(*(10522, 2, (9, 0), (), "RotationDampingCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponentX(self):
		return self._ApplyTypes_(*(10543, 2, (9, 0), (), "RotationDampingExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponentY(self):
		return self._ApplyTypes_(*(10544, 2, (9, 0), (), "RotationDampingExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingExponentZ(self):
		return self._ApplyTypes_(*(10545, 2, (9, 0), (), "RotationDampingExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationDampingSplineX(self):
		return self._ApplyTypes_(*(10524, 2, (9, 0), (), "RotationDampingSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationDampingSplineY(self):
		return self._ApplyTypes_(*(10525, 2, (9, 0), (), "RotationDampingSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationDampingSplineZ(self):
		return self._ApplyTypes_(*(10526, 2, (9, 0), (), "RotationDampingSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationPreloadX(self):
		return self._ApplyTypes_(*(10527, 2, (9, 0), (), "RotationPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationPreloadY(self):
		return self._ApplyTypes_(*(10528, 2, (9, 0), (), "RotationPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationPreloadZ(self):
		return self._ApplyTypes_(*(10529, 2, (9, 0), (), "RotationPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessCoefficientX(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "RotationStiffnessCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessCoefficientY(self):
		return self._ApplyTypes_(*(10514, 2, (9, 0), (), "RotationStiffnessCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessCoefficientZ(self):
		return self._ApplyTypes_(*(10515, 2, (9, 0), (), "RotationStiffnessCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponentX(self):
		return self._ApplyTypes_(*(10539, 2, (9, 0), (), "RotationStiffnessExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponentY(self):
		return self._ApplyTypes_(*(10540, 2, (9, 0), (), "RotationStiffnessExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessExponentZ(self):
		return self._ApplyTypes_(*(10541, 2, (9, 0), (), "RotationStiffnessExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RotationStiffnessSplineX(self):
		return self._ApplyTypes_(*(10517, 2, (9, 0), (), "RotationStiffnessSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationStiffnessSplineY(self):
		return self._ApplyTypes_(*(10518, 2, (9, 0), (), "RotationStiffnessSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_RotationStiffnessSplineZ(self):
		return self._ApplyTypes_(*(10519, 2, (9, 0), (), "RotationStiffnessSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationClearance(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "TranslationClearance", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingCoefficientAxial(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "TranslationDampingCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingCoefficientRadial(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "TranslationDampingCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingExponentAxial(self):
		return self._ApplyTypes_(*(10537, 2, (9, 0), (), "TranslationDampingExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingExponentRadial(self):
		return self._ApplyTypes_(*(10536, 2, (9, 0), (), "TranslationDampingExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationDampingSplineAxial(self):
		return self._ApplyTypes_(*(10509, 2, (9, 0), (), "TranslationDampingSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationDampingSplineRadial(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "TranslationDampingSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationPreloadAxial(self):
		return self._ApplyTypes_(*(10511, 2, (9, 0), (), "TranslationPreloadAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationPreloadRadial(self):
		return self._ApplyTypes_(*(10510, 2, (9, 0), (), "TranslationPreloadRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessCoefficientAxial(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "TranslationStiffnessCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessCoefficientRadial(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "TranslationStiffnessCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessExponentAxial(self):
		return self._ApplyTypes_(*(10534, 2, (9, 0), (), "TranslationStiffnessExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessExponentRadial(self):
		return self._ApplyTypes_(*(10533, 2, (9, 0), (), "TranslationStiffnessExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_TranslationStiffnessSplineAxial(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "TranslationStiffnessSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_TranslationStiffnessSplineRadial(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "TranslationStiffnessSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseFriction(self):
		return self._ApplyTypes_(*(10530, 2, (11, 0), (), "UseFriction", None))
	def _get_UseRotationDampingExponent(self):
		return self._ApplyTypes_(*(10542, 2, (11, 0), (), "UseRotationDampingExponent", None))
	def _get_UseRotationDampingSpline(self):
		return self._ApplyTypes_(*(10523, 2, (11, 0), (), "UseRotationDampingSpline", None))
	def _get_UseRotationStiffnessExponent(self):
		return self._ApplyTypes_(*(10538, 2, (11, 0), (), "UseRotationStiffnessExponent", None))
	def _get_UseRotationStiffnessSpline(self):
		return self._ApplyTypes_(*(10516, 2, (11, 0), (), "UseRotationStiffnessSpline", None))
	def _get_UseTranslationDampingExponent(self):
		return self._ApplyTypes_(*(10535, 2, (11, 0), (), "UseTranslationDampingExponent", None))
	def _get_UseTranslationDampingSpline(self):
		return self._ApplyTypes_(*(10507, 2, (11, 0), (), "UseTranslationDampingSpline", None))
	def _get_UseTranslationStiffnessExponent(self):
		return self._ApplyTypes_(*(10532, 2, (11, 0), (), "UseTranslationStiffnessExponent", None))
	def _get_UseTranslationStiffnessSpline(self):
		return self._ApplyTypes_(*(10502, 2, (11, 0), (), "UseTranslationStiffnessSpline", None))

	def _set_RotationDampingSplineX(self, value):
		if "RotationDampingSplineX" in self.__dict__: self.__dict__["RotationDampingSplineX"] = value; return
		self._oleobj_.Invoke(*((10524, LCID, 4, 0) + (value,) + ()))
	def _set_RotationDampingSplineY(self, value):
		if "RotationDampingSplineY" in self.__dict__: self.__dict__["RotationDampingSplineY"] = value; return
		self._oleobj_.Invoke(*((10525, LCID, 4, 0) + (value,) + ()))
	def _set_RotationDampingSplineZ(self, value):
		if "RotationDampingSplineZ" in self.__dict__: self.__dict__["RotationDampingSplineZ"] = value; return
		self._oleobj_.Invoke(*((10526, LCID, 4, 0) + (value,) + ()))
	def _set_RotationStiffnessSplineX(self, value):
		if "RotationStiffnessSplineX" in self.__dict__: self.__dict__["RotationStiffnessSplineX"] = value; return
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_RotationStiffnessSplineY(self, value):
		if "RotationStiffnessSplineY" in self.__dict__: self.__dict__["RotationStiffnessSplineY"] = value; return
		self._oleobj_.Invoke(*((10518, LCID, 4, 0) + (value,) + ()))
	def _set_RotationStiffnessSplineZ(self, value):
		if "RotationStiffnessSplineZ" in self.__dict__: self.__dict__["RotationStiffnessSplineZ"] = value; return
		self._oleobj_.Invoke(*((10519, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationDampingSplineAxial(self, value):
		if "TranslationDampingSplineAxial" in self.__dict__: self.__dict__["TranslationDampingSplineAxial"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationDampingSplineRadial(self, value):
		if "TranslationDampingSplineRadial" in self.__dict__: self.__dict__["TranslationDampingSplineRadial"] = value; return
		self._oleobj_.Invoke(*((10508, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationStiffnessSplineAxial(self, value):
		if "TranslationStiffnessSplineAxial" in self.__dict__: self.__dict__["TranslationStiffnessSplineAxial"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))
	def _set_TranslationStiffnessSplineRadial(self, value):
		if "TranslationStiffnessSplineRadial" in self.__dict__: self.__dict__["TranslationStiffnessSplineRadial"] = value; return
		self._oleobj_.Invoke(*((10503, LCID, 4, 0) + (value,) + ()))
	def _set_UseFriction(self, value):
		if "UseFriction" in self.__dict__: self.__dict__["UseFriction"] = value; return
		self._oleobj_.Invoke(*((10530, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationDampingExponent(self, value):
		if "UseRotationDampingExponent" in self.__dict__: self.__dict__["UseRotationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((10542, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationDampingSpline(self, value):
		if "UseRotationDampingSpline" in self.__dict__: self.__dict__["UseRotationDampingSpline"] = value; return
		self._oleobj_.Invoke(*((10523, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStiffnessExponent(self, value):
		if "UseRotationStiffnessExponent" in self.__dict__: self.__dict__["UseRotationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((10538, LCID, 4, 0) + (value,) + ()))
	def _set_UseRotationStiffnessSpline(self, value):
		if "UseRotationStiffnessSpline" in self.__dict__: self.__dict__["UseRotationStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10516, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationDampingExponent(self, value):
		if "UseTranslationDampingExponent" in self.__dict__: self.__dict__["UseTranslationDampingExponent"] = value; return
		self._oleobj_.Invoke(*((10535, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationDampingSpline(self, value):
		if "UseTranslationDampingSpline" in self.__dict__: self.__dict__["UseTranslationDampingSpline"] = value; return
		self._oleobj_.Invoke(*((10507, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationStiffnessExponent(self, value):
		if "UseTranslationStiffnessExponent" in self.__dict__: self.__dict__["UseTranslationStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((10532, LCID, 4, 0) + (value,) + ()))
	def _set_UseTranslationStiffnessSpline(self, value):
		if "UseTranslationStiffnessSpline" in self.__dict__: self.__dict__["UseTranslationStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10502, LCID, 4, 0) + (value,) + ()))

	Friction = property(_get_Friction, None)
	'''
	Friction Parameter

	:type: recurdyn.Chain.IChainAssemblyContactFriction
	'''
	RotationDampingCoefficientX = property(_get_RotationDampingCoefficientX, None)
	'''
	Rotation damping coefficient X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingCoefficientY = property(_get_RotationDampingCoefficientY, None)
	'''
	Rotation damping coefficient Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingCoefficientZ = property(_get_RotationDampingCoefficientZ, None)
	'''
	Rotation damping coefficient Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingExponentX = property(_get_RotationDampingExponentX, None)
	'''
	Rotation damping exponent X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingExponentY = property(_get_RotationDampingExponentY, None)
	'''
	Rotation damping exponent Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingExponentZ = property(_get_RotationDampingExponentZ, None)
	'''
	Rotation damping exponent Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationDampingSplineX = property(_get_RotationDampingSplineX, _set_RotationDampingSplineX)
	'''
	Rotation damping spline X

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationDampingSplineY = property(_get_RotationDampingSplineY, _set_RotationDampingSplineY)
	'''
	Rotation damping spline Y

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationDampingSplineZ = property(_get_RotationDampingSplineZ, _set_RotationDampingSplineZ)
	'''
	Rotation damping spline Z

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationPreloadX = property(_get_RotationPreloadX, None)
	'''
	Rotation preload X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationPreloadY = property(_get_RotationPreloadY, None)
	'''
	Rotation preload Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationPreloadZ = property(_get_RotationPreloadZ, None)
	'''
	Rotation preload Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessCoefficientX = property(_get_RotationStiffnessCoefficientX, None)
	'''
	Rotation stiffness coefficient X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessCoefficientY = property(_get_RotationStiffnessCoefficientY, None)
	'''
	Rotation stiffness coefficient Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessCoefficientZ = property(_get_RotationStiffnessCoefficientZ, None)
	'''
	Rotation stiffness coefficient Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessExponentX = property(_get_RotationStiffnessExponentX, None)
	'''
	Rotation stiffness exponent X

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessExponentY = property(_get_RotationStiffnessExponentY, None)
	'''
	Rotation stiffness exponent Y

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessExponentZ = property(_get_RotationStiffnessExponentZ, None)
	'''
	Rotation stiffness exponent Z

	:type: recurdyn.ProcessNet.IDouble
	'''
	RotationStiffnessSplineX = property(_get_RotationStiffnessSplineX, _set_RotationStiffnessSplineX)
	'''
	Rotation stiffness spline X

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationStiffnessSplineY = property(_get_RotationStiffnessSplineY, _set_RotationStiffnessSplineY)
	'''
	Rotation stiffness spline Y

	:type: recurdyn.ProcessNet.ISpline
	'''
	RotationStiffnessSplineZ = property(_get_RotationStiffnessSplineZ, _set_RotationStiffnessSplineZ)
	'''
	Rotation stiffness spline Z

	:type: recurdyn.ProcessNet.ISpline
	'''
	TranslationClearance = property(_get_TranslationClearance, None)
	'''
	Translation clearance

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingCoefficientAxial = property(_get_TranslationDampingCoefficientAxial, None)
	'''
	Translation damping coefficient axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingCoefficientRadial = property(_get_TranslationDampingCoefficientRadial, None)
	'''
	Translation damping coefficient radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingExponentAxial = property(_get_TranslationDampingExponentAxial, None)
	'''
	Translation Damping exponent axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingExponentRadial = property(_get_TranslationDampingExponentRadial, None)
	'''
	Translation Damping exponent radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationDampingSplineAxial = property(_get_TranslationDampingSplineAxial, _set_TranslationDampingSplineAxial)
	'''
	Translation damping spline axial

	:type: recurdyn.ProcessNet.ISpline
	'''
	TranslationDampingSplineRadial = property(_get_TranslationDampingSplineRadial, _set_TranslationDampingSplineRadial)
	'''
	Translation damping spline radial

	:type: recurdyn.ProcessNet.ISpline
	'''
	TranslationPreloadAxial = property(_get_TranslationPreloadAxial, None)
	'''
	Translation preload axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationPreloadRadial = property(_get_TranslationPreloadRadial, None)
	'''
	Translation preload radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessCoefficientAxial = property(_get_TranslationStiffnessCoefficientAxial, None)
	'''
	Translation stiffness coefficient axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessCoefficientRadial = property(_get_TranslationStiffnessCoefficientRadial, None)
	'''
	Translation stiffness coefficient radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessExponentAxial = property(_get_TranslationStiffnessExponentAxial, None)
	'''
	Translation stiffness exponent axial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessExponentRadial = property(_get_TranslationStiffnessExponentRadial, None)
	'''
	Translation stiffness exponent radial

	:type: recurdyn.ProcessNet.IDouble
	'''
	TranslationStiffnessSplineAxial = property(_get_TranslationStiffnessSplineAxial, _set_TranslationStiffnessSplineAxial)
	'''
	Translation stiffness spline axial

	:type: recurdyn.ProcessNet.ISpline
	'''
	TranslationStiffnessSplineRadial = property(_get_TranslationStiffnessSplineRadial, _set_TranslationStiffnessSplineRadial)
	'''
	Translation stiffness spline radial

	:type: recurdyn.ProcessNet.ISpline
	'''
	UseFriction = property(_get_UseFriction, _set_UseFriction)
	'''
	Use Contact Friction

	:type: bool
	'''
	UseRotationDampingExponent = property(_get_UseRotationDampingExponent, _set_UseRotationDampingExponent)
	'''
	Use rotation damping exponent

	:type: bool
	'''
	UseRotationDampingSpline = property(_get_UseRotationDampingSpline, _set_UseRotationDampingSpline)
	'''
	Use rotation damping spline

	:type: bool
	'''
	UseRotationStiffnessExponent = property(_get_UseRotationStiffnessExponent, _set_UseRotationStiffnessExponent)
	'''
	Use rotation stiffness exponent

	:type: bool
	'''
	UseRotationStiffnessSpline = property(_get_UseRotationStiffnessSpline, _set_UseRotationStiffnessSpline)
	'''
	Use rotation stiffness spline

	:type: bool
	'''
	UseTranslationDampingExponent = property(_get_UseTranslationDampingExponent, _set_UseTranslationDampingExponent)
	'''
	Use translation Damping exponent

	:type: bool
	'''
	UseTranslationDampingSpline = property(_get_UseTranslationDampingSpline, _set_UseTranslationDampingSpline)
	'''
	Use translation damping spline

	:type: bool
	'''
	UseTranslationStiffnessExponent = property(_get_UseTranslationStiffnessExponent, _set_UseTranslationStiffnessExponent)
	'''
	Use translation stiffness exponent

	:type: bool
	'''
	UseTranslationStiffnessSpline = property(_get_UseTranslationStiffnessSpline, _set_UseTranslationStiffnessSpline)
	'''
	Use translation stiffness spline

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_RotationDampingSplineX": _set_RotationDampingSplineX,
		"_set_RotationDampingSplineY": _set_RotationDampingSplineY,
		"_set_RotationDampingSplineZ": _set_RotationDampingSplineZ,
		"_set_RotationStiffnessSplineX": _set_RotationStiffnessSplineX,
		"_set_RotationStiffnessSplineY": _set_RotationStiffnessSplineY,
		"_set_RotationStiffnessSplineZ": _set_RotationStiffnessSplineZ,
		"_set_TranslationDampingSplineAxial": _set_TranslationDampingSplineAxial,
		"_set_TranslationDampingSplineRadial": _set_TranslationDampingSplineRadial,
		"_set_TranslationStiffnessSplineAxial": _set_TranslationStiffnessSplineAxial,
		"_set_TranslationStiffnessSplineRadial": _set_TranslationStiffnessSplineRadial,
		"_set_UseFriction": _set_UseFriction,
		"_set_UseRotationDampingExponent": _set_UseRotationDampingExponent,
		"_set_UseRotationDampingSpline": _set_UseRotationDampingSpline,
		"_set_UseRotationStiffnessExponent": _set_UseRotationStiffnessExponent,
		"_set_UseRotationStiffnessSpline": _set_UseRotationStiffnessSpline,
		"_set_UseTranslationDampingExponent": _set_UseTranslationDampingExponent,
		"_set_UseTranslationDampingSpline": _set_UseTranslationDampingSpline,
		"_set_UseTranslationStiffnessExponent": _set_UseTranslationStiffnessExponent,
		"_set_UseTranslationStiffnessSpline": _set_UseTranslationStiffnessSpline,
	}
	_prop_map_get_ = {
		"Friction": (10531, 2, (9, 0), (), "Friction", '{6F6A35D3-97FF-494A-8E1A-DF4E8101EBDB}'),
		"RotationDampingCoefficientX": (10520, 2, (9, 0), (), "RotationDampingCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingCoefficientY": (10521, 2, (9, 0), (), "RotationDampingCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingCoefficientZ": (10522, 2, (9, 0), (), "RotationDampingCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponentX": (10543, 2, (9, 0), (), "RotationDampingExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponentY": (10544, 2, (9, 0), (), "RotationDampingExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingExponentZ": (10545, 2, (9, 0), (), "RotationDampingExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationDampingSplineX": (10524, 2, (9, 0), (), "RotationDampingSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationDampingSplineY": (10525, 2, (9, 0), (), "RotationDampingSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationDampingSplineZ": (10526, 2, (9, 0), (), "RotationDampingSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationPreloadX": (10527, 2, (9, 0), (), "RotationPreloadX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationPreloadY": (10528, 2, (9, 0), (), "RotationPreloadY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationPreloadZ": (10529, 2, (9, 0), (), "RotationPreloadZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessCoefficientX": (10513, 2, (9, 0), (), "RotationStiffnessCoefficientX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessCoefficientY": (10514, 2, (9, 0), (), "RotationStiffnessCoefficientY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessCoefficientZ": (10515, 2, (9, 0), (), "RotationStiffnessCoefficientZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponentX": (10539, 2, (9, 0), (), "RotationStiffnessExponentX", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponentY": (10540, 2, (9, 0), (), "RotationStiffnessExponentY", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessExponentZ": (10541, 2, (9, 0), (), "RotationStiffnessExponentZ", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RotationStiffnessSplineX": (10517, 2, (9, 0), (), "RotationStiffnessSplineX", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationStiffnessSplineY": (10518, 2, (9, 0), (), "RotationStiffnessSplineY", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"RotationStiffnessSplineZ": (10519, 2, (9, 0), (), "RotationStiffnessSplineZ", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationClearance": (10512, 2, (9, 0), (), "TranslationClearance", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingCoefficientAxial": (10506, 2, (9, 0), (), "TranslationDampingCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingCoefficientRadial": (10505, 2, (9, 0), (), "TranslationDampingCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingExponentAxial": (10537, 2, (9, 0), (), "TranslationDampingExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingExponentRadial": (10536, 2, (9, 0), (), "TranslationDampingExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationDampingSplineAxial": (10509, 2, (9, 0), (), "TranslationDampingSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationDampingSplineRadial": (10508, 2, (9, 0), (), "TranslationDampingSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationPreloadAxial": (10511, 2, (9, 0), (), "TranslationPreloadAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationPreloadRadial": (10510, 2, (9, 0), (), "TranslationPreloadRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessCoefficientAxial": (10501, 2, (9, 0), (), "TranslationStiffnessCoefficientAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessCoefficientRadial": (10500, 2, (9, 0), (), "TranslationStiffnessCoefficientRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessExponentAxial": (10534, 2, (9, 0), (), "TranslationStiffnessExponentAxial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessExponentRadial": (10533, 2, (9, 0), (), "TranslationStiffnessExponentRadial", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"TranslationStiffnessSplineAxial": (10504, 2, (9, 0), (), "TranslationStiffnessSplineAxial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"TranslationStiffnessSplineRadial": (10503, 2, (9, 0), (), "TranslationStiffnessSplineRadial", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseFriction": (10530, 2, (11, 0), (), "UseFriction", None),
		"UseRotationDampingExponent": (10542, 2, (11, 0), (), "UseRotationDampingExponent", None),
		"UseRotationDampingSpline": (10523, 2, (11, 0), (), "UseRotationDampingSpline", None),
		"UseRotationStiffnessExponent": (10538, 2, (11, 0), (), "UseRotationStiffnessExponent", None),
		"UseRotationStiffnessSpline": (10516, 2, (11, 0), (), "UseRotationStiffnessSpline", None),
		"UseTranslationDampingExponent": (10535, 2, (11, 0), (), "UseTranslationDampingExponent", None),
		"UseTranslationDampingSpline": (10507, 2, (11, 0), (), "UseTranslationDampingSpline", None),
		"UseTranslationStiffnessExponent": (10532, 2, (11, 0), (), "UseTranslationStiffnessExponent", None),
		"UseTranslationStiffnessSpline": (10502, 2, (11, 0), (), "UseTranslationStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"RotationDampingSplineX": ((10524, LCID, 4, 0),()),
		"RotationDampingSplineY": ((10525, LCID, 4, 0),()),
		"RotationDampingSplineZ": ((10526, LCID, 4, 0),()),
		"RotationStiffnessSplineX": ((10517, LCID, 4, 0),()),
		"RotationStiffnessSplineY": ((10518, LCID, 4, 0),()),
		"RotationStiffnessSplineZ": ((10519, LCID, 4, 0),()),
		"TranslationDampingSplineAxial": ((10509, LCID, 4, 0),()),
		"TranslationDampingSplineRadial": ((10508, LCID, 4, 0),()),
		"TranslationStiffnessSplineAxial": ((10504, LCID, 4, 0),()),
		"TranslationStiffnessSplineRadial": ((10503, LCID, 4, 0),()),
		"UseFriction": ((10530, LCID, 4, 0),()),
		"UseRotationDampingExponent": ((10542, LCID, 4, 0),()),
		"UseRotationDampingSpline": ((10523, LCID, 4, 0),()),
		"UseRotationStiffnessExponent": ((10538, LCID, 4, 0),()),
		"UseRotationStiffnessSpline": ((10516, LCID, 4, 0),()),
		"UseTranslationDampingExponent": ((10535, LCID, 4, 0),()),
		"UseTranslationDampingSpline": ((10507, LCID, 4, 0),()),
		"UseTranslationStiffnessExponent": ((10532, LCID, 4, 0),()),
		"UseTranslationStiffnessSpline": ((10502, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainAssemblyCollection(DispatchBaseClass):
	'''IChainAssemblyCollection'''
	CLSID = IID('{F695BFDC-1A2A-4C74-9908-D337B2FF62B8}')
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
		:rtype: recurdyn.Chain.IChainAssembly
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0963256F-0F65-4E93-8FFA-B58651838BC6}')
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
		:rtype: recurdyn.Chain.IChainAssembly
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0963256F-0F65-4E93-8FFA-B58651838BC6}')
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
		return win32com.client.util.Iterator(ob, '{0963256F-0F65-4E93-8FFA-B58651838BC6}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{0963256F-0F65-4E93-8FFA-B58651838BC6}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IChainAssemblyContactFriction(DispatchBaseClass):
	'''Chain Contact Friction'''
	CLSID = IID('{6F6A35D3-97FF-494A-8E1A-DF4E8101EBDB}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_DynamicFrictionCoefficient(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "DynamicFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DynamicThresholdVelocity(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinDiameter(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticFrictionCoefficient(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticThresholdVelocity(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	DynamicFrictionCoefficient = property(_get_DynamicFrictionCoefficient, None)
	'''
	Dynamic Friction Coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	DynamicThresholdVelocity = property(_get_DynamicThresholdVelocity, None)
	'''
	Dynamic Threshold Velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	PinDiameter = property(_get_PinDiameter, None)
	'''
	Pin Diameter

	:type: recurdyn.ProcessNet.IDouble
	'''
	StaticFrictionCoefficient = property(_get_StaticFrictionCoefficient, None)
	'''
	Static Friction Coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	StaticThresholdVelocity = property(_get_StaticThresholdVelocity, None)
	'''
	Static Threshold Velocity

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DynamicFrictionCoefficient": (10552, 2, (9, 0), (), "DynamicFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DynamicThresholdVelocity": (10502, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinDiameter": (10551, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticFrictionCoefficient": (10503, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticThresholdVelocity": (10501, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IChainBody(DispatchBaseClass):
	'''Chain body'''
	CLSID = IID('{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}')
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
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
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
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
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

class IChainBodyCollection(DispatchBaseClass):
	'''IChainBodyCollection'''
	CLSID = IID('{ED20A123-7EEE-4173-9F9C-2D37D1138E48}')
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
		:rtype: recurdyn.Chain.IChainBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}')
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
		:rtype: recurdyn.Chain.IChainBody
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}')
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
		return win32com.client.util.Iterator(ob, '{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IChainBodyGuardLateral(DispatchBaseClass):
	'''Chain guide'''
	CLSID = IID('{98696CB8-03A8-4036-8D71-2143E04AB2AC}')
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
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(10550, 2, (9, 0), (), "ContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{82124DDF-C246-49F1-86B3-8DAD3B875DDD}'))
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
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact Property

	:type: recurdyn.Chain.IChainContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.Chain.IChainContactSearch
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryGuardLateral
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
		"ContactProperty": (10550, 2, (9, 0), (), "ContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'),
		"ContactSearch": (10552, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{82124DDF-C246-49F1-86B3-8DAD3B875DDD}'),
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

class IChainBodyGuide(DispatchBaseClass):
	'''Chain guide'''
	CLSID = IID('{3A623CE7-0BFB-48D9-AB5B-5B305B9F4D45}')
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


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10561, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(10550, 2, (9, 0), (), "ContactProperty", '{1E51E4E8-E4DC-4C00-BBCB-816315723567}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(10554, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{F2988F5F-6804-4797-9633-0BD1C78C4366}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NormalDirection(self):
		return self._ApplyTypes_(*(10553, 2, (3, 0), (), "NormalDirection", '{5252E329-CB8E-4D92-AA30-EB87B577E633}'))
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
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((10554, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NormalDirection(self, value):
		if "NormalDirection" in self.__dict__: self.__dict__["NormalDirection"] = value; return
		self._oleobj_.Invoke(*((10553, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact Property

	:type: recurdyn.Chain.IChainGuideContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.Chain.IChainContactSearch
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryGuide
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NormalDirection = property(_get_NormalDirection, _set_NormalDirection)
	'''
	Normal Direction

	:type: recurdyn.Chain.ChainNormalDirectionType
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
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_NormalDirection": _set_NormalDirection,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactProperty": (10550, 2, (9, 0), (), "ContactProperty", '{1E51E4E8-E4DC-4C00-BBCB-816315723567}'),
		"ContactSearch": (10552, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'),
		"ForceDisplay": (10554, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{F2988F5F-6804-4797-9633-0BD1C78C4366}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NormalDirection": (10553, 2, (3, 0), (), "NormalDirection", '{5252E329-CB8E-4D92-AA30-EB87B577E633}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((10554, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NormalDirection": ((10553, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyLink(DispatchBaseClass):
	'''Chain Body Link'''
	CLSID = IID('{A04DEA81-0603-4F81-91F5-D11FF259F6A1}')
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
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Graphic": (10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (10501, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((10501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyLinkCollection(DispatchBaseClass):
	'''IChainBodyLinkCollection'''
	CLSID = IID('{7DCEE901-515D-4780-AB01-89ECA089D8BE}')
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
		:rtype: recurdyn.Chain.IChainBodyLink
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{A04DEA81-0603-4F81-91F5-D11FF259F6A1}')
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
		:rtype: recurdyn.Chain.IChainBodyLink
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{A04DEA81-0603-4F81-91F5-D11FF259F6A1}')
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
		return win32com.client.util.Iterator(ob, '{A04DEA81-0603-4F81-91F5-D11FF259F6A1}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{A04DEA81-0603-4F81-91F5-D11FF259F6A1}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IChainBodyLinkMultiplexOffset(DispatchBaseClass):
	'''Chain Body Link Offset Multiplex'''
	CLSID = IID('{8740B4DF-D06F-4FCF-91C6-8302FFFE58B6}')
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
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Graphic": (10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (10501, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((10501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyLinkMultiplexPin(DispatchBaseClass):
	'''Chain Body Link Pin Multiplex'''
	CLSID = IID('{7532D229-00FF-4821-8177-B5225CC2FAE4}')
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


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10552, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{33736DE9-40C6-42C3-96EB-72FD82D10535}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkMultiplexPin
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{33736DE9-40C6-42C3-96EB-72FD82D10535}'),
		"Graphic": (10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (10501, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((10501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyLinkMultiplexRoller(DispatchBaseClass):
	'''Chain Body Link Roller Multiplex'''
	CLSID = IID('{1E546ED7-D793-4715-9F5E-CD694AA8B4E1}')
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


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10552, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkMultiplexRoller
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}'),
		"Graphic": (10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (10501, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((10501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyLinkOffset(DispatchBaseClass):
	'''Chain Body Link Offset'''
	CLSID = IID('{BBDD1814-F174-4AEF-944E-933DC4C656F9}')
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
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Graphic": (10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (10501, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((10501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyLinkPin(DispatchBaseClass):
	'''Chain Body Link Pin'''
	CLSID = IID('{14D6BFE5-15ED-45F4-9A34-0B7315136841}')
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


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10552, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{B4B7B26A-F4EB-486F-9909-74DA518613C4}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkPin
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{B4B7B26A-F4EB-486F-9909-74DA518613C4}'),
		"Graphic": (10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (10501, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((10501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyLinkRoller(DispatchBaseClass):
	'''Chain Body Link Roller'''
	CLSID = IID('{F389179B-A643-41C0-A674-860C335802C8}')
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


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10552, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{E6301A79-B289-4188-B213-AE53CA9E89BB}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkRoller
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{E6301A79-B289-4188-B213-AE53CA9E89BB}'),
		"Graphic": (10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UseBodyGraphic": (10501, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((10501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyLinkSilentInner(DispatchBaseClass):
	'''Chain Body Link Silent Outer'''
	CLSID = IID('{29199CB1-7647-4D2B-8D57-6A7701619A1C}')
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


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10553, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "Profile", '{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkSilentInner
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	Profile = property(_get_Profile, None)
	'''
	Profile of Link Silent

	:type: recurdyn.Chain.IChainProfileLinkSilent
	'''
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}'),
		"Graphic": (10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Profile": (10552, 2, (9, 0), (), "Profile", '{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}'),
		"UseBodyGraphic": (10501, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((10501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyLinkSilentOuter(DispatchBaseClass):
	'''Chain Body Link Silent Outer'''
	CLSID = IID('{33FC1BEE-4A91-4C01-82DE-1C83FC962DC1}')
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


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10553, LCID, 1, (24, 0), (),)


	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "Profile", '{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}'))
	def _get_UseBodyGraphic(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseBodyGraphic", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseBodyGraphic(self, value):
		if "UseBodyGraphic" in self.__dict__: self.__dict__["UseBodyGraphic"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkSilentOuter
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyBody
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
	Profile = property(_get_Profile, None)
	'''
	Profile of Link Silent

	:type: recurdyn.Chain.IChainProfileLinkSilent
	'''
	UseBodyGraphic = property(_get_UseBodyGraphic, _set_UseBodyGraphic)
	'''
	Use graphic of clone boy

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_UseBodyGraphic": _set_UseBodyGraphic,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}'),
		"Graphic": (10502, 2, (9, 0), (), "Graphic", '{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Profile": (10552, 2, (9, 0), (), "Profile", '{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}'),
		"UseBodyGraphic": (10501, 2, (11, 0), (), "UseBodyGraphic", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseBodyGraphic": ((10501, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainBodyRoller(DispatchBaseClass):
	'''Chain Roller Roller'''
	CLSID = IID('{67A861E0-46A2-4D78-A5FA-16B63F2A72AE}')
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
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(10550, 2, (9, 0), (), "ContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{2137EA2C-652F-4C83-B265-17AB71E0E202}'))
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
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact Property

	:type: recurdyn.Chain.IChainContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.Chain.IChainContactSearch
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryRoller
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
		"ContactProperty": (10550, 2, (9, 0), (), "ContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'),
		"ContactSearch": (10552, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{2137EA2C-652F-4C83-B265-17AB71E0E202}'),
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

class IChainBodySprocketMultiplex(DispatchBaseClass):
	'''Chain Sprocket Multiplex'''
	CLSID = IID('{11BBB345-C32E-4A00-9F53-C1FED84012B8}')
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
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(10550, 2, (9, 0), (), "ContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(10553, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "Geometry", '{84F6AAEF-A7BD-4C0E-A1B9-3377E4E8398B}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_SideContactProperty(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "SideContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'))
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
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact Property

	:type: recurdyn.Chain.IChainContactProperty
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.Chain.IChainContactSearch
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometrySprocketMultiplex
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
	SideContactProperty = property(_get_SideContactProperty, None)
	'''
	Side Contact Property

	:type: recurdyn.Chain.IChainContactProperty
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
		"ContactProperty": (10550, 2, (9, 0), (), "ContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'),
		"ContactSearch": (10553, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10552, 2, (9, 0), (), "Geometry", '{84F6AAEF-A7BD-4C0E-A1B9-3377E4E8398B}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SideContactProperty": (10551, 2, (9, 0), (), "SideContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'),
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

class IChainBodySprocketRoller(DispatchBaseClass):
	'''Chain Sprocket Roller'''
	CLSID = IID('{C34B22A6-F4E3-4747-BFF8-733F8317E9C2}')
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
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(10550, 2, (9, 0), (), "ContactProperty", '{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(10553, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(10554, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "Geometry", '{71E9EDCA-8586-4BC4-8C96-CA6CE987B7C7}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_SideContactProperty(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "SideContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((10554, LCID, 4, 0) + (value,) + ()))
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
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact Property

	:type: recurdyn.Chain.IChainContactPropertySprocket
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.Chain.IChainContactSearch
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometrySprocketRoller
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
	SideContactProperty = property(_get_SideContactProperty, None)
	'''
	Side Contact Property

	:type: recurdyn.Chain.IChainContactProperty
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactProperty": (10550, 2, (9, 0), (), "ContactProperty", '{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}'),
		"ContactSearch": (10553, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'),
		"ForceDisplay": (10554, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10552, 2, (9, 0), (), "Geometry", '{71E9EDCA-8586-4BC4-8C96-CA6CE987B7C7}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SideContactProperty": (10551, 2, (9, 0), (), "SideContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((10554, LCID, 4, 0),()),
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

class IChainBodySprocketSilent(DispatchBaseClass):
	'''Chain Sprocket Silent'''
	CLSID = IID('{20AA2528-64F0-4CC6-95B3-BE6402187F92}')
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
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(10550, 2, (9, 0), (), "ContactProperty", '{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}'))
	def _get_ContactSearch(self):
		return self._ApplyTypes_(*(10553, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(10554, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralBody(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "Geometry", '{46136858-6824-49C4-A14E-EC6C582E3C6D}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_SideContactProperty(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "SideContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((10554, LCID, 4, 0) + (value,) + ()))
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
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact Property

	:type: recurdyn.Chain.IChainContactPropertySprocket
	'''
	ContactSearch = property(_get_ContactSearch, None)
	'''
	ContactSearchType

	:type: recurdyn.Chain.IChainContactSearch
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	GeneralBody = property(_get_GeneralBody, None)
	'''
	GeneralBody

	:type: recurdyn.ProcessNet.IBody
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometrySprocketSilent
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
	SideContactProperty = property(_get_SideContactProperty, None)
	'''
	Side Contact Property

	:type: recurdyn.Chain.IChainContactProperty
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactProperty": (10550, 2, (9, 0), (), "ContactProperty", '{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}'),
		"ContactSearch": (10553, 2, (9, 0), (), "ContactSearch", '{134391CE-930C-47BE-983B-B326A771F701}'),
		"ForceDisplay": (10554, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralBody": (10500, 2, (9, 0), (), "GeneralBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"Geometry": (10552, 2, (9, 0), (), "Geometry", '{46136858-6824-49C4-A14E-EC6C582E3C6D}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"SideContactProperty": (10551, 2, (9, 0), (), "SideContactProperty", '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"ForceDisplay": ((10554, LCID, 4, 0),()),
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

class IChainContactFriction(DispatchBaseClass):
	'''Chain Contact Friction'''
	CLSID = IID('{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}')
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
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticFrictionCoefficient(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StaticThresholdVelocity(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	DynamicThresholdVelocity = property(_get_DynamicThresholdVelocity, None)
	'''
	Dynamic Threshold Velocity

	:type: recurdyn.ProcessNet.IDouble
	'''
	StaticFrictionCoefficient = property(_get_StaticFrictionCoefficient, None)
	'''
	Static Friction Coefficient

	:type: recurdyn.ProcessNet.IDouble
	'''
	StaticThresholdVelocity = property(_get_StaticThresholdVelocity, None)
	'''
	Static Threshold Velocity

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"DynamicThresholdVelocity": (10502, 2, (9, 0), (), "DynamicThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticFrictionCoefficient": (10503, 2, (9, 0), (), "StaticFrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StaticThresholdVelocity": (10501, 2, (9, 0), (), "StaticThresholdVelocity", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IChainContactPairInfo(DispatchBaseClass):
	'''IChainContactPairInfo'''
	CLSID = IID('{4BCBE390-C6BB-4E5A-9DA3-40A756B8326F}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_CheckContactPair(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "CheckContactPair", None))
	def _get_LinkSegmentNumber(self):
		return self._ApplyTypes_(*(10502, 2, (8, 0), (), "LinkSegmentNumber", None))

	def _set_CheckContactPair(self, value):
		if "CheckContactPair" in self.__dict__: self.__dict__["CheckContactPair"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
	def _set_LinkSegmentNumber(self, value):
		if "LinkSegmentNumber" in self.__dict__: self.__dict__["LinkSegmentNumber"] = value; return
		self._oleobj_.Invoke(*((10502, LCID, 4, 0) + (value,) + ()))

	CheckContactPair = property(_get_CheckContactPair, _set_CheckContactPair)
	'''
	Check ContactPair

	:type: bool
	'''
	LinkSegmentNumber = property(_get_LinkSegmentNumber, _set_LinkSegmentNumber)
	'''
	Link Segment Number

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_CheckContactPair": _set_CheckContactPair,
		"_set_LinkSegmentNumber": _set_LinkSegmentNumber,
	}
	_prop_map_get_ = {
		"CheckContactPair": (10501, 2, (11, 0), (), "CheckContactPair", None),
		"LinkSegmentNumber": (10502, 2, (8, 0), (), "LinkSegmentNumber", None),
	}
	_prop_map_put_ = {
		"CheckContactPair": ((10501, LCID, 4, 0),()),
		"LinkSegmentNumber": ((10502, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainContactPairInfoCollection(DispatchBaseClass):
	'''IChainContactPairInfo Collection'''
	CLSID = IID('{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}')
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
		:rtype: recurdyn.Chain.IChainContactPairInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{4BCBE390-C6BB-4E5A-9DA3-40A756B8326F}')
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
		:rtype: recurdyn.Chain.IChainContactPairInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{4BCBE390-C6BB-4E5A-9DA3-40A756B8326F}')
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
		return win32com.client.util.Iterator(ob, '{4BCBE390-C6BB-4E5A-9DA3-40A756B8326F}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{4BCBE390-C6BB-4E5A-9DA3-40A756B8326F}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IChainContactProperty(DispatchBaseClass):
	'''Chain contact property'''
	CLSID = IID('{8907B76F-36EF-42E8-AA90-2C02C76EF56F}')
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
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(10516, 2, (9, 0), (), "Friction", '{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(10506, 2, (3, 0), (), "FrictionType", '{6A354324-DD66-4599-9FB4-13728425522F}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(10514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(10510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(10511, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(10504, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(10513, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseMoreFrictionData(self):
		return self._ApplyTypes_(*(10515, 2, (11, 0), (), "UseMoreFrictionData", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(10509, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((10508, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((10506, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10502, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((10513, LCID, 4, 0) + (value,) + ()))
	def _set_UseMoreFrictionData(self, value):
		if "UseMoreFrictionData" in self.__dict__: self.__dict__["UseMoreFrictionData"] = value; return
		self._oleobj_.Invoke(*((10515, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))

	DampingCoefficient = property(_get_DampingCoefficient, None)
	'''
	The Viscous Damping Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingExponent = property(_get_DampingExponent, None)
	'''
	The Damping Exponent for a Non-linear Contact Normal Force

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingSpline = property(_get_DampingSpline, _set_DampingSpline)
	'''
	Damping Spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	Friction = property(_get_Friction, None)
	'''
	Friction

	:type: recurdyn.Chain.IChainContactFriction
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	The Friction Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionSpline = property(_get_FrictionSpline, _set_FrictionSpline)
	'''
	The Spline which Shows Relative Velocity to the Friction Coefficient or the Friction Force.

	:type: recurdyn.ProcessNet.ISpline
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction Type

	:type: recurdyn.Chain.ChainFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	The Indentation Exponent Yields an Indentation Damping Effect.

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessCoefficient = property(_get_StiffnessCoefficient, None)
	'''
	The Stiffness Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	The Stiffness Exponent for a Non-linear Contact Normal Force

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessSpline = property(_get_StiffnessSpline, _set_StiffnessSpline)
	'''
	Stiffness Spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	UseDampingExponent = property(_get_UseDampingExponent, _set_UseDampingExponent)
	'''
	Use Damping Exponent

	:type: bool
	'''
	UseDampingSpline = property(_get_UseDampingSpline, _set_UseDampingSpline)
	'''
	Use Damping Spline

	:type: bool
	'''
	UseIndentationExponent = property(_get_UseIndentationExponent, _set_UseIndentationExponent)
	'''
	Use Indentation Exponent

	:type: bool
	'''
	UseMoreFrictionData = property(_get_UseMoreFrictionData, _set_UseMoreFrictionData)
	'''
	Contact Friction Type

	:type: bool
	'''
	UseStiffnessExponent = property(_get_UseStiffnessExponent, _set_UseStiffnessExponent)
	'''
	Use Stiffness Exponent

	:type: bool
	'''
	UseStiffnessSpline = property(_get_UseStiffnessSpline, _set_UseStiffnessSpline)
	'''
	Use Stiffness Spline

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_DampingSpline": _set_DampingSpline,
		"_set_FrictionSpline": _set_FrictionSpline,
		"_set_FrictionType": _set_FrictionType,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseIndentationExponent": _set_UseIndentationExponent,
		"_set_UseMoreFrictionData": _set_UseMoreFrictionData,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
	}
	_prop_map_get_ = {
		"DampingCoefficient": (10503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (10512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (10505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"Friction": (10516, 2, (9, 0), (), "Friction", '{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}'),
		"FrictionCoefficient": (10507, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (10508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (10506, 2, (3, 0), (), "FrictionType", '{6A354324-DD66-4599-9FB4-13728425522F}'),
		"IndentationExponent": (10514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessCoefficient": (10500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (10510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (10502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (10511, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (10504, 2, (11, 0), (), "UseDampingSpline", None),
		"UseIndentationExponent": (10513, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseMoreFrictionData": (10515, 2, (11, 0), (), "UseMoreFrictionData", None),
		"UseStiffnessExponent": (10509, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (10501, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"DampingSpline": ((10505, LCID, 4, 0),()),
		"FrictionSpline": ((10508, LCID, 4, 0),()),
		"FrictionType": ((10506, LCID, 4, 0),()),
		"StiffnessSpline": ((10502, LCID, 4, 0),()),
		"UseDampingExponent": ((10511, LCID, 4, 0),()),
		"UseDampingSpline": ((10504, LCID, 4, 0),()),
		"UseIndentationExponent": ((10513, LCID, 4, 0),()),
		"UseMoreFrictionData": ((10515, LCID, 4, 0),()),
		"UseStiffnessExponent": ((10509, LCID, 4, 0),()),
		"UseStiffnessSpline": ((10501, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainContactPropertySprocket(DispatchBaseClass):
	'''Chain Contact Property'''
	CLSID = IID('{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}')
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
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(10516, 2, (9, 0), (), "Friction", '{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(10506, 2, (3, 0), (), "FrictionType", '{6A354324-DD66-4599-9FB4-13728425522F}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(10514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_NumberofMaxContactPoints(self):
		return self._ApplyTypes_(*(10551, 2, (3, 0), (), "NumberofMaxContactPoints", None))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(10510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseContactOutputFile(self):
		return self._ApplyTypes_(*(10552, 2, (11, 0), (), "UseContactOutputFile", None))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(10511, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(10504, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(10513, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseMoreFrictionData(self):
		return self._ApplyTypes_(*(10515, 2, (11, 0), (), "UseMoreFrictionData", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(10509, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((10508, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((10506, LCID, 4, 0) + (value,) + ()))
	def _set_NumberofMaxContactPoints(self, value):
		if "NumberofMaxContactPoints" in self.__dict__: self.__dict__["NumberofMaxContactPoints"] = value; return
		self._oleobj_.Invoke(*((10551, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10502, LCID, 4, 0) + (value,) + ()))
	def _set_UseContactOutputFile(self, value):
		if "UseContactOutputFile" in self.__dict__: self.__dict__["UseContactOutputFile"] = value; return
		self._oleobj_.Invoke(*((10552, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((10513, LCID, 4, 0) + (value,) + ()))
	def _set_UseMoreFrictionData(self, value):
		if "UseMoreFrictionData" in self.__dict__: self.__dict__["UseMoreFrictionData"] = value; return
		self._oleobj_.Invoke(*((10515, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))

	DampingCoefficient = property(_get_DampingCoefficient, None)
	'''
	The Viscous Damping Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingExponent = property(_get_DampingExponent, None)
	'''
	The Damping Exponent for a Non-linear Contact Normal Force

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingSpline = property(_get_DampingSpline, _set_DampingSpline)
	'''
	Damping Spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	Friction = property(_get_Friction, None)
	'''
	Friction

	:type: recurdyn.Chain.IChainContactFriction
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	The Friction Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionSpline = property(_get_FrictionSpline, _set_FrictionSpline)
	'''
	The Spline which Shows Relative Velocity to the Friction Coefficient or the Friction Force.

	:type: recurdyn.ProcessNet.ISpline
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction Type

	:type: recurdyn.Chain.ChainFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	The Indentation Exponent Yields an Indentation Damping Effect.

	:type: recurdyn.ProcessNet.IDouble
	'''
	NumberofMaxContactPoints = property(_get_NumberofMaxContactPoints, _set_NumberofMaxContactPoints)
	'''
	Number of Max Contact Points

	:type: int
	'''
	StiffnessCoefficient = property(_get_StiffnessCoefficient, None)
	'''
	The Stiffness Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	The Stiffness Exponent for a Non-linear Contact Normal Force

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessSpline = property(_get_StiffnessSpline, _set_StiffnessSpline)
	'''
	Stiffness Spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	UseContactOutputFile = property(_get_UseContactOutputFile, _set_UseContactOutputFile)
	'''
	Use Contact Output File

	:type: bool
	'''
	UseDampingExponent = property(_get_UseDampingExponent, _set_UseDampingExponent)
	'''
	Use Damping Exponent

	:type: bool
	'''
	UseDampingSpline = property(_get_UseDampingSpline, _set_UseDampingSpline)
	'''
	Use Damping Spline

	:type: bool
	'''
	UseIndentationExponent = property(_get_UseIndentationExponent, _set_UseIndentationExponent)
	'''
	Use Indentation Exponent

	:type: bool
	'''
	UseMoreFrictionData = property(_get_UseMoreFrictionData, _set_UseMoreFrictionData)
	'''
	Contact Friction Type

	:type: bool
	'''
	UseStiffnessExponent = property(_get_UseStiffnessExponent, _set_UseStiffnessExponent)
	'''
	Use Stiffness Exponent

	:type: bool
	'''
	UseStiffnessSpline = property(_get_UseStiffnessSpline, _set_UseStiffnessSpline)
	'''
	Use Stiffness Spline

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_DampingSpline": _set_DampingSpline,
		"_set_FrictionSpline": _set_FrictionSpline,
		"_set_FrictionType": _set_FrictionType,
		"_set_NumberofMaxContactPoints": _set_NumberofMaxContactPoints,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseContactOutputFile": _set_UseContactOutputFile,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseIndentationExponent": _set_UseIndentationExponent,
		"_set_UseMoreFrictionData": _set_UseMoreFrictionData,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
	}
	_prop_map_get_ = {
		"DampingCoefficient": (10503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (10512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (10505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"Friction": (10516, 2, (9, 0), (), "Friction", '{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}'),
		"FrictionCoefficient": (10507, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (10508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (10506, 2, (3, 0), (), "FrictionType", '{6A354324-DD66-4599-9FB4-13728425522F}'),
		"IndentationExponent": (10514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"NumberofMaxContactPoints": (10551, 2, (3, 0), (), "NumberofMaxContactPoints", None),
		"StiffnessCoefficient": (10500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (10510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (10502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseContactOutputFile": (10552, 2, (11, 0), (), "UseContactOutputFile", None),
		"UseDampingExponent": (10511, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (10504, 2, (11, 0), (), "UseDampingSpline", None),
		"UseIndentationExponent": (10513, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseMoreFrictionData": (10515, 2, (11, 0), (), "UseMoreFrictionData", None),
		"UseStiffnessExponent": (10509, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (10501, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"DampingSpline": ((10505, LCID, 4, 0),()),
		"FrictionSpline": ((10508, LCID, 4, 0),()),
		"FrictionType": ((10506, LCID, 4, 0),()),
		"NumberofMaxContactPoints": ((10551, LCID, 4, 0),()),
		"StiffnessSpline": ((10502, LCID, 4, 0),()),
		"UseContactOutputFile": ((10552, LCID, 4, 0),()),
		"UseDampingExponent": ((10511, LCID, 4, 0),()),
		"UseDampingSpline": ((10504, LCID, 4, 0),()),
		"UseIndentationExponent": ((10513, LCID, 4, 0),()),
		"UseMoreFrictionData": ((10515, LCID, 4, 0),()),
		"UseStiffnessExponent": ((10509, LCID, 4, 0),()),
		"UseStiffnessSpline": ((10501, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainContactSearch(DispatchBaseClass):
	'''Chain Contact Search'''
	CLSID = IID('{134391CE-930C-47BE-983B-B326A771F701}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Type(self):
		return self._ApplyTypes_(*(10500, 2, (3, 0), (), "Type", None))
	def _get_UseUserBoundaryForPartialSearch(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseUserBoundaryForPartialSearch", None))
	def _get_UserBoundaryForPartialSearch(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "UserBoundaryForPartialSearch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_Type(self, value):
		if "Type" in self.__dict__: self.__dict__["Type"] = value; return
		self._oleobj_.Invoke(*((10500, LCID, 4, 0) + (value,) + ()))
	def _set_UseUserBoundaryForPartialSearch(self, value):
		if "UseUserBoundaryForPartialSearch" in self.__dict__: self.__dict__["UseUserBoundaryForPartialSearch"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))

	Type = property(_get_Type, _set_Type)
	'''
	Search type of the flange.

	:type: recurdyn.Chain.ChainContactSearchType
	'''
	UseUserBoundaryForPartialSearch = property(_get_UseUserBoundaryForPartialSearch, _set_UseUserBoundaryForPartialSearch)
	'''
	Use the user boundary of the partial search.

	:type: bool
	'''
	UserBoundaryForPartialSearch = property(_get_UserBoundaryForPartialSearch, None)
	'''
	User boundary of the partial search.

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Type": _set_Type,
		"_set_UseUserBoundaryForPartialSearch": _set_UseUserBoundaryForPartialSearch,
	}
	_prop_map_get_ = {
		"Type": (10500, 2, (3, 0), (), "Type", None),
		"UseUserBoundaryForPartialSearch": (10501, 2, (11, 0), (), "UseUserBoundaryForPartialSearch", None),
		"UserBoundaryForPartialSearch": (10502, 2, (9, 0), (), "UserBoundaryForPartialSearch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"Type": ((10500, LCID, 4, 0),()),
		"UseUserBoundaryForPartialSearch": ((10501, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGeometryGroupGuideArc(DispatchBaseClass):
	'''Chain Guide Body Geometry'''
	CLSID = IID('{B0B8CBCE-6E48-4300-9436-0599707E3C93}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_CenterPointsAndArcAngle(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "CenterPointsAndArcAngle", '{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}'))
	def _get_CenterPointsAndRadius(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "CenterPointsAndRadius", '{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}'))
	def _get_Color(self):
		return self._ApplyTypes_(*(10505, 2, (19, 0), (), "Color", None))
	def _get_DampingCoefficient(self):
		return self._ApplyTypes_(*(10516, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(10522, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(10518, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_Depth(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DepthNormalVector(self):
		return self._ApplyTypes_(*(10508, 2, (8197, 0), (), "DepthNormalVector", None))
	def _get_PassingPoints(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "PassingPoints", '{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}'))
	def _get_PointEnd(self):
		return self._ApplyTypes_(*(10511, 2, (8197, 0), (), "PointEnd", None))
	def _get_PointStart(self):
		return self._ApplyTypes_(*(10510, 2, (8197, 0), (), "PointStart", None))
	def _get_PointsType(self):
		return self._ApplyTypes_(*(10500, 2, (3, 0), (), "PointsType", '{ADC464BD-C49B-4632-938A-6FC04B6A492E}'))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(10520, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(10515, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_Thickness(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(10521, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseGroupGuideArcCharacteristic(self):
		return self._ApplyTypes_(*(10512, 2, (11, 0), (), "UseGroupGuideArcCharacteristic", None))
	def _get_UseOnlyLinkRollerContact(self):
		return self._ApplyTypes_(*(10509, 2, (11, 0), (), "UseOnlyLinkRollerContact", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(10519, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(10514, 2, (11, 0), (), "UseStiffnessSpline", None))
	def _get_ViewReferenceFrame(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "ViewReferenceFrame", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))

	def _set_Color(self, value):
		if "Color" in self.__dict__: self.__dict__["Color"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((10518, LCID, 4, 0) + (value,) + ()))
	def _set_DepthNormalVector(self, value):
		if "DepthNormalVector" in self.__dict__: self.__dict__["DepthNormalVector"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10508, LCID, 4, 0) + (variantValue,) + ()))
	def _set_PointEnd(self, value):
		if "PointEnd" in self.__dict__: self.__dict__["PointEnd"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (variantValue,) + ()))
	def _set_PointStart(self, value):
		if "PointStart" in self.__dict__: self.__dict__["PointStart"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (variantValue,) + ()))
	def _set_PointsType(self, value):
		if "PointsType" in self.__dict__: self.__dict__["PointsType"] = value; return
		self._oleobj_.Invoke(*((10500, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10515, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((10521, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_UseGroupGuideArcCharacteristic(self, value):
		if "UseGroupGuideArcCharacteristic" in self.__dict__: self.__dict__["UseGroupGuideArcCharacteristic"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
	def _set_UseOnlyLinkRollerContact(self, value):
		if "UseOnlyLinkRollerContact" in self.__dict__: self.__dict__["UseOnlyLinkRollerContact"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((10519, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10514, LCID, 4, 0) + (value,) + ()))
	def _set_ViewReferenceFrame(self, value):
		if "ViewReferenceFrame" in self.__dict__: self.__dict__["ViewReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))

	CenterPointsAndArcAngle = property(_get_CenterPointsAndArcAngle, None)
	'''
	Ceneter Points and Arc Angle

	:type: recurdyn.Chain.IChainGroupGuidePointsWithAdditionalInfoCollection
	'''
	CenterPointsAndRadius = property(_get_CenterPointsAndRadius, None)
	'''
	Ceneter Points and Radius

	:type: recurdyn.Chain.IChainGroupGuidePointsWithAdditionalInfoCollection
	'''
	Color = property(_get_Color, _set_Color)
	'''
	Group Guide Arc Color

	:type: int
	'''
	DampingCoefficient = property(_get_DampingCoefficient, None)
	'''
	The Viscous Damping Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingExponent = property(_get_DampingExponent, None)
	'''
	The Damping Exponent for a Non-linear Contact Normal Force

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingSpline = property(_get_DampingSpline, _set_DampingSpline)
	'''
	Damping Spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	Depth = property(_get_Depth, None)
	'''
	Depth

	:type: recurdyn.ProcessNet.IDouble
	'''
	DepthNormalVector = property(_get_DepthNormalVector, _set_DepthNormalVector)
	'''
	Depth Normal Vector

	:type: list[float]
	'''
	PassingPoints = property(_get_PassingPoints, None)
	'''
	Passing Points

	:type: recurdyn.Chain.IChainGroupGuidePointsWithAdditionalInfoCollection
	'''
	PointEnd = property(_get_PointEnd, _set_PointEnd)
	'''
	End Point

	:type: list[float]
	'''
	PointStart = property(_get_PointStart, _set_PointStart)
	'''
	Start Point

	:type: list[float]
	'''
	PointsType = property(_get_PointsType, _set_PointsType)
	'''
	Points Type

	:type: recurdyn.Chain.ChainGuidePointsType
	'''
	StiffnessCoefficient = property(_get_StiffnessCoefficient, None)
	'''
	The Stiffness Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	The Stiffness Exponent for a Non-linear Contact Normal Force

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessSpline = property(_get_StiffnessSpline, _set_StiffnessSpline)
	'''
	Stiffness Spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	Thickness = property(_get_Thickness, None)
	'''
	Thickness

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseDampingExponent = property(_get_UseDampingExponent, _set_UseDampingExponent)
	'''
	Use Damping Exponent

	:type: bool
	'''
	UseDampingSpline = property(_get_UseDampingSpline, _set_UseDampingSpline)
	'''
	Use Damping Spline

	:type: bool
	'''
	UseGroupGuideArcCharacteristic = property(_get_UseGroupGuideArcCharacteristic, _set_UseGroupGuideArcCharacteristic)
	'''
	Use Group Guide Arc Characteristic

	:type: bool
	'''
	UseOnlyLinkRollerContact = property(_get_UseOnlyLinkRollerContact, _set_UseOnlyLinkRollerContact)
	'''
	Use Only Link Roller Contact

	:type: bool
	'''
	UseStiffnessExponent = property(_get_UseStiffnessExponent, _set_UseStiffnessExponent)
	'''
	Use Stiffness Exponent

	:type: bool
	'''
	UseStiffnessSpline = property(_get_UseStiffnessSpline, _set_UseStiffnessSpline)
	'''
	Use Stiffness Spline

	:type: bool
	'''
	ViewReferenceFrame = property(_get_ViewReferenceFrame, _set_ViewReferenceFrame)
	'''
	View Reference Frame

	:type: recurdyn.ProcessNet.IMarker
	'''

	_prop_map_set_function_ = {
		"_set_Color": _set_Color,
		"_set_DampingSpline": _set_DampingSpline,
		"_set_DepthNormalVector": _set_DepthNormalVector,
		"_set_PointEnd": _set_PointEnd,
		"_set_PointStart": _set_PointStart,
		"_set_PointsType": _set_PointsType,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseGroupGuideArcCharacteristic": _set_UseGroupGuideArcCharacteristic,
		"_set_UseOnlyLinkRollerContact": _set_UseOnlyLinkRollerContact,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
		"_set_ViewReferenceFrame": _set_ViewReferenceFrame,
	}
	_prop_map_get_ = {
		"CenterPointsAndArcAngle": (10503, 2, (9, 0), (), "CenterPointsAndArcAngle", '{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}'),
		"CenterPointsAndRadius": (10502, 2, (9, 0), (), "CenterPointsAndRadius", '{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}'),
		"Color": (10505, 2, (19, 0), (), "Color", None),
		"DampingCoefficient": (10516, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (10522, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (10518, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"Depth": (10506, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DepthNormalVector": (10508, 2, (8197, 0), (), "DepthNormalVector", None),
		"PassingPoints": (10501, 2, (9, 0), (), "PassingPoints", '{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}'),
		"PointEnd": (10511, 2, (8197, 0), (), "PointEnd", None),
		"PointStart": (10510, 2, (8197, 0), (), "PointStart", None),
		"PointsType": (10500, 2, (3, 0), (), "PointsType", '{ADC464BD-C49B-4632-938A-6FC04B6A492E}'),
		"StiffnessCoefficient": (10513, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (10520, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (10515, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"Thickness": (10507, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseDampingExponent": (10521, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (10517, 2, (11, 0), (), "UseDampingSpline", None),
		"UseGroupGuideArcCharacteristic": (10512, 2, (11, 0), (), "UseGroupGuideArcCharacteristic", None),
		"UseOnlyLinkRollerContact": (10509, 2, (11, 0), (), "UseOnlyLinkRollerContact", None),
		"UseStiffnessExponent": (10519, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (10514, 2, (11, 0), (), "UseStiffnessSpline", None),
		"ViewReferenceFrame": (10504, 2, (9, 0), (), "ViewReferenceFrame", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
	}
	_prop_map_put_ = {
		"Color": ((10505, LCID, 4, 0),()),
		"DampingSpline": ((10518, LCID, 4, 0),()),
		"DepthNormalVector": ((10508, LCID, 4, 0),()),
		"PointEnd": ((10511, LCID, 4, 0),()),
		"PointStart": ((10510, LCID, 4, 0),()),
		"PointsType": ((10500, LCID, 4, 0),()),
		"StiffnessSpline": ((10515, LCID, 4, 0),()),
		"UseDampingExponent": ((10521, LCID, 4, 0),()),
		"UseDampingSpline": ((10517, LCID, 4, 0),()),
		"UseGroupGuideArcCharacteristic": ((10512, LCID, 4, 0),()),
		"UseOnlyLinkRollerContact": ((10509, LCID, 4, 0),()),
		"UseStiffnessExponent": ((10519, LCID, 4, 0),()),
		"UseStiffnessSpline": ((10514, LCID, 4, 0),()),
		"ViewReferenceFrame": ((10504, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGeometryGuardLateral(DispatchBaseClass):
	'''Chain Guide Body Geometry'''
	CLSID = IID('{82124DDF-C246-49F1-86B3-8DAD3B875DDD}')
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
	def _get_Height(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_InactiveType(self):
		return self._ApplyTypes_(*(10504, 2, (3, 0), (), "InactiveType", '{674BB7BB-6BE5-41B4-93AA-649213BBDA72}'))
	def _get_InnerWidth(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "InnerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Length(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "Length", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
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
	def _get_Thickness(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_InactiveType(self, value):
		if "InactiveType" in self.__dict__: self.__dict__["InactiveType"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))
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
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyGeometry
	'''
	Height = property(_get_Height, None)
	'''
	Height of the Guard(H)

	:type: recurdyn.ProcessNet.IDouble
	'''
	InactiveType = property(_get_InactiveType, _set_InactiveType)
	'''
	Inactive type.

	:type: recurdyn.TrackLM.RollerGuardInactiveType
	'''
	InnerWidth = property(_get_InnerWidth, None)
	'''
	Inner Width of the Guard(W)

	:type: recurdyn.ProcessNet.IDouble
	'''
	Length = property(_get_Length, None)
	'''
	Length of the Guard(L)

	:type: recurdyn.ProcessNet.IDouble
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
	Thickness = property(_get_Thickness, None)
	'''
	Thickness of the Guard(T)

	:type: recurdyn.ProcessNet.IDouble
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_InactiveType": _set_InactiveType,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"Height": (10501, 2, (9, 0), (), "Height", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"InactiveType": (10504, 2, (3, 0), (), "InactiveType", '{674BB7BB-6BE5-41B4-93AA-649213BBDA72}'),
		"InnerWidth": (10502, 2, (9, 0), (), "InnerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Length": (10500, 2, (9, 0), (), "Length", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"Thickness": (10503, 2, (9, 0), (), "Thickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"InactiveType": ((10504, LCID, 4, 0),()),
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

class IChainGeometryGuide(DispatchBaseClass):
	'''Chain Guide Body Geometry'''
	CLSID = IID('{F2988F5F-6804-4797-9633-0BD1C78C4366}')
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


	def _get_CenterPointsAndArcAngle(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "CenterPointsAndArcAngle", '{E6353564-8957-4E10-8A7B-12F98C5ECCFB}'))
	def _get_CenterPointsAndRadius(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "CenterPointsAndRadius", '{E6353564-8957-4E10-8A7B-12F98C5ECCFB}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Depth(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberOfPoints(self):
		return self._ApplyTypes_(*(10504, 2, (3, 0), (), "NumberOfPoints", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PassingPoints(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "PassingPoints", '{E6353564-8957-4E10-8A7B-12F98C5ECCFB}'))
	def _get_PointEnd(self):
		return self._ApplyTypes_(*(10510, 2, (8197, 0), (), "PointEnd", None))
	def _get_PointStart(self):
		return self._ApplyTypes_(*(10509, 2, (8197, 0), (), "PointStart", None))
	def _get_PointsType(self):
		return self._ApplyTypes_(*(10500, 2, (3, 0), (), "PointsType", '{ADC464BD-C49B-4632-938A-6FC04B6A492E}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_UseOnlyLinkRollerContact(self):
		return self._ApplyTypes_(*(10507, 2, (11, 0), (), "UseOnlyLinkRollerContact", None))
	def _get_UseSolidGeometry(self):
		return self._ApplyTypes_(*(10508, 2, (11, 0), (), "UseSolidGeometry", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))
	def _get_ViewReferenceFrame(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "ViewReferenceFrame", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_PointEnd(self, value):
		if "PointEnd" in self.__dict__: self.__dict__["PointEnd"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (variantValue,) + ()))
	def _set_PointStart(self, value):
		if "PointStart" in self.__dict__: self.__dict__["PointStart"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (variantValue,) + ()))
	def _set_PointsType(self, value):
		if "PointsType" in self.__dict__: self.__dict__["PointsType"] = value; return
		self._oleobj_.Invoke(*((10500, LCID, 4, 0) + (value,) + ()))
	def _set_UseOnlyLinkRollerContact(self, value):
		if "UseOnlyLinkRollerContact" in self.__dict__: self.__dict__["UseOnlyLinkRollerContact"] = value; return
		self._oleobj_.Invoke(*((10507, LCID, 4, 0) + (value,) + ()))
	def _set_UseSolidGeometry(self, value):
		if "UseSolidGeometry" in self.__dict__: self.__dict__["UseSolidGeometry"] = value; return
		self._oleobj_.Invoke(*((10508, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))
	def _set_ViewReferenceFrame(self, value):
		if "ViewReferenceFrame" in self.__dict__: self.__dict__["ViewReferenceFrame"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))

	CenterPointsAndArcAngle = property(_get_CenterPointsAndArcAngle, None)
	'''
	Ceneter Points and Arc Angle

	:type: recurdyn.Chain.IChainGuidePointsWithAdditionalInfoCollection
	'''
	CenterPointsAndRadius = property(_get_CenterPointsAndRadius, None)
	'''
	Ceneter Points and Radius

	:type: recurdyn.Chain.IChainGuidePointsWithAdditionalInfoCollection
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Depth = property(_get_Depth, None)
	'''
	Depth

	:type: recurdyn.ProcessNet.IDouble
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
	NumberOfPoints = property(_get_NumberOfPoints, None)
	'''
	Number of Points

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
	PassingPoints = property(_get_PassingPoints, None)
	'''
	Passing Points

	:type: recurdyn.Chain.IChainGuidePointsWithAdditionalInfoCollection
	'''
	PointEnd = property(_get_PointEnd, _set_PointEnd)
	'''
	End Point

	:type: list[float]
	'''
	PointStart = property(_get_PointStart, _set_PointStart)
	'''
	Start Point

	:type: list[float]
	'''
	PointsType = property(_get_PointsType, _set_PointsType)
	'''
	Points Type

	:type: recurdyn.Chain.ChainGuidePointsType
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	UseOnlyLinkRollerContact = property(_get_UseOnlyLinkRollerContact, _set_UseOnlyLinkRollerContact)
	'''
	Use Only Link Roller Contact

	:type: bool
	'''
	UseSolidGeometry = property(_get_UseSolidGeometry, _set_UseSolidGeometry)
	'''
	Use Solid Geometry

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)
	ViewReferenceFrame = property(_get_ViewReferenceFrame, _set_ViewReferenceFrame)
	'''
	View Reference Frame

	:type: recurdyn.ProcessNet.IMarker
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
		"_set_PointEnd": _set_PointEnd,
		"_set_PointStart": _set_PointStart,
		"_set_PointsType": _set_PointsType,
		"_set_UseOnlyLinkRollerContact": _set_UseOnlyLinkRollerContact,
		"_set_UseSolidGeometry": _set_UseSolidGeometry,
		"_set_UserData": _set_UserData,
		"_set_ViewReferenceFrame": _set_ViewReferenceFrame,
	}
	_prop_map_get_ = {
		"CenterPointsAndArcAngle": (10503, 2, (9, 0), (), "CenterPointsAndArcAngle", '{E6353564-8957-4E10-8A7B-12F98C5ECCFB}'),
		"CenterPointsAndRadius": (10502, 2, (9, 0), (), "CenterPointsAndRadius", '{E6353564-8957-4E10-8A7B-12F98C5ECCFB}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Depth": (10506, 2, (9, 0), (), "Depth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberOfPoints": (10504, 2, (3, 0), (), "NumberOfPoints", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PassingPoints": (10501, 2, (9, 0), (), "PassingPoints", '{E6353564-8957-4E10-8A7B-12F98C5ECCFB}'),
		"PointEnd": (10510, 2, (8197, 0), (), "PointEnd", None),
		"PointStart": (10509, 2, (8197, 0), (), "PointStart", None),
		"PointsType": (10500, 2, (3, 0), (), "PointsType", '{ADC464BD-C49B-4632-938A-6FC04B6A492E}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"UseOnlyLinkRollerContact": (10507, 2, (11, 0), (), "UseOnlyLinkRollerContact", None),
		"UseSolidGeometry": (10508, 2, (11, 0), (), "UseSolidGeometry", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
		"ViewReferenceFrame": (10505, 2, (9, 0), (), "ViewReferenceFrame", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"PointEnd": ((10510, LCID, 4, 0),()),
		"PointStart": ((10509, LCID, 4, 0),()),
		"PointsType": ((10500, LCID, 4, 0),()),
		"UseOnlyLinkRollerContact": ((10507, LCID, 4, 0),()),
		"UseSolidGeometry": ((10508, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
		"ViewReferenceFrame": ((10505, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGeometryLinkMultiplexPin(DispatchBaseClass):
	'''Chain Link Roller Body Geometry'''
	CLSID = IID('{33736DE9-40C6-42C3-96EB-72FD82D10535}')
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
	def _get_LinkType(self):
		return self._ApplyTypes_(*(10501, 2, (3, 0), (), "LinkType", '{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberOfStrands(self):
		return self._ApplyTypes_(*(10503, 2, (3, 0), (), "NumberOfStrands", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PinDiameter(self):
		return self._ApplyTypes_(*(10511, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Pitch(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PitchTransverse(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "PitchTransverse", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkPinHeight(self):
		return self._ApplyTypes_(*(10510, 2, (9, 0), (), "PlateLinkPinHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkPinThickness(self):
		return self._ApplyTypes_(*(10509, 2, (9, 0), (), "PlateLinkPinThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RollerDiameter(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "RollerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
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
	LinkType = property(_get_LinkType, None)
	'''
	Link Type

	:type: recurdyn.Chain.ChainLinkType
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NumberOfStrands = property(_get_NumberOfStrands, None)
	'''
	Number of Strands

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
	PinDiameter = property(_get_PinDiameter, None)
	'''
	Pin Diameter(Dp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PinLength = property(_get_PinLength, None)
	'''
	Pin Length(Lp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	Pitch = property(_get_Pitch, None)
	'''
	Pitch(P)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PitchTransverse = property(_get_PitchTransverse, None)
	'''
	Transverse Pitch(Pt)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkPinHeight = property(_get_PlateLinkPinHeight, None)
	'''
	Height of Pin Link Plate(Hpl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkPinThickness = property(_get_PlateLinkPinThickness, None)
	'''
	Thickness of Pin Link Plate(Tpl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RollerDiameter = property(_get_RollerDiameter, None)
	'''
	Roller Diameter(Dr)

	:type: recurdyn.ProcessNet.IDouble
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
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LinkType": (10501, 2, (3, 0), (), "LinkType", '{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberOfStrands": (10503, 2, (3, 0), (), "NumberOfStrands", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PinDiameter": (10511, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinLength": (10512, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Pitch": (10502, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PitchTransverse": (10504, 2, (9, 0), (), "PitchTransverse", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkPinHeight": (10510, 2, (9, 0), (), "PlateLinkPinHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkPinThickness": (10509, 2, (9, 0), (), "PlateLinkPinThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RollerDiameter": (10505, 2, (9, 0), (), "RollerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
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

class IChainGeometryLinkMultiplexRoller(DispatchBaseClass):
	'''Chain Link Roller Body Geometry'''
	CLSID = IID('{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}')
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


	def _get_BushingWidth(self):
		return self._ApplyTypes_(*(10516, 2, (5, 0), (), "BushingWidth", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LeftBushingPosition(self):
		return self._ApplyTypes_(*(10514, 2, (8197, 0), (), "LeftBushingPosition", None))
	def _get_LinkType(self):
		return self._ApplyTypes_(*(10501, 2, (3, 0), (), "LinkType", '{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberOfStrands(self):
		return self._ApplyTypes_(*(10503, 2, (3, 0), (), "NumberOfStrands", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PinDiameter(self):
		return self._ApplyTypes_(*(10511, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Pitch(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PitchTransverse(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "PitchTransverse", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkRollerHeight(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "PlateLinkRollerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkRollerThickness(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "PlateLinkRollerThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkRollerWidth(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "PlateLinkRollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RightBushingPosition(self):
		return self._ApplyTypes_(*(10515, 2, (8197, 0), (), "RightBushingPosition", None))
	def _get_RollerDiameter(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "RollerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseBushingPosition(self):
		return self._ApplyTypes_(*(10513, 2, (11, 0), (), "UseBushingPosition", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))

	def _set_BushingWidth(self, value):
		if "BushingWidth" in self.__dict__: self.__dict__["BushingWidth"] = value; return
		self._oleobj_.Invoke(*((10516, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LeftBushingPosition(self, value):
		if "LeftBushingPosition" in self.__dict__: self.__dict__["LeftBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10514, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_RightBushingPosition(self, value):
		if "RightBushingPosition" in self.__dict__: self.__dict__["RightBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10515, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseBushingPosition(self, value):
		if "UseBushingPosition" in self.__dict__: self.__dict__["UseBushingPosition"] = value; return
		self._oleobj_.Invoke(*((10513, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BushingWidth = property(_get_BushingWidth, _set_BushingWidth)
	'''
	Bushing Width (Bw)

	:type: float
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
	LeftBushingPosition = property(_get_LeftBushingPosition, _set_LeftBushingPosition)
	'''
	Left Bushing Position

	:type: list[float]
	'''
	LinkType = property(_get_LinkType, None)
	'''
	Link Type

	:type: recurdyn.Chain.ChainLinkType
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NumberOfStrands = property(_get_NumberOfStrands, None)
	'''
	Number of Strands

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
	PinDiameter = property(_get_PinDiameter, None)
	'''
	Pin Diameter(Dp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PinLength = property(_get_PinLength, None)
	'''
	Pin Length(Lp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	Pitch = property(_get_Pitch, None)
	'''
	Pitch(P)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PitchTransverse = property(_get_PitchTransverse, None)
	'''
	Transverse Pitch(Pt)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkRollerHeight = property(_get_PlateLinkRollerHeight, None)
	'''
	Height of Roller Link Plate(Hrl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkRollerThickness = property(_get_PlateLinkRollerThickness, None)
	'''
	Thickness of Roller Link Plate(Trl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkRollerWidth = property(_get_PlateLinkRollerWidth, None)
	'''
	Width between Roller Link Plate(Wrl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RightBushingPosition = property(_get_RightBushingPosition, _set_RightBushingPosition)
	'''
	Right Bushing Position

	:type: list[float]
	'''
	RollerDiameter = property(_get_RollerDiameter, None)
	'''
	Roller Diameter(Dr)

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseBushingPosition = property(_get_UseBushingPosition, _set_UseBushingPosition)
	'''
	Use Bushing Position

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)

	_prop_map_set_function_ = {
		"_set_BushingWidth": _set_BushingWidth,
		"_set_Comment": _set_Comment,
		"_set_LeftBushingPosition": _set_LeftBushingPosition,
		"_set_Name": _set_Name,
		"_set_RightBushingPosition": _set_RightBushingPosition,
		"_set_UseBushingPosition": _set_UseBushingPosition,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BushingWidth": (10516, 2, (5, 0), (), "BushingWidth", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LeftBushingPosition": (10514, 2, (8197, 0), (), "LeftBushingPosition", None),
		"LinkType": (10501, 2, (3, 0), (), "LinkType", '{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberOfStrands": (10503, 2, (3, 0), (), "NumberOfStrands", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PinDiameter": (10511, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinLength": (10512, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Pitch": (10502, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PitchTransverse": (10504, 2, (9, 0), (), "PitchTransverse", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkRollerHeight": (10508, 2, (9, 0), (), "PlateLinkRollerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkRollerThickness": (10507, 2, (9, 0), (), "PlateLinkRollerThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkRollerWidth": (10506, 2, (9, 0), (), "PlateLinkRollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RightBushingPosition": (10515, 2, (8197, 0), (), "RightBushingPosition", None),
		"RollerDiameter": (10505, 2, (9, 0), (), "RollerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseBushingPosition": (10513, 2, (11, 0), (), "UseBushingPosition", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
	}
	_prop_map_put_ = {
		"BushingWidth": ((10516, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LeftBushingPosition": ((10514, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"RightBushingPosition": ((10515, LCID, 4, 0),()),
		"UseBushingPosition": ((10513, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGeometryLinkPin(DispatchBaseClass):
	'''Chain Link Pin Body Geometry'''
	CLSID = IID('{B4B7B26A-F4EB-486F-9909-74DA518613C4}')
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
	def _get_LinkType(self):
		return self._ApplyTypes_(*(10501, 2, (3, 0), (), "LinkType", '{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PinDiameter(self):
		return self._ApplyTypes_(*(10510, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(10511, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Pitch(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkPinHeight(self):
		return self._ApplyTypes_(*(10509, 2, (9, 0), (), "PlateLinkPinHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkPinThickness(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "PlateLinkPinThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkPinWidth(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "PlateLinkPinWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RollerDiameter(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "RollerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RollerWidth(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "RollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))

	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LinkType(self, value):
		if "LinkType" in self.__dict__: self.__dict__["LinkType"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
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
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicPropertyGeometry
	'''
	LinkType = property(_get_LinkType, _set_LinkType)
	'''
	Link Type

	:type: recurdyn.Chain.ChainLinkType
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
	PinDiameter = property(_get_PinDiameter, None)
	'''
	Pin Diameter(Dp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PinLength = property(_get_PinLength, None)
	'''
	Pin Length(Lp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	Pitch = property(_get_Pitch, None)
	'''
	Pitch(P)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkPinHeight = property(_get_PlateLinkPinHeight, None)
	'''
	Height of Pin Link Plate(Hpl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkPinThickness = property(_get_PlateLinkPinThickness, None)
	'''
	Thickness of Pin Link Plate(Tpl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkPinWidth = property(_get_PlateLinkPinWidth, None)
	'''
	Width between Pin Link Plate(Wpl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RollerDiameter = property(_get_RollerDiameter, None)
	'''
	Roller Diameter(Dr)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RollerWidth = property(_get_RollerWidth, None)
	'''
	Roller Width(Wr)

	:type: recurdyn.ProcessNet.IDouble
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_LinkType": _set_LinkType,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LinkType": (10501, 2, (3, 0), (), "LinkType", '{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PinDiameter": (10510, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinLength": (10511, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Pitch": (10504, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkPinHeight": (10509, 2, (9, 0), (), "PlateLinkPinHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkPinThickness": (10508, 2, (9, 0), (), "PlateLinkPinThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkPinWidth": (10507, 2, (9, 0), (), "PlateLinkPinWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RollerDiameter": (10505, 2, (9, 0), (), "RollerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RollerWidth": (10506, 2, (9, 0), (), "RollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
	}
	_prop_map_put_ = {
		"Comment": ((102, LCID, 4, 0),()),
		"LinkType": ((10501, LCID, 4, 0),()),
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

class IChainGeometryLinkRoller(DispatchBaseClass):
	'''Chain Link Roller Body Geometry'''
	CLSID = IID('{E6301A79-B289-4188-B213-AE53CA9E89BB}')
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


	def _get_BushingWidth(self):
		return self._ApplyTypes_(*(10515, 2, (5, 0), (), "BushingWidth", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LeftBushingPosition(self):
		return self._ApplyTypes_(*(10513, 2, (8197, 0), (), "LeftBushingPosition", None))
	def _get_LinkType(self):
		return self._ApplyTypes_(*(10501, 2, (3, 0), (), "LinkType", '{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberOfLinkSets(self):
		return self._ApplyTypes_(*(10502, 2, (3, 0), (), "NumberOfLinkSets", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PinDiameter(self):
		return self._ApplyTypes_(*(10510, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(10511, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Pitch(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkRollerHeight(self):
		return self._ApplyTypes_(*(10509, 2, (9, 0), (), "PlateLinkRollerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkRollerThickness(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "PlateLinkRollerThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateLinkRollerWidth(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "PlateLinkRollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RightBushingPosition(self):
		return self._ApplyTypes_(*(10514, 2, (8197, 0), (), "RightBushingPosition", None))
	def _get_RollerDiameter(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "RollerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RollerWidth(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "RollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseBushingPosition(self):
		return self._ApplyTypes_(*(10512, 2, (11, 0), (), "UseBushingPosition", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))

	def _set_BushingWidth(self, value):
		if "BushingWidth" in self.__dict__: self.__dict__["BushingWidth"] = value; return
		self._oleobj_.Invoke(*((10515, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LeftBushingPosition(self, value):
		if "LeftBushingPosition" in self.__dict__: self.__dict__["LeftBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10513, LCID, 4, 0) + (variantValue,) + ()))
	def _set_LinkType(self, value):
		if "LinkType" in self.__dict__: self.__dict__["LinkType"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_RightBushingPosition(self, value):
		if "RightBushingPosition" in self.__dict__: self.__dict__["RightBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10514, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseBushingPosition(self, value):
		if "UseBushingPosition" in self.__dict__: self.__dict__["UseBushingPosition"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BushingWidth = property(_get_BushingWidth, _set_BushingWidth)
	'''
	Bushing Width (Bw)

	:type: float
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
	LeftBushingPosition = property(_get_LeftBushingPosition, _set_LeftBushingPosition)
	'''
	Left Bushing Position

	:type: list[float]
	'''
	LinkType = property(_get_LinkType, _set_LinkType)
	'''
	Link Type

	:type: recurdyn.Chain.ChainLinkType
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NumberOfLinkSets = property(_get_NumberOfLinkSets, None)
	'''
	Number of Link Sets

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
	PinDiameter = property(_get_PinDiameter, None)
	'''
	Pin Diameter(Dp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PinLength = property(_get_PinLength, None)
	'''
	Pin Length(Lp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	Pitch = property(_get_Pitch, None)
	'''
	Pitch(P)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkRollerHeight = property(_get_PlateLinkRollerHeight, None)
	'''
	Height of Roller Link Plate(Hrl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkRollerThickness = property(_get_PlateLinkRollerThickness, None)
	'''
	Thickness of Roller Link Plate(Trl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateLinkRollerWidth = property(_get_PlateLinkRollerWidth, None)
	'''
	Width between Roller Link Plate(Wrl)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RightBushingPosition = property(_get_RightBushingPosition, _set_RightBushingPosition)
	'''
	Right Bushing Position

	:type: list[float]
	'''
	RollerDiameter = property(_get_RollerDiameter, None)
	'''
	Roller Diameter(Dr)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RollerWidth = property(_get_RollerWidth, None)
	'''
	Roller Width(Wr)

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseBushingPosition = property(_get_UseBushingPosition, _set_UseBushingPosition)
	'''
	Use Bushing Position

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)

	_prop_map_set_function_ = {
		"_set_BushingWidth": _set_BushingWidth,
		"_set_Comment": _set_Comment,
		"_set_LeftBushingPosition": _set_LeftBushingPosition,
		"_set_LinkType": _set_LinkType,
		"_set_Name": _set_Name,
		"_set_RightBushingPosition": _set_RightBushingPosition,
		"_set_UseBushingPosition": _set_UseBushingPosition,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BushingWidth": (10515, 2, (5, 0), (), "BushingWidth", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LeftBushingPosition": (10513, 2, (8197, 0), (), "LeftBushingPosition", None),
		"LinkType": (10501, 2, (3, 0), (), "LinkType", '{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberOfLinkSets": (10502, 2, (3, 0), (), "NumberOfLinkSets", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PinDiameter": (10510, 2, (9, 0), (), "PinDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinLength": (10511, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Pitch": (10504, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkRollerHeight": (10509, 2, (9, 0), (), "PlateLinkRollerHeight", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkRollerThickness": (10508, 2, (9, 0), (), "PlateLinkRollerThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateLinkRollerWidth": (10507, 2, (9, 0), (), "PlateLinkRollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RightBushingPosition": (10514, 2, (8197, 0), (), "RightBushingPosition", None),
		"RollerDiameter": (10505, 2, (9, 0), (), "RollerDiameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RollerWidth": (10506, 2, (9, 0), (), "RollerWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseBushingPosition": (10512, 2, (11, 0), (), "UseBushingPosition", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
	}
	_prop_map_put_ = {
		"BushingWidth": ((10515, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LeftBushingPosition": ((10513, LCID, 4, 0),()),
		"LinkType": ((10501, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"RightBushingPosition": ((10514, LCID, 4, 0),()),
		"UseBushingPosition": ((10512, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGeometryLinkSilentInner(DispatchBaseClass):
	'''Chain Link Silent Inner Body Geometry'''
	CLSID = IID('{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}')
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


	def _get_BushingWidth(self):
		return self._ApplyTypes_(*(10508, 2, (5, 0), (), "BushingWidth", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LeftBushingPosition(self):
		return self._ApplyTypes_(*(10506, 2, (8197, 0), (), "LeftBushingPosition", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinRadius(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Pitch(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateThickness(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "PlateThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RightBushingPosition(self):
		return self._ApplyTypes_(*(10507, 2, (8197, 0), (), "RightBushingPosition", None))
	def _get_UseBushingPosition(self):
		return self._ApplyTypes_(*(10505, 2, (11, 0), (), "UseBushingPosition", None))
	def _get_UseSingleInnerLink(self):
		return self._ApplyTypes_(*(10504, 2, (11, 0), (), "UseSingleInnerLink", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))

	def _set_BushingWidth(self, value):
		if "BushingWidth" in self.__dict__: self.__dict__["BushingWidth"] = value; return
		self._oleobj_.Invoke(*((10508, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LeftBushingPosition(self, value):
		if "LeftBushingPosition" in self.__dict__: self.__dict__["LeftBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10506, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_RightBushingPosition(self, value):
		if "RightBushingPosition" in self.__dict__: self.__dict__["RightBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10507, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseBushingPosition(self, value):
		if "UseBushingPosition" in self.__dict__: self.__dict__["UseBushingPosition"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_UseSingleInnerLink(self, value):
		if "UseSingleInnerLink" in self.__dict__: self.__dict__["UseSingleInnerLink"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BushingWidth = property(_get_BushingWidth, _set_BushingWidth)
	'''
	Bushing Width (Bw)

	:type: float
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
	LeftBushingPosition = property(_get_LeftBushingPosition, _set_LeftBushingPosition)
	'''
	Left Bushing Position

	:type: list[float]
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
	PinLength = property(_get_PinLength, None)
	'''
	Pin Length(Lp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PinRadius = property(_get_PinRadius, None)
	'''
	Pin Radius(Rp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	Pitch = property(_get_Pitch, None)
	'''
	Pitch(P)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateThickness = property(_get_PlateThickness, None)
	'''
	Plate Thickness(Tp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RightBushingPosition = property(_get_RightBushingPosition, _set_RightBushingPosition)
	'''
	Right Bushing Position

	:type: list[float]
	'''
	UseBushingPosition = property(_get_UseBushingPosition, _set_UseBushingPosition)
	'''
	Use Bushing Position

	:type: bool
	'''
	UseSingleInnerLink = property(_get_UseSingleInnerLink, _set_UseSingleInnerLink)
	'''
	Use Single Inner Link

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)

	_prop_map_set_function_ = {
		"_set_BushingWidth": _set_BushingWidth,
		"_set_Comment": _set_Comment,
		"_set_LeftBushingPosition": _set_LeftBushingPosition,
		"_set_Name": _set_Name,
		"_set_RightBushingPosition": _set_RightBushingPosition,
		"_set_UseBushingPosition": _set_UseBushingPosition,
		"_set_UseSingleInnerLink": _set_UseSingleInnerLink,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BushingWidth": (10508, 2, (5, 0), (), "BushingWidth", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LeftBushingPosition": (10506, 2, (8197, 0), (), "LeftBushingPosition", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PinLength": (10503, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinRadius": (10502, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Pitch": (10500, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateThickness": (10501, 2, (9, 0), (), "PlateThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RightBushingPosition": (10507, 2, (8197, 0), (), "RightBushingPosition", None),
		"UseBushingPosition": (10505, 2, (11, 0), (), "UseBushingPosition", None),
		"UseSingleInnerLink": (10504, 2, (11, 0), (), "UseSingleInnerLink", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
	}
	_prop_map_put_ = {
		"BushingWidth": ((10508, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LeftBushingPosition": ((10506, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"RightBushingPosition": ((10507, LCID, 4, 0),()),
		"UseBushingPosition": ((10505, LCID, 4, 0),()),
		"UseSingleInnerLink": ((10504, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGeometryLinkSilentOuter(DispatchBaseClass):
	'''Chain Link Silent Outer Body Geometry'''
	CLSID = IID('{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}')
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


	def _get_BushingWidth(self):
		return self._ApplyTypes_(*(10508, 2, (5, 0), (), "BushingWidth", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LeftBushingPosition(self):
		return self._ApplyTypes_(*(10506, 2, (8197, 0), (), "LeftBushingPosition", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_OuterLinkTotalWidth(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "OuterLinkTotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PinLength(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PinRadius(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Pitch(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_PlateThickness(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "PlateThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RightBushingPosition(self):
		return self._ApplyTypes_(*(10507, 2, (8197, 0), (), "RightBushingPosition", None))
	def _get_UseBushingPosition(self):
		return self._ApplyTypes_(*(10505, 2, (11, 0), (), "UseBushingPosition", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))

	def _set_BushingWidth(self, value):
		if "BushingWidth" in self.__dict__: self.__dict__["BushingWidth"] = value; return
		self._oleobj_.Invoke(*((10508, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LeftBushingPosition(self, value):
		if "LeftBushingPosition" in self.__dict__: self.__dict__["LeftBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10506, LCID, 4, 0) + (variantValue,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_RightBushingPosition(self, value):
		if "RightBushingPosition" in self.__dict__: self.__dict__["RightBushingPosition"] = value; return
		variantValue = win32com.client.VARIANT(8197, value)
		self._oleobj_.Invoke(*((10507, LCID, 4, 0) + (variantValue,) + ()))
	def _set_UseBushingPosition(self, value):
		if "UseBushingPosition" in self.__dict__: self.__dict__["UseBushingPosition"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	BushingWidth = property(_get_BushingWidth, _set_BushingWidth)
	'''
	Bushing Width (Bw)

	:type: float
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
	LeftBushingPosition = property(_get_LeftBushingPosition, _set_LeftBushingPosition)
	'''
	Left Bushing Position

	:type: list[float]
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	OuterLinkTotalWidth = property(_get_OuterLinkTotalWidth, None)
	'''
	Total Width of Outer Link(Wl)

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
	PinLength = property(_get_PinLength, None)
	'''
	Pin Length(Lp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PinRadius = property(_get_PinRadius, None)
	'''
	Pin Radius(Rp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	Pitch = property(_get_Pitch, None)
	'''
	Pitch(P)

	:type: recurdyn.ProcessNet.IDouble
	'''
	PlateThickness = property(_get_PlateThickness, None)
	'''
	Plate Thickness(Tp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RightBushingPosition = property(_get_RightBushingPosition, _set_RightBushingPosition)
	'''
	Right Bushing Position

	:type: list[float]
	'''
	UseBushingPosition = property(_get_UseBushingPosition, _set_UseBushingPosition)
	'''
	Use Bushing Position

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)

	_prop_map_set_function_ = {
		"_set_BushingWidth": _set_BushingWidth,
		"_set_Comment": _set_Comment,
		"_set_LeftBushingPosition": _set_LeftBushingPosition,
		"_set_Name": _set_Name,
		"_set_RightBushingPosition": _set_RightBushingPosition,
		"_set_UseBushingPosition": _set_UseBushingPosition,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"BushingWidth": (10508, 2, (5, 0), (), "BushingWidth", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LeftBushingPosition": (10506, 2, (8197, 0), (), "LeftBushingPosition", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"OuterLinkTotalWidth": (10501, 2, (9, 0), (), "OuterLinkTotalWidth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PinLength": (10504, 2, (9, 0), (), "PinLength", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PinRadius": (10503, 2, (9, 0), (), "PinRadius", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Pitch": (10500, 2, (9, 0), (), "Pitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"PlateThickness": (10502, 2, (9, 0), (), "PlateThickness", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RightBushingPosition": (10507, 2, (8197, 0), (), "RightBushingPosition", None),
		"UseBushingPosition": (10505, 2, (11, 0), (), "UseBushingPosition", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
	}
	_prop_map_put_ = {
		"BushingWidth": ((10508, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LeftBushingPosition": ((10506, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"RightBushingPosition": ((10507, LCID, 4, 0),()),
		"UseBushingPosition": ((10505, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGeometryRoller(DispatchBaseClass):
	'''Chain Roller Body Geometry'''
	CLSID = IID('{2137EA2C-652F-4C83-B265-17AB71E0E202}')
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
	def _get_RadiusFrange(self):
		return self._ApplyTypes_(*(10604, 2, (9, 0), (), "RadiusFrange", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusRoller(self):
		return self._ApplyTypes_(*(10603, 2, (9, 0), (), "RadiusRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))
	def _get_WidthRoller(self):
		return self._ApplyTypes_(*(10601, 2, (9, 0), (), "WidthRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WidthTotal(self):
		return self._ApplyTypes_(*(10602, 2, (9, 0), (), "WidthTotal", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

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
	RadiusFrange = property(_get_RadiusFrange, None)
	'''
	Frange Radius(Rf)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusRoller = property(_get_RadiusRoller, None)
	'''
	Roller Radius(Rr)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)
	WidthRoller = property(_get_WidthRoller, None)
	'''
	Roller Width(Wr)

	:type: recurdyn.ProcessNet.IDouble
	'''
	WidthTotal = property(_get_WidthTotal, None)
	'''
	Total Width(Wt)

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_Comment": _set_Comment,
		"_set_Name": _set_Name,
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
		"RadiusFrange": (10604, 2, (9, 0), (), "RadiusFrange", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusRoller": (10603, 2, (9, 0), (), "RadiusRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
		"WidthRoller": (10601, 2, (9, 0), (), "WidthRoller", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WidthTotal": (10602, 2, (9, 0), (), "WidthTotal", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IChainGeometrySprocketMultiplex(DispatchBaseClass):
	'''Chain Sprocket Multiplex Body Geometry'''
	CLSID = IID('{84F6AAEF-A7BD-4C0E-A1B9-3377E4E8398B}')
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


	def UpdateProperties(self):
		'''
		Update Sprocket Data for Tooth Profile.
		'''
		return self._oleobj_.InvokeTypes(10531, LCID, 1, (24, 0), (),)


	def UpdatefromISO606Lib(self):
		'''
		Update from ISO 606 Lib.
		'''
		return self._oleobj_.InvokeTypes(10526, LCID, 1, (24, 0), (),)


	def _get_ChainLinkRollerCircleRadiusLoop(self):
		return self._ApplyTypes_(*(10519, 2, (5, 0), (), "ChainLinkRollerCircleRadiusLoop", None))
	def _get_ChainLinkRollerCircleRadiusRoller(self):
		return self._ApplyTypes_(*(10518, 2, (5, 0), (), "ChainLinkRollerCircleRadiusRoller", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DiameterPitchISO606(self):
		return self._ApplyTypes_(*(10506, 2, (5, 0), (), "DiameterPitchISO606", None))
	def _get_DiameterPitchParameter(self):
		return self._ApplyTypes_(*(10510, 2, (9, 0), (), "DiameterPitchParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DiameterRootISO606(self):
		return self._ApplyTypes_(*(10508, 2, (5, 0), (), "DiameterRootISO606", None))
	def _get_DiameterRootParameter(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "DiameterRootParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DiameterTipISO606(self):
		return self._ApplyTypes_(*(10507, 2, (5, 0), (), "DiameterTipISO606", None))
	def _get_DiameterTipParameter(self):
		return self._ApplyTypes_(*(10511, 2, (9, 0), (), "DiameterTipParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(10528, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None))
	def _get_LinkAssemblyRadialDistance(self):
		return self._ApplyTypes_(*(10529, 2, (5, 0), (), "LinkAssemblyRadialDistance", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberOfStrands(self):
		return self._ApplyTypes_(*(10551, 2, (3, 0), (), "NumberOfStrands", None))
	def _get_NumberofTeeth(self):
		return self._ApplyTypes_(*(10505, 2, (3, 0), (), "NumberofTeeth", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_PitchTransverse(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "PitchTransverse", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(10530, 2, (9, 0), (), "Profile", '{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}'))
	def _get_RadiusAddendum(self):
		return self._ApplyTypes_(*(10517, 2, (9, 0), (), "RadiusAddendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusBase(self):
		return self._ApplyTypes_(*(10516, 2, (9, 0), (), "RadiusBase", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusDedendum(self):
		return self._ApplyTypes_(*(10514, 2, (9, 0), (), "RadiusDedendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusPitch(self):
		return self._ApplyTypes_(*(10515, 2, (9, 0), (), "RadiusPitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusTFlankISO606(self):
		return self._ApplyTypes_(*(10509, 2, (5, 0), (), "RadiusTFlankISO606", None))
	def _get_RadiusTFlankParameter(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "RadiusTFlankParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusWheel(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "RadiusWheel", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RollerLinkDiameter(self):
		return self._ApplyTypes_(*(10525, 2, (5, 0), (), "RollerLinkDiameter", None))
	def _get_RollerLinkPitch(self):
		return self._ApplyTypes_(*(10524, 2, (5, 0), (), "RollerLinkPitch", None))
	def _get_RollerSeatingAngleISO606(self):
		return self._ApplyTypes_(*(10521, 2, (5, 0), (), "RollerSeatingAngleISO606", None))
	def _get_RollerSeatingAngleParameter(self):
		return self._ApplyTypes_(*(10523, 2, (9, 0), (), "RollerSeatingAngleParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RollerSeatingRadiusISO606(self):
		return self._ApplyTypes_(*(10520, 2, (5, 0), (), "RollerSeatingRadiusISO606", None))
	def _get_RollerSeatingRadiusParameter(self):
		return self._ApplyTypes_(*(10522, 2, (9, 0), (), "RollerSeatingRadiusParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SprocketType(self):
		return self._ApplyTypes_(*(10501, 2, (3, 0), (), "SprocketType", '{BE5ED324-09C1-462B-8D26-DB09D5B18BF6}'))
	def _get_UseLinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(10527, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))
	def _get_WidthTeeth(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "WidthTeeth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WidthWheels(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "WidthWheels", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_ChainLinkRollerCircleRadiusLoop(self, value):
		if "ChainLinkRollerCircleRadiusLoop" in self.__dict__: self.__dict__["ChainLinkRollerCircleRadiusLoop"] = value; return
		self._oleobj_.Invoke(*((10519, LCID, 4, 0) + (value,) + ()))
	def _set_ChainLinkRollerCircleRadiusRoller(self, value):
		if "ChainLinkRollerCircleRadiusRoller" in self.__dict__: self.__dict__["ChainLinkRollerCircleRadiusRoller"] = value; return
		self._oleobj_.Invoke(*((10518, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LinkAssemblyAssembledRadius(self, value):
		if "LinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["LinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((10528, LCID, 4, 0) + (value,) + ()))
	def _set_LinkAssemblyRadialDistance(self, value):
		if "LinkAssemblyRadialDistance" in self.__dict__: self.__dict__["LinkAssemblyRadialDistance"] = value; return
		self._oleobj_.Invoke(*((10529, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NumberOfStrands(self, value):
		if "NumberOfStrands" in self.__dict__: self.__dict__["NumberOfStrands"] = value; return
		self._oleobj_.Invoke(*((10551, LCID, 4, 0) + (value,) + ()))
	def _set_NumberofTeeth(self, value):
		if "NumberofTeeth" in self.__dict__: self.__dict__["NumberofTeeth"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_RollerLinkDiameter(self, value):
		if "RollerLinkDiameter" in self.__dict__: self.__dict__["RollerLinkDiameter"] = value; return
		self._oleobj_.Invoke(*((10525, LCID, 4, 0) + (value,) + ()))
	def _set_RollerLinkPitch(self, value):
		if "RollerLinkPitch" in self.__dict__: self.__dict__["RollerLinkPitch"] = value; return
		self._oleobj_.Invoke(*((10524, LCID, 4, 0) + (value,) + ()))
	def _set_SprocketType(self, value):
		if "SprocketType" in self.__dict__: self.__dict__["SprocketType"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkAssemblyAssembledRadius(self, value):
		if "UseLinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["UseLinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((10527, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ChainLinkRollerCircleRadiusLoop = property(_get_ChainLinkRollerCircleRadiusLoop, _set_ChainLinkRollerCircleRadiusLoop)
	'''
	Chain Link Roller Circle Loop Radius

	:type: float
	'''
	ChainLinkRollerCircleRadiusRoller = property(_get_ChainLinkRollerCircleRadiusRoller, _set_ChainLinkRollerCircleRadiusRoller)
	'''
	Chain Link Roller Circle Radius

	:type: float
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DiameterPitchISO606 = property(_get_DiameterPitchISO606, None)
	'''
	Pitch Diameter(D) for ISO 606 Library Type

	:type: float
	'''
	DiameterPitchParameter = property(_get_DiameterPitchParameter, None)
	'''
	Pitch Diameter(D) for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	DiameterRootISO606 = property(_get_DiameterRootISO606, None)
	'''
	Root Diameter(Df) for ISO 606 Library Type

	:type: float
	'''
	DiameterRootParameter = property(_get_DiameterRootParameter, None)
	'''
	Root Diameter(Df) for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	DiameterTipISO606 = property(_get_DiameterTipISO606, None)
	'''
	Tip Diameter(Da) for ISO 606 Library Type

	:type: float
	'''
	DiameterTipParameter = property(_get_DiameterTipParameter, None)
	'''
	Tip Diameter(Da) for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
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
	LinkAssemblyAssembledRadius = property(_get_LinkAssemblyAssembledRadius, _set_LinkAssemblyAssembledRadius)
	'''
	Assembled Radius of the Link Assembly.

	:type: float
	'''
	LinkAssemblyRadialDistance = property(_get_LinkAssemblyRadialDistance, _set_LinkAssemblyRadialDistance)
	'''
	Radial Radius of the Link Assembly.

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NumberOfStrands = property(_get_NumberOfStrands, _set_NumberOfStrands)
	'''
	Number of Strands

	:type: int
	'''
	NumberofTeeth = property(_get_NumberofTeeth, _set_NumberofTeeth)
	'''
	Number of Teeth

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
	PitchTransverse = property(_get_PitchTransverse, None)
	'''
	Transverse Pitch(Pt)

	:type: recurdyn.ProcessNet.IDouble
	'''
	Profile = property(_get_Profile, None)
	'''
	Profile of Sprocket

	:type: recurdyn.TrackLM.ITrackLMToothProfileSprocket
	'''
	RadiusAddendum = property(_get_RadiusAddendum, None)
	'''
	Addendum Radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusBase = property(_get_RadiusBase, None)
	'''
	Base Radius(Rb)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusDedendum = property(_get_RadiusDedendum, None)
	'''
	Dedendum Radius(Rd)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusPitch = property(_get_RadiusPitch, None)
	'''
	Pitch Radius(Rp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusTFlankISO606 = property(_get_RadiusTFlankISO606, None)
	'''
	T-Flank Radius(Re) for ISO 606 Library Type

	:type: float
	'''
	RadiusTFlankParameter = property(_get_RadiusTFlankParameter, None)
	'''
	T-Flank Radius(Re) for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusWheel = property(_get_RadiusWheel, None)
	'''
	Radius Wheel(Rw)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RollerLinkDiameter = property(_get_RollerLinkDiameter, _set_RollerLinkDiameter)
	'''
	Roller Link Diameter(D1)

	:type: float
	'''
	RollerLinkPitch = property(_get_RollerLinkPitch, _set_RollerLinkPitch)
	'''
	Roller Link Pitch(P)

	:type: float
	'''
	RollerSeatingAngleISO606 = property(_get_RollerSeatingAngleISO606, None)
	'''
	Roller Seating Angle for ISO 606 Library Type

	:type: float
	'''
	RollerSeatingAngleParameter = property(_get_RollerSeatingAngleParameter, None)
	'''
	Roller Seating Angle for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	RollerSeatingRadiusISO606 = property(_get_RollerSeatingRadiusISO606, None)
	'''
	Roller Seating Radius for ISO 606 Library Type

	:type: float
	'''
	RollerSeatingRadiusParameter = property(_get_RollerSeatingRadiusParameter, None)
	'''
	Roller Seating Radius for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	SprocketType = property(_get_SprocketType, _set_SprocketType)
	'''
	Sprocket Type

	:type: recurdyn.Chain.ChainSprocketType
	'''
	UseLinkAssemblyAssembledRadius = property(_get_UseLinkAssemblyAssembledRadius, _set_UseLinkAssemblyAssembledRadius)
	'''
	Use Assembled Radius.

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)
	WidthTeeth = property(_get_WidthTeeth, None)
	'''
	Width Teeth(Wt)

	:type: recurdyn.ProcessNet.IDouble
	'''
	WidthWheels = property(_get_WidthWheels, None)
	'''
	Width Wheels(Ww)

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_ChainLinkRollerCircleRadiusLoop": _set_ChainLinkRollerCircleRadiusLoop,
		"_set_ChainLinkRollerCircleRadiusRoller": _set_ChainLinkRollerCircleRadiusRoller,
		"_set_Comment": _set_Comment,
		"_set_LinkAssemblyAssembledRadius": _set_LinkAssemblyAssembledRadius,
		"_set_LinkAssemblyRadialDistance": _set_LinkAssemblyRadialDistance,
		"_set_Name": _set_Name,
		"_set_NumberOfStrands": _set_NumberOfStrands,
		"_set_NumberofTeeth": _set_NumberofTeeth,
		"_set_RollerLinkDiameter": _set_RollerLinkDiameter,
		"_set_RollerLinkPitch": _set_RollerLinkPitch,
		"_set_SprocketType": _set_SprocketType,
		"_set_UseLinkAssemblyAssembledRadius": _set_UseLinkAssemblyAssembledRadius,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ChainLinkRollerCircleRadiusLoop": (10519, 2, (5, 0), (), "ChainLinkRollerCircleRadiusLoop", None),
		"ChainLinkRollerCircleRadiusRoller": (10518, 2, (5, 0), (), "ChainLinkRollerCircleRadiusRoller", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DiameterPitchISO606": (10506, 2, (5, 0), (), "DiameterPitchISO606", None),
		"DiameterPitchParameter": (10510, 2, (9, 0), (), "DiameterPitchParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DiameterRootISO606": (10508, 2, (5, 0), (), "DiameterRootISO606", None),
		"DiameterRootParameter": (10512, 2, (9, 0), (), "DiameterRootParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DiameterTipISO606": (10507, 2, (5, 0), (), "DiameterTipISO606", None),
		"DiameterTipParameter": (10511, 2, (9, 0), (), "DiameterTipParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LinkAssemblyAssembledRadius": (10528, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None),
		"LinkAssemblyRadialDistance": (10529, 2, (5, 0), (), "LinkAssemblyRadialDistance", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberOfStrands": (10551, 2, (3, 0), (), "NumberOfStrands", None),
		"NumberofTeeth": (10505, 2, (3, 0), (), "NumberofTeeth", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"PitchTransverse": (10552, 2, (9, 0), (), "PitchTransverse", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Profile": (10530, 2, (9, 0), (), "Profile", '{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}'),
		"RadiusAddendum": (10517, 2, (9, 0), (), "RadiusAddendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusBase": (10516, 2, (9, 0), (), "RadiusBase", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusDedendum": (10514, 2, (9, 0), (), "RadiusDedendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusPitch": (10515, 2, (9, 0), (), "RadiusPitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusTFlankISO606": (10509, 2, (5, 0), (), "RadiusTFlankISO606", None),
		"RadiusTFlankParameter": (10513, 2, (9, 0), (), "RadiusTFlankParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusWheel": (10503, 2, (9, 0), (), "RadiusWheel", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RollerLinkDiameter": (10525, 2, (5, 0), (), "RollerLinkDiameter", None),
		"RollerLinkPitch": (10524, 2, (5, 0), (), "RollerLinkPitch", None),
		"RollerSeatingAngleISO606": (10521, 2, (5, 0), (), "RollerSeatingAngleISO606", None),
		"RollerSeatingAngleParameter": (10523, 2, (9, 0), (), "RollerSeatingAngleParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RollerSeatingRadiusISO606": (10520, 2, (5, 0), (), "RollerSeatingRadiusISO606", None),
		"RollerSeatingRadiusParameter": (10522, 2, (9, 0), (), "RollerSeatingRadiusParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SprocketType": (10501, 2, (3, 0), (), "SprocketType", '{BE5ED324-09C1-462B-8D26-DB09D5B18BF6}'),
		"UseLinkAssemblyAssembledRadius": (10527, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
		"WidthTeeth": (10502, 2, (9, 0), (), "WidthTeeth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WidthWheels": (10504, 2, (9, 0), (), "WidthWheels", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"ChainLinkRollerCircleRadiusLoop": ((10519, LCID, 4, 0),()),
		"ChainLinkRollerCircleRadiusRoller": ((10518, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LinkAssemblyAssembledRadius": ((10528, LCID, 4, 0),()),
		"LinkAssemblyRadialDistance": ((10529, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NumberOfStrands": ((10551, LCID, 4, 0),()),
		"NumberofTeeth": ((10505, LCID, 4, 0),()),
		"RollerLinkDiameter": ((10525, LCID, 4, 0),()),
		"RollerLinkPitch": ((10524, LCID, 4, 0),()),
		"SprocketType": ((10501, LCID, 4, 0),()),
		"UseLinkAssemblyAssembledRadius": ((10527, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGeometrySprocketRoller(DispatchBaseClass):
	'''Chain Sprocket Roller Body Geometry'''
	CLSID = IID('{71E9EDCA-8586-4BC4-8C96-CA6CE987B7C7}')
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


	def UpdateProperties(self):
		'''
		Update Sprocket Data for Tooth Profile.
		'''
		return self._oleobj_.InvokeTypes(10531, LCID, 1, (24, 0), (),)


	def UpdatefromISO606Lib(self):
		'''
		Update from ISO 606 Lib.
		'''
		return self._oleobj_.InvokeTypes(10526, LCID, 1, (24, 0), (),)


	def _get_ChainLinkRollerCircleRadiusLoop(self):
		return self._ApplyTypes_(*(10519, 2, (5, 0), (), "ChainLinkRollerCircleRadiusLoop", None))
	def _get_ChainLinkRollerCircleRadiusRoller(self):
		return self._ApplyTypes_(*(10518, 2, (5, 0), (), "ChainLinkRollerCircleRadiusRoller", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_DiameterPitchISO606(self):
		return self._ApplyTypes_(*(10506, 2, (5, 0), (), "DiameterPitchISO606", None))
	def _get_DiameterPitchParameter(self):
		return self._ApplyTypes_(*(10510, 2, (9, 0), (), "DiameterPitchParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DiameterRootISO606(self):
		return self._ApplyTypes_(*(10508, 2, (5, 0), (), "DiameterRootISO606", None))
	def _get_DiameterRootParameter(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "DiameterRootParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DiameterTipISO606(self):
		return self._ApplyTypes_(*(10507, 2, (5, 0), (), "DiameterTipISO606", None))
	def _get_DiameterTipParameter(self):
		return self._ApplyTypes_(*(10511, 2, (9, 0), (), "DiameterTipParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(10528, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None))
	def _get_LinkAssemblyRadialDistance(self):
		return self._ApplyTypes_(*(10529, 2, (5, 0), (), "LinkAssemblyRadialDistance", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberofTeeth(self):
		return self._ApplyTypes_(*(10505, 2, (3, 0), (), "NumberofTeeth", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(10530, 2, (9, 0), (), "Profile", '{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}'))
	def _get_RadiusAddendum(self):
		return self._ApplyTypes_(*(10517, 2, (9, 0), (), "RadiusAddendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusBase(self):
		return self._ApplyTypes_(*(10516, 2, (9, 0), (), "RadiusBase", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusDedendum(self):
		return self._ApplyTypes_(*(10514, 2, (9, 0), (), "RadiusDedendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusPitch(self):
		return self._ApplyTypes_(*(10515, 2, (9, 0), (), "RadiusPitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusTFlankISO606(self):
		return self._ApplyTypes_(*(10509, 2, (5, 0), (), "RadiusTFlankISO606", None))
	def _get_RadiusTFlankParameter(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "RadiusTFlankParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusWheel(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "RadiusWheel", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_RollerLinkDiameter(self):
		return self._ApplyTypes_(*(10525, 2, (5, 0), (), "RollerLinkDiameter", None))
	def _get_RollerLinkPitch(self):
		return self._ApplyTypes_(*(10524, 2, (5, 0), (), "RollerLinkPitch", None))
	def _get_RollerSeatingAngleISO606(self):
		return self._ApplyTypes_(*(10521, 2, (5, 0), (), "RollerSeatingAngleISO606", None))
	def _get_RollerSeatingAngleParameter(self):
		return self._ApplyTypes_(*(10523, 2, (9, 0), (), "RollerSeatingAngleParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RollerSeatingRadiusISO606(self):
		return self._ApplyTypes_(*(10520, 2, (5, 0), (), "RollerSeatingRadiusISO606", None))
	def _get_RollerSeatingRadiusParameter(self):
		return self._ApplyTypes_(*(10522, 2, (9, 0), (), "RollerSeatingRadiusParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_SprocketType(self):
		return self._ApplyTypes_(*(10501, 2, (3, 0), (), "SprocketType", '{BE5ED324-09C1-462B-8D26-DB09D5B18BF6}'))
	def _get_UseLinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(10527, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))
	def _get_WidthTeeth(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "WidthTeeth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WidthWheels(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "WidthWheels", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_ChainLinkRollerCircleRadiusLoop(self, value):
		if "ChainLinkRollerCircleRadiusLoop" in self.__dict__: self.__dict__["ChainLinkRollerCircleRadiusLoop"] = value; return
		self._oleobj_.Invoke(*((10519, LCID, 4, 0) + (value,) + ()))
	def _set_ChainLinkRollerCircleRadiusRoller(self, value):
		if "ChainLinkRollerCircleRadiusRoller" in self.__dict__: self.__dict__["ChainLinkRollerCircleRadiusRoller"] = value; return
		self._oleobj_.Invoke(*((10518, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LinkAssemblyAssembledRadius(self, value):
		if "LinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["LinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((10528, LCID, 4, 0) + (value,) + ()))
	def _set_LinkAssemblyRadialDistance(self, value):
		if "LinkAssemblyRadialDistance" in self.__dict__: self.__dict__["LinkAssemblyRadialDistance"] = value; return
		self._oleobj_.Invoke(*((10529, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NumberofTeeth(self, value):
		if "NumberofTeeth" in self.__dict__: self.__dict__["NumberofTeeth"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_RollerLinkDiameter(self, value):
		if "RollerLinkDiameter" in self.__dict__: self.__dict__["RollerLinkDiameter"] = value; return
		self._oleobj_.Invoke(*((10525, LCID, 4, 0) + (value,) + ()))
	def _set_RollerLinkPitch(self, value):
		if "RollerLinkPitch" in self.__dict__: self.__dict__["RollerLinkPitch"] = value; return
		self._oleobj_.Invoke(*((10524, LCID, 4, 0) + (value,) + ()))
	def _set_SprocketType(self, value):
		if "SprocketType" in self.__dict__: self.__dict__["SprocketType"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkAssemblyAssembledRadius(self, value):
		if "UseLinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["UseLinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((10527, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ChainLinkRollerCircleRadiusLoop = property(_get_ChainLinkRollerCircleRadiusLoop, _set_ChainLinkRollerCircleRadiusLoop)
	'''
	Chain Link Roller Circle Loop Radius

	:type: float
	'''
	ChainLinkRollerCircleRadiusRoller = property(_get_ChainLinkRollerCircleRadiusRoller, _set_ChainLinkRollerCircleRadiusRoller)
	'''
	Chain Link Roller Circle Radius

	:type: float
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	DiameterPitchISO606 = property(_get_DiameterPitchISO606, None)
	'''
	Pitch Diameter(D) for ISO 606 Library Type

	:type: float
	'''
	DiameterPitchParameter = property(_get_DiameterPitchParameter, None)
	'''
	Pitch Diameter(D) for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	DiameterRootISO606 = property(_get_DiameterRootISO606, None)
	'''
	Root Diameter(Df) for ISO 606 Library Type

	:type: float
	'''
	DiameterRootParameter = property(_get_DiameterRootParameter, None)
	'''
	Root Diameter(Df) for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	DiameterTipISO606 = property(_get_DiameterTipISO606, None)
	'''
	Tip Diameter(Da) for ISO 606 Library Type

	:type: float
	'''
	DiameterTipParameter = property(_get_DiameterTipParameter, None)
	'''
	Tip Diameter(Da) for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
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
	LinkAssemblyAssembledRadius = property(_get_LinkAssemblyAssembledRadius, _set_LinkAssemblyAssembledRadius)
	'''
	Assembled Radius of the Link Assembly.

	:type: float
	'''
	LinkAssemblyRadialDistance = property(_get_LinkAssemblyRadialDistance, _set_LinkAssemblyRadialDistance)
	'''
	Radial Radius of the Link Assembly.

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NumberofTeeth = property(_get_NumberofTeeth, _set_NumberofTeeth)
	'''
	Number of Teeth

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
	Profile = property(_get_Profile, None)
	'''
	Profile of Sprocket

	:type: recurdyn.TrackLM.ITrackLMToothProfileSprocket
	'''
	RadiusAddendum = property(_get_RadiusAddendum, None)
	'''
	Addendum Radius

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusBase = property(_get_RadiusBase, None)
	'''
	Base Radius(Rb)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusDedendum = property(_get_RadiusDedendum, None)
	'''
	Dedendum Radius(Rd)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusPitch = property(_get_RadiusPitch, None)
	'''
	Pitch Radius(Rp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusTFlankISO606 = property(_get_RadiusTFlankISO606, None)
	'''
	T-Flank Radius(Re) for ISO 606 Library Type

	:type: float
	'''
	RadiusTFlankParameter = property(_get_RadiusTFlankParameter, None)
	'''
	T-Flank Radius(Re) for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusWheel = property(_get_RadiusWheel, None)
	'''
	Radius Wheel(Rw)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	RollerLinkDiameter = property(_get_RollerLinkDiameter, _set_RollerLinkDiameter)
	'''
	Roller Link Diameter(D1)

	:type: float
	'''
	RollerLinkPitch = property(_get_RollerLinkPitch, _set_RollerLinkPitch)
	'''
	Roller Link Pitch(P)

	:type: float
	'''
	RollerSeatingAngleISO606 = property(_get_RollerSeatingAngleISO606, None)
	'''
	Roller Seating Angle for ISO 606 Library Type

	:type: float
	'''
	RollerSeatingAngleParameter = property(_get_RollerSeatingAngleParameter, None)
	'''
	Roller Seating Angle for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	RollerSeatingRadiusISO606 = property(_get_RollerSeatingRadiusISO606, None)
	'''
	Roller Seating Radius for ISO 606 Library Type

	:type: float
	'''
	RollerSeatingRadiusParameter = property(_get_RollerSeatingRadiusParameter, None)
	'''
	Roller Seating Radius for Parameters Type

	:type: recurdyn.ProcessNet.IDouble
	'''
	SprocketType = property(_get_SprocketType, _set_SprocketType)
	'''
	Sprocket Type

	:type: recurdyn.Chain.ChainSprocketType
	'''
	UseLinkAssemblyAssembledRadius = property(_get_UseLinkAssemblyAssembledRadius, _set_UseLinkAssemblyAssembledRadius)
	'''
	Use Assembled Radius.

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)
	WidthTeeth = property(_get_WidthTeeth, None)
	'''
	Width Teeth(Wt)

	:type: recurdyn.ProcessNet.IDouble
	'''
	WidthWheels = property(_get_WidthWheels, None)
	'''
	Width Wheels(Ww)

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_ChainLinkRollerCircleRadiusLoop": _set_ChainLinkRollerCircleRadiusLoop,
		"_set_ChainLinkRollerCircleRadiusRoller": _set_ChainLinkRollerCircleRadiusRoller,
		"_set_Comment": _set_Comment,
		"_set_LinkAssemblyAssembledRadius": _set_LinkAssemblyAssembledRadius,
		"_set_LinkAssemblyRadialDistance": _set_LinkAssemblyRadialDistance,
		"_set_Name": _set_Name,
		"_set_NumberofTeeth": _set_NumberofTeeth,
		"_set_RollerLinkDiameter": _set_RollerLinkDiameter,
		"_set_RollerLinkPitch": _set_RollerLinkPitch,
		"_set_SprocketType": _set_SprocketType,
		"_set_UseLinkAssemblyAssembledRadius": _set_UseLinkAssemblyAssembledRadius,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ChainLinkRollerCircleRadiusLoop": (10519, 2, (5, 0), (), "ChainLinkRollerCircleRadiusLoop", None),
		"ChainLinkRollerCircleRadiusRoller": (10518, 2, (5, 0), (), "ChainLinkRollerCircleRadiusRoller", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"DiameterPitchISO606": (10506, 2, (5, 0), (), "DiameterPitchISO606", None),
		"DiameterPitchParameter": (10510, 2, (9, 0), (), "DiameterPitchParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DiameterRootISO606": (10508, 2, (5, 0), (), "DiameterRootISO606", None),
		"DiameterRootParameter": (10512, 2, (9, 0), (), "DiameterRootParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DiameterTipISO606": (10507, 2, (5, 0), (), "DiameterTipISO606", None),
		"DiameterTipParameter": (10511, 2, (9, 0), (), "DiameterTipParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LinkAssemblyAssembledRadius": (10528, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None),
		"LinkAssemblyRadialDistance": (10529, 2, (5, 0), (), "LinkAssemblyRadialDistance", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberofTeeth": (10505, 2, (3, 0), (), "NumberofTeeth", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Profile": (10530, 2, (9, 0), (), "Profile", '{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}'),
		"RadiusAddendum": (10517, 2, (9, 0), (), "RadiusAddendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusBase": (10516, 2, (9, 0), (), "RadiusBase", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusDedendum": (10514, 2, (9, 0), (), "RadiusDedendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusPitch": (10515, 2, (9, 0), (), "RadiusPitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusTFlankISO606": (10509, 2, (5, 0), (), "RadiusTFlankISO606", None),
		"RadiusTFlankParameter": (10513, 2, (9, 0), (), "RadiusTFlankParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusWheel": (10503, 2, (9, 0), (), "RadiusWheel", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"RollerLinkDiameter": (10525, 2, (5, 0), (), "RollerLinkDiameter", None),
		"RollerLinkPitch": (10524, 2, (5, 0), (), "RollerLinkPitch", None),
		"RollerSeatingAngleISO606": (10521, 2, (5, 0), (), "RollerSeatingAngleISO606", None),
		"RollerSeatingAngleParameter": (10523, 2, (9, 0), (), "RollerSeatingAngleParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RollerSeatingRadiusISO606": (10520, 2, (5, 0), (), "RollerSeatingRadiusISO606", None),
		"RollerSeatingRadiusParameter": (10522, 2, (9, 0), (), "RollerSeatingRadiusParameter", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"SprocketType": (10501, 2, (3, 0), (), "SprocketType", '{BE5ED324-09C1-462B-8D26-DB09D5B18BF6}'),
		"UseLinkAssemblyAssembledRadius": (10527, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
		"WidthTeeth": (10502, 2, (9, 0), (), "WidthTeeth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WidthWheels": (10504, 2, (9, 0), (), "WidthWheels", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"ChainLinkRollerCircleRadiusLoop": ((10519, LCID, 4, 0),()),
		"ChainLinkRollerCircleRadiusRoller": ((10518, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LinkAssemblyAssembledRadius": ((10528, LCID, 4, 0),()),
		"LinkAssemblyRadialDistance": ((10529, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NumberofTeeth": ((10505, LCID, 4, 0),()),
		"RollerLinkDiameter": ((10525, LCID, 4, 0),()),
		"RollerLinkPitch": ((10524, LCID, 4, 0),()),
		"SprocketType": ((10501, LCID, 4, 0),()),
		"UseLinkAssemblyAssembledRadius": ((10527, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGeometrySprocketSilent(DispatchBaseClass):
	'''Chain Sprocket Silent Body Geometry'''
	CLSID = IID('{46136858-6824-49C4-A14E-EC6C582E3C6D}')
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


	def UpdateProperties(self):
		'''
		Update Sprocket Data for Tooth Profile.
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), (),)


	def _get_ChainLinkPinCircleRadiusLoop(self):
		return self._ApplyTypes_(*(10510, 2, (5, 0), (), "ChainLinkPinCircleRadiusLoop", None))
	def _get_ChainLinkPinCircleRadiusPin(self):
		return self._ApplyTypes_(*(10509, 2, (5, 0), (), "ChainLinkPinCircleRadiusPin", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'))
	def _get_LinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(10512, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None))
	def _get_LinkAssemblyRadialDistance(self):
		return self._ApplyTypes_(*(10513, 2, (5, 0), (), "LinkAssemblyRadialDistance", None))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_NumberofTeeth(self):
		return self._ApplyTypes_(*(10504, 2, (3, 0), (), "NumberofTeeth", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(10514, 2, (9, 0), (), "Profile", '{BD4851C8-8A99-4B29-80AE-2E160DC0754C}'))
	def _get_RadiusCircleAddendum(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "RadiusCircleAddendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusCircleBase(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "RadiusCircleBase", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusCircleDedendum(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "RadiusCircleDedendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusCirclePitch(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "RadiusCirclePitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RadiusWheelSprocket(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "RadiusWheelSprocket", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_RefFrame(self):
		return self._ApplyTypes_(*(151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'))
	def _get_UseLinkAssemblyAssembledRadius(self):
		return self._ApplyTypes_(*(10511, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))
	def _get_VertexCollection(self):
		return self._ApplyTypes_(*(155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'))
	def _get_WidthbetweenWheels(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "WidthbetweenWheels", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_WidthofTeeth(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "WidthofTeeth", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	def _set_ChainLinkPinCircleRadiusLoop(self, value):
		if "ChainLinkPinCircleRadiusLoop" in self.__dict__: self.__dict__["ChainLinkPinCircleRadiusLoop"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_ChainLinkPinCircleRadiusPin(self, value):
		if "ChainLinkPinCircleRadiusPin" in self.__dict__: self.__dict__["ChainLinkPinCircleRadiusPin"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_LinkAssemblyAssembledRadius(self, value):
		if "LinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["LinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
	def _set_LinkAssemblyRadialDistance(self, value):
		if "LinkAssemblyRadialDistance" in self.__dict__: self.__dict__["LinkAssemblyRadialDistance"] = value; return
		self._oleobj_.Invoke(*((10513, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_NumberofTeeth(self, value):
		if "NumberofTeeth" in self.__dict__: self.__dict__["NumberofTeeth"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))
	def _set_UseLinkAssemblyAssembledRadius(self, value):
		if "UseLinkAssemblyAssembledRadius" in self.__dict__: self.__dict__["UseLinkAssemblyAssembledRadius"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_UserData(self, value):
		if "UserData" in self.__dict__: self.__dict__["UserData"] = value; return
		self._oleobj_.Invoke(*((107, LCID, 4, 0) + (value,) + ()))

	ChainLinkPinCircleRadiusLoop = property(_get_ChainLinkPinCircleRadiusLoop, _set_ChainLinkPinCircleRadiusLoop)
	'''
	Chain Link Pin Circle Radius Loop

	:type: float
	'''
	ChainLinkPinCircleRadiusPin = property(_get_ChainLinkPinCircleRadiusPin, _set_ChainLinkPinCircleRadiusPin)
	'''
	Chain Link Pin Circle Radius Pin

	:type: float
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
	LinkAssemblyAssembledRadius = property(_get_LinkAssemblyAssembledRadius, _set_LinkAssemblyAssembledRadius)
	'''
	Assembled Radius of the Link Assembly.

	:type: float
	'''
	LinkAssemblyRadialDistance = property(_get_LinkAssemblyRadialDistance, _set_LinkAssemblyRadialDistance)
	'''
	Radial Radius of the Link Assembly.

	:type: float
	'''
	Name = property(_get_Name, _set_Name)
	'''
	Name

	:type: str
	'''
	NumberofTeeth = property(_get_NumberofTeeth, _set_NumberofTeeth)
	'''
	Number of Teeth

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
	Profile = property(_get_Profile, None)
	'''
	Profile of Sprocket

	:type: recurdyn.Chain.IChainProfileSprocket2
	'''
	RadiusCircleAddendum = property(_get_RadiusCircleAddendum, None)
	'''
	Addendum Circle Radius(Ra)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusCircleBase = property(_get_RadiusCircleBase, None)
	'''
	Base Circle Radius(Rb)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusCircleDedendum = property(_get_RadiusCircleDedendum, None)
	'''
	Dedendum Circle Radius(Rd)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusCirclePitch = property(_get_RadiusCirclePitch, None)
	'''
	Pitch Circle Radius(Rp)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RadiusWheelSprocket = property(_get_RadiusWheelSprocket, None)
	'''
	Sprocket Wheel Radius(Rw)

	:type: recurdyn.ProcessNet.IDouble
	'''
	RefFrame = property(_get_RefFrame, None)
	'''
	Reference frame

	:type: recurdyn.ProcessNet.IReferenceFrame
	'''
	UseLinkAssemblyAssembledRadius = property(_get_UseLinkAssemblyAssembledRadius, _set_UseLinkAssemblyAssembledRadius)
	'''
	Use Assembled Radius.

	:type: bool
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''
	VertexCollection = property(_get_VertexCollection, None)
	WidthbetweenWheels = property(_get_WidthbetweenWheels, None)
	'''
	Width between Wheels(Ww)

	:type: recurdyn.ProcessNet.IDouble
	'''
	WidthofTeeth = property(_get_WidthofTeeth, None)
	'''
	Width of Teeth(Wt)

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
		"_set_ChainLinkPinCircleRadiusLoop": _set_ChainLinkPinCircleRadiusLoop,
		"_set_ChainLinkPinCircleRadiusPin": _set_ChainLinkPinCircleRadiusPin,
		"_set_Comment": _set_Comment,
		"_set_LinkAssemblyAssembledRadius": _set_LinkAssemblyAssembledRadius,
		"_set_LinkAssemblyRadialDistance": _set_LinkAssemblyRadialDistance,
		"_set_Name": _set_Name,
		"_set_NumberofTeeth": _set_NumberofTeeth,
		"_set_UseLinkAssemblyAssembledRadius": _set_UseLinkAssemblyAssembledRadius,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"ChainLinkPinCircleRadiusLoop": (10510, 2, (5, 0), (), "ChainLinkPinCircleRadiusLoop", None),
		"ChainLinkPinCircleRadiusPin": (10509, 2, (5, 0), (), "ChainLinkPinCircleRadiusPin", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (153, 2, (9, 0), (), "Graphic", '{E4CA4A74-65F0-4528-B4C4-420B7C3ECB25}'),
		"LinkAssemblyAssembledRadius": (10512, 2, (5, 0), (), "LinkAssemblyAssembledRadius", None),
		"LinkAssemblyRadialDistance": (10513, 2, (5, 0), (), "LinkAssemblyRadialDistance", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"NumberofTeeth": (10504, 2, (3, 0), (), "NumberofTeeth", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Profile": (10514, 2, (9, 0), (), "Profile", '{BD4851C8-8A99-4B29-80AE-2E160DC0754C}'),
		"RadiusCircleAddendum": (10508, 2, (9, 0), (), "RadiusCircleAddendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusCircleBase": (10506, 2, (9, 0), (), "RadiusCircleBase", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusCircleDedendum": (10505, 2, (9, 0), (), "RadiusCircleDedendum", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusCirclePitch": (10507, 2, (9, 0), (), "RadiusCirclePitch", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RadiusWheelSprocket": (10501, 2, (9, 0), (), "RadiusWheelSprocket", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"RefFrame": (151, 2, (9, 0), (), "RefFrame", '{6A3295D9-E76B-473C-9655-23B7B1CBD671}'),
		"UseLinkAssemblyAssembledRadius": (10511, 2, (11, 0), (), "UseLinkAssemblyAssembledRadius", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
		"VertexCollection": (155, 2, (9, 0), (), "VertexCollection", '{BD9F9B20-94B2-4BC3-BB29-0CE3F2B9ADED}'),
		"WidthbetweenWheels": (10503, 2, (9, 0), (), "WidthbetweenWheels", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"WidthofTeeth": (10502, 2, (9, 0), (), "WidthofTeeth", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
	}
	_prop_map_put_ = {
		"ChainLinkPinCircleRadiusLoop": ((10510, LCID, 4, 0),()),
		"ChainLinkPinCircleRadiusPin": ((10509, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"LinkAssemblyAssembledRadius": ((10512, LCID, 4, 0),()),
		"LinkAssemblyRadialDistance": ((10513, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"NumberofTeeth": ((10504, LCID, 4, 0),()),
		"UseLinkAssemblyAssembledRadius": ((10511, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGroupGuideArc(DispatchBaseClass):
	'''Chain Group Guide Arc Clone'''
	CLSID = IID('{037DA049-C1EB-4F0B-8457-80FE60733754}')
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


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10511, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(152, 2, (11, 0), (), "Active", None))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_ContactProperty(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "ContactProperty", '{1E51E4E8-E4DC-4C00-BBCB-816315723567}'))
	def _get_EachRenderMode(self):
		return self._ApplyTypes_(*(203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'))
	def _get_ForceDisplay(self):
		return self._ApplyTypes_(*(10502, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Geometry", '{B0B8CBCE-6E48-4300-9436-0599707E3C93}'))
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
	def _get_TotalMass(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_UseAutoUpdateGeometry(self):
		return self._ApplyTypes_(*(10505, 2, (11, 0), (), "UseAutoUpdateGeometry", None))
	def _get_UseTotalMass(self):
		return self._ApplyTypes_(*(10503, 2, (11, 0), (), "UseTotalMass", None))
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
	def _set_ForceDisplay(self, value):
		if "ForceDisplay" in self.__dict__: self.__dict__["ForceDisplay"] = value; return
		self._oleobj_.Invoke(*((10502, LCID, 4, 0) + (value,) + ()))
	def _set_LayerNumber(self, value):
		if "LayerNumber" in self.__dict__: self.__dict__["LayerNumber"] = value; return
		self._oleobj_.Invoke(*((151, LCID, 4, 0) + (value,) + ()))
	def _set_Name(self, value):
		if "Name" in self.__dict__: self.__dict__["Name"] = value; return
		self._oleobj_.Invoke(*((101, LCID, 4, 0) + (value,) + ()))
	def _set_UseAutoUpdateGeometry(self, value):
		if "UseAutoUpdateGeometry" in self.__dict__: self.__dict__["UseAutoUpdateGeometry"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_UseTotalMass(self, value):
		if "UseTotalMass" in self.__dict__: self.__dict__["UseTotalMass"] = value; return
		self._oleobj_.Invoke(*((10503, LCID, 4, 0) + (value,) + ()))
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
	ContactProperty = property(_get_ContactProperty, None)
	'''
	Contact Property

	:type: recurdyn.Chain.IChainGuideContactProperty
	'''
	EachRenderMode = property(_get_EachRenderMode, _set_EachRenderMode)
	'''
	Rendering mode

	:type: recurdyn.ProcessNet.EachRenderMode
	'''
	ForceDisplay = property(_get_ForceDisplay, _set_ForceDisplay)
	'''
	Force display

	:type: recurdyn.ProcessNet.ForceDisplay
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryGroupGuideArc
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
	TotalMass = property(_get_TotalMass, None)
	'''
	Total mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	UseAutoUpdateGeometry = property(_get_UseAutoUpdateGeometry, _set_UseAutoUpdateGeometry)
	'''
	Use Update Geometry Automatically

	:type: bool
	'''
	UseTotalMass = property(_get_UseTotalMass, _set_UseTotalMass)
	'''
	Use total mass

	:type: bool
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
		"_set_ForceDisplay": _set_ForceDisplay,
		"_set_LayerNumber": _set_LayerNumber,
		"_set_Name": _set_Name,
		"_set_UseAutoUpdateGeometry": _set_UseAutoUpdateGeometry,
		"_set_UseTotalMass": _set_UseTotalMass,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (152, 2, (11, 0), (), "Active", None),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"ContactProperty": (10500, 2, (9, 0), (), "ContactProperty", '{1E51E4E8-E4DC-4C00-BBCB-816315723567}'),
		"EachRenderMode": (203, 2, (3, 0), (), "EachRenderMode", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147EC}'),
		"ForceDisplay": (10502, 2, (3, 0), (), "ForceDisplay", '{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}'),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (10501, 2, (9, 0), (), "Geometry", '{B0B8CBCE-6E48-4300-9436-0599707E3C93}'),
		"LayerNumber": (151, 2, (19, 0), (), "LayerNumber", None),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"TotalMass": (10504, 2, (9, 0), (), "TotalMass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"UseAutoUpdateGeometry": (10505, 2, (11, 0), (), "UseAutoUpdateGeometry", None),
		"UseTotalMass": (10503, 2, (11, 0), (), "UseTotalMass", None),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((152, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"EachRenderMode": ((203, LCID, 4, 0),()),
		"ForceDisplay": ((10502, LCID, 4, 0),()),
		"LayerNumber": ((151, LCID, 4, 0),()),
		"Name": ((101, LCID, 4, 0),()),
		"UseAutoUpdateGeometry": ((10505, LCID, 4, 0),()),
		"UseTotalMass": ((10503, LCID, 4, 0),()),
		"UserData": ((107, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGroupGuidePointsWithAdditionalInfo(DispatchBaseClass):
	'''IChainGroupGuidePointsWithAdditionalInfo'''
	CLSID = IID('{0954FD4A-BE83-4A47-A022-39343EABBB1B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AdditionalInfo(self):
		return self._ApplyTypes_(*(10504, 2, (5, 0), (), "AdditionalInfo", None))
	def _get_x(self):
		return self._ApplyTypes_(*(10501, 2, (5, 0), (), "x", None))
	def _get_y(self):
		return self._ApplyTypes_(*(10502, 2, (5, 0), (), "y", None))
	def _get_z(self):
		return self._ApplyTypes_(*(10503, 2, (5, 0), (), "z", None))

	def _set_AdditionalInfo(self, value):
		if "AdditionalInfo" in self.__dict__: self.__dict__["AdditionalInfo"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))
	def _set_x(self, value):
		if "x" in self.__dict__: self.__dict__["x"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
	def _set_y(self, value):
		if "y" in self.__dict__: self.__dict__["y"] = value; return
		self._oleobj_.Invoke(*((10502, LCID, 4, 0) + (value,) + ()))
	def _set_z(self, value):
		if "z" in self.__dict__: self.__dict__["z"] = value; return
		self._oleobj_.Invoke(*((10503, LCID, 4, 0) + (value,) + ()))

	AdditionalInfo = property(_get_AdditionalInfo, _set_AdditionalInfo)
	'''
	Additional Info

	:type: float
	'''
	x = property(_get_x, _set_x)
	'''
	Point x

	:type: float
	'''
	y = property(_get_y, _set_y)
	'''
	Point y

	:type: float
	'''
	z = property(_get_z, _set_z)
	'''
	Point z

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_AdditionalInfo": _set_AdditionalInfo,
		"_set_x": _set_x,
		"_set_y": _set_y,
		"_set_z": _set_z,
	}
	_prop_map_get_ = {
		"AdditionalInfo": (10504, 2, (5, 0), (), "AdditionalInfo", None),
		"x": (10501, 2, (5, 0), (), "x", None),
		"y": (10502, 2, (5, 0), (), "y", None),
		"z": (10503, 2, (5, 0), (), "z", None),
	}
	_prop_map_put_ = {
		"AdditionalInfo": ((10504, LCID, 4, 0),()),
		"x": ((10501, LCID, 4, 0),()),
		"y": ((10502, LCID, 4, 0),()),
		"z": ((10503, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGroupGuidePointsWithAdditionalInfoCollection(DispatchBaseClass):
	'''IChainGroupGuidePointsWithAdditionalInfo Collection'''
	CLSID = IID('{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}')
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
		:rtype: recurdyn.Chain.IChainGroupGuidePointsWithAdditionalInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{0954FD4A-BE83-4A47-A022-39343EABBB1B}')
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
		:rtype: recurdyn.Chain.IChainGroupGuidePointsWithAdditionalInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{0954FD4A-BE83-4A47-A022-39343EABBB1B}')
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
		return win32com.client.util.Iterator(ob, '{0954FD4A-BE83-4A47-A022-39343EABBB1B}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{0954FD4A-BE83-4A47-A022-39343EABBB1B}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IChainGuideContactProperty(DispatchBaseClass):
	'''Chain Guide Contact Property'''
	CLSID = IID('{1E51E4E8-E4DC-4C00-BBCB-816315723567}')
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
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingExponent(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_DampingSpline(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_Friction(self):
		return self._ApplyTypes_(*(10516, 2, (9, 0), (), "Friction", '{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}'))
	def _get_FrictionCoefficient(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_FrictionSpline(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_FrictionType(self):
		return self._ApplyTypes_(*(10506, 2, (3, 0), (), "FrictionType", '{6A354324-DD66-4599-9FB4-13728425522F}'))
	def _get_IndentationExponent(self):
		return self._ApplyTypes_(*(10514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_NumberofMaxContactPoints(self):
		return self._ApplyTypes_(*(10551, 2, (3, 0), (), "NumberofMaxContactPoints", None))
	def _get_StiffnessCoefficient(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessExponent(self):
		return self._ApplyTypes_(*(10510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_StiffnessSpline(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'))
	def _get_UseDampingExponent(self):
		return self._ApplyTypes_(*(10511, 2, (11, 0), (), "UseDampingExponent", None))
	def _get_UseDampingSpline(self):
		return self._ApplyTypes_(*(10504, 2, (11, 0), (), "UseDampingSpline", None))
	def _get_UseIndentationExponent(self):
		return self._ApplyTypes_(*(10513, 2, (11, 0), (), "UseIndentationExponent", None))
	def _get_UseMoreFrictionData(self):
		return self._ApplyTypes_(*(10515, 2, (11, 0), (), "UseMoreFrictionData", None))
	def _get_UseStiffnessExponent(self):
		return self._ApplyTypes_(*(10509, 2, (11, 0), (), "UseStiffnessExponent", None))
	def _get_UseStiffnessSpline(self):
		return self._ApplyTypes_(*(10501, 2, (11, 0), (), "UseStiffnessSpline", None))

	def _set_DampingSpline(self, value):
		if "DampingSpline" in self.__dict__: self.__dict__["DampingSpline"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionSpline(self, value):
		if "FrictionSpline" in self.__dict__: self.__dict__["FrictionSpline"] = value; return
		self._oleobj_.Invoke(*((10508, LCID, 4, 0) + (value,) + ()))
	def _set_FrictionType(self, value):
		if "FrictionType" in self.__dict__: self.__dict__["FrictionType"] = value; return
		self._oleobj_.Invoke(*((10506, LCID, 4, 0) + (value,) + ()))
	def _set_NumberofMaxContactPoints(self, value):
		if "NumberofMaxContactPoints" in self.__dict__: self.__dict__["NumberofMaxContactPoints"] = value; return
		self._oleobj_.Invoke(*((10551, LCID, 4, 0) + (value,) + ()))
	def _set_StiffnessSpline(self, value):
		if "StiffnessSpline" in self.__dict__: self.__dict__["StiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10502, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingExponent(self, value):
		if "UseDampingExponent" in self.__dict__: self.__dict__["UseDampingExponent"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_UseDampingSpline(self, value):
		if "UseDampingSpline" in self.__dict__: self.__dict__["UseDampingSpline"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))
	def _set_UseIndentationExponent(self, value):
		if "UseIndentationExponent" in self.__dict__: self.__dict__["UseIndentationExponent"] = value; return
		self._oleobj_.Invoke(*((10513, LCID, 4, 0) + (value,) + ()))
	def _set_UseMoreFrictionData(self, value):
		if "UseMoreFrictionData" in self.__dict__: self.__dict__["UseMoreFrictionData"] = value; return
		self._oleobj_.Invoke(*((10515, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessExponent(self, value):
		if "UseStiffnessExponent" in self.__dict__: self.__dict__["UseStiffnessExponent"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_UseStiffnessSpline(self, value):
		if "UseStiffnessSpline" in self.__dict__: self.__dict__["UseStiffnessSpline"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))

	DampingCoefficient = property(_get_DampingCoefficient, None)
	'''
	The Viscous Damping Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingExponent = property(_get_DampingExponent, None)
	'''
	The Damping Exponent for a Non-linear Contact Normal Force

	:type: recurdyn.ProcessNet.IDouble
	'''
	DampingSpline = property(_get_DampingSpline, _set_DampingSpline)
	'''
	Damping Spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	Friction = property(_get_Friction, None)
	'''
	Friction

	:type: recurdyn.Chain.IChainContactFriction
	'''
	FrictionCoefficient = property(_get_FrictionCoefficient, None)
	'''
	The Friction Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	FrictionSpline = property(_get_FrictionSpline, _set_FrictionSpline)
	'''
	The Spline which Shows Relative Velocity to the Friction Coefficient or the Friction Force.

	:type: recurdyn.ProcessNet.ISpline
	'''
	FrictionType = property(_get_FrictionType, _set_FrictionType)
	'''
	Friction Type

	:type: recurdyn.Chain.ChainFrictionType
	'''
	IndentationExponent = property(_get_IndentationExponent, None)
	'''
	The Indentation Exponent Yields an Indentation Damping Effect.

	:type: recurdyn.ProcessNet.IDouble
	'''
	NumberofMaxContactPoints = property(_get_NumberofMaxContactPoints, _set_NumberofMaxContactPoints)
	'''
	Number of Max Contact Points

	:type: int
	'''
	StiffnessCoefficient = property(_get_StiffnessCoefficient, None)
	'''
	The Stiffness Coefficient for the Contact Normal Force.

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessExponent = property(_get_StiffnessExponent, None)
	'''
	The Stiffness Exponent for a Non-linear Contact Normal Force

	:type: recurdyn.ProcessNet.IDouble
	'''
	StiffnessSpline = property(_get_StiffnessSpline, _set_StiffnessSpline)
	'''
	Stiffness Spline

	:type: recurdyn.ProcessNet.ISpline
	'''
	UseDampingExponent = property(_get_UseDampingExponent, _set_UseDampingExponent)
	'''
	Use Damping Exponent

	:type: bool
	'''
	UseDampingSpline = property(_get_UseDampingSpline, _set_UseDampingSpline)
	'''
	Use Damping Spline

	:type: bool
	'''
	UseIndentationExponent = property(_get_UseIndentationExponent, _set_UseIndentationExponent)
	'''
	Use Indentation Exponent

	:type: bool
	'''
	UseMoreFrictionData = property(_get_UseMoreFrictionData, _set_UseMoreFrictionData)
	'''
	Contact Friction Type

	:type: bool
	'''
	UseStiffnessExponent = property(_get_UseStiffnessExponent, _set_UseStiffnessExponent)
	'''
	Use Stiffness Exponent

	:type: bool
	'''
	UseStiffnessSpline = property(_get_UseStiffnessSpline, _set_UseStiffnessSpline)
	'''
	Use Stiffness Spline

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_DampingSpline": _set_DampingSpline,
		"_set_FrictionSpline": _set_FrictionSpline,
		"_set_FrictionType": _set_FrictionType,
		"_set_NumberofMaxContactPoints": _set_NumberofMaxContactPoints,
		"_set_StiffnessSpline": _set_StiffnessSpline,
		"_set_UseDampingExponent": _set_UseDampingExponent,
		"_set_UseDampingSpline": _set_UseDampingSpline,
		"_set_UseIndentationExponent": _set_UseIndentationExponent,
		"_set_UseMoreFrictionData": _set_UseMoreFrictionData,
		"_set_UseStiffnessExponent": _set_UseStiffnessExponent,
		"_set_UseStiffnessSpline": _set_UseStiffnessSpline,
	}
	_prop_map_get_ = {
		"DampingCoefficient": (10503, 2, (9, 0), (), "DampingCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingExponent": (10512, 2, (9, 0), (), "DampingExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"DampingSpline": (10505, 2, (9, 0), (), "DampingSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"Friction": (10516, 2, (9, 0), (), "Friction", '{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}'),
		"FrictionCoefficient": (10507, 2, (9, 0), (), "FrictionCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"FrictionSpline": (10508, 2, (9, 0), (), "FrictionSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"FrictionType": (10506, 2, (3, 0), (), "FrictionType", '{6A354324-DD66-4599-9FB4-13728425522F}'),
		"IndentationExponent": (10514, 2, (9, 0), (), "IndentationExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"NumberofMaxContactPoints": (10551, 2, (3, 0), (), "NumberofMaxContactPoints", None),
		"StiffnessCoefficient": (10500, 2, (9, 0), (), "StiffnessCoefficient", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessExponent": (10510, 2, (9, 0), (), "StiffnessExponent", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"StiffnessSpline": (10502, 2, (9, 0), (), "StiffnessSpline", '{E76144D2-715D-41B4-A432-7B6C7F713FC2}'),
		"UseDampingExponent": (10511, 2, (11, 0), (), "UseDampingExponent", None),
		"UseDampingSpline": (10504, 2, (11, 0), (), "UseDampingSpline", None),
		"UseIndentationExponent": (10513, 2, (11, 0), (), "UseIndentationExponent", None),
		"UseMoreFrictionData": (10515, 2, (11, 0), (), "UseMoreFrictionData", None),
		"UseStiffnessExponent": (10509, 2, (11, 0), (), "UseStiffnessExponent", None),
		"UseStiffnessSpline": (10501, 2, (11, 0), (), "UseStiffnessSpline", None),
	}
	_prop_map_put_ = {
		"DampingSpline": ((10505, LCID, 4, 0),()),
		"FrictionSpline": ((10508, LCID, 4, 0),()),
		"FrictionType": ((10506, LCID, 4, 0),()),
		"NumberofMaxContactPoints": ((10551, LCID, 4, 0),()),
		"StiffnessSpline": ((10502, LCID, 4, 0),()),
		"UseDampingExponent": ((10511, LCID, 4, 0),()),
		"UseDampingSpline": ((10504, LCID, 4, 0),()),
		"UseIndentationExponent": ((10513, LCID, 4, 0),()),
		"UseMoreFrictionData": ((10515, LCID, 4, 0),()),
		"UseStiffnessExponent": ((10509, LCID, 4, 0),()),
		"UseStiffnessSpline": ((10501, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGuidePointsWithAdditionalInfo(DispatchBaseClass):
	'''IChainGuidePointsWithAdditionalInfo'''
	CLSID = IID('{B512AC12-46CE-4A35-B10B-1A83C7C91457}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AdditionalInfo(self):
		return self._ApplyTypes_(*(10504, 2, (5, 0), (), "AdditionalInfo", None))
	def _get_x(self):
		return self._ApplyTypes_(*(10501, 2, (5, 0), (), "x", None))
	def _get_y(self):
		return self._ApplyTypes_(*(10502, 2, (5, 0), (), "y", None))
	def _get_z(self):
		return self._ApplyTypes_(*(10503, 2, (5, 0), (), "z", None))

	def _set_AdditionalInfo(self, value):
		if "AdditionalInfo" in self.__dict__: self.__dict__["AdditionalInfo"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))
	def _set_x(self, value):
		if "x" in self.__dict__: self.__dict__["x"] = value; return
		self._oleobj_.Invoke(*((10501, LCID, 4, 0) + (value,) + ()))
	def _set_y(self, value):
		if "y" in self.__dict__: self.__dict__["y"] = value; return
		self._oleobj_.Invoke(*((10502, LCID, 4, 0) + (value,) + ()))
	def _set_z(self, value):
		if "z" in self.__dict__: self.__dict__["z"] = value; return
		self._oleobj_.Invoke(*((10503, LCID, 4, 0) + (value,) + ()))

	AdditionalInfo = property(_get_AdditionalInfo, _set_AdditionalInfo)
	'''
	Additional Info

	:type: float
	'''
	x = property(_get_x, _set_x)
	'''
	Point x

	:type: float
	'''
	y = property(_get_y, _set_y)
	'''
	Point y

	:type: float
	'''
	z = property(_get_z, _set_z)
	'''
	Point z

	:type: float
	'''

	_prop_map_set_function_ = {
		"_set_AdditionalInfo": _set_AdditionalInfo,
		"_set_x": _set_x,
		"_set_y": _set_y,
		"_set_z": _set_z,
	}
	_prop_map_get_ = {
		"AdditionalInfo": (10504, 2, (5, 0), (), "AdditionalInfo", None),
		"x": (10501, 2, (5, 0), (), "x", None),
		"y": (10502, 2, (5, 0), (), "y", None),
		"z": (10503, 2, (5, 0), (), "z", None),
	}
	_prop_map_put_ = {
		"AdditionalInfo": ((10504, LCID, 4, 0),()),
		"x": ((10501, LCID, 4, 0),()),
		"y": ((10502, LCID, 4, 0),()),
		"z": ((10503, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainGuidePointsWithAdditionalInfoCollection(DispatchBaseClass):
	'''IChainGuidePointsWithAdditionalInfo Collection'''
	CLSID = IID('{E6353564-8957-4E10-8A7B-12F98C5ECCFB}')
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
		:rtype: recurdyn.Chain.IChainGuidePointsWithAdditionalInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{B512AC12-46CE-4A35-B10B-1A83C7C91457}')
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
		:rtype: recurdyn.Chain.IChainGuidePointsWithAdditionalInfo
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{B512AC12-46CE-4A35-B10B-1A83C7C91457}')
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
		return win32com.client.util.Iterator(ob, '{B512AC12-46CE-4A35-B10B-1A83C7C91457}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{B512AC12-46CE-4A35-B10B-1A83C7C91457}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IChainInvoluteCurveParameter(DispatchBaseClass):
	'''Chain Contact Search'''
	CLSID = IID('{E56F87E6-1157-4D4A-9F6A-D66FFE9C2C0D}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_Phi1(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Phi1", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Phi2(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Phi2", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Theta(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Theta", '{2B5166E3-4B31-4607-B157-BE237A670336}'))

	Phi1 = property(_get_Phi1, None)
	'''
	Phi1

	:type: recurdyn.ProcessNet.IDouble
	'''
	Phi2 = property(_get_Phi2, None)
	'''
	Phi2

	:type: recurdyn.ProcessNet.IDouble
	'''
	Theta = property(_get_Theta, None)
	'''
	Theta

	:type: recurdyn.ProcessNet.IDouble
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"Phi1": (10502, 2, (9, 0), (), "Phi1", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Phi2": (10503, 2, (9, 0), (), "Phi2", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Theta": (10501, 2, (9, 0), (), "Theta", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
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

class IChainLinkClone(DispatchBaseClass):
	'''Chain Link Clone'''
	CLSID = IID('{3C283940-AAB3-48D1-A521-D8AA43058BC2}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(10516, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(10511, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
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
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (10517, 2, (11, 0), (), "Active", None),
		"CenterMarker": (10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (10511, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((10517, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((10511, LCID, 4, 0),()),
		"Material": ((10510, LCID, 4, 0),()),
		"MaterialInput": ((10509, LCID, 4, 0),()),
		"MaterialUser": ((10512, LCID, 4, 0),()),
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

class IChainLinkCloneCollection(DispatchBaseClass):
	'''IChainLinkCloneCollection'''
	CLSID = IID('{BFBCE202-F4CB-40D0-8652-8DF819E5D886}')
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
		:rtype: recurdyn.Chain.IChainLinkClone
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{3C283940-AAB3-48D1-A521-D8AA43058BC2}')
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
		:rtype: recurdyn.Chain.IChainLinkClone
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{3C283940-AAB3-48D1-A521-D8AA43058BC2}')
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
		return win32com.client.util.Iterator(ob, '{3C283940-AAB3-48D1-A521-D8AA43058BC2}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{3C283940-AAB3-48D1-A521-D8AA43058BC2}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IChainLinkCloneMultiplexOffset(DispatchBaseClass):
	'''Chain Clone Link Offset Multiplex'''
	CLSID = IID('{F02C6C40-A3AC-404E-8FE8-BA034A99392F}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(10516, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(10511, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
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
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (10517, 2, (11, 0), (), "Active", None),
		"CenterMarker": (10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (10511, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((10517, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((10511, LCID, 4, 0),()),
		"Material": ((10510, LCID, 4, 0),()),
		"MaterialInput": ((10509, LCID, 4, 0),()),
		"MaterialUser": ((10512, LCID, 4, 0),()),
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

class IChainLinkCloneMultiplexPin(DispatchBaseClass):
	'''Chain Clone Link Pin Multiplex'''
	CLSID = IID('{18CD7701-60FB-4CC3-9619-36DDD1647F44}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(10516, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10552, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(10511, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{33736DE9-40C6-42C3-96EB-72FD82D10535}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkMultiplexPin
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (10517, 2, (11, 0), (), "Active", None),
		"CenterMarker": (10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (10511, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{33736DE9-40C6-42C3-96EB-72FD82D10535}'),
		"Graphic": (10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((10517, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((10511, LCID, 4, 0),()),
		"Material": ((10510, LCID, 4, 0),()),
		"MaterialInput": ((10509, LCID, 4, 0),()),
		"MaterialUser": ((10512, LCID, 4, 0),()),
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

class IChainLinkCloneMultiplexRoller(DispatchBaseClass):
	'''Chain Clone Link Roller Multiplex'''
	CLSID = IID('{4E0780CE-4019-4B61-AE39-D5E2889DA39E}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(10516, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10552, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(10511, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LinkPlateShapeType(self):
		return self._ApplyTypes_(*(10553, 2, (3, 0), (), "LinkPlateShapeType", '{70767D30-A128-49F0-BFC5-1CEE78841C28}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_LinkPlateShapeType(self, value):
		if "LinkPlateShapeType" in self.__dict__: self.__dict__["LinkPlateShapeType"] = value; return
		self._oleobj_.Invoke(*((10553, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkMultiplexRoller
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	LinkPlateShapeType = property(_get_LinkPlateShapeType, _set_LinkPlateShapeType)
	'''
	Link Plate Shape Type

	:type: recurdyn.Chain.ChainLinkPlateShapeType
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_LinkPlateShapeType": _set_LinkPlateShapeType,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (10517, 2, (11, 0), (), "Active", None),
		"CenterMarker": (10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (10511, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}'),
		"Graphic": (10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LinkPlateShapeType": (10553, 2, (3, 0), (), "LinkPlateShapeType", '{70767D30-A128-49F0-BFC5-1CEE78841C28}'),
		"Mass": (10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((10517, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((10511, LCID, 4, 0),()),
		"LinkPlateShapeType": ((10553, LCID, 4, 0),()),
		"Material": ((10510, LCID, 4, 0),()),
		"MaterialInput": ((10509, LCID, 4, 0),()),
		"MaterialUser": ((10512, LCID, 4, 0),()),
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

class IChainLinkCloneOffset(DispatchBaseClass):
	'''Chain Link Clone Offset'''
	CLSID = IID('{DF2ABA6B-0E35-4110-A019-147E34D9C411}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(10516, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(10511, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
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
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (10517, 2, (11, 0), (), "Active", None),
		"CenterMarker": (10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (10511, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Graphic": (10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((10517, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((10511, LCID, 4, 0),()),
		"Material": ((10510, LCID, 4, 0),()),
		"MaterialInput": ((10509, LCID, 4, 0),()),
		"MaterialUser": ((10512, LCID, 4, 0),()),
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

class IChainLinkClonePin(DispatchBaseClass):
	'''Chain Clone Link Pin'''
	CLSID = IID('{50F61A34-FBAC-4394-9FC3-07729ABA03C3}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(10516, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10552, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(10511, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{B4B7B26A-F4EB-486F-9909-74DA518613C4}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkPin
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (10517, 2, (11, 0), (), "Active", None),
		"CenterMarker": (10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (10511, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{B4B7B26A-F4EB-486F-9909-74DA518613C4}'),
		"Graphic": (10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((10517, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((10511, LCID, 4, 0),()),
		"Material": ((10510, LCID, 4, 0),()),
		"MaterialInput": ((10509, LCID, 4, 0),()),
		"MaterialUser": ((10512, LCID, 4, 0),()),
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

class IChainLinkCloneRoller(DispatchBaseClass):
	'''Chain Link Clone Roller'''
	CLSID = IID('{920A282B-0B31-4AED-9219-BB0163557B7C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(10516, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10552, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(10511, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{E6301A79-B289-4188-B213-AE53CA9E89BB}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_LinkPlateShapeType(self):
		return self._ApplyTypes_(*(10553, 2, (3, 0), (), "LinkPlateShapeType", '{70767D30-A128-49F0-BFC5-1CEE78841C28}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
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
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_LinkPlateShapeType(self, value):
		if "LinkPlateShapeType" in self.__dict__: self.__dict__["LinkPlateShapeType"] = value; return
		self._oleobj_.Invoke(*((10553, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkRoller
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	LinkPlateShapeType = property(_get_LinkPlateShapeType, _set_LinkPlateShapeType)
	'''
	Link Plate Shape Type

	:type: recurdyn.Chain.ChainLinkPlateShapeType
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
		"_set_Density": _set_Density,
		"_set_LinkPlateShapeType": _set_LinkPlateShapeType,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (10517, 2, (11, 0), (), "Active", None),
		"CenterMarker": (10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (10511, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{E6301A79-B289-4188-B213-AE53CA9E89BB}'),
		"Graphic": (10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"LinkPlateShapeType": (10553, 2, (3, 0), (), "LinkPlateShapeType", '{70767D30-A128-49F0-BFC5-1CEE78841C28}'),
		"Mass": (10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((10517, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((10511, LCID, 4, 0),()),
		"LinkPlateShapeType": ((10553, LCID, 4, 0),()),
		"Material": ((10510, LCID, 4, 0),()),
		"MaterialInput": ((10509, LCID, 4, 0),()),
		"MaterialUser": ((10512, LCID, 4, 0),()),
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

class IChainLinkCloneSilentInner(DispatchBaseClass):
	'''Chain Clone Link Silent Outer'''
	CLSID = IID('{F9F223BD-D461-4F06-950E-6A821C5BB83D}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(10516, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10553, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(10511, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "Profile", '{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkSilentInner
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
	Profile = property(_get_Profile, None)
	'''
	Profile of Link Silent

	:type: recurdyn.Chain.IChainProfileLinkSilent
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (10517, 2, (11, 0), (), "Active", None),
		"CenterMarker": (10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (10511, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}'),
		"Graphic": (10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Profile": (10552, 2, (9, 0), (), "Profile", '{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((10517, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((10511, LCID, 4, 0),()),
		"Material": ((10510, LCID, 4, 0),()),
		"MaterialInput": ((10509, LCID, 4, 0),()),
		"MaterialUser": ((10512, LCID, 4, 0),()),
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

class IChainLinkCloneSilentOuter(DispatchBaseClass):
	'''Chain Clone Link Silent Outer'''
	CLSID = IID('{4EC1DA77-AD7C-4C9D-B34D-13690F2187D2}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def FileExport(self, strFile, OverWrite):
		'''
		Export File
		
		:param strFile: str
		:param OverWrite: bool
		'''
		return self._oleobj_.InvokeTypes(10516, LCID, 1, (24, 0), ((8, 1), (11, 1)),strFile
			, OverWrite)


	def FileImport(self, strFile):
		'''
		Import File
		
		:param strFile: str
		'''
		return self._oleobj_.InvokeTypes(10515, LCID, 1, (24, 0), ((8, 1),),strFile
			)


	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def InitialBodyGraphicFlag(self):
		'''
		Initial body graphic flag
		'''
		return self._oleobj_.InvokeTypes(10514, LCID, 1, (24, 0), (),)


	def UpdateGeometry(self):
		'''
		Update geometry
		'''
		return self._oleobj_.InvokeTypes(10553, LCID, 1, (24, 0), (),)


	def _get_Active(self):
		return self._ApplyTypes_(*(10517, 2, (11, 0), (), "Active", None))
	def _get_CenterMarker(self):
		return self._ApplyTypes_(*(10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_Density(self):
		return self._ApplyTypes_(*(10511, 2, (5, 0), (), "Density", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_Geometry(self):
		return self._ApplyTypes_(*(10551, 2, (9, 0), (), "Geometry", '{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}'))
	def _get_Graphic(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'))
	def _get_Ixx(self):
		return self._ApplyTypes_(*(10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Ixy(self):
		return self._ApplyTypes_(*(10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyy(self):
		return self._ApplyTypes_(*(10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Iyz(self):
		return self._ApplyTypes_(*(10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izx(self):
		return self._ApplyTypes_(*(10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Izz(self):
		return self._ApplyTypes_(*(10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Mass(self):
		return self._ApplyTypes_(*(10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'))
	def _get_Material(self):
		return self._ApplyTypes_(*(10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'))
	def _get_MaterialInput(self):
		return self._ApplyTypes_(*(10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'))
	def _get_MaterialUser(self):
		return self._ApplyTypes_(*(10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'))
	def _get_Name(self):
		return self._ApplyTypes_(*(101, 2, (8, 0), (), "Name", None))
	def _get_Owner(self):
		return self._ApplyTypes_(*(106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'))
	def _get_OwnerBody(self):
		return self._ApplyTypes_(*(105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'))
	def _get_OwnerSubSystem(self):
		return self._ApplyTypes_(*(104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_Profile(self):
		return self._ApplyTypes_(*(10552, 2, (9, 0), (), "Profile", '{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}'))
	def _get_UserData(self):
		return self._ApplyTypes_(*(107, 2, (8, 0), (), "UserData", None))

	def _set_Active(self, value):
		if "Active" in self.__dict__: self.__dict__["Active"] = value; return
		self._oleobj_.Invoke(*((10517, LCID, 4, 0) + (value,) + ()))
	def _set_Comment(self, value):
		if "Comment" in self.__dict__: self.__dict__["Comment"] = value; return
		self._oleobj_.Invoke(*((102, LCID, 4, 0) + (value,) + ()))
	def _set_Density(self, value):
		if "Density" in self.__dict__: self.__dict__["Density"] = value; return
		self._oleobj_.Invoke(*((10511, LCID, 4, 0) + (value,) + ()))
	def _set_Material(self, value):
		if "Material" in self.__dict__: self.__dict__["Material"] = value; return
		self._oleobj_.Invoke(*((10510, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialInput(self, value):
		if "MaterialInput" in self.__dict__: self.__dict__["MaterialInput"] = value; return
		self._oleobj_.Invoke(*((10509, LCID, 4, 0) + (value,) + ()))
	def _set_MaterialUser(self, value):
		if "MaterialUser" in self.__dict__: self.__dict__["MaterialUser"] = value; return
		self._oleobj_.Invoke(*((10512, LCID, 4, 0) + (value,) + ()))
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
	CenterMarker = property(_get_CenterMarker, None)
	'''
	Center marker

	:type: recurdyn.ProcessNet.IMarker
	'''
	Comment = property(_get_Comment, _set_Comment)
	'''
	Comment

	:type: str
	'''
	Density = property(_get_Density, _set_Density)
	'''
	Density

	:type: float
	'''
	FullName = property(_get_FullName, None)
	'''
	FullName such as Body1.Marker1@Model1

	:type: str
	'''
	Geometry = property(_get_Geometry, None)
	'''
	Geometry

	:type: recurdyn.Chain.IChainGeometryLinkSilentOuter
	'''
	Graphic = property(_get_Graphic, None)
	'''
	Graphic

	:type: recurdyn.ProcessNet.IGraphicProperty
	'''
	Ixx = property(_get_Ixx, None)
	'''
	Ixx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Ixy = property(_get_Ixy, None)
	'''
	Ixy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyy = property(_get_Iyy, None)
	'''
	Iyy

	:type: recurdyn.ProcessNet.IDouble
	'''
	Iyz = property(_get_Iyz, None)
	'''
	Iyz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izx = property(_get_Izx, None)
	'''
	Izx

	:type: recurdyn.ProcessNet.IDouble
	'''
	Izz = property(_get_Izz, None)
	'''
	Izz

	:type: recurdyn.ProcessNet.IDouble
	'''
	Mass = property(_get_Mass, None)
	'''
	Mass

	:type: recurdyn.ProcessNet.IDouble
	'''
	Material = property(_get_Material, _set_Material)
	'''
	Material

	:type: recurdyn.ProcessNet.Material
	'''
	MaterialInput = property(_get_MaterialInput, _set_MaterialInput)
	'''
	Material input

	:type: recurdyn.ProcessNet.MaterialInput
	'''
	MaterialUser = property(_get_MaterialUser, _set_MaterialUser)
	'''
	User Material

	:type: recurdyn.ProcessNet.IMaterialProperty
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
	Profile = property(_get_Profile, None)
	'''
	Profile of Link Silent

	:type: recurdyn.Chain.IChainProfileLinkSilent
	'''
	UserData = property(_get_UserData, _set_UserData)
	'''
	User supplied data

	:type: str
	'''

	_prop_map_set_function_ = {
		"_set_Active": _set_Active,
		"_set_Comment": _set_Comment,
		"_set_Density": _set_Density,
		"_set_Material": _set_Material,
		"_set_MaterialInput": _set_MaterialInput,
		"_set_MaterialUser": _set_MaterialUser,
		"_set_Name": _set_Name,
		"_set_UserData": _set_UserData,
	}
	_prop_map_get_ = {
		"Active": (10517, 2, (11, 0), (), "Active", None),
		"CenterMarker": (10513, 2, (9, 0), (), "CenterMarker", '{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"Density": (10511, 2, (5, 0), (), "Density", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"Geometry": (10551, 2, (9, 0), (), "Geometry", '{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}'),
		"Graphic": (10501, 2, (9, 0), (), "Graphic", '{4C8B7C23-7D92-4D39-B530-5D93DC97F771}'),
		"Ixx": (10503, 2, (9, 0), (), "Ixx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Ixy": (10506, 2, (9, 0), (), "Ixy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyy": (10504, 2, (9, 0), (), "Iyy", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Iyz": (10507, 2, (9, 0), (), "Iyz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izx": (10508, 2, (9, 0), (), "Izx", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Izz": (10505, 2, (9, 0), (), "Izz", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Mass": (10502, 2, (9, 0), (), "Mass", '{2B5166E3-4B31-4607-B157-BE237A670336}'),
		"Material": (10510, 2, (3, 0), (), "Material", '{EF682F61-990D-40D7-9A4C-46391963D599}'),
		"MaterialInput": (10509, 2, (3, 0), (), "MaterialInput", '{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}'),
		"MaterialUser": (10512, 2, (9, 0), (), "MaterialUser", '{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}'),
		"Name": (101, 2, (8, 0), (), "Name", None),
		"Owner": (106, 2, (9, 0), (), "Owner", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}'),
		"OwnerBody": (105, 2, (9, 0), (), "OwnerBody", '{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}'),
		"OwnerSubSystem": (104, 2, (9, 0), (), "OwnerSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"Profile": (10552, 2, (9, 0), (), "Profile", '{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}'),
		"UserData": (107, 2, (8, 0), (), "UserData", None),
	}
	_prop_map_put_ = {
		"Active": ((10517, LCID, 4, 0),()),
		"Comment": ((102, LCID, 4, 0),()),
		"Density": ((10511, LCID, 4, 0),()),
		"Material": ((10510, LCID, 4, 0),()),
		"MaterialInput": ((10509, LCID, 4, 0),()),
		"MaterialUser": ((10512, LCID, 4, 0),()),
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

class IChainPassingBodyCollection(DispatchBaseClass):
	'''IChainPassingBodyCollection'''
	CLSID = IID('{90DD375C-3EA7-4002-BDB2-8E3E3E03AEE2}')
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
		:rtype: recurdyn.ProcessNet.IGeneric
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, 'Item', '{27A86788-8B85-40CF-BE7F-BA915103A7DB}')
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
		:rtype: recurdyn.ProcessNet.IGeneric
		'''
		ret = self._oleobj_.InvokeTypes(0, LCID, 2, (9, 0), ((12, 1),),var
			)
		if ret is not None:
			ret = Dispatch(ret, '__call__', '{27A86788-8B85-40CF-BE7F-BA915103A7DB}')
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
		return win32com.client.util.Iterator(ob, '{27A86788-8B85-40CF-BE7F-BA915103A7DB}')
	def __getitem__(self, key):
		return self._get_good_object_(self._oleobj_.Invoke(*(0, LCID, 2, 1, key)), "Item", '{27A86788-8B85-40CF-BE7F-BA915103A7DB}')
	#This class has Count() property - allow len(ob) to provide this
	def __len__(self):
		return self._ApplyTypes_(*(1, 2, (3, 0), (), "Count", None))
	#This class has a __len__ - this is needed so 'if object:' always returns TRUE.
	def __nonzero__(self):
		return True

class IChainProfileLinkSilent(DispatchBaseClass):
	'''Chain Profile Silent Link'''
	CLSID = IID('{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Add(self, dX, dY, dR, bCheckContactPair):
		'''
		Add Point
		
		:param dX: float
		:param dY: float
		:param dR: float
		:param bCheckContactPair: bool
		'''
		return self._oleobj_.InvokeTypes(10507, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1), (11, 1)),dX
			, dY, dR, bCheckContactPair)


	def Clear(self):
		'''
		Clear Point and Check Collection
		'''
		return self._oleobj_.InvokeTypes(10508, LCID, 1, (24, 0), (),)


	def Export(self, strName, val):
		'''
		Export method
		
		:param strName: str
		:param val: bool
		'''
		return self._oleobj_.InvokeTypes(10502, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(10503, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_ContactPairInfoCollection(self):
		return self._ApplyTypes_(*(10501, 2, (9, 0), (), "ContactPairInfoCollection", '{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}'))
	def _get_GuideRollerContactLengthSegment(self):
		return self._ApplyTypes_(*(10506, 2, (3, 0), (), "GuideRollerContactLengthSegment", None))
	def _get_GuideRollerContactNodeEnd(self):
		return self._ApplyTypes_(*(10505, 2, (3, 0), (), "GuideRollerContactNodeEnd", None))
	def _get_GuideRollerContactNodeStart(self):
		return self._ApplyTypes_(*(10504, 2, (3, 0), (), "GuideRollerContactNodeStart", None))
	def _get_PointCollection(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	def _set_GuideRollerContactLengthSegment(self, value):
		if "GuideRollerContactLengthSegment" in self.__dict__: self.__dict__["GuideRollerContactLengthSegment"] = value; return
		self._oleobj_.Invoke(*((10506, LCID, 4, 0) + (value,) + ()))
	def _set_GuideRollerContactNodeEnd(self, value):
		if "GuideRollerContactNodeEnd" in self.__dict__: self.__dict__["GuideRollerContactNodeEnd"] = value; return
		self._oleobj_.Invoke(*((10505, LCID, 4, 0) + (value,) + ()))
	def _set_GuideRollerContactNodeStart(self, value):
		if "GuideRollerContactNodeStart" in self.__dict__: self.__dict__["GuideRollerContactNodeStart"] = value; return
		self._oleobj_.Invoke(*((10504, LCID, 4, 0) + (value,) + ()))

	ContactPairInfoCollection = property(_get_ContactPairInfoCollection, None)
	'''
	Check Collection

	:type: recurdyn.Chain.IChainContactPairInfoCollection
	'''
	GuideRollerContactLengthSegment = property(_get_GuideRollerContactLengthSegment, _set_GuideRollerContactLengthSegment)
	'''
	Lenth Segment of Guide/Roller Contact

	:type: int
	'''
	GuideRollerContactNodeEnd = property(_get_GuideRollerContactNodeEnd, _set_GuideRollerContactNodeEnd)
	'''
	End Node of Guide/Roller Contact

	:type: int
	'''
	GuideRollerContactNodeStart = property(_get_GuideRollerContactNodeStart, _set_GuideRollerContactNodeStart)
	'''
	Start Node of Guide/Roller Contact

	:type: int
	'''
	PointCollection = property(_get_PointCollection, None)
	'''
	Point Collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
		"_set_GuideRollerContactLengthSegment": _set_GuideRollerContactLengthSegment,
		"_set_GuideRollerContactNodeEnd": _set_GuideRollerContactNodeEnd,
		"_set_GuideRollerContactNodeStart": _set_GuideRollerContactNodeStart,
	}
	_prop_map_get_ = {
		"ContactPairInfoCollection": (10501, 2, (9, 0), (), "ContactPairInfoCollection", '{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}'),
		"GuideRollerContactLengthSegment": (10506, 2, (3, 0), (), "GuideRollerContactLengthSegment", None),
		"GuideRollerContactNodeEnd": (10505, 2, (3, 0), (), "GuideRollerContactNodeEnd", None),
		"GuideRollerContactNodeStart": (10504, 2, (3, 0), (), "GuideRollerContactNodeStart", None),
		"PointCollection": (10500, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
	}
	_prop_map_put_ = {
		"GuideRollerContactLengthSegment": ((10506, LCID, 4, 0),()),
		"GuideRollerContactNodeEnd": ((10505, LCID, 4, 0),()),
		"GuideRollerContactNodeStart": ((10504, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainProfileSprocket(DispatchBaseClass):
	'''Chain Profile Sprocket'''
	CLSID = IID('{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Add(self, dX, dY, dR):
		'''
		Add Point
		
		:param dX: float
		:param dY: float
		:param dR: float
		'''
		return self._oleobj_.InvokeTypes(10503, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1)),dX
			, dY, dR)


	def Clear(self):
		'''
		Clear Point and Check Collection
		'''
		return self._oleobj_.InvokeTypes(10504, LCID, 1, (24, 0), (),)


	def Export(self, strName, val):
		'''
		Export method
		
		:param strName: str
		:param val: bool
		'''
		return self._oleobj_.InvokeTypes(10501, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(10502, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_PointCollection(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))

	PointCollection = property(_get_PointCollection, None)
	'''
	Point Collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"PointCollection": (10500, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
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

class IChainProfileSprocket2(DispatchBaseClass):
	'''Chain Profile Sprocket'''
	CLSID = IID('{BD4851C8-8A99-4B29-80AE-2E160DC0754C}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def Add(self, dX, dY, dR, bCheckContactPair, bstrSegmentInfo):
		'''
		Add Point
		
		:param dX: float
		:param dY: float
		:param dR: float
		:param bCheckContactPair: bool
		:param bstrSegmentInfo: str
		'''
		return self._oleobj_.InvokeTypes(10559, LCID, 1, (24, 0), ((5, 1), (5, 1), (5, 1), (11, 1), (8, 1)),dX
			, dY, dR, bCheckContactPair, bstrSegmentInfo)


	def Clear(self):
		'''
		Clear Point and Check Collection
		'''
		return self._oleobj_.InvokeTypes(10560, LCID, 1, (24, 0), (),)


	def Export(self, strName, val):
		'''
		Export method
		
		:param strName: str
		:param val: bool
		'''
		return self._oleobj_.InvokeTypes(10557, LCID, 1, (24, 0), ((8, 1), (11, 1)),strName
			, val)


	def Import(self, strName):
		'''
		Import method
		
		:param strName: str
		'''
		return self._oleobj_.InvokeTypes(10558, LCID, 1, (24, 0), ((8, 1),),strName
			)


	def _get_ContactPairInfoCollection(self):
		return self._ApplyTypes_(*(10555, 2, (9, 0), (), "ContactPairInfoCollection", '{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}'))
	def _get_InvoluteCurveParameter(self):
		return self._ApplyTypes_(*(10553, 2, (9, 0), (), "InvoluteCurveParameter", '{E56F87E6-1157-4D4A-9F6A-D66FFE9C2C0D}'))
	def _get_NumberofArc(self):
		return self._ApplyTypes_(*(10554, 2, (3, 0), (), "NumberofArc", None))
	def _get_PointCollection(self):
		return self._ApplyTypes_(*(10556, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'))
	def _get_UseContactPair(self):
		return self._ApplyTypes_(*(10551, 2, (11, 0), (), "UseContactPair", None))
	def _get_UseInvoluteMethod(self):
		return self._ApplyTypes_(*(10552, 2, (11, 0), (), "UseInvoluteMethod", None))

	def _set_NumberofArc(self, value):
		if "NumberofArc" in self.__dict__: self.__dict__["NumberofArc"] = value; return
		self._oleobj_.Invoke(*((10554, LCID, 4, 0) + (value,) + ()))
	def _set_UseContactPair(self, value):
		if "UseContactPair" in self.__dict__: self.__dict__["UseContactPair"] = value; return
		self._oleobj_.Invoke(*((10551, LCID, 4, 0) + (value,) + ()))
	def _set_UseInvoluteMethod(self, value):
		if "UseInvoluteMethod" in self.__dict__: self.__dict__["UseInvoluteMethod"] = value; return
		self._oleobj_.Invoke(*((10552, LCID, 4, 0) + (value,) + ()))

	ContactPairInfoCollection = property(_get_ContactPairInfoCollection, None)
	'''
	ContactPairInfo Collection

	:type: recurdyn.Chain.IChainContactPairInfoCollection
	'''
	InvoluteCurveParameter = property(_get_InvoluteCurveParameter, None)
	'''
	Involute Curve Parameter

	:type: recurdyn.Chain.IChainInvoluteCurveParameter
	'''
	NumberofArc = property(_get_NumberofArc, _set_NumberofArc)
	'''
	The Number of Arc

	:type: int
	'''
	PointCollection = property(_get_PointCollection, None)
	'''
	Point Collection

	:type: recurdyn.ProcessNet.IPoint2DWithRadiusCollection
	'''
	UseContactPair = property(_get_UseContactPair, _set_UseContactPair)
	'''
	Use Contact Pair.

	:type: bool
	'''
	UseInvoluteMethod = property(_get_UseInvoluteMethod, _set_UseInvoluteMethod)
	'''
	Use Involute Method

	:type: bool
	'''

	_prop_map_set_function_ = {
		"_set_NumberofArc": _set_NumberofArc,
		"_set_UseContactPair": _set_UseContactPair,
		"_set_UseInvoluteMethod": _set_UseInvoluteMethod,
	}
	_prop_map_get_ = {
		"ContactPairInfoCollection": (10555, 2, (9, 0), (), "ContactPairInfoCollection", '{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}'),
		"InvoluteCurveParameter": (10553, 2, (9, 0), (), "InvoluteCurveParameter", '{E56F87E6-1157-4D4A-9F6A-D66FFE9C2C0D}'),
		"NumberofArc": (10554, 2, (3, 0), (), "NumberofArc", None),
		"PointCollection": (10556, 2, (9, 0), (), "PointCollection", '{2C0D70A3-D197-4781-940A-1672F3B420B9}'),
		"UseContactPair": (10551, 2, (11, 0), (), "UseContactPair", None),
		"UseInvoluteMethod": (10552, 2, (11, 0), (), "UseInvoluteMethod", None),
	}
	_prop_map_put_ = {
		"NumberofArc": ((10554, LCID, 4, 0),()),
		"UseContactPair": ((10551, LCID, 4, 0),()),
		"UseInvoluteMethod": ((10552, LCID, 4, 0),()),
	}
	def __iter__(self):
		"Return a Python iterator for this object"
		try:
			ob = self._oleobj_.InvokeTypes(-4,LCID,3,(13, 10),())
		except pythoncom.error:
			raise TypeError("This object does not support enumeration")
		return win32com.client.util.Iterator(ob, None)

class IChainSubSystem(DispatchBaseClass):
	'''Chain Subsystem'''
	CLSID = IID('{E8F3EEAE-A4B6-4A6A-A0F2-DE6BA3CF1DEA}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def CreateBodyGuardLateral(self, strName, pFirstPoint, pSecondPoint):
		'''
		Create a Guard Lateral
		
		:param strName: str
		:param pFirstPoint: list[float]
		:param pSecondPoint: list[float]
		:rtype: recurdyn.Chain.IChainBodyGuardLateral
		'''
		ret = self._oleobj_.InvokeTypes(10510, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1)),strName
			, pFirstPoint, pSecondPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyGuardLateral', '{98696CB8-03A8-4036-8D71-2143E04AB2AC}')
		return ret

	def CreateBodyGuide(self, strCloneName, Points):
		'''
		Create a Guide
		
		:param strCloneName: str
		:param Points: list[object]
		:rtype: recurdyn.Chain.IChainBodyGuide
		'''
		_Points_type = True if Points and isinstance(Points[0], win32com.client.VARIANT) else False
		if not _Points_type:
			Points = [win32com.client.VARIANT(12, _data) for _data in Points]

		ret = self._oleobj_.InvokeTypes(10508, LCID, 1, (9, 0), ((8, 1), (8204, 1)),strCloneName
			, Points)

		if not _Points_type:
			Points = [_data.value for _data in Points]

		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyGuide', '{3A623CE7-0BFB-48D9-AB5B-5B305B9F4D45}')
		return ret

	def CreateBodyRoller(self, strName, pPoint):
		'''
		Create a Roller Body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.Chain.IChainBodyRoller
		'''
		ret = self._oleobj_.InvokeTypes(10501, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodyRoller', '{67A861E0-46A2-4D78-A5FA-16B63F2A72AE}')
		return ret

	def CreateBodySprocketMultiplex(self, strName, pPoint):
		'''
		Create a Sprocket Multiplex Body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.Chain.IChainBodySprocketMultiplex
		'''
		ret = self._oleobj_.InvokeTypes(10503, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodySprocketMultiplex', '{11BBB345-C32E-4A00-9F53-C1FED84012B8}')
		return ret

	def CreateBodySprocketRoller(self, strName, pPoint):
		'''
		Create a Sprocket Roller Body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.Chain.IChainBodySprocketRoller
		'''
		ret = self._oleobj_.InvokeTypes(10502, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodySprocketRoller', '{C34B22A6-F4E3-4747-BFF8-733F8317E9C2}')
		return ret

	def CreateBodySprocketSilent(self, strName, pPoint):
		'''
		Create a Sprocket Silent Body
		
		:param strName: str
		:param pPoint: list[float]
		:rtype: recurdyn.Chain.IChainBodySprocketSilent
		'''
		ret = self._oleobj_.InvokeTypes(10504, LCID, 1, (9, 0), ((8, 1), (8197, 1)),strName
			, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateBodySprocketSilent', '{20AA2528-64F0-4CC6-95B3-BE6402187F92}')
		return ret

	def CreateChainAssemblyMultiplex(self, strName, pLinkClone, pBodyList, pInOutList, bushingType, uiNumberOfLink, automaticAlignment):
		'''
		Create Chain Assembly for Multiplex
		
		:param strName: str
		:param pLinkClone: IChainLinkCloneMultiplexRoller
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param bushingType: ChainAssemblyBushingType
		:param uiNumberOfLink: int
		:param automaticAlignment: bool
		:rtype: recurdyn.Chain.IChainAssembly
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10512, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (3, 1), (19, 1), (11, 1)),strName
			, pLinkClone, pBodyList, pInOutList, bushingType, uiNumberOfLink
			, automaticAlignment)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateChainAssemblyMultiplex', '{0963256F-0F65-4E93-8FFA-B58651838BC6}')
		return ret

	def CreateChainAssemblyRoller(self, strName, pLinkClone, pBodyList, pInOutList, bushingType, uiNumberOfLink, automaticAlignment):
		'''
		Create Chain Assembly for Roller
		
		:param strName: str
		:param pLinkClone: IChainLinkCloneRoller
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param bushingType: ChainAssemblyBushingType
		:param uiNumberOfLink: int
		:param automaticAlignment: bool
		:rtype: recurdyn.Chain.IChainAssembly
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10511, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (3, 1), (19, 1), (11, 1)),strName
			, pLinkClone, pBodyList, pInOutList, bushingType, uiNumberOfLink
			, automaticAlignment)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateChainAssemblyRoller', '{0963256F-0F65-4E93-8FFA-B58651838BC6}')
		return ret

	def CreateChainAssemblySilent(self, strName, pLinkClone, pBodyList, pInOutList, bushingType, uiNumberOfLink, automaticAlignment):
		'''
		Create Chain Assembly for Silent
		
		:param strName: str
		:param pLinkClone: IChainLinkCloneSilentOuter
		:param pBodyList: list[object]
		:param pInOutList: list[object]
		:param bushingType: ChainAssemblyBushingType
		:param uiNumberOfLink: int
		:param automaticAlignment: bool
		:rtype: recurdyn.Chain.IChainAssembly
		'''
		_pBodyList_type = True if pBodyList and isinstance(pBodyList[0], win32com.client.VARIANT) else False
		if not _pBodyList_type:
			pBodyList = [win32com.client.VARIANT(12, _data) for _data in pBodyList]
		_pInOutList_type = True if pInOutList and isinstance(pInOutList[0], win32com.client.VARIANT) else False
		if not _pInOutList_type:
			pInOutList = [win32com.client.VARIANT(12, _data) for _data in pInOutList]

		ret = self._oleobj_.InvokeTypes(10513, LCID, 1, (9, 0), ((8, 1), (9, 1), (8204, 1), (8204, 1), (3, 1), (19, 1), (11, 1)),strName
			, pLinkClone, pBodyList, pInOutList, bushingType, uiNumberOfLink
			, automaticAlignment)

		if not _pBodyList_type:
			pBodyList = [_data.value for _data in pBodyList]
		if not _pInOutList_type:
			pInOutList = [_data.value for _data in pInOutList]

		if ret is not None:
			ret = Dispatch(ret, 'CreateChainAssemblySilent', '{0963256F-0F65-4E93-8FFA-B58651838BC6}')
		return ret

	def CreateForceConnectorBushing(self, strName, pBaseBody, pActionBody, pRefFrame):
		'''
		Create bushing connector
		
		:param strName: str
		:param pBaseBody: IGeneric
		:param pActionBody: IGeneric
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ToolkitCommon.IForceConnectorBushing
		'''
		ret = self._oleobj_.InvokeTypes(10517, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorBushing', '{F5A169B5-B529-4935-8B06-ACDD2A0BA456}')
		return ret

	def CreateForceConnectorFixed(self, strName, pBaseBody, pActionBody, pRefFrame):
		'''
		Create fixed connector
		
		:param strName: str
		:param pBaseBody: IGeneric
		:param pActionBody: IGeneric
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ToolkitCommon.IForceConnectorFixed
		'''
		ret = self._oleobj_.InvokeTypes(10514, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorFixed', '{39059D2F-DBEC-49DD-BFF2-AC0185541C99}')
		return ret

	def CreateForceConnectorRevolute(self, strName, pBaseBody, pActionBody, pRefFrame):
		'''
		Create revolute connector
		
		:param strName: str
		:param pBaseBody: IGeneric
		:param pActionBody: IGeneric
		:param pRefFrame: IReferenceFrame
		:rtype: recurdyn.ToolkitCommon.IForceConnectorRevolute
		'''
		ret = self._oleobj_.InvokeTypes(10515, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorRevolute', '{D24BBA28-623F-4F1C-97D5-021413EB6736}')
		return ret

	def CreateForceConnectorSpring(self, strName, pBaseBody, pActionBody, pBaseRefFrame, pActionRefFrame):
		'''
		Create spring connector
		
		:param strName: str
		:param pBaseBody: IGeneric
		:param pActionBody: IGeneric
		:param pBaseRefFrame: IReferenceFrame
		:param pActionRefFrame: IReferenceFrame
		:rtype: recurdyn.ToolkitCommon.IForceConnectorSpring
		'''
		ret = self._oleobj_.InvokeTypes(10516, LCID, 1, (9, 0), ((8, 1), (9, 1), (9, 1), (9, 1), (9, 1)),strName
			, pBaseBody, pActionBody, pBaseRefFrame, pActionRefFrame)
		if ret is not None:
			ret = Dispatch(ret, 'CreateForceConnectorSpring', '{93A5A572-A6DD-4F12-A3E5-64F95B78718F}')
		return ret

	def CreateGroupGuideArc(self, strName, Points, Segments):
		'''
		Create a Group Guide Arc
		
		:param strName: str
		:param Points: list[object]
		:param Segments: list[int]
		:rtype: recurdyn.Chain.IChainGroupGuideArc
		'''
		_Points_type = True if Points and isinstance(Points[0], win32com.client.VARIANT) else False
		if not _Points_type:
			Points = [win32com.client.VARIANT(12, _data) for _data in Points]

		ret = self._oleobj_.InvokeTypes(10509, LCID, 1, (9, 0), ((8, 1), (8204, 1), (8211, 1)),strName
			, Points, Segments)

		if not _Points_type:
			Points = [_data.value for _data in Points]

		if ret is not None:
			ret = Dispatch(ret, 'CreateGroupGuideArc', '{037DA049-C1EB-4F0B-8457-80FE60733754}')
		return ret

	def CreateLinkCloneMultiplex(self, strNameCloneRoller, strNameClonePin, strNameCloneOffset, pPoint, LinkType, nNoOfStrands):
		'''
		Create a Link Multiplex Body
		
		:param strNameCloneRoller: str
		:param strNameClonePin: str
		:param strNameCloneOffset: str
		:param pPoint: list[float]
		:param LinkType: ChainLinkType
		:param nNoOfStrands: int
		:rtype: recurdyn.Chain.IChainLinkCloneMultiplexRoller
		'''
		ret = self._oleobj_.InvokeTypes(10506, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (8197, 1), (3, 1), (3, 1)),strNameCloneRoller
			, strNameClonePin, strNameCloneOffset, pPoint, LinkType, nNoOfStrands
			)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLinkCloneMultiplex', '{4E0780CE-4019-4B61-AE39-D5E2889DA39E}')
		return ret

	def CreateLinkCloneRoller(self, strNameCloneRoller, strNameClonePin, strNameCloneOffset, pPoint, nNoOfLinkSets):
		'''
		Create a Link Roller Body
		
		:param strNameCloneRoller: str
		:param strNameClonePin: str
		:param strNameCloneOffset: str
		:param pPoint: list[float]
		:param nNoOfLinkSets: int
		:rtype: recurdyn.Chain.IChainLinkCloneRoller
		'''
		ret = self._oleobj_.InvokeTypes(10505, LCID, 1, (9, 0), ((8, 1), (8, 1), (8, 1), (8197, 1), (3, 1)),strNameCloneRoller
			, strNameClonePin, strNameCloneOffset, pPoint, nNoOfLinkSets)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLinkCloneRoller', '{920A282B-0B31-4AED-9219-BB0163557B7C}')
		return ret

	def CreateLinkCloneSilent(self, strNameCloneOuter, strNameCloneInner, pPoint):
		'''
		Create a Link Silent Body
		
		:param strNameCloneOuter: str
		:param strNameCloneInner: str
		:param pPoint: list[float]
		:rtype: recurdyn.Chain.IChainLinkCloneSilentOuter
		'''
		ret = self._oleobj_.InvokeTypes(10507, LCID, 1, (9, 0), ((8, 1), (8, 1), (8197, 1)),strNameCloneOuter
			, strNameCloneInner, pPoint)
		if ret is not None:
			ret = Dispatch(ret, 'CreateLinkCloneSilent', '{4EC1DA77-AD7C-4C9D-B34D-13690F2187D2}')
		return ret

	def CreateSensorDistance(self, strName, pPosition, pDirection, pEntity, dRange):
		'''
		Create a Distance Sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pDirection: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorDistance
		'''
		ret = self._oleobj_.InvokeTypes(10519, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pDirection, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorDistance', '{0CC3861B-CC2A-4402-9135-C8BC804EABBD}')
		return ret

	def CreateSensorSpeed(self, strName, pPosition, pDirection, pEntity, dRange):
		'''
		Create a Speed Sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pDirection: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorSpeed
		'''
		ret = self._oleobj_.InvokeTypes(10518, LCID, 1, (9, 0), ((8, 1), (8197, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pDirection, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorSpeed', '{CCB7E742-F0DF-4F22-A377-04AA675FD281}')
		return ret

	def CreateSensorTension(self, strName, pPosition, pEntity, dRange):
		'''
		Create a Tension Sensor
		
		:param strName: str
		:param pPosition: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorTension
		'''
		ret = self._oleobj_.InvokeTypes(10520, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorTension', '{55C49622-A503-4651-BF1E-2A84CD9E27AB}')
		return ret

	def CreateSensorTensionEx(self, strName, pPosition, pEntity, dRange):
		'''
		Create a Tension Sensor Extended
		
		:param strName: str
		:param pPosition: list[float]
		:param pEntity: IGeneric
		:param dRange: float
		:rtype: recurdyn.ProcessNet.ISensorTensionEx
		'''
		ret = self._oleobj_.InvokeTypes(10524, LCID, 1, (9, 0), ((8, 1), (8197, 1), (9, 1), (5, 1)),strName
			, pPosition, pEntity, dRange)
		if ret is not None:
			ret = Dispatch(ret, 'CreateSensorTensionEx', '{FD6480C3-36F4-4627-9725-6B484795DC39}')
		return ret

	def GetRDGeneric(self):
		'''
		FunctionBay Internal Use Only
		
		:rtype: int
		'''
		return self._oleobj_.InvokeTypes(51, LCID, 1, (20, 0), (),)


	def _get_AssemblyCollection(self):
		return self._ApplyTypes_(*(10522, 2, (9, 0), (), "AssemblyCollection", '{F695BFDC-1A2A-4C74-9908-D337B2FF62B8}'))
	def _get_ChainBodyCollection(self):
		return self._ApplyTypes_(*(10523, 2, (9, 0), (), "ChainBodyCollection", '{ED20A123-7EEE-4173-9F9C-2D37D1138E48}'))
	def _get_Comment(self):
		return self._ApplyTypes_(*(102, 2, (8, 0), (), "Comment", None))
	def _get_FullName(self):
		return self._ApplyTypes_(*(103, 2, (8, 0), (), "FullName", None))
	def _get_GeneralSubSystem(self):
		return self._ApplyTypes_(*(10500, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'))
	def _get_LinkCloneCollection(self):
		return self._ApplyTypes_(*(10521, 2, (9, 0), (), "LinkCloneCollection", '{BFBCE202-F4CB-40D0-8652-8DF819E5D886}'))
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

	AssemblyCollection = property(_get_AssemblyCollection, None)
	'''
	Get the Collection of Assembly

	:type: recurdyn.Chain.IChainAssemblyCollection
	'''
	ChainBodyCollection = property(_get_ChainBodyCollection, None)
	'''
	Get the Chain Body Collection of Assembly

	:type: recurdyn.Chain.IChainBodyCollection
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
	GeneralSubSystem = property(_get_GeneralSubSystem, None)
	'''
	General subsystem

	:type: recurdyn.ProcessNet.ISubSystem
	'''
	LinkCloneCollection = property(_get_LinkCloneCollection, None)
	'''
	Get the Collection of Clones

	:type: recurdyn.Chain.IChainLinkCloneCollection
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
		"AssemblyCollection": (10522, 2, (9, 0), (), "AssemblyCollection", '{F695BFDC-1A2A-4C74-9908-D337B2FF62B8}'),
		"ChainBodyCollection": (10523, 2, (9, 0), (), "ChainBodyCollection", '{ED20A123-7EEE-4173-9F9C-2D37D1138E48}'),
		"Comment": (102, 2, (8, 0), (), "Comment", None),
		"FullName": (103, 2, (8, 0), (), "FullName", None),
		"GeneralSubSystem": (10500, 2, (9, 0), (), "GeneralSubSystem", '{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}'),
		"LinkCloneCollection": (10521, 2, (9, 0), (), "LinkCloneCollection", '{BFBCE202-F4CB-40D0-8652-8DF819E5D886}'),
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

class IPoint3DWithRadiusAndCheckCollection(DispatchBaseClass):
	'''Point2D with Radius and Check Collection'''
	CLSID = IID('{314E0700-F8CC-4C1F-B1C3-0C0386F06A89}')
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

IChainAssembly_vtables_dispatch_ = 1
IChainAssembly_vtables_ = [
	(( 'BushingForceParameter' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{15D9554A-5BA8-4892-8AC3-1A026ED0FBCA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'LinkPlateShapeType' , 'pVal' , ), 10502, (10502, (), [ (3, 1, None, "IID('{70767D30-A128-49F0-BFC5-1CEE78841C28}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'LinkPlateShapeType' , 'pVal' , ), 10502, (10502, (), [ (16387, 10, None, "IID('{70767D30-A128-49F0-BFC5-1CEE78841C28}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'PassingBodyCollection' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{E26794CD-5D37-4617-BB5A-1AD85F3ED410}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'AddPassingBody' , 'pVal' , ), 10504, (10504, (), [ (9, 1, None, "IID('{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'DeletePassingBody' , 'pVal' , ), 10505, (10505, (), [ (9, 1, None, "IID('{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'LinkNumbers' , 'pVal' , ), 10506, (10506, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkInitialVelocityXAxis' , 'pVal' , ), 10507, (10507, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkInitialVelocityXAxis' , 'pVal' , ), 10507, (10507, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'LinkInitialVelocityXAxis' , 'ppVal' , ), 10508, (10508, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UpdateLinkInitialVelocityXAxis' , ), 10509, (10509, (), [ ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'GetOutputLinkList' , 'ppSafeArray' , ), 10510, (10510, (), [ (24584, 10, None, None) , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'AddOutputLink' , 'strFileName' , ), 10511, (10511, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'RemoveOutputLink' , 'strFileName' , ), 10512, (10512, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'AddAllOutputLink' , ), 10513, (10513, (), [ ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RemoveAllOutputLink' , ), 10514, (10514, (), [ ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10515, (10515, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10515, (10515, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'ChainBodyLinkCollection' , 'ppVal' , ), 10516, (10516, (), [ (16393, 10, None, "IID('{7DCEE901-515D-4780-AB01-89ECA089D8BE}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IChainAssemblyBushingForceParameter_vtables_dispatch_ = 1
IChainAssemblyBushingForceParameter_vtables_ = [
	(( 'TranslationStiffnessCoefficientRadial' , 'ppVal' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessCoefficientAxial' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessSpline' , 'pVal' , ), 10502, (10502, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessSpline' , 'pVal' , ), 10502, (10502, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineRadial' , 'ppVal' , ), 10503, (10503, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineRadial' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineAxial' , 'ppVal' , ), 10504, (10504, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessSplineAxial' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingCoefficientRadial' , 'ppVal' , ), 10505, (10505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingCoefficientAxial' , 'ppVal' , ), 10506, (10506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingSpline' , 'pVal' , ), 10507, (10507, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingSpline' , 'pVal' , ), 10507, (10507, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineRadial' , 'ppVal' , ), 10508, (10508, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineRadial' , 'ppVal' , ), 10508, (10508, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineAxial' , 'ppVal' , ), 10509, (10509, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingSplineAxial' , 'ppVal' , ), 10509, (10509, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'TranslationPreloadRadial' , 'ppVal' , ), 10510, (10510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'TranslationPreloadAxial' , 'ppVal' , ), 10511, (10511, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'TranslationClearance' , 'ppVal' , ), 10512, (10512, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessCoefficientX' , 'ppVal' , ), 10513, (10513, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessCoefficientY' , 'ppVal' , ), 10514, (10514, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessCoefficientZ' , 'ppVal' , ), 10515, (10515, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessSpline' , 'pVal' , ), 10516, (10516, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessSpline' , 'pVal' , ), 10516, (10516, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineX' , 'ppVal' , ), 10517, (10517, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineX' , 'ppVal' , ), 10517, (10517, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineY' , 'ppVal' , ), 10518, (10518, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineY' , 'ppVal' , ), 10518, (10518, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineZ' , 'ppVal' , ), 10519, (10519, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessSplineZ' , 'ppVal' , ), 10519, (10519, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingCoefficientX' , 'ppVal' , ), 10520, (10520, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingCoefficientY' , 'ppVal' , ), 10521, (10521, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingCoefficientZ' , 'ppVal' , ), 10522, (10522, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingSpline' , 'pVal' , ), 10523, (10523, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingSpline' , 'pVal' , ), 10523, (10523, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineX' , 'ppVal' , ), 10524, (10524, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineX' , 'ppVal' , ), 10524, (10524, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineY' , 'ppVal' , ), 10525, (10525, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineY' , 'ppVal' , ), 10525, (10525, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineZ' , 'ppVal' , ), 10526, (10526, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingSplineZ' , 'ppVal' , ), 10526, (10526, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RotationPreloadX' , 'ppVal' , ), 10527, (10527, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'RotationPreloadY' , 'ppVal' , ), 10528, (10528, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'RotationPreloadZ' , 'ppVal' , ), 10529, (10529, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'UseFriction' , 'pVal' , ), 10530, (10530, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'UseFriction' , 'pVal' , ), 10530, (10530, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'Friction' , 'ppVal' , ), 10531, (10531, (), [ (16393, 10, None, "IID('{6F6A35D3-97FF-494A-8E1A-DF4E8101EBDB}')") , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 10532, (10532, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationStiffnessExponent' , 'pVal' , ), 10532, (10532, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessExponentRadial' , 'ppVal' , ), 10533, (10533, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'TranslationStiffnessExponentAxial' , 'ppVal' , ), 10534, (10534, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 10535, (10535, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'UseTranslationDampingExponent' , 'pVal' , ), 10535, (10535, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingExponentRadial' , 'ppVal' , ), 10536, (10536, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'TranslationDampingExponentAxial' , 'ppVal' , ), 10537, (10537, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 10538, (10538, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationStiffnessExponent' , 'pVal' , ), 10538, (10538, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponentX' , 'ppVal' , ), 10539, (10539, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponentY' , 'ppVal' , ), 10540, (10540, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
	(( 'RotationStiffnessExponentZ' , 'ppVal' , ), 10541, (10541, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 528 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 10542, (10542, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 536 , (3, 0, None, None) , 0 , )),
	(( 'UseRotationDampingExponent' , 'pVal' , ), 10542, (10542, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 544 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponentX' , 'ppVal' , ), 10543, (10543, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 552 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponentY' , 'ppVal' , ), 10544, (10544, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 560 , (3, 0, None, None) , 0 , )),
	(( 'RotationDampingExponentZ' , 'ppVal' , ), 10545, (10545, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 568 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 10546, (10546, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 576 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 10547, (10547, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 584 , (3, 0, None, None) , 0 , )),
]

IChainAssemblyCollection_vtables_dispatch_ = 1
IChainAssemblyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{0963256F-0F65-4E93-8FFA-B58651838BC6}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IChainAssemblyContactFriction_vtables_dispatch_ = 1
IChainAssemblyContactFriction_vtables_ = [
	(( 'PinDiameter' , 'ppVal' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'DynamicFrictionCoefficient' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChainBody_vtables_dispatch_ = 1
IChainBody_vtables_ = [
	(( 'GeneralBody' , 'ppVal' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{26ED5B8E-FF6B-45C8-B6A9-0AA52F6A27B8}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IChainBodyCollection_vtables_dispatch_ = 1
IChainBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IChainBodyGuardLateral_vtables_dispatch_ = 1
IChainBodyGuardLateral_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 10550, (10550, (), [ (16393, 10, None, "IID('{8907B76F-36EF-42E8-AA90-2C02C76EF56F}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{82124DDF-C246-49F1-86B3-8DAD3B875DDD}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{134391CE-930C-47BE-983B-B326A771F701}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IChainBodyGuide_vtables_dispatch_ = 1
IChainBodyGuide_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 10550, (10550, (), [ (16393, 10, None, "IID('{1E51E4E8-E4DC-4C00-BBCB-816315723567}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{F2988F5F-6804-4797-9633-0BD1C78C4366}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{134391CE-930C-47BE-983B-B326A771F701}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'pVal' , ), 10553, (10553, (), [ (3, 1, None, "IID('{5252E329-CB8E-4D92-AA30-EB87B577E633}')") , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'NormalDirection' , 'pVal' , ), 10553, (10553, (), [ (16387, 10, None, "IID('{5252E329-CB8E-4D92-AA30-EB87B577E633}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10554, (10554, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10554, (10554, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10561, (10561, (), [ ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IChainBodyLink_vtables_dispatch_ = 1
IChainBodyLink_vtables_ = [
	(( 'UseBodyGraphic' , 'pVal' , ), 10501, (10501, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseBodyGraphic' , 'pVal' , ), 10501, (10501, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Graphic' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{CB9C645A-A4F6-4F6A-855A-6CBAC8B59BCB}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IChainBodyLinkCollection_vtables_dispatch_ = 1
IChainBodyLinkCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{A04DEA81-0603-4F81-91F5-D11FF259F6A1}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IChainBodyLinkMultiplexOffset_vtables_dispatch_ = 1
IChainBodyLinkMultiplexOffset_vtables_ = [
]

IChainBodyLinkMultiplexPin_vtables_dispatch_ = 1
IChainBodyLinkMultiplexPin_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{33736DE9-40C6-42C3-96EB-72FD82D10535}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10552, (10552, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IChainBodyLinkMultiplexRoller_vtables_dispatch_ = 1
IChainBodyLinkMultiplexRoller_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10552, (10552, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IChainBodyLinkOffset_vtables_dispatch_ = 1
IChainBodyLinkOffset_vtables_ = [
]

IChainBodyLinkPin_vtables_dispatch_ = 1
IChainBodyLinkPin_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{B4B7B26A-F4EB-486F-9909-74DA518613C4}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10552, (10552, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IChainBodyLinkRoller_vtables_dispatch_ = 1
IChainBodyLinkRoller_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{E6301A79-B289-4188-B213-AE53CA9E89BB}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10552, (10552, (), [ ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
]

IChainBodyLinkSilentInner_vtables_dispatch_ = 1
IChainBodyLinkSilentInner_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10553, (10553, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IChainBodyLinkSilentOuter_vtables_dispatch_ = 1
IChainBodyLinkSilentOuter_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10553, (10553, (), [ ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IChainBodyRoller_vtables_dispatch_ = 1
IChainBodyRoller_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 10550, (10550, (), [ (16393, 10, None, "IID('{8907B76F-36EF-42E8-AA90-2C02C76EF56F}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{2137EA2C-652F-4C83-B265-17AB71E0E202}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{134391CE-930C-47BE-983B-B326A771F701}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
]

IChainBodySprocketMultiplex_vtables_dispatch_ = 1
IChainBodySprocketMultiplex_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 10550, (10550, (), [ (16393, 10, None, "IID('{8907B76F-36EF-42E8-AA90-2C02C76EF56F}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SideContactProperty' , 'ppVal' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{8907B76F-36EF-42E8-AA90-2C02C76EF56F}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{84F6AAEF-A7BD-4C0E-A1B9-3377E4E8398B}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 10553, (10553, (), [ (16393, 10, None, "IID('{134391CE-930C-47BE-983B-B326A771F701}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
]

IChainBodySprocketRoller_vtables_dispatch_ = 1
IChainBodySprocketRoller_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 10550, (10550, (), [ (16393, 10, None, "IID('{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SideContactProperty' , 'ppVal' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{8907B76F-36EF-42E8-AA90-2C02C76EF56F}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{71E9EDCA-8586-4BC4-8C96-CA6CE987B7C7}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 10553, (10553, (), [ (16393, 10, None, "IID('{134391CE-930C-47BE-983B-B326A771F701}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10554, (10554, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10554, (10554, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IChainBodySprocketSilent_vtables_dispatch_ = 1
IChainBodySprocketSilent_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 10550, (10550, (), [ (16393, 10, None, "IID('{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'SideContactProperty' , 'ppVal' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{8907B76F-36EF-42E8-AA90-2C02C76EF56F}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{46136858-6824-49C4-A14E-EC6C582E3C6D}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'ContactSearch' , 'ppVal' , ), 10553, (10553, (), [ (16393, 10, None, "IID('{134391CE-930C-47BE-983B-B326A771F701}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10554, (10554, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10554, (10554, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
]

IChainContactFriction_vtables_dispatch_ = 1
IChainContactFriction_vtables_ = [
	(( 'StaticThresholdVelocity' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'DynamicThresholdVelocity' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'StaticFrictionCoefficient' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IChainContactPairInfo_vtables_dispatch_ = 1
IChainContactPairInfo_vtables_ = [
	(( 'CheckContactPair' , 'pVal' , ), 10501, (10501, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'CheckContactPair' , 'pVal' , ), 10501, (10501, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'LinkSegmentNumber' , 'pVal' , ), 10502, (10502, (), [ (8, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'LinkSegmentNumber' , 'pVal' , ), 10502, (10502, (), [ (16392, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
]

IChainContactPairInfoCollection_vtables_dispatch_ = 1
IChainContactPairInfoCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{4BCBE390-C6BB-4E5A-9DA3-40A756B8326F}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IChainContactProperty_vtables_dispatch_ = 1
IChainContactProperty_vtables_ = [
	(( 'StiffnessCoefficient' , 'ppVal' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 10501, (10501, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 10501, (10501, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 10502, (10502, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 10504, (10504, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 10504, (10504, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 10505, (10505, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 10505, (10505, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 10506, (10506, (), [ (3, 1, None, "IID('{6A354324-DD66-4599-9FB4-13728425522F}')") , ], 1 , 4 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'FrictionType' , 'pVal' , ), 10506, (10506, (), [ (16387, 10, None, "IID('{6A354324-DD66-4599-9FB4-13728425522F}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'FrictionCoefficient' , 'ppVal' , ), 10507, (10507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 10508, (10508, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'FrictionSpline' , 'ppVal' , ), 10508, (10508, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 10509, (10509, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 10509, (10509, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 10510, (10510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 10511, (10511, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 10511, (10511, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 10512, (10512, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 10513, (10513, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseIndentationExponent' , 'pVal' , ), 10513, (10513, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'IndentationExponent' , 'ppVal' , ), 10514, (10514, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseMoreFrictionData' , 'pVal' , ), 10515, (10515, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseMoreFrictionData' , 'pVal' , ), 10515, (10515, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'Friction' , 'ppVal' , ), 10516, (10516, (), [ (16393, 10, None, "IID('{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
]

IChainContactPropertySprocket_vtables_dispatch_ = 1
IChainContactPropertySprocket_vtables_ = [
	(( 'NumberofMaxContactPoints' , 'pVal' , ), 10551, (10551, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'NumberofMaxContactPoints' , 'pVal' , ), 10551, (10551, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseContactOutputFile' , 'pVal' , ), 10552, (10552, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseContactOutputFile' , 'pVal' , ), 10552, (10552, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
]

IChainContactSearch_vtables_dispatch_ = 1
IChainContactSearch_vtables_ = [
	(( 'Type' , 'pVal' , ), 10500, (10500, (), [ (3, 1, None, "IID('{00000000-0000-0000-0000-000000000000}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Type' , 'pVal' , ), 10500, (10500, (), [ (16387, 10, None, "IID('{00000000-0000-0000-0000-000000000000}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseUserBoundaryForPartialSearch' , 'pVal' , ), 10501, (10501, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseUserBoundaryForPartialSearch' , 'pVal' , ), 10501, (10501, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'UserBoundaryForPartialSearch' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChainGeometryGroupGuideArc_vtables_dispatch_ = 1
IChainGeometryGroupGuideArc_vtables_ = [
	(( 'PointsType' , 'pVal' , ), 10500, (10500, (), [ (3, 1, None, "IID('{ADC464BD-C49B-4632-938A-6FC04B6A492E}')") , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'PointsType' , 'pVal' , ), 10500, (10500, (), [ (16387, 10, None, "IID('{ADC464BD-C49B-4632-938A-6FC04B6A492E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'PassingPoints' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'CenterPointsAndRadius' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}')") , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'CenterPointsAndArcAngle' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'ViewReferenceFrame' , 'ppVal' , ), 10504, (10504, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'ViewReferenceFrame' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 10505, (10505, (), [ (19, 1, None, None) , ], 1 , 4 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'Color' , 'pVal' , ), 10505, (10505, (), [ (16403, 10, None, None) , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 10506, (10506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'ppVal' , ), 10507, (10507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'DepthNormalVector' , 'pVal' , ), 10508, (10508, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'DepthNormalVector' , 'pVal' , ), 10508, (10508, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'UseOnlyLinkRollerContact' , 'pVal' , ), 10509, (10509, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'UseOnlyLinkRollerContact' , 'pVal' , ), 10509, (10509, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'PointStart' , 'pVal' , ), 10510, (10510, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'PointStart' , 'pVal' , ), 10510, (10510, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PointEnd' , 'pVal' , ), 10511, (10511, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PointEnd' , 'pVal' , ), 10511, (10511, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'UseGroupGuideArcCharacteristic' , 'pVal' , ), 10512, (10512, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UseGroupGuideArcCharacteristic' , 'pVal' , ), 10512, (10512, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessCoefficient' , 'ppVal' , ), 10513, (10513, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 10514, (10514, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessSpline' , 'pVal' , ), 10514, (10514, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 10515, (10515, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessSpline' , 'ppVal' , ), 10515, (10515, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'DampingCoefficient' , 'ppVal' , ), 10516, (10516, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 10517, (10517, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingSpline' , 'pVal' , ), 10517, (10517, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 10518, (10518, (), [ (9, 1, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'DampingSpline' , 'ppVal' , ), 10518, (10518, (), [ (16393, 10, None, "IID('{E76144D2-715D-41B4-A432-7B6C7F713FC2}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 10519, (10519, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'UseStiffnessExponent' , 'pVal' , ), 10519, (10519, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'StiffnessExponent' , 'ppVal' , ), 10520, (10520, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 10521, (10521, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UseDampingExponent' , 'pVal' , ), 10521, (10521, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'DampingExponent' , 'ppVal' , ), 10522, (10522, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
]

IChainGeometryGuardLateral_vtables_dispatch_ = 1
IChainGeometryGuardLateral_vtables_ = [
	(( 'Length' , 'ppVal' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Height' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'InnerWidth' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Thickness' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'InactiveType' , 'pVal' , ), 10504, (10504, (), [ (3, 1, None, "IID('{674BB7BB-6BE5-41B4-93AA-649213BBDA72}')") , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'InactiveType' , 'pVal' , ), 10504, (10504, (), [ (16387, 10, None, "IID('{674BB7BB-6BE5-41B4-93AA-649213BBDA72}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
]

IChainGeometryGuide_vtables_dispatch_ = 1
IChainGeometryGuide_vtables_ = [
	(( 'PointsType' , 'pVal' , ), 10500, (10500, (), [ (3, 1, None, "IID('{ADC464BD-C49B-4632-938A-6FC04B6A492E}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PointsType' , 'pVal' , ), 10500, (10500, (), [ (16387, 10, None, "IID('{ADC464BD-C49B-4632-938A-6FC04B6A492E}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PassingPoints' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{E6353564-8957-4E10-8A7B-12F98C5ECCFB}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CenterPointsAndRadius' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{E6353564-8957-4E10-8A7B-12F98C5ECCFB}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CenterPointsAndArcAngle' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{E6353564-8957-4E10-8A7B-12F98C5ECCFB}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfPoints' , 'pVal' , ), 10504, (10504, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ViewReferenceFrame' , 'ppVal' , ), 10505, (10505, (), [ (9, 1, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ViewReferenceFrame' , 'ppVal' , ), 10505, (10505, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Depth' , 'ppVal' , ), 10506, (10506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseOnlyLinkRollerContact' , 'pVal' , ), 10507, (10507, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseOnlyLinkRollerContact' , 'pVal' , ), 10507, (10507, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseSolidGeometry' , 'pVal' , ), 10508, (10508, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseSolidGeometry' , 'pVal' , ), 10508, (10508, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'PointStart' , 'ppVal' , ), 10509, (10509, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'PointStart' , 'ppVal' , ), 10509, (10509, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'PointEnd' , 'ppVal' , ), 10510, (10510, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'PointEnd' , 'ppVal' , ), 10510, (10510, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IChainGeometryLinkMultiplexPin_vtables_dispatch_ = 1
IChainGeometryLinkMultiplexPin_vtables_ = [
	(( 'LinkType' , 'pVal' , ), 10501, (10501, (), [ (16387, 10, None, "IID('{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Pitch' , 'pVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfStrands' , 'pVal' , ), 10503, (10503, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PitchTransverse' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RollerDiameter' , 'ppVal' , ), 10505, (10505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkPinThickness' , 'ppVal' , ), 10509, (10509, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkPinHeight' , 'ppVal' , ), 10510, (10510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'PinDiameter' , 'ppVal' , ), 10511, (10511, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 10512, (10512, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
]

IChainGeometryLinkMultiplexRoller_vtables_dispatch_ = 1
IChainGeometryLinkMultiplexRoller_vtables_ = [
	(( 'LinkType' , 'pVal' , ), 10501, (10501, (), [ (16387, 10, None, "IID('{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Pitch' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfStrands' , 'pVal' , ), 10503, (10503, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PitchTransverse' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RollerDiameter' , 'ppVal' , ), 10505, (10505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkRollerWidth' , 'ppVal' , ), 10506, (10506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkRollerThickness' , 'ppVal' , ), 10507, (10507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkRollerHeight' , 'ppVal' , ), 10508, (10508, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'PinDiameter' , 'ppVal' , ), 10511, (10511, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 10512, (10512, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 10513, (10513, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 10513, (10513, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 10514, (10514, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 10514, (10514, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 10515, (10515, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 10515, (10515, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 10516, (10516, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 10516, (10516, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
]

IChainGeometryLinkPin_vtables_dispatch_ = 1
IChainGeometryLinkPin_vtables_ = [
	(( 'LinkType' , 'pVal' , ), 10501, (10501, (), [ (3, 1, None, "IID('{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'LinkType' , 'pVal' , ), 10501, (10501, (), [ (16387, 10, None, "IID('{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Pitch' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RollerDiameter' , 'ppVal' , ), 10505, (10505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RollerWidth' , 'ppVal' , ), 10506, (10506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkPinWidth' , 'ppVal' , ), 10507, (10507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkPinThickness' , 'ppVal' , ), 10508, (10508, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkPinHeight' , 'ppVal' , ), 10509, (10509, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'PinDiameter' , 'ppVal' , ), 10510, (10510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 10511, (10511, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
]

IChainGeometryLinkRoller_vtables_dispatch_ = 1
IChainGeometryLinkRoller_vtables_ = [
	(( 'LinkType' , 'pVal' , ), 10501, (10501, (), [ (3, 1, None, "IID('{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'LinkType' , 'pVal' , ), 10501, (10501, (), [ (16387, 10, None, "IID('{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfLinkSets' , 'pVal' , ), 10502, (10502, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'Pitch' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'RollerDiameter' , 'ppVal' , ), 10505, (10505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RollerWidth' , 'ppVal' , ), 10506, (10506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkRollerWidth' , 'ppVal' , ), 10507, (10507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkRollerThickness' , 'ppVal' , ), 10508, (10508, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'PlateLinkRollerHeight' , 'ppVal' , ), 10509, (10509, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'PinDiameter' , 'ppVal' , ), 10510, (10510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 10511, (10511, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 10512, (10512, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 10512, (10512, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 10513, (10513, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 10513, (10513, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 10514, (10514, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 10514, (10514, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 10515, (10515, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 10515, (10515, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

IChainGeometryLinkSilentInner_vtables_dispatch_ = 1
IChainGeometryLinkSilentInner_vtables_ = [
	(( 'Pitch' , 'ppVal' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'PlateThickness' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PinRadius' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'UseSingleInnerLink' , 'pVal' , ), 10504, (10504, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseSingleInnerLink' , 'pVal' , ), 10504, (10504, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 10505, (10505, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 10505, (10505, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 10506, (10506, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 10506, (10506, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 10507, (10507, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 10507, (10507, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 10508, (10508, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 10508, (10508, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IChainGeometryLinkSilentOuter_vtables_dispatch_ = 1
IChainGeometryLinkSilentOuter_vtables_ = [
	(( 'Pitch' , 'ppVal' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'OuterLinkTotalWidth' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'PlateThickness' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'PinRadius' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'PinLength' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 10505, (10505, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'UseBushingPosition' , 'pVal' , ), 10505, (10505, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 10506, (10506, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'LeftBushingPosition' , 'pVal' , ), 10506, (10506, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 10507, (10507, (), [ (24581, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RightBushingPosition' , 'pVal' , ), 10507, (10507, (), [ (8197, 1, None, None) , ], 1 , 4 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 10508, (10508, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'BushingWidth' , 'pVal' , ), 10508, (10508, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

IChainGeometryRoller_vtables_dispatch_ = 1
IChainGeometryRoller_vtables_ = [
	(( 'WidthRoller' , 'ppVal' , ), 10601, (10601, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'WidthTotal' , 'ppVal' , ), 10602, (10602, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'RadiusRoller' , 'ppVal' , ), 10603, (10603, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RadiusFrange' , 'ppVal' , ), 10604, (10604, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
]

IChainGeometrySprocketMultiplex_vtables_dispatch_ = 1
IChainGeometrySprocketMultiplex_vtables_ = [
	(( 'NumberOfStrands' , 'pVal' , ), 10551, (10551, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 504 , (3, 0, None, None) , 0 , )),
	(( 'NumberOfStrands' , 'pVal' , ), 10551, (10551, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 512 , (3, 0, None, None) , 0 , )),
	(( 'PitchTransverse' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 520 , (3, 0, None, None) , 0 , )),
]

IChainGeometrySprocketRoller_vtables_dispatch_ = 1
IChainGeometrySprocketRoller_vtables_ = [
	(( 'SprocketType' , 'pVal' , ), 10501, (10501, (), [ (3, 1, None, "IID('{BE5ED324-09C1-462B-8D26-DB09D5B18BF6}')") , ], 1 , 4 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'SprocketType' , 'pVal' , ), 10501, (10501, (), [ (16387, 10, None, "IID('{BE5ED324-09C1-462B-8D26-DB09D5B18BF6}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'WidthTeeth' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'RadiusWheel' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'WidthWheels' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'NumberofTeeth' , 'pVal' , ), 10505, (10505, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'NumberofTeeth' , 'pVal' , ), 10505, (10505, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'DiameterPitchISO606' , 'pVal' , ), 10506, (10506, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'DiameterTipISO606' , 'pVal' , ), 10507, (10507, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'DiameterRootISO606' , 'pVal' , ), 10508, (10508, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'RadiusTFlankISO606' , 'pVal' , ), 10509, (10509, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'DiameterPitchParameter' , 'ppVal' , ), 10510, (10510, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'DiameterTipParameter' , 'ppVal' , ), 10511, (10511, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'DiameterRootParameter' , 'ppVal' , ), 10512, (10512, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'RadiusTFlankParameter' , 'ppVal' , ), 10513, (10513, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'RadiusDedendum' , 'ppVal' , ), 10514, (10514, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'RadiusPitch' , 'ppVal' , ), 10515, (10515, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'RadiusBase' , 'ppVal' , ), 10516, (10516, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'RadiusAddendum' , 'ppVal' , ), 10517, (10517, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'ChainLinkRollerCircleRadiusRoller' , 'pVal' , ), 10518, (10518, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'ChainLinkRollerCircleRadiusRoller' , 'pVal' , ), 10518, (10518, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
	(( 'ChainLinkRollerCircleRadiusLoop' , 'pVal' , ), 10519, (10519, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 352 , (3, 0, None, None) , 0 , )),
	(( 'ChainLinkRollerCircleRadiusLoop' , 'pVal' , ), 10519, (10519, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 360 , (3, 0, None, None) , 0 , )),
	(( 'RollerSeatingRadiusISO606' , 'pVal' , ), 10520, (10520, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 368 , (3, 0, None, None) , 0 , )),
	(( 'RollerSeatingAngleISO606' , 'pVal' , ), 10521, (10521, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 376 , (3, 0, None, None) , 0 , )),
	(( 'RollerSeatingRadiusParameter' , 'ppVal' , ), 10522, (10522, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 384 , (3, 0, None, None) , 0 , )),
	(( 'RollerSeatingAngleParameter' , 'ppVal' , ), 10523, (10523, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 392 , (3, 0, None, None) , 0 , )),
	(( 'RollerLinkPitch' , 'pVal' , ), 10524, (10524, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 400 , (3, 0, None, None) , 0 , )),
	(( 'RollerLinkPitch' , 'pVal' , ), 10524, (10524, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 408 , (3, 0, None, None) , 0 , )),
	(( 'RollerLinkDiameter' , 'pVal' , ), 10525, (10525, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 416 , (3, 0, None, None) , 0 , )),
	(( 'RollerLinkDiameter' , 'pVal' , ), 10525, (10525, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 424 , (3, 0, None, None) , 0 , )),
	(( 'UpdatefromISO606Lib' , ), 10526, (10526, (), [ ], 1 , 1 , 4 , 0 , 432 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkAssemblyAssembledRadius' , 'pVal' , ), 10527, (10527, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 440 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkAssemblyAssembledRadius' , 'pVal' , ), 10527, (10527, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 448 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyAssembledRadius' , 'pVal' , ), 10528, (10528, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 456 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyAssembledRadius' , 'pVal' , ), 10528, (10528, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 464 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyRadialDistance' , 'pVal' , ), 10529, (10529, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 472 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyRadialDistance' , 'pVal' , ), 10529, (10529, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 480 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppVal' , ), 10530, (10530, (), [ (16393, 10, None, "IID('{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}')") , ], 1 , 2 , 4 , 0 , 488 , (3, 0, None, None) , 0 , )),
	(( 'UpdateProperties' , ), 10531, (10531, (), [ ], 1 , 1 , 4 , 0 , 496 , (3, 0, None, None) , 0 , )),
]

IChainGeometrySprocketSilent_vtables_dispatch_ = 1
IChainGeometrySprocketSilent_vtables_ = [
	(( 'RadiusWheelSprocket' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'WidthofTeeth' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'WidthbetweenWheels' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'NumberofTeeth' , 'pVal' , ), 10504, (10504, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'NumberofTeeth' , 'pVal' , ), 10504, (10504, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'RadiusCircleDedendum' , 'ppVal' , ), 10505, (10505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'RadiusCircleBase' , 'ppVal' , ), 10506, (10506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'RadiusCirclePitch' , 'ppVal' , ), 10507, (10507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'RadiusCircleAddendum' , 'ppVal' , ), 10508, (10508, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'ChainLinkPinCircleRadiusPin' , 'pVal' , ), 10509, (10509, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'ChainLinkPinCircleRadiusPin' , 'pVal' , ), 10509, (10509, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'ChainLinkPinCircleRadiusLoop' , 'pVal' , ), 10510, (10510, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'ChainLinkPinCircleRadiusLoop' , 'pVal' , ), 10510, (10510, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkAssemblyAssembledRadius' , 'pVal' , ), 10511, (10511, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'UseLinkAssemblyAssembledRadius' , 'pVal' , ), 10511, (10511, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyAssembledRadius' , 'pVal' , ), 10512, (10512, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyAssembledRadius' , 'pVal' , ), 10512, (10512, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyRadialDistance' , 'pVal' , ), 10513, (10513, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'LinkAssemblyRadialDistance' , 'pVal' , ), 10513, (10513, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppVal' , ), 10514, (10514, (), [ (16393, 10, None, "IID('{BD4851C8-8A99-4B29-80AE-2E160DC0754C}')") , ], 1 , 2 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'UpdateProperties' , ), 10515, (10515, (), [ ], 1 , 1 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
]

IChainGroupGuideArc_vtables_dispatch_ = 1
IChainGroupGuideArc_vtables_ = [
	(( 'ContactProperty' , 'ppVal' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{1E51E4E8-E4DC-4C00-BBCB-816315723567}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Geometry' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{B0B8CBCE-6E48-4300-9436-0599707E3C93}')") , ], 1 , 2 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10502, (10502, (), [ (3, 1, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 4 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'ForceDisplay' , 'pVal' , ), 10502, (10502, (), [ (16387, 10, None, "IID('{DEB6BDB3-9D28-4F34-953B-9D96D9A147ED}')") , ], 1 , 2 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'UseTotalMass' , 'pVal' , ), 10503, (10503, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'UseTotalMass' , 'pVal' , ), 10503, (10503, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'TotalMass' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoUpdateGeometry' , 'pVal' , ), 10505, (10505, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'UseAutoUpdateGeometry' , 'pVal' , ), 10505, (10505, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10511, (10511, (), [ ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
]

IChainGroupGuidePointsWithAdditionalInfo_vtables_dispatch_ = 1
IChainGroupGuidePointsWithAdditionalInfo_vtables_ = [
	(( 'x' , 'pVal' , ), 10501, (10501, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'x' , 'pVal' , ), 10501, (10501, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'y' , 'pVal' , ), 10502, (10502, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'y' , 'pVal' , ), 10502, (10502, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'z' , 'pVal' , ), 10503, (10503, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'z' , 'pVal' , ), 10503, (10503, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AdditionalInfo' , 'pVal' , ), 10504, (10504, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AdditionalInfo' , 'pVal' , ), 10504, (10504, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IChainGroupGuidePointsWithAdditionalInfoCollection_vtables_dispatch_ = 1
IChainGroupGuidePointsWithAdditionalInfoCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{0954FD4A-BE83-4A47-A022-39343EABBB1B}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IChainGuideContactProperty_vtables_dispatch_ = 1
IChainGuideContactProperty_vtables_ = [
	(( 'NumberofMaxContactPoints' , 'pVal' , ), 10551, (10551, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'NumberofMaxContactPoints' , 'pVal' , ), 10551, (10551, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
]

IChainGuidePointsWithAdditionalInfo_vtables_dispatch_ = 1
IChainGuidePointsWithAdditionalInfo_vtables_ = [
	(( 'x' , 'pVal' , ), 10501, (10501, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'x' , 'pVal' , ), 10501, (10501, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'y' , 'pVal' , ), 10502, (10502, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'y' , 'pVal' , ), 10502, (10502, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'z' , 'pVal' , ), 10503, (10503, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'z' , 'pVal' , ), 10503, (10503, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'AdditionalInfo' , 'pVal' , ), 10504, (10504, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'AdditionalInfo' , 'pVal' , ), 10504, (10504, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
]

IChainGuidePointsWithAdditionalInfoCollection_vtables_dispatch_ = 1
IChainGuidePointsWithAdditionalInfoCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{B512AC12-46CE-4A35-B10B-1A83C7C91457}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IChainInvoluteCurveParameter_vtables_dispatch_ = 1
IChainInvoluteCurveParameter_vtables_ = [
	(( 'Theta' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Phi1' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Phi2' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
]

IChainLinkClone_vtables_dispatch_ = 1
IChainLinkClone_vtables_ = [
	(( 'Graphic' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{4C8B7C23-7D92-4D39-B530-5D93DC97F771}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Mass' , 'ppVal' , ), 10502, (10502, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'Ixx' , 'ppVal' , ), 10503, (10503, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'Iyy' , 'ppVal' , ), 10504, (10504, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'Izz' , 'ppVal' , ), 10505, (10505, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'Ixy' , 'ppVal' , ), 10506, (10506, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'Iyz' , 'ppVal' , ), 10507, (10507, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'Izx' , 'ppVal' , ), 10508, (10508, (), [ (16393, 10, None, "IID('{2B5166E3-4B31-4607-B157-BE237A670336}')") , ], 1 , 2 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'MaterialInput' , 'pVal' , ), 10509, (10509, (), [ (3, 1, None, "IID('{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}')") , ], 1 , 4 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'MaterialInput' , 'pVal' , ), 10509, (10509, (), [ (16387, 10, None, "IID('{4DD8B94B-8CB3-4C58-8171-E897A8BC94F4}')") , ], 1 , 2 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'pVal' , ), 10510, (10510, (), [ (3, 1, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 4 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'Material' , 'pVal' , ), 10510, (10510, (), [ (16387, 10, None, "IID('{EF682F61-990D-40D7-9A4C-46391963D599}')") , ], 1 , 2 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 10511, (10511, (), [ (5, 1, None, None) , ], 1 , 4 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'Density' , 'pVal' , ), 10511, (10511, (), [ (16389, 10, None, None) , ], 1 , 2 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'MaterialUser' , 'pVal' , ), 10512, (10512, (), [ (9, 1, None, "IID('{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}')") , ], 1 , 4 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'MaterialUser' , 'pVal' , ), 10512, (10512, (), [ (16393, 10, None, "IID('{AE7DE34C-11E0-48FD-B8E5-423996FF7DF2}')") , ], 1 , 2 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CenterMarker' , 'pVal' , ), 10513, (10513, (), [ (16393, 10, None, "IID('{6B6F192C-B83F-4503-89E8-5CAB8DE726AA}')") , ], 1 , 2 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'InitialBodyGraphicFlag' , ), 10514, (10514, (), [ ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'FileImport' , 'strFile' , ), 10515, (10515, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'FileExport' , 'strFile' , 'OverWrite' , ), 10516, (10516, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 10517, (10517, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'Active' , 'pVal' , ), 10517, (10517, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
]

IChainLinkCloneCollection_vtables_dispatch_ = 1
IChainLinkCloneCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{3C283940-AAB3-48D1-A521-D8AA43058BC2}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IChainLinkCloneMultiplexOffset_vtables_dispatch_ = 1
IChainLinkCloneMultiplexOffset_vtables_ = [
]

IChainLinkCloneMultiplexPin_vtables_dispatch_ = 1
IChainLinkCloneMultiplexPin_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{33736DE9-40C6-42C3-96EB-72FD82D10535}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10552, (10552, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

IChainLinkCloneMultiplexRoller_vtables_dispatch_ = 1
IChainLinkCloneMultiplexRoller_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10552, (10552, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'LinkPlateShapeType' , 'pVal' , ), 10553, (10553, (), [ (3, 1, None, "IID('{70767D30-A128-49F0-BFC5-1CEE78841C28}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'LinkPlateShapeType' , 'pVal' , ), 10553, (10553, (), [ (16387, 10, None, "IID('{70767D30-A128-49F0-BFC5-1CEE78841C28}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
]

IChainLinkCloneOffset_vtables_dispatch_ = 1
IChainLinkCloneOffset_vtables_ = [
]

IChainLinkClonePin_vtables_dispatch_ = 1
IChainLinkClonePin_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{B4B7B26A-F4EB-486F-9909-74DA518613C4}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10552, (10552, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
]

IChainLinkCloneRoller_vtables_dispatch_ = 1
IChainLinkCloneRoller_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{E6301A79-B289-4188-B213-AE53CA9E89BB}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10552, (10552, (), [ ], 1 , 1 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'LinkPlateShapeType' , 'pVal' , ), 10553, (10553, (), [ (3, 1, None, "IID('{70767D30-A128-49F0-BFC5-1CEE78841C28}')") , ], 1 , 4 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
	(( 'LinkPlateShapeType' , 'pVal' , ), 10553, (10553, (), [ (16387, 10, None, "IID('{70767D30-A128-49F0-BFC5-1CEE78841C28}')") , ], 1 , 2 , 4 , 0 , 344 , (3, 0, None, None) , 0 , )),
]

IChainLinkCloneSilentInner_vtables_dispatch_ = 1
IChainLinkCloneSilentInner_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10553, (10553, (), [ ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IChainLinkCloneSilentOuter_vtables_dispatch_ = 1
IChainLinkCloneSilentOuter_vtables_ = [
	(( 'Geometry' , 'ppGeometry' , ), 10551, (10551, (), [ (16393, 10, None, "IID('{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'Profile' , 'ppVal' , ), 10552, (10552, (), [ (16393, 10, None, "IID('{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'UpdateGeometry' , ), 10553, (10553, (), [ ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IChainPassingBodyCollection_vtables_dispatch_ = 1
IChainPassingBodyCollection_vtables_ = [
	(( 'Item' , 'var' , 'ppVal' , ), 0, (0, (), [ (12, 1, None, None) , 
			 (16393, 10, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Count' , 'pVal' , ), 1, (1, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( '_NewEnum' , 'ppEnum' , ), -4, (-4, (), [ (16397, 10, None, None) , ], 1 , 2 , 4 , 0 , 72 , (3, 0, None, None) , 1 , )),
]

IChainProfileLinkSilent_vtables_dispatch_ = 1
IChainProfileLinkSilent_vtables_ = [
	(( 'PointCollection' , 'ppVal' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{2C0D70A3-D197-4781-940A-1672F3B420B9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'ContactPairInfoCollection' , 'ppVal' , ), 10501, (10501, (), [ (16393, 10, None, "IID('{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}')") , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 10502, (10502, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 10503, (10503, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'GuideRollerContactNodeStart' , 'pVal' , ), 10504, (10504, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'GuideRollerContactNodeStart' , 'pVal' , ), 10504, (10504, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'GuideRollerContactNodeEnd' , 'pVal' , ), 10505, (10505, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'GuideRollerContactNodeEnd' , 'pVal' , ), 10505, (10505, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'GuideRollerContactLengthSegment' , 'pVal' , ), 10506, (10506, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'GuideRollerContactLengthSegment' , 'pVal' , ), 10506, (10506, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'dX' , 'dY' , 'dR' , 'bCheckContactPair' , 
			 ), 10507, (10507, (), [ (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 10508, (10508, (), [ ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
]

IChainProfileSprocket_vtables_dispatch_ = 1
IChainProfileSprocket_vtables_ = [
	(( 'PointCollection' , 'ppVal' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{2C0D70A3-D197-4781-940A-1672F3B420B9}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 10501, (10501, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 10502, (10502, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'dX' , 'dY' , 'dR' , ), 10503, (10503, (), [ 
			 (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 10504, (10504, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

IChainProfileSprocket2_vtables_dispatch_ = 1
IChainProfileSprocket2_vtables_ = [
	(( 'UseContactPair' , 'pVal' , ), 10551, (10551, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'UseContactPair' , 'pVal' , ), 10551, (10551, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'UseInvoluteMethod' , 'pVal' , ), 10552, (10552, (), [ (11, 1, None, None) , ], 1 , 4 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'UseInvoluteMethod' , 'pVal' , ), 10552, (10552, (), [ (16395, 10, None, None) , ], 1 , 2 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'InvoluteCurveParameter' , 'ppVal' , ), 10553, (10553, (), [ (16393, 10, None, "IID('{E56F87E6-1157-4D4A-9F6A-D66FFE9C2C0D}')") , ], 1 , 2 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
	(( 'NumberofArc' , 'pVal' , ), 10554, (10554, (), [ (3, 1, None, None) , ], 1 , 4 , 4 , 0 , 96 , (3, 0, None, None) , 0 , )),
	(( 'NumberofArc' , 'pVal' , ), 10554, (10554, (), [ (16387, 10, None, None) , ], 1 , 2 , 4 , 0 , 104 , (3, 0, None, None) , 0 , )),
	(( 'ContactPairInfoCollection' , 'ppVal' , ), 10555, (10555, (), [ (16393, 10, None, "IID('{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}')") , ], 1 , 2 , 4 , 0 , 112 , (3, 0, None, None) , 0 , )),
	(( 'PointCollection' , 'ppVal' , ), 10556, (10556, (), [ (16393, 10, None, "IID('{2C0D70A3-D197-4781-940A-1672F3B420B9}')") , ], 1 , 2 , 4 , 0 , 120 , (3, 0, None, None) , 0 , )),
	(( 'Export' , 'strName' , 'val' , ), 10557, (10557, (), [ (8, 1, None, None) , 
			 (11, 1, None, None) , ], 1 , 1 , 4 , 0 , 128 , (3, 0, None, None) , 0 , )),
	(( 'Import' , 'strName' , ), 10558, (10558, (), [ (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 136 , (3, 0, None, None) , 0 , )),
	(( 'Add' , 'dX' , 'dY' , 'dR' , 'bCheckContactPair' , 
			 'bstrSegmentInfo' , ), 10559, (10559, (), [ (5, 1, None, None) , (5, 1, None, None) , (5, 1, None, None) , 
			 (11, 1, None, None) , (8, 1, None, None) , ], 1 , 1 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'Clear' , ), 10560, (10560, (), [ ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
]

IChainSubSystem_vtables_dispatch_ = 1
IChainSubSystem_vtables_ = [
	(( 'GeneralSubSystem' , 'ppSubSystem' , ), 10500, (10500, (), [ (16393, 10, None, "IID('{15C1E9DF-9C1A-404F-8E27-92B26D8F03AA}')") , ], 1 , 2 , 4 , 0 , 144 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyRoller' , 'strName' , 'pPoint' , 'ppResult' , ), 10501, (10501, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{67A861E0-46A2-4D78-A5FA-16B63F2A72AE}')") , ], 1 , 1 , 4 , 0 , 152 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodySprocketRoller' , 'strName' , 'pPoint' , 'ppResult' , ), 10502, (10502, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{C34B22A6-F4E3-4747-BFF8-733F8317E9C2}')") , ], 1 , 1 , 4 , 0 , 160 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodySprocketMultiplex' , 'strName' , 'pPoint' , 'ppResult' , ), 10503, (10503, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{11BBB345-C32E-4A00-9F53-C1FED84012B8}')") , ], 1 , 1 , 4 , 0 , 168 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodySprocketSilent' , 'strName' , 'pPoint' , 'ppResult' , ), 10504, (10504, (), [ 
			 (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{20AA2528-64F0-4CC6-95B3-BE6402187F92}')") , ], 1 , 1 , 4 , 0 , 176 , (3, 0, None, None) , 0 , )),
	(( 'CreateLinkCloneRoller' , 'strNameCloneRoller' , 'strNameClonePin' , 'strNameCloneOffset' , 'pPoint' , 
			 'nNoOfLinkSets' , 'ppResult' , ), 10505, (10505, (), [ (8, 1, None, None) , (8, 1, None, None) , 
			 (8, 1, None, None) , (8197, 1, None, None) , (3, 1, None, None) , (16393, 10, None, "IID('{920A282B-0B31-4AED-9219-BB0163557B7C}')") , ], 1 , 1 , 4 , 0 , 184 , (3, 0, None, None) , 0 , )),
	(( 'CreateLinkCloneMultiplex' , 'strNameCloneRoller' , 'strNameClonePin' , 'strNameCloneOffset' , 'pPoint' , 
			 'LinkType' , 'nNoOfStrands' , 'ppResult' , ), 10506, (10506, (), [ (8, 1, None, None) , 
			 (8, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , (3, 1, None, "IID('{F8D8A690-07E7-4E18-BA1F-7CB58883DB7B}')") , (3, 1, None, None) , 
			 (16393, 10, None, "IID('{4E0780CE-4019-4B61-AE39-D5E2889DA39E}')") , ], 1 , 1 , 4 , 0 , 192 , (3, 0, None, None) , 0 , )),
	(( 'CreateLinkCloneSilent' , 'strNameCloneOuter' , 'strNameCloneInner' , 'pPoint' , 'ppResult' , 
			 ), 10507, (10507, (), [ (8, 1, None, None) , (8, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{4EC1DA77-AD7C-4C9D-B34D-13690F2187D2}')") , ], 1 , 1 , 4 , 0 , 200 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyGuide' , 'strCloneName' , 'Points' , 'ppResult' , ), 10508, (10508, (), [ 
			 (8, 1, None, None) , (8204, 1, None, None) , (16393, 10, None, "IID('{3A623CE7-0BFB-48D9-AB5B-5B305B9F4D45}')") , ], 1 , 1 , 4 , 0 , 208 , (3, 0, None, None) , 0 , )),
	(( 'CreateGroupGuideArc' , 'strName' , 'Points' , 'Segments' , 'ppResult' , 
			 ), 10509, (10509, (), [ (8, 1, None, None) , (8204, 1, None, None) , (8211, 1, None, None) , (16393, 10, None, "IID('{037DA049-C1EB-4F0B-8457-80FE60733754}')") , ], 1 , 1 , 4 , 0 , 216 , (3, 0, None, None) , 0 , )),
	(( 'CreateBodyGuardLateral' , 'strName' , 'pFirstPoint' , 'pSecondPoint' , 'ppResult' , 
			 ), 10510, (10510, (), [ (8, 1, None, None) , (8197, 1, None, None) , (8197, 1, None, None) , (16393, 10, None, "IID('{98696CB8-03A8-4036-8D71-2143E04AB2AC}')") , ], 1 , 1 , 4 , 0 , 224 , (3, 0, None, None) , 0 , )),
	(( 'CreateChainAssemblyRoller' , 'strName' , 'pLinkClone' , 'pBodyList' , 'pInOutList' , 
			 'bushingType' , 'uiNumberOfLink' , 'automaticAlignment' , 'ppResult' , ), 10511, (10511, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{920A282B-0B31-4AED-9219-BB0163557B7C}')") , (8204, 1, None, None) , (8204, 1, None, None) , (3, 1, None, "IID('{C4E01B4A-5D51-44F3-A49A-1BCAD2F1FECA}')") , 
			 (19, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{0963256F-0F65-4E93-8FFA-B58651838BC6}')") , ], 1 , 1 , 4 , 0 , 232 , (3, 0, None, None) , 0 , )),
	(( 'CreateChainAssemblyMultiplex' , 'strName' , 'pLinkClone' , 'pBodyList' , 'pInOutList' , 
			 'bushingType' , 'uiNumberOfLink' , 'automaticAlignment' , 'ppResult' , ), 10512, (10512, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{4E0780CE-4019-4B61-AE39-D5E2889DA39E}')") , (8204, 1, None, None) , (8204, 1, None, None) , (3, 1, None, "IID('{C4E01B4A-5D51-44F3-A49A-1BCAD2F1FECA}')") , 
			 (19, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{0963256F-0F65-4E93-8FFA-B58651838BC6}')") , ], 1 , 1 , 4 , 0 , 240 , (3, 0, None, None) , 0 , )),
	(( 'CreateChainAssemblySilent' , 'strName' , 'pLinkClone' , 'pBodyList' , 'pInOutList' , 
			 'bushingType' , 'uiNumberOfLink' , 'automaticAlignment' , 'ppResult' , ), 10513, (10513, (), [ 
			 (8, 1, None, None) , (9, 1, None, "IID('{4EC1DA77-AD7C-4C9D-B34D-13690F2187D2}')") , (8204, 1, None, None) , (8204, 1, None, None) , (3, 1, None, "IID('{C4E01B4A-5D51-44F3-A49A-1BCAD2F1FECA}')") , 
			 (19, 1, None, None) , (11, 1, None, None) , (16393, 10, None, "IID('{0963256F-0F65-4E93-8FFA-B58651838BC6}')") , ], 1 , 1 , 4 , 0 , 248 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorFixed' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 10514, (10514, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{39059D2F-DBEC-49DD-BFF2-AC0185541C99}')") , ], 1 , 1 , 4 , 0 , 256 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorRevolute' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 10515, (10515, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{D24BBA28-623F-4F1C-97D5-021413EB6736}')") , ], 1 , 1 , 4 , 0 , 264 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorSpring' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pBaseRefFrame' , 
			 'pActionRefFrame' , 'ppResult' , ), 10516, (10516, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{93A5A572-A6DD-4F12-A3E5-64F95B78718F}')") , ], 1 , 1 , 4 , 0 , 272 , (3, 0, None, None) , 0 , )),
	(( 'CreateForceConnectorBushing' , 'strName' , 'pBaseBody' , 'pActionBody' , 'pRefFrame' , 
			 'ppResult' , ), 10517, (10517, (), [ (8, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (9, 1, None, "IID('{6A3295D9-E76B-473C-9655-23B7B1CBD671}')") , (16393, 10, None, "IID('{F5A169B5-B529-4935-8B06-ACDD2A0BA456}')") , ], 1 , 1 , 4 , 0 , 280 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorSpeed' , 'strName' , 'pPosition' , 'pDirection' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 10518, (10518, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{CCB7E742-F0DF-4F22-A377-04AA675FD281}')") , ], 1 , 1 , 4 , 0 , 288 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorDistance' , 'strName' , 'pPosition' , 'pDirection' , 'pEntity' , 
			 'dRange' , 'ppVal' , ), 10519, (10519, (), [ (8, 1, None, None) , (8197, 1, None, None) , 
			 (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , (5, 1, None, None) , (16393, 10, None, "IID('{0CC3861B-CC2A-4402-9135-C8BC804EABBD}')") , ], 1 , 1 , 4 , 0 , 296 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorTension' , 'strName' , 'pPosition' , 'pEntity' , 'dRange' , 
			 'ppVal' , ), 10520, (10520, (), [ (8, 1, None, None) , (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{55C49622-A503-4651-BF1E-2A84CD9E27AB}')") , ], 1 , 1 , 4 , 0 , 304 , (3, 0, None, None) , 0 , )),
	(( 'LinkCloneCollection' , 'ppVal' , ), 10521, (10521, (), [ (16393, 10, None, "IID('{BFBCE202-F4CB-40D0-8652-8DF819E5D886}')") , ], 1 , 2 , 4 , 0 , 312 , (3, 0, None, None) , 0 , )),
	(( 'AssemblyCollection' , 'ppVal' , ), 10522, (10522, (), [ (16393, 10, None, "IID('{F695BFDC-1A2A-4C74-9908-D337B2FF62B8}')") , ], 1 , 2 , 4 , 0 , 320 , (3, 0, None, None) , 0 , )),
	(( 'ChainBodyCollection' , 'ppVal' , ), 10523, (10523, (), [ (16393, 10, None, "IID('{ED20A123-7EEE-4173-9F9C-2D37D1138E48}')") , ], 1 , 2 , 4 , 0 , 328 , (3, 0, None, None) , 0 , )),
	(( 'CreateSensorTensionEx' , 'strName' , 'pPosition' , 'pEntity' , 'dRange' , 
			 'ppVal' , ), 10524, (10524, (), [ (8, 1, None, None) , (8197, 1, None, None) , (9, 1, None, "IID('{27A86788-8B85-40CF-BE7F-BA915103A7DB}')") , 
			 (5, 1, None, None) , (16393, 10, None, "IID('{FD6480C3-36F4-4627-9725-6B484795DC39}')") , ], 1 , 1 , 4 , 0 , 336 , (3, 0, None, None) , 0 , )),
]

IPoint3DWithRadiusAndCheckCollection_vtables_dispatch_ = 1
IPoint3DWithRadiusAndCheckCollection_vtables_ = [
]

RecordMap = {
}

CLSIDToClassMap = {
	'{4BCBE390-C6BB-4E5A-9DA3-40A756B8326F}' : IChainContactPairInfo,
	'{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}' : IChainContactPairInfoCollection,
	'{B512AC12-46CE-4A35-B10B-1A83C7C91457}' : IChainGuidePointsWithAdditionalInfo,
	'{E6353564-8957-4E10-8A7B-12F98C5ECCFB}' : IChainGuidePointsWithAdditionalInfoCollection,
	'{0954FD4A-BE83-4A47-A022-39343EABBB1B}' : IChainGroupGuidePointsWithAdditionalInfo,
	'{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}' : IChainGroupGuidePointsWithAdditionalInfoCollection,
	'{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}' : IChainContactFriction,
	'{6F6A35D3-97FF-494A-8E1A-DF4E8101EBDB}' : IChainAssemblyContactFriction,
	'{8907B76F-36EF-42E8-AA90-2C02C76EF56F}' : IChainContactProperty,
	'{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}' : IChainContactPropertySprocket,
	'{1E51E4E8-E4DC-4C00-BBCB-816315723567}' : IChainGuideContactProperty,
	'{E56F87E6-1157-4D4A-9F6A-D66FFE9C2C0D}' : IChainInvoluteCurveParameter,
	'{2137EA2C-652F-4C83-B265-17AB71E0E202}' : IChainGeometryRoller,
	'{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}' : IChainProfileSprocket,
	'{BD4851C8-8A99-4B29-80AE-2E160DC0754C}' : IChainProfileSprocket2,
	'{314E0700-F8CC-4C1F-B1C3-0C0386F06A89}' : IPoint3DWithRadiusAndCheckCollection,
	'{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}' : IChainProfileLinkSilent,
	'{71E9EDCA-8586-4BC4-8C96-CA6CE987B7C7}' : IChainGeometrySprocketRoller,
	'{84F6AAEF-A7BD-4C0E-A1B9-3377E4E8398B}' : IChainGeometrySprocketMultiplex,
	'{46136858-6824-49C4-A14E-EC6C582E3C6D}' : IChainGeometrySprocketSilent,
	'{F2988F5F-6804-4797-9633-0BD1C78C4366}' : IChainGeometryGuide,
	'{B0B8CBCE-6E48-4300-9436-0599707E3C93}' : IChainGeometryGroupGuideArc,
	'{82124DDF-C246-49F1-86B3-8DAD3B875DDD}' : IChainGeometryGuardLateral,
	'{E6301A79-B289-4188-B213-AE53CA9E89BB}' : IChainGeometryLinkRoller,
	'{B4B7B26A-F4EB-486F-9909-74DA518613C4}' : IChainGeometryLinkPin,
	'{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}' : IChainGeometryLinkMultiplexRoller,
	'{33736DE9-40C6-42C3-96EB-72FD82D10535}' : IChainGeometryLinkMultiplexPin,
	'{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}' : IChainGeometryLinkSilentOuter,
	'{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}' : IChainGeometryLinkSilentInner,
	'{134391CE-930C-47BE-983B-B326A771F701}' : IChainContactSearch,
	'{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}' : IChainBody,
	'{67A861E0-46A2-4D78-A5FA-16B63F2A72AE}' : IChainBodyRoller,
	'{C34B22A6-F4E3-4747-BFF8-733F8317E9C2}' : IChainBodySprocketRoller,
	'{11BBB345-C32E-4A00-9F53-C1FED84012B8}' : IChainBodySprocketMultiplex,
	'{20AA2528-64F0-4CC6-95B3-BE6402187F92}' : IChainBodySprocketSilent,
	'{A04DEA81-0603-4F81-91F5-D11FF259F6A1}' : IChainBodyLink,
	'{F389179B-A643-41C0-A674-860C335802C8}' : IChainBodyLinkRoller,
	'{14D6BFE5-15ED-45F4-9A34-0B7315136841}' : IChainBodyLinkPin,
	'{BBDD1814-F174-4AEF-944E-933DC4C656F9}' : IChainBodyLinkOffset,
	'{1E546ED7-D793-4715-9F5E-CD694AA8B4E1}' : IChainBodyLinkMultiplexRoller,
	'{7532D229-00FF-4821-8177-B5225CC2FAE4}' : IChainBodyLinkMultiplexPin,
	'{8740B4DF-D06F-4FCF-91C6-8302FFFE58B6}' : IChainBodyLinkMultiplexOffset,
	'{33FC1BEE-4A91-4C01-82DE-1C83FC962DC1}' : IChainBodyLinkSilentOuter,
	'{29199CB1-7647-4D2B-8D57-6A7701619A1C}' : IChainBodyLinkSilentInner,
	'{3A623CE7-0BFB-48D9-AB5B-5B305B9F4D45}' : IChainBodyGuide,
	'{037DA049-C1EB-4F0B-8457-80FE60733754}' : IChainGroupGuideArc,
	'{98696CB8-03A8-4036-8D71-2143E04AB2AC}' : IChainBodyGuardLateral,
	'{3C283940-AAB3-48D1-A521-D8AA43058BC2}' : IChainLinkClone,
	'{920A282B-0B31-4AED-9219-BB0163557B7C}' : IChainLinkCloneRoller,
	'{50F61A34-FBAC-4394-9FC3-07729ABA03C3}' : IChainLinkClonePin,
	'{DF2ABA6B-0E35-4110-A019-147E34D9C411}' : IChainLinkCloneOffset,
	'{4E0780CE-4019-4B61-AE39-D5E2889DA39E}' : IChainLinkCloneMultiplexRoller,
	'{18CD7701-60FB-4CC3-9619-36DDD1647F44}' : IChainLinkCloneMultiplexPin,
	'{F02C6C40-A3AC-404E-8FE8-BA034A99392F}' : IChainLinkCloneMultiplexOffset,
	'{4EC1DA77-AD7C-4C9D-B34D-13690F2187D2}' : IChainLinkCloneSilentOuter,
	'{F9F223BD-D461-4F06-950E-6A821C5BB83D}' : IChainLinkCloneSilentInner,
	'{15D9554A-5BA8-4892-8AC3-1A026ED0FBCA}' : IChainAssemblyBushingForceParameter,
	'{7DCEE901-515D-4780-AB01-89ECA089D8BE}' : IChainBodyLinkCollection,
	'{0963256F-0F65-4E93-8FFA-B58651838BC6}' : IChainAssembly,
	'{90DD375C-3EA7-4002-BDB2-8E3E3E03AEE2}' : IChainPassingBodyCollection,
	'{BFBCE202-F4CB-40D0-8652-8DF819E5D886}' : IChainLinkCloneCollection,
	'{F695BFDC-1A2A-4C74-9908-D337B2FF62B8}' : IChainAssemblyCollection,
	'{ED20A123-7EEE-4173-9F9C-2D37D1138E48}' : IChainBodyCollection,
	'{E8F3EEAE-A4B6-4A6A-A0F2-DE6BA3CF1DEA}' : IChainSubSystem,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{4BCBE390-C6BB-4E5A-9DA3-40A756B8326F}' : 'IChainContactPairInfo',
	'{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}' : 'IChainContactPairInfoCollection',
	'{B512AC12-46CE-4A35-B10B-1A83C7C91457}' : 'IChainGuidePointsWithAdditionalInfo',
	'{E6353564-8957-4E10-8A7B-12F98C5ECCFB}' : 'IChainGuidePointsWithAdditionalInfoCollection',
	'{0954FD4A-BE83-4A47-A022-39343EABBB1B}' : 'IChainGroupGuidePointsWithAdditionalInfo',
	'{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}' : 'IChainGroupGuidePointsWithAdditionalInfoCollection',
	'{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}' : 'IChainContactFriction',
	'{6F6A35D3-97FF-494A-8E1A-DF4E8101EBDB}' : 'IChainAssemblyContactFriction',
	'{8907B76F-36EF-42E8-AA90-2C02C76EF56F}' : 'IChainContactProperty',
	'{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}' : 'IChainContactPropertySprocket',
	'{1E51E4E8-E4DC-4C00-BBCB-816315723567}' : 'IChainGuideContactProperty',
	'{E56F87E6-1157-4D4A-9F6A-D66FFE9C2C0D}' : 'IChainInvoluteCurveParameter',
	'{2137EA2C-652F-4C83-B265-17AB71E0E202}' : 'IChainGeometryRoller',
	'{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}' : 'IChainProfileSprocket',
	'{BD4851C8-8A99-4B29-80AE-2E160DC0754C}' : 'IChainProfileSprocket2',
	'{314E0700-F8CC-4C1F-B1C3-0C0386F06A89}' : 'IPoint3DWithRadiusAndCheckCollection',
	'{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}' : 'IChainProfileLinkSilent',
	'{71E9EDCA-8586-4BC4-8C96-CA6CE987B7C7}' : 'IChainGeometrySprocketRoller',
	'{84F6AAEF-A7BD-4C0E-A1B9-3377E4E8398B}' : 'IChainGeometrySprocketMultiplex',
	'{46136858-6824-49C4-A14E-EC6C582E3C6D}' : 'IChainGeometrySprocketSilent',
	'{F2988F5F-6804-4797-9633-0BD1C78C4366}' : 'IChainGeometryGuide',
	'{B0B8CBCE-6E48-4300-9436-0599707E3C93}' : 'IChainGeometryGroupGuideArc',
	'{82124DDF-C246-49F1-86B3-8DAD3B875DDD}' : 'IChainGeometryGuardLateral',
	'{E6301A79-B289-4188-B213-AE53CA9E89BB}' : 'IChainGeometryLinkRoller',
	'{B4B7B26A-F4EB-486F-9909-74DA518613C4}' : 'IChainGeometryLinkPin',
	'{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}' : 'IChainGeometryLinkMultiplexRoller',
	'{33736DE9-40C6-42C3-96EB-72FD82D10535}' : 'IChainGeometryLinkMultiplexPin',
	'{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}' : 'IChainGeometryLinkSilentOuter',
	'{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}' : 'IChainGeometryLinkSilentInner',
	'{134391CE-930C-47BE-983B-B326A771F701}' : 'IChainContactSearch',
	'{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}' : 'IChainBody',
	'{67A861E0-46A2-4D78-A5FA-16B63F2A72AE}' : 'IChainBodyRoller',
	'{C34B22A6-F4E3-4747-BFF8-733F8317E9C2}' : 'IChainBodySprocketRoller',
	'{11BBB345-C32E-4A00-9F53-C1FED84012B8}' : 'IChainBodySprocketMultiplex',
	'{20AA2528-64F0-4CC6-95B3-BE6402187F92}' : 'IChainBodySprocketSilent',
	'{A04DEA81-0603-4F81-91F5-D11FF259F6A1}' : 'IChainBodyLink',
	'{F389179B-A643-41C0-A674-860C335802C8}' : 'IChainBodyLinkRoller',
	'{14D6BFE5-15ED-45F4-9A34-0B7315136841}' : 'IChainBodyLinkPin',
	'{BBDD1814-F174-4AEF-944E-933DC4C656F9}' : 'IChainBodyLinkOffset',
	'{1E546ED7-D793-4715-9F5E-CD694AA8B4E1}' : 'IChainBodyLinkMultiplexRoller',
	'{7532D229-00FF-4821-8177-B5225CC2FAE4}' : 'IChainBodyLinkMultiplexPin',
	'{8740B4DF-D06F-4FCF-91C6-8302FFFE58B6}' : 'IChainBodyLinkMultiplexOffset',
	'{33FC1BEE-4A91-4C01-82DE-1C83FC962DC1}' : 'IChainBodyLinkSilentOuter',
	'{29199CB1-7647-4D2B-8D57-6A7701619A1C}' : 'IChainBodyLinkSilentInner',
	'{3A623CE7-0BFB-48D9-AB5B-5B305B9F4D45}' : 'IChainBodyGuide',
	'{037DA049-C1EB-4F0B-8457-80FE60733754}' : 'IChainGroupGuideArc',
	'{98696CB8-03A8-4036-8D71-2143E04AB2AC}' : 'IChainBodyGuardLateral',
	'{3C283940-AAB3-48D1-A521-D8AA43058BC2}' : 'IChainLinkClone',
	'{920A282B-0B31-4AED-9219-BB0163557B7C}' : 'IChainLinkCloneRoller',
	'{50F61A34-FBAC-4394-9FC3-07729ABA03C3}' : 'IChainLinkClonePin',
	'{DF2ABA6B-0E35-4110-A019-147E34D9C411}' : 'IChainLinkCloneOffset',
	'{4E0780CE-4019-4B61-AE39-D5E2889DA39E}' : 'IChainLinkCloneMultiplexRoller',
	'{18CD7701-60FB-4CC3-9619-36DDD1647F44}' : 'IChainLinkCloneMultiplexPin',
	'{F02C6C40-A3AC-404E-8FE8-BA034A99392F}' : 'IChainLinkCloneMultiplexOffset',
	'{4EC1DA77-AD7C-4C9D-B34D-13690F2187D2}' : 'IChainLinkCloneSilentOuter',
	'{F9F223BD-D461-4F06-950E-6A821C5BB83D}' : 'IChainLinkCloneSilentInner',
	'{15D9554A-5BA8-4892-8AC3-1A026ED0FBCA}' : 'IChainAssemblyBushingForceParameter',
	'{7DCEE901-515D-4780-AB01-89ECA089D8BE}' : 'IChainBodyLinkCollection',
	'{0963256F-0F65-4E93-8FFA-B58651838BC6}' : 'IChainAssembly',
	'{90DD375C-3EA7-4002-BDB2-8E3E3E03AEE2}' : 'IChainPassingBodyCollection',
	'{BFBCE202-F4CB-40D0-8652-8DF819E5D886}' : 'IChainLinkCloneCollection',
	'{F695BFDC-1A2A-4C74-9908-D337B2FF62B8}' : 'IChainAssemblyCollection',
	'{ED20A123-7EEE-4173-9F9C-2D37D1138E48}' : 'IChainBodyCollection',
	'{E8F3EEAE-A4B6-4A6A-A0F2-DE6BA3CF1DEA}' : 'IChainSubSystem',
}


NamesToIIDMap = {
	'IChainContactPairInfo' : '{4BCBE390-C6BB-4E5A-9DA3-40A756B8326F}',
	'IChainContactPairInfoCollection' : '{52327AC3-142D-4C66-9D0B-7D8CCC13FE0E}',
	'IChainGuidePointsWithAdditionalInfo' : '{B512AC12-46CE-4A35-B10B-1A83C7C91457}',
	'IChainGuidePointsWithAdditionalInfoCollection' : '{E6353564-8957-4E10-8A7B-12F98C5ECCFB}',
	'IChainGroupGuidePointsWithAdditionalInfo' : '{0954FD4A-BE83-4A47-A022-39343EABBB1B}',
	'IChainGroupGuidePointsWithAdditionalInfoCollection' : '{DCA7B2FB-178E-4904-89BD-4BCC3B8AD7FF}',
	'IChainContactFriction' : '{6C447E36-46C6-4A1A-8D5A-58E6B9BD0166}',
	'IChainAssemblyContactFriction' : '{6F6A35D3-97FF-494A-8E1A-DF4E8101EBDB}',
	'IChainContactProperty' : '{8907B76F-36EF-42E8-AA90-2C02C76EF56F}',
	'IChainContactPropertySprocket' : '{BA1CBEBA-2CA5-410A-90FE-4ACB78564EC9}',
	'IChainGuideContactProperty' : '{1E51E4E8-E4DC-4C00-BBCB-816315723567}',
	'IChainInvoluteCurveParameter' : '{E56F87E6-1157-4D4A-9F6A-D66FFE9C2C0D}',
	'IChainGeometryRoller' : '{2137EA2C-652F-4C83-B265-17AB71E0E202}',
	'IChainProfileSprocket' : '{71244ADF-A639-4B50-AB3C-0EAFB11EE5BA}',
	'IChainProfileSprocket2' : '{BD4851C8-8A99-4B29-80AE-2E160DC0754C}',
	'IPoint3DWithRadiusAndCheckCollection' : '{314E0700-F8CC-4C1F-B1C3-0C0386F06A89}',
	'IChainProfileLinkSilent' : '{7B22AD88-1A3E-4F2F-BD7E-DA4C4B79986B}',
	'IChainGeometrySprocketRoller' : '{71E9EDCA-8586-4BC4-8C96-CA6CE987B7C7}',
	'IChainGeometrySprocketMultiplex' : '{84F6AAEF-A7BD-4C0E-A1B9-3377E4E8398B}',
	'IChainGeometrySprocketSilent' : '{46136858-6824-49C4-A14E-EC6C582E3C6D}',
	'IChainGeometryGuide' : '{F2988F5F-6804-4797-9633-0BD1C78C4366}',
	'IChainGeometryGroupGuideArc' : '{B0B8CBCE-6E48-4300-9436-0599707E3C93}',
	'IChainGeometryGuardLateral' : '{82124DDF-C246-49F1-86B3-8DAD3B875DDD}',
	'IChainGeometryLinkRoller' : '{E6301A79-B289-4188-B213-AE53CA9E89BB}',
	'IChainGeometryLinkPin' : '{B4B7B26A-F4EB-486F-9909-74DA518613C4}',
	'IChainGeometryLinkMultiplexRoller' : '{42AE2554-BEB1-44FF-AD8C-F0A2F8A4764F}',
	'IChainGeometryLinkMultiplexPin' : '{33736DE9-40C6-42C3-96EB-72FD82D10535}',
	'IChainGeometryLinkSilentOuter' : '{A73FFAA6-E0E4-47F1-A531-4B99E61F85C6}',
	'IChainGeometryLinkSilentInner' : '{113D67BF-ABDB-44E1-BC9C-66BC20A365BB}',
	'IChainContactSearch' : '{134391CE-930C-47BE-983B-B326A771F701}',
	'IChainBody' : '{DBA5B80B-B196-4FD5-A1A4-70B841FBFDCB}',
	'IChainBodyRoller' : '{67A861E0-46A2-4D78-A5FA-16B63F2A72AE}',
	'IChainBodySprocketRoller' : '{C34B22A6-F4E3-4747-BFF8-733F8317E9C2}',
	'IChainBodySprocketMultiplex' : '{11BBB345-C32E-4A00-9F53-C1FED84012B8}',
	'IChainBodySprocketSilent' : '{20AA2528-64F0-4CC6-95B3-BE6402187F92}',
	'IChainBodyLink' : '{A04DEA81-0603-4F81-91F5-D11FF259F6A1}',
	'IChainBodyLinkRoller' : '{F389179B-A643-41C0-A674-860C335802C8}',
	'IChainBodyLinkPin' : '{14D6BFE5-15ED-45F4-9A34-0B7315136841}',
	'IChainBodyLinkOffset' : '{BBDD1814-F174-4AEF-944E-933DC4C656F9}',
	'IChainBodyLinkMultiplexRoller' : '{1E546ED7-D793-4715-9F5E-CD694AA8B4E1}',
	'IChainBodyLinkMultiplexPin' : '{7532D229-00FF-4821-8177-B5225CC2FAE4}',
	'IChainBodyLinkMultiplexOffset' : '{8740B4DF-D06F-4FCF-91C6-8302FFFE58B6}',
	'IChainBodyLinkSilentOuter' : '{33FC1BEE-4A91-4C01-82DE-1C83FC962DC1}',
	'IChainBodyLinkSilentInner' : '{29199CB1-7647-4D2B-8D57-6A7701619A1C}',
	'IChainBodyGuide' : '{3A623CE7-0BFB-48D9-AB5B-5B305B9F4D45}',
	'IChainGroupGuideArc' : '{037DA049-C1EB-4F0B-8457-80FE60733754}',
	'IChainBodyGuardLateral' : '{98696CB8-03A8-4036-8D71-2143E04AB2AC}',
	'IChainLinkClone' : '{3C283940-AAB3-48D1-A521-D8AA43058BC2}',
	'IChainLinkCloneRoller' : '{920A282B-0B31-4AED-9219-BB0163557B7C}',
	'IChainLinkClonePin' : '{50F61A34-FBAC-4394-9FC3-07729ABA03C3}',
	'IChainLinkCloneOffset' : '{DF2ABA6B-0E35-4110-A019-147E34D9C411}',
	'IChainLinkCloneMultiplexRoller' : '{4E0780CE-4019-4B61-AE39-D5E2889DA39E}',
	'IChainLinkCloneMultiplexPin' : '{18CD7701-60FB-4CC3-9619-36DDD1647F44}',
	'IChainLinkCloneMultiplexOffset' : '{F02C6C40-A3AC-404E-8FE8-BA034A99392F}',
	'IChainLinkCloneSilentOuter' : '{4EC1DA77-AD7C-4C9D-B34D-13690F2187D2}',
	'IChainLinkCloneSilentInner' : '{F9F223BD-D461-4F06-950E-6A821C5BB83D}',
	'IChainAssemblyBushingForceParameter' : '{15D9554A-5BA8-4892-8AC3-1A026ED0FBCA}',
	'IChainBodyLinkCollection' : '{7DCEE901-515D-4780-AB01-89ECA089D8BE}',
	'IChainAssembly' : '{0963256F-0F65-4E93-8FFA-B58651838BC6}',
	'IChainPassingBodyCollection' : '{90DD375C-3EA7-4002-BDB2-8E3E3E03AEE2}',
	'IChainLinkCloneCollection' : '{BFBCE202-F4CB-40D0-8652-8DF819E5D886}',
	'IChainAssemblyCollection' : '{F695BFDC-1A2A-4C74-9908-D337B2FF62B8}',
	'IChainBodyCollection' : '{ED20A123-7EEE-4173-9F9C-2D37D1138E48}',
	'IChainSubSystem' : '{E8F3EEAE-A4B6-4A6A-A0F2-DE6BA3CF1DEA}',
}


