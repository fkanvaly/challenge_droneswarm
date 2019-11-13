# CHALLENGE ESSAIM DE DRONE

# Envirennemnt de simulation

## Requirements (ROS Melodic [vient avec gazebo]) #

L'environnement de simultaion a été fait avec Gazebo + ROS Melodic (Ubuntu 18.04 LTS).
Par defaut la version complete de ROS vient avec Gazebo. Nous suggerons donc d'installer la version complete en suivant les instructions suivantes:

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

Installation complète de ros: (Recommandé): 
```
sudo apt-get install ros-melodic-desktop
```

2. Initialiser rosdep

Avant de pouvoir utiliser ROS, vous devez initialiser rosdep . rosdep vous permet d'installer facilement les dépendances du système pour la source que vous souhaitez compiler et est nécessaire pour exécuter certains composants essentiels dans ROS.
```
sudo rosdep init
update rosdep
```

3. Configuration de des variable du systeme

```
echo "source /opt/ros/melodic/setup.bash" >> ~ / .bashrc
source ~ / .bashrc
```

4. Installer les package python 

```
sudo pip3 install rospkg catkin_pkg
sudo apt-get install python-catkin-tools python3-dev python3-numpy
```

## Compiler notre environnement 
une fois ROS installer, il suffira juste d'aller dans le dossier **simulation_ws** et compiler l'environnement.

```
cd simulation_ws
catkin build
```


Après la compilation de nouveaux dossier se créeront et le dossier simulation_ws devrait être organisé comme suit

```
simulation_ws
    +-- build
    +-- devel
    +-- logs
    +-- src
```

toujours dans le dossier simulation_ws entrer la commande:
`source devel/setup.bash`

Maintenant toute les variables du système devrait être installée pour lancer demarer il vous reste juste a entrer:
```
roslaunch sjtu_drone challenge.launch
```


