import os
import shutil
import random

source_dir = 'data/MO_94'
target_dir = 'data/organized'
train_dir = os.path.join(target_dir, 'train')
test_dir = os.path.join(target_dir, 'test')

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

if not os.path.exists(train_dir):
    os.mkdir(train_dir)

if not os.path.exists(test_dir):
    os.mkdir(test_dir)

for dir in [train_dir, test_dir]:
    for cat in ['edible', 'non-edible', 'toxic']:
        if not os.path.exists(os.path.join(dir, cat)):
            os.mkdir(os.path.join(dir, cat))

mapping = {}
for cat in ['edible', 'non-edible', 'toxic']:
    with open('data/mapping/'+cat+'.txt') as f:
        mapping[cat] = [s.strip() for s in f.readlines()]

images_paths = {
    "edible": [],
    "non-edible": [],
    "toxic": []
}
for dir in os.listdir(source_dir):
    species_dir = os.path.join(source_dir, dir)
    for cat in ['edible', 'non-edible', 'toxic']:
        if dir in mapping[cat]:
            for filename in os.listdir(species_dir):
                images_paths[cat].append(os.path.join(species_dir, filename))

for cat in ['edible', 'non-edible', 'toxic']:
    test_set_size = int(len(images_paths[cat]) * 0.2)
    test_files = random.sample(images_paths[cat], test_set_size)
    train_files = [file for file in images_paths[cat] if file not in test_files]
    for file in test_files:
        shutil.copy(file, 'data/organized/test/'+cat)
    for file in train_files:
        shutil.copy(file, 'data/organized/train/'+cat)