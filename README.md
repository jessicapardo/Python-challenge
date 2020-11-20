# Python-challenge

## Background

Welcome to the world of programming with Python. In this assignment, two Python Challenges will be completed: PyBank and PyPoll.

## PyBank

![revenue](Images/revenue-per-lead.png)

In this challenge, The Python script for analyzing the financial records of a company will be created using a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

The Python script will analyzes the records and calculate each of the following:

  * The total number of months included in the dataset

  * The net total amount of "Profit/Losses" over the entire period

  * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire 
  period

## Results

Python script: PyBank/main.py
Results: PyBank/Analysis/PyBankResults.txt

 ```text
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1170593)
Greatest Decrease in Profits: Sep-2013 ($-1196225)
```

## PyPoll

![Vote-counting](Images/Vote-counting.png)

In this challenge,the Python script will be helping a small, rural town modernize its vote counting process using a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`.

The Python script will analyzes the votes and calculate each of the following:

  * The total number of votes cast

  * A complete list of candidates who received votes

  * The percentage of votes each candidate won

  * The total number of votes each candidate won

  * The winner of the election based on popular vote.

## Results

Python script: PyPoll/main.py
Results: PyPoll/Analysis/PyPollResults.txt

 ```text
Election Results
----------------------------
Total Votes: 3521001
----------------------------
Khan: 63.00% (2218231)
Correy: 20.00% (704200)
Li: 14.00% (492940)
O'Tooley: 3.00% (105630)
----------------------------
Winner: Khan
----------------------------
```

## Copyright

Trilogy Education Services © 2019. All Rights Reserved.