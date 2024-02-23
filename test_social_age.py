from tests import get_social_status

import unittest


class TestSocialAge(unittest.TestCase):
	def test_can_get_child_age(self):
		age = 8
		expected_res = 'ребенок'
		function_res = get_social_status(age)
		self.assertEqual(expected_res, function_res)

	def test_can_get_teenager_age(self):
		age = 14
		expected_res = 'подросток'
		function_res = get_social_status(age)
		self.assertEqual(expected_res, function_res)

	def test_can_get_man_age(self):
		age = 20
		expected_res = 'взрослый'
		function_res = get_social_status(age)
		self.assertEqual(expected_res, function_res)

	def test_can_get_old_man_age(self):
		age = 55
		expected_res = 'пожилой'
		function_res = get_social_status(age)
		self.assertEqual(expected_res, function_res)

	def test_can_get_super_old_age(self):
		age = 80
		expected_res = 'пенсионер'
		function_res = get_social_status(age)
		self.assertEqual(expected_res, function_res)

	def test_cannot_pass_str_as_age(self):
		age = '55'
		with self.assertRaises(ValueError):
			get_social_status(age)

	def test_cannot_pass_negative_int(self):
		age = -55
		with self.assertRaises(ValueError):
			get_social_status(age)

	def test_cannot_pass_dict_as_age(self):
		age = {}
		with self.assertRaises(ValueError):
			get_social_status(age)

	def test_asdasd(self):
		age = []
		with self.assertRaises(ValueError):
			get_social_status(age)