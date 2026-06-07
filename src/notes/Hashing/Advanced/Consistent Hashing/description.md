# Consistent Hashing

**Consistent Hashing** is a distributed hashing scheme that operates independently of the number of servers or objects in a distributed hash table. It minimizes the number of keys that need to be remapped when a hash table is resized (i.e., when servers are added or removed).

This is a massive topic in **System Design** and is widely used in distributed databases, caches, and load balancers.

## The Problem with Traditional Hashing
In a standard load balancer or distributed cache, you distribute requests (or data) across `N` servers using a simple modulo hash:
`server_index = hash(key) % N`

**The fatal flaw:** If a server crashes (so `N` becomes `N-1`), or if you need to scale up and add a server (so `N` becomes `N+1`), the modulo `N` changes.
Suddenly, `hash(key) % 4` is completely different from `hash(key) % 5`. 
This results in **almost all keys being rehashed and moved to different servers**, causing massive cache misses and bringing down the entire system (the "thundering herd" problem).

## How Consistent Hashing Works

Instead of hashing into an array of size `N`, Consistent Hashing hashes both the **keys** and the **servers** themselves onto an infinitely wrapping circle (a "hash ring").

### 1. The Hash Ring
Imagine a hash function (like SHA-1) that outputs values from `0` to `2^160 - 1`. We map this range onto a circle.

### 2. Hashing the Servers
We hash the IP address or ID of each server and place it on the ring.

### 3. Hashing the Data (Keys)
To figure out which server stores a particular piece of data (key), we hash the key to find its position on the ring. Then, we walk **clockwise** around the ring until we hit the first server. That server owns the data.

## Adding or Removing Servers

- **Adding a Server:** If we add Server D between Server A and Server B, only the keys that fall between A and D are reassigned to D. All other keys in the system stay exactly where they are.
- **Removing a Server:** If Server B crashes, only the keys that were stored on Server B need to be remapped. They are simply moved clockwise to the next available server (Server C).

*Result:* Instead of moving $O(K)$ keys (all of them), we only move $O(K / N)$ keys, where K is the number of keys and N is the number of servers. This is highly efficient.

## Virtual Nodes (V-Nodes)
**Problem:** In reality, randomly hashing 4 servers onto a massive ring usually results in a highly uneven distribution of data. One server might own 50% of the ring, while another owns 5%.
**Solution:** We use **Virtual Nodes**. Instead of placing Server A on the ring once, we place 100 "virtual" replicas of Server A on the ring (e.g., by hashing "ServerA_1", "ServerA_2", ..., "ServerA_100").
We do this for all servers. The ring becomes densely packed with thousands of interleaved virtual nodes, guaranteeing a near-perfectly uniform distribution of data across all physical servers.

## Real-World Usage
- **Amazon DynamoDB:** Data partitioning.
- **Memcached & Redis:** Distributed caching architectures.
- **Discord & Twitch:** Routing chat messages to specific stateful websocket servers.
