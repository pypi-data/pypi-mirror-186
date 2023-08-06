import argparse
from premesh_lib.src.multiskin_joshelgar.model import Model
from premesh_lib.src.multiskin_joshelgar.model import InferConfig


def main():
    parser = argparse.ArgumentParser(
        prog = 'ModelRunner',
        description = 'Runs pre-trained SD models locally on M1 hardware.',
        epilog = '--- auth: jelgar ---')
    parser.add_argument("prompt", help="The prompt to infer with the model.")
    parser.add_argument("--num_inference_steps", type=int, default=50, help="The number of inference steps.")
    parser.add_argument("--width", type=int, default=512, help="The width of the inference image.")
    parser.add_argument("--height", type=int, default=512, help="The height of the inference image.")
    parser.add_argument("--num", type=int, default=4, help="The number of images to create.")
    args = parser.parse_args()
    infer_config = InferConfig(prompts=[args.prompt] * args.num, num_inference_steps=args.num_inference_steps, width=args.width, height=args.height)
    model = Model()
    return model.infer(infer_config=infer_config)

if __name__ == "__main__":
    main()
