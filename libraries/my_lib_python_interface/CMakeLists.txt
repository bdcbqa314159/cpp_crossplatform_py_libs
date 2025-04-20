project(superfastcode)

find_package(Python3 COMPONENTS Interpreter Development)

set(includes includes/ 
            ${my_lib_dir}/ 
            ${my_lib_dir}/includes
            ${common_dir}/
)

set(sources src/py_functions.cpp)

# add_compile_definitions(${PROJECT_NAME}_EXPORTS
#                         _WINDLL
# )
message(STATUS "[===] Python3_INCLUDE_DIRS: ${Python3_INCLUDE_DIRS}")
message(STATUS "[===] Python3_LIBRARIES: ${Python3_LIBRARIES}")
message(STATUS "[===] Python3_EXECUTABLE: ${Python3_EXECUTABLE}")


add_library(${PROJECT_NAME} SHARED ${sources})
target_include_directories(${PROJECT_NAME} PUBLIC ${includes} ${common_includes_dir} ${Python3_INCLUDE_DIRS})
target_link_libraries(${PROJECT_NAME} PUBLIC my_lib ${Python3_LIBRARIES})
# set_target_properties(${PROJECT_NAME} PROPERTIES PREFIX "${PYTHON_MODULE_PREFIX}" SUFFIX "${PYTHON_MODULE_EXTENSION}")
