Genetic Algorithm for Optimizing Delivery Routes

Problem
The main challenge we’re tackling is how to optimize delivery routes to minimize both travel distance and time for vehicles.

Goals
Our goal is to improve delivery routes using a genetic algorithm. We also want to speed things up by taking advantage of parallelism with MPI and evaluate the algorithm's performance.

Approach
We developed a genetic algorithm that evolves delivery routes over multiple generations. To enhance performance, we utilized MPI for parallel computing.

Tools and Technologies
Programming Language: Python
Libraries: mpi4py, numpy
MPI Implementation: MPICH

Challenges
We encountered some obstacles while setting up MPI and ensuring it worked properly. Debugging parallel code proved to be another challenge, as did finding the right balance between solution accuracy and processing time.

Results
The genetic algorithm effectively optimized the routes, resulting in a significant reduction in both travel time and distance, especially when we used parallel computing.

Future Work
Looking ahead, we plan to explore different strategies for the genetic algorithm, enhance parallelism for larger datasets, and integrate real-time traffic data for even better optimization.

Conclusion
This project showcased that genetic algorithms can successfully optimize delivery routes, and that MPI plays a crucial role in speeding up the process.
