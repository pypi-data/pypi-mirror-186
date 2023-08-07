# pypackages

Script specific packages similar to PEP 582 using a `__pypackages__` directory.
The `__pypackages__` directory must be in the same directory as the script being executed.

## Intent

Simplify the distribution of python scripts with dependencies.
No need to use virtual environments or explicitly install dependencies using pip.

## (Optional) Automatic requirements install

Place requirements.txt in the `__pypackages__` folder to install or upgrade on startup using pip.

This saves the need for distributing python version specific packages explicitly.

## Requirements

pip must already exist in the python environment if requirements.txt is used.

## Structure of __pypackages__

    myapp.py
    __pypackages__/
        requirements.txt  (optional)
        bin/
        lib/
            python3.11/
                site-packages/

## Structure of deployment

    myapp.py
    pypackages/
        __init__.py
    __pypackages__/
        requirements.txt

## Example (requirements.txt)

    sanic==22.12.0

## Example (myapp.py)

    #!/usr/bin/python
    import pypackages
    from sanic import Sanic
    from sanic.response import text

    app = Sanic('myapp')


    @app.route('/')
    async def hello(request):
        return text('Hello, world')


    if __name__ == '__main__':
        app.run(port=9999)

## References

https://peps.python.org/pep-0582/

