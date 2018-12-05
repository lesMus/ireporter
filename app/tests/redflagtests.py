import unittest
import json
from app import create_app


class Tests_for_Redflags(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context=self.app
        self.app.testing=True
        self.data = {
            "id": 1,
            "createdOn" : "30.12.2018",
            "createdBy" : "Mutheu Nzuma",
            'type' : 'red-flag',
            "location" : "Kaloleni",
            "status" : "Under investigation",
            "images" : "",
            "videos" : "",
            "title" : "seatbelts",
            "comment" : "Police asked for bribe"
        }

    def test_can_fetch_all_redflags(self):
        response = self.client.get("/api/v1/redflags",
         headers={'Content-Type': 'application/json'},
         data = json.dumps(self.data))
        self.assertEqual(response.status_code, 200)

        
    

if __name__ == "__main__":
    unittest.main() 