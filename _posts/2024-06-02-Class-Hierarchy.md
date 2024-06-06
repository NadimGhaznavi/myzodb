---
layout: post
title: Class Hierarchy
date: 2024-06-02
---

# Class Diagram showing Inheritance

The chart below shows the inheritance structrue of the Db4e codebase.

<pre class="mermaid">
  classDiagram
    note "MyZODB Classes"
    Db4eRoot <|-- XMR
    Db4eRoot <|-- Miner
    Db4eRoot <|-- Wallet
    Db4eRoot <|-- P2PoolDaemon
    Db4eRoot <|-- Chart
    Db4eRoot <|-- History
    
    Db4eRoot <|-- Transaction
    Transaction <|-- ShareTransaction
    Transaction <|-- XMRTransaction
    
    Db4eRoot <|-- Db4eTree
    Db4eTree <|-- Wallets
    Db4eTree <|-- Miners
    Db4eTree <|-- P2Pools
    
    
    class Db4eTree{
      +B-Tree items
      add(item)
      get(item_key)
      remove(item)
      items()
    }

    class Chart{
      +String csv_file
      read_csv()
      write_csv()
    }
    class History{
      +ShareTransactions share_transaction
      +XMRTransactions xmr_transaction
      add_history()
      get_history()
    }
    class Miner{
      +String hostname
      +History history
      accept_share()
      blockfound()
    }
    class Db4eRoot{
      +ZODB.DB db
      get_root()
      set_root(self.db)
      commit()
      _setup_zodb(ZODB.DB)
      __str__()
    }
    class P2PoolDaemon{
      +Miners miners
      +String logfile
      monitor_log()
    }
    class ShareTransaction{
      +Miner miner
      +Float effort
      +Float difficulty
      +DateTime timestamp
    }
    class Transaction{
      +String to
      +String from
      +XMR amount
      +DateTime timestamp
    }
    class Wallet{
      +Float balance
      +XMRTransactions transactions
      receive(XMRTransaction)
    }
    class XMR{
      +Float amount
    }
    class XMRTransaction{
      +String to
      +String from
      +XMR amount
      +DateTime timestamp
      execute()
    }
</pre>
  
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'dark'});
</script> 

