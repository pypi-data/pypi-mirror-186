# What is phybers?

Phybers is a library for Python that integrates multiple tractography and neural-fibers related algorithms. It includes the following modules:

1. **Segmentation**: Fibers segmentation based on a multi-subject atlas. It's purpose is clasifying subject fibers in function of a multisubject-fascicle atlas.

2. **Hierarchichal Clustering**: A hierarchichal clustering algorithm based on euclidean distance between pairs of fibers, originally applied between subjects, as part of an automatic method to identify short fiber fascicles that are reproducibles on a HARDI database.

3. **FFClust**: A intra-subject clustering algorithm based on K-Means between fibers' points. It can be applied to the fibers of the whole brain's tractography. It's objective is creating similar groups of fibers, contingent on its position.

4. **Utils**: The utils module is a compendium of tools used for both the pre-processing of a tractography as well as for evaluating the performance of the clustering and the segmentation. It includes:

    1. Tools for normalization to the MNI space for the HCP database.
    2. Sampling of the fibers to n equidistant points.
    3. The calculation of the intersection between fascicles.
    4. Tools to extract and filter statistics measures over the clustering or segmentation of fibers. Some of the measures extracted are: size, length and inter/intra distance over clusters or fascicles.
    5. Fibervis: A visualization tool for bundles and MRIs.

## What do you need?

For now, phybers only works on Linux. It's currently being worked on for Windows cmd/PowerShell compatibilty.

What you'll need is:

- g++
- gcc
- python >= 3.8 (might work on previous versions, but for compatibility, >= 3.8.8 is recommended.)

## New in version 0.0.6!

Now the utils module includes a visualization tool for bundles, MRIs and more!

# FAQ

## When running the utils' visualization submodule, i get: fatal error: GL/gl.h: No such file or directory

To fix this on LinuxFollow the **Open GL Installation on Linux** section on the following page: https://en.wikibooks.org/wiki/OpenGL_Programming/Installation/Linux

## The utils' visualization submodule tool returns a PyQt5 error.

To solve this in Linux, you will need to upgrade your pip:
 > pip install --user --upgrade pip
Then, manually install PyQt5:
 > pip install PyQt5
