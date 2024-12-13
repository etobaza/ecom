# Asynchronous Processing with Celery

## Overview

This document explains how to set up asynchronous tasks for tasks such as sending order confirmation emails and processing payments using Celery.

## Prerequisites

1. Setup Redis with Docker-Compose
2. Install Celery

```python
CELERY_BROKER_URL = os.environ.get("REDIS_TASKS_URL")
CELERY_BEAT_SCHEDULE = {
    'send-order-confirmation-emails': {
        'task': 'myapp.tasks.send_order_confirmation_email',
        'schedule': 60.0,
    },
    'process-payments': {
        'task': 'myapp.tasks.process_payment',
        'schedule': 300.0,
    },
}
```

