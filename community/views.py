from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Review
from .form import ReviewForm

def index(request):
    reviews = Review.objects.all().order_by('-id')
    paginator = Paginator(reviews, 5)
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    return render(request, 'community/review_list.html', {
        'reviews': reviews,
    })


def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            return redirect('community:index')
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'community/form.html', context)


## ID required ##
def detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.hits += 1
    review.save()
    return render(request, 'community/review_detail.html', {
        'review':review,
    })


@require_POST
def delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('community:index')


def update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('community:detail', review.pk)
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form
    }
    return render(request, 'community/form.html', context)