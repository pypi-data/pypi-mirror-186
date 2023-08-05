""" The Classr MLaaS SDK.

Authors:
    Saul Johnson (saul.a.johnson@gmail.com)
Since:
    15/01/2021
"""

import json
from uuid import UUID
import urllib.parse
import urllib.request
import urllib.error


DEFAULT_BASE_URL = 'https://www.classr.dev/'
""" The default base API URL (the URL of the official Classr API).
"""


class ClassifierInfo:
    """ Represents a collection of information about a classifier.
    """

    def __init__(self, raw: dict):
        """ Initializes a new instance of a collection of information about a classifier.

        Args:
            raw (dict): The raw dictionary received from a call to the Classr API.
        """
        self.raw = raw

    @property
    def uuid(self) -> str:
        """ The UUID of the classifier.
        """
        return self.raw['uuid']

    @property
    def name(self) -> str:
        """ The name of the classifier.
        """
        return self.raw['name']

    @property
    def description(self) -> str:
        """ The description of the classifier.
        """
        return self.raw['description']

    @property
    def precision(self) -> float:
        """ The macro precision of the classifier.
        """
        return self.raw['precision']

    @property
    def recall(self) -> float:
        """ The macro recall of the classifier.
        """
        return self.raw['recall']

    @property
    def f1_score(self) -> float:
        """ The macro F1 score of the classifier.
        """
        return self.raw['f1Score']

    @property
    def overall_accuracy(self) -> float:
        """ The overall accuracy of the classifier.
        """
        return self.raw['overallAccuracy']

    @property
    def support(self) -> dict:
        """ The support of the training data used to create the classifier.
        """
        return self.raw['support']

    @property
    def confusion_matrix(self) -> dict:
        """ The confusion matrix for the classifier.
        """
        return self.raw['confusionMatrix']

    @property
    def normalized_confusion_matrix(self) -> dict:
        """ The normalized confusion matrix for the classifier.
        """
        return self.raw['normalizedConfusionMatrix']


def validate_uuid(uuid: str) -> bool:
    """ Validates that a UUID is well-formed.

    Args:
        uuid (str): The UUID to validate.
    Returns:
        bool: True if the UUID is well-formed, otherwise false.
    """
    try:
        uuid_obj = UUID(uuid)
    except ValueError:
        return False
    return str(uuid_obj) == uuid


def classify(classifier_uuid: str, document: str, base_url: str = DEFAULT_BASE_URL) -> str:
    """ Classifies an unseen document using the classifier with the specified UUID.

    Args:
        classifier_uuid (str): The UUID of the classifier.
        document (str): The document to classify.
        base_url (str): The base URL of the API to use (optional, defaults to the official API).
    Returns:
        str: The predicted class of the document.
    """

    # Check validity of UUID.
    if not validate_uuid(classifier_uuid):
        raise ValueError('The UUID provided is not valid.')

    # Prepare request.
    request_body = json.dumps({'document': str(document)}).encode('utf8')
    request = urllib.request.Request(urllib.parse.urljoin(base_url, f'/api/classifier/{classifier_uuid}'),
        data=request_body, headers={'content-type': 'application/json'})

    # Send off API request.
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(f'A classifier with UUID {classifier_uuid} could not be found.')
        if e.code == 413:
            raise ValueError('The document provided was too large.')
        if e.code == 429:
            raise ValueError(f'You are making too many calls to the Classr API. Please wait a while and try again.')

    # Otherwise decode and return class.
    response_body = response.read().decode('utf-8')
    return json.loads(response_body)['class']


def get_info(classifier_uuid: str, base_url: str = DEFAULT_BASE_URL) -> ClassifierInfo:
    """ Gets information about the classifier with the specified UUID.

    Args:
        classifier_uuid (str): The UUID of the classifier.
        base_url (str): The base URL of the API to use (optional, defaults to the official API).
    Returns:
        ClassifierInfo: Information about the classifier.
    """

    # Check validity of UUID.
    if not validate_uuid(classifier_uuid):
        raise ValueError('The UUID provided is not valid.')

    # Prepare request.
    request = urllib.request.Request(urllib.parse.urljoin(base_url, f'/api/classifier/{classifier_uuid}'),
        headers={'accept': 'application/json'})

    # Send off API request.
    try:
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            raise ValueError(f'A classifier with UUID {classifier_uuid} could not be found.')
        if e.code == 429:
            raise ValueError(f'You are making too many calls to the Classr API. Please wait a while and try again.')

    # Otherwise decode and return info dictionary.
    response_body = response.read().decode('utf-8')
    return ClassifierInfo(json.loads(response_body))


class Classr:
    """ Represents a cloud-based classifier on the Classr platform.
    """

    def __init__(self, classifier_uuid: str, base_url: str = DEFAULT_BASE_URL):
        """ Initializes a new instance of a cloud-based classifier on the Classr platform.

        Args:
            classifier_uuid (str): The UUID of the classifier.
            base_url (str): The base URL of the API to use (optional, defaults to the official API).
        """
        self.classifier_uuid = classifier_uuid
        self.base_url = base_url

    def classify(self, document: str) -> str:
        """ Classifies an unseen document using the classifier.

        Args:
            document (str): The document to classify.
        Returns:
            str: The predicted class of the document.
        """
        return classify(self.classifier_uuid, document, self.base_url)

    def get_info(self) -> ClassifierInfo:
        """ Gets information about the classifier.

        Returns:
            ClassifierInfo: Information about the classifier.
        """
        return get_info(self.classifier_uuid, self.base_url)
