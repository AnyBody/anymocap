# AnyMoCap

The AnyMoCap model is an effort to create a simple and unified framework for 
doing any kind of mocap analysis with the [AnyBody Modeling System](http://anybodytech.com). 


Current motion caputure model examples in the [AnyBody Managed Model Repository (AMMR)](http://anybodytech.com/software/ammr)
are releative complex and quite difficult to understand for new users. 

The reason is that the MoCap models are different from the other examples models in the AMMR. Most importantly, MOCAP models
usually require an over-determinate kinematic solver to handle the excess in information that the optical markers provide. 
The over-determinate solver in AMS works great, but it can only find velocities and accelerations numerically. 
That has some performance issue when running inverse dynamics analysis. To overcome the problem, the MOCAP analysis is split into a
two-step producedure. 

![image](https://cloud.githubusercontent.com/assets/1038978/24096596/92051708-0d62-11e7-9cdd-360fc4b28339.png)

The overdeterminate kinematic analysis solves the model for positions, and writes joint angles to a a set of files. 
These joint angles can then be used with the determinate kinematic solver in the inverse dynamic analysis. 

## Model structure.

The AnyMoCap framwork contains two main folder `Examples` and `Model`. 

```
AnyMoCap\
├───Model
├───Examples
│   ├───ABTstandardLE
│   ├───ExternalDesVar
│   ├───force_plate_offset
│   ├───gait_cycle_abscissa
│   ├───IndividualMarkerCutoffFrequency
│   ├───InitialPosExample
│   ├───MarkerWeightExample
│   ├───Plug-in-gait
│   ├───SQUAT
│   └───Static_Dynamic_Trials
```

The core of the framework is located under `Model`. The core files will eventually
become part of the AMMR, and you shouldn't need to change these files unless you want to help improve the AnyMoCap framework (See "Contributing" below.)

The `Examples` folder contains examples of how to use the framework. These Examples are equvivalent to the examples in the AMMR. 




