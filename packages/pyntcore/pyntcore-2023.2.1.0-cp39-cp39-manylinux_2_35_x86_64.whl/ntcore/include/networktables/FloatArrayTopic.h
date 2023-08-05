// Copyright (c) FIRST and other WPILib contributors.
// Open Source Software; you can modify and/or share it under the terms of
// the WPILib BSD license file in the root directory of this project.

#pragma once

#include <stdint.h>

#include <utility>
#include <span>
#include <string_view>
#include <vector>

#include "networktables/Topic.h"

namespace wpi {
template <typename T>
class SmallVectorImpl;
class json;
}  // namespace wpi

namespace nt {

class FloatArrayTopic;

/**
 * NetworkTables FloatArray subscriber.
 */
class FloatArraySubscriber : public Subscriber {
 public:
  using TopicType = FloatArrayTopic;
  using ValueType = std::vector<float>;
  using ParamType = std::span<const float>;
  using TimestampedValueType = TimestampedFloatArray;

  using SmallRetType = std::span<float>;
  using SmallElemType = float;
  using TimestampedValueViewType = TimestampedFloatArrayView;


  FloatArraySubscriber() = default;

  /**
   * Construct from a subscriber handle; recommended to use
   * FloatArrayTopic::Subscribe() instead.
   *
   * @param handle Native handle
   * @param defaultValue Default value
   */
  FloatArraySubscriber(NT_Subscriber handle, ParamType defaultValue);

  /**
   * Get the last published value.
   * If no value has been published, returns the stored default value.
   *
   * @return value
   */
  ValueType Get() const;

  /**
   * Get the last published value.
   * If no value has been published, returns the passed defaultValue.
   *
   * @param defaultValue default value to return if no value has been published
   * @return value
   */
  ValueType Get(ParamType defaultValue) const;

  /**
   * Get the last published value.
   * If no value has been published, returns the stored default value.
   *
   * @param buf storage for returned value
   * @return value
   */
  SmallRetType Get(wpi::SmallVectorImpl<SmallElemType>& buf) const;

  /**
   * Get the last published value.
   * If no value has been published, returns the passed defaultValue.
   *
   * @param buf storage for returned value
   * @param defaultValue default value to return if no value has been published
   * @return value
   */
  SmallRetType Get(wpi::SmallVectorImpl<SmallElemType>& buf, ParamType defaultValue) const;

  /**
   * Get the last published value along with its timestamp
   * If no value has been published, returns the stored default value and a
   * timestamp of 0.
   *
   * @return timestamped value
   */
  TimestampedValueType GetAtomic() const;

  /**
   * Get the last published value along with its timestamp.
   * If no value has been published, returns the passed defaultValue and a
   * timestamp of 0.
   *
   * @param defaultValue default value to return if no value has been published
   * @return timestamped value
   */
  TimestampedValueType GetAtomic(ParamType defaultValue) const;

  /**
   * Get the last published value along with its timestamp.
   * If no value has been published, returns the stored default value and a
   * timestamp of 0.
   *
   * @param buf storage for returned value
   * @return timestamped value
   */
  TimestampedValueViewType GetAtomic(
      wpi::SmallVectorImpl<SmallElemType>& buf) const;

  /**
   * Get the last published value along with its timestamp.
   * If no value has been published, returns the passed defaultValue and a
   * timestamp of 0.
   *
   * @param buf storage for returned value
   * @param defaultValue default value to return if no value has been published
   * @return timestamped value
   */
  TimestampedValueViewType GetAtomic(
      wpi::SmallVectorImpl<SmallElemType>& buf,
      ParamType defaultValue) const;

  /**
   * Get an array of all value changes since the last call to ReadQueue.
   * Also provides a timestamp for each value.
   *
   * @note The "poll storage" subscribe option can be used to set the queue
   *     depth.
   *
   * @return Array of timestamped values; empty array if no new changes have
   *     been published since the previous call.
   */
  std::vector<TimestampedValueType> ReadQueue();

  /**
   * Get the corresponding topic.
   *
   * @return Topic
   */
  TopicType GetTopic() const;

