from django.utils.decorators import decorator_from_middleware
from customcontent.middleware import CustomContentMiddleware

# Since the change to django 1.3 I think this is likely broken
# See http://old.nabble.com/TemplateResponse-and-decorator_from_middleware-td31590636.html
# for a discussion on it (May 2011) on how TemplateResponse with
# a middleware decorator changing the response is broke.

customcontented = decorator_from_middleware(CustomContentMiddleware)
