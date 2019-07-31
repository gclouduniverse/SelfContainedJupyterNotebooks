# Standard Way Of Representing Environment For A Notebook
This repository contains json.schema that can be used to embed informaiton about the environment that is enough to make notebook reproducible. Plese look on the revisions list to check what exactly is stored by a specific version of the schema.

# Limitations 

1. Scope limited to specifying the notebook's environment.  
    * Out of scope: including local files that the notebook may depend on (though we could get some files by linking to a public git repo)
