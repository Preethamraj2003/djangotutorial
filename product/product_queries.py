# 1. Give the detils of parivular category id
Product.objects.filter(id='5').values()

# Based on name dispay products
Product.objects.select_related('category').filter(category__name='cname8').values()

# list all sub-categories under a category
Category.objects.filter(parent_cat_id_id='4').values('parent_cat_id_id', 'id', 'name')

# list all sub categories  under a list of categories
Category.objects.filter(parent_cat_id_id__in=['4', '1']).values('parent_cat_id_id', 'id', 'name')

# list all sub_category under a category(based on name)
Category.objects.filter(parent_cat_id_id__name='cname1').values('id')