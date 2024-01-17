# Deep Learning - LLM Assignment

Raichman Univercity

## Introduction

In this assignment I implemented generative text model with a deep multilayer RNN network based on GRU from **scratch** . The GRU was trained on a corpus of Shakespeare books and then I generate my own work ;). 
Got accuracy of 63% on test set

## General Guidelines

- This assignment requires running on GPU-enabled hardware. The run in the notebook done in google colab. Use the `checkpoint` to download the trained model back to your computer for inference and submission.
- The repo is based on a assigment as part of the DEEP LEARNING course at Reichman University
  
## Contents
- [Sequence Models](#part1)
    - [Text generation with a char-level RNN](#part1_1)
    - [Obtaining the corpus](#part1_2)
    - [Data Preprocessing](#part1_3)
    - [Dataset Creation](#part1_4)
    - [Model Implementation](#part1_5)
    - [Generating text by sampling](#part1_6)
    - [Training](#part1_7)
    - [Generating a work of art](#part1_8)
