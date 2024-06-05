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
    PROD o-- Wallet
    PROD o-- P2Pool
    PROD o-- History
    PROD o-- Chart
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

