# RapidKing
homework_7_cs3030_personal

This assignment consists of two Tasks.

Task1:
Task1 has two modules.

Module 1 contains two functions:
  inputGet() is designed to utilize user input to test the variable values being passed to doorCheck() (the second function).
  -This is used as a way to test doorCheck() while it's being designed and built.
  
  doorCheck() is designed to take arguments and test the possible combinations to simulate switch possitions of a virtual minivan.
  -These switch combinations dictate which doors will open or close based on the input provided.
  -doorCheck performs error checking on a gearshift option that requires a certain set of input values.
  -doorCheck also has safety logic to ensure that the doors will stay closed on the event that the master unlock is not activated or if the care is thought to be in gear
  
Module 2 contains two functions:
  fileup() uses urlopen() to capture file content from "http//icarus.cs.weber.edu/~hvalle/cs3030/data/minivanTest.csv", decode it, and perform an initial cleaning of the data.
  
  list_prep() formats the data from fileup() into variables and then calls mod1.doorCheck to pass in the values it formated from fileup().
  - Once it passes the arguments in to doorCheck(), doorCheck performs the calculations and returns the results of the files provided values.


Task2:

