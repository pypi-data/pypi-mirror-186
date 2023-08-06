# -*- coding:utf-8 -*-
from __future__ import unicode_literals

# Stdlib imports

# Core Django imports
from django import template
from django.template.loader import render_to_string


register = template.Library()

@register.filter
def inject_adsense_after_paragraph(value,params):
    params = params.split("&")
    path = params[0]
    try:
        ad_after = int(params[1]) 
    except:
        ad_after = 0

    ad_code = render_to_string(path)

    paragraphs = value.split("</p>")


    if ad_after == 0:
        ad_count = 0
        for i, para in enumerate(paragraphs):
            if len(para)>450:
                if ad_count < len(paragraphs)/10:
                    paragraphs[i] = paragraphs[i] + ad_code + "<p></p>"

                    value = "</p>".join(paragraphs)
                    ad_count += 1
    else:
        if ad_after<len(paragraphs):
            paragraphs[ad_after] = paragraphs[ad_after] + ad_code + "<p></p>"

            value = "</p>".join(paragraphs)

    return value
