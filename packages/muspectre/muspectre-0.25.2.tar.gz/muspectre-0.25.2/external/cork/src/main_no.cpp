// +-------------------------------------------------------------------------
// | main.cpp
// |
// | Author: Gilbert Bernstein
// +-------------------------------------------------------------------------
// | COPYRIGHT:
// |    Copyright Gilbert Bernstein 2013
// |    See the included COPYRIGHT file for further details.
// |
// |    This file is part of the Cork library.
// |
// |    Cork is free software: you can redistribute it and/or modify
// |    it under the terms of the GNU Lesser General Public License as
// |    published by the Free Software Foundation, either version 3 of
// |    the License, or (at your option) any later version.
// |
// |    Cork is distributed in the hope that it will be useful,
// |    but WITHOUT ANY WARRANTY; without even the implied warranty of
// |    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// |    GNU Lesser General Public License for more details.
// |
// |    You should have received a copy
// |    of the GNU Lesser General Public License
// |    along with Cork.  If not, see <http://www.gnu.org/licenses/>.
// +-------------------------------------------------------------------------

// This file contains a command line program that can be used
// to exercise Cork's functionality without having to write
// any code.

#include "files.h"

#include <iostream>
using std::cerr;
using std::cout;
using std::endl;
#include <sstream>
using std::string;
using std::stringstream;

using std::ostream;

#include "cork.hh"
#include "cork_interface.hh"


int main(int argc, char *argv[]) {
  corkpp::CorkTriMesh pixel;
  corkpp::CorkTriMesh precipitate140;
  corkpp::CorkTriMesh intersection140;

  corkpp::loadMesh("toolbox_graph/precipitate140.off", precipitate140);
  corkpp::loadMesh("toolbox_graph/pixel.off", pixel);

  corkpp::compute_intersection(precipitate140, pixel, intersection140);
  auto && vol = corkpp::volume_calculator(intersection140);
  std::cout<< vol <<std::endl;
  corkpp::saveMesh("toolbox_graph/intersection140.off", intersection140);

  return 0;
}
