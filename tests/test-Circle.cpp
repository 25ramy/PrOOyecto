#include "../include/Circle.hpp"
#include "../include/Generador.hpp"
#include "../include/catch.hpp"

TEST_CASE("Circle area gets returned", "[Circle]") {
  Circle circle = Circle('a', 2, 2, 2);
  REQUIRE(std::abs(circle.getArea() - 12.566371) < 0.00001);
}
TEST_CASE("Circle perimeter gets returned", "[Circle]") {
  Circle circle = Circle('a', 3, 3, 3);
  REQUIRE(std::abs(circle.getPerimeter() - 18.8495) < 0.0001);
}
TEST_CASE("Circle is printed on matrix", "[Circle]") {
  SECTION("Should succed only when figure is in map boundries") {
    Circle circle = Circle('a', 1, 1, 1);
    int rows = 3, cols = 3;
    char **testmap = new char *[rows];
    for (int i = 0; i < rows; ++i) {
      testmap[i] = new char[cols];
      for (int j = 0; j < cols; j++) {
        testmap[i][j] = 'o';
      }
    }
    testmap[0][1] = circle.getColor();
    testmap[2][1] = circle.getColor();
    testmap[1][0] = circle.getColor();
    testmap[1][2] = circle.getColor();
    Generador gen = Generador("input", true, cols, rows);
    REQUIRE(circle.draw(gen.getMap(), cols, rows) == true);
    REQUIRE(gen.compareMap(testmap));

    circle = Circle('a', 1, 2, 2);
    REQUIRE(circle.draw(gen.getMap(), cols, rows) != true);
  }
}
