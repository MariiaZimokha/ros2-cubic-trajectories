// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from ar_interface:srv/ComputeCubicTraj.idl
// generated code does not contain a copyright notice

#ifndef AR_INTERFACE__SRV__DETAIL__COMPUTE_CUBIC_TRAJ__STRUCT_H_
#define AR_INTERFACE__SRV__DETAIL__COMPUTE_CUBIC_TRAJ__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/ComputeCubicTraj in the package ar_interface.
typedef struct ar_interface__srv__ComputeCubicTraj_Request
{
  double p0;
  double pf;
  double v0;
  double vf;
  double t0;
  double tf;
} ar_interface__srv__ComputeCubicTraj_Request;

// Struct for a sequence of ar_interface__srv__ComputeCubicTraj_Request.
typedef struct ar_interface__srv__ComputeCubicTraj_Request__Sequence
{
  ar_interface__srv__ComputeCubicTraj_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ar_interface__srv__ComputeCubicTraj_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/ComputeCubicTraj in the package ar_interface.
typedef struct ar_interface__srv__ComputeCubicTraj_Response
{
  double a0;
  double a1;
  double a2;
  double a3;
} ar_interface__srv__ComputeCubicTraj_Response;

// Struct for a sequence of ar_interface__srv__ComputeCubicTraj_Response.
typedef struct ar_interface__srv__ComputeCubicTraj_Response__Sequence
{
  ar_interface__srv__ComputeCubicTraj_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} ar_interface__srv__ComputeCubicTraj_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AR_INTERFACE__SRV__DETAIL__COMPUTE_CUBIC_TRAJ__STRUCT_H_
