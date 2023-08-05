
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <networktables\StringTopic.h>




#include <rpygen/nt__Subscriber.hpp>

namespace rpygen {

using namespace nt;


template <typename CfgBase>
using PyTrampolineCfgBase_nt__StringSubscriber =
    PyTrampolineCfg_nt__Subscriber<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_nt__StringSubscriber :
    PyTrampolineCfgBase_nt__StringSubscriber< CfgBase>
{
    using Base = nt::StringSubscriber;

};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_nt__StringSubscriber =
    PyTrampoline_nt__Subscriber<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_nt__StringSubscriber : PyTrampolineBase_nt__StringSubscriber<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_nt__StringSubscriber<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_nt__StringSubscriber;

    using TopicType [[maybe_unused]] = typename nt::StringSubscriber::TopicType;
    using ValueType [[maybe_unused]] = typename nt::StringSubscriber::ValueType;
    using ParamType [[maybe_unused]] = typename nt::StringSubscriber::ParamType;
    using TimestampedValueType [[maybe_unused]] = typename nt::StringSubscriber::TimestampedValueType;
    using SmallRetType [[maybe_unused]] = typename nt::StringSubscriber::SmallRetType;
    using SmallElemType [[maybe_unused]] = typename nt::StringSubscriber::SmallElemType;
    using TimestampedValueViewType [[maybe_unused]] = typename nt::StringSubscriber::TimestampedValueViewType;





};

}; // namespace rpygen
