#!/usr/bin/env python3
""" Prueba SUITE Unittest """

from unittest import TestCase, mock
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """ Clase para probar la función Mapa anidado """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path,
         expected_output):
        """ Salida de retorno del método de prueba """
        real_out = access_nested_map(map, path)
        self.assertEqual(real_out, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path,
        wrong_output):
        """ El método de prueba genera la excepción correcta """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(TestCase):
    """ Clase para probar la función get_json """
    # order of args: test_url, test_payload
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ El método de prueba
        devuelve la salida correcta """
        # set mock response to have return value of test payload
        mock_respons = Mock()
        mock_respons.json.return_value = test_payload
        # function calls requests.get, need patch to get mock return value
        with patch('requests.get', return_value=mock_respons):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            # check that mocked method called once per input
            mock_respons.json.assert_called_once()


class TestMemoize(TestCase):
    """ Clase para probar la memorización """

    def test_memoize(self):
        """ Prueba la función de memoria """

        class TestClass:
            """ test de clases """

            def a_method(self):
                """ siempre retorna
                42 """
                return 42

            @memoize
            def a_property(self):
                """ retorna la memoria """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_clas = TestClass()
            real_ret = test_clas.a_property
            real_ret = test_clas.a_property

            self.assertEqual(real_ret, 42)
            patched.assert_called_once()
