Assignment 1 – Part 1/2: Multiprocessing

• What are your conclusions?
- Sequential for loop: This method is the slowest since it processes each number individually, one at a time.
- Multiprocessing for loop (one process per number): This can be a bit sluggish too, as spinning up a new process for each number can drain system resources and lead to inefficiency.
- Multiprocessing pool with map(): This approach is quicker than the previous two because it handles multiple tasks simultaneously, managing processes in a more efficient way.
- Multiprocessing pool with apply(): It’s similar to map(), but it tackles one task at a time. When you have a lot of tasks, it tends to be slower than map().
- ProcessPoolExecutor: This is a more straightforward, high-level method for running tasks in parallel. It’s user-friendly and can be just as efficient as using a multiprocessing pool.


• Redo the test with 107 numbers.
• Test both synchronous and asynchronous versions in the pool.
• What are your conclusions?
If you run the test with 10 million numbers, the sequential method will take significantly longer. The multiprocessing methods will still be quicker, but your computer might struggle with the increased workload, and you could run into system limits, like having too many open files.

• What happens if more processes try to access the pool than there are available connections?
If there are more processes than available connections, the extra processes will have to wait until a connection opens up. This helps avoid issues and ensures that no more than the permitted number of processes are using the connections at any given time.

• How does the semaphore prevent race conditions and ensure safe access to the connections?
The semaphore functions like a gatekeeper, limiting how many processes can access the connections simultaneously. If too many processes attempt to use a connection, the semaphore holds them back until one becomes available, ensuring that only the allowed number of processes can access the connections at once
