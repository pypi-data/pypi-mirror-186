include(CMakeFindDependencyMacro)

list(APPEND CMAKE_MODULE_PATH ${CMAKE_CURRENT_LIST_DIR}/modules)

if(G2O_USE_OPENGL)
  find_dependency(OpenGL)
endif()
find_dependency(Eigen3)
find_dependency(SuiteSparse)

include("${CMAKE_CURRENT_LIST_DIR}/g2oTargets.cmake")

