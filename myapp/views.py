from django.shortcuts import render
from django.views.generic import ListView ,DetailView ,CreateView , UpdateView ,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Article

# Create your views here.

# HOME
def home(request):
    return render(request, 'myapp/home.html', {'title': 'Личный блог ItologJS'})


# BLOG
# def blog(request):
#     data = {
#         "title": 'Home',
#         "news": Article.objects.all()
#     }
#     return render(request, 'myapp/blog.html', data)

# BlogView
class BlogNewsView(ListView):
    model = Article
    template_name = 'myapp/blog.html'
    context_object_name = 'news'
    # queryset = Article.objects.all()
    ordering = ['-id']
    paginate_by = 5

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(BlogNewsView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['title'] = "Статьи IT"
        return context


# DETAIL
class BlogDetailView(DetailView):
    model = Article
    template_name = 'myapp/blog_detail.html'

    def get_context_data(self, **kwards):
        # Call the base implementation first to get a context
        context = super(BlogDetailView, self).get_context_data(**kwards)
        # Add in the publisher
        context['title'] = Article.objects.filter(pk=self.kwargs['pk']).first()
        return context


# Create Article
class CreateNews(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'href']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


#  Update Article
class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        name = self.get_object()
        if self.request.user == name.user:
            return True
        else:
            return False

#  Delete Article
class DelNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    success_url = '/'

    def test_func(self):
        name = self.get_object()
        if self.request.user == name.user:
            return True
        else:
            return False

# CONTACT
def contact(request):
    data = {
        "title": "contact"
    }
    return render(request, 'myapp/contact.html', data)
