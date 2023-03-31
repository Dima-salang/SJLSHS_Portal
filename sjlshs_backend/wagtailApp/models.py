from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, TabbedInterface, ObjectList
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.search import index

class ArticlePage(Page):
    body = RichTextField(blank=True)
    date = models.DateField("Post date", null=True, blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('feed_image'),
        FieldPanel('body', classname="full"),
        
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])




class OrgHomePage(Page):
    body = RichTextField(blank=True)
    date = models.DateField("Post date", null=True, blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('feed_image')
    ]


class IndexPage(Page):
    body = RichTextField(blank=True)
    date = models.DateField("Post date", null=True, blank=True)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('feed_image')
    ]




class ArticleIndexPage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body", classname="full"),
        InlinePanel("latest_articles", label="Latest Articles"),
    ]

    def get_latest_articles(self):
        return ArticlePage.objects.live().order_by("date")

class ArticleIndexPageLatestArticles(Orderable):
    page = ParentalKey(ArticleIndexPage, on_delete=models.CASCADE, related_name="latest_articles")
    article = models.ForeignKey(ArticlePage, on_delete=models.CASCADE, related_name="+", blank=True, null=True)

    panels = [
        FieldPanel("article"),
    ]


class CareerInformationArticle(Page):
    School_Image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    School_Description = RichTextField(blank=True)
    
    search_fields = Page.search_fields + [
        index.SearchField('School_Description'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('School_Image'),
        FieldPanel('School_Description', classname="full"),
        
    ]

    edit_handler = TabbedInterface([
        ObjectList(content_panels, heading='Content'),
        ObjectList(Page.promote_panels, heading='Promote'),
        ObjectList(Page.settings_panels, heading='Settings'),
    ])
