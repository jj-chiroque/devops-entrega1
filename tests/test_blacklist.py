import json
from .base import TestBase

class TestBlacklist(TestBase):
         
    def test_index(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Running")

    def test_add_item_without_authorization(self):
        item_data = {
            "email": "test_forbidden@gmail.com",
            "app_uuid": "app test forbidden",
            "blocked_reason": "reason test forbidden"
        }
        response = self.app.post("/blacklists", data=json.dumps(item_data))
        self.assertEqual(response.status_code, 403)

    def test_add_item_success(self):
        item_data = {
            "email": "test_account@gmail.com",
            "app_uuid": "app test",
            "blocked_reason": "reason test"
        }

        item_headers = {
            "Content-Type": "application/json",
            "Authorization": "DEVOPS"
        }

        response = self.app.post("/blacklists", data=json.dumps(item_data), headers=item_headers)
        
        self.assertEqual(response.status_code,201)

    def test_get_item_added(self):
        item_data = { "email": "test_added@gmail.com", "app_uuid": "app test", "blocked_reason": "reason test" }
        item_headers = { "Content-Type": "application/json", "Authorization": "DEVOPS" }
        response = self.app.post("/blacklists", data=json.dumps(item_data), headers=item_headers)
        
        response = self.app.get("/blacklists/test_added@gmail.com", headers=item_headers)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json["data"]["email"], "test_added@gmail.com")
 