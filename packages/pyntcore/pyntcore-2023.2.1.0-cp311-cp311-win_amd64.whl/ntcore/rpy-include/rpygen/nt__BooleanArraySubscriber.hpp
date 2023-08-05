
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <networktables\BooleanArrayTopic.h>




#include <rpygen/nt__Subscriber.hpp>

namespace rpygen {

using namespace nt;


template <typename CfgBase>
using PyTrampolineCfgBase_nt__BooleanArraySubscriber =
    PyTrampolineCfg_nt__Subscriber<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_nt__BooleanArraySubscriber :
    PyTrampolineCfgBase_nt__BooleanArraySubscriber< CfgBase>
{
    using Base = nt::BooleanArraySubscriber;

};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_nt__BooleanArraySubscriber =
    PyTrampoline_nt__Subscriber<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_nt__BooleanArraySubscriber : PyTrampolineBase_nt__BooleanArraySubscriber<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_nt__BooleanArraySubscriber<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_nt__BooleanArraySubscriber;

    using TopicType [[maybe_unused]] = typename nt::BooleanArraySubscriber::TopicType;
    using ValueType [[maybe_unused]] = typename nt::BooleanArraySubscriber::ValueType;
    using ParamType [[maybe_unused]] = typename nt::BooleanArraySubscriber::ParamType;
    using TimestampedValueType [[maybe_unused]] = typename nt::BooleanArraySubscriber::TimestampedValueType;
    using SmallRetType [[maybe_unused]] = typename nt::BooleanArraySubscriber::SmallRetType;
    using SmallElemType [[maybe_unused]] = typename nt::BooleanArraySubscriber::SmallElemType;
    using TimestampedValueViewType [[maybe_unused]] = typename nt::BooleanArraySubscriber::TimestampedValueViewType;





};

}; // namespace rpygen