 private:
  ValueType m_defaultValue;
};

/**
 * NetworkTables FloatArray publisher.
 */
class FloatArrayPublisher : public Publisher {
 public:
  using TopicType = FloatArrayTopic;
  using ValueType = std::vector<float>;
  using ParamType = std::span<const float>;

  using SmallRetType = std::span<float>;
  using SmallElemType = float;

  using TimestampedValueType = TimestampedFloatArray;

  FloatArrayPublisher() = default;

  /**
   * Construct from a publisher handle; recommended to use
   * FloatArrayTopic::Publish() instead.
   *
   * @param handle Native handle
   */
  explicit FloatArrayPublisher(NT_Publisher handle);

  /**
   * Publish a new value.
   *
   * @param value value to publish
   * @param time timestamp; 0 indicates current NT time should be used
   */
  void Set(ParamType value, int64_t time = 0);

  /**
   * Publish a default value.
   * On reconnect, a default value will never be used in preference to a
   * published value.
   *
   * @param value value
   */
  void SetDefault(ParamType value);

  /**
   * Get the corresponding topic.
   *
   * @return Topic
   */
  TopicType GetTopic() const;
};

/**
 * NetworkTables FloatArray entry.
 *
 * @note Unlike NetworkTableEntry, the entry goes away when this is destroyed.
 */
class FloatArrayEntry final : public FloatArraySubscriber,
                                  public FloatArrayPublisher {
 public:
  using SubscriberType = FloatArraySubscriber;
  using PublisherType = FloatArrayPublisher;
  using TopicType = FloatArrayTopic;
  using ValueType = std::vector<float>;
  using ParamType = std::span<const float>;

  using SmallRetType = std::span<float>;
  using SmallElemType = float;

  using TimestampedValueType = TimestampedFloatArray;

  FloatArrayEntry() = default;

  /**
   * Construct from an entry handle; recommended to use
   * FloatArrayTopic::GetEntry() instead.
   *
   * @param handle Native handle
   * @param defaultValue Default value
   */
  FloatArrayEntry(NT_Entry handle, ParamType defaultValue);

  /**
   * Determines if the native handle is valid.
   *
   * @return True if the native handle is valid, false otherwise.
   */
  explicit operator bool() const { return m_subHandle != 0; }

  /**
   * Gets the native handle for the entry.
   *
   * @return Native handle
   */
  NT_Entry GetHandle() const { return m_subHandle; }

  /**
   * Get the corresponding topic.
   *
   * @return Topic
   */
  TopicType GetTopic() const;

  /**
   * Stops publishing the entry if it's published.
   */
  void Unpublish();
};

/**
 * NetworkTables FloatArray topic.
 */
class FloatArrayTopic final : public Topic {
 public:
  using SubscriberType = FloatArraySubscriber;
  using PublisherType = FloatArrayPublisher;
  using EntryType = FloatArrayEntry;
  using ValueType = std::vector<float>;
  using ParamType = std::span<const float>;
  using TimestampedValueType = TimestampedFloatArray;
  /** The default type string for this topic type. */
  static constexpr std::string_view kTypeString = "float[]";

  FloatArrayTopic() = default;

  /**
   * Construct from a topic handle; recommended to use
   * NetworkTableInstance::GetFloatArrayTopic() instead.
   *
   * @param handle Native handle
   */
  explicit FloatArrayTopic(NT_Topic handle) : Topic{handle} {}

  /**
   * Construct from a generic topic.
   *
   * @param topic Topic
   */
  explicit FloatArrayTopic(Topic topic) : Topic{topic} {}

