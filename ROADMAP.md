## The Workflow
There will be a basic library that provides the ability to embed environment information into a notebook and parse the information out from there.  This library can be invoked by a Jupyter plugin or other tooling to embed/restore the required environment.

# Packing the notebook
Have a jupyter plugin that, upon every save, will update the environment metadata with as much of the below information as possible (via the above mentioned plugin)

 * If running on Cloud AI Notebooks, it will add the gcp notebook section, with the required image/container info (other formats can be defined for other cloud platforms. This will be extensible)
 * If there is a local file named requirements.txt or environment.yaml, their contents will be filled into their respective fields

# Unpacking the notebook:
Ideally,  when creating a new notebook there will be some open/unpack/recreate notebook from existing *.ipynb file option.  Alternatively, we could have a library that sets up an environment based on the data in a given notebook and then sends that notebook to that environment (the details can be figured out later).

The unpacker will create local versions of requirements.txt, environment.yaml, etc and will run the commands to apply those settings as appropriate.
