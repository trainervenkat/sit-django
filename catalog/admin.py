from django.contrib import admin
from catalog.models import Book,Genre,Author

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields = ('id','name')
    fields = [('name','purchase_date'),('genre','author')]
    # note : RelatedOnlyFieldListFilter=> applicable when some fields are related to other tables
    list_filter = ('name','purchase_date',('author',admin.RelatedOnlyFieldListFilter))
    
    # list_filter = ('name','purchase_date','author')
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
    
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass
