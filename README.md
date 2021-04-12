# Introduction

This is the artifact for the paper *CodeDJ: Reproducible Queries over Large-Scale Software Repositories* submitted to ECOOP 2021. The artifact consists of three parts:
- **Getting started** A walkthrough through the setting up the system from scratch and executing queries;
- **Query submission** A presentation of our mechanism query submission scheme; and
- **Experiment** A re-creation of the experiment from the paper.

## Paper details

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

This part describes setting up the CodeDJ system from scratch, downloading a dataset, and running a query.

Prerequisites:

- [git](https://git-scm.com/), 
- [Rust and cargo](https://www.rust-lang.org/tools/install), 
- TODO libs.

In order to download projects from GitHub Parasite requires the user have a GitHub account and a personal access token. You can generate a token for your GitHub account by following the instructions [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). The token does not need any scopes or permissions.

### Setup

Downloading and building Parasite (the GitHub dataset downloader):

```
git clone https://github.com/PRL-PRG/codedj-parasite.git parasite
cd parasite
cargo build --release
cd ..
```

Downloading and building Djanco (the query engine):

```
git clone https://github.com/PRL-PRG/djanco.git 
cd djanco 
cargo build --release
cd ..
```

### Downloading a toy dataset

We explain how to download a small 10-project dataset using Parasite. We also provide a pre-downloaded repository in `toy-dataset-predownloaded` so this step can be skipped.

To create a basic dataset, first create a directory that will contain the downloaded. Be aware that datasets tend to be large. 

```
mkdir -p toy-dataset/
```

Next, specify the list of repositories to include in the dataset in a CSV file. The toy dataset will contain the following 10 repositories (4 Python, 4 JavaScript, and 2 TypeScript repositories):

```
repository
https://github.com/nodejs/node.git
https://github.com/pixijs/pixi.js.git
https://github.com/angular/angular.git
https://github.com/apache/airflow.git
https://github.com/facebook/react.git
https://github.com/vuejs/vue.git
https://github.com/xonsh/xonsh.git
https://github.com/meteor/meteor.git
https://github.com/3b1b/manim.git
https://github.com/s0md3v/photon.git
```

This file is located at `toy-dataset-repositories.csv`.

Then, feed the list of repositories to Parasite:

```
parasite/target/release/parasite --datastore toy-dataset add toy-dataset-repositories.csv
```

Next, create a CSV file containing one of more [GitHub personal access tokens](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token). No special scopes or permissions are needed on the token. These are used to download data using the GitHub REST API and are essential for the downloader to work.

```
token
fa56454....
```

We cannot provide a file with these for presentation purposes. We assume the reader prepares their own token file in the current directory at `ghtokens.csv`.

The next step is to enter interactive console in Parasite. Provide a path to the GitHub token file via the ght flag. You can also specify the number of threads that the downloader will use with the n flag (here we use 8).

```
parasite --datastore toy-dataset -ght ghtokens.csv -n 8 --interactive
```

![](img/interactive.png)

In interactive console: execute the loadall command to load substore information into memory.

```
> loadall
```

![](img/loadall.png)

Then, also in *interactive* console: execute `updateall` to start the
downloader. This will cause Parasite to download, process and store information
about each added repository using 8 threads.

```
 > updateall
 ```

Wait until the download completes (about 15 minutes for the example dataset).
Exit the downloader (`^C`). The example dataset is ready for querying. 

### Running a query



## Part 2: Query submission

## Part 3: Experiment


