from dataclasses import dataclass, replace, field

import ezmsg.core as ez
import scipy.signal
import numpy as np
import asyncio
import logging

from .messages import TSMessage as TimeSeriesMessage

from typing import AsyncGenerator, Optional, Tuple

logger = logging.getLogger('ezmsg')


@dataclass
class FilterCoefficients:
    b: np.ndarray = field(default_factory = lambda: np.array([1.0, 0.0]))
    a: np.ndarray = field(default_factory = lambda: np.array([1.0, 0.0]))



class FilterSettings(ez.Settings):
    # If you'd like to statically design a filter, define it in settings
    filt: Optional[FilterCoefficients] = None
    fs: Optional[float] = None


class FilterState(ez.State):
    zi: Optional[np.ndarray] = None
    filt_designed: bool = False
    filt: Optional[FilterCoefficients] = None
    filt_set: asyncio.Event = asyncio.Event()
    samp_shape: Optional[Tuple[int, ...]] = None
    fs: Optional[float] = None  # Hz


class Filter(ez.Unit):
    SETTINGS: FilterSettings
    STATE: FilterState

    INPUT_FILTER = ez.InputStream(FilterCoefficients)
    INPUT_SIGNAL = ez.InputStream(TimeSeriesMessage)
    OUTPUT_SIGNAL = ez.OutputStream(TimeSeriesMessage)

    def design_filter(self) -> Optional[Tuple[np.ndarray, np.ndarray]]:
        raise NotImplementedError("Must implement 'design_filter' in Unit subclass!")

    # Set up filter with static initialization if specified
    def initialize(self) -> None:
        if self.SETTINGS.filt is not None:
            self.STATE.filt = self.SETTINGS.filt
            self.STATE.filt_set.set()
        else:
            self.STATE.filt_set.clear()

        if self.SETTINGS.fs is not None:
            try:
                self.update_filter()
            except NotImplementedError:
                logger.debug("Using filter coefficients.")

    @ez.subscriber(INPUT_FILTER)
    async def redesign(self, message: FilterCoefficients):
        self.STATE.filt = message

    def update_filter(self):
        try:
            coefs = self.design_filter()
            self.STATE.filt = FilterCoefficients() if coefs is None else FilterCoefficients( *coefs )
            self.STATE.filt_set.set()
            self.STATE.filt_designed = True
        except NotImplementedError as e:
            raise e
        except Exception as e:
            logger.warning(f"Error when designing filter: {e}")

    @ez.subscriber(INPUT_SIGNAL)
    @ez.publisher(OUTPUT_SIGNAL)
    async def apply_filter(self, message: TimeSeriesMessage) -> AsyncGenerator:
        if self.STATE.fs != message.fs and self.STATE.filt_designed is True:
            self.STATE.fs = message.fs
            self.update_filter()

        # Ensure filter is defined
        if self.STATE.filt is None:
            self.STATE.filt_set.clear()
            logger.info("Awaiting filter coefficients...")
            await self.STATE.filt_set.wait()
            logger.info("Filter coefficients received.")

        arr_in: np.ndarray

        # If the array is one dimensional, add a temporary second dimension so that the math works out
        one_dimensional = False
        if message.data.ndim == 1:
            arr_in = np.expand_dims(message.data, axis=1)
            one_dimensional = True
        else:
            arr_in = message.data

        # We will perform filter with time dimension as last axis
        arr_in = np.moveaxis(arr_in, message.time_dim, -1)
        samp_shape = arr_in[..., 0].shape

        # Re-calculate/reset zi if necessary
        if self.STATE.zi is None or samp_shape != self.STATE.samp_shape:
            zi: np.ndarray = scipy.signal.lfilter_zi(
                self.STATE.filt.b, self.STATE.filt.a
            )
            self.STATE.samp_shape = samp_shape
            self.STATE.zi = np.array([zi] * np.prod(self.STATE.samp_shape))
            self.STATE.zi = self.STATE.zi.reshape(
                tuple(list(self.STATE.samp_shape) + [zi.shape[0]])
            )

        arr_out, self.STATE.zi = scipy.signal.lfilter(
            self.STATE.filt.b, self.STATE.filt.a, arr_in, zi=self.STATE.zi
        )

        arr_out = np.moveaxis(arr_out, -1, message.time_dim)

        # Remove temporary first dimension if necessary
        if one_dimensional:
            arr_out = np.squeeze(arr_out, axis=1)

        yield (self.OUTPUT_SIGNAL, replace(message, data=arr_out))
