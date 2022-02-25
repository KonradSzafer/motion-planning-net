# **motion-planning-net**

This work is based on Motion Planning Neural Network presented in:
https://arxiv.org/abs/1806.05767 \
The goal was to create a Neural Planner for 2D maps.

# **Network structure**

<p align="center">
    <img src="images/network_architecture.png" alt="drawing" width="1000"/>
</p>

The network structure consists of two main parts. An encoder that encodes map images into obstacle space X_obs and the planning network itself.\
The encoder is part of an autoencoder network that has been trained to return input images. Later on planning network, which is a simple feedfroward network, uses encoded images, start position and goal positon to predict next state of an agent.\
During online planning, the paths provided by the Planning Network are simplified and checked for validity. If two consecutive states cannot be connected without encountering an object, then the A* planning algorithm is used to plan a new path between these points.

# **Data**

To train the Neural Planner, 100 diferent environments were generated. For each of this environment 4000 diferent starting and goal points were randomly choosen. It gives a total of 400000 path planning problems.

This element is necessary to focus network learning on the path.
Each image has a resolution of 120x120px.

A* algorithm was used for path planning. To minimize the number of turns, special heuristics was implemented.

Unsolved samples:
<p align="center">
    <img src="images/map_sample0.png" alt="drawing" width="240"/>
    <img src="images/map_sample1.png" alt="drawing" width="240"/>
    <img src="images/map_sample2.png" alt="drawing" width="240"/>
    <img src="images/map_sample3.png" alt="drawing" width="240"/>
    <img src="images/map_sample4.png" alt="drawing" width="240"/>
</p>

Solved samples:
<p align="center">
    <img src="images/map_solved_sample0.png" alt="drawing" width="240"/>
    <img src="images/map_solved_sample1.png" alt="drawing" width="240"/>
    <img src="images/map_solved_sample2.png" alt="drawing" width="240"/>
    <img src="images/map_solved_sample3.png" alt="drawing" width="240"/>
    <img src="images/map_solved_sample4.png" alt="drawing" width="240"/>
</p>

# **Code**

To generate a dataset, first you need to generate maps. To do this, run the generate_maps.ipnb file. Then you have to plan training paths. The next step is to plan the paths for the generated maps. To do so run A_star_path_planning.ipnb.\
Last step is to train the network, for this use the motion_planning_network.ipnb file.

# **Results**

First part was to train encoding part of a network. To do so  Simple autoencoder model was created as suggested in the papier. But because of its simplicity the output results were quite bad. 

Zdjęcia

To improve them resunet model structure was implemented, which uses residual layers and shortcut connections. Now the results looked a lot better but the encoder output vector was bigger.

Zdjęcia

Next the planning part of a network was trained, and it is the most problematic one. If encoder from resunet was used the network no matter the input, was returning always the same results for predicted points. Always half of the map dimensions.

Zdjęcia

The problem was too big output vector from resunet encoder. So simpler encoder from autoencoder was used. Now it was a little bit better but still not perfect. The network was outputting different points for different maps but not for different input points on the same map.

Zdjęcia

The problem was that the network was learning the wrong thing. Instead of learning how to predict points on a map for a given start and goal, it was learning how to predict the best (smallest loss) point for a map and was deaf on start and goal change.

The solution to this problem is to generate more data paths for a given map to make the network focus on changing start and goal points and not on a map.


