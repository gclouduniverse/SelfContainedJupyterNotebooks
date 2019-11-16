import argparse
import nbformat


def get_args_parser():
    parser = argparse.ArgumentParser(
        description="Write container metadata required for environment")
    parser.add_argument("--path", required=True)
    parser.add_argument("--environment", required=True)
    return parser


def main():
    args = get_args_parser().parse_args()
    with open(args.path, "r") as nb_file:
      nb_obj = nbformat.read(nb_file, nbformat.NO_CONVERT)
    nb_obj.metadata["env"] = {
        "container": args.environment
    }
    with open(args.path, "w") as nb_file:
      nbformat.write(nb_obj, nb_file)


if __name__ == "__main__":
  main()
