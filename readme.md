# py_lopatin

## Description
Create a burial history of geological formation based on age and formation thickness...

## Input Data
You can edit in input.in file using Notepad (or related app) and edit some features.
```py
8                                     # number of formations
Dahor                                 # 1st formation name 
Warukin Atas                          # 2nd formation name
Warukin Tengah                        # 3rd formation name
Warukin Bawah                         # 4th formation name
Berai Atas			      # 5th formation name
Berai Masif			      # 6th formation name
Tanjung Atas                          # 7th formation name
Tanjung Bawah                         # 8th formation name
1.6 8 11.6 12.5 15.2 20 36 46 54      # age of formation (in list of float number)
950 0 0 0 0 0 0 0 0                   # thickness of formation #1 based on age input'd
1038 1238 0 0 0 0 0 0 0               # thickness of formation #2 based on age input'd
457 484 631 0 0 0 0 0 0
804 830 941 1077 0 0 0 0 0
492 507 559 605 812 0 0 0 0
600 614 656 689 796 997 0 0 0
550 560 585 603 653 718 941 0 0
400 406 422 433 459 489 562 759 0    # ...etc until 8th formation
```

## Running and simulation graph
Run in terminal
```bash
python lopatin.py < input.in
```
