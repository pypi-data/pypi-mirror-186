import time
import subprocess
import winreg
import win32com.client
import pythoncom


class COMConnectionTimeoutError(Exception):
    def __str(self):
        return "RecurDyn COM is not connected. Connection timed out."

        
def is_available_use_wmi_tools():
    try:
        wmi = win32com.client.GetObject('winmgmts:')
        wprocess = wmi.InstancesOf('Win32_Process')
    except:
        return False
    return True


def _get_registry_recurdyn_path(version):
    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        reg_sub_key = "SOFTWARE\\FunctionBay, Inc.\\RecurDyn {}\\Path".format(version.upper())
        reg_key = winreg.OpenKey(reg, reg_sub_key)
        if reg_key is None:
            return None
        dataValue, _ = winreg.QueryValueEx(reg_key, "ROOT")
        if not dataValue:
            return None
        else:
            return "{}\\Bin\\RecurDyn.exe".format(dataValue)
    except:
        return None


def exist_recurdyn_name_in_process():
    wmi = win32com.client.GetObject('winmgmts:')
    wprocess = wmi.InstancesOf('Win32_Process')
    for process in wprocess:
        if process.Properties_('Name').Value == "RecurDyn.exe":
            return True
    return False


def _exist_recurdyn_executable_path_in_process(version):
    recurdyn_path = _get_registry_recurdyn_path(version)
    if not recurdyn_path:
        return False

    wmi = win32com.client.GetObject('winmgmts:')
    wprocess = wmi.InstancesOf('Win32_Process')
    for process in wprocess:
        if process.Properties_('ExecutablePath').Value == recurdyn_path:
            return True

    return False


def _get_active_recurdyn_object():
    try:
        win32com.client.GetActiveObject("RecurDyn.RDApplication")
        return True
    except:
        return False


def _wait_while_recurdyn_com_is_actived(version, maxDelayTimeSec, regRunFlag):
    time_count = 0
    while (time_count < maxDelayTimeSec):
        if _get_active_recurdyn_object():
            return True
        
        if regRunFlag is False and time_count%30 == 0:
            if not exist_recurdyn_name_in_process():
                regRunFlag = _RunRecurDynFromRegistry(version)

        time.sleep(1)
        time_count += 1
        continue

    return False


def _CheckRecurdynRunning(version):
    if not exist_recurdyn_name_in_process():
        print("RecurDyn {} is not running.".format(version))
        return False

    if _exist_recurdyn_executable_path_in_process(version):
        return True
    
    print("Another version of RecurDyn is running.")
    return True

def _RunRecurDynFromRegistry(version):
    recurdyn_path = _get_registry_recurdyn_path(version)
    if not recurdyn_path:
        print("RecurDyn {} is not installed.".format(version))
        return False

    recurdyn_process = subprocess.Popen(recurdyn_path)

    print("Run RecurDyn")
    return True
   

def dispatch_recurdyn(version="2023", autoRunFlag=True, maxDelayTimeSec=300):
    '''
    Dispatch RecurDyn Application
	
	:param version: str
	:param autoRunFlag: bool
	:param maxDelayTimeSec: int
    :rtpye: IRecurDynApp
    '''
    if _get_active_recurdyn_object() is False:
        if is_available_use_wmi_tools() and autoRunFlag:
            regRunFlag = False
            if not _CheckRecurdynRunning(version):
                regRunFlag = _RunRecurDynFromRegistry(version)

            if not _wait_while_recurdyn_com_is_actived(version, maxDelayTimeSec, regRunFlag):
                raise COMConnectionTimeoutError

    return win32com.client.Dispatch("RecurDyn.RDApplication")

# Post Application
def _get_registry_post_path(version):
    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        reg_sub_key = "SOFTWARE\\FunctionBay, Inc.\\RecurDyn {}\\Path".format(version.upper())
        reg_key = winreg.OpenKey(reg, reg_sub_key)
        if reg_key is None:
            return ""
        dataValue, _ = winreg.QueryValueEx(reg_key, "ROOT")
        if "" == dataValue:
            return ""
        else:
            return "{}\\Bin\\Post\\RecurDynPost.exe".format(dataValue)
    except:
        return ""


def exist_post_name_in_process():
    wmi = win32com.client.GetObject('winmgmts:')
    wprocess = wmi.InstancesOf('Win32_Process')
    for process in wprocess:
        if process.Properties_('Name').Value == "RecurDynPost.exe":
            return True
    return False


def _exist_post_executable_path_in_process(version):
    post_path = _get_registry_post_path(version)
    if "" == post_path:
        return False

    wmi = win32com.client.GetObject('winmgmts:')
    wprocess = wmi.InstancesOf('Win32_Process')
    for process in wprocess:
        if process.Properties_('ExecutablePath').Value == post_path:
            return True

    return False


def _get_active_post_object():
    try:
        win32com.client.GetActiveObject("RecurDynPost.Application")
        return True
    except:
        return False


