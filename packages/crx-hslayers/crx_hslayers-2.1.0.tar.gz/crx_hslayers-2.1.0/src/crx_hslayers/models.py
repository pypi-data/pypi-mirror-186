# from django.utils.translation import gettext_lazy as _
# from django.db import models
# from coderedcms.models import CoderedWebPage, CoderedArticleIndexPage, CoderedArticlePage
# from coderedcms.blocks import (
#     CONTENT_STREAMBLOCKS,
#     LAYOUT_STREAMBLOCKS,
#     GridBlock,
#     HeroBlock,
#     CardGridBlock,
#     CardBlock,
# )
# from wagtail.admin.panels import FieldPanel
# from wagtail.admin.edit_handlers import StreamFieldPanel
# from wagtail.core.fields import StreamField
# from wagtail.core.blocks import RawHTMLBlock
# from hslayers import blocks


# # class MapPage(CoderedWebPage):

# #     class Meta:
# #         verbose_name = 'Map Page'

# #     template = 'map_page.html'
# #     # Override body to add Map block content
# #     body = StreamField(LAYOUT_STREAMBLOCKS + [("map_block", blocks.MapBlock())])
# #     #body_content_panels = CoderedWebPage.body_content_panels


# class WebPage2(CoderedWebPage):
#     """
#     General use page with featureful streamfield and SEO attributes.
#     """

#     class Meta:
#         verbose_name = "Web Page Extended"

#     template = "coderedcms/pages/web_page.html"

#     # remove original GridBlock, HeroBlock and create it later with extended local_blocks in constructor
#     if "row" in [x[0] for x in LAYOUT_STREAMBLOCKS]:
#         idx = [x[0] for x in LAYOUT_STREAMBLOCKS].index("row")
#         LAYOUT_STREAMBLOCKS.pop(idx)
#     if "hero" in [x[0] for x in LAYOUT_STREAMBLOCKS]:
#         idx = [x[0] for x in LAYOUT_STREAMBLOCKS].index("hero")
#         LAYOUT_STREAMBLOCKS.pop(idx)

#     content_blocks_ext = CONTENT_STREAMBLOCKS + [
#         ("aligned_paragraph_block", blocks.AlignedParagraphBlock()),
#         ("header", blocks.HeaderBlock()),
#         ("map_block", blocks.MapBlock()),
#         ("remote_block", blocks.RemoteBlock()),
#     ]

#     body = StreamField(
#         LAYOUT_STREAMBLOCKS
#     + [
#         # create extended GridBlock and Hero
#         ('row', GridBlock(content_blocks_ext)),
#         ('hero', HeroBlock([
#             ('row', GridBlock(content_blocks_ext)),
#             ('cardgrid', CardGridBlock([
#                 ('card', CardBlock()),
#             ])),
#             ('html', RawHTMLBlock(icon='code', form_classname='monospace', label=_('HTML'))),
#         ])),
#         ("aligned_paragraph_block", blocks.AlignedParagraphBlock()),
#             ("header", blocks.HeaderBlock()),
#         ("map_block", blocks.MapBlock()),
#         ("remote_block", blocks.RemoteBlock()),
#             # ('list', ListBlock()),
#             # ('image_text_overlay', ImageTextOverlayBlock()),
#             # ('cropped_images_with_text', CroppedImagesWithTextBlock()),
#             # ('list_with_images', ListWithImagesBlock()),
#             # ('thumbnail_gallery', ThumbnailGalleryBlock()),
#             # ('chart', ChartBlock()),
#             # ('map', MapBlock()),
#             # ('image_slider', ImageSliderBlock()),
#         ],
#         null=True,
#         blank=True,
#     )


# class ArticleIndexPageExtended(CoderedArticleIndexPage):
#     class Meta:
#         verbose_name = "Article Landing Page Extended "

#     body = StreamField(
#         LAYOUT_STREAMBLOCKS + [("map_block", blocks.MapBlock())], null=True, blank=True
#     )
#      # Override to specify custom index ordering choice/default.
#     index_query_pagemodel = 'hslayers.ArticlePageExtended'

#     # Only allow ArticlePages beneath this page.
#     subpage_types = ['website.ArticlePage', 'hslayers.ArticlePageExtended']

#     template = 'hslayers/pages/article_index_page.html'

# class ArticlePageExtended(CoderedArticlePage):
#     """
#     Article, suitable for news or blog content.
#     """
#     class Meta:
#         verbose_name = 'Article Extended'
#         ordering = ['-first_published_at']

#     body = StreamField(
#         CONTENT_STREAMBLOCKS + [("map_block", blocks.MapBlock())], null=True, blank=True
#     )

#     remote_cover_image_url = models.URLField(
#         verbose_name=_("Remote cover image URL"),
#         null=True,
#         blank=True
#     )

#     content_panels = CoderedArticlePage.content_panels + [
#         FieldPanel('remote_cover_image_url')
#     ]    

#     # Only allow this page to be created beneath an ArticleIndexPage.
#     parent_page_types = ['website.ArticleIndexPage', 'hslayers.ArticleIndexPageExtended']

#     template = 'hslayers/pages/article_page.html'
#     search_template = 'coderedcms/pages/article_page.search.html'

    
    