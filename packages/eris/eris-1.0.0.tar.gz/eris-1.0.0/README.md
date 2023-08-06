# python-eris

This is a Python implementation of the [Encoding for Robust Immutable Storage (ERIS)](http://purl.org/eris).

# Usage

```
import eris
import asyncio

async def main():

    # create a store
    store = eris.DictStore()

    # encode content
    encoder = eris.Encoder(eris.null_convergence_secret(), store, block_size = 1024)
    await encoder.write(b'Hello world!')
    read_capability = await encoder.close()

    # decode content
    decoder = eris.Decoder(store, read_capability)
    decoded = await decoder.readall()

    print(decoded)

asyncio.run(main())
```

See also the [online documentation](https://eris.codeberg.page/python-eris/) and the [examples](./examples/).

# Development

## Running Tests

```
python -m unittest tests/*.py
```

## Building Documentation

```
make -C docs html
```

## Publishing to PyPi

```
python -m build
python3 -m twine upload --repository pypi dist/*
```

# License

[AGPL-3.0-or-later](./LICENSE/AGPL-3.0-or-later)
