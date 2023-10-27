
🎬 Demo
======

Here, we also show some cases of solving tasks by XAgent:
You can check our live demo on `XAgent Official Website <https://www.x-agent.net/>`_. We also provide a video demo and showcases of using XAgent here:

.. image:: assets/demo.gif
   :alt: Demo


Case 1. Data Analysis: Demonstrating the Effectiveness of Dual-Loop Mechanism
-----------------------------------------------------------------------------
We start with a case of aiding users in intricate data analysis. Here, our user submitted an `iris.zip` file to XAgent, seeking assistance in data analysis. XAgent swiftly broke down the task into four sub-tasks: (1) data inspection and comprehension, (2) verification of the system's Python environment for relevant data analysis libraries, (3) crafting data analysis code for data processing and analysis, and (4) compiling an analytical report based on the Python code's execution results.
Here is a figure drawn by XAgent.

.. image:: assets/statistics.png
   :alt: Data Statics by XAgent

Case 2. Recommendation: A New Paradigm of Human-Agent Interaction


### Case 2. Recommendation: A New Paradigm of Human-Agent Interaction
Empowered with the unique capability to actively seek human assistance and collaborate in problem-solving, XAgent continues to redefine the boundaries of human-agent cooperation. As depicted in the screenshot below, a user sought XAgent's aid in recommending some great restaurants for a friendly gathering yet failed to provide specific details. Recognizing the insufficiency of the provided information, XAgent employed the AskForHumanHelp tool, prompting human intervention to elicit the user's preferred location, budget constraints, culinary preferences, and dietary restrictions. Armed with this valuable feedback, XAgent seamlessly generated tailored restaurant recommendations, ensuring a personalized and satisfying experience for the user and their friends.

.. image:: assets/ask_for_human_help.png
   :alt: Illustration of Ask for Human Help of XAgent

Case 3. Training Model: A Sophisticated Tool User
-------------------------------------------------
XAgent not only tackles mundane tasks but also serves as an invaluable aid in complex tasks such as model training. Here, we show a scenario where a user desires to analyze movie reviews and evaluate the public sentiment surrounding particular films. In response, XAgent promptly initiates the process by downloading the IMDB dataset to train a cutting-edge BERT model (see screenshot below), harnessing the power of deep learning. Armed with this trained BERT model, XAgent seamlessly navigates the intricate nuances of movie reviews, offering insightful predictions regarding the public's perception of various films.

.. image:: assets/bert_1.png
   :alt: bert_1

.. image:: assets/bert_2.png
   :alt: bert_2

.. image:: assets/bert_3.png
   :alt: bert_3

📊 Evaluation
=============
We conduct human preference evaluation to evaluate XAgent's performance. We prepare over 50 real-world complex tasks for assessment, which can be categorized into 5 classes: Search and Report, Coding and Developing, Data Analysis, Math, and Life Assistant.
We compare the results of XAgent with [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT), which shows a total win of XAgent over AutoGPT. 
All running records will be released soon.

.. image:: assets/agent_comparison.png
   :alt: HumanPrefer


We report a significant improvement of XAgent over AutoGPT in terms of human preference.

.. image:: assets/eval_on_dataset.png
   :alt: Benchmarks


.. _Blog:
