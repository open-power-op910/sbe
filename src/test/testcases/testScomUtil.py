# IBM_PROLOG_BEGIN_TAG
# This is an automatically generated prolog.
#
# $Source: src/test/testcases/testScomUtil.py $
#
# OpenPOWER sbe Project
#
# Contributors Listed Below - COPYRIGHT 2017
#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied. See the License for the specific language governing
# permissions and limitations under the License.
#
# IBM_PROLOG_END_TAG
import sys
import os
import struct
sys.path.append("targets/p9_nimbus/sbeTest" )
import testUtil
err = False

def getsingleword(dataInInt):
    hex_string = '0'*(8-len(str(hex(dataInInt))[2:])) + str(hex(dataInInt))[2:]
    return list(struct.unpack('<BBBB',hex_string.decode('hex')))
def getdoubleword(dataInInt):
    hex_string = '0'*(16-len(str(hex(dataInInt))[:18][2:])) + str(hex(dataInInt))[:18][2:]
    return list(struct.unpack('<BBBBBBBB',hex_string.decode('hex')))

def getscom(addr, expStatus = [0, 0, 0, 0], HWPffdc = False):
    req = ([0, 0, 0, 4]
          + [0,0,0xA2,0x01]
          + getdoubleword(addr))

    testUtil.writeUsFifo(req)
    testUtil.writeEot( )

    expData = ([0xc0,0xde,0xa2,0x01]
              + expStatus)
    success = False
    if(expStatus == [0, 0, 0, 0]):
        success = True

    data = [0]*8
    if(success):
        data = testUtil.readDsEntryReturnVal()
        data += testUtil.readDsEntryReturnVal()
    testUtil.readDsFifo(expData)
    if(not success and HWPffdc):
        testUtil.extractHWPFFDC( )
    #flush out distance
    testUtil.readDsEntryReturnVal()
    testUtil.readEot( )

    val = 0
    for i in range(0, 8):
        val |= data[i] << ((7-i)*8)
    return val

def putscom(addr, data, expStatus = [0, 0, 0, 0]):
    req = ([0,0,0,6,
            0,0,0xA2,0x02]
          + getdoubleword(addr)
          + getdoubleword(data))
    testUtil.writeUsFifo(req)
    testUtil.writeEot( )

    expData = ([0xc0,0xde,0xa2,0x02]
               + expStatus)

    success = False
    if(expStatus == [0, 0, 0, 0]):
        success = True
    testUtil.readDsFifo(expData)
    #flush out distance
    testUtil.readDsEntryReturnVal()
    testUtil.readEot( )

def putScomUnderMask(addr, data, mask, expStatus = [0, 0, 0, 0]):
    req = ([0,0,0,8,
            0,0,0xA2,0x04]
          + getdoubleword(addr)
          + getdoubleword(data)
          + getdoubleword(mask))
    testUtil.writeUsFifo(req)
    testUtil.writeEot( )

    expData = ([0xc0,0xde,0xa2,0x04]
               + expStatus)

    success = False
    if(expStatus == [0, 0, 0, 0]):
        success = True
    testUtil.readDsFifo(expData)
    #flush out distance
    testUtil.readDsEntryReturnVal()
    testUtil.readEot( )

def modifyScom(operation, addr, data, expStatus = [0, 0, 0, 0]):
    req = ([0,0,0,7,
            0,0,0xA2,0x03]
          + getsingleword(operation)
          + getdoubleword(addr)
          + getdoubleword(data))
    testUtil.writeUsFifo(req)
    testUtil.writeEot( )

    expData = ([0xc0,0xde,0xa2,0x03]
               + expStatus)

    success = False
    if(expStatus == [0, 0, 0, 0]):
        success = True
    testUtil.readDsFifo(expData)
    #flush out distance
    testUtil.readDsEntryReturnVal()
    testUtil.readEot( )
