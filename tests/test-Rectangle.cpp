#include "../include/Generador.hpp"
#include "../include/Rectangle.hpp"
#include "../include/catch.hpp"

TEST_CASE("Rectangle area gets returned", "[Rectangle]") {
  Rectangle rectangle = Rectangle('a', 2, 2, 0, 0);
  REQUIRE(rectangle.getArea() == 4.0);
}
TEST_CASE("Rectangle perimeter gets returned", "[Rectangle]") {
  Rectangle rectangle = Rectangle('a', 2, 2, 0, 0);
  REQUIRE(rectangle.getPerimeter() == 8.0);
}

TEST_CASE("Rectangle should get mapped only when inside matrix",
          "[Rectangle]") {
  Rectangle rectangle = Rectangle('a', 2, 2, 0, 0);
  int rows = 4, cols = 4;
  char **testmap = new char *[rows];
  for (int i = 0; i < rows; ++i) {
    testmap[i] = new char[cols];
    for (int j = 0; j < cols; j++) {
      testmap[i][j] = 'o';
    }
  }
  testmap[0][0] = rectangle.getColor();
  testmap[0][1] = rectangle.getColor();
  testmap[1][0] = rectangle.getColor();
  testmap[1][1] = rectangle.getColor();
  Generador gen = Generador("input", true, cols, rows);
  REQUIRE(rectangle.draw(gen.getMap(), cols, rows) == true);
  REQUIRE(gen.compareMap(testmap));

  rectangle = Rectangle('a', 5, 1, 0, 0);
  REQUIRE(rectangle.draw(gen.getMap(), cols, rows) != true);
}
