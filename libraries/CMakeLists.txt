project(libraries)

set(common_includes_dir ${CMAKE_CURRENT_SOURCE_DIR}/common/)

set(my_lib_dir ${CMAKE_CURRENT_SOURCE_DIR}/my_lib)
set(common_dir ${CMAKE_CURRENT_SOURCE_DIR}/common)

add_subdirectory(my_lib)
add_subdirectory(my_lib_python_interface)

