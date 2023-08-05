
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <networktables\IntegerTopic.h>




#include <rpygen/nt__Publisher.hpp>

namespace rpygen {

using namespace nt;


template <typename CfgBase>
using PyTrampolineCfgBase_nt__IntegerPublisher =
    PyTrampolineCfg_nt__Publisher<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_nt__IntegerPublisher :
    PyTrampolineCfgBase_nt__IntegerPublisher< CfgBase>
{
    using Base = nt::IntegerPublisher;

};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_nt__IntegerPublisher =
    PyTrampoline_nt__Publisher<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_nt__IntegerPublisher : PyTrampolineBase_nt__IntegerPublisher<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_nt__IntegerPublisher<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_nt__IntegerPublisher;

    using TopicType [[maybe_unused]] = typename nt::IntegerPublisher::TopicType;
    using ValueType [[maybe_unused]] = typename nt::IntegerPublisher::ValueType;
    using ParamType [[maybe_unused]] = typename nt::IntegerPublisher::ParamType;
    using TimestampedValueType [[maybe_unused]] = typename nt::IntegerPublisher::TimestampedValueType;





};

}; // namespace rpygen
