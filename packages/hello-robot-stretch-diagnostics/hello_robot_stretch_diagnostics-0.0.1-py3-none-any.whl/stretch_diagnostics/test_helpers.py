from colorama import Fore, Style
import os
import glob
import pyrealsense2 as rs
import stretch_factory.hello_device_utils as hdu

def val_in_range(val_name, val, vmin, vmax,silent=False):
    p = val <= vmax and val >= vmin
    if silent:
        return p
    if p:
        print(Fore.GREEN + '[Pass] ' + val_name + ' = ' + str(val))
        print(Style.RESET_ALL)
        return True
    else:
        print(Fore.RED + '[Fail] ' + val_name + ' = ' + str(val) + ' out of range ' + str(vmin) + ' to ' + str(vmax))
        print(Style.RESET_ALL)
        return False


def val_is_not(val_name, val, vnot):
    if val is not vnot:
        print(Fore.GREEN + '[Pass] ' + val_name + ' = ' + str(val))
        return True
    else:
        print(Fore.RED + '[Fail] ' + val_name + ' = ' + str(val))
        return False


def confirm(question: str) -> bool:
    reply = None
    while reply not in ("y", "n"):
        reply = input(Style.BRIGHT + f"{question} (y/n): " + Style.RESET_ALL).lower()
    return (reply == "y")


def print_instruction(text, ret=0):
    return_text = Fore.BLUE + Style.BRIGHT + 'INSTRUCTION:' + Style.RESET_ALL + Style.BRIGHT + text + Style.RESET_ALL
    if ret == 1:
        return return_text
    else:
        print(return_text)

def print_bright(text):
    print(Style.BRIGHT + Fore.BLUE + text + Style.RESET_ALL)

def print_bright_red(text):
    print(Style.BRIGHT + Fore.RED + text + Style.RESET_ALL)



def system_check_warn(warning=None):
    def decorator(test_item):
        test_item.__system_check_warn__ = True
        test_item.__system_check_warning__ = warning
        return test_item

    return decorator


def command_list_exec(cmd_list):
    cmd = ''
    for c in cmd_list:
        cmd = cmd + c + ';'
    os.system(cmd)



def find_tty_devices():
    devices_dict = {}
    ttyUSB_dev_list = glob.glob('/dev/ttyUSB*')
    ttyACM_dev_list = glob.glob('/dev/ttyACM*')
    for d in ttyACM_dev_list:
        devices_dict[d] = {"serial": extract_udevadm_info(d, 'ID_SERIAL_SHORT'),
                           "vendor": extract_udevadm_info(d, 'ID_VENDOR'),
                           "model": extract_udevadm_info(d, 'ID_MODEL'),
                           "path": extract_udevadm_info(d, 'DEVPATH')}
    for d in ttyUSB_dev_list:
        devices_dict[d] = {"serial": extract_udevadm_info(d, 'ID_SERIAL_SHORT'),
                           "vendor": extract_udevadm_info(d, 'ID_VENDOR'),
                           "model": extract_udevadm_info(d, 'ID_MODEL'),
                           "path": extract_udevadm_info(d, 'DEVPATH')}
    return devices_dict


def get_serial_nos_from_udev(udev_file_full_path, device_name):
    sns = []
    try:
        f = open(udev_file_full_path, 'r')
        x = f.readlines()
        f.close()
        lines = []
        for xx in x:
            if xx.find(device_name) > 0 and xx[0] != '#':
                lines.append(xx)
        for l in lines:
            ll = l.split(',')
            for q in ll:
                if q.find('serial') > -1:
                    s = q[q.find('"') + 1:q.rfind('"')]
                    if len(s) == 8 or len(s) == 32:  # FTDI or Arduino
                        sns.append(s)
    except:
        pass
    return sns


def find_ftdi_devices_sn():
    devices_dict = {}
    ttyUSB_dev_list = glob.glob('/dev/ttyUSB*')
    for d in ttyUSB_dev_list:
        devices_dict[d] = extract_udevadm_info(d, 'ID_SERIAL_SHORT')
    return devices_dict


def find_arduino_devices_sn():
    devices_dict = {}
    ttyACM_dev_list = glob.glob('/dev/ttyACM*')
    for d in ttyACM_dev_list:
        devices_dict[d] = extract_udevadm_info(d, 'ID_SERIAL_SHORT')
    return devices_dict


def extract_udevadm_info(usb_port, ID_NAME=None):
    """
    Extracts usb device attributes with the given attribute ID_NAME

    example ID_NAME:
    ID_SERIAL_SHORT
    ID_MODEL
    DEVPATH
    ID_VENDOR_FROM_DATABASE
    ID_VENDOR
    """
    value = None
    dname = bytes(usb_port[5:], 'utf-8')
    out = hdu.exec_process([b'udevadm', b'info', b'-n', dname], True)
    if ID_NAME is None:
        value = out.decode(encoding='UTF-8')
    else:
        for a in out.split(b'\n'):
            a = a.decode(encoding='UTF-8')
            if "{}=".format(ID_NAME) in a:
                value = a.split('=')[-1]
    return value

def get_rs_details():
    """
    Returns the details of the first found realsense devices in the bus
    """
    dev = None
    ctx = rs.context()
    devices = ctx.query_devices()
    found_dev = False
    for dev in devices:
        if dev.get_info(rs.camera_info.serial_number):
            found_dev = True
            break
    if not found_dev:
        print('No RealSense device found.')
        return None

    data = {}
    data["device_pid"] =  dev.get_info(rs.camera_info.product_id)
    data["device_name"] = dev.get_info(rs.camera_info.name)
    data["serial"] = dev.get_info(rs.camera_info.serial_number)
    data["firmware_version"] = dev.get_info(rs.camera_info.firmware_version)

    return data

