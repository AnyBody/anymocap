# Lower extremity squat Example

This example show the AnyMoCap frame work applied to squating. The subject scaling and marker optimization is done on a standing reference recording, and the values are then applied two squating trials. 

The data is provided by Maria Jönsson from KTH (Royal Institute of Technology
School of Technology and Health) in Sweeden. 


![StandingRefOptimzation](https://cloud.githubusercontent.com/assets/1038978/24747389/87a99f74-1abc-11e7-8953-6323c0a0334a.gif) ![FlyWheelSquat]https://cloud.githubusercontent.com/assets/1038978/24746857/d3f0b13a-1aba-11e7-8b02-ef7eab1dd260.gif) 

## Structure
The example is structured so each trials has its own folder with a main file (`Main.any`), a file with trial specific data (`TrialSpecificData.any`) and a C3D file. (The C3D files could have been placed together in a separate folder if that was desireable.)

```
│   AnyMoCap.libdef.any
│   BodyModelConfig.any
│   C3DSettings.any
│   ExtraDrivers.any
│   ForcePlates.any
│   LabSpecificData.any
│   MarkerProtocol.any
│   ReadMe.md
│
├───Output\
│
└───Trials\
    │   SubjectSpecificData.any
    │
    ├───FlywheelSquat_1\
    │       FlywheelSquat_1.c3d
    │       Main.any
    │       TrialSpecificData.any
    │
    └───StandingRef_1\
            Main.any
            StandingRef_1.c3d
            TrialSpecificData.any
```



