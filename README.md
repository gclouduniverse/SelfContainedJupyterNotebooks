# SelfContainedJupyterNotebooks
Embed your notebook's environment inside the notebook itself.  Libraries + format to both embed key information about it's environmental dependencies into the notebook as well as extract the required info to recreate that environment.

This concept is still in the early stages. Any and all feedback is most welcome!

We try to keep the format generic, using existing standards, while also making it possible to specify which cloud the notebook is supposed to be executed on.

# Principles
The principles were:
1. Scope limited to specifying the notebook's environment.  
    * Out of scope (for now): including local files that the notebook may depend on (though we could get some files by linking to a public git repo)
2. The notebook file should be self contained.  A single notebook file should contain all the information necessary to recreate the environment.  All that information will be embedded in the notebook’s “metadata” tag

# The Workflow
There will be a basic library that provides the ability to embed environment information into a notebook and parse the information out from there.  This library can be invoked by a Jupyter plugin or other tooling to embed/restore the required environment.

## Packing the notebook
Have a jupyter plugin that, upon every save, will update the environment metadata with as much of the below information as possible (via the above mentioned plugin)

 * If running on Cloud AI Notebooks, it will add the gcp notebook section, with the required image/container info (other formats can be defined for other cloud platforms. This will be extensible)
 * If there is a local file named requirements.txt or environment.yaml, their contents will be filled into their respective fields

## Unpacking the notebook:
Ideally,  when creating a new notebook there will be some open/unpack/recreate notebook from existing *.ipynb file option.  Alternatively, we could have a library that sets up an environment based on the data in a given notebook and then sends that notebook to that environment (the details can be figured out later).

The unpacker will create local versions of requirements.txt, environment.yaml, etc and will run the commands to apply those settings as appropriate.

# Metadata Format
```
{
 "cells": [],
 "metadata": {
   "environment" : {
     // The version string for the format, in case there are breaking changes in the future
     "env_ver" : "0.1",

     // This list should contain analogues for the most common
     // configuration file types listed in https://mybinder.readthedocs.io/en/latest/config_files.html#config-files
     //
     // Difference will be things like Dockerfile, which should be 
     // replaced with a pointer to specific images"
     //
     // We can start small by supporting just the configs listed below.
     //
     "requirements.txt" : "Contains contents of requirements.txt (if the file exists)",
     "environment.yaml" : "Contains contents of environment.yml file (if one exists).  This is a standard configuration file used to setup an anaconda environment" ,
     "container" : "path to container your notebook should be run inside",
    
     "setup.sh" : "Contains contents of setup.sh (name can be changed) if file exist. This will be some generic setup script, to be run after the other setup operations have completed",

     "cloud" : {
       “env_name”: “Name”,
       “handler_url”: “url”,
       “Cloud_ver”: [version],
       “metadata” : {
           // custom metadata added by the manager of that env...
       }
       // Example how the above could look for JaaS Notebooks
       “Env_name”: "gcp notebook",
       “handler_url”: “http://notebooks.google.com/deploy_notebook”,
       “cloud_ver”: 0.3,
       “metadata”: {
             // format: [flavor].[version of the flavor].[version of base it has been built on top of]
         "environment_version":"DLVM env string (e.g. ‘tf-gpu.1-13.m24’)",
         //"image":"image name",
         "container": "container path", // might not be necessary
         "machine_configuration" : 
            "TBD: some way to specify what the machine hardware sould be"
       } ,
     },

     // Rough thoughts below that won't work as-is, will need to be 
     // fleshed out better later
     //
     // This should make it easier to share public code.  Will prob need
     // to modify this to handle git repos which require auth
     "git" : {
       // This would be set to the repo's origin path by default
       "path": 
        "path go git repro where source code should be downloaded from. ",
       // set to the git repo's current HEAD.  This will probably need to
       // use tags and integrate with "git commit" commands so that the 
       // saved notebook can also be part of the commit
       //
       // This section is a POC only, not to be implemented just yet :)
       "commit id": "commit id/hash, to ensure consistency"
     }
   }
 },
 "nbformat": 1,
 "nbformat_minor": 2
}
```
