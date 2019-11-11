#include "lib/XmlRpc.h"
#include <iostream>

using namespace XmlRpc;

int main(int argc, char* argv[]) {
  if (argc != 3) {
    std::cerr << "Usage: HelloClient serverHost serverPort\n";
    return -1;
  }
  const char* hostname = argv[1];
  int port = atoi(argv[2]);

// Create a client and connect to the server at hostname:port
  XmlRpcClient c(hostname, port);

  XmlRpcValue noArgs, result;
double a1, a2;
  while (true) {
    char opcion;
    std::cout << "=========================================" << std::endl
              << "ROBOT MOVIL 3GDL RPC" << std::endl
              << "=========================================" << std::endl;
    std::cout << "A. Activar Robot" << std::endl
              << "D. Desactivar Robot" << std::endl
              << "1. Mover articulacion 1" << std::endl
              << "2. Mover articulacion 2" << std::endl
              << "3. Mover articulacion 3" << std::endl
              << "4. Abrir/Cerrar Pinza" << std::endl
              << "H. HOMING" << std::endl
              << "r. Reporte" << std::endl
	      << "t. Terminar" << std::endl
              << "*****************************************" << std::endl;
    std::cout << "Opcion: ";
    std::cin >> opcion;
    switch (opcion) {
    case 't':
      return 0;
      break;
    case 'r':
    if (c.execute("rep", noArgs, result))
    std::cout << result << std::endl;
      break;   
    case 'A':
    std::cout << "El robot se activara... ";
    noArgs[0] = 1;
    if (c.execute("actv", noArgs, result))
    std::cout << result << std::endl;
      break;
    case 'D':
    std::cout << "El robot se desactivara... ";
    noArgs[0] = 0;
    if (c.execute("desactv", noArgs, result))
    std::cout << result << std::endl;
      break;
      case 'H':
    std::cout << "Homing en proceso ... ";
    noArgs[0] = 0;
    if (c.execute("hom", noArgs, result))
    std::cout << result << std::endl;
      break;
      
    case '1':
    std::cout << "¿A qué posición final quiere llegar en articulación 1? (en grados): ";
      std::cin >> a1;
    noArgs[0] = a1;
    if (c.execute("art1", noArgs, result))
    std::cout << result << std::endl;
      break;
    case '2':
    std::cout << "¿A qué posición final quiere llegar en articulación 2? (en grados): ";
      std::cin >> a1;
    noArgs[0] = a1;
    if (c.execute("art2", noArgs, result))
    std::cout << result << std::endl;
      break;
    case '3':
    std::cout << "¿A qué posición final quiere llegar en articulación 3? (en grados): ";
      std::cin >> a1;
    noArgs[0] = a1;
    if (c.execute("art3", noArgs, result))
    std::cout << result << std::endl;
      break;
    case '4':
    std::cout << "1=Abrir pinza 0=Cerrar pinza: ";
      std::cin >> a1;
    noArgs[0] = a1;
    if (c.execute("efec", noArgs, result))
    std::cout << std::endl << result << std::endl;
      break;
    default:
      std::cout << "No se seleccionó ninguna operación válida." << std::endl; 
  }
  }
}
