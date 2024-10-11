from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from providers.models import Provider
from providers.utils import add_request_to_queue
from django.shortcuts import get_object_or_404


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"


class RequestSerializer(serializers.Serializer):
    provider = serializers.IntegerField()
    request = serializers.CharField()


class ProvidersView(APIView):
    def post(self, request):
        serializer = ProviderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class RequestsView(APIView):
    def post(self, request):
        serializer = RequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        provider = get_object_or_404(Provider, pk=serializer.validated_data["provider"])
        add_request_to_queue(
            provider=provider.pk,
            p_rate_limit=provider.limit_by_sec,
            requst=serializer.validated_data["request"],
        )
        return Response(serializer.data)
