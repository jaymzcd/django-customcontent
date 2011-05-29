import re
from customcontent.models import CustomContent
from customcontent.templatetags.customcontent_tags import cc_item

class CustomContentMiddleware(object):

    def process_response(self, request, response):
        """
            TODO: refactor some to improve load time - probably need to
            change the cc_item as that's doing a hit to the db for each
            call of it when we already have our item essentially.
        """
        item = CustomContent.find(request)
        head_data = cc_item(item, 'extra_head', 'js', 'css')
        encoded =  response.content.decode('utf-8')
        response.content = re.sub(r'(</head>)', r'%s\1' % head_data, encoded)
        # atm do not insert at positions, just append before body close
        body_data = cc_item(item, 'customitem_set')
        response.content = re.sub(r'(</body>)', r'%s\1' % body_data, encoded)
        return response
