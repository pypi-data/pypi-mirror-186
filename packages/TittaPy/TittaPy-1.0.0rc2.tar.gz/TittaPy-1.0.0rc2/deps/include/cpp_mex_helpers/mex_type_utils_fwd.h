#pragma once
#include <string>

#include <vector>
#include <array>

#include <variant>
#include <optional>
#include <memory>

#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>

#include <utility>
#include <tuple>
#include <concepts>


#include "include_matlab.h"
#include "is_container_trait.h"
#include "is_specialization_trait.h"


namespace mxTypes {
    //// functionality to convert C++ types to MATLAB ClassIDs and back
    template <typename T>
    struct typeToMxClass;

    template <typename T>
    struct typeNeedsMxCellStorage;

    template <typename T>
    struct typeDumpVectorOneAtATime;

    template <mxClassID T>
    constexpr mxClassID MxClassToType();

    template <mxClassID T>
    constexpr const char* mxClassToString();

    //// converters of generic data types to MATLAB variables
    //// to simple variables
    mxArray* ToMatlab(std::string str_);

    template<class T>
    requires std::is_arithmetic_v<T>
    mxArray* ToMatlab(T val_);

    template<class Cont, typename... Extras>
    requires Container<Cont>
    mxArray* ToMatlab(Cont data_, Extras&& ...extras_);
    template <class... Types>  mxArray* ToMatlab(std::variant<Types...> val_);
    template <class T>         mxArray* ToMatlab(std::optional<T> val_);
    template <class T>         mxArray* ToMatlab(std::shared_ptr<T> val_);

    // associative containers
    // associative key-value container with unique string keys -> matlab struct
    // NB: all other key-value containers are handled by Cont<std::pair> handler
    // below
    template <template <class...> class Cont, class... Args>
    requires
        (
            is_specialization_v<Cont<Args...>, std::map> ||
            is_specialization_v<Cont<Args...>, std::unordered_map>
            )
        &&
            std::is_convertible_v<typename Cont<Args...>::key_type, std::string>
    mxArray* ToMatlab(Cont<Args...> data_);
    // sets
    template <template <class...> class Cont, class... Args>
    requires
        is_specialization_v<Cont<Args...>, std::set> ||
        is_specialization_v<Cont<Args...>, std::unordered_set> ||
        is_specialization_v<Cont<Args...>, std::multiset> ||
        is_specialization_v<Cont<Args...>, std::unordered_multiset>
    mxArray* ToMatlab(Cont<Args...> data_);

    // std::tuple or std::pair
    // 1. simple std::tuple or std::pair
    template <template <class...> class T, class... Args>
    requires
        is_specialization_v<T<Args...>, std::pair> ||
        is_specialization_v<T<Args...>, std::tuple>
    mxArray* ToMatlab(T<Args...> val_);
    // 2. special implementation for containers (e.g. vectors and arrays
    // containing std::tuple or std::pair)
    template<class Cont>
    requires
        Container<Cont> && (
            is_specialization_v<typename Cont::value_type, std::pair> ||
            is_specialization_v<typename Cont::value_type, std::tuple>)
    mxArray* ToMatlab(Cont data_);

    // generic ToMatlab that converts provided data through type tag dispatch
    template <class T, class U>
    requires (!Container<T>)
    mxArray* ToMatlab(T val_, U);

    //// struct of arrays
    // machinery to turn a container of objects into a single struct with an array per object field
    // default output is storage type corresponding to the type of the member variable accessed through this function, but it can be overridden through type tag dispatch (see getFieldWrapper implementation)
    template<typename Cont, typename... Fs>
    requires Container<Cont>
    mxArray* FieldToMatlab(const Cont& data_, bool rowVector_, Fs... fields);
}