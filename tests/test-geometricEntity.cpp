#include "../include/catch.hpp"
#include "../include/geometricEntityMock.hpp"

TEST_CASE("GeomtricEntity can calculate euclidean distance",
          "[geometricEntity]") {
  geometricEntityMock gem = geometricEntityMock('a');
  REQUIRE(std::abs(gem.euclideanDistance(0, 0, 0, 5) - 5.0) == 0.0);
  REQUIRE(std::abs(gem.euclideanDistance(0, 0, 5, 5) - 7.0710) < 0.0001);
  REQUIRE(std::abs(gem.euclideanDistance(-5, -5, 5, 5) - 14.1421) < 0.0001);
  REQUIRE(std::abs(gem.euclideanDistance(0, 0, 0, 0)) == 0.0);
}
TEST_CASE("GeomtricEntity can calculate manhattan distance",
          "[geometricEntity]") {
  geometricEntityMock gem = geometricEntityMock('a');
  REQUIRE(gem.manhattanDistance(0, 0, 0, 5) == 5);
  REQUIRE(gem.manhattanDistance(0, 0, 5, 5) == 10);
  REQUIRE(gem.manhattanDistance(-5, -5, 5, 5) == 20);
  REQUIRE(gem.manhattanDistance(0, 0, 0, 0) == 0.0);
}
