# Activities of Daily Living - Machine Learning
> Contains data preprocessing and visualization methods for ADL datasets.

![PyPI version](https://img.shields.io/pypi/v/pyadlml?style=flat-square)
![Download Stats](https://img.shields.io/pypi/dd/pyadlml?style=flat-square)
![Read the Docs (version)](https://img.shields.io/readthedocs/pyadlml/latest?style=flat-square)
![License](https://img.shields.io/pypi/l/pyadlml?style=flat-square)
<p align="center"><img width=95% src="https://github.com/tcsvn/pyadlml/blob/master/media/pyadlml_banner.png"></p>
Activities of Daily living (ADLs) e.g cooking, working, sleeping and device readings are recorded by Smart 
Home inhabitants. 

The objective is to predict inhabitants activities using the device readings.
Pyadlml offers an easy way to fetch, visualize and preprocess common datasets. Furthermore 
a pipeline and TODO

## !! Disclaimer !!
Package is still an alpha-version and in active development. 
Consequently, things are going to change and break and may not work at all. 
Nevertheless, feel free to take a look the package and use what is already finished.

## Last Stable Release
```sh 
$ pip install pyadlml
```
## Latest Development Changes
```sh
$ git clone https://github.com/tcsvn/pyadlml
$ cd pyadlml
$ pip install .
```

## Usage example

```python
from pyadlml.dataset import fetch_amsterdam

# Fetch dataset
data = fetch_amsterdam()
df_activites = data['activities']
df_devices = data['devices']

# Plot an inhabitants activity density distribution over one day
from pyadlml.plot import plot_act_density

plot_act_density(df_activities).show()

# Create a vector of smart home device states and discretize the event data in 20 second bins
from pyadlml.preprocessing import StateVectorEncoder, LabelEncoder

sve = StateVectorEncoder(encoding='raw', dt='20s')
raw = sve.fit_transform(df_devices)

# Label the datapoints with the corresponding activity
lbls = LabelEncoder().fit_transform(df_activities, raw)

X = raw.values
y = lbls.values

# Proceed with machine learning techniques you already know
from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X, y)
...
```

_For more examples and how to use, please refer to the [documentation](https://pyadlml.readthedocs.io/en/latest/)
or the [notebooks](https://github.com/tcsvn/pyadlml/notebooks/README.md)._
## Features
  - 12 Datasets
  - Importing data from [Home Assistant]() or [Activity Assistant]()
  - Many visualizations and statistics for devices, activities and their interaction
  - Multiple device representations:
      - Raw
      - Changepoint
      - Lastfired
  - Timeseries sampler
    - Sequential
    - Timeslice
    - Event based
  - Feature extraction for event-times 
  - Cross validation iterators adapted for ADLs

 
### Supported Datasets
  - [x] Amsterdam [1]
  - [x] Aras [2]
  - [x] Casas Aruba (2011) [3]
  - [x] Kasteren House A,B,C [5]
  - [x] MITLab [6]
  - [x] Tuebingen 2019 [7]
  - [x] UCI Adl Binary [8]
  - [ ] Casas Milan (2009) [4]
  - [ ] Casas Cairo [4]
  - [ ] Casas Tokyo [4]
  - [ ] Chinokeeh [9]

## Educational examples, benchmarks and replications
The project includes a leaderboard of current models to the best of knowledge. 
In addition, a lot of models are compared on a cleaned version of all the available datasets. 
Furthermore, there is a useful list of references that is still 
growing on papers to read. 
For all this check out the [notebooks]().


## Contributing 
1. Fork it (<https://github.com/tcsvn/pyadlml/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Related projects
  - [Activity-assistant](https://github.com/tcsvn/activity-assistant) - Recording, predicting ADLs within Home assistant.
  - [Sci-kit learn](https://github.com/sklearn) - The main inspiration and some borrowed source of code.
  
## Support 
[![Buy me a coffee][buy-me-a-coffee-shield]][buy-me-a-coffee]
  
## How to cite
If you are using pyadlml for publications consider citing the package
```
@software{pyadlml,
  author = {Christian Meier},
  title = {PyADLMl - Machine Learning library for Activities of Daily Living},    
  url = {https://github.com/tcsvn/pyadlml},
  version = {0.0.10-alpha},
  date = {2022-11-15}
}
```

## Sources
[1]: T.L.M. van Kasteren; A. K. Noulas; G. Englebienne and B.J.A. Kroese, Tenth International Conference on Ubiquitous Computing 2008  
[2]: H. Alemdar, H. Ertan, O.D. Incel, C. Ersoy, ARAS Human Activity Datasets in Multiple Homes with Multiple Residents, Pervasive Health, Venice, May 2013.  
[3,4]: WSU CASAS smart home project: D. Cook. Learning setting-generalized activity models for smart spaces. IEEE Intelligent Systems, 2011.  
[5]: Transferring Knowledge of Activity Recognition across Sensor networks. Eighth International Conference on Pervasive Computing. Helsinki, Finland, 2010.  
[6]: E. Munguia Tapia. Activity Recognition in the Home Setting Using Simple and Ubiquitous sensors. S.M Thesis  
[7]: Activity Recognition in Smart Home Environments using Hidden Markov Models. Bachelor Thesis. Uni Tuebingen.   
[8]: Ordonez, F.J.; de Toledo, P.; Sanchis, A. Activity Recognition Using Hybrid Generative/Discriminative Models on Home Environments Using Binary Sensors. Sensors 2013, 13, 5460-5477.  
[9]: D. Cook and M. Schmitter-Edgecombe, Assessing the quality of activities in a smart environment. Methods of information in Medicine, 2009
  
## License
MIT  © [tcsvn](http://deadlink)


[buy-me-a-coffee-shield]: https://img.shields.io/static/v1.svg?label=%20&message=Buy%20me%20a%20coffee&color=6f4e37&logo=buy%20me%20a%20coffee&logoColor=white
[buy-me-a-coffee]: https://www.buymeacoffee.com/tscvn
