# Classr SDK for Python
Use microclassifiers in the cloud for spam detection, sentiment analysis and more.

![Classr logo](./logo.svg)

## Requirements

- Python 3.6 or newer

## Installation

The Classr SDK for Python can be installed using `pip`:

```sh
pip install classr
```

## Usage

Initiaize your microclassifier by passing its UUID to the `Classr` constructor like so:

```python
from classr import Classr

# Initialize cloud microclassifier.
classifier = Classr('acd78708-850b-4cea-aeaa-23cec50d13b6')
```

Now, call the `classify` or `get_info` functions of `classifier` to make use of it:

```python
# Classify unseen input.
document = input('Enter your input: ')
print(f'Predicted class: {classifier.classify(document)}')

# Print macro F1 score of classifier.
info = classifier.get_info()
print(f'Classifier macro F1 score is: {info.f1_score}')
```

If you'd like to use a self-hosted deployment of the Classr application (i.e. not the default official API), you can
pass a different base URL when constructing your `Classr` object:

```python
from classr import Classr

# Initialize cloud microclassifier.
classifier = Classr('acd78708-850b-4cea-aeaa-23cec50d13b6', 'https://self-hosted-classr.example.com/')
```

## Related Projects

This SDK is for the official [Classr application](https://github.com/lambdacasserole/classr) (but will work with a
self-hosted deployment too, of course).

## License

[MIT](LICENSE) © [lambdacasserole](https://github.com/lambdacasserole).
