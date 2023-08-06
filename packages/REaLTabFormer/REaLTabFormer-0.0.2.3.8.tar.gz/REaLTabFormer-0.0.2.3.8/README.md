# DevRealTabFormer


### Upload package to test pypi

```
python setup.py sdist
twine upload --repository testpypi dist/*
```

### Install package from test pypi
```
pip install --upgrade --no-cache-dir --use-deprecated=legacy-resolver -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ REaLTabFormer==0.0.2.3.8
```


### Generating constrained tokens per step
```
    1 -> BOS
    2 -> BMEM or EOS
    3 -> col 0
    ...
    3 + col_size -> col col_size - 1
    3 + col_size + 1 -> EMEM
    3 + col_size + 2 -> BMEM or EOS
    3 + col_size + 3 -> col 0
```


# Using the discriminator callback

We can control the training process to prevent overfitting by using specific constraints and metrics based on a validation data.

In this case, we propose to use a discriminator model to regulate the training process. We first identify the proportion of the full training data that will serve as the validation data. Then, we define the validation steps. For each step that is a multiple of the validation step, we generate synthetic data from the model. Then, we use the generated sample together with the validation data to train the discriminator model and quantify the model's ability to generate realistic samples.

We should note that at the early stages of the model, the model will not be able to generate meaningful observations. This implies that we should at least set a warm-up period before we perform the disciminator-based assessment.
