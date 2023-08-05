#ifndef TETGEN_INTERFACE_HH
#define TETGEN_INTERFACE_HH

// #include <memory>
#include <array>
#include <iostream>
#include <string.h>
#include <vector>

#include "tetgen.hh"

namespace corkpp {
using point_t = std::array<REal, 3>;
using face_t = std::array<uint, 3>;
// }
void make_faces_from_nodes(const std::vector<point_t> &precipitate_vertices,
                           std::vector<face_t> &facets);

} // namespace corkpp
#endif /* TETGEN_INTERFACE_HH */