def _wait_while_post_com_is_actived(version, maxDelayTimeSec):
    time_count = 0
    while (time_count < maxDelayTimeSec):
        if not _CheckPostRunning(version):
            return False

        if _get_active_post_object():
            return True

        time.sleep(1)
        time_count += 1
        continue
    return False


def _CheckPostRunning(version):
    if exist_post_name_in_process() and _exist_post_executable_path_in_process(version):
        return True

    print("RecurDyn Post {} is not running.".format(version))
    return False


def _RunPostFromRegistry(version):
    post_path = _get_registry_post_path(version)
    if "" == post_path:
        print("RecurDyn Post {} is not installed.".format(version))
        return False

    recurdyn_process = subprocess.Popen(post_path)

    print("Run RecurDyn Post")
    return True


def dispatch_post(version="2023", autoRunFlag=True, maxDelayTimeSec=300):
    '''
    Dispatch RecurDyn Post Application
	
	:param version: str
	:param autoRunFlag: bool
	:param maxDelayTimeSec: int
    :rtpye: IPostApplication
    '''
    if _get_active_post_object() is False:
        if is_available_use_wmi_tools() and autoRunFlag:
            if not _CheckPostRunning(version):
                _RunPostFromRegistry(version)
                
    return win32com.client.Dispatch("RecurDynPost.Application")

_CONST_ARRAY_DATA_TYPE = [ \
    type([]),\
    type(()),\
    type({1}), ] 


def _get_variant_data_type(data):
    variant_type = 0

    if type(1) == type(data):
        return pythoncom.VT_I8
    elif type(0.1) == type(data):
        return pythoncom.VT_R8
    elif type(True) == type(data):
        return pythoncom.VT_BOOL
    elif type("") == type(data):
        return pythoncom.VT_BSTR
    elif type(data) in _CONST_ARRAY_DATA_TYPE:
        variant_type |= pythoncom.VT_ARRAY
        variant_type |= _get_data_type_in_array_recursive(data)
        return variant_type

    return variant_type


def _get_data_type_in_array_recursive(data):
    if type(data) in _CONST_ARRAY_DATA_TYPE:
        for inner_data in data:
            return _get_data_type_in_array_recursive(inner_data)
        return 0
    else:
        return _get_variant_data_type(data)


def convert_variant_data(data):
    '''
    Converted to variant data type automatically.
    It is dependent on the first data type.
    
    :rtype: win32com.client.VARIANT(variant_type, data)
    '''

    variant_type = _get_variant_data_type(data)
    return win32com.client.VARIANT(variant_type, data)


def convert_variant_int(iValue):
    '''
    Converted to variant int type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_I4, iValue)
    '''
    return win32com.client.VARIANT(pythoncom.VT_I4, iValue)


def convert_variant_int_array(iArray):
    '''
    Converted to variant int array type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_I4, iArray)
    '''
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_I4, iArray)


def convert_variant_float(fValue):
    '''
    Converted to variant float type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_R4, fValue)
    '''
    return win32com.client.VARIANT(pythoncom.VT_R4, fValue)


def convert_variant_float_array(fArray):
    '''
    Converted to variant float array type.
    
    :rtype: variant
    '''
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R4, fArray)


def convert_variant_double(dValue):
    '''
    Converted to variant double type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_R8, dValue)
    '''
    return win32com.client.VARIANT(pythoncom.VT_R8, dValue)


def convert_variant_double_array(dArray):
    '''
    Converted to variant double array type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, dArray)
    '''
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, dArray)


def convert_variant_uint(uiValue):
    '''
    Converted to variant uint type.
    
    :rtype: variant
    '''
    return win32com.client.VARIANT(pythoncom.VT_UI4, uiValue)


def convert_variant_uint_array(uiArray):
    '''
    Converted to variant uint array type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_UI4, uiArray)
    '''
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_UI4, uiArray)


def convert_variant_string(strValue):
    '''
    Converted to variant str type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_BSTR, strValue)
    '''
    return win32com.client.VARIANT(pythoncom.VT_BSTR, strValue)


def convert_variant_string_array(strArray):
    '''
    Converted to variant str array type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_BSTR, strArray)
    '''
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_BSTR, strArray)


def convert_variant_bool(bValue):
    '''
    Converted to variant bool type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_BOOL, bValue)
    '''
    return win32com.client.VARIANT(pythoncom.VT_BOOL, bValue)


def convert_variant_bool_array(bArray):
    '''
    Converted to variant bool array type.
    
    :rtype: win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_BOOL, bArray)
    '''
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_BOOL, bArray)


def get_type(com_object, full_name=False):
    '''
    Get the actual type name of COM object.

    :param com_object: object
    :param full_name: bool
    :rtype: str
    '''
    if not com_object:
        return None

    com_object_type = None
    try:
        com_object_type = type(win32com.client.Dispatch(com_object))
    except:
        pass

    if not com_object_type:
        return None

    if full_name:
        return str(com_object_type)[8:-2]
    else:
        return com_object_type.__name__
