---
layout: post
title: MyZODB Class Hierarchy
date: 2024-06-02
---

# Class Diagram
<pre class="mermaid">
    classDiagram
    note "MyZODB Classes"
    persistent.Persistent <|-- MyZODBRoot
    MyZODBRoot <|-- XMR
    MyZODBRoot <|-- Transaction
    Transaction <|-- ShareTransaction
    Transaction <|-- XMRTransaction
    MyZODBRoot <|-- Miner
    MyZODBRoot <|-- Wallet
    MyZODBRoot <|-- P2Pool
    MyZODBRoot <|-- P2PoolDaemon
    MyZODBRoot <|-- Chart
    MyZODBRoot <|-- MyZODB
    class MyZODBRoot{
        db (ZODB.DB)
        get_root()
        set_root()
        update()
        __str__()
    }
    class XMR{
        amount
    }
    class Transaction{
        to (anObject) 
        from (anObject)
        amount (float)
        timestamp (datetime)
    }
    class ShareTransaction{
        miner (Miner)
        effort (float)
        difficulty (float)
    }
    class Chart{
        csv_file (string)
        read_csv()
        write_csv()
    }
    class Miner{
        hostname (string)
        accept_share()
        blockfound()
    }
    class Wallet{
        balance (float)
        transactions (XMRTransactions)
        accept_trans(XNRTransaction)
    }
    class P2Pool{
        send_trans(Transaction)
    }
    class P2PoolDaemon{
        miners (Miners)
        logfile (string)
        monitor_log()
    }
</pre>
  
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'dark'});
</script> 

