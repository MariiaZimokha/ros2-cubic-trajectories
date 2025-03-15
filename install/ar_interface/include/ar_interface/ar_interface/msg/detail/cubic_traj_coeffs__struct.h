// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ar_interface:msg/CubicTrajCoeffs.idl
// generated code does not contain a copyright notice

#ifndef AR_INTERFACE__MSG__DETAIL__CUBIC_TRAJ_COEFFS__STRUCT_H_
#define AR_INTERFACE__MSG__DETAIL__CUBIC_TRAJ_COEFFS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/CubicTrajCoeffs in the package ar_interface.
typedef struct ar_interface__msg__CubicTrajCoeffs
{
  double a0;
  double a1;
  double a2;
  double a3;
  double t0;
  double tf;
} ar_interface__msg__CubicTrajCoeffs;

// Struct for a sequence of ar_interface__msg__CubicTrajCoeffs.
typedef struct ar_interface__msg__CubicTrajCoeffs__Sequence
{
  ar_interface__msg__CubicTrajCoeffs * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ar_interface__msg__CubicTrajCoeffs__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AR_INTERFACE__MSG__DETAIL__CUBIC_TRAJ_COEFFS__STRUCT_H_
