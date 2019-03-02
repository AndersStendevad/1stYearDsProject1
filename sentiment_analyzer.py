from afinn import Afinn
import sys
import statistics
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

afinn = Afinn(language='da')

path = sys.argv[1]


scores = list()
with open(path) as text:
    lines = text.readlines()

    for line in lines:
        score = afinn.score(line)
        if score != 0.0: #excluding neutral scores
            scores.append(afinn.score(line))

plt.hist(scores, bins=[-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])
title = input('area for histogram title:')
plt.suptitle('Sentiment distribution for {}'.format(title))
plt.figtext(.75, .8, "Std dev: {}".format(round(statistics.stdev(scores),2)))
plt.figtext(.75, .75, "Mean: {}".format(round(statistics.mean(scores),2)))
plt.xlabel('sentiment rating')
plt.ylabel('count')
hist_name = input('save histogram as (without extension):')
plt.savefig(hist_name + '.png')