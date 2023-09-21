from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect

class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info == '/login/':
            return
        info_dict = request.session.get('info')
        print("process_request", info_dict)
        if info_dict:
            request.info_dict = info_dict
            return

        return redirect('/login/')

    # def process_response(self, request, response):
    #     print("process_response")
    #     return response