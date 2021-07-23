from articles.models import Article
from django.contrib import admin
from .models import Article, Comments
# Register your models here.


admin.site.register(Comments)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","created_date"]

    list_display_links =["title","created_date"]
    
    search_fields = ["title"]

    list_filter = ["created_date"]

    class Meta:
        model = Article