// +-------------------------------------------------------------------------
// | main.cpp
// |
// | Author: Ali Falsafi
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

#include "cork.hh"
#include "cork_interface.hh"
#include <math.h>

template <typename T>
std::vector<double> linspace(T start_in, T end_in, int num_in) {

  std::vector<double> linspaced;

  double start = static_cast<double>(start_in);
  double end = static_cast<double>(end_in);
  double num = static_cast<double>(num_in);

  if (num == 0) {
    return linspaced;
  }
  if (num == 1) {
    linspaced.push_back(start);
    return linspaced;
  }

  double delta = (end - start) / (num - 1);

  for (int i = 0; i < num - 1; ++i) {
    linspaced.push_back(start + delta * i);
  }
  linspaced.push_back(end); // I want to ensure that start and end
                            // are exactly the same as the input
  return linspaced;
}

int main(int argc, char *argv[]) {
  REal Pi = M_PI;
  corkpp::point_t center({70.5, 70.5, 0.0});
  std::vector<REal> theta = linspace(0.0, 2 * Pi, 100);
  REal vertices_precipitate_x;
  REal vertices_precipitate_y;
  REal radius{35.25};
  std::vector<corkpp::point_t> vertices_precipitate;
  for (int i = 0; i < theta.size() - 1; ++i) {
    vertices_precipitate_x = center[0] + radius * cos(theta[i]);
    vertices_precipitate_y = center[1] + radius * sin(theta[i]);
    vertices_precipitate.push_back(
        {vertices_precipitate_x, vertices_precipitate_y, 0.0});
  }

  for (int i = 0; i < theta.size() - 1; ++i) {
    vertices_precipitate_x = center[0] + radius * cos(theta[i]);
    vertices_precipitate_y = center[1] + radius * sin(theta[i]);
    vertices_precipitate.push_back(
        {vertices_precipitate_x, vertices_precipitate_y, 1.0});
  }

  std::vector<corkpp::point_t> vertices_pixel;
  corkpp::point_t origin_pixel{45.0, 45.0, 0.0};
  corkpp::point_t size_pixel{1.0, 1.0, 1.00};

  vertices_pixel = corkpp::cube_vertice_maker(origin_pixel, size_pixel);
  for (auto &&pixel_point : vertices_precipitate) {
    std::cout << pixel_point[0] << ", " << pixel_point[1] << ", "
              << pixel_point[2] << std::endl;
  }
  auto &&vol_norm = corkpp::calculate_intersection_volume_normal_state(
      vertices_precipitate, vertices_pixel);

  auto &&vol_state = corkpp::calculate_intersection_volume_state(
      vertices_precipitate, vertices_pixel);

  std::cout << "verctor:" << std::endl << vol_norm.normal_vector << std::endl;
  std::cout << "vol: " << vol_state.volume << std::endl;
  std::cout << "vol_ratio: " << vol_norm.volume_ratio << std::endl;
  std::cout << "status:" << static_cast<int>(vol_norm.status) << std::endl;
  // auto && normal average

  return 0;
}
