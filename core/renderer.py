"""
========
Renderer
========
Change the framework's standard response structure to Eventops specific response.

The response design is follow

For single object or data::


    {
        "data": {
        }
    }

For list of object::

    {
        "meta": {
            "count": "TOTAL RECORD COUNT"
            "next": "NEXT PAGE LINK"
            "previous": "PREVIOUS PAGE LINK"
        },
        "data": [
        ]
    }

When error occurs::

    {
        "error": {
            "type": "ERROR TYPE",
            "detail": "HUMAN READABLE MESSAGE",
            "status_code": "APPROPRIATE STATUS CODE",
            "error_code": "ERROR CODE"

        }
    }
"""
from rest_framework.renderers import JSONRenderer as RFJSONRenderer

# import helper
#
#
# class ExJSONRenderer(RFJSONRenderer):
#     """
#     Override the ``render()`` of the rest framework JSONRenderer to produce JSON output as per \
#     API specification
#     """
#
#     def render(self, data, accepted_media_type=None, renderer_context=None):
#         response_data = {}
#         context = 'data'  # Default
#
#         # When exception handler will pass the response, we would expect
#         # the context to be `error`
#         if isinstance(data, dict) and data.get('_context') == 'error':
#             context = 'error'
#             data.pop('_context', None)
#
#             # Normalizing detail field in error, only first element of dict should be visible
#             if data.get('non_field_errors'):
#                 data['detail'] = data.pop('non_field_errors')[0]
#             elif data.get('detail'):
#                 pass
#             else:
#                 detail = None
#                 for k, v in data.items():
#                     if k in ['type', 'error_code', 'status_code']:
#                         continue
#
#                     err_list = data.pop(k)
#                     if isinstance(err_list, list):
#                         detail = err_list[0].replace(
#                             'This field', '%s' % helper.snake_case_to_title(k)
#                         ).replace(
#                             'This list', '%s' % helper.snake_case_to_title(k)
#                         )
#                     else:
#                         error_string=''
#                         for k, v in err_list.items():
#                             error_string = error_string + str(v)
#
#                         detail = error_string
#
#                 data['detail'] = detail
#
#         # check if the results have been paginated
#         if isinstance(data, dict) and data.has_key('results'):
#             # add the resource key and copy the results
#             response_data[context] = data.pop('results')
#             response_data['meta'] = data
#         else:
#             response_data[context] = data
#
#         # call super to render the response
#         response = super(ExJSONRenderer, self).render(response_data, accepted_media_type,
#                                                       renderer_context)
#
#         return response
