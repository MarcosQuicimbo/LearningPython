import matplotlib.pyplot as plt 
from random_walk import RandomWalk


# Keeep making new walks, as long as the program is active. 
while True: 
    # Make a random walk, and plot the points. 
    rw = RandomWalk(500)
    rw.fill_walk()
    plt.figure(dpi=128, figsize=(10,6))
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values)
    
    # Emphasize the first and last points. 
    #plt.scatter(0, 0, c='green', edgecolors='none', s=20)
    #plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=20 )
    
   # Set the size of the plotting window
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break