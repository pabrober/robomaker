# robomaker
inicio robomaker

proyecto de curso

IMPORTANTE  luego de clonar el repositorio debemos darle permisos de ejecucion a los scripts de python 
            para esto nos ubicamos en el directorio robot_ws/src/robot_app y ejecutamos el comando
            
            chmod +x scripts/rotate.py
            
para crear los paquertes de robot y simulacion 
primero nos ubicamos en el directorio de robot_wr e ingresamos los comandos 

            rosdep update
            rosdep install --from-paths src --ignore-src -r -y
            colcon build
            colcon bundle

luego hacemos los mismo pero en el directrio simulation_wr

            rosdep update
            rosdep install --from-paths src --ignore-src -r -y
            colcon build
            colcon bundle


*los comandos colcon sirven para agrupar y compilar los codigos escrito(trabajo en ROS)

luego de los de ejecutar los comandos en ambas areas de trabajo tenremos nuevas carpetas que se crearon una de estas se llama bundle
dentro de esta se encuentra un .tar llamado output .tar el cual debemos mover a un AWS s3 (bucket) para esto hacemos

estando en robot_wr

            aws s3 cp bundle/output.tar s3://nombre_bucket/nuevo_nombre_para_identificar.tar
            
estando en simulation_wr

            aws s3 cp bundle/output.tar s3://nombre_bucket/nuevo_nombre_para_identificar.tar

