# safeexec

Instructions to set up safeexec can be found in [cemc's safeexec's README.md](https://github.com/cemc/safeexec/blob/master/README.md).

Basically the steps are:

1. Clone the repository and `cd` into it.
2. Run `cmake .` and then `make`.
3. Change user to root: `sudo chown root:root safeexec`.
4. Set sid bit on executable: `sudo chmod u+s safeexec`.
5. Make a symlink to safeexec and place it in OJL3's root directory

Make sure that the partition in which safeexec exists does not have `nosuid` as a mount option.
