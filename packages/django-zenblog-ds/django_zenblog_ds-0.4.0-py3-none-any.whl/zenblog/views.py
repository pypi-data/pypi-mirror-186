import re
from django.shortcuts import render
from .models import Post, CATEGORY
from django.views import generic
from hitcount.views import HitCountDetailView
from _data import zenblog_contents
from .forms import Search
from util_demian import utils

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.INFO)

num_pagination = 7


def robots(request):
    from django.shortcuts import HttpResponse
    file_content = utils.make_robots()
    return HttpResponse(file_content, content_type="text/plain")


def home(request):
    """
    모델의 CATEGORY를 context에 전달하면 category_pattern.html을 할당하여 보여준다.
    """
    c = zenblog_contents.context
    c['category'] = CATEGORY
    logger.info(c)
    return render(request, 'zenblog/index.html', c)


def about(request):
    c = blog.context
    logger.info(c)
    return render(request, 'zenblog/about.html', c)


def contact(request):
    c = blog.context
    return render(request, 'zenblog/contact.html', c)


class Category(generic.ListView):
    template_name = 'zenblog/category.html'
    paginate_by = num_pagination

    def get_queryset(self):
        return Post.objects.filter(status=1).filter(category=self.kwargs['category_int']).order_by('-updated_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pages_devided = make_page_bundle(context['paginator'].page_range)

        # 현재 페이지에 해당하는 묶음을 page_bundle로 전달한다.
        for page_bundle in pages_devided:
            if context['page_obj'].number in page_bundle:
                context['page_bundle'] = page_bundle

        context.update({
            'category': CATEGORY[self.kwargs['category_int']][1],
        })
        return context


class SearchResult(generic.ListView):
    template_name = 'zenblog/search-result.html'
    paginate_by = num_pagination

    def get_queryset(self):
        form = Search(self.request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
        else:
            q = ''
        return Post.objects.filter(content__contains='' if q is None else q).filter(status=1).order_by('-updated_on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pages_devided = make_page_bundle(context['paginator'].page_range)

        # 현재 페이지에 해당하는 묶음을 page_bundle로 전달한다.
        for page_bundle in pages_devided:
            if context['page_obj'].number in page_bundle:
                context['page_bundle'] = page_bundle

        return context


class SearchTag(SearchResult):
    def get_queryset(self):
        # https://stackoverflow.com/questions/56067365/how-to-filter-posts-by-tags-using-django-taggit-in-django
        return Post.objects.filter(tags__name__in=[self.kwargs['tag']]).filter(status=1).order_by('-updated_on')


class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'zenblog/single-post.html'
    context_object_name = 'object'
    slug_field = 'slug'
    count_hit = True

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['object'].content = adjust_html_tags(context['object'].content)
        logger.info(context['object'].content)
        return context


def adjust_html_tags(origin: str) -> str:
    """
    summernote로 입력받은 컨텐츠에는 부적합한 태그 있다.
    1. 글의 첫글자를 크게 하기 위해서 firstcharacter 클래스를 적용한다.
    2. img 태그 내부에 class="img-fluid"를 넣는다.
    3. img 태그 전후의 불필요한 p 태그를 삭제한다.
    4. img 태크 전후에 figure 태그를 삽입한다.
    5. 코드 블록을 표시하기 위해 <pre class=""></pre>를 <div class="callout">...</div>으로 고친다.
    """

    # 1. 글의 첫글자를 크게 하기 위해서 firstcharacter 클래스를 적용한다.
    index = origin.find('<p>')
    print(index)
    if origin.startswith('<p>'):
        if origin[3:4] == '<':
            # 블로그 글이 글자가 없이 그림으로 시작되는 경우는 에러를 막기 위해 수정하지 않는다.
            new_str = origin
        else:
            # 일반적인 경우...
            new_str = origin[:3] + '<span class="firstcharacter">' + origin[3:4] + '</span>' + origin[4:]
    else:
        # 블로그 글의 시작이 <p>로 시작하지 않는 경우
        new_str = '<span class="firstcharacter">' + origin[0] + '</span>' + origin[1:]

    # 2. img 태그 내부에 class="img-fluid"를 넣는다.
    # 정규표현식으로 패턴의 위치를 찾아 문자열을 삽입하며 삽입할때마다 문자열의 길이가 길어지기 때문에 그만큼 인덱스를 더해준다.
    pattern = "<img"
    inserted_str = ' class="img-fluid"'
    for i, match in enumerate(re.finditer(pattern, new_str)):
        new_str = new_str[:match.end()+(len(inserted_str)*i)] + inserted_str + new_str[match.end()+(len(inserted_str)*i):]

    # 3. img 태그 전후의 불필요한 p 태그를 삭제한다.
    # 명명 그룹을 사용하는벱 -
    # https://greeksharifa.github.io/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re)/2018/08/04/regex-usage-05-intermediate/
    pattern = "<p><img(?P<image_tags>.*?)>.*?</p>"
    new_str = re.sub(pattern, r"<img\g<image_tags>>", new_str)

    # 4. img 태크 전후에 figure 태그를 삽입한다.
    inserted_str_1 = '<figure class="my-4">'
    for i, match in enumerate(re.finditer(pattern, new_str)):
        new_str = new_str[:match.start()+(len(inserted_str_1)*i)] + inserted_str_1 + new_str[match.start()+(len(inserted_str_1)*i):]
    inserted_str_2 = '</figure>'
    for i, match in enumerate(re.finditer(pattern, new_str)):
        new_str = new_str[:match.end()+(len(inserted_str_2)*i)] + inserted_str_2 + new_str[match.end()+(len(inserted_str_2)*i):]

    # 5. 코드 블록을 표시하기 위해 <pre class=""></pre>를 <div class="callout">...</div>으로 고친다.
    origin_n_target_tags = [
        ['<pre class="">', '<div class="alert alert-secondary" role="alert">'],
        ["</pre>", "</div>"]
    ]
    for origin, target in origin_n_target_tags:
        new_str = re.sub(origin, target, new_str)
    return new_str


def make_page_bundle(page_range, n=5):
    # 전체 페이지를 n 개수의 묶음으로 만든다.
    # pagination에 사용
    l = [i for i in page_range]
    return [l[i:i + n] for i in range(0, len(l), n)]
