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
    Db4eRoot o-- Wallets
    Wallets o-- Wallet
    Db4eRoot o-- P2Pools
    P2Pools o-- P2Pool
    note for History "All data values are contained by the History object"
    Db4eRoot o-- Charts
    Charts o-- Chart
    Chart o-- History
    P2Pool o-- Miner
    P2Pool o-- Wallet
    Wallet o-- History
    Miner o-- History
    History o-- XMRTransaction
    History o-- ShareTransaction
    XMRTransaction o-- XMR
</pre>
  
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true, theme: 'dark'});
</script> 

