from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

class SourceValueQueryTest(TestCase):
    def test_query_by_content_type_and_object_id(self):
        # Create a SomeModel instance to use for testing
        some_model_instance = SomeModel.objects.create(name='Test Model')

        # Create some SourceValue instances
        for i in range(3):
            SourceValue.objects.create(
                value=FeatureValue.objects.create(feature=Feature.objects.create(name=f'Feature {i}')),
                marketdata=some_model_instance
            )

        # Get the ContentType for the SomeModel model
        content_type = ContentType.objects.get_for_model(SomeModel)

        # Query the SourceValue instances using the ContentType and object ID
        source_values = SourceValue.objects.filter(
            marketdata_ct=content_type,
            marketdata_fk=some_model_instance.pk
        )

        # Check that the query returns the expected number of results
        self.assertEqual(source_values.count(), 3)

    def test_query_by_object(self):
        # Create a SomeModel instance to use for testing
        some_model_instance = SomeModel.objects.create(name='Test Model')

        # Create some SourceValue instances
        for i in range(3):
            SourceValue.objects.create(
                value=FeatureValue.objects.create(feature=Feature.objects.create(name=f'Feature {i}')),
                marketdata=some_model_instance
            )

        # Query the SourceValue instances using the object
        source_values = some_model_instance.source_values.all()

        # Check that the query returns the expected number of results
        self.assertEqual(source_values.count(), 3)
