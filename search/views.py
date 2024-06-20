from django.shortcuts import render, redirect

from offers.models import Offers
from django.db.models import Q
import re


# TODO: Contract page with new model
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

        if min_price != '':
            min_price = float(min_price)
        else:
            min_price = 1

        if max_price != '':
            max_price = float(max_price)
        else:
            max_price = 999999

        if min_price <= max_price:
            filters = filters & Q(price__gte=min_price, price__lte=max_price)
        else:
            messages.append('Min price can\'t be higher than max')

        if category != '':
            filters = filters & Q(category__contains=category)

        offers = Offers.objects.filter(filters)

        filters = Q()
        if tags != '':
            tag_list = re.split(', |; |\. |,|;|\.| ', tags.strip().lower())
            for tag in tag_list:
                filters = filters | Q(tags__contains=tag)

            offers = offers.filter(filters)

            offer_similarities = []

            for offer in offers:
                offer_tags = offer.tags.lower()
                similarity_count = sum(1 for el in tag_list if el in offer_tags)
                offer_similarities.append((offer, similarity_count))

            sorted_offers = sorted(offer_similarities, key=lambda x: x[1], reverse=True)

            offers = [el for el, count in sorted_offers]

        return render(request, 'search.html', {'offers': offers, 'messages': messages, "search_params": search_params})

    return render(request, 'search.html', )


def search_offer(request, offer):
    offer = Offers.objects.get(id=offer)
    return render(request, 'search-offer.html', {'offer': offer, 'seller': offer.user_id})
