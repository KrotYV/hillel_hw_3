from .models import LogModel


def LogMiddleware(get_response):
    def middleware(request):
        response = get_response(request)
        log_method = request.method
        log_path = request.path
        request_log = LogModel(path=log_path, method=log_method)
        if log_path != '/admin/':
            request_log.save()
        return response

    return middleware
