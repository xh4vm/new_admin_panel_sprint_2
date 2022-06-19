from django.http import HttpRequest, JsonResponse
from django.views import View


class MoviesListApi(View):
    http_method_names: list[str] = ('get', )

    def get(self, request: HttpRequest, *args, **kwargs):
        return JsonResponse({'status': 'success'})
