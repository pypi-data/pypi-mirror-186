import os
import math

from PIL import Image as PILImage
from PIL import ImageEnhance

import mock

WIA_FORMAT_BMP = '{B96B3CAB-0728-11D3-9D7B-0000F81EF32E}'
MOCK_DEVICE_UID = '123'

class MockProperty:
    def __init__(self, key, value, IsReadOnly):
        self.Name = key
        self.Value = value
        self.IsReadOnly = IsReadOnly


class MockList:
    def __init__(self, values):
        self.values = values

    @property
    def Count(self):
        return len(self.values)

    def __call__(self, idx):
        if isinstance(idx, int):
            assert (idx >= 1 and idx <= len(self.values))
            return self.values[idx-1]
        else:
            raise ValueError

    def __iter__(self):
        return self.values.__iter__()


class MockSCList:
    def __init__(self, values, attribute_name):
        self.values = values
        self.attribute_name = attribute_name

    @property
    def Count(self):
        return len(self.values)

    def __call__(self, idx):
        if isinstance(idx, int):
            assert (idx >= 1 and idx <= len(self.values))
            return self.values[idx-1]
        elif isinstance(idx, str):
            for prop_ in self:
                if getattr(prop_, self.attribute_name) == idx:
                    return prop_
            return None
        else:
            raise ValueError

    def __iter__(self):
        return self.values.__iter__()


class MockCommand:
    def __init__(self, id, description):
        self.Name = id
        self.CommandID = id
        self.Description = description


def clamp(i):
    return 0 if i < 0 else (255 if i > 255 else i)


class MockImage:
    def __init__(self, width, height, brightness, contrast, formatID):
        self.brightness = brightness
        self.contrast = contrast
        self.FormatID = formatID
        self.FrameCount = 1
        self.IsAlphaPixelFormat = False
        self.IsExtendedPixelFormat = False
        self.IsIndexedPixelFormat = False
        self.PixelDepth = 24
        self.VerticalResolution = 100
        self.Width = width
        self.Height = height

    def SaveFile(self, output_file):
        img = PILImage.new(mode="RGB", size=(self.Width, self.Height))
        pixels = img.load()
        brightness = self.brightness
        const_off = brightness / 1000.0
        for i in range(self.Height):
            for j in range(self.Width):
                pixels[i, j] = (
                    clamp(int((i/self.Height + const_off)*255)),
                    clamp(int((j/self.Width + const_off)*255)),
                    clamp(int((0.5 + const_off)*255)),
                )
        contrast_lambda = (self.contrast + 1000.0)/2000.0
        contrast_factor = 1.0 / (1.0 - contrast_lambda) - 1.0
        img = ImageEnhance.Contrast(img).enhance(contrast_factor)
        img.save(output_file)


class MockDevice:
    def __init__(self):
        self.Items = MockList([])
        self.Properties = MockSCList([
            MockProperty('Brightness', '1000', False),
            MockProperty('Contrast', '1000', False),
            MockProperty('Horizontal Resolution', '200', False),
            MockProperty('Vertical Resolution', '200', False),
            MockProperty('Data Type', '3', False),
            MockProperty('Preferred Format', WIA_FORMAT_BMP, True),
            MockProperty('Format', WIA_FORMAT_BMP, False),
        ], "Name")
        self.Commands = MockList([
            MockCommand("{AF933CAC-ACAD-11D2-A093-00C04F72DC3C}",
                        'Take picture')
        ])
        self.imageCount = 0
        self.Formats = MockList([
            WIA_FORMAT_BMP
        ])

    def ExecuteCommand(self, commandId):
        assert commandId == "{AF933CAC-ACAD-11D2-A093-00C04F72DC3C}"
        self.imageCount += 1

    def Transfer(self, format):
        self.imageCount -= 1
        assert self.imageCount >= 0
        return MockImage(
            100, 100, self.Properties('Brightness').Value, self.
            Properties('Contrast').Value,
            WIA_FORMAT_BMP)


class MockDeviceInfo:
    def __init__(self):
        self.DeviceID = MOCK_DEVICE_UID
        self.Type = 1
        self.properties = MockSCList([
            MockProperty('Unique Device ID', MOCK_DEVICE_UID, True),
            MockProperty('Manufacturer', 'MockManu', True),
            MockProperty('Description', 'Insert Description', True),
            MockProperty('Server', 'local', True),
            MockProperty('Port', '//port1', True),
            MockProperty('Name', 'MockDevice', True)
        ], "Name")

    @property
    def Properties(self):
        return self.properties

    def Connect(self):
        return MockDevice()


class MockDeviceManager:
    def __init__(self):
        # https://learn.microsoft.com/en-us/previous-versions/windows/desktop/wiaaut/-wiaaut-deviceinfo
        self.DeviceInfos = MockSCList([MockDeviceInfo()], "DeviceID")


def get_device_manager_mock():
    return MockDeviceManager()


def get_output_folder():
    output_folder = './test_output'
    os.makedirs(output_folder, exist_ok=True)
    return output_folder
