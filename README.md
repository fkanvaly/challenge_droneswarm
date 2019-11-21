# CHALLENGE ESSAIM DE DRONE

# Environnement de simulation

## Requirements (ROS Melodic [vient avec gazebo]) #

L'environnement de simulation a été fait avec Gazebo + ROS Melodic (Ubuntu 18.04 LTS).
Par defaut la version complete de ROS vient avec Gazebo. Il faut donc d'installer la version complète: **ros-melodic-desktop-full**. Vous trouverez les instructions sur le site de ros : [lien installation](http://wiki.ros.org/melodic/Installation/Ubuntu)

## Compiler notre environnement et lancer la simulation

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


Toujours dans le dossier **simulation_ws** entrer la commande:
`source devel/setup.bash`

Maintenant toutes les variables du système devraient être installées pour lancer la simulation il vous reste juste à entrer:
```
roslaunch sjtu_drone simple.launch
```

# Package python
dans le dossier `py_control` se trouve le script qui permet de contrôler les drones. Nous avons fournis un notebook qui vous servira d'exemple d'utilisation du script.

installation des packages python:
```
pip3 install -r requirements.txt
```


## Piloter les drones depuis Python

Le dossier **py_control** contient une interface Python permettant d'intéragir avec l'environnement de simulation dans lequel les drones évoluent. Deux classes sont fournies : ``Drone`` et ``DroneSwarm``, la seconde étant devant suffire pour se familiariser avec l'environnement.

Le fichier **exemple.py** fournit un exemple basique démontrant comment piloter un essaim de drones. Lancez Gazebo avec ``roslaunch sjtu_drone simple.launch``, mettez en marche la simulation en cliquant sur le bouton play en bas de la fenêtre qui s'ouvre, puis exécutez ``python3 exemple.py``. Notez bien dans **exemple.py** l'utilisation nécessaire de ``turn_on`` et ``turn_off`` avant et après l'envoi de toute commande. Pour plus de détails sur l'interface des classes, se référer aux fichiers **drone.py** et **drone_swarm.py**.

