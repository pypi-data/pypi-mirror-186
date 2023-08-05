
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <..\..\_impl\include\frc\filter\LinearFilter.h>





namespace rpygen {

using namespace frc;


template <typename T>
struct bind_frc__LinearFilter {

    
    
    
    py::class_<typename frc::LinearFilter<T>> cls_LinearFilter;




    py::module &m;
    std::string clsName;

bind_frc__LinearFilter(py::module &m, const char * clsName) :
    cls_LinearFilter(m, clsName),



    m(m),
    clsName(clsName)
{
    
}

void finish(const char * set_doc = NULL, const char * add_doc = NULL) {

    
  cls_LinearFilter.doc() =
    "This class implements a linear, digital filter. All types of FIR and IIR\n"
"filters are supported. Static factory methods are provided to create commonly\n"
"used types of filters.\n"
"\n"
"Filters are of the form:\n"
"y[n] = (b0 x[n] + b1 x[n-1] + … + bP x[n-P]) -\n"
"(a0 y[n-1] + a2 y[n-2] + … + aQ y[n-Q])\n"
"\n"
"Where:\n"
"y[n] is the output at time \"n\"\n"
"x[n] is the input at time \"n\"\n"
"y[n-1] is the output from the LAST time step (\"n-1\")\n"
"x[n-1] is the input from the LAST time step (\"n-1\")\n"
"b0 … bP are the \"feedforward\" (FIR) gains\n"
"a0 … aQ are the \"feedback\" (IIR) gains\n"
"IMPORTANT! Note the \"-\" sign in front of the feedback term! This is a common\n"
"convention in signal processing.\n"
"\n"
"What can linear filters do? Basically, they can filter, or diminish, the\n"
"effects of undesirable input frequencies. High frequencies, or rapid changes,\n"
"can be indicative of sensor noise or be otherwise undesirable. A \"low pass\"\n"
"filter smooths out the signal, reducing the impact of these high frequency\n"
"components.  Likewise, a \"high pass\" filter gets rid of slow-moving signal\n"
"components, letting you detect large changes more easily.\n"
"\n"
"Example FRC applications of filters:\n"
"- Getting rid of noise from an analog sensor input (note: the roboRIO's FPGA\n"
"can do this faster in hardware)\n"
"- Smoothing out joystick input to prevent the wheels from slipping or the\n"
"robot from tipping\n"
"- Smoothing motor commands so that unnecessary strain isn't put on\n"
"electrical or mechanical components\n"
"- If you use clever gains, you can make a PID controller out of this class!\n"
"\n"
"For more on filters, we highly recommend the following articles:\n"
"https://en.wikipedia.org/wiki/Linear_filter\n"
"https://en.wikipedia.org/wiki/Iir_filter\n"
"https://en.wikipedia.org/wiki/Fir_filter\n"
"\n"
"Note 1: Calculate() should be called by the user on a known, regular period.\n"
"You can use a Notifier for this or do it \"inline\" with code in a\n"
"periodic function.\n"
"\n"
"Note 2: For ALL filters, gains are necessarily a function of frequency. If\n"
"you make a filter that works well for you at, say, 100Hz, you will most\n"
"definitely need to adjust the gains if you then want to run it at 200Hz!\n"
"Combining this with Note 1 - the impetus is on YOU as a developer to make\n"
"sure Calculate() gets called at the desired, constant frequency!";

  cls_LinearFilter
      .def(py::init<std::span<const double >, std::span<const double >>(),
      py::arg("ffGains"), py::arg("fbGains"), release_gil(), py::doc(
    "Create a linear FIR or IIR filter.\n"
"\n"
":param ffGains: The \"feedforward\" or FIR gains.\n"
":param fbGains: The \"feedback\" or IIR gains.")
  )
    
      .def_static("singlePoleIIR", &frc::LinearFilter<T>::SinglePoleIIR,
      py::arg("timeConstant"), py::arg("period"), release_gil(), py::doc(
    "Creates a one-pole IIR low-pass filter of the form:\n"
"y[n] = (1 - gain) x[n] + gain y[n-1]\n"
"where gain = e:sup:`-dt / T`, T is the time constant in seconds\n"
"\n"
"Note: T = 1 / (2 pi f) where f is the cutoff frequency in Hz, the frequency\n"
"above which the input starts to attenuate.\n"
"\n"
"This filter is stable for time constants greater than zero.\n"
"\n"
":param timeConstant: The discrete-time time constant in seconds.\n"
":param period:       The period in seconds between samples taken by the\n"
"                     user.")
  )
    
      .def_static("highPass", &frc::LinearFilter<T>::HighPass,
      py::arg("timeConstant"), py::arg("period"), release_gil(), py::doc(
    "Creates a first-order high-pass filter of the form:\n"
"y[n] = gain x[n] + (-gain) x[n-1] + gain y[n-1]\n"
"where gain = e:sup:`-dt / T`, T is the time constant in seconds\n"
"\n"
"Note: T = 1 / (2 pi f) where f is the cutoff frequency in Hz, the frequency\n"
"below which the input starts to attenuate.\n"
"\n"
"This filter is stable for time constants greater than zero.\n"
"\n"
":param timeConstant: The discrete-time time constant in seconds.\n"
":param period:       The period in seconds between samples taken by the\n"
"                     user.")
  )
    
      .def_static("movingAverage", &frc::LinearFilter<T>::MovingAverage,
      py::arg("taps"), release_gil(), py::doc(
    "Creates a K-tap FIR moving average filter of the form:\n"
"y[n] = 1/k (x[k] + x[k-1] + … + x[0])\n"
"\n"
"This filter is always stable.\n"
"\n"
":param taps: The number of samples to average over. Higher = smoother but\n"
"             slower\n"
"             @throws std::runtime_error if number of taps is less than 1.")
  )
    
      .def("reset", &frc::LinearFilter<T>::Reset, release_gil(), py::doc(
    "Reset the filter state.")
  )
    
      .def("calculate", &frc::LinearFilter<T>::Calculate,
      py::arg("input"), release_gil(), py::doc(
    "Calculates the next value of the filter.\n"
"\n"
":param input: Current input value.\n"
"\n"
":returns: The filtered value at this step")
  )
    
;

  

    if (set_doc) {
        cls_LinearFilter.doc() = set_doc;
    }
    if (add_doc) {
        cls_LinearFilter.doc() = py::cast<std::string>(cls_LinearFilter.doc()) + add_doc;
    }

    
}

}; // struct bind_frc__LinearFilter

}; // namespace rpygen