from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from .utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(_("Название города"), max_length=50)
    slug = models.SlugField(_("URL"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super(City, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Город")
        verbose_name_plural = _("Города")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("сity_detail", kwargs={"pk": self.pk})


class Language(models.Model):

    name = models.CharField(_("Язык программирования"), max_length=50)
    slug = models.SlugField(_("URL"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(self.name)
        super(Language,self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Язык")
        verbose_name_plural = _("Языки")

    def __str__(self): 
        return self.name

    def get_absolute_url(self):
        return reverse("language_detail", kwargs={"pk": self.pk})


class Vacancy(models.Model):

    url = models.URLField(_("URL"), max_length=200, unique=True)
    title = models.CharField(_("Заголовок"), max_length=250)
    company = models.CharField(_("Компания"), max_length=250)
    description = models.TextField(_("Описание"))
    language = models.ForeignKey(Language, verbose_name=_("Язык программирования"), on_delete=models.CASCADE)
    city = models.ForeignKey(City, verbose_name=_("Город"), on_delete=models.CASCADE)
    timestamp = models.DateField(_("Время добавления"), auto_now_add=True)


    class Meta:
        verbose_name = _("Вакансия")
        verbose_name_plural = _("Вакансии")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("vacancy_detail", kwargs={"pk": self.pk})



