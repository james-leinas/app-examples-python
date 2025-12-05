# Custom Code in Automation Designer
This repository contains Python snippets compatible with the Custom Code feature in Automation Designer. This feature allows users to execute Python logic directly within Benchling Analysis.

![image info](./snippets/plot-chromatogram/docs/Example_Chromatogram_Plot.gif)

## Overview
These examples demonstrate how to extend Benchling's native capabilities using Python scripts within the Automation Designer context. They cover common use cases such as data visualization, file handling, and complex data transformations.

## Key Capabilities
The code examples included in this directory cover the following functionalities:

- Visualizations: Create custom charts, graphs, and annotations (e.g., chromatograms).

- File Parsing: Logic to read and parse various file formats.

- File Creation: Generate new files, such as instruction lists for laboratory instruments.

- Data Transformation: Apply transformations, merge/join datasets, and perform complex calculations on data.

## Dependencies
See [requirements.txt](./requirements.txt) for the specific library versions used in these examples.

## Constraints & Limitations
When adapting these examples for your tenant, please note the current beta limitations:

 - Runtime Limit: Execution is limited to 15 minutes per run.

 - No Network Access: The environment does not support general network access.

 - Fixed Packages: You cannot install custom libraries (e.g., via `pip`). You are limited to the pre-installed packages listed above

 - No API Access: The Benchling SDK/API is not currently supported within the execution environment.

 - Bring your own Container: BYOC is not supported; code runs in the standard Benchling runtime environment

 - Lifecycle Management: The feature does not currently support native GitHub integration or versioning within the UI.