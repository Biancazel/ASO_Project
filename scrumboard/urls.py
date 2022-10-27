from scrumboard.api import CardViewSet, ListViewSet
from rest_framework.routers import DefaultRouter

"""
DefaultRouter class allows automatic routing of
ALL URLS for all operations on object from DB
ViewSet is mapped with Router below in code.
Finally, urlpatterns get applied
"""

router = DefaultRouter() # instead of urlpatterns list
router.register('lists', ListViewSet)
router.register('cards', CardViewSet)

# calling a bad URL shows a lot of URLS created automatically
urlpatterns = router.urls