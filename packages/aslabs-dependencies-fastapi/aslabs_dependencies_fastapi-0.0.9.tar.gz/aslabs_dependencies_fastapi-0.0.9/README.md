## ASLabs Dependencies: FastAPI

FastAPI Adapter for the ASLabs Dependencies package.

# How to use it:

In your `main.py`, add the `Dependencies` additional handler:

```py
from fastapi import FastAPI

from aslabs.dependencies.fastapi import Dependencies


app = FastAPI()
deps = Dependencies(app)    # Add line
```

In your various routers, replace `APIRouter` with `DependencyRouter` and use it to register your dependencies:

```py
from aslabs.dependencies.fastapi import DependencyRouter, D


router = DependencyRouter()
router.register_dependencies(lambda deps: deps.add_direct(MyDependencyClass))      # Register your dependencies here
```

Once registered, use the `D` parameter function to request dependencies. Notably, you must specify the type as the parameter for `D` (cannot be infered).

```py
@router.get("/")
def index(dep: MyDependencyClass = D(MyDependencyClass)):
    return {"Hello": dep.get_world()}
```

Once setup, back in your `main.py`, register the router on `deps`, not on `app`. The same parameters can be used as `app.include_router`

```py
deps.include_router(router)
```

You are now done.

## Adding global dependencies

You can add dependencies directly to the `deps` object, by calling `register_with`:

```py
deps.register_with(lambda deps: deps.add_direct(GlobalDependency))
```