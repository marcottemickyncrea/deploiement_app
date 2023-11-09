import unittest
from fastapi.testclient import TestClient
from back.app import app

class TestAPI(unittest.TestCase):
    client = TestClient(app)
    data = "Le chlorure de sodium se retrouve dans toutes les mers, ainsi que dans les cuisines de toutes les familles, plus communément appelé sel. Le dioxyde de carbone est le déchet de la respiration."
    
    def test_reponse(self):
        """
        Vérifie que la reponse est correcte
        """
        reponse=self.client.post("/predict",
                     json=self.data)
        self.assertEqual(reponse.status_code,200)
        self.assertEqual(dict,type(reponse.json()))

if __name__ == '__main__':
    unittest.main()