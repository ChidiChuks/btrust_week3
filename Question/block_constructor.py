import csv
from collections import defaultdict

class Transaction:
    def __init__(self, txid, fee, weight, parents):
        self.txid = txid
        self.fee = int(fee)
        self.weight = int(weight)
        self.parents = parents.split(';') if parents else []

def parse_mempool_csv(file_path):
    transactions = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            txid, fee, weight, parents = row
            transactions[txid] = Transaction(txid, fee, weight, parents)
    return transactions

def create_graph(transactions):
    graph = defaultdict(list)
    for txid, transaction in transactions.items():
        for parent in transaction.parents:
            graph[parent].append(txid)
    return graph

def select_transactions(graph, transactions, remaining_weight):
    selected_txs = []
    visited = set()

    def dfs(txid):
        if txid in visited:
            return
        visited.add(txid)
        transaction = transactions[txid]
        if all(parent in selected_txs for parent in transaction.parents):
            if transaction.weight <= remaining_weight:
                selected_txs.append(txid)
                remaining_weight -= transaction.weight
        for child in graph[txid]:
            dfs(child)

    for txid in graph:
        dfs(txid)

    return selected_txs

def main():
    mempool_file = 'mempool.csv'
    transactions = parse_mempool_csv(mempool_file)
    graph = create_graph(transactions)
    selected_txs = select_transactions(graph, transactions, 4000000)

    total_fee = sum(transactions[txid].fee for txid in selected_txs)
    print(f"Total fee: {total_fee}")

    with open('block.txt', 'w') as f:
        for txid in selected_txs:
            f.write(txid + '\n')

if __name__ == "__main__":
    main()

