import unittest
import tests.config as config
from salesfly import Client
from salesfly.errors import ResponseError


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = Client(api_key=config.API_KEY)

    def test_get_version(self):
        v = self.client.version()
        self.assertIsNotNone(v)
        print("Version: {0}".format(v))

    def test_get_api_usage(self):
        try:
            usage = self.client.usage.get()
            self.assertIsNotNone(usage)
            print("Allowed requests: {0}".format(usage["allowed"]))
            print("Used requests: {0}".format(usage["used"]))
        except ValueError:
            pass
        except ResponseError as e:
            self.assertIsNotNone(e)

    # def test_get_geoip(self):
    #     location = self.client.geoip.get("8.8.8.8")
    #     self.assertIsNotNone(location)
    #     print("Country code: {0}".format(location["country_code"]))

    # def test_get_geoip_with_options(self):
    #     location = self.client.geoip.get("8.8.8.8", fields="country_code,hostname", hostname=True)
    #     self.assertIsNotNone(location)
    #     print("Country code: {0}".format(location["country_code"]))
    #     print("Host name: {0}".format(location["hostname"]))

    # def test_get_geoip_invalid_ip(self):
    #     try:
    #         self.client.geoip.get("288.8.8.8")
    #     except ValueError:
    #         pass
    #     except ResponseError as e:
    #         self.assertEqual(e.code, "err-invalid-ip")

    # def test_get_geoip_myip(self):
    #     location = self.client.geoip.get_current()
    #     self.assertIsNotNone(location)

    # def test_get_geoip_bulk(self):
    #     locations = self.client.geoip.get_bulk("8.8.8.8,google.com")
    #     self.assertIsNotNone(locations)
    #     for i in range(len(locations)):
    #         print("Country code: {0}".format(locations[i]["country_code"]))

    # def test_get_geoip_bulk2(self):
    #     locations = self.client.geoip.get_bulk(["8.8.8.8,google.com"])
    #     self.assertIsNotNone(locations)
    #     for i in range(len(locations)):
    #         print("Country code: {0}".format(locations[i]["country_code"]))

    # def test_send_mail(self):
    #     message = {
    #         "from": "ok@demo2.org",
    #         "to": ["ok@demo2.org", "okey@demo2.org"],
    #         "subject": "Test",
    #         "text": "This is just a test",
    #         "attachments": ["/Users/otto/me.png"]
    #     }
    #     receipt = self.client.mail.send(message)
    #     self.assertIsNotNone(receipt)


if __name__ == "__main__":
    unittest.main()
