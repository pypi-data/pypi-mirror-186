
import inspect
import os
import tkinter as T
from typing import Any, Tuple, Type, TypeVar, Union
from PIL import Image
from PIL.ImageTk import PhotoImage



ExtendWidget = TypeVar('ExtendWidget', bound=T.Widget)
IntOrNone    = TypeVar('IntOrNone', None, int)







def images_factory(
    project_name:str,
    *path_to_images:str,
    any_file_in_project:str=None,
    image_only:bool=True
):
    """ Build an image factory, digging through the project hierarchy to access the image files
        directly inside their location when using the returned factory function.

        Given the full path of `any_file_in_project` and the `project_name` of the root directory
        holding the project as well as the relative path segments to the location of the images,
        this function:

        - Extracts the full path of the project root
        - Builds the path to the directory holding the pictures
        - Will use that as location to extract and build ImageTk.PhotoImage instances
          with the [`build_image_from`][src.fake_for_docs.build_image_from] subfunction.

        Parameters:
            project_name:      Top parent directory holding the project.
            *path_to_images:   Relative path from the root directory to the one holding the images.
            any_file_in_project: Absolute path of any file in the current project. If the argument
                               isn't given, extract automatically the filename location of the
                               caller through inspection.
            image_only:        Define what the output of the factory function will be. If True, only
                               the image is returned, otherwise, it is a `Tuple[image,width,height]`

        Raises:
            FileNotFoundError:  If the `project_name` location cannot be found or if the targeted
                                images location does not exist.

        Returns:
            A [`build_image_from`][src.fake_for_docs.build_image_from] factory function.
    """

    if any_file_in_project is None:
        any_file_in_project = inspect.stack()[1].filename

    # Cut the leaves as long as the root project directory isn't reached:
    while len(any_file_in_project) > 1:
        root,name = os.path.split(any_file_in_project)
        if name == project_name:
            break
        any_file_in_project = root
    project_root = any_file_in_project

    if len(project_root)<2:                 # forbid hdd root as well (not possible from a project)
        raise FileNotFoundError(
            f"Couldn't find the project name { project_name !r} in the given path:\n"
            f"{ any_file_in_project !r}"
        )

    images_directory = os.path.join(project_root, *path_to_images)

    if not os.path.isdir(images_directory):
        raise FileNotFoundError(f"{ images_directory !r} isn't a valid directory location")


    def build_image_from(
        file:str, width:int=None, height:int=None, *, size:int=16
    ) -> Union[ PhotoImage, Tuple[PhotoImage,int,int] ] :
        """ Factory function returned by [`images_factory`][src.tkutils.images.images_factory].

            Build an image/icon usable for tkinter components from the given file, with the given
            dimensions. The dimensions for the image must be given either using exclusively the
            `size` argument, or using both `width` and `height`.

            Parameters:
                file:   Filename of the picture to use, in the directory defined with the
                        image factory
                width:  Define the width to use for the image
                height: Define the height to use for the image
                size:   Define the width and height one shot (square)

            Raises:
                ValueError: For invalid dimensions arguments, or FileNotFoundError if the
                            filename or the path is invalide.

            Returns:
                The image itself, or a tuple `(image, width, height)`, depending on the `image_only` argument of [`images_factory`][src.tkutils.images.images_factory].
        """
        filepath = os.path.join(images_directory, file)
        data     = _tk_image_from(filepath, width, height, size)
        return data[0] if image_only else data

    return build_image_from





















