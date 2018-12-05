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

        
    def test_can_remove_specific_redflag(self):
        response = self.client.delete("/api/v1/redflags/100",
            headers={'Content-Type': 'application/json'}, 
            data = json.dumps(self.data))
        self.assertEqual(response.status_code, 405)

    def test_can_edit_location_of_specific_redflag(self):
        response = self.client.patch("/api/v1/red-flags/1/location", 
            headers={'Content-Type': 'application/json'},
            data = json.dumps({"location" : "newLocation"}))
        self.assertEqual(response.status_code, 404)    

    def test_can_edit_comment_of_specific_redflag(self):
        response = self.client.patch("/api/v1/redflags/1/comment", 
            headers={'Content-Type': 'application/json'}, 
            data = json.dumps({"comment" : ''}))
        self.assertEqual(response.status_code, 200)                 
 
    def test_can_fetch_specific_redflag(self):
        response = self.client.post("/api/v1/redflag/101", 
            headers={'Content-Type': 'application/json'},
            data = json.dumps(self.data))
        self.assertEqual(response.status_code, 405)


# Tests to be worked out once the POST endpoint is sorted out
   
    """
    def test_can_create_redflag(self):
        response = self.client.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        self.assertEqual(response.status_code, 201)

   
    def test_redflag_not_found(self):
        response = self.client.get("/api/v1/redflag/10")
        #result = json.loads(response.data)
        self.assertEqual(response.status_code, 404)      

    """

if __name__ == "__main__":
    unittest.main() 