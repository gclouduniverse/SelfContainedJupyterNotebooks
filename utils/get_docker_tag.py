import nbformat
import argparse

#nbformat.reads

def get_args_parser():
    parser = argparse.ArgumentParser(
      description="Read Docker Container TAG that is required by the Notebook")
    parser.add_argument("--path", required=True)
    return pareser


if __name__ == "__main__":
    args = get_args_parser().parse_args()
    nb_obj = nbformat.reads(unicode(args.apth), nbformat.NO_CONVERT)
    print(nb_obj)