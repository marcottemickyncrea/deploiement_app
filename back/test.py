import unittest
from fastapi.testclient import TestClient
from app import app

class TestAPI(unittest.TestCase):
    client = TestClient(app)
    data = "Le chlorure de sodium se retrouve dans toutes les mers, ainsi que dans les cuisines de toutes les familles, il est plus communément appelé sel. Le dioxyde de carbone est un déchet de la respiration animale."
    
    def test_reponse(self):
        """
        Vérifie que la reponse est correcte
        """
        reponse=self.client.post("/predict",
                     json={'text': self.data})
        self.assertEqual(reponse.status_code,200)
        self.assertEqual(dict,type(reponse.json()))

if __name__ == '__main__':
    unittest.main()