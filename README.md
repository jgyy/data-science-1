# Training Piscine datascience - 1

**Data Warehouse**

**Summary:** Today, you will discover the creation of a Data Warehouse

**Version:** 1.1

## Contents

1. [General rules](#chapter-i-general-rules)
2. [Introduction](#chapter-ii-introduction)
3. [Exercise 00](#chapter-iii-exercise-00)
4. [Exercise 01](#chapter-iv-exercise-01)
5. [Exercise 02](#chapter-v-exercise-02)
6. [Exercise 03](#chapter-vi-exercise-03)
7. [Submission and peer-evaluation](#chapter-vii-submission-and-peer-evaluation)

## Chapter I
### General rules

- You have to render your modules from a computer in the cluster either using a virtual machine:
  - You can choose the operating system to use for your virtual machine
  - Your virtual machine must have all the necessary software to realize your project. This software must be configured and installed.
- Or you can use the computer directly in case the tools are available.
  - Make sure you have the space on your session to install what you need for all the modules (use the goinfre if your campus has it)
  - You must have everything installed before the evaluations
- Your functions should not quit unexpectedly (segmentation fault, bus error, double free, etc) apart from undefined behaviors. If this happens, your project will be considered non functional and will receive a 0 during the evaluation.
- We encourage you to create test programs for your project even though this work won't have to be submitted and won't be graded. It will give you a chance to easily test your work and your peers' work. You will find those tests especially useful during your defence. Indeed, during defence, you are free to use your tests and/or the tests of the peer you are evaluating.
- Submit your work to your assigned git repository. Only the work in the git repository will be graded. If Deepthought is assigned to grade your work, it will be done after your peer-evaluations. If an error happens in any section of your work during Deepthought's grading, the evaluation will stop.
- By Odin, by Thor! Use your brain!!!

## Chapter II
### Introduction

ETL, which stands for extract, transform and load, is a data integration process that combines data from multiple data sources into a single, consistent data store that is loaded into a data warehouse.

> Be careful with this "piscine". Even if you manage to validate a module, you may be stuck later if you haven't cleaned up or stored your data properly.

## Chapter III
### Exercise 00

**Exercise 00: Show me your DB**

Turn-in directory: `ex00/`

Files to turn in: 

Allowed functions: pgadmin, Postico, dbeaver or what you want to see the db easily

- Find a way to see the db easily with a software
- The software chosen must be easy to file and to use for the search of an ID

## Chapter IV
### Exercise 01

**Exercise 01: customers table**

Turn-in directory: `ex01/`

Files to turn in: `customers_table.*`

Allowed functions: All

- You have to join all the `data_202*_***` tables together in a table called "customers"

## Chapter V
### Exercise 02

**Exercise 02: remove duplicates**

Turn-in directory: `ex02/`

Files to turn in: `remove_duplicates.*`

Allowed functions: All

- You must delete the duplicate rows in the "customers" table.

> Sometimes the server sends the same instruction with 1 second interval, so you must also remove them

For example:

| event_time           | event_type       | product_id |
|----------------------|-------------------|------------|
| 2022-10-01 00:00:32  | remove_from_cart  | 5779403    |
| 2022-10-01 00:00:33  | remove_from_cart  | 5779403    |

## Chapter VI
### Exercise 03

**Exercise 03: fusion**

Turn-in directory: `ex03/`

Files to turn in: `fusion.*`

Allowed functions: All

- You must combine the "customers" tables with "items" in the "customers" table
- Be careful not to lose any information

## Chapter VII
### Submission and peer-evaluation

Turn in your assignment in your Git repository as usual. Only the work inside your repository will be evaluated during the defense. Don't hesitate to double check the names of your folders and files to ensure they are correct.

> The evaluation process will happen on the computer of the evaluated group.
