# Benchling App Python Examples

The `examples/` directory contains Benchling App samples written by Benchling.

## custom-code-in-automation-designer
Example snippets of code that can be utilized in a Custom Code step of the Automation-Designer with Benchling Analysis.

![image info](./examples/custom-code-in-automation-designer/docs/Example_Chromatogram_Plot.gif)

**Code Includes:**
* Custom Code to create visualizations (charting/annotations)
* Custom Code to parse files 
* Custom Code to create a new file (e.g instruction for instruments)
* Custom Code to apply transformations, merging/joining, and/or calculations of dataset(s)


## chem-sync-local-flask

Demonstrates creating a custom UI in Benchling allowing users to search for 
molecules from [PubChem](https://pubchem.ncbi.nlm.nih.gov/) and sync them into Benchling.

Uses [Cloudflare-tunnel](https://www.cloudflare.com/products/tunnel/) and [Docker](https://www.docker.com/) to receive webhooks 
in a local development environment running [Flask](https://flask.palletsprojects.com/) with the 
[Benchling SDK](https://docs.benchling.com/docs/getting-started-with-the-sdk).

![image info](./examples/chem-sync-local-flask/docs/demo-short.gif)

**Code Includes:**
* Benchling App Authentication via [Client Credentials](https://docs.benchling.com/docs/getting-started-benchling-apps#getting-credentials)
* Custom UI via [App Canvas](https://docs.benchling.com/docs/introduction-to-app-canvas)
* User Feedback via [App Status](https://docs.benchling.com/docs/introduction-to-app-status)
* Data Mapping via [App Config](https://docs.benchling.com/docs/app-configuration)
* Receiving and verifying [Webhooks](https://docs.benchling.com/docs/getting-started-with-webhooks)
* Creating [molecule custom entities](https://benchling.com/api/reference#/Molecules/createMolecule)