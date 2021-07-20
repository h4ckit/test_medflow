from rest_framework.viewsets import ModelViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class TestView(ModelViewSet):
    """
    """
    # serializer_class =

    def retrieve(self, *args, **kwargs):
        # obj = get_object_or_404(Rubric.objects, id=rubric_id)
        # serializer = self.get_serializer(obj)
        # result = serializer.data
        result = {
            'asd': 'asd'
        }
        return Response(result)
