/***************************************************************************
* Copyright (c) Johan Mabille, Sylvain Corlay and Wolf Vollprecht          *
* Copyright (c) QuantStack                                                 *
*                                                                          *
* Distributed under the terms of the BSD 3-Clause License.                 *
*                                                                          *
* The full license is in the file LICENSE, distributed with this software. *
****************************************************************************/

// This file is generated from test/files/cppy_source/test_extended_xmath_interp.cppy by preprocess.py!

#include <algorithm>

#include "gtest/gtest.h"
#include "xtensor/xarray.hpp"
#include "xtensor/xtensor.hpp"
#include "xtensor/xmath.hpp"

namespace xt
{
    using namespace xt::placeholders;

    /*py
    xp = np.sort(np.random.random(20) - 0.5)
    fp = np.random.random(20) - 0.5
    x  = np.linspace(-1,1,50)
    f  = np.interp(x, xp, fp)
    */
    TEST(xtest_extended_xmath, interp)
    {
        // py_xp
        xarray<double> py_xp = {-0.4794155057041976,-0.4419163878318005,-0.3440054796637974,
                                -0.3439813595575635,-0.3181750327928994,-0.3165954901465662,
                                -0.2876608893217238,-0.2087708598019581,-0.1957577570404623,
                                -0.1254598811526375,-0.0680549813578842, 0.0247564316322378,
                                 0.0986584841970366, 0.1011150117432088, 0.2080725777960455,
                                 0.2319939418114051, 0.3324426408004217, 0.3661761457749352,
                                 0.4507143064099162, 0.4699098521619943};
        // py_fp
        xarray<double> py_fp = { 0.1118528947223795,-0.3605061393479582,-0.2078553514647818,
                                -0.1336381567063083,-0.0439300157829641, 0.2851759613930136,
                                -0.3003262178416403, 0.0142344384136116, 0.0924145688620425,
                                -0.4535495872800023, 0.1075448519014384,-0.3294758763127085,
                                -0.4349484070147205, 0.4488855372533332, 0.4656320330745594,
                                 0.3083973481164611,-0.1953862308266293,-0.4023278859936161,
                                 0.1842330265121569,-0.0598475062603987};
        // py_x
        xarray<double> py_x = {-1.                ,-0.9591836734693877,-0.9183673469387755,
                               -0.8775510204081632,-0.8367346938775511,-0.7959183673469388,
                               -0.7551020408163265,-0.7142857142857143,-0.6734693877551021,
                               -0.6326530612244898,-0.5918367346938775,-0.5510204081632654,
                               -0.5102040816326531,-0.4693877551020409,-0.4285714285714286,
                               -0.3877551020408164,-0.3469387755102041,-0.3061224489795918,
                               -0.2653061224489797,-0.2244897959183674,-0.1836734693877552,
                               -0.1428571428571429,-0.1020408163265307,-0.0612244897959184,
                               -0.0204081632653061, 0.0204081632653061, 0.0612244897959182,
                                0.1020408163265305, 0.1428571428571428, 0.1836734693877551,
                                0.2244897959183672, 0.2653061224489794, 0.3061224489795917,
                                0.346938775510204 , 0.3877551020408163, 0.4285714285714284,
                                0.4693877551020407, 0.510204081632653 , 0.5510204081632653,
                                0.5918367346938773, 0.6326530612244896, 0.6734693877551019,
                                0.7142857142857142, 0.7551020408163265, 0.7959183673469385,
                                0.8367346938775508, 0.8775510204081631, 0.9183673469387754,
                                0.9591836734693877, 1.                };
        // py_f
        xarray<double> py_f = { 0.1118528947223795, 0.1118528947223795, 0.1118528947223795,
                                0.1118528947223795, 0.1118528947223795, 0.1118528947223795,
                                0.1118528947223795, 0.1118528947223795, 0.1118528947223795,
                                0.1118528947223795, 0.1118528947223795, 0.1118528947223795,
                                0.1118528947223795,-0.0144620389902249,-0.3397003008210678,
                               -0.276064445327787 ,-0.2124285898345059, 0.0732501614278388,
                               -0.2111903640369242,-0.0484421620454266,-0.0014373125435324,
                               -0.3184348176553962,-0.2246439173504261, 0.0753821436708398,
                               -0.1168095294085587,-0.3090012024879573,-0.3815228526932218,
                                0.4490304917727565, 0.4554211611466747, 0.4618118305205929,
                                0.3577219608188899, 0.1413257010677429,-0.063381729350545 ,
                               -0.2843142598776403,-0.2526041141115967, 0.0305965322604367,
                               -0.0532087927693443,-0.0598475062603987,-0.0598475062603987,
                               -0.0598475062603987,-0.0598475062603987,-0.0598475062603987,
                               -0.0598475062603987,-0.0598475062603987,-0.0598475062603987,
                               -0.0598475062603987,-0.0598475062603987,-0.0598475062603987,
                               -0.0598475062603987,-0.0598475062603987};

        auto f = xt::interp(py_x, py_xp, py_fp);

        EXPECT_TRUE(xt::allclose(f, py_f));
    }
}

