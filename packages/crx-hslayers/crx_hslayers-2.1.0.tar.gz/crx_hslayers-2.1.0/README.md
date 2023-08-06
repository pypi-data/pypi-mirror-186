# HSLayers-NG map widget for Wagtail CodeRed CMS

Note: Has npm dependency on [HSLayers-NG](https://www.npmjs.com/package/hslayers-ng-app) that gets automatically installed into static files. `python manage.py collectstatic` must be executed for the module to correctly locate the HSLayers bundles.


## Instalation
1. Copy whole codered-hslayers to the Wagtail root to a new folder named 'hslayers'

2. Add 'hslayers' to the INSTALLED_APPS list in the settings/base.py
```
INSTALLED_APPS = [
    # This project
    'website',
    
    # CodeRed CMS
    'coderedcms',
    'bootstrap4',
    ...
    
    'hslayers'
]
```

3. You have three options now:
    * Keep existing CodeRed 'Web Page', 'Article Landing Page' and 'Article Page' untouched and add a new page type 'Web Page Extended', 'Article Landing Page Extended' and 'Article Page Extended' with new widgets of hslayers
        * Run hslayers migrations
        ```
        $ python3 manage.py makemigrations hslayers
        ```
        * Go to point 4

    * Modify existing CodeRed 'Web Page' and/or 'Article Landing Page' and/or 'Article Page' type and add hslayers widgets to it
        * Edit Wagtail's models.py file
            * Add those imports at the top
            ```
            from coderedcms.blocks import (
              CONTENT_STREAMBLOCKS,
              LAYOUT_STREAMBLOCKS,
              GridBlock,
              HeroBlock,
              CardGridBlock,
              CardBlock
            )

            from django.utils.translation import gettext_lazy as _
            from hslayers import blocks
            from wagtail.core.fields import StreamField
            from wagtail.core.blocks import RawHTMLBlock
            ```

            * Replace code of WebPage and/or ArticleIndexPage and/or ArticlePage function with the WebPage2 and/or ArticleIndexPageExtended and/or ArticlePageExtended function code from the hslayers/models.py file

        * Delete WebPage2 and/or ArticleIndexPageExtended and/or ArticlePageExtended method in the hslayers/models.py file
        * In case of ArticleIndexPage and ArticlePage overriding, don't forget to modify ```subpage_types``` and ```parent_page_types``` to your needs. In this particular case delete 'hslayers.ArticlePageExtended' and 'hslayers.ArticleIndexPageExtended' from the code
        ```
        parent_page_types = ['website.ArticleIndexPage', 'hslayers.ArticleIndexPageExtended']
        ...
        subpage_types = ['website.ArticlePage', 'hslayers.ArticlePageExtended']
        ```
        * Go to point 4

    * Use hslayers widgets in any other Wagtail models
        * Take the code of WebPage2 and/or ArticleIndexPageExtended the hslayers/models.py file and modify it as you wish or use the widgets anywhere else
        * Go to point 4

4. Update Wagtail migrations
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py collectstatic
```

5. Restart Wagtail

6. New HSLayers blocks are added to the CMS
    * HSLayers map
    * Aligned Paragraph
    * Header


## Development
Update semantic version of the package

Run test update without commiting
```
$ bumpver update --patch(--minor|--major) --dry
```

Run update and commit the changes to the repo
```
$ bumpver update --patch(--minor|--major)
```