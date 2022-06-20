from typing import Any

from django.http import JsonResponse
from django.views.generic import DetailView, ListView
from movies.models import FilmWork


class MoviesApiMixin:
    model = FilmWork
    http_method_names: list[str] = ('get',)

    def get_queryset(self):
        return FilmWork.objects.all()

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, ListView):
    paginate_by: int = 50

    def get_context_data(self, object_list=None, *args, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset=queryset, page_size=self.paginate_by)

        return {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(page.object_list),
        }


class MoviesDetailApi(MoviesApiMixin, DetailView):
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        return {}
