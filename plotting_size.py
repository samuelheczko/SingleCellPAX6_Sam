import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
import glob


##uncomment for toy data set - sam's mac
path_main = "../.."
path_plot = path_main + '/plots/'



cell_lines = ['nas2m','nas2s','d5','e8']
file_paths = {}
data_frames = {}


for line in cell_lines:
    file_paths[line] = glob.glob(path_main + f'/organoid_images/csvs/Organoid_Morphology-*{line}*.csv')
    data_frames[line] = pd.DataFrame()
    for days in file_paths[line]:
        day = days.split('-')[-1].split('.')[0]
        data_frame = pd.read_csv(days)
        data_frame.insert(0, 'day', day)
        data_frames[line] = pd.concat([data_frames[line],data_frame])
        
    data_frames[line]


full_df = pd.DataFrame()
for df in data_frames:
    data_frames[df]['line'] = df
    full_df = pd.concat([full_df,data_frames[df]])

#/Users/samuelheczko/Documents/School/phd/mini-projects/chans_data/organoid_images/csvs

full_df['day'] = full_df['day'].str.replace('d', '', regex=True).astype(int) ##take the day as intreger

sns.catplot(
    data=full_df.sort_values(by="day"), 
    x="day", 
    y="Area [um^2]",
    hue = 'line',
    kind="point")

plt.show()