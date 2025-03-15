// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ar_interface:msg/CubicTrajParams.idl
// generated code does not contain a copyright notice

#ifndef AR_INTERFACE__MSG__DETAIL__CUBIC_TRAJ_PARAMS__STRUCT_H_
#define AR_INTERFACE__MSG__DETAIL__CUBIC_TRAJ_PARAMS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/CubicTrajParams in the package ar_interface.
typedef struct ar_interface__msg__CubicTrajParams
{
  double p0;
  double pf;
  double v0;
  double vf;
  double t0;
  double tf;
} ar_interface__msg__CubicTrajParams;

// Struct for a sequence of ar_interface__msg__CubicTrajParams.
typedef struct ar_interface__msg__CubicTrajParams__Sequence
{
  ar_interface__msg__CubicTrajParams * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ar_interface__msg__CubicTrajParams__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AR_INTERFACE__MSG__DETAIL__CUBIC_TRAJ_PARAMS__STRUCT_H_