def widgets_with_images_factory(
    project_name:str,
    *path_to_images:str,
    any_file_in_project:str=None
):
    """ Build a widget factory, whose the widget will all have an image automatically assigned
        to them. This factory relies on the [`images_factory`][src.tkutils.images.images_factory]
        one for the path/image related operations.

        Given the full path of `any_file_in_project` and the `project_name` of the root directory
        holding the project as well as the relative path segments to the location of the images,
        this function:

        - Extracts the full path of the project root
        - Builds the path to the directory holding the pictures
        - Will use that as location to extract and build ImageTk.PhotoImage instances with the
          [`widget_with_image`][src.fake_for_docs.widget_with_image] subfunction, to build widgets.

        Parameters:
            project_name:      Top parent directory holding the project.
            *path_to_images:   Relative path from the root directory to the one holding the images.
            any_file_in_project: Absolute path of any file in the current project. If the argument
                               isn't given, extract automatically the filename location of the caller
                               through inspection.

        Raises:
            FileNotFoundError:  If the `project_name` location cannot be found or if the targeted
                                images location does not exist.

        Returns:
            A [`widget_with_image`][src.fake_for_docs.widget_with_image] factory function to build widgets with an image on them.
    """

    # Inspection must be done here, otherwise the file of the caller becomes THIS FILE in the
    # following `images_factory` call...
    if any_file_in_project is None:
        any_file_in_project = inspect.stack()[1].filename

    image_from = images_factory(
        project_name, *path_to_images, any_file_in_project=any_file_in_project, image_only=False
    )


    def widget_with_image(
        widget_class:  Type[ExtendWidget],
        image_file:    str,
        parent:        T.Widget,
        *,
        width:         int=None,
        height:        int=None,
        size:          int=16,
        resize_widget: bool=True,
        **kwargs:      Any,
    ) -> ExtendWidget:
        """ Factory function returned by
            [`widgets_with_images_factory`][src.tkutils.images.widgets_with_images_factory].

            Build a widget of the given type with the `file` image on it. The image is resized to
            teh given dimensions (if any).

            !!! warning
                This factory function cannot be used before a top level `tkinter` widget has been
                instantiated (this is a `PIL.ImageTk` requirement at runtime).

            Parameters:
                parent:     Parent widget
                image_file: A valid file name, in the directory pointed in the factory function.
                width:      Resize the image width
                height:     Resize the image height
                size:       Default size for the images (used for buttons in menu bars, for instance)
                **kwargs:   Any additional arguments needed to build the widget.

            Raises:
                ValueError:         For invalid dimensions arguments
                FileNotFoundError:  If the filename or the path is invalide.

            Returns:
                The instantiated widget with the image.
        """
        data: Tuple[PhotoImage,int,int] = image_from(
            image_file, width=width, height=height, size=size
        )
        image, width, height = data                     # pylint: disable=unpacking-non-sequence


        # NOTE: as for now, the option to give a size to the widget that isn't the one of the image
        # is just NOT working. The widget always automatically get's the size of the image (+ some
        # extra pixels).
        if resize_widget:
            kwargs.update({'width':width, 'height':height})
            # Note: the widget will actually be a bit bigger than the image
            #       (+6 pixels for buttons, for example)

        widget = widget_class(parent, image=image, **kwargs)
        widget.__image_ref_to_avoid_GC = image          # pylint: disable=protected-access
        return widget

    return widget_with_image













def _check_size_args(width:IntOrNone, height:IntOrNone, size:IntOrNone):
    """ Check that the call configuration of the arguments is consistent and return the
        appropriate height and width values. Correct use of arguments are:
            * size (takes precedence over any given value for width and height)
            * height + width, no size
            * none used
    """
    if size is not None:
        width = height = size

    given_dims = sum(v is not None for v in (width,height))
    if given_dims==1:
        raise ValueError("Cannot resize the image with one dimension only, use @size argument")

    return width,height




def _tk_image_from(
    filepath:str, width:int=None, height:int=None, size:int=None
) -> Tuple[ PhotoImage, int, int ] :
    """ Build an image/icon usable for tkinter components from the given pathname, with
        the given dimensions.

        @filepath:  A valid full path to the image source.
        @size:      Resize the image (square)
        @width:     Resize the image width
        @height:    Resize the image height
        @return:    A tuple (PhotoImage, width, height), where the dimensions are the actual
                    one used for the image, or None if it's not resized
    """
    width,height = _check_size_args(width, height, size)
    image          = Image.open(filepath)

    if width is not None:
        image = image.resize((width,height), Image.LANCZOS)

    return (PhotoImage(image), width, height)
