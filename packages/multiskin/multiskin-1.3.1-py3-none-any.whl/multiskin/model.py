from time import strftime
from os import mkdir, path, getcwd, environ
from PIL import Image
from typing import List
from dataclasses import dataclass
from huggingface_hub import login
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

from multiskin_lib.src.multiskin.clean.clean_skin import clean_skin

@dataclass
class InferConfig:
    prompts: List[str]
    num_inference_steps: int = 50
    width: int = 512
    height: int = 512

def dummy(images, **kwargs):
            return images, False

class Model:
    '''
    Python class that wraps the real model (weights, etc) hosted on HF under model_path.
    Uses HuggingFace libs to download the model, configure it for CUDA.
    infer() function
    '''
    # model_path="src/TrainedModel", 
    model_path: str = "joshelgar/premesh-mc-skin-2k"
    output_folder: str = "generated_images"

    def __init__(self, hf_token: str = "", mac: bool = False):
        login(environ.get("HUGGING_FACE_TOKEN", hf_token))
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_path)
        if mac:
            self.pipe = self.pipe.to("mps")
            self.pipe.enable_attention_slicing() # Recommended if your computer has < 64 GB of RAM
        else:
            self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(self.pipe.scheduler.config)
            self.pipe = self.pipe.to("cuda")
        
        self.pipe.safety_checker = dummy
        self.make_output_folder()
        if mac:
            self.warmup_pass()

    def warmup_pass(self):
        _ = self.pipe("nothing", num_inference_steps=1) # warmup to fix first-inference bug

    def make_output_folder(self):
        print("Creating output folder")
        dir = path.join(getcwd(), f'./{self.output_folder}')
        if not path.isdir(dir):
            mkdir(dir)

    def pipeline_args(self, infer_config: InferConfig):
        args = {
            "num_inference_steps": infer_config.num_inference_steps,
            "height": infer_config.height,
            "width": infer_config.width
        }
        return args


    def infer(self, infer_config: InferConfig) -> List[str]:
        ''' 
        Runs the model based on a supplied RunConfig (prompts, inf steps, resolution etc.)
        Returns -> List of filenames of resized images
        '''
        prompts = infer_config.prompts
        generated_filenames = []
        for idx, prompt in enumerate(prompts):
            print(f"Generating prompt [{idx}/{len(prompts)}]: [{prompt}]...")
            images: List[Image.Image] = self.pipe(f"{prompt} mc", **self.pipeline_args(infer_config=infer_config)).images
            currtime = strftime("%Y%m%d-%H%M%S")
            prompt_as_list = prompt.split()
            prompt_as_list.append(currtime)
            filename = "_".join(prompt_as_list)
            for image in images:
                # full_filename = f"./{self.output_folder}/{filename}.png"
                # image.save(full_filename)
                resized = image.resize((64, 64))
                cleaned = clean_skin(resized)
                final_filename = f"./{self.output_folder}/{filename}_resized.png"
                cleaned.save(final_filename)
                generated_filenames.append(final_filename)

        return generated_filenames