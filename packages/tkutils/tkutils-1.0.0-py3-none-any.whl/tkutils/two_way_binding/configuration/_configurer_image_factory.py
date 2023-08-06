
import os
import inspect

from typing import Callable, Tuple

from ..errors import TwoWaysBindingConfigError







def __scoped_image_factory_definitions():

    # pylint: disable=import-outside-toplevel, redefined-outer-name
    from tkutils.images import images_factory, IntOrNone, PhotoImage

    # Non locals:
    images_user_location: str = 'Not defined'
    build_image_from: Callable[ [str, IntOrNone, IntOrNone, IntOrNone],
                                Tuple[PhotoImage, IntOrNone, IntOrNone] ] = None

    def configure_image_factory(
        project_name:str,
        *path_to_images:str,
        any_file_in_project:str=None
    ):
        """ Configure the path to the directory holding images, to use `Binder.with_image`.
            The interface is the same as the one of `tk_image_from`:

            Parameters:
                project_name:        Name of the root directory of the project
                *path_to_images:     Path of subdirectories to the one containing the images.
                any_file_in_project: To provide only if the `project_name` directory isn't in
                                     the path of the file of the caller.

            !!! tip
                The location of the project is discovered through inspection of the call stack,
                getting the filename of the caller of the function.
        """
        nonlocal build_image_from, images_user_location

        caller = any_file_in_project or inspect.stack()[1].filename

        images_user_location = os.path.join(project_name, *path_to_images)
        build_image_from     = images_factory(
            project_name,
            *path_to_images,
            any_file_in_project=caller
        )


    def reset_image_factory():
        """ Reset the factory image "data" (testing purpose only: not provided to the user) """
        nonlocal images_user_location, build_image_from
        images_user_location = 'Not defined'
        build_image_from     = None


    def get_image_factory():
        """ Callback used in Binder.with_image, to extract the user defined image factory """

        if build_image_from is None:
            raise TwoWaysBindingConfigError(
                "No images factory configuration. You need to run configure_image_factory(*path) "
                "before you use it."
            )
        return build_image_from


    def get_image_factory_config_location():
        """ Extract the current user directory defined for the images factory """
        return images_user_location


    return (
        get_image_factory,
        get_image_factory_config_location,
        configure_image_factory,
        reset_image_factory
    )

(
    get_image_factory,
    get_image_factory_config_location,
    configure_image_factory,
    reset_image_factory,

)= __scoped_image_factory_definitions()
