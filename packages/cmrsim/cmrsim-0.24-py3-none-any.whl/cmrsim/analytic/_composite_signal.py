""" This module contains the base implementation for all signal-process building blocks. """
__all__ = ["CompositeSignalModel"]

from typing import Union, Tuple, Optional

import tensorflow as tf
import numpy as np

from cmrsim.analytic.contrast import BaseSignalModel


class CompositeSignalModel(tf.Module):
    """ Class that sequentially calls the signal-process building blocks. This offers a general
    way to stack and exchange arbitrary building blocks without changing the simulation calling
    signature

    :param args: All signal modules that need to be concatenated.
    """

    required_quantities: Tuple[str] = ('M0',)
    _sub_module_order: Tuple[str] = ()
    _expansion_factors: Tuple[int] = ()
    _expansion_names: Tuple[str] = ()
    _apply_expansion: Tuple[bool] = ()

    def __init__(self, *args):
        """ Container module to concatenate and sequentially call subclasses of BaseSignalModules.
         Calling order is equal to order arguments.

        :param args: All signal modules that need to be concatenated.
        """
        super().__init__(name="composite_signal_model")

        with self.name_scope:
            for module in args:
                if isinstance(module, BaseSignalModel):
                    self.__dict__[module.name] = module
                    self.required_quantities += module.required_quantities
                    self._sub_module_order += (module.name,)

                    if module.expansion_factor is None or module.expansion_factor < 1:
                        raise NotImplementedError(f"The module {module.name} seems to not have set"
                                                  f" the expansion factor for the #repetition-axis."
                                                  f" If the module does not increase the number of "
                                                  f"repetitions make sure it is set to 1! Currently"
                                                  f" it is: {module.expansion_factor}")

                    self._expansion_factors += (module.expansion_factor,)
                    self._apply_expansion += (module.expand_repetitions, )
                    self._expansion_names += (module.name,)
        self.required_quantities = tuple(dict.fromkeys(self.required_quantities).keys())

    def __call__(self, signal_tensor: tf.Tensor, segment_index: Optional[Union[int, tf.Tensor]] = 0,
                 **kwargs):
        """ Consecutively calls submodules which the signal change to the passed in tensor.

        :param kwargs: dictionary of tensors containing all required quantities. Is forwarded
         to BaseSignalModule.
        """
        kwargs.update({'segment_index': segment_index})
        for sub_mod_name in self._sub_module_order:
            sub_mod = self.__dict__[sub_mod_name]
            signal_tensor = sub_mod(signal_tensor, **kwargs)
        return signal_tensor

    def update(self):
        """ Calls update function of all sub-modules and records the overall expansion factor """
        self._expansion_factors = ()
        self._expansion_names = ()
        for module_name in self._sub_module_order:
            module = self.__dict__[module_name]
            module.update()
            self._expansion_factors += (int(module.expansion_factor),)
            self._expansion_names += (module.name,)

    @property
    def expected_number_of_repetitions(self) -> tf.Tensor:
        """ Returns the total expansion factor (factor by which the #repetitions axis grows)"""
        self.update()
        appl_idx = tf.squeeze(tf.where(tf.stack(self._apply_expansion)))
        exps = tf.stack(self._expansion_factors)
        return tf.reduce_prod(tf.gather(exps, appl_idx))

    @property
    def unstacked_axis_names(self) -> Tuple[str]:
        """ returns the name of modules with expansion factors > 1 in the order that is used in
         unstack_repetitions: """
        names = tuple((str(n) for (n, f, apply) in
                       zip(self._expansion_names, self._expansion_factors, self._apply_expansion)
                       if f > 1 and apply))
        return names

    def unstack_repetitions(self, simulation_result: Union[tf.Tensor, 'np.ndarray']) -> tf.Tensor:
        """ Uses the dimension expansion information from the sub modules to unstack the simulated
        tensor of k-space, samples or images. In both cases the second axis (index=1) is assumed to
        represent the stacked repetitions.
        :param simulation_result: (-1, [noise], samples)
        :return: k-space (..., [noise], samples)
        """
        self.update()
        input_shape = tf.shape(simulation_result)
        unstacked_repetitions_shape = tuple(
                (f for (f, apply) in zip(self._expansion_factors[::-1], self._apply_expansion[::-1])
                 if (f > 1 and apply)))
        resulting_shape = tf.concat((unstacked_repetitions_shape, input_shape[1:]), 0)
        return tf.reshape(simulation_result, resulting_shape)
