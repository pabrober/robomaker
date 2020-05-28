################################################################################
#archivo make propio de ros, se puede entender como la entrada al sistema de compilacion 
# establecer la version minima requerida del cmake (compilacion) y opciones de compilacion
################################################################################
cmake_minimum_required(VERSION 2.8.3)

# nombre del paquete(donde se encuentan la aplicacion de robot)
project(robot_app)

################################################################################
# Encontrar paquetes y librerias de catkin , y dependecias del sistema
################################################################################
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

################################################################################
# configuración para módulos y scripts de Python
################################################################################
catkin_python_setup()

################################################################################
# declarar la configuración específica de catkin para pasar a dependencias del proyecto
################################################################################
catkin_package(
  CATKIN_DEPENDS
    rospy
    std_msgs
)

################################################################################
# construir
################################################################################
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

################################################################################
# instalar
################################################################################
# Add your custom nodes here. 
catkin_install_python(PROGRAMS 
  scripts/rotate.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)
