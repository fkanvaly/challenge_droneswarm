# CHALLENGE ESSAIM DE DRONE

# Envirennemnt de simulation

## Requirements (ROS Melodic [vient avec gazebo]) #

L'environnement de simultaion a été fait avec ROS Melodic (Ubuntu 18.04 LTS).
Par defaut cette version de ROS vient avec Gazebo. Nous suggerons donc d'installer la version complete avec la commande:
1. Installation 
Tout d’abord, assurez-vous que votre index de paquet Debian est à jour:
    ```Shell
    sudo apt update
    ```

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
    sudo apt installer python-rosinstall python-rosinstall-generator python-wstool build-essential
    ```

## Compiler notre environnement 
une fois ros installer, il suffira juste d'aller dans le dossier **simulation_ws** et compiler l'environnement.

```
cd simulation_ws
catkin build
```

Après la compilation de nouveaux dossier se créeront et le dossier simulation_ws devrait être organisé comme suit

simulation_ws
    |-> build
    |-> devel
    |-> logs
    |-> src

toujours dans le dossier simulation_ws entrer la commande:
`source devel/setup.bash`

Maintenant toute les variables du système devrait être installée pour lancer demarer il vous reste juste a entrer:
```
roslaunch sjtu_drone challenge.launch
```


