# YOLOv8-SmallObj-Garbage
##  Abstract

With the dramatic increase in the amount of garbage worldwide, garbage
classification and recycling have become a key part of environmental
protection and resource recycling. The aim of this project is to develop
a machine learning-based garbage recognition system for the automatic
classification of daily garbage. We adopt deep learning methods,
especially Convolution Neural Networks to recognize and classify various
kinds of garbage. By collecting and processing a large amount of garbage
image data, we trained a high-precision model and performed several
rounds of optimization on it. Preliminary test results show that the
system can effectively recognize and classify different kinds of garbage
and provide a decision basis for its automatic sorting. The successful
implementation of this system will not only improve the efficiency of
garbage sorting but also encourage society to make more progress in
garbage management and resource recovery.

##  Introduction

Object detection is one of the cornerstone tasks in the field of
computer vision, playing a pivotal role in many contemporary
applications like autonomous driving, medical image analysis, and
automated surveillance. With the growing global garbage, applying object
detection techniques to automated garbage classification becomes
increasingly imperative. While the YOLO series has excelled in various
detection scenarios, the detection of small objects remains a vexing
challenge. In addressing this, we present an augmented YOLO model
tailored for enhanced small object detection. We aim to validate its
efficacy through garbage detection tasks, hoping that it not only boosts
garbage detection accuracy but also brings substantial value to other
related domains. Moreover, advancements in tech-driven sorting, such as
AI and robotics, offer prospects for smart city waste management,
enhancing efficiency and reducing environmental footprints.

##  Input and Output

**Input:** An image containing various types of garbage, potentially
with small objects.

**Output:** Detection labels for the garbage items in the image.

##  Methodology

To tackle small object detection in garbage classification, we’ll test
and compare three primary strategies:

-   *SPD-Conv Module:* Modifying convolution and pooling for better
    feature detail.

-   *SAHI Framework:* A flexible slicing-aided inference pipeline
    tailored for small object detection.

-   *YOLOv8 Enhancements:* Integrating extra prediction heads,
    Involution blocks, and CBAM mechanisms.

##  Related Work

The object detection domain, particularly focusing on small objects, has
been an area of active research. The YOLO series introduced fast and
efficient detection models. However, specific challenges like detecting
smaller objects led to advancements like the SPD-Conv module , the SAHI
framework , and enhancements in YOLOv5 . Our work builds on these
foundations but introduces unique modifications for garbage
classification.

##   Evaluation

-   Assessing the model’s accuracy using the size, mAP, params(M), and
    FLOPs(B).

-   Displaying visual results to provide an intuitive grasp of the
    model’s performance in real-world scenarios, including successful
    and failed detections.

