project(my_lib_python_interface)

set(includes includes/ 
            ${my_lib_dir}/ 
            ${my_lib_dir}/includes
            ${common_dir}/
)

set(sources src/xlExport.cpp)

add_compile_definitions(${PROJECT_NAME}_EXPORTS
                        _WINDLL
)

add_library(${PROJECT_NAME} SHARED ${sources})
target_include_directories(${PROJECT_NAME} PUBLIC ${includes} ${common_includes_dir})
target_link_libraries(${PROJECT_NAME} PUBLIC fdm_world excel_sdk_api)
set_target_properties(${PROJECT_NAME} PROPERTIES SUFFIX ".xll")