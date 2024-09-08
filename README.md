# django-jalali-date

[![PyPI version](https://badge.fury.io/py/django-jalali-date.svg)](https://badge.fury.io/py/django-jalali-date)
[![Django versions](https://img.shields.io/badge/Django-%3E=3.2-blue)](https://www.djangoproject.com/)
[![Python versions](https://img.shields.io/badge/Python-%3E=3.6-blue)](https://www.python.org/)

`django-jalali-date` یک پلاگین برای جنگو است که تاریخ‌های میلادی را به تاریخ شمسی (جلالی) تبدیل می‌کند. این پلاگین با استفاده از کتابخانه‌ی `khayyam` تاریخ‌ها را در قالب‌های جنگو به شمسی نمایش می‌دهد.

## ویژگی‌ها

- تبدیل خودکار تاریخ میلادی به شمسی.
- استفاده آسان از فیلتر سفارشی جنگو در قالب‌ها.
- بدون نیاز به تغییرات اساسی در پروژه.

## نصب

ابتدا با استفاده از `pip` پلاگین را نصب کنید:

```bash
pip install django-jalali-date

# settings.py

INSTALLED_APPS = [
    ...
    'jalali_date',
]

{% load jalali_date_tags %}

<p>تاریخ شمسی: {{ object.date|to_jalali }}</p>


{% load jalali_date_tags %}

<ul>
    {% for event in events %}
        <li>تاریخ رویداد: {{ event.date|to_jalali }}</li>
    {% endfor %}
</ul>