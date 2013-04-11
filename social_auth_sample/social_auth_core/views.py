from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self):
        context = super(LandingView, self).get_context_data()
        context['user'] = self.request.user
        return context


class LoginError(TemplateView):
    template_name = 'login_err.html'

    def get_context_data(self):
        return super(LoginError, self).get_context_data()