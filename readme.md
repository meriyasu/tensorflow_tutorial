# Tensorflow Tutorial

## Environment
- venv
- pip

## pip-Package
- tensorflow
- matplotlib

(Following packages, to install scikit-learn)
- scipy
- pandas
- numpy

## caution
TensorBoard cannot function on venv.
When it uses, venv must be deactivated.

## Tensorboard
You need to write the following code to use tensorboard.
This code is to record the log in the directory.

```python
if tf.gfile.Exists('./logdir'):
  tf.gfile.DeleteRecursively('./logdir')
writer = tf.summary.FileWriter('./logdir', sess.graph)
```

Finally, you must write the following code.

```python
merged = tf.summary.merge_all()
...
summary = sess.run(merged)
writer.add_summary(summary, epoch)
```

### graphs
Tensorboard can show computing-graphs.
As much as possible, you had better to name to variable.
How to name to variables is the following code.
You should write the code 'name='xxx'' in the arguments.

```python
X = tf.placeholder(dtype=tf.float32, shape=[None,p], name='X')
```

### histograms
Histogram can show the value of tensor in the variable.
As histogram goes to front, time passes.
The horizontal axis indicates value of the tensor.
The value which focucing in your mouse indicates the value's frequency.

```python
tf.summary.histogram('name', name)
```

### scalars
You can see change of the scalar-value passing time.

```python
tf.summary.scalar('name', name)
```

