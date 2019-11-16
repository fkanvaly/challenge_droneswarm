# CHALLENGE ESSAIM DE DRONE

# Environnement de simulation

## Requirements (ROS Melodic [vient avec gazebo]) #

L'environnement de simulation a été fait avec Gazebo + ROS Melodic (Ubuntu 18.04 LTS).
Par defaut la version complete de ROS vient avec Gazebo. Nous suggérons donc d'installer la version complète en suivant les instructions suivantes:

1. Configure your Ubuntu repositories

run:
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
```
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```
```
curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
```
```
sudo apt update
```

1. Installation 

Installation complète de ros (recommandé): 
```
sudo apt-get install ros-melodic-desktop
```

2. Initialiser rosdep

Avant de pouvoir utiliser ROS, vous devez initialiser rosdep . rosdep vous permet d'installer facilement les dépendances du système pour la source que vous souhaitez compiler et est nécessaire pour exécuter certains composants essentiels dans ROS.
```
sudo rosdep init
update rosdep
```

3. Configuration des variables système

```
echo "source /opt/ros/melodic/setup.bash" >> ~ / .bashrc
source ~ / .bashrc
```

4. Il faut enfin configurer un environnement Python permettant d'intéragir avec ROS, avec
```
sudo apt-get install python3-dev
sudo pip3 install -r requirements.txt
```

## Compiler notre environnement 

Une fois ROS installé, il suffira juste d'aller dans le dossier **simulation_ws** et compiler l'environnement.

```
cd simulation_ws
catkin build
```


Après la compilation de nouveaux dossier se créeront et le dossier **simulation_ws** devrait être organisé comme suit

```
simulation_ws
    +-- build
    +-- devel
    +-- logs
    +-- src
```

toujours dans le dossier **simulation_ws** entrer la commande:
`source devel/setup.bash`

Maintenant toutes les variables du système devrait être installée. Pour lancer il vous reste juste à entrer:
```
roslaunch sjtu_drone simple.launch
```


