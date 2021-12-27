from drf_yasg import openapi

account_post_params = [
    openapi.Parameter("category", openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING),
    openapi.Parameter("created_by", openapi.IN_QUERY, required=False, type=openapi.TYPE_STRING),
]