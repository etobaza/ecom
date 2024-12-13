# Distributed Systems and Data Consistency

This document describes the distributed architecture used for managing data replication and maintaining consistency across multiple nodes.

---

### PostgreSQL Cluster Setup

In the PostgreSQL distributed system, data replication and consistency are configured using the settings outlined below:

### Data Replication Strategies

- Master-Slave Replication: All write operations are performed on the master, with updates propagated to slave nodes.
- Multi-Master Replication: Multiple masters handle write operations, and synchronization ensures data consistency.
- CRDT (Conflict-free Replicated Data Types): Used to achieve eventual consistency across different nodes.

## Consistency Models

- Strong Consistency: Ensures all nodes are synchronized and transactions comply with ACID properties.
- Eventual Consistency: Systems gradually reach a consistent state over time.
- Linearizability: A robust consistency model that ensures a globally accepted state.
