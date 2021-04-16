#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LogNorm
from os import listdir
from os.path import isfile, join
get_ipython().run_line_magic('matplotlib', 'inline')


# In[90]:


sns.set(style='white', rc={'figure.figsize':(14,8)}) #24,8 for big one
plt.rcParams.update({'font.size': 42})

MICRO_SIZE = 24#16
SMALL_SIZE = 30#20
MEDIUM_SIZE = 39#26
BIGGER_SIZE = 48#32

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MICRO_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


# In[34]:


ref_FSE = [0.15, 0.23, 0.03, -0.29, -0.07, 0, -0.08, -0.23, -0.01, 0.06, 0.18, -0.15, 0.15, 0.1, -0.15, -0.28, -0.43]


# ### All languages distribution

# In[35]:


frames = []

for i in range(1, 10001):
    temp = pd.read_csv('./ts_by_year/2020/' + str(i)+ "2020_new.csv")

    frames.append(temp[5:])


# In[36]:


ref = pd.read_csv('./reference.csv')[5:]
ref['coef'] = ref_FSE


# In[37]:


df_dist = pd.concat(frames, ignore_index=True, sort=False)
df_dist = pd.concat([df_dist, ref], ignore_index=True, sort=False)
df_dist['split'] = ['ours']*(len(df_dist) - 17) + ['their']*17
df_dist.rename(columns={'Unnamed: 0': 'Language:'}, inplace=True)


# In[84]:


plt.figure(figsize=(28,12))
f = sns.violinplot(x='Language:',
               y='coef',
               data=df_dist,
               width=0.9,
               palette='Greens',
               hue='split',
               split=True
              )
plt.axhline(0, ls='--', color='b')
plt.legend().set_visible(False)
plt.title('')
plt.xlabel(None)
plt.ylabel('Coefficient')
f.set_xticklabels(f.get_xticklabels(), rotation=45)
plt.ylim((-0.7, 0.65))

plt.axhline(0.54, 0.77, 0.82, ls='-', color='black')
plt.text(13.8, 0.52, 'FSE 2014')

plt.savefig("./figures_last/all_languages_subsets.pdf", bbox_inches='tight')
plt.show()


# In[43]:


#plt.savefig("./figures_last/languages_distribution.pdf")


# ### Typescript disctribution over years

# In[12]:


years = range(2013, 2021)


# In[14]:


frames_concat = []

for year in years:
    
    frames = []
    
    print(year)

    for i in range(1, 1001):
        temp = pd.read_csv('./ts_by_year/'+str(year)+ '/' + str(i)+ str(year) + "_new.csv")
        temp['year'] = [int(year)]*len(temp)

        frames.append(temp[21:])
        temp_concat = pd.concat(frames, ignore_index=True, sort=False)
        
    frames_concat.append(temp_concat)


# In[15]:


df_concat = pd.concat(frames_concat, ignore_index=True, sort=False)
df_concat.rename(columns={'Unnamed: 0': 'Language:'}, inplace=True)


# In[16]:


df_ref = pd.DataFrame({'year': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
                       'coef': [-0.43]*8,
                       'Language:': ['Typescript']*8,
                       'check' : ['issue']*8
                      })


# In[17]:


df_concat = pd.concat([df_concat, df_ref], ignore_index=True, sort=False)


# In[18]:


df_concat['check'] = ['all']*(len(df_concat) - 1) + ['issues']


# In[85]:


#colors = ["faded green", "pale red", "windows blue", "amber", "greyish", "dusty purple"]
#sns.palplot(sns.xkcd_palette(colors))

plt.figure(figsize=(24,12))
f = sns.violinplot(x='year',
               y='coef',
               data=df_concat,
               width=0.9,
               split=True,
               hue='check',
               palette='Greens'
              )
plt.axhline(0, ls='--', color = 'black')
plt.legend().set_visible(False)
#plt.title('.TS over time')
plt.xlabel(None)
plt.ylabel('Coefficient')
f.set_xticklabels(f.get_xticklabels(), rotation=45)
plt.text(2.4, -0.6, 'FSE 2014')
plt.ylim((-0.72, 0.6))
plt.axhline(-0.43, 0.0, 1.0, ls='-', color='red')
plt.savefig("./figures_last/ts_subsets_over_time.pdf", bbox_inches='tight')
plt.show()
#plt.axhline(-0.43, 0.065, 0.168, ls='-', color='red')
#plt.axhline(-0.43, 0.188, 0.685, ls='-', color='red')
#plt.axhline(-0.43, 0.690, 0.812, ls='-', color='red')
#plt.axhline(-0.43, 0.815, 1.0, ls='-', color='red')


# In[27]:


#plt.savefig("./figures_last/ts_over_years.pdf")


# ### Smart queries output

# In[66]:


mypath = './outputs/smart_new2/'


# In[67]:


fs = [f for f in listdir(mypath) if isfile(join(mypath, f))]


# In[68]:


#names
ns = ['Stars',
      '50% Experienced',     
      'Experienced Author',
      'Number of Commits',
      'Message Size',      
      'Issues',
      'Touched Files',]


# In[69]:


fs


# In[70]:


files = ['stars.csv',
         'experienced_authors_ratio.csv',
         'experienced_authors.csv',
         'commits.csv',
         'mean_commit_message_sizes.csv',
         'issues.csv',
         'mean_changes_in_commits.csv'
        ]


# In[71]:


#fs = files[0:2]+[files[3]]+[files[5]]+[files[7]]+[files[8]]+[files[10]]


