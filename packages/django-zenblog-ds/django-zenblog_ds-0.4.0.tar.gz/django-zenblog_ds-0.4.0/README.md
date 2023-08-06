# django-zenblog_ds

django-zenblog_ds 는 zenblog-pro v1.1.0을 장고에 맞게 포팅한 장고앱이다.
django_non_dark_admin앱은 python3.9이상을 필요로하여 일단 비활성화 하였다.


> 프로젝트에 설치하기
> 1. zenblog 앱 및 필요앱을 프로젝트 settings.py 의 INSTALLED_APPS 에 추가한다.
> ```python
> import os
> INSTALLED_APPS = [
>     # django_non_dark_admin,
>     django.contrib.admin,
>     ...
>     'demian_parts',
>     'zenblog',
>     'compressor',         # scss 사용하기
>     'django_summernote',  # WYSIWYG 에디터 사용하기
>     'user',               # user프로필에 사진추가하기 앱
>     'hitcount',
>     'taggit',
>     'django.contrib.sitemaps'
> ]
> ```
> 2. 프로젝트의 urls.py에 zenblog 와 summernote, sitemap 앱을 추가하고 media 경로를 추가한다.
> ```python
> from django.urls import path, include
> from django.conf import settings
> from django.conf.urls.static import static
> from django.contrib import admin
> 
> from zenblog.sitemaps import PostSitemap
> from django.contrib.sitemaps.views import sitemap
>
> sitemaps = {
>     "posts": PostSitemap,
> }
> 
> urlpatterns = [
>     ...
>     path('admin/', admin.site.urls),
>     path('', include('zenblog.urls')),
>     path('summernote/', include('django_summernote.urls')),
>     path('sitemap.xml', sitemap, {"sitemaps": sitemaps}),
> ]
> 
> if settings.DEBUG:
>     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
> ```
> 3. settings.py에 필요한 설정을 추가한다.
> ```python
> COMPRESS_PRECOMPILERS = (
>     ('text/x-scss', 'django_libsass.SassCompiler'),
> )
> STATICFILES_FINDERS = [
>     'django.contrib.staticfiles.finders.FileSystemFinder',
>     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
>     'compressor.finders.CompressorFinder',
> ]
> STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
>
> MEDIA_URL = '/media/'
> MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
> X_FRAME_OPTIONS = 'SAMEORIGIN'
> 
> SUMMERNOTE_CONFIG = {
>     'attachment_filesize_limit': 4096 * 4096,
>     'summernote': {
>         'width': '100%',
>         'height': '480',
>     },
>     'lang': 'ko-kr',
> }
> 
> # DISABLE_DARK_MODE = True
> ```
> 4. 블로그를 입력하기 위해서 프로젝트에 데이터베이스를 생성한다.
> ```commandline
>     python manage.py makemigrations zenblog user
>     python manage.py migrate
>     python manage.py createsuperuser
> ```
> 5. http://127.0.0.1:8000/admin 으로 접속하여 블로그를 입력한다.


> 참고 : SCSS 설치하기        
> https://www.accordbox.com/blog/how-use-scss-sass-your-django-project-python-way/   
> 1. django_compressor, django-libsass를 설치한다. 앱을 설치하면 자동으로 설치된다.
> ```commandline
> pip install django_compressor django-libsass
> ```
> 2. 프로젝트 settings.py 의 INSTALLED_APPS 에 다음을 추가한다.
> ```python
> import os
> INSTALLED_APPS = [
>     ...
>     'compressor',
> ]
> 
> COMPRESS_PRECOMPILERS = (
>     ('text/x-scss', 'django_libsass.SassCompiler'),
> )
> 
> STATICFILES_FINDERS = [
>     'django.contrib.staticfiles.finders.FileSystemFinder',
>     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
>     'compressor.finders.CompressorFinder',
> ]
> 
> # compressor 앱을 실행하기 위해서는 STATIC_ROOT가 설정되어 있어야 한다.
> STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
> ```

> 참고 : WYSIWYG 설치, pillow 설치
> 1. django-summernote를 설치한다. 앱을 설치하면 자동으로 설치된다.
> ```commandline
> pip install django-summernote Pillow
> ```
> 2. 프로젝트 settings.py 에 다음을 추가한다.
> ```python
> import os
> INSTALLED_APPS += ('django_summernote', )
> MEDIA_URL = '/media/'
> MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
> X_FRAME_OPTIONS = 'SAMEORIGIN'
> ``` 
> 3. 프로젝트의 urls.py에 다음을 추가한다.
> ```python
> from django.urls import include, path
> from django.conf import settings
> from django.conf.urls.static import static
> # ...
> urlpatterns = [
>   ...
>   path('summernote/', include('django_summernote.urls')),
>   ...
> ]
> if settings.DEBUG:
>   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
> ```
> 4. 데이터베이스 마이그레이션 시행

> 참고 : Disable Dark mode Admin       
> https://djangolearn.com/p/disable-or-enable-dark-mode-user-interface-in-django-admin-panel

> 참고 : user 앱    
> 장고의 기본 users 에 사진을 첨부할 수 있는 기능을 추가한 앱이다.         
> https://www.devhandbook.com/django/user-profile/

> 참고 : hitcount 사용하기   
> https://dev.to/thepylot/how-to-track-number-of-hits-views-for-chosen-objects-in-django-django-packages-series-2-3bcb

> 참고 : taggit 사용하기   
> https://dev.to/thepylot/how-to-add-tags-to-your-models-in-django-django-packages-series-1-3704