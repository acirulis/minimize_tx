# Minimize number of transactions between group of people

Small research project trying to solve simple sounding problem:

> Given a list of debts between pairs of people, minimize the number of transactions needed to clear all debts.

As it soon turns out this is [NP-hard](https://en.wikipedia.org/wiki/NP-hardness) problem without simple solution.

Some links researched:

1. https://hackernoon.com/adventures-in-programming-interviews-misleadingly-difficult-np-hard-problem-43092597018c (explanation, why it's NP-hard)
2. https://miguelbiron.github.io/2018/02/17/demo-for-simple-payments-with-linear-programming/ (clever approach using Linear Programming but not optimal for all cases)
3. https://stackoverflow.com/questions/877728/what-algorithm-to-use-to-determine-minimum-number-of-actions-required-to-get-the (general Stack Overflow discussion)



Example: 

1. Payments between group of people:
   1. Person A paid 0€ for everybody
   2. Person B paid 4€ for everybody
   3. Person C paid 8€ for everybody
   4. Extra: Person A paid 2€ for Person B (Adjusted spend)
2. Calculate average spent amount for group: (8+4+0) / 3 = 4€
3. Calculate adjusted spend (1.4)
4. Calculate individual balance:

| Person   | Spent for Group | Average spend | Adjusted spend | Individual balance |
| -------- | --------------- | ------------- | -------------- | ------------------ |
| Person A | 0€              | 4€            | 2€             | -2€                |
| Person B | 4€              | 4€            | 6€             | -2€                |
| Person C | 8€              | 4€            | 4€             | 4€                 |

As you can see, individual balance sums up to 0€ (it always must!) and minimal number of transaction can be found to settle between persons.

