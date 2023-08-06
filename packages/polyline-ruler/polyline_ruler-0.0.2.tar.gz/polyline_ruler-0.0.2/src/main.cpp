// https://github.com/microsoft/vscode-cpptools/issues/9692
#if __INTELLISENSE__
#undef __ARM_NEON
#undef __ARM_NEON__
#endif

#include <Eigen/Core>

#include <pybind11/eigen.h>
#include <pybind11/iostream.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>

#include "cheap_ruler.hpp"
#include "crs_transform.hpp"
#include "eigen_helpers.hpp"
#include "polyline_ruler.hpp"

#define CUBAO_ARGV_DEFAULT_NONE(argv) py::arg_v(#argv, std::nullopt, "None")

#include "pybind11_crs_transform.hpp"
#include "pybind11_polyline_ruler.hpp"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

namespace py = pybind11;
using rvp = py::return_value_policy;
using namespace pybind11::literals;

PYBIND11_MODULE(polyline_ruler, m)
{
    m.doc() = R"pbdoc(
        cubao/polyline-ruler is more than mapbox/cheap-ruler
        ----------------------------------------------------

        .. currentmodule:: polyline_ruler

        .. autosummary::
           :toctree: _generate

           TODO
    )pbdoc";

    auto tf = m.def_submodule("tf");
    cubao::bind_crs_transform(tf);

    cubao::bind_polyline_ruler(m);

#ifdef VERSION_INFO
    m.attr("__version__") = MACRO_STRINGIFY(VERSION_INFO);
#else
    m.attr("__version__") = "dev";
#endif
}
