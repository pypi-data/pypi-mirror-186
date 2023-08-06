# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDynCOMExternal.tlb'
# On Tue Jun 28 10:10:45 2022
'RecurDyn V9R5 RecurDynCOMExternal Type Library'
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

CLSID = IID('{E0FDFD09-8D4C-4CDF-9DE8-3B727861D718}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IRDDevelopementExternal(DispatchBaseClass):
	'''IRDDevelopementExternal'''
	CLSID = IID('{3105E177-73B8-47E1-A229-D6294DA1E657}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_AutoDesign(self):
		return self._ApplyTypes_(*(180001, 2, (9, 0), (), "AutoDesign", '{F87006F2-2B70-4A5F-91E0-4338A4CCDF88}'))

	AutoDesign = property(_get_AutoDesign, None)
	'''
	AutoDesign

	:type: recurdyn.External.IRDExternalAutoDesign
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"AutoDesign": (180001, 2, (9, 0), (), "AutoDesign", '{F87006F2-2B70-4A5F-91E0-4338A4CCDF88}'),
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

class IRDExternalAutoDesign(DispatchBaseClass):
	'''IRDExternalAutoDesign'''
	CLSID = IID('{F87006F2-2B70-4A5F-91E0-4338A4CCDF88}')
	coclass_clsid = None

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def OpenAnalysisResponsePage(self):
		'''
		Open Analysis Response Page
		'''
		return self._oleobj_.InvokeTypes(90002, LCID, 1, (24, 0), (),)


	def OpenDesgnParameterPage(self):
		'''
		Open Design Parameter Page
		'''
		return self._oleobj_.InvokeTypes(90001, LCID, 1, (24, 0), (),)


	def OpenDesignStudyPage(self):
		'''
		Open Design Study Page
		'''
		return self._oleobj_.InvokeTypes(90003, LCID, 1, (24, 0), (),)


	def OpenOptimizationPage(self):
		'''
		Open Optimization Page
		'''
		return self._oleobj_.InvokeTypes(90004, LCID, 1, (24, 0), (),)


	def OpenRobustOptimizationPage(self):
		'''
		Open Robust Optimization Page
		'''
		return self._oleobj_.InvokeTypes(90005, LCID, 1, (24, 0), (),)


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

IRDDevelopementExternal_vtables_dispatch_ = 1
IRDDevelopementExternal_vtables_ = [
	(( 'AutoDesign' , 'ppVal' , ), 180001, (180001, (), [ (16393, 10, None, "IID('{F87006F2-2B70-4A5F-91E0-4338A4CCDF88}')") , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

IRDExternalAutoDesign_vtables_dispatch_ = 1
IRDExternalAutoDesign_vtables_ = [
	(( 'OpenDesgnParameterPage' , ), 90001, (90001, (), [ ], 1 , 1 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
	(( 'OpenAnalysisResponsePage' , ), 90002, (90002, (), [ ], 1 , 1 , 4 , 0 , 64 , (3, 0, None, None) , 0 , )),
	(( 'OpenDesignStudyPage' , ), 90003, (90003, (), [ ], 1 , 1 , 4 , 0 , 72 , (3, 0, None, None) , 0 , )),
	(( 'OpenOptimizationPage' , ), 90004, (90004, (), [ ], 1 , 1 , 4 , 0 , 80 , (3, 0, None, None) , 0 , )),
	(( 'OpenRobustOptimizationPage' , ), 90005, (90005, (), [ ], 1 , 1 , 4 , 0 , 88 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{F87006F2-2B70-4A5F-91E0-4338A4CCDF88}' : IRDExternalAutoDesign,
	'{3105E177-73B8-47E1-A229-D6294DA1E657}' : IRDDevelopementExternal,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{F87006F2-2B70-4A5F-91E0-4338A4CCDF88}' : 'IRDExternalAutoDesign',
	'{3105E177-73B8-47E1-A229-D6294DA1E657}' : 'IRDDevelopementExternal',
}


NamesToIIDMap = {
	'IRDExternalAutoDesign' : '{F87006F2-2B70-4A5F-91E0-4338A4CCDF88}',
	'IRDDevelopementExternal' : '{3105E177-73B8-47E1-A229-D6294DA1E657}',
}


