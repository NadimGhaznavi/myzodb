---
layout: post
title: MyZODB Class Hierarchy
date: 2024-06-02
---

# Class Diagram
<pre class="mermaid">
    classDiagram
    note "MyZODB Classes"
    MyZODBRoot <|-- XMR
    MyZODBRoot <|-- Transaction
    Transaction <|-- ShareTransaction
    Transaction <|-- XMRTransaction
    MyZODBRoot <|-- Miner
    MyZODBRoot <|-- Wallet
    MyZODBRoot <|-- P2PoolDaemon
    MyZODBRoot <|-- Chart
    MyZODBRoot <|-- MyZODB
    MyZODBROOT <|-- History
    Miner --o History
    History --o XMRTransaction
    History --o ShareTransaction
    XMRTransaction --o XMR
    Wallet --o XMRTransaction

    class Chart{
        csv_file (string)
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
    class MyZODBRoot{
        +ZODB.DB db
        get_root()
        set_root(MyZODBRoot)
        update()
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
        execute()
    }
    class Transaction{
        +String to
        +String from
        +XMR amount
        +DateTime timestamp
        execute()
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

