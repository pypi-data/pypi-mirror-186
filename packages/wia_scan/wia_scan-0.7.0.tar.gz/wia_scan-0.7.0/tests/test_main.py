import os

import wia_scan as ws

from test_base import *

import pytest

def test_entry_point():
    exit_status = os.system('wia_scan --help')
    assert exit_status == 0
    exit_status = os.system('wia_scan --version')
    assert exit_status == 0

    # check that uid is required
    exit_status = os.system('wia_scan single -q')
    assert exit_status == -1


def test_main():
    ws.main(argv=['list_devices'])
    ws.main(argv=['list_devices', '-v'])
    
    ws.list_devices(get_device_manager_mock(), verbose=True)

def test_single():
    output_folder = get_output_folder()

    output_file = os.path.join(output_folder, '1.png')
    with mock.patch.object(ws.core, 'get_device_manager', new=get_device_manager_mock):
        ws.main(argv=['single', f'--file={output_file}', '-q', f'--uid={MOCK_DEVICE_UID}'])

    with pytest.raises(SystemExit):
        ws.main(argv=['single', f'--file={output_file}', '-q'])
    
    with mock.patch.object(ws.core, 'get_device_manager', new=get_device_manager_mock):
        ws.scan_single_side_main(quiet=True, device_uid=MOCK_DEVICE_UID,
            output_file=os.path.join(output_folder, '2.png'))
    

def ask_for_an_int_mock(prompt_message, number_of_sides):
    if prompt_message == 'Choose a device number':
        return 1
    if prompt_message == 'Input number of sides of this document (0 to stop)':
        print('number_of_sides', number_of_sides)
        return number_of_sides.pop(0)
    raise NotImplementedError


def prompt_scan_profile_mock(print_function, scan_profile_answers):
    return scan_profile_answers.pop(0)


def test_many():
    output_folder = get_output_folder()

    number_of_sides = [1, 2, 0]
    scan_profile_answers = ['h', 'g', 'c']
    with mock.patch.object(ws.core, 'get_device_manager', new=get_device_manager_mock):
        with mock.patch.object(ws.core, 'ask_for_an_int',
                               new=lambda prompt_message, default, valid_range: ask_for_an_int_mock(prompt_message, number_of_sides)):
            with mock.patch.object(ws.core, 'prompt_scan_profile',
                                   new=lambda print_function: prompt_scan_profile_mock(print_function=print_function,
                                        scan_profile_answers=scan_profile_answers)):
                ws.main(argv=['many', f'--out={output_folder}', '-v'])


def test_calibration():
    output_folder = get_output_folder()

    with mock.patch.object(ws.core, 'get_device_manager', new=get_device_manager_mock):
        with mock.patch.object(ws.core, 'ask_for_an_int',
                               new=lambda prompt_message, default, valid_range: ask_for_an_int_mock(prompt_message, [])):
            ws.main(
                argv=['calibrate', 'brightness', '--start=-1000',
                      '--end=1000', '--num_runs=9', f'--uid={MOCK_DEVICE_UID}',
                      f'--out={output_folder}'])
