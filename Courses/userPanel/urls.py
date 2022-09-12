from userPanel import views
from django.urls import path


urlpatterns = [
    path('panel/', views.Dashboard),
    path('dashboard/', views.Dashboard),

    path('set_slider/', views.setSlider),
    path('view_slider/', views.viewSlider),
    path('update_slider/<id>', views.updateSlider),
    path('del_slider/<id>', views.delSlider),

    path('set_found/', views.setFound),
    path('view_found/', views.viewFound),
    path('update_found/<id>', views.updateFound),
    path('del_found/<id>', views.delFound),

    path('set_feature/', views.setFeature),
    path('view_feature/', views.viewFeature),
    path('update_feature/<id>', views.updateFeature),
    path('del_feature/<id>', views.delFeature),

    path('set_tips/', views.setTips),
    path('view_tips/', views.viewTips),
    path('update_tips/<id>', views.updateTips),
    path('del_tips/<id>', views.delTips),

    path('set_subject/', views.setSubject),
    path('view_subject/', views.viewSubject),
    path('update_subject/<id>', views.updateSubject),
    path('del_subject/<id>', views.delSubject),

    path('set_community/', views.setCommunity),
    path('view_community/', views.viewCommunity),
    path('update_community/<id>', views.updateCommunity),
    path('del_community/<id>', views.delCommunity),

    path('set_guideline/', views.setGuideline),
    path('view_guideline/', views.viewGuideline),
    path('update_guideline/<id>', views.updateGuideline),
    path('del_guideline/<id>', views.delGuideline),

    path('set_blog/', views.setBlog),
    path('view_blog/', views.viewBlog),
    path('update_blog/<id>', views.updateBlog),
    path('del_blog/<id>', views.delBlog),

    path('set_contact/', views.setContact),
    path('view_contact/', views.viewContact),
    path('update_contact/<id>', views.updateContact),
    path('del_contact/<id>', views.delContact),
]
