from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user_profile', views.user_profile, name='user_profile'),
    path('filter_querries/<int:id>/', views.filter_querries, name='filter_querries'),
    path('querries/<int:id>/', views.QuerryView.as_view(), name='querries2'),
    path('querries/', views.QuerryView.as_view(), name='querries')
    # path('course', views.course, name='course'),
    # path('course/<int:course_id>', views.course_detail, name='course_detail'),
    # path('course/<int:course_id>/enroll', views.enroll, name='enroll'),
    # path('course/<int:course_id>/drop', views.drop, name='drop'),
    # path('course/<int:course_id>/add_review', views.add_review, name='add_review'),
    # path('course/<int:course_id>/review/<int:review_id>/delete', views.delete_review, name='delete_review'),
    # path('course/<int:course_id>/review/<int:review_id>/update', views.update_review, name='update_review'),
    # path('course/<int:course_id>/review/<int:review_id>/like', views.like_review, name='like_review'),
    # path('course/<int:course_id>/review/<int:review_id>/dislike', views.dislike_review, name='dislike_review'),
    # path('course/<int:course_id>/review/<int:review_id>/report', views.report_review, name='report_review'),
    # path('course/<int:course_id>/review/<int:review_id>/unreport', views.unreport_review, name='unreport_review'),
    # path('course/<int:course_id>/review/<int:review_id>/comment', views.add_comment, name='add_comment'),
    # path('course/<int:course_id>/review/<int:review_id>/comment/<int:comment_id>/delete', views.delete_comment, name='delete_comment'),
    # path('course/<int:course_id>/review/<int:review_id>/comment/<int:comment_id>/update', views.update_comment, name='update_comment'),
    # path('course/<int:course_id>/review/<int:review_id>/comment/<int:comment_id>/like', views.like_comment, name='like_comment'),
    # path('course/<int:course_id>/review/<int:review_id>/comment/<int:comment_id>/dislike', views.dislike_comment, name='dislike_comment'),
    # path('course/<int:course_id>/review/<int:review_id>/comment/<int:comment_id>/report', views.report_comment, name='report_comment'),
]