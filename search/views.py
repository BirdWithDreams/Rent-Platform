from django.shortcuts import render
from offers.models import Offers
from django.db.models import Q
import re
from django.contrib import messages


# Create your views here.
def search(request):
    if request.method == 'POST':
        tags = request.POST.get('tags', None)
        category = request.POST.get('category', None)
        min_price = request.POST.get('min_price', None)
        max_price = request.POST.get('max_price', None)

        search_params = {
            'tags': tags,
            'category': category,
            'min_price': min_price,
            'max_price': max_price,
        }

        messages = []
        filters = Q()

        if min_price is not '':
            min_price = float(min_price)
        else:
            min_price = 1

        if max_price is not '':
            max_price = float(max_price)
        else:
            max_price = 999999

        if min_price <= max_price:
            filters = filters & Q(price__gte=min_price, price__lte=max_price)
        else:
            messages.append('Min price can\'t be higher than max')

        if category is not '':
            filters = filters & Q(category__contains=category)

        offers = Offers.objects.filter(filters)

        filters = Q()
        if tags is not '':
            tag_list = re.split(', |; |\. |,|;|\.| ', tags.strip().lower())
            for tag in tag_list:
                filters = filters | Q(tags__contains=tag)

            offers = offers.filter(filters)

            offer_similarities = []

            for offer in offers:
                offer_tags = offer.tags.lower()
                print(offer_tags)
                similarity_count = sum(1 for el in tag_list if el in offer_tags)
                print(similarity_count)
                offer_similarities.append((offer, similarity_count))

            sorted_offers = sorted(offer_similarities, key=lambda x: x[1], reverse=True)

            print(sorted_offers)

            offers = [el for el, count in sorted_offers]

        return render(request, 'search.html', {'offers': offers, 'messages': messages, "search_params": search_params})

    return render(request, 'search.html', )
