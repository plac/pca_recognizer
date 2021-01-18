import cv2
import numpy as np

from os import listdir
from os.path import isfile, join
from random import random

class Person():

  def __init__(self, id, label, data):
    self.id = id
    self.label = label
    self.data = data

  def __str__(self):
    return f'Person [id={self.id}, label={self.label}, data={self.data}]'

class PCA():

  def __init__(self, path, n_samples = 10, min_components = 2, max_components = 30, training_size = 7):
    self.path = path
    self.n_samples = 10
    self.min_components = min_components
    self.max_components = max_components
    self.training_size = training_size

  def load_person(self, path, filename):
      data = filename.split('.')[0].split('_')
      id = int(data[0])
      label = int(data[1])
      img_data = self.get_image_data(join(path, filename))
      person = Person(id, label, img_data)
      #print(person)
      return person

  def get_image_data(self, filepath):
      img = cv2.imread(filepath)
      img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      img = cv2.resize(img, (80, 80), interpolation=cv2.INTER_AREA)
      return img
  
  def load_data(self):
    files = [f for f in listdir(self.path) if isfile(join(self.path, f)) if f.endswith('.jpg')]    
    persons = []

    for file in files:
      persons.append(self.load_person(self.path, file))

    persons.sort(key=lambda x: x.id)

    samples, train, test = [], [], []

    for person in persons:
      samples.append(person)
      if len(samples) == self.n_samples:
        while len(samples) > self.training_size:
            idx = int(random() * len(samples))
            sample = samples[idx]
            test.append(sample)
            samples.remove(sample)

        train.extend(samples)
        samples = []
    return train, test

  def run(self):    
    train = []
    test = []

    train, test = self.load_data()

    for n_components in range(self.min_components, self.max_components+1):
      src, labels = [], []

      model = cv2.face.EigenFaceRecognizer_create(n_components)

      for p in train:
        src.append(p.data)
        labels.append(p.label)

      model.train(src, np.asarray(labels))
      
      test_labels = []
      prediction = []

      for p in test:
        label, confidence = model.predict(p.data)
        test_labels.append(p.label)
        prediction.append(label)

      correct = [ 1 for x,y in zip(prediction, test_labels) if x == y]
      acc = (sum(correct) / len(test_labels)) * 100

      print('{} componentes principais, acurácia: {:.2f}%'.format(n_components, acc))

pca = PCA('./ORL2')
pca.run()