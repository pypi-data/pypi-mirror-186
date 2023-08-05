
 

// This file is autogenerated. DO NOT EDIT

#pragma once
#include <robotpy_build.h>


#include <networktables/GenericEntry.h>




#include <rpygen/nt__Publisher.hpp>

namespace rpygen {

using namespace nt;


template <typename CfgBase>
using PyTrampolineCfgBase_nt__GenericPublisher =
    PyTrampolineCfg_nt__Publisher<
CfgBase
>;

template <typename CfgBase = EmptyTrampolineCfg>
struct PyTrampolineCfg_nt__GenericPublisher :
    PyTrampolineCfgBase_nt__GenericPublisher< CfgBase>
{
    using Base = nt::GenericPublisher;

};


template <typename PyTrampolineBase, typename PyTrampolineCfg>
using PyTrampolineBase_nt__GenericPublisher =
    PyTrampoline_nt__Publisher<
        PyTrampolineBase
        
        , PyTrampolineCfg
    >
;

template <typename PyTrampolineBase, typename PyTrampolineCfg>
struct PyTrampoline_nt__GenericPublisher : PyTrampolineBase_nt__GenericPublisher<PyTrampolineBase, PyTrampolineCfg> {
    using PyTrampolineBase_nt__GenericPublisher<PyTrampolineBase, PyTrampolineCfg>::PyTrampolineBase_nt__GenericPublisher;

    using TopicType [[maybe_unused]] = typename nt::GenericPublisher::TopicType;
    using ValueType [[maybe_unused]] = typename nt::GenericPublisher::ValueType;
    using ParamType [[maybe_unused]] = typename nt::GenericPublisher::ParamType;
    using TimestampedValueType [[maybe_unused]] = typename nt::GenericPublisher::TimestampedValueType;





};

}; // namespace rpygen
