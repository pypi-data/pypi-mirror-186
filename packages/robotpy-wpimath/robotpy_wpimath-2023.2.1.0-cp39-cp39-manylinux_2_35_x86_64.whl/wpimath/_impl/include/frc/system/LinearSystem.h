// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#pragma once

#include <algorithm>
#include <functional>
#include <stdexcept>

#include "frc/EigenCore.h"
#include "frc/StateSpaceUtil.h"
#include "frc/system/Discretization.h"
#include "units/time.h"

namespace frc {

/**
 * A plant defined using state-space notation.
 *
 * A plant is a mathematical model of a system's dynamics.
 *
 * For more on the underlying math, read
 * https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
 *
 * @tparam States Number of states.
 * @tparam Inputs Number of inputs.
 * @tparam Outputs Number of outputs.
 */
template <int States, int Inputs, int Outputs>
class LinearSystem {
 public:
  using StateVector = Vectord<States>;
  using InputVector = Vectord<Inputs>;
  using OutputVector = Vectord<Outputs>;

  /**
   * Constructs a discrete plant with the given continuous system coefficients.
   *
   * @param A    System matrix.
   * @param B    Input matrix.
   * @param C    Output matrix.
   * @param D    Feedthrough matrix.
   * @throws std::domain_error if any matrix element isn't finite.
   */
  LinearSystem(const Matrixd<States, States>& A,
               const Matrixd<States, Inputs>& B,
               const Matrixd<Outputs, States>& C,
               const Matrixd<Outputs, Inputs>& D) {
    if (!A.allFinite()) {
      throw std::domain_error(
          "Elements of A aren't finite. This is usually due to model "
          "implementation errors.");
    }
    if (!B.allFinite()) {
      throw std::domain_error(
          "Elements of B aren't finite. This is usually due to model "
          "implementation errors.");
    }
    if (!C.allFinite()) {
      throw std::domain_error(
          "Elements of C aren't finite. This is usually due to model "
          "implementation errors.");
    }
    if (!D.allFinite()) {
      throw std::domain_error(
          "Elements of D aren't finite. This is usually due to model "
          "implementation errors.");
    }

    m_A = A;
    m_B = B;
    m_C = C;
    m_D = D;
  }

  LinearSystem(const LinearSystem&) = default;
  LinearSystem& operator=(const LinearSystem&) = default;
  LinearSystem(LinearSystem&&) = default;
  LinearSystem& operator=(LinearSystem&&) = default;

  /**
   * Returns the system matrix A.
   */
  const Matrixd<States, States>& A() const { return m_A; }

  /**
   * Returns an element of the system matrix A.
   *
   * @param i Row of A.
   * @param j Column of A.
   */
  double A(int i, int j) const { return m_A(i, j); }

  /**
   * Returns the input matrix B.
   */
  const Matrixd<States, Inputs>& B() const { return m_B; }

  /**
   * Returns an element of the input matrix B.
   *
   * @param i Row of B.
   * @param j Column of B.
   */
  double B(int i, int j) const { return m_B(i, j); }

  /**
   * Returns the output matrix C.
   */
  const Matrixd<Outputs, States>& C() const { return m_C; }

  /**
   * Returns an element of the output matrix C.
   *
   * @param i Row of C.
   * @param j Column of C.
   */
  double C(int i, int j) const { return m_C(i, j); }

  /**
   * Returns the feedthrough matrix D.
   */
  const Matrixd<Outputs, Inputs>& D() const { return m_D; }

  /**
   * Returns an element of the feedthrough matrix D.
   *
   * @param i Row of D.
   * @param j Column of D.
   */
  double D(int i, int j) const { return m_D(i, j); }

  /**
   * Computes the new x given the old x and the control input.
   *
   * This is used by state observers directly to run updates based on state
   * estimate.
   *
   * @param x        The current state.
   * @param clampedU The control input.
   * @param dt       Timestep for model update.
   */
  StateVector CalculateX(const StateVector& x, const InputVector& clampedU,
                         units::second_t dt) const {
    Matrixd<States, States> discA;
    Matrixd<States, Inputs> discB;
    DiscretizeAB<States, Inputs>(m_A, m_B, dt, &discA, &discB);

    return discA * x + discB * clampedU;
  }

  /**
   * Computes the new y given the control input.
   *
   * This is used by state observers directly to run updates based on state
   * estimate.
   *
   * @param x The current state.
   * @param clampedU The control input.
   */
  OutputVector CalculateY(const StateVector& x,
                          const InputVector& clampedU) const {
    return m_C * x + m_D * clampedU;
  }

 private:
  /**
   * Continuous system matrix.
   */
  Matrixd<States, States> m_A;

  /**
   * Continuous input matrix.
   */
  Matrixd<States, Inputs> m_B;

  /**
   * Output matrix.
   */
  Matrixd<Outputs, States> m_C;

  /**
   * Feedthrough matrix.
   */
  Matrixd<Outputs, Inputs> m_D;
};

}  // namespace frc
