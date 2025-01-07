
# ASD Tracking Challenges


## Overview

** MOT  Evaluation on Autism Application**


## Usage

1. **Apply a tracking method on Your Input Video**

Set the class parameter for object detectors to detect only the 'person' class (class number 0).

To use the **MOTR algorithm**, clone it from (https://github.com/megvii-research/MOTR.git).

To use the **ByteTrack algorithm**, clone it from (https://github.com/ifzhang/ByteTrack.git).

To use the **StrongSORT algorithm**, clone it from (https://github.com/dyhBUPT/StrongSORT.git).

To use the **OC-SORT algorithm**, https://github.com/noahcao/OC_SORT.git

To use the **DeepSORT algorithm**, clone it from (https://github.com/nwojke/deep_sort.git).

To use the **FairMOT algorithm**, clone it from (https://github.com/ifzhang/FairMOT.git).


To use the **DragonTrack algorithm**, clone it from (https://github.com/ostadabbas/DragonTrack.git).



2. **Adjust the lable format **

   Save the GT and output label in this fromat:
    ```bash
   <frame>, <id>, <bb_left>, <bb_top>, <bb_width>, <bb_height>, <conf>, <class>
    ```

   
4. ** Validation **
   
   
     ```bash
     python validation.py 
     ```


## Results

### Performance on ASD Test Set
| Tracker                       | MOTA ↑   | IDF1 ↑   | IDS      |
|-------------------------------|----------|----------|----------|
| FairMOT                  | 57.9     | 40.3   | 401   | 
| MOTR                       | 58.3      | 47.8| 398| 
| DeepSORT                    | 60.0 | 44.6    | 369    | 
| StrongSORT                   | 60.1     | 48.1    | 358   | 
| ByteTrack                    | 62.2    | 53.0   | 317  | 



## Citation

If you find the ASD paper useful in your research, please consider citing our work:
```
@inproceedings{amraee2025asd,
  title={ “Advancing multi- person tracking for autism behavior analysis: Challenges, opportunities, and future directions in clinical settings,”},
  author={S. Amraee, E. B. Mallo, D. Erdogmus, A. McCullough, M. Goodwin, and S. Ostadabbas},
  booktitle={in Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision Workshops (WACVW), Feb. 2025.},
  year={2025},
}
```

---


