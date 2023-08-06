##  python-exiv2 - Python interface to libexiv2
##  http://github.com/jim-easterbrook/python-exiv2
##  Copyright (C) 2022  Jim Easterbrook  jim@jim-easterbrook.me.uk
##
##  This program is free software: you can redistribute it and/or
##  modify it under the terms of the GNU General Public License as
##  published by the Free Software Foundation, either version 3 of the
##  License, or (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
##  General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see
##  <http://www.gnu.org/licenses/>.

import os
import unittest

import exiv2


class TestMiscellaneous(unittest.TestCase):
    def test_xmp_properties(self):
        ns = exiv2.XmpProperties.registeredNamespaces()
        self.assertIsInstance(ns, dict)
        self.assertEqual(ns['exif'], 'http://ns.adobe.com/exif/1.0/')
        info = exiv2.XmpProperties.nsInfo('exif')
        self.assertEqual(info.ns_, 'http://ns.adobe.com/exif/1.0/')
        self.assertEqual(info.prefix_, 'exif')
        self.assertEqual(info.desc_, 'Exif schema for Exif-specific Properties')
        props = info.xmpPropertyInfo_
        self.assertEqual(props[0].name_, 'ExifVersion')
        props = exiv2.XmpProperties.propertyList('exif')
        self.assertEqual(props[0].name_, 'ExifVersion')


if __name__ == '__main__':
    unittest.main()
