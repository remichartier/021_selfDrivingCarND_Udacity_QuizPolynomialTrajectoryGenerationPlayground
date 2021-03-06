#!/usr/bin/env python

# History
# v00 : initial
# v01 : change delta s=-10 meaning want at target time our vehicle behind by 10.

from ptg import PTG
from helpers import Vehicle, show_trajectory

def main():
	vehicle = Vehicle([0,10,0, 0,0,0])
	predictions = {0: vehicle}
	target = 0
	delta = [-10, 0, 0, 0, 0 ,0]
	start_s = [10, 10, 0]
	start_d = [4, 0, 0]
	T = 5.0
	best = PTG(start_s, start_d, target, delta, T, predictions)
	show_trajectory(best[0], best[1], best[2], vehicle)

if __name__ == "__main__":
	main()