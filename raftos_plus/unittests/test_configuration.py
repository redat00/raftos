# Python Standard Library
import unittest

# First Party
import raftos_plus


class TestConfiguration(unittest.TestCase):
    def test_configure(self):
        raftos_plus.configure(
            {
                "log_path": "/test_path/",
                "serializer": "TestSerializer",
                "secret_key": b"raftos test secret key",
                "salt": b"raftos test salt",
            }
        )

        self.assertEqual(raftos_plus.config.log_path, "/test_path/")
        self.assertEqual(raftos_plus.config.serializer, "TestSerializer")
        self.assertEqual(
            raftos_plus.config.secret_key,
            b"raftos test secret key",
        )
        self.assertEqual(raftos_plus.config.salt, b"raftos test salt")


if __name__ == "__main__":
    unittest.main()
