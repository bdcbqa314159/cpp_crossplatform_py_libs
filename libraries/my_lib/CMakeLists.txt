project(my_lib)

set(includes includes/)
set(sources src/functions.cpp)

add_library(${PROJECT_NAME} ${sources})
target_include_directories(${PROJECT_NAME} PUBLIC ${includes} ${common_includes_dir})