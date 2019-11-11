#include "../include/Generador.hpp"
#include "../include/Triangle.hpp"
#include "../include/catch.hpp"

TEST_CASE("Triangle area gets returned", "[Triangle]") {
  Triangle triangle = Triangle('a', 0, 0, 2, 0, 2, 2);
  REQUIRE(triangle.getArea() == 2.0);
}
TEST_CASE("Triangle perimeter gets returned", "[Triangle]") {
  Triangle triangle = Triangle('a', 0, 0, 2, 0, 2, 2);
  REQUIRE(std::abs(triangle.getPerimeter() - 6.828427) < 0.0001);
}

TEST_CASE("Triangle should get drawed only when inside map", "[Triangle]") {
  Triangle triangle = Triangle('a', 0, 0, 1, 0, 0, 1);
  int rows = 4, cols = 4;
  char **testmap = new char *[rows];
  for (int i = 0; i < rows; ++i) {
    testmap[i] = new char[cols];
    for (int j = 0; j < cols; j++) {
      testmap[i][j] = 'o';
    }
  }
  testmap[0][0] = triangle.getColor();
  // testmap[0][1] = triangle.getColor();
  // testmap[0][2] = triangle.getColor();
  testmap[1][0] = triangle.getColor();
  testmap[0][1] = triangle.getColor();
  // testmap[1][2] = triangle.getColor();

  Generador gen = Generador("input", true, cols, rows);
  REQUIRE(triangle.draw(gen.getMap(), cols, rows) == true);
  REQUIRE(gen.compareMap(testmap));

  triangle = Triangle('a', 0, 0, 2, 0, 2, 5);
  REQUIRE(triangle.draw(gen.getMap(), cols, rows) != true);
}
