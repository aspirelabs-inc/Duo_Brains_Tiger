

<img src="https://user-images.githubusercontent.com/25334227/162142531-44377fdd-3b0c-40f3-b925-d907b57d5852.png" height="64" width="auto">

# Duo

### Table of Contents:
1. [Contributors](#Contributors)
2. [Problem Statement](#Problem)
3. [Description](#Description)
4. [Dependencies](#Dependencies)
5. [Installation](#Installation)
6. [Issues and Improvements](#Issues)
7. [Reflections](#Reflections)
8. [References](#References)

<a name="Contributors"/>

## Contributors
1. Ryan Kelly

    a. 5197019904

    b. lryannathaniel@gmail.com
2. Anish Jain

    a. 5164685054

    b. anishjain@live.com

3. Silen Naihin

    a. 3853106667

    b. silen.naihin@gmail.com


<a name="Problem"/>

## Problem Statement
#### Graph for better world. 

If you live in a first world country, you can fulfill most of your lower-level needs with a few taps. Hungry? Food at your doorstep. Feeling down? Post on social media and get hundreds of comments praising you. But then, why, are the overwhelming majority people still unfulfilled?

The answer is in the lack of fulfillment. Once the basic needs are covered, the next step is to reach fulfillment in the pursuit of self-actualization - the realization of one’s truest potential. So many are tricked into optimizing for short term relief. And who could blame them? An infinite amount of tasks constantly vying for attention, robbing us of our valuable time and making a profit off of it. The things that give fulfillment get pushed to the side. How many great engineers and scientists that could have contributed to the great march of human progress has the world been deprived of?

What is it going to take for more people to realize their true potential?

First, we need to understand that to realize our potential, we need to pursue the things that are meaningful to us - our aspirations. Meditation. Staying healthy. Talking to your family. Working on something that truly excites you. To pursue these aspirations, we need to give back stolen time and the inspiration needed to execute.

Currently, many knowledge workers spend hours every week copying and pasting of data from one software window to another over and over again. Duo frees up that time by automating those tasks and giving people back the priceless resource of time. Duo inspires them to utilize that for the pursuit of their own aspirational ideals - how much great change can we enable with the resulting first, second, third, etc. order effects?

<a name="Description"/>

## Description
Creating an AI desktop assistant that effectively automates data entry tasks on the UI of a computer is a long-tail problem. A data entry task that one user is doing will likely be completely different compared to one another is doing. Therefore, a true solution needs to be robust across a wide set of tasks. The status quo consists of a brittle solution - scripts. Here, UI scripts are either written in code or using “low-code” tools like Robotic Process Automation (RPA). The problem here is three-fold. First, there is a high learning curve, which is a barrier to many knowledge workers extracting the value. Second, the time investment per script is high, additional friction. And third, the scripts are brittle because any slight perturbance in the UI structure would render them useless.

Graphs offer the perfect answer to creating this successful AI assistant. The UI is naturally structured in a graph. Various elements like software applications, buttons, blocks of texts, lists, and links would all be nodes. There would be directed edges connecting different nodes to encapsulate relationships between them, such as software applications being “parents” of all the elements within them.

By effectively encapsulating the UI in the optimal graphical structure, and creating an AI desktop assistant that learns the right properties about different nodes within the graph, the assistant can learn data entry tasks as queries on that graph.

To minimize the friction and learning curve needed to learn the tasks as queries on that graph, we created a system that learns a (basic set) of queries by observing the user perform a task.

By representing the UI as a graph and tasks as queries on that, which are learned by observing the user, we can have a system that minimizes the learning curve, minimizes the time investment to create an automation, and increase generalizability.

Note: because of the complexity of the full, end system with all of its subsystems, we created a minimum functioning prototype. For a more robust set of capabilities, the various subsystems would have to be expanded upon.

##### Impactfulness
There are so many problems in the world, just think about how many are listed for this competition. All of them critical to our success and progress as a species. The real problem, is not enough people are working on hard problems. Even for the people that want to work on those pressing challenges, many do not have the time or inspiration to pursue those goals. There needs to be a solution that frees peoples’ time and allows them to direct it towards their aspirations. This has the potential to be that solution.

##### Innovativeness
We have three innovative components of our graph formulation, in its nodes, edges, and queries. Structuring the UI as a knowledge graph with UI elements (buttons, text, links, lists, etc.) as nodes is innovative. Capturing parent/child and spatial relationships as directed edges between nodes is innovative. And learning tasks as queries on the UI knowledge graph is innovative.

##### Ambitiousness
We believe that while data entry is the starting point, there are a wide variety of tasks that we can encapsulate as queries on a UI knowledge graph.
The plan is to use user data to incrementally learn additional edges and queries to consistently expand out the set of tasks that our assistant can automate. This way, we free more and more time for peoples’ aspirations. Eventually, the graph will feature a wide set of edges and queries, allowing it to automate a variety of tasks across domains, well beyond simpler, starting ones like data entry or formatting. The more the users teach it various tasks, the greater the shared knowledge across users would be. As that shared knowledge accumulates, it will be a great step in human technological progress.

##### Applicabilty
Entry-level knowledge workers who aren’t designers or engineers, including analysts, accountants, marketers, consultants, auditors, and more, spend hours every week on data entry. Copy-paste, copy-paste between one software to another. They all have the potential to be in our eventual market.
But initially, we can’t market to all of them. So, we are going to start with the market with the highest need for a data entry solution - data entry freelancers. They do data entry tasks for a living, and if it works for them - it will likely work for others. 

##### Data 
Using Windows Accessability Service we are able to generate data based off of the ui.

##### Technology Stack
Python with pyTigerGraph in order to generate the graph.

<a name="Dependencies"/>

## Dependencies
- pyTigerGraph
- grpcio
- grpcio-tools

<a name="Installation"/>

## Installation

1. Create a local instances in an environment
2. Create a Python environent with pyTigerGraph installed
4. Clone this repository
5. Open config.py and enter your details to the TigerGraph instance (host, username and password)
6. Run python schema.py to generate the queries
7. Run server.py to see the output based on a simulated ui layer. We were working with Windows Accessibility service in order to get an actual UI output done but were unable to get the two different repos connected and ready by the submission time.

<a name="Issues"/>

## Issues and Improvements

- We can improve the speed at which Duo runs and complete tasks even faster. Now that we have a better grasp on TigerGraph we could probably improve certain things if we were to do this again.
- There is an error when building the wheel for numpy on M1 Macs.
- In the future we could have a more robust system that could handle any type of entry data regardless of the context and expand to things further than data entry.
- Instead of a simulated dataset we would have an actual parser of ui objects.

<a name="Reflections"/>

## Reflections

- The TigerGraph docs were useful in debugging and figuring out next steps to do what needed to be done. At times, I thought that error messages were a bit vague, and we struggled to get some things running on an M1 Mac. The learning resources on Devpost allowed us to get off of the ground quickly. Something that we could have improved is having a smaller scope of the project. We had huge aspirations to build a robust system and worked towards that starting from the system architecture and in the way that we were using TigerGraph. Towards the end we realized we needed to cap off what our goals were and scope down the plan. Even still, we found it hard to get everything done by the deadline and should have been a bit less ambitous in our project goals. Overall, we enjoyed working with TigerGraph and will become a tool that we use in the future. We hope to continue to working on the project moving past TigerGraph and smooth out things we weren't able to by the submission period.

<a name="References"/>

## References
- http://toby.li/files/TobyLi_Thesis.pdf was used as the basis for which to build upon.
