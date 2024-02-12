## BLOCK SAMPLE
2e3da8fbc1eaca8ed9b7c2db9e6545d8ccac3c67deadee95db050e41c1eedfc0
6eb38fad135e38a93cb47a15a5f953cbc0563fd84bf1abdec578c2af302e10bf
79c51c9d4124c5cbb37a85263748dcf44e182dff83561fa3087f0e9e43f41c33
8c25f9be93990b96e8bc363778d6debee6867c7d73cefab69405d41e677b536c


## BLOCK CONSTRUCTOR
This task will give you a chance to showcase your abilities and give us a sense of how you approach problems and write code. The challenge is open-ended and allows for multiple approaches.

# The problem

Bitcoin miners construct blocks by selecting a set of transactions from their mempool. Each transaction in the mempool:

includes a fee which is collected by the miner if that transaction is included in a block
has a weight, which indicates the size of the transaction
may have one or more parent transactions which are also in the mempool


The miner selects an ordered list of transactions that have a combined weight below the maximum block weight. Transactions with parent transactions in the mempool may be included in the list, but only if all of their parents appear before them in the list.

Naturally, the miner would like to include the transactions that maximize the total fee.

Your task is to write a program that reads a file mempool.csv, with the format:

```<txid>,<fee>,<weight>,<parent_txids>```

`txid` is the transaction identifier
`fee` is the transaction fee
`weight` is the transaction weight
`parent_txids` is a list of the txids of the transaction’s immediate parent transactions in the mempool. Ancestors that are not immediate parents (eg parents of parents) and parent transactions already in the chain are not included in this list. It is of the form: `<txid1>;<txid2>;...`


The output from the program should be txids, separated by newlines, which make a valid block, maximizing the fee to the miner. Transactions MUST appear in order. No transaction should appear unless its parents are included, no transaction should appear before its parents, and no transaction may appear more than once.

We've included a `BLOCK_SAMPLE` at the top of this document which you can put in a txt file to demonstrate the expected format.
The mempool transactions are included in this CSV file which you should download and use in your code.

Input file
Here are two lines of the mempool.csv file:
First transaction:
```2e3da8fbc1eaca8ed9b7c2db9e6545d8ccac3c67deadee95db050e41c1eedfc0,452,1620,```

This is a transaction with txid “2e3da8…”, fees of 452 satoshis, weight of 1620, and no parent transactions in the mempool.

```9d317fb308fd5451fd0ec612165638cb9e37bd8aa8918dff99a48fe05224276f,350,1400,288ea91bb52d8cb28289f4db0d857356622e39e78f33f26bf6df2bbdd3810fad;b5b993bda3c23bdefe4a1cf75b1f7cbdfe43058f2e4e7e25898f449375bb685c;c1ae3a82e52066b670e43116e7bfbcb6fa0abe16088f920060fa41e09715db7d```


This is a transaction with txid “9d317f…”, fees of 350 satoshis, weight of 1400 and three parent transactions in the mempool with txids “288ea9....”, “b5b993…” and “c1ae3a…”


Programming Language Choice

You can do this in any programming language of your choosing. The only dependency you will need is the mempool.csv file.

Hints

The total weight of transactions in a block must not exceed 4,000,000 weight. For this exercise assume that there is no coinbase transaction.
A transaction may only appear in a block if all of its parents appear earlier in the block.
A transaction must not appear more than once in the block.
A transaction may have zero, one, or many parents in the mempool. It may also have zero, one, or many children in the mempool.

General advice

First, make a naive solution that constructs a valid block, then iterate to improve it.
You should be able to explain your reasoning, design decisions, and trade-offs.
You should write the solution. If you use any external code in your solution, it must be attributed.


