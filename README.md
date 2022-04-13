# Notion-Take Home Assessment

This assessment will helped me learn a bit about how Notion works, and gave me a chance to read through code you've written in an environment and I have used Python to complete this assesment

## Goal
In this exercise, your goal is to gather some interesting information from a CSV file and populate your database with it.

## Description

 - In this assessment I have been given an input dataset (ratings.csv) which I converted to pandas dataframe and performed various transformations, analysis on the dataframe the final result is then uploaded to a Notion database by making api calls to the database. 

 - While working on this project I was stuck in the part where we required the pandas dataframe to be uploaded to the Notion api in their json format. I did complete it by referring various online resources and parsing the database format into the project and udpating it with dataframe values.

## Instructions to Run 

1. Clone the repository using git clone and open the cloned folder in any editor (I have used Pycharm to compile my code)
2. Just the run the main.py script in the terminal with command - "python main.py"
3. Once the excution is completed you can check the values updated in the Notion database

**Input**

A csv file to be ingested in the program

**Output**

Each row in the database have the following columns:

- Book name (normalized for extra whitespace and capitalization)
- Average rating from all members
- Number of “Favorites”


### References

 - https://stackoverflow.com/
 - https://sparkbyexamples.com/pandas/pandas-drop-rows-with-condition/#:~:text=Use%20pandas.,rows%20with%20condition(s).
 - https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html
 - https://devdocs.io/pandas~0.25/
