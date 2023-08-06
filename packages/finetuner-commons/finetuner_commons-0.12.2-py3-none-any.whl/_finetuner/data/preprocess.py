import abc
from typing import TYPE_CHECKING

import numpy as np
from docarray import Document

if TYPE_CHECKING:
    from docarray.typing import DocumentContentType


_CHANNEL_LAST = [-1, 2]


class BasePreprocess(abc.ABC):
    @abc.abstractmethod
    def __call__(self, doc: Document) -> 'DocumentContentType':
        ...


class DefaultPreprocess(BasePreprocess):
    """
    Default built-in preprocess class to unpack the content from a ``Document`` object.
    """

    def __call__(self, doc: Document) -> 'DocumentContentType':
        """
        Returns the content of a ``Document`` object.

        :param doc: A docarray ``Document`` object.
        :return: Content of the input document.
        """
        return doc.content


class TextPreprocess(DefaultPreprocess):
    """
    Default built-in preprocess class to unpack the text from a ``Document`` object.
    """

    pass


class VisionPreprocess(BasePreprocess):
    """
    Built-in preprocess class for ``Document`` objects holding image data. It
    transforms an image given by a BLOB, URI, or a tensor into a tensor which can be
    passed into an image embedding model.

    Thereby, the function can also resize and normalize images and move their channel
    axis. To omit those transformations set the `normalization`, `resize`, or
    `move_channel_axis` parameter to False.

    Please note, in any case, normalization can not be applied if the image is passed
    in the form of a float32 tensor is passed.
    If the image is passed as an (u)int8 tensor, BLOB, or a URI, normalization can be
    applied.

    :param height: The target height of the image.
    :param width: The target width of the image.
    :param channel_axis: The default channel axis of the image. If move_channel_axis
        is set, it will be set to 0 (C * H * W) afterwards.
    :param augmentation: If `True`, apply random augmentation for the image content.
    :param normalization: If set `False` no normalization is performed.
    :param move_channel_axis: If set `False` channel axis is not moved to the PyTorch
        default channel axis (0)


    """

    def __init__(
        self,
        height: int = 224,
        width: int = 224,
        channel_axis: int = -1,
        augmentation: bool = False,
        normalization: bool = True,
        move_channel_axis: bool = True,
        resize: bool = True,
    ):
        self._height = height
        self._width = width
        self._channel_axis = channel_axis
        self._augmentation = augmentation
        self._normalization = normalization
        self._move_channel_axis = move_channel_axis
        self._resize = resize

    def __call__(self, doc: Document) -> np.ndarray:
        """
        Unpacks and preprocesses the content of a ``Document`` object with image
        content.

        :param doc: A docarray ``Document`` object.
        :return: Preprocessed tensor content of the input document.
        """
        current_channel_axis = self._channel_axis
        doc = Document(doc, copy=True)
        loaded_image = False
        load_args = {'channel_axis': self._channel_axis}
        if self._resize:
            load_args.update(
                {
                    'width': self._width,
                    'height': self._height,
                }
            )
        if doc.tensor is None:
            if doc.blob:
                doc.convert_blob_to_image_tensor(**load_args)
                loaded_image = True
            elif doc.uri:
                doc.load_uri_to_image_tensor(**load_args)
                loaded_image = True
            else:
                raise AttributeError(
                    f'Document `tensor` is None, loading it from url: {doc.uri} failed.'
                )
        if self._resize and not loaded_image:
            doc.set_image_tensor_shape(
                shape=(self._height, self._width), channel_axis=self._channel_axis
            )
        # Normalize image as np.float32.
        if doc.tensor.dtype in [np.int8, np.uint8]:
            doc.tensor = doc.tensor.astype(np.uint8)
            if self._normalization:
                doc.set_image_tensor_normalization(channel_axis=self._channel_axis)
        elif doc.tensor.dtype == np.float64:
            doc.tensor = np.float32(doc.tensor)
        if self._augmentation:
            import albumentations as A

            if self._channel_axis not in _CHANNEL_LAST:
                # if image is not channel_last, move C to last axis.
                # This is required for albumentations.
                doc.set_image_tensor_channel_axis(self._channel_axis, _CHANNEL_LAST[0])
                current_channel_axis = _CHANNEL_LAST[0]

            transform = A.Compose(
                [
                    A.HorizontalFlip(p=0.5),
                    A.ColorJitter(p=1),
                    A.RandomResizedCrop(width=self._width, height=self._height, p=1),
                    A.GaussianBlur(p=1),
                    A.GridDropout(
                        ratio=0.2, p=0.5
                    ),  # random erase 0.2 percent of image with 0.5 probability
                ]
            )
            doc.tensor = transform(image=doc.tensor)['image']

        if self._move_channel_axis:
            # Set image channel axis to pytorch default channel 0.
            doc.set_image_tensor_channel_axis(current_channel_axis, 0)

        return doc.tensor


class PointCloudPreprocess:
    """
    Built-in preprocess class for ``Document`` objects holding 3D meshes which should
    be processed in the form of point clouds by a deep learning model. It
    transforms a 3D mesh given by a point clould tensor or URI into a tensor which
    can be passed into a point cloud model.

    Thereby, the function samples a certain amount of points, normalizes them and can
    also apply simple augmentation on them.

    :param num_points: The number of points to be sampled.
    :param augmentation: Set this to True to enable augmentation.
    """

    def __init__(self, num_points: int = 1024, augmentation: bool = True):
        self._num_points = num_points
        self._augmentation = augmentation

    def __call__(self, doc: Document) -> 'DocumentContentType':
        """
        Unpack and preprocess the content of a document with 3D meshes to obtain a point
        cloud input.

        :param doc: A docarray ``Document`` object containing a 3D mesh input.
        :return: Preprocessed point cloud tensor
        """

        doc = Document(doc, copy=True)

        if doc.tensor is None:
            if doc.uri:
                doc.load_uri_to_point_cloud_tensor(max(2048, self._num_points))

        points = np.float32(doc.tensor)
        points = self._random_sample(points, self._num_points)

        points = points - np.expand_dims(np.mean(points, axis=0), 0)  # center
        dist = np.max(np.sqrt(np.sum(points**2, axis=1)), 0)
        points = points / dist  # scale

        if self._augmentation:
            points = self._apply_augmentation(points)
        return points

    @staticmethod
    def _random_sample(points: np.ndarray, sample_size: int):
        permutation = np.arange(len(points))
        np.random.shuffle(permutation)
        sample = points[permutation[:sample_size]]
        return sample

    @staticmethod
    def _apply_augmentation(points: np.ndarray) -> np.ndarray:
        theta = np.random.uniform(0, np.pi * 2)
        rotation_matrix = np.array(
            [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
        )
        points[:, [0, 2]] = points[:, [0, 2]].dot(rotation_matrix)  # random rotation
        points += np.random.normal(0, 0.02, size=points.shape)  # random jitter
        return points
