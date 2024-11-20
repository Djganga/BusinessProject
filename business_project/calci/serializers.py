from rest_framework import serializers
from calci import models

class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ledger
        fields = '__all__'