# In[72]:


frames = []

for f in files:
    temp = pd.read_csv(mypath + f)[5:]
    frames.append(temp)


# In[73]:


df_smart = pd.concat(frames, ignore_index=True, sort=False)


# In[74]:


df_smart.rename(columns={'Unnamed: 0': 'Language:'}, inplace=True)


# In[75]:


df_smart['split'] = sum([[f]*17 for f in ns], []) #change to names


# In[76]:


df_smart_sig = df_smart.copy()
df_smart_insig = df_smart.copy()


# In[77]:


df_smart_sig.loc[(df_smart_sig['pVal'] <= 0.05), 'coef'] = 0.0
df_smart_insig.loc[(df_smart_insig['pVal'] > 0.05), 'coef'] = 0.0


# In[78]:


sns.set(style='white', rc={'figure.figsize':(24,8)})
plt.rcParams.update({'font.size': 42})

MICRO_SIZE = 16
SMALL_SIZE = 20
MEDIUM_SIZE = 26
BIGGER_SIZE = 32

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MICRO_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

fig, ax = plt.subplots()

sns.barplot(x='Language:',
               y='coef',
               data=df_smart_sig,
               hue='split',
               #palette='Greens',
               edgecolor='k',
               #color=('blue'),
               ax = ax
              )

sns.barplot(x='Language:',
               y='coef',
               data=df_smart_insig,
               hue='split',
               #palette='Greens',
               edgecolor='k',
               alpha = 1.0,
               ax=ax,
               #legend=False,
               color='white'
              )

sns.barplot(x='Language:',
               y='coef',
               data=df_smart_insig,
               hue='split',
               #palette='Greens',
               edgecolor='k',
               alpha = 0.2,
               ax=ax,
               #legend=False
               #color=('blue'),
              )

plt.xlabel(None)
plt.ylabel('Coefficient')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
plt.xlim((-0.42, 16.43))
#plt.ylim((-0.55, 0.8))

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles[0:len(ns)],
          labels[0:len(ns)],
          frameon=False,
          #loc = "upper right",
          bbox_to_anchor=(0.85, 0.58),
          #loc=2
         ) 


for i in range(9):
    
    ax.axvspan(-0.4 + 2*i, 0.60 + 2*i, facecolor='gray', alpha=0.1)
    
plt.savefig("./figures_last/smart_bars_last.pdf", bbox_inches='tight')
plt.show()


# In[ ]:


#plt.savefig("../figures/smart_bars.pdf")


# ## More violins

# In[47]:


mypath2 = './inputs/artifact-inputs/'
stuff = [f for f in listdir(mypath2) if isfile(join(mypath2, f))]


# In[48]:


stuff


# In[49]:


t = pd.read_csv(mypath2 + 'summary-messages-p.csv')


# In[50]:


df_names = ['summary-full-p.csv',
            'summary-stars-p.csv',
            'summary-expr-p.csv',
            'summary-expa-p.csv',
            'summary-commits-p.csv',
            'summary-messages-p.csv',
            'summary-issues-p.csv',
            'summary-changes-p.csv',
          ]


# In[51]:


names = ['Full dataset',
         'Stars',
         '50% Experienced',     
         'Experienced Author',
         'Number of Commits',
         'Message Size',      
         'Issues',
         'Touched Files'
        ]


# In[52]:


frames = []

for i,f in enumerate(df_names):
    temp = pd.read_csv(mypath2 + f)
    temp['name'] = [names[i]] * len(temp.index)
    frames.append(temp)


# In[53]:


df_full = pd.concat(frames, ignore_index=True, sort=False)


# In[54]:


df_full['plotValue'] = np.log10(df_full.commits)
df_full['name_value'] = ['Commits']*len(df_full.index)


# In[55]:


df_full_age = pd.concat(frames, ignore_index=True, sort=False)


# In[56]:


df_full_age['plotValue'] = np.log10(df_full.age/3600/24+1)
df_full_age['name_value'] = ['Age [days]']*len(df_full.index)


# In[57]:


df_full = pd.concat([df_full, df_full_age], ignore_index=True, sort=False)


# In[93]:


sns.set(style='white', rc={'figure.figsize':(24,14)}) #24,8 for big one
plt.rcParams.update({'font.size': 42})

MICRO_SIZE = 24
SMALL_SIZE = 30
MEDIUM_SIZE = 39
BIGGER_SIZE = 48

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=MICRO_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

flatui = ["#97DBA3", "#FF5733", "#2ecc71", "#e74c3c", "#9b59b6", "#3498db", "#95a5a6", "#34495e"]
sns.set_palette(flatui)

fig, ax = plt.subplots()

ax2 = ax.twinx()

sns.violinplot(x='name',
               y='plotValue',
               data=df_full,
               width=0.9,
               hue='name_value',
               split=True,
               cut = 0,
               #palette='Greens',
               ax=ax
              )

ax.set(ylabel = "$\mathregular{log_{10}}$ (Commits)", xlabel = None)
ax2.set(ylabel = "$\mathregular{log_{10}}$ (Age [days])", xlabel = None)
ax.set_xticklabels(ax.get_xticklabels(), rotation=45)

ax.legend(frameon=True, loc = "upper right") 

ax.set_ylim([-0.1, 5.3])
ax2.set_ylim([-0.1, 5.3])

plt.savefig("./figures_last/commits_vs_age.pdf", bbox_inches='tight')
plt.show()


# In[ ]:



