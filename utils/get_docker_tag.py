import nbformat
import argparse


def get_args_parser():
    parser = argparse.ArgumentParser(
      description="Read Docker Container TAG that is required by the Notebook")
    parser.add_argument("--path", required=True)
    parser.add_argument("--test", required=False, action='store_true')
    parser.add_argument("--out-path", required=False)
    return parser


def get_container_uri_from_nb_dict(nb_obj):
    if "env" not in nb_obj.metadata:
        raise ValueError("There is no 'env' key in the Notebook's metadata")
    return nb_obj.metadata.env.container

if __name__ == "__main__":
    args = get_args_parser().parse_args()
    with open(args.path, "r") as nb_file:
        nb_obj = nbformat.read(nb_file, nbformat.NO_CONVERT)
        ## Adding metadat for testing
        if args.test:
            nb_obj.metadata["env"] = {
                "container": "gcr.io/deeplearning-platform-release/base-cpu:m39"
            }
        ##
        container_uri = get_container_uri_from_nb_dict(nb_obj)
        if args.out_path:
            with open(args.out_path, "w") as out_file:
              out_file.write(container_uri)
        else:
            print(container_uri)
