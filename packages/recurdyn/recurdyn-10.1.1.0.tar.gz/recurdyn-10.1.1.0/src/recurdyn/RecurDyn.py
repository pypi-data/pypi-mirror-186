# -*- coding: mbcs -*-
# Created by makepy.py version 0.5.01
# By python version 3.8.10 (tags/v3.8.10:3d8993a, May  3 2021, 11:48:03) [MSC v.1928 64 bit (AMD64)]
# From type library 'RecurDyn.tlb'
# On Mon Jan 16 02:20:00 2023
'RecurDyn V9 RecurDyn Type Library'
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

CLSID = IID('{B54AAE4D-A7FF-48B8-BD80-BA40C17B74FA}')
MajorVersion = 1
MinorVersion = 0
LibraryFlags = 8
LCID = 0x0

from win32com.client import DispatchBaseClass
class IRecurDynApp(DispatchBaseClass):
	CLSID = IID('{09A65909-6FBB-488A-9726-D320F5666394}')
	coclass_clsid = IID('{FEAC72DD-1D1B-47D0-8958-5BF3E69F0A93}')

	def __setattr__(self, attr, value):
		if '_set_'+attr in dir(self):
			try:
				self._prop_map_set_function_['_set_'+attr](self, value)
			except:
				super().__setattr__(attr, value)
		else:
			super().__setattr__(attr, value)
	def _get_RecurDynApplication(self):
		return self._ApplyTypes_(*(13200, 2, (9, 0), (), "RecurDynApplication", None))

	RecurDynApplication = property(_get_RecurDynApplication, None)
	'''
	property Application

	:type: dispatch
	'''

	_prop_map_set_function_ = {
	}
	_prop_map_get_ = {
		"RecurDynApplication": (13200, 2, (9, 0), (), "RecurDynApplication", None),
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

from win32com.client import CoClassBaseClass
# This CoClass is known by the name 'RecurDyn.RDApplication.1'
class RDApplication(CoClassBaseClass): # A CoClass
	# Global Application Object
	CLSID = IID('{FEAC72DD-1D1B-47D0-8958-5BF3E69F0A93}')
	coclass_sources = [
	]
	coclass_interfaces = [
		IRecurDynApp,
	]
	default_interface = IRecurDynApp

IRecurDynApp_vtables_dispatch_ = 1
IRecurDynApp_vtables_ = [
	(( 'RecurDynApplication' , 'ppApplication' , ), 13200, (13200, (), [ (16393, 10, None, None) , ], 1 , 2 , 4 , 0 , 56 , (3, 0, None, None) , 0 , )),
]

RecordMap = {
}

CLSIDToClassMap = {
	'{09A65909-6FBB-488A-9726-D320F5666394}' : IRecurDynApp,
	'{FEAC72DD-1D1B-47D0-8958-5BF3E69F0A93}' : RDApplication,
}
CLSIDToPackageMap = {}
win32com.client.CLSIDToClass.RegisterCLSIDsFromDict( CLSIDToClassMap )
VTablesToPackageMap = {}
VTablesToClassMap = {
	'{09A65909-6FBB-488A-9726-D320F5666394}' : 'IRecurDynApp',
}


NamesToIIDMap = {
	'IRecurDynApp' : '{09A65909-6FBB-488A-9726-D320F5666394}',
}


