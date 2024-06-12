---
layout: post
title: ZODB Schema
date: 2024-06-05
---

# ZODB Schema for db4e

The diagram shows the node names in the backend ZODB storage. B-Trees are used as
container objects.

<pre class="mermaid">    
  classDiagram
    note "ZODB Schema for the db4e application"
    Db4eRoot o-- Reports
    Db4eRoot o-- History
    Db4eRoot o-- Mining
    
    Reports o-- Report
    
    Mining o-- P2Pool
    Mining o-- Wallets

    Wallets o-- Wallet

    P2Pool o-- Miners
    Miners o-- Miner
    P2Pool o-- Wallet
    P2Pool o-- History
        
    Report o-- History
    Wallet o-- History
    Miner o-- History
        
    History o-- XMRTransaction
    History o-- ShareTransaction
    History o-- ShareFoundEvent
    
    XMRTransaction o-- XMR
    note for History "All data values are contained by the History object"
</pre>
  
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'dark'});
</script> 

