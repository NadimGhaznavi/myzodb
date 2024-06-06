---
layout: post
title: ZODB Schema
date: 2024-06-05
---

# ZODB Schema for db4e

The diagram shows the node names in the backend ZODB storage.

<pre class="mermaid">
  classDiagram
    note "ZODB Schema for db4e"
    db4e o-- PROD
    note for PROD "This container is the root ZODB object"
    PROD o-- Wallets
    note for Wallets "A container to hold Wallet objects"
    Wallets o-- Wallet
    PROD o-- P2Pools
    note for P2Pools "A container to hold P2Pool objects"
    P2Pools o-- P2Pool
    PROD o-- History
    note for History "All stored data is kept here"
    PROD o-- Charts
    note for Charts "A container to hold Chart objects"
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

