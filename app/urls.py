from django.urls import path
from .views import IndexView, IndexImportView, YuklamalarView, UzSentTokenizationView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('yuklamalar/', YuklamalarView.as_view(), name='yuklamalar'),
    path('yuklamalar/<int:id>/', YuklamalarView.as_view(), name='yuklamalar-delete'),
    path('uzsenttokenization/', UzSentTokenizationView.as_view(), name='uzsenttokenization'),
    path('uzsenttokenization/<int:id>/', UzSentTokenizationView.as_view(), name='uzsenttokenization-delete'),
    path('import/', IndexImportView.as_view(), name='import'),
]
