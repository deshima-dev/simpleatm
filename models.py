def _load_models() -> None:

    # standard library
    from pathlib import Path

    # dependent packages
    import xarray as xr

    data_path = Path(__file__).parent / "data"
    for path in data_path.glob("*.nc"):
        name = path.stem
        try:
            globals()[name] = xr.open_dataarray(path)
        except Exception as e:
            print(e)


# execute load process
_load_models()
