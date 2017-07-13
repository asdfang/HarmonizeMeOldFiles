import matplotlib.pyplot as plt, matplotlib, numpy as np
'''
# Random test data
#np.random.seed(123)
#all_data = [np.random.normal(0, std, 100) for std in range(1, 4)]

data0 = np.random.rand(15) * 20
data0 += 25

data1 = np.random.rand(15) * 20
data1 += 80

data2 = np.random.rand(15) * 15
data2 += 65
'''

'''
#FEMALE:
YIN_all_pitches_percent_correct = [60.0, 33.33333333333333, 56.25, 66.66666666666666, 6.666666666666667, 7.6923076923076925, 21.052631578947366, 0.0, 0.0, 0.0, 0.0, 0.0, 28.57142857142857, 0.0, 60.0]
YIN_all_onsets_recall = [100.0, 100.0, 100.0, 100.0, 93.33333333333333, 100.0, 100.0, 100.0, 100.0, 100.0, 57.14285714285714, 80.0, 85.71428571428571, 100.0, 90.0]
YIN_all_onsets_precision = [17.857142857142858, 3.488372093023256, 16.49484536082474, 3.1578947368421053, 25.0, 19.696969696969695, 20.43010752688172, 5.714285714285714, 4.838709677419355, 16.883116883116884, 44.44444444444444, 4.166666666666666, 6.976744186046512, 20.689655172413794, 10.465116279069768]

aubio_all_pitches_percent_correct = [60.0, 33.33333333333333, 50.0, 33.33333333333333, 13.333333333333334, 0.0, 15.789473684210526, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 16.666666666666664, 50.0]
aubio_all_onsets_recall = [100.0, 100.0, 43.75, 0, 6.666666666666667, 23.076923076923077, 42.10526315789473, 25.0, 66.66666666666666, 23.076923076923077, 14.285714285714285, 0, 0, 16.666666666666664, 100.0]
aubio_all_onsets_precision = [100.0, 100.0, 100.0, 0, 100.0, 100.0, 57.14285714285714, 50.0, 50.0, 75.0, 100.0, 0, 0, 33.33333333333333, 23.809523809523807]

essentia_all_pitches_percent_correct = [70.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
essentia_all_onsets_recall = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
essentia_all_onsets_precision = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
'''


#MALE:
YIN_all_pitches_percent_correct = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.090909090909092, 0.0, 12.5, 0.0, 0.0, 0.0, 0.0, 5.555555555555555]
YIN_all_onsets_precision = [100.0, 77.77777777777779, 100.0, 100.0, 93.33333333333333, 87.5, 88.88888888888889, 100.0, 100.0, 70.0, 75.0, 88.88888888888889, 83.33333333333334, 62.5, 100.0, 83.33333333333334]
YIN_all_onsets_recall = [15.0, 10.44776119402985, 17.5, 21.568627450980394, 18.666666666666668, 24.137931034482758, 23.52941176470588, 9.615384615384617, 14.473684210526317, 14.285714285714285, 15.0, 28.57142857142857, 20.833333333333336, 9.803921568627452, 19.230769230769234, 12.0]

aubio_all_pitches_percent_correct = [0.0, 0.0, 14.285714285714285, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 20.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
aubio_all_onsets_precision = [100.0, 100.0, 85.71428571428571, 9.090909090909092, 26.666666666666668, 87.5, 55.55555555555556, 80.0, 100.0, 40.0, 62.5, 11.11111111111111, 16.666666666666664, 12.5, 73.33333333333333, 66.66666666666666]
aubio_all_onsets_recall = [100.0, 90.0, 85.71428571428571, 33.33333333333333, 100.0, 70.0, 62.5, 80.0, 73.33333333333333, 40.0, 83.33333333333334, 50.0, 66.66666666666666, 100.0, 64.70588235294117, 19.35483870967742]

essentia_all_pitches_percent_correct = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
essentia_all_onsets_precision = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
essentia_all_onsets_recall = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]



all_pitch = []
all_pitch.append(aubio_all_pitches_percent_correct)
all_pitch.append(essentia_all_pitches_percent_correct)
all_pitch.append(YIN_all_pitches_percent_correct)

all_onset_correct = []
all_onset_correct.append(aubio_all_onsets_recall)
all_onset_correct.append(essentia_all_onsets_recall)
all_onset_correct.append(YIN_all_onsets_recall)

all_onset_false = []
all_onset_false.append(aubio_all_onsets_precision)
all_onset_false.append(essentia_all_onsets_precision)
all_onset_false.append(YIN_all_onsets_precision)


fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 30))

#add space between the plots
fig.subplots_adjust(wspace=.50)

bplot0 = axes[0].boxplot(all_pitch,
                         vert=True,   # vertical box aligmnent
                         patch_artist=True)   # fill with color

bplot1 = axes[1].boxplot(all_onset_correct,
                         vert=True,   # vertical box aligmnent
                         patch_artist=True)   # fill with color

bplot2 = axes[2].boxplot(all_onset_false,
                         vert=True,   # vertical box aligmnent
                         patch_artist=True)   # fill with color

# fill with colors
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot0, bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)

# adding horizontal grid lines
axes[0].set_title('Pitch Detector Accuracy')
axes[0].yaxis.grid(True)
axes[0].set_ylim([-10, 110])
axes[0].set_xticks([y+1 for y in range(len(all_pitch))], )
axes[0].set_xlabel('Pitch Detection Method')
axes[0].set_ylabel('Percent correct (%)')

axes[1].set_title('Onset Detector Accuracy (Recall)')
axes[1].set_xticks([y+1 for y in range(len(all_onset_correct))], )
axes[1].set_xlabel('Onset Detection Method')
axes[1].set_ylabel('Recall (%)')
axes[1].yaxis.grid(True)
axes[1].set_ylim([-10, 110])

axes[2].set_title('Precision')
axes[2].set_xticks([y+1 for y in range(len(all_onset_false))], )
axes[2].set_xlabel('Onset Detection Method')
axes[2].set_ylabel('Precision (%)')
axes[2].yaxis.grid(True)
axes[2].set_ylim([-10, 110])

# add x-tick labels
plt.setp(axes, xticks=[y+1 for y in range(len(all_pitch))],
         xticklabels=['Aubio', 'Essentia', 'Tunescribe'])
for line in bplot0['medians']:
    x, y = line.get_xydata()[0] # top of median line
    axes[0].text(x+.15, y+.25, 'median: %.2f' % y, verticalalignment='center') # draw above, centered
for line in bplot1['medians']:
	x, y = line.get_xydata()[0] # top of median line
	axes[1].text(x-.35, y-.5, 'median: %.2f' % y, verticalalignment='center') # draw above, centered
for line in bplot2['medians']:
    x, y = line.get_xydata()[0] # top of median line
    axes[2].text(x+.35, y-.25, 'median: %.2f' % y, verticalalignment='center') # draw above, centered


plt.show()