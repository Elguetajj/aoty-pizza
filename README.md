# Aoty pizza 💿🍕
In its current state aoty-pizza allows you to rate, love and review albums previously selected by me. Spotify api implementation is on the way, soon you will be able to rate what you have been listening recently or anything in the spotify backlog. ( I'm still kind of figuring out the OAuth 2.0 danse)

## Usage
First clone the repo.
Then get docker ready!!! To use aoty-pizza you need to build and run a docker container using the DOCKERFILE provided.
The commands you need to run are:

```console
your@console: path/to/aoty-pizza$ docker build --tag whichever-tag-you-want .
```
This command will build and tag an image from the DOCKERFILE contained in this repository. After this run the following:
```console
your@console: path/to/aoty-pizza$ docker run --publish 5000:5000 --detach --name aoty-pizza aoty-pizza:1.0
```
This command should start running a container based on the image you just created!!!

Now we are almost ready to start rating.
If you aren't on docker toolbox, you can head over to http://localhost:5000 the aoty-pizza should be up and running.
If you are running docker toolbox, then you need to find out the ip that your computer has assigned to the docker machine.
To do this you just need to execute the following command.

```console
your@console: path/to/aoty-pizza$ docker-machine ip default
```
After executing this command the ip should be printed out on your console. To access aoty-pizza now you just need to type http://whatever-ip-you-got:5000

## Walkthrough 

When you first enter aoty-pizza you will be met up by something like this.

![Home screenshot](./images/home_screen.png)

As it clearly states, you haven' logged any albums yet. To start rating and logging head over to albums on the nav bar. The albums page will look something like this. 

![Albums screenshot](./images/albums.png)

Now you just have to select an album and click on the log button. That will lead you to a screen like this one.

![Log screenshot](./images/log.png)

Now just rate it, love it, and/or review it.
After clicking on the log button you won't get any prompt (work in progress 😬) but if you head back home by clicking on aoty-pizza on the nav bar you'll see your log is there.

![dashboard screenshot](./images/dashboard.png)

In this page you'll see every log you make, alongside 2 buttons, if none of those buttons are clicked this page will show you the logs from earliest to latest. If you click one of those the albums will get sorted by their rating in either descening or ascending order (How I did that is the interesting part). 

## Data Structures

1. Arrays of Dictionaries: Since I have yet to implement a database, everything is currently running on the python runtime. To store the albums, I used arrays of dictionaries. Every album is a dictionary, a series of albums is an array of dictionaries. This is because it is easy to transform jsons into dictionaries and vice versa. This is usefull because most API calls are made with jsons, so it saves me time and memory to just use the json.loads() function from the python standard library rather than creating custom objects to store the albums. However this might change once a database is implemented. As it is, ./app/albums.py contains the class that is used to store and update the albums. This class acts as our pretend database for now. 

2. Heapsort vs. Quicksort: 
In an app like this, specially when it is extended and the social features implemented, sorting this kind of logs will be a recurring task. On the finished app you will have the ability to follow people and see in a dashboard similar to the one you can see right now all of your friends logs. All of this means that on the finished app, sorting albums will be a recurring task, and the amount of albums to be sorted could potentially grow to be around the thousands of albums. Therefore shoosing a good sorting algorithm is vital. 

As you might have notice, aoty-pizza has the option to sort the albums you have logged in two ways. The ascending and descending sorts are implemented using different sorting algorithms, Heapsort and Quicksort respectively. These are commonly known as the best sorting algorithns, however they are very different. I wasn't sure which to use so i implemented both and compared them. Profiling for my heapsort and quicksort implementations can be found on ./app/logs and will be discussed briefly over the next section.



## Profiling Heapsort vs. Quicksort


Like Merge Sort, QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot Heap sort is a comparison based sorting technique based on Binary Heap data structure. These sorting algorithms are among the most used because they can easilly be implemented with arrays which is the most common data structure in web development and they are very reliable in terms of time complexity.

![dashboard screenshot](./images/sorting.png)

However, implementing the Heapsort poses a greater conceptual challenge as you need to stop thinking of your array as an array and start thinking of it as a heap. 

![dashboard screenshot](./images/binaryheap.png)

This problem shows why data structures are worth it. As you might have noticed on the table, time complexities are the same for both algorithms for their best and avarage cases. However their worst cases greatly differ as well as their memory efficiency. It might not look significant given nowedays we have very powerfull computers but as the profiling of my implementations shows, it is extremely significant.

![dashboard screenshot](./images/heapsrot_prof.png)
![dashboard screenshot](./images/quicksort_profile.png)

As you can see heapsort manages to sort 10,000 elements in only 0.065 and without using any extra space whereas quicksort couldn't even sort 1,000  elements without the compiler shutting of the recursion because it was approaching a stack overflow.

These profiling logs are stored in ./app/logs , the files ./app/profiler_quicksort.py and ./app/profiler_heapsort.py have the code for profiling the implementations, you can play around with the amount of random ratings to give them to see how they would perform. The random function can also be changed to represent different distributions of data to see how the algorithms would behave under different circumstances. But as far as the specific use case, heap sort wins by a long shot. Hurrah for heaps!!!!