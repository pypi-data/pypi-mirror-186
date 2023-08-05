
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <networktables/FloatTopic.h>




#include <rpygen/nt__Publisher.hpp>

namespace rpygen {

using namespace nt;


template <typename CfgBase>
using PyTrampolineCfgBase_nt__FloatPublisher =
    PyTrampolineCfg_nt__Publisher<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_nt__FloatPublisher :
    PyTrampolineCfgBase_nt__FloatPublisher< CfgBase>
{
    using Base = nt::FloatPublisher;

};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_nt__FloatPublisher =
    PyTrampoline_nt__Publisher<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_nt__FloatPublisher : PyTrampolineBase_nt__FloatPublisher<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_nt__FloatPublisher<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_nt__FloatPublisher;

    using TopicType [[maybe_unused]] = typename nt::FloatPublisher::TopicType;
    using ValueType [[maybe_unused]] = typename nt::FloatPublisher::ValueType;
    using ParamType [[maybe_unused]] = typename nt::FloatPublisher::ParamType;
    using TimestampedValueType [[maybe_unused]] = typename nt::FloatPublisher::TimestampedValueType;





};

}; // namespace rpygen
