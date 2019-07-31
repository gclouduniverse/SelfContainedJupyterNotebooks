This file includes rest of the standard that yet to be migrated to the schema.

# Metadata Format
```
{
 "cells": [],
 "metadata": {
   "environment" : {    
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
