
add_subdirectory("./tetgen")


file(
	GLOB cork_SRC
	"./*.cpp"
	"./*.h"
    "./*.cc"
    "./*.hh"
	"./accel/*.cpp"
	"./accel/*.h"
	"./file_formats/*.cpp"
	"./file_formats/*.h"
	"./isct/*.cpp"
	"./isct/*.c"
    "./isct/*.cc"
	"./isct/*.h"
    "./isct/*.hh"
	"./math/*.cpp"
	"./math/*.h"
	"./mesh/*.cpp"
	"./mesh/*.tpp"
	"./mesh/*.h"
	"./rawmesh/*.cpp"
	"./rawmesh/*.tpp"
	"./rawmesh/*.h"
	"./util/*.cpp"
	"./util/*.h"
    "./tetgen/*.h"
    "./tetgen/*.c"
    "./tetgen/*.hh"
    "./tetgen/*.cc"
)


file(
	GLOB public_headers
	"./*.h"
)

add_definitions(
	-D_USE_MATH_DEFINES 
	-DNOMINMAX 
	-DNO_TIMER
	-DREDUCED
	-DCDT_ONLY
	-DTRILIBRARY
	-DANSI_DECLARATORS
	)

set_source_files_properties(
${cork_SRC}
PROPERTIES
COMPILE_FLAGS "-Wno-deprecated"
)

#add_definitions(-DDLLEXPORT)

add_library(corkpp STATIC ${cork_SRC})


#link tetgen 
target_link_libraries(corkpp PUBLIC gmp)
target_link_libraries(corkpp PUBLIC tetgen)

#install public facing headers and lib
# install (TARGETS cork64 DESTINATION ${PROJECT_SOURCE_DIR}/lib)
# install (FILES ${public_headers} DESTINATION ${PROJECT_SOURCE_DIR}/include)
