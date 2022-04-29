# CMPS 2200 Assignment 5

## Answers

**Name:** Ruoqin Ji

Place all written answers from `assignment-05.md` here for easier grading.

- **1a.**
  We can greeduily take the coin with the highest denomination until all money are exchanged.
  Since the money we need to exchange is fixed and the set of denomination is singualr (power of 2), greedy algorithm is optimal in this case.
- **1b.**
  Since we repeatily apply $\log_2(N)$ till $N=0$ which is a serial process, the work and span of this algorithm are both $O(\log n)$.
- **2a.**
  Counter example: We want to exchange for 10 dollars but the bank provides denominations of ${D_2, D_5}$.
  The greedy algorithm will take the highest denomination (i.e., $2^3$) first which results a total of three coins.
  However, the optimal solution should be two coins of $5^1$.
- **2b.**
  We can implement a bottom-up dynamic programming by filling up a table where its columns are elements in the set of denomination and rows are powers of each denomination. 
  The work is equal to the number of distinct subprpblems considered, which is all nodes of DAG, $O(n * k)$, where $n$ is the length of denomination set and $k$ is the highest power required to exchange money.
  The span is represented by the longest path in hte DAG, which is $O(n)$.
