from django import template
from ..models import Post, CATEGORY
from ..forms import Search
from _data.zenblog_contents import context
import re

register = template.Library()


@register.filter
def get_category_display(value):
    # 카테고리의 숫자값이 아닌 문자열을 템플릿에서 사용하기 위해 템플릿태그를 만들어 사용한다.
    # https://stackoverflow.com/questions/1333189/django-template-system-calling-a-function-inside-a-model
    return value.get_category_display()


@register.filter
def remove_html_tags(value):
    return re.sub('(<([^>]+)>)', '', value)


@register.inclusion_tag('zenblog/index/_hero_slider.html')
def show_hero_slider():
    return {
        'remarkables': Post.objects.filter(status=1).filter(remarkable=True).order_by('-updated_on')
    }


@register.inclusion_tag('zenblog/index/_post_grid.html')
def show_post_grid():
    # the_others는 6개만 뽑는다.
    return {
        'latest_one': Post.objects.filter(status=1).latest('updated_on'),
        'the_others': Post.objects.filter(status=1).order_by('-updated_on')[1:7],
        'trending': Post.objects.filter(status=1).order_by('hit_count_generic')[:5],
    }


@register.inclusion_tag('zenblog/index/_category-pattern0.html')
def show_category_pattern0(category_int):
    objects = Post.objects.filter(status=1).filter(category=category_int).order_by('-updated_on')
    return {
        'top4': objects[:4],
        'the_others': objects[4:10]
    }


@register.inclusion_tag('zenblog/index/_category-pattern1.html')
def show_category_pattern1(category_int):
    objects = Post.objects.filter(status=1).filter(category=category_int).order_by('-updated_on')
    return {
        'top4': objects[:4],
        'the_others': objects[4:10]
    }


@register.inclusion_tag('zenblog/index/_category-pattern2.html')
def show_category_pattern2(category_int):
    objects = Post.objects.filter(status=1).filter(category=category_int).order_by('-updated_on')
    return {
        'top3': objects[:3],
        'the_others1': objects[3:6],
        'the_others2': objects[6:9],
        'the_others3': objects[9:15],
    }


@register.inclusion_tag('zenblog/_sidebar.html')
def show_sidebar():
    from taggit.models import Tag
    tags = Tag.objects.all()
    print(tags)
    return {
        'category': CATEGORY,
        'all_tags': tags,
        'latest': Post.objects.filter(status=1).order_by('-updated_on')[:6],
        'trending': Post.objects.filter(status=1).order_by('hit_count_generic')[:6],
    }


@register.inclusion_tag('zenblog/base/_header.html')
def show_header():
    try:
        latest_one = Post.objects.filter(status=1).latest('updated_on')
    except Post.DoesNotExist:
        from django.contrib.auth.models import User
        u = User.objects.all()[0]
        p = Post(
            title="test",
            slug="test",
            author=u,
            content="test",
            status=1
        )
        p.save()
        latest_one = p
    return {
        'category': CATEGORY,
        'latest_one': latest_one,
        'form': Search(),
        'menu': context['menu'],
        'clinic_link': context['clinic_link'],
        'blog_name': context['blog_name'],
    }


@register.inclusion_tag('zenblog/base/_footer.html')
def show_footer():
    return {
        'category': CATEGORY,
        'latest_one': Post.objects.filter(status=1).latest('updated_on'),
        'latest': Post.objects.filter(status=1).order_by('-updated_on')[:4],
        'menu': context['menu'],
        'clinic_link': context['clinic_link'],
        'blog_name': context['blog_name'],
        'footer_about': context['footer']['about'],
    }


@register.inclusion_tag('zenblog/base/_seo.html')
def show_seo():
    return {
        'seo': context['seo'],
        # _variables.scss 에서 한글 폰트를 추가해주고 여기에 적절한 폰트 링크를 적용한다.
        'font_link': "https://fonts.googleapis.com/css2?family=EB+Garamond:wght@400;500"
                     "&family=Inter:wght@400;500"
                     "&family=Hahmlet:wght@100;200;300;400;500;600;700;800;900&"
                     "&family=Noto+Sans+KR:wght@100;300;400;500;700;900&"
                     "&family=Noto+Serif+KR:wght@200;300;400;500;600;700;900&"
                     "&family=Playfair+Display:ital,wght@0,400;0,700;1,400;1,700&display=swap"
    }
