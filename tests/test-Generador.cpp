#include "../include/Generador.hpp"
#include "../include/catch.hpp"

TEST_CASE("Map gets initialized", "[Generador]") {

  Generador gen = Generador("input", false, 4, 4);

  SECTION("Initializes map with default fill") {
    int rows = 4, cols = 4;
    char **testmap = new char *[rows];
    for (int i = 0; i < rows; ++i) {
      testmap[i] = new char[cols];
      for (int j = 0; j < cols; j++) {
        testmap[i][j] = 'o';
      }
    }
    REQUIRE(gen.compareMap(testmap) == true);
  }
}
