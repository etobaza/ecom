from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import (
    UserViewSet,
    ProductViewSet,
    OrderViewSet,
    CartItemViewSet,
    OrderItemViewSet,
    ShoppingCartViewSet,
    CategoryViewSet,
    PaymentViewSet,
    ReviewViewSet,
    WishlistViewSet,
    WishlistItemViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('orders', OrderViewSet)
router.register('order-items', OrderItemViewSet)
router.register('shopping-carts', ShoppingCartViewSet)
router.register('cart-items', CartItemViewSet)
router.register('payments', PaymentViewSet)
router.register('reviews', ReviewViewSet)
router.register('wishlists', WishlistViewSet)
router.register('wishlist-items', WishlistItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
