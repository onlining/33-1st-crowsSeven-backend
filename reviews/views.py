import json

from django.views       import View
from django.http        import JsonResponse
from django.db.models   import Q

from reviews.models     import Review

class ReviewSearchView(View):
    def get(self, request):
        try:
            days         = request.GET.get('days')
            type         = request.GET.get('type', None)
            type_keyword = request.GET.get('q', None)

            search_keyword = Q()
            search_time_keyword = {
                "일주일" : 7,
                "한달"  : 5,
                "세달"  : 3,
            }

            if days in search_time_keyword:
                q &= Q(created_at__gte = datetime.datetime.now() - datetime.timedelta(minutes=int(search_time_keyword)))
            
            search_dict = {
                "title"  : "title__icontains",
                "content": "context__icontains",
                "author" : "user__name__icontains",
                "id"     : "user__id__icontains",
                "product": "product__name__icontains",
            }

            search_filter = {search_dict[search_type] : search_type_keyword} if search_type_keyword and search_type else {}

            searched_reviews = Review.objects.filter(q, **search_filter).distinct()

            review_list =[{
                "review_id"        : review.id,
                "review_product"   : review.product.name,
                "review_title"     : review.title,
                "review_thumb_nail": review.product.thumbnail_image_url,
                "review_name"      : review.user.username,
                "review_date"      : review.updated_at,
                "review_view_count": review.view_count
            } for review in searched_reviews]

            return JsonResponse({"message" : review_list}, status=200)

        except KeyError :
            return JsonResponse({"message" : "KEY_ERROR"}, status=400)