#pragma once
#include <tuple>
#include <type_traits>

// get last type in template parameter pack (or optionally 2nd last when N=1, 3rd last when N=2, etc)
template<size_t N, class... Ts>
using last = typename std::tuple_element_t< sizeof...(Ts) - N - 1, std::tuple<Ts...> >;

// higher order function to forward an index sequence
template <typename F, size_t... Is>
constexpr auto indices_impl(F f, std::index_sequence<Is...>)
{
    return f(std::integral_constant<size_t, Is>()...);
}
template <size_t N, typename F>
constexpr auto indices(F f)
{
    return indices_impl(f, std::make_index_sequence<N>());
}

// Given f and some args t0, t1, ..., tn, calls f(tn, t0, t1, ..., tn-1)
template <typename F, typename... Ts>
constexpr auto rotate_right(F f, Ts... ts)
{
    auto tuple = std::make_tuple(ts...);
    return indices<sizeof...(Ts) - 1>([&f, &tuple](auto... Is) constexpr// pass elements 1 to N-1 as input to lambda
    {
        return f(												        // call user's function with:
                    std::get<sizeof...(Ts) - 1>(tuple),			        // last element of tuple
                    std::get<Is>(tuple)...);						    // all inputs to lambda (elements 1 to N-1)
    });
}
// Given f and some args t0, t1, ..., tn, calls f(tn-1, t0, t1, ..., tn)
template <typename F, typename... Ts>
constexpr auto rotate_right_except_last(F f, Ts... ts)
{
    auto tuple = std::make_tuple(ts...);
    return indices<sizeof...(Ts) - 2>([&f, &tuple](auto... Is) constexpr// pass elements 1 to N-2 as input to lambda
    {
        return f(												        // call user's function with:
                    std::get<sizeof...(Ts) - 2>(tuple),			        // element N-1
                    std::get<Is>(tuple)...,						        // all inputs to lambda (elements 1 to N-2)
                    std::get<sizeof...(Ts) - 1>(tuple)				    // last element
        );
    });
}
// Given f and some args t0, t1, ..., tn, calls f(t0, t1, ..., tn-1)
template <typename F, typename... Ts>
constexpr auto drop_last(F f, Ts... ts)
{
    return indices<sizeof...(Ts) - 1>([&f, &ts...](auto... Is) constexpr
    {
        auto tuple = std::make_tuple(ts...);
        return f(std::get<Is>(tuple)...);
    });
}