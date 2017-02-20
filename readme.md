# AnyMOCAP

The AnyMOCAP model is an effort to create a simple and unified framework for 
doing mocap analysis with the [AnyBody Modeling System](http://anybodytech.com). 


Current MoCap examples in the [AnyBody Managed Model Repository (AMMR)](http://anybodytech.com/software/ammr)
are releative complex and quite difficult to understand for new users. The reason is that the MOCAP models are 
different from the other examples models in the AMMR.

Most importantly, MOCAP models usually require an over-determinate kinematic solver to handle the excess in information that the optical markers provide. 
The over-determinate solver in AMS works great, but it can only find velocities and accelerations numerically. 
That has some performance issue when running inverse dynamics analysis. To overcome the problem, the MOCAP analysis is split into a
two-step producedure. The overdeterminate kinematic analysis solves the model for positions, and writes joint angles to a a set of files. 
These joint angles constitute a determinate set of kinematics drivers, which are then used in the inverse dynamic analysis. 




