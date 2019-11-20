# CHALLENGE ESSAIM DE DRONE

# Environnement de simulation

## Requirements (ROS Melodic [vient avec gazebo]) #

L'environnement de simulation a été fait avec Gazebo + ROS Melodic (Ubuntu 18.04 LTS).
Par defaut la version complete de ROS vient avec Gazebo. Il faut donc d'installer la version complète: **ros-melodic-desktop-full**. Vous trouverez les instructions sur le site de ros : [lien installation](http://wiki.ros.org/melodic/Installation/Ubuntu)

## Compiler notre environnement 

Une fois ROS installé, il suffira juste d'aller dans le dossier **simulation_ws** et compiler l'environnement.

```
cd simulation_ws
catkin build
```

Après la compilation de nouveaux dossiers se créeront et le dossier simulation_ws devrait être organisé comme suit

```
simulation_ws
    +-- build
    +-- devel
    +-- logs
    +-- src
```

toujours dans le dossier **simulation_ws** entrer la commande:
`source devel/setup.bash`

Maintenant toutes les variables du système devraient être installées pour lancer demarer il vous reste juste à entrer:
```
roslaunch sjtu_drone simple.launch
```

# Controle sur python
dans le dossier `py_control` se trouve le script qui permet de contrôler les drones. Nous avons fournis un notebook qui vous servira d'exemple d'utilisation du script.

installation des packages python:
```
pip3 install -r requirements.txt
```



