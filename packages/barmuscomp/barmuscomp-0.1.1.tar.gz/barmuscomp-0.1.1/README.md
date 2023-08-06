# BarMusComp: Encoding songs with linear and nonlinear compression methods to reveal structure #

Hello, and welcome on this repository!

This project aims at compressing all bars in a song, and studies the compressed representations of every bar to infer its structure. It is related to my PhD thesis [1].

This repository contains code for the NTD, PCA, NMF, and Autoencoders (developed in PyTorch), as presented in [2].

This project is an extension of the toolbox as_seg [3], which computes the segmentation of an autosimilarity matrix.

It can be installed with pip using `pip install barmuscomp`.

This is a first release, and may contain bug. Comments are welcomed!

## Software version ##

This code was developed with Python 3.8.5, and some external libraries detailed in dependencies.txt. They should be installed automatically if this project is downloaded using pip.

## Tutorial Notebook ##

3 tutorial notebooks are available in the folder "Notebooks", and present the different compression methods on the song 'Come Together'.

## How to cite ##

You should cite the package `BarMusComp`, available on HAL (https://hal.archives-ouvertes.fr/hal-03782914).

Here are two styles of citations:

As a bibtex format, this should be cited as: @softwareversion{marmoret2022barmuscomp, title={BarMusComp: module for computing barwise compressed representations of music}, author={Marmoret, Axel and Cohen, J{\'e}r{\'e}my and Bimbot, Fr{\'e}d{\'e}ric}, URL={https://gitlab.inria.fr/amarmore/barmuscomp}, LICENSE = {BSD 3-Clause ''New'' or ''Revised'' License}, year={2022}}

In the IEEE style, this should be cited as: A. Marmoret, J.E. Cohen, and F. Bimbot, BarMusComp: module for computing barwise compressed representations of music, 2022, url: https://gitlab.inria.fr/amarmore/barmuscomp.

## Credits ##

Code was created by Axel Marmoret (<axel.marmoret@gmail.com>), and strongly supported by Jeremy E. Cohen (<jeremy.cohen@cnrs.fr>).

The technique in itself was also developed by Frédéric Bimbot (<bimbot@irisa.fr>).

## References ##
[1] A. Marmoret, "Unsupervised Machine Learning Paradigms for the Representation of Music Similarity and Structure", Ph.D. dissertation, Université de Rennes 1, 2022.
(not uploaded yet but will be soon! You should check the website hal.archives-ouvertes.fr/ in case this README is not updated with the reference.)

[2] A. Marmoret, J.E. Cohen, and F. Bimbot, "Barwise Compression Schemes for Audio-Based Music Structure Analysis"", in: 19th Sound and Music Computing Conference, SMC 2022, Sound and music Computing network, 2022.

[3] A. Marmoret, J.E. Cohen, and F. Bimbot, "as_seg: module for computing and segmenting autosimilarity matrices", 2022, url: https://gitlab.inria.fr/amarmore/autosimilarity_segmentation.