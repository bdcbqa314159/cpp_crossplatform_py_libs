#include "functions.hpp"

#include <cmath>

#include "constants.hpp"

double sinh_impl(double x) { return (1 - pow(e, (-2 * x))) / (2 * pow(e, -x)); }

double cosh_impl(double x) { return (1 + pow(e, (-2 * x))) / (2 * pow(e, -x)); }

double tanh_impl(double x) { return sinh_impl(x) / cosh_impl(x); }