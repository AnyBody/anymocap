# AnyMOCAP

The AnyMOCAP model is an effort to create a simple and unified framework for 
doing mocap analysis with the [AnyBody Modeling System](http://anybodytech.com). 
The previous Mocap examples in the [AnyBody Managed Model Repository (AMMR)](http://anybodytech.com/software/ammr)
have all been quite difficult to use and understand for new users. The reason is that the MOCAP models are quite 
different from the other examples models in the AMMR. Most importantly, MOCAP models usually require an over-detminate
solver. This because we all the information provided by the optical markers are redundant compared to the degrees of freedom 
of the model. The over-determinate solver in AMS works great, but it can only find velocities and accelerations numerically,
which can be problem when running inverse dynamics analysis. To over come the problem, the MOCAP analysis is split into a
two-step producedure. The overdeterminate kinematic analysis calulcates the odel is split into a


There are number of issues which specific to MOCAP models that is important to handle:

* Use an over-determinate solver
* The need a kinematics and inverse dynamics analysis since the over determinate kinematics can't be 

