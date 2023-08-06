import unittest
import os
from unittest.mock import patch
from multiskin.model import Model, InferConfig

class TestInference(unittest.TestCase):
    @patch('PIL.Image.Image.save')
    def test_inference(self, _mock):
        model_inst = Model()
        nif=1
        prompt="spiderman mc"
        inf_conf = InferConfig(prompts=[prompt], num_inference_steps=nif, width=512, height=512)
        gen_filenames = model_inst.infer(infer_config=inf_conf)
        self.assertTrue('spiderman' in gen_filenames[0])

if __name__ == '__main__':
    unittest.main()