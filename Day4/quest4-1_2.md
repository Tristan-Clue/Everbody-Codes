You have a list of numbers like this

> 10 7 13 6

Each number represents the number of "teeth" of the given gear.

Each gears are connected to each other and turned by the windmill.

So for an example for this combination:

> 128 64 32 16 8

The second gear (64) has half as many teeth as the first one (128). For this reason, for every full turn of the first gear, the second gear will make two full turns.

The same relationship occurs between successive pairs of gears. The gear (32) will therefore turn twice for one turn of the gear (64) and thus 4 times for each turn of the gear (128).

Analysing the movement of gears (16) and (8) analogously, it can be observed that for each single turn of gear (128), the last gear (8) will make exactly 16 full turns.

Multiplying 16 by 2025 (the number of full turns of the first gear) gives you the final result for this example: `32400` 


So for the solution of **Question 1**:

> 1000 975 952 931 914 900 897 880 872 853 842 833 815 807 797 779 754 753 746 745 721 706 687 666 648 624 596 579 565 539 534 523 499 477 469 455 426 403 378 374 364 352 336 331 312 287 263 238 213 189
(Phew, that's a lot of numbers)

Get the number of ticks for the **1st** gear, which is `1000 * 2025`, then divide it by the **last** gear, which will be `2025000 / 189`.

This will give you a final answer of `10714 cycles`!

As for **Question 2**, we need to find what's the minimum cycles the first gear has to make to make the last gear turn at least **10 trillion times** (10,000,000,000,000).

As for the solution:

> 967 963 954 938 936 929 905 901 880 853 826 825 822 807 806 798 794 769 742 720 707 702 699 690 678 667 648 626 605 589 584 567 543 521 503 486 475 446 443 438 419 411 402 397 369 351 335 317 312 288

Multiple the the ticks of the **last** gear by 10 trillion, then divide it by the ticks of the **first** gear.
The other way round of Question 1.

The final answer would be `2978283350569`
