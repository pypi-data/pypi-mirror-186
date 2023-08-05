// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#pragma once

#include <stdint.h>

#include "ntcore_c.h"

#ifdef __cplusplus
extern "C" {
#endif


/**
 * Timestamped Boolean.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedBoolean {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  NT_Bool value;
};

/**
 * @defgroup ntcore_Boolean_cfunc Boolean Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 */
NT_Bool NT_SetBoolean(NT_Handle pubentry, int64_t time, NT_Bool value);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 */
NT_Bool NT_SetDefaultBoolean(NT_Handle pubentry, NT_Bool defaultValue);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @return value
 */
NT_Bool NT_GetBoolean(NT_Handle subentry, NT_Bool defaultValue);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param value timestamped value (output)
 */
void NT_GetAtomicBoolean(NT_Handle subentry, NT_Bool defaultValue, struct NT_TimestampedBoolean* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicBoolean).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedBoolean(struct NT_TimestampedBoolean* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedBoolean* NT_ReadQueueBoolean(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueBoolean).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueBoolean(struct NT_TimestampedBoolean* arr, size_t len);
/**
 * Get an array of all value changes since the last call to ReadQueue.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of values; NULL if no new changes have
 *     been published since the previous call.
 */
NT_Bool* NT_ReadQueueValuesBoolean(NT_Handle subentry, size_t* len);

/** @} */

/**
 * Timestamped Integer.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedInteger {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  int64_t value;
};

/**
 * @defgroup ntcore_Integer_cfunc Integer Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 */
NT_Bool NT_SetInteger(NT_Handle pubentry, int64_t time, int64_t value);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 */
NT_Bool NT_SetDefaultInteger(NT_Handle pubentry, int64_t defaultValue);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @return value
 */
int64_t NT_GetInteger(NT_Handle subentry, int64_t defaultValue);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param value timestamped value (output)
 */
void NT_GetAtomicInteger(NT_Handle subentry, int64_t defaultValue, struct NT_TimestampedInteger* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicInteger).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedInteger(struct NT_TimestampedInteger* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedInteger* NT_ReadQueueInteger(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueInteger).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueInteger(struct NT_TimestampedInteger* arr, size_t len);
/**
 * Get an array of all value changes since the last call to ReadQueue.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of values; NULL if no new changes have
 *     been published since the previous call.
 */
int64_t* NT_ReadQueueValuesInteger(NT_Handle subentry, size_t* len);

/** @} */

/**
 * Timestamped Float.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedFloat {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  float value;
};

/**
 * @defgroup ntcore_Float_cfunc Float Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 */
NT_Bool NT_SetFloat(NT_Handle pubentry, int64_t time, float value);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 */
NT_Bool NT_SetDefaultFloat(NT_Handle pubentry, float defaultValue);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @return value
 */
float NT_GetFloat(NT_Handle subentry, float defaultValue);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param value timestamped value (output)
 */
void NT_GetAtomicFloat(NT_Handle subentry, float defaultValue, struct NT_TimestampedFloat* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicFloat).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedFloat(struct NT_TimestampedFloat* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedFloat* NT_ReadQueueFloat(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueFloat).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueFloat(struct NT_TimestampedFloat* arr, size_t len);
/**
 * Get an array of all value changes since the last call to ReadQueue.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of values; NULL if no new changes have
 *     been published since the previous call.
 */
float* NT_ReadQueueValuesFloat(NT_Handle subentry, size_t* len);

/** @} */

/**
 * Timestamped Double.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedDouble {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  double value;
};

/**
 * @defgroup ntcore_Double_cfunc Double Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 */
NT_Bool NT_SetDouble(NT_Handle pubentry, int64_t time, double value);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 */
NT_Bool NT_SetDefaultDouble(NT_Handle pubentry, double defaultValue);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @return value
 */
double NT_GetDouble(NT_Handle subentry, double defaultValue);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param value timestamped value (output)
 */
void NT_GetAtomicDouble(NT_Handle subentry, double defaultValue, struct NT_TimestampedDouble* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicDouble).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedDouble(struct NT_TimestampedDouble* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedDouble* NT_ReadQueueDouble(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueDouble).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueDouble(struct NT_TimestampedDouble* arr, size_t len);
/**
 * Get an array of all value changes since the last call to ReadQueue.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of values; NULL if no new changes have
 *     been published since the previous call.
 */
double* NT_ReadQueueValuesDouble(NT_Handle subentry, size_t* len);

/** @} */

/**
 * Timestamped String.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedString {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  char* value;
  /**
   * Value length.
   */
  size_t len;

};

/**
 * @defgroup ntcore_String_cfunc String Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 * @param len length of value

 */
NT_Bool NT_SetString(NT_Handle pubentry, int64_t time, const char* value, size_t len);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 * @param defaultValueLen length of default value

 */
NT_Bool NT_SetDefaultString(NT_Handle pubentry, const char* defaultValue, size_t defaultValueLen);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value
 * @param len length of returned value (output)

 * @return value
 */
char* NT_GetString(NT_Handle subentry, const char* defaultValue, size_t defaultValueLen, size_t* len);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value

 * @param value timestamped value (output)
 */
void NT_GetAtomicString(NT_Handle subentry, const char* defaultValue, size_t defaultValueLen, struct NT_TimestampedString* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicString).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedString(struct NT_TimestampedString* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedString* NT_ReadQueueString(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueString).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueString(struct NT_TimestampedString* arr, size_t len);

/** @} */

/**
 * Timestamped Raw.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedRaw {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  uint8_t* value;
  /**
   * Value length.
   */
  size_t len;

};

/**
 * @defgroup ntcore_Raw_cfunc Raw Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 * @param len length of value

 */
NT_Bool NT_SetRaw(NT_Handle pubentry, int64_t time, const uint8_t* value, size_t len);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 * @param defaultValueLen length of default value

 */
NT_Bool NT_SetDefaultRaw(NT_Handle pubentry, const uint8_t* defaultValue, size_t defaultValueLen);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value
 * @param len length of returned value (output)

 * @return value
 */
uint8_t* NT_GetRaw(NT_Handle subentry, const uint8_t* defaultValue, size_t defaultValueLen, size_t* len);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value

 * @param value timestamped value (output)
 */
void NT_GetAtomicRaw(NT_Handle subentry, const uint8_t* defaultValue, size_t defaultValueLen, struct NT_TimestampedRaw* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicRaw).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedRaw(struct NT_TimestampedRaw* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedRaw* NT_ReadQueueRaw(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueRaw).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueRaw(struct NT_TimestampedRaw* arr, size_t len);

/** @} */

/**
 * Timestamped BooleanArray.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedBooleanArray {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  NT_Bool* value;
  /**
   * Value length.
   */
  size_t len;

};

/**
 * @defgroup ntcore_BooleanArray_cfunc BooleanArray Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 * @param len length of value

 */
NT_Bool NT_SetBooleanArray(NT_Handle pubentry, int64_t time, const NT_Bool* value, size_t len);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 * @param defaultValueLen length of default value

 */
NT_Bool NT_SetDefaultBooleanArray(NT_Handle pubentry, const NT_Bool* defaultValue, size_t defaultValueLen);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value
 * @param len length of returned value (output)

 * @return value
 */
NT_Bool* NT_GetBooleanArray(NT_Handle subentry, const NT_Bool* defaultValue, size_t defaultValueLen, size_t* len);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value

 * @param value timestamped value (output)
 */
void NT_GetAtomicBooleanArray(NT_Handle subentry, const NT_Bool* defaultValue, size_t defaultValueLen, struct NT_TimestampedBooleanArray* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicBooleanArray).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedBooleanArray(struct NT_TimestampedBooleanArray* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedBooleanArray* NT_ReadQueueBooleanArray(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueBooleanArray).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueBooleanArray(struct NT_TimestampedBooleanArray* arr, size_t len);

/** @} */

/**
 * Timestamped IntegerArray.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedIntegerArray {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  int64_t* value;
  /**
   * Value length.
   */
  size_t len;

};

/**
 * @defgroup ntcore_IntegerArray_cfunc IntegerArray Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 * @param len length of value

 */
NT_Bool NT_SetIntegerArray(NT_Handle pubentry, int64_t time, const int64_t* value, size_t len);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 * @param defaultValueLen length of default value

 */
NT_Bool NT_SetDefaultIntegerArray(NT_Handle pubentry, const int64_t* defaultValue, size_t defaultValueLen);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value
 * @param len length of returned value (output)

 * @return value
 */
int64_t* NT_GetIntegerArray(NT_Handle subentry, const int64_t* defaultValue, size_t defaultValueLen, size_t* len);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value

 * @param value timestamped value (output)
 */
void NT_GetAtomicIntegerArray(NT_Handle subentry, const int64_t* defaultValue, size_t defaultValueLen, struct NT_TimestampedIntegerArray* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicIntegerArray).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedIntegerArray(struct NT_TimestampedIntegerArray* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedIntegerArray* NT_ReadQueueIntegerArray(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueIntegerArray).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueIntegerArray(struct NT_TimestampedIntegerArray* arr, size_t len);

/** @} */

/**
 * Timestamped FloatArray.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedFloatArray {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  float* value;
  /**
   * Value length.
   */
  size_t len;

};

/**
 * @defgroup ntcore_FloatArray_cfunc FloatArray Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 * @param len length of value

 */
NT_Bool NT_SetFloatArray(NT_Handle pubentry, int64_t time, const float* value, size_t len);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 * @param defaultValueLen length of default value

 */
NT_Bool NT_SetDefaultFloatArray(NT_Handle pubentry, const float* defaultValue, size_t defaultValueLen);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value
 * @param len length of returned value (output)

 * @return value
 */
float* NT_GetFloatArray(NT_Handle subentry, const float* defaultValue, size_t defaultValueLen, size_t* len);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value

 * @param value timestamped value (output)
 */
void NT_GetAtomicFloatArray(NT_Handle subentry, const float* defaultValue, size_t defaultValueLen, struct NT_TimestampedFloatArray* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicFloatArray).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedFloatArray(struct NT_TimestampedFloatArray* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedFloatArray* NT_ReadQueueFloatArray(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueFloatArray).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueFloatArray(struct NT_TimestampedFloatArray* arr, size_t len);

/** @} */

/**
 * Timestamped DoubleArray.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedDoubleArray {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  double* value;
  /**
   * Value length.
   */
  size_t len;

};

/**
 * @defgroup ntcore_DoubleArray_cfunc DoubleArray Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 * @param len length of value

 */
NT_Bool NT_SetDoubleArray(NT_Handle pubentry, int64_t time, const double* value, size_t len);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 * @param defaultValueLen length of default value

 */
NT_Bool NT_SetDefaultDoubleArray(NT_Handle pubentry, const double* defaultValue, size_t defaultValueLen);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value
 * @param len length of returned value (output)

 * @return value
 */
double* NT_GetDoubleArray(NT_Handle subentry, const double* defaultValue, size_t defaultValueLen, size_t* len);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value

 * @param value timestamped value (output)
 */
void NT_GetAtomicDoubleArray(NT_Handle subentry, const double* defaultValue, size_t defaultValueLen, struct NT_TimestampedDoubleArray* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicDoubleArray).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedDoubleArray(struct NT_TimestampedDoubleArray* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedDoubleArray* NT_ReadQueueDoubleArray(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueDoubleArray).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueDoubleArray(struct NT_TimestampedDoubleArray* arr, size_t len);

/** @} */

/**
 * Timestamped StringArray.
 * @ingroup ntcore_c_handle_api
 */
struct NT_TimestampedStringArray {
  /**
   * Time in local time base.
   */
  int64_t time;

  /**
   * Time in server time base.  May be 0 or 1 for locally set values.
   */
  int64_t serverTime;

  /**
   * Value.
   */
  struct NT_String* value;
  /**
   * Value length.
   */
  size_t len;

};

/**
 * @defgroup ntcore_StringArray_cfunc StringArray Functions
 * @ingroup ntcore_c_handle_api
 * @{
 */

/**
 * Publish a new value.
 *
 * @param pubentry publisher or entry handle
 * @param time timestamp; 0 indicates current NT time should be used
 * @param value value to publish
 * @param len length of value

 */
NT_Bool NT_SetStringArray(NT_Handle pubentry, int64_t time, const struct NT_String* value, size_t len);

/**
 * Publish a default value.
 * On reconnect, a default value will never be used in preference to a
 * published value.
 *
 * @param pubentry publisher or entry handle
 * @param defaultValue default value
 * @param defaultValueLen length of default value

 */
NT_Bool NT_SetDefaultStringArray(NT_Handle pubentry, const struct NT_String* defaultValue, size_t defaultValueLen);

/**
 * Get the last published value.
 * If no value has been published, returns the passed defaultValue.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value
 * @param len length of returned value (output)

 * @return value
 */
struct NT_String* NT_GetStringArray(NT_Handle subentry, const struct NT_String* defaultValue, size_t defaultValueLen, size_t* len);

/**
 * Get the last published value along with its timestamp.
 * If no value has been published, returns the passed defaultValue and a
 * timestamp of 0.
 *
 * @param subentry subscriber or entry handle
 * @param defaultValue default value to return if no value has been published
 * @param defaultValueLen length of default value

 * @param value timestamped value (output)
 */
void NT_GetAtomicStringArray(NT_Handle subentry, const struct NT_String* defaultValue, size_t defaultValueLen, struct NT_TimestampedStringArray* value);

/**
 * Disposes a timestamped value (as returned by NT_GetAtomicStringArray).
 *
 * @param value timestamped value
 */
void NT_DisposeTimestampedStringArray(struct NT_TimestampedStringArray* value);

/**
 * Get an array of all value changes since the last call to ReadQueue.
 * Also provides a timestamp for each value.
 *
 * @note The "poll storage" subscribe option can be used to set the queue
 *     depth.
 *
 * @param subentry subscriber or entry handle
 * @param len length of returned array (output)
 * @return Array of timestamped values; NULL if no new changes have
 *     been published since the previous call.
 */
struct NT_TimestampedStringArray* NT_ReadQueueStringArray(NT_Handle subentry, size_t* len);

/**
 * Frees a timestamped array of values (as returned by NT_ReadQueueStringArray).
 *
 * @param arr array
 * @param len length of array
 */
void NT_FreeQueueStringArray(struct NT_TimestampedStringArray* arr, size_t len);

/** @} */


#ifdef __cplusplus
}  // extern "C"
#endif
