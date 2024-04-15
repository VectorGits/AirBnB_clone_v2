import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        """Set up the test case."""
        self.cli = HBNBCommand()

    def test_do_create_no_args(self):
        """Test do_create with no arguments."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create")
            self.assertEqual(f.getvalue(), "** class name missing **\n")

    def test_do_create_invalid_class(self):
        """Test do_create with an invalid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create MyClass")
            self.assertEqual(f.getvalue(), "** class doesn't exist **\n")

    def test_do_create_valid_class(self):
        """Test do_create with a valid class."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd("create BaseModel")
            self.assertTrue(len(f.getvalue().strip()) > 0)

    def test_do_create_with_params(self):
        """Test do_create with parameters."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.cli.onecmd('create State name="California"')
            self.assertTrue(len(f.getvalue().strip()) > 0)

if __name__ == "__main__":
    unittest.main()