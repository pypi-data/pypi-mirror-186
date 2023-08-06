import unittest
from pds.api_client.rest import ApiException
from pds.api_client import Configuration
from pds.api_client import ApiClient
from pds.api_client.api.collections_api import CollectionsApi
from pds.api_client.model.pds_product import PdsProduct
from pds.api_client.model.pds_products import PdsProducts
from pds.api_client.model.pds4_product import Pds4Product
from pds.api_client.model.pds4_products import Pds4Products


class CollectionsApiTestCase(unittest.TestCase):

    def setUp(self):
        # create an instance of the API class
        configuration = Configuration()
        configuration.host = 'http://localhost:8080'
        api_client = ApiClient(configuration)
        self.collections = CollectionsApi(api_client)

    def test_all_collections(self):

        api_response: PdsProducts = self.collections.get_collection(start=0, limit=20)
        assert len(api_response.data) == 2
        assert api_response.summary.hits == 2

        assert all(['id' in c for c in api_response['data']])

        # select one collection with lidvid 'urn:nasa:pds:insight_rad:data_calibrated::7.0'
        collection = [c for c in api_response.data if c.id == 'urn:nasa:pds:insight_rad:data_derived::7.0'][0]
        assert 'type' in collection
        assert collection.type == 'Product_Collection'

        assert 'title' in collection
        assert collection.title == 'InSight RAD Derived Data Collection'

    def test_all_collections_one_property(self):
        api_response = self.collections.get_collection(
            start=0, limit=20,
            fields=['ops:Label_File_Info.ops:file_ref']
        )
        assert "data" in api_response

        collections_expected_labels = iter([
            '/data_derived/collection_data_rad_derived.xml',
            '/data_raw/collection_data_rad_raw.xml'
        ])

        for collection in api_response['data']:
            urls = collection['properties']['ops:Label_File_Info.ops:file_ref']
            assert next(collections_expected_labels) in urls.value[0]

    def test_collection_by_lidvid_all(self):
        collections = self.collections.collections_by_lidvid_all('urn:nasa:pds:insight_rad:data_derived::7.0')
        assert 'data' in collections
        assert len(collections.data) > 0
        assert 'id' in collections.data[0]
        assert collections.data[0]['id'] == 'urn:nasa:pds:insight_rad:data_derived::7.0'

    def test_collection_by_lidvid_all_content_type(self):
        collections: Pds4Products = self.collections.collections_by_lidvid_all(
            'urn:nasa:pds:insight_rad:data_derived::7.0',
            _content_type='application/vnd.nasa.pds.pds4+json'
        )
        assert 'data' in collections
        assert len(collections.data) > 0
        assert collections.data[0].type == 'Product_Collection'
        

if __name__ == '__main__':
    unittest.main()
