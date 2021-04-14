from django.urls import path, reverse_lazy
from src.posts.views import posts as post_views
from src.posts.views import tags as tags_views

app_name = "posts"

urlpatterns = [
    path("", post_views.PostListView.as_view(), name="all"),
    path("post/<slug:slug>/", post_views.PostDetailView.as_view(), name="post_detail"),
    path(
        "post/create",
        post_views.PostCreateView.as_view(),
        name="create",
    ),
    path(
        "post/<slug:slug>/update",
        post_views.PostUpdateView.as_view(),
        name="post_update",
    ),
    path(
        "post/<slug:slug>/delete",
        post_views.PostDeleteView.as_view(),
        name="post_delete",
    ),
    path("post_picture/<slug:slug>", post_views.stream_file, name="post_picture"),
    path(
        "post/<slug:slug>/comment",
        post_views.CommentCreateView.as_view(),
        name="post_comment_create",
    ),
    path(
        "comment/<int:pk>/delete",
        post_views.CommentDeleteView.as_view(success_url=reverse_lazy("posts")),
        name="post_comment_delete",
    ),
    path(
        "post/<int:pk>/favorite",
        post_views.AddFavoriteView.as_view(),
        name="post_favorite",
    ),
    path(
        "post/<int:pk>/unfavorite",
        post_views.DeleteFavoriteView.as_view(),
        name="post_unfavorite",
    ),
    path(
        "tag/",
        tags_views.TagListView.as_view(),
        name="tag_list",
    ),
    path("tag-creation/", tags_views.tag_creation_view, name="tag_create"),
    # path(
    #     "validate-tag-edit-or-update/<int:pk>/<slug:action>/",
    #     validate_update_or_delete_tag_view,
    #     name="validate_tag_edit_or_update",
    # ),
    # path("ajax-update/tag/<int:pk>/", ajax_update_tag_view, name="ajax_update_tag"),
]
