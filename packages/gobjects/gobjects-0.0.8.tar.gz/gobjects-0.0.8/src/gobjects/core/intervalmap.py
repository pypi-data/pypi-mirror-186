# File Name: intervalmap.py
# Created By: ZW
# Created On: 2023-01-15
# Purpose: defines IntervalMap structure which allows efficient searching of 
#   contiguous bed-like or gtf-like intervals with a supplied query interval

# module imports
# ----------------------------------------------------------------------------
from collections import OrderedDict

# class definitions
# ----------------------------------------------------------------------------
# define a class IntervalMap which acts as a searchable hashtable
# like structure in which to store contiguous intervals for searching
# intersections against. each child node is either of type 
#
#           root
#            |
#       /    |     \
#    chr1  chr2  .. chrN
#    / |    / |      / |
#   A  B   C  D      E  F

class IntervalNode:
    def __init__ (self, chrom, intervals, isSorted=False):
        self.chrom = chrom
        self.intervals = intervals
        self.zero_idx_start = None
        self.zero_idx_end = None
        self._set_bounds(isSorted=isSorted)

    def _set_bounds(self, isSorted):
        if not isSorted: self.intervals.sort()
        self.zero_idx_start = self.intervals[0].zero_idx_start
        self.zero_idx_end = max([i.zero_idx_end for i in self.intervals])


class IntervalMap:
    def __init__ (self, interval_list, interval_list_sorted=False, subnodes=20):
        self.interval_list_sorted = interval_list_sorted
        self.subnodes = subnodes
        self._map = OrderedDict()
        self.create_map(interval_list, interval_list_sorted)

    def create_map(self, interval_list, isSorted):
        print(f"Building Interval Map for {len(interval_list)} contiguous objects..")
        ilist = sorted(interval_list) if not isSorted else interval_list
         # place the intervals into a chromosome level map
        for i in ilist:
            if i.chrom not in self._map.keys(): self._map[i.chrom] = [i]
            else: self._map[i.chrom].append(i)

        # for each chromosome, divide intervals into self.subnodes bins
        for chrom in self._map.keys():
            clist = self._map[chrom]
            intervals_per_node = int(len(clist) / self.subnodes)
            if intervals_per_node < 1: 
                self.subnodes = len(clist)
                intervals_per_node = 1
            bins = []
            for bin_num in range(self.subnodes):
                node = IntervalNode(chrom, clist[:intervals_per_node], isSorted=True)
                clist = clist[intervals_per_node:]
                bins.append(node)
            if len(clist) > 0:
                bins[-1].intervals.extend(clist)
                bins[-1]._set_bounds(isSorted=True)
            self._map[chrom] = bins

    # define external accessor function for the map
    def get_map(self): return self._map