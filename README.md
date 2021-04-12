# Introduction

This is the artifact for the paper *CodeDJ: Reproducible Queries over Large-Scale Software Repositories* submitted to ECOOP 2021. The artifact consists of three parts:
- **Getting started** A walkthrough through the setting up the system from scratch and executing queries;
- **Query submission** A presentation of our mechanism query submission scheme; and
- **Experiment** A re-creation of the experiment from the paper.

## Paper Details

**CodeDJ: Reproducible Queries over Large-Scale Software Repositories**

Petr Maj. CTU Prague.  
Konrad Siek. CTU Prague.  
Alexander Kovalenko. CTU Prague.   
Jan Vitek. CTU Prague and Northeastern.  

**Abstract** Analyzing massive code bases is a staple of modern software
engineering research – a welcome side-effect of the advent of large-scale
software repositories such as GitHub. Selecting projects to analyze is a
labor-intensive process that can lead to biased results if the chosen projects
are not representative. One issue is that the interface exposed by software
repositories only allows formulation of the most basic of queries. Code DJ is an
infrastructure for querying repositories composed of a persistent datastore,
constantly updated with data acquired GitHub, and an in-memory database with a
Rust query interface. Code DJ supports reproducibility, historical queries are
answered deterministically using historical states of the datastore; thus
researchers can reproduce published results. To illustrate the benefits of Code
DJ , we identify biases in the data of a published study and, by repeating the
analysis with new data, we demonstrate that its conclusions were sensitive to
the choice of projects.

## Part 1: Getting started

## Part 2: Query submission

## Part 3: Experiment


