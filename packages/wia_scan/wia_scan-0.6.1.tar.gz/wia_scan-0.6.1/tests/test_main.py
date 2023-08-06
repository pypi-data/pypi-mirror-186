import os

from wia_scan import main as scan_main
from wia_scan import scan_functions

from test_base import *


def test_entry_point():
    exit_status = os.system('wia_scan --help')
    assert exit_status == 0
    exit_status = os.system('wia_scan --version')
    assert exit_status == 0

    # check that uid is required
    exit_status = os.system('wia_scan single -q')
    assert exit_status == -1


def test_main():
    scan_main(argv=['list_devices'])
    scan_main(argv=['list_devices', '-v'])


def test_single():
    output_folder = get_output_folder()

    output_file = os.path.join(output_folder, '1.png')
    with mock.patch.object(scan_functions, 'get_device_manager', new=get_device_manager_mock):
        scan_main(argv=['single', f'--file={output_file}', '-q', '--uid=123'])


def ask_for_an_int_mock(prompt_message, number_of_sides):
    if prompt_message == 'Choose a device number':
        return 1
    if prompt_message == 'Input number of sides of this document (0 to stop)':
        print('number_of_sides', number_of_sides)
        return number_of_sides.pop(0)
    raise NotImplementedError


def prompt_scan_profile_mock(print_function):
    return 'c'


def test_many():
    output_folder = get_output_folder()

    number_of_sides = [1, 2, 0]
    with mock.patch.object(scan_functions, 'get_device_manager', new=get_device_manager_mock):
        with mock.patch.object(scan_functions, 'ask_for_an_int',
                               new=lambda prompt_message, default, valid_range: ask_for_an_int_mock(prompt_message, number_of_sides)):
            with mock.patch.object(scan_functions, 'prompt_scan_profile',
                                   new=prompt_scan_profile_mock):
                scan_main(argv=['many', f'--out={output_folder}', '-v'])


def test_calibration():
    output_folder = get_output_folder()

    with mock.patch.object(scan_functions, 'get_device_manager', new=get_device_manager_mock):
        with mock.patch.object(scan_functions, 'ask_for_an_int',
                               new=lambda prompt_message, default, valid_range: ask_for_an_int_mock(prompt_message, [])):
            scan_main(
                argv=['calibrate', 'brightness', '--start=-1000',
                      '--end=1000', '--num_runs=9', '-q', '--uid=123',
                      f'--out={output_folder}'])
