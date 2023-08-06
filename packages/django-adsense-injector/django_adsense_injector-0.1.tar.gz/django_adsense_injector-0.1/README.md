=====
django_adsense_injector
=====

django_adsense_injector is a Django app to inject adsense ad code inside ckeditor body. easy to intergrate and and show ads to the users.

Detailed documentation is in the "www.instandblog.xyz" website.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_adsense_injector',
    ]

2. Add this line under templates settings in settings.py

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR,'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',

                    'social_django.context_processors.backends',
                ],
                'libraries':{
                    'adsense_tags': 'django_adsense_injector.templatetags.adsense_tags' #<---------
                }
            },
        },
    ]

2. Include the template tags load tag like this inside the template::

    {% load adsense_tags %}

3. Filter your ckeditor body field like below to inject your adsense code::

    {{post.body|inject_adsense_after_paragraph:"your_template_directory/your_html_file_name.html"|safe}}

4. create `your_html_file_name.html` file inside the template directory and paste your adsense code.

4. Start the development server http://127.0.0.1:8000/

5. Visit http://127.0.0.1:8000/your-post-url/ to see the outputs(you can't view adsense ad in the development time, but if you inspect the page you can see the injected code).