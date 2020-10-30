import numpy as np
import xarray as xr

# constance
DIMS = "freq", "PWV", "T_atm"


def get_brightness(
    model: DataArray,
    f: Quantity,
    PWV: Quantity,
    T_atm: Quantity,
    Z: Quantity,
) -> DataArray:

    # main feature
    if not isinstance(model, xr.DataArray):
        raise ("model must be xarray.DataArray")

    if not set(model.dims) == set(DIMS):
        raise (f"Dimension must be {DIMS}")

    # modelのinterpolation
    Tb_interp = model.interp(freq=f, PWV=PWV, T_atm=T_atm)

    # 天頂角対応(軸の追加)
    Z = xr.DataArray(Z, dims="Z")

    return Tb_interp / np.cos(Z)