  /**
   * Create a new subscriber to the topic.
   *
   * <p>The subscriber is only active as long as the returned object
   * is not destroyed.
   *
   * @note Subscribers that do not match the published data type do not return
   *     any values. To determine if the data type matches, use the appropriate
   *     Topic functions.
   *
   * @param defaultValue default value used when a default is not provided to a
   *        getter function
   * @param options subscribe options
   * @return subscriber
   */
  [[nodiscard]]
  SubscriberType Subscribe(
      ParamType defaultValue,
      const PubSubOptions& options = kDefaultPubSubOptions);
  /**
   * Create a new subscriber to the topic, with specific type string.
   *
   * <p>The subscriber is only active as long as the returned object
   * is not destroyed.
   *
   * @note Subscribers that do not match the published data type do not return
   *     any values. To determine if the data type matches, use the appropriate
   *     Topic functions.
   *
   * @param typeString type string
   * @param defaultValue default value used when a default is not provided to a
   *        getter function
   * @param options subscribe options
   * @return subscriber
   */
  [[nodiscard]]
  SubscriberType SubscribeEx(
      std::string_view typeString, ParamType defaultValue,
      const PubSubOptions& options = kDefaultPubSubOptions);

  /**
   * Create a new publisher to the topic.
   *
   * The publisher is only active as long as the returned object
   * is not destroyed.
   *
   * @note It is not possible to publish two different data types to the same
   *     topic. Conflicts between publishers are typically resolved by the
   *     server on a first-come, first-served basis. Any published values that
   *     do not match the topic's data type are dropped (ignored). To determine
   *     if the data type matches, use the appropriate Topic functions.
   *
   * @param options publish options
   * @return publisher
   */
  [[nodiscard]]
  PublisherType Publish(const PubSubOptions& options = kDefaultPubSubOptions);

  /**
   * Create a new publisher to the topic, with type string and initial
   * properties.
   *
   * The publisher is only active as long as the returned object
   * is not destroyed.
   *
   * @note It is not possible to publish two different data types to the same
   *     topic. Conflicts between publishers are typically resolved by the
   *     server on a first-come, first-served basis. Any published values that
   *     do not match the topic's data type are dropped (ignored). To determine
   *     if the data type matches, use the appropriate Topic functions.
   *
   * @param typeString type string
   * @param properties JSON properties
   * @param options publish options
   * @return publisher
   */
  [[nodiscard]]
  PublisherType PublishEx(std::string_view typeString,
    const wpi::json& properties, const PubSubOptions& options = kDefaultPubSubOptions);

  /**
   * Create a new entry for the topic.
   *
   * Entries act as a combination of a subscriber and a weak publisher. The
   * subscriber is active as long as the entry is not destroyed. The publisher
   * is created when the entry is first written to, and remains active until
   * either Unpublish() is called or the entry is destroyed.
   *
   * @note It is not possible to use two different data types with the same
   *     topic. Conflicts between publishers are typically resolved by the
   *     server on a first-come, first-served basis. Any published values that
   *     do not match the topic's data type are dropped (ignored), and the entry
   *     will show no new values if the data type does not match. To determine
   *     if the data type matches, use the appropriate Topic functions.
   *
   * @param defaultValue default value used when a default is not provided to a
   *        getter function
   * @param options publish and/or subscribe options
   * @return entry
   */
  [[nodiscard]]
  EntryType GetEntry(ParamType defaultValue,
                     const PubSubOptions& options = kDefaultPubSubOptions);
  /**
   * Create a new entry for the topic, with specific type string.
   *
   * Entries act as a combination of a subscriber and a weak publisher. The
   * subscriber is active as long as the entry is not destroyed. The publisher
   * is created when the entry is first written to, and remains active until
   * either Unpublish() is called or the entry is destroyed.
   *
   * @note It is not possible to use two different data types with the same
   *     topic. Conflicts between publishers are typically resolved by the
   *     server on a first-come, first-served basis. Any published values that
   *     do not match the topic's data type are dropped (ignored), and the entry
   *     will show no new values if the data type does not match. To determine
   *     if the data type matches, use the appropriate Topic functions.
   *
   * @param typeString type string
   * @param defaultValue default value used when a default is not provided to a
   *        getter function
   * @param options publish and/or subscribe options
   * @return entry
   */
  [[nodiscard]]
  EntryType GetEntryEx(std::string_view typeString, ParamType defaultValue,
                       const PubSubOptions& options = kDefaultPubSubOptions);

};

}  // namespace nt

#include "networktables/FloatArrayTopic.inc"
