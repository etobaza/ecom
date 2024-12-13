# Approaches to Scaling

---

### Cases for Sharding

1. **User Data**:

   - **Sharding Key**: User ID.
   - **Reasoning**: Distributes user records across multiple shards to prevent congestion on a single database instance.

2. **Order Data**:

   - **Sharding Key**: Order ID or User ID.
   - **Reasoning**: Order records can expand rapidly. Sharding ensures efficient read and write operations.

3. **Product Catalog**:
   - **Sharding Key**: Category ID.
   - **Reasoning**: Groups and distributes products within a category, enabling efficient category-based queries.

---

## Transitioning to Microservices

The microservices architecture breaks down a monolithic application into smaller, independently deployable services. This facilitates improved scalability, fault isolation, and greater development agility.

### Key Features to Transition

1. **Product Management**

   - **Service**: "Product Service"
   - **Responsibilities**:
     - Manage the product catalog (CRUD operations).
     - Handle product categorization and inventory updates.
   - **Technology**: Django REST Framework for APIs, supported by a scalable database.

2. **Order Processing**

   - **Service**: "Order Service"
   - **Responsibilities**:
     - Manage order creation, updates, and tracking.
     - Integrate with payment gateways.
   - **Technology**: FastAPI for lightweight performance and asynchronous capabilities.

3. **User Authentication**
   - **Service**: "Auth Service"
   - **Responsibilities**:
     - User registration and login.
     - Token-based authentication.
   - **Technology**: Django with built-in authentication modules.

### Architecture Plan

- **API Gateway**:

  - Serves as a unified entry point for clients, directing requests to the appropriate microservices.

- **Communication**:

  - REST APIs for synchronous interactions between services.

- **Database Strategy**:
  - Assign each service its own database to maintain clear data boundaries.

---

## Code Examples

```python
# Database sharding logic
class ShardRouter:
    def db_for_read(self, model, **hints):
        """Directs read operations to the appropriate shard."""
        if model._meta.app_label == 'orders':
            shard_key = hints.get('user_id') % NUM_SHARDS
            return f'shard_{shard_key}'
        return 'default'

    def db_for_write(self, model, **hints):
        """Directs write operations to the appropriate shard."""
        if model._meta.app_label == 'orders':
            shard_key = hints.get('user_id') % NUM_SHARDS
            return f'shard_{shard_key}'
        return 'default'
```

### Microservices Example (Product Service)

```python
from fastapi import FastAPI
from pydantic import BaseModel

   app = FastAPI()

   class Product(BaseModel):
      user_id: int
      product_ids: list[int]
      total_amount: float

   @app.post("/products/")
   async def create_product(product: Product):
      # Process product creation
      return {"message": "Product created successfully", "product": product.dict()}
```
