/* IBM_PROLOG_BEGIN_TAG                                                   */
/* This is an automatically generated prolog.                             */
/*                                                                        */
/* $Source: src/import/chips/p9/procedures/hwp/cache/p9_hcd_cache_chiplet_l3_dcc_setup.C $ */
/*                                                                        */
/* OpenPOWER sbe Project                                                  */
/*                                                                        */
/* Contributors Listed Below - COPYRIGHT 2016,2017                        */
/* [+] International Business Machines Corp.                              */
/*                                                                        */
/*                                                                        */
/* Licensed under the Apache License, Version 2.0 (the "License");        */
/* you may not use this file except in compliance with the License.       */
/* You may obtain a copy of the License at                                */
/*                                                                        */
/*     http://www.apache.org/licenses/LICENSE-2.0                         */
/*                                                                        */
/* Unless required by applicable law or agreed to in writing, software    */
/* distributed under the License is distributed on an "AS IS" BASIS,      */
/* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or        */
/* implied. See the License for the specific language governing           */
/* permissions and limitations under the License.                         */
/*                                                                        */
/* IBM_PROLOG_END_TAG                                                     */
//------------------------------------------------------------------------------
/// @file  p9_hcd_cache_chiplet_l3_dcc_setup.C
///
/// @brief Setup L3 DCC, Drop L3 DCC bypass
//------------------------------------------------------------------------------
// *HWP HW Owner        : Anusha Reddy Rangareddygari <anusrang@in.ibm.com>
// *HWP HW Backup Owner : Srinivas V Naga <srinivan@in.ibm.com>
// *HWP FW Owner        : Sunil Kumar <skumar8j@in.ibm.com>
// *HWP Team            : Perv
// *HWP Consumed by     : SBE:SGPE
// *HWP Level           : 3
//------------------------------------------------------------------------------


//## auto_generated
#include "p9_hcd_cache_chiplet_l3_dcc_setup.H"

#include <p9_quad_scom_addresses.H>
#include <p9_quad_scom_addresses_fld.H>
#include <p9_ring_id.h>


fapi2::ReturnCode p9_hcd_cache_chiplet_l3_dcc_setup(const
        fapi2::Target<fapi2::TARGET_TYPE_EQ>& i_target_chiplet)
{
    const fapi2::Target<fapi2::TARGET_TYPE_SYSTEM> FAPI_SYSTEM;
    fapi2::buffer<uint64_t> l_data64;
    FAPI_DBG("Entering ...");

    FAPI_DBG("Scan eq_ana_bndy_bucket_l3dcc ring");
    FAPI_TRY(fapi2::putRing(i_target_chiplet, eq_ana_bndy_bucket_l3dcc, fapi2::RING_MODE_SET_PULSE_NSL),
             "Error from putRing (eq_ana_bndy_bucket_l3dcc)");

    FAPI_DBG("Drop L3 DCC bypass");
    //Setting NET_CTRL1 register value
    l_data64.flush<1>();
    //NET_CTRL1.CLK_DCC_BYPASS_EN = 0
    l_data64.clearBit<C_NET_CTRL1_CLK_DCC_BYPASS_EN>();
    FAPI_TRY(fapi2::putScom(i_target_chiplet, EQ_NET_CTRL1_WAND, l_data64));

    FAPI_DBG("Exiting ...");

fapi_try_exit:
    return fapi2::current_err;

}
