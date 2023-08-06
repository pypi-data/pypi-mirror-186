from time import strftime
from os import mkdir, path, getcwd, environ
from PIL import Image
from typing import List
from dataclasses import dataclass
from huggingface_hub import login
from diffusers import StableDiffusionPipeline

@dataclass
class InferConfig:
    prompts: List[str]
    num_inference_steps: int = 50
    width: int = 512
    height: int = 512

class Model:
    # model_path="src/TrainedModel", 
    model_path: str = "joshelgar/premesh-mc-skin-2k"
    output_folder: str = "generated_images"

    def __init__(self, hf_token: str = ""):
        print(f"Downloading model: {self.model_path} from HF.")
        # Mac-specific setup
        login(environ.get("HUGGING_FACE_TOKEN", hf_token))
        self.pipe = StableDiffusionPipeline.from_pretrained(self.model_path)
        print("Finished downloading model")
        self.pipe = self.pipe.to("mps")
        self.pipe.enable_attention_slicing() # Recommended if your computer has < 64 GB of RAM
        def dummy(images, **kwargs):
            return images, False
        self.pipe.safety_checker = dummy
        self.make_output_folder()
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


    def infer(self, infer_config: InferConfig):
        ''' 
        Runs the model based on a supplied RunConfig (prompts, inf steps, resolution etc.)
        Returns -> List of filenames of resized images
        '''
        prompts = infer_config.prompts
        generated_filenames = []
        for idx, prompt in enumerate(prompts):
            print(f"Generating prompt [{idx}/{len(prompts)}]: [{prompt}]...")
            images: List[Image.Image] = self.pipe(prompt, **self.pipeline_args(infer_config=infer_config)).images
            currtime = strftime("%Y%m%d-%H%M%S")
            prompt_as_list = prompt.split()
            prompt_as_list.append(currtime)
            filename = "_".join(prompt_as_list)
            for image in images:
                full_filename = f"./{self.output_folder}/{filename}.png"
                image.save(full_filename)
                resized = image.resize((64, 64))
                resized_filename = f"./{self.output_folder}/{filename}_resized.png"
                resized.save(resized_filename)
                generated_filenames.extend([resized_filename])
                print(f"Done.")

        return generated_filenames