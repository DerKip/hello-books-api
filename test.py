import unittest
import json
from app import api

class HelloBooksTestCase(unittest.TestCase):
    """This class represents the hello-books-api test case"""

    def setUp(self):
        """
        Define test variables and initialize app.
        """
        self.app = create_app(config_name="testing") #creates an environment for a test to run 
        self.client = self.app.test_client()
        self.app_context.push() #activate
        self.book = {'book_id': 254,'book_title': 'Learning Flask','author': 'John Waithaka','publisher':'dojoDevs','edition': 3}
        
    def test_add_book(self):
        """Test API can add a book (POST request)"""
        res = self.client().post('/api/books', data=self.book)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Learning Flask', str(res.data))

    def test_api_can_modify_book(self):
        """Test API can modify a books information (PUT request)"""
        rv = self.client().post('/api/books/254',data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put('/bucketlists/1',data={"name": "Dont just eat, but also pray and love :-)"})
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/bucketlists/1')
        self.assertIn('Dont just eat', str(results.data))


    def test_api_can_get_all_bucketlists(self):
        """Test API can get a bucketlist (GET request)."""
        res = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/bucketlists/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Go to Borabora', str(res.data))

    def test_api_can_get_bucketlist_by_id(self):
        """Test API can get a single bucketlist by using it's id."""
        rv = self.client().post('/bucketlists/', data=self.bucketlist)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/bucketlists/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('Go to Borabora', str(result.data))

    def test_bucketlist_deletion(self):
        """Test API can delete an existing bucketlist. (DELETE request)."""
        rv = self.client().post(
            '/bucketlists/',
            data={'name': 'Eat, pray and love'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/bucketlists/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/bucketlists/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):
        """teardown all initialized variables."""
        self.app.app_context.pop()#removes the keys

           
# Make the tests conveniently executable
    if __name__ == "__main__":
        unittest.main()