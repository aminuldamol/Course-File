from viewPanel import views
from django.urls import path


urlpatterns = [
    path('', views.homePage),
    path('home/', views.homePage),
    path('about/', views.aboutPage),
    path('blog/', views.blogPage),
    path('profile/', views.profilePage),
    path('blog_details/<int:id>', views.blogDetailsPage),
    path('contact/', views.contactPage),
    path('course/', views.coursePage),
    path('details_course/', views.course_detailsPage),
    path('login/', views.loginPage),
    path('register/', views.registerPage),
 ]
