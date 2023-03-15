import unittest
import k8s


class K8sTestCase(unittest.TestCase):
    def test_generate_cmds(self):
        cmds = k8s.generate_cmds()
        self.assertIsNotNone(cmds)
